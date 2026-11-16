import csv
import json
import os
import time
from datetime import datetime


class Assistente:
    """Controla o fluxo de atendimento ao cidadao, seguranca, historico e indicadores."""

    def __init__(self, nome, base, caminho_historico="data/historico.json", caminho_csv="data/atendimentos.csv"):
        self.nome = nome
        self.base = base
        self.caminho_historico = caminho_historico
        self.caminho_csv = caminho_csv
        self.historico = self._carregar_historico()
        self.notas_facilidade = []

    def _carregar_historico(self):
        """Carrega o historico existente se disponivel."""
        if os.path.exists(self.caminho_historico):
            try:
                with open(self.caminho_historico, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    if isinstance(dados, list):
                        return dados
            except Exception:
                return []
        return []

    def _salvar_historico(self):
        """Persiste a lista de atendimentos em data/historico.json."""
        os.makedirs(os.path.dirname(self.caminho_historico), exist_ok=True)
        with open(self.caminho_historico, "w", encoding="utf-8") as f:
            json.dump(self.historico, f, ensure_ascii=False, indent=4)

    def contem_dado_pessoal(self, texto):
        """Verifica se o texto contem '@' (e-mail) ou 8 ou mais digitos (CPF/telefone)."""
        if "@" in texto:
            return True
        qtd_digitos = sum(1 for c in texto if c.isdigit())
        if qtd_digitos >= 8:
            return True
        return False

    def _perguntar_se_ajudou(self):
        """Solicita feedback binario (s/n) validando entradas invalidas."""
        while True:
            resp = input("\nEssa orientacao respondeu sua duvida? (s/n): ").strip().lower()
            if resp in ("s", "sim"):
                return True
            elif resp in ("n", "nao", "não"):
                return False
            else:
                print("Entrada invalida. Digite 's' para sim ou 'n' para nao.")

    def registrar(self, origem, pergunta, orientacao_id, encontrou, ajudou, tentativas, tempo_seg):
        """Registra um atendimento no historico em memoria e no arquivo JSON."""
        registro = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "origem": origem,
            "pergunta": pergunta,
            "id_orientacao": orientacao_id,
            "encontrou": encontrou,
            "ajudou": ajudou,
            "tentativas": tentativas,
            "tempo_segundos": tempo_seg
        }
        self.historico.append(registro)
        self._salvar_historico()

    def perguntar(self):
        """Fluxo de pergunta em texto livre com pontuacao, bloqueio de PII e cronometragem."""
        inicio = time.time()
        tentativas = 0

        while True:
            duvida = input("\nDigite sua duvida (0 para voltar): ").strip()

            if duvida == "0":
                return

            if not duvida:
                print("Entrada vazia. Por favor, escreva sua duvida ou digite 0 para voltar.")
                continue

            if self.contem_dado_pessoal(duvida):
                print("Atencao: nao digite CPF, RG, telefone ou e-mail por seguranca. Reescreva sua duvida sem dados pessoais.")
                continue

            tentativas += 1
            resultados = self.base.buscar(duvida)

            if not resultados or resultados[0][0] < 3:
                print("\nNao encontrei uma orientacao exata com confianca suficiente para essa duvida.")
                print("Sugestao: tente usar palavras-chave como 'rg', 'cpf', 'chuveiro', 'energia solar' ou navegue pelas categorias:")
                for cat in self.base.categorias():
                    print(f"  * {cat}")

                tempo_seg = round(time.time() - inicio, 1)
                self.registrar("pergunta", duvida, None, False, False, tentativas, tempo_seg)

                continuar = input("\nDeseja tentar reformular a pergunta? (s/n): ").strip().lower()
                if continuar not in ("s", "sim"):
                    return
                continue

            melhor_pts, melhor_orientacao = resultados[0]
            confianca = "ALTA" if melhor_pts >= 6 else "MEDIA"

            melhor_orientacao.exibir(pontos=melhor_pts, confianca=confianca)

            # Exibe ate duas alternativas caso existam com pontuacao >= 3
            alternativas = [r for r in resultados[1:3] if r[0] >= 3]
            if alternativas:
                print("Outras orientacoes relacionadas:")
                for pts_alt, ori_alt in alternativas:
                    print(f"  - [{ori_alt.id}] {ori_alt.titulo} ({pts_alt} pts)")

            ajudou = self._perguntar_se_ajudou()
            tempo_seg = round(time.time() - inicio, 1)
            self.registrar("pergunta", duvida, melhor_orientacao.id, True, ajudou, tentativas, tempo_seg)
            return

    def navegar(self):
        """Fluxo de navegacao estruturada por categorias numeradas."""
        inicio = time.time()
        categorias = self.base.categorias()

        if not categorias:
            print("Nenhuma categoria disponivel na base.")
            return

        while True:
            print("\n--- Categorias Disponiveis ---")
            for i, cat in enumerate(categorias, start=1):
                print(f"{i}. {cat}")
            print("0. Voltar ao menu principal")

            escolha_cat = input("Escolha uma categoria: ").strip()
            if escolha_cat == "0":
                return

            if not escolha_cat.isdigit() or not (1 <= int(escolha_cat) <= len(categorias)):
                print("Opcao invalida. Digite um numero da lista.")
                continue

            cat_selecionada = categorias[int(escolha_cat) - 1]
            orientacoes_cat = self.base.por_categoria(cat_selecionada)

            while True:
                print(f"\n--- Orientacoes em '{cat_selecionada}' ---")
                for idx, ori in enumerate(orientacoes_cat, start=1):
                    print(f"{idx}. {ori.titulo}")
                print("0. Voltar para categorias")

                escolha_ori = input("Escolha uma orientacao: ").strip()
                if escolha_ori == "0":
                    break

                if not escolha_ori.isdigit() or not (1 <= int(escolha_ori) <= len(orientacoes_cat)):
                    print("Opcao invalida. Digite um numero da lista.")
                    continue

                ori_escolhida = orientacoes_cat[int(escolha_ori) - 1]
                ori_escolhida.exibir()

                ajudou = self._perguntar_se_ajudou()
                tempo_seg = round(time.time() - inicio, 1)
                self.registrar("categoria", f"Navegacao: {cat_selecionada}", ori_escolhida.id, True, ajudou, 1, tempo_seg)
                return

    def avaliar_facilidade(self):
        """Pede nota de facilidade de uso (1 a 5) ao encerrar a sessao."""
        if not self.historico:
            return
        while True:
            nota = input("\nAntes de sair, de uma nota de 1 a 5 para a facilidade de uso do assistente (0 para pular): ").strip()
            if nota == "0":
                return
            if nota.isdigit() and 1 <= int(nota) <= 5:
                self.notas_facilidade.append(int(nota))
                print("Obrigado pela sua avaliacao!")
                return
            print("Entrada invalida. Digite um numero inteiro entre 1 e 5.")

    def indicadores(self):
        """Calcula e exibe os indicadores de desempenho do assistente."""
        total = len(self.historico)
        print("\n" + "=" * 65)
        print(f"INDICADORES DE ATENDIMENTO - {self.nome}")
        print("=" * 65)

        if total == 0:
            print("Nenhum atendimento registrado ate o momento.")
            print("=" * 65)
            return

        encontrados = [h for h in self.historico if h["encontrou"]]
        ajudaram = [h for h in self.historico if h["ajudou"]]
        nao_encontrados = [h["pergunta"] for h in self.historico if not h["encontrou"]]

        pct_encontrada = (len(encontrados) / total) * 100
        pct_ajudou = (len(ajudaram) / total) * 100

        if encontrados:
            tempo_medio = sum(h["tempo_segundos"] for h in encontrados) / len(encontrados)
        else:
            tempo_medio = 0.0

        media_tentativas = sum(h["tentativas"] for h in self.historico) / total

        if self.notas_facilidade:
            media_facilidade = f"{sum(self.notas_facilidade) / len(self.notas_facilidade):.1f} / 5.0"
        else:
            media_facilidade = "Ainda nao avaliada nesta sessao"

        print(f"Total de atendimentos registrados: {total}")
        print(f"Resposta encontrada (%):           {pct_encontrada:.1f}%")
        print(f"Taxa de acerto - ajudou (%):       {pct_ajudou:.1f}%")
        print(f"Tempo medio para encontrar:        {tempo_medio:.1f} segundos")
        print(f"Tentativas medias por atendimento: {media_tentativas:.1f}")
        print(f"Facilidade de uso (1 a 5):         {media_facilidade}")
        print("\nDuvidas sem solucao:")
        if nao_encontrados:
            for d in nao_encontrados:
                print(f"  - {d}")
        else:
            print("  Nenhuma duvida sem solucao registrada.")
        print("=" * 65)

    def exportar_csv(self):
        """Exporta o historico de atendimentos para data/atendimentos.csv usando csv.DictWriter."""
        if not self.historico:
            print("\nNao ha atendimentos no historico para exportar.")
            return

        os.makedirs(os.path.dirname(self.caminho_csv), exist_ok=True)
        campos = [
            "data", "origem", "pergunta", "id_orientacao",
            "encontrou", "ajudou", "tentativas", "tempo_segundos"
        ]

        try:
            with open(self.caminho_csv, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.DictWriter(f, fieldnames=campos, delimiter=";")
                writer.writeheader()
                writer.writerows(self.historico)
            print(f"\nHistorico exportado com sucesso para '{self.caminho_csv}' ({len(self.historico)} registros).")
        except Exception as e:
            print(f"\n[ERRO] Falha ao exportar CSV: {e}")

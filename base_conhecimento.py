import json
import os
from orientacao import Orientacao

ACENTOS = {
    "á": "a", "à": "a", "ã": "a", "â": "a",
    "é": "e", "ê": "e",
    "í": "i",
    "ó": "o", "õ": "o", "ô": "o",
    "ú": "u", "ü": "u",
    "ç": "c"
}


def normalizar(texto):
    """Remove acentos, pontuacao e converte texto para minusculas."""
    texto = str(texto).lower().strip()
    for letra, troca in ACENTOS.items():
        texto = texto.replace(letra, troca)
    for sinal in "?!.,;:()[]{}'\"-_/":
        texto = texto.replace(sinal, " ")
    return " ".join(texto.split())


class BaseConhecimento:
    """Gerencia o carregamento, filtragem e busca pontuada das orientacoes."""

    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []

    def carregar(self):
        """Le o arquivo JSON e instancia objetos Orientacao com tratamento de erros."""
        if not os.path.exists(self.caminho):
            print(f"[ERRO] Arquivo '{self.caminho}' nao encontrado.")
            return False

        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            if not isinstance(dados, list):
                print("[ERRO] Formato invalido no JSON: esperada uma lista de orientacoes.")
                return False

            self.orientacoes = []
            for item in dados:
                orientacao = Orientacao(
                    id=item["id"],
                    categoria=item["categoria"],
                    titulo=item["titulo"],
                    palavras_chave=item["palavras_chave"],
                    resposta=item["resposta"],
                    documentos=item["documentos"],
                    onde=item["onde"],
                    fonte=item["fonte"],
                    verificado_em=item["verificado_em"]
                )
                self.orientacoes.append(orientacao)
            return True

        except json.JSONDecodeError:
            print(f"[ERRO] O arquivo '{self.caminho}' esta corrompido (JSON invalido).")
            return False
        except KeyError as e:
            print(f"[ERRO] Campo obrigatorio ausente no JSON: {e}")
            return False
        except Exception as e:
            print(f"[ERRO] Falha inesperada ao carregar base: {e}")
            return False

    def categorias(self):
        """Retorna uma lista ordenada de categorias unicas."""
        cats = []
        for o in self.orientacoes:
            if o.categoria not in cats:
                cats.append(o.categoria)
        return cats

    def por_categoria(self, categoria):
        """Retorna todas as orientacoes pertencentes a uma categoria."""
        return [o for o in self.orientacoes if o.categoria == categoria]

    def pontuar(self, pergunta_norm, orientacao):
        """Calcula a pontuacao de uma orientacao com base na pergunta normalizada."""
        pontos = 0
        # +3 pontos para cada palavra-chave presente na pergunta
        for kw in orientacao.palavras_chave:
            kw_norm = normalizar(kw)
            if kw_norm and kw_norm in pergunta_norm:
                pontos += 3

        # +1 ponto para palavras da pergunta (4+ letras) presentes no titulo
        titulo_norm = normalizar(orientacao.titulo)
        palavras_titulo = set(titulo_norm.split())
        for palavra in pergunta_norm.split():
            if len(palavra) >= 4 and palavra in palavras_titulo:
                pontos += 1

        return pontos

    def buscar(self, pergunta):
        """Retorna lista de tuplas (pontos, orientacao) ordenada da maior para menor pontuacao."""
        pergunta_norm = normalizar(pergunta)
        resultados = []
        for orientacao in self.orientacoes:
            pts = self.pontuar(pergunta_norm, orientacao)
            if pts > 0:
                resultados.append((pts, orientacao))

        resultados.sort(key=lambda x: x[0], reverse=True)
        return resultados

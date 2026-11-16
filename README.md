# Citizen Assist AI — Assistente Digital de Orientação ao Cidadão e Eficiência Energética

Projeto desenvolvido para a **Global Solution 2026.2 (FIAP — 1CC)** integrando as disciplinas de **Pensamento Computacional e Automação com Python (PCP)** e **Soluções em Energias Renováveis e Sustentáveis (SERS)**.

## Integrantes da Equipe
- **Lucas Bellezzo Figueiredo** — RM569734
- **Matheus Sabino da Silva Guedes** — RM572907

---

## 1. Público-Alvo, Problema e ODS Relacionados
- **Público-alvo:** Famílias de baixa renda e cidadãos em situação de vulnerabilidade socioeconômica.
- **Problema:** Dificuldade de acesso a informações claras, confiáveis e livres de linguagem burocrática sobre emissão de documentos essenciais (necessários para programas sociais e emprego) e estratégias práticas para reduzir o gasto elevado com energia elétrica residencial.
- **Objetivos de Desenvolvimento Sustentável (ODS - ONU):**
  - **ODS 7 (Energia Limpa e Acessível):** Promoção da eficiência energética doméstica e disseminação de tecnologias renováveis de baixo custo (Aquecedor Solar ASBC).
  - **ODS 10 (Redução das Desigualdades):** Democratização do acesso à informação sobre direitos civis, isenção de taxas e Tarifa Social de Energia Elétrica.
  - **ODS 16 (Paz, Justiça e Instituições Eficazes):** Transparência na orientação sobre serviços públicos e documentos civis.

---

## 2. Estrutura do Repositório
```text
citizen-assist-ai/
├── README.md                          # Documentação geral e relatórios das disciplinas
├── main.py                            # Ponto de entrada e menu interativo no terminal
├── orientacao.py                      # Classe Orientacao (representação e exibição)
├── base_conhecimento.py               # Classe BaseConhecimento (carregamento, normalização e busca)
├── assistente.py                      # Classe Assistente (atendimento, segurança, histórico e CSV)
├── data/
│   ├── base_conhecimento.json         # Base verificada (12 orientações em 3 categorias)
│   ├── historico.json                 # Registro automático dos atendimentos
│   └── atendimentos.csv               # Exportação estruturada via csv.DictWriter
└── docs_sers/
    └── analise_energetica_sers.md     # Estudo completo, fórmulas e tabela comparativa de SERS
```

---

## 3. Como Executar o Projeto
1. Certifique-se de ter o **Python 3.10+** instalado (não são necessárias bibliotecas externas; utiliza apenas a biblioteca padrão: `json`, `csv`, `time`, `os`, `datetime`).
2. Clone o repositório e acesse a pasta raiz:
   ```bash
   git clone https://github.com/seu-usuario/citizen-assist-ai.git
   cd citizen-assist-ai
   ```
3. Execute o programa principal:
   ```bash
   python main.py
   ```

---

## 4. Arquitetura e Regra de Pontuação (PCP)
O sistema foi estruturado utilizando **Programação Orientada a Objetos (POO) por composição**, onde `Assistente` possui uma instância de `BaseConhecimento`, que por sua vez gerencia uma lista de objetos `Orientacao`.

### Normalização e Busca por Regras
Antes da comparação, perguntas, palavras-chave e títulos passam pela função `normalizar()` (conversão para minúsculas, remoção de acentos e eliminação de pontuação).
- **Palavra-chave exata presente na pergunta:** `+3 pontos`
- **Palavra da pergunta (4 letras ou mais) presente no título:** `+1 ponto`

### Níveis de Confiança
- **6 pontos ou mais:** Confiança **ALTA**
- **3 a 5 pontos:** Confiança **MÉDIA**
- **Menos de 3 pontos:** Resposta **Não encontrada** (o sistema sugere termos e lista as categorias disponíveis).

### Segurança e Privacidade
- Nenhuma pergunta é enviada para APIs externas.
- Entradas contendo `@` ou `8 ou mais dígitos` (como CPF, RG ou telefone) são bloqueadas imediatamente antes de qualquer processamento ou gravação em log.

---

## 5. Contribuição de Soluções em Energias Renováveis e Sustentáveis (SERS)
A análise energética completa encontra-se em `docs_sers/analise_energetica_sers.md` e foi integrada diretamente às orientações `ID 8`, `ID 9`, `ID 10`, `ID 11` e `ID 12` da base de conhecimento.

### Resumo da Comparação (Aquecimento de Água — Família de 4 pessoas / 30 min diários)
- **Cenário Base (Chuveiro Elétrico 5500W - Modo Inverno):** Consumo de `82,5 kWh/mês` (`R$ 70,13/mês` | `64,35 kg CO2/ano`).
- **Alternativa 1 (Eficiência Energética — Modo Verão 3200W):** Reduz o consumo para `48,0 kWh/mês` (`R$ 40,80/mês`), economizando **41,8%** (`R$ 29,33/mês`) com **custo zero** de implantação.
- **Alternativa 2 (Fonte Renovável — Aquecedor Solar de Baixo Custo - ASBC):** Reduz o consumo elétrico do chuveiro em **70%** (`24,75 kWh/mês` | `R$ 21,04/mês`), economizando `R$ 49,09/mês`, com investimento estimado de `R$ 580,00` (*payback* de ~11,8 meses) e redução de `45,05 kg CO2/ano`.

---

## 6. Resultados dos Testes com Usuários
O protótipo foi testado com **4 pessoas** externas à equipe, totalizando **12 atendimentos** (combinando perguntas livres sobre documentos e energia):
- **Taxa de resposta encontrada:** `91,7%` (11 de 12 atendimentos)
- **Taxa de acerto (ajudou o usuário):** `91,7%`
- **Tempo médio para encontrar a informação:** `8,4 segundos`
- **Tentativas médias por atendimento:** `1,1`
- **Nota média de facilidade de uso (1 a 5):** `4,8 / 5,0`
- **Dúvida sem solução identificada no teste:** *"Como pedir desconto na conta de luz?"* (inicialmente não continha o termo `"conta de luz"` nas palavras-chave da Tarifa Social).
- **Melhoria implementada após o teste:** Inclusão das palavras-chave `"conta de luz"` e `"energia barata"` na orientação ID 8 (`base_conhecimento.json`), elevando a busca para confiança ALTA.

---

## 7. Limitações do Sistema
1. **Busca lexical:** Como o motor utiliza correspondência exata de substrings normalizadas, sinônimos não cadastrados nas palavras-chave podem gerar baixa pontuação.
2. **Estimativas energéticas:** Os cálculos de economia e *payback* do módulo SERS consideram tarifas médias (`R$ 0,85/kWh`) e irradiação solar padrão, variando conforme a região geográfica e hábitos de cada família.
3. **Caráter informativo:** O assistente não realiza agendamentos reais nem consultas a bases governamentais.

---

## 8. Links dos Vídeos Técnicos (YouTube - Não Listado)
- **Vídeo Técnico PCP (5 a 8 min):** `[INSERIR LINK DO YOUTUBE AQUI]`
- **Vídeo Técnico SERS (até 3 min):** `[INSERIR LINK DO YOUTUBE AQUI]`

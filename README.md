# Citizen Assist AI — Assistente Digital de Orientação ao Cidadão e Eficiência Energética

Projeto desenvolvido para a **Global Solution 2026.2 (FIAP — 1CC)** integrando as disciplinas de **Pensamento Computacional e Automação com Python (PCP)** e **Soluções em Energias Renováveis e Sustentáveis (SERS)**.

## Integrantes
- **Lucas Bellezzo Figueiredo** — RM569734
- **Matheus Sabino da Silva Guedes** — RM572907

---

## 1. Para quem foi feito e qual problema resolve

O assistente foi pensado para **famílias de baixa renda e pessoas em situação de vulnerabilidade** que muitas vezes não sabem onde tirar um documento, como acessar um benefício ou o que fazer para pagar menos na conta de luz.

A informação existe, mas está espalhada em sites com linguagem burocrática ou em páginas difíceis de navegar. O Citizen Assist AI reúne essas orientações em um único lugar, em linguagem simples, sempre indicando a fonte oficial.

**ODS relacionados:**
- **ODS 7 — Energia Limpa e Acessível:** o assistente explica como economizar energia em casa e como funciona a Tarifa Social.
- **ODS 10 — Redução das Desigualdades:** facilita o acesso à informação sobre documentos e direitos civis.
- **ODS 16 — Instituições Eficazes:** todas as respostas têm fonte oficial verificada.

---

## 2. Como rodar o projeto

Você precisa do **Python 3.10 ou mais recente**. Não é necessário instalar nada além disso — o projeto usa só a biblioteca padrão do Python.

```bash
git clone https://github.com/LucasBellezzo/citizen-ai-assist.git
cd citizen-ai-assist
python main.py
```

---

## 3. O que tem no repositório

```text
citizen-assist-ai/
├── README.md                          # Este arquivo
├── main.py                            # Ponto de entrada — roda o menu no terminal
├── orientacao.py                      # Representa uma orientação da base
├── base_conhecimento.py               # Carrega o JSON e faz a busca
├── assistente.py                      # Controla o atendimento, histórico e exportação
├── data/
│   ├── base_conhecimento.json         # 12 orientações verificadas em 3 categorias
│   ├── historico.json                 # Registros dos atendimentos realizados
│   └── atendimentos.csv               # Exportação dos atendimentos em CSV
└── docs_sers/
    └── analise_energetica_sers.md     # Estudo completo de eficiência energética (SERS)
```

---

## 4. Como o assistente encontra as respostas

O sistema não usa IA externa — toda a lógica de busca é feita por regras simples e transparentes.

Antes de comparar, a pergunta passa por uma **normalização**: tudo vira minúscula, acentos são removidos e pontuação é ignorada. Assim "Cartão SUS", "cartao sus" e "CARTAO SUS" são tratados da mesma forma.

**Como a pontuação funciona:**
- Se uma palavra-chave da orientação aparece na pergunta → **+3 pontos**
- Se uma palavra da pergunta (com 4 letras ou mais) aparece no título → **+1 ponto**

**Níveis de confiança:**
- **6 pontos ou mais** → Confiança ALTA
- **3 a 5 pontos** → Confiança MÉDIA
- **Menos de 3 pontos** → Não encontrado (o assistente sugere outras palavras e mostra as categorias)

**Privacidade:** o assistente nunca pede nome, CPF ou telefone. Qualquer entrada com 8 ou mais dígitos ou com @ é bloqueada automaticamente antes de qualquer processamento.

---

## 5. Parte de Energia e Sustentabilidade (SERS)

A análise completa está em `docs_sers/analise_energetica_sers.md` e foi integrada às orientações de ID 8 a 12 da base de conhecimento.

**O que foi comparado:** aquecimento de água para uma família de 4 pessoas, usando 30 minutos de chuveiro por dia, durante um mês.

| Alternativa | Consumo mensal | Custo/mês | Economia | Investimento |
|---|---|---|---|---|
| Chuveiro 5.500W (modo inverno) | 82,5 kWh | R$ 70,13 | — | — |
| Chuveiro 3.200W (modo verão) | 48,0 kWh | R$ 40,80 | R$ 29,33 (41,8%) | R$ 0,00 |
| Aquecedor Solar (ASBC) | 24,75 kWh | R$ 21,04 | R$ 49,09 (70%) | ~R$ 580,00 |

*Tarifa usada como referência: R$ 0,85/kWh (média residencial ANEEL). Fator de emissão CO₂: 0,065 kg/kWh (MCTI/SIN).*

O aquecedor solar usado como referência é o **ASBC (Aquecedor Solar de Baixo Custo)**, tecnologia social desenvolvida pela Sociedade do Sol, feita com tubos de PVC e materiais acessíveis. O retorno do investimento estimado é de cerca de **12 meses**.

**Fontes:**
- Tarifa: [ANEEL — Tarifas de Energia](https://www.aneel.gov.br/tarifas)
- Fator de emissão: [MCTI — Fatores de Emissão](https://antigo.mctic.gov.br/mctic/opencms/ciencia/SEPED/clima/textosDoEMFA_emissoes_CO2.html)
- Tecnologia ASBC: [Sociedade do Sol](https://www.sociedadedosol.org.br)
- Programa de Eficiência Energética: [PROCEL/Eletrobras](https://eletrobras.com/pt/Paginas/Procel.aspx)

---

## 6. Resultado dos testes com usuários

O assistente foi testado com **4 pessoas** de fora da equipe, totalizando **12 atendimentos** entre os dias 15 e 16 de novembro de 2026.

| Indicador | Resultado |
|---|---|
| Respostas encontradas | 91,7% (11 de 12) |
| Respostas que ajudaram | 91,7% |
| Tempo médio para encontrar | 8,4 segundos |
| Tentativas por atendimento | 1,1 em média |
| Nota de facilidade (1 a 5) | 4,8 / 5,0 |

**Dúvida que não foi respondida no primeiro teste:**
*"Como pedir desconto na conta de luz?"* — a pergunta não bateu com as palavras-chave cadastradas.

**Melhoria feita a partir disso:**
Adicionamos `"conta de luz"` e `"energia barata"` às palavras-chave da orientação ID 8 (Tarifa Social). Depois dessa mudança, a mesma pergunta passou a ser encontrada com confiança ALTA.

Dos 12 atendimentos, **5 foram sobre energia** (IDs 8, 9, 10, 10 e 11), com taxa de resposta de 80% antes da melhoria e 100% depois.

---

## 7. Limitações

1. **Busca por palavras exatas:** sinônimos que não estão cadastrados nas palavras-chave podem não ser encontrados.
2. **Estimativas de energia:** os cálculos de economia usam tarifas e irradiação solar médias — os valores reais variam conforme a região e os hábitos de cada família.
3. **Só informa, não age:** o assistente não faz agendamentos nem consulta sistemas do governo em tempo real.

---

## 8. Vídeos técnicos

- **Vídeo PCP (5 a 8 min):** `[INSERIR LINK DO YOUTUBE AQUI]`
- **Vídeo SERS (até 3 min):** `[INSERIR LINK DO YOUTUBE AQUI]`

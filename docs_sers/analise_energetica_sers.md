# Estudo Técnico — Soluções em Energias Renováveis e Sustentáveis (SERS)
**Projeto:** Citizen Assist AI — Eficiência Energética e Acesso à Energia Renovável para Famílias de Baixa Renda  
**Integrantes:**  
- Lucas Bellezzo Figueiredo (RM569734)  
- Matheus Sabino da Silva Guedes (RM572907)  

---

## 1. Definição do Contexto e Público-Alvo
- **Público escolhido:** Famílias de baixa renda residentes em moradias populares urbanas.
- **Necessidade energética abordada:** Redução do custo mensal da fatura de energia elétrica residencial, com foco no aquecimento de água para banho (responsável por cerca de 25% a 35% do consumo total de uma residência popular brasileira, segundo o PROCEL/EPE).
- **Como o assistente contribui:** O *Citizen Assist AI* traduz cálculos técnicos de potência ($W$), consumo ($kWh$) e retorno financeiro (*payback*) em orientações práticas e acessíveis, além de orientar sobre a documentação necessária para acesso à Tarifa Social de Energia Elétrica.

---

## 2. Premissas e Dados de Consumo (Base de Referência)
Para permitir uma comparação justa em um período de referência comum (**1 mês = 30 dias**), adotaram-se as seguintes premissas técnicas verificáveis:
- **Residência padrão:** 4 moradores.
- **Tempo diário de uso do chuveiro:** 7,5 minutos por pessoa = **30 minutos/dia** ($0,5\text{ h/dia}$).
- **Dias de uso no mês:** $30\text{ dias}$ ($15\text{ horas/mês}$ de operação).
- **Tarifa média de energia elétrica (estimada com impostos):** $\text{R\$ } 0,85 / \text{kWh}$ (referência média residencial ANEEL/distribuidoras).
- **Fator de emissão de $CO_2$ do Sistema Interligado Nacional (SIN):** $\approx 0,065\text{ kg CO}_2 / \text{kWh}$ (MCTI — dado estimado médio anual).
- **Fórmula de consumo mensal:**
  $$E_{\text{mês}} (\text{kWh}) = \frac{P (\text{W}) \times t (\text{h/dia}) \times 30}{1000}$$

---

## 3. Comparação de Alternativas (Cenário Base vs. Alternativas)

### Cenário Base (Referência Atual): Chuveiro Elétrico no Modo Inverno (5.500 W)
- **Consumo mensal:** $\frac{5500 \times 0,5 \times 30}{1000} = 82,5\text{ kWh/mês}$
- **Custo mensal com eletricidade:** $82,5 \times \text{R\$ } 0,85 = \text{R\$ } 70,13/\text{mês}$ ($	ext{R\$ } 841,50/\text{ano}$)
- **Emissão anual associada:** $82,5 \times 12 \times 0,065 = 64,35\text{ kg CO}_2/\text{ano}$

---

### Alternativa 1 (Eficiência e Mudança de Hábito): Chuveiro Elétrico no Modo Verão (3.200 W)
- **Descrição:** Ajuste da chave seletora de potência do chuveiro existente para a posição "Verão" ou "Morno" (3.200 W) e redução de desperdícios.
- **Consumo mensal:** $\frac{3200 \times 0,5 \times 30}{1000} = 48,0\text{ kWh/mês}$
- **Custo mensal com eletricidade:** $48,0 \times \text{R\$ } 0,85 = \text{R\$ } 40,80/\text{mês}$ ($	ext{R\$ } 489,60/\text{ano}$)
- **Economia obtida:** **$34,5\text{ kWh/mês}$** (**$41,8\%$** de redução) = **$\text{R\$ } 29,33/\text{mês}$** ($	ext{R\$ } 351,90/\text{ano}$).
- **Investimento inicial:** $\text{R\$ } 0,00$ (*Payback* imediato).
- **Impacto ambiental:** Redução de **$26,91\text{ kg CO}_2/\text{ano}$** e alívio na demanda de ponta da rede elétrica.
- **Limitações:** Conforto térmico reduzido em dias muito frios; continua dependendo 100% da rede elétrica.

---

### Alternativa 2 (Fonte Renovável): Aquecedor Solar de Baixo Custo (ASBC)
- **Descrição:** Sistema térmico solar construído com tubos de PVC, conexões hidráulicas e isolantes térmicos acessíveis (tecnologia social difundida pela Sociedade do Sol), atuando em pré-aquecimento ou substituição do chuveiro elétrico.
- **Premissa de cobertura solar:** Cobre em média **$70\%$** da demanda térmica anual (nos dias nublados/chuvosos, o chuveiro elétrico atua como apoio).
- **Consumo elétrico residual mensal:** $82,5 \times (1 - 0,70) = 24,75\text{ kWh/mês}$
- **Custo mensal com eletricidade:** $24,75 \times \text{R\$ } 0,85 = \text{R\$ } 21,04/\text{mês}$ ($	ext{R\$ } 252,45/\text{ano}$)
- **Economia obtida:** **$57,75\text{ kWh/mês}$** (**$70,0\%$** de redução) = **$\text{R\$ } 49,09/\text{mês}$** ($	ext{R\$ } 589,05/\text{ano}$).
- **Investimento inicial estimado:** $\text{R\$ } 580,00$ (materiais hidráulicos e reservatório térmico adaptado).
- **Tempo de retorno (*Payback* simples):** $\frac{580,00}{49,09} \approx 11,8\text{ meses}$ (menos de 1 ano).
- **Impacto ambiental:** Fonte 100% limpa e renovável na operação; evita **$45,05\text{ kg CO}_2/\text{ano}$** por residência.
- **Limitações:** Exige área ensolarada no telhado/laje, estrutura capaz de suportar o peso da água e manutenção periódica contra vazamentos ou ressecamento do PVC.

---

## 4. Tabela Comparativa Consolidada

| Indicador (Base Mensal / Anual) | Cenário Base (Inverno 5500W) | Alternativa 1 (Modo Verão 3200W) | Alternativa 2 (Aquecedor Solar ASBC - Renovável) |
| :--- | :---: | :---: | :---: |
| **Consumo Elétrico Mensal** | $82,50\text{ kWh}$ | $48,00\text{ kWh}$ | $24,75\text{ kWh}$ |
| **Custo Mensal na Conta** | $\text{R\$ } 70,13$ | $\text{R\$ } 40,80$ | $\text{R\$ } 21,04$ |
| **Economia Mensal (R$)** | — | $\text{R\$ } 29,33$ ($41,8\%$) | $\text{R\$ } 49,09$ ($70,0\%$) |
| **Investimento Inicial** | $\text{R\$ } 0,00$ | $\text{R\$ } 0,00$ | $\text{R\$ } 580,00$ (estimado) |
| **Payback (Retorno)** | — | Imediato | $\approx 11,8\text{ meses}$ |
| **Emissão Anual de $CO_2$** | $64,35\text{ kg}$ | $37,44\text{ kg}$ | $19,30\text{ kg}$ |
| **Viabilidade** | Alta (já instalado) | Altíssima (ação imediata) | Média/Alta (depende de telhado/sol) |

---

## 5. Justificativa das Recomendações no Assistente
No *Citizen Assist AI*, as duas alternativas são apresentadas de forma complementar (IDs `9` e `10` da base JSON):
1. **Curto prazo (Custo Zero):** Recomenda-se imediatamente a mudança para o **Modo Verão** e a adesão à **Tarifa Social de Energia Elétrica** (ID `8`), pois não exigem investimento financeiro.
2. **Médio prazo (Sustentabilidade Estrutural):** Para famílias que possuem laje ou telhado com boa incidência solar, recomenda-se o **Aquecedor Solar de Baixo Custo (ASBC)**, que oferece a maior redução permanente na conta ($70\%$) e o maior benefício ambiental.

---

## 6. Referências Verificáveis
1. **PROCEL / ELETROBRAS** — *Tabela de Consumo de Energia Elétrica Residencial*. Disponível em: https://www.gov.br/mme
2. **ANEEL** — *Tarifa Social de Energia Elétrica e Programa de Eficiencia Energetica (PEE)*. Disponível em: https://www.gov.br/aneel
3. **Sociedade do Sol** — *Manual do Aquecedor Solar de Baixo Custo (ASBC)*. Disponível em: https://sociedadedosol.org.br
4. **MCTI** — *Fatores de Emissão de $CO_2$ para geração de energia elétrica no Sistema Interligado Nacional (SIN)*.

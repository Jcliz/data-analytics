# Limpeza e preparação

## Registro das decisões

### D1

**Decisão e diagnóstico:** D1 — Preservação das participações nos charts; Q4, Q5 e Q6.

#### Problema e abrangência

219/2.800 ocorrências excedentes por id, sem duplicata chart-faixa nem linha igual: a faixa aparece em vários charts. Evidência: notebook §3, "Duplicidade e limite da chave".

#### Tratamento e justificativa

Uma linha por par chart-faixa: excluir pelo id apagaria participações das P1–P4. Nenhum dos 2.800 registros saiu; a chave final inclui a data da coleta.

**Implementação:** notebook §4, célula "Preservação do vínculo entre faixa e chart".

#### Validação após o tratamento

Chave composta com 0/2.800 duplicatas e 219/2.800 excedentes por id mantidos. Evidência: notebook §5, "Comparação antes e depois da preparação".

### D2

**Decisão e diagnóstico:** D2 — Padronização dos espaços em textos; Q12.

#### Problema e abrangência

1/2.800: "Sona Mohapatra" com espaço não separável no fim. Evidência: notebook §3, "Datas, formatos e categorias".

#### Tratamento e justificativa

Espaços nas pontas removidos de título, artista e chart, preservando acentos e maiúsculas; um campo mudou, nenhum registro saiu.

**Implementação:** notebook §4, célula "Padronização dos campos textuais".

#### Validação após o tratamento

Texto antes e depois exibido; de 1/2.800 para 0/2.800. Evidência: notebook §5, "Comparação antes e depois da preparação".

### D3

**Decisão e diagnóstico:** D3 — Conversão e sinalização das datas de lançamento; Q11.

#### Problema e abrangência

1/2.800: faixa 4346251442, "Dirty Bird", lançada em 28/10/2026, após a coleta de 16/10/2026; causa não confirmada. Evidência: notebook §3, "Datas, formatos e categorias".

#### Tratamento e justificativa

Lançamento convertido para data sem mudar o valor; criados data_coleta (metadados, UTC) e lancamento_posterior_coleta, que separa o futuro dos já ocorridos na P2. Sem exclusão nem estimativa.

**Implementação:** notebook §4, célula "Conversão e validação temporal", e §5, "Padronização dos nomes e tipos".

#### Validação após o tratamento

2.800 datas convertidas sem perda (formato, calendário e texto conferidos), a futura sinalizada e preservada na releitura. Evidência: notebook §5, "Gravação e releitura do conjunto preparado".

### D4

**Decisão e diagnóstico:** D4 — Identificação do chart geral e preservação da origem; Q14, Q15 e Q16.

#### Problema e abrangência

100/2.800 do chart geral e 11/2.800 com gênero genérico no álbum; ids e nomes de chart consistentes. Evidência: notebook §3, "Datas, formatos e categorias".

#### Tratamento e justificativa

Id e nome do chart mantidos e tipo_chart (geral ou genero) criado; o geral serve à P3 e o gênero do álbum não substitui a origem das P1–P4. Sem exclusão nem gênero estimado.

**Implementação:** notebook §4, célula "Identificação do chart de origem".

#### Validação após o tratamento

100/2.800 com id_chart zero como geral e 2.700/2.800 como genero, origens preservadas. Evidência: notebook §5, "Verificações finais do conjunto preparado".

### D5

**Decisão e diagnóstico:** D5 — Seleção dos atributos do conjunto preparado; Q2, Q3, Q9 e Q10.

#### Problema e abrangência

Uma prévia e 2.533 versões ausentes, 1.890 BPM e 27 ganhos zerados, em campos fora das P1–P4 e do RA2. Evidências: notebook §3, "Ausências nulas e textos vazios" e "Estatísticas descritivas e domínios numéricos".

#### Tratamento e justificativa

12 dos 102 atributos mais quatro de contexto ou qualidade: 16 colunas. Os 90 restantes (prévia, versão, BPM, ganho, álbum) ficam no bruto, sem imputação nem exclusão.

**Implementação:** notebook §5, célula "Seleção e organização dos atributos".

#### Validação após o tratamento

16 colunas do dicionário, sem nulos nos 2.800 registros, com os campos das P1–P4 e os cinco nomes do gerador do RA2. Evidência: notebook §5, "Verificações finais do conjunto preparado".

### D6

**Decisão e diagnóstico:** D6 — Padronização dos nomes e tipos; Q7 e Q8.

#### Problema e abrangência

Sem problemas de tipo ou domínio nas 2.800, mas nomes da API e datas em texto a organizar. Evidência: notebook §3, "Estatísticas descritivas e domínios numéricos".

#### Tratamento e justificativa

Nomes em português (rank mantido pelo gerador): oito inteiros, quatro textos, duas datas e dois booleanos. Valores válidos intactos; falha de conversão não vira zero.

**Implementação:** notebook §5, célula "Padronização dos nomes e tipos".

#### Validação após o tratamento

Inteiros conferidos (ausência, finitude, fração) antes da conversão; domínios, valores e tipos mantidos na releitura. Evidências: notebook §5, "Verificações finais do conjunto preparado" e "Gravação e releitura do conjunto preparado".

### D7

**Decisão e diagnóstico:** D7 — Preservação e sinalização dos extremos de duração; Q17 e Q18.

#### Problema e abrangência

143/2.800 durações fora do IQR (66,5 a 366,5 s) e 0/2.800 ranks. Evidência: notebook §3, "Possíveis outliers e integridade do enriquecimento".

#### Tratamento e justificativa

Valores mantidos e duracao_fora_limites_iqr criado: extremo não comprova erro, e cortá-lo alteraria a distribuição da P1.

**Implementação:** notebook §4, célula "Sinalização dos extremos de duração".

#### Validação após o tratamento

143/2.800 sinalizadas pela regra de Q17 e Q18 (seção 03), valores iguais à origem. Evidência: notebook §5, "Verificações finais do conjunto preparado".

### D8

**Decisão e diagnóstico:** D8 — Manutenção e revalidação dos dados aprovados; Q1, Q13 e Q19–Q21.

#### Problema e abrangência

0/2.800 problemas em campos essenciais, nomes por artista e junções (inclusive duração e rank). Evidências: notebook §3, "Ausências nulas e textos vazios", "Datas, formatos e categorias" e "Possíveis outliers e integridade do enriquecimento".

#### Tratamento e justificativa

Valores aprovados mantidos e testes repetidos, sem imputação; o df_bruto ficou intacto (a preparação usou uma cópia).

**Implementação:** notebook §5, célula "Verificações finais do conjunto preparado".

#### Validação após o tratamento

2.800 registros aprovados em obrigatórios, chave, domínios, nomes, datas, sinalizações e integridade; valores iguais ao bruto e releitura igual à memória. Evidência: notebook §5, "Gravação e releitura do conjunto preparado".

## Resumo das intervenções

| Decisão | Ação executada | Impacto nos dados | Evidência |
|---|---|---|---|
| D1 | Preservar o vínculo chart-faixa | 2.800/2.800 mantidos; 219/2.800 excedentes por id preservados | Notebook §4, "Preservação do vínculo entre faixa e chart" |
| D2 | Remover espaços nas pontas | De 1/2.800 para 0/2.800 | Notebook §4, "Padronização dos campos textuais" |
| D3 | Converter e sinalizar datas | 2.800 convertidas; 1/2.800 futura mantida e sinalizada | Notebook §4, "Conversão e validação temporal" |
| D4 | Identificar o tipo de chart | 100/2.800 do geral identificadas e preservadas | Notebook §4, "Identificação do chart de origem" |
| D5 | Selecionar atributos | 12 de origem, 90 não selecionados e quatro novos; 16 finais | Notebook §5, "Seleção e organização dos atributos" |
| D6 | Padronizar nomes e tipos | 16 colunas: oito inteiros, quatro textos, duas datas, dois booleanos | Notebook §5, "Padronização dos nomes e tipos" |
| D7 | Sinalizar extremos | 143/2.800 sinalizadas, sem exclusão ou alteração | Notebook §4, "Sinalização dos extremos de duração" |
| D8 | Revalidar consistência | 2.800/2.800 aprovados pelas regras finais | Notebook §5, "Verificações finais do conjunto preparado" |

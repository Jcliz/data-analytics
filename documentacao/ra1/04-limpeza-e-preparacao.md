# Limpeza e preparação

## Registro das decisões

### D1

**Decisão e diagnóstico:** D1 — Preservação das participações nos charts; Q4, Q5 e Q6.

#### Problema e abrangência

O diagnóstico identificou 219/2.800 ocorrências excedentes por id de faixa, mas nenhuma duplicata pelo par chart-faixa nem linha inteira igual. Uma faixa pode participar de charts diferentes. Evidência: notebook §3, célula "Duplicidade e limite da chave".

#### Tratamento e justificativa

Preservamos uma linha por combinação de chart e faixa. Excluir somente pelo id eliminaria participações necessárias às P1–P4. Nenhum dos 2.800 registros foi removido. No arquivo final, a chave inclui também a data da coleta.

**Implementação:** notebook §4, célula "Preservação do vínculo entre faixa e chart".

#### Validação após o tratamento

As combinações de origem foram comparadas antes e depois, sem perda. A chave composta permaneceu com 0/2.800 duplicatas, e os 219/2.800 excedentes por id foram mantidos. Evidências: notebook §4, célula "Preservação do vínculo entre faixa e chart", e §5, "Comparação antes e depois da preparação".

### D2

**Decisão e diagnóstico:** D2 — Padronização dos espaços em textos; Q12.

#### Problema e abrangência

Uma das 2.800 ocorrências tinha espaço na ponta de um campo textual. O caso era o nome "Sona Mohapatra", com um espaço não separável ao final. Evidências: notebook §3, célula "Datas, formatos e categorias", e §4, "Padronização dos campos textuais".

#### Tratamento e justificativa

Removemos espaços no início e no fim de título, nome do artista e nome do chart. A operação preservou acentos, letras maiúsculas e minúsculas e o conteúdo dos nomes. Houve uma alteração de campo em uma ocorrência, sem exclusão de registros.

**Implementação:** notebook §4, célula "Padronização dos campos textuais".

#### Validação após o tratamento

A célula exibe o texto antes e depois. A verificação de espaços nas pontas passou de 1/2.800 para 0/2.800 ocorrências. Evidências: notebook §4, "Padronização dos campos textuais", e §5, "Comparação antes e depois da preparação".

### D3

**Decisão e diagnóstico:** D3 — Conversão e sinalização das datas de lançamento; Q11.

#### Problema e abrangência

Uma das 2.800 ocorrências tem lançamento posterior à coleta: a faixa 4346251442, "Dirty Bird", registra 28/10/2026, após a coleta de 16/10/2026. A causa não foi confirmada. Evidência: notebook §3, célula "Datas, formatos e categorias".

#### Tratamento e justificativa

Convertemos o lançamento para data e conservamos seu valor. Acrescentamos data_coleta, obtida dos metadados em UTC, e lancamento_posterior_coleta. A faixa não foi excluída e nenhuma data foi estimada. A sinalização distingue o lançamento futuro dos já ocorridos no recorte da P2.

**Implementação:** notebook §4, célula "Conversão e validação temporal", e §5, "Padronização dos nomes e tipos".

#### Validação após o tratamento

As 2.800 datas de lançamento foram convertidas sem perda, conferindo formato, calendário e equivalência com o texto original. A única ocorrência posterior à coleta foi mantida e sinalizada. A releitura do CSV preservou as datas. Evidências: notebook §4, "Conversão e validação temporal", e §5, "Gravação e releitura do conjunto preparado".

### D4

**Decisão e diagnóstico:** D4 — Identificação do chart geral e preservação da origem; Q14, Q15 e Q16.

#### Problema e abrangência

O retrato tem 100/2.800 ocorrências do chart geral e 11/2.800 com gênero genérico no álbum. Não houve inconsistência entre id e nome dos charts. Evidência: notebook §3, célula "Datas, formatos e categorias".

#### Tratamento e justificativa

Preservamos id e nome do chart de origem e criamos tipo_chart, com as categorias geral e genero. Mantivemos o geral para a comparação geral da P3. O gênero do álbum não substituiu a origem definida para P1–P4. Nenhuma faixa foi excluída nem recebeu gênero estimado.

**Implementação:** notebook §4, célula "Identificação do chart de origem".

#### Validação após o tratamento

As 100/2.800 ocorrências com id_chart igual a zero foram classificadas como geral; as demais 2.700/2.800, como genero. As relações entre ids e nomes e os pares de origem foram preservados. Evidências: notebook §4, "Identificação do chart de origem", e §5, "Verificações finais do conjunto preparado".

### D5

**Decisão e diagnóstico:** D5 — Seleção dos atributos do conjunto preparado; Q2, Q3, Q9 e Q10.

#### Problema e abrangência

Entre as 2.800 ocorrências, houve uma prévia ausente, 2.533 versões complementares ausentes, 1.890 BPM iguais a zero e 27 ganhos iguais a zero. Esses campos não alimentam P1–P4 nem o evento do RA2. Evidências: notebook §3, células "Ausências nulas e textos vazios" e "Estatísticas descritivas e domínios numéricos".

#### Tratamento e justificativa

Selecionamos 12 dos 102 atributos de origem e acrescentamos quatro campos de contexto ou qualidade, totalizando 16 colunas. Os 90 atributos não selecionados, inclusive prévia, versão, BPM, ganho e metadados de álbum, permanecem no bruto. Não houve imputação nem exclusão de faixas por essas ausências ou zeros.

**Implementação:** notebook §5, célula "Seleção e organização dos atributos".

#### Validação após o tratamento

O conjunto final contém as 16 colunas do dicionário atualizado, sem valores nulos em 2.800 registros. Os campos das P1–P4 e os cinco nomes esperados pelo gerador do RA2 foram mantidos. Evidências: notebook §5, "Seleção e organização dos atributos" e "Verificações finais do conjunto preparado".

### D6

**Decisão e diagnóstico:** D6 — Padronização dos nomes e tipos; Q7 e Q8.

#### Problema e abrangência

Q7 e Q8 não encontraram problemas de tipo ou domínio entre as 2.800 ocorrências. Os nomes da API e as datas em texto ainda precisavam ser organizados para o conjunto preparado. Evidência: notebook §3, célula "Estatísticas descritivas e domínios numéricos".

#### Tratamento e justificativa

Padronizamos os nomes em português, mantendo rank por compatibilidade com o gerador de eventos. Os campos finais têm oito inteiros, quatro textos, duas datas e dois booleanos. Valores numéricos válidos não foram modificados e falhas de conversão não foram substituídas por zero.

**Implementação:** notebook §5, célula "Padronização dos nomes e tipos".

#### Validação após o tratamento

Os inteiros foram conferidos quanto a ausência, finitude e parte fracionária antes da conversão. Os domínios e a igualdade dos valores preservados foram validados. A exportação e a releitura mantiveram todos os valores e tipos explicitamente reconstruídos. Evidências: notebook §5, "Padronização dos nomes e tipos", "Verificações finais do conjunto preparado" e "Gravação e releitura do conjunto preparado".

### D7

**Decisão e diagnóstico:** D7 — Preservação e sinalização dos extremos de duração; Q17 e Q18.

#### Problema e abrangência

Foram identificadas 143/2.800 durações fora dos limites IQR de 66,5 a 366,5 segundos e 0/2.800 ranks fora dos limites calculados. Evidência: notebook §3, célula "Possíveis outliers e integridade do enriquecimento".

#### Tratamento e justificativa

Preservamos duração e rank e criamos duracao_fora_limites_iqr. Um extremo estatístico não comprova erro. Excluir ou substituir esses valores alteraria a distribuição que será estudada na P1, sem evidência suficiente para a intervenção.

**Implementação:** notebook §4, célula "Sinalização dos extremos de duração".

#### Validação após o tratamento

As 143/2.800 ocorrências foram sinalizadas pela mesma regra da T03. Duração e rank permaneceram iguais aos valores de origem. Não houve corte, substituição por média nem exclusão. Evidências: notebook §4, "Sinalização dos extremos de duração", e §5, "Verificações finais do conjunto preparado".

### D8

**Decisão e diagnóstico:** D8 — Manutenção e revalidação dos dados aprovados; Q1, Q13 e Q19–Q21.

#### Problema e abrangência

Essas verificações encontraram 0/2.800 ocorrências problemáticas em campos essenciais, nomes por id de artista e integridade das junções, incluindo duração e rank. Evidências: notebook §3, células "Ausências nulas e textos vazios", "Datas, formatos e categorias" e "Possíveis outliers e integridade do enriquecimento".

#### Tratamento e justificativa

Mantivemos os valores aprovados e repetimos os testes após a preparação. Nenhuma informação foi imputada. O df_bruto permaneceu intacto; a preparação trabalhou sobre uma cópia.

**Implementação:** notebook §5, célula "Verificações finais do conjunto preparado".

#### Validação após o tratamento

Os 2.800 registros passaram nos testes de campos obrigatórios, chave composta, domínios, nomes por artista, datas, sinalizações e integridade. Os valores preservados foram comparados com o bruto, e a releitura do CSV foi igual ao conjunto em memória. Evidências: notebook §5, "Verificações finais do conjunto preparado" e "Gravação e releitura do conjunto preparado".

## Resumo das intervenções

| Decisão | Ação executada | Impacto nos dados | Evidência |
|---|---|---|---|
| D1 | Preservar o vínculo chart-faixa | 2.800/2.800 registros mantidos; 219/2.800 excedentes por id preservados | Notebook §4, "Preservação do vínculo entre faixa e chart" |
| D2 | Remover espaços nas pontas | De 1/2.800 para 0/2.800 ocorrências | Notebook §4, "Padronização dos campos textuais" |
| D3 | Converter e sinalizar datas | 2.800 datas convertidas; 1/2.800 lançamentos futuros mantido e sinalizado | Notebook §4, "Conversão e validação temporal" |
| D4 | Identificar o tipo de chart | 100/2.800 ocorrências do geral identificadas e preservadas | Notebook §4, "Identificação do chart de origem" |
| D5 | Selecionar atributos | 12 atributos de origem mantidos, 90 não selecionados e quatro novos; 16 finais | Notebook §5, "Seleção e organização dos atributos" |
| D6 | Padronizar nomes e tipos | 16 colunas; oito inteiros, quatro textos, duas datas e dois booleanos | Notebook §5, "Padronização dos nomes e tipos" |
| D7 | Sinalizar extremos | 143/2.800 durações sinalizadas, sem exclusão ou alteração do valor | Notebook §4, "Sinalização dos extremos de duração" |
| D8 | Revalidar consistência | 2.800/2.800 registros aprovados pelas regras finais | Notebook §5, "Verificações finais do conjunto preparado" |

# Conjunto de dados resultante

**Arquivo ou conjunto final:** `dados/preparados/faixas_preparadas.csv`, CSV UTF-8, separador vírgula, sem coluna de índice: 2.800 registros, 16 atributos e 370.733 bytes. Evidência: notebook §5, célula "Gravação e releitura do conjunto preparado", e o próprio CSV.

**Unidade de observação final:** uma ocorrência de faixa em um chart de origem na data da coleta, com chave `data_coleta`, `id_chart` e `id_faixa`; a mesma faixa em charts diferentes não é duplicata. Evidência: notebook §5, célula "Verificações finais do conjunto preparado".

**Dicionário atualizado:** `dados/preparados/dicionario-faixas.md`, com origem, significado, tipo e domínio dos 16 atributos: oito inteiros, quatro textos, duas datas e dois booleanos. `rank` manteve o nome por compatibilidade com o gerador de eventos; os demais foram padronizados em português. Evidência: notebook §5, célula "Padronização dos nomes e tipos".

## Comparação antes e depois

| Medida | Após ingestão | Após preparação | Explicação da diferença |
|---|---|---|---|
| Registros | 2.800 | 2.800 | Ocorrências preservadas, sem exclusão (D1) |
| Atributos | 102 | 16 | 12 atributos de origem e quatro campos de contexto ou qualidade (D5) |
| Ocorrências com espaços nas pontas | 1/2.800 (0,04%) | 0/2.800 (0,00%) | Correção textual sem alterar a escrita (D2) |
| Duplicatas pela chave chart-faixa | 0/2.800 (0,00%) | 0/2.800 (0,00%) | Unicidade mantida em cada chart e retrato (D1) |
| Ocorrências excedentes por id da faixa | 219/2.800 (7,82%) | 219/2.800 (7,82%) | Participações em charts distintos mantidas (D1) |
| Ocorrências do chart geral | 100/2.800 (3,57%) | 100/2.800 (3,57%), identificadas | Preservadas e distinguidas pelo tipo de chart (D4) |
| Lançamentos posteriores à coleta | 1/2.800 (0,04%) | 1/2.800 (0,04%), sinalizado | Valor da fonte preservado, sem imputar data (D3) |
| Durações fora dos limites IQR | 143/2.800 (5,11%) | 143/2.800 (5,11%), sinalizadas | Valores preservados, com sinalização de qualidade (D7) |

Evidência: notebook §5, célula "Comparação antes e depois da preparação", sobre o retrato de 16/10/2026. As medidas usam 2.800 registros como denominador e podem se sobrepor; não devem ser somadas.

## Verificações finais

Os 2.800 registros passaram nas verificações abaixo (notebook §5, células "Padronização dos nomes e tipos" e "Verificações finais do conjunto preparado"):

- As 16 colunas seguem o dicionário, sem nulos nos campos selecionados.
- A chave data-chart-faixa tem 0/2.800 duplicatas e preserva os vínculos de origem.
- Ids de faixa, artista e álbum, posição e duração são inteiros positivos; id_chart, rank e número de fãs, inteiros não negativos.
- Textos sem vazios nem espaços nas pontas; um nome de chart e um nome de artista por id.
- Datas convertidas sem perda; a data da coleta vem dos metadados, e as sinalizações seguem as regras temporal e IQR.
- Identificadores, duração, rank e fãs mantêm os valores de origem, e as junções com faixa, álbum e artista seguem consistentes.
- O df_bruto, comparado com a cópia anterior à preparação, permaneceu intacto.

O CSV foi relido com tipos informados e datas convertidas, e o relido é igual ao conjunto em memória em 2.800 linhas e 16 colunas (notebook §5, célula "Gravação e releitura do conjunto preparado"). Como CSV não guarda tipos, futuras leituras devem reaplicá-los conforme o dicionário.

## Limitações e pendências

O conjunto é o retrato de 16/10/2026, com país aparente US: não é série histórica nem permite comparar países. Evidência: `dados/brutos/2026-10-16/metadados.json`.

A causa da data futura (1/2.800) não foi confirmada; ela foi preservada e sinalizada, e na P2 não deve contar como lançamento já ocorrido nos 12 meses anteriores à coleta. As 143/2.800 durações fora dos limites IQR também foram mantidas e sinalizadas, pois o critério estatístico não comprova erro. Evidências: notebook §4, células "Conversão e validação temporal" e "Sinalização dos extremos de duração".

BPM, ganho, prévia, versão complementar e outros metadados ficaram fora do CSV, mas seguem no retrato bruto; a seleção não os corrige nem estima. Evidência: notebook §5, célula "Seleção e organização dos atributos".

As 100/2.800 ocorrências do chart geral seguem disponíveis para a P3. Os eventos por gênero do RA2 usam só `tipo_chart == "genero"`, 2.700/2.800 ocorrências; o filtro é aplicado na seção 9. Evidência: notebook §4, célula "Identificação do chart de origem".

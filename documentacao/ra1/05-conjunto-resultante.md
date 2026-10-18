# Conjunto de dados resultante

**Arquivo ou conjunto final:** `dados/preparados/faixas_preparadas.csv`, em CSV UTF-8, com separador vírgula e sem coluna de índice. O arquivo gerado tem 2.800 registros, 16 atributos e 370.733 bytes. Evidência: notebook §5, célula "Gravação e releitura do conjunto preparado", e o próprio CSV.

**Unidade de observação final:** uma ocorrência de faixa em um chart de origem na data da coleta. A chave é composta por `data_coleta`, `id_chart` e `id_faixa`. A faixa pode aparecer em charts diferentes sem constituir uma duplicata dessa chave. Evidência: notebook §5, célula "Verificações finais do conjunto preparado".

**Dicionário atualizado:** `dados/preparados/dicionario-faixas.md`, com os 16 atributos, sua origem, significado, tipos e domínios. São oito inteiros, quatro textos, duas datas e dois booleanos. O nome `rank` foi mantido por compatibilidade com o gerador de eventos; os demais nomes selecionados foram padronizados em português. Evidência: notebook §5, célula "Padronização dos nomes e tipos".

## Comparação antes e depois

| Medida | Após ingestão | Após preparação | Explicação da diferença |
|---|---|---|---|
| Registros | 2.800 | 2.800 | Preservação das ocorrências nos charts, sem exclusão (D1) |
| Atributos | 102 | 16 | Seleção de 12 atributos de origem e acréscimo de quatro campos de contexto ou qualidade (D5) |
| Ocorrências com espaços nas pontas | 1/2.800 (0,04%) | 0/2.800 (0,00%) | Correção textual, sem alterar a escrita dos nomes (D2) |
| Duplicatas pela chave chart-faixa | 0/2.800 (0,00%) | 0/2.800 (0,00%) | Preservação da unicidade dentro de cada chart e retrato (D1) |
| Ocorrências excedentes por id da faixa | 219/2.800 (7,82%) | 219/2.800 (7,82%) | Manutenção das participações em charts distintos (D1) |
| Ocorrências do chart geral | 100/2.800 (3,57%) | 100/2.800 (3,57%), identificadas | Preservação e distinção explícita do tipo de chart (D4) |
| Lançamentos posteriores à coleta | 1/2.800 (0,04%) | 1/2.800 (0,04%), sinalizado | Preservação do valor da fonte, sem imputação de data (D3) |
| Durações fora dos limites IQR | 143/2.800 (5,11%) | 143/2.800 (5,11%), sinalizadas | Preservação dos valores e inclusão de sinalização de qualidade (D7) |

Evidência: notebook §5, célula "Comparação antes e depois da preparação". As medidas por ocorrência usam 2.800 registros como denominador, podem se sobrepor e não devem ser somadas. Os valores finais resultam da execução sobre o retrato de 16/10/2026.

## Verificações finais

Os 2.800 registros passaram nas verificações abaixo. Evidência: notebook §5, células "Padronização dos nomes e tipos" e "Verificações finais do conjunto preparado".

- As 16 colunas correspondem ao dicionário atualizado, sem valores nulos nos campos selecionados.
- A chave data-chart-faixa tem 0/2.800 duplicatas e preserva os vínculos de origem.
- Os identificadores de faixa, artista e álbum, a posição e a duração são inteiros positivos; id_chart, rank e número de fãs são inteiros não negativos.
- Os textos selecionados não estão vazios nem têm espaços nas pontas; há um nome de chart por id e um nome de artista por id no conjunto preparado.
- As datas foram convertidas sem perda de seus valores; a data da coleta vem dos metadados, e as sinalizações correspondem às regras de comparação temporal e IQR.
- Identificadores, duração, rank e quantidade de fãs mantêm seus valores de origem. As junções com faixa, álbum e artista continuam consistentes.
- O df_bruto foi comparado com a cópia anterior à preparação e permaneceu intacto.

A exportação foi seguida de releitura do CSV, com tipos explicitamente informados e datas convertidas. A comparação entre o conjunto em memória e o relido confirmou igualdade em 2.800 linhas e 16 colunas. Evidência: notebook §5, célula "Gravação e releitura do conjunto preparado". Como CSV não armazena tipos, esses parâmetros devem ser reaplicados em futuras leituras, conforme o dicionário.

## Limitações e pendências

O conjunto representa o retrato de 16/10/2026, com país aparente US; não constitui uma série histórica nem permite comparar países. Evidência: `dados/brutos/2026-10-16/metadados.json`.

A causa da data futura em 1/2.800 ocorrências não foi confirmada. Ela foi preservada e sinalizada; na P2, esse lançamento não deve ser contado como já ocorrido nos 12 meses anteriores à coleta. As 143/2.800 durações fora dos limites IQR também foram mantidas e sinalizadas: o critério estatístico não comprova erro. Evidências: notebook §4, células "Conversão e validação temporal" e "Sinalização dos extremos de duração".

BPM, ganho, prévia, versão complementar e outros metadados não integram o CSV selecionado, mas continuam disponíveis no retrato bruto. A seleção não corrige nem estima essas informações. Evidência: notebook §5, célula "Seleção e organização dos atributos".

As 100/2.800 ocorrências do chart geral permanecem disponíveis para a P3. Nos eventos por gênero do RA2, a fonte deve ser filtrada para `tipo_chart == "genero"`, que identifica 2.700/2.800 ocorrências. A integração desse filtro na seção 9 ainda precisa ser concluída antes da execução final do RA2. Evidência: notebook §4, célula "Identificação do chart de origem".

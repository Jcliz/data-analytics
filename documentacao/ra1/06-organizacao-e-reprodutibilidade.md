# Organização e reprodutibilidade

**Repositório e versão:** https://github.com/eduardofabrii/data-analytics-ras • ramo `main`, com o notebook executado, os dados brutos e preparados e as dependências

**Ambiente:** Google Colab (referência) ou Python 3.9 ou mais novo em máquina local • versões mínimas em `requirements.txt`: pandas 2.2 a 2.x e requests 2.31 ou mais novo (RA1), pyspark 4.0.3 com Java 17 ou mais novo (RA2), jupyter e nbconvert (execução do notebook) • conferidas em 16/10/2026 numa instalação limpa: Python 3.13.16, pandas 2.3.3, requests 2.34.2, pyspark 4.0.3, nbconvert 7.17.2, python-docx 1.2.0 e pypdf 6.21.0

## Localização dos artefatos

| Artefato | Caminho ou forma de obtenção |
|---|---|
| Dados brutos | `dados/brutos/2026-10-16/`, versionado: respostas cruas da API em JSON (`infos.json`, `generos.json`, `charts.json`, `faixas.json`, `albuns.json`, `artistas.json`, 57,7 MB) e `metadados.json` (horário, país aparente US, 6.591 chamadas, 0 erros). Nova coleta só com `BAIXAR_DA_API = True` na célula "Preparação do ambiente" (primeira célula de código da seção 2) |
| Código de ingestão e preparação | `notebook/ra1-ra2-deezer.ipynb`, já executado e com as saídas salvas (ambiente e ingestão na seção 2, a partir da célula "Preparação do ambiente", exploração na 3, limpeza na 4 e transformação na 5) |
| Dados preparados | `dados/preparados/faixas_preparadas.csv` (UTF-8, separador vírgula), regravado pelas seções 4 e 5 a cada execução; nunca editado à mão. Colunas descritas em `dados/preparados/dicionario-faixas.md` |
| Documentação e dependências | `README.md` (seções "Execução no Google Colab", "Execução local" e "Dados e resultados esperados"), `dados/preparados/dicionario-faixas.md` e `requirements.txt` |

## Passos para reprodução

| Ordem | Instrução executável | Resultado esperado |
|---|---|---|
| 1 | Preparar o ambiente. No Colab: *Arquivo → Abrir notebook → GitHub*, repositório `eduardofabrii/data-analytics-ras`, arquivo `notebook/ra1-ra2-deezer.ipynb`. Localmente: `git clone https://github.com/eduardofabrii/data-analytics-ras.git`, `cd data-analytics-ras`, `python -m venv .venv`, ativar e `pip install -r requirements.txt` | No Colab, o notebook abre com o RA1 e o RA2. Localmente, `pip` e `python -c "import pandas, requests"` terminam sem erro |
| 2 | Obter os dados, sem acessar a API: a célula "Preparação do ambiente", na seção 2, clona o repositório no Colab com `BAIXAR_DA_API = False`, e as células seguintes leem o retrato versionado em `dados/brutos/` | "Preparação do ambiente" mostra a raiz do projeto; "Leitura do retrato bruto mais recente", `dados/brutos/2026-10-16` e os sete JSON |
| 3 | Executar do início ao fim. No Colab: *Ambiente de execução → Executar tudo*. Localmente: `python -m jupyter notebook notebook/ra1-ra2-deezer.ipynb` e executar todas as células na ordem, ou `jupyter nbconvert --to notebook --execute --inplace notebook/ra1-ra2-deezer.ipynb` | Nenhuma célula com erro; na seção 2, `df_bruto: 2800 linhas × 102 colunas`, 2.581 faixas, 2.292 álbuns, 1.688 artistas e nenhum item sem detalhe ("Verificação do carregamento") |
| 4 | Validar a saída: conferir o conjunto preparado e as contagens do RA2 | `dados/preparados/faixas_preparadas.csv` regravado com 2.800 linhas e 16 colunas (seção 5, célula "Gravação e releitura do conjunto preparado"); na seção 11, totais de 30, 60 e 90 reproduções simuladas |

A reprodução não depende da API (fora do ar, bloqueada ou com outro chart conforme o país e o dia): o notebook lê por padrão o retrato versionado de 16/10/2026, base dos números deste documento. Uma coleta nova (`BAIXAR_DA_API = True`) grava outra pasta em `dados/brutos/`, lida por ser a mais recente, e muda todas as contagens; para voltar ao retrato da entrega, apague a pasta nova ou use um clone limpo.

## Verificação da reprodução

Em 20/10/2026, João Correa, que não escreveu o código das seções, executou o notebook a partir de um clone limpo: ambiente novo com `pip install -r requirements.txt` e execução com `jupyter nbconvert --execute`, em Linux (WSL2), Python 3.13.5, pandas 2.3.3, requests 2.34.2, PySpark 4.0.3 e Java 21. Resultado: 47 células de código em sequência, sem erro, em 14 s; `df_bruto` com 2.800 linhas × 102 colunas; `dados/preparados/faixas_preparadas.csv` regravado idêntico ao versionado; três lotes de 30 eventos processados (90 reproduções). Em 21/10/2026, o repositório da entrega foi executado de novo do mesmo modo, a partir de um clone limpo, em Linux com Python 3.13.16, pandas 2.3.3 e PySpark 4.0.3: as mesmas 47 células de código sem erro, `df_bruto` com 2.800 linhas × 102 colunas e o CSV preparado idêntico ao versionado.

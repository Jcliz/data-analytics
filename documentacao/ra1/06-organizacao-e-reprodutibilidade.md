# Organização e reprodutibilidade

<!--
Área B (T05) · Critérios C6.1 a C6.3. A "Verificação da reprodução" (C6.4) é preenchida na T13, depois da execução
final, por alguém que NÃO escreveu o código, a partir de um clone limpo e seguindo só os passos abaixo; o documento é
gerado de novo em seguida. Na T13, confira também se as versões do campo "Ambiente" batem com a saída da célula
"Preparação do ambiente" da execução final e ajuste se o Colab tiver mudado de versão.
-->

**Repositório e versão:** https://github.com/Jcliz/data-analytics • tag `entrega`, no commit da execução final (o PDF entregue fica em `output/entrega-ra1-ra2.pdf` nessa tag)

**Ambiente:** Google Colab (referência) ou Python 3.9 ou mais novo em máquina local • versões mínimas em `requirements.txt`: pandas 2.2 a 2.x e requests 2.31 ou mais novo (RA1), pyspark 4.0.3 com Java 17 ou mais novo (RA2), jupyter, nbconvert, python-docx e pypdf (notebook e PDFs) • conferidas em 16/10/2026 numa instalação limpa: Python 3.13.16, pandas 2.3.3, requests 2.34.2, pyspark 4.0.3, nbconvert 7.17.2, python-docx 1.2.0 e pypdf 6.21.0

## Localização dos artefatos

| Artefato | Caminho ou forma de obtenção |
|---|---|
| Dados brutos | `dados/brutos/2026-10-16/`, versionado: respostas cruas da API em JSON (`infos.json`, `generos.json`, `charts.json`, `faixas.json`, `albuns.json`, `artistas.json`, 57,7 MB) e `metadados.json` (horário, país aparente US, 6.591 chamadas, 0 erros). Nova coleta só com `BAIXAR_DA_API = True` na seção 00b |
| Código de ingestão e preparação | `notebook/projeto_data_analytics.ipynb`, gerado por `python scripts/montar_notebook.py` a partir de `notebook/secoes/` (ambiente em `00b`, ingestão em `02`, exploração em `03`, limpeza em `04`, transformação em `05`) |
| Dados preparados | `dados/preparados/faixas_preparadas.csv` (UTF-8, separador vírgula), regravado pelas seções 04 e 05 a cada execução; nunca editado à mão |
| Documentação e dependências | `README.md` (seção "Como executar"), este documento em `documentacao/ra1/` (gerado por `python scripts/gerar_docx_ra1.py`), `dados/README.md`, `requirements.txt` e `docs/adr/` (decisões) |

## Passos para reprodução

| Ordem | Instrução executável | Resultado esperado |
|---|---|---|
| 1 | Preparar o ambiente. No Colab: *Arquivo → Abrir notebook → GitHub*, repositório `Jcliz/data-analytics`, arquivo `notebook/projeto_data_analytics.ipynb`. Localmente: `git clone https://github.com/Jcliz/data-analytics.git`, `cd data-analytics`, `python -m venv .venv`, ativar e `pip install -r requirements.txt` | No Colab, o notebook abre com o RA1 e o RA2. Localmente, `pip` e `python -c "import pandas, requests"` terminam sem erro |
| 2 | Obter os dados, sem acessar a API: a seção 00b clona o repositório no Colab com `BAIXAR_DA_API = False`, e a seção 02 lê o retrato versionado em `dados/brutos/` | "Preparação do ambiente" mostra a raiz do projeto; "Leitura do retrato bruto mais recente", `dados/brutos/2026-10-16` e os sete JSON |
| 3 | Executar do início ao fim. No Colab: *Ambiente de execução → Executar tudo*. Localmente: `python scripts/montar_notebook.py` e `jupyter nbconvert --to notebook --execute --inplace notebook/projeto_data_analytics.ipynb` | Nenhuma célula com erro; na seção 2, `df_bruto: 2800 linhas × 102 colunas`, 2.581 faixas, 2.292 álbuns, 1.688 artistas e nenhum item sem detalhe ("Verificação do carregamento") |
| 4 | Validar a saída: conferir o conjunto preparado e rodar `python scripts/verificar_entrega.py` | `dados/preparados/faixas_preparadas.csv` regravado (seção 05); script sem pendência de notebook desatualizado ou não executado |

A reprodução não depende da API (fora do ar, bloqueada ou com outro chart conforme o país e o dia): o notebook lê por padrão o retrato versionado de 16/10/2026, base dos números deste documento. Uma coleta nova (`BAIXAR_DA_API = True`) grava outra pasta em `dados/brutos/`, lida por ser a mais recente, e muda todas as contagens; para voltar ao retrato da entrega, apague a pasta nova ou use um clone limpo.

## Verificação da reprodução

[Registre a data, o responsável, o ambiente e o resultado de uma execução completa a partir das instruções acima.]

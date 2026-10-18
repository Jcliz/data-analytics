# Organização e reprodutibilidade

<!--
Área B (T05) · Critérios C6.1 a C6.3. A "Verificação da reprodução" (C6.4) é preenchida na T13, depois da execução
final, por alguém que NÃO escreveu o código, a partir de um clone limpo e seguindo só os passos abaixo; o documento é
gerado de novo em seguida. Na T13, confira também se as versões do campo "Ambiente" batem com a saída da célula
"Preparação do ambiente" da execução final e ajuste se o Colab tiver mudado de versão.
-->

**Repositório e versão:** https://github.com/Jcliz/data-analytics • tag `entrega`, criada no commit da execução final (o PDF entregue fica em `output/entrega-ra1-ra2.pdf` nessa tag)

**Ambiente:** Google Colab como ambiente de referência, ou Python 3.9 ou mais novo em máquina local • bibliotecas e versões mínimas em `requirements.txt`: pandas 2.2 a 2.x e requests 2.31 ou mais novo (RA1), pyspark 4.0.3 com Java 17 ou mais novo (RA2), jupyter, nbconvert, python-docx e pypdf (geração do notebook e dos PDFs) • versões conferidas em 16/10/2026, numa instalação limpa do `requirements.txt`: Python 3.13.16, pandas 2.3.3, requests 2.34.2, pyspark 4.0.3, nbconvert 7.17.2, python-docx 1.2.0 e pypdf 6.21.0

## Localização dos artefatos

| Artefato | Caminho ou forma de obtenção |
|---|---|
| Dados brutos | `dados/brutos/2026-10-16/`, versionado no repositório: respostas cruas da API da Deezer em JSON (`infos.json`, `generos.json`, `charts.json`, `faixas.json`, `albuns.json`, `artistas.json`, 57,7 MB) e o `metadados.json` da coleta (horário, país aparente US, 6.591 chamadas, 0 erros). Nova coleta só com `BAIXAR_DA_API = True` na seção 00b do notebook |
| Código de ingestão e preparação | Notebook `notebook/projeto_data_analytics.ipynb`, gerado por `python scripts/montar_notebook.py` a partir de `notebook/secoes/` (um arquivo por seção: ambiente em `00b`, ingestão em `02`, exploração em `03`, limpeza em `04`, transformação em `05`) |
| Dados preparados | `dados/preparados/faixas_preparadas.csv` (UTF-8, separador vírgula), gravado pelas seções 04 e 05 do notebook a cada execução; não é editado à mão |
| Documentação e dependências | `README.md` (seção "Como executar"), este documento em `documentacao/ra1/` (gerado no template por `python scripts/gerar_docx_ra1.py`), `dados/README.md` (o que cada pasta guarda), `requirements.txt` (bibliotecas e versões) e as decisões em `docs/adr/` |

## Passos para reprodução

| Ordem | Instrução executável | Resultado esperado |
|---|---|---|
| 1 | Preparar o ambiente. No Colab: *Arquivo → Abrir notebook → GitHub*, repositório `Jcliz/data-analytics`, arquivo `notebook/projeto_data_analytics.ipynb`. Localmente: `git clone https://github.com/Jcliz/data-analytics.git`, `cd data-analytics`, `python -m venv .venv`, ativar o ambiente e `pip install -r requirements.txt` | No Colab, o notebook abre com as seções do RA1 e do RA2. Localmente, o `pip` termina sem erro e `python -c "import pandas, requests"` não acusa falta de biblioteca |
| 2 | Obter os dados: não é preciso acessar a API. A seção 00b do notebook clona o repositório no Colab e deixa `BAIXAR_DA_API = False`, e a seção 02 lê o retrato bruto versionado em `dados/brutos/` | A célula "Preparação do ambiente" mostra a raiz do projeto, e a célula "Leitura do retrato bruto mais recente" mostra `dados/brutos/2026-10-16` e os sete arquivos JSON do retrato |
| 3 | Executar o notebook do início ao fim. No Colab: *Ambiente de execução → Executar tudo*. Localmente: `python scripts/montar_notebook.py` e `jupyter nbconvert --to notebook --execute --inplace notebook/projeto_data_analytics.ipynb` | Nenhuma célula com erro. A seção 2 mostra `df_bruto: 2800 linhas × 102 colunas`, com 2.581 faixas, 2.292 álbuns e 1.688 artistas únicos e nenhum item sem detalhe (célula "Verificação do carregamento") |
| 4 | Validar e localizar a saída: conferir o conjunto preparado e rodar `python scripts/verificar_entrega.py` | `dados/preparados/faixas_preparadas.csv` regravado com as linhas e colunas descritas na seção 05 deste documento, e o script sem pendência de notebook desatualizado ou não executado |

A reprodução não depende da API da Deezer. A API pode estar fora do ar, bloqueada na rede ou responder outro chart conforme o país de onde vem a requisição, e o chart muda todo dia; por isso o notebook lê, por padrão, o retrato bruto de 16/10/2026 versionado no repositório, coletado com país aparente US, e os números deste documento são os desse retrato. Uma coleta nova (`BAIXAR_DA_API = True`) grava outra pasta em `dados/brutos/`, que passa a ser a lida por ser a mais recente, e muda as contagens de todas as seções. Para voltar ao retrato da entrega, basta apagar a pasta nova ou executar o notebook a partir de um clone limpo.

## Verificação da reprodução

[Registre a data, o responsável, o ambiente e o resultado de uma execução completa a partir das instruções acima.]

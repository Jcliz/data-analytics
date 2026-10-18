#> Seção do notebook: Preparação do ambiente (célula extra, antes do RA1)
#> Área responsável: B · Tarefa: T02 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ## Preparação do ambiente
#
# Esta célula prepara as bibliotecas, as pastas do projeto e a origem dos dados. No Google Colab, ela clona o repositório para ter acesso ao retrato bruto da API já coletado.

# %%
#> Contrato (CONTEXT.md §6): define RAIZ, PASTA_BRUTOS, PASTA_PREPARADOS, PASTA_STREAMING e BAIXAR_DA_API.
#> Não renomeie essas variáveis: as seções das outras áreas dependem delas.
# Preparação do ambiente: bibliotecas, pastas do projeto e origem dos dados
import subprocess
import sys
from pathlib import Path

import pandas as pd

URL_REPOSITORIO = "https://github.com/Jcliz/data-analytics.git"
RAMO = "main"  # no Colab, troque pelo ramo do repositório que quiser executar
NO_COLAB = "google.colab" in sys.modules

if NO_COLAB:
    if Path("data-analytics").exists():
        # Clone de uma execução anterior nesta sessão do Colab: traz a versão mais nova do ramo
        subprocess.run(["git", "-C", "data-analytics", "pull", "-q", "origin", RAMO], check=False)
    else:
        subprocess.run(["git", "clone", "-q", "-b", RAMO, URL_REPOSITORIO], check=True)

# A raiz é a pasta que contém o CONTEXT.md (funciona no Colab, na raiz ou dentro de notebook/)
candidatos = [Path("data-analytics"), Path.cwd(), Path.cwd().parent]
RAIZ = next((p.resolve() for p in candidatos if (p / "CONTEXT.md").exists()), None)
if RAIZ is None:
    raise FileNotFoundError(
        "Raiz do repositório não encontrada (pasta com o CONTEXT.md). Rode o notebook de dentro do clone "
        f"(raiz ou notebook/) ou, no Colab, confira se o ramo '{RAMO}' já tem a estrutura do projeto."
    )

PASTA_BRUTOS = RAIZ / "dados" / "brutos"
PASTA_PREPARADOS = RAIZ / "dados" / "preparados"
PASTA_STREAMING = RAIZ / "dados" / "streaming"
for pasta in (PASTA_BRUTOS, PASTA_PREPARADOS, PASTA_STREAMING):
    pasta.mkdir(parents=True, exist_ok=True)

# False: lê o retrato bruto versionado (ADR-0004). True: coleta de novo na API da Deezer.
BAIXAR_DA_API = False

pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 120)
print(f"Raiz do projeto: {RAIZ}")
print(f"Ambiente: {'Google Colab' if NO_COLAB else 'local'} · Python {sys.version.split()[0]} · pandas {pd.__version__}")

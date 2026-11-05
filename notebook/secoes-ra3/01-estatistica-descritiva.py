#> Notebook do RA3 — 1. Análise estatística descritiva (requisito 1 do enunciado)
#> Área responsável: C · Tarefa: T16 (entregas/plano-de-tarefas-ra3.md) · Critérios R1.1–R1.5
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Não há template do RA3: o enunciado desta seção é o requisito 2.1 de enunciados/ra3.md (ADR-0012). Não mude o sentido.
#> Leia antes: base/analise-e-ml.md, seções 1 e 2.

# %% [markdown]
# ## 1. Análise estatística descritiva
#
# Realize uma análise estatística dos dados, contemplando:
#
# - **Tendência central:** utilização de média e/ou mediana para compreender valores representativos.
# - **Dispersão:** utilização de medidas como amplitude ou desvio-padrão para analisar a variabilidade.
# - **Distribuição:** investigação da frequência, concentração ou distribuição dos valores.
#
# As medidas utilizadas devem ser coerentes com as características dos dados e com o problema investigado. Apresente os resultados e explique o que eles representam no contexto do projeto.

# %%
#> Esta célula e a seguinte vêm prontas da estrutura (CONTEXT.md, seção 6): as seções 2 a 4 usam RAIZ, PASTA_PREPARADOS e df_analise.
# Preparação do ambiente: bibliotecas, pastas do projeto e origem dos dados
import subprocess
import sys
from pathlib import Path

import pandas as pd

URL_REPOSITORIO = "https://github.com/eduardofabrii/data-analytics-ras.git"
PASTA_CLONE = "data-analytics-ras"
RAMO = "main"  # no Colab, troque pelo ramo do repositório que quiser executar
NO_COLAB = "google.colab" in sys.modules

if NO_COLAB:
    if Path(PASTA_CLONE).exists():
        # Clone de uma execução anterior nesta sessão do Colab: traz a versão mais nova do ramo
        subprocess.run(["git", "-C", PASTA_CLONE, "pull", "-q", "origin", RAMO], check=False)
    else:
        subprocess.run(["git", "clone", "-q", "-b", RAMO, URL_REPOSITORIO], check=True)

# A raiz é a pasta que contém o requirements.txt e o conjunto preparado (Colab, raiz ou dentro de notebook/)
candidatos = [Path(PASTA_CLONE), Path.cwd(), Path.cwd().parent]
RAIZ = next(
    (p.resolve() for p in candidatos
     if (p / "requirements.txt").exists() and (p / "dados" / "preparados" / "faixas_preparadas.csv").exists()),
    None,
)
if RAIZ is None:
    raise FileNotFoundError(
        "Raiz do repositório não encontrada (pasta com o requirements.txt e dados/preparados). "
        f"Rode o notebook de dentro do clone (raiz ou notebook/) ou, no Colab, confira o ramo '{RAMO}'."
    )
PASTA_PREPARADOS = RAIZ / "dados" / "preparados"

pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 120)
print(f"Raiz do projeto: {RAIZ.name}")  # só o nome da pasta: o caminho completo é da máquina de quem executa
print(f"Ambiente: {'Google Colab' if NO_COLAB else 'local'} · Python {sys.version.split()[0]} · pandas {pd.__version__}")

# %%
# Releitura do conjunto preparado para a análise
colunas_inteiras_analise = ["id_faixa", "id_chart", "posicao_chart", "id_artista", "id_album",
                            "duracao_s", "rank", "numero_fas"]
colunas_texto_analise = ["titulo", "genero", "tipo_chart", "artista"]
colunas_booleanas_analise = ["lancamento_posterior_coleta", "duracao_fora_limites_iqr"]
df_analise = pd.read_csv(
    PASTA_PREPARADOS / "faixas_preparadas.csv", encoding="utf-8",
    dtype={**{c: "int64" for c in colunas_inteiras_analise},
           **{c: "string" for c in colunas_texto_analise},
           **{c: "bool" for c in colunas_booleanas_analise}},
    parse_dates=["data_lancamento", "data_coleta"],
)
print(f"{len(df_analise)} ocorrências faixa-chart, {df_analise['id_faixa'].nunique()} faixas distintas, "
      f"{df_analise.loc[df_analise['tipo_chart'].eq('genero'), 'genero'].nunique()} charts de gênero "
      f"e {df_analise['tipo_chart'].eq('geral').sum()} ocorrências no chart geral.")

# %%
# Utilize quantas células de código forem necessárias para esta etapa.

# %% [markdown]
# **Resposta do grupo:**
#
# [Preencha aqui.]

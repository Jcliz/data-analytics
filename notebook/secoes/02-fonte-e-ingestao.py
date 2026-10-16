#> Seção do notebook: RA1 — 2. Fonte e ingestão dos dados
#> Área responsável: B · Tarefa: T02 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ## 2. Fonte e ingestão dos dados
#
# - Identifique a fonte dos dados, incluindo link ou referência de acesso.
# - Descreva brevemente o dataset e o que seus registros representam.
# - Explique como os dados foram carregados e implemente a ingestão.

# %% [markdown]
# **Resposta do grupo:**
#
# A fonte é a API pública da Deezer (`https://api.deezer.com`, documentação em `https://developers.deezer.com/api`), acessada sem autenticação e sem chave. Coletamos os charts de faixas mais tocadas: o chart geral e um chart por gênero da lista `/genre`. Cada registro do `df_bruto` é um item de um chart, ou seja, uma faixa na posição em que apareceu em um chart de origem; a mesma faixa pode aparecer em mais de um chart, e essas repetições ficam no bruto. Cada item recebe os campos extras da faixa (`/track/{id}`, como `bpm`, `isrc` e `release_date`), do álbum (`/album/{id}`, como gênero, gravadora e data de lançamento) e do artista (`/artist/{id}`, como `nb_fan` e `nb_album`), juntados pelo id.
#
# A ingestão é feita por código nas células abaixo: as chamadas passam por uma função com pausa entre requisições, novas tentativas e tratamento do objeto `error`, que a API devolve mesmo com HTTP 200. Os charts são paginados por `index` e `limit`. As respostas são gravadas cruas no retrato bruto `dados/brutos/AAAA-MM-DD/`, com um `metadados.json` da coleta, e o notebook lê esse retrato por padrão (`BAIXAR_DA_API = False`), para que os números sejam os mesmos em toda execução.
#
# [Preencha após a coleta: data do retrato, país aparente, quantidade de chamadas e de erros, gêneros coletados e df_bruto.shape, com os números das saídas abaixo.]

# %%
#> Contrato (CONTEXT.md §6): esta seção cria df_bruto. Lê RAIZ, PASTA_BRUTOS e BAIXAR_DA_API da seção 00b.
# Parâmetros da coleta e acesso à API
import json
import platform
import time
from datetime import datetime, timezone

import requests
from IPython.display import display

URL_API = "https://api.deezer.com"
LIMITE_PAGINA = 100       # itens por página do chart (parâmetro limit)
TETO_POR_CHART = 300      # máximo de itens lidos por chart, mesmo que a API ofereça mais
PAUSA_S = 0.15            # pausa entre chamadas; a API aceita cerca de 50 chamadas a cada 5 s
TENTATIVAS = 4            # tentativas por chamada antes de registrar o erro
TIMEOUT_S = 20

sessao = requests.Session()
registro = {"chamadas": 0, "chamadas_por_endpoint": {}, "novas_tentativas": 0, "erros": []}


def chamar_api(caminho, endpoint, **params):
    """GET em URL_API + caminho. Devolve o JSON da resposta ou None, registrando o erro.

    A Deezer devolve falhas como {"error": {...}} com HTTP 200: o código 4 (limite de chamadas)
    e falhas de rede ganham nova tentativa com espera crescente; os demais erros são registrados.
    """
    ultimo_erro = None
    for tentativa in range(1, TENTATIVAS + 1):
        time.sleep(PAUSA_S)
        registro["chamadas"] += 1
        registro["chamadas_por_endpoint"][endpoint] = registro["chamadas_por_endpoint"].get(endpoint, 0) + 1
        try:
            resposta = sessao.get(URL_API + caminho, params=params, timeout=TIMEOUT_S)
            resposta.raise_for_status()
            corpo = resposta.json()
        except (requests.RequestException, ValueError) as erro:
            ultimo_erro = {"tipo": type(erro).__name__, "mensagem": str(erro)[:200]}
        else:
            if not (isinstance(corpo, dict) and "error" in corpo):
                return corpo
            ultimo_erro = {"tipo": corpo["error"].get("type"), "codigo": corpo["error"].get("code"),
                           "mensagem": corpo["error"].get("message")}
            if ultimo_erro["codigo"] != 4:   # objeto inexistente ou parâmetro inválido: repetir não resolve
                break
        if tentativa < TENTATIVAS:
            registro["novas_tentativas"] += 1
            time.sleep(2 ** tentativa)
    registro["erros"].append({"caminho": caminho, "parametros": params, **ultimo_erro})
    return None


print(f"API: {URL_API} · limit={LIMITE_PAGINA} · teto por chart={TETO_POR_CHART} · pausa={PAUSA_S} s")
print(f"Coletar de novo na API: {BAIXAR_DA_API}")

# %%
#> Só roda com BAIXAR_DA_API = True (seção 00b). Coletar de novo muda todas as contagens: combine com o grupo antes.
# Coleta dos charts por gênero
if BAIXAR_DA_API:
    inicio_coleta = datetime.now(timezone.utc)
    infos = chamar_api("/infos", "/infos")   # país de onde a API enxerga a requisição

    resposta_generos = chamar_api("/genre", "/genre")
    if resposta_generos is None:
        raise RuntimeError(f"A API não devolveu a lista de gêneros: {registro['erros'][-1]}")
    generos = {g["id"]: g["name"] for g in resposta_generos["data"]}
    generos.setdefault(0, "All")   # chart geral

    charts = []
    for id_genero, nome_genero in generos.items():
        paginas = []
        for index in range(0, TETO_POR_CHART, LIMITE_PAGINA):
            pagina = chamar_api(f"/chart/{id_genero}/tracks", "/chart/{id}/tracks",
                                index=index, limit=LIMITE_PAGINA)
            if pagina is None:
                break
            paginas.append({"index": index, "limit": LIMITE_PAGINA, "resposta": pagina})
            lidos = len(pagina.get("data", []))
            if lidos < LIMITE_PAGINA or index + lidos >= pagina.get("total", index + lidos):
                break   # última página do chart
        charts.append({"id_genero": id_genero, "nome_genero": nome_genero, "paginas": paginas})
        itens = sum(len(p["resposta"].get("data", [])) for p in paginas)
        print(f"Chart {id_genero:>4} ({nome_genero}): {itens} itens em {len(paginas)} página(s)")
    print(f"{len(charts)} charts coletados em {registro['chamadas']} chamadas")

# %%
# Coleta dos detalhes de faixas, álbuns e artistas
if BAIXAR_DA_API:
    itens_chart = [item for c in charts for p in c["paginas"] for item in p["resposta"].get("data", [])]
    ids_faixas = sorted({item["id"] for item in itens_chart})
    ids_albuns = sorted({item["album"]["id"] for item in itens_chart if item.get("album")})
    ids_artistas = sorted({item["artist"]["id"] for item in itens_chart if item.get("artist")})
    print(f"{len(itens_chart)} itens nos charts · {len(ids_faixas)} faixas únicas · {len(ids_albuns)} álbuns únicos"
          f" · {len(ids_artistas)} artistas únicos")

    faixas = {}
    for i, id_faixa in enumerate(ids_faixas, 1):
        faixas[str(id_faixa)] = chamar_api(f"/track/{id_faixa}", "/track/{id}")
        if i % 250 == 0:
            print(f"  faixas: {i}/{len(ids_faixas)}")
    albuns = {}
    for i, id_album in enumerate(ids_albuns, 1):
        albuns[str(id_album)] = chamar_api(f"/album/{id_album}", "/album/{id}")
        if i % 250 == 0:
            print(f"  álbuns: {i}/{len(ids_albuns)}")
    artistas = {}
    for i, id_artista in enumerate(ids_artistas, 1):
        artistas[str(id_artista)] = chamar_api(f"/artist/{id_artista}", "/artist/{id}")
        if i % 250 == 0:
            print(f"  artistas: {i}/{len(ids_artistas)}")
    fim_coleta = datetime.now(timezone.utc)
    print(f"Coleta terminada: {registro['chamadas']} chamadas, {len(registro['erros'])} erro(s)")

# %%
# Gravação do retrato bruto
if BAIXAR_DA_API:
    pasta_retrato = PASTA_BRUTOS / inicio_coleta.strftime("%Y-%m-%d")
    pasta_retrato.mkdir(parents=True, exist_ok=True)
    conteudo = {"infos.json": infos, "generos.json": resposta_generos, "charts.json": charts,
                "faixas.json": faixas, "albuns.json": albuns, "artistas.json": artistas}
    for nome, dados in conteudo.items():
        # Respostas cruas da API, sem nenhuma alteração; JSON compacto para o retrato caber no repositório
        (pasta_retrato / nome).write_text(json.dumps(dados, ensure_ascii=False, separators=(",", ":")),
                                          encoding="utf-8")
    metadados = {
        "inicio_utc": inicio_coleta.isoformat(timespec="seconds"),
        "fim_utc": fim_coleta.isoformat(timespec="seconds"),
        "url_api": URL_API,
        "pais_aparente": (infos or {}).get("country_iso"),
        "endpoints": ["/infos", "/genre", "/chart/{id}/tracks", "/track/{id}", "/album/{id}", "/artist/{id}"],
        "parametros": {"limit": LIMITE_PAGINA, "teto_por_chart": TETO_POR_CHART, "pausa_s": PAUSA_S,
                       "tentativas": TENTATIVAS, "timeout_s": TIMEOUT_S},
        "chamadas": registro["chamadas"],
        "chamadas_por_endpoint": registro["chamadas_por_endpoint"],
        "novas_tentativas": registro["novas_tentativas"],
        "quantidade_erros": len(registro["erros"]),
        "erros": registro["erros"],
        "charts": len(charts),
        "itens_chart": len(itens_chart),
        "faixas_unicas": len(ids_faixas),
        "albuns_unicos": len(ids_albuns),
        "artistas_unicos": len(ids_artistas),
        "arquivos": sorted(conteudo) + ["metadados.json"],
        "ambiente": {"python": platform.python_version(), "pandas": pd.__version__,
                     "requests": requests.__version__, "colab": NO_COLAB},
    }
    (pasta_retrato / "metadados.json").write_text(json.dumps(metadados, ensure_ascii=False, indent=2),
                                                  encoding="utf-8")
    tamanho_mb = sum(a.stat().st_size for a in pasta_retrato.iterdir()) / 1e6
    print(f"Retrato gravado em {pasta_retrato.relative_to(RAIZ)} ({tamanho_mb:.1f} MB)")

# %%
# Leitura do retrato bruto mais recente
retratos = sorted(p for p in PASTA_BRUTOS.glob("????-??-??") if (p / "metadados.json").exists())
if not retratos:
    raise FileNotFoundError(
        f"Nenhum retrato bruto em {PASTA_BRUTOS}. Atualize o clone do repositório ou rode a seção 00b "
        "com BAIXAR_DA_API = True para coletar na API da Deezer."
    )
PASTA_RETRATO = retratos[-1]


def ler_json(nome):
    return json.loads((PASTA_RETRATO / nome).read_text(encoding="utf-8"))


metadados = ler_json("metadados.json")
charts = ler_json("charts.json")
faixas = ler_json("faixas.json")
albuns = ler_json("albuns.json")
artistas = ler_json("artistas.json")
print(f"Retrato lido: {PASTA_RETRATO.relative_to(RAIZ)} ({len(retratos)} retrato(s) disponível(is))")
for arquivo in sorted(PASTA_RETRATO.iterdir()):
    print(f"  {arquivo.name:<15} {arquivo.stat().st_size / 1e6:6.2f} MB")

# %%
# Metadados do retrato lido
resumo_metadados = pd.Series({
    "Início da coleta (UTC)": metadados["inicio_utc"],
    "Fim da coleta (UTC)": metadados["fim_utc"],
    "País aparente da requisição": metadados["pais_aparente"],
    "Endpoints": ", ".join(metadados["endpoints"]),
    "Parâmetros": ", ".join(f"{k}={v}" for k, v in metadados["parametros"].items()),
    "Chamadas à API": metadados["chamadas"],
    "Novas tentativas": metadados["novas_tentativas"],
    "Erros registrados": metadados["quantidade_erros"],
    "Charts coletados": metadados["charts"],
    "Itens nos charts": metadados["itens_chart"],
    "Faixas únicas": metadados["faixas_unicas"],
    "Álbuns únicos": metadados["albuns_unicos"],
    "Artistas únicos": metadados["artistas_unicos"],
    "Ambiente da coleta": ", ".join(f"{k} {v}" for k, v in metadados["ambiente"].items()),
}, name="valor")
display(resumo_metadados.to_frame())
display(pd.Series(metadados["chamadas_por_endpoint"], name="chamadas").to_frame())
if metadados["erros"]:
    display(pd.DataFrame(metadados["erros"]))

# %%
#> Achata sem limpar: tipos, ausências, duplicatas e valores estranhos ficam como vieram (diagnóstico na seção 3,
#> tratamento na seção 4). Nomes da API mantidos; prefixos: chart_ (origem), detalhe_faixa_, detalhe_album_ e detalhe_artista_.
# Montagem do df_bruto
linhas = []
for chart in charts:
    ordem = 0
    for pagina in chart["paginas"]:
        for item in pagina["resposta"].get("data", []):
            ordem += 1
            linhas.append({"chart_id_genero": chart["id_genero"], "chart_nome_genero": chart["nome_genero"],
                           "chart_ordem": ordem, **item})
itens = pd.json_normalize(linhas, sep="_")


def campos_simples(objeto, prefixo, ignorar=()):
    """Campos de primeiro nível de uma resposta (objetos aninhados ficam de fora; listas ficam como vieram)."""
    return {f"{prefixo}{k}": v for k, v in objeto.items() if not isinstance(v, dict) and k not in ignorar}


detalhe_faixas = pd.DataFrame([campos_simples(f, "detalhe_faixa_") for f in faixas.values() if f])
detalhe_albuns = pd.DataFrame([
    {**campos_simples(a, "detalhe_album_", ignorar=("tracks",)),
     "detalhe_album_genres": (a.get("genres") or {}).get("data")}
    for a in albuns.values() if a
])
detalhe_artistas = pd.DataFrame([campos_simples(a, "detalhe_artista_") for a in artistas.values() if a])

df_bruto = (
    itens
    .merge(detalhe_faixas, how="left", left_on="id", right_on="detalhe_faixa_id")
    .merge(detalhe_albuns, how="left", left_on="album_id", right_on="detalhe_album_id")
    .merge(detalhe_artistas, how="left", left_on="artist_id", right_on="detalhe_artista_id")
)
print(f"df_bruto: {df_bruto.shape[0]} linhas × {df_bruto.shape[1]} colunas")

# %%
# Verificação do carregamento
origem_colunas = pd.Series(
    ["chart" if c.startswith("chart_") else "detalhe da faixa" if c.startswith("detalhe_faixa_")
     else "detalhe do álbum" if c.startswith("detalhe_album_")
     else "detalhe do artista" if c.startswith("detalhe_artista_") else "item do chart" for c in df_bruto.columns]
).value_counts().rename("colunas")
print(f"Linhas: {len(df_bruto)} (itens nos charts segundo os metadados: {metadados['itens_chart']})")
print(f"Faixas únicas: {df_bruto['id'].nunique()} · álbuns únicos: {df_bruto['album_id'].nunique()} · "
      f"artistas únicos: {df_bruto['artist_id'].nunique()}")
print(f"Itens sem detalhe da faixa: {df_bruto['detalhe_faixa_id'].isna().sum()} · "
      f"sem detalhe do álbum: {df_bruto['detalhe_album_id'].isna().sum()} · "
      f"sem detalhe do artista: {df_bruto['detalhe_artista_id'].isna().sum()}")
display(origem_colunas.to_frame())
display(df_bruto.groupby(["chart_id_genero", "chart_nome_genero"]).size().rename("itens").to_frame())
display(df_bruto.head())

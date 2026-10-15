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
# [Preencha aqui.]
#
# <!--
# Fonte (Deezer, URL da API, data da coleta), o que um registro representa e como os dados são carregados
# (endpoints, paginação, pausa, retrato bruto). Mesmo conteúdo da ficha em documentacao/ra1/02-fontes-e-ingestao.md.
# -->

# %%
#> Template: "Utilize quantas células de código forem necessárias para esta etapa."
#> Crie quantas células "# %%" precisar; comece cada uma com um comentário-título curto (ex.: "# Duplicados por id"),
#> que é como o documento do RA1 cita a evidência.
#> Passos esperados (base/api-deezer.md §6):
#> 1. Funções de acesso à API com pausa entre chamadas e tratamento do objeto "error" (resposta com HTTP 200).
#> 2. Se BAIXAR_DA_API: coletar /genre, /chart/{id}/tracks (paginado), /track/{id} e /album/{id};
#>    gravar as respostas cruas em PASTA_BRUTOS / "AAAA-MM-DD" e um metadados.json (data, chamadas, erros).
#> 3. Sempre: ler o retrato mais recente de PASTA_BRUTOS e achatar em df_bruto (uma linha por item coletado,
#>    mantendo duplicatas entre charts e a coluna do chart de origem). NÃO limpar aqui (é da área D).
#> 4. Verificar o carregamento: df_bruto.shape, colunas, primeiras linhas, quantidade por chart de origem.
#> Contrato (CONTEXT.md §6): esta seção cria df_bruto.

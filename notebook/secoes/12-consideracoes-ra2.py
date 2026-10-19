#> Seção do notebook: RA2 — 12. Considerações do RA2
#> Área responsável: A · Tarefa: T07 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ## 12. Considerações do RA2
#
# Responda brevemente:
#
# - O que foi possível observar com o processamento em streaming?
# - Qual foi a contribuição das janelas temporais para a análise?
# - Essa abordagem faria sentido em uma aplicação real do projeto? Por quê?
#
# Na última resposta, o grupo pode reconhecer que o streaming foi utilizado apenas como exercício didático, se esse for o caso.

# %% [markdown]
# **Resposta do grupo:**
#
# **O que observamos com o streaming.** A consulta processou cada lote assim que ele chegou à pasta monitorada, sem reler os anteriores: o total recebido passou de 30 para 60 e depois para 90 reproduções, e a tabela mudou a cada lote (seção 11, células "Segundo lote: atualização de uma janela existente e abertura de novos intervalos" e "Terceiro lote: novas reproduções e comparação das contagens acumuladas"). Um lote novo pode atualizar uma janela já exibida, como 10:05–10:10, que foi de 14 para 17, e abrir janelas novas, como 10:20–10:25, com 17. A janela 10:00–10:05 ficou em 16, porque nenhum evento novo caiu nela.
#
# **Contribuição das janelas temporais.** A janela tumbling de 5 minutos transformou um fluxo contínuo de eventos em intervalos comparáveis: em vez de um total único, cada intervalo mostra quantas reproduções cada gênero teve (seção 10). Como a janela usa o instante do evento, e não a hora de chegada do arquivo, um evento atrasado ainda é contado no intervalo certo. É isso que permite responder ao objetivo da seção 8: qual gênero concentra mais reproduções em cada intervalo.
#
# **Uso numa aplicação real.** Faria sentido com eventos reais de reprodução, por exemplo para a Deezer ou uma gravadora perceberem em minutos um gênero ou uma faixa ganhando audiência. Neste projeto, porém, o streaming foi um exercício didático: a API pública só oferece um retrato diário dos charts, sem fluxo de reproduções, e os eventos são simulados a partir do conjunto preparado do RA1, com semente fixa. Os números mostram o funcionamento do processamento, não a audiência real.

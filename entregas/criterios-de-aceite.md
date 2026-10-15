# Critérios de aceite — RA1 e RA2

> Definição de pronto das entregas. Cada tarefa do [plano](plano-de-tarefas.md) cita os IDs daqui. Os critérios saem dos enunciados ([ra1](../enunciados/ra1.md), [ra2](../enunciados/ra2.md)), dos templates do professor e da rubrica.

## 0. Protocolo para agentes de IA

1. **Condição de conclusão:** a tarefa só está concluída quando todos os critérios dela estiverem atendidos, cada um com evidência.
2. **Lista antes de começar:** crie uma lista de tarefas com um item por ID de critério do escopo.
3. **Evidência por critério:** seção e célula do notebook, arquivo, contagem real (ex.: "1.948 linhas, `df_bruto.shape`, seção 2"). "Feito" sem evidência não conta.
4. **Contagem por comando**, nunca por estimativa.
5. **Não encerre com itens abertos.** Se houver bloqueio real, diga qual critério está bloqueado e por quê.
6. **Verificação independente:** ao terminar, faça uma segunda passagem separada da escrita, percorrendo os IDs.
7. **Relatório final:** tabela `ID | status | evidência`.

## 1. RA1 — documento (template `Template_RA1_Data_Analytics.docx`) e notebook

Peso na rubrica entre parênteses.

### C1 — Problema e perguntas analíticas (20%)
- [ ] **C1.1** Contexto e problema: a situação investigada, quem é afetado e por que importa, em texto próprio.
- [ ] **C1.2** Objetivo e recorte: objetivo, período (data da coleta), unidade de análise (faixa) e limites do projeto.
- [ ] **C1.3** Pelo menos 3 perguntas P1…Pn **específicas** (medida, grupos e recorte), cada uma com os dados necessários e todos esses dados existindo na fonte.
- [ ] **C1.4** Viabilidade inicial: como os dados permitem investigar as perguntas e quais lacunas existem.

### C2 — Fontes e ingestão (compreensão 20% + ingestão 15%)
- [ ] **C2.1** Ficha da fonte completa: identificação; origem e acesso (Deezer, URL da API, data de acesso); formato e volume (JSON via API, registros aproximados, atributos); cobertura (data, país aparente da coleta); condições de uso.
- [ ] **C2.2** Relação com o problema: quais perguntas a fonte apoia e por quê.
- [ ] **C2.3** Ingestão por código no notebook (seção 2): endpoints, paginação, pausa entre chamadas, tratamento de erro da API; tabela "Procedimento de ingestão" com a célula de cada etapa.
- [ ] **C2.4** Retrato bruto gravado em `dados/brutos/AAAA-MM-DD/` com metadados (data, quantidade de chamadas, erros); o notebook lê do retrato por padrão (`BAIXAR_DA_API = False`).
- [ ] **C2.5** Resultado da ingestão: volume carregado (`df_bruto.shape`), local dos dados brutos, etapas manuais (se houver).

### C3 — Compreensão e qualidade (compreensão 20% + qualidade 35%)
- [ ] **C3.1** Unidade de observação ("uma linha representa…") e chave dos registros, com o limite de unicidade.
- [ ] **C3.2** Dicionário inicial: todos os atributos usados no projeto, com significado, tipo observado e domínio ou unidade.
- [ ] **C3.3** Exploração inicial no notebook (seção 3): quantidade de linhas e colunas, tipos, ausentes, estatísticas descritivas.
- [ ] **C3.4** Diagnóstico Q1…Qn com regra, resultado (quantidade e proporção, com denominador) e célula; cobre cada categoria do enunciado (ausentes, duplicados, tipos, formatos, inválidos, categorias, outliers) **ou** registra "não se aplica" com justificativa.
- [ ] **C3.5** Impacto: quais problemas comprometem o uso e quais têm prioridade.

### C4 — Limpeza e preparação (35%)
- [ ] **C4.1** Cada problema relevante do diagnóstico tem uma decisão D (tratar **ou** manter), ligada ao Q correspondente.
- [ ] **C4.2** Cada decisão tem justificativa e efeito ou perda (linhas e colunas afetadas).
- [ ] **C4.3** Cada decisão aponta a célula que a executa.
- [ ] **C4.4** Cada tratamento tem validação depois de executado (teste e resultado).
- [ ] **C4.5** Tabela "Resumo das intervenções" completa.

### C5 — Conjunto resultante
- [ ] **C5.1** Arquivo final identificado (`dados/preparados/faixas_preparadas.csv`), unidade de observação final e dicionário atualizado, com colunas em português.
- [ ] **C5.2** Tabela antes × depois com registros, atributos e pelo menos uma medida de qualidade (com denominador, se percentual).
- [ ] **C5.3** Verificações finais de tipos, domínios, ausências, duplicidade e integridade, executadas no notebook (ex.: `assert`).
- [ ] **C5.4** Limitações e pendências para o uso posterior.
- [ ] **C5.5** Nenhuma agregação analítica, indicador, visualização de resultado ou conclusão sobre as perguntas no RA1.

### C6 — Organização e reprodutibilidade (10%)
- [ ] **C6.1** Repositório e versão (URL e tag da entrega); ambiente (Python, bibliotecas e versões, `requirements.txt`).
- [ ] **C6.2** Localização dos artefatos: dados brutos, código, dados preparados, documentação.
- [ ] **C6.3** Passos de reprodução executáveis, com o resultado esperado de cada um.
- [ ] **C6.4** Verificação da reprodução registrada: data, responsável, ambiente e resultado de uma execução completa a partir do clone limpo.

### C7 — Referências e conferência
- [ ] **C7.1** Referências da fonte de dados, da documentação técnica e do material usado, no padrão "Autor. Título. Ano. Disponível em: URL. Acesso em: data."
- [ ] **C7.2** "Conferência da entrega" do template com todos os itens marcados de verdade.

### N — Notebook
- [ ] **N.1** Identificação preenchida: título, nomes dos integrantes (exatamente como no `CONTEXT.md`, seção 1) e descrição do problema. A turma não entra.
- [ ] **N.2** Todas as células executadas em ordem, sem erro, a partir de um ambiente limpo (contadores de execução em sequência).
- [ ] **N.3** Nenhum `[Preencha aqui.]` ou orientação entre colchetes sobrando.
- [ ] **N.4** Respostas do grupo curtas, com números tirados das saídas das células.

## 2. RA2 — notebook (seções 8 a 12)

- [ ] **S8.1** Objetivo: o que o grupo quer monitorar e que informação espera obter com o streaming.
- [ ] **S9.1** Cenário informado (A, simulação) e como os novos registros chegam.
- [ ] **S9.2** Leitura com `spark.readStream`, esquema explícito e eventos coerentes com o conjunto preparado do RA1 (faixas e gêneros reais).
- [ ] **S9.3** Recebimento demonstrado: pelo menos 3 lotes publicados em momentos diferentes, com a saída depois de cada um. (Processamento em streaming: 3,0.)
- [ ] **S10.1** Tipo de janela, duração, deslocamento (se sliding), operação de agregação e o que se calcula em cada intervalo.
- [ ] **S10.2** `window()` aplicada sobre o instante do evento, com modo de saída declarado. (Janelas temporais: 3,0.)
- [ ] **S11.1** Resultados depois de cada lote e interpretação de quais janelas mudaram e por quê. (Documentação e interpretação: 2,0.)
- [ ] **S11.2** Consulta encerrada (`consulta.stop()`) e pastas temporárias limpas.
- [ ] **S12.1** As três perguntas das considerações respondidas.
- [ ] **S.D** Roteiro da demonstração oral de 5 minutos, com quem fala e qual célula mostrar. (Demonstração: 2,0.)

## 3. Regras gerais

- [ ] **X.1** Tudo em português do Brasil.
- [ ] **X.2** Nenhum commit com coautoria de IA (verificação "Verificar commits" verde na `main`).
- [ ] **X.3** Os quatro nomes da equipe (`CONTEXT.md`, seção 1), iguais na capa do documento e na identificação do notebook.
- [ ] **X.4** PDF do documento do RA1: capa preenchida, notas cinza e exemplos do template removidos, nenhum campo entre colchetes, tabelas legíveis ([orientações](orientacoes-documento-final.md)).
- [ ] **X.5** PDF do notebook (RA2): seções do RA1 e do RA2 organizadas, saídas visíveis e sem corte ([orientações](orientacoes-documento-final.md)).
- [ ] **X.6** Os mesmos números no documento, no notebook e na apresentação.
- [ ] **X.7** Declaração de uso de IA (se o grupo decidir incluir; ver [dúvida 6 do plano](plano-de-tarefas.md#8-dúvidas-em-aberto-para-o-grupo-decidir)).

## 4. Revisão cruzada (T12)

- [ ] **K.1** Toda pergunta P tem os dados necessários no dicionário (C3.2) e no conjunto final (C5.1).
- [ ] **K.2** Todo Q relevante tem um D; todo D aponta para um Q.
- [ ] **K.3** Os números do documento batem com as saídas do notebook executado.
- [ ] **K.4** As colunas usadas no RA2 existem no conjunto preparado.
- [ ] **K.5** O objetivo do RA2 (S8.1) conversa com o problema do RA1 (C1.1).
- [ ] **K.6** Nenhuma issue `pendencia-cruzada` aberta.
- [ ] **K.7** `python scripts/verificar_entrega.py` sem pendência.
- [ ] **K.8** Execução completa a partir de um clone limpo, registrada em C6.4.

# Roteiro da apresentação do RA1 e da demonstração do RA2

> O RA1 é avaliado na apresentação da equipe em sala ([enunciados/ra1.md](../enunciados/ra1.md), "Rubrica de avaliação"); o RA2 tem uma demonstração de 5 minutos só para a professora ([enunciados/ra2.md](../enunciados/ra2.md), seção 3). Todo número abaixo sai do notebook executado no Colab ou do PDF da entrega; a única exceção, o lote ao vivo, está marcada e explicada no fim.

**Páginas:** as do `output/entrega-ra2.pdf` (50 páginas): **p. 1–18 é o documento do RA1** (igual ao `output/entrega-ra1.pdf`) e **p. 19–50 é o notebook** executado (rodapé do notebook "1/32" a "32/32"; página do notebook = página do PDF − 18). O antigo `output/entrega-ra1-ra2.pdf` não existe mais: o equivalente é o `entrega-ra2.pdf`. As células são citadas pelo comentário-título, que é como aparecem no notebook.

**Ordem dos blocos (igual nas duas partes):** João Correa → João Pedro Cardoso → Eduardo Fabri → Rodrigo Alves. Cada um fala uma vez por parte, num bloco contínuo; o fechamento fica no bloco do Rodrigo.

---

## Parte 1. Apresentação do RA1

O enunciado não fixa a duração da apresentação do RA1. Os tempos abaixo são uma sugestão (cerca de 11 minutos), com mais tempo para qualidade e preparação, que vale 35%.

### Bloco 1 — João Correa (≈ 2 min)

**Critério:** problema e perguntas analíticas (20%).

**O que dizer:**
- Os charts da Deezer mostram as faixas mais ouvidas no geral e em cada gênero, mas só a ordem, não o que elas têm em comum.
- Problema: descrever o perfil das faixas do topo de cada gênero e ver se ele muda entre gêneros.
- Recorte: um único retrato dos charts, na data da coleta (16/10/2026); o chart é ao vivo e o projeto não acompanha a evolução.
- Unidade de observação: a faixa. Ela pode estar em mais de um chart; o gênero de comparação é o do chart em que aparece.
- Perguntas:
  - **P1:** como a duração das faixas varia entre os gêneros.
  - **P2:** que parte das faixas de cada gênero foi lançada nos 12 meses anteriores à coleta.
  - **P3:** se faixas de artistas com mais fãs têm `rank` mais alto, no geral e dentro de cada gênero.
  - **P4:** quantos artistas distintos ocupam cada chart de gênero e que fatia das posições fica com os 5 artistas com mais faixas.
- Viabilidade: todos os campos existem na API pública, sem autenticação (`duration`, `rank`, `position`, `artist.id`, `release_date`, `nb_fan`, gêneros).
- Limites: só as faixas dos charts, não o catálogo; sem número de reproduções, só o `rank`; `bpm` fica fora porque a API costuma devolvê-lo zerado.
- As respostas das perguntas ficam para a próxima etapa; o RA1 prepara os dados.

**Mostrar:**
- Documento, **p. 2** ("Contexto e problema", "Objetivo e recorte" e a tabela "Perguntas analíticas") e **p. 3** ("Viabilidade inicial").
- Notebook, **p. 19** ("Identificação do projeto" e seção 1, "Contexto e objetivo").

### Bloco 2 — João Pedro Cardoso (≈ 3 min)

**Critérios:** compreensão dos dados, parte da origem (20%); ingestão e reprodutibilidade (15%); organização, documentação e reprodutibilidade (10%).

**O que dizer — origem:**
- Fonte: API pública da Deezer (`https://api.deezer.com`), sem chave.
- Coletamos o chart geral e um chart por gênero da lista `/genre`.
- Cada item recebe o detalhe da faixa, do álbum e do artista, juntados pelo id.
- Retrato de 16/10/2026, de 21h03 a 21h41 UTC, com país aparente US:
  - 6.591 chamadas, 0 novas tentativas e 0 erros;
  - 28 charts (o geral e 27 gêneros) com 100 itens cada, que é o máximo que a API devolve.

**O que dizer — ingestão:**
- A ingestão é feita por código: pausa de 0,15 s, até 4 tentativas e tratamento do `error` que a API devolve com HTTP 200.
- Os charts são paginados por `index` e `limit=100`.
- As respostas ficam gravadas cruas em `dados/brutos/2026-10-16/`, com um `metadados.json`.
- Resultado: `df_bruto` com 2.800 linhas × 102 colunas, com 2.581 faixas, 2.292 álbuns e 1.688 artistas únicos, e nenhum item sem detalhe.

**O que dizer — reprodutibilidade e organização:**
- O notebook lê o retrato versionado por padrão (`BAIXAR_DA_API = False`), então toda execução repete os mesmos números. Coletar de novo é opcional e muda todas as contagens.
- O repositório é `github.com/eduardofabrii/data-analytics-ras` e tem:
  - o notebook já executado;
  - os dados brutos e preparados;
  - o dicionário do conjunto preparado;
  - o `requirements.txt` e o `README.md`.
- Reprodução em 4 passos: preparar o ambiente, obter os dados sem acessar a API, executar tudo e validar a saída.
- Verificação da reprodução:
  - Em 20/10/2026, um clone limpo rodou 47 células de código sem erro, em 14 s, e regravou o CSV idêntico ao versionado.
  - Em 21/10/2026 foi repetida no repositório da entrega, com o mesmo resultado.

**Mostrar:**
- Documento:
  - **p. 4** ("Ficha da fonte" e o início de "Procedimento de ingestão");
  - **p. 5** (etapas 2 a 7 e "Resultado da ingestão");
  - **p. 16** ("Localização dos artefatos" e "Passos para reprodução");
  - **p. 17** (passos 2 a 4 e "Verificação da reprodução").
- Notebook:
  - **p. 19**, célula "Preparação do ambiente: bibliotecas, pastas do projeto e origem dos dados";
  - **p. 20**, célula "Parâmetros da coleta e acesso à API";
  - **p. 22**, célula "Leitura do retrato bruto mais recente" (mostra "Retrato lido: dados/brutos/2026-10-16");
  - **p. 23**, célula "Metadados do retrato lido" (6591 chamadas, 0 erros, 28 charts);
  - **p. 24**, célula "Verificação do carregamento" (2800 linhas, 2581 faixas, 2292 álbuns, 1688 artistas, 0 sem detalhe).
- O repositório da entrega aberto no navegador, por 10 segundos, mostrando as pastas.

### Bloco 3 — Eduardo Fabri (≈ 2,5 min)

**Critérios:** compreensão dos dados, parte do que os registros representam e dos atributos (20%); qualidade e preparação, parte do diagnóstico (35%).

**O que dizer — o que é cada registro:**
- Uma linha é uma ocorrência de faixa num chart de origem: 2.800 ocorrências, 102 atributos, 2.581 faixas e 28 charts.
- O `id` da faixa se repete entre charts. A chave é o par chart e `id`, com 0 excedentes.
- A posição pertence ao chart, não à faixa.
- Dicionário inicial com os atributos que as perguntas e o RA2 usam:
  - `chart_id_genero` e `chart_nome_genero`, o grupo de todas as perguntas;
  - `duration`, `rank` e `position`;
  - `artist_id`;
  - `detalhe_faixa_release_date`;
  - `detalhe_artista_nb_fan`.

**O que dizer — diagnóstico (Q1 a Q21, sobre 2.800 ocorrências):**
- Nos campos das perguntas, a qualidade de origem é boa:
  - Q1, nenhuma ausência em campo essencial;
  - Q7, nenhum tipo divergente;
  - Q20 e Q21, a duração e o `rank` do chart são iguais aos de `/track`, todos com 0/2.800.
- **Q4:** 219/2.800 (7,82%) ocorrências excedentes por `id`. É a mesma faixa em charts diferentes, não uma duplicata, porque Q5 e Q6 dão 0.
- **Q15:** 100/2.800 (3,57%) são do chart geral, que não é um gênero.
- **Q16:** 11/2.800 (0,39%) têm o gênero do álbum genérico, por isso o gênero do álbum não substitui o do chart.
- **Q11:** 1/2.800, a faixa "Dirty Bird", tem lançamento em 28/10/2026, depois da coleta de 16/10. A causa não foi confirmada.
- **Q12:** 1/2.800 tem espaço nas pontas do nome.
- **Q17:** 143/2.800 (5,11%) durações estão fora do IQR (66,5 a 366,5 s; o observado vai de 41 a 2.120 s). Valor extremo não prova erro.
- **Q18:** 0/2.800 valores de `rank` fora do IQR.
- Problemas fora das perguntas:
  - **Q9:** `bpm` zerado em 1.890/2.800 (67,50%);
  - **Q3:** `title_version` vazio em 2.533/2.800 (90,46%);
  - **Q10:** `gain` zerado em 27/2.800;
  - **Q2:** 1 prévia ausente.
- A seção de diagnóstico não altera o `df_bruto`; as decisões vêm a seguir.

**Mostrar:**
- Documento:
  - **p. 6** ("Unidade de observação", "Identificação dos registros" e "Dicionário inicial dos dados");
  - **p. 7** ("Diagnóstico de qualidade", com o texto de Q11 e Q17);
  - **p. 8–9** (a tabela Q1–Q21 e "Impacto dos problemas identificados").
- Notebook:
  - **p. 27**, célula "Visão geral e tipos observados";
  - **p. 28**, célula "Duplicidade e limite da chave";
  - **p. 29**, células "Datas, formatos e categorias" e "Possíveis outliers e integridade do enriquecimento";
  - **p. 30–31**, célula "Diagnóstico de qualidade Q1 a Q21" (tabela com quantidade, denominador 2800 e percentual).

### Bloco 4 — Rodrigo Alves (≈ 3,5 min, com o fechamento)

**Critérios:** qualidade e preparação, parte do tratamento e da justificativa (35%); conjunto resultante e documentação do conjunto preparado.

**O que dizer — decisões D1 a D8, cada uma ligada a um Q:**

| Decisão | Ligada a | Ação e motivo | Impacto |
|---|---|---|---|
| D1 | Q4–Q6 | Uma linha por par chart-faixa. Excluir pelo `id` apagaria participações nas perguntas. | 2.800/2.800 mantidas; 219 excedentes por id preservadas |
| D2 | Q12 | Tira só os espaços das pontas e preserva acentos. | De 1/2.800 para 0/2.800 |
| D3 | Q11 | Converte a data sem mudar o valor e cria `lancamento_posterior_coleta`, para que a data futura não conte na P2. | 2.800 convertidas; 1 sinalizada |
| D4 | Q14–Q16 | Cria `tipo_chart` (geral ou genero). | 100 do geral identificadas; 2.700 de gênero |
| D5 | Q2, Q3, Q9, Q10 | Seleciona 12 dos 102 atributos e cria 4 de contexto ou qualidade. Prévia, versão, BPM e ganho ficam no bruto, sem imputar. | 16 colunas |
| D6 | Q7, Q8 | Dá nomes em português (`rank` fica como está, por causa do gerador do RA2). | 8 inteiros, 4 textos, 2 datas, 2 booleanos |
| D7 | Q17, Q18 | Sinaliza os extremos com `duracao_fora_limites_iqr` sem excluí-los, porque cortar mudaria a distribuição da P1. | 143/2.800 sinalizadas |
| D8 | Q1, Q13, Q19–Q21 | Mantém os valores aprovados e repete os testes. O `df_bruto` fica intacto. | 2.800/2.800 aprovadas |

- Nenhuma linha foi excluída e nenhum valor foi imputado.

**O que dizer — conjunto resultante:**
- `dados/preparados/faixas_preparadas.csv`: 2.800 registros, 16 atributos, 367.932 bytes.
- Chave `data_coleta`, `id_chart` e `id_faixa`, com 0 duplicatas.
- O conjunto tem um dicionário próprio, em `dados/preparados/dicionario-faixas.md`.
- Na comparação antes e depois, só mudam:
  - os atributos, de 102 para 16;
  - os espaços nas pontas, de 1 para 0.
- Registros (2.800), excedentes por id (219), chart geral (100), data futura (1) e extremos (143) se mantêm.
- O CSV relido é igual ao conjunto em memória: 2.800 linhas × 16 colunas, sem perda.

**Fechamento:**
- O retrato vale para um único dia e país aparente (US).
- A data futura e os extremos ficaram sinalizados para que a análise decida como tratá-los.
- No RA2, as 2.700 ocorrências dos charts de gênero alimentam os eventos simulados.

**Mostrar:**
- Documento:
  - **p. 10–13** (registro das decisões D1–D8);
  - **p. 13** ("Resumo das intervenções");
  - **p. 14** ("Conjunto de dados resultante" e a tabela "Comparação antes e depois");
  - **p. 15** ("Verificações finais" e "Limitações e pendências").
- Notebook:
  - **p. 32**, células "Preservação do vínculo entre faixa e chart" e "Padronização dos campos textuais";
  - **p. 33**, células "Conversão e validação temporal", "Identificação do chart de origem" e "Sinalização dos extremos de duração";
  - **p. 36**, célula "Verificações finais do conjunto preparado" ("Validações aprovadas em 2800 ocorrências");
  - **p. 36–37**, célula "Comparação antes e depois da preparação";
  - **p. 37**, célula "Gravação e releitura do conjunto preparado" (367.932 bytes; 2800 linhas × 16 colunas);
  - **p. 38**, seção 7, "Considerações do RA1", para o fechamento.

### Cobertura da rubrica

| Critério (peso) | Quem cobre | Onde está a evidência |
|---|---|---|
| Problema e perguntas analíticas (20%) | João Correa | Documento p. 2–3; notebook p. 19 |
| Compreensão dos dados (20%) | João Pedro (origem e fonte) e Eduardo (o que os registros representam e os atributos relevantes) | Documento p. 4 e p. 6–7; notebook p. 23–24 e p. 27–28 |
| Qualidade e preparação dos dados (35%) | Eduardo (problemas, Q1–Q21) e Rodrigo (tratamento e justificativa, D1–D8, conjunto resultante) | Documento p. 7–15; notebook p. 29–37 |
| Ingestão e reprodutibilidade (15%) | João Pedro | Documento p. 4–5; notebook p. 19–24 |
| Organização, documentação e reprodutibilidade (10%) | João Pedro (repositório, artefatos, passos e verificação da reprodução); Rodrigo cita o dicionário do conjunto preparado | Documento p. 14 e p. 16–17; repositório da entrega |

---

## Parte 2. Demonstração do RA2 (até 5 minutos)

Antes de começar, o notebook já está executado até a célula **"Terceiro lote: novas reproduções e comparação das contagens acumuladas"**, inclusive. O encerramento da seção 11 ainda **não** foi executado (ver Parte 3).

| Tempo | Quem | O que fazer e dizer | Célula (página do PDF) |
|---|---|---|---|
| 0:00–0:40 | João Correa | **Dizer:** no RA1, comparamos o perfil das faixas do topo entre gêneros. No RA2, queremos monitorar as reproduções dessas faixas por gênero ao longo do tempo: em cada janela, quantas reproduções cada gênero acumula e qual concentra mais. A API não tem um fluxo de reproduções, então usamos o cenário A, com eventos simulados a partir das faixas e dos gêneros do conjunto preparado. | Seção 8, "Resposta do grupo" (p. 39) |
| 0:40–1:50 | João Pedro Cardoso | **Fazer:** rolar pelas três células e parar na saída do recebimento. **Dizer:** `gerar_eventos` sorteia faixas e gêneros reais, com chance proporcional ao `rank`, semente 42, a partir de 21/10/2026 às 10:00, com 5 a 30 s entre eventos. `publicar_lote` grava o lote em JSON e só depois o move para `dados/streaming/entrada/`, a pasta que o `spark.readStream` monitora com esquema explícito. O 1º lote tem 30 eventos, de 10:00:28 a 10:09:05, de 19 gêneros. | Seção 9: "Gerador de eventos" (p. 41), "Leitura em streaming" (p. 42) e "Recebimento do 1º lote" (p. 43) |
| 1:50–2:50 | Eduardo Fabri | **Fazer:** mostrar a tabela da janela e o total. **Dizer:** é uma única janela tumbling de 5 minutos, sem sobreposição. Cada intervalo inclui o início e exclui o fim, então um evento às 10:05:00 cai em 10:05–10:10. A contagem é por `genero`, pelo `instante` do evento, em modo `complete` e com saída em memória. Depois do 1º lote: 16 reproduções em 10:00–10:05 e 14 em 10:05–10:10, num total de 30. | Seção 10: "Agregação por gênero em janela tumbling de cinco minutos" e "Tabela das janelas após o primeiro lote" (p. 44–45) |
| 2:50–3:40 | Rodrigo Alves | **Fazer:** mostrar os dois resumos "Mudanças por janela" já processados. **Dizer:** o total passa de 30 para 60 e depois para 90. O 2º lote atualiza uma janela que já existia (10:05–10:10, de 14 para 17) e abre 10:10–10:15 (18) e 10:15–10:20 (9). O 3º leva 10:15–10:20 de 9 para 16 e abre 10:20–10:25 (17) e 10:25–10:30 (6). A janela 10:00–10:05 fica em 16, porque nenhum evento novo cai nela. | Seção 11: "Segundo lote: atualização de uma janela existente e abertura de novos intervalos" (p. 46–47) e "Terceiro lote: novas reproduções e comparação das contagens acumuladas" (p. 47–49) |
| 3:40–4:30 | Rodrigo Alves | **Lote novo ao vivo.** **Fazer:** criar uma célula de código nova logo acima de "Encerramento da consulta e limpeza das subpastas da simulação", digitar `publicar_proximo_lote(10);` e executar. O ponto e vírgula esconde a lista de eventos que a função devolve. Rolar até o fim da saída, em "Mudanças por janela". **Saída esperada:** "Lote 4 publicado: lote_004.json, 10 eventos, de 2026-10-21 10:26:20 a 2026-10-21 10:28:50" e "Após o lote 4: 100 reproduções recebidas." **Dizer:** os 10 eventos caem todos na janela **10:25–10:30, que vai de 6 para 16**; as outras ficam iguais (+0); o **total vai de 90 para 100**. A janela é escolhida pelo instante do evento, por isso uma janela já exibida recebe novas contagens. | Célula nova na seção 11, antes do encerramento |
| 4:30–4:50 | Rodrigo Alves | **Fazer:** executar o encerramento. **Dizer:** a consulta fica inativa ("Consulta ativa após o encerramento? False") e as subpastas da simulação são apagadas. Fechar com uma frase: a janela transforma um fluxo contínuo em intervalos comparáveis, e um evento atrasado ainda entra no intervalo certo. | "Encerramento da consulta e limpeza das subpastas da simulação" (p. 49); seção 12, "Considerações do RA2" (p. 50) |

Sobram 10 s de folga para a troca de quem fala.

---

## Parte 3. Antes do dia

- [ ] Abrir o notebook do repositório da entrega no Colab (*Arquivo → Abrir notebook → GitHub*, `eduardofabrii/data-analytics-ras`, `notebook/ra1-ra2-deezer.ipynb`).
- [ ] Executar o notebook antes de a apresentação começar, até a célula anterior ao encerramento da seção 11 ("Terceiro lote…"), inclusive.
  - No Colab, a instalação do PySpark ("Instalação do PySpark (só no Colab)") leva alguns minutos, então comece cedo.
  - Não execute "Encerramento da consulta e limpeza das subpastas da simulação" antes da demonstração.
- [ ] Deixar o PDF (`output/entrega-ra2.pdf`) aberto, com a página de cada bloco à mão:
  - Parte 1: p. 2, 4, 6, 10 e 14 do documento;
  - Parte 2: p. 39, 41, 44, 46 e 49.
- [ ] Deixar o repositório da entrega aberto numa aba, para o bloco do João Pedro.
- [ ] Fazer um ensaio cronometrado da demonstração, com 5 minutos ou menos, no ambiente em que ela será feita, incluindo o `publicar_proximo_lote(10);` ao vivo.
- [ ] Para repetir o ensaio do zero, executar de novo as seções 9, 10 e 11.
  - A semente é reiniciada na célula "Gerador de eventos".
  - Se alguém chamar `publicar_proximo_lote` fora da ordem, os horários e as contagens do lote ao vivo mudam.
- [ ] Depois do ensaio, deixar o notebook de novo no ponto de partida da demonstração. Ou seja, reexecutar as seções 9, 10 e 11 até "Terceiro lote…", sem a célula nova.

---

## Conferência deste roteiro

**Páginas do PDF conferidas** (`output/entrega-ra2.pdf`):
- Documento: p. 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 e 17.
- Notebook: p. 19, 20, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49 e 50.

**Células citadas**, conferidas pelo título no notebook executado no Colab:

| Seção | Células |
|---|---|
| Seção 2 | "Preparação do ambiente: bibliotecas, pastas do projeto e origem dos dados"; "Parâmetros da coleta e acesso à API"; "Leitura do retrato bruto mais recente"; "Metadados do retrato lido"; "Verificação do carregamento" |
| Seção 3 | "Visão geral e tipos observados"; "Duplicidade e limite da chave"; "Datas, formatos e categorias"; "Possíveis outliers e integridade do enriquecimento"; "Diagnóstico de qualidade Q1 a Q21" |
| Seção 4 | "Preservação do vínculo entre faixa e chart"; "Padronização dos campos textuais"; "Conversão e validação temporal"; "Identificação do chart de origem"; "Sinalização dos extremos de duração" |
| Seção 5 | "Verificações finais do conjunto preparado"; "Comparação antes e depois da preparação"; "Gravação e releitura do conjunto preparado" |
| Seção 9 | "Instalação do PySpark (só no Colab)"; "Gerador de eventos"; "Leitura em streaming"; "Recebimento do 1º lote" |
| Seção 10 | "Agregação por gênero em janela tumbling de cinco minutos"; "Tabela das janelas após o primeiro lote" |
| Seção 11 | "Segundo lote: atualização de uma janela existente e abertura de novos intervalos"; "Terceiro lote: novas reproduções e comparação das contagens acumuladas"; "Encerramento da consulta e limpeza das subpastas da simulação" |

**O que não está no PDF ou não foi confirmado:**
- **Lote ao vivo (lote 4):** os números (10 eventos, de 10:26:20 a 10:28:50; 10:25–10:30 de 6 para 16; total de 90 para 100) não estão no PDF, porque o lote só existe na hora.
  - Eles vêm de uma execução local do mesmo notebook, com a mesma semente, depois dos três lotes.
  - A sequência é determinística, então o Colab deve repetir os mesmos valores se o notebook for executado na ordem. Confirme no ensaio.
- **Duração da Parte 1:** o enunciado do RA1 não fixa um tempo; os tempos dos blocos são uma sugestão.
- **Instalação do PySpark no Colab:** "alguns minutos" não foi cronometrado.

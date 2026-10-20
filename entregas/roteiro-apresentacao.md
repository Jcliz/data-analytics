# Roteiro da apresentação do RA1 e da demonstração do RA2

> Tarefa T14 (geral). Critérios AP.1 e S.D ([critérios de aceite](criterios-de-aceite.md)). O RA1 é avaliado na apresentação da equipe em sala ([enunciados/ra1.md](../enunciados/ra1.md), "Rubrica de avaliação"); o RA2 tem uma demonstração de 5 minutos só para a professora ([enunciados/ra2.md](../enunciados/ra2.md), seção 3). Use os números do notebook executado da entrega (critério X.6).

**Páginas:** as do documento do RA1 (parte 1 do PDF único, 18 páginas, cada capítulo começando numa página nova). Confira de novo depois da execução final, que gera o documento outra vez; se algo mudar de página, ajuste aqui. As células do notebook são citadas pelo título, que é como aparecem no PDF.

## 1. Apresentação do RA1

Ordem da rubrica. Cada integrante apresenta a parte da sua área.

| Critério da rubrica (peso) | Quem fala | O que dizer | Mostrar |
|---|---|---|---|
| Problema e perguntas analíticas (20%) | João Correa | Os charts da Deezer mostram quais faixas estão no topo de cada gênero, mas não o que elas têm em comum. O projeto compara o perfil dessas faixas entre gêneros, num único retrato dos charts (a faixa é a unidade de observação). Perguntas: P1, duração por gênero; P2, parte das faixas lançada nos 12 meses antes da coleta; P3, `rank` × fãs do artista; P4, concentração de artistas em cada chart. Todos os campos existem na API; `bpm` ficou de fora por vir zerado com frequência. | Documento, p. 2–3 (seção 01 e tabela P1–P4) |
| Compreensão dos dados (20%) | João Pedro Cardoso e Eduardo Fabri | **João Pedro:** fonte é a API pública da Deezer, sem chave; retrato de 16/10/2026 (país aparente US), 6.591 chamadas sem erro, 28 charts de 100 itens (geral e 27 gêneros); `df_bruto` com 2.800 linhas e 102 colunas, 2.581 faixas, 2.292 álbuns e 1.688 artistas. **Eduardo:** uma linha é uma ocorrência de faixa num chart; a chave é o par chart-faixa (0 repetições), mas o `id` da faixa se repete 219 vezes entre charts; dicionário com os atributos usados pelas perguntas. | Documento, p. 4 (ficha da fonte) e p. 6 (unidade de observação e dicionário); notebook §2, célula "Verificação do carregamento" |
| Qualidade e preparação dos dados (35%) | Eduardo Fabri e Rodrigo Alves | **Eduardo:** 21 verificações (Q1–Q21) sobre 2.800 ocorrências; nos campos das perguntas, nenhuma ausência nem divergência (Q1, Q7, Q20, Q21 = 0); problemas fora delas: `bpm` zerado em 1.890 (67,50%) e `title_version` vazio em 2.533 (90,46%); 1 data posterior à coleta; 143 durações fora do IQR (5,11%). **Rodrigo:** decisões D1–D8, cada uma ligada a um Q: nenhuma linha excluída; vínculo faixa-chart preservado (D1); 1 espaço corrigido (D2); data futura sinalizada (D3); 100 ocorrências do chart geral identificadas (D4); 102 → 16 colunas (D5, D6); extremos sinalizados, não removidos (D7); validação final (D8). | Documento, p. 7–9 (diagnóstico e tabela Q1–Q21), p. 10–13 (decisões D1–D8 e resumo) e p. 14–15 (conjunto resultante e comparação antes e depois); notebook §3, célula "Diagnóstico de qualidade Q1 a Q21"; §5, célula "Comparação antes e depois da preparação" |
| Ingestão e reprodutibilidade (15%) | João Pedro Cardoso | A ingestão é por código: chamadas com pausa, novas tentativas e tratamento do `error` que a API devolve com HTTP 200; charts paginados; respostas gravadas cruas em `dados/brutos/2026-10-16/` com `metadados.json`. O notebook lê esse retrato por padrão (`BAIXAR_DA_API = False`), então qualquer execução repete os números; coletar de novo é uma opção, não uma necessidade. | Documento, p. 4–5 (procedimento de ingestão); notebook §2, células "Parâmetros da coleta e acesso à API" e "Leitura do retrato bruto mais recente" |
| Organização, documentação e reprodutibilidade (10%) | João Pedro Cardoso | Repositório público com tag `entrega`; dados brutos, preparados, notebook e documento versionados; notebook montado por seção (`scripts/montar_notebook.py`) e documento gerado do template (`scripts/gerar_docx_ra1.py`); quatro passos para reproduzir do zero, no Colab ou localmente. | Documento, p. 16–17 (localização dos artefatos e passos para reprodução); repositório no GitHub |

Fechamento (João Correa, 30 s): o conjunto preparado (`dados/preparados/faixas_preparadas.csv`, 2.800 × 16) é a entrada do RA2 e do RA3; mostrar o notebook §7, "Considerações do RA1".

## 2. Demonstração do RA2 (5 minutos)

Antes de começar, o notebook já foi executado até a célula anterior ao encerramento da seção 11 (ver seção 3 abaixo). Na demonstração, publica-se **um lote novo ao vivo** e a tabela da janela é mostrada mudando.

| Tempo | Quem fala | O que fazer | Célula do notebook |
|---|---|---|---|
| 0:00–0:45 | João Correa | Objetivo: monitorar as reproduções por gênero ao longo do tempo; cenário A, com eventos simulados a partir do conjunto preparado do RA1, porque a API não tem um fluxo de reproduções. | Seção 8, "Resposta do grupo" |
| 0:45–2:00 | João Pedro Cardoso | Como os eventos chegam: `gerar_eventos` sorteia faixas e gêneros reais (chance proporcional ao `rank`, semente 42, início 21/10/2026 10:00); `publicar_lote` grava o JSON e o move para a pasta que o `readStream` monitora. Mostrar o 1º lote: 30 eventos, de 10:00:28 a 10:09:05, 19 gêneros. | Seção 9, "Gerador de eventos", "Leitura em streaming" e "Recebimento do 1º lote" |
| 2:00–3:15 | Eduardo Fabri | Janela tumbling de 5 minutos, sem sobreposição (início incluído, fim excluído); contagem de reproduções por gênero pelo `instante` do evento; modo `complete` e saída `memory`. Tabela do 1º lote: 16 reproduções em 10:00–10:05 e 14 em 10:05–10:10. | Seção 10, "Agregação por gênero em janela tumbling de cinco minutos" e "Tabela das janelas após o primeiro lote" |
| 3:15–4:00 | Rodrigo Alves | Mostrar os dois lotes já processados: o total passa de 30 para 60 e depois para 90. O 2º lote atualiza uma janela já exibida (10:05–10:10, de 14 para 17) e abre 10:10–10:15 (18) e 10:15–10:20 (9); o 3º leva 10:15–10:20 de 9 para 16 e abre 10:20–10:25 (17) e 10:25–10:30 (6). A janela 10:00–10:05 fica em 16, porque nenhum evento novo cai nela. | Seção 11, resumos "Mudanças por janela" das células "Segundo lote: atualização de uma janela existente e abertura de novos intervalos" e "Terceiro lote: novas reproduções e comparação das contagens acumuladas" |
| 4:00–4:45 | Rodrigo Alves | **Lote novo ao vivo:** numa célula nova, logo antes do encerramento, digitar e executar `publicar_proximo_lote(10);` (o ponto e vírgula esconde a lista dos eventos devolvida pela função). Os 10 eventos caem todos na janela 10:25–10:30, que vai de 6 para 16; o total passa de 90 para 100. Explicar que a janela é escolhida pelo instante do evento, por isso uma janela já exibida recebe novas contagens. | Seção 11, célula nova antes de "Encerramento da consulta e limpeza das subpastas da simulação"; olhar o resumo "Mudanças por janela" da saída |
| 4:45–5:00 | Rodrigo Alves | Encerrar a consulta: a consulta fica inativa e as subpastas da simulação são apagadas. | Seção 11, "Encerramento da consulta e limpeza das subpastas da simulação" |

## 3. Antes do dia

- [ ] Notebook executado no ambiente da apresentação (Colab ou máquina de quem apresenta) até a célula anterior ao encerramento da seção 11. No Colab, a instalação do PySpark leva alguns minutos: rode antes de a apresentação começar.
- [ ] PDF único aberto na página de cada bloco (p. 2, 4, 6, 7, 10, 14, 16 do documento).
- [ ] Ensaio cronometrado da demonstração (até 5 minutos), no ambiente em que ela será feita, incluindo o `publicar_proximo_lote(10);` ao vivo. Para repetir o ensaio do zero, execute de novo as seções 9, 10 e 11.
- [ ] Páginas deste roteiro conferidas no PDF da execução final.

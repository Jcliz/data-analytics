# Instruções do projeto Data Analytics (para colar no claude.ai)

> Cole o bloco abaixo em **Projeto → Instruções do projeto** no claude.ai. Este arquivo só guarda o texto; ele não é aplicado sozinho.

```
Este projeto é o trabalho da disciplina Data Analytics (PjBL, BSI PUCPR, 2026): RA1 (ingestão e preparação dos dados) e RA2 (processamento em streaming com janelas temporais). O repositório oficial é Jcliz/data-analytics. A fonte de dados é a API pública da Deezer, a mesma do app rdsalvesPUC/dataaudio.

Antes de responder sobre o notebook, o documento do RA1, os dados ou as decisões:
1. Consulte o CONTEXT.md do repositório (raiz). Ele resume entregas, fonte de dados, glossário, decisões, o contrato de variáveis entre as seções do notebook e o que ler para cada tarefa (seção 9).
2. Leia a issue da tarefa: ela traz os arquivos da área e os critérios de aceite (entregas/criterios-de-aceite.md).
3. Precedência: enunciados (enunciados/) > decisões (docs/adr/) > base de conhecimento (base/) > rascunhos. Não contradiga uma decisão; se algo pedir mudança, aponte a dúvida e onde ela surgiu.
4. O RA1 não tem análise: nada de indicadores, gráficos de resultado ou conclusões sobre as perguntas. Isso fica para o RA2 e o RA3.
5. Toda afirmação sobre os dados tem evidência (seção e célula do notebook, com a contagem e o denominador). Separe [Fato] de [Inferência] e cite fontes pelo número de base/fontes.md.
6. Código do notebook vai em notebook/secoes/NN-*.py (formato percent), nunca no .ipynb gerado. Respeite os nomes fixos: RAIZ, PASTA_BRUTOS, PASTA_PREPARADOS, PASTA_STREAMING, BAIXAR_DA_API, df_bruto, df_preparado, spark, consulta.
7. Commits: nenhum commit com Claude ou outra IA como coautor (sem Co-Authored-By de IA, sem Claude-Session). O autor é a pessoa do grupo.
8. Responda em português do Brasil.
```

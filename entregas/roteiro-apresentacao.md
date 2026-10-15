# Roteiro da apresentação do RA1 e da demonstração do RA2

> Tarefa T14 (geral). Critérios AP.1 e S.D ([critérios de aceite](criterios-de-aceite.md)). O RA1 é avaliado na apresentação da equipe em sala ([enunciados/ra1.md](../enunciados/ra1.md), "Rubrica de avaliação"); o RA2 tem uma demonstração de 5 minutos só para a professora ([enunciados/ra2.md](../enunciados/ra2.md), seção 3). Use os números do notebook executado da entrega (critério X.6). Apague os comentários `<!-- ... -->` quando o roteiro estiver pronto.

## 1. Apresentação do RA1

<!-- Um bloco por critério da rubrica, na ordem. Quem fala é quem fez a parte (plano de tarefas, seção 1). "Mostrar" aponta para a página do PDF único ou para a célula do notebook. -->

| Critério da rubrica (peso) | Quem fala | O que dizer | Mostrar |
|---|---|---|---|
| Problema e perguntas analíticas (20%) | [Área A] | [Problema, recorte e perguntas P1…Pn] | [Documento, seção 01] |
| Compreensão dos dados (20%) | [Área B e C] | [Origem dos dados, o que uma linha representa, atributos relevantes] | [Documento, seções 02 e 03] |
| Qualidade e preparação dos dados (35%) | [Área C e D] | [Problemas Q encontrados, decisões D e a justificativa de cada uma] | [Documento, seções 03 e 04; notebook, seções 3 e 4] |
| Ingestão e reprodutibilidade (15%) | [Área B] | [Como os dados são carregados e como reproduzir a coleta] | [Notebook, seção 2] |
| Organização, documentação e reprodutibilidade (10%) | [Área B] | [Estrutura do repositório e como rodar do zero] | [Documento, seção 06; repositório] |

## 2. Demonstração do RA2 (5 minutos)

<!-- A demonstração precisa mostrar o processamento de registros novos (critério "Demonstração", 2,0). Execute o notebook até a célula anterior ao encerramento da seção 11 (consulta.stop()), publique um lote novo ao vivo, mostre a tabela mudando e só então encerre. Ensaie com cronômetro. -->

| Tempo | Quem fala | O que fazer | Célula do notebook |
|---|---|---|---|
| 0:00–0:45 | [Área A] | [Objetivo da análise em streaming] | [Seção 8] |
| 0:45–2:00 | [Área B] | [Como os eventos simulados chegam; o 1º lote recebido] | [Seção 9] |
| 2:00–3:15 | [Área C] | [Janela, duração, deslocamento e agregação; tabela do 1º lote] | [Seção 10] |
| 3:15–5:00 | [Área D] | [Publicar um lote novo ao vivo; o que mudou na tabela e por quê; encerrar a consulta] | [Seção 11] |

## 3. Antes do dia

- [ ] Notebook executado no ambiente da apresentação (Colab ou máquina de quem apresenta) até a célula anterior ao encerramento da seção 11. No Colab, a instalação do PySpark leva alguns minutos: rode antes de a apresentação começar.
- [ ] PDF único aberto na página de cada bloco.
- [ ] Ensaio cronometrado da demonstração (até 5 minutos).

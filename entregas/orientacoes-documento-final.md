# Orientações do documento final (PDFs e envio)

> Como a entrega deve ficar antes de ir para o Canvas. Vale para pessoas e agentes. Prazo do RA1 e do RA2: **21/10/2026**.

## 1. O que vai na entrega

O RA1 e o RA2 vão **em arquivos separados** ([ADR-0011](../docs/adr/0011-entregas-separadas-e-repositorio-da-entrega.md), que substituiu o ADR-0009). O repositório citado no texto entregue é o da entrega, `https://github.com/eduardofabrii/data-analytics-ras`.

| Entrega | Arquivo | Fonte | Como gerar |
|---|---|---|---|
| **RA1:** documento do template do professor, com a URL do repositório da entrega na capa, **sem o notebook** | `output/ra1-documentacao.pdf` | `documentacao/ra1/` | seção 2 |
| **RA2:** PDF do notebook executado: identificação, RA1 (seções 1 a 5 e 7) e RA2 (seções 8 a 12) | exportado no Colab | `notebook/secoes/`, copiado para `notebook/ra1-ra2-deezer.ipynb` do repositório da entrega | seção 3 |

A tarefa do **RA1** só aceita URL (campo "Insira o URL da web"): o link do PDF do documento ainda será definido pelo grupo (repositório da entrega ou este, na tag `entrega`). O repositório da entrega é público; confira que a URL da capa abre numa janela anônima antes de enviar.

## 2. Documento do RA1 (do `.docx` ao PDF)

### Como gerar

```bash
python scripts/gerar_docx_ra1.py            # grava output/ra1-documentacao.docx (e .pdf, se houver LibreOffice)
```

Se não houver LibreOffice, abra o `.docx` no Word e use *Arquivo → Exportar → Criar PDF*. Ajustes visuais no Word (quebra de página, largura de coluna) são permitidos; **mudança de texto volta para o Markdown** e o documento é gerado de novo.

### Como deve ficar

- **Visual do template do professor:** capa com PUCPR, "RA1 — Ingestão e preparação dos dados", e as sete seções "RA1 / 01" a "RA1 / 07" na ordem, com os títulos originais.
- **Capa preenchida:** projeto, curso e período letivo (sem turma), professora Marina de Lara, equipe com os quatro nomes do `CONTEXT.md` (seção 1), repositório (URL) e entrega (Curitiba • 21/10/2026). Responsável pelo `.docx`: João Correa (área A, T11).
- **Sem declaração de uso de IA** (critério X.7): nem seção, nem nota, nem frase sobre assistentes de IA, no documento e no notebook. Decisão do grupo.
- **Sem citação da organização interna** (critério X.9): nada de área, tarefa, issue, PR, branch ou kanban no documento e no notebook; a evidência cita a seção, a célula ou o arquivo.
- **Nenhum campo entre colchetes** e nenhuma nota cinza de orientação ("COMO PREENCHER", "Exemplo de formulação", "LIMITE DESTA ENTREGA"…). O script remove as notas; os colchetes que sobrarem são campos não preenchidos.
- **Evidência em toda tabela:** a coluna "Evidência" cita o notebook pela seção e pelo título da célula (ex.: `notebook §3, célula "Duplicados por id"`) ou o caminho do arquivo. Não colar blocos de código no documento.
- **Números iguais aos do notebook executado** da entrega.
- **Decisões de limpeza:** um bloco por decisão (D1, D2…), todos com problema, tratamento, implementação e validação.
- **Conferência da entrega** marcada (☒) só no que estiver de fato atendido.
- **Anexos opcionais:** remova a seção se não houver anexo (basta não escrevê-la no Markdown).
- **Um capítulo por página:** cada seção "RA1 / 01" a "RA1 / 07" começa numa página nova, como no template, mesmo que a anterior termine no meio da página. Não junte capítulos para economizar páginas: o conteúdo corrido, com um capítulo começando logo abaixo do fim do anterior, fica difícil de ler. O gerador já faz isso.
- **Sem limite de páginas:** o documento pode ter quantas páginas precisar. O template tem 8 páginas, mas isso não é teto nem meta.

## 3. Notebook (`.ipynb` executado e PDF)

### Como gerar e executar

```bash
python scripts/montar_notebook.py            # gera notebook/projeto_data_analytics.ipynb
```

- **Copie o `.ipynb` gerado** para `notebook/ra1-ra2-deezer.ipynb` do repositório da entrega (os dois ficam iguais). A primeira célula de código da seção 2 clona esse repositório no Colab.
- **Colab (referência, gera o PDF do RA2):** abra o notebook do repositório da entrega (*Arquivo → Abrir notebook → GitHub*), *Ambiente de execução → Executar tudo* e, ao terminar sem erro, *Arquivo → Imprimir → Salvar como PDF*.
- **Local:** `jupyter nbconvert --to notebook --execute --inplace notebook/projeto_data_analytics.ipynb` e, para o PDF, `jupyter nbconvert --to webpdf --allow-chromium-download notebook/projeto_data_analytics.ipynb --output-dir output` (requer `pip install "nbconvert[webpdf]"`; na primeira vez a opção baixa o Chromium que o exportador usa).

### Como deve ficar

- **Identificação preenchida** no topo, com os campos do template: título, os quatro nomes da equipe como no `CONTEXT.md`, turma (curso e período, como na capa do documento) e descrição.
- **Ordem do template:** RA1 (seções 1 a 5 e 7) e RA2 (seções 8 a 12), com os enunciados do professor mantidos e as respostas do grupo no lugar de `[Preencha aqui.]`. A seção 6 não existe no template; não criar.
- **Todas as células executadas em sequência** (contadores 1, 2, 3…), sem erro e sem aviso vermelho sobrando.
- **Saídas legíveis no PDF:** tabelas com no máximo 10 a 20 linhas (`head`, `show(n=…, truncate=False)`); nada de imprimir o DataFrame inteiro ou JSON cru grande; linhas de código com até ~100 caracteres para não cortar na impressão.
- **Cada célula de código com um comentário de uma linha** dizendo o que faz; as células citadas no documento do RA1 começam com um título curto em comentário (ex.: `# Duplicados por id`), que é como o documento as referencia.
- **RA2:** a saída depois de cada lote aparece no PDF (não só a final), para mostrar a chegada de novos registros; início e fim da janela em colunas separadas. A célula do `%pip install` começa com `%%capture`, para a barra de progresso não sair no PDF.
- **Estrutura do template à risca:** nenhuma célula fora das seções do template (a preparação do ambiente é a primeira célula de código da seção 2); a célula do enunciado fica como o professor escreveu, e o texto do grupo vai só na resposta; a ordem de enunciado, código e resposta de cada seção é a do template.
- Para conferir localmente: `python scripts/exportar_notebook_pdf.py` grava `output/projeto_data_analytics.pdf`. O PDF enviado no RA2 é o do Colab.

## 4. Antes de enviar

1. `python scripts/verificar_entrega.py` sem pendência.
2. Revisão cruzada (T12) concluída, com a tabela `ID | status | evidência`.
3. Tag da entrega: `git tag entrega && git push origin entrega`, no commit da `main` que gerou o PDF enviado; a URL da capa aponta para o repositório.
4. Os dois PDFs abertos e conferidos página a página por alguém que não os gerou.
5. O notebook do repositório da entrega igual ao montado aqui; no RA2, o PDF do notebook exportado no Colab; no RA1, o link do PDF do documento, conferido numa janela anônima.

# Orientações do documento final (PDF único e envio)

> Como a entrega deve ficar antes de ir para o Canvas. Vale para pessoas e agentes. Prazo do RA1 e do RA2: **21/10/2026**.

## 1. O que vai na entrega

O RA1 e o RA2 vão **no mesmo arquivo** ([ADR-0009](../docs/adr/0009-entrega-unica-em-pdf.md)): um PDF único. Na tarefa do **RA2**, envie o arquivo. A tarefa do **RA1** só aceita URL (campo "Insira o URL da web"): envie o link do mesmo PDF no repositório, na tag `entrega`: `https://github.com/Jcliz/data-analytics/blob/entrega/output/entrega-ra1-ra2.pdf`.

| Parte do PDF único | Arquivo | Fonte no repositório | Como gerar |
|---|---|---|---|
| 1. Documento do RA1 (template do professor), com a URL do repositório na capa | `output/ra1-documentacao.pdf` | `documentacao/ra1/` | seção 2 |
| 2. Notebook executado: identificação, RA1 (seções 1 a 5 e 7) e RA2 (seções 8 a 12) | `output/projeto_data_analytics.pdf` | `notebook/secoes/` | seção 3 |
| **Arquivo da entrega (RA2: o arquivo; RA1: o link dele)** | **`output/entrega-ra1-ra2.pdf`** (versionado) | as duas partes acima | `python scripts/montar_entrega.py` |

No repositório (tag `entrega`) ficam também o `.docx`, o notebook `notebook/projeto_data_analytics.ipynb` executado e os dados. O repositório é público; confira que a URL da capa e o link do PDF abrem numa janela anônima antes de enviar.

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
- Tamanho de referência: o template tem 8 páginas; o documento preenchido deve ficar entre 8 e 15.

## 3. Notebook (`.ipynb` executado e PDF)

### Como gerar e executar

```bash
python scripts/montar_notebook.py            # gera notebook/projeto_data_analytics.ipynb
```

- **Colab (referência):** envie o `.ipynb` gerado, *Ambiente de execução → Executar tudo*; ao terminar sem erro, *Arquivo → Fazer download → .ipynb* e substitua o do repositório. Para o PDF: *Arquivo → Imprimir → Salvar como PDF*.
- **Local:** `jupyter nbconvert --to notebook --execute --inplace notebook/projeto_data_analytics.ipynb` e, para o PDF, `jupyter nbconvert --to webpdf --allow-chromium-download notebook/projeto_data_analytics.ipynb --output-dir output` (requer `pip install "nbconvert[webpdf]"`; na primeira vez a opção baixa o Chromium que o exportador usa).

### Como deve ficar

- **Identificação preenchida** no topo (título, os quatro nomes da equipe como no `CONTEXT.md`, descrição). A turma não entra.
- **Ordem do template:** RA1 (seções 1 a 5 e 7) e RA2 (seções 8 a 12), com os enunciados do professor mantidos e as respostas do grupo no lugar de `[Preencha aqui.]`. A seção 6 não existe no template; não criar.
- **Todas as células executadas em sequência** (contadores 1, 2, 3…), sem erro e sem aviso vermelho sobrando.
- **Saídas legíveis no PDF:** tabelas com no máximo 10 a 20 linhas (`head`, `show(n=…, truncate=False)`); nada de imprimir o DataFrame inteiro ou JSON cru grande; linhas de código com até ~100 caracteres para não cortar na impressão.
- **Cada célula de código com um comentário de uma linha** dizendo o que faz; as células citadas no documento do RA1 começam com um título curto em comentário (ex.: `# Duplicados por id`), que é como o documento as referencia.
- **RA2:** a saída depois de cada lote aparece no PDF (não só a final), para mostrar a chegada de novos registros; início e fim da janela em colunas separadas. A célula do `%pip install` começa com `%%capture`, para a barra de progresso não sair no PDF.
- Grave o PDF do notebook como `output/projeto_data_analytics.pdf`: é a parte 2 do PDF único.

## 4. PDF único

```bash
python scripts/montar_entrega.py             # junta as duas partes em output/entrega-ra1-ra2.pdf
```

- **Ordem:** documento do RA1 primeiro (a capa dele é a capa da entrega), notebook em seguida. Cada parte vira um marcador no leitor de PDF.
- O script recusa juntar se faltar uma parte e avisa se uma parte foi gerada antes da última mudança na sua fonte; nesse caso, gere a parte de novo.
- **Sem declaração de uso de IA** em nenhuma das partes (critério X.7).

## 5. Antes de enviar

1. `python scripts/verificar_entrega.py` sem pendência.
2. Revisão cruzada (T12) concluída, com a tabela `ID | status | evidência`.
3. Tag da entrega: `git tag entrega && git push origin entrega`, no commit da `main` que gerou o PDF enviado; a URL da capa aponta para o repositório.
4. PDF único aberto e conferido página a página por alguém que não o gerou.
5. `output/entrega-ra1-ra2.pdf` commitado na `main` antes da tag; no RA2, o arquivo enviado; no RA1, o link `https://github.com/Jcliz/data-analytics/blob/entrega/output/entrega-ra1-ra2.pdf`, conferido numa janela anônima.

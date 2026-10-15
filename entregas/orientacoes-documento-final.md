# Orientações do documento final (PDFs e envio)

> Como cada entrega deve ficar antes de ir para o Canvas. Vale para pessoas e agentes. Prazo das duas: **21/10/2026**.

## 1. O que vai em cada entrega

| Entrega | Envio no Canvas | Arquivos | Fonte no repositório |
|---|---|---|---|
| **RA1** | **URL** do repositório (tag `ra1-entrega`) | `notebook/projeto_data_analytics.ipynb` executado + `output/ra1-documentacao.pdf` (e `.docx`) | `notebook/secoes/`, `documentacao/ra1/` |
| **RA2** | **Arquivo PDF** | `output/projeto_data_analytics.pdf`: o notebook inteiro (RA1 + RA2) executado | `notebook/secoes/` |

O repositório é público; confira que a URL abre numa janela anônima antes de enviar.

## 2. Documento do RA1 (do `.docx` ao PDF)

### Como gerar

```bash
python scripts/gerar_docx_ra1.py            # grava output/ra1-documentacao.docx (e .pdf, se houver LibreOffice)
```

Se não houver LibreOffice, abra o `.docx` no Word e use *Arquivo → Exportar → Criar PDF*. Ajustes visuais no Word (quebra de página, largura de coluna) são permitidos; **mudança de texto volta para o Markdown** e o documento é gerado de novo.

### Como deve ficar

- **Visual do template do professor:** capa com PUCPR, "RA1 — Ingestão e preparação dos dados", e as sete seções "RA1 / 01" a "RA1 / 07" na ordem, com os títulos originais.
- **Capa preenchida:** projeto, curso (sem turma), professora Marina, equipe com os quatro nomes do `CONTEXT.md` (seção 1), repositório (URL) e entrega (Curitiba • 21/10/2026). Responsável pelo `.docx`: Eduardo Fabri (área A, T11).
- **Nenhum campo entre colchetes** e nenhuma nota cinza de orientação ("COMO PREENCHER", "Exemplo de formulação", "LIMITE DESTA ENTREGA"…). O script remove as notas; os colchetes que sobrarem são campos não preenchidos.
- **Evidência em toda tabela:** a coluna "Evidência" cita o notebook pela seção e pelo título da célula (ex.: `notebook §3 — "Duplicados por id"`) ou o caminho do arquivo. Não colar blocos de código no documento.
- **Números iguais aos do notebook executado** da entrega.
- **Decisões de limpeza:** um bloco por decisão (D1, D2…), todos com problema, tratamento, implementação e validação.
- **Conferência da entrega** marcada (☒) só no que estiver de fato atendido.
- **Anexos opcionais:** remova a seção se não houver anexo (basta não escrevê-la no Markdown).
- Tamanho de referência: o template tem 8 páginas; o documento preenchido deve ficar entre 8 e 15.

## 3. Notebook (`.ipynb` do RA1 e PDF do RA2)

### Como gerar e executar

```bash
python scripts/montar_notebook.py            # gera notebook/projeto_data_analytics.ipynb
```

- **Colab (referência):** envie o `.ipynb` gerado, *Ambiente de execução → Executar tudo*; ao terminar sem erro, *Arquivo → Fazer download → .ipynb* e substitua o do repositório. Para o PDF: *Arquivo → Imprimir → Salvar como PDF*.
- **Local:** `jupyter nbconvert --to notebook --execute --inplace notebook/projeto_data_analytics.ipynb` e, para o PDF, `jupyter nbconvert --to webpdf notebook/projeto_data_analytics.ipynb --output-dir output` (requer `pip install "nbconvert[webpdf]"`).

### Como deve ficar

- **Identificação preenchida** no topo (título, os quatro nomes da equipe como no `CONTEXT.md`, descrição). A turma não entra.
- **Ordem do template:** RA1 (seções 1 a 5 e 7) e RA2 (seções 8 a 12), com os enunciados do professor mantidos e as respostas do grupo no lugar de `[Preencha aqui.]`. A seção 6 não existe no template; não criar.
- **Todas as células executadas em sequência** (contadores 1, 2, 3…), sem erro e sem aviso vermelho sobrando.
- **Saídas legíveis no PDF:** tabelas com no máximo 10 a 20 linhas (`head`, `show(n=…, truncate=False)`); nada de imprimir o DataFrame inteiro ou JSON cru grande; linhas de código com até ~100 caracteres para não cortar na impressão.
- **Cada célula de código com um comentário de uma linha** dizendo o que faz; as células citadas no documento do RA1 começam com um título curto em comentário (ex.: `# Duplicados por id`), que é como o documento as referencia.
- **RA2:** a saída depois de cada lote aparece no PDF (não só a final), para mostrar a chegada de novos registros.
- Nome do arquivo enviado no RA2: `projeto_data_analytics.pdf` (ou o padrão que o professor pedir).

## 4. Antes de enviar

1. `python scripts/verificar_entrega.py` sem pendência.
2. Revisão cruzada (T12) concluída, com a tabela `ID | status | evidência`.
3. Tag da entrega do RA1: `git tag ra1-entrega && git push origin ra1-entrega`; a URL enviada aponta para a tag ou para a `main` no mesmo commit.
4. PDFs abertos e conferidos página a página por alguém que não os gerou.

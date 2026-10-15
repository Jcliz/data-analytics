---
id: qualidade-de-dados
titulo: "Qualidade de dados: o que verificar nesta base"
tipo: base
status: vigente
atualizado: 2026-10-15
fontes: [3, 5, 10, 11]
relacionados: [api-deezer, adr-0004]
---
# Qualidade de dados: o que verificar nesta base

## 1. O que o enunciado cobra

- Avaliar, **quando aplicável**: ausentes, duplicados, tipos incorretos, formatos inconsistentes, valores inválidos ou impossíveis, categorias inconsistentes, possíveis outliers e outros problemas [Fato, fonte 3].
- "Nem todos os conjuntos apresentarão todos esses problemas": discutir **os que forem relevantes** e justificar as decisões. "O objetivo não é aplicar a maior quantidade possível de técnicas" [Fato, fonte 3].
- O template pede registrar **também as verificações sem problema** e usar "não se aplica" com justificativa; e lembra que "um valor extremo, por si só, não justifica exclusão" [Fato, fonte 5].

## 2. Ciclo das aulas

Carregar → conhecer → inspecionar → identificar problemas → decidir → transformar → validar [Fato, fonte 10]. No RA1 o ciclo para no "validar": a etapa "analisar" do notebook de aula é dos próximos RAs.

Limpeza × transformação [Fato, fonte 11]: limpeza corrige (ausentes, duplicados, inválidos, formatos, inconsistências); transformação muda a forma (agregar, combinar, criar variáveis, mudar a granularidade). No RA1 entram só as transformações **de preparo** (renomear, converter tipo, juntar faixa com álbum, derivar ano de lançamento); agregações analíticas ficam para depois.

## 3. Verificações candidatas (área C escolhe e numera Q1…Qn)

| Problema | Campo | Regra de verificação | Tratamento possível (área D decide) |
|---|---|---|---|
| Duplicados | `id` | `df.duplicated("id")` depois de juntar os charts | Manter uma linha por faixa; guardar a lista de charts de origem em outra coluna |
| Ausentes | `preview`, `title_version`, `album.genre_id` | `isna()` e texto vazio | Manter (ausência informativa) ou marcar "desconhecido" |
| Valor inválido | `bpm`, `gain` | `== 0` | Converter para ausente (`NaN`), não excluir a faixa |
| Data inválida | `release_date` | não converte com `pd.to_datetime(errors="coerce")`, ou ano fora de 1900–2026 | Ausente; derivar `ano_lancamento` só quando válida |
| Tipo | `duration`, `rank`, `explicit_lyrics` | `dtype` diferente do esperado | Converter e validar a conversão |
| Formato | `title`, `artist.name` | espaços nas pontas, caixa diferente para o mesmo artista | `str.strip()`; comparar por `id` do artista, não pelo nome |
| Categoria | gênero | mesmo gênero com nomes diferentes, ou gênero "Todos" | Mapear para uma lista fechada |
| Outlier | `duration`, `rank` | IQR ou percentis; olhar os casos | Manter e documentar; excluir só se impossível (ex.: duração 0) |
| Integridade | `artist.id`, `album.id` | faixa sem artista ou sem álbum | Investigar; provavelmente "não se aplica" |

Cada linha que entrar no documento precisa da contagem real e da célula do notebook.

## 4. Antes × depois

O documento do RA1 (seção 05) pede a comparação "após ingestão" × "após preparação": registros, atributos e pelo menos uma medida de qualidade (ex.: duplicados pela chave `id`), com o denominador quando for percentual [Fato, fonte 5].

---

## Ligações

- **API:** [api-deezer](api-deezer.md) · **Material de aula:** [material-de-aula](material-de-aula.md)
- **Critérios:** [criterios-de-aceite](../entregas/criterios-de-aceite.md)

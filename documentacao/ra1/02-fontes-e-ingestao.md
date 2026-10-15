# Fontes de dados e ingestão

<!--
Área B (T02) · Critérios C2.1 a C2.5 · Leia: base/api-deezer.md, ADR-0001 e ADR-0004.
Evidência = notebook §2 + título da célula (ex.: notebook §2, célula "Coleta dos charts por gênero") ou caminho do arquivo.
Fonte única do projeto: F1 = API pública da Deezer (ADR-0001). O template pede uma ficha por fonte; aqui há uma só.
-->

## Ficha da fonte

**Identificação:** [F1 • nome do conjunto de dados]

**Origem e acesso:** [Deezer • https://api.deezer.com (documentação: https://developers.deezer.com/api) • data de acesso]

**Formato e volume:** [JSON via API REST • registros aproximados • atributos]

**Cobertura:** [Data da coleta • país aparente da requisição • charts incluídos]

**Condições de uso:** [API pública sem autenticação; dados da Deezer e dos detentores de direitos; uso acadêmico]

## Relação com o problema

[Indique quais perguntas esta fonte poderá apoiar e por quê.]

## Procedimento de ingestão

| Etapa | Procedimento ou parâmetro | Evidência no repositório |
|---|---|---|
| 1 | [Como os dados são obtidos] | [Arquivo ou célula] |
| 2 | [Leitura e parâmetros utilizados] | [Arquivo ou célula] |
| 3 | [Verificação do carregamento] | [Arquivo ou célula] |

<!-- Registre endpoints, index/limit da paginação, pausa entre chamadas e o tratamento do objeto "error". Sem tokens. -->

## Resultado da ingestão

[Informe o volume carregado, a localização dos dados brutos e eventuais etapas manuais necessárias.]

# Dados, schema e consultas

Leia esta referência quando a direção cria, altera, deriva, migra ou retém estado persistente.

## Ontologia do dado

Antes de discutir tabela ou coluna, esclareça:

- qual fato do domínio está sendo representado e quem é seu dono;
- fonte da verdade versus projeção, cache, snapshot ou evento;
- identidade, escopo de tenant e relações;
- estados válidos, transições, temporalidade e histórico necessário;
- ausência versus desconhecido versus não aplicável;
- autoria, proveniência, auditabilidade e explicabilidade;
- sensibilidade, finalidade, retenção, exportação e exclusão;
- quem lê, quem escreve e com qual consistência.

## Cenários que expõem o modelo

Inclua criação, correção, duplicata, concorrência, leitura antiga, backfill, exclusão, restauração, importação, reprocessamento e evolução de schema somente quando forem plausíveis. Para estado derivado, pergunte como detectar e reparar divergência da origem.

## Opções de modelagem

Compare modelos pelas invariantes e acessos que precisam sustentar, não por preferência estética. Exemplos de eixos legítimos: normalizado versus snapshot, evento versus estado atual, referência versus cópia histórica, cálculo na leitura versus materialização, campo estruturado versus payload extensível.

Para cada opção, torne explícitos:

- o que ela consegue garantir;
- consultas principais e volume/cardinalidade esperados;
- custo de escrita, leitura e operação;
- compatibilidade e caminho de evolução;
- comportamento durante migração e rollback;
- informação que se perde ou fica ambígua.

No debate, feche a semântica e as garantias. Índices, constraints, migrações expand/backfill/contract e queries exatas são trabalho do `/exiva` e `/pl`, guiados pelos acessos decididos aqui.

## Don’ts a derivar

Verifique se seria inaceitável perder autoria/histórico, misturar tenants, sobrescrever fonte da verdade, tornar estados inválidos representáveis, apagar dado necessário para auditoria ou reter dado sem finalidade. Não registre nenhum deles por reflexo; vincule cada um a cenário e impacto reais.

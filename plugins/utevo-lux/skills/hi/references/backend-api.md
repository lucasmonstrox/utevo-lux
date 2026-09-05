# Backend e API

Leia esta referência para endpoints, serviços, integrações, webhooks, jobs, eventos ou contratos entre sistemas.

## Atores e cenários

Considere como público o cliente da API, serviços chamadores, integrações externas, operadores, suporte, mantenedores e atores hostis. Modele o ciclo completo quando material:

- chamada válida e resultado observável;
- entrada inválida e erro útil;
- identidade válida sem autorização suficiente;
- duplicata, retry e idempotência;
- concorrência e ordem de eventos;
- timeout, indisponibilidade externa e falha parcial;
- volume grande, paginação/filtros e limites;
- compatibilidade de clientes durante evolução;
- operação, reconciliação e auditoria.

## Decisões de contrato

Explore alternativas somente onde mudam garantias ou consumidores:

- síncrono, assíncrono ou híbrido;
- recurso, comando, evento ou webhook;
- unidade de atomicidade e consistência percebida;
- formato de entrada/saída e semântica de ausência, `null`, default e erro;
- taxonomia de erros, retryability e idempotency key;
- paginação, ordenação, filtros e estabilidade do cursor;
- versionamento, compatibilidade e depreciação;
- ownership, autenticação, autorização e escopo do tenant;
- observabilidade e reconciliação de efeitos externos.

Pode esboçar de 2 a 3 contratos comportamentais comparáveis quando isso tornar a decisão concreta. Introduza uma hipótese por vez e compare somente os finalistas num passo posterior; mantenha os mesmos cenários em todos e não transforme o esboço em código final.

## Validação, consultas e performance

- Defina quais invariantes são validadas na borda e quais pertencem ao domínio ou ao armazenamento.
- Dê ao erro um consumidor e uma ação possível; “400 genérico” raramente fecha o cenário.
- Derive consultas dos acessos reais: cardinalidade, filtros, ordenação, consistência e frequência. Não prescreva índice ou cache sem workload.
- Troque “rápido” por orçamento ou ordem de grandeza quando performance puder decidir a opção: latência, throughput, payload, fan-out, volume e custo.
- Trate cache, batch, fila e denormalização como opções com invalidação, atraso e operação — não como virtudes automáticas.

## Don’ts típicos a investigar, não copiar

Procure efeitos duplicados em retry, autorização baseada apenas na UI, confiança em payload externo, erro que vaza segredo, mudança quebradora silenciosa, operação sem trilha e consulta sem limite. Só registre o que for plausível nesta tarefa.

## Não decidir aqui

Paths, nomes de funções, detalhes do framework, SQL final, testes e sequência de implementação pertencem ao `/pl`. O `hi` fixa as garantias que esses mecanismos terão de cumprir.

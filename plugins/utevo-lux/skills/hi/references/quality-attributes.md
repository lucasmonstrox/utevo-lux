# Atributos de qualidade

Leia esta referência quando um atributo não funcional puder eliminar uma opção ou mudar o produto. Não transforme todo debate numa lista universal de NFRs.

## Método

Para cada atributo material, defina:

1. cenário e público afetado;
2. condição observável ou orçamento;
3. consequência de falhar;
4. como comparar opções;
5. custo/trade-off aceito;
6. como saberemos depois se funcionou.

## Lentes possíveis

- **Performance:** latência percebida e de backend, throughput, payload, volume/cardinalidade, frequência, pico, custo e degradação. Use faixa ou ordem de grandeza quando número exato ainda exigir `/exiva`.
- **Confiabilidade:** disponibilidade necessária, consistência, perda tolerável, retry/idempotência, recuperação, RPO/RTO quando realmente aplicável e comportamento degradado.
- **Acessibilidade:** tarefas críticas sem mouse/visão/cor/áudio, ordem de foco, semântica, zoom, contraste e tecnologia assistiva. Não trate acessibilidade como polimento posterior da opção visual.
- **Privacidade:** finalidade, minimização, visibilidade, retenção, exclusão, exportação, consentimento e inferências sensíveis.
- **Observabilidade:** qual pergunta operacional precisa ser respondida, por quem, com logs/métricas/traces/eventos e sem vazar dados.
- **Manutenibilidade:** ownership, frequência de mudança, compatibilidade, capacidade de diagnosticar, superfície de configuração e custo de evolução.

Termos vagos não fecham decisão. `rápido`, `resiliente`, `acessível` ou `fácil de manter` devem ganhar cenário e evidência observável; o `/pl` depois define a prova executável aderente ao repositório.

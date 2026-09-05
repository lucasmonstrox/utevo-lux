---
name: pl
description: Transforma uma direção definida em plano de implementação com passos, dependências, critérios de aceite e verificações executáveis. Entrega na conversa, sem implementar ou criar documentação.
---

# Pl

Uso: `/pl <tarefa, brief ou investigação>`, ou a invocação de skills do agente.

Planeje o trabalho que `hunt` executará. Entregue o plano **na conversa**. Não crie documentos, pastas de planos, registros de features ou código.

## 1. Recuperar intenção e estado

Leia instruções locais, pedido e briefs/investigações disponíveis. Consulte documentação existente e código para confirmar premissas.

- Preserve decisões, restrições, opções rejeitadas e critérios estabelecidos.
- Confira o que está implementado. Algo pronto não vira tarefa de reconstrução; planeje só o que falta.
- Decisão de produto material aberta: esclareça uma por vez ou encaminhe a investigação para `exiva`. Não esconda investigação improvisada nos passos.
- Se faltar contexto indispensável, peça-o. Nenhuma outra skill precisa estar instalada.

## 2. Mapear dependências e impacto

Use busca conceitual/LSP disponíveis, ou `rg` e leitura direcionada. Leia contratos, schemas e dependências reais. Investigue a história quando ela explicar a área.

Identifique arquivos/símbolos a alterar, consumidores, referências dinâmicas, pré-requisitos, superfícies que podem regredir e comandos de verificação existentes.

Código como evidência usa arquivo/linha e, quando necessário, hash. Instruções de execução preferem arquivo/símbolo: linhas mudam. Não invente paths, comandos, tabelas ou serviços.

## 3. Escrever passos executáveis

Use [o formato do plano](templates/plano.md) como apoio. Adapte o tamanho ao trabalho; tarefa trivial não pede análise arquitetural extensa.

Cada passo declara intenção, resultado observável, arquivos/símbolos, dependências reais, restrições locais e prova (comando/ação → resultado esperado).

Não antecipe a implementação. Inclua snippets somente quando a forma exata for um contrato necessário.

- Prefira uma primeira fatia integrada que revele riscos cedo.
- Separe mudanças independentes. Divida passos grandes demais para verificar.
- Cole a regra importante junto ao passo que a usa, sem reproduzir o manual inteiro.
- Declare o que preservar, o que evitar e o que ficou fora.
- Mudança de dados distingue expansão, migração e remoção, com prova antes de cada transição.
- Não invente stubs para mascarar dependências. Se fizerem parte do desenho, explique contrato, substituição e o que permitem testar.

## 4. Planejar a verificação

A prova exercita a superfície alterada:

- UI: navegador real, erros relevantes, variantes, caminho principal, console e rede.
- API: request/handler real e efeitos; aguardar efeitos assíncronos quando existirem.
- Dados: schema e consultas que demonstrem integridade, transformação e compatibilidade.
- Lógica: teste que diferencie correto e incorreto, na infraestrutura existente.
- IA: casos que avaliem contrato e comportamento da saída, não só se o modelo respondeu.

Typecheck/lint complementam as provas. Um teste sem infraestrutura não pode aparecer como comando pronto: planeje o preparo necessário ou declare a limitação.

Inclua regressões dos consumidores e fechamento do caminho principal. Nomeie o que será testado; evite “adicionar testes” sem caso concreto.

## 5. Entregar o plano

Apresente na conversa objetivo, aceite, passos, riscos, verificações e pendências. Mostre o que impede executar antes de sugerir `hunt`.

Para risco operacional, explique rollback e o que não pode ser desfeito. Não force essa seção para ajustes triviais.

Outro agente consegue executar sem inventar decisões? Inclua o contexto que faltar na mensagem. Não crie arquivos de documentação ou status.

Em outra sessão, o usuário fornece o plano ou o contexto correspondente. Não presuma acesso à conversa anterior nem crie persistência por conta própria.

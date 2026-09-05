---
name: exura
description: Trata pedidos de mudança de um PR lendo descrição, issues, reviews e discussões completas. Corrige e testa cada change em um commit separado, atualiza o PR e responde ao comentário com o commit e a evidência. Use quando o usuário pedir para corrigir feedback ou requests changes de uma revisão.
---

# Exura

Uso: `/exura <URL ou número do PR> [--local]`.

O comando explícito pede o ciclo completo: ler os pedidos, corrigir, verificar, criar **um commit por change**, enviar os commits à branch do PR e responder às discussões de origem. `--local` prepara os commits e as respostas sem push nem publicação. Para pedidos em linguagem natural, respeite as ações autorizadas; a seleção automática da skill não amplia a autorização. Complete o trabalho local e prepare as respostas antes de pedir uma autorização de publicação que realmente falte; nunca peça novamente uma já concedida.

## 1. Ler o contexto inteiro

Leia [o protocolo de contexto do GitHub](references/github-pr.md) e reúna o mesmo material de `look`: descrição, issues vinculadas e seus comentários, specs/planos relevantes, commits, diff, reviews completas, comentários gerais, discussões inline com todas as respostas e checks.

- Registre a base e o head atuais, o repositório/branch de origem do PR e o estado da árvore local. Confirme que o PR está aberto e que a branch que será alterada é a dele, inclusive quando vier de um fork.
- Leia as instruções do repositório e os arquivos afetados. Leia a documentação de produto e o registro de features/impacto quando existirem; respeite o fluxo de busca das instruções locais.
- Não use apenas `reviewDecision` ou a última review. Leia o corpo dos **`CHANGES_REQUESTED`**, os pedidos em reviews `COMMENTED`, comentários gerais e threads, considerando respostas e decisões posteriores.
- Review antiga ou dispensada e thread resolvida são histórico; não reabra sem evidência de que o pedido permanece válido. `isOutdated` só indica que a posição ficou antiga: **não prova que o problema foi corrigido**.

## 2. Transformar feedback em uma fila de changes

Uma **change** é um pedido lógico e verificável de alteração. Um comentário com dois pedidos independentes gera duas changes; vários comentários sobre a mesma causa podem apontar para uma única change. Leia as respostas antes de decidir o que o revisor quis dizer.

Mantenha uma fila curta na conversa, reconstruível pelos comentários e commits do PR. Não crie documentação ou registros de features:

| Origem | Pedido | Estado | Commit | Verificação | Resposta |
|---|---|---|---|---|---|
| URL/ID do comentário, review ou item | Resultado esperado | pendente / corrigido / já atendido / esclarecimento / discordância / bloqueado | SHA quando existir | Prova ou limitação | URL publicada ou rascunho |

- Confirme cada pedido no código atual. Aplique uma correção que satisfaça a intenção e as regras do projeto, não necessariamente o patch sugerido literalmente.
- Já atendido: identifique a prova e o commit existente quando localizável; não crie commit vazio.
- Discordância: explique com evidência por que a sugestão quebra um contrato, contradiz um requisito ou não resolve o problema; não altere só para silenciar o comentário.
- Ambiguidade que muda comportamento: peça esclarecimento no canal autorizado e siga com changes independentes. Não responda pelo revisor nem declare o pedido resolvido.
- Diferencie sugestões opcionais de exigências; implemente as incluídas no pedido do usuário e não amplie o PR por conta própria.

## 3. Corrigir uma change por vez

1. Trabalhe sobre o head correto, em checkout limpo ou worktree próprio. Preserve arquivos e commits alheios; não faça stash, reset, rebase ou force-push para limpar o caminho silenciosamente.
2. Localize a causa e seus consumidores antes do patch. Uma correção em função compartilhada precisa cobrir os callers afetados. Siga as dependências entre changes sem misturar pedidos independentes.
3. Para bug ou lógica não trivial, obtenha uma prova que falhe antes e passe depois, preferindo o harness/teste existente. Para ajuste trivial, use a verificação proporcional; não crie testes que apenas repitam a implementação.
4. Faça a menor mudança que resolve o pedido e rode as verificações relevantes. UI exige navegador real. Não crie nem atualize documentação; se o pedido de review depender disso, declare o item pendente e explique a limitação.
5. Inspecione o diff e o staging. Faça **um commit desta change**, incluindo implementação e testes necessários. Não inclua changes independentes nem trabalho que já estava no workspace. Cada commit deve ser coerente e verificável.
6. Use a convenção do repositório, com o ID da feature quando aplicável. No corpo do commit, inclua `Review: <URL de origem>` (todas as origens se houver duplicatas) e a verificação executada. Grave o SHA real na fila.

Um comentário com vários pedidos pode receber vários links de commit. Um pedido que exige alterar vários arquivos continua sendo uma change. Não use amend ou squash para juntar changes distintas. Se uma change bloquear, registre o motivo e avance apenas nas independentes.

## 4. Atualizar o PR e responder

- Execute as verificações finais sobre o conjunto dos commits e a lista de impacto. Corrija falhas causadas pelo trabalho antes de anunciar sucesso; falhas preexistentes ou externas precisam de evidência e devem aparecer no resultado.
- Antes do push, releia o head remoto. Se ele avançou, preserve os novos commits, reconcilie sem reescrever histórico alheio e revalide o que mudou; nunca sobrescreva o head observado anteriormente. Envie apenas os commits esperados à branch de origem do PR, com push normal.
- Confirme que o PR contém os commits enviados. **Só então** responda a cada discussão com o link do commit e o resultado concreto da verificação. Se push falhar ou estiver em `--local`, mantenha rascunhos; não publique “corrigido” apontando para um commit que o revisor não consegue acessar.
- Responda a comentários inline na thread original. Pedidos no corpo de uma review ou comentário geral recebem resposta no PR com link direto para a origem e identificação do item; não abra uma discussão inline artificial.
- Para duplicatas, responda em cada origem apontando para o mesmo commit. Para “já atendido”, discordância ou esclarecimento, responda conforme a evidência, sem simular uma correção.
- **Deixe a thread aberta para o revisor conferir**, salvo pedido explícito para resolvê-la. Não descarte reviews, aprove o próprio trabalho ou faça merge.

Formato curto de resposta, adaptado ao idioma da discussão:

```markdown
Corrigido em [<SHA curto>](<URL do commit>): <o que mudou e como atende ao pedido>.
Verificação: <comando/cenário e resultado real; limitações, se houver>.
```

Antes de repetir qualquer publicação, consulte a thread e a fila: uma retomada ou timeout não pode duplicar resposta ou commit. Use [o protocolo compartilhado](references/github-pr.md) para distinguir IDs de reviews, comentários e threads e conferir o resultado da API.

## 5. Fechar a rodada

Releia o estado do PR, das discussões e dos checks para identificar changes ainda abertas, novos pedidos e interferências de outra pessoa. Corrigido no código, respondido no GitHub e aceito pelo revisor são estados diferentes.

Entregue a relação **pedido → commit → verificação → resposta**, incluindo já atendidos, discordâncias, bloqueios, novos pedidos e checks pendentes. Não anuncie “tudo resolvido” enquanto houver itens não tratados, publicação faltante ou verificação necessária inconclusiva.

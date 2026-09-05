---
name: hunt
description: Executa um plano de implementação em passos verificáveis, respeita dependências e demonstra o resultado no fluxo real. Use para executar um plano ou implementar uma tarefa definida.
---

# Hunt

Uso: `/hunt <plano ou tarefa definida>`, ou a invocação de skills do agente.

Execute o plano da conversa ou indicado pelo usuário. Não crie nem atualize documentação, wishlist, planos em arquivo ou registros de features. Progresso e resultados ficam na conversa.

## 1. Confirmar o ponto de partida

Leia instruções locais e documentação existente relevante. Confira `git status --short`, histórico recente e código da área. Preserve alterações e commits alheios.

- Já implementado e comprovado: reporte a evidência, sem reconstruir.
- Parcial: execute só o que falta, após conferir o estado real.
- Plano disponível: leia objetivo, aceite, dependências, passos e verificações.
- Sem plano: tarefa trivial e inequívoca pode seguir diretamente. Trabalho amplo ou com decisões abertas precisa de planejamento antes do código.
- Plano de outra sessão ausente: peça o conteúdo, não finja conhecê-lo.

Compare premissas com o repositório atual. Se alguma caiu, pare o passo afetado, explique a divergência e ajuste o plano na conversa antes de continuar.

## 2. Executar por dependência

- Mantenha o progresso na conversa. Atualize cada passo quando sua prova passar.
- Execute passos cujos pré-requisitos estejam atendidos; uma pendência bloqueia seus dependentes, não necessariamente tudo.
- Antes de editar, encontre origem e consumidores do comportamento. Use busca/LSP disponíveis, ou `rg` e leitura direcionada.
- Reutilize padrões e infraestrutura. Faça a menor mudança que atende ao plano, em fatias integradas e verificáveis.
- Releia os cuidados do passo antes de implementar. Não replique regras de outra stack nem introduza abstrações especulativas.
- Em migração de dados, prove a transição antes de remover o formato antigo.

Use comandos e versões reais do projeto. Testes novos verificam comportamento; ajustes triviais não pedem suíte artificial.

## 3. Tratar falhas

Teste ou análise falhou: registre o erro literal, localize o defeito e corrija a causa. Não faça mudanças aleatórias até ficar verde.

Duas tentativas com a mesma hipótese sem avanço pedem reavaliação: evidência nova, reprodução menor ou bloqueio explicado. Continue os passos independentes. Separe falha de infraestrutura de regressão do patch.

Não faça stash, reset, rebase, force-push nem limpe dados do usuário para facilitar a execução. Experimentos com outro estado Git usam checkout/worktree isolado.

## 4. Verificar

Leia [a matriz de verificação](verificacao.md). Cada critério do plano precisa de prova ou limitação explícita.

- Exercite o caminho real e rode os checks relevantes.
- Re-teste consumidores afetados.
- Revise o diff contra pedido e aceite. Use revisão independente quando disponível e autorizada; não finja outro revisor se a revisão foi própria.
- Falha não resolvida continua pendente. Typecheck verde não substitui prova de comportamento.

## 5. Entregar

Informe mudanças, verificações, resultados e pendências na conversa, com caminhos e evidências úteis.

Respeite a autorização da sessão para commits e ações remotas. Implementar sozinho não autoriza publicar PR, push, deploy ou merge. Quando autorizado a commitar, inclua só o trabalho desta tarefa e siga a convenção do projeto.

---
name: look
description: Revisa um PR contra sua descrição, issues vinculadas, discussões e regras do repositório. Investiga bugs, regressões e requisitos ausentes com evidências. Use para revisar PR, branch ou diff; para aplicar pedidos de revisão, use exura.
---

# Look

Uso: `/look <URL ou número do PR> [--publish]`. Também aceita uma referência Git e o escopo informado pelo usuário. Sem alvo, tente identificar o PR da branch atual; pergunte apenas se houver ambiguidade.

O entregável é uma revisão independente na conversa ou no PR, quando a publicação for solicitada. Não crie arquivos de documentação, execute o plano, altere código nem aplique os próprios achados. O `/hunt` executa o plano; o `/exura` trata correções solicitadas na revisão.

## 1. Entender o pedido e fixar o código revisado

- Para PR, leia [o protocolo de contexto do GitHub](references/github-pr.md). Carregue **descrição completa, issues vinculadas com seus comentários, reviews, discussões inline com respostas, commits e checks** antes de concluir o que foi pedido. `gh pr diff` e `gh pr view --comments` sozinhos não bastam.
- Registre repositório, PR, SHA da base, SHA do head e merge-base. Revise o diff `git diff <base-sha>...<head-sha>` e os commits dessa mudança; confirme que o checkout lido corresponde ao head. Preserve trabalho local usando um worktree separado quando necessário.
- Para uma revisão local, esclareça se o alvo é o intervalo de commits, as mudanças não commitadas ou ambos; capture o diff correspondente. Não inclua mudanças locais numa revisão de PR sem verificar que pertencem ao head remoto.
- Leia `AGENTS.md` aplicáveis aos arquivos, regras documentadas e as specs/planos citados. Leia a visão do produto e o registro de features/impacto quando existirem; use os comandos documentados pelo projeto.
- Faça um mapa breve dos critérios esperados e suas fontes. A descrição do PR explica a proposta; a implementação não prova que ela está correta. Uma divergência entre issue, descrição, plano e discussão precisa ser explicada, não resolvida por preferência do agente.
- Sem issue vinculada, use a descrição e os requisitos disponíveis. Fonte inacessível ou requisito ambíguo vira limitação localizada; continue o que puder revisar e não invente uma especificação.

## 2. Revisar por dois eixos

| Eixo | O que verificar |
|---|---|
| **Requisitos** | Critérios da issue/PR/plano atendidos, omissões, comportamentos incorretos e mudanças de escopo sem justificativa. Considere decisões registradas nas discussões. |
| **Correção e padrões** | Bugs e regressões no fluxo real, contratos entre consumidores, validação/autorização, integridade de dados, concorrência e erros, conforme a superfície alterada; regras documentadas do repositório. |

Leia as funções alteradas e o contexto necessário, incluindo consumidores, testes e configuração. Use a busca conceitual/LSP disponível e `rg` para confirmar aliases, strings e referências dinâmicas. Sem integração de busca, afunile com busca textual e leitura direcionada; não exija um MCP específico.

Siga cada suspeita até um cenário concreto: entrada/gatilho → caminho executado → resultado incorreto. Compare com a base para distinguir regressão introduzida ou agravada pelo PR de dívida preexistente. Um requisito inteiramente ausente também é achado, mesmo sem linha adicionada correspondente.

Duplicação, abstrações e nomes só justificam apontamento quando houver custo concreto ou violação documentada. Não imponha padrões arquiteturais pessoais nem crie achados para preencher cotas. Não repita comentários já abertos sobre o mesmo problema: vincule a discussão e informe se continua válido.

## 3. Verificar antes de afirmar

- Reproduza a suspeita ou sustente-a com uma cadeia de código inequívoca. Separe hipótese de defeito demonstrado; dúvida sem evidência fica como pergunta, não bloqueio.
- Execute checks relevantes à mudança e às suspeitas em ambiente isolado. Consulte os scripts reais do projeto. UI exige navegador real; API/dados exigem prova na superfície correspondente. Não transforme revisão em uma implementação de testes dentro do PR.
- Registre o que executou e o que não conseguiu executar. CI verde é evidência complementar; falha de infraestrutura não é automaticamente bug do PR.
- Relacione cada achado ao requisito ou regra aplicável e ao SHA revisado. Se não houver defeitos demonstráveis, diga isso sem inventar sugestões.

## 4. Entregar a revisão

Apresente os achados por gravidade, identificando o eixo de cada um. Um problema que afeta ambos aparece uma vez, com as duas etiquetas. Declare separadamente a cobertura de requisitos e a de correção/padrões para uma não esconder a outra.

Cada achado contém:

- **Prioridade e título concreto:** P0 crítico e imediato; P1 alto impacto; P2 defeito normal; P3 melhoria menor comprovadamente útil.
- **Local:** arquivo e menor intervalo suficiente no SHA revisado, ou referência ao requisito ausente.
- **Problema e impacto:** cenário que falha e consequência observável.
- **Evidência:** código, requisito/issue/comentário ou resultado de reprodução; direção de correção quando sustentada.

Finalize com critérios atendidos/pendentes/inconclusivos, verificações executadas e limitações. Recomende `REQUEST_CHANGES` para problemas que impedem aceitar o PR, `COMMENT` para dúvidas ou revisão inconclusiva e `APPROVE` somente quando o escopo estiver coberto e não houver bloqueios. A recomendação não equivale a uma review publicada.

## 5. Publicar quando solicitado

`--publish` ou pedido explícito de publicar/enviar a revisão autoriza a publicação. Caso contrário, entregue a revisão na conversa. Preserve autorização já dada; a seleção automática desta skill não autoriza mensagens no GitHub.

Antes de publicar, releia base/head, descrição e discussões. Se mudaram, revise o delta relevante, atualize posições e elimine achados já corrigidos ou duplicados. Publique uma review consolidada no SHA efetivamente revisado, com comentários inline onde houver linha válida e um resumo para achados sem âncora no diff. Use o protocolo compartilhado para payloads, respostas da API e prevenção de duplicatas.

No próprio PR, publique como `COMMENT`, mantendo a recomendação no texto; não tente aprovar ou solicitar mudanças formalmente em nome do próprio autor. Não faça merge nem invoque `exura` automaticamente. Se a API impedir a publicação, preserve o relatório pronto e informe o que falta.

Referência de desenho: [code-review de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md), especialmente a separação entre requisitos e padrões. Aqui a revisão inclui o contexto completo do PR e consolida achados duplicados.

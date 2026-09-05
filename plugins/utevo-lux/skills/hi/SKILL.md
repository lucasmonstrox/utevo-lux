---
name: hi
description: Amadurece uma ideia de software por debate estruturado, uma decisão por vez, até fechar intenção, público, cenários, precedentes, opções e trade-offs. Use para debater ou explorar uma ideia antes de pesquisar ou planejar; entregue o brief na conversa.
---

# Hi

Debata a ideia ou tarefa apresentada pelo usuário. Uso: `/hi <ideia>` (ou a invocação de skills do agente).

Leia primeiro as instruções locais (`AGENTS.md`, `CLAUDE.md` ou equivalentes) e a documentação de produto que elas indicarem. Resolva os links desta skill a partir da pasta do seu `SKILL.md`.

O resultado desta skill é uma **decisão entendida e confirmada**, não código nem plano de código. Debata até conseguir explicar o problema e a direção e entregue a síntese na conversa. Não crie nem atualize documentação, wishlist ou registros de features.

## Limites de altitude

- **`/hi` decide:** por quê, para quem, em quais cenários, qual comportamento queremos, quais opções existem, o que não pode acontecer e quais custos aceitamos.
- **`/exiva` prova:** estado real do produto/código, viabilidade, mercado, concorrentes, padrões e fatos externos com evidência. O `hi` pode fazer consultas focadas para destravar uma decisão; levantamento amplo pertence ao `/exiva`.
- **`/pl` operacionaliza:** arquitetura aderente ao repositório, paths, símbolos, contratos finais, passos, provas, testes e `Don't:` **de código** junto de cada função ou passo.
- **`/hunt` executa e verifica.** Não escreva código durante o `hi`.
- Code review é outra skill e está fora deste fluxo.

Não presuma que já existe algo para “melhorar”. Primeiro classifique a transformação: capacidade nova, mudança de comportamento, correção, redução de risco, manutenção/refactor, infraestrutura ou feedback para developers. Em greenfield, o baseline pode ser simplesmente “isso ainda não existe”; procure capacidades adjacentes e restrições, não invente um estado atual.

## Carregamento progressivo

Antes da primeira pergunta, identifique as superfícies e preocupações materiais. Leia **somente** as referências aplicáveis; combine mais de uma quando a tarefa cruza camadas.

- UI, fluxo, tela ou interação: [references/frontend-ui.md](references/frontend-ui.md)
- Endpoint, integração, serviço, webhook ou contrato: [references/backend-api.md](references/backend-api.md)
- Persistência, schema, migração ou consulta: [references/data.md](references/data.md)
- Infra, deploy, configuração, lint, CI ou developer experience: [references/infra-tooling.md](references/infra-tooling.md)
- Autenticação, autorização, dados sensíveis, dinheiro, endpoint público ou abuso plausível: [references/security.md](references/security.md)
- Performance, confiabilidade, acessibilidade, privacidade, observabilidade ou manutenibilidade material: [references/quality-attributes.md](references/quality-attributes.md)
- Ao chegar em precedentes, para qualquer superfície: [references/web-precedents.md](references/web-precedents.md)

Essas referências são menus de exploração, não checklists obrigatórios. Elimine uma pergunta se ela não muda decisão, risco, escopo ou critério de sucesso.

## Mecânica do debate — uma decisão por vez

Modele a conversa como uma **árvore de decisões**, mas nunca despeje a árvore no usuário. Só pergunte uma decisão quando suas premissas estiverem resolvidas; entre as disponíveis, escolha a de maior impacto e trate **somente ela**. Profundidade vem de vários passos curtos, não de muitas decisões na mesma resposta.

1. Preserve o pedido original como a semente. Extraia fatos declarados, preferências, restrições e termos vagos sem reinterpretá-los silenciosamente.
2. Mantenha um registro interno com `confirmado`, `provisório`, `rejeitado`, `hipótese factual` e `aberto`.
3. Cada passo contém **exatamente 1 pergunta e 1 decisão**. Faça a pergunta, dê contexto mínimo, recomende uma resposta e espere. Não avance, antecipe nem apresente as próximas decisões na mesma mensagem.
4. Fatos verificáveis são trabalho do agente. Inspecione fontes disponíveis ou rotule a hipótese; não transforme “como concorrentes fazem?” ou “isso já existe?” em pergunta de preferência ao usuário. Decisões de valor, prioridade e risco aceito pertencem ao usuário.
5. Se o usuário disser “você escolhe”, escolha, explique o critério e registre a decisão. Se a evidência não sustenta uma escolha, recomende experimento ou `/exiva`, não falsa certeza.
6. Questione premissas vagas ou contraditórias com cenários concretos. “Simples”, “rápido”, “intuitivo”, “seguro” e “melhor prática” só contam quando viram comportamento ou critério observável.
7. Não repita perguntas já respondidas. Uma resposta pode fechar vários ramos; descarte os que deixaram de importar.
8. Se uma pergunta contém dois eixos que poderiam receber respostas diferentes, ela está agrupada demais: divida. Configuração, superfície, automação, escopo e risco são passos separados quando cada um pode mudar sozinho.
9. Depois da resposta do usuário, registre a decisão **em silêncio** e vá direto à próxima pergunta. Não elogie, agradeça, diga “anotado”, repita a resposta, acrescente interpretação nem antecipe trade-offs. Só reflita a resposta quando houver ambiguidade, contradição ou uma interpretação que precise ser confirmada; nesse caso, faça apenas essa confirmação.
10. Não entregue resumo acumulado, mapa das próximas perguntas, IDs do repositório, dependências ou ramificações laterais enquanto não forem necessários para a decisão atual. Guarde tudo para a árvore interna e para a síntese final.

**Regra de hiperfoco:** cada mensagem de debate deve ser respondível olhando para uma única escolha. Mesmo que três decisões estejam prontas, faça uma agora e deixe as outras invisíveis até a resposta. Só agrupe se o usuário pedir explicitamente para receber tudo de uma vez.

**Regra de densidade:** escreva o mínimo necessário para o usuário entender e decidir corretamente — nem mais, nem menos.

- Corte preâmbulo, repetição, conclusão duplicada e explicação de processo. Não abra com “perfeito”, “brutal”, “entendi” ou “anotado”.
- Não recapitule a decisão anterior. Se a próxima pergunta depender dela, mencione somente a consequência indispensável.
- Contexto: no máximo 1 frase curta e apenas fatos que mudam esta escolha.
- Recomendação + motivo: preferencialmente 1 frase. Dê a conclusão e a razão decisiva, não todo o raciocínio.
- Alternativas são opcionais. Mostre somente opções reais, em uma linha cada; se exigirem muita explicação, apresente-as progressivamente.
- Não cite IDs, paths, dependências, benchmarks ou exemplos só para demonstrar pesquisa. Inclua-os apenas quando mudarem a decisão atual.
- Compacto não é superficial: se retirar uma informação puder mudar a escolha ou causar entendimento errado, mantenha-a. Se duas frases ensinam a mesma coisa, fique com a mais clara.
- Cada frase deve fazer pelo menos uma destas coisas: trazer um fato decisivo, distinguir opções, recomendar ou perguntar. Caso contrário, remova.

Formato preferido por mensagem:

```markdown
<contexto indispensável em 1 frase, se necessário>

**Pergunta:** <uma escolha que realmente muda a direção>

**Recomendo:** <resposta concreta>, porque <razão decisiva>.

<alternativas curtas, somente se necessárias para responder>
```

Após esse bloco, **pare e espere a resposta**. Não acrescente “e também precisamos decidir...” nem uma segunda pergunta disfarçada nas alternativas.

**Antipadrão `ack-recap`:** gastar o começo de cada mensagem celebrando, recontando ou analisando a resposta anterior. Isso não avança a decisão e se multiplica ao amadurecer várias ideias. O fluxo normal é `resposta do usuário → registro silencioso → próxima pergunta`.

## Ordem da ontologia

Siga esta ordem de dependência, voltando quando uma resposta invalidar uma premissa:

### 1. Intenção — por que mudar e qual transformação buscamos

Descubra o gatilho, dor ou oportunidade; o resultado que deve passar a ser possível ou verdadeiro; por que isso importa e por que agora. Não aceite uma solução sugerida como intenção (`“criar um modal”` ainda não diz qual resultado buscamos).

**Por que primeiro:** sem intenção, todo o resto otimiza uma solução sem saber qual mudança precisa produzir.

### 2. Público e atores — para quem e com quem

Mapeie quem recebe o valor e quem participa ou é afetado: usuário direto, beneficiário, comprador/decisor, operador, suporte, mantenedor, sistema consumidor, terceiro, pessoa afetada indiretamente, ator hostil e não-público. Para tooling/config, developers, CI e operadores são públicos legítimos.

**Por que agora:** o mesmo objetivo muda de forma conforme autoridade, conhecimento, frequência, contexto e incentivo do ator.

### 3. Cenários — quando e onde a intenção vira comportamento

Escreva cada cenário como `ator + gatilho + contexto + ação + resultado observável`. Cubra primeiro o cenário principal e depois somente os alternativos relevantes: erro, recuperação, borda, repetição/retry, concorrência, permissão, abuso e anti-use-case.

**Por que antes da solução:** cenários impedem uma ideia abstrata de parecer completa e revelam requisitos que uma tela feliz ou endpoint feliz esconderia.

### 4. Precedentes — quem já resolveu algo comparável

Faça uma **busca web obrigatória e atual** seguindo [references/web-precedents.md](references/web-precedents.md). Não use memória do modelo como evidência. Procure concorrentes, produtos análogos, padrões públicos, APIs maduras, bibliotecas e configurações consolidadas; combine com precedentes internos quando existirem. Um precedente é **evidência para pensar**, não uma decisão. Registre fonte, contexto, o que funciona, onde diverge do nosso público/cenário e classifique como `adotar`, `adaptar`, `rejeitar` ou `experimentar`.

**Por que depois dos cenários:** sem público e situação fixos, copiamos a aparência de uma solução feita para outro problema. O `/hi` sempre faz uma busca focada suficiente para decidir; pesquisa competitiva ampla, viabilidade profunda ou evidência inconclusiva seguem para `/exiva`.

### 5. Opções — maneiras realmente diferentes de satisfazer a intenção

Gere alternativas que mudem experiência, contrato, garantia, risco, custo ou reversibilidade; não conte microvariações cosméticas como opções. Inclua manter o estado atual quando isso for uma alternativa honesta e inclua experimento quando a incerteza for o ponto central. Compare todas contra os mesmos cenários e critérios.

**Por que depois dos precedentes:** opções passam a combinar evidência e contexto, em vez de reinventar ou copiar. Aqui se consolida **o quê** será feito e o **como comportamental**; mecanismos de código ficam para `/pl`.

### 6. Don’ts — o espaço de erro que precisa ficar explícito

Derive don’ts de falhas plausíveis descobertas nos cenários e opções. Separe:

- **invariante:** nunca pode ser violado;
- **fora de escopo:** não será resolvido nesta iniciativa;
- **anti-use-case:** comportamento que não queremos incentivar ou suportar;
- **atalho proibido:** caminho tentador já vetado por produto, segurança ou regra do repositório;
- **opção rejeitada:** decisão arquivada com motivo — não a trate como proibição eterna.

Cada don’t deve ser concreto, local e observável. Quando ajudar, use contraste mínimo `errado → desejado`. Não use cotas nem frases como “não quebrar nada”, “não ficar lento” ou “não ter bugs”; excesso de instruções vagas dilui as importantes.

Há duas camadas relacionadas, mas distintas:

| Camada | Pergunta que responde | Exemplo | Onde fica |
|---|---|---|---|
| **Don’t do debate** | Que comportamento, resultado ou fronteira o produto/sistema não pode cruzar? | “não enviar ao lead sem confirmação humana” | brief do `/hi` na conversa |
| **`Don't:` do plano** | Que erro de implementação esta função ou passo não pode cometer? | “o handler não envia mensagem; chama o service que aplica autorização e idempotência” | passo/função no `/pl` |

Um don’t do debate pode originar vários `Don't:` de código, mas não existe tradução mecânica nem relação obrigatoriamente 1:1. O `/pl` também acrescenta restrições técnicas vindas do repositório; não rebaixe o don’t comportamental a detalhe de código nem copie a mesma frase genericamente em todos os passos.

**Por que depois das opções:** comparar alternativas torna visíveis os atalhos e efeitos colaterais reais. Se um limite surgir antes, registre-o imediatamente e consolide aqui.

### 7. Trade-offs e decisão — qual preço aceitamos

Para cada finalista, explicite ganho, custo, risco, complexidade, reversibilidade, lock-in, impacto futuro e confiança da evidência. Trade-off é um custo **aceito conscientemente**; don’t é um limite que não pode ser trocado sem reabrir a decisão. Se um custo não é aceitável, descarte ou altere a opção.

Registre a opção escolhida, por que venceu, desvantagens aceitas, mitigação, confiança e gatilhos que justificariam revisitar a decisão.

**Por que por último:** trade-offs só existem entre opções concretas julgadas para um público e cenários conhecidos.

## Stress test e auditoria 5W1H

Antes da síntese final, ataque a direção escolhida com os cenários de erro, borda, recuperação, abuso e crescimento que forem materiais. Depois use 5W1H como **auditoria de cobertura**, não como roteiro mecânico:

- **Why:** a intenção e o valor estão claros?
- **Who:** públicos, atores técnicos, afetados e excluídos estão claros?
- **When / Where:** gatilhos, contextos e superfícies aparecem nos cenários?
- **What:** a transformação e o comportamento escolhido estão claros?
- **How:** o usuário/sistema percebe o funcionamento, sem fingir um plano de implementação?
- **Don’ts:** a fronteira negativa está explícita?

Não force uma resposta artificial para uma dimensão irrelevante. A auditoria deve encontrar lacunas, não preencher um formulário.

## Gate de entendimento compartilhado

Pare de abrir ramos quando:

- não restar decisão do dono que altere materialmente experiência, contrato, escopo ou risco;
- incertezas factuais restantes estiverem nomeadas e roteadas para lookup, experimento ou `/exiva`;
- direção, don’ts e trade-offs não se contradisserem;
- ideias futuras estiverem separadas do escopo atual.

Apresente então uma síntese compacta e completa no formato abaixo e peça confirmação explícita. Use uma linha por campo; expanda somente conflitos ou riscos que ainda possam mudar a decisão. Silêncio ou mudança de assunto não são confirmação. Se o usuário corrigir algo, atualize a árvore e faça um novo passo.

```markdown
## Brief de decisão

**Intenção:** ...
**Público e atores:** ...
**Cenários-chave:** ...
**Direção escolhida:** ...
**Precedentes:** ...
**Don’ts de produto/sistema e invariantes:** ...
**Trade-offs aceitos:** ...
**Fora de escopo / depois:** ...
**Como saberemos que funcionou:** ...
**Hipóteses e perguntas para `/exiva`:** ...
```

## Encaminhar

O brief confirmado fica na conversa. Hipóteses continuam rotuladas; não invente prioridade, urgência nem escopo aprovado.

Encaminhe perguntas factuais abertas para `exiva`; direção sustentada e pronta para codificar vai para `pl`. Se outra skill não estiver instalada, o brief deve permitir continuar sem ela. Não crie arquivos de documentação, instale skills nem invoque outra etapa automaticamente.

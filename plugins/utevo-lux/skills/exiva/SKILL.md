---
name: exiva
description: Investiga um problema de software com arqueologia de código e Git, pesquisa externa e verificação de evidências. Use para descobrir o que existe, avaliar viabilidade ou comparar abordagens antes de planejar.
---

# Exiva

Uso: `/exiva <tema ou pergunta>`, ou a invocação de skills do agente.

Investigue para responder ao pedido. Entregue a pesquisa **na conversa**; não crie nem atualize documentação, wishlist, registros de features ou código do produto.

## 1. Delimitar a investigação

Leia as instruções locais e a documentação de produto relevante, quando existir. Reaproveite o brief de `hi` se estiver disponível; preserve decisões, restrições e perguntas abertas. Sem brief, extraia esses pontos do pedido. Outra skill não é pré-requisito.

Classifique o esforço e informe o recorte:

| Escopo | Trabalho proporcional |
|---|---|
| Consulta | Um fato verificável com evidência suficiente. |
| Comparação | Opções concretas julgadas pelos mesmos critérios. |
| Tema amplo | Frentes que podem mudar a recomendação. |

Mantenha um brief curto: pergunta central, escopo, restrições e o que conta como respondido. Ambiguidade que muda a direção merece uma pergunta por vez; não pergunte fatos que você pode verificar.

Defina um orçamento proporcional de pesquisa. Delegue apenas frentes independentes quando houver ferramentas e autorização, com objetivo, limite e formato de evidência claros. Não exija provedor, modelo ou quantidade fixa de agentes.

## 2. Arqueologia interna

- Confira código, testes, schemas, migrações, dependências e histórico da área. Leia investigações e decisões existentes antes de repetir trabalho.
- Use busca conceitual/LSP disponíveis; sem eles, afunile com `rg`, busca de arquivos e leitura direcionada. Confirme referências dinâmicas, aliases e strings.
- Separe o que funciona, o que é parcial/mock e o que só aparece na documentação. Uma assinatura não prova comportamento completo.
- Rastreie consumidores e efeitos de contratos compartilhados. Confirme modelos no schema real; não deduza colunas pela interface.
- Use `git log -- <paths>`, `git log --follow -- <arquivo>` e `git log -S <termo> -- <paths>` quando a história explicar uma decisão.

Achados internos levam arquivo/linha lidos nesta sessão; cite o hash quando o histórico sustentar a conclusão. Fatos sobre dados levam consulta e contexto, sem expor segredos ou dados pessoais desnecessários.

Uma busca vazia não prova ausência. Teste outros termos, camadas ou representações. Hipótese já refutada só volta com evidência nova.

## 3. Pesquisa externa quando necessária

Pesquise quando a resposta depender de APIs, bibliotecas, mercado, regras ou fatos externos atuais. Consulta inteiramente interna não precisa virar levantamento de mercado.

- Derive buscas das perguntas abertas e dos atores afetados.
- Comece amplo e afunile; mude termos, idioma ou tipo de fonte quando necessário.
- Prefira documentação oficial, código-fonte, changelogs, issues e pesquisas primárias. Fontes secundárias ajudam a localizar ou complementar evidências.
- Leia a página real antes de usar uma afirmação decisiva. Snippet e memória do modelo não são prova.
- Confira compatibilidade, manutenção, licença, limitações e custo das opções quando importarem.
- Distinga inspiração de requisito: concorrente ter algo não demonstra que o projeto precisa disso.

Mantenha um registro compacto na conversa ou no raciocínio: respondido, falta verificar, próxima busca. Pare quando novos resultados deixarem de mudar a decisão ou o orçamento terminar; declare as lacunas.

## 4. Verificar e tentar refutar

Classifique afirmações decisivas como verificadas, refutadas, inferidas ou inconclusivas. Cite fonte e data de consulta para fatos que envelhecem.

Confronte números e alegações relevantes com fontes independentes quando possível. Vários textos repetindo um anúncio continuam sendo uma origem. Explique divergências entre fontes.

Tente demonstrar por que sua recomendação pode falhar: cenário adverso, custo oculto, incompatibilidade ou alternativa mais simples. Revisão independente pode ajudar quando disponível e autorizada; não invente problemas para preencher cotas.

Se a evidência invalidar a direção do brief, exponha o conflito e retome a decisão com o usuário. Não substitua a intenção em silêncio.

## 5. Entregar na conversa

Consulta simples: resposta, fonte e limite. Investigação ampla:

- recomendação e confiança;
- o que já existe, com evidências;
- opções e diferenças relevantes;
- lacunas, riscos e hipóteses refutadas;
- fontes decisivas próximas das afirmações;
- perguntas que ainda impedem decidir.

Não escreva um plano de implementação completo aqui. Com direção sustentada, ofereça `pl`; se indisponível, entregue o contexto para continuar. Não crie arquivos de relatório nem invoque a próxima etapa automaticamente.

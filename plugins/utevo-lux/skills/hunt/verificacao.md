# Verificação por superfície

Use a infraestrutura real do projeto. Não presuma linguagem, framework, banco, portas ou comandos de outro repositório.

| Superfície | Evidência |
|---|---|
| UI | Interação em navegador real, resultado visível, console e requests relevantes. |
| API | Rota/handler real, resposta e efeito. Aguardar condição observável para trabalho assíncrono. |
| Dados | Schema, consultas e integridade antes/depois. Dados de teste e restauração do estado criado pelo teste. |
| Lógica | Teste que diferencia comportamento incorreto e correto. |
| IA | Saída e ação contra critérios do produto. Rodar sem erro não prova resposta correta. |

Typecheck, lint e build complementam as provas. Descubra comandos no projeto.

Cubra erros e variantes relevantes e feche com o caminho principal. Não crie matriz exaustiva para ajuste pequeno.

Use a automação de navegador disponível. Com `agent-browser`: abrir → snapshot interativo → agir → observar resultado → conferir console/rede. Refaça snapshot quando refs expirarem. Feche só a sessão criada para o teste. Use DevTools para races e requests complexos quando disponível. Sem navegador, declare UI pendente.

Compare o diff completo com pedido e plano: omissões, mudanças fora de escopo e regressões. Outro agente pode revisar quando disponível e autorizado.

Relate resultados na conversa. Verificação não executada é limitação, não aprovação. Não salve relatórios de documentação.

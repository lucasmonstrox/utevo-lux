# Infra, configuração e tooling

Leia esta referência para deploy, runtime, rede, observabilidade, lint, formatação, build, CI, automação interna e developer experience.

## Público não é necessariamente cliente final

Mapeie developers, reviewers, CI, operadores, suporte, segurança, serviços dependentes e a pessoa de plantão. Diga quem recebe o benefício, quem paga o custo e quem mantém a solução.

Para uma regra de lint ou config nova, a transformação pode ser criar feedback ou impedir uma classe de erro que hoje não é detectada; não é necessário fingir uma feature existente.

## Cenários úteis

- execução local, CI, preview/staging e produção;
- primeira configuração e uso repetido;
- sucesso, warning, erro verdadeiro e falso positivo;
- falha parcial, retry, timeout e recuperação;
- rollout gradual, rollback e compatibilidade entre versões;
- credenciais ausentes/rotacionadas e permissões insuficientes;
- diagnóstico por alguém sem contexto da implementação;
- exceção legítima, bypass auditável e expiração da exceção;
- custo, quota, saturação e dependência de fornecedor.

## Opções e critérios

Compare prevenção versus detecção, enforcement local versus CI, erro versus warning, automação versus passo manual, managed versus self-hosted, síncrono versus fila/workflow e configuração central versus por workspace quando esses eixos forem materiais.

Julgue por tempo de feedback, determinismo, falsos positivos/negativos, blast radius, operabilidade, rollback, custo total, lock-in e ownership. “Mais rigoroso” não é automaticamente melhor se a equipe aprende a ignorar o sinal.

## Don’ts a investigar

Procure bypass silencioso, regra que só funciona numa máquina, segredo em config/log, deploy sem rollback, alerta sem dono, automação não idempotente e falha que bloqueia todo o workspace sem proporcionalidade. Registre apenas os riscos plausíveis e descreva o comportamento desejado em contraste.

## Não decidir aqui

Arquivo exato, comando final, provider API, configuração literal, sequência de rollout e prova executável pertencem ao `/exiva`/`/pl`. O `hi` decide a política, os públicos e as garantias operacionais.

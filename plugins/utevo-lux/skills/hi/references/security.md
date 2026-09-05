# Segurança e abuso

Leia esta referência quando houver identidade, autorização, dados sensíveis, dinheiro, endpoint público, webhook, upload, segredo, integração externa, ação privilegiada ou dano plausível.

O objetivo no `hi` não é executar uma auditoria completa; é impedir que a direção nasça sem modelo de abuso e sem invariantes de segurança. Pesquisa normativa ou técnica profunda pertence ao `/exiva`.

## Modelo mínimo

1. **Ativos:** o que precisa ser protegido — dado, dinheiro, disponibilidade, reputação, ação privilegiada ou segredo.
2. **Atores:** usuário legítimo, papel com privilégio diferente, serviço externo, insider, bot e atacante.
3. **Fronteiras de confiança:** onde identidade, tenant, payload ou origem deixam de ser confiáveis.
4. **Caminhos de abuso:** como a funcionalidade pode ser usada, repetida, forjada, enumerada, escalada ou combinada de maneira danosa.
5. **Impacto e postura de falha:** o que acontece quando não sabemos, quando dependência falha ou quando autorização é ambígua; fail closed versus continuidade degradada deve ser decisão consciente.

## Cenários a selecionar

Explore somente os relevantes: acesso cross-tenant, elevação de privilégio, replay/retry, enumeração, brute force/rate abuse, payload adulterado, SSRF/upload, exfiltração por log/erro, segredo exposto, automação induzida a agir, fraude, deleção indevida e ausência de trilha.

## Invariantes e trade-offs

Expresse limites observáveis: quem pode fazer o quê, em qual recurso, sob qual prova e qual evento precisa ser auditado. Diferencie autenticação, autorização e validação de origem. Menor privilégio, consentimento/finalidade, retenção e redaction entram quando conectados ao ativo real.

Segurança também tem trade-offs de fricção, disponibilidade, custo e suporte. Um trade-off aceito nunca deve ficar escondido atrás de “é seguro o suficiente”; registre ameaça tolerada, motivo, mitigação e gatilho de revisão.

Evite don’ts genéricos como “não expor dados”. Prefira contraste contextual, por exemplo: `aceitar tenant_id do payload → derivar o tenant da identidade autenticada`, somente se esse for de fato o contrato decidido.

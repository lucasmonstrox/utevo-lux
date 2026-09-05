# Diagnóstico quando o runtime é Bun

Confirme versão e scripts do projeto. Consulte a documentação antes de usar flags.

- Reproduza no teste/handler mais próximo. Confira opções com `bun test --help`.
- Filtre arquivo/nome do teste; repetição de casos intermitentes depende das opções da versão.
- Use o debugger suportado pelo Bun e o endereço informado pelo processo.
- Logs de fetch podem expor headers e corpos. Use dados de teste, remova credenciais da evidência e desative a instrumentação depois.
- Confira a cadeia de dependências com o comando disponível na versão.
- Suspeita Node/Bun: rode a mesma reprodução isolada nos runtimes relevantes. A diferença é evidência para investigar, não prova automática de culpa.

Fontes: [Bun](https://bun.com/docs), [compatibilidade Node.js](https://bun.com/docs/runtime/nodejs-apis). Verifique limitações atuais.

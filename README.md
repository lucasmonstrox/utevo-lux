<p align="center">
  <img src="plugins/utevo-lux/assets/logo.png" alt="Utevo Lux" width="172">
</p>

<h1 align="center">Utevo Lux</h1>

<p align="center">Skills de software inspiradas em Tibia. Da primeira conversa ao PR corrigido.</p>

```text
hi → exiva → pl → hunt → look → exura
                  bug ↗
```

| Skill | O que faz |
|---|---|
| [hi](plugins/utevo-lux/skills/hi/SKILL.md) | Debate a ideia, uma decisão por vez, até fechar o problema e a direção. |
| [exiva](plugins/utevo-lux/skills/exiva/SKILL.md) | Rastreia código, histórico e fontes para investigar com evidências. |
| [pl](plugins/utevo-lux/skills/pl/SKILL.md) | Prepara passos, dependências, critérios de aceite e verificações. |
| [hunt](plugins/utevo-lux/skills/hunt/SKILL.md) | Executa o plano e prova o resultado. |
| [bug](plugins/utevo-lux/skills/bug/SKILL.md) | Investiga a causa-raiz; corrige quando solicitado ou com `--fix`. |
| [look](plugins/utevo-lux/skills/look/SKILL.md) | Revisa PR, descrição, issues e discussões; aponta problemas demonstráveis. |
| [exura](plugins/utevo-lux/skills/exura/SKILL.md) | Corrige feedback de revisão, com um commit por mudança e resposta na origem. |

Use a etapa que o trabalho precisa. A sequência não é obrigatória, e `pl` mantém esse nome por enquanto.

Briefs, pesquisas, planos, progresso e relatórios ficam **na conversa**. As skills leem documentação existente, mas não criam nem atualizam docs, wishlist ou registros de features. Não exigem uma stack, sistema de IDs, MCP ou modelo específico.

## Instalar como skills — nomes curtos

No projeto em que deseja usar as skills, com Node.js 22.20+ e Git disponíveis:

```sh
npx skills add lucasmonstrox/utevo-lux --agent claude-code codex cursor --skill '*'
```

O instalador permite escolher o destino e o método. Para instalar em todos os seus projetos, acrescente `--global`. Para instalar apenas em um agente, deixe só seu nome depois de `--agent`.

Para escolher uma skill ou conferir o catálogo antes de instalar:

```sh
npx skills add lucasmonstrox/utevo-lux --list
npx skills add lucasmonstrox/utevo-lux --agent codex --skill exiva
```

No Claude Code e Cursor, use `/hi`, `/exiva`, `/pl` etc. No Codex, selecione a skill no seletor ou mencione `$hi`, `$exiva`, `$pl` etc. O formato de invocação é do agente; as instruções são as mesmas.

O instalador é o [Skills CLI da Vercel](https://github.com/vercel-labs/skills). Cada skill inclui suas referências e pode ser instalada separadamente.

## Instalar como plugin pelo marketplace

**Repositório** é onde os arquivos vivem. **Plugin** é o pacote das sete skills. **Marketplace** é o catálogo que indica onde encontrar esse pacote. Não é necessário criar um site ou servidor.

Este repositório fornece os catálogos dos três agentes, apontando para o mesmo pacote em `plugins/utevo-lux/`.

### Claude Code

Dentro do Claude Code:

```text
/plugin marketplace add lucasmonstrox/utevo-lux
/plugin install utevo-lux@utevo-lux
```

O primeiro `utevo-lux` identifica o plugin; o segundo, o marketplace. Escolha o escopo da instalação na interface e recarregue os plugins quando solicitado.

Plugins usam namespace no Claude: `/utevo-lux:hi`, `/utevo-lux:exiva` etc. Para manter `/hi` e os outros nomes curtos, use a instalação direta de skills acima. Evite instalar as duas formas no mesmo escopo se não quiser comandos duplicados. [Documentação oficial](https://code.claude.com/docs/en/plugins)

### Codex

No terminal, em uma versão com suporte a plugins:

```sh
codex plugin marketplace add lucasmonstrox/utevo-lux
codex plugin add utevo-lux@utevo-lux
```

Abra uma nova conversa e selecione a skill instalada. O catálogo fica em `.agents/plugins/marketplace.json`; o manifesto do pacote fica em `.codex-plugin/plugin.json`. [Plugins no Codex](https://learn.chatgpt.com/docs/build-plugins)

### Cursor

A instalação direta com `npx skills add` acima disponibiliza as skills no Cursor. Para testar o pacote como plugin local, clone o repositório e copie a pasta **`plugins/utevo-lux` inteira** para `~/.cursor/plugins/local/utevo-lux`, depois recarregue a janela e confira Customize.

O catálogo `.cursor-plugin/marketplace.json` prepara o repositório para distribuição como plugin. A listagem na loja pública do Cursor requer submissão e revisão; ter este repositório não significa estar listado nela. [Documentação oficial](https://cursor.com/docs/plugins)

## Uso

```text
/hi Quero melhorar o fluxo de cadastro
/exiva Compare as opções a partir do brief acima
/pl Planeje a direção que escolhemos
/hunt Execute o plano acima
/bug O formulário envia duas vezes --fix
/look https://github.com/owner/repo/pull/123
/exura https://github.com/owner/repo/pull/123
```

Adapte o prefixo ao modo de instalação. Uma nova sessão precisa receber o plano/contexto anterior: as skills não geram arquivos de memória.

`look` entrega a revisão na conversa; `--publish` ou pedido explícito autoriza publicar no PR. A invocação explícita de `exura` inclui corrigir, testar, commitar, enviar e responder; `--local` prepara os commits e rascunhos sem push nem comentários. Cada uma respeita as autorizações e ferramentas disponíveis.

Revisões no GitHub precisam de acesso pelo conector ou pela CLI `gh`. Pesquisas externas precisam de busca/web. Verificação de UI precisa de navegador real; indisponibilidade é declarada.

## Estrutura e manutenção

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
.cursor-plugin/marketplace.json
plugins/utevo-lux/
  .claude-plugin/plugin.json
  .codex-plugin/plugin.json
  .cursor-plugin/plugin.json
  assets/logo.png
  skills/{hi,exiva,pl,hunt,bug,look,exura}/SKILL.md
```

As sete skills têm uma única origem. Os três manifestos empacotam os mesmos arquivos. As referências do GitHub acompanham tanto `look` quanto `exura` para permitir instalação individual; o validador verifica que as duas cópias permanecem iguais.

Validação local:

```sh
python scripts/check.py
claude plugin validate .
claude plugin validate plugins/utevo-lux
```

Ao publicar uma atualização do plugin, incremente a versão nos três manifestos e nos catálogos que a declaram. Usuários de skills diretas podem usar `npx skills check` e `npx skills update`; usuários de plugins atualizam pelo agente.

Referências: [Agent Skills](https://agentskills.io/specification), [skills no Claude](https://code.claude.com/docs/en/skills), [skills no Codex](https://learn.chatgpt.com/docs/build-skills) e [skills no Cursor](https://cursor.com/docs/skills). A separação entre requisitos e correção em `look` se inspira no [code-review de Matt Pocock](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md).

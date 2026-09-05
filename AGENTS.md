# Utevo Lux

Coleção de sete skills de software, distribuída como Agent Skills e como plugin para Claude Code, Codex e Cursor.

- Fonte: `plugins/utevo-lux/skills/`. Nomes: `hi`, `exiva`, `pl`, `hunt`, `bug`, `look`, `exura`.
- As skills entregam briefs, pesquisa, planos e relatórios na conversa. Não adicionar criação/atualização automática de documentação nos projetos consumidores.
- Manter instruções portáveis: sem paths de projetos particulares, modelos obrigatórios, injeção de shell específica de harness ou dependências implícitas de outras skills.
- Referências devem permanecer dentro da pasta de cada skill, porque a instalação pode ser individual. As duas cópias de `references/github-pr.md` devem permanecer iguais.
- `pl` planeja; `hunt` executa; `look` revisa; `exura` aplica feedback. Não misturar responsabilidades ou ampliar autorizações remotas.
- Preservar os três formatos de manifesto e os catálogos. Não duplicar as skills por agente.
- Executar `python scripts/check.py` depois de mudanças; validar manifestos Claude com `claude plugin validate .` e `claude plugin validate plugins/utevo-lux` quando a CLI estiver disponível.

# Utevo Lux — agentes

## Visão do produto

Antes de criar, investigar ou alterar uma feature, leia a [visão do produto](docs/produto/visao.md). Ela define a filosofia do Utevo Lux, as 7 skills (hi, mission, equip, hunt, look, exura, bug), a exigência de portabilidade e os limites do repositório.

A collection of seven software skills, distributed as Agent Skills and as a plugin for Claude Code, Codex and Cursor.

- Source: `plugins/utevo-lux/skills/`. Names: `hi`, `mission`, `equip`, `hunt`, `bug`, `look`, `exura`.
- Keep all repository content in English: instructions, descriptions, references, templates and README.
- Skills deliver briefs, research, plans and reports in the conversation. Do not add automatic documentation, wishlist or feature-record creation or updates in consumer projects.
- Keep instructions portable: no private project paths, mandatory models, agent-specific shell injection or implicit dependencies on other skills.
- References must stay inside each skill's directory because skills can be installed individually. Keep both copies of `references/github-pr.md` identical.
- `equip` plans; `hunt` executes; `look` reviews; `exura` addresses feedback. Preserve their responsibilities and the scope of remote authorization.
- Preserve all three manifest formats and catalogs. Share the skill source across agents.
- Run `python scripts/check.py` after changes; validate Claude manifests with `claude plugin validate .` and `claude plugin validate plugins/utevo-lux` when the CLI is available.

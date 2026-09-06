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

<!-- code-intelligence:start -->
## Code search and impact analysis (required)

Use **CocoIndex, Serena and Graphify** according to the question. Run commands from this project root and verify the active MCP project. Internal clones and dependencies are outside the scope.

MCP clients: `.mcp.json` (Claude Code), `.cursor/mcp.json` (Cursor), and `.codex/config.toml` (Codex). Start the client from this repository root. Codex loads project settings only for trusted projects; verify the effective servers with `codex mcp list`.

| Question | Tool and approach |
| --- | --- |
| Concept, behavior, "where does X happen?" | **CocoIndex** MCP `search`, starting with `limit: 5`; narrow with `paths` and `languages`. |
| Known symbol, definition, class members | **Serena** `find_symbol`; `get_symbols_overview` for a file's symbols. |
| Who calls or references a symbol? | **Serena** `find_referencing_symbols`, using the definition's `name_path` and `relative_path`. |
| Dependencies, paths between modules, transitive impact | **Graphify** `query_graph`, `get_node`, `get_neighbors`, `shortest_path`; CLI `affected` for dependents. |
| Literal string, error, configuration, table name or dynamic dispatch | **`rg -n -F "text" path`**; use `rg -n "regex" path` for regular expressions. |
| Filename or extension | **`rg --files -g '*name*'`**; add `--hidden` for hidden configuration. |
| Schema, contract, migration, decision or documentation | **Targeted `rg`** followed by reading. Do not assume these are in the code index. |
| When or why did something change? | **Git**: `git log -- path`, `git blame path`, `git log -S 'text' -- path`. |

### CocoIndex — conceptual search

- Prefer the `cocoindex-code` MCP in `.mcp.json`; `.cursor/mcp.json` configures Cursor. Example: `search({query: "input validation", limit: 5, paths: ["scripts/**"]})`; adapt the path to the actual tree.
- CLI fallback: `ccc search --limit 5 "input validation"`; narrow with `--path 'scripts/**'` and `--lang python` or the relevant language. Add `--refresh` after changes since the last index update.
- `ccc status` checks the index; `ccc index` creates or incrementally updates it. MCP `search` refreshes by default. Do not use `ccc reset` for routine maintenance.
- Filters live in `.cocoindex_code/settings.yml`; local embeddings use Ollama `qwen3-embedding:0.6b`. An empty result does not prove the code is absent. Diagnose setup with `ccc doctor`.

### Serena — LSP symbols and references

- Start with `get_symbols_overview({relative_path: "scripts/check.py", depth: 1})` or `find_symbol({name_path_pattern: "Name", relative_path: "path", include_body: false})`.
- Read the needed definition with `find_symbol(..., include_body: true)`, then call `find_referencing_symbols({name_path: "Name", relative_path: "scripts/check.py"})`. Use paths returned by the tool, including class/method paths when applicable.
- Use `find_implementations` for interfaces/traits when available. References can be imports, types or registrations rather than calls.
- LSP configuration lives in `.serena/project.yml`. MCP clients use `.mcp.json` (`--context claude-code`) and `.cursor/mcp.json` (`--context ide`), in read-only mode. Diagnose with `serena project health-check .`.

### Graphify — structure and transitive impact

- The `graphify` MCP reads `graphify-out/graph.json`. Create it with `graphify extract . --code-only --no-cluster --max-workers 2`; code extraction uses local AST parsing without an LLM/API. Respect `.graphifyignore` and `.gitignore`.
- Explore with `graphify query "topic" --budget 2000`, `graphify explain "node"` and `graphify path "source" "target"`. MCP tools include `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `graph_stats` and `god_nodes`.
- **Blast radius:** `graphify affected "node-or-ID" --depth 3` follows reverse dependencies. Use an unambiguous ID/path from a query; narrow with `--relation calls` or `--relation imports_from` when appropriate.
- Refresh structural changes with `graphify update . --no-cluster`. If intentional deletions trigger the graph-shrink guard, review the diff before adding `--force`.
- Edges may be inferred; dynamic dispatch is not fully covered. Verify direction, relation and source evidence. A graph path does not prove runtime execution, and `--code-only` does not index all documentation.

### Blast radius / impact analysis workflow

1. Scope the change and locate the code with CocoIndex or Serena. Narrow each reading batch to at most three files; read the actual flow and relevant helpers before editing.
2. Query Serena references for every symbol being changed. For contracts, deletions, renames or shared dependencies, expand with `graphify affected` to the relevant transitive consumers.
3. Confirm exports/barrels, aliases, macros, convention-based routes, string-based jobs/events, RPCs, configuration and SQL with `rg`. **Zero indexed references does not mean zero impact.**
4. Identify direct consumers, transitively affected areas and tests that exercise those paths. Report unexpected or broad impact and update necessary consumers within the authorized scope.
5. Review `git diff`, `git diff --cached` and `git ls-files --others --exclude-standard`; include `git diff <base>...HEAD` for branch analysis. Repeat relevant queries and run the stack's checks and affected tests. Indexes and graphs do not replace compilers or tests.
6. Refresh affected indexes. If MCP, LSP, Ollama or the graph is unavailable, report the error, try its diagnostic/CLI and use `rg` plus reading as an explicit fallback. Never invent impact results. Reload the session after MCP configuration changes.
<!-- code-intelligence:end -->

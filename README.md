<p align="center">
  <img src="plugins/utevo-lux/assets/logo.png" alt="Utevo Lux" width="172">
</p>

<h1 align="center">Utevo Lux</h1>

<p align="center">Software skills inspired by Tibia. From the first conversation to the fixed PR.</p>

```text
hi → exiva → pl → hunt → look → exura
                  bug ↗
```

| Skill | What it does |
|---|---|
| [hi](plugins/utevo-lux/skills/hi/SKILL.md) | Discusses the idea, one decision at a time, until the problem and direction are settled. |
| [exiva](plugins/utevo-lux/skills/exiva/SKILL.md) | Finds answers in code, history, the web, and other sources; investigates with evidence. |
| [pl](plugins/utevo-lux/skills/pl/SKILL.md) | Prepares steps, dependencies, acceptance criteria, and verifications. |
| [hunt](plugins/utevo-lux/skills/hunt/SKILL.md) | Executes the plan and proves the result. |
| [bug](plugins/utevo-lux/skills/bug/SKILL.md) | Investigates the root cause; fixes it when asked or with `--fix`. |
| [look](plugins/utevo-lux/skills/look/SKILL.md) | Inspects the PR, its description, issues, and discussions; points out demonstrable problems. |
| [exura](plugins/utevo-lux/skills/exura/SKILL.md) | Heals the PR from review feedback, one commit per change, with a reply at the source. |

Use the step the work needs. The sequence is not mandatory, and `pl` keeps that name for now.

Briefs, research, plans, progress, and reports stay **in the conversation**. The skills read existing documentation but do not create or update docs, wishlists, or feature records. They do not require a specific stack, ID system, MCP, or model.

## Install as skills — short names

In the project where you want to use the skills, with Node.js 22.20+ and Git available:

```sh
npx skills add lucasmonstrox/utevo-lux --agent claude-code codex cursor --skill '*'
```

The installer lets you choose the destination and method. To install in all your projects, add `--global`. To install for a single agent, keep only its name after `--agent`.

To pick one skill or check the catalog before installing:

```sh
npx skills add lucasmonstrox/utevo-lux --list
npx skills add lucasmonstrox/utevo-lux --agent codex --skill exiva
```

In Claude Code and Cursor, use `/hi`, `/exiva`, `/pl`, etc. In Codex, select the skill in the picker or mention `$hi`, `$exiva`, `$pl`, etc. The invocation format belongs to the agent; the instructions are the same.

The installer is the [Vercel Skills CLI](https://github.com/vercel-labs/skills). Each skill ships with its references and can be installed separately.

## Install as a plugin from the marketplace

The **repository** is where the files live. The **plugin** is the package of the seven skills. The **marketplace** is the catalog that says where to find that package. No website or server is needed.

This repository provides the catalogs for the three agents, all pointing to the same package in `plugins/utevo-lux/`.

### Claude Code

Inside Claude Code:

```text
/plugin marketplace add lucasmonstrox/utevo-lux
/plugin install utevo-lux@utevo-lux
```

The first `utevo-lux` identifies the plugin; the second, the marketplace. Choose the install scope in the interface and reload plugins when prompted.

Plugins are namespaced in Claude: `/utevo-lux:hi`, `/utevo-lux:exiva`, etc. To keep `/hi` and the other short names, use the direct skill install above. Avoid installing both forms in the same scope unless you want duplicate commands. [Official documentation](https://code.claude.com/docs/en/plugins)

### Codex

In the terminal, on a version with plugin support:

```sh
codex plugin marketplace add lucasmonstrox/utevo-lux
codex plugin add utevo-lux@utevo-lux
```

Open a new conversation and select the installed skill. The catalog lives in `.agents/plugins/marketplace.json`; the package manifest lives in `.codex-plugin/plugin.json`. [Plugins in Codex](https://learn.chatgpt.com/docs/build-plugins)

### Cursor

The direct install with `npx skills add` above makes the skills available in Cursor. To test the package as a local plugin, clone the repository and copy the **entire `plugins/utevo-lux` folder** to `~/.cursor/plugins/local/utevo-lux`, then reload the window and check Customize.

The `.cursor-plugin/marketplace.json` catalog prepares the repository for distribution as a plugin. Listing in Cursor's public store requires submission and review; having this repository does not mean it is listed there. [Official documentation](https://cursor.com/docs/plugins)

## Usage

```text
/hi I want to improve the sign-up flow
/exiva Compare the options based on the brief above
/pl Plan the direction we chose
/hunt Execute the plan above
/bug The form submits twice --fix
/look https://github.com/owner/repo/pull/123
/exura https://github.com/owner/repo/pull/123
```

Adapt the prefix to your install mode. A new session needs to receive the previous plan/context: the skills do not generate memory files.

`look` delivers the review in the conversation; `--publish` or an explicit request authorizes publishing to the PR. Explicitly invoking `exura` includes fixing, testing, committing, pushing, and replying; `--local` prepares the commits and drafts without pushing or commenting. Each one respects the available authorizations and tools.

GitHub reviews need access through the connector or the `gh` CLI. External research needs search/web access. UI verification needs a real browser; unavailability is stated.

## Structure and maintenance

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

The seven skills have a single source. The three manifests package the same files. The GitHub references ship with both `look` and `exura` to allow individual installs; the validator checks that the two copies stay identical.

Local validation:

```sh
python scripts/check.py
claude plugin validate .
claude plugin validate plugins/utevo-lux
```

When publishing a plugin update, bump the version in the three manifests and in the catalogs that declare it. Direct-skill users can run `npx skills check` and `npx skills update`; plugin users update through their agent.

References: [Agent Skills](https://agentskills.io/specification), [skills in Claude](https://code.claude.com/docs/en/skills), [skills in Codex](https://learn.chatgpt.com/docs/build-skills), and [skills in Cursor](https://cursor.com/docs/skills). The split between requirements and correctness in `look` is inspired by [Matt Pocock's code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md).

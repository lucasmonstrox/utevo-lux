<p align="center">
  <img src="plugins/utevo-lux/assets/logo.png" alt="Utevo Lux" width="172">
</p>

<h1 align="center">Utevo Lux</h1>

<p align="center">Software skills inspired by Tibia. From the first conversation to the fixed PR.</p>

```text
hi → mission → equip → hunt → look → exura
                  bug ↗
```

<img src="plugins/utevo-lux/assets/hi-npc.gif" alt="Cipfried" width="20"> **[hi](plugins/utevo-lux/skills/hi/SKILL.md)** — Opens the dialog with the NPC: one decision at a time until the quest and the route are clear.

<img src="plugins/utevo-lux/assets/mission-scroll.gif" alt="Scroll" width="20"> **[mission](plugins/utevo-lux/skills/mission/SKILL.md)** — Takes the mission from the quest log: finds answers in code, history, and the web, with evidence.

<img src="plugins/utevo-lux/assets/magic-sword.gif" alt="Magic Sword" width="20"> **[equip](plugins/utevo-lux/skills/equip/SKILL.md)** — Gears up for the hunt: steps, dependencies, acceptance criteria, and verifications before anyone attacks.

<img src="plugins/utevo-lux/assets/hunt-dragon.gif" alt="Dragon" width="20"> **[hunt](plugins/utevo-lux/skills/hunt/SKILL.md)** — Attacks the code: executes the plan and loots the proof that it works.

<img src="plugins/utevo-lux/assets/look-golden-helmet.gif" alt="Golden Helmet" width="20"> **[look](plugins/utevo-lux/skills/look/SKILL.md)** — Looks at the item a friend found: PR, issues, and discussions; points out demonstrable problems.

<img src="plugins/utevo-lux/assets/exura-health-potion.gif" alt="Health Potion" width="20"> **[exura](plugins/utevo-lux/skills/exura/SKILL.md)** — Heals the PR wounded on the hunt: one commit per change, with a reply at the source.

<img src="plugins/utevo-lux/assets/bug.gif" alt="Bug" width="20"> **[bug](plugins/utevo-lux/skills/bug/SKILL.md)** — Tracks the bug to its lair and finds the root cause; slays it when asked or with `--fix`.

Use the step the work needs. The sequence is not mandatory.

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
npx skills add lucasmonstrox/utevo-lux --agent codex --skill mission
```

In Claude Code and Cursor, use `/hi`, `/mission`, `/equip`, etc. In Codex, select the skill in the picker or mention `$hi`, `$mission`, `$equip`, etc. The invocation format belongs to the agent; the instructions are the same.

The installer is the [Vercel Skills CLI](https://github.com/vercel-labs/skills). Each skill can be installed separately and ships with whatever files it references.

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

Plugins are namespaced in Claude: `/utevo-lux:hi`, `/utevo-lux:mission`, etc. To keep `/hi` and the other short names, use the direct skill install above. Avoid installing both forms in the same scope unless you want duplicate commands. [Official documentation](https://code.claude.com/docs/en/plugins)

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
/mission Compare the options based on the brief above
/equip Plan the direction we chose
/hunt Execute the plan above
/bug The form submits twice --fix
/look https://github.com/owner/repo/pull/123
/exura https://github.com/owner/repo/pull/123
```

Adapt the prefix to your install mode. A new session needs to receive the previous plan/context: the skills do not generate memory files.

`look` delivers the review in the conversation; `--publish` or an explicit request authorizes publishing to the PR. Explicitly invoking `exura` includes fixing, testing, committing, pushing, and replying; `--local` prepares the commits and drafts without pushing or commenting. Each one respects the available authorizations and tools.

GitHub reviews need access through the connector or the `gh` CLI. External research needs search/web access. UI verification needs a real browser; unavailability is stated.

## Evidence

Each skill instructs an agent to work a certain way. Those instructions are claims about how a model behaves, and most of them have been measured by someone.

This section collects the papers and benchmarks behind them, one entry per benchmark, grouped by skill. Each entry says what the benchmark measures, what it reports, which step of which skill relies on it, and where the finding stops holding. Every source listed here was opened and checked at the source, not recalled from memory.

### `hi`

<details>
<summary><b>Sharded instructions</b> — what does asking one question at a time cost?</summary>

**Used in** · [`hi` › Discussion mechanics](plugins/utevo-lux/skills/hi/SKILL.md#discussion-mechanics-one-decision-at-a-time) — one question and one decision per message, and the internal record of what is confirmed, provisional, rejected or still open.

**Benchmark** · [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120) — Laban, Hayashi, Zhou & Neville, 2025 (`arXiv:2505.06120`). 15 models across eight families, over 200,000 simulated conversations, six generation tasks, ten runs per combination.

**What it measures.** A fully specified instruction is cut into "shards" — the first carries the high-level intent, the rest are clarifications — and at most one shard is revealed per turn. That is compared against delivering the same instruction whole. Two metrics separate the effects: aptitude, the 90th-percentile score, and unreliability, the gap between the 90th and 10th percentiles across repeated runs.

**What it reports.** A **39% average performance drop** in the sharded setting. The split is the useful part: "model aptitude degrades in a non-significant way between the full and sharded settings, with an average drop of 16%. On the other hand, unreliability skyrockets with an average increase of 112%." The cause is named: "LLMs often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely" — and "when LLMs take a wrong turn in a conversation, they get lost and do not recover."

**What it means for `hi`.** This is the closest thing to a direct test of the skill's central mechanic, and it points against it. Asking one question per turn is structurally the sharded condition. What `hi` does about it is keep an explicit internal record across turns and consolidate everything into a single brief at the gate, so the final artifact is delivered whole rather than reconstructed from a drifting conversation. Whether that is enough is not measured anywhere.

**Where the benchmark stops.** In the experiment the information already exists and is deliberately withheld; the model is being starved of something knowable. In `hi` the information does not exist yet — the user has not decided. That is a real difference, and it is why the finding is a warning rather than a verdict. But it does not dissolve the risk: the model still accumulates state across turns and still commits early. No study anywhere compares one-question-per-turn against a batched questionnaire on the quality of the resulting decision.

</details>

<details>
<summary><b>Bridge</b> — does a decision structure the user never sees improve the answer?</summary>

**Used in** · [`hi` › Discussion mechanics](plugins/utevo-lux/skills/hi/SKILL.md#discussion-mechanics-one-decision-at-a-time) — modelling the conversation as a decision tree that is never dumped on the user, and the internal record of what is confirmed, provisional, rejected, hypothetical or open.

**Benchmark** · [Bridging the Novice-Expert Gap via Models of Decision-Making: A Case Study on Remediating Math Mistakes](https://arxiv.org/abs/2310.10648) — Wang, Zhang, Robinson, Loeb & Demszky, NAACL 2024 (`arXiv:2310.10648`). Built by cognitive task analysis over 700 real tutoring conversations.

**What it measures.** Experts annotate the decisions they make silently before replying to a student's mistake: error identification, remediation strategy, intention. GPT-4 is then conditioned on that structure — which the student never sees — and its replies are compared against the same model with no structure. A second condition swaps the expert decisions for random ones, holding the format fixed.

**What it reports.** "Responses from GPT4 with expert decisions (e.g., 'simplify the problem') are +76% more preferred than without." With randomised decisions in the same slots, quality falls to **−97% relative to the expert version**. The control is what makes this useful: the benefit comes from what the structure contains, not from having a structure at all.

**Why `hi` works this way.** The skill keeps a running internal record — confirmed, provisional, rejected, factual hypothesis, open — and explicitly forbids dumping the tree on the user, previewing upcoming questions, or narrating the process. Bridge is the closest existing test of that arrangement: state the model reasons over, held out of the reply.

**Where the benchmark stops.** The framework there is expert-authored and specific to math remediation; nothing shows a generic tree helps. And the randomisation result cuts the other way too — a structure filled with the wrong content scored far below having none, so a sloppy internal record is not a free bet. `hi`'s five categories have never been validated as the right ones for a design conversation.

</details>

<details>
<summary><b>Ask-before-Plan</b> — should the agent look it up, or ask?</summary>

**Used in** · [`hi` › Discussion mechanics](plugins/utevo-lux/skills/hi/SKILL.md#discussion-mechanics-one-decision-at-a-time) — "verifiable facts are the agent's work… do not turn 'how do competitors do this?' into a preference question. Value, priority and accepted risk belong to the user."

**Benchmark** · [Ask-before-Plan: Proactive Language Agents for Real-World Planning](https://arxiv.org/abs/2406.12639) — Zhang, Deng, Ren, Ng & Chua, EMNLP 2024 Findings (`arXiv:2406.12639`). 1,000 training and 1,000 test samples with 2,800 dialogue turns, built on travel-planning requests that are deliberately missing details.

**What it measures.** Three things an agent has to get right on an underspecified request: predict that clarification is needed and ask for it, call tools to gather what is discoverable without asking, and produce a plan that satisfies the stated constraints. Scored by delivery rate, commonsense pass rate, hard-constraint pass rate and final pass rate.

**What it reports.** Removing the clarification step from the full framework drops hard-constraint pass rate from **19.2% to 8.4%**, delivery rate from 98.8% to 93.3%, and commonsense pass rate from 64.3% to 53.3%. Asking, and looking things up, roughly doubles how often the resulting plan honours what the user actually required.

**Why `hi` works this way.** The skill splits the work by who can settle it. Anything checkable — what a competitor ships, whether something already exists — is the agent's job, resolved or labelled as a hypothesis. Only value, priority and accepted risk go back to the user as a question. This benchmark is the planning-agent version of that split, and it measures the cost of skipping it.

**Where the benchmark stops.** Final pass rate is **0.1% with clarification and 0% without** — one fully passing plan out of 1,000. Clarifying doubles constraint satisfaction on a task that essentially nobody completes, so the direction is trustworthy and the magnitude is not transferable. And only half the rule is tested here: every number measures task accuracy, none measures user burden. Whether resolving facts yourself actually costs the user fewer turns or less patience is unmeasured, in this paper and everywhere else found.

</details>

<details>
<summary><b>FreshQA</b> — does searching the web beat answering from memory?</summary>

**Used in** · [`hi` › 4. Precedents](plugins/utevo-lux/skills/hi/SKILL.md#4-precedents-who-has-solved-something-comparable) — the mandatory current search, the line that model memory is not evidence, and the rule to open the page instead of trusting a search snippet.

**Benchmark** · [FreshQA](https://github.com/freshllms/freshqa), released with [FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation](https://arxiv.org/abs/2310.03214) — Vu, Iyyer, Wang, Constant, Wei, Wei, Tar, Sung, Zhou, Le & Luong, 2023 (`arXiv:2310.03214`). The dataset is still maintained; it is revised on a rolling basis so the answers stay current.

**What it measures.** Questions sorted by how fast their answer decays — never-changing, slow-changing, fast-changing — plus questions built on a false premise. Grading is strict: a response counts only if every claim in it is correct and current.

**What it reports.** GPT-4 answering from its own parameters scores **28.6%**. The same model with search-augmented prompting scores **75.6%** — a gap of **47.0 points**. GPT-3.5 moves 26.0% → 56.0%. Gains run from +30 points on false-premise questions to +73.6 on never-changing ones.

**Why `hi` works this way.** The precedents stage asks what competitors ship today, whether an API already covers the case, whether the thing already exists. Those answers age, and a model's memory is frozen at training time. FreshQA is the benchmark built for exactly that class of question, which is why `hi` requires a current search there and states that model memory is not evidence.

**Where the benchmark stops.** [When Not to Trust Language Models](https://arxiv.org/abs/2212.10511) (Mallen et al., ACL 2023) finds unassisted models "remain competitive in questions about high-popularity entities" — searching a settled principle is not harmful, just unnecessary. And even with search, GPT-4 reaches only 59.2% on slow-changing questions: search shrinks the error, it does not close it. Search where the fact moves, not by reflex.

</details>

<details>
<summary><b>FollowBench</b> — how many rules can a model hold at once?</summary>

**Used in** · [`hi` › 6. Don'ts](plugins/utevo-lux/skills/hi/SKILL.md#6-donts-make-plausible-mistakes-explicit) — the ban on quotas, and the rule that a constraint only earns its place if a plausible failure justifies it.

**Benchmark** · [FollowBench: A Multi-level Fine-grained Constraints Following Benchmark for Large Language Models](https://arxiv.org/abs/2310.20410) — Jiang, Wang, Zeng, Zhong, Li, Mi, Shang, Jiang, Liu & Wang, ACL 2024 (`arXiv:2310.20410`, [ACL Anthology](https://aclanthology.org/2024.acl-long.257/)). 820 instructions across five constraint categories — content, situation, style, format, example — evaluated over 13 models at temperature 0.

**What it measures.** Constraints are added to a base instruction one at a time, giving five difficulty levels. Hard Satisfaction Rate "measures the average rate at which all constraints of individual instructions are fully satisfied"; Soft Satisfaction Rate "calculates the average satisfaction rate of individual constraints across all instructions". The gap between the two is the interesting part: it separates failing one rule from failing to hold the set.

**What it reports.** GPT-4's average HSR falls from **84.7% at level 1 to 61.9% at level 5**, while its SSR only falls 84.7% → 72.3% — individual rules keep being honoured well after the model stops satisfying all of them together. GPT-3.5-Turbo drops harder, 80.3% → 53.2%. The steepest category is example constraints, where GPT-4 goes from 87.5% to 42.5%.

**Why `hi` works this way.** Step 6 emits a set: invariants, out-of-scope items, unwanted use, prohibited shortcuts, rejected options. Each is a constraint, and the executor has to hold all of them at once. That is why `hi` refuses to write constraints to fill a quota and requires each one to trace back to a plausible failure found in the scenarios — every rule added past what the risk justifies makes the whole set less likely to survive.

**Where the benchmark stops.** It stacks constraints inside a single instruction in one turn, which is not the same shape as a brief handed to a separate agent later. It also varies count, not quality — nothing here says a well-written constraint survives better than a vague one. And it does not separate prohibitions from requirements, so it cannot answer whether a "don't" costs more than a "do".

</details>

<details>
<summary><b>Compositional constraint satisfaction</b> — where does a rule set break, and which rule survives?</summary>

**Used in** · [`hi` › 6. Don'ts](plugins/utevo-lux/skills/hi/SKILL.md#6-donts-make-plausible-mistakes-explicit) — "each constraint must be concrete, local and observable", and the ban on vague constraints and on quotas.

**Benchmark** · [Large Language Models Can Follow Instructions, But Not Many at Once: Phase Transitions in Compositional Constraint Satisfaction](https://arxiv.org/abs/2608.12426) — Vasileva, 2026 (`arXiv:2608.12426`, ARR May 2026 cycle; preprint, not yet a published venue). 15 models, 36 constraint types, 369,753 individual checks.

**What it measures.** Constraints are composed into a single instruction and each one is checked independently, so per-constraint compliance can be separated from all-at-once compliance. A second setting builds deliberately impossible instructions — two rules that cannot both hold — to see which one the model sacrifices.

**What it reports.** Per-constraint satisfaction decays as `mCSR(k) = 72.0% × 0.922^(k−1)` (held-out MAE 0.2pp). At eight constraints the model still passes any given rule about **41%** of the time but satisfies **all eight together only 5.7%** of the time, because "failures are nearly independent, which is what makes the accumulation multiplicative". Reliable following breaks down beyond **five to six** simultaneous constraints. Under forced impossibility, "prohibition beats requirement (N2: 91%, N1: 0%)" and "concrete inclusion beats abstract avoidance (L2: 73%, L1: 0%)".

**Why `hi` works this way.** Two of the skill's rules land exactly here. Constraints must be **concrete, local and observable** — the abstract-avoidance result is what happens to "don't be slow": it is the first thing dropped. And the ban on quotas is the count result: every rule added past what the risk justifies multiplies against all the others, and the set stops holding somewhere around six.

**Where the benchmark stops.** The survival numbers come from artificial impossibility scenarios built on lexical constraints — "no digits" against "sum to an integer", mandatory words against a lipogram. Those are not product invariants, so read the prohibition and concreteness findings as a strong analogy rather than a measurement of design Don'ts. This is also a preprint. And nothing here tests the shape `hi` actually recommends: whether a constraint written as a `wrong → intended` pair survives better than the same rule stated flatly.

</details>

<details>
<summary><b>Contrastive reflection</b> — does showing the intended version beat naming the mistake?</summary>

**Used in** · [`hi` › 6. Don'ts](plugins/utevo-lux/skills/hi/SKILL.md#6-donts-make-plausible-mistakes-explicit) — "when useful, use a short `wrong → intended` example".

**Benchmark** · [Contrastive Reflection for Iterative Prompt Optimization](https://arxiv.org/html/2606.30840v1) — Koh, Mo, Le, Zhan, Zheng, Bevis, Owen, Charney, Liu & Wu (LinkedIn), KDD 2026 Workshop on AI Agents for Information Retrieval (`arXiv:2606.30840`). Measured on HotpotQA exact match.

**What it measures.** Not exemplars inside a prompt — prompt revision. The method locates error-heavy regions of a task, then pairs each failure with a nearby success from the same region before handing both to a teacher model that proposes an edit. The control is the same loop given failures alone. The paper's own framing: "failures decide where the optimizer should look, but successes decide what the edit must preserve."

**What it reports.** Test accuracy goes from a 51.4% baseline to **60.4%** with contrastive pairs (+9.0pp), against **54.6%** for failure-only reflection (+3.2pp) — contrast beats naming the failure by **5.8 points**. The regression count matters as much: contrastive breaks **9** previously correct examples, failure-only breaks **19**.

**Why `hi` works this way.** A constraint that only names the mistake tells the executor what to stop doing and nothing about what to keep. The `wrong → intended` shape carries both halves, which is the same asymmetry this paper isolates: the failure locates the problem, the paired success is what stops the fix from destroying something that already worked.

**Where the benchmark stops.** This optimizes prompts across a dataset; it does not test a `wrong → intended` example written inside a single instruction, which is what `hi` actually does. One benchmark, one task family, a workshop paper. And the margin over an existing optimizer is thin — MIPROv2-light reaches +8.0pp against contrastive's +9.0pp, so the honest claim is that contrast beats failure-only, not that it beats everything.

</details>

<details>
<summary><b>Grounding in communication</b> — when is confirming worth what it costs?</summary>

**Used in** · [`hi` › Shared understanding gate](plugins/utevo-lux/skills/hi/SKILL.md#shared-understanding-gate) — presenting a compact brief, requesting explicit confirmation, and treating silence or a change of subject as not-confirmed.

**Source** · Clark & Brennan, "Grounding in Communication," in *Perspectives on Socially Shared Cognition* (Resnick, Levine & Teasley, eds.), American Psychological Association, 1991. Read in full from [the author's own faculty page](https://psychology.psy.sunysb.edu/sbrennan-/papers/clarkbrennan.pdf). This is theory and field observation, not a benchmark — it is where the confirm-before-proceeding step comes from, not proof that it works for agents.

**What it describes.** The **grounding criterion**: "that we and our addressees mutually believe that they have understood what we meant well enough for current purposes." Not perfect understanding — enough for the task at hand. The chapter then makes confirming expensive on purpose, naming **eleven costs** that shift with the medium: formulation, production, reception, understanding, start-up, delay, asynchrony, speaker change, display, fault and repair. Over all of it sits the *principle of least collaborative effort*: "participants try to minimize their collaborative effort — the work that both do from the initiation of each contribution to its mutual acceptance."

**What it reports.** In British directory-enquiry calls, customers confirmed the number they were given by repeating it back verbatim **over 70% of the time**, and operators did the same back for names, towns and street addresses. Operators also "always divided numbers of seven or more digits into their conventional groupings" before presenting them. Nobody instructed any of this — it is what people converge on when getting it wrong is expensive and the content is literal.

**Why `hi` works this way.** The gate is that behaviour, made explicit. The brief is the verbatim display: a compact restatement handed back before anyone commits, on exactly the content that is costly to get wrong. And silence not counting as confirmation is the grounding criterion taken seriously — mutual belief has to be demonstrated, not assumed.

**Where it stops.** No controlled study anywhere measures rework, disputes or completion time with a terminal confirmation gate versus without one, for humans or for agents. The 70% figure is about grounding a number mid-conversation, not a one-shot summary at the end. The cost framework is also the reason `hi` reads back in full only what is costly to reverse and lets cheap, reversible fields stand on one line — but that proportionality rule is reasoning applied from the chapter, not a result measured in it.

</details>

### `mission`

<details>
<summary><b>Adaptive-RAG</b> — is it worth sizing the investigation before starting it?</summary>

**Used in** · [`mission` › 1. Scope the investigation](plugins/utevo-lux/skills/mission/SKILL.md#1-scope-the-investigation) — writing one line on what would settle the question before the first tool call, and spending to that line.

**Benchmark** · [Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity](https://arxiv.org/abs/2403.14403) — Jeong, Baek, Cho, Hwang & Park, NAACL 2024 (`arXiv:2403.14403`). Evaluated on open-domain QA, including multi-hop sets.

**What it measures.** Three strategies are available for any question: answer with no retrieval, retrieve once, or retrieve iteratively. A small classifier predicts the complexity of the incoming question and routes it to one of them. Scoring tracks accuracy **and** cost together — F1 alongside average retrieval steps and seconds per query — so a method cannot win by simply spending more.

**What it reports.** With FLAN-T5-XL, routing reaches **F1 46.94 at 2.17 retrieval steps and 3.60 seconds per query**, against **F1 48.85 at 4.69 steps and 8.81 seconds** for always running the iterative pipeline. Under half the steps and **2.16× faster**, for 1.91 F1. The pattern holds across model sizes.

**Why `mission` works this way.** The skill decides what would settle the question before touching a tool, so a single fact does not get the treatment a market comparison deserves. The classifier's labels come from which strategy actually succeeded most cheaply — the same judgement, made once, up front.

**Where the benchmark stops.** The routing there is a trained classifier; `mission` routes on the model's own judgement of its own question, and nobody has measured that version. The tasks are open-domain QA, not code archaeology or market research, so the tiers transfer as an idea and not as calibration. And the honest shape of the result is a trade: routing is cheaper and slightly *less* accurate than always doing the expensive thing. It wins on cost per answer, not on answers.

</details>

<details>
<summary><b>BEIR and CLARC</b> — does semantic search replace exact match?</summary>

**Used in** · [`mission` › 2. Investigate the repository](plugins/utevo-lux/skills/mission/SKILL.md#2-investigate-the-repository) — searching lexically and semantically without ranking one above the other, and confirming anything decisive with a direct read.

**Benchmarks** · [BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models](https://arxiv.org/abs/2104.08663) — Thakur, Reimers, Rücklé, Srivastava & Gurevych, NeurIPS 2021 Datasets & Benchmarks (`arXiv:2104.08663`), 18 datasets across diverse retrieval tasks. · [CLARC: C/C++ Benchmark for Robust Code Search](https://arxiv.org/abs/2603.04484) — Wang, Huang, Fang & Wang, ICLR 2026 (`arXiv:2603.04484`), six models evaluated on code that has been identifier-anonymized or compiled down to Assembly and WebAssembly.

**What they measure.** BEIR asks how retrieval models behave **out of their training domain** — the situation any tool is in when pointed at a repository it has never seen. CLARC asks a sharper question: when a code-search model finds the right function, is it reading the code or reading the names?

**What they report.** On BEIR, lexical BM25 outperforms DPR on **16 of 18** datasets zero-shot — on TREC-COVID, nDCG@10 **0.656 against 0.332** — and the paper's conclusion is that "BM25 is a robust baseline", with dense models showing "considerable room for improvement in their generalization capabilities". CLARC points the other way first: on ordinary code search the embedding models are far ahead, Voyage-code-3 reaching **86.93 MRR** where BM25 gets **8.20**. Then it removes the names, and reports "sharp drops in retrieval effectiveness" that "highlight the models' persistent reliance on lexical features rather than code semantic understanding".

**Why `mission` works this way.** Read together, neither tool wins. Semantic search finds what you could not name — that is the 86.93 against 8.20. But its advantage leans on the identifiers, so it is the tool that degrades exactly when a rename, a refactor or generated code takes the names away, and exact match is the one that still works there. The skill therefore refuses to rank them, sends identifiers and strings to exact match, and requires a direct read before anything decisive rests on either.

**Where the benchmarks stop.** BEIR is text retrieval, not code, and predates current embedding models. CLARC's degradation varies a great deal by model and by evaluation group, and the tables do not support a single headline drop figure — the reliable claim is the direction and the mechanism, not a magnitude. Neither benchmark evaluates an agent choosing between the two tools, which is the actual decision the skill is instructing.

</details>

### `equip`

<details>
<summary><b>ClarEval</b> — what does an ambiguous instruction cost, and does the agent ask?</summary>

**Used in** · [`equip` › 1. Recover intent and current state](plugins/utevo-lux/skills/equip/SKILL.md#1-recover-intent-and-current-state) — resolving open decisions one at a time instead of hiding them inside steps — and the handoff test in [`equip` › 5. Deliver the plan](plugins/utevo-lux/skills/equip/SKILL.md#5-deliver-the-plan): could another agent execute this without inventing decisions?

**Benchmark** · [ClarEval: A Benchmark for Evaluating Clarification Skills of Code Agents under Ambiguous Instructions](https://arxiv.org/abs/2603.00187) — Li, Wu & Chang, 2026 (`arXiv:2603.00187`). 2,250 instances built from 750 source tasks — 150 from HumanEval, 600 from LiveCodeBench — each injected with one of three realistic ambiguity types: missing goals, missing premises, ambiguous terminology.

**What it measures.** Two things at once. Whether the agent still produces correct code when the instruction is underspecified, and whether it asks well: Average Turns to Clarify, for how few turns it needs, and Key Question Coverage, for whether it asked about the thing that actually mattered.

**What it reports.** "GPT-4o achieves a state-of-the-art Pass@1 of 89.02% on clarified tasks, its performance plummets to 8.94% under ambiguity." Ambiguous terminology is the worst case, at 6.71%. Same model, same problems — the gap is the instruction. The paper also finds that coding ability does not carry over: models that excel at code "often lack the strategic communication skills required for efficient partnership."

**Why `equip` works this way.** A plan is a handoff. `equip` never writes the code, so the only thing it controls is how little the executor has to invent — the exact variable ClarEval isolates. That is why open product decisions get settled during planning instead of buried in a step, and why the plan is measured against "could another agent execute this without inventing decisions?" before it is delivered.

**Where the benchmark stops.** The tasks are function-level, not repository-scale, and the ambiguity is injected rather than naturally occurring — a real feature request is messier than a stripped premise. It also scores asking without pricing it: a low turn count is rewarded, the cost of interrupting a human is not modelled.

</details>

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
  skills/{hi,mission,equip,hunt,bug,look,exura}/SKILL.md
```

The seven skills have a single source. The three manifests package the same files. The GitHub references ship with both `look` and `exura` to allow individual installs; the validator checks that the two copies stay identical.

Local validation:

```sh
python scripts/check.py
claude plugin validate .
claude plugin validate plugins/utevo-lux
```

When publishing a plugin update, bump the version in the three manifests and in the catalogs that declare it. Direct-skill users can run `npx skills check` and `npx skills update`; plugin users update through their agent.

## <img src="plugins/utevo-lux/assets/ferumbras-hat.gif" alt="Ferumbras' Hat" width="24"> Acknowledgments

Thanks to [fbuchetti](https://github.com/fbuchetti), one of the most absurd sorcerers out there: explores every corner of the map and casts pure magic on ontology. I was the knight blocking the creatures so the sorcerer could unleash all those spells and powers.

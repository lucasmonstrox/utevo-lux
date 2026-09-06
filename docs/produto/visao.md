---
tipo: produto
status: ativo
updated: 2026-09-06
description: Visão geral do Utevo Lux — conjunto de 7 skills de engenharia de software inspiradas no Tibia para agentes de IA (Claude Code, Codex, Cursor), cobrindo da conversa inicial ao PR revisado.
---

# Utevo Lux — Visão do Produto

> **Para que serve este documento.** Explicar em um só lugar **o que é** o Utevo Lux: conceito, público, conjunto de skills (`hi`, `mission`, `equip`, `hunt`, `look`, `exura`, `bug`), princípios de portabilidade e limites de escopo. É o documento-âncora de produto do repositório.

---

## 1. Resumo em uma frase

**O Utevo Lux é um conjunto modular e agnóstico de sete skills de engenharia de software inspiradas no universo do Tibia, projetado para orientar agentes de IA (Claude Code, Codex, Cursor) desde a concepção de requisitos até a entrega e revisão de código com evidências reais.**

---

## 2. O problema

O trabalho com agentes autônomos de IA frequentemente sofre de falta de processo estruturado:

1. **Prematuridade na execução**: o agente começa a alterar código antes de entender o problema real ou pesquisar as causas-raiz.
2. **Poluição de repositórios**: muitos frameworks geram dezenas de arquivos de controle, logs e metadados que poluem a base de código do usuário.
3. **Acoplamento a stacks específicas**: ferramentas amarradas a linguagens ou modelos restritos que perdem portabilidade.
4. **Falta de evidências de teste**: modificações entregues sem comprovação visual ou mecânica de funcionamento.

---

## 3. Para quem é

| Persona | Quem é | O que precisa no Utevo Lux |
|---|---|---|
| **Engenheiro de Software / Usuário de IA** | Desenvolvedor utilizando Claude Code, Codex ou Cursor | Instruções portáteis, fluxo previsível em etapas e execução com validação prática |
| **Mantenedor de Skills** | Quem desenvolve e distribui o plugin | Manter paridade entre formatos de manifesto (Agent Skills, Claude Plugin, Cursor Plugin) e testes de integridade (`scripts/check.py`) |

---

## 4. O ciclo das 7 skills

```text
hi ──> mission ──> equip ──> hunt ──> look ──> exura
               bug ↗
```

1. **`hi`**: abre o diálogo com o "NPC" — alinha escopo, faz perguntas necessárias e define o roteiro com o usuário antes de codificar.
2. **`mission`**: aceita a missão do quest log — pesquisa a fundo no código, histórico do git e documentação externa, reunindo evidências.
3. **`equip`**: equipa o time para a caçada — define plano passo a passo, critérios de aceite e estratégias de validação antes de alterar arquivos.
4. **`hunt`**: caçada ao código — executa o plano definido, roda verificações e recolhe as evidências de que a mudança funciona.
5. **`look`**: inspeção do loot — revisa PRs, diffs e discussões com olhar crítico, apontando defeitos demonstráveis.
6. **`exura`**: cura para o PR ferido — aplica correções solicitadas em reviews, com um commit focado por ajuste e resposta na fonte.
7. **`bug`**: rastreia o bug até o covil — investiga causa-raiz com rigor metodológico e elimina o problema (com opção `--fix`).

---

## 5. Princípios fundamentais

- **Na conversa, não no repositório**: briefs, planos e relatórios pertencem ao diálogo do agente com o usuário; as skills não criam documentação automática indesejada nem poluem o projeto-alvo.
- **Portabilidade universal**: instruções agnósticas de stack, sem dependências implícitas de caminhos privados ou modelos proprietários fixos.
- **Evidência sobre presunção**: nenhuma tarefa é dada como concluída sem validação mecânica correspondente.

---

## 6. O que NÃO somos (Anti-escopo)

- ❌ Não somos um framework pesado de orquestração com banco de dados próprio ou servidor dedicado.
- ❌ Não criamos arquivos `.md` temporários no projeto do usuário sem solicitação explícita.
- ❌ Não somos restritos a uma única ferramenta de IA: suportamos simultaneamente Claude Code, Codex e Cursor.

---

## 7. Glossário

- **Skill**: instrução especializada invocável por slash command (`/hi`, `/hunt`) ou menção (`$equip`).
- **Plugin Manifest**: arquivos de especificação (`claude-plugin.json`, `package.json`, etc.) que expõem as skills nos ecossistemas suportados.
- **Hunting**: fase de implementação ativa guiada por plano e testes.

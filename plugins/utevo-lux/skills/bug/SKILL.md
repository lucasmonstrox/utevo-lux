---
name: bug
description: Investiga a causa-raiz de bugs com reprodução, histórico Git e experimentos que refutam hipóteses. Entrega diagnóstico na conversa e aplica correção quando solicitada ou com --fix.
---

# Bug

Uso: `/bug <sintoma> [--fix]`, ou a invocação de skills do agente.

**Evidência antes de teoria, reprodução antes de conserto, causa-raiz antes de patch.** Sintoma conhecido pode ter causa nova.

Leia instruções locais e documentação relevante existente. Diagnóstico, hipóteses e resultados ficam na conversa; não crie nem atualize documentação ou registros de features.

## 1. Triagem

Obtenha esperado, observado, erro literal e contexto necessário para reproduzir. Confira quando começou e se afeta todos os casos ou apenas dados/ambientes específicos.

Confira estado local, commits recentes, entrypoint executado, porta real, versões e configuração. Em variáveis de ambiente, confira presença/formato sem imprimir segredos.

| Sinal | Rota |
|---|---|
| Funcionava antes | Histórico e possível bisect. |
| UI, console, rede, race | Navegador; [DevTools](devtools.md) se precisar aprofundar. |
| API/runtime em Bun | Reprodução de rota/handler; [Bun](bun.md) somente se usado pelo projeto. |
| Cache, HMR, logs em Next.js | [Next.js](web-next.md), conferindo a versão. |
| Dependência após atualização | Comparar versões e isolar o uso. |
| Dado específico | Comparar entrada que falha com entrada que funciona. |
| IA ou conversa | Isolar entrada, estado, resposta e ação. |
| Intermitente/desconhecido | Experimentos dirigidos por hipóteses. |

Leia só referências pertinentes. Ferramentas específicas são opcionais; declare limites.

## 2. Delimitar origem e consumidores

Busque o entrypoint e siga o fluxo real. Use busca conceitual/LSP disponíveis, ou `rg` e leitura direcionada. Confirme consumidores dos contratos que podem mudar.

Consulte decisões existentes: comportamento deliberado pode ser pedido de mudança, não bug. Hipótese refutada só volta com evidência nova.

Achado interno leva arquivo/linha; histórico leva hash; dado leva consulta e contexto seguro. Separe evidência de inferência.

## 3. Reproduzir

Construa o menor detector de bom/ruim na infraestrutura existente. Scripts de reprodução podem ser temporários; testes definitivos cobrem o comportamento.

- UI: interaja como o usuário; observe console, rede e resultado.
- API: exercite rota/handler real; verifique resposta e efeito, inclusive assíncrono.
- Dados: preserve a característica que causa a falha em uma amostra segura.
- IA: fixe entrada e estado relevante; use sessão nova quando estado acumulado importar.
- Caso grande: remova metade da entrada/etapas, repita e minimize o que é necessário para falhar.

Não reproduziu: reporte hipóteses e evidência faltante. Um bug que sumiu sozinho não foi consertado.

## 4. Histórico Git

- `git log -- <paths>` delimita a janela.
- `git log -S <trecho> -p -- <paths>` encontra mudanças de conteúdo; `-G` ajuda com expressões regulares.
- `git blame` e `git log --follow` ajudam a atravessar refactors.
- Leia o diff inteiro do commit suspeito para explicar a regressão.

Use bisect com detector confiável em checkout/worktree isolado. Em `git bisect run`: 0 = bom; 1–127, exceto 125, = ruim; 125 = não testável. Termine com `git bisect reset`. Preserve o estado de trabalho do usuário.

## 5. Refutar hipóteses

Mantenha na conversa: hipótese → experimento → resultado → veredito.

Cada experimento responde uma pergunta clara e muda uma variável. Separe código, dados, configuração, dependência e ferramenta. Culpar uma biblioteca exige reprodução isolada.

Valor errado sem stack: observe o meio do fluxo, determine se já está errado e continue na metade responsável até achar o primeiro produtor incorreto. A linha que recebe dado inválido pode ser apenas vítima.

Bug que desaparece com log/espera sugere timing. Observe com menos interferência e teste com e sem instrumentação.

Tentativas repetidas sem evidência nova pedem outra hipótese. Delegação pode testar hipóteses independentes quando disponível e autorizada, sem modelo obrigatório.

## 6. Dependências quando necessário

Compare lockfile, versões instaladas e histórico. Use o gerenciador do projeto para entender a cadeia de dependências.

Busque a mensagem de erro **literal**, não uma paráfrase: o texto exato é o que casa com o relato de quem já passou por isso. Procure na documentação oficial e no changelog da versão que você tem, nas issues e discussões do repositório da dependência **incluindo as fechadas** — bug já corrigido costuma existir só como issue fechada ou PR de correção — e na web aberta, que alcança fórum, post e changelog que o rastreador do projeto não indexa.

Abra a página antes de concluir; snippet de busca não é prova, e relato sem versão não serve. Confirme em reprodução mínima e compare versões em ambiente isolado quando útil.

Prefira corrigir nosso uso, fixar uma versão compatível ou aplicar workaround localizado com causa e fonte. Não publique issues upstream sem solicitação.

## 7. Diagnóstico e correção

Entregue na conversa causa confirmada ou hipótese, origem e sintoma, commit causador quando demonstrável, reprodução, impacto, correção mínima e sua verificação.

Por padrão, investigue e proponha. `--fix` ou pedido explícito autoriza implementar. Não peça nova confirmação se já autorizada.

Ao corrigir, prove o comportamento incorreto antes e o correto depois com teste proporcional. Para retirar o patch na comparação, use contexto isolado, sem stash do trabalho do usuário. Refaça o fluxo original e os checks dos consumidores e remova instrumentação temporária.

Não crie arquivos de documentação. Commits, push, mensagens externas e deploy seguem a autorização da sessão.

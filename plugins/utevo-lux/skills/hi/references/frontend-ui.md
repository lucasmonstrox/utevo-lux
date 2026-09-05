# UI e frontend

Leia esta referência quando a tarefa altera tela, navegação, formulário, visualização ou interação. Use apenas os ramos que mudam a decisão.

## O que explorar

- **Público e contexto:** papel, frequência de uso, conhecimento, dispositivo, ambiente, urgência e autoridade. Diferencie quem opera da pessoa que recebe o benefício.
- **Job e entrada:** o que disparou a visita, qual informação já existe, o que a pessoa tenta decidir/fazer e para onde precisa seguir.
- **Hierarquia:** informação primária, secundária e progressivamente revelada; densidade; navegação; relação com fluxos adjacentes.
- **Estados reais:** inicial, loading, vazio, parcial, erro, sem permissão, conflito, sucesso, repetição e recuperação/undo quando material.
- **Interação e feedback:** ação principal, ações perigosas, prevenção de erro, confirmação, latência percebida, edição, teclado, mobile e continuidade entre sessões.
- **Acessibilidade e linguagem:** ordem de foco, leitura por tecnologia assistiva, contraste, alvos, alternativas não visuais e copy que explique consequência em vez de jargão interno.
- **Confiança:** origem e frescor dos dados, automação versus ação humana, reversibilidade e explicação quando o sistema toma decisões.

## Precedentes de UI

Olhe primeiro o design system e fluxos internos comparáveis; depois concorrentes e produtos análogos. Compare o fluxo inteiro e os estados, não apenas o screenshot feliz. Registre o que o precedente pressupõe sobre público, volume de dados e plataforma.

## Exploração com mocks

Quando houver pelo menos duas estruturas plausíveis e a escolha for material, produza **de 3 a 5 mocks estruturalmente distintos** antes de fechar a opção. Não fabrique cinco variações para uma mudança trivial.

Fixe antes um mini-brief comum: mesmo público, cenário, conteúdo/dados, plataforma e restrições. Varie hipóteses como navegação, hierarquia, densidade, disclosure ou modelo de interação — não apenas cor, borda ou posição de um botão.

Para cada mock, declare:

- hipótese que ele testa;
- cenário em que é melhor e em que falha;
- custo cognitivo e operacional;
- don’ts respeitados ou tensionados.

Apresente-os progressivamente: **uma hipótese visual e uma pergunta por mensagem**. Só depois de o usuário entender as direções compare os finalistas; não despeje cinco mocks acompanhados de cinco análises. Use ferramenta visual disponível; sem ela, faça wireframes de baixa fidelidade. O mock é descartável e serve para decidir, não autoriza código de produção. Após a escolha, preserve a direção e o motivo; não preserve todas as variações como requisitos.

## Não decidir aqui

Não transforme a conversa em escolha de componente, arquivo, hook, state manager ou classe CSS, salvo quando isso altera uma restrição visível já decidida. Esses mecanismos pertencem ao `/pl`.

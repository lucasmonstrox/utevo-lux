# Diagnóstico profundo no navegador

Use para races, corpo de requests, console durante redirects, hydration e emulação. Descubra as capacidades disponíveis; não invente tools ou parâmetros.

Reproduza a ação, espere uma condição observável e confira árvore de acessibilidade, console e requests. Screenshot não substitui erro ou resposta.

Para request falhando, compare URL, método, headers necessários, payload, resposta e efeitos. Não exponha cookies, tokens ou dados pessoais na evidência.

- Redirect: preserve console entre navegações.
- Intermitência: simule rede/CPU mais lenta e confronte a ordem dos eventos.
- Hydration: leia a diferença servidor/cliente e isole sua origem; esconder aviso não corrige causa.
- Dialog: trate somente a sessão de teste; não aceite ação destrutiva para liberar a ferramenta.
- Estado do navegador: compare sessão isolada sem apagar cookies ou fechar processos do usuário.

Desfaça emulação/instrumentação e feche só a sessão criada para investigar. Declare capacidades indisponíveis.

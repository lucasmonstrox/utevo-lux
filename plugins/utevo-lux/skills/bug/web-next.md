# Diagnóstico quando o projeto usa Next.js

Confira a versão e sua documentação, inclusive guias locais quando existirem.

- Separe logs do navegador e servidor. Correlacione digest com o log do servidor.
- Ação aparentemente ausente: confira request, status e resposta antes de mudar o handler.
- Serialização: localize a fronteira servidor/cliente e os valores que a atravessam.
- Dado antigo: distinga cache do servidor, navegador e navegação, uma hipótese por vez.
- HMR: confirme que o arquivo editado é servido pelo processo/porta corretos.
- Compare bundlers só com opções suportadas; retirar uma flag não garante a troca.
- Limpar cache e o erro sumir é uma pista. Qualquer limpeza limita-se ao diretório de build confirmado, preservando dados e configuração.
- MCP de diagnóstico do Next é opcional; logs e navegador continuam disponíveis.

Não altere configurações de segurança do sistema para acelerar a investigação.

Consulte a [documentação oficial](https://nextjs.org/docs) para a versão usada.

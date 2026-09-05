# Diagnosing when the project uses Next.js

Check the version and its documentation, including local guides where they exist.

- Separate browser logs from server logs. Correlate the digest with the server log.
- An action that looks missing: check the request, status and response before changing the handler.
- Serialization: locate the server/client boundary and the values that cross it.
- Stale data: distinguish server, browser and navigation caches, one hypothesis at a time.
- HMR: confirm the file you edited is served by the right process and port.
- Compare bundlers only with supported options; removing a flag does not guarantee the switch.
- Clearing the cache and watching the error disappear is a clue. Any clearing stays inside the confirmed build directory, preserving data and configuration.
- The Next diagnostic MCP is optional; logs and the browser remain available.

Do not change the system's security settings to speed up the investigation.

Read the [official documentation](https://nextjs.org/docs) for the version in use.

# Diagnosing when the runtime is Bun

Confirm the version and the project's scripts. Read the documentation before using flags.

- Reproduce in the closest test or handler. Check the options with `bun test --help`.
- Filter by file or test name; repeating intermittent cases depends on the options your version offers.
- Use the debugger Bun supports and the address the process reports.
- Fetch logs can expose headers and bodies. Use test data, strip credentials from the evidence and turn the instrumentation off afterwards.
- Inspect the dependency chain with the command available in your version.
- Node/Bun suspicion: run the same isolated reproduction on the relevant runtimes. A difference is evidence to investigate, not automatic proof of blame.

Sources: [Bun](https://bun.com/docs), [Node.js compatibility](https://bun.com/docs/runtime/nodejs-apis). Check the current limitations.

# Deep diagnosis in the browser

Use this for races, request bodies, the console during redirects, hydration and emulation. Discover the capabilities available; do not invent tools or parameters.

Reproduce the action, wait for an observable condition, then check the accessibility tree, the console and the requests. A screenshot does not replace an error or a response.

For a failing request, compare URL, method, required headers, payload, response and effects. Do not expose cookies, tokens or personal data in the evidence.

- Redirect: preserve the console across navigations.
- Intermittence: simulate a slower network or CPU and compare the order of events.
- Hydration: read the server/client difference and isolate its origin; hiding the warning does not fix the cause.
- Dialog: handle only the test session; do not accept a destructive action to unblock the tool.
- Browser state: compare against an isolated session without deleting cookies or closing the user's processes.

Undo the emulation and instrumentation, and close only the session you created to investigate. State any capability that was unavailable.

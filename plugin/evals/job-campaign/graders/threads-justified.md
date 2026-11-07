---
type: llm
---
PASS if every sub-agent thread the reply reports (in its Threads line, decisions.md or the text) gives a reason that matches one of the director's four spawn rules (parallel, noise, fresh eyes, model or tools), and sequential work that depended on earlier decisions was done in the main thread. Also PASS if no thread was spawned and the work stayed in the main thread. FAIL if a thread was spawned only because a specialist exists for the discipline.

# The owner's prompt, verbatim

**Serves:** prompt TOOL-aScouredKit-1 TOOL-aScouredKit-2

Handed to `/unattended` as the `--prompt` value on 2026-08-30, node `a`. The value carried
whitespace and named no readable file, so it is the prompt itself and is taken verbatim. Recorded
here rather than in the build README because the README's heading set is closed and its slots are
byte-capped, and because a mandate that points at an editable file is not a mandate.

```text
Conduct a full adversarial review of the kit.
Things to look for:

* dead code
* hardcoded values (prefixes, paths, variables - they should all be flexible, owner adjustable)
* govkit convergence (can every tool in the kit be deployed, updated, wired to another project?)
* inefficient or flawed design (eg. codebase-map reuse audit couldn't see python, can it see everything else now? Would other tools from the kit suffer the same bug? inspect for additional flaws as necessary)
* prose optimization - can any of the load-bearing instruction .md files be optimized without breaking their instructions/unambiguity/context?

Fix your discoveries per the protocol.
```

## Reading taken, and the one ambiguity resolved

"The kit" is read as the WHOLE shipped product — every directory under `tools/` carrying a
`kit.toml`, plus `skills/session-kickoff/`, the charter template and the instruction documents under
`memory/guides/`. The narrower reading, one named kit, is refused by the third bullet: "can every
tool in the kit be deployed" only has a referent under the wide reading.

No clarification was asked. Every field the kickoff checker's `--task-skeleton` names was derivable
from the prose, the memory tree and the code, and ACCEPTANCE and GATES were both derivable, so no
gap was disqualifying.

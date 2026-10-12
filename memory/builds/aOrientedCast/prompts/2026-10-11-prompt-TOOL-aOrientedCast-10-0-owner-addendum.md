**Serves:** research TOOL-aOrientedCast-10 TOOL-aOrientedCast-11

# The owner's addendum, verbatim — two features added to the running build

Sent by the owner in this build's session on 2026-10-11, while `TOOL-aOrientedCast-8` was building.
It extends the confirmed brief. The run records it as two `--rescope add` units, and quotes it here
so a resumed session holds the owner's own bytes.

```text
Two features should be designed and integrated into this build:

1.  a default effort  workflows/agents run per their role: default effort level for any generic agent is 'MEDIUM'; 'Prompt writers' should always run at 'EXTRA' (xhigh) effort; 'Spec writers' should run at 'EXTRA' (xhigh) effort by default; 'Spec reviewers' and their workflows at 'MEDIUM'; 'code builders' building from specs should run at 'HIGH' effort by default; Tier2-reviews (code, diff, closing reviews) should run at 'HIGH' effort by default. Default effort levels should be modeled in a config file and read from it, freely owner-adjustable as they would want to.
2. workflows and agent brief handoffs should be strictly forbidden (and preferably mechanically gated) from running gates within their role-specific agents, especially self-tests, with exception for memory hygiene and lexicon - spec writers should ensure their specs pass hygiene and lexicon and that only, while code writers should ensure to pass lexicon. The rest of the gates are always the job of the main session at the merge and/or push threshold and should never execute by agents.
```

## How the run reads it

- **Feature 1 is `TOOL-aOrientedCast-10`**: a per-role effort level, read from one owner-editable
  config file and carried into every agent the catalogue spawns.
- **Feature 2 is `TOOL-aOrientedCast-11`**: a role agent may run no gate and no self-test. A spec
  writer may run only memory hygiene and the lexicon, and a builder only the lexicon. The
  prohibition is gated mechanically, and the texts that hand agents their work say the same.
- **From the moment this addendum arrived**, the run's own remaining dispatches carry feature 2's
  rule in their ground text, so its passes stop running gates before the gate exists.

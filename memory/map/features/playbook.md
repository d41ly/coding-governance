# playbook — the governance template, its companions, and the gates that hold their claims

```toml
feature = "playbook"
title = "The governance playbook — the shipped template + companions, and the gates over their claims"
status = "shipped"
streams = ["playbook", "tooling"]
decisions = ["TOOL-aSiftedPlaybook-1"]

[claims]
gate-legs = ["template size gate selftest", "playbook parity", "playbook parity selftest"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
[paths]
globs = [
  "tools/check-template-size.sh",
  "tools/check-template-size.test.sh",
  "tools/template-size-highwater.txt",
  "tools/check-playbook-parity.sh",
  "tools/check-playbook-parity.test.sh",
  "tools/playbook-kit-waivers.txt",
]
```

The product this repo ships is three files at the root — `parallel-coding-governance.template.md`
(the operating ruleset), `.customize.md` (the deploy-time placeholder catalog) and `.domain-rules.md`
(the activity-scoped checklists the template references by §-stub). This dossier covers the
machinery that holds their claims true, not the documents' contents.

Minted by `TOOL-aSiftedPlaybook-2` because that unit adds the first genuinely NEW leg key in this
area. `TOOL-aSiftedPlaybook-1` renamed an existing key in place and minted nothing, which is why the
map had no playbook dossier until now.

## Constraints & why

- **The size ceiling is 49152 bytes, and that is a REVERSAL.** It read 32 KiB and "never raise the
  limit" in four carriers until 2026-08-16, when the owner ordered the raise
  (`memory/DECISIONS.md`, `TOOL-aSiftedPlaybook-1`). Three prior units cite the old ceiling as a
  binding constraint; their reasoning stands and their premise does not. Read the live limit from
  the gate, never from prose — it has moved.
- **The gate has TWO consumers, and only one of them is the playbook.** `tools/gate-legs.json` runs
  the same script over `skills/session-kickoff/SKILL.md` at 18432, passed POSITIONALLY. The
  positional exists because a leg cannot set an environment variable: `run-gates.sh` execs its argv
  with no shell. Raising the default therefore cannot move the kickoff engine's cap — insulated by
  construction, and verified rather than assumed, because the other reading would have silently
  raised it from 18 KiB to 48 KiB.
- **The high-water ratchet is ADVISORY and never changes the exit code.** It replaces the forcing
  function the old ceiling was providing: at 86 free every template edit was priced by the gate, and
  at 16470 free nothing prices one. No fixed threshold works — every conventional fraction is silent
  through a whole build, and anything tight enough to price one sits below the current size and
  fires forever, the permanently-red decoration `tools/drift-audit/drift_signals.py` names as an
  anti-pattern.
- **The record is KEYED BY MEASURED FILE**, one `<path>\t<bytes>` row per subject, because one
  shared number cannot serve two consumers ~14 KB apart: the smaller could never warn, and a
  `--bump` on it would make the larger warn on every run forever.
- **`--bump` is a flag, not a positional.** The three positionals are subject, limit and record
  path; a mode sharing a slot with a path is how one silently becomes the other.

## Shared seams

- `tools/gate-legs.json` — the single source the runner, the codebase-map inventory extractor and
  the drift-audit charter probe all read. Renaming a leg label therefore trips three gates at once:
  coverage reds the old key as `stale_baseline` AND the new one as `unclaimed`, and freshness
  byte-compares the generated artifacts.
- `tools/memory-tree/check-arms.py` — the size gate entered its population when its exit paths
  became a numbered `fail()` helper. The `ARMS_FLOORS` entry in `.memory-tree.conf` is what makes
  the pin real: an UNDECLARED floor is silently skipped, not refused.
- `tools/govkit/registry.toml` — every depth-1 path under `tools/` must be a declared entry member
  or an exact-path `[[exempt]]` row. Every path in this dossier's `[paths].globs` above carries
  one; the globs list is the enumeration and no count is repeated here, having gone stale once
  already when this feature grew from three paths to six inside one build.
- `memory/guides/SESSION-KICKOFF.md` — `tools/check-template-size.sh` is a watched pathspec, so any
  change to the gate forces a manifest re-stamp.

## Gaps

- **The template's CONTENT is not covered here.** No dossier claims the three playbook documents
  themselves, and no gate reads them for accuracy. `TOOL-aSiftedPlaybook-3` adds structural parity
  checks over three classes of claim; a fluent paraphrase that is subtly wrong still passes, and
  that gate's own header says so.
- **The ceiling is a shell constant, not a declared pin.** `.memory-tree.conf`'s `READ_PATH_CEILING`
  is the same problem solved the other way — a declared byte budget with each raise justified in the
  conf beside the number. Recorded as a backlog row rather than done here.
- **Nothing enforces that the high-water record shrinks.** `--bump` moves it in either direction and
  says by how much; the visibility is the diff, not a gate.

## Reuse affordance

seam: check-template-size.sh positional resolution — reuse for gating ANY file's byte size on the
merge bar without writing a sibling script; extend via one `tools/gate-legs.json` entry passing the
subject and its limit positionally, plus one `--bump` to seed the subject's row. The
positional/env/default chain and the per-file keying already admit a third consumer unchanged.
seam: the high-water record — reuse for pricing growth in any tracked artifact where a fixed
threshold is either silent or permanently red; extend via a `<path>\t<bytes>` row, remembering that
`--bump` writes the key through the same derivation the reader uses, so a new consumer needs an arm
comparing its key to a LITERAL.

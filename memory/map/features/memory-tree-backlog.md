# memory-tree backlog — per-build asks, and the family files that are their views

```toml
feature = "memory-tree-backlog"
title = "The backlog in both modes: authored family shards, or asks filed per build with generated family views"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-dDerivedDocket-19", "TOOL-dDerivedDocket-33", "TOOL-dDerivedDocket-34"]

[claims]
gate-legs = []
kits = []
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = ["DEPL.md", "KICK.md", "PLAY.md", "TOOL.md"]
lexicon-verbs = []
[paths]
globs = [
  "tools/memory-tree/backlog.py",
  "tools/memory-tree/migrate_backlog.py",
  "tools/memory-tree/transition_audit.py",
  "memory/backlog/*.md",
  "memory/builds/*/BACKLOG.md",
]
```

The four family files are ONE mechanism read two ways, so one dossier claims all four. Before this
dossier three of them sat unclaimed in the baseline and the fourth, `DEPL.md`, was claimed by the
govkit dossier, which had nothing to say about the backlog: the map disagreed with itself about where
a family file belongs. The inventory keeps its `backlog-shards` name in both modes, because every
dossier carries that field and renaming it would churn all of them to say what one extractor comment
says.

## Constraints & why

**The mode is one conf key, and absent means `shards`.** `BACKLOG_MODE` blank or absent reads
`shards`: the family files under `memory/backlog/` are the authored backlog, one status slot per row.
`builds` makes each ask a row of `builds/<slug>/BACKLOG.md` in the folder of its own id's slug, derives
its status, and turns every family file into a GENERATED view of the live asks. This repo runs
`builds`. Any other value refuses by name, because defaulting a typo to `shards` would keep the old
renderer alive after a tree had migrated. The key's spelling is frozen: the transition audit
classifies every commit by it.

**Status is derived, never typed.** A typed status drifts from the records that decide it. The fold
in `backlog.derive_statuses` reads SETS — the specs whose header `closes` or `advances` an ask, and the
disposition rows about it — and nothing reads a date, a file order or a row order, so a permuted
corpus folds to the same bytes and a merge cannot change a status by its order. Each writer appends to
its OWN build's file, so what used to be a merge conflict over a status token is a derivation over the
union of files. One writer per file is a practice, not a construction, which is why each build's
`BACKLOG.md` carries the row-keyed merge attribute.

**The same-id pairing is declared, never inferred.** `unit` on an ask says its same-id spec is its
answer. Four id pairs in this corpus are a backlog row and a spec about different subjects, so equal
ids prove nothing; the legacy pairs were adjudicated once, by rule, in the records
`TOOL-dDerivedDocket-33` signed, and the switch-over applied exactly what was signed.

**A grant is a proposal until an owner commits it** (`TOOL-dDerivedDocket-19`). An ask row's `may`
names what a run could do; only a build README an owner committed honours it, and a `SCOPE` row
carrying one is a verdict, because its writer is a triager adding clauses to somebody else's ask.

**The switch retired a counted-never-refused rule** (`TOOL-dDerivedDocket-34`). A signed `unit` ask
derives its spec's status, so the drift signal that counted backlog rows outliving closed specs, and
its pin, had nothing left to count.

## Shared seams

- `backlog.py` owns the grammar, the fold, the verdicts as data, READY and the view renderer; the
  generator, the planner, the relocation engine, the transition audit and the row driver import it
  and spell none of it a second time. It reads no tree.
- The one relocation recipe is `backlog.RELOCATION_RECIPE`, rendered by every view banner, the row
  driver's view-against-shard refusal and the generator's V17 remedy, and printed by
  `migrate_backlog.py --recipe`.
- The kit README's backlog-modes section is the author-facing statement of the grammar, and
  `gen_build_index.py --selftest` fails when a verdict code or row kind the module declares has no
  defining line there. It proves each is defined, not that the definition is true.
- `gen_build_index.py --asks --json` is what the agent carriers read — the review protocol, the two
  review harness lenses, the drift-audit Skill and the recall Skill — each falling back to the family
  shards when the output's `mode` field says `shards`, where the ask set is empty by design.

## Gaps

- The drift arm grades definition lines, not their meaning: a README line that says the wrong thing
  about a verdict passes.
- The transition audit reads MERGES. A rebase, a squash or a cherry-pick that drops a row leaves no
  merge behind and is invisible to it; that hole is stated in the module, not closed.
- A foreign text amendment — one session editing another build's ask row — is not stopped by
  anything mechanical.

## Reuse affordance

seam: `gen_build_index.py --asks --json` — reuse for reading ask status from a program; extend via the pinned field names `build_ask_row` returns.
seam: `backlog.extract_row` — reuse for classifying any backlog line; extend via a new verb constant, which the drift arm then requires a README line for.

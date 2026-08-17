# memory-recall — offline retrieval over the memory tree, with a floor that can fail

```toml
feature = "memory-recall"
title = "Conf-driven retrieval over the memory tree, and a merge-bar floor over a committed question set"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = [
  "memory-recall kit selftest",
  "memory-recall skill wiring",
  "recall floor",
  "recall floor arms",
]
kits = ["memory-recall"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = ["memory-recall"]
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/memory-recall/*",
  ".claude/skills/memory-recall/SKILL.md",
]
```

The kit answers "why is this repo the way it is" from its own records, offline and stdlib-only:
`extract.py` walks the corpus once, `bench.py` scores retrieval substrates, `query.py` serves the
CLI and the rendered Skill, and `check-recall.py` grades a committed question set against a declared
floor on the merge bar.

## Constraints & why

- **Stdlib only, offline, no model files.** The kit has to run on every node with nothing installed;
  the four lexical substrates stay importable without the optional dense stack, and a missing
  dependency raises with its install line rather than silently dropping an arm.
- **A query writes nothing inside the worktree.** `sys.dont_write_bytecode = True` sits ABOVE the
  sibling imports in every entry point, because CPython writes bytecode next to the SOURCE — which is
  inside the adopter's tree, and `__pycache__/` being a near-universal ignore rule means
  `git status` stays clean while it happens.
- **`bench.py` and `union.py` are byte-pinned** in `verbatim.json` and asserted by `selftest.py`. The
  floor gate therefore IMPORTS their scoring functions rather than extending them; `bench.py` always
  returns 0 and its flag set is closed, so the exit code has to live somewhere else.
- **The graded corpus is the SERVED corpus.** `extract.CHUNK_MAX` is 2400 and the live index is built
  at 600, so `check-recall.py` imports `query.CHUNK_MAX` rather than restating it — grading at the
  extractor's default would pin a substrate no session is served.
- **The floor is DECLARED and DERIVED, never recomputed from the run it grades.** `RECALL_FLOOR` in
  `.memory-tree.conf` names one CELL of the metric matrix as a single token, and its value is the
  one-retirement worst case `(h-1)/(R-1)`, not the day's score. A gate that recomputes its own
  threshold can never fail.
- **The floor is GOV-ONLY.** `kit.toml` withholds `recall-fixture.json`, `check-recall.py` and
  `test_recall_floor.py` through a `project-owned` rule claiming their destinations. An adopter's
  floor has to be measured against their corpus; shipping this one is
  `memory/gotchas/pin-copied-from-another-corpus.md`.

## Shared seams

- `recall_conf.resolve()` / `recall_conf.load_conf()` — the project layer every module reads. The
  floor gate takes `RECALL_FLOOR` through `load_conf` rather than a `Conf` slot, so `Conf.digest()`,
  the `KEY=VALUE` protocol `adopt-memory-recall.sh` parses, and the rendered Skill are all untouched
  by a value only the gate reads.
- `extract.corpus_files()` — the ONE corpus walk, for both the measurement path (`rev`-pinnable) and
  the query path (which also takes untracked-not-ignored files). There used to be two, and every
  widening had to teach both.
- `bench.expected_by_target()` — target-keyed expected hits. It DROPS an unresolvable target, so the
  per-id assertion is a set difference against its keys, never a search for an empty hit set.
- `bench.terms()` — the tokenizer. The fixture's overlap audit imports it so the audit and the index
  agree on what a content word is.

## Gaps

- **The fixture is twelve questions, not coverage.** The floor measures that these questions still
  find these records. A change that improves them while degrading a hundred others passes.
- **Only `records` is graded.** `chunks:fts5:r@5` measures 0.1667 against `records` 0.8333 on this
  fixture, because an id is a record-level target. Grading chunks needs a path- or passage-keyed
  fixture, which is its own unit.
- **The graded ensemble is not the served one.** `query.py` fuses records and chunks through RRF;
  the floor grades one set with one substrate, because `union.py` reports no `ceiling` and one `k`.
- **No adopter gets a floor.** The parked half of that decision is recorded in
  `TOOL-aWalkedCorpus-3` §8: an adopter-facing version needs a seeding path and a measuring verb that
  differ in what gets BUILT, not merely in configuration.
- **The pin's derivation is re-checked, not re-derived.** `--audit-fixture` prints `h`, `R` and
  `(h-1)/(R-1)` beside the declared value and reds when they disagree; nothing recomputes the pin,
  by design.

## Reuse affordance

seam: `check-recall.py` — the shape for any gate that pins a MEASURED number over a matrix. Three
parts travel: the pin names a CELL as one token so value and coordinate cannot drift apart; the value
is derived from a worst case rather than read off today's run; and the arms prove each direction can
red ALONE, because two checks that only ever fail together are one check wearing two names.

seam: `recall-fixture.json` — the shape for a question set that must not be a tautology. Every
question carries a `from` naming the record a person wrote, and `--audit-fixture` measures
content-term overlap against the union of the target's homes, redding above a declared `OVERLAP_MAX`.
A fixture authored by reading what the index returns scores ~1.0 there.

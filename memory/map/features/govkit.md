# govkit — the deployer, and the registry that is its population

```toml
feature = "govkit"
title = "govkit — a declared kit population, and the selfcheck that keeps it honest"
status = "building"
streams = ["deployer", "tooling"]
decisions = []

[claims]
gate-legs = ["govkit selfcheck", "govkit selftest", "govkit refusal join", "govkit acceptance matrix", "govkit runbook parity",
  "kit epoch (shipped bytes move, the version moves)", "step-rows-frozen"]
kits = ["govkit"]
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = ["deploy-governance"]
rendered-skills = []
gotcha-classes = ["fixture-lacks-a-gate-the-consumer-has.md", "a-new-local-collides-in-a-long-function.md",
  "guard-above-a-fold-makes-its-fallback-dead.md", "verdict-printed-before-the-step-that-reverts-it.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/govkit/*",
  "tools/govkit/entries/*",
  "tools/*/kit.toml",
  "skills/deploy-governance/*",
]
```

## Constraints & why

- `read_gate_verdicts` runs the target's runner with `GATE_REGEN_CHECK=0`, so a stale generated output reads as its own leg's red, never as an empty map apply could certify (DEPL-aPrimedIndex-1).
**The registry is a DECLARATION, and that is the whole design.** No directory listing equals the
deployable set, and the ways it fails are not symmetric. Some `tools/*` directories are not
deployable — `tools/lib/` ships nothing, and the gate-runner cluster is a stated non-goal because
gov's runner sources `tools/lib/` and exits 2 with zero legs run without it. Some entries are not
`tools/*` directories at all: the playbook is root files, the kickoff ratchet lives under `skills/`
and lands renamed and flat, and several single-file gates sit directly under `tools/`. One directory
carries TWO entries, because `tools/workflows/` versions its files under two kit ids. And one entry
writes ONE source to TWO destinations, because the agent-cap parity arm fails outright when the wired
copy is absent. `map_extractors._tool_kits()`'s own docstring records the same lesson from the other
side: README-gating "would have silently dropped three of ten".

**No population count appears in the spec or the registry, on purpose.** The spec stated two counts
across its life and both were true when measured and false when read — the `tools/` directory count
moved when the unattended kit landed, and the playbook file count was always one high because the
deploy-time catalogue it counted was prose to READ, never a file the entry shipped — and v3.0 then
deleted that catalogue outright. `selfcheck` derives every figure at the moment it
checks. A number in that prose is now a defect in the document.

**The DEFAULT selection is declared in the registry, not the engine.** It began as a constant in
`govkit.py` and a scratch fixture caught what that meant: the engine named five kits by hand while the
registry named the population, so any registry but gov's own reported five entries missing. Two
answers to one question, inside the tool whose thesis is that there should be one. `--all` was already
derived; the default set now comes from the same single source.

**The surface predicate is the ratchet.** Every tracked path in the declared surface — depth-1 under
`tools/`, everything under the hook and kickoff trees, and the shipped root playbook files — is an
entry, a member of exactly one entry's file rules, or an exemption carrying a non-empty reason. It is
asserted in BOTH directions, and an exemption naming a path that no longer exists reds: a stale
exemption silently widens the surface it was written to narrow. This replaces a predicate that
quantified over `tools/*` DIRECTORIES and therefore left every single-file deployable the runbook
already prescribes in no population at all.

**A new predicate is run over the real tree before it is trusted, and this one earned that rule.**
Its first run found seven problems, three of them real defects in the descriptors it was reading:
sources for an entry whose bytes straddle the install prefix and a verbatim repo-root path were being
resolved against the wrong tree, a destination TEMPLATE carrying `{relpath}` was being compared as if
it were a literal destination, and one tracked hook was claimed by nothing. All three are fixed and
the fix for the first is the `root_relative` rule flag.

**`repo_root()` walks up for the registry rather than asking git.** Two measured reasons. A
`git -C <dir> rev-parse --show-toplevel` returns `<dir>` itself when an absolute `GIT_DIR` is
inherited — which is exactly what git exports to a merge driver in a linked worktree, and how the
row-keyed merge driver was found to be inert in this repo. And a fixed `parents[]` index is correct
at only one install prefix. The walk inherits nothing and is correct at any prefix. Where govkit
does need a remote — gov's currency check and `epoch`'s default base — it asks the inlined remote
ladder (`resolve_remote`, `GOV_REMOTE` first), never a literal `origin`; a ladder refusal is an
`unverified` or a failed exit naming it, never a guessed remote.

**A target's own edit to a gov-owned leg row is drift, except its ceiling.** `write_gate_legs`
compares the target's row against what the RECEIPT recorded, never against gov's fresh descriptor,
so a new gov vintage lands on an untouched row and a hand-edited `argv`, guard or `doc_reads` is
reported rather than overwritten. A `ceiling` that differs from the receipt's is the adopter's own
bound: it is written back and reported, outside the drift comparison, so it can never withhold
the manifest. A DELETED ceiling is not preserved — it takes gov's value back.

**`update` carries an exec bit up and never down.** `resolve_landed_mode` is the one mode rule: an
existing `engine` row keeps its mode except `100644` where gov ships `100755`, and a symlink is left
alone. `update` prints a `mode-carry` line per carried row; `check` notes a mode deficit and never
fails on one, because redding a target over a bit it chose is not gov's call.

## Shared seams

- `tools/govkit/registry.toml` — the population: entries with their descriptor paths, the surface
  globs, and the exemptions with their reasons.
- `tools/govkit/govkit.py` — `selfcheck` (and `selfcheck --fix`, which writes every kit-version
  carrier from its entry's `version_from` constant), the read-only `shipped`, `plan`, `check`,
  `update` and `adopt`, the writing `apply` / `apply --resume` with the receipt, `intake`, and the
  version pair `epoch` / `mint`. **The COUNT is not spelled**, here or in that file's docstring:
  this line read "all five verbs" from the commit that landed the sixth, and `USAGE` and `main`'s
  dispatch tuple own the set between them with a selftest arm joining the two. `apply` lands the
  roles it can honour, prints one `SKIPPED` line per rule it does not land, naming the role and who
  does produce it, and refuses the rest BY NAME. `adopt` is the BOOTSTRAP — it writes the receipt
  an already-installed tree never had by measuring that tree against gov's own history, and it is
  the only path onto the engine for a repo somebody vendored kits into by hand.
- `epoch` / `mint` — one verdict, `derive_epoch_state`, read by both. `epoch` fails a kit whose
  shipped bytes moved with no version bump; with no explicit base and no `GATE_PUSH_BASE` it
  reports such a move as `owed at the lander` and passes it. `mint`, which `push-main.sh` runs
  while it prepares a landing, writes the next version of every kit `epoch` would fail into every
  carrier, so a branch owes no bump of its own.
- `write_gate_legs` — the ONE leg emitter, shared by `apply` and `update`, into a target runner of
  `[gate_runner] kind = "manifest"` (the `json-array` grammar, deduped by `name`). Each optional
  row key travels only when the target's INSTALLED run-gates can read it, measured from its version
  constant against a floor beside the emitter: `subject`, `doc_reads` and `ceiling` each have one,
  an unreadable version reads as below the floor, and a target with no run-gates gets every key. `doc_reads` is all-or-nothing against the
  target's tracked tree, since a list that loses one element skips the leg on exactly that doc push.
- `tools/check-install-prefix.sh` — ONE pure ban since `TOOL-aRepatriatedFork-30`: any kit-path
  spelling in the tracked shipped surface reds by `<path>:<line>`, with no ratchet, waiver or
  marker to buy one back. Its dossier is `install-prefix.md`.
- `tools/govkit/selftest.py` — every refusal and reported state, exercised in throwaway repos. Each
  arm asserts a specific MESSAGE or on-disk effect, never an exit code alone: an exit code shared by
  six unrelated outcomes is the ambiguity the descriptors' outcome probes exist to resolve.
- `tools/<kit>/kit.toml` — a descriptor beside each kit that is a directory.
- `tools/govkit/entries/<id>.kit.toml` — a descriptor for each entry with no kit directory of its
  own.

## Reuse affordance

seam: `registry.toml` — reuse for any question of the form "what is the deployable population and who
owns this path"; extend via a new `[[entry]]` with its descriptor, or an `[[exempt]]` row carrying a
non-empty reason. Never by editing a listing.

seam: `govkit.py selfcheck` — reuse for asserting a declared population against a tracked surface in
both directions; extend via a new arm inside `selfcheck`, which is the single home for every
registry-shaped assertion this unit adds.

seam: `derive_marker_coupling` — reuse for "which kits must move together because one ships the
other's version marker", read from each descriptor's `marker_carriers` and owned through
`entry_members`; `update --kits` closes its scope over it. Extend via a descriptor's
`marker_carriers`, never by naming a kit pair in code.

seam: `refusal_join.py` — reuse for "is every branch of this shape reached by something that
asserts it", over any Python population; extend via the matcher in `_is_refusal`, which is the one
place the branch SHAPES are named. Its anchor is module-function-ordinal rather than a line, so it
survives edits above the branch.

## Gaps

Named rather than assumed, because a deployer that is quiet about its own holes is the thing this
unit exists to replace:

- **`rendered` rows are never copied.** They are produced by the ADOPTERS, so govkit copying one
  would be a second renderer racing the real one; the receipt records them, `apply` prints them
  `SKIPPED`, and selfcheck 3b-ii refuses a descriptor shipping a `rendered` row with no
  `[[regenerate]]` argv, since that is how `update` refreshes one. `merged` rows DO land now:
  `apply` writes the source's marker block into the target's file through `write_block`, by line
  index so an edit outside the block survives, and a `json-pointer` block is delegated to the
  adopter at CONFIGURE. The `.gitattributes` LF-pin block and the renormalize that follows it are
  `apply`'s ATTRIBUTES and RENORMALIZE steps.
- **The gate-runner emitter speaks one grammar, and the CI emitter is not built.** `kind =
  "manifest"` is implemented; `make`, `npm` and `shell` are refused by name rather than half-written.
  `[gate_runner.ci]` is only validated (`github-actions` is the one system accepted), and a `ci`
  receipt row is report-only: nothing writes a CI job into a target.
- **The runbook parity gate grades presence, not prose.** `check_runbook_parity.py` keys
  `WIRE-INTO-PROJECT.md`'s sections to registry entries by an entry-id HTML-comment anchor, in both
  directions, and reds an anchor whose section body is empty. It cannot tell a correct sentence
  from a wrong one, and its header says so.
All three AC10 assertions that were open have landed: the version cross-check, the guard-class
partition, and the derived `mutates_index`. Each carries a LIVENESS arm in the selftest — a scratch
gov tree fed input that must red — because an assertion finding nothing on a clean tree is
indistinguishable from one that cannot find anything, and that is this repo's own
`fixture-passes-by-finding-nothing` class.

**The guard partition has a sixth class, and guards are graded for COMPLETENESS.** A root file some
descriptor declares as its `[config] file` is `root-conf`, derived and never listed, so a guard can
name the conf its own leg reads; a root file nobody declares still falls into no class and reds 7c.
Check 7c2 then reds a guarded bar leg, unheld by the runner's own predicate, whose tracked argv bytes
name a declared root conf its guard lacks. A conf reached through a same-directory import or a
literally sourced file prints as a report-only near-miss, since a transitive rule would red on every
shared library. Its liveness refusal needs a declared conf, because a manifest with no guarded bar
leg and nothing to protect is a true zero. Both counts it prints are derived, never written here.
TOOL-dDerivedDocket-21.

**A self-test gov holds must ship held.** Check 7j4 calls a descriptor `[[gate_leg]]`
self-test-shaped when its manifest chunk is `selftests` or a resolved argv basename matches
`*.test.sh`, `test_*.py` or `*selftest*`; a shaped leg filed in any other chunk is exempt, because
gov runs it on every bar. A shaped, non-exempt leg whose descriptor `subject` is not `kit` reds,
since every adopter would run it on its default bar while gov holds it. Its zero-graded and
zero-shaped liveness reds bind only while gov's manifest holds a row in chunk `selftests`, and an
absent manifest is a note, as 7h treats it. Beside it, 7h holds a descriptor's `doc_reads` equal to
gov's manifest row, and a declared `ceiling` to a positive integer equal to the manifest's, because
the emitter carries both verbatim into adopters. The selftest stages 7j4's and the ceiling
clause's breaks in `check_benched_probe_arms` and exercises the ceiling's emission and keep rule in
`check_ceiling_emission`. DEPL-aBenchedProbe-1, DEPL-aBenchedProbe-2.

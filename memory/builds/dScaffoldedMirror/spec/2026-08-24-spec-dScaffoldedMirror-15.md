# TOOL-dScaffoldedMirror-15 — wire the runbook-parity gate, and pay what wiring it costs

**Status:** DEFERRED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling · correct work, not lexicon work; S3 dies permanently

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md](../build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md) | spec-audit | TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/govkit/check_runbook_parity.py` works, exits 1 today naming eighteen registry entries with no
anchored runbook section, has zero callers and is absent from `tools/gate-legs.json`. So a
hand-wiring adopter is never told that eighteen deployables exist, which is the mechanical reason
this repo's kits have a live adoption count of one. **This is not the lexicon's own work** — the
lexicon is one of the eighteen, at output line 12, and is the reason the gap was found rather than
the reason it matters. Wire the gate, and answer all eighteen, because wiring it without answering
them reds the bar.

## 2. Scope (IN)

- **S1** — write an anchored runbook section for each of the eighteen unanchored entries, sized by
  kind per §4, so `check_runbook_parity.py` exits 0 on a tree it currently reds.
- **S2** — add the leg to `tools/gate-legs.json`, guarded on `tools/govkit/registry.toml` and
  `WIRE-INTO-PROJECT.md`, in the commit where the count first reaches zero and not before.
- **S3** — declare the leg in the govkit descriptor that owns it, so an ADOPTER receives it. That is
  the whole point: a parity gate that only ever runs here proves gov's runbook is complete and tells
  a target nothing.
- **S4** — claim the new gate-leg key in the codebase map in the same commit, per the map's coverage
  ratchet.
- **S5** — carry the gate's own stated limit into the leg row: it asserts that every deployable has
  a section and every section names a deployable, and it cannot tell a correct sentence from a wrong
  one. Its header already says this; the leg row must not imply more.

## 3. Non-goals (OUT)

- **No change to `check_runbook_parity.py`.** It is correct, both-directional, has a liveness half
  that reds on an empty body, and states what it does not do. The defect is that nothing runs it.
- **No use of `runbook_exempt` to reach green.** The mechanism exists and is hardened — an empty
  reason reds, an id naming no entry reds — and §4 explains why reaching for it here would produce a
  gate covering seven of twenty-five entries.
- **No narrowing of the gate's population.** Restricting it to non-`conditional` entries would make
  it pass by grading less, which is an exemption wearing a scope's clothes.
- **No generated runbook sections.** The descriptors carry `[adopt]`, `[check]` and `[[gate_leg]]`
  tables that a renderer could turn into a section skeleton. That is a second generated artifact with
  its own freshness gate, and it is not this unit.
- **No lexicon work.** The lexicon's section is one of the eighteen and gets the same treatment as
  the other seventeen. Nothing about `.lexicon.conf`, the predicates or the pins is touched.

## 4. Design

### The measurement, taken 2026-08-24 on this worktree

`python tools/govkit/check_runbook_parity.py` prints eighteen `has no anchored runbook section`
lines, then `7 anchored section(s) · 25 registry entr(y|ies) · 0 exempt`, then `18 problem(s)`, and
exits 1. `git grep -l check_runbook_parity` matches three files, all of them records —
`memory/backlog/TOOL.md`, this build's research record, and the generated
`memory/map/generated/symbols.json`. No script, no leg, no hook.

### The eighteen split cleanly in two, and that is what makes this affordable

Nine are directory kits declared by a `<dir>/kit.toml`: `playbook-render`, `run-gates`,
`agent-instructions`, `unattended`, `pytest-parallel-guardrails`, `gate-lint`, `lexicon`,
`agent-cap` and `review-harness`.

Nine are single-file gates declared under `tools/govkit/entries/`: `check-line-length`,
`check-microformats`, `check-placeholders`, `settings-merge`, `check-testsuite-counts`,
`check-wiring`, `check-kit-versions`, `check-agent-cap-restatement` and `check-install-prefix`.

The nine single-file gates are one script and one declaration each. Their whole wiring story is the
command, where the target's declaration lives, and what the gate does not grade — three or four
sentences. The nine directory kits need a real section apiece.

### The budget, measured rather than guessed

`WIRE-INTO-PROJECT.md` is 51,481 bytes over 684 lines. Its seven existing anchored sections run 641
bytes (`kickoff-manifest`, 17 lines) to 16,662 bytes (`push-main`, 205 lines), median 4,141, 46,421
bytes in total. Two shapes are therefore already on the record: a 17-line section is enough for a
one-command install step, and a 205-line one is what a kit with real forks costs.

Sizing this unit off those two: nine short sections at roughly the `kickoff-manifest` shape, and
nine kit sections at well under the median because they document adoption rather than argue design,
lands at approximately +20 KB and +300 lines. That is a 40% growth of the runbook, and it is the
real cost of this unit. The wiring itself is three lines of JSON.

### The fork, priced

| option | day-one cost | what the gate grades | verdict |
|---|---|---|---|
| write all eighteen, then wire | +20 KB, several commits | 25 of 25 | recommended |
| exempt all eighteen, wire now | one commit | 7 of 25 | rejected |
| narrow to non-`conditional` entries | one commit | whatever already passes | rejected by name |
| generate from descriptors | a second artifact | 25 of 25, plus a freshness gate | out of scope |

**Why exemption is rejected even though the mechanism is built for it.** `runbook_exempt` is the
right tool for an entry with genuinely no adopter-facing wiring story. None of the eighteen is that:
every one is a real deployable `govkit apply` can install into a target, and an entry a target
receives with no instructions is the exact gap this gate was written to measure. Eighteen exemptions
carrying the same sentence would satisfy the gate's non-empty-reason rule while emptying it of
meaning — coverage by declaration, which this repo's own charter calls an exemption rather than a
check.

**Why narrowing is rejected by name.** Redefining a gate's population to what already passes is the
pin-shaped move: it produces a green run and grades strictly less than it did before anyone looked.
It is listed here so that a future session meeting a red parity gate finds the argument already made.

### Rollout: the gate lands last

Sections land first, in bounded commits; `check_runbook_parity.py` is run by hand after each and its
problem count is quoted in the commit message, so the drain is visible. The leg, the descriptor row
and the map claim all land together in the commit that takes the count to zero. Wiring a leg that
reds is how a gate gets `--no-verify`'d into irrelevance, and this one has already spent its whole
life being ignored.

### Alternatives rejected

- **Wire it now and let the bar be red until the sections land.** A red default branch is the
  landing-day failure this build's Phase 0 unit already priced, and here it would last for as many
  commits as eighteen sections take.
- **Write the sections and never wire the gate.** That is today's state plus prose. The eighteen
  would drift back out of parity with no signal, which is the drift the gate exists to catch.

### Files touched (estimate)

`WIRE-INTO-PROJECT.md` (+~300 lines, eighteen anchored sections), `tools/gate-legs.json` (one leg),
the govkit descriptor that owns `check_runbook_parity.py` (one `[[gate_leg]]` row), and one map
dossier claiming the new gate-leg key.

## 5. Production-readiness checklist

- **security** — N/A. A parity check over two tracked files; no input, no network, no write path.
- **perf / scale** — the check parses one TOML registry and one markdown file. It is milliseconds
  against a bar whose longest leg is measured in minutes, and it is guarded to two paths besides.
- **a11y** — N/A. A CLI gate and a markdown runbook.
- **i18n** — N/A.
- **error / empty / loading states** — the gate already handles all three honestly: a missing runbook
  reds, an anchor with an empty body reds, and zero anchors reds with `this gate would pass
  vacuously`. Nothing here needs adding, and inheriting a checked empty state rather than writing one
  is worth saying.
- **observability** — the summary line (`N anchored · M entries · K exempt`) is the observability,
  and it derives all three figures rather than restating any. No count is written into prose here or
  into the leg row.
- **risks** — the real risk is eighteen sections written to clear a gate. The gate's own header names
  this: an anchor with nothing under it *reads as covered*, which it calls worse than an absent one.
  A body that is technically non-empty and substantively hollow passes the machine check and fails
  the reader, and no automation reaches it. The compensating control is that each section states a
  command a reader can run.
- **testing + left-shift gates** — the leg IS the left-shift. Its failing case is already observable
  with no staged break: the gate reds on this tree today, and it will red again the moment a new
  registry entry lands without a section, which is the class.
- **migration / rollback** — none. Rollback is removing the leg row; the sections are prose and harm
  nothing if the gate is dropped.
- **user docs** — this unit is eighteen user docs. That is the unit.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/check_runbook_parity.py` runs on the landed tree, it prints no
  problem line at all, its summary reads `25 anchored section(s) · 25 registry entr(y|ies) · 0
  exempt`, and it exits 0. Today the same command prints eighteen problem lines and exits 1.
- **AC2** — When a new `[[entry]]` is added to `tools/govkit/registry.toml` with no anchored section,
  `python tools/govkit/check_runbook_parity.py` exits 1 naming it. Staged, observed RED, unstaged —
  the gate is being wired, not written, so its failing case must still be watched once here.
- **AC3** — When an anchored section's body is emptied, the gate reds with its `EMPTY body` message.
  Staged and observed, because that liveness half is the reason a presence check was not enough and
  it has never been exercised on this tree.
- **AC4** — When `bash tools/run-gates/run-gates.sh` runs on a commit touching
  `WIRE-INTO-PROJECT.md`, the new leg appears in the leg list and reports a verdict rather than
  being skipped, proving the guard names live paths.
- **AC5** — When `python3 tools/codebase-map/test_codebase_map.py` runs after the change, it is
  green, so the new gate-leg key is claimed by a dossier rather than sitting unclaimed in
  `memory/map/baseline.toml`.
- **AC6** — When the govkit descriptor is applied to a target, the target receives the parity leg;
  observed through `python tools/govkit/govkit.py selfcheck` staying green with the new
  `[[gate_leg]]` row declared.
- **AC7** — When any of the eighteen new sections is read, it names at least one runnable command
  for that entry, as the existing `kickoff-manifest` section does in 17 lines. This is the
  documented check against a hollow body; it is a review item rather than a machine one, stated so
  nobody mistakes AC1 for it.

## 7. Gates

Keeps green: `govkit selfcheck`, `govkit selftest`, `govkit refusal join`, `govkit acceptance
matrix`, `codebase-map coverage + freshness`, `line length`, `memory hygiene`, and the three lexicon
legs — `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring` — which this unit leaves
untouched and which are named because every spec in this build names them.

**Adds one leg**, and it is a genuine addition rather than a refusal inside an existing one: nothing
on the bar reads `WIRE-INTO-PROJECT.md` against the registry today, so there is no existing leg to
extend. `WIRE-INTO-PROJECT.md` carries no row in `tools/line-length-limits.txt` and is therefore
graded at the 450-character default, which the new sections must respect.

**What this unit does NOT check.** The gate cannot tell a correct instruction from a wrong one, and
neither can the leg. A section that documents the wrong command passes. What lands is the assertion
that every deployable has a section and every section names a deployable, which is the claim the
runbook's usefulness rests on — and it is a weaker claim than "the runbook is right".

## 8. Open questions

- **F1 — eighteen sections, eighteen exemptions, a narrowed population, or generated sections?**
  Priced in §4. RECOMMENDATION: eighteen sections, sized by kind, with the gate wired in the commit
  that takes the count to zero. Exemption produces a gate grading seven of twenty-five; narrowing is
  the pin-shaped move; generation buys a second artifact and a freshness gate to keep it honest.
  RESOLVED (agent, 2026-08-24, delegated): write the eighteen, wire last.
- **F2 — is the wiring blocked until all eighteen land, or does the leg go in guarded and skipped?**
  A guard that never matches would skip forever and silently, which the run-gates canary already
  refuses. RECOMMENDATION: blocked. The leg lands with a guard naming two paths that both exist and
  both move. RESOLVED (agent, 2026-08-24, delegated): blocked until zero, then landed guarded on
  `tools/govkit/registry.toml` and `WIRE-INTO-PROJECT.md`.
- **F3 — does this unit write all eighteen sections, or does it wire the gate and hand the prose to
  eighteen owners?** Genuinely the owner's, and left UNRESOLVED: it is a scope question about how
  much runbook prose one unit should carry, and this build has no other unit to hand it to.
  RECOMMENDATION: this unit writes all eighteen. Splitting them leaves the gate unwired for as long
  as the slowest owner takes, and an unwired gate is the exact state this unit exists to end.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on the `dScaffoldedMirror` research pass
  (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`, diagnosis B4 and
  demand 3, which places wiring this gate upstream of promising anything to an adopter) and on the
  read-only probe of `incms/main` taken the same day, which found a full gov adopter carrying no
  `.lexicon.conf`. Every figure in §4 was re-measured on this worktree at writing time.
- rev-1 status 2026-08-24 · DEFERRED and recommended for RE-FILING out of this build - its own section 1 says it is not lexicon work. S3 dies permanently: it ships a leg whose script, registry and subject are all declared un-shippable, and AC6 observes gov to certify a target. The +20 KB of runbook prose across eighteen sections is the single largest schedule item in the build, and it makes a lexicon build's completion depend on seventeen unrelated deployables.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py runbook parity registry anchor deployable wiring` returns
`anchors` (`tools/memory-tree/merge-rows.py`, fan-in 7, SEAM), `anchor_at`
(`tools/memory-recall/extract.py`, fan-in 2), and the `registry.toml` affordance seam on the `govkit`
dossier. **No existing seam fits for the wiring, and the honest reason is that the mechanism already
exists**: `check_runbook_parity.py` is written, correct and complete, so this unit adds no code at
all and has nothing to route. The two `anchor` hits are different mechanisms wearing the same word —
`merge-rows.anchors` locates row keys for the merge driver and `extract.anchor_at` locates a chunk
offset for recall — and adopting either would be a name collision mistaken for reuse. The
`registry.toml` seam IS the right one to READ: it is the population both directions of the gate
quantify over, and S3's descriptor row is written against it rather than against a hand-kept list.
The reuse decision this unit records is therefore a refusal to build: the gate exists, and the work
is prose plus three lines of declaration.

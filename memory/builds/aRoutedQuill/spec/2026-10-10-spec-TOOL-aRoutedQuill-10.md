# TOOL-aRoutedQuill-10 — the push boundary's routed-commits run grades the whole history beside the pushed range

**Status:** SPECCED · rev-1 · 2026-10-10 · node a · Tier-2 · base e6585db4 · streams tooling · order 8 · ratified 2026-10-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-10-prompt-TOOL-aRoutedQuill-10-build-brief.md](../prompts/2026-10-10-prompt-TOOL-aRoutedQuill-10-build-brief.md) | journal | — |
| [2026-10-10-prompt-TOOL-aRoutedQuill-10-spec-brief.md](../prompts/2026-10-10-prompt-TOOL-aRoutedQuill-10-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

At the pre-push hook the routed-commits leg grades only `$GATE_PUSH_BASE..HEAD`, while remote CI
grades all of HEAD's history, so a push can land a red that only CI sees (closing review H1, and
the left-shift its B1 names). This unit makes the push-boundary run grade the whole history too,
beside the pushed range, so the landing push sees what remote CI will see.

## 2. Scope (IN)

- **S1** — When `derive_commit_range` in `tools/memory-tree/routed_commits.py` yields RANGE,
  `check_routed_commits` grades two populations and exits 1 when either reds. The RANGE half is
  graded exactly as today and reads no waiver. The WHOLE half is HEAD's whole history, graded
  exactly as WHOLE mode grades it today, `ROUTED_COMMIT_WAIVED` and the stale-waiver rule included.
  The trigger is the resolvable base alone, never the shape of the range. Observed by AC1 and AC2.
- **S2** — The RANGE half keeps its own verdict: a pushed violation that `ROUTED_COMMIT_WAIVED` lists
  still reds, and a stale waiver reds at the push boundary as it does in CI. Observed by AC3.
- **S3** — The output keeps today's RANGE summary line byte for byte and adds a second summary line
  for the WHOLE half, labelled `WHOLE beside RANGE`, with the same counts today's WHOLE line prints.
  A violation is listed once: the WHOLE half lists only shas the RANGE half did not, under its own
  FAILED heading. Observed by AC1 and AC2.
- **S4** — Cost stays a constant number of git spawns whatever either population holds. The id map
  and the conf are read once and shared; the WHOLE half adds one log pass, one `rev-list --count`
  and at most one `cat-file --batch-check`. Observed by AC4.
- **S5** — Every context that reads WHOLE today (the variable unset, all zeros, or naming no commit)
  is unchanged: one summary line, no `WHOLE beside RANGE` line. Observed by AC5.
- **S6** — The carriers that state the push boundary reads no waiver are corrected: the module
  docstring's THE RANGE paragraph, the kit README's `routed_commits.py` row, the
  `ROUTED_COMMIT_WAIVED` comment in `tools/memory-tree/.memory-tree.conf.example` and in gov's
  `.memory-tree.conf`, and the routed-commits paragraph of the
  `memory/map/features/memory-tree-hygiene.md` dossier. Observed by AC6.

## 3. Non-goals (OUT)

- No edit to `.githooks/pre-push`, `tools/run-gates/run-gates.sh` or `tools/gate-legs.json`. The
  hook already exports the base and the runner already runs the leg with no guard on every bar; the
  seam is the leg.
- No `signature` row and no `--offenders` verb for the leg, so an inherited-only WHOLE red does not
  land under `INHERITED_RED=land` (§8 F1).
- No change to what a commit must carry, to `ROUTED_PATHS`, to the cutoff, or to the waiver
  grammar. The waiver VALUES at the landing tip are the preceding unit's.
- No new function. The grading block runs once per population inside `check_routed_commits`, so
  nothing new reaches the lexicon leg or `memory/map/generated/symbols.json`.

### Edges

- **consumes-from** `TOOL-aRoutedQuill-9` — a waiver set complete for every cutoff-day commit at the
  landing tip. Without it this unit's own landing push reds on the WHOLE half, naming d6aae9d1,
  22efab65 and 670436cd, and its edit to the waiver comment would collide with that unit's.
- **hands-off** external — an owner turn on whether the leg gains a `signature` so an inherited-only
  WHOLE red can land under the inherited-red policy (§8 F1).

## 4. Design

### Evidence

- `derive_commit_range` (`tools/memory-tree/routed_commits.py:199-211`) returns RANGE over
  `<base>..<head>` when `GATE_PUSH_BASE` resolves, else WHOLE over `HEAD` with its reason.
  `check_routed_commits` (`:228-300`) applies `ROUTED_COMMIT_WAIVED` and the stale check only when
  the mode is WHOLE (`:278`).
- `.githooks/pre-push:1561` exports `GATE_PUSH_BASE` as the remote's sha before the push, on a
  default-branch push only; a branch bar unsets it (`:949`). Every other context grades WHOLE,
  remote CI included.
- The class is live today. Measured on node a, 2026-10-10, PINNED: at 4edeb467,
  `GATE_PUSH_BASE=$(git rev-parse origin/main) python tools/memory-tree/routed_commits.py` exits 0
  (`RANGE e6585db4..4edeb467 · graded 8 · 2 merge(s)`), and the same command with the variable
  unset exits 1 naming d6aae9d1, 22efab65 and 670436cd, all three ancestors of origin/main. The
  preceding unit waives them, so this instance does not survive to this unit's build; the arms in
  AC1 and AC2 are the observation.
- Cost, measured on node a, 2026-10-10, PINNED: the WHOLE run over this repository took 2.8 s wall
  (4517 exempt, 462 merges, 45 graded), against the leg's 300 s ceiling. The RANGE half already
  pays the spec read, so the WHOLE half adds the log pass and one batch read.
- Attribution. The leg's row in `tools/gate-legs.json` declares no `signature`, so
  `run-gates.sh` reads a red as INHERITED only when the normalised output at L and at R is
  byte-identical (`:3259-3264`). The RANGE summary line carries the head's short sha, so it never
  is. A WHOLE red at the push therefore reads OWN or MIXED and blocks, whether or not R carried it.

### The two populations

| Context | `GATE_PUSH_BASE` | Graded | Waiver read |
|---|---|---|---|
| `.githooks/pre-push`, default-branch push | the remote's sha before the push | RANGE, then WHOLE beside it | WHOLE half only |
| the same, a push creating the branch | all zeros | WHOLE | yes |
| a worktree or branch bar, a declared branch bar, CI, an adopter's bar | unset | WHOLE | yes |
| any, the variable naming no commit in this clone | set | WHOLE, the reason printed | yes |

Only the first row changes. The refusals (S7 of the push-leg unit) run before either population is
graded and are shared, so a refusal still exits 2 with nothing graded.

### Output

```text
routed-commits: RANGE <base8>..<head8> · graded <n> · ... (today's line, unchanged)
routed-commits: WHOLE beside RANGE (the history remote CI grades) · graded <n> · <x> exempt by the <cutoff> cutoff · <m> merge(s) · <r> not routed · <w> waived · <k> spec id(s) at HEAD · ROUTED_PATHS <value>
routed-commits FAILED — a commit touching ROUTED_PATHS names no unit specced before it:
  <sha8> <subject> — <ids or "no unit id"> — <reason>
routed-commits FAILED in WHOLE — a commit outside the pushed range names no unit specced before it, and remote CI grades it:
  <sha8> <subject> — <ids or "no unit id"> — <reason>
```

A half that grades nothing prints today's `graded 0` line; the WHOLE half's carries `WHOLE` after
the `routed-commits:` prefix. Stale-waiver lines print as today, from the WHOLE half.

### Inventory

No identifier is minted. The second population is a loop over a two-row list inside
`check_routed_commits`; the strings `WHOLE beside RANGE` and `FAILED in WHOLE` are output, not names.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py` — S1 to S5, the docstring, and the new self-test arms.
- `tools/memory-tree/README.md` — the `routed_commits.py` row.
- `tools/memory-tree/.memory-tree.conf.example` — the `ROUTED_COMMIT_WAIVED` comment.
- `.memory-tree.conf` — the `ROUTED_COMMIT_WAIVED` comment only; its value is the preceding unit's.
- `memory/map/features/memory-tree-hygiene.md` — the routed-commits paragraph, refreshed on touch.

### Rollout

The unit builds after TOOL-aRoutedQuill-9, which leaves the WHOLE half green at the tip. The
closing review's minors batch, TOOL-aRoutedQuill-12, also edits `routed_commits.py` (its M3 and M7
items), so the two never build concurrently; their order verbs sequence them. The memory-tree kit's
shipped bytes move, and the version bump is the build's once-per-kit mint after its last
memory-tree unit, per the build README's rule; this unit mints none.

### Alternatives rejected

Each candidate was written down with what would make it lose before the probe ran.

- **B. Grade WHOLE beside RANGE only when the pushed range holds a merge**, the brief's trigger. It
  loses if a WHOLE-only red can reach main through a range with no merge. Probe, node a, 2026-10-10,
  in a `git clone --local` of 4edeb467 under `%TEMP%`: one commit added the three cutoff-day shas to
  the waiver list, then a second, linear, conf-only commit omitted 61c3a3aa47a0 from it. With
  `GATE_PUSH_BASE` at the first commit the leg read `RANGE · graded 0 · 0 merge(s)` and exited 0;
  with the variable unset it exited 1 naming 61c3a3aa. A merge trigger would not have fired, so B
  is rejected. The same holds for any conf edit that widens `ROUTED_PATHS`, moves the cutoff earlier
  or edits `FAMILIES`, and for a spec moved since an old commit named it.
- **C. A second leg row, or a second run in the hook, with `GATE_PUSH_BASE` unset.** It loses if
  the row would grade the same population twice in contexts that already read WHOLE. The context
  table above shows three of the four contexts unset the variable, so a second row is a duplicate run
  and a duplicate red there, and a hook edit ships verbatim to every push-main adopter. Rejected.
- **A, chosen.** Unconditional on a resolvable base, inside the leg. It loses if the WHOLE pass
  costs the push materially; 2.8 s against a 300 s ceiling says it does not.

## 5. Production-readiness checklist

- security — Read-only, as before. The push boundary gains a check rather than losing one: RANGE
  still honours no waiver, and the WHOLE half honours only the committed conf, which the hook's
  dirty-tree refusal already pins to the pushed sha.
- perf / scale — One more log pass and batch read per push, 2.8 s over gov's history (PINNED, node a,
  2026-10-10), growing linearly; S4 keeps spawns constant.
- error / empty / loading states — Refusals are shared and precede both halves; each half prints its
  own `graded 0` line.
- observability — Two summary lines name both populations; the WHOLE list names each sha once.
- risks — A WHOLE red that R already carries now blocks a default-branch push instead of passing it,
  because it cannot read INHERITED (§4 Evidence). The remedy is a `ROUTED_COMMIT_WAIVED` entry in
  the pushed commits, which the WHOLE half honours. One `--no-verify` push to main by any node
  therefore blocks every node's next push until someone waives it.
- testing — New `--selftest` arms in `routed_commits.py`; the held leg keeps its 80 s budget row
  (the suite measured 22 s on node a, 2026-10-10, PINNED).
- migration — N/A — no data or conf shape changes; an adopter's conf reads the same.
- user docs — The kit README row and the example conf comment (S6).

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/routed_commits.py --selftest` runs, an arm builds a
  scratch history whose remote side carries an unattributed post-cutoff commit reaching HEAD through
  a merge, sets `GATE_PUSH_BASE` to that remote tip, and observes exit 1, the RANGE summary line,
  a `WHOLE beside RANGE` line, and the remote commit's sha under `FAILED in WHOLE`.
  Red when: the WHOLE half is not graded at a resolvable base, which is today's code, and the run
  exits 0.
  cost: about 25 s for the whole self-test, which is the only way to run one arm.
- **AC2** — When the same `--selftest` runs, an arm grades a linear range holding no merge at a
  resolvable base, with a conf whose `ROUTED_COMMIT_WAIVED` omits a needed sha, and observes exit 1
  naming that sha; with the sha listed it observes exit 0 and `1 waived` on the `WHOLE beside RANGE`
  line.
  Red when: the WHOLE half is gated on the range holding a merge, as candidate B would gate it.
- **AC3** — When the same `--selftest` runs at a resolvable base, a pushed violation that
  `ROUTED_COMMIT_WAIVED` lists still exits 1 under the RANGE heading, and a waiver naming no
  violation exits 1 with the stale line.
  Red when: the RANGE half starts reading the waiver, or the stale check stays WHOLE-mode only.
- **AC4** — When the same `--selftest` runs, the spawn arm also runs with `GATE_PUSH_BASE` at the
  first commit for 3 and for 30 routed commits, and observes equal `GIT_SPAWNS` deltas.
  Red when: the WHOLE half spawns per commit or per id.
  figure: the counts are DERIVED at observation time; only their equality is asserted.
- **AC5** — When the same `--selftest` runs, the existing unset, all-zeros and unresolvable-base arms
  also assert that the output carries no `WHOLE beside RANGE` line.
  Red when: the WHOLE half runs in a context that already reads WHOLE.
- **AC6** — When `grep -n "WHOLE mode only" tools/memory-tree/README.md` and
  `grep -n "push boundary grades the pushed range and reads none" tools/memory-tree/.memory-tree.conf.example`
  and `grep -n "never at the" .memory-tree.conf` run, each prints nothing, and
  `grep -c "beside" tools/memory-tree/README.md memory/map/features/memory-tree-hygiene.md` counts at
  least one per file.
  Red when: a carrier still says the push boundary reads no waiver or grades only the pushed range.

## 7. Gates

The close runs these; a pass runs only the direct checks in §6.

`routed commits name a specced unit` · `routed-commits selftest` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py --selftest · covers AC1 AC2 AC3 AC4 AC5 · a scratch history whose violation sits outside the pushed range, observed RED against the unchanged leg · none

## 8. Open questions

- **F1 — Does an inherited-only WHOLE red at the push land under `INHERITED_RED=land`?**
  (a) No. The leg declares no `signature`, so its red at the push reads OWN or MIXED and blocks; the
  pusher waives the inherited sha in the pushed commits. (b) Yes, through an `--offenders` verb and a
  `signature` on gov's leg row, so the runner lands a red whose offenders R already carries. (c) Yes,
  by the leg grading R itself and subtracting R's violations. Veto 2 discards (b): it adds a CLI verb
  to a shipped kit tool, a new public surface, and `kit.toml` carries no `signature` key, so an
  adopter would not receive it. Veto 1 discards (c): the push would then pass a red that remote CI
  shows, which is the defect this unit closes, and the leg would decide inheritance the runner owns.
  RESOLVED (agent, 2026-10-10, delegated): (a). The owner turn on (b) is the §3 hands-off.

## 9. Revision log

- rev-1 · 2026-10-10 · initial draft, from the spec brief for closing review H1.

## 10. Reuse audit

The seam is `tools/memory-tree/routed_commits.py` itself: `check_routed_commits` already holds both
grading modes, and this unit runs its WHOLE grading beside RANGE rather than adding a reader. The
`tools/codebase-map/reuse_lookup.py` probe, phrased "grade the pushed range and the whole history in
one push-boundary run", ranked `read_history_range` in `tools/unattended/lib-unattended.sh` as the
nearest range reader; it learns the tip from `ls-remote` for the pass-order leg and is shell, so it
does not fit a Python leg that already resolves its own base. No existing seam grades two
populations in one run.

Recall terms used: `GATE_PUSH_BASE RANGE WHOLE pre-push remote-ci routed-commits waiver inherited-red
history-wide leg push boundary reconcile merge`, with the question "why does the pre-push run grade
only the pushed range while remote CI grades the whole history". It surfaced TOOL-aMendedFleet-62,
TOOL-dUnstuckLanding-17, the push-leg unit's range table and the closing review's B1 left-shift.

# KICK-dKeptSession-36 — the transition guard runs the driver through a bash that shares this filesystem, never the bare name, and an unresolved shell refuses

**Status:** DEFERRED · rev-5 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-30 |
| [2026-10-26-build-KICK-dKeptSession-36-deviation-361.md](../build/2026-10-26-build-KICK-dKeptSession-36-deviation-361.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-36-deviation-362.md](../build/2026-10-26-build-KICK-dKeptSession-36-deviation-362.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-40 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-30 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-36-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-36-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief.md) | research | KICK-dKeptSession-27 KICK-dKeptSession-24 |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 22 at HIGH**, report item **H4**, which no other id shares.

`KICK-dKeptSession-5` S9 had `write_transition`, a Windows python, run bare `bash
<prefix>/unattended/unattended.sh --mail read`. On this node the bare name reaches the WSL launcher,
which sees another filesystem, so the driver path does not resolve and S9 passed "an absent driver"
with a NOTE: the guard passed with open mail and certified a check it never ran. The class is
recorded in `memory/gotchas/subprocess-resolves-a-different-shell.md`. The loop kit now carries the
one resolver that runs each candidate, and unit 5's rev-9 S9 launches the guard through it and the
kit's one locator. This unit holds what that launch leaves to it: the missing-shell refusal's words,
the plants that observe the launch, the absent pass and the refusal, and the user page's sentence.
It builds one step after `KICK-dKeptSession-5` (order 17).

## 2. Scope (IN)

- **S1** — id 22. The resolver, already landed: `tools/loop/loop_witness.py#resolve_bash`, the
  loop kit's inline copy of the canonical `tools/lib/resolve_bash.py#resolve_bash`
  (TOOL-dGroundRules-25 S28), held byte-identical by the `resolve_bash_py` row of
  `tools/lib/resolve-python.test.sh`. `resolve_bash(script)` tries `GOV_BASH`, the bash PATH names
  and Git for Windows' two paths, keeps the first under which `test -f <script>` exits 0, and
  returns `None` when none does. This unit mints no resolver and edits none; it observes the landed
  one on this node. Observed by AC1 and AC2.
- **S2** — id 22. The guard's argv, observed. `KICK-dKeptSession-5` S9's `read_mail_rows(root,
  build)` in `tools/loop/loop_transition.py` runs `[<bash>, <driver>, "--mail", "read", <slug>]`,
  `<driver>` being `resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"` through
  `tools/loop/loop_lib.py#resolve_kit_dir`, and `<bash>` being `resolve_bash(<driver>)`, both
  imported inside the function as `tools/loop/loop_transition.py#write_card_follow` imports them.
  The read is unfiltered, with no `--open`: it is the one read the guard and the disposal share
  (spec-5 F9). This unit adds nothing to that launch; where unit 5 landed another, it sets the launch
  to this one. Observed by AC3.
- **S3** — id 22. Absent is the locator's refusal, tested in Python before any spawn. The guard
  passes as "an absent driver" only when `resolve_kit_dir` raises its `LookupError`, which names the
  kit and the three places looked (`tools/lib/resolve_kit_dir.py#resolve_kit_dir`), unit 5's
  `loop: mail · unarmed · <why>` line carrying that error's text. A located driver for which
  `resolve_bash` returns `None` raises unit 5's `ValueError` in this unit's words,
  `mail unknown: no bash that can see <driver>`, which `record` prints after `loop: unanswered`
  and exits 2 on (`tools/loop/loop_transition.py#main`), writing nothing. Observed by AC4.
- **S4** — The plants, in `tools/loop/loop_transition.py`'s fixture: `mail-argv` wraps the guard's
  spawn call for the one run, recording its argv and answering zero rows; `mail-no-driver` calls the
  real `resolve_kit_dir` with an empty scratch directory as `here`; `mail-no-bash` has
  `resolve_bash` answer `None`. Each rebinds the name the guard imports inside its function, on
  `loop_lib`, `loop_witness` or `subprocess`, and restores it after the run, so the guard carries no
  test hook. No bare `bash` launch is left to supersede: unit 5's rev-9 S9 already launches through
  `loop_witness.resolve_bash`, so the supersession rev-3's S4 named is void and this item holds only
  the plants. Observed by AC3, AC4.
- **S5** — The user page. `help/loop.md`'s guard paragraph (`KICK-dKeptSession-5` S14) gains one
  sentence: the driver runs under the bash that can see it, `GOV_BASH` tried first, and a node where
  none can refuses the transition as `mail unknown`. Observed by AC5.

## 3. Non-goals (OUT)

- No resolver of the loop kit's own: the canonical block and its inline copy are
  TOOL-dGroundRules-25's, and a change to their contract is an ask to that block's owner.
- No launch, bound or guard of its own: `read_mail_rows`, `MAIL_GUARD_SECONDS` and every pass and
  refusal of the guard but S3's words are `KICK-dKeptSession-5`'s.
- The guard's other exits, a non-zero read with no rows among them: id 59, item M26, batched into
  `KICK-dKeptSession-44`.
- The position engine's own reads, `--claims` and `--mail read`: ids 23 and 24, items M13 and M14,
  batched into `KICK-dKeptSession-44`.
- A factory for the locate-then-resolve pair the loop kit spells at each driver call (§8 F2).
- The report's left-shift lint over `subprocess` argv. No clause of this build names it.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — S9's transition guard, `read_mail_rows` in `write_transition`, whose launch this unit observes and whose missing-shell refusal it words (id 22)
- **hands-off** `KICK-dKeptSession-44` — the guard's launch through `resolve_bash` in `loop_witness.py`, which the position engine's mail and claims reads take for ids 23 and 24
- **hands-off** `KICK-dKeptSession-42` — `resolve_bash`, through which the consuming step posts its `--mail ack`
- **hands-off** `KICK-dKeptSession-56` — `resolve_bash`, its override and §3's parity claim, and §7's legs, the batch's S3 to S6, S27, S44 and S42 (ids 5, 6, 23, 52, 36, 53, 41)

## 4. Design

### Evidence

- The audit's probe from Windows python: `subprocess.run(['bash','-c','uname -a; pwd'])` printed
  `microsoft-standard-WSL2` and `/mnt/c/projects/...`, while `shutil.which('bash')` named git-bash
  and the System32 launcher exists.
- Re-probed at this rev: `loop_witness.resolve_bash` over the driver's absolute `C:/` path answered
  Git for Windows' `usr/bin` bash, and answered it again with `GOV_BASH` naming the System32 WSL
  launcher, whose `test -f` over that path exits 1.
- The loop kit already spells this launch at each driver call: `resolve_item_seed` locates the
  driver, runs `resolve_bash(driver)`, and answers `unarmed` where either fails
  (`tools/loop/loop_lib.py#resolve_item_seed`); `write_card_follow` does the same for the kickoff
  engine and prints `card — skipped` where no bash resolves
  (`tools/loop/loop_transition.py#write_card_follow`); `read_handover` and `run_driver` raise
  `LookupError` (`tools/loop/position.py#read_handover`, `tools/loop/position.py#run_driver`).
- `KICK-dKeptSession-5` rev-9 S9: "`mail — off`, the locator's `LookupError` and zero rows each
  pass", and "a present driver no bash runs" raises `ValueError`, exit 2 (spec-5 S9).
- `record` prints a `LookupError` after `loop: unarmed` and a `ValueError` after
  `loop: unanswered`, each exit 2 (`tools/loop/loop_transition.py#main`).

### The guard's launch, in order

1. `resolve_kit_dir("unattended", "unattended.sh", KIT)`; its `LookupError` passes with unit 5's
   `unarmed` line carrying the error's text, and nothing is spawned.
2. `resolve_bash(<driver>)`; `None` raises S3's `ValueError`, exit 2, and nothing is spawned.
3. The spawn of S2's argv in the repository, under unit 5's bound and exits.

Steps 1 to 3 are unit 5's code; this unit's diff is step 2's words, the plants and the page.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `mail-argv`, `mail-no-driver`, `mail-no-bash` | plants of `loop_transition.py --fixture` | none |

### Migration

None: the guard is new in `KICK-dKeptSession-5`.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: S3's words in `read_mail_rows`, and S4's three plants with their cases
- `help/loop.md`: S5's sentence

### Alternatives rejected

- **`shutil.which("bash")`.** It names a path that exists, which is not evidence it runs on this
  filesystem; the canonical block's docstring records the same mistake.
- **A loop-kit resolver of its own in `loop_lib.py`.** It would be a second spelling of the
  canonical block the parity table holds, and its `LoopError` and `uname` test would answer no case
  the landed `test -f` probe does not.

## 5. Production-readiness checklist

- security — the shell is chosen by running it over the very driver it will run.
- perf / scale — one probe spawn per candidate tried, at most one guard per transition.
- error / empty / loading states — no usable shell refuses the transition as unknown, never as none.
- observability — the refusal names the driver no bash can see; the absent line names the three
  places looked.
- risks — a host with only a WSL bash cannot transition; that is the intended refusal.
- testing — the plants of §6 and the arm in §7.
- migration — none.
- user docs — `help/loop.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys, pathlib; sys.path.insert(0, 'tools/loop'); import
  loop_witness as w; print(w.resolve_bash(pathlib.Path('tools/unattended/unattended.sh').absolute().as_posix()))"`
  runs on this node, it prints a Git for Windows bash and never the System32 WSL launcher.
  Red when: the resolver returns the bare name or the WSL launcher.
- **AC2** — When the same probe runs with `GOV_BASH` naming the System32 WSL launcher, it still
  prints the Git for Windows bash.
  Red when: an override that cannot see the driver is returned.
- **AC3** — When `python tools/loop/loop_transition.py --fixture --plant mail-argv` records the
  guard's spawn argv over a fixture build, `argv[0]` equals `resolve_bash(argv[1])`, `argv[1]` equals
  the absolute path `resolve_kit_dir("unattended", "unattended.sh", KIT)` resolved, joined with
  `unattended.sh`, and the rest reads `--mail read <slug>`.
  Red when: `argv[0]` is `bash`, as a scratch copy of the guard launching the bare name shows.
- **AC4** — When `--plant mail-no-driver` runs, the move records and prints `loop: mail · unarmed`
  with the error naming the `unattended` kit; when `--plant mail-no-bash` runs, the move exits 2
  printing `mail unknown: no bash that can see` after `loop: unanswered`, and the fixture's commit
  count is unchanged.
  Red when: a located driver with no usable shell passes as absent, as a scratch copy reading a
  `None` bash as the locator's refusal shows.
- **AC5** — When `grep -n "GOV_BASH" help/loop.md` runs, the guard paragraph names `GOV_BASH` and
  `mail unknown`.
  Red when: the page is silent on which shell runs the driver.

## 7. Gates

`loop transition record` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_transition.py · covers AC3 AC4 · the `mail-argv`, `mail-no-driver` and `mail-no-bash` plants, staged red by a scratch copy of `read_mail_rows` launching bare `bash` and reading a `None` bash as absent · none

## 8. Open questions

- **F1 — Does the guard take the landed resolver, or mint the loop kit's own?** The rev-3 text
  minted `resolve_bash()` in `loop_lib.py` with a `LoopError` on an unusable `GOV_BASH` and a `uname`
  test. Since then TOOL-dGroundRules-25 S28 landed the canonical block and its loop-kit copy in
  `loop_witness.py`, which keeps a candidate only when it can see the script. Options: (a) take the
  landed copy, the override's fall-through included; (b) mint the rev-3 resolver beside it.
  RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; the charter's `[reuse]` rule, and the
  landed probe already refuses the WSL launcher over a `C:/` path, so id 22 closes with no second
  spelling. widens: none · relaxes: none
- **F2 — Does this unit extract a factory for locate-then-resolve?** Options: (a) the guard spells
  the two calls, as each driver call of the loop kit does; (b) this unit extracts one and moves
  every such call. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; the two primitives are the
  shared factories, each gated inline, and each caller answers their failure differently, an
  `unarmed` string, a skip line, a `LookupError` or here a pass and a refusal. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H4 (id 22).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared
- rev-3 · 2026-10-26 · S2 · S3 · AC3 · AC4 · §4 Evidence · re-grounded on the cross-check record
  `2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck`, row 100: `<driver>` is found through
  `loop_lib.py`'s inline `resolve_kit_dir`, an absent driver is its `LookupError`, and AC4's plant
  removes the kit from every place the block searches.
- rev-4 · 2026-11-21 · §1 · S1 · S2 · S3 · S4 · S5 · §3 · §4 · AC1 to AC5 · §7 · §8 F1 · F2 · §10 ·
  re-grounded on the landed tree at `c2a407b0` and on `KICK-dKeptSession-5` rev-9 by
  `2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief`: narrowed S1 to an
  observation of the landed `loop_witness.py#resolve_bash`, no resolver minted in `loop_lib.py`
  (F1), so AC2's `LoopError` became the override's fall-through; narrowed S2 to an observation of
  unit 5's `read_mail_rows` launch and S3 to the refusal's words; the old S4's supersession is void,
  since unit 5 no longer launches the bare name, and S4 now holds the plants; the arm moved from the
  absent `tools/loop/selftest.py` to `loop_transition.py` under `loop transition record`; S5 and
  AC5 added for `help/loop.md`; every line-number citation replaced by a `path#symbol` one.
- rev-5 · 2026-11-21 · S2 · S4 · folded `KICK-dKeptSession-5` rev-9 under
  `2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief`: S2 names the guard's read as
  the one unfiltered read, with no `--open`, that the guard and the disposal share (spec-5 F9); S4
  states that no bare `bash` launch is left to supersede, since unit 5's S9 already launches through
  `loop_witness.resolve_bash`; no other section moved.

## 10. Reuse audit

The seam is the loop kit's landed `tools/loop/loop_witness.py#resolve_bash`, the inline copy of
`tools/lib/resolve_bash.py#resolve_bash` that the parity table holds, taken with
`tools/loop/loop_lib.py#resolve_kit_dir` in the pair `tools/loop/loop_lib.py#resolve_item_seed`
already spells and unit 5's `read_mail_rows` takes. `python tools/codebase-map/reuse_lookup.py
"resolve the bash that shares this filesystem by running each candidate"`, re-run 2026-11-21,
ranked `resolve_kit_dir` and `resolve_bash`, the latter across twelve files with
`tools/lib/resolve_bash.py` and `tools/loop/loop_witness.py` among them; `resolve_bash` is the seam
named, and the rev-3 premise that `tools/lib` held no bash resolver no longer holds. The recall
query returned TOOL-aMendedFleet-98, a suite's `bash` resolved to Git-Bash, and scout C's row of
dWitnessedBar naming the `tools/lib/resolve_bash.py` dGroundRules landed; neither disagrees with
source.

Recall terms used: `python tools/memory-recall/query.py "how does a Windows python run bash without
reaching WSL" --terms "resolve_bash GOV_BASH WSL System32 bash.exe git-bash candidate transition
guard subprocess"`

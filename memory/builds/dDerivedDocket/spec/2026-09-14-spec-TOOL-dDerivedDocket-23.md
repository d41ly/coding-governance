# TOOL-dDerivedDocket-23 — red attribution, report-only

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 23

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |

<!-- /gen:spec-records -->

## 1. Goal

A red bar names which legs failed and never whose failure each one is. Five recorded stops were a
run deciding, with no owner to ask, that a red "was not mine" (i12, i69, i93, i100 and i152), and at
least two such claims were wrong: the reds at `aStagedLane/RUN.md:51` and `dCarriedReceipt/RUN.md:89`
were the run's own. Give the runner an attribution mode that re-runs each red leg at a base R the run
cannot rewrite, classifies it OWN, INHERITED, MIXED, CONTENDED or DEAD PROBE by the rules the design
critique hardened (KF14, KF3), and REPORTS. No exit code changes; the policy that acts on a verdict is
the inherited-red policy unit's.

## 2. Scope (IN)

- **S1** `GATE_ATTRIBUTE=<R>` on `tools/run-gates/run-gates.sh`. After the pool drains and after every
  other verdict pass, each leg whose final verdict is a FAIL re-runs alone at R: R's own manifest row,
  in a detached scratch worktree at R, under R's ceiling for that row. R's row also supplies the
  `signature` both ends are graded with (§4, F4). Observed by AC1, AC3, AC7, AC10 and AC15.
- **S2** One classifier with five verdicts, first match wins, specified in §4. Observed by AC1, AC2,
  AC3, AC4, AC5, AC9, AC10, AC11 and AC14.
- **S3** An optional manifest key `signature`: an argv, run in the tree being graded, that prints one
  stable key per offender and nothing else — no line number, no count, no summary or header line —
  and truncates nothing. It is declared on four legs, each through a new `--offenders` mode, because
  no existing list mode has that shape (§4, measured at BASE): `lexicon naming predicates`
  (`tools/lexicon/lexicon.py`), `install-prefix (shipped surface)` (`tools/check-install-prefix.sh`),
  `drift-audit records` (`tools/drift-audit/drift_report.py`) and `memory hygiene`
  (`tools/memory-tree/check-memory-hygiene.sh`). No checker's default output changes. The signature a
  leg is graded with is always R's (§8 F4): a `signature` declared or edited in L's manifest is never
  executed, so the run cannot choose its own grader. Observed by AC1, AC6, AC10, AC12 and AC13.
- **S4** The manifest key set the shipped canary pins gains `signature`, and the runner carries it as
  an eighth wire field appended after `ceiling`. Observed by AC6.
- **S5** Output: one `GATE attr  <leg>  <VERDICT> …` line per red leg in manifest order, then
  `attributed N of M red legs against <R8>`, and the same rows in a new `attribution` file in the run
  record. N counts every verdict except DEAD PROBE; N below M prints the DEAD PROBE count. Observed
  by AC3 and AC7.
- **S6** KF3, nobody grades their own grader: when the diff between R and the working tree touches
  the runner, `gate-fingerprint.sh`, `.githooks/pre-push` or the attribution module, every red reads
  OWN and the lines say why. The runner's header states that it grades itself and that this predates
  this build. Observed by AC5.
- **S7** The FAIL-line normaliser and the detached worktree runner that the held-suite baseline unit
  builds into `run-selftests.sh` move into one sourced kit file, `lib-attribute.sh` beside the
  runner, which both runners source. Observed by AC8.
- **S8** `.githooks/pre-push` exports `GATE_ATTRIBUTE` set to the remote sha it reads for the default
  branch, so a red at the push boundary is attributed too. The hook's exit is unchanged. Observed by
  AC7.
- **S9** No version constant moves in this unit. The kits whose shipped bytes S3 and S7 change each
  move once in this build's landing range, in their owner unit — `TOOL-dDerivedDocket-1` for
  run-gates, `TOOL-dDerivedDocket-21` for drift-audit and lexicon, `TOOL-dDerivedDocket-36` for
  memory-tree under the verdict-epoch rule — and this unit's bytes ride those moves; install-prefix
  carries no version constant. NOT OBSERVED by a criterion here: `kit version markers` grades the
  final tree's constant-marker agreement, which is all it can grade.

## 3. Non-goals (OUT)

- **Any exit code, and any policy.** A bar red before this unit is red after it. Landing over an
  INHERITED red, the `gate-inherited-green` stamp, refusing a "not mine" override and the auto-filed
  ask are all the inherited-red policy unit's.
- **The driver.** `gates-green` exporting `GATE_ATTRIBUTE` and reading the record is the policy
  unit's, which is allowed to run the unattended suites; this unit is not (D12-h, D12-i8).
- **Retrying a timeout.** A timed-out leg is CONTENDED here and is never re-run at R; the serial retry
  is the honest-verdicts unit's.
- **The equal-input-key shortcut**, reusing a verdict when a leg's input key matches between L and R.
  DR keeps it rejected, because guards omit inputs.
- **Attributing held self-test suites.** That is the held-suite baseline unit's `--attribute`; this
  unit shares its normaliser and worktree runner and attributes bar legs only.
- **Shipping `signature` to adopters.** The four declarations are rows in gov's manifest; no kit
  descriptor gains the key, so govkit emits nothing new.
- **Transitive reads outside a grader's directory.** A module imported from another directory, or a
  conf named at runtime, is outside the comparator (§8 F5). A grader directly under `tools/` is
  compared against the whole of `tools/`, which reads its reds OWN on any `tools/` diff: the safe
  direction.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-1` — the FAIL-line normaliser and the detached scratch
  worktree runner at R. Without them S1 re-spells both, and two normalisers disagree about which
  failure is the same failure.
- **consumes-from** `TOOL-dDerivedDocket-21` — a drift verdict that does not depend on the node's
  local main. Without it a stale-local-main red is red at L and at R alike and reads INHERITED.
- **hands-off** `TOOL-dDerivedDocket-24` — the attribution record, its five verdicts and the
  `GATE_ATTRIBUTE` contract, on which that unit's landing policy, refusals and auto-filed asks act.
- **hands-off** `TOOL-dDerivedDocket-26` — the CONTENDED reading of a leg's FIRST attempt record (its
  `.leg` status, rc, `.sec` and `.bound`), which that unit's retry records must keep intact, and the
  fired-ceiling predicate both units spell identically.
- **hands-off** `TOOL-dDerivedDocket-27` — an attribution pass bounded by the runner's own wall,
  which is what lets that unit's pinned backstop stay one bound.

## 4. Design

### Data model

```
env        GATE_ATTRIBUTE=<rev>                     resolved with rev-parse --verify <rev>^{commit}
manifest   "signature": ["python", "tools/lexicon/lexicon.py", "--offenders"]      optional, per row
stdout     GATE attr  <leg>  INHERITED · offenders <n> · at <R8>
           GATE attr  <leg>  MIXED · inherited <i> · own <o> · at <R8>
           GATE attr  <leg>  OWN · <reason>
           GATE attr  <leg>  CONTENDED · timed out after <n>s; not re-run at R
           GATE attr  <leg>  DEAD PROBE · <reason>
           attributed <N> of <M> red legs against <R8>[ · DEAD PROBE <k>]
record     <git-dir>/gate-run/<id>/attribution      one TAB-separated row per red leg:
           <leg> <verdict> <inherited> <own> <R sha> <reason>     <reason> is always LAST;
           a unit that extends the row inserts its columns before <reason>, never after it
```

Every tail keeps the runner's two-space contract, so `read_gate_verdicts` in govkit still splits the
bare leg name. It matches only the runner descriptor's declared green, red and skip prefixes, and a
`GATE attr` line starts with none of them.

### The classifier, first match wins

For a red leg with output O_L at L, run at R to O_R and exit rc_R:

1. **OWN, forced** — the diff between R and the working tree touches a KF3 path. Every red, a
   timed-out one included, because a run that edited the grader cannot vouch for any of its verdicts.
2. **CONTENDED** — the leg's recorded attempt ended with its ceiling FIRED: rc 124 with a positive
   bound in its `.bound` file, or rc 137 whose `.sec` is at or above that bound, which is
   `timeout -k`'s kill after an ignored TERM. Read from the attempt record, so a later retry pass that keeps the
   first attempt's row keeps this reading. Not re-run. Any other rc 137 is a failure like any other and
   goes on to rule 3.
3. **OWN** — the leg has no row in R's manifest; or its `argv` at L differs from R's, the line naming
   `argv`; or the diff between R and the working tree touches its COMPARATOR: every tracked file under
   the directory that holds a tracked file of the leg's argv or of R's `signature` argv, plus every
   tracked root-level file whose name occurs in those files' bytes (§8 F5); or rc_R is 0.
4. **DEAD PROBE** — the leg cannot be run at R: the worktree cannot be made, R's argv file is absent,
   R's run hits its ceiling, or R's output normalises to nothing while rc_R is non-zero. Also a red
   leg whose own L output normalises to nothing: an empty S(L) with a non-zero exit is not evidence
   of anything (KF14).
5. **INHERITED or MIXED** — when R's row declares a signature, S(X) is the stdout of R's `signature`
   argv run in the tree at X, after the normaliser; INHERITED when S(L) is non-empty and S(L) ⊆ S(R),
   else MIXED, whose `own` is |S(L) − S(R)|. When R's row declares none, S(X) is the normalised output,
   whatever L's row declares; INHERITED only when the two are byte-identical, else MIXED. A new
   offender line that arrives with no FAIL line is therefore MIXED, never INHERITED — the direction
   KF14 ranked as the blocker.

The normaliser is the shared one (S7) with a single addition: the worktree path at R is one of the
roots it strips. Over-normalising reads a new failure as inherited; the normaliser strips only what
varies between two runs of an unchanged leg, and a variation it does not know reads MIXED, the safe
direction.

### The R run

- R is resolved once; an unresolvable R makes every red leg a DEAD PROBE and the summary says why.
- The worktree is `git worktree add --detach` under the git COMMON dir, as the baseline unit places
  it, and one worktree serves every red leg of one bar. A trap removes it on every exit path.
- The leg runs from the worktree root with the same launcher substitution `runleg` applies
  (`tools/run-gates/run-gates.sh:1369`) and R's own ceiling, captured through a file, never a pipe.
- It runs INSIDE the run's wall, before `remove_wall_watcher`, so the wall bounds the bar and its
  attribution pass together and the declared-wall unit's pinned backstop stays one bound. A wall that
  fires during the pass ends each unfinished R run as DEAD PROBE with the reason `cut by the wall`,
  and the summary's DEAD PROBE count includes it. The pass still prints its own bound, the sum of the
  red legs' R ceilings, before it starts, and says so when that sum exceeds the wall's remaining
  seconds (§8 F6).

### The `--offenders` modes

`lexicon.py --offenders` prints `<path><TAB><rule><TAB><identifier>` for every offender of every
predicate — the verb table, a banned suffix, a cell's convention — with no `bad[:40]` cut;
`check-install-prefix.sh --offenders` prints `<path><TAB><kind><TAB><spelling>` for every hit, the
carried-prefix section included. In all four modes a key that repeats inside one file carries `#<k>`,
its occurrence ordinal there, so two identical offenders stay two; every mode exits as its checker's
default mode does. `drift_report.py --offenders` prints `<signal><TAB><detail key>` for each
gateable signal over its pin and each ratchet finding, and exits as `--check` does.
`check-memory-hygiene.sh --offenders` prints `check <n><TAB><key>` for each offender each failing
check lists, the key being the offender key the check names — a path, an id, or both — never a line
locator or a count, and exits as the default mode does. No mode changes the default output of its
checker.

**Why not the existing `--list` modes** (measured at BASE `abac6d59`).
`python tools/lexicon/lexicon.py --list` prints every offender keyed `path:line:`, per-cell `.conv`
summary rows with population and teeth counts, the totals `graded=… offenders=…`, `armed … of …`
and `… tracked file(s)`, and cuts `.conv` violations and the over-pin re-list at 40
(`tools/lexicon/lexicon.py:2745-2802`). `bash tools/check-install-prefix.sh --list` opens with a
`hit(s) over … shipped files` header and keys hits by `path:line`. One added function or line
anywhere shifts a key, so both legs would read MIXED on almost every branch, and the 40-row cut can
hide a new offender behind a fixed one: the unsound direction F2 names.

### Inventory

In the `sh.function` cell: the pass that re-runs red legs, the classifier, the offender reader and
the worktree runner lifted from the baseline unit, each named at build time through
`python tools/lexicon/lexicon.py --suggest <identifier> --as sh.function`. In the `py.function` cell:
the drift report's offender emitter. The manifest key `signature`; the run-record file
`attribution`; the kit file `lib-attribute.sh`.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/run-selftests.sh` · the new `lib-attribute.sh` ·
`tools/run-gates/run-gates.test.sh` · `tools/run-gates/kit.toml` · `tools/gate-legs.json` ·
`.githooks/pre-push` · `.githooks/pre-push.test.sh` · `tools/drift-audit/drift_report.py` ·
`tools/drift-audit/selftest.py` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/memory-tree/check-memory-hygiene.test.sh` · `tools/lexicon/lexicon.py` ·
`tools/lexicon/selftest.py` · `tools/lexicon/README.md` · `tools/check-install-prefix.sh` ·
`tools/check-install-prefix.test.sh` · `tools/run-gates/README.md` · the run-gates dossier.

### Alternatives rejected

- **Comparing failure counts.** The fixture that rejects it: R carries one offender, L fixed it and
  added two. A count comparison reads one inherited and one own; the sets read none inherited and two
  own. That is AC1's break.
- **Re-running R's whole bar with `GATE_LEGS` set to a one-row manifest.** The inner bar shares the
  git common dir, so it queues behind the outer bar's turnstile beacon until the queue bound fires,
  and it writes a stamp and a ledger into the scratch git dir. Running R's argv directly has neither
  problem and is what `runleg` does anyway.
- **A signature as a regular expression over the leg's own output.** The gov canary prints the first
  twelve offenders and then a count; a selector over truncated output sees a subset, and a subset
  test over a truncated S(L) reads a hidden new offender as inherited. An `--offenders` mode
  truncates nothing, which is why S3 adds one where the existing `--list` modes cut (above).

## 5. Production-readiness checklist

- security — R is a commit of this repository; the run executes R's tracked argv, which a scoped bar
  would have executed at R anyway. An unresolvable R runs nothing.
- perf / scale — a red bar pays each red leg once more at R, plus one worktree. A green bar pays
  nothing. The pass sits inside the run's wall and prints its own bound.
- error / empty / loading states — DEAD PROBE for every way R cannot answer; an unresolvable R is
  named once in the summary; a worktree left by a killed run is found by its printed path.
- observability — one line per red leg, the `attributed N of M` summary, and the `attribution` file
  in the run record beside the verdict.
- risks — a flaky leg reads MIXED or OWN, never INHERITED, because it must fail identically at both
  ends. A leg whose output embeds a timestamp reads MIXED until the normaliser learns it; that is
  the safe direction. The hook ships verbatim to adopters, whose older runner ignores the export.
- testing — arms in `tools/run-gates/run-gates.test.sh` and `.githooks/pre-push.test.sh` over a
  two-commit fixture repo, one per verdict and per KF14 break, each staged RED first.
- migration — none. The key is optional and absent means the byte-identical rule.
- user docs — `tools/run-gates/README.md` gains the attribution section and the `signature` key;
  the lexicon README and the install-prefix gate's header gain the `--offenders` mode.

## 6. Acceptance criteria

- **AC1** — When a fixture bar runs with `GATE_ATTRIBUTE` set and its signature leg carries one
  offender at R and at L that one plus one more, the leg reads `MIXED · inherited 1 · own 1`; when L
  fixed R's offender and added two others, it reads `MIXED · inherited 0 · own 2`.
  Red when: offenders are compared as counts, so the second fixture reads one inherited and one own.
  permission: the canary is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`.
- **AC2** — When the fixture branch edits the red leg's checker file, the leg reads `OWN` naming its
  comparator, even though it is red at R too.
  Red when: the comparator clause is dropped, so a checker the branch rewrote reads INHERITED.
- **AC3** — When the fixture leg's argv file does not exist at R, its line reads `DEAD PROBE` and the
  summary reads `attributed 0 of 1 red legs`; when its L output normalises to nothing with a non-zero
  exit, it reads `DEAD PROBE` as well; and `<git-dir>/gate-run/<id>/attribution` holds one
  TAB-separated row per red leg, in §4's column order, carrying the verdict, both counts and the full
  R sha.
  Red when: a leg that cannot run at R is read as an empty set, so it reads INHERITED; or the runner
  prints its `GATE attr` lines and writes no record, or writes the columns in another order, so every
  reader finds no attribution and `land` never engages.
- **AC4** — When a fixture leg without a signature fails with byte-identical normalised output at L and
  R it reads `INHERITED`; when L's output gains one line and its FAIL line is unchanged, it reads
  `MIXED`.
  Red when: the no-signature rule compares FAIL lines only, so the new line passes unseen.
- **AC5** — When the fixture diff between R and L touches `tools/run-gates/run-gates.sh`, a red that
  is identical at both ends reads `OWN` with the KF3 reason.
  Red when: the forced reading is dropped, so an edited classifier can grade its own red INHERITED.
- **AC6** — When the shipped canary runs over a manifest row carrying `signature`, it passes; over one
  carrying a near-miss spelling of it, it reds; `tools/gate-legs.json` declares the key on exactly the
  four S3 legs.
  Red when: the pinned key set is not widened, so every real manifest reds the canary.
- **AC7** — When `.githooks/pre-push.test.sh` drives the hook with a fake runner that prints its
  environment, `GATE_ATTRIBUTE` equals the remote sha fed on the hook's stdin, and the hook's exit
  equals the runner's.
  Red when: the hook exports its own local sha, which attributes a red against the tree that has it.
- **AC8** — When the baseline unit's `--attribute` arms in `tools/run-gates/run-selftests.test.sh` run
  after S7, every one of them passes unedited, and `run-selftests.sh` holds no second copy of the
  normaliser.
  Red when: the lift changes the normaliser those arms were written against, or leaves a copy behind.
  permission: the suite is a held kit leg; it runs at the build's one post-build bar.
- **AC9** — Replays of the reds recorded at `aStagedLane/RUN.md:51` and `dCarriedReceipt/RUN.md:89`,
  rebuilt as two-commit fixtures from the records' own descriptions, both read `OWN`.
  Red when: either replay reads INHERITED, which is the claim those runs made and got wrong.
  fixture: the replays are reconstructions from prose records; the tree holds neither original state.
- **AC10** — When the fixture branch rewrites its red signature leg's `signature` in its own
  manifest, once to print one constant line and once to a wrapper that drops the branch's new
  offender from the real list, while that offender stands, the leg reads `MIXED` both times; a leg
  whose `signature` exists only in L's manifest is graded by the byte-identical rule; and a red leg
  whose `argv` differs between R and L reads `OWN` naming `argv`.
  Red when: S(L) is computed from L's row, so the constant-line signature equals S(R), reads
  INHERITED, and lands the run's own red under the policy unit's `land`.
  permission: the canary is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`.
- **AC11** — When the fixture branch edits a helper module beside its red leg's checker so the
  checker hides the branch's new offender, and separately edits a root conf whose name the checker's
  bytes carry, the leg reads `OWN` naming the comparator both times.
  Red when: the comparator is the argv file alone, so a helper edit that hides the run's own
  offender reads INHERITED.
  permission: the canary is held; it runs at the build's one post-build bar.
- **AC12** — When each of the four declared `signature` argvs runs on the real tree, every stdout
  line is TAB-separated, carries no `:<digits>:` locator, and no line has a summary shape — a bare
  count, a colon-terminated header, a line beginning `… and`.
  Red when: a declared signature prints a count or a locator, so one unrelated insertion puts a
  line in S(L) that S(R) lacks and the leg reads MIXED on every branch.
  permission: the arm lives in the held canary and runs at the build's one post-build bar; its
  staged break declares `python tools/lexicon/lexicon.py --list` as the lexicon row's signature in a
  scratch copy.
- **AC13** — When `lexicon.py --offenders` and `check-install-prefix.sh --offenders` run over a
  fixture with a known offender set, each prints exactly that set; when an unrelated function and an
  unrelated tracked file land between R and L above an inherited offender, the signature leg still
  reads `INHERITED`; and each checker's default output over the same fixture is byte-identical to its
  output at BASE.
  Red when: a key carries a line number or the mode truncates, so the unrelated insertion reads
  MIXED or a new offender past the cut reads INHERITED.
  permission: `lexicon selftest`, `install-prefix self-test`, `drift-audit selftest` and
  `memory-hygiene self-test` are held kit legs; they run at the build's one post-build bar.
- **AC14** — When the fixture bar's red legs are one that timed out at 124 under a positive bound,
  one whose argv changed between R and L, one absent from R's manifest, one green at R, one whose R
  copy runs past its ceiling, and one signature leg with a non-empty S(L) ⊆ S(R), their lines read
  `CONTENDED` with no R run recorded, `OWN` naming argv, `OWN` naming the missing row, `OWN` naming
  green at R, `DEAD PROBE`, and `INHERITED`; and with `GATE_ATTRIBUTE` naming a rev that does not
  resolve, every red reads `DEAD PROBE` and the summary names the unresolvable R.
  Red when: any one rule is deleted and its leg falls through to a later one — a CONTENDED leg
  re-run at R, or a changed argv compared as though unchanged and read INHERITED.
  permission: the canary is held; it runs at the build's one post-build bar.
- **AC15** — When a fixture bar's wall fires while its attribution pass is re-running a red leg at
  R, that leg's `GATE attr` line reads `DEAD PROBE` with the reason `cut by the wall`, the summary
  counts it, and the runner exits within the wall plus its watcher's kill window.
  Red when: the pass runs after `remove_wall_watcher`, so the runner outlives its own wall and the
  driver's backstop kills it as never-returned.
  permission: the canary is held; it runs at the build's one post-build bar.

## 7. Gates

`run-gates canary` · `run-gates evidence` · `pre-push self-test` · `run-selftests self-test` · `drift-audit selftest` · `memory-hygiene self-test` · `lexicon selftest` · `install-prefix self-test` · `testsuite counts (every bar self-test prints one)` · `install-prefix (shipped surface)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · a two-commit fixture with a signature leg, a comparator edit, a leg absent at R, a KF3 touch and an L-only signature rewrite · the canary's executed-assertion floor, raised by the arms added
New arm: .githooks/pre-push.test.sh · a fake runner printing its environment · none
New arm: tools/lexicon/selftest.py · a fixture with known offenders and an unrelated insertion · none
New arm: tools/check-install-prefix.test.sh · a fixture with known hits and an unrelated shipped file · none

## 8. Open questions

- **F1 — where does the classifier's input come from at R?** Options: R's whole bar with a one-row
  manifest, or R's argv run directly. The first deadlocks on the turnstile and writes records into
  a scratch git dir (§4). RESOLVED (agent, 2026-09-14, delegated): R's argv, directly.
- **F2 — how is a per-offender signature declared?** Options: an argv to a complete list mode, or a
  selector over the leg's own output. A selector over truncated output makes the subset test unsound
  in the dangerous direction. RESOLVED (agent, 2026-09-14, delegated): an argv, with `--offenders`
  added where no complete list mode exists.
- **F3 — does the driver half of DR 21.4 U21 belong here?** Its `gates-green` export needs the
  unattended suites to verify, and this unit is not among those allowed to run them. RESOLVED
  (agent, 2026-09-14, delegated): the inherited-red policy unit carries it.
- **F4 — which manifest row supplies the signature, and which L edits force OWN?** Options: (a) R's
  row for both ends, L's signature never run, OWN on an `argv` difference; (b) as (a), plus OWN on
  any row difference but `ceiling`; (c) the manifest joins KF3's forced-OWN list. (c) reads every red
  OWN once a run adds a leg, and (b) once it edits a guard, which unit 21 does to four legs; neither
  field changes what a red leg printed. RESOLVED (agent, 2026-09-14, delegated): (a), which closes
  the constant-line and filtering-wrapper attacks with the fewest false OWN readings.
- **F5 — what is a leg's comparator?** Options: (a) its guard set; (b) its tracked argv files;
  (c) every tracked file under each argv file's directory, for the leg's argv and R's signature argv,
  plus the root-level files their bytes name; (d) (b) plus four kit directories on KF3's forced-OWN
  list. (a) leaves three unguarded signature legs with no comparator, (b) admits a helper edit that
  hides the run's own offenders, (d) forces every red OWN on a touch to four kits. RESOLVED (agent,
  2026-09-14, delegated): (c).
- **F6 — does the attribution pass run inside the runner's wall?** Options: (a) inside, before
  `remove_wall_watcher`, so one bound covers the bar and its attribution, and the declared-wall
  unit's pinned backstop stays one bound; (b) outside, with `gates-green` extending its bound by the
  pass's printed bound as a fourth term. (b) adds a runtime-derived term on top of owner ruling
  D12-i7's `GATE_BOUND = GATE_WALL + queue`, so the effective bound on a close would stop being the
  owner's one declared number. That is the owner's call, so (b) is excluded. RESOLVED (agent,
  2026-09-14, delegated): (a). A wall cut is recorded per leg as DEAD PROBE `cut by the wall`, which
  reads as not inherited, the safe direction (KF14).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U21 with KF14 and KF3. Departs from DR in two
  places: the driver half moves to unit 24 (F3), and the signature is an argv to a complete list
  mode, adding `--offenders` to the drift report and the hygiene engine (F2). One edge the brief's
  table does not list is added inside this group: consumes-from unit 21, which DR 21.6 orders first.
- rev-2 · 2026-09-14 · folds the round-1 spec audit (G4 H1, H3, H4, M5, M8, M15, M16; G1 H1, M11).
  H1: S1, S3 and §4 rule 5 grade both ends with R's row's signature, and L's is never run (F4,
  AC10). M8: §4 rule 3's comparator is each grader's directory plus the root confs its bytes name,
  with a §3 non-goal for the residual (F5, AC11). H4: S3 gives all four signature legs an
  `--offenders` mode, since both `--list` modes print counts and locators and cut at 40 (measured,
  §4; AC12, AC13). M15: AC3 reads the record, reason last. M16 with H3: CONTENDED needs a fired
  ceiling, the predicate unit 26 shares; AC14 stages every classifier branch but the worktree
  failure, which needs a seam; a hands-off to unit 26 declares that seam. M5 with G1 H1: the
  attribution pass runs inside the runner's wall, so the declared-wall unit's pinned backstop stays
  one bound, and a wall cut reads DEAD PROBE `cut by the wall` (F6, AC15); a hands-off to unit 27
  declares it. G1 M11: S9's owners follow the build's one-owner rule (run-gates unit 1, drift-audit
  and lexicon unit 21, memory-tree unit 36).

## 10. Reuse audit

- **Probe result.** `reuse_lookup.py` over "re-run a red gate leg at a base commit and classify it
  inherited or own" named `read_gate_verdicts` in `tools/govkit/govkit.py` — the consumer whose
  prefix parse the new `GATE attr` lines must not disturb — and generic `run` and `classify` symbols
  with no attribution semantics; its header reports `.sh` unscanned, so it is blind to both runners.
  Reading source found the seams: `runleg` and its launcher substitution, the per-leg `.leg` rows and
  `.bound` files in the run record, the shipped canary's pinned key set (`KNOWN` in
  `tools/run-gates/run-gates.test.sh:99`), the eighth wire field after `ceiling`, and the baseline
  unit's normaliser and worktree runner, which S7 lifts rather than re-spells.
- **DR against BASE.** DR places the attribution at `GATE_LEGS` (`tools/run-gates/run-gates.sh:91`);
  BASE agrees that the runner reads one manifest path, so R's row is read by `git show` rather than
  by re-pointing that variable. DR's KF3 list names "the attribution module", which does not exist at
  BASE; S7 creates it, so the list has a file to name.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: inherited-red attribution OWN INHERITED MIXED signature normaliser re-run base
  scratch-worktree dead-probe comparator pre-push — passed as `--terms` with the question "how should
  a red merge-bar leg be attributed to another build rather than to this run". Top hits:
  TOOL-dScaffoldedMirror-21, TOOL-aBoundedCeiling-10, the baseline unit's spec, and
  TOOL-dUnstalledConvoy-24.

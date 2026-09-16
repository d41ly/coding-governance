# TOOL-dDerivedDocket-24 — inherited-red policy

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |

<!-- /gen:spec-records -->

## 1. Goal

With a red leg attributed, a run still has two answers to a red it did not cause: override
`gates-green`, which spends the one check between an unattended run and its landing, or abort. By
owner ruling D12-i4 this repository LANDS over an inherited red, bounded at 10 first-parent landings
and recorded with a stamp of its own (KF2); the kit default PARKS, holding as `inherited-red`. By
D12-i5 a run may ABSORB an inherited red, fixing it in-run beyond its declared write set, under four
conditions. This unit reads that policy where the run cannot write it, applies it at `gates-green`
and at the push boundary, refuses the two escape routes unless the attribution backs them, writes the
absorb rule, and files an ask for every inherited leg so the red has an owner on the record.

## 2. Scope (IN)

- **S1** The policy is two keys in this repository's gate policy file, `.githooks/gate-env.sh`:
  `INHERITED_RED=park|land` and `INHERITED_RED_MAX_AGE=<n>`. Both readers take them from the file AS
  COMMITTED AT R and parse only those two keys, never sourcing R's bytes. Absent, blank, malformed, or
  `land` with no positive age reads `park`, announced. Gov declares `land` and `10`. Observed by AC1
  and AC17.
- **S2** The driver finds that file through a new `.unattended.conf` key, `GATE_POLICY_FILE`, which
  it too reads from the conf as committed at R, so neither the path nor the values come from the
  run's tree. Blank means no policy is adopted: `park`, announced. Observed by AC1 and AC5.
- **S3** The runner, under `GATE_ATTRIBUTE` and `GATE_INHERITED_RED_MAX_AGE=<n>`, AGES and OWNS each
  INHERITED leg: one run at R's n-th first-parent ancestor decides `aged` when the red is already
  there, and otherwise a first-parent bisection inside that window finds the landing that introduced
  it and the id its subject carries. Both go on the leg's attribution row. Observed by AC3.
- **S4** The runner writes a `gate-inherited-green` stamp (KF2) when `GATE_INHERITED_RED=land` is
  exported and every failed leg reads INHERITED and not aged, under every precondition of the
  full-green stamp except "failed nothing". It records R and the leg set, and it never touches
  `gate-full-green`. The stamp records the age bound it was written under, `max_age <n>`. Observed
  by AC4, AC14 and AC17.
- **S5** `.githooks/pre-push` reads the policy at the remote sha it receives, exports it with
  `GATE_ATTRIBUTE`, and gains two acts. Whenever predicates 1 to 8 would force FULL, an
  inherited-green stamp whose R equals that sha, which passes predicates 2 to 8, and whose `max_age`
  equals `INHERITED_RED_MAX_AGE` read at that sha selects the scoped gate. After the gate, a red whose
  record reads every red leg INHERITED and not aged, on a bar whose verdict reads `tree_moved no`, is
  accepted under `land` and printed; anything else is blocked as today. To find that record the hook
  pins `GATE_RUN_ID` to a fresh unpredictable id and removes any directory of that name first,
  spelled exactly as the honest-verdicts unit specifies its own pin. Observed by AC2, AC4, AC14,
  AC15, AC16 and AC17.
- **S6** `gates-green` exports `GATE_ATTRIBUTE` set to the advertised tip `observe_anchor` reads —
  never local main or any other local ref, which the run can write — and the policy read at R, pins
  `GATE_RUN_ID` so it can read that bar's attribution record, records that id and HEAD as a
  `gates-run` fact after every bar, and maps the outcome. Under `land`, an inherited-only red on a
  bar whose verdict reads `tree_moved no` is MET and writes a `gates-inherited` fact. Under `park`,
  or with any red aged, it is UNMET and prints
  `hold · inherited-red · until probe gate · <legs> red at <R8>, INHERITED; INHERITED_RED=<policy>`,
  the line shape the gate-wall unit's Skill step acts on. Every other red is UNMET with the
  attribution lines. This mapping is an arm of `gates-green`'s outcome table, which the gate-wall
  unit later rewrites and must carry (hands-off below). Observed by AC5, AC13, AC15, AC17, AC18 and
  AC19.
- **S7** `--close --override gates-green` and `--abort --code gate-red-out-of-scope` are each
  refused, with a new numbered code, unless the attribution record they consult reads every red leg
  INHERITED. That record is the one the `gates-run` fact names, and it counts only when that run's
  header shows `head` equal to HEAD and `tree_clean yes` and its verdict shows `tree_moved no`. Any
  other state refuses with the same code, naming the condition that failed and that `gates-green`
  must run on HEAD first. An override runs no bar (`tools/unattended/unattended.sh:2977` skips an
  overridden item), so the record is always an earlier one, and those three fields are what tie it
  to the tree being closed. Observed by AC6, AC7 and AC13.
- **S8** ABSORB, per D12-i5, is written into the stops companion guide and the Skill: an inherited
  red may be fixed in-run when the attribution names its owner, no M3 veto is tripped, the fix is its
  own commit whose subject is `absorb(<slug>): <leg> inherited at <R8>` and names no unit id, and the
  fix is recorded CLOSED against the auto-filed ask. KF3 still binds. The write-set clause is gone.
  Observed by AC8 and AC10.
- **S9** The leg's check 23 classifies a commit carrying the absorb subject as an ABSORB, reports its
  paths on an `ABSORB` line, and keeps it out of both anomaly branches. Observed by AC8.
- **S10** The auto-file, DARK until `ASKS_CMD` is declared: for each INHERITED leg the driver writes,
  in the run's own `BACKLOG.md` and staged, an ask carrying a `seen` clause with a pinned locator and
  a `run` command and an `accept` clause, a SEV row and a KEEP row. It then asks `ASKS_CMD` for the
  new id and requires exactly one OPEN ask back; otherwise it removes its rows and says why. With
  `ASKS_CMD` blank it prints the rows it would have filed and writes nothing. The rows are staged,
  never committed: no driver verb commits. On the MET path they ride the close's records commit; on a
  path that prints a `hold ·` line, the Skill's Close sequence — commit the staged records, push the
  branch, reap the keepalive, then `--hold` with `--reaped` — commits them before `--hold`, whose
  clean-tree precondition would otherwise refuse (unit 4 S3). Observed by AC9 and AC21.
- **S11** Gov's `.githooks/gate-env.sh` declares `INHERITED_RED=land` and `INHERITED_RED_MAX_AGE=10`,
  and `.unattended.conf` declares `GATE_POLICY_FILE` naming that file. Observed by AC11. NOT OBSERVED
  for versions: this unit moves no version constant; the unattended and run-gates kits move once in
  this build's landing range, in `TOOL-dDerivedDocket-1` S9, and this unit's bytes ride that move.
- **S12** The unattended suites run once at the unit's end under attribution. Observed by AC12.
- **S13** One `memory/DECISIONS.md` row under the TOOL heading, keyed by this unit's id, records
  D12-i4 — gov lands over an inherited-only red, age-bounded at 10 — and names the sentences it
  departs from: the charter's 'blocks a red one' and 'green at the push boundary', and the protocol's
  `gates-green` definition. Observed by AC20.
- **S14** govkit selfcheck's policy predicate (`tools/govkit/govkit.py:1773-1776`, check 7h3)
  compiles its key alternation from one `POLICY_KEYS` constant naming `GATE_SELFTESTS`,
  `INHERITED_RED` and `INHERITED_RED_MAX_AGE`, so a shipped file carrying a bare assignment of any of
  them reds, trailing-comment and default-expansion spellings included. Observed by AC22.

## 3. Non-goals (OUT)

- **Classifying a red.** The five verdicts, signatures and KF3's forced OWN are the red-attribution
  unit's; this unit reads its record and adds the age and owner fields to it.
- **Arming the auto-file.** Gov's `ASKS_CMD` is set by the arming unit for the asks-disposed item, and
  the auto-file goes live with it. No staged RED of the auto-file is owed there.
- **A policy for timeouts.** A CONTENDED leg is neither inherited nor own, so it blocks `land` and
  both S7 routes; the serial retry and HOST are the honest-verdicts unit's.
- **The charter's landing sentence** and any change to predicates 1 to 8 of the hook. S5 adds a path
  in front of the FULL force, whichever of predicates 1 to 8 raises it; it never makes the inherited
  stamp satisfy predicate 1.
- **Remote CI's per-sha verdicts.** They would let R's own verdict be READ rather than re-run; that is
  the remote-CI unit's publish, and `land` does not wait for it (DR 21.6).

### Edges

- **consumes-from** `TOOL-dDerivedDocket-23` — the attribution record, its five verdicts and the
  `GATE_ATTRIBUTE` pass, which S3 extends and S5 to S7 read.
- **consumes-from** `TOOL-dDerivedDocket-4` — the `inherited-red` hold code, the `probe gate`
  condition and the `--hold` verb a park ends with, and the stops companion guide S8 writes into.
- **consumes-from** `TOOL-dDerivedDocket-6` — the ask row and the SEV and KEEP disposition rows S10
  writes, in the grammar that unit's parser reads and its renderers spell. The driver is shell and
  cannot call a Python renderer in another kit without a declared command, so it writes in that
  grammar and has the parser, reached through `ASKS_CMD`, read each new id back.
- **consumes-from** `TOOL-dDerivedDocket-15` — the `seen` clause with its pinned locator and `run`
  command, and the `accept` clause, which make the auto-filed ask runnable under V14.
- **consumes-from** `TOOL-dDerivedDocket-1` — `run-unattended-gates.sh --attribute`, whose "no NEW
  FAIL" reading of the unattended suites against BASE is the only criterion AC12 can meet over suites
  red at BASE for causes this unit does not own.
- **consumes-from** `TOOL-dDerivedDocket-16` — the `ASKS_CMD` key and its eleven-field projection
  contract, through which S10 reads each auto-filed id back.
- **hands-off** `TOOL-dDerivedDocket-27` — the age and bisection runs, kept inside the runner's wall
  with the rest of the attribution pass, and the decision table `gates-green` applies to exit 1 when
  the pinned attribution record exists, with the `gates-inherited` fact and the
  `hold · inherited-red · until probe gate` line; that unit rewrites `gates-green` into a closed table
  after this one.

## 4. Design

### Data model

```
.githooks/gate-env.sh (at R)     INHERITED_RED=land           INHERITED_RED_MAX_AGE=10
.unattended.conf (at R)          GATE_POLICY_FILE=".githooks/gate-env.sh"
env to the runner                GATE_ATTRIBUTE=<R> GATE_INHERITED_RED=<park|land> GATE_INHERITED_RED_MAX_AGE=<n>
attribution row (extended)       <leg> <verdict> <inherited> <own> <R sha> <age k|aged|-> <owner sha8|-> <owner id|-> <reason>
                                 all TAB-separated, <reason> LAST as the red-attribution unit requires
<git-dir>/gate-inherited-green   sha · fingerprint · manifest_blob · selftests · base <R> · max_age <n> ·
                                 legs <name>,<name> · run_id · stamped
RUN.md fact                      gates-inherited: <R8> <leg>,<leg>
RUN.md fact                      gates-run: <GATE_RUN_ID> <head8>
hook stdout                      pre-push: scoped gate on <def> push — inherited green <S8> at base <R8>
                                 pre-push: red on inherited legs only — landing under INHERITED_RED=land: <legs>
```

### Reading the policy at R

`git show "<R>:<path>"` into a variable, then one anchored match per key — `^INHERITED_RED=` and
`^INHERITED_RED_MAX_AGE=` — with the value's quotes stripped and validated against its closed set or
a positive integer. Sourcing R's bytes would execute them; parsing two keys reads data. The hook's
existing `. gate-env.sh` of the pushed tree stays for every other variable, and the two keys are
never taken from it: K18 closes for them and stays open for the rest, as DR states.

### Age and owner

Under `land`, "within age" means the red arrived within the last n first-parent landings. The probe
is one leg run at `R~n` on the first-parent line: a red there with S(L) ⊆ S(`R~n`) is `aged`. Else
the red arrived inside (`R~n`, R], and at most ⌈log2(n+1)⌉ further runs bisect that window to the
first first-parent commit whose run contains S(L). That commit is a landing, and when its subject
carries an id, the id names the owner. With n = 10 that is at most five leg runs per INHERITED leg,
on a red bar only; the pass prints its bound before it starts. The age and bisection runs belong to
the attribution pass and run inside the runner's wall. A wall that fires mid-bisection leaves the
leg's age unproven, which never lands, and the pass says so.

### The two readers' decisions

| Record at L | Policy at R | `gates-green` | pre-push |
|---|---|---|---|
| verdict reads `tree_moved yes` | either | UNMET, naming the move | block, naming the move |
| every red INHERITED, none aged | land | MET, `gates-inherited` fact | accept, printed |
| every red INHERITED, none aged | park | UNMET, names the hold | block |
| any red aged | either | UNMET, names the hold | block |
| any OWN, MIXED, DEAD PROBE or CONTENDED | either | UNMET, attribution lines | block |
| no attribution record | either | UNMET as at BASE | block as at BASE |

The first matching row decides. `tree_moved` is the one verdict-file field the table reads besides
attribution: a red on a tree that moved mid-bar describes no commit, the hazard the scratch-hygiene
unit closes for a green bar.

KF3's forced OWN lands in the fifth row, so a run that edited the grader can never reach `land`:
the "policy to park" half of KF3 holds by construction, and the line prints why.

`AGENTS.md` and the unattended protocol still describe a push boundary that blocks every red;
whether they are edited is an owner turn parked by this build's spec audit, and AC20's row names the
departure meanwhile.

### The stamp at the push

Whenever predicates 1 to 8 would force FULL — `gate-full-green` absent, or present and rejected by
any of predicates 2 to 8 — the hook first looks for `gate-inherited-green`: when its `sha` passes
predicates 2 to 8 exactly as a full green would, its `base` equals the remote sha on the hook's
stdin, its `max_age` equals the bound parsed there, and the policy at that sha is `land`, the hook
selects the scoped gate from the stamp's sha. A full green that passes is used as today, and the
inherited stamp is not read. A different remote sha forces FULL, whose own attribution then
decides. A stamp written under another bound forces FULL, naming both bounds. The stamp is a
different file, so no later push can read it as a full green.

### The auto-file

The ask id is minted under the run's slug: the family is the owner id's family when S3 found one,
else the first family of the build README's `roster:` value; the sequence is the numeric maximum of
that family and slug in the tracked and working trees, plus one. The rows:

```
- <F>-<slug>-<n> · filed <date> · inherited red: leg <leg> red at <R8>, introduced by <owner8> · seen `<argv file>`@<R8> run `<argv at R>` · accept the leg is green at the default branch's tip → <owner sha>
- SEV · <F>-<slug>-<n> · HIGH · a merge-bar leg is red on the default branch
- KEEP · <F>-<slug>-<n> · filed by an unattended run for the owning build; outside this build's goal
```

The locator pins R, as the envelope unit's grammar requires of a line-free path. The `run` command
is what `--asks --probe` may execute under an allow-list and nothing else does (D12-e). The read-back
is `$ASKS_CMD --tsv --ready <new id> --target <slug>`, and one `ask` row with status OPEN, SEV HIGH
and this slug as its home is the only acceptance; anything else removes the three rows and prints the
witness's output, so a grammar drift between this writer and the parser is caught at write time. It
reads the WORKING TREE — no `--at`, because the rows are staged and exist at no rev, and no
`--live-builds`, because only the new row's status, severity and home are read — and it is one of
the call shapes the ask-awareness unit's contract enumerates.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.test.sh` · the stops
companion template · `tools/unattended/SKILL.template.md` · `tools/unattended/.unattended.conf.example`
· `.unattended.conf` · `tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.test.sh` ·
`.githooks/pre-push` · `.githooks/pre-push.test.sh` · `.githooks/gate-env.sh` ·
`memory/DECISIONS.md` · `tools/govkit/govkit.py` · `tools/govkit/selftest.py` · the rendered guides.

### Alternatives rejected

- **Reading the policy from the pushed tree**, as the hook sources `gate-env.sh` today. Rejected by
  the one fixture that matters: a branch that commits `INHERITED_RED=land` would enable its own
  landing, which is AC1's break.
- **Measuring age by the commit that last touched the leg's comparator.** A red introduced by content
  the checker grades, not by the checker, is never aged by it: the lexicon red of 435 offenders sat for
  weeks under an unchanged checker (`dFramedEntrypoint/RUN.md:41`).
- **Letting the runner decide `land` from an exported variable alone.** Any caller can export it, so a
  run invoking the runner directly could stamp its own landing. The runner only writes the stamp; both
  deciding readers read the policy at R themselves.

## 5. Production-readiness checklist

- security — the policy and its path are read at R, which only a gated push can move; R's bytes are
  parsed for two keys and never executed. The `seen` locator in an auto-filed ask is data. The two
  refusals shrink what an override and an abort can buy. govkit's policy predicate covers the two new
  keys (S14), so a kit whose include list later covers `gate-env.sh` cannot ship gov's `land` under a
  green zero.
- perf / scale — a green bar pays nothing. An inherited red under `land` pays at most five more leg
  runs per inherited leg, printed as a bound before the pass starts.
- error / empty / loading states — no policy file, no key or a malformed value reads `park`,
  announced; a missing attribution record leaves `gates-green` exactly as at BASE; a zero remote sha
  on a new branch reads `park`.
- observability — the hook's two new decision lines, the `gates-inherited` fact, the aged and owner
  fields, and the printed would-be rows while the auto-file is dark.
- risks — a flaky leg can bisect to the wrong owner; the ask's `seen` names the argv, so a reader
  re-runs it. An attended push also lands over an inherited red under `land`, which is gov's policy
  for every push rather than an unattended exception, and the hook's decision line says so.
- testing — driver and leg arms over a scratch repository with a bare remote, and runner and hook arms
  in their held suites, each staged RED; the unattended suites once at the unit's end.
- migration — the kit ships `park`; an adopter changes nothing unless it declares a policy file.
- user docs — the stops companion's ABSORB and park paragraphs, the Skill's Close section, and the
  `.unattended.conf.example` key.

## 6. Acceptance criteria

- **AC1** — When a fixture branch commits `INHERITED_RED=land` into its own `.githooks/gate-env.sh`
  while R's copy says `park`, both the hook's decision line and `gates-green` read `park`, and an
  inherited-only red is blocked.
  Red when: either reader takes the policy from the working tree, so the run enables its own landing.
- **AC2** — When a fixture push under `land` at R fails only on a leg attributed INHERITED and not
  aged, `.githooks/pre-push.test.sh` sees the hook exit 0 and print the leg; when the red leg reads
  MIXED, the push is blocked.
  Red when: a MIXED leg is accepted, which lands a red the run worsened.
- **AC3** — When the fixture's red leg is already red with the same offenders at `R~10`, its
  attribution row reads `aged` and `land` does not apply; when it went red inside that window, the row
  names the first-parent landing that introduced it.
  Red when: the age probe is skipped, so a red that has sat on main indefinitely keeps being landed
  over.
  permission: the runner arms live in the held canary and run at the build's one post-build bar.
- **AC4** — When an inherited-only bar runs under `land`, `gate-inherited-green` appears naming R and
  the leg, `gate-full-green` is unchanged, and the next push whose remote sha equals R prints
  `scoped gate` naming the inherited green; with a different remote sha it prints `FULL gate`.
  Red when: the inherited stamp satisfies predicate 1, so a later push treats a red tree as green.
- **AC5** — When `gates-green` runs in `tools/unattended/unattended.test.sh` over an inherited-only
  fixture bar with `land` at R, it is MET and the record gains a `gates-inherited` fact; with `park`
  at R it is UNMET and prints `hold · inherited-red · until probe gate`.
  Red when: the driver reads `GATE_POLICY_FILE` or the policy from its working tree.
- **AC6** — When a fixture replays the override recorded at `aStagedLane/RUN.md:51` over an
  attribution with an OWN leg, `--close --override gates-green` refuses with a numbered message; over
  an attribution whose every red is INHERITED, it proceeds and writes its `override` park row.
  Red when: the override is admitted without reading the attribution, which is the i12 path.
- **AC7** — When `--abort --code gate-red-out-of-scope` runs over an attribution with a MIXED leg, it
  refuses; over an inherited-only one, it proceeds.
  Red when: the abort is admitted over a red the run worsened.
- **AC8** — When `bash tools/unattended/check-unattended.sh` grades a fixture run whose dispatched
  pass declared one path and whose `absorb(` commit wrote another, check 23 prints an `ABSORB` line
  for that commit and no anomaly; a commit with the same paths and a unit id in its subject is still
  the anomaly.
  Red when: the absorb grammar also admits a subject naming a unit id.
- **AC9** — When the fixture's `ASKS_CMD` is blank, `gates-green` over an inherited-only bar prints the
  three rows it would file and `git status --porcelain` shows no change to the build's `BACKLOG.md`;
  with `ASKS_CMD` set to a fixture witness, the three rows are staged in it, the ask carrying `seen`
  and `accept`; with a witness that returns no row for the new id, the rows are removed and named.
  Red when: rows are written while `ASKS_CMD` is blank, which arms the auto-file before the flip, or
  kept when the parser cannot read them back.
- **AC10** — When `bash tools/unattended/check-unattended.sh` and the skill-wiring check run over the
  rendered tree, the companion guide states ABSORB's four conditions and the absorb subject, and the
  Skill's Close section names the hold for an inherited red under `park`, and the Close section
  orders a `hold ·` line's steps as commit, push, reap, `--hold`.
  Red when: the Skill render never names the hold, so an agent following it overrides instead; or
  the render reaches `--hold` before committing the staged rows, so the hold it names is refused on a
  dirty tree.
- **AC11** — When this repository is read at HEAD, `.githooks/gate-env.sh` declares
  `INHERITED_RED=land` and `INHERITED_RED_MAX_AGE=10`, `.unattended.conf` declares a
  `GATE_POLICY_FILE` that resolves to that file at HEAD, and the driver's policy reader in
  `tools/unattended/unattended.test.sh` and the hook's in `.githooks/pre-push.test.sh`, each run over
  this repository at HEAD, resolve `land` with an age bound of `10`.
  Red when: gov ships `land` without its age bound or without the conf key, so both readers, or the
  driver alone, read `park` and D12-i4 has no effect for unattended runs.
  permission: both suites run at this unit's end (D12-i8) and at the build's one post-build bar.
- **AC12** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at the
  unit's end, it reports no NEW failure.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).
- **AC13** — When the fixture run's `gates-run` fact names a bar whose record reads every red leg
  INHERITED at an earlier HEAD, and the run then commits, `--close --override gates-green` and
  `--abort --code gate-red-out-of-scope` each refuse with the numbered code naming the moved HEAD; with
  that record at HEAD, `tree_clean yes` and `tree_moved no`, both proceed.
  Red when: the refusal reads the newest record without comparing its `head` with HEAD, so a run
  whose earlier bar was all-INHERITED overrides after committing its own red, which is the i12 path.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).
- **AC14** — When `.githooks/pre-push.test.sh` finds a `gate-inherited-green` whose `max_age` is 50
  while `INHERITED_RED_MAX_AGE` at the remote sha is 10, the hook prints `FULL gate` naming both
  bounds.
  Red when: the hook trusts the stamp's window, so a direct runner call exporting a large
  `GATE_INHERITED_RED_MAX_AGE` stamps a red older than D12-i4's bound and a scoped gate skips it.
- **AC15** — When the inherited-only fixture bar's verdict reads `tree_moved yes` under `land` at R,
  `.githooks/pre-push.test.sh` sees the push blocked naming the move, and `gates-green` in
  `tools/unattended/unattended.test.sh` is UNMET naming the move.
  Red when: the readers consult attribution alone, so an inherited-only red on a tree that moved
  mid-bar lands with no verdict describing the pushed commit.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).
- **AC16** — When the fixture git dir holds a stale `gate-full-green` that predicate 2 rejects and a
  `gate-inherited-green` whose base equals the pushed remote sha under `land`,
  `.githooks/pre-push.test.sh` sees `scoped gate` naming the inherited green, not `FULL gate`.
  Red when: the inherited stamp is read only when `gate-full-green` is absent, so every git dir
  that ever earned a full green forces a FULL bar on each push while main holds an inherited red.
  fixture: seeded with a stale full green, the state gov's primary and worktree git dirs hold.
- **AC17** — Under `land` at R, when the fixture's INHERITED leg carries an `aged` attribution row,
  `.githooks/pre-push.test.sh` sees the push blocked, `gates-green` in
  `tools/unattended/unattended.test.sh` is UNMET printing `hold · inherited-red`, and no
  `gate-inherited-green` is written; and with `INHERITED_RED=land` beside `INHERITED_RED_MAX_AGE`
  blank, `0` or `ten`, both readers print `park`, announced.
  Red when: a reader ignores the age field, or reads a blank or zero bound as unbounded, so a red
  that has sat on main indefinitely lands, against DR 21.4 U22's acceptance 4, "a red past the age
  limit parks".
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).
- **AC18** — When the fixture's local main carries a commit the bare remote lacks, which sets
  `INHERITED_RED=land` in `.githooks/gate-env.sh` and introduces the red, an environment-printing stub
  gate shows `gates-green` exporting `GATE_ATTRIBUTE` equal to the remote's advertised sha, and the
  item reads `park`.
  Red when: the driver takes R from local main, so the run's own committed `land` and its own red
  both sit at R, read INHERITED, and land — the local-ref base the unattended protocol records as a
  reproduced bypass.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).
- **AC19** — When `gates-green` in `tools/unattended/unattended.test.sh` runs the REAL
  `tools/run-gates/run-gates.sh` as `$GATE_CMD` over a scratch repository whose one-leg manifest is
  red at L and identically red at R, under `land` at R, the item is MET reading the `attribution` file
  that runner wrote, and its row carries the age and owner columns before the reason.
  Red when: the runner prints its `GATE attr` lines but writes no record, or writes its columns in
  another order, so the reader finds no attribution and the land path never engages — which every
  planted-record arm in this unit passes.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).
- **AC20** — When `memory/DECISIONS.md` is read, its TOOL heading carries one row keyed by this
  unit's id that names D12-i4 and the charter's push-boundary sentence it departs from, within the
  300-character entry budget.
  Red when: the landing over an inherited red ships with no row, so the only record that the
  charter no longer describes the push boundary is this build's design record.
- **AC21** — When `gates-green` under `park` with `ASKS_CMD` set leaves the three rows staged and
  prints its `hold · inherited-red · until probe gate` line, and the fixture then commits the staged
  records, pushes the branch and reaps the keepalive, the `--hold` that line names, run verbatim with
  `--reaped`, is accepted.
  Red when: the sequence reaches `--hold` with the rows still staged, so unit 4's clean-tree
  precondition refuses the very hold `gates-green` named.
  permission: the brief lists this unit among those allowed to run the unattended suites (D12-i8).
- **AC22** — When `tools/govkit/selftest.py` plants `INHERITED_RED=land` in a shipped fixture path,
  `govkit selfcheck` reds naming the file; with `export INHERITED_RED_MAX_AGE=10  # gov only` it reds
  too.
  Red when: the predicate still matches `GATE_SELFTESTS` alone, so gov's `land` could ship to
  adopters under a green zero.
  permission: `govkit selftest` is a held kit leg; it runs at the build's one post-build bar.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `run-gates canary` · `pre-push self-test` · `pass-order history` · `memory hygiene` · `kit version markers` · `govkit selfcheck` · `govkit selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · an inherited-only fixture bar under each policy, an override and an abort over an OWN attribution, and a blank ASKS_CMD · none
New arm: .githooks/pre-push.test.sh · a branch-committed land policy against a park policy at R, and an inherited stamp with a moved remote sha · none
New arm: tools/run-gates/run-gates.test.sh · a red leg already red at the age window's far end · the canary's executed-assertion floor
New arm: tools/govkit/selftest.py · a shipped fixture path carrying `INHERITED_RED=land` · none

## 8. Open questions

- **F1 — gov's policy.** RESOLVED (owner, 2026-09-13): D12-i4, `land` with an age bound of 10
  first-parent landings, recorded with a `gate-inherited-green` stamp (KF2, KF14, KF3).
- **F2 — ABSORB's bound.** RESOLVED (owner, 2026-09-13): D12-i5, wider than the write set; its own
  commit per fix, naming the leg and R; KF3 still binds; check 23 records it as ABSORB.
- **F3 — how is "within age" measured?** Options: a run at the window's far end, the comparator's last
  change, or a per-sha verdict published by remote CI. The second misses content-borne reds (§4); the
  third is not built yet. RESOLVED (agent, 2026-09-14, delegated): the far-end run, with a bisection
  inside the window that also names the owner ABSORB's first condition needs.
- **F4 — how does the driver reach a repository policy file without naming it?** Options: a literal
  path, a conf key read from the working tree, or a conf key read at R. A literal breaks the kit
  install-prefix rule, and a working-tree key lets a run re-point the policy at any R file carrying
  the right line. RESOLVED (agent, 2026-09-14, delegated): `GATE_POLICY_FILE`, read at R.
- **F5 — how does the hook know the age bound a stamp was written under?** Options: (a) the stamp
  records `max_age` and the hook compares it with the bound parsed at R; (b) the hook re-derives
  `aged`. (b) re-runs the age probe at every push, the push-time cost KF2 removes. RESOLVED (agent,
  2026-09-14, delegated): (a).
- **F6 — who commits the auto-filed rows when `gates-green` names a hold?** Options: (a) the driver,
  in its own records commit; (b) nobody, because rows are staged only on the MET path; (c) the Skill's
  Close sequence, before it pushes, reaps and holds. (a) breaks the kit's recorded rule that no driver
  verb commits and adds a write surface this tier did not price (M3 veto 3); (b) files nothing on the
  park path, where the red most needs an owner. RESOLVED (agent, 2026-09-14, delegated): (c).
- **F7 — where does govkit's policy predicate get its keys?** Options: (a) the two keys typed into
  the pattern; (b) one `POLICY_KEYS` constant the pattern compiles from; (c) the keys
  `.githooks/gate-env.sh` assigns, read at selfcheck time. (c) finds none at BASE, drops
  `GATE_SELFTESTS`, and names a hook path by literal. RESOLVED (agent, 2026-09-14, delegated): (b).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U22 with D12-i4, D12-i5 and KF2. Takes the driver
  half of DR 21.4 U21 from unit 23, which may not run the unattended suites. Adds the age-and-owner
  probe DR leaves unspecified (F3) and the `GATE_POLICY_FILE` key (F4). Adds three edges the brief's
  table does not list, all order-consistent and all outside this spec's group: consumes-from units
  4, 6 and 15. Units 4, 6 and 15 declare the matching hands-off. Unit 6 offers its row renderers;
  this spec writes in their grammar and reads each row back through `ASKS_CMD` instead, because the
  shell driver has no declared route to a Python renderer. The hook's `GATE_RUN_ID` pin lands here
  first, in the honest-verdicts unit's own spelling; that unit, later in build order, finds it built,
  and no criterion of either rests on the other, so no edge is declared for it.
- rev-2 · 2026-09-14 · folds the round-1 spec audit (G4 H2, H5, M1, M2, M3, M4, M5, M12, M13, M15,
  M17, M18, L1, L2; G1 M11, L5). H2: S6 records a `gates-run` fact and S7's two refusals read the
  bar it names, requiring its head, clean tree and unmoved tree (AC13). M1: S4's stamp records
  `max_age` (F5, AC14). M2: `tree_moved yes` is the decision table's first row, and S5 and S6 require
  it unmoved (AC15). M3: S5 reads the inherited stamp whenever FULL would be forced, per KF2 (AC16).
  M4: S10's rows stay staged and the Skill commits them before holding (F6, AC10, AC21); the rev-1
  sentence that no criterion rests on the landing path's commit is struck. H5: S6's park line takes
  the gate-wall unit's `hold ·` shape, with a hands-off to it (AC5). M5 with G1 H1: the age and
  bisection runs sit inside the runner's wall with the rest of the attribution pass (§4 Age and
  owner). M12: S13's DECISIONS row records D12-i4's departure (AC20); the charter and protocol edits
  are parked as an owner turn. M13: S14 makes govkit's policy predicate cover the new keys (F7,
  AC22). M15, M17, M18: the record, the age bound and R's source each get a criterion (AC19, AC17,
  AC18). L1 with G1 L5, and L2: consumes-from units 1 and 16. G1 M11: S11's version clause rides the
  held-suite baseline unit's move. The rev-1 line now says unit 4 declares its hands-off, which it
  already did. G4 M19 with G1 M11: S11 and AC11 take fold plan c4 C4-M19's rewrite, settled by the
  orchestrator where the two plans disagreed, because it grades all three of gov's declarations and
  keeps AC12, where c1 E19's deletion dropped the declaration half.

## 10. Reuse audit

- **Probe result.** `reuse_lookup.py` over "let a landing proceed over an inherited red gate leg with
  an age bound" returned `read_gate_verdicts` in `tools/govkit/govkit.py` and the `.unattended.conf`
  affordance seam, and no seam for a landing policy; `.sh` is an unscanned layer. Reading source found
  the seams: the hook's predicate block and its `gate-env.sh` sourcing (`.githooks/pre-push:198`), the
  full-green stamp writer and its preconditions (`tools/run-gates/run-gates.sh:1855`), the
  `gates-green` arm and the override loop in the driver, the halt-code validation `--abort` already
  uses, and check 23's two anomaly branches in the leg.
- **DR against BASE.** DR names the policy file only as "the policy file"; at BASE the one
  repository-owned, kit-unshipped policy file is `.githooks/gate-env.sh`, whose own header says no kit
  ships its path, so S1 puts the keys there. DR's KF2 says the hook reads the inherited stamp; BASE's
  predicate 1 reads only `gate-full-green`, so S5 adds the look in front of the force rather than
  widening the predicate.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: INHERITED_RED land park age-bound gate-inherited-green stamp ABSORB override
  gate-red-out-of-scope auto-file ask — passed as `--terms` with the question "when may an unattended
  run land over a red it did not cause". Top hits: DEPL-dRetiredFork-15, the owner mandate's
  round-3 rulings, DEPL-dCarriedReceipt-14, TOOL-aBoundedCeiling-9 and TOOL-aReapedTicket-5.

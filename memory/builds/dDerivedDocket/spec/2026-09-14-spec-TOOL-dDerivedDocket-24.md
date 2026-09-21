# TOOL-dDerivedDocket-24 — inherited-red policy

**Status:** SPECCED · rev-6 · 2026-09-21 · node d · Tier-2 · base fb07ca25 · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |
| [2026-09-20-review-TOOL-dDerivedDocket-21-spec-audit-g4-round2.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-21-spec-audit-g4-round2.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |

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
  run's tree. Blank means no policy is adopted: `park`, announced. The key also gains its row in the
  protocol's section 8 key table and a blank-valued line in the kit's example conf, the two carriers the
  `unattended kit gate` leg's check 22 joins, as `SPEC_TOKENS_CLI` did when aDeferredBar added it.
  That row LANDS NET ZERO on `memory/guides/UNATTENDED-PROTOCOL.md`, which measures 60324 of the
  61440 its class declares at BASE and is written by other units of this build as well. The row is
  funded, not spent from that headroom: the §3 one-residual paragraph on two runs CLOSING together
  contending on the bar's turnstile (`memory/guides/UNATTENDED-PROTOCOL.md:324-326`, 195 bytes with
  its blank line at BASE) is removed from `tools/unattended/PROTOCOL.template.md` and its render,
  and that fact moves to `tools/unattended/README.md`, the kit document that owns how the driver's
  bar behaves. This unit is the one that may move it: S6 rewrites the `gates-green` outcome arm the
  residual describes. The row is written no larger than the trim frees. Observed by AC1, AC5 and
  AC24.
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
  must run on HEAD first. An override runs no bar (`tools/unattended/unattended.sh:3175` skips an
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
  new id and requires exactly one OPEN ask back; otherwise it removes its rows and says why. Before
  writing a leg's rows it REUSES: when the build's `BACKLOG.md` already carries an auto-filed ask for
  the same leg red at the same R, and `ASKS_CMD` reads that id back as one OPEN ask, the driver prints
  that it reused the id and writes no row for that leg, so a repeated hold on one inherited red never
  files a second HIGH ask (§8 F8). An ask for that leg at another R, or one not read back OPEN, is
  not reused, and a new ask is filed. With `ASKS_CMD` blank it prints the rows it would have filed
  and writes nothing. The rows are staged, never committed: no driver verb commits. On the MET path
  they ride the close's records commit; on a path that prints a `hold ·` line, the Skill's Close
  sequence — commit the staged records, push the branch, reap the keepalive, then `--hold` with
  `--reaped` — commits them before `--hold`, whose clean-tree precondition would otherwise refuse
  (unit 4 S3). The gate-wall unit's later rewrite of `gates-green` carries the auto-file and its
  reuse (hands-off below). Observed by AC9, AC21 and AC23.
- **S11** Gov's `.githooks/gate-env.sh` declares `INHERITED_RED=land` and `INHERITED_RED_MAX_AGE=10`,
  and `.unattended.conf` declares `GATE_POLICY_FILE` naming that file. Observed by AC11. NOT OBSERVED
  for versions: this unit moves no version constant; the unattended and run-gates kits move once in
  this build's landing range, in `TOOL-dDerivedDocket-1` S9, and govkit, whose bytes S14 changes,
  moves once in `TOOL-dDerivedDocket-21` S8, which owns that kit's one move in this build; this
  unit's bytes ride those moves.
- **S12** The unattended suites run once under attribution at VERIFYING, after the last unit, and
  they are on no bar leg; D12-i8's in-pass lift is parked (§9). Observed by AC12.
- **S13** One `memory/DECISIONS.md` row under the TOOL heading, keyed by this unit's id, records
  D12-i4 — gov lands over an inherited-only red, age-bounded at 10 — and names the sentences it
  departs from: the charter's 'blocks a red one' and 'green at the push boundary', and the protocol's
  `gates-green` definition. Observed by AC20.
- **S14** govkit selfcheck's policy predicate (`tools/govkit/govkit.py:1801-1804`, check 7h3)
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
  condition and the `--hold` verb a park ends with, the resumable HELD stop AC23's second hold
  resumes from, and the stops companion guide S8 writes into.
- **consumes-from** `TOOL-dDerivedDocket-6` — the ask row and the SEV and KEEP disposition rows S10
  writes, in the grammar that unit's parser reads and its renderers spell. The driver is shell and
  cannot call a Python renderer in another kit without a declared command, so it writes in that
  grammar and has the parser, reached through `ASKS_CMD`, read each new id back.
- **consumes-from** `TOOL-dDerivedDocket-15` — the `seen` clause with its pinned locator and `run`
  command, and the `accept` clause, which make the auto-filed ask runnable under V14.
- **consumes-from** `TOOL-dDerivedDocket-1` — `run-unattended-gates.sh --attribute`, whose attributed
  verdict of the unattended suites against BASE, `verdict clean` with every inherited suite filed, is
  the only criterion AC12 can meet over suites red at BASE for causes this unit does not own.
- **consumes-from** `TOOL-dDerivedDocket-16` — the `ASKS_CMD` key and its eleven-field projection
  contract, through which S10 reads each auto-filed id back.
- **hands-off** `TOOL-dDerivedDocket-27` — the age and bisection runs, kept inside the runner's wall
  with the rest of the attribution pass, and the decision table `gates-green` applies to exit 1 when
  the pinned attribution record exists, with the `gates-inherited` fact and the
  `hold · inherited-red · until probe gate` line; and S10's auto-file of one ask per INHERITED leg
  inside that arm, with its reuse of an OPEN ask for the same leg and R, which prints
  `gates-green: ask <id> already OPEN for leg <leg> at <R8> · reused` instead of filing a second.
  That unit rewrites `gates-green` into a closed table after this one, and the table carries both.

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
driver stdout                    gates-green: ask <id> already OPEN for leg <leg> at <R8> · reused
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

The reuse runs first, per INHERITED leg. The driver reads the build's `BACKLOG.md` in the working
tree for ask rows carrying the fixed string `inherited red: leg <leg> red at <R8>,`, in file order,
and reads each matched id back with the same call shape,
`$ASKS_CMD --tsv --ready <id> --target <slug>`. The first id read back as one `ask` row with status
OPEN, SEV HIGH and this slug as its home is reused: the driver prints
`gates-green: ask <id> already OPEN for leg <leg> at <R8> · reused` and writes nothing for that leg.
No match, or no match read back OPEN, files the three rows above. The match needs both the leg and
R, because the `seen` locator and the `run` command pin R: an ask for the same leg at an older R
points a reader at a tree the red no longer describes. A repeated hold under `park` is the
population this closes — each resume of a held run reruns `gates-green` over the same inherited red
— and with the ask committed by the first Close sequence, the second finds it.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.test.sh` · the stops
companion template · `tools/unattended/SKILL.template.md` · `tools/unattended/.unattended.conf.example`
· `tools/unattended/PROTOCOL.template.md` · `.unattended.conf` · `tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.test.sh` ·
`.githooks/pre-push` · `.githooks/pre-push.test.sh` · `.githooks/gate-env.sh` ·
`memory/DECISIONS.md` · `tools/govkit/govkit.py` · `tools/govkit/selftest.py` ·
`tools/unattended/README.md` (S2's moved residual) · the rendered guides.

### Alternatives rejected

- **Reading the policy from the pushed tree**, as the hook sources `gate-env.sh` today. Rejected by
  the one fixture that matters: a branch that commits `INHERITED_RED=land` would enable its own
  landing, which is AC1's break.
- **Measuring age by the commit that last touched the leg's comparator.** A red introduced by content
  the checker grades, not by the checker, is never aged by it: the lexicon red of 435 offenders sat
  under an unchanged checker, and the record that found it states outright that it cannot say for how
  long, the leg being guarded on four paths so that a red can sit in it for the length of any build
  that moves none of them (`memory/builds/dFramedEntrypoint/RUN.md:41`). The bullet rests on that and
  not on a duration: the line declines the measurement, which is itself the argument against aging a
  red by its comparator.
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
  fields, the printed would-be rows while the auto-file is dark, and the reuse line naming the OPEN
  ask a repeated hold did not duplicate.
- risks — a flaky leg can bisect to the wrong owner; the ask's `seen` names the argv, so a reader
  re-runs it. An attended push also lands over an inherited red under `land`, which is gov's policy
  for every push rather than an unattended exception, and the hook's decision line says so.
- testing — driver and leg arms over a scratch repository with a bare remote, and runner and hook arms
  in their held suites, each staged RED; the unattended suites once after the last unit, at
  VERIFYING.
- migration — the kit ships `park`; an adopter changes nothing unless it declares a policy file.
- user docs — the stops companion's ABSORB and park paragraphs, the Skill's Close section, and the
  `.unattended.conf.example` key.

## 6. Acceptance criteria

- **AC1** — When a fixture branch commits `INHERITED_RED=land` into its own `.githooks/gate-env.sh`
  while R's copy says `park`, both the hook's decision line and `gates-green` read `park`, and an
  inherited-only red is blocked.
  Red when: either reader takes the policy from the working tree, so the run enables its own landing.
  permission: the hook suite is the HELD `pre-push self-test` leg and runs at the build's one
  post-build bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain
  bar; the driver suite is on no bar leg and runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass
  lift is parked, §9).
- **AC2** — When a fixture push under `land` at R fails only on a leg attributed INHERITED and not
  aged, `.githooks/pre-push.test.sh` sees the hook exit 0 and print the leg; when the red leg reads
  MIXED, the push is blocked.
  Red when: a MIXED leg is accepted, which lands a red the run worsened.
  permission: the hook suite is the held `pre-push self-test` leg, so it runs at the build's
  one post-build bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`,
  never a plain bar.
- **AC3** — When the fixture's red leg is already red with the same offenders at `R~10`, its
  attribution row reads `aged` and `land` does not apply; when it went red inside that window, the row
  names the first-parent landing that introduced it.
  Red when: the age probe is skipped, so a red that has sat on main indefinitely keeps being landed
  over.
  permission: the runner arms live in the held canary, so they run at the build's one post-build
  bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC4** — When an inherited-only bar runs under `land`, `gate-inherited-green` appears naming R and
  the leg, `gate-full-green` is unchanged, and the next push whose remote sha equals R prints
  `scoped gate` naming the inherited green; with a different remote sha it prints `FULL gate`.
  Red when: the inherited stamp satisfies predicate 1, so a later push treats a red tree as green.
  permission: the canary and the hook suite are held, so they run at the build's one post-build
  bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC5** — When `gates-green` runs in `tools/unattended/unattended.test.sh` over an inherited-only
  fixture bar with `land` at R, it is MET and the record gains a `gates-inherited` fact; with `park`
  at R it is UNMET and prints `hold · inherited-red · until probe gate`.
  Red when: the driver reads `GATE_POLICY_FILE` or the policy from its working tree.
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
- **AC6** — When a fixture replays the override recorded at
  `memory/builds/aStagedLane/RUN.md:51` over an
  attribution with an OWN leg, `--close --override gates-green` refuses with a numbered message; over
  an attribution whose every red is INHERITED, it proceeds and writes its `override` park row.
  Red when: the override is admitted without reading the attribution, which is the i12 path.
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
- **AC7** — When `--abort --code gate-red-out-of-scope` runs over an attribution with a MIXED leg, it
  refuses; over an inherited-only one, it proceeds.
  Red when: the abort is admitted over a red the run worsened.
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
- **AC8** — When `bash tools/unattended/check-unattended.sh` grades a fixture run whose dispatched
  pass declared one path and whose `absorb(` commit wrote another, check 23 prints an `ABSORB` line
  for that commit and no anomaly; a commit with the same paths and a unit id in its subject is still
  the anomaly.
  Red when: the absorb grammar also admits a subject naming a unit id.
  permission: the leg's own command runs here over a FIXTURE, which STAYS in this unit's pass
  under rule 1's narrow reading: that is the direct check `memory/guides/BUILD-METHOD.md` M6
  requires. The same command over the real tree is AC10's half and defers to the run at
  VERIFYING.
- **AC9** — When the fixture's `ASKS_CMD` is blank, `gates-green` over an inherited-only bar under
  `land` at R, the MET path, prints the three rows it would file and `git status --porcelain` shows
  no change to the build's `BACKLOG.md`; with `ASKS_CMD` set to a fixture witness, the item is still
  MET and the three rows are staged in it, the ask carrying `seen` and `accept`; with a witness that
  returns no row for the new id, the rows are removed and named. AC21 and AC23 observe the `park`
  path.
  Red when: rows are written while `ASKS_CMD` is blank, which arms the auto-file before the flip, or
  kept when the parser cannot read them back; or the auto-file runs only on a path that prints a
  `hold ·` line, so a MET landing over an inherited red files no ask.
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
- **AC10** — When `bash tools/unattended/check-unattended.sh` and the skill-wiring check run over the
  rendered tree, the companion guide states ABSORB's four conditions and the absorb subject, and the
  Skill's Close section names the hold for an inherited red under `park`, and the Close section
  orders a `hold ·` line's steps as commit, push, reap, `--hold`.
  Red when: the Skill render never names the hold, so an agent following it overrides instead; or
  the render reaches `--hold` before committing the staged rows, so the hold it names is refused on a
  dirty tree.
  permission: `bash tools/unattended/check-unattended.sh` is the `unattended kit gate` leg and runs
  at the build's one post-build bar; the skill-wiring check is a `--check` form and stays in the pass.
- **AC11** — When this repository is read at HEAD, `.githooks/gate-env.sh` declares
  `INHERITED_RED=land` and `INHERITED_RED_MAX_AGE=10`, `.unattended.conf` declares a
  `GATE_POLICY_FILE` that resolves to that file at HEAD, and the driver's policy reader in
  `tools/unattended/unattended.test.sh` and the hook's in `.githooks/pre-push.test.sh`, each run over
  this repository at HEAD, resolve `land` with an age bound of `10`.
  Red when: gov ships `land` without its age bound or without the conf key, so both readers, or the
  driver alone, read `park` and D12-i4 has no effect for unattended runs.
  permission: the hook suite is the HELD `pre-push self-test` leg and runs at the build's one
  post-build bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain
  bar; the driver suite is on no bar leg and runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass
  lift is parked, §9).
- **AC12** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once after
  the last unit, at VERIFYING, its attribution summary reads `verdict clean`: no NEW FAIL, no
  `DEAD PROBE at L` and no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or `DEAD PROBE at R` is named by
  its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it; or the run is
  read by its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or
  pushed past its budget, reads as clean; or an inherited failure is attributed away with no record
  filing it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the unattended suites are on no bar leg; they run at VERIFYING, after the last
  unit, not at this unit's end (D12-i8's in-pass lift is parked, §9).
- **AC13** — When the fixture run's `gates-run` fact names a bar whose record reads every red leg
  INHERITED at an earlier HEAD, and the run then commits, `--close --override gates-green` and
  `--abort --code gate-red-out-of-scope` each refuse with the numbered code naming the moved HEAD;
  with the same record at HEAD but its header reading `tree_clean no`, and again with its header at
  HEAD, `tree_clean yes`, and its verdict reading `tree_moved yes`, both verbs refuse with that same
  numbered code naming the condition that failed; and with that record at HEAD, `tree_clean yes` and
  `tree_moved no`, both proceed. S7 ties the consulted record to three conditions, so each is held
  false ALONE by an arm of its own; the proceed arm supplies all three at once and grades the
  conjunction, never a conjunct.
  Red when: the refusal reads the newest record without comparing its `head` with HEAD, so a run
  whose earlier bar was all-INHERITED overrides after committing its own red, which is the i12 path;
  or it compares `head` alone, so an all-INHERITED record produced on a DIRTY tree, or on a bar whose
  verdict reads `tree_moved yes`, is admitted and reaches `land` over a red the run may own — the
  same path with one extra step, and neither AC6 and AC7, which grade attribution CONTENT, nor AC15,
  which reaches `tree_moved` through `gates-green`, can see it, because S7's two verbs run no bar and
  always consult an earlier record.
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
- **AC14** — When `.githooks/pre-push.test.sh` finds a `gate-inherited-green` whose `max_age` is 50
  while `INHERITED_RED_MAX_AGE` at the remote sha is 10, the hook prints `FULL gate` naming both
  bounds.
  Red when: the hook trusts the stamp's window, so a direct runner call exporting a large
  `GATE_INHERITED_RED_MAX_AGE` stamps a red older than D12-i4's bound and a scoped gate skips it.
  permission: the hook suite is the held `pre-push self-test` leg, so it runs at the build's
  one post-build bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`,
  never a plain bar.
- **AC15** — When the inherited-only fixture bar's verdict reads `tree_moved yes` under `land` at R,
  `.githooks/pre-push.test.sh` sees the push blocked naming the move, and `gates-green` in
  `tools/unattended/unattended.test.sh` is UNMET naming the move.
  Red when: the readers consult attribution alone, so an inherited-only red on a tree that moved
  mid-bar lands with no verdict describing the pushed commit.
  permission: the hook suite is the HELD `pre-push self-test` leg and runs at the build's one
  post-build bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain
  bar; the driver suite is on no bar leg and runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass
  lift is parked, §9).
- **AC16** — When the fixture git dir holds a stale `gate-full-green` that predicate 2 rejects and a
  `gate-inherited-green` whose base equals the pushed remote sha under `land`,
  `.githooks/pre-push.test.sh` sees `scoped gate` naming the inherited green, not `FULL gate`.
  Red when: the inherited stamp is read only when `gate-full-green` is absent, so every git dir
  that ever earned a full green forces a FULL bar on each push while main holds an inherited red.
  fixture: seeded with a stale full green, the state gov's primary and worktree git dirs hold.
  permission: the hook suite is the held `pre-push self-test` leg, so it runs at the build's
  one post-build bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`,
  never a plain bar.
- **AC17** — Under `land` at R, when the fixture's INHERITED leg carries an `aged` attribution row,
  `.githooks/pre-push.test.sh` sees the push blocked, `gates-green` in
  `tools/unattended/unattended.test.sh` is UNMET printing `hold · inherited-red`, and no
  `gate-inherited-green` is written; and with `INHERITED_RED=land` beside `INHERITED_RED_MAX_AGE`
  blank, `0` or `ten`, both readers print `park`, announced.
  Red when: a reader ignores the age field, or reads a blank or zero bound as unbounded, so a red
  that has sat on main indefinitely lands, against DR 21.4 U22's acceptance 4, "a red past the age
  limit parks".
  permission: the hook suite is the HELD `pre-push self-test` leg and runs at the build's one
  post-build bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain
  bar; the driver suite is on no bar leg and runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass
  lift is parked, §9).
- **AC18** — When the fixture's local main carries a commit the bare remote lacks, which sets
  `INHERITED_RED=land` in `.githooks/gate-env.sh` and introduces the red, an environment-printing stub
  gate shows `gates-green` exporting `GATE_ATTRIBUTE` equal to the remote's advertised sha, and the
  item reads `park`.
  Red when: the driver takes R from local main, so the run's own committed `land` and its own red
  both sit at R, read INHERITED, and land — the local-ref base the unattended protocol records as a
  reproduced bypass.
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
- **AC19** — When `gates-green` in `tools/unattended/unattended.test.sh` runs the REAL
  `tools/run-gates/run-gates.sh` as `$GATE_CMD` over a scratch repository whose one-leg manifest is
  red at L and identically red at R, under `land` at R, the item is MET reading the `attribution` file
  that runner wrote, and its row carries the age and owner columns before the reason.
  Red when: the runner prints its `GATE attr` lines but writes no record, or writes its columns in
  another order, so the reader finds no attribution and the land path never engages — which every
  planted-record arm in this unit passes.
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
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
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
- **AC22** — When `tools/govkit/selftest.py` plants `INHERITED_RED=land` in a shipped fixture path,
  `govkit selfcheck` reds naming the file; with `export INHERITED_RED_MAX_AGE=10  # gov only` it reds
  too.
  Red when: the predicate still matches `GATE_SELFTESTS` alone, so gov's `land` could ship to
  adopters under a green zero.
  permission: `govkit selftest` is a held kit leg, so it runs at the build's one post-build bar,
  spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC23** — When `gates-green` in `tools/unattended/unattended.test.sh` runs under `park` at R with
  `ASKS_CMD` set to a fixture witness over an inherited-only bar, the fixture holds as AC21 does,
  then resumes the held run with `--resume <slug> --keepalive-id <id>`, runs `gates-green` again over
  the same leg red at the same R and holds a second time: the second `gates-green` prints the reuse
  line naming the first ask's id and stages no row, the second `--hold` is accepted, and the build's
  `BACKLOG.md` holds exactly one ask row for that leg and R, with one SEV row and one KEEP row for
  its id. With the witness reading the first ask back CLOSED before the second run, a second ask is
  filed; with the second run's R advanced to a new sha carrying the same red, a second ask is filed.
  Red when: the second hold files a duplicate HIGH ask for a red that already has an OPEN one, so
  every repeated hold of one inherited red adds another ask for an owner to dispose; or the reuse
  matches the leg alone, so a red at a new R is folded into an ask whose `seen` locator pins the old
  one; or it reuses an ask the parser reads CLOSED, so a red whose ask was closed is left with no
  open record.
  permission: the driver suite is on no bar leg; it runs at VERIFYING, after the last unit,
  through `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's
  in-pass lift is parked, §9).
- **AC24** — When `wc -c < memory/guides/UNATTENDED-PROTOCOL.md` and
  `wc -l < memory/guides/UNATTENDED-PROTOCOL.md` are read at this unit's commit and at its parent,
  EACH reading at this unit's commit is NO LARGER than the reading at the parent, and
  `grep -c 'contend on the bar' tools/unattended/README.md` prints 1. Both halves are read because
  the checker declares both for this class, 61440 bytes and 750 lines
  (`tools/memory-tree/check-memory-hygiene.sh:84`), and the carrier is inside the scoped net-zero
  rule on the byte half with 1116 free at BASE.
  Red when: S2's `GATE_POLICY_FILE` row lands without the §3 residual trim that funds it, or is
  written as a paragraph rather than a table row, so a carrier other units of this build write too
  loses headroom to a unit that priced itself at nothing; or the row is folded onto fewer, longer
  lines so the byte half reads net zero while the line half grows, or the reverse, either of which a
  one-half criterion passes; or the residual is removed from the
  protocol and lands in no other document, so a stated fact leaves the tree silently. The over-cap
  half is red by the `memory hygiene` leg's index-cap check; the NET delta against the parent is
  the half no leg reads, which is why this criterion reads it.
  permission: both readings are `wc -c` and `grep -c` over tracked files in the pass. NO CAP IS
  RAISED here: moving the 61440 is an owner turn.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `run-gates canary` · `pre-push self-test` · `pass-order history` · `memory hygiene` · `kit version markers` · `govkit selfcheck` · `govkit selftest` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · an inherited-only fixture bar under each policy, an override and an abort over an OWN attribution, the same two verbs over an all-INHERITED record whose header reads tree_clean no and over one whose verdict reads tree_moved yes, a blank ASKS_CMD, and a second hold over one inherited red at one R · the driver suite's executed-assertion floor
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
- **F8 — what does the auto-file do when an OPEN ask already covers the same inherited red?**
  Options: (a) file a new ask on every `gates-green`, as rev-2, with the duplicates bounded by the
  auto-resume unit's `RESUME_SCHEDULE_LIMIT`; (b) reuse an OPEN ask the build's `BACKLOG.md` already
  carries for the same leg and the same R, confirmed through the same `ASKS_CMD` read-back; (c) reuse
  any ask for the same leg, whatever R. (a) files one more HIGH ask per repeated hold of one red,
  which the bound caps but never removes; (c) folds a red at a new R into an ask whose `seen` locator
  and `run` command pin the old R, so a reader re-runs a tree the red no longer describes. (b) adds
  no write surface and no call shape: it reads the file S10 already writes and calls the read-back
  S10 already makes. RESOLVED (agent, 2026-09-16, delegated), decided by the orchestrator: (b), observed by AC23.

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
- rev-3 · 2026-09-16 · spec-audit round 2 fold, second pass.
  - Plan c1 E40, G1 H1 (2, 24), a sibling fold from the G1 round-2 record: §6 AC12 reads unit 1's
    `verdict clean` and the inherited-suite filing, and the §3 consumes-from edge to unit 1 is
    updated.
  - Plan c1 ADD 4, decided by the orchestrator as a fold in this unit's scope: §2 S10's auto-file
    reuses an OPEN ask the build's `BACKLOG.md` already carries for the same leg and the same R, read
    back through the existing `ASKS_CMD` call shape, instead of filing a duplicate HIGH ask on a
    repeated hold; §4 The auto-file states the match and the reuse line; §5 observability; new §6
    AC23 holds twice on one inherited red and observes exactly one ask; §7 arm line; §8 F8; the §3
    consumes-from edge to unit 4 names the resumable HELD stop AC23 resumes from.
  - Third pass, from the fold-2 verifier problem that neither end of the edge to unit 27 named the
    auto-file: the §3 hands-off to unit 27 names S10's auto-file, its OPEN-ask reuse and the reuse
    line, whose tokens unit 27 carries, and §2 S10 says the gate-wall unit's rewrite of
    `gates-green` carries them. Fold verification: unit 27 observes the kept auto-file only through
    this unit's arms, and §6 AC9 named no policy, so a rewrite that filed only on the hold path could
    pass every arm; AC9 now runs under `land` at R on the MET path, and its `Red when:` reds an
    auto-file that runs only where a `hold ·` line prints.
- rev-4 · 2026-09-16 · regrounded on fb07ca25 (origin/main). Line citations re-read at fb07ca25: §2
  S7's override skip is `unattended.sh:3175`, §2 S14's check 7h3 predicate is `govkit.py:1801-1804`,
  and §10's stamp writer is `run-gates.sh:1861`. §2 S2 gives `GATE_POLICY_FILE` its protocol key
  table row and example-conf line, which check 22 of the `unattended kit gate` leg joins, following
  aDeferredBar's `SPEC_TOKENS_CLI`; §4 Files touched gains `tools/unattended/PROTOCOL.template.md`.
  §2 S11's version clause adds govkit, which S14 changes and unit 21 S8 owns the one move of. The
  third fold pass's text, the hands-off to unit 27, S10's pointer and AC9 on the MET path, was read
  against units 4, 16 and 27 and agrees. §10's BASE paragraph describes fb07ca25. No S-item landed
  on main. §2 S12 and §6 AC12's unit-end suite run, and every criterion whose permission line rests
  on D12-i8, meet the gate-guard hook TOOL-aDeferredBar-3 landed and the build method's rule that a
  pass runs no self-test suite; that is reported to the orchestrator and not decided here. §7 gains
  `codebase-map coverage + freshness`, which dUnstagedSymbol's pre-commit leg now runs on any commit
  staging a `.py`, and this unit stages two under `tools/govkit/`; S14's change is a constant and a
  predicate inside an existing function, so no generated map artifact moves with it. The
  `tools/unattended/unattended.test.sh` arm line now names that suite's executed-assertion floor,
  which the arms raise: the suite carries TWO `FLOOR_ASSERTIONS` lines at HEAD, the first marked
  SHADOWED and inert and the second the effective pin, and that effective pin ROSE in the window, so
  `· none` never described it and a bump of the shadowed line would do nothing.
  Extended 2026-09-20, same base, by the build-wide consolidation pass. The parked suite-permission
  conflict is FOLDED on its conservative reading, and not decided: §2 S12, §5 testing and §6 AC12
  move the attributed suite run from this unit's end to the run made at VERIFYING, after the last
  unit, and every `permission:` line that rested on D12-i8 now says the same, naming the parked
  lift rather than claiming it. The unattended driver and leg suites are named as being on NO bar
  leg, because their `*.test.sh` rows left `tools/gate-legs.json`; the hook suite, the canary and
  the `unattended kit gate` leg are bar legs and are deferred to the post-build bar instead. Criteria that carried no line and whose
  observation is a held suite or a merge-bar leg command gained one, so AC1 to AC19 and AC21 to
  AC23 are consistent with each other; AC10's skill-wiring half keeps its in-pass observation
  because `--check` is a read-only verb the hook admits, and AC20 reads a tracked file. The ruling
  conflict itself is parked for the owner in this build's `RUN.md`. Under the same pass §2 S2's
  protocol row is PRICED at at most 200 bytes against the 1116 free at BASE, and new §6 AC24 reads
  the carrier's size in the pass; no cap is raised. §7's four `New arm:` third fields were re-read
  and stand.
  Extended again 2026-09-20, same base, by the closing consolidation pass, which applied the
  build's NET-ZERO rule for a capped carrier. §2 S2's protocol row is no longer priced at "at most
  200 bytes" of shared headroom: it is FUNDED by trimming the §3 one-residual paragraph at
  `memory/guides/UNATTENDED-PROTOCOL.md:324-326`, 195 bytes with its blank line, whose fact moves
  to `tools/unattended/README.md`; §4 Files touched gains that README, and AC24 now reads the
  carrier at this unit's commit against its PARENT and reds any growth. The trim is this unit's
  because S6 rewrites the `gates-green` arm the residual describes, and it is named precisely so a
  second unit cannot claim the same passage. AC24's old claim that no §7 leg reds an over-cap
  guide was WRONG and is gone: check 6 of the `memory hygiene` leg caps every file under
  `memory/guides/`, and what no leg reads is the delta against the parent. The two sibling run
  records this spec cites are respelled from the build root, `memory/builds/aStagedLane/RUN.md:51`
  and `memory/builds/dFramedEntrypoint/RUN.md:41`, so the spec-token checker grades them instead of
  skipping them. The c1 pass's owed cross-edit was re-read line by line against this spec and is
  ALREADY APPLIED in a stronger wording: §2 S12, §5 testing and every `permission:` line that
  rested on D12-i8 place the attributed run at VERIFYING and record that the driver and leg suites
  sit on NO bar leg, which the cross-edit's "at the build's one post-build bar" would have got
  wrong for those two suites. The header date moves to the last-change date; the rev does not,
  because no criterion changed its subject.
  Verified in the same pass: the trimmed passage measures 195 bytes over the cited
  `:324-326`, not the 194 first written, because 194 is the paragraph WITHOUT the blank line above
  it and the citation includes that line; §2 S2 and this log now both read 195. Re-measured at
  BASE and at HEAD, where the file and the paragraph are byte-identical. Any park row recording
  this trim should carry 195 too.
  Closed 2026-09-20, same base, by the last consolidation pass before the spec audits re-run.
  Three rulings land. Rule 1's NARROW reading is ratified, so §6 AC8's run of
  `bash tools/unattended/check-unattended.sh` over a FIXTURE moves back INTO this unit's pass as
  the direct check `memory/guides/BUILD-METHOD.md` M6 requires, while AC10's run of the same
  command over the RENDERED tree keeps deferring to the run at VERIFYING; the nine driver-suite
  lines and the leg-suite lines are untouched, because a `*.test.sh` file invocation with no
  read-only verb defers wherever it runs. Second, every `permission:` line naming a HELD leg now
  spells the VERIFYING run `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, so the
  hook suite, the canary and `govkit selftest` cannot be read as covered by a plain bar. Third,
  the check-22 ruling is already satisfied here and needed no CONDITIONAL branch removed: §2 S2
  has given `GATE_POLICY_FILE` both its row in the protocol's section 8 key table and its
  blank-valued line in the kit's example conf since rev-4, which is exactly what check 22 joins.
  The 195-byte trim funding that row stands under the scoped net-zero rule, because
  `memory/guides/UNATTENDED-PROTOCOL.md` has 1116 bytes free at BASE and is inside the
  2048-byte class the rule binds. The park row this build still owes `RUN.md` was returned as a
  cross-edit carrying 195 rather than 194 and without the superseded "at most 200 bytes"
  pricing. The header date stays at the last-change date; the rev does not move.
- rev-5 · 2026-09-20 · spec-audit round 3 fold, G4 round 2 · §4 §10 · S7 AC13. M4: S7 ties the
  record an override or an abort may consult to THREE conditions — `head` equal to HEAD,
  `tree_clean yes`, verdict `tree_moved no` — and AC13 staged a refusal for one of them and supplied
  all three together on its proceed arm, so an implementation comparing `head` alone passed both
  clauses and round-1 H2's other two conditions went unobserved. AC13 now holds each condition false
  ALONE, one arm per condition, and its `Red when:` names the admitted state: an all-INHERITED record
  produced on a dirty tree or on a `tree_moved yes` bar reaching `land` over a red the run may own.
  The rule behind it is left-shifted rather than restated — an admission predicate with N conditions
  owes N negative arms. L2: §4's second rejected alternative claimed the 435-offender lexicon red
  "sat for weeks" on the authority of `memory/builds/dFramedEntrypoint/RUN.md:41`, and that line
  records the opposite, that the duration is unknowable from that build because the leg is guarded on
  four paths. The duration clause is gone and the bullet now rests on what the line does establish;
  §10 gains the documented manual check the respell could not buy, because
  `tools/check-spec-tokens.py` resolves a citation's existence and range and never its role. No
  criterion's permission line moved, and the 195-byte trim funding S2's protocol row still stands.
  One format correction rides with the fold, owed by no finding: AC24 read the BYTE half of this
  carrier's cap alone, and the checker declares both halves for the class, 61440 bytes and 750 lines
  at `tools/memory-tree/check-memory-hygiene.sh:84`. A row folded onto fewer, longer lines would have
  read net zero in bytes while the line half grew, so AC24 now reads `wc -l` beside `wc -c` at the
  same two commits and its `Red when:` names that trade. No cap is raised and no figure is re-priced.
  Verified in the same round and corrected in place, at no further rev bump: §7's driver-suite
  `New arm:` row still listed only the fixture shapes AC13 held before this fold, so it now names the
  `tree_clean no` and `tree_moved yes` records the two new refusal arms need; its third field is
  unchanged.
- rev-6 · 2026-09-21 · order re-declared from 24 to 26 in the status header only, derived from the §3 edges. The remaining
  units run in concurrent waves where M6's three conditions hold (owner, 2026-09-21); a wave shares
  one order, and this unit runs at order 26, alone, because M6 condition 3 or the flip keeps it off any shared wave. No criterion, design or edge moved.

## 10. Reuse audit

- **Probe result.** `reuse_lookup.py` over "let a landing proceed over an inherited red gate leg with
  an age bound" returned `read_gate_verdicts` in `tools/govkit/govkit.py` and the `.unattended.conf`
  affordance seam, and no seam for a landing policy; `.sh` is an unscanned layer. Reading source found
  the seams: the hook's predicate block and its `gate-env.sh` sourcing (`.githooks/pre-push:198`), the
  full-green stamp writer and its preconditions (`tools/run-gates/run-gates.sh:1861`), the
  `gates-green` arm and the override loop in the driver, the halt-code validation `--abort` already
  uses, and check 23's two anomaly branches in the leg.
- **DR against BASE fb07ca25.** DR names the policy file only as "the policy file"; at BASE the one
  repository-owned, kit-unshipped policy file is `.githooks/gate-env.sh`, whose own header says no kit
  ships its path, so S1 puts the keys there. DR's KF2 says the hook reads the inherited stamp; BASE's
  predicate 1 reads only `gate-full-green`, so S5 adds the look in front of the force rather than
  widening the predicate. Between `abac6d59` and fb07ca25 `.githooks/pre-push` and `gate-env.sh` did
  not move, and the runner moved only in its version pair and in `report_one`'s kill tail, which put
  the stamp writer six lines lower. The driver grew `--audit`, `read_bound_key`, `REVIEW_ROUNDS`, the
  `BOUNDED` review exit and a pre-dispatch spec-token run, and none of those touched the `gates-green`
  arm, `observe_anchor`, the override skip or `--abort`'s halt-code check. Check 23 of the leg gained
  a brief-row exclusion that reports each excluded path, the shape S9's `ABSORB` line follows, and
  govkit's check 7h3 still compiles its predicate from `GATE_SELFTESTS` alone.
- **A citation carrying a number must be READ, not resolved.** `memory/builds/dFramedEntrypoint/RUN.md:41`
  was respelled by the closing consolidation pass so `tools/check-spec-tokens.py` would grade it, and
  that checker resolves existence and range only — its own header concedes that a citation naming a
  real line that argues the opposite passes. The line argues the opposite of the duration §4's second
  rejected alternative attributed to it, which the round-2 audit caught by reading it. Until the
  checker grades a citation's ROLE, this is a documented manual check on the spec-audit checklist.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: INHERITED_RED land park age-bound gate-inherited-green stamp ABSORB override
  gate-red-out-of-scope auto-file ask — passed as `--terms` with the question "when may an unattended
  run land over a red it did not cause". Top hits: DEPL-dRetiredFork-15, the owner mandate's
  round-3 rulings, DEPL-dCarriedReceipt-14, TOOL-aBoundedCeiling-9 and TOOL-aReapedTicket-5.

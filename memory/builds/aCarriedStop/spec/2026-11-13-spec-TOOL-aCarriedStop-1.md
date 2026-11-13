# TOOL-aCarriedStop-1 — the owner-stop row: `--record-round --owner-stop` appends it citing the owner's tracked record, and the one chain verdict reads it as STOP

**Status:** CLOSED · rev-2 · 2026-11-13 · node a · Tier-2 · base d646814e · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-build-TOOL-aCarriedStop-1-1-acceptance-ledger.md](../build/2026-11-13-build-TOOL-aCarriedStop-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-13-build-TOOL-aCarriedStop-1-candidates.md](../build/2026-11-13-build-TOOL-aCarriedStop-1-candidates.md) | research | — |
| [2026-11-13-prompt-TOOL-aCarriedStop-1-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-aCarriedStop-1-2-builder.md](../prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-2-builder.md) | journal | — |
| [2026-11-13-prompt-TOOL-aCarriedStop-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-brief.md) | research | — |
| [2026-11-13-prompt-TOOL-aCarriedStop-1-build-brief.md](../prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Past `SPEC_FOLD_CUTOFF`, `--dispatch` refuses every pass while the spec-audit chain verdict is not
STOP, and the verdict reads one tracked chain record. A build whose spec run audited before that
record existed has none, so its build run dispatches nothing although the owner ended the chain.
This unit gives the owner's stop a row in that record, so the verdict both verbs share reads STOP
from a recorded, cited act, and a build with no such row is refused as it is today.

## 2. Scope (IN)

- **S1** — `--record-round <slug> --owner-stop <path>` appends one row,
  `round <N> · owner-stop · record <path>`, to the build's chain record and stages it, with no
  run-state file needed. Observed by AC2.
- **S2** — The writer refuses, before any byte is written and each as a value of
  `check_chain_fault`: an audit round's flag beside `--owner-stop`, a path outside the build's
  `prompts/` folder or outside the file-name grammar, a path git does not track, and a roster
  that yields no id to name a new record from. Observed by AC4.
- **S3** — The round number is the record's last round plus one, counted over every row of the
  record, for an audit round as well as for an owner-stop row. Observed by AC5.
- **S4** — `derive_chain_verdict` admits the row, and when the record's last round holds one the
  verdict is `STOP` with reason `owner-stop`, read ahead of every other step. Observed by AC2, AC5
  and AC6.
- **S5** — `--chain-verdict` and `--dispatch` print the cited record on their line, through the
  one derivation. Observed by AC2 and AC3.
- **S6** — A build with no owner-stop row is refused by `--dispatch` in today's bytes, and an
  owner-stop row does not answer for a terminal spec exit no round records. Observed by AC1 and
  AC7.
- **S7** — The driver gains no refusal site, no check number and no second derivation. Observed
  by AC8.
- **S8** — The verb's documents state the flag, the row and the reason: the driver's usage header,
  `tools/unattended/VERBS.template.md`, `tools/unattended/SKILL.template.md`, their two rendered
  copies, and `help/spec-audit.md` with its two usage anchors. Observed by AC9 and AC10.
- **S9** — The Skill's size row in `tools/template-size-limits.txt` moves to the render's measured
  bytes, argued in place, with its row in `memory/DECISIONS.md`. Observed by AC11.
- **S10** — The suite arms of §7 land in `tools/unattended/unattended.test.sh`. NOT OBSERVED by a
  criterion of this spec: a suite is no acceptance observation, so the main loop observes each arm
  red and then green at the close.

## 3. Non-goals (OUT)

- No change to `--close`, to the `specs-audited` item or to its override. A unit no audit names
  still closes under its recorded override, and the owner-stop verdict names no unit for one.
- No reading of a run-state file by the verdict, rotated or live, and no waiver that reaches
  check 118.
- No backfill. This build writes an owner-stop row into no existing build, and writes nothing
  under `memory/builds/dDeclaredLoop/`.
- No change to a refusal text `check_chain_dispatch` prints. The gate keeps naming the re-audit,
  and the documents of S8 name the flag.
- No change to `tools/unattended/check-unattended.sh`. Its chain-round join reads `subject` and
  `finding` rows and passes over every other row (§4, "Readers that pass over the row").
- No change to `memory/guides/BUILD-METHOD.md` or its template. M4 is a governance carrier.
- No change to the build harness under `tools/workflows/`. It renders the two commands and reads
  no verdict line.
- No repair of the suite's census arm, which reads red at the base (§4, "An inherited red").

### Edges

- **consumes-from** external — `write_chain_round`, `derive_chain_verdict`, `read_chain_verdict`
  and `check_chain_dispatch`, built by TOOL-dFoldedAudit-5 and TOOL-dFoldedAudit-9. Without them
  there is no record and no gate for the row to join.
- **hands-off** external — M4's ordered list of verdict steps omits the owner-stop reading after
  this unit. Amending M4 is the owner's.
- **hands-off** external — the suite arm `FA9 AC15 the driver's census holds` and the count it
  compares, which disagree at the base. The main loop routes that red.
- **hands-off** external — each at-risk build's own owner-stop row, written by that build's run.

## 4. Design

### Evidence

Read at `d646814e`. Line citations are blob-pinned to that commit.

| Claim | Where |
|---|---|
| The gate refuses on any word but STOP, after the rule reads `folds` | `tools/unattended/unattended.sh#check_chain_dispatch`, `tools/unattended/unattended.sh@d646814e:13943` to `:13950` |
| The verdict reads the tracked record and the roster, nothing else | `tools/unattended/unattended.sh#read_chain_verdict` |
| The writer counts the last round over `subject` rows only | `tools/unattended/unattended.sh@d646814e:13704` |
| A row outside three shapes is a fault | `tools/unattended/unattended.sh@d646814e:13812` to `:13824` |
| Every refusal of the two verbs is one `fail 118` site | `tools/unattended/unattended.sh#check_chain_fault` |
| A HOLD waits for the owner to move the ceiling "or rules" | `tools/unattended/VERBS.template.md@d646814e:316` |
| An unknown flag is refused at check 14 today | probe, 2026-11-13: `--record-round dFix --owner-stop x` |

### Data model

One new row kind in the chain record, on a round of its own:

```text
round <N> · owner-stop · record <path>
```

`<path>` is the repository-relative path of a file tracked directly under
`<memory root>/builds/<slug>/prompts/`. Its file name matches `[A-Za-z0-9._-]+`. That charset
keeps the row's separator, whitespace, a line end and the verdict's `|` field mark out of the
record, so no separate test for each is written.

The row cites a path and matches no file name, because the owners' stop records carry several
names across the at-risk builds (§10).

### The writer

`write_chain_round` reads one new variable, `RR_OWNER_STOP`, set by a `--owner-stop <path>` arm in
the argument loop between the `gov:argv` sentinels and initialised beside `RR_AUDITED`. An empty
value reads as the flag not given, so the audit route answers it.

With `RR_OWNER_STOP` set, in this order, each test ahead of the first byte:

1. `check_slug`, then the build-folder test, as today.
2. Any of `--subject`, `--audited`, `--blockers`, `--highs`, `--finding` and `--sibling` given
   refuses, naming those given. The four `check_verb_flag --record-round` calls are not reached, so
   `VERB_REQUIRES` keeps its row and leg check 52 keeps its join of four calls to four pairs.
3. The path is tested by prefix and charset: stripped of `$M/builds/$slug/prompts/` it must
   change, and what remains must match `^[A-Za-z0-9._-]+$`.
4. The path is tracked: `git ls-files -- "$path"` prints exactly the path. The equality is the
   test, because a name of `..` passes step 3 and lists the build's other files.
5. `read_chain_record`, then the round count of S3.
6. For a new record, the id that names it is the first id of `spec_ids` and then `roster_ids`, the
   order `read_chain_verdict` walks. No id refuses.

The tail is the one the audit route has: the record's name and three header lines when the record
is new, one append, `stage_runmd`, and the `chain round recorded` line. It is shared, never
copied, so the function keeps one append site and one echo site.

The round count's awk matches `/^round [0-9]+ · /` for the last round and keeps the `subject` test
for the replay refusal. On every record written before this unit the result is unchanged, because
a `finding` or `sibling` row carries its `subject` row's number.

The four refusal values, each whole and literal up to its variable, with no trimming expansion
inside a message:

| Case | Value of `why` |
|---|---|
| a round flag beside it | `--owner-stop records the owner's ruling alone, and a round's flag beside it would mix a ruling with an audit: $mixed` |
| outside the folder or the charset | `--owner-stop names no file directly under this build's prompts folder, or its file name leaves [A-Za-z0-9._-], so the row would cite nothing a reader can open: $path` |
| not tracked | `--owner-stop names a file git does not track, and a ruling no commit holds is one no later run can read: $path` |
| no id for a new record | `the roster yields no id, so a new chain record has no unit to be named from: $slug` |

### The reader

`derive_chain_verdict`'s awk gains one branch beside the three it has: three fields, the second
exactly `owner-stop`, the third `record ` followed by one token of `[A-Za-z0-9._/-]+`. It stores
the path under the row's round. In `END`, when the last round `N` holds such a path, the output is
`N`, `STOP`, `owner-stop`, an empty audit set, an empty override set and the path. Every other
output gains an empty sixth field, read into `_cv_record`.

The owner-stop test stands ahead of the unreviewed test and ahead of the ceiling. It reads the
last round only, so an audit round recorded after the row takes the verdict back. That is how the
owner's "one more round" reverses a stop, with no second flag.

What follows from reading the last round, stated because it is behaviour:

- An owner-stop row passes a record that reads CONTINUE and one that reads HOLD (§8, F1).
- An owner-stop round counts toward `review.spec-audit.chain-ceiling`, like any round.
- The round after an owner-stop row has an empty previous round, so no fold or promotion of the
  round before the stop is carried into it as unreviewed, and step 3 cannot stop it on own work.
- The override set is empty. The record cannot tell which units the spec run's audits named,
  because the audit records are what `specs-audited` reads, so the verdict names none.

`print_chain_verdict` and `check_chain_dispatch` append ` · record <path>` to their line when
`_cv_record` is set:

```text
unattended: chain <slug> · round <N> · STOP · reason owner-stop · record <path>
unattended: dispatch — chain <slug> · round <N> · STOP · reason owner-stop · record <path>
```

The comment above `check_chain_dispatch` that opens `NOTHING A RUN WRITES PASSES A HOLD` and the
step list above `derive_chain_verdict` are rewritten to say what is now true.

### Readers that pass over the row

- `read_unrecorded_exits` matches `/^round [0-9]+ · subject /` and nothing else
  (`tools/unattended/unattended.sh@d646814e:13904`). An owner-stop row records no subject, so a
  terminal spec exit in the live run-state file still refuses the dispatch until its round is
  recorded. That is S6, and it is intended: the row carries a chain the owner ended, never a round
  a run skipped.
- The kit gate's chain join skips a row that is neither `subject` nor a BLOCKER or HIGH `finding`
  (`tools/unattended/check-unattended.sh@d646814e:1213` to `:1220`). Its append-only test compares
  bytes, so it holds the new row as it holds every row.
- No file under `tools/workflows/` parses the verdict line. The harness renders the command and
  tells the caller to take what it prints.

### The documents

| File | What moves |
|---|---|
| `tools/unattended/unattended.sh` header | a second `#   unattended.sh --record-round <slug> --owner-stop <path>` line, which `usage` renders and leg check 26 joins to the parser; a comment at `VERB_REQUIRES` that the row's four are owed by the audit route only |
| `tools/unattended/VERBS.template.md` | the `--record-round` entry: the flag, the row, the four refusals, that no round flag sits beside it; the `--chain-verdict` entry: the tail `[ · record <path>]` on the line grammar, the reason `owner-stop`, read ahead of the five steps, and that a ruling to stop at a HOLD is recorded this way |
| `tools/unattended/SKILL.template.md` | one line in the fenced command block, under the `--record-round` line |
| `memory/guides/UNATTENDED-VERBS.md` · `.claude/skills/unattended/SKILL.md` | re-rendered by `bash tools/unattended/adopt-unattended.sh`, never edited |
| `help/spec-audit.md` | "Recording a round" gains the flag and its refusals; "Asking the verdict" gains the `record` tail, a row for `owner-stop` above step 1, and the HOLD bullet's ruling; both usage anchors take the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints |
| `tools/template-size-limits.txt` · `memory/DECISIONS.md` | the Skill row's raise and its decision row |

The help page is in this unit because the usage header's new line moves the `--record-round`
fingerprint, and a stale anchor reds the `docs` leg in the same commit.

The Skill's render measures 10524 bytes against a row of 10524 (PINNED, 2026-11-13), so one added
line passes it. The raise is a run's own on the four terms the limits file states
(`tools/template-size-limits.txt@d646814e:16` to `:23`): this unit's change takes the render past
the row, the block reserves nothing to the owner and rules no headroom, the movement is argued
above the row in the `RAISED <old> -> <new>` shape, and the decision row lands with it. The
precedent is TOOL-dFoldedAudit-1's raise for the same block and the same reason. The verbs guide
measures 95825 bytes against the guide cap of 98304 (PINNED, 2026-11-13), so its entries fit.

### The probe fixture

The criteria run the driver in a scratch repository. The builder saves this as `stopfix.sh` in its
scratch directory and runs it as `bash stopfix.sh <worktree> <fx>`. It mirrors the suite's
`write_gate_fixture`: a conf committed as the base, a run-state file above it declaring the audit,
both dated past the fixture's cutoff, two OPEN specs and one tracked prompt record.

```bash
set -eu
W=$1; F=$2; B=memory/builds/dFix; D="2026-11-02T12:00:00 +0000"
rm -rf "$F"; mkdir -p "$F/u" "$F/$B/spec" "$F/$B/prompts"
cp "$W/tools/unattended/unattended.sh" "$W/tools/unattended/lib-unattended.sh" "$F/u/"
printf 'MEMORY_ROOT=memory\nDISPOSITION_CUTOFF="2000-01-01"\nREVIEW_ROUNDS="1"\nSPEC_FOLD_CUTOFF="2026-11-01"\n' > "$F/.unattended.conf"
printf '# dFix\n\n<!-- roster:units -->\nFIX-dFix-1\nFIX-dFix-2\n<!-- /roster:units -->\n' > "$F/$B/README.md"
for i in 1 2; do
  printf '# FIX-dFix-%s — u\n\n**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base 0123abcd\n\n## 2. Scope (IN)\n\n- s\n\n## 6. Acceptance criteria\n\n- AC1 observable.\n\n## 7. Gates\n\n- g\n\n## 8. Open questions\n\nnone\n\n## 9. Revision log\n\n- rev-1 · 2026-11-01 · u.\n' "$i" > "$F/$B/spec/2026-11-01-spec-FIX-dFix-$i.md"
done
printf '# the owner ends the audit chain\n' > "$F/$B/prompts/2026-10-24-prompt-FIX-dFix-1-owner-review-stop.md"
cd "$F"; git init -q -b main .; git config user.email t@t.test; git config user.name t; git config core.autocrlf false
git add -A >/dev/null; GIT_COMMITTER_DATE="$D" git commit -q -m conf --no-verify
printf '# dFix\n\n## Run facts\nphase: BUILDING\nwitness: abc\nspec-audit: 2026-11-01\nbase: %s\n\n## Parked\n\n' "$(git rev-parse HEAD)" > "$B/RUN.md"
git add -A >/dev/null; GIT_COMMITTER_DATE="$D" git commit -q -m record --no-verify
```

In §6, each criterion starts from a fresh fixture, and these names stand:

- `run` is `env -u GOV_REMOTE -u GOV_DEFAULT_BRANCH bash u/unattended.sh "$@" 2>/dev/null`, called
  from `<fx>`. The driver's notes go to stderr.
- `<b>` is the fixture's build folder, `memory/builds/dFix`.
- `<stop>` is `memory/builds/dFix/prompts/2026-10-24-prompt-FIX-dFix-1-owner-review-stop.md`.
- `<pass>` is `--dispatch dFix --pass FIX-dFix-1 --writes a.sh`.
- "commit" is `git add -A && GIT_COMMITTER_DATE="2026-11-02T12:00:00 +0000" git commit -q -m c --no-verify`.
- `<118>` is `UNATTENDED check 118 FAILED — the spec-audit chain record refuses this: `.

Probed against the driver at `d646814e` on 2026-11-13: the fixture reproduces AC1's refusal, a
clean audit round recorded and committed in it admits `<pass>` with one dispatch row, AC6's four
rounds read `round 4 · HOLD · reason ceiling`, and AC7's review row refuses naming `s2`.

### What it does not check

- That the owner wrote the cited record, or that it rules a stop. Any tracked file directly under
  the build's `prompts/` folder passes, one the run itself wrote included. The row is evidence a
  reviewer and the owner can open, printed on every dispatch line, and no guard against a run
  that lies. A forged audit round with no terminal review row passes in the same way today.
- That the cited file still exists when the verdict reads the row. The writer tests it once.
- A row written by hand. The reader holds the row to its grammar and never to the folder or to
  the index, and a hand-written round holding an owner-stop row beside audit rows reads as STOP.
- A repeat. A second `--owner-stop` appends a second row, and the verdict is the same.
- The path's case on a filesystem that folds case.

### An inherited red

`grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh` prints 319 at `d646814e`
and at `8db6f4be`, the default branch's tip (PINNED, 2026-11-13). The suite arm
`FA9 AC15 the driver's census holds` compares that count with 318
(`tools/unattended/unattended.test.sh@d646814e:3264`). This unit adds no site, so the count stays
319, and the arm reads red before and after it. AC8 therefore pins 319.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/SKILL.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `.claude/skills/unattended/SKILL.md`
- `help/spec-audit.md`
- `tools/template-size-limits.txt`
- `memory/DECISIONS.md`

### Alternatives rejected

The three candidates and their tests are the main loop's, run on 2026-11-13 at `d646814e` and
recorded in this build's candidates record. The reasons below are as this spec verified them.

- **A, the gate reads a `specs-audited` override row from the spec run's run-state record.** The
  row kind cannot tell an owner's stop from an ordinary unaudited close without parsing its free
  prose: `memory/builds/dSafePassage/` holds one of each. Of the 16 at-risk builds, 15 hold no
  rotated run-state file to read (PINNED, 2026-11-13).
- **B, the gate honours a preflight waiver of `specs-reviewed`.** A waiver is a fact of one run
  with no chain state, so a later audit round cannot take the verdict back, an attended run has no
  preflight to carry it, and the two verbs would no longer share one derivation. The owner-stop
  row also passes a CONTINUE and a HOLD, so that is not what separates the two.
- **A new verb.** The row belongs to the record `--record-round` owns (§8, F2).
- **Requiring the cited file at the run's base.** Every build with a landed spec run holds prompt
  records at its base, so the test narrows nothing, and an attended call has no base to read.
- **Naming the flag in the gate's refusal.** The refusal would advertise, to a run with no ruling
  in hand, the one act that passes it.
- **Refusing a repeated row.** A repeat changes no verdict, so the refusal guards nothing.

## 5. Production-readiness checklist

- security — The flag's value reaches a tracked record the verdict parses, so the writer holds it
  to a charset, a folder and the index before a byte is written. The row is run-writable, as every
  round is, and "What it does not check" says what that leaves open.
- perf / scale — One more awk branch per verdict and one `git ls-files` per owner-stop call.
- error / empty / loading states — A new record with no roster id refuses. An empty flag value
  takes the audit route's check 112. A build with no row keeps today's refusal.
- observability — The cited record is printed on the verdict line and on every admitted dispatch
  line, and the row is a tracked line a diff review reads.
- risks — The suite's census arm is red at the base, so the close's suite run shows a red this
  unit did not cause. The Skill's size row has no headroom, so the template edit and the raise
  land in one commit.
- testing — AC1 to AC8 are driver runs in the probe fixture and greps over the driver. The arms
  of §7 repeat them in the suite, which the main loop runs once at the close. The arms add about
  thirty driver launches at roughly 1.2 s each (PINNED, the figure in the driver's `--plan`
  comment), so under a minute of suite wall.
- migration — None. A record with no owner-stop row reads as it did, and a driver from before
  this unit refuses a record holding the row as outside the grammar, which is a refusal and no
  misread.
- user docs — `help/spec-audit.md`, S8.

## 6. Acceptance criteria

The names `run`, `<b>`, `<stop>`, `<pass>`, `<118>`, "commit" and the fixture are §4's.

- **AC1** — When `run <pass>` runs in a fresh fixture, it exits 1 and prints `<118>` followed by
  `--dispatch builds nothing while the chain reads CONTINUE: round 0, reason unreviewed; re-invoke the build harness with auditIds: FIX-dFix-1 FIX-dFix-2`,
  and `grep -c ' dispatch · item ' <b>/RUN.md` prints 0.
  Red when: the gate admits a declared audit with no round, or its refusal moved a byte.
- **AC2** — When `run --record-round dFix --owner-stop <stop>` runs in a fresh fixture, it exits 0
  and prints a line opening `unattended: chain round recorded — dFix · round 1 · `. Then
  `git ls-files '*-chain-rounds.md'` prints one path whose name ends
  `-build-FIX-dFix-1-chain-rounds.md`, the last line of that file is
  `round 1 · owner-stop · record <stop>`, and `run --chain-verdict dFix` exits 0 and prints
  `unattended: chain dFix · round 1 · STOP · reason owner-stop · record <stop>`.
  Red when: the flag is unknown, which is check 14 at `d646814e`; the row is not written or not
  staged; or the verdict reads the row as a fault or as unreviewed.
- **AC3** — When AC2's record is committed and `run <pass>` runs, it exits 0, prints
  `unattended: dispatch — chain dFix · round 1 · STOP · reason owner-stop · record <stop>`, and
  `grep -c ' dispatch · item ' <b>/RUN.md` prints 1.
  Red when: the gate reads a second derivation that does not know the row, or the line names no
  record.
- **AC4** — When each of these runs in a fresh fixture, it exits 1 and prints `<118>` followed by
  the text beside it, and `git ls-files '*-chain-rounds.md'` then prints nothing:
  `run --record-round dFix --owner-stop <stop> --subject s1` with
  `--owner-stop records the owner's ruling alone, and a round's flag beside it would mix a ruling with an audit: --subject`;
  the same with `--finding 1/HIGH/new-mechanism/FIX-dFix-1/FIX-dFix-2/1` in place of the subject,
  with the same text ending `--finding`;
  `run --record-round dFix --owner-stop <b>/spec/2026-11-01-spec-FIX-dFix-1.md` and
  `run --record-round dFix --owner-stop "<b>/prompts/a b.md"`, each with
  `--owner-stop names no file directly under this build's prompts folder`;
  `run --record-round dFix --owner-stop <b>/prompts/..` and the same flag naming
  `<b>/prompts/untracked.md` after `touch` creates that file, each with
  `--owner-stop names a file git does not track`.
  Red when: a round flag is written beside the row, a path outside the folder or the index is
  cited, or a refusal left a record behind.
- **AC5** — When, in a fresh fixture, `run --record-round dFix --owner-stop <stop>` and then
  `run --record-round dFix --subject s1 --audited "FIX-dFix-1 FIX-dFix-2" --blockers 0 --highs 1 --finding 1/HIGH/new-mechanism/FIX-dFix-1/FIX-dFix-2/1`
  run, the second prints a line holding `dFix · round 2 · `, the record holds
  `round 2 · subject s1 · audited FIX-dFix-1 FIX-dFix-2`, and `run --chain-verdict dFix` prints
  `unattended: chain dFix · round 2 · CONTINUE · reason open · audit FIX-dFix-2`.
  Red when: the count reads `subject` rows only, so the audit round reuses number 1 and the
  verdict stays `owner-stop`.
- **AC6** — When, in a fresh fixture, AC5's audit command runs first, `run --chain-verdict dFix`
  prints a line holding `round 1 · CONTINUE · reason open`, and after
  `run --record-round dFix --owner-stop <stop>` it prints a line holding
  `round 2 · STOP · reason owner-stop`. And when, in another fresh fixture, that audit command
  runs and then three more as
  `run --record-round dFix --subject s<i> --audited FIX-dFix-2 --blockers 0 --highs 1 --finding <i>/HIGH/new-mechanism/FIX-dFix-1/FIX-dFix-2/1`
  for `<i>` of 2, 3 and 4, `run --chain-verdict dFix` prints a line holding
  `round 4 · HOLD · reason ceiling`, and after the owner-stop command it prints a line holding
  `round 5 · STOP · reason owner-stop` and no second line.
  Red when: the owner-stop test stands behind the unreviewed test or behind the ceiling.
- **AC7** — When, in a fresh fixture,
  `printf '2026-11-02T01:00:00Z review · item s2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 0 · folded 0 · promoted 0\n' >> <b>/RUN.md`
  runs, then `run --record-round dFix --owner-stop <stop>`, a commit and `run <pass>`, the last
  exits 1 and prints `<118>` followed by
  `--dispatch reads a terminal spec exit no chain round records, so the verdict would be read without it: s2;`.
  Red when: an owner-stop row is read as recording a subject, so a round a run skipped is passed.
- **AC8** — When `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh` runs it
  prints 319, `grep -c 'derive_chain_verdict "' tools/unattended/unattended.sh` prints 1,
  `grep -c 'check_verb_flag --record-round' tools/unattended/unattended.sh` prints 4, and
  `grep -c 'chain round recorded' tools/unattended/unattended.sh` prints 1.
  Red when: a refusal took a new site, the gate or the verb grew a second derivation, the required
  flags left their table's reader, or the owner-stop route copied the append tail.
  figure: the four counts are PINNED, 2026-11-13, from the driver at `d646814e`.
- **AC9** — When `grep -c -e '--owner-stop'` runs over `tools/unattended/VERBS.template.md` and
  over `.claude/skills/unattended/SKILL.md`, each prints at least 1;
  `grep -c '^#   unattended[.]sh --record-round <slug> --owner-stop ' tools/unattended/unattended.sh`
  prints 1; `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` prints
  nothing; and `grep -c -F '[ · record <path>]' memory/guides/UNATTENDED-VERBS.md` prints at
  least 1.
  Red when: a rendered copy was edited by hand or not re-rendered, the usage header lacks the form,
  or the verdict entry's line grammar lacks the record tail.
- **AC10** — When `python tools/govkit/docs_leg.py --fingerprints` runs, the rows for
  `verb:unattended.sh:--record-round` and `verb:unattended.sh:--chain-verdict` each carry a
  fingerprint that `grep -c "<id> <fingerprint> -->" help/spec-audit.md` finds once, and
  `grep -c -e '--owner-stop' help/spec-audit.md` prints at least 2.
  Red when: the usage header moved and the page kept the old anchor, or the page names the flag
  under neither the record nor the verdict.
  figure: the fingerprints are DERIVED from the built header at observation time.
- **AC11** — When `tr -d '\r' < .claude/skills/unattended/SKILL.md | wc -c` runs, it prints the
  figure on the `.claude/skills/unattended/SKILL.md` row of `tools/template-size-limits.txt`, the
  comment above that row holds `by TOOL-aCarriedStop-1`, and
  `grep -c '^- \*\*TOOL-aCarriedStop-1\*\*' memory/DECISIONS.md` prints 1.
  Red when: the row kept 10524 under a longer render, the row was given headroom, or the raise
  landed with no decision row.
  figure: the new figure is DERIVED from the render at the pass; 10524 is PINNED, 2026-11-13.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended skill size` · `docs` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `scratch-guard self-test` · `check-wiring self-test` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `policy fixtures`

The first six are the legs that grade this unit's change. The last seven are owed by a guard a
path of the estimate trips. The main loop runs the merge bar once, at the close, with the
self-test tier that holds the driver's suite. No leg is added.

Every arm below lives beside the suite's check 118 arms and uses its `write_gate_fixture`,
`run_chain`, `check_gate_refused` and `check_gate_admits` helpers. The RED observation of each is
the suite run against the driver at `d646814e`, where `--owner-stop` is an unknown argument. AC1
has an arm already, `AC6 a declared audit with no round`, which stays as written and is the red
case beside the new green ones.

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 · the same fixture after the owner-stop row is recorded and committed: the verdict line and the dispatch line each end with the record, and the pass gains its row · none
New arm: tools/unattended/unattended.test.sh · covers AC4 · each of the four refusal values quoted whole, the record's bytes compared after each · none
New arm: tools/unattended/unattended.test.sh · covers AC5 · an audit round after the row takes the next number and the verdict · none
New arm: tools/unattended/unattended.test.sh · covers AC6 · a CONTINUE record and `write_hold_rounds`' HOLD record, each then stopped by the row, the HOLD one admitted by the gate · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · `write_gate_exit s2` beside an owner-stop row still refuses through `check_gate_refused` · none

What these arms do not check: the truth of the cited record, a hand-written row, and the census
arm's own figure, which §4 names as red at the base.

## 8. Open questions

- **F1 — Does an owner-stop row pass a HOLD at the ceiling, or only a CONTINUE?**
  - (a) It passes both. The verdict reads the last round, and the row is the last round.
  - (b) It passes a CONTINUE only, and a HOLD still waits for the ceiling to move. The reader then
    looks behind the row for the round the ceiling counted.
  - Recommendation: (a). A HOLD "stays the answer until the owner moves the ceiling or rules"
    (`tools/unattended/VERBS.template.md@d646814e:316`). Moving the ceiling yields CONTINUE and one
    more round, so before this unit a ruling to stop had no form the verdict could read. And (b)
    makes the reader look behind the last round, a second reading the derivation does not have.
  - RESOLVED (agent, 2026-11-13, delegated): (a), the main loop's pick under the build's prompt
    mandate, by M3: the goal names the owner's ended chain, and one that ended at the ceiling is
    such a chain.
- **F2 — Is the writer a flag on `--record-round` or a verb of its own?**
  - (a) A flag. The row joins the one record that verb owns, through its one append tail.
  - (b) A verb. It keeps `VERB_REQUIRES`' row unconditional, and grows the verb list, the Skill's
    verb block, the verbs guide's entry list and each census that joins them.
  - Recommendation: (a). One record has one writer, and the kit gate's verb joins grow with a
    verb and not with a flag.
  - RESOLVED (agent, 2026-11-13, delegated): (a), the main loop's pick under the build's prompt
    mandate, by M3: the smaller surface that meets the goal.

## 9. Revision log

- rev-1 · 2026-11-13 · initial draft.
- rev-2 · 2026-11-13 · §7 · §8 · the writer's own correction after commit `17926918` took rev-1
  mid-check: the `New arm:` line for AC1 became prose, because that arm exists and is not new, and
  F1's recommendation and mark lost a claim about the observed chain that the code does not bear
  out. No scope item, design rule or criterion moved.

## 10. Reuse audit

The seam is the chain record's own three functions in `tools/unattended/unattended.sh`:
`write_chain_round` takes the flag and shares its append tail, `derive_chain_verdict` takes one
row branch and one early output, and `check_chain_dispatch` with `print_chain_verdict` take the
line's tail. `check_chain_fault` carries every refusal. The brief's probe,
`tools/codebase-map/reuse_lookup.py`, ranked name stems only and named no closer seam, and recall
returned TOOL-dFoldedAudit-5 and TOOL-dFoldedAudit-9, which built the record and the gate.

The candidates and the test each met, per M12, run by the main loop on 2026-11-13 at `d646814e`
over the 16 DEFERRED builds that declare `spec-audit:` and hold no chain record. This spec
re-counted the 16, found one rotated run-state file among them, and found each one's override
row citing a tracked file whose name fits the row's charset (PINNED, 2026-11-13):

| Candidate | Test | Result |
|---|---|---|
| A, the gate reads a `specs-audited` override row | does every such row name an owner ruling? | lost: `memory/builds/dSafePassage/` holds one that cites the M4 precision floor and no ruling |
| B, the gate honours a `specs-reviewed` waiver | can a later round take the verdict back, and does an attended run have one? | lost: a waiver holds no chain state and an attended run has no preflight |
| C, the owner-stop row | does every one of the builds hold a tracked record under `prompts/` to cite? | passed: each override reason cites one, under four different file names |

Recall terms used: chain-verdict record-round dispatch chain-rounds specs-audited override owner
stop spec-audit folds ceiling HOLD

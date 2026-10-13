# TOOL-aSweptBar-7 — the closing review's three mediums and four lows, batched

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-1 · base c99ce09c · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aSweptBar-7-brief.md](../prompts/2026-10-13-prompt-TOOL-aSweptBar-7-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of aSweptBar, round 1
(`memory/builds/aSweptBar/reviews/2026-10-13-review-TOOL-aSweptBar-1-6-closing-diff-round1.md`), read
CLEAN WITH FIXES with 3 mediums and 4 lows, and BUILD-METHOD M4 promotes all seven into this one
unit. Each closes with the fix the report's skeptic confirmed: two arms that lost coverage come back,
one arm derives its population from the driver's dispatch table, seven instruments run from their
own folder again, and three records say what the code does.

Tier-1 by the kickoff tier rule. Each change is an arm, a comment, a record or a render in the
source repo only, and no contract an adopter reads moves. The base is the run branch's tip
`c99ce09c3`, where every defect lives; local main `53b25884` holds none of them, so every line cited
below is read at `c99ce09c3`.

## 2. Scope (IN)

- **S1** — M1. The F2 no-run-state refusal set in `tools/workflows/unattended-build.test.sh` is read
  from the driver's dispatch arms, joined to the handlers whose body calls `check_run_state "`. A
  liveness arm asserts `--hold`, `--settle` and `--audit` are in it, a reach arm names any refusing
  handler no arm dispatches, and the comment above it says so. Observed by AC1.
- **S2** — M2. Each of the seven build-folder instruments sources `tools/lib/resolve-python.sh`
  through the slash guard `tools/hooks/format-guard.test.sh:17` uses, applied to `BASH_SOURCE[0]`,
  so an instrument run by its bare filename from its own folder finds the resolver. Observed by AC2.
- **S3** — M3. A new pre-push arm 25c reaches the hook's non-runner FULL force with no bar record to
  adopt, and asserts the FULL decision line carries the reason "is not this kit's runner". Observed
  by AC3.
- **S4** — L1. The lineage block's header in `tools/run-gates/run-gates.evidence.test.sh`, lines
  1469-1471, states the control `check_lin_control` runs today: `pa`'s saved ledger row carries the
  input key the lineage run computed. Observed by AC4.
- **S5** — L2. In the source repo, `{{REVIEW_PROTOCOL}}` resolves to the memory root's
  `guides/REVIEW-PROTOCOL.md` when no receipt row answers, in all three byte-identical
  `derive_kit_paths` copies. Gov's four rendered docs are re-rendered, and the kickoff manifest is
  re-stamped because `memory/guides/BUILD-METHOD.md` is a watched file. Observed by AC5.
- **S6** — L3. Arm C2 of `skills/session-kickoff/manifest-check.test.sh` also runs the checker with
  `LBC` exported to a valid sha, over the manifest that lacks the key, and expects the same refusal.
  So the `getval` empty-first guard at `skills/session-kickoff/manifest-check.sh:366` has an arm
  that reds without it. Observed by AC6.
- **S7** — L4. The CLOSED `TOOL-aSweptBar-3` spec goes to rev-3 in THIS spec pass, not the build:
  its §4 S5 says the plain earning bar stamps a full green on the clean tree, which the arm clears
  before the opt-in run, and its revision log gains one rev-3 line naming §4 S5. Observed by AC7.

## 3. Non-goals (OUT)

- Nothing beyond the seven items, and no write under `tools/roles/`, `.claude/agents/`,
  `.claude/skills/build/` or `tools/playbook/`.
- No change to `.githooks/pre-push`, `skills/session-kickoff/manifest-check.sh`,
  `tools/unattended/unattended.sh` or any `tools/memory-tree/*.template.md`. S1, S3 and S6 are arms,
  and S5 moves the rendered docs by re-render only.
- `{{UNATTENDED_PROTOCOL}}` renders its phrase in gov too. It is the same gap with a different
  token, the review did not find it, and it is a follow-up rather than part of S5.
- No rewrite of the CLOSED `TOOL-aSweptBar-4` spec, whose S7 and AC10 say gov answers the phrase.
  That was true at its tip, and §4 S5 here records the reversal. S7 differs: `TOOL-aSweptBar-3`'s S5
  was already false at its own close.
- No left-shift gate beyond the arms S1, S3 and S6 add. The report's left-shift proposals for M2 (a
  lint), L1 and L4 (self-review rules) are new mechanisms, and M8 makes the left-shift the close's.
  L2 needs none: once gov's live docs carry the path, the `kit/dogfood doc parity` leg reds a
  reverted resolution.

### Edges

- **consumes-from** `TOOL-aSweptBar-1` — the F2 derivation S1 rewrites is its commit `b692baa04`.
- **consumes-from** `TOOL-aSweptBar-3` — arm 25b that S3 sits beside, the lineage header S4 corrects,
  and the spec S7 revises.
- **consumes-from** `TOOL-aSweptBar-4` — the `{{REVIEW_PROTOCOL}}` token S5 resolves, from `96b17341b`.
- **consumes-from** `TOOL-aSweptBar-5` — the `getval` guard S6 arms, from `26091fb86`.
- **consumes-from** `TOOL-aSweptBar-6` — the seven resolver lines S2 rewrites, from `301a36664`.
- **hands-off** external — the M8 left-shift for M2, L1 and L4, for the build's close to dispose.

## 4. Design

Every fix is the one the report's skeptic judged sound, or the skeptic's corrected fix where it
rejected the finder's (L1, L2).

**S1.** The awk at `tools/workflows/unattended-build.test.sh:1037-1041` keeps only functions named
`verb_*`, so it derives 15 verbs. The driver has 23 functions that call `check_run_state "`, and its
`case "$VERB" in` dispatch at `tools/unattended/unattended.sh:14307-14332` routes eight verbs to
handlers with other names: `run_hold`, `run_handoff`, `run_settle`, `write_claim_beat`, `print_audit`,
`write_task_register`, `print_liveness` and `print_authorization`. The derivation becomes one awk
reading `"$DRV"` twice. Pass one records every top-level function whose body, up to the next
top-level definition, holds `check_run_state "`. Pass two reads every case arm opening `--<flag>)`
up to its `;;` and keeps the flag when the arm calls a recorded function. Reading to `;;` is what
reaches `--phase`, whose arm in the argument loop spans `unattended.sh:14273-14277`. Measured with
that awk at `c99ce09c3`, it prints 23 flags for 23 functions, each reached once; `--preflight` and
`--release-task` dispatch to handlers that never call it and stay out.

Two assertions follow the existing `-ge 3` floor, which stays as the vacuity guard. The liveness
arm asserts `--hold`, `--settle` and `--audit` are in the set, so a predicate that keeps only
`verb_*` handlers reds. The reach arm asserts every recorded function is some derived flag's
handler and names any that is not, so an arm reader that stops at a line misses `verb_phase` and
reds. The comment states both readings and drops the claim that the set is "every verb whose body
refuses", which a helper-dispatched verb falsified. The `hasnt_` loop iterates the flags as before.

**S2.** The seven lines, each `. "${BASH_SOURCE[0]%/*}/../../../../tools/lib/resolve-python.sh" || exit 2`
today, become the guard's one-line form, as the report gives it:

```bash
_d=.; [[ ${BASH_SOURCE[0]} == */* ]] && _d=${BASH_SOURCE[0]%/*}; . "$_d/../../../../tools/lib/resolve-python.sh" || exit 2
```

| Instrument | Line |
|---|---|
| `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh` | 10 |
| `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh` | 39 |
| `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-10-plan-fixture.sh` | 11 |
| `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-direct-checks.sh` | 16 |
| `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-15-direct-checks.sh` | 20 |
| `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` | 25 |
| `memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-12-direct-checks.sh` | 14 |

A tracked-tree `git grep` at `c99ce09c3` finds the unguarded strip on these seven lines and nowhere
else. The comment line above each stays true. No instrument assigns `_d` at top level; the only
`$_d` in them is literal text inside an awk program in the aSparedSpawn-15 record (lines 62-63). The
line adds no function, so the lexicon corpus does not move, and it forks nothing.

**S3.** At `.githooks/pre-push:1753-1755` a bar classed `other` sets the FULL reason "the bar this
push runs is not this kit's runner". When no bar record is adoptable, line 1791 keeps that
force, and line 2134 prints it on the `FULL gate on main push` line. The rewritten 25b at
`.githooks/pre-push.test.sh:470-483` scopes from arm 25's `gate-bar-green`, so no arm matches the
reason any more. Arm 25c goes directly after 25b in the same fixture. It clears every bar-record slot
of the work clone's git dir with `rm -f "$(git rev-parse --git-dir)"/gate-bar-green*`, which covers
`gate-bar-green`, `.scoped` and their `.shared` copies because that git dir is the common dir
(`.githooks/pre-push:1404-1414`). It then commits, writes a runner stamp at that commit with
`stamp`, and commits a file no earlier push carried, so the cover pass has nothing to answer with.
It pushes with `GOV_GATE_CMD="bash tracked-bar.sh"` and `GATE_SELFTESTS=` cleared, as 25b does, and
matches `*"FULL gate"*"is not this kit's runner"*`. The valid stamp is what makes the arm
discriminate: with the hook's `if [ "$bar_record" = other ]` block disabled, the push scopes from
that stamp. Arms 26 onward are refused before the cover pass or run under the stub, so 25c's own
green record moves none of them.

**S4.** Lines 1469-1471 say the control is "a GATE_REUSE=1 run after the lineage run". Since
`e0088cb2e`, `check_lin_control` at lines 1487-1496 runs no bar and compares field 4 of `pa`'s row in
`$tmp/ru.led` with `read_ru_key pa`. The three lines are rewritten to say that, and keep the reason:
without the control, a key that never matched passes the refusal arm as well as the lineage term it
names. Lines 1467-1468 stay, because AC6 still runs `GATE_REUSE=1`.

**S5.** `derive_kit_paths` answers `{{REVIEW_PROTOCOL}}` only from a `rendered` receipt row
(`tools/lib/render-doc.sh:198`), and gov has no `.governance/install.json`. So gov's renders say
"the review protocol of this repo", at `memory/TEMPLATE-SPEC.md:384` and at
`memory/guides/BUILD-METHOD.md:130` and `:331`. In the `got.update({...})` call of each copy
(`tools/lib/render-doc.sh:250`, `tools/memory-tree/adopt-memory-tree.sh:362`,
`tools/memory-tree/kit-dogfood-parity.test.sh:290`), one entry is added beside the
`{{SPEC_TOKEN_CHECKER}}` precedent:

```python
"{{REVIEW_PROTOCOL}}": got["{{REVIEW_PROTOCOL}}"] or (ans["gov_source"] == "." and "{{MEMORY_ROOT}}/guides/REVIEW-PROTOCOL.md"),
```

The `or` keeps a receipt row's answer first. Without it, an adopter whose receipt carries the row
would render the phrase, which the memory-hygiene self-test's I4 arm reds. Only a source tree with
no row reaches the path, and an adopter, whose `gov_source` is never `.`, keeps the phrase.
`{{MEMORY_ROOT}}` is resolved by `render_doc` after the `KIT_PATHS` pass (`tools/lib/render-doc.sh:51`).
The path is where the review-harness descriptor renders the protocol (`tools/workflows/kit.toml:39-41`).
Like that precedent it asks no `git ls-files`: `gov_source = "."` names gov itself, which tracks
the file. The ceiling, stated: a source-mode tree without the review-harness kit would cite a path
it lacks, and no such tree exists today; the `{{KICKOFF_SKILL}}` tracked check is the upgrade path.
The block's header comment, `tools/lib/render-doc.sh:88-89` and its twins, gains the source-repo
clause. Both edits sit inside the marked block, so all three copies take identical bytes, which
`tools/lib/resolve-python.test.sh` rows 168 and 171 gate.

The docs are re-rendered by `bash tools/memory-tree/adopt-memory-tree.sh --render`, the canonical
render path. That moves exactly the lines citing the token: 2 in `BUILD-METHOD.template.md` and 1 in
`SPEC-TEMPLATE.template.md`. `memory/guides/BUILD-METHOD.md` grows 6 bytes, well under its 30720
ceiling. If any other line moves, the two render paths disagree, and that goes back to the main loop
rather than into this diff. This reverses `TOOL-aSweptBar-4` S7's last sentence, "Gov answers the
phrase", for the reason the review's L2 gives.

`memory/guides/BUILD-METHOD.md` is on the kickoff manifest's `watch` list, and the staged leg refuses
a watched change without a re-stamp. The build commit therefore re-stamps `last-audit` in
`memory/guides/SESSION-KICKOFF.md` and carries a `manifest-audit: delta none` line, because §B line 57
already names `memory/guides/REVIEW-PROTOCOL.md`. `TOOL-aSweptBar-6` and `-4` did the same.

**S6.** `getval` empties its target first (`skills/session-kickoff/manifest-check.sh:366`), because
`LBC` has no initialiser and a caller's exported `LBC` would otherwise survive an absent key. Check
2's refusal at line 1365 would then never fire. Arm C2 at `manifest-check.test.sh:574-577` runs with
`LBC` unset. Directly after it, the same `c2k` repository is run again as
`LBC=$(head_sha "$R") run "C2 an exported LBC does not hide the missing key" ...` with the same
refusal text. A temporary assignment on a function call is exported to the checker that `run`
starts and leaves the suite's counters intact (probed on bash at spec time).

**S7.** Done in this spec pass. `memory/builds/aSweptBar/spec/2026-10-13-spec-TOOL-aSweptBar-3.md`
§4 S5 now says the plain bar also stamps a full green on the clean tree, as the evidence suite's
AC8 control observes, and the arm clears `gate-full-green` before the opt-in run. That is what
`tools/run-gates/run-gates.evidence.test.sh:1519-1521` does since `bc024b8b1`. Its header reads
rev-3, and its §8 carries the rev-3 line naming §4 S5. The builder touches no spec.

### Inventory

Nothing is minted: no function, file, flag or registry row. The arms are inline assertions, so the
codebase map's `symbols.json` does not move.

### Files touched (estimate)

- `tools/workflows/unattended-build.test.sh`
- `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh`
- `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh`
- `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-10-plan-fixture.sh`
- `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-direct-checks.sh`
- `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-15-direct-checks.sh`
- `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh`
- `memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-12-direct-checks.sh`
- `.githooks/pre-push.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/lib/render-doc.sh`
- `tools/memory-tree/adopt-memory-tree.sh`
- `tools/memory-tree/kit-dogfood-parity.test.sh`
- `memory/TEMPLATE-SPEC.md`
- `memory/guides/BUILD-METHOD.md`
- `memory/guides/SESSION-KICKOFF.md`
- `skills/session-kickoff/manifest-check.test.sh`

### Alternatives rejected

- S1 pinning the set against `VERBS_SLUG`: `--phase` refuses through `check_run_state` but sits in
  `VERBS_INLINE` beside five verbs that never do. Either pin needs an exception list, which is a
  hand-kept second copy. The reach arm compares two readings of the driver instead.
- S1 a fixed count: it reds on every retired or added verb without saying which handler moved.
- S5 reading the review-harness descriptor's `to` row inside `derive_kit_paths`: a TOML parse in a
  block byte-copied into three files, for a value only the source repo asks. The
  `{{SPEC_TOKEN_CHECKER}}` precedent answers the same source-repo-only question with a literal.
- S5 the finder's fix, which edits two of the three copies and breaks their byte parity.
- S3 asserting the reason inside 25b: 25b must scope from `gate-bar-green`, so a FULL decision
  cannot occur there. The FULL outcome needs a fixture with no record to adopt.

## 5. Acceptance criteria

- **AC1** — When the suite's F2 derivation is cut out and run alone with
  `DRV=tools/unattended/unattended.sh`, its flags include `--hold`, `--settle`, `--audit`,
  `--beat` and `--phase`, and every function whose body calls `check_run_state "` is reached by one
  of them. `grep -c 'every verb whose body refuses' tools/workflows/unattended-build.test.sh` prints
  0, and `bash -n tools/workflows/unattended-build.test.sh` exits 0.
  Red when: the `verb_` name filter returns, the set falls to 15, and `--hold` is absent.
  figure: DERIVED at observation; 23 flags for 23 functions is the PINNED reading of `c99ce09c3`.
- **AC2** — When each of the seven resolver lines, taken by `grep -h 'resolve-python.sh" || exit 2'`
  from its instrument, is written with a trailing `resolve_python` call to `i.sh` in a scratch
  `memory/builds/x/build/` folder, beside a copy of `tools/lib/resolve-python.sh` at the scratch
  root's `tools/lib/`, `bash i.sh` run from that folder prints an interpreter name. Over the tracked
  tree, `git grep -nE '(BASH_SOURCE\[0\]|\{0)%/\*' -- '*.sh'` prints only lines that also carry
  `== */*`.
  Red when: a line keeps the unguarded strip and the source fails with `Not a directory`.
  fixture: built under the run's scratch; none is in the tree. At `c99ce09c3` each of the seven
  lines reds it, which both skeptics observed.
- **AC3** — When `grep -n -B8 'FULL gate"\*"is not this kit' .githooks/pre-push.test.sh` runs, it
  shows arm 25c's pattern after 25b, and the arm's setup clears this git dir's `gate-bar-green*`,
  writes a `stamp`, and commits a file before its push. `bash -n .githooks/pre-push.test.sh` exits 0.
  Red when: the hook's `if [ "$bar_record" = other ]` block is disabled, so the push scopes from the
  runner stamp and the line names `gate-full-green`.
  permission: the RED and GREEN run of the arm is the main loop's, at the close.
- **AC4** — When `grep -c 'GATE_REUSE=1 run after the lineage run' tools/run-gates/run-gates.evidence.test.sh`
  runs, it prints 0, and `grep -n -A3 'EVERY REFUSAL ARM CARRIES ITS CONTROL' tools/run-gates/run-gates.evidence.test.sh`
  names `check_lin_control` and the input key in field 4.
  Red when: the header still describes a control that runs the cache's env mode.
- **AC5** — When `bash tools/memory-tree/adopt-memory-tree.sh --render` has run in gov,
  `grep -c 'guides/REVIEW-PROTOCOL.md' memory/TEMPLATE-SPEC.md memory/guides/BUILD-METHOD.md` reads 1
  and 2, and `git diff --numstat -- memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides/BUILD-METHOD.md memory/guides/ANNOTATION-STYLE.md`
  moves only those three lines. `sed -n '/^# >>> derive_kit_paths/,/^# <<< derive_kit_paths/p'`
  prints the same bytes for `tools/lib/render-doc.sh`, `tools/memory-tree/adopt-memory-tree.sh` and
  the parity suite beside the adopter, compared with `cmp`. A scratch adopter laid out as the
  memory-hygiene self-test's I4 arm lays it out (`build_fixture_r3`, `gov_source = "../gov"`, a
  review-harness receipt row at `docs/rp.md`) still renders `docs/rp.md` and no gov path.
  Red when: the `or` that keeps the receipt's answer is lost and that adopter renders the phrase, or
  one copy of the block differs from the others.
  figure: DERIVED; 1 and 2 are the token counts `git grep -c '{{REVIEW_PROTOCOL}}' -- 'tools/memory-tree/*.template.md'` gives.
  fixture: the adopter is built under `%TEMP%` at a short name, since it is a git repository.
- **AC6** — When `grep -n 'LBC=' skills/session-kickoff/manifest-check.test.sh` runs, it shows a C2
  arm that runs the checker with `LBC` set to the fixture's HEAD sha and expects the refusal
  `lacks a last-body-change value`. In a scratch repository laid out as arm C2 lays it out,
  `LBC=$(git rev-parse HEAD) bash skills/session-kickoff/manifest-check.sh` exits 1 naming that
  refusal.
  Red when: the `printf -v "$2" '%s' ''` line in `getval` is absent, the exported `LBC` survives the
  absent key, and check 2 never fires.
  fixture: a git repository under `%TEMP%` at a short name; the suite's `mkrepo` and `write_manifest`
  shape it.
- **AC7** — When `sed -n 3p memory/builds/aSweptBar/spec/2026-10-13-spec-TOOL-aSweptBar-3.md` runs, it
  reads `CLOSED · rev-3`, `grep -c 'stamps nothing' memory/builds/aSweptBar/spec/2026-10-13-spec-TOOL-aSweptBar-3.md`
  prints 0, and its revision log carries a rev-3 line naming §4 S5.
  Red when: §4 S5 still says only a full bar stamps.

## 6. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `pre-push self-test` · `run-gates evidence` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `install-prefix (shipped surface)` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `kickoff-manifest ratchet` · `build-method size` · `recall floor` · `recall floor arms` · `memory hygiene`

The close runs these in its one bar, with the suites run serially per the owner's ruling.

New arm: tools/workflows/unattended-build.test.sh · covers AC1 · put the `verb_` name filter back on the function pass and the liveness arm reds naming `--hold`; read each dispatch arm's first line only and the reach arm reds naming `verb_phase` · none
New arm: .githooks/pre-push.test.sh · covers AC3 · disable the hook's `if [ "$bar_record" = other ]` block and 25c reds on a decision scoped from the runner stamp · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC6 · delete the empty-first `printf -v` line in `getval` and the exported-LBC arm reds with no check 2 refusal · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft from the brief and the round-1 report, every cited line re-read
  at `c99ce09c3`; the S1 derivation, the S2 class and the S5 render effect measured over the tree.

## 9. Reuse audit

`python tools/codebase-map/reuse_lookup.py "derive a refusal set from a dispatch table and pin it
with a liveness member"` and `"render a sibling kit's document path in the shipping repo when no
install receipt row answers"` returned name-stem neighbours, plus `resolve_kit_dir`, which
`derive_kit_paths` already calls. No existing helper fits the arms, and this unit mints none. The
seams it extends are named in §4. The driver's own dispatch arms
(`tools/unattended/unattended.sh:14273-14277` and `:14307-14332`) answer S1. The guard at
`tools/hooks/format-guard.test.sh:17` answers S2. The suite's `stamp` helper and 25b's push form
answer S3. The `{{SPEC_TOKEN_CHECKER}}` source-repo entry in `derive_kit_paths` and the
review-harness rendered row answer S5. The `run` helper's inherited environment answers S6.
`VERBS_SLUG` and `VERBS_INLINE`, which `tools/unattended/check-unattended.sh` reads, were weighed for
S1 and rejected in §4. Recall returned the three precedent batches `TOOL-aGraftedHelix-32`,
`TOOL-aDistilledCharter-7` and `TOOL-aGraftedHelix-36`, and the review itself. It found no earlier
record of the F2 derivation or the source-repo protocol path.

Recall terms used: `python tools/memory-recall/query.py "how is a closing review's medium and low
findings batch built, and how are arms that lost coverage restored" --terms "closing review promoted
batch F2 refusal set check_run_state dispatch BASH_SOURCE resolver REVIEW_PROTOCOL getval LBC 25b"`

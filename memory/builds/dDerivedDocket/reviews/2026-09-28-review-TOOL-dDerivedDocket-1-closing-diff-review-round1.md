**Serves:** diff-review DEPL-dDerivedDocket-1 PLAY-dDerivedDocket-1 TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-49 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54 TOOL-dDerivedDocket-61 TOOL-dDerivedDocket-62 TOOL-dDerivedDocket-63 TOOL-dDerivedDocket-64 TOOL-dDerivedDocket-65

# Closing diff review (BUILD-METHOD M8): dDerivedDocket, per-build asks, derived status and ask-driven unattended runs

Node `d` · 2026-09-28 · Tier-2 · on `branch/backlog-maintenance-mechanics-10588f` · run phase VERIFYING, 50 units CLOSED and one WONTDO · adversarial fan through `tools/workflows/tier2-review.js`, with 4 finder lenses, then 5 skeptic batches, then this synthesis. The fan was briefed with the bug-class checklist that `tools/memory-tree/gotchas.py --for-diff` produced for exactly this range. Every confirmed finding below was re-read at source in this worktree before I adjudicated it. Three of them I also re-executed, as stated per finding. For the rest, the reproduction is the skeptic's, and I say so where it matters.

**Reviewed range:** `869209edc6f8056706989e05e45558607b0eb709...364278a8b104c6e42f250e68fb8d98fc210a1aa0`, **ROUND 1**. HEAD is `364278a8`. The diff is 172 commits and 444 files, +105049/−2887. The product share under `tools/`, `skills/`, `.githooks/` and `.github/` is 135 files, +37923/−1675. The rest is records, most of it the switch-over's 731 migrated asks.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing, and nothing is HIGH. The build is the shape its design record describes. Asks are filed once per build folder, status is folded from records, the family files are generated views, and pre-flip merges are audited rather than trusted. The unattended landing path rides a mandate observed on the remote. Five findings are MEDIUM, and four of them share one shape: a reader or probe that cannot answer falls through to the answer that lets the run continue. The run-gates age probe reads "different red" as "green there". The asks: mandate expander drops tokens it cannot parse. The plan counts a SEV row as a disposition. And a fail-closed rollback deletes the file it was protecting when its own backup failed. The fifth is a signal trap that resumes the attribution loop after cleanup. The remaining findings are LOW. Every fix below is a few lines plus one test arm. The build is at VERIFYING with verify-phase fix commits already its pattern, so I recommend folding the five MEDIUMs before the landing and either folding or filing the LOWs. A fold earns a round 2 over the fold itself, per M8.

## Review shape

Raw **15** · confirmed **11** · refuted **4** · unverified **0** · precision **0.73**.

Precision is well above the 0.5 floor §8 sets. The eleven confirmed findings collapse to **10 items**. Ids 6 and 14 are one defect, `read_conf_value` in `.githooks/straggler-guard.sh` disagreeing with the kit's conf parser, reported by two lenses with the same reproduction. I merged them here, at write time. The pipeline itself discarded no duplicates. Id 14 also names the same comment defect in `tools/check-wiring.sh`, and the merged item carries both sites.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 5 MEDIUM · 5 LOW** (10 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 5 MEDIUM · 6 LOW** (11 findings; ids 6 and 14 both take the LOW of the item that holds them).

The four refuted findings are the ids absent from the confirmed set: 2, 11, 12 and 15. A skeptic refuted each one, and none is carried here.

Two severities moved at adjudication. Id 14 came in as MEDIUM and is LOW here: the merged item's refusal layers only instruct, and hygiene check 26 still reads the conf through the Python parser at the bar and in remote CI, so the defect costs an early instruction and never a wrong merge. Id 1's skeptic judged it "closer to low than medium", but I hold it at MEDIUM. The trigger is narrow. The consequence, though, is a silent staged deletion of a build's authored asks that rides a commit, and preventing silent loss of backlog rows is this build's stated purpose.

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so the run is complete, and a zero in this report is evidence of absence within what the lenses read. That qualifier matters at this size. Four lenses over 38k added product lines is a prioritised read, not an exhaustive one. The brief pointed them at write paths, refusals, fail-closed claims, merge and landing logic, and fixtures that could pass by finding nothing. A class with no confirmed finding means the lenses hunted it and found nothing that survived a skeptic. It does not prove the class is absent from every line.

**Base choice, recorded deliberately.** M8 says round 1 runs from the run's pinned BASE. That base is `abac6d59`, and it predates two merges of `origin/main` into this branch, so a diff from it would re-review about 800 of main's own already-reviewed commits. This round instead runs from `origin/main`'s tip `869209ed`, which I confirmed is an ancestor of HEAD. The diff is therefore exactly what lands on main, reviewed once at the integration boundary as charter §8 requires. Round 2, if one runs, starts from this round's recorded tip `364278a8`.

**What this synthesis ran.** I re-read every cited line at source. I executed three reproductions by extracting the shipped functions verbatim into a scratch script:

- `read_conf_value` on three spellings: the quoted one reads `builds`, the commented one reads `builds   # flipped by unit 34`, and the exported one reads empty with rc 1. This covers ids 6 and 14.
- `expand_id_runs` on four asks: values. A `-5..6` continuation drops to the head id alone, a comma-suffixed id is dropped, an elision `…` yields only its two ends, and a canonical `N..M` expands correctly. This covers id 8.
- `ask_disposition_of` over an ask whose only row beside it is a SEV row. It returns `SEV`. This covers id 5.

I ran no suite and no bar leg. The unattended kit's own self-tests are not run on the owner's behalf, by standing owner ruling. The reproductions for ids 1, 3, 4, 7, 9, 10 and 13 are the skeptics', done in scratch fixtures. I verified their mechanism by reading the code, not by re-execution.

**Known and not re-reported**, per the brief. These were excluded from the finding set:

- The unattended kit's self-test verdict, which is pending the owner.
- The unattended DoD's two accepted forms, which are an owner decision.
- Hygiene check 23's owed acceptance-ledger lines.
- `VERB_OFFENDER_PIN` raised 982 to 1071, with the drain filed as TOOL-dDerivedDocket-67.
- The declined discoveries 38 to 47 and 55 to 60, which are kept asks.
- Unit 34's AC20, owed only if main moves.
- Spec 34 §4 step 1's merge-driver claim that did not reproduce.
- `migrate_backlog.py --ingest` raising `FileNotFoundError` on a missing `--signed` path.

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| F1 | MED | 4 | `tools/run-gates/run-gates.sh:2811` | For a leg with no `signature` (118 of 122), the age probe answers "green there" for a rev that is red with DIFFERENT output, so an old red can read young and land under `INHERITED_RED=land`. |
| F2 | MED | 8 | `tools/unattended/unattended.sh:3172` via `tools/unattended/lib-unattended.sh:1385` | The asks: mandate is expanded by a lossy reader that silently drops tokens the canonical reader refuses by name, so a run can close without disposing asks the owner named. |
| F3 | MED | 5 | `tools/unattended/unattended.sh:3792` | `--plan` takes a SEV, SCOPE or RELOCATED row as an ask's disposition, so an undecided ask reads covered and the `next:` ladder never offers it. |
| F4 | MED | 1 | `tools/unattended/unattended.sh:6849` | `had=1` is set before the backup exists; when the backup fails, the fail-closed rollback deletes the build's existing BACKLOG.md and stages the deletion. |
| F5 | MED | 13 | `tools/run-gates/run-selftests.sh:1571` | `trap attr_cleanup EXIT INT TERM HUP` never exits, so a signal cleans up and then RESUMES the attribution loop, which reports a false `verdict red`, exit 1, and a false orphan line. |
| F6 | LOW | 6, 14 | `.githooks/straggler-guard.sh:74`, `tools/check-wiring.sh:1137` | A second conf reader keeps an unquoted trailing comment and misses an `export` prefix, so the straggler layers go dormant on a flipped tree with a documented-legal spelling. |
| F7 | LOW | 3 | `tools/push-main.sh:365` | The carry-set refusal attributes a commit to a build by the FIRST id in its subject, so another build's commit that cites this build's id first is not FOREIGN. |
| F8 | LOW | 9 | `.githooks/pre-push:1168` | The S6 run-record check is skipped whenever `GOV_GATE_CMD` is set, yet every admissible override IS the runner, so the environment switches the envelope off. |
| F9 | LOW | 7 | `tools/memory-tree/migrate_backlog.py:1740` | `--relocate` inside an open merge filters "already accounted" at HEAD, not the index, so a re-run duplicates ask and RELOCATED rows. |
| F10 | LOW | 10 | `tools/memory-tree/transition_audit.py:704` | The per-merge delta cache sits in the shared git common dir and is keyed by merge sha and epoch only, not by the conf and grammar that shape the delta. |

### F1 — MEDIUM · the age probe reads "red with different output" as "green there" (id 4)

`tools/run-gates/run-gates.sh:2807-2812`, the tail of `check_red_at`:

```bash
  if [ -n "$A_RSIG" ]; then
    [ -z "$(LC_ALL=C comm -23 "$A_LSET" "$xset")" ] && return 0
    return 1
  fi
  cmp -s "$A_LSET" "$xset" && return 0
  return 1
```

Return 1 is the code the function uses for green, via `[ "$rc_x" = 0 ] && return 1` a few lines above. A leg without a declared `signature` therefore returns the green code for any rev where it is red with output that is not byte-identical after normalisation. Only 4 of the 122 legs in `tools/gate-legs.json` carry a signature. The normaliser strips paths and whitespace, not counts or offender lines. `derive_age` reads rc 1 at `R~n` as "not aged" and bisects toward the commit where the TEXT last changed, not the one where the red arrived. The age then comes back as a number under the bound, `land_n` counts the leg, and `ATTR_LANDABLE=1`. This repo declares `INHERITED_RED=land` and `INHERITED_RED_MAX_AGE=10` in `.githooks/gate-env.sh:83-84`.

Concrete case: a leg has been red since before `R~10` with offenders {a, b, c}, and a landing inside the window fixed c. Spec 24's own rule reads that as aged, because every L offender is present at `R~10`. The code names the fixing landing as owner at an age under 10, and the push lands over a red older than the declared bound.

Why MEDIUM and not HIGH: the red is inherited in every case. It is already on the default branch, and this path never admits a NEW red. What fails is the age bound's pressure, which exists to force a long-standing red to be fixed rather than carried. It fails in the unsafe direction, against the block's own rule that a probe which cannot answer leaves the age unproven. The WHAT-IT-DOES-NOT-CHECK list does not disclose it.

**Fix.** In the no-signature branch, when `rc_x != 0` and `cmp` fails, set `A_AGE_WHY` to say the output at that sha differs from L's, so whether L's red was already there cannot be answered, and `return 2`. That makes the age read unproven and blocks the landing. The better alternative is to compare sorted unique non-blank line sets and return 0 when L's set is a subset (`comm -23` empty), which is the signature branch's own rule applied to text.

**Left-shift.** Add an arm to `tools/run-gates/run-gates.test.sh`: a no-signature leg red at `R~n` with a superset output, and another with a changed count line. Assert the recorded age is `aged` or `-`, never a number, and that no inherited-green stamp is written. Class: `fallback-fabricates-the-passing-value` and `one-value-field-records-a-mixed-outcome`. One return code carries both "green" and "red, but I cannot compare", and the caller cannot tell them apart.

### F2 — MEDIUM · the asks: mandate is narrowed silently by a second, lossy reader (id 8)

`expand_id_runs` (`tools/unattended/lib-unattended.sh:1385-1399`) prints a token only when it matches `^[A-Z]+-[A-Za-z0-9]+-[0-9]+$` or the `N..M` run form, and drops everything else without a word. The producer that grades the mandate, `gen_build_index.py read_idlist`, reads the same IDLIST grammar all-or-nothing: it expands `-N` and `-N..M` continuations and refuses comma-suffixed tokens and elisions by name.

I re-executed the expander on four values, written here with the id elided:

- `<id>-3 -5..6` gives the `-3` id alone.
- `<id>-1, <id>-2` gives `-2` only, because the comma-suffixed first token is dropped.
- `<id>-1 … <id>-4` gives the two ends.
- A canonical `<id>-1..3` expands correctly.

The skeptic also reproduced `<id>-1,<id>-2` with no space. It expands to nothing and lands on a misleading fail 75.

The consequences follow from what reads the narrowed set. `check_ask_mandate` hands only the survivors to P5 and to `$ASKS_CMD --tsv --ready`. The witness's "fewer rows than asked" DEAD PROBE iterates the already-narrowed list, so it cannot fire. asks-disposed at `tools/unattended/unattended.sh:8196`, the leg's P5 re-derivation in `tools/unattended/check-unattended.sh`, and the mandate joins at 3440, 3718 and 9535 all read the same narrowed set. P6 compares raw strings, so it cannot notice either. A run can therefore close GREEN with asks the owner named never disposed.

This is the silent-narrowing class that fix F2 of the spec audits gave `read_idlist` its all-or-nothing rule to refuse, reintroduced one layer up. It is mitigated only when the README comes from `--new-build`, which writes canonical ranges. A hand-added asks: line is a sanctioned route (E1), and owners are recorded typing `-4` continuations.

Why MEDIUM: the mandate narrows and never widens, so no unauthorised work is admitted. But the run's claim that it finished the owner's asks becomes false with every check green.

**Fix.** Refuse the mandate at preflight when any whitespace token of the raw asks: value is not consumed. Have the expander print a `BAD <token>` marker the caller fails on by name. The stronger fix is to stop re-deriving: pass the RAW asks: tokens to `$ASKS_CMD --ready`, let `read_idlist` decide, and pin the ids it returns.

**Left-shift.** Add a parity arm that runs both readers over one shared table of IDLIST spellings (canonical, `-N`, `-N..M`, comma-suffixed, no-space comma, elision) and asserts they agree or both refuse. Add a preflight arm in `tools/unattended/unattended.test.sh` staging a `-N` continuation and a comma-suffixed id. Adding the arm is in scope; running that suite is the owner's, per the standing ruling. Class: `two-readers-of-one-config-one-re-derived`, `second-implementation-is-not-a-second-opinion` and `trailing-comma-counted-as-an-element`.

### F3 — MEDIUM · a SEV row reads as a disposition in the plan (id 5)

`tools/unattended/unattended.sh:3792-3794`:

```bash
    _disp=$(ask_disposition_of "$_bl" "$_id")
    [ -n "$_cover" ] || _cover="$_disp"
    [ -n "$_cover" ] || _cover="-"
```

`ask_disposition_of` (line 3198) returns the verb of ANY `- <VERB> · <id>` row. I re-executed it over an ask plus one `SEV · … · HIGH · triaged` row, and it returned `SEV`. Line 3806 then does `[ "$_cover" = "-" ] || continue`, so the ask is skipped for `ASK_PLAN_NEXT` and the UNDECIDED rung of the `next:` ladder is never reached for it.

The adjacent `ask_disposition_row_of` (line 3414) restricts to `ASK_STATUS_VERBS="CLOSED WONTDO BLOCKED DEFERRED KEEP REOPEN"`, and its comment names this exact misread. It was fixed for the DoD reader and left standing for the planner.

The impact is imminent rather than latent. V12 in `tools/memory-tree/backlog.py` requires a SEV row on every ask filed on or after `ASK_CUTOFF`, which is 2026-09-29, tomorrow. `memory/guides/UNATTENDED-ASKS.md` §5 has a declined discovery write its ask row and its SEV row in one commit, with the disposition due later. So after landing, almost every new ask reads covered in `--plan` and is hidden from an ask-driven run's planner.

Only the asks-disposed DoD at `--close` catches it. The run therefore stops late, at the close, rather than planning the ask. The failure direction is a stop and not a wrong landing, which keeps this at MEDIUM.

**Fix.** Take the cover from `ask_disposition_row_of` (the status-verb reader), not from `ask_disposition_of`. Better still, restrict `ask_disposition_of` itself to `ASK_STATUS_VERBS`, so there is one answer to "is this ask disposed".

**Left-shift.** Add a `--plan` arm with a SEV-only ask that asserts the ask is printed `cover=-` and offered as the UNDECIDED `next:`. Add a second arm with a RELOCATED-only ask, the other non-status verb. Class: `two-guards-one-question-two-answers`. The fix already existed one function away, which is the class's signature.

### F4 — MEDIUM · a failed backup turns the fail-closed rollback into a deletion (id 1)

`tools/unattended/unattended.sh:6848-6858`:

```bash
    had=0; prior=""
    if [ -f "$bl" ]; then had=1; prior=$(mktemp) && cp -- "$bl" "$prior"; fi
    ...
      if [ "$had" = 1 ] && [ -n "$prior" ]; then cp -- "$prior" "$bl"; GIT add -- "$bl" 2>/dev/null
      else GIT rm -q --cached -f -- "$bl" >/dev/null 2>&1; rm -f -- "$bl"; fi
```

The script runs `set -u`, not `-e`. When `mktemp` fails, `had=1` and `prior` is empty, so the restore guard is false. The else branch then deletes a file that existed before the write, and stages the deletion. When `mktemp` succeeds but `cp` fails, for example under an AV or file lock, the restore copies an empty or partial temp file over the backlog.

The chain that reaches the rollback holds under a broken TMPDIR. `write_backlog_rows` fails at its own `mktemp`, and `read_ask_back`'s `run_bounded` fails at `mktemp -d`, so the read-back returns 1. The skeptic narrowed reachability honestly. A TMPDIR broken from the start also breaks the bar's own `run_bounded`, which leaves no attribution record, and the function returns early. The trigger therefore needs the temp store to fail after the bar ran.

The tracked copy is recoverable from HEAD. But the deletion stays staged and rides the close's records commit, or the Skill's commit before `--hold`. Nothing reds: the file is gone rather than malformed, so asks-disposed simply sees fewer filings. The echoed message says the rows for one leg were removed, not that the whole file was.

**Fix.** Take the backup before touching the file, and treat a failed backup as a refusal to file:

```bash
if [ -f "$bl" ]; then
  had=1; prior=$(mktemp) && cp -- "$bl" "$prior" \
    || { rm -f -- "$prior"; echo "gates-green: no backup of $bl, nothing filed for leg $leg"; continue; }
fi
```

In the rollback, never delete a path that existed before the write. Restore it from the backup, or with `git restore --staged --worktree -- "$bl"`.

**Left-shift.** Add an arm that seeds a BACKLOG.md with an authored row, points `TMPDIR` at a non-writable directory after the attribution record exists, and runs the filer. Assert the file is byte-identical afterwards and no deletion is staged. Class: `destructive-step-before-its-precondition`. The rollback's precondition is that the backup exists, and the rollback never checks it.

### F5 — MEDIUM · the attribution trap cleans up and then resumes the loop (id 13)

`tools/run-gates/run-selftests.sh:1571`, `trap attr_cleanup EXIT INT TERM HUP`. `attr_cleanup` (1559-1567) neither exits nor clears `ATTR_WT`.

On INT, TERM or HUP, bash waits for the in-flight suite, runs cleanup (removing `ATTR_TMP`, `RS_SCRATCH` and the R worktree), then returns into the `while … done < $POP_FILE` loop. Every remaining suite's `> "$ATTR_TMP/l.out"` fails on the missing directory, which reads as `DEAD PROBE at L`. The run prints `verdict red` and exits 1 instead of 130 or 143. The EXIT trap then runs cleanup a second time. `remove_scratch_worktree` (`tools/run-gates/lib-attribute.sh`) fails on the already-removed path, which prints a false line saying the R worktree could not be removed and must be removed by hand.

The skeptic reproduced this shape under this host's bash: TERM at 0.4 s, then two DEAD PROBE rows, `verdict red`, rc 1, cleanup twice, and the false orphan line. The comment's premise is also false on this platform. With only `trap cleanup EXIT`, SIGTERM ran the handler at once and exited 143.

This regresses a fix the same diff's sibling already carries. `tools/run-gates/run-gates.sh` records this defect for its own ticket trap and gives each signal its own `exit 130/143/129` arm. It stays MEDIUM, although the verdict errs toward red, because an outer bound that TERMs the DoD run now reads as a genuine red verdict with exit 1. For an unattended driver that classifies stop causes, a wall cut and a real red become indistinguishable.

**Fix.** Use `trap attr_cleanup EXIT` plus `trap 'exit 130' INT`, `trap 'exit 143' TERM` and `trap 'exit 129' HUP`, so each signal re-exits and EXIT cleans up once. Set `ATTR_WT=""` after a successful removal so cleanup is idempotent. Correct the comment.

**Left-shift.** Add an arm to `tools/run-gates/run-selftests.test.sh` that sends TERM to `--attribute` mid-suite and asserts exit 143, no `verdict` line, one cleanup, and no "could not be removed" line. Class: `signal-trap-runs-the-exit-handler-twice` and `trapped-signal-waits-for-the-foreground-child`. Both were selected by the checklist for this range, and this is a live instance of both. A structural scan also fits: a trap naming INT, TERM or HUP whose handler body contains no `exit` reds.

### F6 — LOW · a second conf reader disarms the straggler layers on legal spellings (ids 6, 14)

`.githooks/straggler-guard.sh:74-81`, `read_conf_value`, greps `^[[:space:]]*KEY[[:space:]]*=`, takes everything after `=`, strips quotes and edge blanks, and stops there. I re-executed it on three spellings. The quoted `BACKLOG_MODE="builds"` reads `builds`. The unquoted `BACKLOG_MODE=builds   # flipped by unit 34` reads `builds   # flipped by unit 34`. The exported `export BACKLOG_MODE=builds` reads empty with rc 1. `tree_lib.parse_conf_line` in `tools/memory-tree/tree_lib.py` reads `builds` for both of the latter. Its docstring, from TOOL-aScouredKit-19, records both spellings as legal, because the shell gate sources the conf with `set -a`. It also records that a reader which mis-reads them removes coverage while the gate stays green.

`init_straggler_guard` then takes `[ "$mode" = builds ] || return 1` and prints nothing. The pre-commit refusal, the pre-rebase refusal and the per-ref pre-push straggler layer all go dormant, against the file's own LIVENESS header. `read_conf_modes` mis-classifies builds-mode merge bases as shards for the same reason. A commented `MEMORY_ROOT` would corrupt `STRAGGLER_WATCHED` the same way. `tools/check-wiring.sh:1137-1138` (`check_backlog_stragglers`) has the same trailing-comment defect. It also misses `export`, and it at least prints a skip line, though the reason it prints is wrong.

Why LOW: gov's conf spells `BACKLOG_MODE="builds"` with no comment, so the defect is latent here. Hygiene check 26 reads the conf through the Python parser at the bar and in remote CI, so a dormant hook layer costs an early instruction and never a wrong merge. The header's own words are "these layers instruct; the bar decides". It is reachable for any adopter using a documented-legal spelling.

**Fix.** Port `parse_conf_line`'s two rules into both shell readers: accept an optional `export ` before the key, and drop an unquoted `#` that begins a word before peeling quotes. Better, ask the kit's parser rather than re-deriving it.

**Left-shift.** Add a shell-versus-Python agreement arm to `.githooks/straggler-guard.test.sh` and `tools/check-wiring.test.sh` over the absent, blank, quoted, commented and exported spellings. The hygiene suite already runs this arm for its own reader. Class: `two-readers-of-one-config-one-re-derived`. A class-level scan for ad-hoc `.memory-tree.conf` key readers in shipped shell outside the sanctioned one would stop the next copy.

### F7 — LOW · the carry-set refusal trusts the first id in a subject (id 3)

`tools/push-main.sh:362-370`, `resolve_commit_build`, returns the slug of the first `[A-Z][A-Z]+-[A-Za-z]+-[0-9]+` token in the commit subject. The build-folder fallback runs only when the subject holds no id. So another build's records commit whose subject leads with this build's id is read as this build's. `check_carry_set` then prints it without FOREIGN, and `--land` publishes it. That is the fail-open case the function's own header rules out, in the refusal that TOOL-dDerivedDocket-2 exists to provide.

The subject shape is ordinary in this repo. `fd4c11f0`, `e6573b75` and `beb75c23` are each one build's `records(<slug>):` commit whose subject leads with another build's id. Records commits are doc-only, which §3 routes straight onto local main, unpushed: exactly the carry-set population. The per-build ask flow makes cross-build citations routine, because a build disposing another build's ask cites that ask's id.

The rule matches spec 2 as written. The spec's predicate contradicts the refusal's purpose, and the code is inside this diff.

**Fix.** Classify by the build folders the commit touches first. Accept a subject id as ownership only when the touched folders agree, or when it is the slug in the conventional `<verb>(<slug>):` prefix. Anything ambiguous is FOREIGN.

**Left-shift.** Add an arm to `tools/push-main.test.sh`: a commit touching only another build's folder, whose subject cites this build's unit id first, on local main. Assert `--land` refuses it as FOREIGN. Class: `record-citing-a-foreign-id-defines-or-orphans-it`, the same misread one layer up. A cited id is taken as a definition of ownership.

### F8 — LOW · the S6 run-record check is switched off by the environment (id 9)

`.githooks/pre-push:1167-1174`: when `rc` is 0 and `GOV_GATE_CMD` is set, the hook announces that the override's run record is not checked and skips `check_verdict_record`. The premise, that an override is not the runner and writes no record, does not hold here.

`check_bar_command`'s `declared` rule admits only `bash $GATE_RUNNER` or the committed `GATE_CMD`. In gov those are the same script: `.unattended.conf:42` declares `GATE_CMD="bash tools/run-gates/run-gates.sh"`. So every admissible non-stub override is the runner, which receives the exported `GATE_RUN_ID` and writes the record that the skip declines to read.

That value vets as `bar_class=tracked`, and `tools/push-main.sh` still writes the lander marker for it. The hook's own refusal text points operators at that exact value. So exporting it switches off the envelope added after TOOL-aSurfacedLexicon-25's unexplained exit-0 landing, against the hook's rule that the environment may REFUSE, never SELECT.

Why LOW: it matters only if the runner's still-unexplained exit-0-without-a-verdict path recurs under an override.

**Fix.** Key the skip on what ran, not on the knob. Run `check_verdict_record` whenever the vetted bar path equals `$GATE_RUNNER`. Skip it only for a declared `GATE_CMD` naming a different script, and announce that skip.

**Left-shift.** Add an arm to `.githooks/pre-push.test.sh`: `GOV_GATE_CMD` equal to the runner, with a runner double that exits 0 without writing `verdict GREEN`. Assert the push reds. Class: `inputs-inside-the-subjects-reach`. The subject's environment chooses whether its own verdict is checked.

### F9 — LOW · `--relocate` is not idempotent inside an open merge (id 7)

`tools/memory-tree/migrate_backlog.py:1740` filters already-accounted entries with `audit.accounted(entries, "HEAD", …)`. During `--relocate` inside an uncommitted merge, HEAD is the straggler's pre-flip commit, so rows the previous run wrote into the index count as unaccounted and are planned again. `add_row` appends without a presence check. `check_collisions` guards only status-class rows, so ask and provenance rows pass it.

The skeptic reproduced this in a hermetic `seed_transition` fixture. A straggler added one NEW OPEN ask, `git merge --no-commit main` ran, then `--relocate` ran twice. Run 2 exited 1 after writing, which left the ask row twice in the home build's BACKLOG.md, two identical RELOCATED rows in the relocating build's, both staged, and a check 26 DUPLICATE the operator must hand-delete.

The S7 comment claims every verb is idempotent. The only idempotence arm covers `--repair` after a commit. The verb's own exit-1-after-write path invites exactly this re-run.

**Fix.** For `--relocate`, and for any run with `MERGE_HEAD` present, compute `open_now` with `audit.accounted(entries, audit.INDEX, root)`, which is the tree the merge commits, as line 2038 already does for the post-write re-read. Alternatively, skip a record whose exact line already exists in its target file.

**Left-shift.** Add an arm to `tools/memory-tree/migrate_backlog.py`'s own self-test: `--relocate` twice in one open merge, where the second run writes zero records and exits 0. Class: `guard-fed-the-value-it-supersedes`. The filter reads HEAD while the index supersedes it.

### F10 — LOW · the delta cache key omits the inputs that shape the delta (id 10)

`tools/memory-tree/transition_audit.py` `read_cache`/`write_cache` (696-727) key each entry on `<merge>.json` and `CACHE_EPOCH = 1` (line 54). The directory is under `rev-parse --git-common-dir`, which every worktree shares.

`derive_entries` also depends on the working tree's `.memory-tree.conf`, whose `MEMORY_ROOT` and `FAMILIES` fix the watched paths and `archive_re`. It depends as well on the recall conf's families, cited families and node-tag eras, via `extract.grammar_for`. None of those enters the key. `accounted()` re-reads the CURRENT grammar and families, so a stale cached delta gets graded against a new grammar. After retiring a family, a warm node reads cached entries as UNACCOUNTED while remote CI's cold `history-audit` does not produce them. Two worktrees with different confs disagree the same way.

The sibling kit measured and fixed this exact class for its own cache: `recall_conf.Conf.digest()` in `tools/memory-recall/recall_conf.py` folds root, families, eras and the kit version into its freshness key. That contradicts `read_cache`'s docstring, which says the delta cannot change while the merge exists.

Why LOW: the only effect is a local-versus-CI disagreement until the cache is deleted. Nothing lands wrong.

**Fix.** Write a fingerprint of the inputs into each entry beside the epoch: memory root, sorted families, conf path, and the resolved grammar's id pattern or `Conf.digest()`. Treat a mismatch as the existing "foreign epoch" recompute.

**Left-shift.** Add an arm to `tools/memory-tree/transition-audit.test.sh`: warm the cache, edit `FAMILIES`, re-run, and assert the delta is recomputed and equals a cold run's. Class: `join-key-widened-by-a-shared-location`. A cache shared across worktrees is keyed narrower than what it caches.

## Bug classes

`gotchas.py --for-diff 869209ed..364278a8` selected 84 classes, 78 by anchor plus 6 universal, over 444 changed files. The brief took them first. Confirmed live instances:

- `two-readers-of-one-config-one-re-derived`: F2, F6.
- `second-implementation-is-not-a-second-opinion` and `trailing-comma-counted-as-an-element`: F2.
- `two-guards-one-question-two-answers`: F3.
- `destructive-step-before-its-precondition`: F4.
- `signal-trap-runs-the-exit-handler-twice` and `trapped-signal-waits-for-the-foreground-child`: F5.
- `fallback-fabricates-the-passing-value` and `one-value-field-records-a-mixed-outcome`: F1.
- `record-citing-a-foreign-id-defines-or-orphans-it`: F7, by analogy.
- `inputs-inside-the-subjects-reach`: F8.
- `guard-fed-the-value-it-supersedes`: F9.
- `join-key-widened-by-a-shared-location`: F10.

No confirmed finding fell in `fixture-passes-by-finding-nothing`, the class the brief prioritised. Every stage returned, so that is the lenses' answer and not a hole. It is bounded by the coverage caveat under Run integrity. Several fixes above do add the missing failing-case arm, which is that class's remedy applied forward: F1, F3, F5 and F9 each cover a path no current arm reaches.

## Next

Fold F1 to F5 before the landing, each with its arm, and fold or file F6 to F10. A fold that touches product code earns a round 2 per M8. It runs from `364278a8` to the fold's tip, with this round's confirmed set as `priorFindings`, and it reads the fold rather than re-reading the diff. That matters because fold text is unreviewed surface.

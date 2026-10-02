# TOOL-aSightedSkeptic-13 — check 23 stops grading a run that derived LANDED

**Status:** SPECCED · rev-1 · 2026-10-02 · node a · Tier-2 · base 4e0057a7 · streams tooling · order 13 · ratified 2026-10-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-02-prompt-TOOL-aSightedSkeptic-13-1-spec-brief.md](../prompts/2026-10-02-prompt-TOOL-aSightedSkeptic-13-1-spec-brief.md) | journal | — |
| [2026-10-02-prompt-TOOL-aSightedSkeptic-13-2-build-brief.md](../prompts/2026-10-02-prompt-TOOL-aSightedSkeptic-13-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Check 23 of the unattended kit gate skips a run record only when its own `phase` fact reads `LANDED`
or `ABORTED`. Under in-place landing a landed record stays `LANDING` forever, so check 23 re-grades
every in-place run that ever landed, on every bar, and its undeclared-write count carries landed,
append-only history against every later run's ceiling. This unit makes check 23 apply the
derived-LANDED exclusion check 7 already applies, through one predicate both checks call, and lowers
the shrink-only pin to the count that remains.

## 2. Scope (IN)

- **S1** — One predicate in `tools/unattended/check-unattended.sh`, `check_derived_landed`, defined
  directly below `check_adv_reaches`. It takes a run-state path and returns 0 when the record is
  derived LANDED, 1 when it is not, and 2 when the answer is UNAVAILABLE. On 0 it sets the global
  `DERIVED_LANDING_COMMIT` to the landing commit. Observed by AC1, AC2, AC3 and AC5.
- **S2** — Check 7 calls `check_derived_landed` in place of its inline test, and its EXCLUDED and
  UNAVAILABLE lines stay byte-identical. The local anchor `c7anchor` is retired, and the UNAVAILABLE
  condition reads `ADV_HEAD_OK` instead. Observed by AC5.
  **Readers:**
  by name: only check 7's own block in `tools/unattended/check-unattended.sh` spells `c7anchor`.
  by value: NO VALUE READERS — the value was the advertised tip, which `ADV_HEAD` still carries.
- **S3** — Check 23 calls `check_derived_landed` for every record that survives its existing
  `LANDED|ABORTED` skip and its existing no-dispatch skip. A derived-LANDED record is not graded and
  prints one `check 23 EXCLUDED` line on the default channel. Observed by AC1 and AC2.
- **S4** — Check 23 prints one `check 23 exclusion UNAVAILABLE` line per run on the default channel,
  the first time the predicate returns 2, and grades that record as before. Observed by AC3 and AC4.
- **S5** — The leg's header exception TWO names check 23's two notices beside check 7's, so the
  header's "exit 0 + no output" contract still describes the code. Observed by AC8.
- **S6** — Four new arms in `tools/unattended/check-unattended.test.sh`, placed directly after the
  check 23 ceiling arms. Observed by AC1, AC2, AC3, AC4 and AC6.
- **S7** — `UNDECLARED_WRITE_CEILING` in `.unattended.conf` falls to the count measured after the
  change, never rises, and its comment names the closing cause. The comment's sentence that check 23
  stops grading only at a terminal phase is corrected. Observed by AC7.
- **S8** — The unattended kit version moves 1.55 to 1.56 in every carrier, and the kickoff manifest's
  `last-audit` is re-stamped for the watched `.unattended.conf`. Observed by AC9 and AC10.

## 3. Non-goals (OUT)

- **Check 22** carries the same skip shape, at `tools/unattended/check-unattended.sh` lines 3434 to
  3437 (`for f in $RUNS` then `LANDED|ABORTED) continue`). It grades a live record's README
  amendments, and whether a derived-LANDED record still owes that is its own question. Follow-up, not
  this unit.
- **Check 19's grant arm**, lines 2265 to 2269, already reads a LANDING record's landing commit
  through `read_landing_commit` and `check_adv_reaches`, so it carries the same test inline. It is not
  a defect, because it already excludes correctly. Routing it through `check_derived_landed` is a
  follow-up refactor, not this unit's mechanism.
- **Check 15's fact-set arm**, lines 1851 to 1859, is mode-specific by design: under `in-place` a
  committed LANDING is graded rather than excluded. It does not share this predicate.
- **The driver's `read_derived_phase`** in `tools/unattended/unattended.sh` answers the same question
  against its own once-per-process quiet observation. Sharing it would put `ADV_HEAD` into the kit
  library. Untouched.
- **Raising the pin**, for any reason. See §4 Rollout for what happens if the measured count exceeds
  it.
- **Check 23's dodged-join and ambiguous-attribution branches** keep their shape. They stop printing
  for derived-LANDED records only because those records are no longer graded.
- **Check 7's grandfathered `nlive` reporting** below the exclusion is unchanged.

### Edges

- **consumes-from** external — `read_landing_commit` in `tools/unattended/lib-unattended.sh` and the
  leg's `ADV_HEAD_OK` and `check_adv_reaches`, all present at base; this unit builds none of them.

## 4. Design

### Evidence

Read at base `4e0057a7`; `tools/unattended/` is byte-identical at the run branch's tip `d552c77e`.
Line numbers are PINNED to that reading; the builder locates each by the quoted text.

| Site | Lines | What it does today |
|---|---|---|
| `check_adv_reaches` | 404–426 | ancestry against `ADV_HEAD`, from a reach set warmed once per shell when `ADV_HEAD_OK` is 1 |
| `ADV_HEAD_OK` | 1208–1209 | 1 when the advertised HEAD resolves to a commit here, fixed for the run |
| check 7 anchor and UNAVAILABLE | 2651–2659 | `c7anchor` re-verifies `ADV_HEAD` with `rev-parse`; prints UNAVAILABLE when more than one record is live and no anchor resolves |
| check 7 loop | 2661–2678 | phase LANDING, `read_landing_commit`, then `merge-base --is-ancestor` against `c7anchor` |
| check 23 record loop | 3625–3640 | the LANDED-or-ABORTED skip, then dispatch rows, then the no-dispatch report skip |
| check 23 ratchet | 3819–3829 | liveness on `ds_graded`, then the count against `UNDECLARED_WRITE_CEILING` |
| `read_landing_commit` | lib 1065–1074 | the commit that last wrote the record at HEAD, when HEAD's copy reads LANDING and the working copy differs in lease lines only |

`c7anchor` and `ADV_HEAD_OK` answer one question two ways: `rev-parse --verify` of `ADV_HEAD^{commit}`
and `cat-file -e` of the same object. Both are true exactly when that commit is in this clone, so
check 7 keeps its verdict when it reads `ADV_HEAD_OK`.

A read-only probe over the tracked run records at base, testing each record's last commit against
`git ls-remote origin HEAD`, found seven `LANDING` records on the advertised tip. Six carry dispatch
rows: aRepatriatedFork, dAlignedCarrier, dDerivedDocket, dMendedRecall, dRatifiedSeam and
dRetiredFork. Those six are what check 23 stops grading here. The figure is PINNED to 2026-10-02 and
is evidence for the design, not an acceptance number.

### Data model

```bash
DERIVED_LANDING_COMMIT=""
check_derived_landed() { # run-state file -> 0 derived LANDED (sets DERIVED_LANDING_COMMIT) · 1 not · 2 UNAVAILABLE
  DERIVED_LANDING_COMMIT=""
  local _dl_c
  [ "$(phase_of "$1")" = LANDING ] || return 1
  _dl_c=$(read_landing_commit "$1" 2>/dev/null) || return 1
  [ "${ADV_HEAD_OK:-0}" = 1 ] || return 2
  check_adv_reaches "$_dl_c" || return 1
  DERIVED_LANDING_COMMIT=$_dl_c
}
```

Its header comment states two things. It is CALLED AS A PLAIN COMMAND, never inside `$(...)`, because
a substitution discards both the global and the reach set `check_adv_reaches` warms, and would re-walk
the advertised history once per record. And it is mode-independent, exactly as check 7 and the
driver's `read_derived_phase` are: ruling D12-i2 derives LANDED from the remote, not from
`LANDER_MODE`.

Check 7 becomes, with the two message strings unchanged:

```bash
if [ "$nlive" -gt 1 ] && [ "$ADV_HEAD_OK" != 1 ]; then printf '<the existing UNAVAILABLE line>'; fi
...
  if check_derived_landed "$c7f"; then
    c7drop="$c7drop $c7f"
    printf '<the existing EXCLUDED line, with $DERIVED_LANDING_COMMIT and $ADV_HEAD>'
  else ...
```

Check 23 adds, after the no-dispatch skip and before the row loop, with `ds_unavail=0` declared
beside `ds_over`:

```bash
  check_derived_landed "$f"; ds_dl=$?
  if [ "$ds_dl" = 0 ]; then
    printf 'unattended: check 23 EXCLUDED %s — derived LANDED: its landing commit %s is an ancestor of the advertised default-branch tip %s, so its dispatch history is landed and append-only and is not graded against the ceiling\n' "$f" "$DERIVED_LANDING_COMMIT" "$ADV_HEAD"
    continue
  fi
  if [ "$ds_dl" = 2 ] && [ "$ds_unavail" = 0 ]; then
    ds_unavail=1
    printf 'unattended: check 23 exclusion UNAVAILABLE — no advertised default-branch tip resolves in this clone, so a LANDING record already on the remote cannot be told from a live one; every LANDING record with dispatch rows is graded\n'
  fi
```

Placing the call after the no-dispatch skip keeps the default channel quiet for derived-LANDED
records that were never graded. Placing it after the `LANDED|ABORTED` skip is what makes the
exclusion a no-op under `LANDER_MODE=primary` in steady state, where every landed record is rewritten
to `LANDED` and never reaches the predicate.

The ratchet below is unchanged. Excluding records lowers `ds_graded` too, and its liveness branch
still fires only when the ceiling is above zero and nothing at all was graded.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `check_derived_landed` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest check_derived_landed --as sh.function` answered OK |
| `DERIVED_LANDING_COMMIT` | shell global | not graded; no shell-variable cell is declared |
| `ds_unavail`, `ds_dl` | check 23 locals | not graded |
| `check 23 EXCLUDED`, `check 23 exclusion UNAVAILABLE` | default-channel message heads | none |

### The arms (S6)

Each arm opens with `reset_tree`, builds on the existing check 23 fixture (a `drow` declaring
`work/one.txt`, then a commit writing `work/one.txt` and the undeclared `work/stray.txt`), and asserts
only check-23-specific strings, because a LANDING record also moves checks 7, 15 and 19.

| Arm | Fixture after the stray write | Asserts | Red against |
|---|---|---|---|
| A | phase set to `LANDING`, committed, `git push -q -f origin HEAD:main`, restored to `$ANCHOR0` after | `check 23 EXCLUDED` with the record and `$(git rev-parse HEAD)`; no `check 23 FAILED` | the pre-change gate |
| B | phase `LANDING`, committed, not pushed | `check 23 FAILED`; no `check 23 EXCLUDED` | a staged break returning 0 for any committed LANDING record |
| C | phase `LANDING`, committed, origin's HEAD symref pointed at `refs/heads/nothing-here`, restored after | `check 23 exclusion UNAVAILABLE` exactly once; `check 23 FAILED` | the pre-change gate, and a break treating return 2 as excluded |
| D | phase `LANDED`, committed, symref pointed at `refs/heads/nothing-here`, restored after | no `check 23 EXCLUDED`; no `check 23 exclusion UNAVAILABLE` | a break moving the predicate call above the LANDED-or-ABORTED skip |

Arms B and D are CONTROLS. A control that is red against the pre-change gate would mean that gate
was already wrong, so each is observed red against the staged break its row names instead. This is
the one place the spec departs from the brief's "each arm observed RED against the pre-change gate".

Check 7's existing arm (`check 7 EXCLUDED memory/builds/tLand/RUN.md — derived LANDED`) is the
regression witness for S2, observed red against a staged break making `check_derived_landed` always
return 1.

### Rollout

1. Before any edit, measure: `bash tools/unattended/check-unattended.sh --emit-ceiling`, recording
   stdout, stderr and wall time to the scratchpad. This is the BEFORE count.
2. Write S1 to S5 and the arms.
3. Observe each arm red and green with a scratchpad slice of the suite: its prologue and the new
   block only, with `HERE` set to `tools/unattended` and `TMPDIR` set to a short `%TEMP%` directory
   for the fixture repositories. Stage each break in the leg, run the slice, then
   `git checkout -- tools/unattended/check-unattended.sh` and confirm a clean diff before the next.
4. Measure again with `--emit-ceiling`. This is the AFTER count.
5. If AFTER is at or below 45, set `UNDECLARED_WRITE_CEILING` to AFTER, add a dated comment line
   naming this unit and the six records it stopped grading, and correct the terminal-phase sentence.
   If AFTER is above 45, the pin is not touched and the pass parks with the per-instance report lines
   (`GOV_UNATTENDED_REPORT=1`), because raising it is a non-goal.
6. Bump the kit version in every carrier and re-stamp the manifest, then commit once.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`.unattended.conf` · `tools/unattended/` (the version carriers) · `memory/guides/` (the rendered
kit docs and `memory/guides/SESSION-KICKOFF.md`) · `.claude/skills/unattended/SKILL.md`

### Alternatives rejected

- **Put the predicate in `tools/unattended/lib-unattended.sh`.** That is where `read_landing_commit`
  lives, but the advertised tip, `ADV_HEAD_OK` and the reach set are leg state that the library never
  sees. The driver observes the remote its own way, through `read_advertised_tip`. Moving the leg's
  observation into the library would give it a second owner. See §8 F1.
- **Print the landing commit on stdout and call the predicate in `$(...)`**, the shape
  `check_generated_render` uses. It discards the warmed reach set on every call, so each record would
  re-walk the advertised history. The driver's `read_derived_phase` takes the global-setting shape for
  the same reason.
- **Gate the exclusion on `LANDER_MODE=in-place`.** Check 7 does not, and two checks applying one
  predicate under two conditions is the drift the shared predicate exists to prevent.
- **Announce on the report channel.** Header exception TWO records why check 7 moved off it: an
  exclusion changes the verdict, and a REPORT line is invisible on every bar run.

## 5. Production-readiness checklist

- security — N/A: a read-only gate leg; no new input crosses a trust boundary, and the landing commit
  is found by the library rather than read from a field the run authors.
- perf / scale — the predicate adds one `read_landing_commit` per LANDING record that has dispatch
  rows, and removes the whole row walk for each derived-LANDED one, which is the leg's dominant cost.
  The reach set is warmed once per shell. The two `--emit-ceiling` wall times in Rollout record the
  effect.
- error / empty / loading states — the predicate fails closed: an uncommitted record, no
  advertisement or an unresolvable tip keeps the record graded, and UNAVAILABLE says so once.
- observability — every exclusion prints the record, its landing commit and the tip on the default
  channel, and the header's contract line is amended to admit them.
- risks — the leg's default output grows by one line per derived-LANDED record with dispatch rows. The
  suite's whole-output green controls run on fixtures holding none, so `remove_announcements` is not
  widened. If AFTER exceeds 45 the unit parks rather than closing.
- testing — arms A to D plus check 7's existing arm, each observed red against its named break.
- migration — the pin falls; adopters ship at `0` and are unaffected. No data moves.
- user docs — N/A: no verb, flag or conf key changes; the kit README's `--emit-ceiling` line still
  describes the measurement.

## 6. Acceptance criteria

- **AC1** — When the slice runs arm A, the output carries `check 23 EXCLUDED` naming the fixture
  record and its landing commit, and carries no `check 23 FAILED`.
  Red when: run against the pre-change `tools/unattended/check-unattended.sh`, which grades the record
  and fails at the fixture's ceiling of 0.
  fixture: the suite's own check 23 fixture and bare origin; nothing in the tree is required.
- **AC2** — When the slice runs arm B, the output carries `check 23 FAILED` and no
  `check 23 EXCLUDED`.
  Red when: `check_adv_reaches` is removed from `check_derived_landed`, so any committed LANDING record
  is excluded.
- **AC3** — When the slice runs arm C, `grep -c 'check 23 exclusion UNAVAILABLE'` over its output
  prints 1, and the output carries `check 23 FAILED`.
  Red when: run against the pre-change gate (no UNAVAILABLE line), or with check 23 treating return 2
  as excluded (no FAILED line).
- **AC4** — When the slice runs arm D, the output carries neither `check 23 EXCLUDED` nor
  `check 23 exclusion UNAVAILABLE`.
  Red when: the `check_derived_landed` call is moved above the `LANDED|ABORTED` skip, so a recorded
  LANDED record with no advertisement prints UNAVAILABLE.
- **AC5** — When `grep -c 'check_derived_landed' tools/unattended/check-unattended.sh` runs it prints
  at least 3, `grep -n 'c7anchor' tools/unattended/check-unattended.sh` prints nothing, and the slice
  run of check 7's existing arm passes, asserting `check 7 EXCLUDED` with its unchanged text.
  Red when: `check_derived_landed` is staged to always return 1, which reds check 7's arm and proves
  check 7 reads the shared predicate.
- **AC6** — When `bash tools/unattended/check-arms-groups.sh` runs over the edited suite it exits 0.
  Red when: two new arms in one group carry an identical assertion text, or a capture is named other
  than `out`.
- **AC7** — When `bash tools/unattended/check-unattended.sh --emit-ceiling` runs before the edit and
  after it, stdout prints one `UNDECLARED_WRITE_CEILING=` line each time, the AFTER value is at or
  below the BEFORE value and at or below 45, and `grep -n '^UNDECLARED_WRITE_CEILING=' .unattended.conf`
  at the pass's commit prints the AFTER value.
  Red when: AFTER equals BEFORE while derived-LANDED records with dispatch rows exist, the pin differs
  from AFTER, or the pin rose.
  cost: the leg's recorded wall time on node a is 886 s to 2029 s per run, so two runs cost up to
  about an hour.
  figure: BEFORE and AFTER are DERIVED at observation time; 45 is the pin at base.
- **AC8** — When `sed -n 1,45p tools/unattended/check-unattended.sh | grep -c 'check 23'` runs it
  prints at least 1.
  Red when: the header's exception TWO still names check 7 alone while check 23 prints on the default
  channel.
- **AC9** — When `bash tools/check-kit-versions.sh` and `python tools/govkit/govkit.py epoch` run they
  exit 0, `grep -n '^KIT_UNATTENDED_VERSION=1.56' tools/unattended/unattended.sh` prints one line, and
  `git grep -l 'gov:kit unattended@1.55' -- tools .claude memory/guides` prints nothing.
  Red when: a carrier still names 1.55, or a shipped byte moved without the version.
- **AC10** — When `bash skills/session-kickoff/manifest-check.sh` runs at the pass's commit it exits 0.
  Red when: `.unattended.conf` moved and `last-audit` in `memory/guides/SESSION-KICKOFF.md` was not
  re-stamped.

## 7. Gates

`unattended kit gate` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `kickoff-manifest ratchet` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-unattended.test.sh · arms A to D after the check 23 ceiling arms, each staged per §4's arm table · none (this suite declares no assertion floor)

The suite itself is withheld from the bar by the 2026-08-23 owner ruling. The main loop runs the
slice and the `unattended kit gate` leg at VERIFYING.

## 8. Open questions

- **F1 — Does the shared predicate live in the leg or in the kit library?** The brief asks this be
  decided by reading where `read_landing_commit` lives. (a) The leg, directly below
  `check_adv_reaches`, calling the library's `read_landing_commit`. (b) The library, beside
  `read_landing_commit`. (b) needs the leg's advertised tip, `ADV_HEAD_OK` and reach set in the
  library, which the driver does not use, since it observes through `read_advertised_tip`. The leg's
  other ancestry predicates, `check_head_reaches` and `check_adv_reaches`, already live in the leg.
  Recommendation (a).
  RESOLVED (agent, 2026-10-02, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-02 · initial draft, from the owner-adopted spec brief, the leg and the kit library
  read at base `4e0057a7`, and a read-only probe of which tracked LANDING records are on the
  advertised tip.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "exclude a run record whose landing commit is on the advertised default-branch tip"`
ranked name-stem neighbours only (`run`, `records`, `build_run_model`, `derive_record_commits`), none
of which reads a run record's phase against the remote, and printed `unscanned layers: .sh`, so it
cannot see the shell seam. The seam was read directly instead, and this unit extends it:
`read_landing_commit` in `tools/unattended/lib-unattended.sh`, plus `check_adv_reaches` and
`ADV_HEAD_OK` in `tools/unattended/check-unattended.sh`, the same three check 7 and check 19 use.
The recall probe returned the derived-terminal unit TOOL-dDerivedDocket-22, which introduced
derived LANDED and wired it into check 7, check 15's fact-set arm and check 19's grant arm but not
check 23; the driver's `read_derived_phase`; and this unit's own brief and parked rescope entry.
None of them records a reason for leaving check 23 out.

Recall terms used: check 23 undeclared-write ceiling derived LANDED landing commit advertised tip in-place LANDING record exclusion shrink-only

The question passed with them: "why does check 23 keep grading run records that landed in place".

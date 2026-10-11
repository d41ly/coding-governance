**Serves:** diff-review TOOL-aQuotedBrief-1 TOOL-aQuotedBrief-2 TOOL-aQuotedBrief-3

# Tier-2 closing diff review — aQuotedBrief, ROUND 1

*The closing review of build aQuotedBrief, over the cumulative diff landing on `main` at the
integration boundary. The build makes a prompt record stand on its own (unit 1), refuses a carried
branch at a first preflight (unit 2), and makes every brief item carry a disposition that
build-complete grades as term 7 (unit 3). Five finder lenses, a skeptic per batch, one synthesis
pass. Node `a`, 2026-10-09.*

Reviewed range: `6473ae38a517a3559f2b7daed67a9820c505bd4d...cc627830097f2e88cab5e196fc301fbf1d6f1a40` · ROUND 1

## Verdict: BLOCKED

One blocker survived the skeptic: `check_prompt_brief` refuses a conforming prompt record whenever
the last record under `prompts/` is a spec or build brief, which is the layout every prompt-mode
build in this corpus already has (B1). Three highs follow. Two of them (H1, H2) are the same class:
term 7 can go green without grading a single brief item. The third (H3) is the blocker's defect
filed by a second lens at a lower binding grade. The mediums and lows are contained.

## Review shape

Intensity full. Raw 21, confirmed 18, refuted 3, unverified 0 (0 uncertain). Precision 0.86.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 4 | 3 | 1 | 0 | 0 | 0.75 |
| correctness | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| seams | yes | 5 | 4 | 1 | 0 | 0 | 0.80 |
| verification | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |

- Adjudicated tally by raw confirmed finding: BLOCKER 1 (id 5), HIGH 3 (ids 6, 7, 9), MEDIUM 9
  (ids 2, 8, 10, 11, 12, 14, 15, 18, 19), LOW 5 (ids 3, 4, 16, 17, 21).
- Adjudicated tally by item: BLOCKER 1 (B1), HIGH 3 (H1 to H3), MEDIUM 6 (M1 to M6), LOW 4 (L1 to L4).
  Merges were made only within one binding grade: ids 2, 11 and 18 into M1, and ids 14 and 15 into
  M5 at medium; ids 16 and 17 into L4 at low.

### Run integrity

- Lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 12 judged sound, 6 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
  Every UNSOUND fix below is replaced by the skeptic's corrected fix; the finder's rejected proposal
  is not repeated.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 6 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: 4 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 30 items, each assigned to exactly one of 5 lenses (security 6, correctness 6, seams 6,
  verification 6, intent 6).
- By design: none supplied, with no caller byDesign and no block.

No lens or skeptic died, so the finding set is complete for this round's shape.

## BLOCKER

### B1 — `check_prompt_brief` refuses a conforming record when a non-prompt record sorts last (id 5)

- **Where:** [tools/unattended/unattended.sh:3206](../../../../tools/unattended/unattended.sh)
- **Defect:** the per-record awk verdict and the join result share one variable, `why`. A record
  with no `## The prompt` sets `why=skip`, and `[ "$why" = skip ] && continue` leaves it set. When
  that record is the last one `git ls-tree` lists, the loop ends with `why=skip` and `found=1`. Join
  rule 3 is then skipped by `[ -z "$why" ]`, and fail 115 fires with the reason `skip`.
- **Reachable on the common path:** prompt-mode builds keep `<date>-prompt-<ID>-1-0-run-mandate.md`
  beside `-1-1-spec-brief.md` and `-N-M-build-brief.md` records that sort after it (aDeferredBar,
  aEvidencedLens and others). Prompt mode resolves BASE at the pushed run tip, and the check runs on
  every preflight (:6782, not gated on `_pf_first`). The protocol directs a re-preflight after
  compaction. So the first pushed brief record makes every later preflight refuse a valid record,
  and check 115 has no override. Every suite arm writes a single record, so none catches it.
- **Fix (judged SOUND by the skeptic):** keep the per-record verdict apart from the join result, for
  example `res=$(... awk ...); [ "$res" = skip ] && continue; found=1; if [ -n "$res" ]; then fail 112
  "... $res $rec"; return 1; fi`, so `why` holds only join output. Also run `check_prompt_brief` only
  on a first preflight (gate on `_pf_first`, as `check_branch_carried` is), or against the recorded
  base, so a later preflight does not re-grade the brief at a moved BASE. Add an arm with a second
  record that carries no `## The prompt` and sorts after the mandate.
- **Left-shift gate:** a suite arm with a conforming mandate plus a `...-1-1-build-brief.md` record
  that asserts `preflight OK`. Recurring class for §10: a sentinel value sharing a variable with a
  result, surviving a `continue`.

## HIGH

### H1 — term 7 reads `PROMPT_BRIEF_CUTOFF` from the working copy at close, and is silent when it is off (id 6)

- **Where:** [tools/unattended/unattended.sh:3115](../../../../tools/unattended/unattended.sh)
- **Defect:** `check_brief_items` pins mode, record and README `opened:` to BASE but gates on
  `${PROMPT_BRIEF_CUTOFF:-}` from the conf sourced at `--close`. A blank or malformed value returns 0
  with no output. Runs do commit edits to `.unattended.conf` (this build did, in c3d7761af), and
  `scan_grant_writes` watches only `SPEC_AUDIT_DEFAULT` in that file. A run that blanks the cutoff,
  or moves it past `opened:`, after preflight closes green with no brief item graded. The kit
  already reads `LANDING_NODES` and `SPEC_AUDIT_DEFAULT` at BASE for this exact reason. Class:
  decision-re-derived-by-a-second-process.
- **Fix (judged SOUND by the skeptic):** read `PROMPT_BRIEF_CUTOFF` in `check_brief_items` from the
  conf blob at the default-branch side of the pinned BASE, using the eval-with-sentinel reader
  `resolve_landing_at` uses. Alternatively, have preflight record a run-state fact when
  `check_prompt_brief` graded the run, and key term 7 on that fact. Announce the blank-cutoff case
  the same way preflight does.
- **Open point for the fix:** the three medium duplicates in M1 disagree on the announcement. Id 2's
  corrected fix announces through a `BRIEF_NOTE` the caller appends to `DOD_OUT`; id 11's corrected
  fix adds no announcement, citing spec S3 ("meets the term and says nothing"). Pinning the read to
  BASE is common to all four. Whether a blank cutoff is announced at close is a spec question to
  settle in the unit that takes this fix.
- **Left-shift gate:** the close arm from id 18: over the AC4 fixture, commit `PROMPT_BRIEF_CUTOFF=""`
  after preflight and still expect the term-7 refusal.

### H2 — preflight and term 7 disagree on what a prompt record is (id 7)

- **Where:** [tools/unattended/unattended.sh:3125](../../../../tools/unattended/unattended.sh)
- **Defect:** preflight's awk normalises headings with `sub(/^## +/)`, so `##  The prompt` (two
  spaces) is graded and joined. Term 7 gates with `grep -qE '^## The prompt[[:space:]]*\r?$'`, which
  needs exactly one space, so it skips that record and meets term 7 green with no item graded.
  `read_brief_items` is a third copy that splits headings the way preflight does. The skeptic raised
  this from medium to high because the consequence is a DoD term certifying what it did not check.
- **Fix (judged SOUND by the skeptic):** use one predicate in both places. Either have term 7 run the
  same awk heading normalisation as `check_prompt_brief`, or extract a shared `is_prompt_record`
  helper used by `check_prompt_brief`, `check_brief_items` and `read_audit_ask_record`.
- **Left-shift gate:** an arm with a `##  The prompt` record carrying an unmet `planned` item that
  expects the term-7 refusal at close. Recurring class: two answers to one question.

### H3 — the `why=skip` sentinel survives the loop, seen from the seams lens (id 9)

- **Where:** [tools/unattended/unattended.sh:3206](../../../../tools/unattended/unattended.sh)
- **Defect:** the same defect as B1, found independently by the seams lens: build briefs named
  `-N-M-build-brief.md` carry no `##` headings at all (checked on aEvidencedLens) and sort after the
  mandate, so a re-preflight or a rotation refuses with check 115 and the reason `skip`.
- **Grade note:** the binding grade is high, so this stays a separate item. On the rubric I would
  grade it blocker, since it is the same reachable refusal as id 5; it is closed by B1's fix and owes
  no separate unit.
- **Fix (judged SOUND by the skeptic):** clear the sentinel before continuing, for example
  `[ "$why" = skip ] && { why=""; continue; }`, or keep the awk verdict in its own variable. Add an
  arm with a conforming mandate plus a `...-1-1-build-brief.md` record (no `## The prompt`) that
  asserts `preflight OK`.
- **Left-shift gate:** the arm named in B1 covers both.

## MEDIUM

### M1 — the unpinned cutoff read, from three lenses (ids 2, 11, 18)

- **Where:** [tools/unattended/unattended.sh:3115](../../../../tools/unattended/unattended.sh)
- **Defect:** the same defect as H1, filed by the security (id 2), seams (id 11) and verification
  (id 18) lenses at a binding grade of medium. Id 2 adds that `check_prompt_brief` has the same
  unpinned read at preflight. Id 11 adds the reverse case: a run admitted under a blank key, then
  closed after the key is declared, is graded on dispositions preflight never checked. Id 18 adds
  that no arm pins either reading. Two caveats from id 11's skeptic: the silence follows spec S3, and
  `SPEC_THIN_CUTOFF` and `UNITS_REGION_CUTOFF` are read from the working copy the same way.
- **Grade note:** these are H1's defect. I would grade them high with H1; the binding grade keeps
  them here, and H1's fix closes them.
- **Fix, id 2 (REJECTED by the skeptic; corrected fix):** pin the read to BASE:
  `cut=$(read_conf_value <(GIT show "$base:$CONF_REL") PROMPT_BRIEF_CUTOFF)` (`CONF_REL` = the conf
  path relative to the repo root). When the value is off, have `check_brief_items` set a variable
  (for example `BRIEF_NOTE`) instead of writing `DOD_OUT`, and have the build-complete caller append
  it to `DOD_OUT` after its own assignment on both met paths, at :10786 and :10820.
- **Fix, id 11 (REJECTED by the skeptic; corrected fix):** in `check_brief_items`, read
  `PROMPT_BRIEF_CUTOFF` from the `.unattended.conf` blob at the recorded base, the way
  `resolve_landing_at` and the `SPEC_AUDIT_DEFAULT` read do (eval the blob in a subshell). Grade on
  that value and add no `DOD_OUT` announcement.
- **Fix, id 18 (judged SOUND by the skeptic):** read `PROMPT_BRIEF_CUTOFF` in `check_brief_items`
  from the conf blob at `$base`, using the evaluated-subshell idiom `check_authorization` uses for
  `SPEC_AUDIT_DEFAULT`. Add a close arm whose run commits `PROMPT_BRIEF_CUTOFF=""` after preflight
  over the AC4 fixture and still expects the term-7 refusal.
- **Left-shift gate:** id 18's close arm, as in H1.

### M2 — a bare `[stale]` or `[parked]` counts as a disposition (id 8)

- **Where:** [tools/unattended/unattended.sh:3097](../../../../tools/unattended/unattended.sh)
- **Defect:** `read_brief_items` accepts `k == "stale" || k == "parked" || a != ""`, so `[stale]` with
  no evidence and `[parked]` with no reason pass join rule 1 and are met at close. Spec 3 §4 and
  VERBS.template.md:575 define `[stale <evidence>]` and `[parked <reason>]`.
- **Fix (judged SOUND by the skeptic):** require non-empty args for all four kinds:
  `if (k ~ /^(planned|stale|duplicate|parked)$/ && a != "")`. Add an arm showing `[stale]` refused at
  check 115 rule 1.
- **Left-shift gate:** that arm.

### M3 — `check_prompt_brief` re-grades the join at every preflight against a moved BASE (id 10)

- **Where:** [tools/unattended/unattended.sh:6782](../../../../tools/unattended/unattended.sh)
- **Defect:** `verb_preflight` calls `check_prompt_brief "$slug" "${base:-}"` on every preflight, with
  the freshly derived TB. Runs grow their roster mid-run (aEvidencedLens went from 14 to 19 units),
  and a late unit has no `planned` item because dispositions are frozen at BASE. Rule 3 then refuses
  a run its first preflight admitted, the outcome the function's header says it avoids at `--close`.
- **Fix (judged SOUND by the skeptic):** grade only at a first preflight
  (`[ -z "$_pf_first" ] || check_prompt_brief ...`, the same gate as `check_branch_carried`), or pass
  the recorded `base` fact when RUN.md already exists.
- **Left-shift gate:** a re-preflight arm over a run that added a roster unit after its first
  preflight, asserting `preflight OK`.

### M4 — `### Items` lines that are not `<n>.` are invisible to the join and to term 7 (id 12)

- **Where:** [tools/unattended/unattended.sh:3091](../../../../tools/unattended/unattended.sh)
- **Defect:** `read_brief_items` emits only lines matching `^[0-9]+\.`, and rule 2 needs only one
  numbered line. `1. The unit. [planned X]` followed by `- The docs.` passes preflight, and the bullet
  item never needs a disposition, a CLOSED unit or a park. No record in the repo carries `### Items`
  today, so the fix breaks nothing that exists.
- **Fix (judged SOUND by the skeptic):** in `read_brief_items`, emit every non-blank line under
  `### Items`, giving non-numbered lines a sentinel number and kind `none`, so join rule 1 refuses
  them by line. Or have `check_prompt_brief`'s structural awk refuse any non-blank Items line that
  does not open `<n>.`.
- **Left-shift gate:** an arm with a numbered item plus a bullet item, expecting check 115 rule 1.

### M5 — two term-7 paths the suite cannot see (ids 14, 15)

- **Where:** [tools/unattended/unattended.sh:10819](../../../../tools/unattended/unattended.sh) and
  [tools/unattended/unattended.test.sh:4435](../../../../tools/unattended/unattended.test.sh)
- **Defect, id 14:** every term-7 close arm builds its conf with a bare `mkconf`, so
  `SPEC_THIN_CUTOFF` is blank and term 7 runs only through the call at :10785. This repo's conf
  declares `SPEC_THIN_CUTOFF="2026-08-31"`, so production always takes :10819, which no arm reaches.
  Deleting :10819 leaves the suite green. The skeptic graded it medium from high, since the
  production code is correct today.
- **Defect, id 15:** the slug-mode half of AC7 passes over an empty `prompts/` loop, because `bcopen`
  resets to a BASE with no prompt record. It passes whether or not the `fact mode = prompt` guard at
  :3113 exists.
- **Fix, id 14 (REJECTED by the skeptic; corrected fix):** in `build_brief_run` use
  `mkconf true true 2026-08-19 3600 2026-07-01` (the form the THIN arms use at :8834), or append
  `SPEC_THIN_CUTOFF="2026-07-01"` to `.unattended.conf` next to the `PROMPT_BRIEF_CUTOFF` line and
  commit both. Run AC4 and the WONTDO-successor arm of AC5 under it and assert the term-7 message.
  The fixture spec `spec/one.md` has no date in its filename, so term 6 logs a skip and stays met.
- **Fix, id 15 (REJECTED by the skeptic; corrected fix):** do not write the record before `bcopen`,
  because `bcreset` runs `git reset --hard $BCP; git clean -qfd` and wipes it. Instead: `bcreset`;
  `write_brief_record tRun '1. The unit. [planned ARCH-tRun-1]'`; commit it so it is at the BASE the
  preflight pins. Then run the rest of `bcopen` inline (`run --preflight tRun --keepalive-id KA-1234`,
  `add_facts`, the CONVERGED review line), set WONTDO and `PROMPT_BRIEF_CUTOFF=2026-07-01`, and assert
  `close OK`. Confirm the arm goes red with :3113 removed.
- **Left-shift gate:** both arms, each observed red with the guarded line removed (§7: a gate is not
  landed until its failing case has been observed).

### M6 — `PROMPT_BRIEF_CUTOFF="2026-10-09"` strands prompt-mode runs already in flight (id 19)

- **Where:** [.unattended.conf:493](../../../../.unattended.conf)
- **Defect:** the cutoff equals the `opened:` date of runs in flight. aLevelledCopy
  (origin/branch/friendly-napier-49e2c6, mode prompt, opened 2026-10-09, phase REVIEWING) has no
  `## The prompt` heading in its only record. Once it merges main, a re-preflight (after compaction,
  or after `--abort`) gets fail 113 with no override. aHomedAnchor's `## The prompt, verbatim` hits
  the same refusal. The conf comment covers landed builds only. The skeptic graded it medium from
  high: the run can recover through park or handoff, and term 7 at close is unaffected.
- **Fix (REJECTED by the skeptic; corrected fix):** set `PROMPT_BRIEF_CUTOFF` to a date after every
  prompt-mode run in flight (for example `"2026-10-10"`), and correct the conf comment to cover runs
  in flight as well as landed builds. Leave `check_prompt_brief` on every preflight.
- **Note:** this corrected fix and M3's sound fix pull in opposite directions on the `_pf_first` gate.
  The cutoff move is needed either way; whether the check stays on every preflight is decided with
  B1 and M3.
- **Left-shift gate:** a documented §10 check rather than a gate: a cutoff date is set after the
  `opened:` of every live prompt-mode row in `memory/LIVE.md`.

## LOW

### L1 — non-ASCII record names are C-quoted and skipped ungraded (id 3)

- **Where:** [tools/unattended/unattended.sh:3231](../../../../tools/unattended/unattended.sh) (and :3150)
- **Defect:** both new listings call `GIT ls-tree --name-only` without `-z` or `core.quotepath=off`.
  Git C-quotes a non-ASCII name, `GIT show base:<quoted>` fails, and the record reads as empty and is
  skipped. `check_branch_carried` in the same diff does pass `-c core.quotepath=off`. The skeptic
  graded it low from medium: the naming convention uses ASCII ids.
- **Fix (judged SOUND by the skeptic):** list with `GIT ls-tree -z --name-only --full-tree` and read
  with `read -r -d ''`, or add `-c core.quotepath=off`. Also refuse, rather than skip, a listed record
  whose `GIT show` fails.
- **Left-shift gate:** a scan over `tools/` for `ls-tree --name-only` with neither `-z` nor
  `core.quotepath=off`, gating the class rather than these two call sites.

### L2 — a park reason can satisfy a brief item it does not name (id 4)

- **Where:** [tools/unattended/unattended.sh:3128](../../../../tools/unattended/unattended.sh)
- **Defect:** term 7 matches ` · item brief item $n:` anywhere in RUN.md. `verb_park` refuses ` · `
  only in the item, so a reason containing ` · item brief item 3:` meets item 3.
- **Fix (judged SOUND by the skeptic):** anchor the match to the parked-line shape, for example
  `grep -qE "^[0-9][0-9-]*T[0-9:]*Z [a-z]+ · item brief item $n:" "$rm"`.
- **Left-shift gate:** an arm parking a different item with that reason, expecting the term-7 refusal.

### L3 — the protocol row overstates term 7 for `stale` and `duplicate` items (id 21)

- **Where:** [tools/unattended/PROTOCOL.template.md:348](../../../../tools/unattended/PROTOCOL.template.md)
- **Defect:** the build-complete row says each brief item is built by CLOSED units or parked. Spec 3
  meets `stale` and `duplicate` items at BASE. The checker follows the spec; only the documentation is
  wrong.
- **Fix (REJECTED by the skeptic; corrected fix):** reword the clause to: "Past
  `PROMPT_BRIEF_CUTOFF`, each `planned` brief item of a prompt run is built by CLOSED units or parked
  as `brief item <n>:`, each `parked` item is parked so, and `stale` and `duplicate` items are met at
  BASE." Then trim an equal amount elsewhere if a size budget applies, and re-render
  `memory/guides/UNATTENDED-PROTOCOL.md` from the template.
- **Left-shift gate:** none fits; a §10 check that a DoD row naming a term is read against the term's
  spec section.

### L4 — rule and disposition branches with no arm (ids 16, 17)

- **Where:** [tools/unattended/unattended.sh:3201](../../../../tools/unattended/unattended.sh) and :3098
- **Defect, id 16:** structural rules 2, 3 and 4, and the order and non-empty halves of rule 1, have
  no arm; the rule number is interpolated into one fail-112 message, so the arms pin text, not
  predicates. Spec 1's ACs require arms only for rules 1 and 5.
- **Defect, id 17:** the "two dispositions" (`many`) half of join rule 1 is never triggered.
- **Fix, id 16 (judged SOUND by the skeptic):** add one record variant per rule to the
  TOOL-aQuotedBrief-1 block: Items holding only prose (rule 2), no Drawn section (rule 3), no Owner
  confirmation section (rule 4), and a brief with Acceptance before Items or an empty Gates (rule 1).
  Assert each `first rule failed, then the record: rule N $_qb_rec`.
- **Fix, id 17 (judged SOUND by the skeptic):** add an arm to the `for _bq_arm` loop with
  `1. The unit. [planned ARCH-tBr-1] [stale it is built]` and assert
  `$_bq_why $_qb_rec rule 1, not exactly one disposition among planned, stale, duplicate and parked: item 1`.
- **Left-shift gate:** the arms themselves.

## Refuted

Ids 1, 13 and 20 were refuted by their skeptics; the reasons are in the appendix.

review-shape kind=diff-review round=1 intensity=full at=synth raw=21 confirmed=18 refuted=3 unverified=0 blocker=1 high=3 medium=9 low=5 agents=11 out-tokens=174807

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/unattended.sh:3275 | medium | - | refuted | The mechanics are as described. GENERATED_INDEXES is resolved at conf load from the working tree's .unattended.conf and its tracked kit.toml files (resolve_generated_indexes, lib-unattended.sh:730). covers() is one-way, and scan_shared_index_overlaps only compares the indexes against SHARED_RECORDS. But spec TOOL-aQuotedBrief-2 lists 'A security boundary' as a non-goal (line 55). The function header says it is 'A guard against accident, not a security boundary' and that 'a run with shell access can rewrite its branch'. A carried commit that deliberately rewrites GENERATED_INDEXES so it covers itself and tools/ is an act of evasion, the same class as rewriting the branch, not an accident. An accidental carried commit that touches .unattended.conf or a kit.toml without such a self-covering widening is still refused, because neither file is under a declared index. Within the check's declared scope this is not a defect. | sound | containment-tested-one-way |
| 2 | security | tools/unattended/unattended.sh:3115 | medium | medium | confirmed | PROMPT_BRIEF_CUTOFF is loaded from the working-copy conf at HEAD. check_brief_items (unattended.sh:3115) returns 0 with no output when the value is blank or malformed, while mode, record and opened: are read at the pinned BASE. Its sibling term 6 says when it is off ('note - the project declares no SPEC_THIN_CUTOFF', :10787), and check_prompt_brief prints a NOTE at preflight. Term 7 gives no notice. A conf edit after preflight therefore turns term 7 off and build-complete still passes. The path is narrow and the effect is contained to one term. | unsound | - |
| 3 | security | tools/unattended/unattended.sh:3231 | medium | low | confirmed | The GIT wrapper (lib-unattended.sh:61) adds no core.quotepath setting, and both new listings at :3150 and :3231 call ls-tree --name-only without -z. Git C-quotes a non-ASCII name, so GIT show base:<quoted> fails. txt is then empty, the awk prints 'skip', and the record is skipped without being graded. check_brief_items has the same skip. The new check_branch_carried does pass -c core.quotepath=off, so the new code is inconsistent with itself. The same idiom exists at the base (read_audit_ask_record), but these two call sites are new in this diff. Reaching the hole needs a non-ASCII record name next to a conforming record, and the naming convention uses ASCII IDs, so the path is narrow. | sound | - |
| 4 | security | tools/unattended/unattended.sh:3128 | low | low | confirmed | check_brief_items at :3128 uses grep -qF ' · item brief item $n:' against the whole of RUN.md. verb_park (:11946) refuses ' · ' only in the item; the reason is free, and park() writes '<ts> <kind> · item <item> · reason <reason>'. A reason containing ' · item brief item 3:' therefore satisfies item 3 although no parked line's item opens 'brief item 3:'. Spec 3 lines 108-109 require the item to open that way. The path is deliberate or very unlikely. | sound | - |
| 5 | correctness | tools/unattended/unattended.sh:3206 | blocker | blocker | confirmed | In check_prompt_brief the per-record awk result goes into why. For a record with no '## The prompt' that result is 'skip', and the loop continues with why still set to 'skip'. If the last record listed is such a record, why='skip' after the loop. Rule 3 is then skipped by `if [ -z "$why" ]`, and `[ -z "$why" ] && return 0` falls through to fail 115 '...: skip'. Existing builds show the layout that triggers this: aDeferredBar, aEvidencedLens and others hold <date>-prompt-<ID>-1-0-run-mandate.md (the only record with '## The prompt') followed by -1-1-spec-brief / -N-M-build-brief records, which sort after it. Prompt mode resolves BASE at the second anchor, the pushed run tip (fail 50/89 comments; RB_BASE=$BSHA). check_prompt_brief runs on every preflight (:6782, not gated on _pf_first). PROTOCOL.template.md:614 documents a re-preflight after compaction. So the first pushed brief record makes every later preflight refuse a valid record, with no override. | sound | - |
| 6 | correctness | tools/unattended/unattended.sh:3115 | high | high | confirmed | check_brief_items (new in this diff) gates on ${PROMPT_BRIEF_CUTOFF:-} from the sourced working-copy conf at --close, and returns 0 with no output when the value is blank or malformed. check_prompt_brief announces that same case. Nothing guards an edit to this key: the leg's scan_grant_writes only watches SPEC_AUDIT_DEFAULT in .unattended.conf. So a run that blanks the cutoff, or moves it past `opened:`, after preflight gets term 7 met without any item being graded. The kit already reads LANDING_NODES and SPEC_AUDIT_DEFAULT at BASE for this exact reason. Term 6 reading SPEC_THIN_CUTOFF from the working copy is precedent for cutoffs, but term 6 announces its blank case and term 7 does not. The path needs a run-side conf edit, so it is narrow, but the consequence is a DoD term certifying items it never graded. | sound | decision-re-derived-by-a-second-process |
| 7 | correctness | tools/unattended/unattended.sh:3125 | medium | high | confirmed | In check_prompt_brief, the awk normalises headings with sub(/^## +/), so a record headed `##  The prompt` sets seen["The prompt"], counts as found=1, and is graded and joined. check_brief_items gates with grep -qE '^## The prompt[[:space:]]*\r?$', which needs exactly one space, so it skips that record and term 7 grades none of its items. Both functions are new in this diff, and no lint elsewhere normalises prompt-record headings. The trigger is a narrow malformed heading, but the consequence is term 7 going green without grading. | sound | - |
| 8 | correctness | tools/unattended/unattended.sh:3097 | medium | medium | confirmed | read_brief_items accepts kind stale/parked with a='' through `(k == "stale" \|\| k == "parked" \|\| a != "")`. Spec 3 §4 and VERBS.template.md:575 both define the grammar as `[stale <evidence>]` and `[parked <reason>]`. A bare `[stale]` therefore passes preflight rule 1 and is met at close, with no evidence in the authorized record. The test arms only use forms that carry evidence. The effect is contained: the owner still reads the record, and the spec does not grade whether a stale disposition is true. | sound | - |
| 9 | seams | tools/unattended/unattended.sh:3206 | high | high | confirmed | In the loop, `[ "$why" = skip ] && continue` leaves why=skip in place. If the last record ls-tree lists has no `## The prompt`, the loop ends with why=skip and found=1. `[ -z "$why" ]` then skips the rule-3 join and fail 115 fires with reason 'skip'. This is reachable: build briefs named `-N-M-build-brief.md` have no ## headings at all (checked aEvidencedLens), and they sort after `-1-0-run-mandate.md`. Prompt mode resolves at the run-branch anchor, so a re-preflight after compaction, or a rotation, derives TB from the pushed tip, which carries those briefs. The result is a refusal with a nonsense message on a common path. | sound | - |
| 10 | seams | tools/unattended/unattended.sh:6782 | medium | medium | confirmed | verb_preflight calls check_prompt_brief "$slug" "${base:-}" on every preflight. base is the freshly derived TB, and trusted_base keeps the recorded base as evidence only. Runs do grow the authored roster mid-run: aEvidencedLens went from 14 to 19 roster units across its README history. So on a re-preflight (which the protocol directs after compaction), rule 3 finds new roster units that no planned item names and refuses with 115. That strands a run its first preflight admitted, which is the outcome the function's own header says it avoids at --close. The consequence is an over-refusal, contained to that run. | sound | - |
| 11 | seams | tools/unattended/unattended.sh:3115 | medium | medium | confirmed | Confirmed. check_brief_items (unattended.sh:3115) reads PROMPT_BRIEF_CUTOFF from the working-copy conf, which is sourced at line 545 from $ROOT/.unattended.conf. Nothing pins it to BASE, and preflight records no fact saying it graded the brief. A run that blanks or moves the key in its own tree switches term 7 off when it closes. The kit already guards against exactly this for LANDING_NODES (comment at :539: 'a run that added its own node to the working copy would grant itself a landing'), and term 7 is a new check this diff added with the same exposure. Two caveats keep this at medium. The silence itself follows the spec: S3 says every other run 'meets the term and says nothing'. And the existing cutoffs (SPEC_THIN_CUTOFF, UNITS_REGION_CUTOFF) are read from the working copy the same way, so the hole is contained and in keeping with the kit's handling of cutoffs. | unsound | - |
| 12 | seams | tools/unattended/unattended.sh:3091 | medium | medium | confirmed | Confirmed. read_brief_items (unattended.sh:3093) skips every `### Items` line that does not match `^[0-9]+\.`. check_prompt_brief's structural awk sets `items = 1` as soon as one numbered line exists, so rule 2 only needs one. A record with `1. X [planned ARCH-..-1]` followed by `- The docs.` therefore passes rules 1-5 and the join, and term 7 never sees the bullet item. Spec S1 says each `### Items` line is one item ending in a disposition, and join rule 1 says every item line carries one, so the bullet is an item that goes ungraded. The run writes this record itself, so the path is reachable. No record in the repo today carries `### Items`, so the fix breaks nothing that exists. | sound | - |
| 13 | seams | tools/unattended/unattended.sh:3186 | low | - | refuted | This matches the spec. Spec 3 section 4, 'The preflight join', says it is read 'from the prompt record and the README's authored roster pair'. Rule 2 says 'a unit row of the authored roster', and S2 says 'a unit of the README's authored roster at BASE'. Leaving out the unit-ask half is what the spec asks for, not drift from it. roster_ids also reads the working copy rather than BASE, so it is not a drop-in for a join pinned at BASE. The finder graded it low, and the claimed disagreement is a spec choice rather than a defect. | unsound | - |
| 14 | verification | tools/unattended/unattended.sh:10819 | high | medium | confirmed | Confirmed. build_brief_run calls mkconf with no arguments (unattended.test.sh:4396), and mkconf writes SPEC_THIN_CUTOFF="${5-}", which comes out empty. Every term-7 close arm (the green control, AC4, the park arm, AC5 with both successors, the AC7 halves) therefore reaches term 7 only through the blank-cutoff call at unattended.sh:10785. This repo's .unattended.conf:310 declares SPEC_THIN_CUTOFF="2026-08-31", so a real close always goes through the call at :10819, which no arm exercises. The THIN arms at 8834-8847 do declare the cutoff, but they run slug mode under PROMPT_BRIEF_CUTOFF=2099, where term 7 returns 0 at once. Deleting :10819 would leave the suite green. Graded medium rather than high: the production code is correct today, so the effect is a missing regression guard and no wrong result ships. | unsound | - |
| 15 | verification | tools/unattended/unattended.test.sh:4435 | medium | medium | confirmed | Confirmed. The slug-mode half of AC7 calls bcopen, and bcreset hard-resets it to BCP. bcsetup set BCP before the bq-fixture commit, so the BASE has a slug-mode README and no prompts/ folder. Without the `fact mode = prompt` guard at :3113, check_brief_items would still return 0: the cutoff is valid, ls-tree of prompts/ at base is empty, and unmet stays empty. So the arm passes whether or not the guard exists, and AC7's 'red when term 7 grades a run it does not cover' is never put under test. | unsound | - |
| 16 | verification | tools/unattended/unattended.sh:3201 | medium | low | confirmed | Confirmed. In unattended.test.sh lines 4224-4290, the TOOL-aQuotedBrief-1 block has arms for rule 1 (a bare record with no brief), rule 5 (_qb_unasked), the conforming pass, the blank and grandfathered cutoff, and the absent record (113). No record has Items holding only prose, a missing Drawn section, a missing Owner confirmation section, out-of-order sub-heads or an empty sub-head. Rule N is interpolated into the one fail-112 message, so the existing positive assertions pin the text and not the predicates. Spec 1's ACs only require arms for rules 1 and 5, so the suite matches its spec. The gap affects test coverage only: the awk predicate at unattended.sh:3201-3207 reads correctly today. That makes it low. | sound | - |
| 17 | verification | tools/unattended/unattended.sh:3098 | medium | low | confirmed | Confirmed. The check-115 loop (test.sh:4359-4386) runs arms 1, 2, 3, 4 and ok. Arm 1 is `2. The docs.` with no bracket, which gives kind `none`. No arm puts two disposition groups on one line, so the `many` branch in read_brief_items (unattended.sh:3098, `rest ~ /\[(planned\|stale\|duplicate\|parked)( [^][]*)?\]$/`) is never exercised. A regression there would read `[planned X] [stale y]` as stale, and both preflight and term 7 would then pass it. The current code handles that line correctly, so this is a coverage gap with no effect on behaviour. | sound | - |
| 18 | verification | tools/unattended/unattended.sh:3115 | medium | medium | confirmed | Confirmed. check_brief_items (unattended.sh:3115) gates on the `${PROMPT_BRIEF_CUTOFF:-}` that `. "$CONF"` (line ~547) binds from the working copy when --close runs. It is not read from the conf blob at $base, although the README `opened:` and the record are both read at $base. The kit's own comment at lines 506-508 and 538-541 says SPEC_AUDIT_DEFAULT and LANDING_NODES are re-read at the pinned BASE because a run could blank its working copy to opt out. This key does not follow that precedent. A run that commits `PROMPT_BRIEF_CUTOFF=""` after preflight makes term 7 return 0 silently (no announcement on this path), and an unbuilt brief item then closes green. No arm covers it. It needs the run to edit the tracked conf, so the effect is contained: medium. | sound | two-answers-to-one-question |
| 19 | intent | .unattended.conf:493 | high | medium | confirmed | Confirmed. The diff sets PROMPT_BRIEF_CUTOFF="2026-10-09" in .unattended.conf, and origin/main is still at the diff's base (6473ae38), so this has not landed yet. check_prompt_brief is called at unattended.sh:6782 on every preflight, with no _pf_first guard (compare check_branch_carried on the next line). aLevelledCopy on origin/branch/friendly-napier-49e2c6 is in flight: mode prompt, opened 2026-10-09, phase REVIEWING. Its only prompt record at BASE ce9192c0 carries no `## The prompt` heading, only `## The clarification...` and `## How this run read it`. Once that branch merges main, a re-preflight (the verbs guide names one 'after a compaction' to re-issue waivers, and another after --abort) gets fail 113, and preflight takes no override. term 7 at close is unaffected: with no `## The prompt` record it grades nothing and returns 0. The conf comment covers landed builds only. The consequence is a stranded run that can recover through park or handoff, not a wrong result, so medium rather than high. | unsound | a-merged-in-check-can-refuse-a-pinned-record |
| 20 | intent | tools/unattended/unattended.sh:3129 | medium | - | refuted | The key collision is real in the code: term 7 matches ` · item brief item $n:` without naming a record, and both functions loop over every `## The prompt` record. But no path the kit documents produces two such records in one build. The prompt path (UNATTENDED-VERBS.md step 3) writes one record when it creates the build folder. A later run of an existing prompt-mode build preflights that folder rather than re-entering the prompt path. Other records under prompts/ (spec and build briefs) carry no `## The prompt` and are skipped. No build in memory/builds/ has more than one such record. The failure needs a hand-written second record whose items also join the same roster under rules 2 and 3. That state is outside the design, and the finder graded it medium, so: refuted. | sound | id-matched-as-a-substring |
| 21 | intent | tools/unattended/PROTOCOL.template.md:348 | low | low | confirmed | This diff added the sentence at tools/unattended/PROTOCOL.template.md:348. The base row says SIX terms and has no brief-item clause, and the rendered memory/guides/UNATTENDED-PROTOCOL.md:348 copies the new text. The sentence says that past PROMPT_BRIEF_CUTOFF each brief item of a prompt run is built by CLOSED units or parked as `brief item <n>:`. Spec 3, Term 7 (lines 104-110) says instead that a `planned` item is met by CLOSED units or a park, a `parked` item is met by a park, and `stale` and `duplicate` items are met at BASE. The protocol row therefore overstates what term 7 asks of stale and duplicate items. The checker follows the spec, so only the documentation is wrong and runtime behaviour is unaffected. That makes it low. | unsound | - |

**Serves:** diff-review TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-36 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 TOOL-dTotalRecall-114
**Caused-by:** TOOL-dTotalRecall-1

# dTotalRecall — Tier-2 CLOSING DIFF review, round 1

*Node `d`, 2026-11-25. dTotalRecall is the Memory build of the dClosedLoop chain, run unattended. This review covers 87 units over the memory-tree kit and its neighbours. The base is origin/main `3d6c1702a`, which the branch reconciled in at `ffa0dcf2d`, so the diff is this build's own changes plus that reconcile's resolutions. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent came from 2 spec documents supplied as `specs`, beside the range's commit messages. The checklist had 152 items, acquired by the harness from `--for-diff 3d6c1702afb6c2e86638785950d80657a187192c..acbb74bb38af4c6b6408cf356ca91fe02d9d3277`, each assigned to exactly one lens: security 31, correctness 31, seams 30, verification 30, intent 30. By design: the caller's byDesign, plus 2 invariants from the checklist's by-design block.* (DERIVED 2026-11-25, the review)

**Range reviewed: `3d6c1702afb6c2e86638785950d80657a187192c...acbb74bb38af4c6b6408cf356ca91fe02d9d3277`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER.
Six items are HIGH and hold eight raw findings.
H1: the change feed re-appends already-fed record events after a merge landing, and its check is falsely red.
H2: `record show` and `budget` return a blob under a key they never verified.
H3: the record door answers `exists` for a record that differs in its unit, title or cause.
H4: the memory re-measure drops a root-wide search, so its median is understated.
H5: the claim root of the orphan walk reads a ref namespace no production writer fills.
H6: the causes leg goes green, reading nothing, once its legacy population drains.
I recommend folding the six HIGHs before the landing, each with an arm seen red first.
The ten MEDIUMs and the LOW can be folded or filed.

## Review shape

Intensity full, raw 20, confirmed 20, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 7 | 7 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 17 items (0 blocker, 6 high, 10 medium, 1 low).
Adjudicated tally by raw confirmed finding: 20 (0 blocker, 8 high, 11 medium, 1 low).
The two tallies differ because findings 4, 8 and 19 are one defect, and findings 2 and 6 are one defect.
Every confirmed finding takes its binding grade.
No finding was refuted, so no twin is flagged.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 15 judged sound, 1 judged UNSOUND (finding 3), 4 judged INSTANCE-ONLY (findings 5, 8, 14, 20), 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing, so those items carry the skeptic's class-level fix.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 5 RE-GRADED by the skeptic (findings 1, 4, 10, 13, 14).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 0. Same-address pairs shown: 0.
- Dispositions: unclassed is `refuse`; 152 class slugs handed; 230 leg names read from tools/gate-legs.json.

Every count that would mark the run incomplete is zero, so this run is complete.

## HIGH

### H1. The change feed resumes from a commit that does not dominate what it already fed, so a merge landing duplicates events and its check goes red (findings 4, 8, 19)

**Where:** `tools/lib/gov-feed.sh@2520b71e:326` (`derive_record_rows`) and `:331`, with `check_feed` at `:384`. The same shared block is carried in `tools/push-main.sh`, `tools/run-gates/post-merge.sh`, `tools/unattended/unattended.sh` and `tools/memory-tree/gov-claim.sh`.

**What is wrong:** `derive_record_rows` takes the newest `record` line's commit as the sole lower bound of `<from>..<tip>`, and the walk is `--no-merges`.
After a merge landing that commit is one side branch's last commit, so `<from>..<tip>` re-lists every commit of the other side.
`write_feed_lines` does no key check.
`check_feed`'s record arm walks to that same newest line's commit, so logged commits outside its ancestry are called `extra`.
`derive_record_rows` documents 'appended once', and spec 24's AC2 names 'a repeated call appends a duplicate key' as its red condition; the header's disclosed blind spot covers only a force-rewritten branch.

**Consequence:** in a scratch repo (p, b on branch b1, m1 on main, then a `--no-ff` merge) `check_feed` printed `extra refs/heads/main <m1>` and exited 1 on a feed holding exactly p, m1 and b.
The next landing appended m1 a second time, after which the check passed on sets.
On this repo the topo-last non-merge memory commit up to `3d6c1702a` is `7ff7bbe5e`, and `7ff7bbe5e..3d6c1702a -- memory/` lists 413 commits already in the feed, so the next landing re-appends them. (DERIVED 2026-11-25, the review)
Every landing here is a merge.
No tracked data is lost, no gate leg found consumes the feed, and no key goes missing, so it is bounded.
The only AC2 arm (the rr_* block of `unattended.test.sh`) builds a linear history and cannot red.
On one sub-claim the notes differ: finding 4 and 8's notes say the check is red after the merge append, and 19's that it stays green. Finding 4's probe shows both, red first and green on sets once the duplicate is appended.

**Grades:** 4 HIGH (finder blocker, re-graded: bounded, as above), 8 HIGH, 19 HIGH.

**Fix:** dedupe in `derive_record_rows` against the (ref, blob, commit) keys already logged, under the lock, or exclude every logged record commit of the ref via `--stdin`.
In `check_feed`'s record arm, derive the expected set from all logged record commits of the ref that a branch or remote-tracking branch reaches (their union as walk tips), not only the newest line's commit, and print duplicate keys.
Re-render every `gov_feed_sh` carrier.
This is the class-level fix the skeptic wrote for finding 8, whose own proposal (dedupe alone, plus a duplicate line in `check_feed`) is INSTANCE-ONLY: it leaves `check_feed` on the non-dominating anchor.
The other two proposals were judged SOUND by the skeptic: finding 4's records the landed tip as a per-ref cursor that both append and check walk from, and finding 19's filters the walked rows by (blob, commit) under the lock. Finding 19's cures the append alone, so the class-level fix is the one to build, with finding 4's cursor as an equal alternative.

**Left-shift gate:** an arm in `unattended.test.sh` with a `--no-ff` merge of a branch forked before the last fed commit, two landings, one line per key and `check_feed` clean after each, seen red on today's builder; plus `check_feed` printing duplicate (ref, blob, commit) keys. Class `append-without-an-idempotence-key`.

### H2. `read_section` with a blob certifies a key it never checks (findings 2, 6)

**Where:** `tools/memory-tree/record_find.py@9274eaf3:478` and `:493` (the blob branch, lines 487-502).

**What is wrong:** for `<key>@<blob>`, when no indexed record row of the key sits at the blob and `extract_record` finds none, `held` falls back to line 1 through the last line.
An unknown key gives empty rows and path `''` and takes the same fallback.
The unknown-key `FindError` exists only in the branch with no blob.
Spec TOOL-dTotalRecall-9 S5 (line 157) says an unknown key exits 2, naming it.

**Consequence:** `read_section('.', 'NO-SUCH-KEY@<blob of HEAD:README.md>')` returned key NO-SUCH-KEY, path `''`, lines 1-121 and the README text.
`gov_record.py show` and `budget` certify the address.
`check_read_set` looks supersession up by the unverified key, so a superseded record's blob addressed under another key passes `memory.superseded-slices=refuse` with no mark, and `handoff.py --read` lists it as a valid read.
`edge_grammar.resolve_edge` reports it resolved.
It needs an explicitly mismatched pinned address, which is narrow.

**Grades:** 2 HIGH, 6 MEDIUM.

**Fix:** with a blob given, raise `FindError` unless the index or the extraction of the blob's text yields a record row of the key.
Drop the `else (1, len(text))` fallback, and resolve the path from the index rows or `git ls-tree` for archived records.
Both findings' fixes were judged SOUND by the skeptic, and they agree.

**Left-shift gate:** fixture plants for an unknown key with a real blob and for a known key with another record's blob, each expecting exit 2, in the `memory-hygiene self-test`. Class `fallback-fabricates-the-passing-value`.

### H3. The record door's `exists` key leaves out most of what the caller supplies (finding 5)

**Where:** `tools/memory-tree/build_records.py@693f05d3:1348` (`write_new_record`, key derived at lines 1330-1346).

**What is wrong:** `derive_content_key` hashes the kind, the stem and the bullet fields only.
The unit on the Serves line, the title, and an untyped record's `Caused-by` (a header line) are outside it.
For `log`, `research`, `design-record`, `spec-audit` and `diff-review`, whose schema fields are `["Serves"]`, the key is kind plus `--name`.
A second call with the same `--name` and another unit, title or cause returns `exists <path>` before the refusal at 1350.
Spec TOOL-dTotalRecall-2's table promises exit 2 for a different value under an existing id.

**Consequence:** a record with different content is dropped while the caller is told it was already written, exit 0.
For typed kinds, two units with identical field values collapse into one record.
It needs a reused name, which makes the path narrow.

**Grades:** 5 HIGH.

**Fix:** compare everything the caller supplies: serving unit, title, header `Caused-by` and the Edges lines, read back through the one edge parser.
Exclude only `Made-by`, the date and the minted `<n>`, including the `<n>` in a typed kind's H1.
The skeptic judged the finder's fix INSTANCE-ONLY: adding unit, title and `Caused-by` to the key would cure the cited instance and leave a call differing only in its edges answering `exists`. The text above is the skeptic's class-level fix.

**Left-shift gate:** one refusal arm per supplied input, `--edge` included, each asserting `refused` and never `exists`. Class `new:content-key-omits-a-supplied-input`.

### H4. The memory re-measure drops a root-wide search (finding 9)

**Where:** `tools/runlog/memory_measure.py@1dcdc842:128` and `:134` (`check_memory_word`).

**What is wrong:** both absolute branches require `<root>/`, and `posixpath.normpath` has already cut a trailing slash.
So `memory`, `memory/` and the absolute `<main>/memory` do not count, and they count only on the branch with no cwd.
The harness records a cwd on every transcript record, and the docstring says a word that is `<root>` alone counts.

**Consequence:** a search of the whole root is the widest memory read and contributes zero bytes: `derive_read_channel` gives None for a Grep of path `memory` and for `rg foo memory/`.
The acceptance median is understated, so `--landed` can print `pass` under the 33,000-byte target over channels it claims to count in full.
The fixture plants only `memory/<file>` words.

**Grades:** 9 HIGH.

**Fix:** in both absolute branches also accept equality: `folded == f"{main}/{root}"`, and `rest == root` for a worktree.
The skeptic judged it SOUND.

**Left-shift gate:** runlog-selftest plants for Grep path=memory and for `rg x memory/` with a recorded cwd. Class `containment-tested-one-way`.

### H5. The claim root of the orphan walk reads a ref no production writer makes (finding 12)

**Where:** `tools/memory-tree/record_causes.py@5c2f60ee:533` (`read_claim_slugs`); the `claim-root` plant is at `:1201`. The writer is `tools/memory-tree/gov-claim.sh@9ab8a922:602`.

**What is wrong:** `read_claim_slugs` lists local `refs/gov/claims/`.
`gov-claim.sh` writes locally only the cache `refs/gov/remote/claims/<slug>`, and `gen_build_index`'s claim cache namespace reads that cache.
The plant passes because it runs `update-ref refs/gov/claims/fClaim` itself.

**Consequence:** the claim-rooted half of the walk selects nothing in a real clone.
A record caused by a unit of a claimed build with no README yet reads as an orphan and reds the leg.
The fixture certifies a state production never reaches.

**Grades:** 12 HIGH.

**Fix:** read the slugs from `refs/gov/remote/claims/`, keeping the local namespace too if a bare remote is ever graded, and mint the `claim-root` plant's claim through `gov-claim.sh slug` against a bare remote.
The skeptic judged it SOUND.

**Left-shift gate:** the plant minted through the CLI, seen red on the current reader; the class rule is that a fixture reaches a state only through the production writer. Class `new:fixture-plants-a-state-no-writer-makes`.

### H6. The causes leg reads nothing and passes once its legacy population is empty (finding 17)

**Where:** `tools/memory-tree/record_causes.py@5c2f60ee:416` (`read_legacy_paths`), consumed by `run_check` at about line 875.

**What is wrong:** an armed `record-kinds-legacy` home whose last causes row for a record is gone returns None.
`run_check` then prints `unarmed` and exits 0 before causes, orphans and the writer census run; the writer census carries the keep-registry homes, which do not use the legacy set at all.
`run_backfill` does the same.
The registration is `shrink-only` with drain by key, so emptying is the direction the ratchet rewards.
`record_kinds.read_legacy_keys` returns a set in the same situation and keeps grading.

**Consequence:** the full drain, or one bulk deletion, turns the whole leg green with nothing read.
The home holds 11408 causes rows today, so the path is narrow.
No plant covers the armed-but-empty home.

**Grades:** 17 HIGH.

**Fix:** return an empty set for a home whose read state is `armed`, so everything is graded, and keep `unarmed` for no registration or an absent or unarmed home.
The skeptic judged it SOUND: every caller is safe with the empty set.

**Left-shift gate:** a plant with an armed home of zero rows beside a causeless record, expecting exit 1. Class `vacuous-selector-empty-population`.

## MEDIUM

### M1. The record door checks a field's value and never its name (finding 1)

**Where:** `tools/memory-tree/build_records.py@693f05d3:1235` (`write_new_record`, and `write_record`).

**What is wrong:** the line-break and forged-field checks run over each field's value.
The caller-supplied name (`gov_record.py new <kind> --field <Name>=<value>`) is only `check_line_break`'s label.
A name holding newlines renders several lines, one of them a column-0 header field such as Commissions.

**Consequence:** one `--field` can plant any header or body line.
`check_header` reads back only made-by and caused-by, and edges only when `--edge` was given; an untyped kind checks only Serves; typed kinds ignore unknown keys.
The door writes and stages the forged binding.

**Grades:** 1 MEDIUM (finder high, re-graded): the caller is a local agent that could edit the file directly, so there is no privilege boundary and the forged line is tracked and diffable.

**Fix:** validate each field key at the write boundary in both functions against the key grammar `[A-Z][a-z-]+(?: [a-z]+)?` by fullmatch, with no duplicates, and refuse otherwise.
The skeptic judged it SOUND.

**Left-shift gate:** an arm passing a `--field` name holding a newline, expecting `refused` and nothing written. Class `invariant-held-on-one-admission-path`.

### M2. Two sessionless processes compare equal as one claim holder (finding 3)

**Where:** `tools/memory-tree/build_records.py@693f05d3:1078` (`read_mint_authority`), with `tools/memory-tree/gov-claim.sh@9ab8a922:951`.

**What is wrong:** the reader compares the claim's session with `CLAUDE_CODE_SESSION_ID or 'absent'`, and `gov-claim.sh` writes the literal `session: absent` when that variable is unset.
A claim with no session line also defaults to `absent`.
The sibling `placement.read_lease_class` requires `me != 'absent'`, so this rung departs from the kit's own rule.

**Consequence:** where no lease is held or no loop kit is installed, a sessionless caller mints records under another claimant's build, stamped owner, with neither the held-by refusal nor the session-rule notice.

**Grades:** 3 MEDIUM.

**Fix (the skeptic's corrected fix; the finder's was REJECTED):** when the claim's holder is a named session, keep refusing any caller whose session differs, an absent caller included.
When the holder is `absent`, or there is no session line, never report a match: continue with an announced line naming the unidentified claim holder (a session-rule mint).
Add arms for both absent, holder named with caller absent, and holder absent with caller named.

**Left-shift gate:** those three arms. Class `fallback-fabricates-the-passing-value`.

### M3. A failed `git add` is reported as `wrote` (finding 7)

**Where:** `tools/memory-tree/build_records.py@693f05d3:1377`, and `tools/memory-tree/gov_record.py@5622bd55:261` and `:272`.

**What is wrong:** the stage runs with `check=False`, its exit is discarded, and the function returns `wrote`, which the exit table defines as written and staged.

**Consequence:** with `index.lock` held by another process, or an ignored path, the record stays untracked and the caller's commit omits it.
A replay does not see it: a typed kind mints a second copy under the next `<n>`, and a named kind refuses its own record as untracked.

**Grades:** 7 MEDIUM.

**Fix:** read the add's exit, remove or restore the written file on non-zero, and raise naming git's stderr (exit 2 or 3), through one helper at every call site.
The skeptic judged it SOUND.

**Left-shift gate:** a plant that holds `.git/index.lock`. Class `failed-stage-reads-as-nothing-staged`.

### M4. The claim CLI refuses a slug the derived grammar admits (finding 10)

**Where:** `tools/memory-tree/gov-claim.sh@9ab8a922:948` (`check_claim_args`).

**What is wrong:** the CLI refuses any slug outside `^[A-Za-z0-9]+$` before asking the derived grammar.
`id_grammar.py`'s in-slug date shape admits and mints hyphenated slugs such as `d2026-10-26ClosedLoop`.

**Consequence:** under `builds.slug-date = in-slug`, `--new-build` and `gov_record.py new ask` fail for a build the grammar declares valid.
The grammar's flip probe never runs the claim CLI.
The refusal is loud and writes nothing.

**Grades:** 10 MEDIUM (finder high, re-graded): the failure is contained to that policy value.

**Fix:** widen the pre-check to `^[A-Za-z][A-Za-z0-9-]*$`, as `push-main.sh` does, and leave the grammar to the `id_grammar.py` match below it.
The skeptic judged it SOUND.

**Left-shift gate:** the hyphenated flip slug in the claim CLI's self-test arms, for both verbs. Class `two-answers-to-one-question`.

### M5. `show <key>#<tag>` falls back to a section outside the addressed record (finding 11)

**Where:** `tools/memory-tree/record_find.py@9274eaf3:500` (the final pick) and the candidate loop above it (line 476).

**What is wrong:** when no section of the tag lies inside the record, the pick falls back to any section of that tag in the file.
The candidate loop likewise accepts a file because the tag exists anywhere in it.
Spec 9 S5 says the result is the record's section and an unknown tag exits 2.

**Consequence:** another record's section is returned under the addressed key.
The extractor over `memory/builds/d*` finds 1229 anchored records in sectioned files with no section inside their extent, so the input is common.
`gov_record` show, `gov_tag` show, the edge grammar's `id#tag` resolution and the read budget all use this reader.
The finder's decisions-ledger example does not hold, because sections are extracted only from record files and specs; the defect does.

**Grades:** 11 MEDIUM.

**Fix:** require `line <= s[1] <= end` in both places and raise `FindError` otherwise; if an H1 id's row has a short extent and needs the whole file, extend that record's end line.
The skeptic judged it SOUND.

**Left-shift gate:** two anchored records in one file, the section only under the second, `show <first>#<tag>` must exit 2. Class `fallback-fabricates-the-passing-value`.

### M6. `record_kinds.py --selftest` is run by nothing (finding 13)

**Where:** `tools/memory-tree/record_kinds.py@cf958bc1:2421`.

**What is wrong:** the leg runs only `--check`, and `check-memory-hygiene.test.sh` runs one plant (`alias-row-drained`) and one `check_row` import.
`--selftest` has no caller, so 55 of the 56 plants are exercised by nothing automated.

**Consequence:** every red branch of the `record-kinds` leg except `alias-row-drained` can be broken or deleted with the bar green.

**Grades:** 13 MEDIUM (finder high, re-graded): the checker works today, so the effect is missing regression cover.

**Fix:** run `record_kinds.py --selftest` from `check-memory-hygiene.test.sh`, asserting exit 0 and the PASS line, or declare a pass leg for it; raise the floor and check it reds with one predicate cut.
The skeptic judged it SOUND.

**Left-shift gate:** that call, joined with M8's rule that every plant a module declares is named by a suite. Class `refusal-branch-with-no-arm`.

### M7. No fixture reaches any red branch of the shape-run check (finding 14)

**Where:** `tools/memory-tree/shape_run.py@f6cda96d:170` (`check_shape_runs`).

**What is wrong:** the only executed callers are `tier2-review.test.sh` spawning `--parse-line` and the `--check` leg.
There is no fixture verb, no writer calls the door, and the tree tracks no shape-run record, so the leg takes only its announced unarmed path.

**Consequence:** a compare broken in any red branch stays green until the first record exists.

**Grades:** 14 MEDIUM (finder high, re-graded): contained while the population is empty.

**Fix:** add a `--fixture --plant` set with a red case for every red branch: malformed record, Caused-by naming none, Caused-by naming two, a review with no line or a refused line, and one field differing (including a field absent on one side), plus one equal green case.
Run all of them from `check-memory-hygiene.test.sh`, asserting the exit and the named record and field, skip-counted where git is absent, and raise the floor.
This is the skeptic's class-level fix: the finder's set (equal, one field differing, Caused-by none and two, refused review line) is INSTANCE-ONLY and omits the malformed-record branch.

**Left-shift gate:** the plant set above. Class `refusal-branch-with-no-arm`.

### M8. Three census plants are run by no suite (finding 15)

**Where:** `tools/memory-tree/record_causes.py@5c2f60ee:227` (`CENSUS_PLANTS`).

**What is wrong:** `literal-without-cause`, `duplicate-cause` and `unmarked-writer` are named nowhere outside the module.

**Consequence:** the per-line grading of the writer census (TOOL-dTotalRecall-53 S9, S34) has no check.
A regression to per-file grading, or a marker that keeps the whole file, still passes the one plant that runs.

**Grades:** 15 MEDIUM.

**Fix:** a loop over the three plants in `check-memory-hygiene.test.sh`, asserting each exit and its `fixture <plant> · PASS` line, plus a join that every PLANTS member is run by the suite.
The skeptic judged it SOUND.

**Left-shift gate:** the PLANTS-to-suite join, which M6 and L1 can share. Class `refusal-branch-with-no-arm`.

### M9. The hygiene suite's assertion floor does not cover its own new arms (finding 16)

**Where:** `tools/memory-tree/check-memory-hygiene.test.sh@44d5dafd:5803`.

**What is wrong:** `FLOOR_ASSERTIONS` moved from 797 to 830 for units 2 and 7 only.
The arms added by the other units (about lines 3735-4045, 86 lines calling hit or miss plus many counter assertions) raised nothing. (DERIVED 2026-11-25, the review)

**Consequence:** the record-find, record-causes and census-kept block can be stranded past an early exit or deleted, and the floor still passes.

**Grades:** 16 MEDIUM.

**Fix:** raise the floor to the observed count of a whole run, less nothing, with skips carried by `n_skip`.
The skeptic judged it SOUND.

**Left-shift gate:** the observed whole-run count as the pin, re-measured when arms land. Class `floor-left-below-the-arms-it-guards`.

### M10. The map replay's byte term cannot decide on real transcripts (finding 20)

**Where:** `tools/workflows/replay_scorer.py@6d355898:1319` (`measure_bytes_before_act`).

**What is wrong:** the measure ends at the first call that is neither runlog's `read` class nor an existence search.
`derive_tool_class` returns `other` for a shell `git diff`, `cat` or `sed -n`, so a lens's first `git diff` reads as its first act.
The code conforms to spec 17 §4, but the term is inert.

**Consequence:** the build's verdict record states the term read 0 in all 40 scored lens runs and cannot lose as measured.
Ask TOOL-dTotalRecall-111 offers a second replay's win as its acceptance with no mention of the defect, which would admit units 14 and 15 on a verdict whose byte term is always `rise 0`.
The `map-transcript` fixture opens with Grep, git grep and Read, so it cannot see it.
Recall lost on its own, so the recorded verdict stands.

**Grades:** 20 MEDIUM.

**Fix:** decide the act by an explicit closed reading, not by runlog's `other`.
A shell call is a pre-act read when every segment's program is in a declared read set (existence searches, git diff/show/log/blame/status/cat-file/rev-parse, cat, head, tail, sed without -i, wc, cd, echo) with no file-writing redirection, and non-acting harness tools such as ToolSearch never count as an act.
Amend spec 17's §4 definition to match.
Print `term bytes: unarmed`, and have `derive_map_verdict` refuse `win` when every run of both arms reads 0.
This is the skeptic's class-level fix: the finder's (an act only where a writing class or a writing segment) is INSTANCE-ONLY, since runlog has no detector for a segment that writes and non-shell `other` calls still end the measure.

**Left-shift gate:** the `map-transcript` arm extended with an opening `git diff`, a `sed -n` pipe and a writing `sed -i`, seen red on today's loop. Class `armed-but-unreachable-rule`.

## LOW

### L1. The `cardinality-refused` plant is run by no suite (finding 18)

**Where:** `tools/playbook/edge_grammar.py@03b58448:1149`.

**What is wrong:** the plant is declared and implemented, and the arm table in `adopt-playbook.sh` lists only missing, mirror, branch and merge.

**Consequence:** TOOL-dTotalRecall-53 S12 has no automated check, so cutting the `cardinality: refused` lines leaves the suite green.

**Grades:** 18 LOW.

**Fix:** add a `cardinality-refused` row, expecting exit 0 and `edges: plant cardinality-refused · PASS`, to the edge arms in `adopt-playbook.sh`.
The skeptic judged it SOUND.

**Left-shift gate:** that row, under M8's join. Class `refusal-branch-with-no-arm`.

review-shape kind=diff-review round=1 intensity=full at=synth raw=20 confirmed=20 refuted=0 merged=0 unverified=0 blocker=0 high=8 medium=11 low=1 agents=11 out-tokens=99713 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=8 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/memory-tree/build_records.py@693f05d3:1235 | high | medium | confirmed | gov_record.py main partitions --field at the first '=' and checks only that the key is non-empty. write_new_record's forged check and write_record's test only the value; the key is just a label. I re-ran the finder's key: check_line_break returned '' and FORGED_FIELD did not match, and render_text emits `- **{k}:** {v}` verbatim. check_header compares only made-by and caused-by (edges only with --edge), and untyped kinds check only Serves. So a planted `**Commissions:**` line is written and staged. Reachable, and new through this CLI. The caller is a local agent that could edit the file directly, so there is no privilege boundary and the effect is a forged but tracked, diffable line: medium. Fix: all KINDS fields and shape-run field names match the key grammar, and the write_record callers I read use conforming, non-duplicate keys. | sound | a-view-fix-trades-one-blindness-for-another | class:invariant-held-on-one-admission-path |
| 2 | security | tools/memory-tree/record_find.py@9274eaf3:478 | high | high | confirmed | Re-ran read_section('.', 'NO-SUCH-KEY@<blob of HEAD:README.md>'): key NO-SUCH-KEY, path '', lines 1-121, README text. The code's `found[0] if found else (1, len(text))` fallback has no key check on the blob branch. Spec TOOL-dTotalRecall-9 S5 says an unknown key exits 2 naming it. check_read_set looks supersession up by the unverified sec['key'], and handoff.py --read passes through `gov_record.py budget`, so a mislabelled blob passes as a valid read. It needs an explicit mismatched @blob address, so the path is narrow: high. | sound | decision-re-derived-by-a-second-process | class:fallback-fabricates-the-passing-value |
| 3 | security | tools/memory-tree/build_records.py@693f05d3:1078 | medium | medium | confirmed | tools/memory-tree/build_records.py@693f05d3:1078 compares `env or 'absent'` with the claim's session. tools/memory-tree/gov-claim.sh@9ab8a922:951 writes `${CLAUDE_CODE_SESSION_ID:-absent}`, and a missing session line also defaults to 'absent', so two sessionless processes compare equal and the mint is admitted silently. The sibling placement.read_lease_class explicitly requires `me != 'absent'` and its docstring says a session the harness exposes none of holds no lease, so this rung departs from the kit's own rule. Contained: it needs a sessionless claimant and caller, and only mints a record stamped owner. The fix offers falling through to the session rule when either side is absent; where the claim names a real session and the caller is absent, that would admit what today is refused. | unsound | - | class:fallback-fabricates-the-passing-value |
| 4 | correctness | tools/lib/gov-feed.sh@acbb74bb:326 | blocker | high | confirmed | Re-ran in a scratch repo: p, b on branch b1, m1 on main, add_record_events, --no-ff merge, add_record_events. check_feed printed `extra refs/heads/main <m1>` rc 1 on a feed holding exactly p, m1, b. The next landing appended m1 again (rows 2 and 4), and check then passed on sets. The code resumes from the last record line's commit, with --no-merges, so it never resumes at the merge. The header's stated blind spot covers only a force-rewritten branch. Introduced by this diff and reachable on ordinary merge landings. It is bounded: a false red on the `--feed check` verb and duplicate node-local events, which no gate leg I found consumes and no tracked data is lost: high rather than blocker. A per-ref landed-tip cursor used by both append and check cures it, in the shared block and its carriers. | sound | a-merge-of-the-default-branch-read-as-additions | class:append-without-an-idempotence-key |
| 5 | correctness | tools/memory-tree/build_records.py@acbb74bb:1348 | high | high | confirmed | I read tools/memory-tree/build_records.py@693f05d3:1308-1352. read_ordered_fields keeps only bullet FIELD lines. The order list drops Serves. For untyped kinds Caused-by is removed from fields and written as a header line. derive_content_key therefore hashes only kind, stem and bullets. The log, research, design-record, spec-audit and diff-review rows have schema fields = ["Serves"], so a second call with the same --name but another unit, title or cause returns `exists` at 1348, before the refusal at 1350. Spec TOOL-dTotalRecall-2's table promises exit 2 for `a different value under an existing id`, so this is not by design. It loses a different record silently, but only on a reused name. The fix adds unit, title and Caused-by but leaves the --edge lines outside the key. A call differing only in its edges would still answer `exists` and drop them. | instance | - | new:content-key-omits-a-supplied-input |
| 6 | correctness | tools/memory-tree/record_find.py@acbb74bb:493 | medium | medium | confirmed | I read tools/memory-tree/record_find.py@9274eaf3:487-512. In the blob branch, an unknown key gives path '' and found [], so held becomes (1, len(lines)) and the whole blob is returned as that key's record. A known key with an unrelated blob takes the same fallback when extract_record finds no row of the key. The unknown-key FindError exists only in the blob-None branch. Spec TOOL-dTotalRecall-9 line 157 says an unknown key exits 2, so the behaviour breaks the spec. check_read_set and edge_grammar.resolve_edge (id#tag form) both consume this result. The effect is contained to wrong pinned addresses. The fix, raising unless the index or the extraction yields a row of the key, cures it and keeps the unheld-old-blob case. | sound | - | class:fallback-fabricates-the-passing-value |
| 7 | correctness | tools/memory-tree/build_records.py@acbb74bb:1377 | medium | medium | confirmed | tools/memory-tree/build_records.py@693f05d3:1377 runs git add with capture_output and check=False, discards the result and returns `wrote`. tools/memory-tree/gov_record.py@5622bd55:261 and :272 do the same. The spec's exit table says `wrote` means `written and staged`. The listing uses record_kinds.read_tracked, so an unstaged record is invisible to a replay: a typed kind mints the next n, and a named kind hits the untracked refusal at 1352. It is reachable when index.lock is held by another process in the worktree. The file stays on disk, so the effect is contained. Checking the exit, undoing the write and refusing through one helper at every call site cures it. | sound | failed-stage-reads-as-nothing-staged | class:failed-stage-reads-as-nothing-staged |
| 8 | seams | tools/lib/gov-feed.sh@2520b71e:326 | high | high | confirmed | derive_record_rows takes the last `record` line's commit as the walk start, derive_record_events walks <from>..<tip> with --no-merges, and write_feed_lines does no key check. I re-ran the probe: the last walked commit for 3d6c1702a is 7ff7bbe5e, and `git log --no-merges 7ff7bbe5e..3d6c1702a -- memory/` lists 413 commits. All 413 were in the first walk, so the next landing (tools/push-main.sh@8ddf8a3e:2146 and 2358, tools/unattended/unattended.sh@522fcd60:20640) appends them again, against the documented `appended once`. The disclosed limitation covers only a force-rewritten branch. One sub-claim is wrong: check_feed does not stay green. Its record arm derives the walk to that same newest line's commit, so logged commits outside its ancestry print `extra`, a false red from the same non-dominating anchor. The finder's dedupe cures the append, but check_feed keeps that anchor and stays wrong. | instance | - | class:append-without-an-idempotence-key | (DERIVED 2026-11-25, the review)
| 9 | seams | tools/runlog/memory_measure.py@1dcdc842:128 | high | high | confirmed | I ran check_memory_word with main and cwd C:/projects/coding-governance. 'memory' and 'memory/' return False with the cwd and True with cwd None. The absolute <main>/memory returns False, and memory/a.md returns True. derive_read_channel gives None for Grep path=memory and for `rg foo memory/`. The docstring says a relative word that is `<root>` alone counts, and measure_agent_memory passes the recorded cwd, so a root-wide search contributes no bytes and the median is understated. The file is new in this diff. Adding the equality to both absolute branches closes every spelling of the root. | sound | - | class:containment-tested-one-way |
| 10 | seams | tools/memory-tree/gov-claim.sh@9ab8a922:948 | high | medium | confirmed | check_claim_args applies ^[A-Za-z0-9]+$ before reading --print slug-re. I ran that regex on d2026-10-26ClosedLoop and it refuses. id_grammar's _SLUG_DATE_SHAPE and its flip probe admit and mint that exact slug, and the header states the admit grammar is the test. write_slug_claim and the ask mint both run this CLI, and any non-zero exit stops --new-build. It is reachable only under builds.slug-date = in-slug with a hyphenated date, and it is a loud refusal that writes nothing, so it is contained. The widened pre-check is the one push-main.sh uses; the derived grammar still bounds the slug, and it stays ref-safe. | sound | - | class:two-answers-to-one-question |
| 11 | seams | tools/memory-tree/record_find.py@9274eaf3:500 | medium | medium | confirmed | The candidate loop accepts any file where the tag exists anywhere, and the final pick falls back to `[s for s in secs if s[0] == tag]` without containment, so a section outside the addressed record is returned. Spec 9 S5 says the result is the record's section and that an unknown tag exits 2. extract_record gives non-H1 anchored ids an extent of only their own lines. I ran the extractor over memory/builds/d*: 1229 anchored records sit in sectioned files with no section inside their extent (for example TOOL-dBoundRoles-14 in another unit's brief). The input is therefore common. gov_record, gov_tag, edge_grammar and the budget all use this reader. The finder's decisions-ledger example does not hold, because sections are extracted only from record files and specs, but the defect does. Spec H1 rows and file-key records already span the whole file, so strict containment in both places is safe. | sound | - | class:fallback-fabricates-the-passing-value |
| 12 | verification | tools/memory-tree/record_causes.py@5c2f60ee:533 | high | high | confirmed | read_claim_slugs runs for-each-ref over refs/gov/claims/ in the local repository. gov-claim.sh sets only refs/gov/remote/claims/<slug> locally (write_feed_success, GC_CACHE), and gen_build_index's CLAIM_CACHE_NS reads that cache. I listed refs/gov in this worktree and it holds only refs/gov/remote/claims/asks/TOOL-dWitnessedBar. The claim-root plant creates refs/gov/claims/fClaim itself with update-ref, so it certifies a state no production writer makes, and the claim root never fires in a clone. The existing nested-name filter still excludes ask counters under the cache namespace. Minting the plant through the CLI exercises the real path. | sound | - | new:fixture-plants-a-state-no-writer-makes |
| 13 | verification | tools/memory-tree/record_kinds.py@cf958bc1:2421 | high | medium | confirmed | I searched tools/ and .github for record_kinds. The leg in tools/gate-legs.json@9e4e2026:5502 runs only `--check`. The suite runs only `--fixture --plant alias-row-drained` (tools/memory-tree/check-memory-hygiene.test.sh@44d5dafd:3937 and 3948) and one check_row import (3803). `--selftest` is dispatched at tools/memory-tree/record_kinds.py@cf958bc1:2628 and has no caller, so 55 of the 56 PLANTS are exercised by nothing automated. The checker is new in this diff and works today, so the effect is missing regression cover rather than a wrong result. Fix: run_selftest iterates the shows, want and refusals plants plus the new and --write arms, which covers every PLANTS member, so running it in the suite or as a leg closes the class. | sound | - | class:refusal-branch-with-no-arm |
| 14 | verification | tools/memory-tree/shape_run.py@f6cda96d:170 | high | medium | confirmed | The only executed callers of shape_run.py are tools/workflows/tier2-review.test.sh@5f066383:2073 (`--parse-line`) and the `--check` leg (tools/gate-legs.json@9e4e2026:1472). shape_run.py has no fixture or selftest verb, and its own docstring says no writer calls the door yet. The tree tracks no shape-run record, so the leg only takes the announced unarmed path and no compare branch is exercised. The effect is contained while the population is empty. Fix: the proposed plants leave out the malformed-record branch, so one of the red branches the claim names still has no failing case. | instance | - | class:refusal-branch-with-no-arm |
| 15 | verification | tools/memory-tree/record_causes.py@5c2f60ee:227 | medium | medium | confirmed | A search of tools/ and .github for `literal-without-cause`, `duplicate-cause`, `unmarked-writer` and CENSUS_PLANTS matched only record_causes.py itself. The suite runs `writer-without-cause` at line 3778 but none of the three. check_census_plant (tools/memory-tree/record_causes.py@5c2f60ee:1345) is the only code asserting per-line grading, and nothing runs it. Fix: check_census_plant returns exit 0 and a PASS line as the fix assumes, and the PLANTS-to-suite join covers the class. | sound | - | class:refusal-branch-with-no-arm |
| 16 | verification | tools/memory-tree/check-memory-hygiene.test.sh@44d5dafd:5803 | medium | medium | confirmed | The base floor is 797 and the head floor is 830. The comments above it credit only TOOL-dTotalRecall-2 (+31) and -7 (+2). Lines 3735-4045 hold 86 lines calling hit or miss, plus many `n=$((n+1))` exit assertions such as 3785 to 4028, several of them in loops. Apart from unit 7's two arms these add to n without raising the floor, so that block can be stranded and n still clears 830. Other floor history pins the floor to the measured count, so this diff opened the gap. Fix: pinning to an observed whole-run count, with skips carried by n_skip, restores the property for every arm. | sound | floor-left-below-the-arms-it-guards | class:floor-left-below-the-arms-it-guards | (DERIVED 2026-11-25, the review)
| 17 | verification | tools/memory-tree/record_causes.py@5c2f60ee:416 | high | high | confirmed | Read read_legacy_paths: the home is already established as `armed`, then `if not paths: return None, ... holds no record row`. run_check tests `g['legacy'] is None`, prints unarmed and exits 0 before check_causes, check_orphans and check_cause_writers (which carries check_kept_home). run_backfill does the same. The registration is shrink-only with drain=key, so emptying the slice is the admitted direction. record_kinds.read_legacy_keys returns a set for the same situation and keeps grading. The home holds 11408 `-` causes rows today, so the path is narrow (full drain or bulk deletion). Returning the empty set is safe at every caller: line 677 uses `legacy or ()`, and the set is only intersected or tested for membership. | sound | - | class:vacuous-selector-empty-population |
| 18 | verification | tools/playbook/edge_grammar.py@03b58448:1149 | low | low | confirmed | CARDINALITY_PLANTS declares cardinality-refused and its branch is implemented. The adopt-playbook.sh PLANTS heredoc has rows for only missing, mirror, branch and merge. A grep over tools finds no other caller and no other check of `cardinality: refused`. TOOL-dTotalRecall-53 names this plant as its New arm. The plant returns rc 0 on PASS, so one row with exit 0 arms it. | sound | - | class:refusal-branch-with-no-arm |
| 19 | intent | tools/lib/gov-feed.sh@2520b71e:331 | high | high | confirmed | derive_record_rows takes only the file-order last record commit as `from` and runs `from..tip`; no key test follows. Re-ran the evidence: the topo-last non-merge memory commit up to 3d6c1702a is 7ff7bbe5e, and `7ff7bbe5e..3d6c1702a -- memory/` lists 413 non-merge commits. A repeat call or the next landing therefore appends those keys again. check_feed compares sets and its duplicate test sees only consecutive equal keys, so it stays green. The function comment says `appended once`, and spec 24's AC2 red condition is a repeated call appending a duplicate key; the header's known limits name only a force-rewritten branch. This is the normal landing shape here. No key goes missing, so it is not a blocker. Filtering by (blob, commit) for the ref under the lock restores append-once for any walk start, including the forced-rewrite case, and leaves the walk's coverage unchanged. | sound | - | class:append-without-an-idempotence-key |
| 20 | intent | tools/workflows/replay_scorer.py@6d355898:1319 | medium | medium | confirmed | measure_bytes_before_act breaks at the first call that is neither class `read` nor a search, and derive_tool_class returns `other` for a shell `git diff`, `cat` or `sed -n`. The build's verdict record states the term read 0 in all 40 runs and `cannot lose as the instrument measures it`. The code conforms to spec 17 §4, but the term cannot decide in practice. Ask TOOL-dTotalRecall-111 accepts a second replay's win with no mention of it. The map-transcript fixture opens with Grep, git grep and Read, so it cannot see it. Contained: recall lost alone, so the recorded verdict stands. On the fix: `a segment writes` has no detector in runlog (an `other` class covers `sed -i` and redirections alike), and non-shell `other` calls still end the measure, so a class-level act definition is needed. | instance | - | class:armed-but-unreachable-rule |

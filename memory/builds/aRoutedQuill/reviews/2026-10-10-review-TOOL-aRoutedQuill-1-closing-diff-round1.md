**Serves:** diff-review TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-7

# Tier-2 closing diff review — aRoutedQuill, ROUND 1

*The closing review (BUILD-METHOD M8) of the unattended build aRoutedQuill, over the cumulative diff
at the integration boundary. The build routes every code build through orientation, a brief and a
specced unit: a Tier-1 micro-spec profile, `## route` rules on the session card, a PreToolUse write
gate in scratch-guard.js, a push-time routed-commits leg, SubagentStart route injection, the charter
DoR rule, govkit's default-gained kits and routing scaffold, and the unattended prompt-brief check
reading its sub-heads from the kickoff checker. Base is origin/main's tip 76b9c451, which the branch
merged at 8dea35478, so base..head is exactly this build's change. TOOL-aRoutedQuill-6 (a trial) is
carried forward unbuilt and is not in the diff. Node `a`, 2026-10-10.*

Reviewed range: `76b9c4518b9e97fa7478ccac76a99041ce984ced...ff0b3dc327514e020eb47009de931d4dfd78c608` · ROUND 1

## Verdict: BLOCKED

One blocker survived. The new routed-commits leg is red at head in WHOLE mode, because three
post-cutoff commits that arrived with the origin/main merge are not waived. TOOL-aRoutedQuill-3 AC10
requires that run to exit 0, and gov's remote CI runs it that way. Two highs and fourteen mediums
were also confirmed. The largest cluster is one config key, MEMORY_ROOT, read three different ways by
the route writer, the gate and check-wiring. All of them fail closed or misreport rather than admit
a wrong write, except finding 1, a junction path that the gate admits silently. The push leg still
grades that write, which keeps it contained.

## Review shape

Intensity full, raw 28, confirmed 27, refuted 1, unverified 0 (0 uncertain), precision 0.96.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |
| correctness | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| seams | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| verification | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| intent | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by raw confirmed finding: BLOCKER 1 (id 23), HIGH 2 (ids 4, 9), MEDIUM 14
  (ids 1, 3, 5, 6, 10, 11, 13, 16, 17, 18, 19, 24, 25, 26), LOW 10 (ids 7, 8, 12, 14, 15, 20, 21,
  22, 27, 28).
- Adjudicated tally by item: BLOCKER 1 (B1), HIGH 2 (H1, H2), MEDIUM 9 (M1 to M9), LOW 7 (L1 to L7).
- Every binding grade was kept. Findings 5, 16 and 17 carry the skeptic's re-grade from high to
  medium, which is their binding grade.
- Two defects were reported under different binding grades, and findings are merged only within one
  grade. So they appear twice. Finding 4 (HIGH, H1) is the same defect as finding 23 (BLOCKER, B1).
  Finding 9 (HIGH, H2) is the same defect as findings 16 and 24 (MEDIUM, M2). Each pair is
  cross-referenced below, and one fix closes both items.
- Intent: 9 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 38 items, each assigned to exactly one of 5 lenses (security 8, correctness 8, seams 8,
  verification 7, intent 7).
- By design: the caller's byDesign. The security model supplied to every lens is that the gate is a
  ROUTING aid, not a security boundary. It reads a status the agent itself writes, so approval is
  recorded, not proven, and the push leg is the guarantee.

## Run integrity

- Lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 25 judged sound, 2 judged UNSOUND (findings 14 and 16, whose corrected
  fixes are given below), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 3 RE-GRADED by the skeptic (findings 5,
  16, 17).
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief. No lens died, so the
  finding set is complete for those briefs; it is not evidence of absence beyond them.

## BLOCKER

### B1 — the routed-commits leg is red at head in WHOLE mode; AC10 is not met (id 23)

- **Where:** `.memory-tree.conf:18` (`ROUTED_COMMIT_WAIVED`), graded by
  `tools/memory-tree/routed_commits.py`.
- **Defect:** `ROUTED_COMMIT_WAIVED` was written before the merge of origin/main 76b9c451
  (8dea35478). That merge brought in 3d05f1ea, 4e49aeb5 and d31d7bc9. All three were committed on
  2026-10-09, which is not before the cutoff, they touch `tools/`, and they name no unit. None is on
  the waiver list.
- **Impact:** At ff0b3dc3, `python tools/memory-tree/routed_commits.py` with GATE_PUSH_BASE unset
  prints `routed-commits FAILED` naming all three, and exits 1. The leg has `guard []` and
  `history_depth full`, so it runs on every bar. Remote CI runs `GATE_FULL=1 run-gates.sh` on every
  push to main with no GATE_PUSH_BASE, which is WHOLE mode. The pre-push RANGE run excludes origin's
  commits, so the landing push passes and the breakage shows up only afterwards. From then on every
  branch bar and gov's remote CI go red on commits no session can change. TOOL-aRoutedQuill-3 AC10
  requires the WHOLE run over this repo to exit 0, and its Rollout says the landing commit waives
  every cutoff-day commit.
- **Fix (judged SOUND by the skeptic):** Add 3d05f1ead, 4e49aeb53 and d31d7bc96 as 12-hex prefixes
  to `ROUTED_COMMIT_WAIVED` and extend its comment. Re-run `python tools/memory-tree/routed_commits.py`
  with GATE_PUSH_BASE unset after every reconcile merge until it exits 0, and do this before the
  mint commit.
- **Left-shift:** The pre-push bar should run this leg in WHOLE mode as well as RANGE mode whenever
  the push carries a merge of the remote's tip, so the landing push sees what remote CI will see.
  Failing that, add a §10 checklist item: after any reconcile merge on a build that ships a
  history-wide leg, run that leg history-wide before landing.

## HIGH

### H1 — main's CI bar goes red on landing and stays red (id 4)

- **Same defect as B1.** Finding 4 was graded HIGH by both finder and skeptic, on the consequence
  that the CI job blocks nothing but reports a false red that hides real ones. Finding 23 graded the
  same root cause BLOCKER through the unmet acceptance criterion. Both grades are binding, so it is
  listed twice. Fixing B1 closes it.
- **Where:** `.memory-tree.conf:18`.
- **Defect:** `ROUTED_COMMIT_WAIVED` lists only five shas and leaves out 3d05f1ea, 4e49aeb5 and
  d31d7bc9.
- **Impact:** `env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py` exits 1 at ff0b3dc3.
  `gate-legs.json:1003` wires the leg, and `remote-ci.yml` runs it in WHOLE mode with fetch-depth 0.
- **Fix (judged SOUND by the skeptic):** Add the three 12-hex prefixes to `ROUTED_COMMIT_WAIVED`, or
  move `ROUTED_COMMIT_CUTOFF` past their committer dates. Then rerun the leg with GATE_PUSH_BASE unset
  and confirm it exits 0 before landing.
- **Left-shift:** As B1.

### H2 — check-wiring certifies a conf with no MEMORY_ROOT as armed while the gate refuses every write (id 9)

- **Same defect as M2 (ids 16, 24).** Finding 9 kept its HIGH grade; 16 was re-graded to medium and
  24 was graded medium. All three grades are binding. Fixing M2 closes this item.
- **Where:** `tools/check-wiring.sh:1455` (`check_routed`), against `checkUnarmed` in
  `tools/hooks/scratch-guard.js:869`.
- **Defect:** `check_routed` reads `${MEMORY_ROOT:-memory}`. The gate reads
  `readConfKey(confBytes,'MEMORY_ROOT')`, which is null when the key is absent, and `checkUnarmed`
  then returns `MEMORY_ROOT is blank or absent` and refuses every write. TOOL-aRoutedQuill-2 §4
  rejects defaulting to `memory` on purpose.
- **Impact:** A conf with ROUTED_PATHS and a cutoff but no MEMORY_ROOT gets
  `ok routed — ROUTED_PATHS (...) and ROUTED_COMMIT_CUTOFF (...) are armed`, while scratch-guard
  refuses every Edit, Write, MultiEdit and NotebookEdit except to the conf. That is a check
  certifying a state it did not check. The path is narrow because adopt scaffolds from the example,
  which sets `MEMORY_ROOT=memory`, and the gate's deny names the cause.
- **Fix (judged SOUND by the skeptic):** Read MEMORY_ROOT without a default (`${MEMORY_ROOT:-}`) and
  report `UNWIRED routed — MEMORY_ROOT is blank or absent`, worded exactly as `checkUnarmed` words
  it. Better still, take the verdict from scratch-guard.js itself (`node -e` requiring
  `checkUnarmed`/`readConfKey`) so the gate and the checker have one answer. Add a
  check-wiring.test.sh arm for a conf with no MEMORY_ROOT.
- **Left-shift:** One reader, not three. A parity arm that feeds the same set of confs to
  `checkUnarmed` and to `check_routed` and asserts they agree on armed or unarmed for each.

## MEDIUM

### M1 — the route writer reads MEMORY_ROOT with a third grammar (ids 5, 10, 17, 25)

- **Where:** `skills/session-kickoff/manifest-check.sh:469` (`read_memory_root`, lines 467-470),
  feeding route rules R0 (`:963`) and R4 (`:988`).
- **Defect:** `read_memory_root` is `sed -n 's/^MEMORY_ROOT=[[:space:]]*//p' | head -1 | tr -d` on
  quotes. It takes the FIRST bare assignment, does not match an `export` prefix, and keeps an
  unquoted trailing `# comment`. The gate's `readConfKey` (`scratch-guard.js:770-773`), the push
  leg's `tree_lib.parse_conf_line` and the hygiene engine's shell `source` take the LAST assignment
  and accept both spellings. tree_lib's docstring (`tree_lib.py:68-75`) documents
  `MEMORY_ROOT=memory   # note` as a spelling adopters really write. The finders disagree on whether
  the sed existed at base: finding 25 says the function is new in this diff, findings 5, 10 and 17
  say the same sed fed only the cosmetic live cell at base. Either way, this diff is what makes it
  gate R0 and R4, so it is in scope.
- **Impact:** With `export MEMORY_ROOT=memory`, the value is empty and R0 exits 2 claiming there is
  no MEMORY_ROOT. With `MEMORY_ROOT=memory  # note`, R4 builds `memory  # note/builds/<b>/spec/`
  and refuses every unit as outside it. With two assignments, R4 checks a different root from the
  gate. In each case no `## route` can land on the card, the gate reads the conf as armed and
  refuses every product write, and the remedy it names (`--card --append`) cannot succeed. It fails
  closed with a self-describing error, so the effect is contained; this repo's own conf is plain.
- **Fix (judged SOUND by the skeptic, all four findings):** Read MEMORY_ROOT the way the shell does:
  source the conf in a subshell and print `${MEMORY_ROOT-}`, as check-wiring's `check_routed` and
  adopt-memory-tree's `derive_routed_candidate` already do. Alternatively apply readConfKey's grammar:
  last assignment wins, optional `export`, quotes peeled, `#` comment only after whitespace. Add
  manifest-check.test.sh arms for the commented and exported spellings that expect a conforming
  route to append.
- **Left-shift:** A shared conf-spelling fixture (plain, exported, trailing comment, quoted, two
  assignments) run against every MEMORY_ROOT reader in the kits, asserting one value. Add a §10
  checklist item: a new caller of an existing config reader inherits that reader's grammar, so check
  the reader before trusting it with a gate.

### M2 — check_routed defaults an absent MEMORY_ROOT the gate treats as unarmed (ids 16, 24)

- **Same defect as H2 (id 9).** Listed here at the binding medium grade of 16 (re-graded by the
  skeptic from high, because the scaffold writes MEMORY_ROOT and the gate's refusal names the exact
  cause) and 24.
- **Where:** `tools/check-wiring.sh:1454-1455`; the pinning fixture at
  `tools/check-wiring.test.sh:403`.
- **Defect:** As H2. The suite pins the disagreement: the fixture at check-wiring.test.sh:403 writes
  a conf with no MEMORY_ROOT and expects `ok routed`. The arm's header claims it grades "by the rules
  the gate and the ownership leg grade it by", but it matches only routed_commits.py, which defaults
  to `memory`.
- **Impact:** The session-start reporter that D7 relies on approves a state the gate rejects.
- **Fix (finding 16's proposal was judged UNSOUND; this is the skeptic's corrected fix, and finding
  24's fix was judged SOUND and agrees with it):** Make `check_routed` refuse a blank or absent
  MEMORY_ROOT first, as the gate does: read `${MEMORY_ROOT-}` and set
  `why="MEMORY_ROOT is blank or absent"` before the ROUTED_PATHS test. Then add `MEMORY_ROOT=memory`
  to all three fixtures in check-wiring.test.sh (`:403`, `:414` and the `:422` loop), and add one arm
  with no MEMORY_ROOT that expects `UNWIRED  routed    — MEMORY_ROOT is blank or absent`.
- **Left-shift:** As H2.

### M3 — the mint names the newest id, not the newest specced id (ids 6, 11)

- **Where:** `tools/memory-tree/routed_commits.py:303-330` (`read_newest_unit`), used by
  `tools/push-main.sh:902-904`.
- **Defect:** `read_newest_unit` returns `ids[0]` of the newest commit in the range that names any
  family-shaped id, merges included, and never checks the id map. The grader (`:258-270`) reds a
  commit when none of its ids has a spec at HEAD.
- **Impact:** Suppose the newest pushed commit is a records commit that names an ask first, for
  example one filing TOOL-aRoutedQuill-8 during a closing review. That id has a backlog row and no
  spec. The records commit touches only memory/ and is not graded, so the range is green. push-main
  then commits `mint: … for TOOL-aRoutedQuill-8` with `Pass: none`, which touches version carriers
  under ROUTED_PATHS. The pre-push leg reds it with `no spec defines it at HEAD` and the attended
  landing aborts, even though older commits in the range name specced units. Nothing wrong lands.
- **Fix (judged SOUND by the skeptic, both findings):** In `read_newest_unit`, load the id map once
  with `load_spec_paths` over HEAD's tracked specs (one cat-file pass), and return the first id,
  walking newest first, that the map defines. Skip merges with `--no-merges` so the population
  matches what the leg grades.
- **Left-shift:** An AC11 arm whose newest commit names an unspecced id first, asserting the mint
  names the older specced unit and the leg passes on the mint.

### M4 — check-wiring reads "the write gate is wired" from any scratch-guard group, and misreports the no-conf case (id 3)

- **Related lows:** L2 (ids 14, 20) report the same two halves at low grade.
- **Where:** `tools/check-wiring.sh:1442` (`check_routed`) and `:1519` (`check_skill_install`); the
  no-conf message at `:1448`.
- **Defect:** Both arms call `matchers_of scratch-guard.js` with no event and no matcher filter. At
  base the shipped fragment's matcher was `Bash|PowerShell`, so every existing adopter carries a
  group that sets `gated=yes` although Edit and Write are not wired. Separately, with no
  `.memory-tree.conf`, the arm says every product write is refused. The gate does the opposite:
  `checkRouted` step 4 returns a witness on ENOENT and admits every write.
- **Impact:** An adopter on the old wiring, or wired only under SubagentStart, gets `UNWIRED routed`
  and `UNWIRED skill` lines that state the write gate is wired. An operator with no conf is told a
  gate is blocking writes when it is off. `check_scratch_guard` still flags the stale matcher, so the
  effect is limited to wrong diagnosis text and extra UNWIRED lines.
- **Fix (judged SOUND by the skeptic):** Make "gated" mean the PreToolUse matchers carrying the
  marker include Edit or Write:
  `matchers_of scratch-guard.js '' PreToolUse | grep -qE '(^|\|)(Edit|Write)(\||$)'`, with the same
  test in `check_skill_install`. Reword the no-conf line to say the gate admits every write here (it
  is off) until a conf declares ROUTED_PATHS. Add a fixture arm with a `Bash|PowerShell`-only
  scratch-guard group that expects no `routed` or `skill` UNWIRED line.
- **Left-shift:** That fixture arm, plus a §10 checklist item: a grep for a marker word is a presence
  probe, not proof the hook fires on the event and tool in question.

### M5 — a product file reached through a junction or symlink is not gated (id 1)

- **Where:** `tools/hooks/scratch-guard.js:924`, in `checkRouted` (`:905-975`).
- **Defect:** The gate finds the target's repository by walking `path.resolve(target)` upward for
  `.git`. Nothing calls realpath on the target.
- **Impact:** Confirmed on node `a`. `~/.claude/skills/session-kickoff` is a junction to
  `C:/projects/coding-governance/skills/session-kickoff`, which sits under the routed `skills/` entry.
  With a session that has no card, an Edit to the repo spelling of `manifest-check.sh` is denied. An
  Edit to `C:/Users/daily-agent/.claude/skills/session-kickoff/manifest-check.sh` finds no `.git` on
  the walk, so `checkRouted` returns null and the write is admitted with no line printed. That
  junction path is the skill's own base directory, which the harness shows the agent when the skill
  loads, so a KICK unit editing the checker is likely to use it. Only the push leg catches it later.
- **Fix (judged SOUND by the skeptic):** Before step 3, replace `target` with the realpath of its
  deepest existing ancestor (`resolveRealPath` already exists), then append the not-yet-existing
  tail. Run `resolveComparableCommon`, the toplevel walk and the `rel` computation on that real path.
- **Left-shift:** A scratch-guard.test.sh arm that writes through a symlink or junction into a routed
  directory and expects a deny.

### M6 — adopters' copy of the routed leg is not declared impure (id 13)

- **Where:** `tools/memory-tree/kit.toml:324-329` (the `[[gate_leg]]`), and govkit's row builder at
  `tools/govkit/govkit.py:4080-4091`.
- **Defect:** Only gov's own `tools/gate-legs.json:1008` marks the leg impure. The kit.toml leg that
  adopters receive does not carry `impure`, and govkit never copies it into the target row.
- **Impact:** In an adopter, a GATE_REUSE run reuses a proven green whenever the tree fingerprint and
  BASE are unchanged. `input_key` (`run-gates.sh:2196-2214`) has no HEAD or commit-message part, so
  after a `git commit --amend` that removes the unit id from the subject, the leg reports
  reused-green for a range it would red. Gov's own `impure` text names exactly this case. The
  pre-push run never sets GATE_REUSE, so the authoritative run still executes the leg.
- **Fix (judged SOUND by the skeptic):** Declare `impure = "…"` on the kit.toml gate_leg and have
  govkit's leg emission copy `impure` into the target row, behind the same reader-floor check used for
  `subject` and `doc_reads`. Alternatively give run-gates' `input_key` a HEAD-commit component for
  this leg.
- **Left-shift:** A parity check that every field of a gov gate-legs.json row whose leg comes from a
  kit is either present on that kit's `[[gate_leg]]` or listed as gov-only.

### M7 — the "covers MEMORY_ROOT" guard tests containment one way only (id 18)

- **Where:** `tools/hooks/scratch-guard.js:876` (`checkUnarmed`, with `checkUnderRoot` at `:213`);
  `tools/memory-tree/routed_commits.py:151`; `tools/check-wiring.sh:1477`.
- **Defect:** All three readers ask only whether MEMORY_ROOT lies under an entry. An entry strictly
  inside MEMORY_ROOT, such as `memory/builds/`, passes as armed.
- **Impact:** With `ROUTED_PATHS="src/ memory/builds/"`, every spec and brief write is gated and
  every spec commit must name a unit already specced. That is the "a spec would need a spec first"
  deadlock spec S6 gives as the rule's reason. The gate reads the conf as armed, check-wiring prints
  `ok routed` and the push leg grades instead of refusing. The configuration is unusual and the
  refusals are loud.
- **Fix (judged SOUND by the skeptic):** Test containment both ways in all three readers: refuse an
  entry when MEMORY_ROOT is under it OR it is under MEMORY_ROOT (`checkUnderRoot(c, mem)` as well as
  `checkUnderRoot(mem, c)`).
- **Left-shift:** A `memory/builds/` arm in scratch-guard.test.sh W-AC5, the routed_commits AC4
  refusal table and check-wiring RQ5 AC7.

### M8 — govkit `update --write` migration has no permanent check (id 19)

- **Where:** `tools/govkit/govkit.py:8656-8690` (the gained list, receipt mutation, `add_deploy_kits`,
  `git add`) and the settings-merge wiring branch at `:10842`.
- **Defect:** The only RQ5 AC4 arms in selftest.py (`:5862-5906`) call `derive_default_gained` with
  `blob_at` stubbed and `add_deploy_kits` on a scratch deploy.toml. Nothing runs `update --write`,
  checks that gained kits are installed and wired, or checks that a deliberate unwire stays unwired.
  The spec's arm row (spec-5 line 289) still says selftest.py covers AC4. AC4 was observed once by
  hand.
- **Impact:** This is the path every existing adopter takes to receive the gate. A regression that
  clobbers an adopter, skips wiring or re-wires a deliberate unwire turns no leg red. No current
  wrong behaviour was shown.
- **Fix (judged SOUND by the skeptic):** Add a govkit matrix shape, or extend shape 6: install at a
  base vintage whose registry default lacks the three entries, run `update --write` to a commit that
  has them, and assert the three `default-gained` lines, the receipt claim and every fragment
  `wired`. Then `settings-merge.py --unwire` the gate fragment, update again, and assert it stays
  unwired and check-wiring names it UNWIRED.
- **Left-shift:** That matrix shape is the gate. Also correct the spec's arm row so it does not claim
  coverage selftest.py lacks.

### M9 — the gate parses the spec H1 more strictly than the writer and the push leg (id 26)

- **Where:** `tools/hooks/scratch-guard.js:845-847` (`checkBuildable`).
- **Defect:** The gate takes the first line starting `# ` and uses its raw first whitespace token. It
  strips no backticks or asterisks, no trailing `:`, and is not fence-aware. KICK R4
  (`manifest-check.sh:989-994`) skips fenced lines and strips `` ` ``, `*` and trailing `:.,;`.
  `tree_lib.parse_spec_h1` matches ``^#\s+[`*]*ID\b``.
- **Impact:** A spec whose H1 reads `# <ID>: title` or `# **<ID>** — title` gets a route through
  `--card --append` and is graded as specced by the push leg, but the gate refuses every product
  write with `has H1 naming <ID>:, not <ID>`, and the remedy does not point at the H1. No spec in
  this repo uses those spellings today, so the effect is an adopter's, and it fails closed.
- **Fix (judged SOUND by the skeptic):** Parse the H1 the way R4 and `parse_spec_h1` do: first
  unfenced `^#\s+` line, strip `` ` `` and `*`, then match the unit id as a whole token.
- **Left-shift:** scratch-guard.test.sh arms for `# <ID>: title` and `# **<ID>** — title`, and a
  shared H1 fixture run through all three readers.

## LOW

### L1 — the example conf says the gate refuses shell writes (ids 8, 15, 27)

- **Where:** `tools/memory-tree/.memory-tree.conf.example:451`.
- **Defect:** The new ROUTED_PATHS paragraph says the write gate "refuses an Edit, Write or shell
  write". The gate only sees Edit, Write, MultiEdit and NotebookEdit. Its header
  (`scratch-guard.js:84`), its README and the spec all state that a Bash or PowerShell write passes,
  and the push leg grades it.
- **Impact:** Adopters read this conf as the key's documentation and are told shell writes are
  blocked. No behaviour changes.
- **Fix (judged SOUND by the skeptic, all three findings):** Reword to "refuses an Edit, Write,
  MultiEdit or NotebookEdit under one …; a shell write passes it, and the routed-commits leg grades
  the commit".
- **Left-shift:** A §10 checklist item: adopter-facing prose about a gate's reach is checked against
  the gate's own "what escapes" header.

### L2 — check-wiring's gated test counts every event, and its no-conf line is backwards (ids 14, 20)

- **Related medium:** M4 (id 3) covers the same two halves at medium grade; fixing M4 closes this.
- **Where:** `tools/check-wiring.sh:1442` and `:1519` (gated test); `:1448` (no-conf message).
- **Defect:** `matchers_of scratch-guard.js` with no event reads every event's groups (`:348-372`),
  so the old `Bash|PowerShell` PreToolUse group and the SubagentStart group both count as the write
  gate being wired. With no conf, the arm says every product write refuses, while the gate admits
  every write (`checkRouted` `:930-934`), which the suite's own W-AC5 arm pins.
- **Impact:** Misleading advice only. Check S flags the stale matcher, and the UNWIRED verdict for
  the no-conf case is right. The skeptic notes the RQ5 AC7 needle only greps
  `.*no .memory-tree.conf`, so the test does not assert the wrong clause.
- **Fix (finding 14's proposal was judged UNSOUND; this is the skeptic's corrected fix):** In both
  `check_routed` and `check_skill_install`, set `gated` only when a PreToolUse scratch-guard matcher
  names a write tool:
  `matchers_of scratch-guard.js "" PreToolUse | grep -qE '(^|\|)(Edit|Write|MultiEdit|NotebookEdit)(\||$)' && gated=yes`.
  **Finding 20's fix (judged SOUND):** change the no-conf message to say the gate admits every write
  because there is no conf to arm it, and update the RQ5 AC7 needle.
- **Left-shift:** As M4.

### L3 — the gate refuses a nested spec the writer and push leg accept (id 7)

- **Where:** `tools/hooks/scratch-guard.js:842`, against `manifest-check.sh:988` (R4) and
  `tree_lib.parse_spec_h1`.
- **Defect:** The gate refuses any spec with a `/` after `<mem>/builds/<b>/spec/`. R4 tests only
  `index(usp, dir "spec/") == 1`, and the push leg accepts any depth. Nested spec folders are tracked
  here (`memory/builds/aDrainedSluice/spec/units/`, `aFoldedQuarry/spec/units/`).
- **Impact:** The writer accepts a route that the gate then refuses, and the SubagentStart context
  reports the unit as not buildable. Fails safe; new specs from gen_build_index are flat.
- **Fix (judged SOUND by the skeptic):** Make the gate and the writer agree on one rule. Either drop
  the `rel.slice(want.length).includes('/')` clause so any depth is accepted, matching
  `parse_spec_h1`, or make R4 refuse nested paths.
- **Left-shift:** A nested-spec arm in both scratch-guard.test.sh and manifest-check.test.sh that
  expects the same verdict.

### L4 — the mint subject can carry a refusal message (id 12)

- **Where:** `tools/push-main.sh:664` (`read_mint_unit`), against `routed_commits.py` `main()` at
  `:544-546`.
- **Defect:** `read_mint_unit` takes the first stdout line of `--newest-unit` with no status check.
  On a Refusal, `main()` prints `routed-commits REFUSED — …` to stdout and exits 2.
- **Impact:** When the kit is present but refusing (a non-letter FAMILIES prefix, a missing conf, a
  failed git call), the mint subject becomes `… for routed-commits REFUSED — …`, contradicting the
  comment that a failure prints nothing. The push leg would red that mint anyway.
- **Fix (judged SOUND by the skeptic):** Capture output and status separately and use the value only
  on exit 0, for example `u=$("$py" … --newest-unit "$1" 2>/dev/null) || return 0;
  printf '%s\n' "${u%%$'\n'*}"`. Or have `main()` print refusals to stderr for that verb.
- **Left-shift:** A push-main arm with a refusing `--newest-unit` stub that asserts the mint subject
  names no unit.

### L5 — scratch-guard admission and refusal branches with no arm (id 21)

- **Where:** `tools/hooks/scratch-guard.js:757` (BUILDABLE_STATUS) and `checkBuildable`; the
  fail-closed catch in `main` at `:1069-1073`.
- **Defect:** W-AC1/W-AC2 cover Tier-2 at INPROGRESS and SPECCED, Tier-1 at SPECCED, a missing spec,
  a spec outside the build, an H1 mismatch and two-unit routes. No arm covers Tier-1 at INPROGRESS
  admitting, a spec with no Tier cell, an absolute or `..` spec path, a route with no `- build:`
  line, or a unit line with no spec, and nothing reaches the fail-closed catch.
- **Impact:** Dropping INPROGRESS from Tier-1's list would wrongly refuse every in-progress Tier-1
  unit, and flipping the catch to admit would make the gate fail open, with the suite green in both
  cases. No current wrong behaviour.
- **Fix (judged SOUND by the skeptic):** Add `run_write` arms: a Tier-1 INPROGRESS spec admits; a
  spec with no Tier cell, an absolute spec path, a route with no `- build:` line and a unit line with
  no spec each refuse naming the reason. Add one arm that forces a throw, for example a `.git` file
  the walk finds but cannot read, and expects exit 2 with `fails closed`.
- **Left-shift:** Those arms. The fail-closed arm is the one that matters most: a hook whose throw
  path is never exercised is a fail-open waiting for a refactor.

### L6 — a `## route` heading with trailing whitespace is a route to the gate but not to the checker (id 22)

- **Where:** `skills/session-kickoff/manifest-check.sh:959` (`grep -c '^## route$'`), `:969` and the
  stale-route strip at `:1054`; against `extractRouteUnits` in scratch-guard.js, which trims lines.
- **Defect:** A body whose heading is `## route ` (or has leading whitespace) sets CARD_ROUTE=0, so
  R0-R6 are skipped and the stored route is not stripped. The gate still reads both sections.
- **Impact:** The card can hold two route sections and the gate reads the union of their units.
  `checkBuildable` re-verifies each unit at write time, so the worst case is a stale route's unit
  admitting a write, which the push leg still grades.
- **Fix (judged SOUND by the skeptic):** Match the gate's reading: detect the heading with
  `^[[:space:]]*## route[[:space:]]*$` in `check_card_route` and the strip awk. Or make the gate
  exact-match, so both read one spelling.
- **Left-shift:** A KQ arm with a trailing-space heading.

### L7 — the build README roster still shows PLAY-aRoutedQuill-1 as INPROGRESS (id 28)

- **Where:** `memory/builds/aRoutedQuill/README.md:67`, inside the hand-kept `roster:units` region.
- **Defect:** The spec status header and the generated build-index row (`README.md:85`) both say
  CLOSED rev-4.
- **Impact:** The document contradicts itself. No gate reads the roster.
- **Fix (judged SOUND by the skeptic):** Set roster row 7 to CLOSED.
- **Left-shift:** Derive the roster's status column from the same front matter the generated table
  reads, or drop the column; a hand-kept copy of a generated fact is the class.

## Refuted

- **id 2** (security, `tools/memory-tree/routed_commits.py:95`) — not reachable within the threat
  model. RANGE mode exists only at the pre-push boundary, where `.githooks/pre-push` refuses a dirty
  tree before the bar runs, and push-main.sh refuses one too. `.memory-tree.conf` is tracked, so an
  uncommitted edit to it is a dirty tree. The only remaining route is `--no-verify`, which the spec
  names as the bypass that remote CI's WHOLE run catches against the committed conf.

review-shape kind=diff-review round=1 intensity=full at=synth raw=28 confirmed=27 refuted=1 unverified=0 blocker=1 high=2 medium=14 low=10 agents=11 out-tokens=257774

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/hooks/scratch-guard.js:924 | medium | medium | confirmed | checkRouted (scratch-guard.js:905-975) runs resolveComparableCommon(target) on path.resolve(target). resolveToplevel walks the lexical path looking for `.git`, and nothing calls realpath on the target. On this machine C:/Users/daily-agent/.claude/skills/session-kickoff is a junction to C:\projects\coding-governance\skills\session-kickoff (checked with dir). Neither C:/Users/daily-agent/.git nor .claude/.git exists, so the walk returns hit=null and key=''. Step 3 then returns null, and the write is admitted silently. The same file under its repo spelling is under routed `skills/` and is graded. That is a wrong admit on a real path. The push leg still catches it, which keeps the effect contained. | sound | - |
| 2 | security | tools/memory-tree/routed_commits.py:95 | medium | - | refuted | Within this threat model the narrowing cannot be reached. RANGE mode exists only at the pre-push boundary. There .githooks/pre-push:1045 computes `git status --porcelain --ignore-submodules=untracked`, and :1442-1447 refuses the push before the bar runs when it is non-empty. push-main.sh refuses a dirty tree too (:688, :869). `.memory-tree.conf` is tracked, so an uncommitted edit to it is exactly a dirty tree and the push is refused. The only remaining route is --no-verify, which the spec already names as the bypass that remote CI's WHOLE run catches, and CI reads the committed conf. | sound | - |
| 3 | security | tools/check-wiring.sh:1442 | medium | medium | confirmed | check_routed (:1442) and check_skill_install (:1519) call `matchers_of scratch-guard.js` with no event and no matcher filter. At the base, the shipped fragment's matcher was `Bash\|PowerShell`, so every existing adopter carries a group that sets gated=yes even though Edit/Write is not wired. Separately, the gate with no conf returns a witness (scratch-guard.js step 4, ENOENT returns { witness }), which admits every write. The arm's text says 'every product write refuses', the opposite of what happens. check_scratch_guard does flag the stale matcher, so the operator still gets a correct UNWIRED line, and the effect is limited to wrong diagnosis text and extra UNWIRED lines. | sound | a-grep-for-a-word-is-a-presence-probe |
| 4 | correctness | .memory-tree.conf:18 | high | high | confirmed | I reproduced it. At ff0b3dc3, `env -u GATE_PUSH_BASE python tools/memory-tree/routed_commits.py` exits 1 and names 3d05f1ea, 4e49aeb5 and d31d7bc9 as 'names no unit'. All three are ancestors of base 76b9c451 and were committed on 2026-10-09, which is not before the cutoff. ROUTED_COMMIT_WAIVED lists only the five other shas. gate-legs.json:1003 wires the leg into the bar, and remote-ci.yml runs `GATE_FULL=1 run-gates.sh` on every push to main with fetch-depth 0 and no GATE_PUSH_BASE, which is WHOLE mode. Main's CI bar therefore goes red on landing and stays red. The CI job blocks nothing, but it reports a false red that hides real ones. | sound | - |
| 5 | correctness | skills/session-kickoff/manifest-check.sh:469 | high | medium | confirmed | read_memory_root (manifest-check.sh:467-470) is `sed -n 's/^MEMORY_ROOT=[[:space:]]*//p' \| head -1 \| tr -d '\r"'`. `export MEMORY_ROOT=memory` does not match and yields an empty value, so check_card_route's R0 exits 2. `MEMORY_ROOT=memory  # note` yields `memory  # note`, so the R4 prefix test `index(usp, dir "spec/")` refuses every unit. tree_lib's parse_conf docstring (:74-75) documents both spellings as legal, and readConfKey accepts both. The sed was already there at base for the live cell (line 409). This diff makes it reachable from the new route rules, so it is in scope. The consequence fails closed: on a narrow population, every route is refused and so is every product write, with a self-describing error. That keeps the effect contained, so medium rather than high. | sound | - |
| 6 | correctness | tools/memory-tree/routed_commits.py:316 | medium | medium | confirmed | read_newest_unit (routed_commits.py:316-330) returns ids[0] from the newest commit that names any family-shaped id, and it never checks the id map. check_routed_commits reds an id that no spec at HEAD defines (:270, 'no spec defines it at HEAD'). push-main.sh:902-904 puts that id in the mint commit, and the mint touches version carriers under ROUTED_PATHS, so it is graded. Ask ids such as TOOL-aRoutedQuill-8 share the TOOL family and have only backlog rows, no spec. A newest records-only commit that names an ask first is therefore plausible, for example filing an ask during a closing review. In that case the pre-push leg refuses the mint and the attended landing aborts. Nothing wrong lands, so the effect is contained. | sound | - |
| 7 | correctness | tools/hooks/scratch-guard.js:842 | low | low | confirmed | scratch-guard.js:842 refuses any spec whose path has a '/' after `<mem>/builds/<b>/spec/`. manifest-check.sh:988 R4 only tests `index(usp, dir "spec/") == 1`, so it accepts nested paths. Nested spec folders are tracked in this repo (memory/builds/aDrainedSluice/spec/units/..., aFoldedQuarry/spec/units/...). The writer therefore accepts a route that the gate then refuses. The failure is safe and contained, and new specs from gen_build_index are flat. | sound | - |
| 8 | correctness | tools/memory-tree/.memory-tree.conf.example:451 | low | low | confirmed | .memory-tree.conf.example:451 says the gate refuses 'an Edit, Write or shell write'. The hook only sees Edit/Write/MultiEdit/NotebookEdit, and the stated security model is that shell writes pass the gate and the push leg grades them. This is adopter-facing documentation that misstates behaviour; the code itself is unaffected. | sound | - |
| 9 | seams | tools/check-wiring.sh:1455 | high | high | confirmed | check-wiring.sh check_routed reads `${MEMORY_ROOT:-memory}`. The gate reads `readConfKey(confBytes,'MEMORY_ROOT')`, which returns null when the key is absent, and checkUnarmed (line 869) then returns 'MEMORY_ROOT is blank or absent', which refuses every write. The TOOL-aRoutedQuill-2 spec (line 255) explicitly rejects defaulting to `memory`. So a conf with ROUTED_PATHS and a cutoff but no MEMORY_ROOT gets 'ok routed' from the checker while the gate refuses everything: a check certifying a state it did not check. The path is narrow, because adopt scaffolds from the example, which sets MEMORY_ROOT=memory, and the gate's deny names the cause, so this is high rather than blocker. | sound | - |
| 10 | seams | skills/session-kickoff/manifest-check.sh:469 | medium | medium | confirmed | read_memory_root is `sed -n 's/^MEMORY_ROOT=[[:space:]]*//p' \| head -1 \| tr -d quotes`. It keeps a trailing `# note` and trailing spaces, does not match `export MEMORY_ROOT=`, and takes the first assignment rather than the last. At base the same sed only fed the cosmetic live cell (base line 409); this diff makes it gate R0 (line 963, exit 2) and R4's dir (line 988). On those legal spellings no route can be appended, while readConfKey parses them correctly and refuses product writes for lack of a route. The effect is contained to adopters using those spellings, and this repo's conf is bare `MEMORY_ROOT=memory`. | sound | two-answers-to-one-question |
| 11 | seams | tools/memory-tree/routed_commits.py:303 | medium | medium | confirmed | read_newest_unit returns ids[0] of the newest commit in the range, merges included, and never checks id_map. The grader (lines 258-266) reds a commit when none of its ids has a spec at HEAD. The mint's subject carries only mint_unit, and `Pass: none` contributes no id, so an unspecced first id (an ask or backlog id) yields 'no spec defines it at HEAD' on the mint, and the attended landing's pre-push refuses. Older commits naming specced units do not save it. This is reachable but needs an unspecced id first in the newest commit; the effect is a refused landing, not a wrong pass. | sound | decision-re-derived-by-a-second-process |
| 12 | seams | tools/push-main.sh:664 | low | low | confirmed | main() prints `routed-commits REFUSED — ...` to stdout and returns 2 (lines 544-546). read_mint_unit pipes stdout through `head -n 1` with no status check, so on a Refusal (for example a conf/FAMILIES refusal or a git failure inside read_newest_unit) the mint subject becomes '... for routed-commits REFUSED — ...'. That contradicts the comment that a failure prints nothing. The path is narrow (kit present but refusing), and the consequence is a malformed mint subject that the push leg would red anyway. | sound | - |
| 13 | seams | tools/memory-tree/kit.toml:324 | medium | medium | confirmed | The kit.toml `[[gate_leg]]` for `routed commits name a specced unit` (tools/memory-tree/kit.toml:324-329) has no `impure`. govkit.py:4080-4091 builds each target row from name, argv, subject, guard and doc_reads only. No kit.toml anywhere declares `impure`, and govkit never copies it. So only gov's tools/gate-legs.json:1008 marks the leg impure. In an adopter, run-gates.sh:2294 skips reuse only for impure legs. input_key (run-gates.sh:2196-2214) hashes argv, BASE and the tree fingerprint, with no HEAD or commit-message part. An amend that only rewrites the message therefore keeps the key, and a GATE_REUSE run reuses the green. Gov's own impure text names exactly this case. The damage is contained: pre-push never sets GATE_REUSE, so the authoritative run still executes the leg. | sound | two-answers-to-one-question |
| 14 | seams | tools/check-wiring.sh:1442 | low | low | confirmed | check-wiring.sh:1442 and :1519 call `matchers_of scratch-guard.js` with no event. Per matchers_of (:348-372), that reads every event's groups. So both of these count as 'the write gate is wired': the old `Bash\|PowerShell` PreToolUse group (this diff changed the fragment matcher from it) and the SubagentStart group. Under the old wiring no Edit or Write is gated, so 'every product write refuses' is untrue. The effect is only misleading advice. Check S separately flags the stale matcher, and once the adopter re-merges they need routing armed and the skill installed anyway. | unsound | decision-re-derived-by-a-second-process |
| 15 | seams | tools/memory-tree/.memory-tree.conf.example:451 | low | low | confirmed | tools/memory-tree/.memory-tree.conf.example:451 says the gate 'refuses an Edit, Write or shell write'. That contradicts scratch-guard.js:84 ('WHAT ESCAPES THE WRITE GATE — ... a Bash or PowerShell write') and the spec. Shell writes are never seen; only the push leg grades them. This is comment text with no effect on behaviour, but it misstates the guarantee to the adopter who edits this conf. | sound | two-answers-to-one-question |
| 16 | verification | tools/check-wiring.sh:1455 | high | medium | confirmed | check_routed (check-wiring.sh:1454) sources the conf with `${MEMORY_ROOT:-memory}`. The gate's checkUnarmed (scratch-guard.js:869) returns UNARMED on an absent MEMORY_ROOT and denies every write. The spec does this deliberately: TOOL-aRoutedQuill-2 §4 rejects 'Reading MEMORY_ROOT as memory when absent'. Yet the arm's header claims it grades 'by the rules the gate ... grade it by', and the fixture at check-wiring.test.sh:403 (no MEMORY_ROOT) expects `ok routed`. The hygiene engine hard-sets MEMORY_ROOT=memory and the kit declares a default, so such a conf is plausible, and check-wiring would certify as armed a conf under which every Edit/Write refuses. Graded medium rather than high: the scaffold writes MEMORY_ROOT, and the gate's own refusal names the exact cause. | unsound | two-guards-one-question-two-answers |
| 17 | verification | skills/session-kickoff/manifest-check.sh:469 | high | medium | confirmed | read_memory_root (manifest-check.sh:467-470) takes the first `^MEMORY_ROOT=` with sed. It does not match `export MEMORY_ROOT=...`, and it keeps an unquoted inline `# comment`. At the base this sed only fed the card's live line. This diff made check_card_route (:962) use it as well. With `export`, R0 exits 2 claiming there is no MEMORY_ROOT. With `MEMORY_ROOT=memory   # note`, dir becomes 'memory   # note/builds/<b>/' and R4 refuses every conforming route. The gate's readConfKey (scratch-guard.js:773) and tree_lib.parse_conf_line both accept these spellings, and tree_lib documents them as ones adopters write. The gate therefore reads the conf as armed and refuses product writes with a remedy (`--card --append`) that cannot succeed. Graded medium rather than high: it fails closed and loudly, and the conf can be fixed. | sound | two-guards-one-question-two-answers |
| 18 | verification | tools/hooks/scratch-guard.js:876 | medium | medium | confirmed | checkUnarmed tests only `checkUnderRoot(mem, c)` (scratch-guard.js:876), with checkUnderRoot at :213. routed_commits.py:151 uses `memory_root == bare or memory_root.startswith(bare + '/')`. check_routed (:1477) runs the same one-way test. An entry such as `memory/builds/` therefore passes all three as armed, though it gates every spec write. The first spec of a new build can then only be written under a route naming an already-buildable unit, which is the 'a spec would need a spec first' deadlock that spec S6 states as the rule's reason. No suite has an arm for an entry inside MEMORY_ROOT. The configuration is unusual and its refusals are loud, so the effect is contained. | sound | containment-tested-one-way |
| 19 | verification | tools/govkit/govkit.py:8664 | medium | medium | confirmed | The `update --write` block at govkit.py:8656-8690 (the gained list, the receipt mutation, add_deploy_kits and git add) and the settings-merge wiring branch at :10842 have no end-to-end arm. The only RQ5 AC4 arms in selftest.py (:5862-5906) call derive_default_gained with blob_at stubbed, and add_deploy_kits on a scratch deploy.toml. Nothing runs `update --write`, checks that the gained kits are installed or wired, or checks that a deliberate unwire stays unwired on a later update. The spec's arm row (spec-5 line 289) still says selftest.py covers AC4. A regression in that block would turn no leg red. No current wrong behaviour was shown, so the effect is contained. | sound | - |
| 20 | verification | tools/check-wiring.sh:1448 | low | low | confirmed | check-wiring.sh check_routed, no-conf branch: when the gate is wired and there is no .memory-tree.conf, it prints that 'every product write refuses'. scratch-guard.js checkRouted (:930-934) returns a witness on ENOENT, which admits the write, and the suite's own arm 'W-AC5 no conf at the target's toplevel -> allow, one witness line' pins that behaviour. The UNWIRED verdict is right and only the explanation is wrong. One small correction to the finding: the RQ5 AC7 needle only greps '.*no .memory-tree.conf', so the test does not assert the wrong clause. | sound | two-guards-one-question-two-answers |
| 21 | verification | tools/hooks/scratch-guard.js:757 | low | low | confirmed | The W-AC1/W-AC2 arms in scratch-guard.test.sh cover Tier-2 at INPROGRESS and SPECCED, Tier-1 at SPECCED (both sides of the cutoff and a blank cutoff), a missing spec, a spec outside the build folder, an H1 mismatch, and two-unit routes. No arm covers Tier-1 at INPROGRESS admitting, a spec with no Tier cell, an absolute or `..` spec path, a route with no `- build:` line, or a unit line with no spec. Nothing reaches the fail-closed catch at :1069-1073 either. Both regressions the finder names would leave the suite green. This is a coverage gap and changes no behaviour. | sound | - |
| 22 | verification | skills/session-kickoff/manifest-check.sh:959 | low | low | confirmed | check_card_route uses grep -c '^## route$' (manifest-check.sh:959) and awk /^## route$/ (:969), and the stale-route strip at :1054 uses /^## route$/ too. extractRouteUnits in scratch-guard.js strips backticks and trims each line before comparing it to '## route'. So a body whose heading is '## route ' (or carries leading whitespace) sets CARD_ROUTE=0: R0-R6 are skipped, the stored route is not stripped, and the gate still reads both sections. Impact is contained, because checkBuildable re-verifies each unit's spec file, H1, tier and status at write time. The worst outcome is a stale route's unit admitting a write, which the push leg still grades. | sound | two-guards-one-question-two-answers |
| 23 | intent | .memory-tree.conf:18 | blocker | blocker | confirmed | Reproduced at head ff0b3dc3 with GATE_PUSH_BASE unset: `python tools/memory-tree/routed_commits.py` prints 'routed-commits FAILED' naming 3d05f1ea, 4e49aeb5 and d31d7bc9 ('names no unit'), then exit=1. All three were committed on 2026-10-09, are ancestors of base 76b9c451, and are absent from ROUTED_COMMIT_WAIVED. gate-legs.json and kit.toml declare the leg 'routed commits name a specced unit' with guard [] and history_depth full, so it runs on every bar. Spec TOOL-aRoutedQuill-3 AC10 requires the WHOLE run over this repo to exit 0, and its Rollout says the landing commit waives every cutoff-day commit. The leg is new in this diff, so the diff introduced the defect. | sound | - |
| 24 | intent | tools/check-wiring.sh:1455 | medium | medium | confirmed | check_routed reads `${MEMORY_ROOT:-memory}`, so a conf with MEMORY_ROOT absent or blank reaches 'ok       routed'. scratch-guard.js checkUnarmed (:869) returns 'MEMORY_ROOT is blank or absent', so every write except the one to the conf is refused. Spec-2 S6 makes this behaviour deliberate, and its line 255 rejects defaulting to 'memory'. The arm's header claims it grades 'by the rules the gate and the ownership leg grade it by', but it matches only routed_commits.py, which defaults to 'memory'. The effect is contained: the gate's own refusal names the missing key, and adopter confs normally carry MEMORY_ROOT. | sound | sourced-conf-blank-overrides-the-default |
| 25 | intent | skills/session-kickoff/manifest-check.sh:469 | medium | medium | confirmed | read_memory_root (manifest-check.sh:467-470) is new in this diff; it does not exist at base. It runs `sed -n 's/^MEMORY_ROOT=[[:space:]]*//p' \| head -1 \| tr -d quotes`. That takes the FIRST bare assignment, rejects an `export` prefix (so the value is empty and R0 exits 2), and keeps an inline `# note`. R4 then builds dir = mr "/builds/" build "/" from that value, so with `MEMORY_ROOT=memory  # note` every unit fails the `is outside` test. readConfKey in scratch-guard.js:770 and tree_lib.parse_conf_line take the last assignment and accept export and inline comments. tree_lib.py:68-74 documents `MEMORY_ROOT=memory   # note` as a spelling adopters really write. On such a conf no route can land, so the gate refuses every product write. The effect is contained: it fails closed, the error message names the folder, and this repo's own conf is plain. | sound | two-readers-of-one-config-one-re-derived |
| 26 | intent | tools/hooks/scratch-guard.js:847 | medium | medium | confirmed | checkBuildable (scratch-guard.js:845-847) takes the first line that starts with '# ' and uses its raw first whitespace token. It strips no backticks or asterisks, removes no trailing ':', and is not fence-aware. KICK R4 (manifest-check.sh:989-994) skips fenced lines, strips backticks and asterisks and trailing :.,;, and accepts any unfenced H1. tree_lib.parse_spec_h1 matches ^#\s+[`*]*ID\b, so `TOOL-x-1:` passes there. So `# TOOL-x-1: title` or `# **TOOL-x-1** — title` gets a route through --card --append and is graded as specced by the push leg, but the gate refuses with `has H1 naming TOOL-x-1:`. No spec in this repo uses those spellings today (the grep found none), so the effect is contained to an adopter's spelling, and it fails closed. | sound | two-readers-of-one-config-one-re-derived |
| 27 | intent | tools/memory-tree/.memory-tree.conf.example:451 | low | low | confirmed | The ROUTED_PATHS paragraph is new in this diff. Line 451 says the gate refuses an Edit, Write or shell write. scratch-guard gates only WRITE_TOOLS (Edit/Write/MultiEdit/NotebookEdit). By design a Bash or PowerShell write passes, and the push leg is the guarantee. The documentation misstates the gate's reach, but no behaviour changes. | sound | - |
| 28 | intent | memory/builds/aRoutedQuill/README.md:67 | low | low | confirmed | README.md:67, inside the hand-kept roster:units region, shows PLAY-aRoutedQuill-1 as INPROGRESS. Its spec status header (line 3) and the generated build-index row (README.md:85) both say CLOSED rev-4. The document contradicts itself, but no gate reads the roster. | sound | - |

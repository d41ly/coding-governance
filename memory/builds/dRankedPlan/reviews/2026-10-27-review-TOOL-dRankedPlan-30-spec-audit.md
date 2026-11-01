**Serves:** spec-audit TOOL-dRankedPlan-34@rev-1 TOOL-dRankedPlan-35@rev-1 TOOL-dRankedPlan-30@rev-1 TOOL-dRankedPlan-31@rev-1 TOOL-dRankedPlan-32@rev-1 TOOL-dRankedPlan-36@rev-1 TOOL-dRankedPlan-33@rev-1 TOOL-dRankedPlan-37@rev-1

# Tier-2 spec audit — dRankedPlan, the round-2 audit promotions, units 30 to 37 (round 1)

Provenance: a Tier-2 adversarial review of the eight specs that the second spec audit promoted. The finders were gov-spec-reviewer on five lenses, the skeptic batches were gov-skeptic, and the synthesis was gov-synthesizer. The build's purpose is taken from memory/builds/dRankedPlan/README.md and its run mandate.

Reviewed: memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-34.md@cbb8fca98f6c966a4747a820afb0e22d49eb85fc, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-35.md@111400b72bf46eb659d26aa0ffa05c31cadc737f, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-30.md@54f1586bfecfbdf41667c226a7ab98c884b9de61, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-31.md@70a9e5b365ebb31faa2134fb0fd06148611d4511, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md@db14f40e67fb38875c6b352d76ea25dbf4fbf3d6, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-36.md@b0a8ddc2e046f1e57b407e735c8f75d1044bfa54, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-33.md@69bc3d9bcdb09c76a4f089560f7eab5cfcebbd26, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md@2cb1c49bae09b5e5c2b783baea118997e6211298

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers. Seven high findings stand, grouped into six items, and each one is a spec edit whose fix the skeptic either judged sound or corrected. The specs should not go to build until items H1 to H6 are folded in. Three of the six items concern unit 32's caller reader: H1, H2 and H3 each let a hook or shell caller of the session predicate pass the always-run leg.

## Review shape

Review shape: intensity full, raw 42, confirmed 39, refuted 3, unverified 0 (0 uncertain), precision 0.93.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 11 | 10 | 1 | 0 | 0 | 0.91 |
| reuse | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 9 | 8 | 1 | 0 | 0 | 0.89 |
| failure-envelope | yes | 10 | 9 | 1 | 0 | 0 | 0.90 |

By item, the adjudicated tally is 33 items: 0 blocker, 6 high, 18 medium and 9 low.

By raw confirmed finding, the tally is 39: 0 blocker, 7 high, 23 medium and 9 low.

Merges only join findings that share a binding grade. Two defects were found at two binding grades, so their items stay separate and point to each other: the unspecified shlex error (H3 at high, M7 at medium) and the unread `.githooks/*.py` file (M8 at medium, L9 at low).

The three refuted findings (8, 26, 38) do not appear in the body, only in the appendix.

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified.
- Discards: 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 35 judged sound, 4 judged UNSOUND (ids 9, 20, 23 and 36; the skeptic's corrected fixes are written below), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 4 RE-GRADED by the skeptic (ids 9, 12, 23 and 35).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 28 spec documents were supplied as `specs`, as sibling context.
- Checklist: 49 items, each assigned to exactly one of 5 lenses (coherence 10, grounding 10, reuse 10, blast-radius 10, failure-envelope 9).
- By design: 1 invariant from the checklist's by-design block.
- Move check: no checked subject moved.

Every count above is clean, so the run is complete on its own terms.

## High

### H1 — Unit 32 drops the textual caller rule that units 22, 30 and 31 plant against (id 1)

- **Where:** TOOL-dRankedPlan-32 §2 S2, S5, against TOOL-dRankedPlan-31 S4/AC3, TOOL-dRankedPlan-30 S3/AC2 and TOOL-dRankedPlan-22 S3.
- **What:** S5 supersedes unit 22's definition of a caller. Under S2, a shell or `.githooks/` file is a caller only when it invokes `ratify.py`. A `read_plan_ratification(` line in a hook no longer counts as a caller, and the in-process forms (`python -c`, a heredoc) are read by neither reader.
- **Consequence:** Unit 31 AC3 (a `read_plan_ratification(` call in `.githooks/pre-commit` exits 1) cannot pass. The `caller-guard` plant and unit 30 AC2 go green because they find nothing. A hook that calls the predicate in-process passes the always-on leg, so that leg certifies an absence over a class it does not read.
- **Fix (skeptic judged it SOUND):** In S2, keep unit 22's rule for shell and `.githooks/` files beside the invocation rule: a code line matching `\bread_plan_ratification\s*\(` (or any non-comment line naming `read_plan_ratification`) is a caller. Add a plant `caller-hook-inline` whose `.githooks/pre-commit` runs `"$py" -c 'from ratify import read_plan_ratification; ...'`, and require it to be refused. The alternative is to respell unit 31 S4/AC3 and the caller-guard plant in an invocation form, and to name the in-process hook form in unit 32 §3 as unread.
- **Left-shift gate:** A spec-token check: when a spec supersedes another unit's definition, every AC or plant in a sibling spec that cites the old definition's shape is listed and re-pinned in the same edit.

### H2 — A command led by a shell keyword or prefix is never read as an invocation (ids 2, 34)

- **Where:** TOOL-dRankedPlan-32 §2 S2; §5 security.
- **What:** S2 reads a command's first word after stripping only `NAME=value` words. As a result, `if ! "$py" "$d/ratify.py" "$slug"; then`, `if "$py" ...`, `exec "$py" "$d/ratify.py" "$@"` and a case arm `--x) exec "$py" ...` are not invocations. The tree already uses every one of these shapes (tools/lexicon/adopt-lexicon.sh:423, tools/memory-tree/merge-rows.sh:60, tools/run-gates/run-gates.sh:224). §5's claim that "every unread form is named in §3" is false.
- **Consequence:** The likeliest hook spelling, a guarded or wrapping call to the predicate's CLI, passes the deny-by-default ban that units 31 and 37 S9 rely on. No plant observes it.
- **Fix (skeptic judged it SOUND, both findings):** Strip leading reserved words and prefix builtins before reading the command word: `if`, `then`, `elif`, `else`, `while`, `until`, `do`, `!`, `exec`, `command`, `time`, `env`, `nohup`, and a case pattern ending `)`. The alternative is to judge any later interpreter word that is followed by a word ending `ratify.py`. Add plants `caller-shell-if` (`if ! "$py" "$d/ratify.py" "$slug"; then`) and `caller-shell-exec` (`exec "$py" "$d/ratify.py" "$@"`), each refused. Correct §5's claim.
- **Left-shift gate:** A bug-class checklist entry: a shell-command reader owes a plant for every compound-command prefix the tree's own `*.sh` files use.

### H3 — A shlex error on a split piece has no rule (id 33)

- **Where:** TOOL-dRankedPlan-32 §2 S2; §4 "The probe over the tree"; §5 error states.
- **What:** S2 splits at `;`, `|`, `$(`, a backtick and `(`, then calls `shlex.split`. Splitting at `$(` inside a quoted argument leaves an open quote, and about one piece in six on the real tree raises ValueError (`ok 74 err 14` for gen_build_index.py, `ok 12 err 2` for drift_report.py). Neither S2 nor §5 says what happens next.
- **Consequence:** Built as written, `--check-callers` either crashes on the real tree, which reds unit 31's unguarded leg on every bar, or skips the piece and fails open. The second path lets the natural hook shape `"$py" "$d/ratify.py" "$(...)"` pass unseen. The §4 probe table records no error count.
- **Fix (skeptic judged it SOUND):** State the rule for a piece shlex cannot split. Either fall back to a POSIX-quote-aware tokenizer that tolerates an open quote, or refuse the file closed: exit 2 naming the file and line, or count the piece as a caller when it names `ratify.py`. Add an error count to the §4 probe table. Add a plant whose invocation line also carries a quoted `"$(…)"` and an apostrophe, and require it to be refused.
- **Left-shift gate:** A checklist entry: every parser call in a deny-by-default check owes a stated error rule and a probe-table error column.
- **See also:** M7 (id 13), the same gap at medium.

### H4 — AC19's CLI half exercises the drive-letter rule, not `~` (id 10)

- **Where:** TOOL-dRankedPlan-37 §6 AC19.
- **What:** `gen_build_index.py --asks --path ~/x` is unquoted, so bash expands the tilde and MSYS rewrites it to `C:/Users/daily-agent/x`. It already refuses at base through the drive-letter rule. The quoted `'~/x'` exits 0 at base, which is the real defect S23 closes, and AC19 never runs it.
- **Consequence:** AC19 would go green even if `read_asks_args` were never routed through `check_repo_relative_path`.
- **Fix (skeptic judged it SOUND):** Spell the argument quoted, `--path '~/x'`, and pin that it exits 2 naming `~`. Add a red case: at base, `--path '~/x'` exits 0.
- **Left-shift gate:** A spec-token check that flags an unquoted `~` or glob character in an AC's command line.

### H5 — `--follow` dates a fresh near-copy disposition to the older record's add (id 19)

- **Where:** TOOL-dRankedPlan-34 §2 S1; §4 "The date after this unit", row "added after T".
- **What:** S1 reuses `git log --follow --diff-filter=A` but drops that seam's documented caveat (tools/unattended/lib-unattended.sh:1725-1727) that `--follow` also follows copies. A second disposition record shares the first record's fields form, so it is dated to the first record's add, which lies before T.
- **Consequence:** The owner's fresh `terminal` record is not kept, and the re-entry never releases. AC3's "exits 0 once a second `terminal` record is committed" fails, and so does every disposition reader built on units 24, 25 and 26. The failure is closed (a false hold).
- **Fix (skeptic judged it SOUND):** Follow renames only, never copies. Read `git log -M --name-status --format=%H -- <build>/build/` once and walk the `R` lines back from the record's path to its oldest `A`; without `-C` that log reports a copy as a plain `A`. Add a `reader-bound` case `copied-fresh`, a near-copy of a pre-T record committed after T, which must be kept. Cite lib-unattended.sh:1725 in §4.
- **Left-shift gate:** A checklist entry: a spec that reuses a seam carries the seam's documented caveats into its own table.
- **See also:** M15 (id 36), the same `--follow` similarity behaviour for a replace-in-one-commit.

### H6 — Dormancy's cross-item "newest" pick stays unordered (id 22)

- **Where:** TOOL-dRankedPlan-35 §3 Non-goals (dormancy bullet); §2 S1.
- **What:** S1 orders kept records only within one item. Unit 24 S4's `read_build_disposition` asks once per item of its three moves and "takes the newest answer", and no spec in the set redefines that pick. §3 nevertheless says dispose "reads the same answer through the reader it is built on".
- **Consequence:** Two merged dispositions for different moves, written on two machines, reach a pick with no ancestry order and no conflict hold. `write_transition` then records the move that code order chooses. That is the defect unit 35 closes, still open on its one other reader, and the "newest" rule ends up spelled twice.
- **Fix (skeptic judged it SOUND):** Have unit 4's `read_build_disposition` pass the union of the three items' kept records to `derive_newest_disposition`, with the conflict test over the `(Item, Disposition)` pair, so that cross-item disagreement holds with `disposition conflict <paths>`. Name this in S1 as superseding unit 24 S4's "taking the newest answer". Add a `reader-bound` or dispose plant with two merged-side records for two different moves.
- **Left-shift gate:** A checklist entry: a reader that defines an order lists every caller that picks across its answers.

## Medium

### M1 — Caller paths fail `relative_to(root)` under an 8.3 or other differing spelling (ids 9, 35)

- **Where:** TOOL-dRankedPlan-30 §2 S2; §4 "The derivation".
- **What:** The derivation builds paths with `Path(__file__).absolute()` and `resolve_kit_dir`, neither of which resolves the path, and keeps a path only if the lexical `relative_to(root)` succeeds. Root's source is never stated. On this machine `%TEMP%` is `DAILY-~1`, while `git rev-parse --show-toplevel` prints the long form.
- **Consequence:** In every scratch repository under a short `%TEMP%` path, the kit's own `ratify.py` and the planted `triage.py` are refused as undeclared callers. This affects unit 31 AC3, unit 37 AC5, `caller-guard-prefix` and `foreign-prefix parity`. It is a false red on Windows that CI on Linux does not show, and it fails closed. The skeptics graded both findings medium; the finders had graded them high.
- **Fix (id 9: the finder's fix was judged UNSOUND, and the skeptic's corrected fix follows; id 35: judged SOUND):** Get each derived path's repo-relative form from git: run `git -C <root> ls-files --full-name -- <path>`, which normalises the 8.3 and long forms itself, and keep the entry only when it prints one line. State in S2 that root is the directory `--root` names, or the cwd's git toplevel otherwise. Add `fixture: a scratch repository under a short %TEMP% path` to AC2. Add a `caller-guard-prefix` case that runs the check with `--root` in its 8.3 or other spelling and requires the kit's own module to be admitted. Id 35's skeptic judged canonical-form comparison (`os.path.normcase(os.path.realpath(...))` on both sides) sound, while id 9's skeptic rejected that route in favour of git. The git route satisfies both findings.
- **Left-shift gate:** A gotcha-checklist entry: a path comparison across a git-reported and a Python-derived path goes through git or through realpath on both sides.

### M2 — A variable-bound argv path is not read as a caller (id 3)

- **Where:** TOOL-dRankedPlan-32 §2 S1 (argv list).
- **What:** An argv element counts as a caller only when it holds a `str` constant ending `ratify.py`. The repository's own idiom, `CLI = HERE / "ratify.py"` with `[sys.executable, str(CLI), slug]` (tools/branch-reconcile/selftest.py:28, :121), is not read as a caller.
- **Consequence:** This is a fail-open on a form the tree already uses. The §4 probe covered only two analogues.
- **Fix (skeptic judged it SOUND):** Resolve a `Name` or `Attribute` element through the file's module-level and function-local assignments whose value holds a `str` constant ending `ratify.py`. The alternative is to name the form in §3 as unread. Add a plant `caller-argv-bound`, refused.
- **Left-shift gate:** A checklist entry: an AST caller reader owes a plant for the tree's bound-constant call idiom.

### M3 — Unit 30 AC1 counts a file that does not exist until order 10 (id 4)

- **Where:** TOOL-dRankedPlan-30 §6 AC1, against the build order.
- **What:** AC1 requires `derive_predicate_callers` to return exactly two tracked paths, one of them `tools/memory-tree/triage.py`. Unit 30 is at order 7, but unit 3 creates that file at order 10, and by S2 an unresolved anchor yields no path.
- **Consequence:** At unit 30's tip a correct build returns one path, so AC1 cannot pass. A builder either fails the unit or weakens the deny-by-default skip.
- **Fix (skeptic judged it SOUND):** Restate AC1 for order 7: the set holds exactly the tracked `tools/loop/ratify.py`, and the triage anchor raises `LookupError` and adds nothing. Move the two-path observation to TOOL-dRankedPlan-37's tip (order 18), or plant `triage.py` in a scratch repository.
- **Left-shift gate:** A spec-token check that an AC's named repository paths exist at or before the unit's build order.

### M4 — Unit 33 S2 exempts three plants from the only kit copy its table gives them (id 5)

- **Where:** TOOL-dRankedPlan-33 §2 S2, against §4 "The base after this unit" and §6 AC4.
- **What:** S2 exempts `plan-record-absent`, `plan-record-unread` and `plan-record-open-probe` from the seed, and the seed is the only step that copies the memory-tree kit. The §4 table nevertheless gives two of them a copied kit and gives `plan-record-unread` "the seed".
- **Consequence:** Built as S2 reads, `plan-record-absent` answers `unread`, so AC4's `unwitnessed` cannot pass, and `plan-record-open-probe` misses its refusal.
- **Fix (skeptic judged it SOUND):** Seed every plant, then have `plan-record-absent` remove the seeded record, `plan-record-unread` remove the copied kit, and `plan-record-open-probe` replace the record with its eleven-field one. The alternative is to split S1 into a kit copy every plant takes and a record write the three skip. Either way, make the table match.
- **Left-shift gate:** A checklist entry: a spec's per-plant state table and its scope items name each plant's state from one source.

### M5 — Unit 31's new leg misses its ceiling-evidence row, its descriptor ceiling and the meta-gates it trips (ids 6, 24)

- **Where:** TOOL-dRankedPlan-31 §2 S1, S2; §4 Files touched; §7 leg line.
- **What:** S2 owes a `tools/run-gates/ceiling-evidence.txt` row and a `memory/map/features/loop.md` dossier claim, but Files touched omits ceiling-evidence.txt. S1 spells the gate-legs.json row with no `ceiling`, while S2 puts the ceiling "in the descriptor". §7 omits `govkit selfcheck` (the unguarded leg that joins `[[gate_leg]]` against the manifest and subject-pins), `codebase-map coverage + freshness` and `leg ceilings clear their evidenced maximum`, and lists only the held `govkit selftest`.
- **Consequence:** The pass's own verification never runs the meta-gates that grade the new leg, so a missing claim or a descriptor/manifest disagreement first shows at the close's bar. The ceiling's home is left to the builder. Audit item M13 recorded the same omission against unit 15.
- **Fix (skeptic judged it SOUND, both findings):** Add `tools/run-gates/ceiling-evidence.txt` (written by `derive-ceilings.py --write`) to Files touched. Add `govkit selfcheck`, `codebase-map coverage + freshness` and `leg ceilings clear their evidenced maximum` to §7. In S1, give the gate-legs.json row a `ceiling` field, as `review-join ban (no ref-keyed join)` carries `"ceiling": 300`. Extend AC1 to read the ceiling field and the dossier claim. Have the close run the full bar with GATE_FULL=1.
- **Left-shift gate:** A spec-token check: a spec whose Files touched names `tools/gate-legs.json` must name ceiling-evidence.txt and the three meta-gate legs on §7.

### M6 — The seed's conf declares no family for the id it mints (id 11)

- **Where:** TOOL-dRankedPlan-33 §2 S1.
- **What:** The seed copies `.memory-tree.conf.example`, whose FAMILIES has no `TOOL`, and then mints `TOOL-<slug>-1`. The id grammar's alternation is derived from FAMILIES (tree_lib.py:416-418).
- **Consequence:** `**Serves:** plan TOOL-tFix-1` does not bind. S1's assertion raises at the fixture base, and every `plan.exit` plant of units 10, 21, 25 and 26, plus unit 10 AC8's driver fixture, stays red. The tempting repair is the precondition bypass §4 rejects.
- **Fix (skeptic judged it SOUND):** Have the seed write a conf whose FAMILIES declares the family it mints (append `tooling:TOOL` and its stream), or derive the family from the scratch conf. State which conf keys the seed sets.
- **Left-shift gate:** A fixture selftest that asserts the seeded record's Serves line binds under the seeded conf.

### M7 — Unit 32's shell reader has no rule for unparseable lines (id 13)

- **Where:** TOOL-dRankedPlan-32 §2 S2 (shell reading).
- **What:** S2 applies `shlex.split` to every joined line, with no prefilter. Over the named population, about 6190 lines in 147 files raise ValueError, and no rule says what happens then.
- **Consequence:** A crash reds unit 31's always-run leg, and a silent skip fails open on a `ratify.py` invocation inside a multi-line string. Nothing is missed at base, since no erroring line names ratify.py today.
- **Fix (skeptic judged it SOUND):** Apply S2 only to lines naming `ratify.py` (a textual prefilter, as S1 has), and treat a shlex error on such a line as a refusal naming file and line. Add a plant whose hook line carries an unbalanced quote across lines.
- **Left-shift gate:** As for H3.
- **See also:** H3 (id 33), the same gap at high.

### M8 — `.githooks/*.py` and heredoc Python are read by neither reader, and §5 says no such form exists (id 14)

- **Where:** TOOL-dRankedPlan-32 §2 S2, S5; §5 security.
- **What:** S2 sends every file under `.githooks/` to the shell reader, including the Python file `.githooks/pre_push_bar_selftest.py`. S5 does not say how a file's kind is decided. A heredoc'd Python `read_plan_ratification` reference inside a `.sh` file is read by neither reader, yet §5 claims "every unread form is named in §3", and §4:126 and §5:165 claim that heredoc lines fail closed.
- **Consequence:** A Python argv call in `.githooks/*.py` read as shell, or a heredoc'd predicate call, passes the always-run leg. This is a fail-open the spec says does not exist.
- **Fix (skeptic judged it SOUND):** In S5, decide a file's kind by extension first, so `*.py` anywhere, `.githooks/` included, goes to the Python reader. Either read heredoc bodies fed to a python interpreter with S1, or name the heredoc form in §3 as unread.
- **Left-shift gate:** A checklist entry: a "no unread form" claim is backed by a table that lists each population file kind and its reader.
- **See also:** L9 (id 42), the dispatch-order gap at low.

### M9 — AC16's `grep -c "697"` cannot reach 0 as S19 and S20 scope it (ids 15, 29)

- **Where:** TOOL-dRankedPlan-37 §2 S19, S20; §4 "L1"; §6 AC16.
- **What:** S19 and S20 cite unit 16's 697s at :149 and :248, which are now at :151 and :250. A third copy sits at :136, unit 16's hands-off edge ("whose figure 697 that unit corrects to 695"), and no item edits it.
- **Consequence:** Built as scoped, the grep prints 1, and the §9 line S19 asks for ("697 to 695") adds another hit. The builder either edits an unlisted line or weakens the grep.
- **Fix (skeptic judged it SOUND, both findings):** Cite lines by content, not number. Have S19 name unit 16's §3 hands-off line and its rev-bump §9 line, spelled without the old figure (e.g. "corrects the population figure to 695"). Or restate AC16 as a count of 697 on the §4 and §5 lines only.
- **Left-shift gate:** A spec-token check that refuses a `:<line>` citation into another spec and asks for a content anchor instead.

### M10 — Unit 31's Rollout states a one-pass red window that runs from order 13 to 17 (ids 16, 25, 41)

- **Where:** TOOL-dRankedPlan-31 §4 Rollout.
- **What:** The Rollout says the leg reds on `plan_revision.py` "from order 13 … until order 14". Unit 23 (order 14) removes only one plant's stub. Unit 15 S6's other stubs stay, unit 29 S32 (order 17) adds one, and only unit 37 S3 to S5 (order 18) remove them all, as its S9 says.
- **Consequence:** The unguarded leg is red, in remote CI too, on every pass tip from 13 to 17. A builder who trusts the stated window reads the red as a regression and may widen the allowlist or weaken the predicate.
- **Fix (skeptic judged it SOUND, all three findings):** Restate the Rollout: the leg reds from order 13 (unit 15 S6's stubs), stays red through order 17 (unit 29 S32's stub), and reads green from order 18, when TOOL-dRankedPlan-37 S3 to S5 de-stub every plant. Cite unit 37 S9 as the owner of the green observation. Id 25's alternative of building unit 15's plants with explicit `ratification=` values would not keep the leg green at 13 on its own, because unit 15 S5's own call in `show` is already a caller.
- **Left-shift gate:** A checklist entry: a stated red window names the unit and scope item that closes it, and is checked against every scope item that adds or removes its cause.

### M11 — Unit 32 hand-rolls a shell and a JS tokenizer that the lexicon kit already ships (id 20)

- **Where:** TOOL-dRankedPlan-32 §2 S2, S3; §10 Reuse audit.
- **What:** S2 builds line joining, splitting and `shlex.split`, and S3 builds a JS array-literal scanner. `scan_shell_tokens` (tools/lexicon/lexicon.py:469) already tracks quotes, `$'…'`, continuations, `$(…)`, heredocs and here-strings. `scan_ts_tokens` (:950) already emits `[ ] ,`. Both are already imported across kits through resolve_kit_dir. §10 dismisses only `parse_shell_defs`.
- **Consequence:** The build ships a second, weaker tokenizer per language, which keeps the heredoc miss class §4 admits and can drift from the tokenizer the lexicon and codebase-map kits are tested against. The heredoc miss fails closed.
- **Fix (the finder's fix was judged UNSOUND; the skeptic's corrected fix follows):** Extend `scan_shell_tokens` behind an opt-in parameter (for example `seps=True`), so that `parse_shell_defs` and every current caller get an unchanged token stream. In that mode, emit `;` `&&` `||` `|` `(` and the opening of `$(` and of a backtick span as op tokens, and tokenize backtick spans as code rather than as one opaque span. Catch its SyntaxError as the check's exit 2. Read array literals from `scan_ts_tokens`. Add a heredoc plant to S6.
- **Left-shift gate:** A reuse-audit checklist entry: a spec that adds a tokenizer names the tree's existing tokenizer for that language and why it is or is not extended.

### M12 — §7 cannot name `loop selftest` yet, and the guards arm will red once it lands (id 27)

- **Where:** TOOL-dRankedPlan-30 §7 leg line, and the same in units 31 to 37.
- **What:** Every subject spec whose Files touched names a file under tools/loop/ omits `loop selftest`. That leg's guard is `{prefix}/loop/` (TOOL-dDeclaredLoop-75 S21), and it is the only leg that runs these specs' new fixture arms. SPEC_GUARD_LEGS_CUTOFF=2026-09-22 arms the spec-tokens guards check (tools/check-spec-tokens.py:1609-1622). It cannot be named today, because a §7 token absent from gate-legs.json is itself a hit (:1546-1547).
- **Consequence:** Once dDeclaredLoop lands the loop legs, all eight specs trip spec-tokens. In each pass, builders never run the one leg that executes their arms.
- **Fix (skeptic judged it SOUND):** At the build run's start, once the loop legs exist in the manifest, re-pin each spec's §7 to name `loop selftest` and every other `{prefix}/loop/`-guarded leg that `check-spec-tokens.py --legs-for` returns. Until then, state in §7 prose that the leg is owed and graded at the build.
- **Left-shift gate:** The build-run preflight runs `check-spec-tokens.py` against the manifest as it will stand at each pass, not only at HEAD.

### M13 — Unit 37 S13's guards miss sibling-kit files the suites read, and AC11 is false at base (id 28)

- **Where:** TOOL-dRankedPlan-37 §2 S13; §6 AC11.
- **What:** `build-index selftest` writes moves through `write_transition` (tools/loop/loop_transition.py) but gains only `{prefix}/loop/ratify.py`. `loop selftest` copies the whole memory-tree kit and runs gov_record.py, plan_record.py and the conf example over tree_lib.py, but gains only plan_record.py and plan_fields.py. AC11's "each kit's [[gate_leg]] entry carries the same guard" is already false: tools/memory-tree/kit.toml:277-280 spells `{kit}/`, while gate-legs.json:482-486 spells three entries.
- **Consequence:** An edit to loop_transition.py, gov_record.py or tree_lib.py (which S23 edits) skips the suite that reads it, and AC11 is red before the unit starts.
- **Fix (skeptic judged it SOUND):** Widen `build-index selftest` to `{prefix}/loop/` and `loop selftest` to `{prefix}/memory-tree/`, or to every file the seed and plants import or copy, derived by reading the imports. Restate AC11 as "the manifest guard holds the added entries, and the descriptor guard holds the same added entries beside its `{kit}/`", or name the descriptor rewrite and its adopter render in Files touched.
- **Left-shift gate:** A govkit check comparing each descriptor guard with its manifest guard (govkit.py:2604 says none exists).

### M14 — Unit 36 changes `derive_step_scenarios`'s contract without naming its caller (id 30)

- **Where:** TOOL-dRankedPlan-36 §2 S2; §4 Files touched.
- **What:** S2 passes the pending move's own `scenario` field as `pin=`. The specced signature is `derive_step_scenarios(build)`, called from tools/loop/loop_transition.py before `write_transition` writes, so the field is not yet on disk. Files touched lists only tools/loop/scenario.py.
- **Consequence:** Building S2 forces a signature and call-site change in loop_transition.py. That is a write outside the declared set, its guarded legs go unnamed, and dDeclaredLoop-27's caller meets an unannounced contract change.
- **Fix (skeptic judged it SOUND):** Name `tools/loop/loop_transition.py` in Files touched, spell the new signature (e.g. `derive_step_scenarios(build, move_fields=None)`), and add a consumes-from edge on TOOL-dDeclaredLoop-27's caller.
- **Left-shift gate:** A checklist entry: a scope item that adds an input to a function names its signature and every call site.

### M15 — A fresh disposition added in the commit that deletes a similar stale one is dated before T (id 36)

- **Where:** TOOL-dRankedPlan-34 §2 S1; §5 risks.
- **What:** `--follow` pairs a deleted path and an added path by similarity, so a fresh record added in the same commit that removes a templated stale record is followed back to the stale add. §5 prices only the >50% rewrite case.
- **Consequence:** A natural owner act is silently ignored, and the gate holds with "no fresh record". The failure is closed.
- **Fix (the finder's fix was judged UNSOUND; the skeptic's corrected fix follows):** Add a §4 row: "stale record deleted and a similar fresh record added in one commit after T: dated by the stale add, not kept". State that git records no rename, so this history matches a `git mv`. The hold line names the stale record and tells the owner to add the fresh record in a commit that does not delete the stale one. Add a `reader-bound` case `replaced-in-one-commit` pinning "not kept".
- **Left-shift gate:** As for H5.
- **See also:** H5 (id 19).

### M16 — `ratify.py --fixture --seed <dir>` is an unvalidated write path (id 37)

- **Where:** TOOL-dRankedPlan-33 §2 S1 (`--seed`); §5 security.
- **What:** Against any directory, the seed copies a kit in, replaces `.memory-tree.conf` and commits a plan record. Nothing validates `<dir>`, and nothing says what happens to an existing conf, kit copy or record. unattended.test.sh fixtures already write their own `.memory-tree.conf` (e.g. :2537, :6521). §5 calls this "no new write path".
- **Consequence:** A mistyped path or `.` commits into a real repository and overwrites its conf, and existing fixture state is handled however the builder guesses.
- **Fix (skeptic judged it SOUND):** Refuse a `<dir>` that is the repository holding `ratify.py`, or that lacks a fixture marker the fixture builders write. Refuse, or explicitly keep, an existing `.memory-tree.conf`, memory-tree kit copy or plan record for the slug, and name the choice. Add a refusal plant that points `--seed` at a non-fixture repository.
- **Left-shift gate:** A TEMPLATE-SPEC checklist entry: every new `--write`-like flag in a shipped kit names its target validation and its existing-state rule.

### M17 — A first move with an absent or empty `scenario` field restores exit 2 (id 39)

- **Where:** TOOL-dRankedPlan-36 §2 S1, S2.
- **What:** S2 passes the move's `scenario` field as `pin=`, but that field is written through the optional `--field` (dDeclaredLoop-27 S8), so it can be absent or empty. Then `pin=None` brings back the exit 2 this unit exists to remove.
- **Consequence:** Unit 14 S3 reads exit 2 as a refusal that stops the move, so the build cannot start. This is the H6 defect of the earlier audit, on the absent-field input class.
- **Fix (skeptic judged it SOUND):** Refuse an absent or empty field on a first move with exit 1 and a line naming the missing `scenario=` field, never exit 2. Or make the claim's `scenarios` required non-empty and cite the rule. Add a plant `plan-first-no-field` with a pinned answer.
- **Left-shift gate:** A checklist entry: every optional field a reader consumes owes an absent-field and an empty-field case.

### M18 — The shared `check_repo_relative_path` never names the backslash fold (id 40)

- **Where:** TOOL-dRankedPlan-37 §2 S23; §6 AC19.
- **What:** The helper is specified by four forward-slash shapes. Both existing copies fold `\` to `/` at the caller (routed_commits.py:155, gen_build_index.py:3339), and the new `Scope` caller has no fold. AC19 probes only forward-slash shapes.
- **Consequence:** On this Windows-first repo, `\abs`, `a\..\b` and `\\server\x` pass through any caller that does not fold, the three callers disagree, and AC19 cannot see it.
- **Fix (skeptic judged it SOUND):** Make the helper fold `\` to `/` itself and refuse empty, `\`-led and UNC values. Add `\abs`, `a\..\b` and `\\srv\x` to AC19's probe list.
- **Left-shift gate:** A checklist entry: a helper extracted from callers absorbs each caller's input normalisation, and its AC probes the pre-normalised forms.

## Low

### L1 — `merged-sides` never says its two branch records carry different words (id 7)

- **Where:** TOOL-dRankedPlan-35 §2 S3; §6 AC2.
- **What:** AC2 expects `None` with `disposition conflict` before the third record, but S3 names no Disposition words. By S1, two unranked records that carry the same word return no conflict.
- **Consequence:** A builder who uses one word builds a correct reader whose AC2 reds. The gap is limited to the plant and can be inferred from AC3.
- **Fix (skeptic judged it SOUND):** In S3, state that the branch records carry different words, a deferral on one and `continue` on the other, and that the third carries a releasing word.
- **Left-shift gate:** A checklist entry: a plant whose AC pins a conflict names the conflicting values.

### L2 — The unranked clause uses a reflexive ancestry test (id 12)

- **Where:** TOOL-dRankedPlan-35 §2 S1.
- **What:** The unranked records are defined as "no other record's ancestor" by `git merge-base --is-ancestor`, which exits 0 for X X. Read literally, records sharing one adding commit are each other's ancestors, and the unranked set is empty. The governing clause already says "proper", which is why the skeptic graded this low (the finder had graded it medium).
- **Consequence:** A wording gap that the AC1 plant would catch in the build.
- **Fix (skeptic judged it SOUND):** Define proper ancestry as `a != b and merge-base --is-ancestor a b`, and state that records sharing one adding commit are mutually unranked.
- **Left-shift gate:** None fits. Add a checklist entry: git primitives quoted in a spec carry their reflexivity.

### L3 — AC4's single `grep -c` cannot show both driver shapes (id 17)

- **Where:** TOOL-dRankedPlan-32 §6 AC4.
- **What:** One whole-file `grep -c "ratify.py" tools/unattended/unattended.sh` ≥ 1 stands as evidence for both the resolver line and the `--exit` call.
- **Consequence:** A missing `--exit` arm goes unseen in the evidence. The real `--check-callers` run still covers the tree.
- **Fix (skeptic judged it SOUND):** Grep each shape on its own: one matching `resolve_kit_dir .* loop ratify.py` and one matching `ratify.py" .*--exit`, each ≥ 1.
- **Left-shift gate:** A spec-token check that flags one whole-file count cited as evidence for more than one shape.

### L4 — S25 calls a staged-only record untracked (id 18)

- **Where:** TOOL-dRankedPlan-37 §2 S25.
- **What:** A staged-only file appears in `git ls-files`, so it falls into the "has no adding commit" branch, not "not committed".
- **Consequence:** The gate fails closed either way. Only the why-line changes, and AC21's plant is ambiguous.
- **Fix (skeptic judged it SOUND):** Define "not committed" as absent from `git ls-files`, or present with no adding commit at HEAD, and print `not committed` for both. Pin the AC21 plant as one staged and one untracked case.
- **Left-shift gate:** A checklist entry: a git-dated record owes a staged-only and an untracked case.

### L5 — §10 cites as reused the rule the unit replaces (id 21)

- **Where:** TOOL-dRankedPlan-32 §10 Reuse audit.
- **What:** §10 says "The rule reused is the code-line rule of `tools/workflows/check-review-join.sh`", but §2 replaces that textual rule with `ast` and `shlex`, and §4 rejects a regex.
- **Consequence:** A later change could restore the textual rule in the belief that it follows this unit. Behaviour is unaffected.
- **Fix (skeptic judged it SOUND):** Restate §10 to say that this unit supersedes the check-review-join.sh code-line rule that unit 22 S2 cited, and name the seam it does extend (see M11).
- **Left-shift gate:** None fits. Add a checklist entry: §10's reused seams match §2's mechanism.

### L6 — Unit 31 §7 omits the leg it creates and the selftest it edits (id 23)

- **Where:** TOOL-dRankedPlan-31 §7 Gates.
- **What:** S1 adds `session-predicate callers (asked only at the act)` and S3 edits tools/loop/selftest.py, yet §7 names neither that leg nor `loop selftest`. The skeptic graded this low (the finder had graded it medium): the New arm line names the leg in prose, the leg is unguarded, and the close's bar reads it.
- **Consequence:** The pass's named gates can be green while its own new leg reds.
- **Fix (the finder's fix was judged UNSOUND; the skeptic's corrected fix follows):** State in §7 prose that the leg `session-predicate callers (asked only at the act)` and `loop selftest` are owed and graded at the build. Re-pin the §7 leg line to name both in the pass that adds their rows to tools/gate-legs.json. The loop-selftest half for units 30, 32, 34 and 35 is covered by M12.
- **Left-shift gate:** As for M12.

### L7 — Forced renders are missing from Files touched (id 31)

- **Where:** TOOL-dRankedPlan-37 §4 Files touched (S24, also S23), and units 30 and 32 to 35.
- **What:** `memory/gotchas/INDEX.md` must be re-rendered for S24's new gotcha, and `memory/map/generated/symbols.json` for every new function.
- **Consequence:** `memory hygiene` (gotchas.py check 17) and `codebase-map coverage + freshness` red a pass on a write it never planned. Both reds are caught.
- **Fix (skeptic judged it SOUND):** Add `memory/gotchas/INDEX.md` (`gotchas.py --write`) to unit 37's Files touched. Add `memory/map/generated/symbols.json` to each function-minting unit's Files touched, with `codebase-map coverage + freshness` on its §7.
- **Left-shift gate:** A spec-token check: a Files touched entry that adds a function or a gotcha record must name its render.

### L8 — The seed's perf line omits the per-plant kit copy (id 32)

- **Where:** TOOL-dRankedPlan-33 §5 perf / scale.
- **What:** §5 counts "one door run, one commit and one check per plant". S1 also copies the 36-file memory-tree kit into every seeded plant, which the skeptic measured at about 5.1s per copy, and no budget row is revisited.
- **Consequence:** A held suite can go over budget with no unit owning the overrun. The budget gate would catch it.
- **Fix (skeptic judged it SOUND):** State the measured per-plant seed cost in §5. Seed once into a template repository and clone it per plant, or copy only the files the door and check import. Have the close re-measure and re-declare the `loop selftest` budget row.
- **Left-shift gate:** A checklist entry: a fixture change that adds per-plant I/O restates the suite's budget row.

### L9 — S5 gives no dispatch order for `.githooks/*.py` (id 42)

- **Where:** TOOL-dRankedPlan-32 §2 S2, S5.
- **What:** S2 sends every `.githooks/` file to shell, S1 reads `*.py`, and S5 gives no precedence between them, while `.githooks/pre_push_bar_selftest.py` is tracked.
- **Consequence:** The builder chooses which reader the file gets. The effect stays inside that one directory.
- **Fix (skeptic judged it SOUND):** State the dispatch order in S5: extension first (`*.py` to Python, `*.js` to JS, `*.sh` to shell), and extensionless files under `.githooks/` to shell.
- **Left-shift gate:** As for M8.
- **See also:** M8 (id 14).

review-shape kind=spec-audit round=1 intensity=full at=synth raw=42 confirmed=39 refuted=3 unverified=0 blocker=0 high=7 medium=23 low=9 agents=11 out-tokens=249608

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2 and S5, against TOOL-dRankedPlan-31 S4/AC3, TOOL-dRankedPlan-30 S3/AC2 and TOOL-dRankedPlan-22 S3 | high | high | confirmed | Unit 32 S1 covers Python files only (read_python_callers). S2 counts a shell or `.githooks/` file as a caller only when one of its commands invokes ratify.py, either as the first word or after an interpreter word. S5 (32:67-70) 'supersedes unit 22 S2's sentence that defines a caller'. Units 30, 31 and 32 are all Status order 7. Unit 31 S4 and AC3 (31:48-50, :142-146) add a `read_plan_ratification(` call to `.githooks/pre-commit` and expect exit 1. Unit 22 S3's caller-guard plant (22:48-51) and unit 30 S3 and AC2 (30:51-52, :145-147) refuse that same hook line. Under S2 none of these lines is an invocation, so the hook is read as having no caller. A hook that calls the predicate in-process through `python -c` or a heredoc is also read by neither reader. §3 names only run-time assembled calls as unread. Unit 32's own §7 arm still describes the staged break as 'a predicate that matches only `read_plan_ratification(`'. | sound | two-answers-to-one-question |
| 2 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2, against section 5 security | high | high | confirmed | S2 (32:49-55) splits commands at `;`, `&&`, `\|\|`, `\|`, `$(`, a backtick and `(`, and strips only leading NAME=value words. A command counts as an invocation only when its first word ends in ratify.py or is an interpreter. In `if ! "$py" "$d/ratify.py" "$slug"; then`, the command before `;` has `if` as its first word, so the line is never read as an invocation. The probe over tracked *.sh and .githooks files reproduced the idiom at tools/lexicon/adopt-lexicon.sh:423 (`if ! "$PY" "$KIT_DIR/lexicon_conf.py" ...`) and tools/memory-tree/merge-rows.test.sh:423. §3 (32:81-88) names only run-time assembled calls as unread, so §5's claim that 'every unread form is named in §3' (32:159-160) is false. No plant covers the guarded form. | sound | - |
| 3 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S1 (argv list) | medium | medium | confirmed | In S1 (32:40-45), an argv-list element counts only when it holds a `str` constant ending in ratify.py. In `str(CLI)` the only leaf is the Name `CLI`, so `[sys.executable, str(CLI), slug]` is not a caller. The tree uses this idiom: grep printed tools/branch-reconcile/selftest.py:28 `CLI = HERE / "branch_reconcile.py"` and :121 `subprocess.run([sys.executable, str(CLI), "--root", ...])`. §3 does not name the variable-bound form, and the §4 probe table covers only the drift_report and map_diff analogues. | sound | - |
| 4 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-30.md:section 6 AC1, against the build order | medium | medium | confirmed | Unit 30's Status is order 7, while unit 3, which creates tools/memory-tree/triage.py (unit 3 S1), is order 10. `ls tools/memory-tree/triage.py` printed 'No such file', and `git ls-files \| grep -i triage` lists no file under tools/. resolve_kit_dir.py:47 probes `(cand / anchor).is_file()` and raises LookupError otherwise, and unit 30 S2 (30:43-44) says an unresolved anchor yields no path. So at unit 30's own tip, AC1's 'exactly two paths ... git ls-files lists' (30:141-144) cannot hold for a correct build. | sound | - |
| 5 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-33.md:section 2 S2 against section 4 'The base after this unit' and section 6 AC4 | medium | medium | confirmed | Unit 33 S1 (33:34-37) is the only step that copies the memory-tree kit. Line 25 says the shared fixture has no memory-tree kit, and S2 (33:44-48) says the three plan-record-* plants 'keep their own state' and are not seeded. Yet the §4 table (33:94-99) gives plan-record-absent and plan-record-open-probe a 'copied' kit and gives plan-record-unread 'the seed'. Unit 19's plant table (19:105-107) names no kit copy. Built as S2 reads, plan-record-absent has no kit and refuses `unread` (unit 19 S1:41), so AC4's expected `unwitnessed` cannot hold. | sound | - |
| 6 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-31.md:section 2 S2 against section 4 Files touched and section 7 Gates | medium | medium | confirmed | Unit 31 S2 (31:38-43) owes a ceiling-evidence.txt row and a loop.md dossier claim. §4 Files touched (31:104-108) lists kit.toml, gate-legs.json, subject-pins.tsv, loop.md and selftest.py, with no ceiling-evidence.txt. §7 (31:150) lacks `codebase-map coverage + freshness`. That leg exists (gate-legs.json:833), and map_extractors.py:175-196 reads every gate-legs name as an inventory key. S1 models the row on review-join's row, which carries `"ceiling": 300` (gate-legs.json:717-724), but S1 names no ceiling, and S2 puts the ceiling 'in the descriptor'. This is the same omission the earlier audit recorded as M13 (review :211-216). | sound | - |
| 7 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-35.md:section 2 S3 (merged-sides) against section 6 AC2 | low | low | confirmed | Unit 35 S3 (35:50-53) describes merged-sides as one record on each branch plus a third on top of the merge, and names no Disposition words. By S1 (35:35-38), unranked records with one word return the path-sorted first record with no conflict. AC2 (35:138-140) expects None with the conflict reason before the third record, and AC3's red case implies a deferral and a `continue`. The words are inferable from AC3, so the effect is a spec gap in a plant only. | sound | - |
| 8 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2 and S5 (against TOOL-dRankedPlan-30 S3/AC2 and TOOL-dRankedPlan-31 S4/AC3) | high | - | refuted | duplicate of id=1. It is the same defect: unit 32 S2 and S5 drop the textual `read_plan_ratification(` rule for shell and `.githooks/` files, which breaks unit 31 S4/AC3, unit 30 S3/AC2 and unit 22 S3's caller-guard, and leaves an in-process or heredoc call in a hook unread. The extra heredoc evidence I confirmed under id=1. | sound | - |
| 9 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-30.md:section 2 S2 and section 4 'The derivation' | high | medium | confirmed | Re-probed under the scratch directory. tempfile.mkdtemp returned `C:\Users\DAILY-~1\...\tmpw35d2upn`, while `git rev-parse --show-toplevel` printed `C:/Users/daily-agent/...`. `Path(<short>/scripts/loop/ratify.py).absolute().relative_to(Path(toplevel))` raised ValueError, and `.resolve()` printed the long form. Unit 30 §4's derivation (30:91-98) uses `.absolute()` and `relative_to(root)` and never states where root comes from, so a builder who takes root from git toplevel refuses the kit's own module in every short-%TEMP% scratch repository. Units 31 AC3 and 37 AC5 pin such clones. I graded this medium, not high: the effect is a false red on Windows that the plants surface, not a fail-open. | unsound | - |
| 10 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md:section 6 AC19 | high | high | confirmed | Reproduced. `python -c "import sys;print(sys.argv[1:])" --path ~/x` printed ['--path', 'C:/Users/daily-agent/x']. `gen_build_index.py --asks --path ~/x` exits 2 at base with the existing 'is absolute or climbs out with ..' refusal. `--path '~/x'` exits 0 and prints the backlog summary. AC19 (spec-37 :363-366) spells the CLI case unquoted, so the shell expands the tilde before the program sees it. That half of the criterion is green before S23 is built and never exercises the `~` rule in read_asks_args. The direct helper probe in the same AC still checks the helper itself, so what goes unproven is only that the caller routes through it. That makes this high, not blocker. | sound | - |
| 11 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-33.md:section 2 S1 | medium | medium | confirmed | In spec-33, S1 (:34-43) copies `.memory-tree.conf.example` as the scratch conf and mints `TOOL-<slug>-1`. The example conf's line 20 reads FAMILIES="architecture:ARCH deployment:DEPL design:DES", with no TOOL. tree_lib.py:416-418 `_id_alternation` builds the family alternation only from FAMILIES. The binding reader (tree_lib.py:490 onward) uses that alternation, and unit 16 S2 serves a plan as `plan <FAMILY>-<slug>-1`. A TOOL id therefore does not parse under the seeded conf, and S1's witness assertion would raise at the fixture base. S1 never says which conf keys the seed overrides. | sound | - |
| 12 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-35.md:section 2 S1 | medium | low | confirmed | Half of the claim is refuted. Spec-35 S1 :34 already says the governing record's commit must be a 'proper ancestor', so two records from one commit cannot each govern when the text is read as written. The unranked clause at :35-36 ('no other record's ancestor') drops the word 'proper', though. It names `git merge-base --is-ancestor`, which is reflexive (exit 0 for X X). Read literally, records sharing one commit are each other's ancestors, so the unranked set comes out empty. That is a wording gap the AC1 plant (:49, :137) would catch in the build, so it is graded low. | sound | - |
| 13 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2 (shell reading) | medium | medium | confirmed | Spec-32 S2 (:48-56) applies shlex.split to every joined line of `*.sh` and `.githooks/*`. Unlike S1's textual prefilter, it has no prefilter, and it states no rule for a ValueError. My scratch probe over git ls-files reported 176 files, with 6189 lines in 147 files raising ValueError. None of those lines names ratify.py today, so nothing is missed at base. The behaviour on an unparseable line is still left unspecified, and the choice is between crashing the always-run leg and failing open. | sound | - |
| 14 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2/S5 and section 5 'security' | medium | medium | confirmed | git ls-files lists `.githooks/pre_push_bar_selftest.py`, a Python file. S2 :48 assigns 'every file under .githooks/' to the shell reader, and S5 :68-70 never says how a file's kind is decided. S2 detects only ratify.py command invocations. A heredoc'd Python `read_plan_ratification` reference inside a .sh file is therefore read by neither reader. §3 (:86-88) names only getattr, importlib and built-up strings, so §5 :159-160's claim that 'every unread form is named in §3' is false. §4 :126 and §5 :165 also claim heredoc lines fail closed, which holds only for command-shaped ratify.py lines. | sound | - |
| 15 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md:section 2 S19/S20, section 4 'L1', section 6 AC16 | medium | medium | confirmed | `grep -n "697\\|695"` over unit 16's spec printed :136 (the hands-off edge 'whose figure 697 that unit corrects to 695'), :151 and :250. Spec-37 S19/S20 cite :149 and :248 and correct only §4's population line and §5's perf line. Line 136 is left alone, so AC16's `grep -c "697"` prints 0 (:352-354) cannot go green as scoped. | sound | - |
| 16 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-31.md:section 4 Rollout | medium | medium | confirmed | Spec-31's rollout (:98-99) says the leg reds on plan_revision.py from order 13 until order 14. In the README build order, unit 15 is at step 13, unit 23 at 14, unit 29 at 17 and unit 37 at 18. Unit 23 replaces only its own plant's stub (unit 23 :53). Unit 15 S6's stubs (:86) and unit 29 S32's stub (:210) stay in place. Spec-37 S5 (:74-76) itself says ratify.py --check-callers admits plan_revision.py only 'at this unit's tip', after S3/S4 remove every stub. By the spec set's own account the red window runs from order 13 to 17. | sound | - |
| 17 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 6 AC4 | low | low | confirmed | `grep -c "ratify.py" tools/unattended/unattended.sh` prints 0 at base. AC4 (spec-32 :180-183) pins a single whole-file count of at least 1 for two distinct shapes, the resolver line and the --exit call. One mention of either satisfies it, so the count cannot show that the --exit arm is present. It is evidence wording only, since the --check-callers exit 0 still runs over the real tree. | sound | line-claim-matched-over-the-whole-output |
| 18 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md:section 2 S25 | low | low | confirmed | In a scratch repo, a staged-only file appears in `git ls-files` and has no adding commit. Spec-37 S25 (:164-167) calls a staged-only record one 'git does not track'. A builder who tests tracking with ls-files therefore routes it to the 'has no adding commit' line, not 'not committed'. Either way the record is not kept and the gate fails closed. The only effect is which why-line is printed, plus AC21's plant being ambiguous. | sound | index-derivation-reads-a-half-staged-move-as-a-deletion |
| 19 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-34.md:section 2 S1 and section 4 "The date after this unit" (row "added after T") | high | high | confirmed | tools/unattended/lib-unattended.sh:1725-1727 does say '`--follow` ALSO FOLLOWS COPIES'. Unit 34 S1 adopts `git log --follow --diff-filter=A` and drops that caveat, and its §4 row 'added after T -> the add' leaves the copy case out. I re-ran the probe in scratch (verify-r1/fc, git 2.54.0.windows.1): commit d1 (a 7-line disposition), commit T, then commit d2, a near-copy of d1 with 2 lines changed. `git log --follow --diff-filter=A --format=%s -- b/d2.md` printed `d1`; without --follow it printed `d2`. So a fresh second `terminal` record is dated before T and is not kept, and AC3's 'exits 0 once a second terminal record is committed' fails. Disposition records share one fields form, so this path is likely. It fails closed (a false hold, never a false release), which is why I grade it high and not blocker. | sound | - |
| 20 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2 and S3; section 10 Reuse audit | medium | medium | confirmed | tools/lexicon/lexicon.py:469 ships `scan_shell_tokens`. Its docstring says it tracks quotes, `$'…'`, continuations, `$(…)`, heredocs and here-strings. `scan_ts_tokens` at :950 emits `[ ] ,` as op tokens. tools/codebase-map/map_extractors.py:309-314 imports from the lexicon kit through resolve_kit_dir. Unit 32 S2 instead builds line joining plus `shlex.split`, §4 admits the heredoc miss class, and §10 names only parse_shell_defs. So the unit ships a second, weaker tokenizer. The effect is contained: the heredoc miss fails closed as a refusal. | unsound | - |
| 21 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 10 Reuse audit, sentence "The rule reused is the code-line rule" | low | low | confirmed | Unit 32 lines 205-206 read 'The rule reused is the code-line rule of `tools/workflows/check-review-join.sh`'. tools/workflows/check-review-join.sh:25-28 is a comment-stripping line gate over *.js. Unit 32 S1 and S2 replace that textual rule with `ast` and `shlex` readings, and §4 rejects 'A regex over Python source'. The sentence misdescribes what the unit reuses, and it has no effect on behaviour. | sound | - |
| 22 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-35.md:section 3 Non-goals (dormancy bullet) and section 2 S1 | high | high | confirmed | Unit 24:56-57 says `read_build_disposition` asks the reader 'once per item of its three moves and taking the newest answer'. Unit 35 S1 orders kept records only within one item's set. No subject spec redefines the cross-item pick: grep for read_build_disposition finds only units 24 and 4. Yet unit 35 §3 says dispose 'reads the same answer through the reader it is built on'. So two merged records naming different moves, written on two machines, still reach an unordered 'newest' pick, and that pick records one move through write_transition. That is a wrong move on a narrow, multi-machine path. | sound | - |
| 23 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-31.md:section 7 Gates | medium | low | confirmed | Unit 31 §7 (line 150) does name neither `loop selftest` nor `session-predicate callers (asked only at the act)`, while S1 creates that leg and S3 edits tools/loop/selftest.py. The consequence is softer than claimed. The New arm line already names the leg in prose, the leg is unguarded so every bar runs it, and the Rollout says the close's bar reads it. The loop-selftest half for units 30/32/34/35 is the same class as id 27. | unsound | hand-named-gate-list-green-while-the-bar-reds |
| 24 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-31.md:section 7 leg line; section 4 Files touched | medium | medium | confirmed | In tools/gate-legs.json, `govkit selfcheck` is in the declarations chunk with no guard (argv govkit.py selfcheck), and govkit.py:2863-2868 fails when the descriptor and manifest disagree on doc_reads. `codebase-map coverage + freshness` and `leg ceilings clear their evidenced maximum` are also unguarded declarations legs. Unit 31 §7 lists `govkit selftest` (a held selftests leg) but none of those three. Its Files touched omits tools/run-gates/ceiling-evidence.txt, although S2 writes that row through derive-ceilings.py --write. | sound | a-new-leg-trips-a-growing-set-of-meta-gates |
| 25 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-31.md:section 4 Rollout | medium | medium | confirmed | Unit 15 S6 (line 86) gives its plants a stub `read_plan_ratification`. Unit 23 S3 (order 14) replaces the stub in only one plant, `unratified-reentry`. Unit 29 S32 (order 17) adds another stub. Unit 37 S3 and S5 (order 18) remove all of them, and its S9 says the tree run exits 0 only 'after units 21, 23 and 29 and S3 to S5 here'. Unit 32 S1 counts any Name or Attribute reference as a caller. So unit 31's unguarded leg is red from order 13 through 17, not '13 until order 14' as its Rollout states. The restated window is the cure. The 'better' alternative would not by itself keep the leg green at 13, because unit 15 S5's own call to read_plan_ratification in `show` is already a caller there. | sound | - |
| 26 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-33.md:section 7 leg line and the unattended.test.sh New arm (also unit 37 §7 for S15) | medium | - | refuted | Case 2, the section already says it. Unit 33 §7 line 171 and unit 37 §7 line 386 each carry `New arm: tools/unattended/unattended.test.sh · covers AC5` and `· covers AC13`. So the suite that runs the arms is named, the way tools/check-spec-tokens.py:396-398 requires: 'name the suite under New arm:; the bar and the suites run once, after the build is complete'. It is true that no gate-legs row runs unattended.test.sh and that `unattended kit gate` runs check-unattended.sh, but no nameable leg exists for the shards. Spelling `bash tools/unattended/unattended.test.sh --shard <k>/8` or `run-unattended-gates.sh --selftests` on the leg line matches the BAR pattern at :390-394 and would be a spec-tokens hit, so the fix is unsound. | unsound | criterion-asserts-what-its-own-command-cannot-show |
| 27 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-30.md:section 7 leg line (same in units 31, 32, 33, 34, 35, 36, 37) | medium | medium | confirmed | .memory-tree.conf sets SPEC_GUARD_LEGS_CUTOFF=2026-09-22. tools/check-spec-tokens.py:1609-1622 adds a hit when §4 Files touched names a path that trips a non-broad guard of a leg that §7 does not name. TOOL-dDeclaredLoop-75 S21 gives `loop selftest` the guard `{prefix}/loop/`, and dDeclaredLoop is a parent build (README line 9). tools/loop does not exist today, so the arm is silent now. Once the loop legs land, every subject spec that touches tools/loop/* trips it, and none of their §7 lines names `loop selftest`. They cannot name it today: :1546-1547 makes a §7 token that is not in gate-legs.json a hit, which is why re-pinning at the build is the right cure. | sound | held-suite-guard-misses-a-sibling-kit |
| 28 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md:section 2 S13 and AC11 | medium | medium | confirmed | Re-read: tools/memory-tree/kit.toml:277-280 gives `build-index selftest` the guard ["{kit}/"], while tools/gate-legs.json:482-486 has ["{prefix}/lib/","{prefix}/memory-tree/","{prefix}/check-spec-tokens.py"]. `routed-commits selftest` shows the same split (kit.toml:345 `{kit}/`). tools/govkit/govkit.py:2604 says nothing compares a descriptor's guard with the manifest's. So AC11's 'each kit's [[gate_leg]] entry carries the same guard' is not true at base. Unit 37 S1 has the drafts-cross-session plant write moves 'through write_transition', which lives in tools/loop/loop_transition.py (dDeclaredLoop-27 Files touched), but S13 adds only `{prefix}/loop/ratify.py`. Unit 33 S1 copies the whole memory-tree kit and runs gov_record.py new, plan_record.py check and the conf example, but S13 gives `loop selftest` only plan_record.py and plan_fields.py. AC11's own Red-when ('a suite reads a sibling kit file its leg's guard does not name') is therefore met as specified. The effect stays inside a held suite that skips on an edit, so medium. | sound | held-suite-guard-misses-a-sibling-kit |
| 29 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md:section 2 S19/S20 and AC16 | medium | medium | confirmed | `grep -n "697\\|695"` over 2026-10-26-spec-TOOL-dRankedPlan-16.md printed line 136 (the hands-off edge 'whose figure 697 that unit corrects to 695'), line 151 (the population line) and line 250 (the perf line). `grep -c 697` printed 3. S19 and S20 correct only the population and perf lines and cite :149 and :248, which are stale. The edge at :136 keeps 697, so AC16's required count of 0 stays red when the unit is built as written. | sound | - |
| 30 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-36.md:section 2 S2; section 4 Files touched | medium | medium | confirmed | dDeclaredLoop-27:201 spells the call `derive_step_scenarios(build)`, and :240 puts its call in tools/loop/loop_transition.py 'before write_transition writes'. Unit 14:51/116 uses the same one-argument signature. In unit 36, S2 has the function pass the pending move's own `scenario` field as pin=. That field is not on disk before write_transition writes, so the caller must hand it over, which means a signature and call-site change in loop_transition.py. Yet unit 36 §4 Files touched lists only tools/loop/scenario.py, and no new signature is spelled. The builder meets this as a write outside the declared set, so it is contained. | sound | - |
| 31 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md:section 4 Files touched (S24; also S23 and units 30/32-35's new functions) | low | low | confirmed | Read gotchas.py:529-531: check 17 reds a missing or stale gotchas/INDEX.md. check-memory-hygiene.sh:3027 runs `gotchas.py --check`. `grep -c read_adding_commits memory/map/generated/symbols.json` printed 1, so kit functions are inventoried there. The `codebase-map coverage + freshness` leg (gate-legs.json:833) is a repo-subject leg with no guard. Unit 37 Files touched adds a gotcha record but not INDEX.md, and no unit that mints a function lists symbols.json. 282 spec files in the tree name these renders, so naming them is the convention. Both reds are caught by gates and the list is labelled an estimate, so low. | sound | - |
| 32 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-33.md:section 5 perf / scale | low | low | confirmed | Unit 33 §5:131 reads 'one door run, one commit and one check per plant'. Its S1 copies the memory-tree kit into each scratch repository, and the perf line does not count that copy. `git ls-files tools/memory-tree \| wc -l` printed 36. My own scratch probe (git archive of the kit, extract, git add, commit) took 5.10s for one copy, which reproduces the finder's ~5s. selftest-budgets.txt:55 holds `build-index selftest 140`, and no unit revisits a budget row. The budget gate would catch an overrun, so the effect is contained to a misstated perf line: low. | sound | - |
| 33 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2 (and §4 "The probe over the tree", §5 error states) | high | high | confirmed | Unit 32 S2 splits at ;, &&, \|\|, \|, $(, backtick and ( and then calls shlex.split. Neither S2 nor §5 says what happens when shlex raises; §5 covers only an unparsable Python file. My own probe (scratchpad/verify-r1/shl.py) applied the join, split set and shlex.split(comments=True) to tracked *.sh and .githooks/* files. It printed `ok 74 err 14` for gen_build_index.py, e.g. adopt-memory-tree.sh '$KIT_REL/gen_build_index.py)."' No closing quotation, and `ok 12 err 2` for drift_report.py, e.g. unattended.test.sh 'git -C "$HERE" rev-parse --show-toplevel)/$_da_rel/drift_report.py"'. Splitting at `$(` inside a quoted argument breaks the most natural hook shape (`"$py" "$d/ratify.py" "$(...)"`). Built as written, the check either crashes on every bar or skips the piece and fails open. The §4 table records no error count. | sound | - |
| 34 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2 | high | high | confirmed | Unit 32 S2 counts a command as an invocation only when its first word, after skipped NAME=value words, ends in ratify.py or is an interpreter. A leading `if`, `!`, `exec` or a case pattern is never skipped, so those commands are not invocations. Re-read in the tree: tools/lexicon/adopt-lexicon.sh:423 `if ! "$PY" "$KIT_DIR/lexicon_conf.py" ...`, tools/memory-tree/merge-rows.sh:60 `exec "$PY" "$HERE/merge-rows.py" "$@"`, and tools/run-gates/run-gates.sh:224 `--regen)       exec "$PYBIN" "$KITDIR/regen.py" --write ;;`. `(` is a split character but `)` is not, so the case arm keeps `--regen)` as its first word. A predicate call in an if condition or behind exec passes the tree-wide ban, so the check certifies an absence it does not test on that path. | sound | - |
| 35 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-30.md:section 2 S2 and §4 "The derivation" | high | medium | confirmed | Unit 30 §4 derivation keeps `path.relative_to(root)` and never normalises either side. I reproduced it in a scratch repo reached through C:/Users/DAILY-~1/...: Path(__file__).absolute() printed the short form, `git rev-parse --show-toplevel` printed C:\Users\daily-agent\..., and relative_to raised ValueError 'is not in the subpath of'. echo $TEMP prints the 8.3 form, and resolve_kit_dir.py:28 deliberately uses .absolute() and never resolve(). Unit 22 S2 leaves the default root unstated, so the failure needs root spelled differently from __file__ (git toplevel, a long --root, a junction or a case difference). Then the kit's own module is refused. That fails closed and a fixture run on this machine shows it, so medium, not high. | sound | - |
| 36 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-34.md:section 2 S1 and §5 risks | medium | medium | confirmed | Scratch probe (verify-r1/f3): commit A adds b/2026-10-01-disp-a.md (Disposition: defer, templated body), commit T is empty, and one commit `replace` git-rms it and adds b/2026-10-27-disp-b.md (Disposition: continue, same template). `git log --follow --diff-filter=A --format=%s -- b/2026-10-27-disp-b.md` printed `A`, while the path-limited form printed `replace`. With a less similar body (verify-r1/f2) no rename was detected, so the case depends on similarity, as claimed. Unit 34 §4's table has no such row, and §5 prices only the >50% rewrite case. The fresh owner act is dated before T and not kept. That fails closed but is silent: medium. | unsound | - |
| 37 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-33.md:section 2 S1 (--seed) and §5 security | medium | medium | confirmed | Spec-33 S1 (:34-43) has `--fixture --seed <dir> --build <slug>` copy the memory-tree kit into any directory it is given, turn `.memory-tree.conf.example` into `.memory-tree.conf` and commit a plan record. Nothing validates `<dir>`, and nothing says what happens to an existing conf, kit copy or record. §5 (:129-130) says the callers create the directory and calls this 'no new write path in the product', but nothing in the spec checks either. The S3 target is an existing suite repo, and unattended.test.sh writes `.memory-tree.conf` files in its fixtures (e.g. :2537, :6521), so the overwrite case is real. The damage stays inside fixture tooling unless someone mistypes the path. | sound | - |
| 38 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-33.md:section 2 S1 | medium | - | refuted | Premise not established. The gotcha file puts identity on whoever creates a repo: 'Every repo a fixture COMMITS in gets its own identity at creation'. The seed only commits inside repos its callers create, and the driver suite sets a local identity on those repos (unattended.test.sh:200, :479-480 for the bare origin). The `ratify.py --fixture` scratch repo belongs to units 9/10, which are not under audit, and the other plants there commit too, so a seed-specific identity would fix nothing. The gpgsign concern applies just as much to the existing suites, which mostly do not neutralise it. The finder graded it medium and I cannot show it as a defect of spec 33, so it is refuted. | sound | fixture-inherits-ambient-machine-state |
| 39 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-36.md:section 2 S1-S2 | medium | medium | confirmed | Spec-36 S1 (:32-37) keeps exit 2 for 'no transition record and no pin given'. S2 (:38-43) passes the move's own `scenario` field as `pin=` and never covers a first move where that field is absent or empty. dDeclaredLoop-27 S8 (:80-87) says records 'carry' `scenario=` but writes it through `write_transition`'s optional `--field`, and neither spec makes it required. Spec-36 §5 (:116) only covers the CLI case with no pin. So the absent or empty field on a first move has no defined result, and exit 2 is the likely one. | sound | - |
| 40 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md:section 2 S23 and AC19 | medium | medium | confirmed | In the code, routed_commits.py:155 does `entry = raw.replace("\\", "/")` before the :159 regex, and gen_build_index.py:3339 sets `folded = value.replace(...)` before the :3340 test. In both, the backslash fold happens at the caller. Spec-37 S23 (:149-155) defines the shared helper only by its four shapes, replaces only the inline lines :159-162, and adds the `Scope` check as a third caller with no mention of a fold. AC19 (:363-366) probes only forward-slash shapes. A helper built as written would let backslash-led and `a\..\b` values through any caller that does not fold, and AC19 would not catch it. Folding inside the helper fixes this; a UNC value folds to `//...` and is refused as absolute. | sound | - |
| 41 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-31.md:section 4 Rollout | medium | medium | confirmed | Spec-31 Rollout (:98-100) says the leg is red on `plan_revision.py` 'from order 13 ... until order 14'. Spec-37 (order 18) S3 (:66-69) still has to remove stubs from unit 15 S6's seven plants and from unit 29 S32's (unit 29 is order 17). Its S9 (:88-91) says the tree run of `--check-callers` first exits 0 only at unit 37's tip. The Status lines confirm unit 15 at order 13, unit 23 at 14, unit 29 at 17 and unit 37 at 18. The red window the Rollout states is wrong: it runs through order 17 and turns green at 18. | sound | - |
| 42 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-32.md:section 2 S2 and S5 | low | low | confirmed | `git ls-files .githooks` printed `.githooks/pre_push_bar_selftest.py` beside the extensionless hooks and the `*.sh` files. Spec-32 S2 (:48) sends 'every file under `.githooks/`' to the shell reader, the Python reader covers `*.py`, and S5 (:67-68) gives no precedence between them. So the dispatch for that tracked `.py` file is undefined, though only within that one directory. | sound | - |

**Serves:** research TOOL-dGroundRules-10

# Divergence brief — TOOL-dGroundRules-10, the leg line and four gaps

## The prompt

> Its builder handed TOOL-dGroundRules-10 back as a DIVERGENCE: `--dispatch` refused (check 49) because `tools/check-spec-tokens.py` reds the spec once it reads INPROGRESS: §4 names `tools/policy/policy.py`, which trips the `policy fixtures` leg's guard, and §7's leg line lacks that leg, though §7's own first `New arm:` line puts the `limit-` cases in it. It found four more gaps.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. §7's leg line adds `policy fixtures`.
2. S3/AC5: gov's own `.claude/settings.json` is not rendered by the builder, since rewriting it changes the configuration of the session running in this worktree. The render is the main loop's, at the close before the bar, through the file's `[[generated]]` regeneration; AC5 is observed then and says so.
3. S5: rule 7 adds no rule when the payload `cwd` lies in no checkout; say so, and that TOOL-dGroundRules-21 S38 later makes that case refuse.
4. §4's suite clause covers what rule 7 does to the existing `tools/hooks/agent-cap.test.sh` arms: the rule-6 admit arms run on a hook copy with no `policy` kit beside it, and the slot-ledger checks in the rule-6 section (around lines 2456-2460, 2482-2486, 2502-2506) and the `--only=scripts` arm (around line 2517, which asserts rule 1's message) are named in the suite update's scope. Verify the line numbers against the tree.
5. S9's no-denial-lost property (around lines 2046-2281): a BASE denial that came from a rule this unit retires (rule 1 or rule 3) is an expected loss, excluded by name, never counted as a lost denial; the property's own fixtures that hit those rules are listed.
6. The status header's rev rises by one, with a §9 line naming what disagreed and each ruling.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS; every `**Carries:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
AC13 stays red by design until TOOL-dGroundRules-18 (`SPEC_WRITERS` 6 against `MAX_VERIFIERS` 5). AC15 to AC17 need the live driver at the close.

### Reuse
The builder's reading of `tools/hooks/agent-cap.test.sh` is the evidence; re-read it.

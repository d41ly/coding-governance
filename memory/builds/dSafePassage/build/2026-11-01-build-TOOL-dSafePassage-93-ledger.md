**Serves:** journal TOOL-dSafePassage-93

# TOOL-dSafePassage-93 — acceptance ledger

The unit as built, at spec rev-2. Product write: `tools/govkit/selftest.py`. `run_in_gov` gains the
keyword `root`, defaulting to `PFX`, and no current caller moves. S1's `[dSP-93]` arm sits in the
`DEPL-dCarriedReceipt-11` block after `[dSP-91 L1]` and before the `mvfail` fixture, as the spec's
§4 fenced text writes it. No function, `Refusal` site, flag, conf key or gate leg is added.
`tools/govkit/govkit.py` is not edited.

S2, the narrowed claim of the round-4 closing review's id 4:

set_environ holds the three copies in check_step_isolation and the new check_floor_bash:
the [dSP-45] parent hold and the [dSP-75] fakes hold in check_step_isolation, and the
[dSP-87 AC5] and [dSP-91 L2] holds in check_floor_bash. The GOVKIT_NO_REMOTE_PROBE copy and the
GOV_BASH copy in main() are still typed by hand. This corrects the TOOL-dSafePassage-91 commit
message, spec 91's rev-2 L3 note and its ledger, each of which says set_environ holds all four
environment uses.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion was observed
on node a (Windows 11) from this worktree's root. AC1's probe is the spec's §4 text as written, saved
as `p93_probe.py` in the run's scratchpad; its `tempfile.mkdtemp` fixture repositories sit under
`%TEMP%`, the short-path exception for fixture repositories. The staged break was a scratch copy of
`tools/govkit` in the run's scratchpad with `_case = _alias` at `govkit.py:11113`.

Owed at the close: AC4, the RED-first observation of §7's `New arm:` line inside the suite (the
`[dSP-93]` check under `_case = _alias`, and separately under the link-or-alias text cut), and the
§7 legs at the bar. AC1's red row below is a probe of the engine, not of the suite arm: it does not
discharge the arm's staged-break observation.

**Evidences:** TOOL-dSafePassage-93
- AC1 — `python p93_probe.py` printed `hard link: update exit 1 | other name named: True | case-only named: False | bytes kept: True | link kept: True`; with the scratch engine holding `_case = _alias` it printed `hard link: update exit 1 | other name named: False | case-only named: True | bytes kept: True | link kept: True`.
- AC2 — `git grep -n -F "[dSP-93]" -- tools/govkit/selftest.py` printed one line, `:13244`, after `[dSP-91 L1]` at `:13218` in the `DEPL-dCarriedReceipt-11` block; `git grep -n -F "os.link(" -- tools/govkit/selftest.py` printed one line, `:13233`, in the same arm.
- AC3 — the spec's two `git grep` commands over `memory/builds/dSafePassage/build/`, the first for S2's three-copies phrase and the second for spec 91's note, each printed one line, both in this ledger: `:13` and `:17`. This line spells neither phrase, so it is not a second hit.
- AC4 — owed at the close (§7's `New arm:` line); not observed in this pass.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in a scratch clone of `390033278` (batch g, `2026-11-01-prompt-TOOL-dSafePassage-91-1-researcher.md`), each break staged alone and restored. The DEPL-dCarriedReceipt-11 slice of tools/govkit/selftest.py: `_case = _alias` at govkit.py:11113: `FAIL [dSP-93] a rename onto the adopter's own link to the row's file is refused naming the link, not case folding — apply 0 update 1 ROLLED BACK`; the link-or-alias text cut: `FAIL [dSP-93] … HELD BACK (pinned/demo/keep.txt refused) · ROLLED BACK`. Control: cutting only `or a filesystem alias` moves nothing, the needle being `under another name (a link`. GREEN restored: `FAILURES []`.

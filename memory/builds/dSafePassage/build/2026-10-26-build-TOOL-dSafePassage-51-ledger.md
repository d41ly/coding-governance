**Serves:** journal TOOL-dSafePassage-51

# TOOL-dSafePassage-51 — acceptance ledger

The unit as built, at spec rev-4. Product writes: `tools/govkit/upgrade_steps.py` (S6's link and
listing refusals in `read_target_repositories`'s `modules/` walk, S7's "or a file it includes"
wording, S15's `lstat`/`stat` type test in `submodule_paths` with no open, the
`submodule-modules-link-loop` and `gitmodules-fifo` plants, `UNLISTED_EXECUTOR_KEYS` deleted),
`tools/govkit/selftest.py` (S9's literal, the dSP-51 arm, two existing needles moved to the new
texts) and `help/upgrade-steps.md`. Held at HEAD with no write: S1 (AC1), S4 (TOOL-dSafePassage-49
deviation 181 built the order), S8's row rule (TOOL-dSafePassage-49 S16) and S10. S2, S3 and AC2 are
struck; S11, S13 and S14 are readings no code carries. One departure: deviation 182.

S10 as read: the two fixture calls `startswith(DOWN_STOP_PREFIXES[0])` in `run_rollback_fixture` test
for the one `down interrupted:` stop, which `test_step_row` cannot answer; their argument is an entry,
not `DOWN_STOP_PREFIXES`, so AC7's count stays one.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
(Windows, Python 3.15.2) over this worktree, by the probe the spec names, run directly.

Owed at the close: the `New arm:` line's RED-first observation of the dSP-51 checks in
`tools/govkit/selftest.py` (AC3 AC4 AC5 AC6 AC9), and the §7 legs `govkit selftest`,
`govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `recall floor arms`,
`encoding posture`, `lexicon naming predicates`, `policy fixtures` and `spec tokens` at the bar.

AC1 grades the build run's commit order, which no write of this pass moves, so its line sits in
`2026-10-28-build-TOOL-dSafePassage-59-order-check.md`, committed with `Pass: none`
(TOOL-dSafePassage-59 S1).

**Evidences:** TOOL-dSafePassage-51
- AC2 — amended rev-4 — struck at TOOL-dSafePassage-51's rev-4 with its number retained; its Red when reads never, so no observation is owed.
- AC3 — `or a file it includes` — `fixture isolation --plant submodule-config-malformed` exited 1 printing `` `git config --list` over .git/modules/sub exits 128, so .git/modules/sub/config or a file it includes does not read ``, nothing spawned; a staged walk copy running `rev-parse` before the config read exited 1 with `isolation: FAILED`, its refusal naming `.git/modules/sub: git will not open this repository`.
- AC4 — `is a link under modules/` — `fixture isolation --plant submodule-modules-link-loop` exited 1 in 5 s naming `.../t/.git/modules/a/loop is a link under modules/`, no `Traceback`; a staged copy with the link test replaced by `if False:` exited 1 with `isolation: FAILED`, the step run `up · ok`.
- AC5 — `Refusal: 'fx/s2'` — the reverse-walk copy whose move 3 reads `state = state or "applied"` ran `fixture rollback --plant rolled-back-witness-holds`, exited 1 and printed `upgrade_steps.Refusal: 'fx/s2': a rolled-back row carries no `failure`, and this one carries 'down interrupted: started ...'`; over the module TOOL-dSafePassage-49's dSP-49 row stands for the exit 0.
- AC6 — `sendemail.sendmailcmd` — `git grep -n UNLISTED_EXECUTOR_KEYS -- tools/govkit/upgrade_steps.py` printed nothing (exit 1); `sendemail.sendmailCmd` sits at selftest.py:3940, two lines below `:394` at 3938; the widening probe over the literal named `[]` against the module's table and `['sendemail.sendmailcmd']` against a copy without that row.
- AC7 — `test_step_row` — the `ast` walk found one `startswith` call whose argument is the name `DOWN_STOP_PREFIXES`, at line 1206 inside `test_step_row`.
- AC8 — `## What the receipt records` — §4's probe over a scratch page printed the section through its `###` subheading and a fenced `# a shell comment`, and nothing after the next `##`; over `help/upgrade-steps.md` it printed 118 lines ending before `## What the receipt records about steps`, holding the config line "refuses the step, naming that config file", `sendemail.sendmailCmd` and `sendemail.<identity>.<key>`, one line with `ssh://` and `not refused`, and `protocol.ext.allow`.
- AC9 — `skip — gitmodules-fifo` — the `ast` probe read `submodule_paths`'s `os.lstat` and `os.stat` at lines 1451 and 1457 before its one `git` spawn at 1462, no `open`; over a copy spawning `config -f` first it read False. `fixture isolation --plant gitmodules-fifo` printed `isolation: skip — gitmodules-fifo needs os.mkfifo, which this host lacks` and exited 0; the FIFO half needs a POSIX host. `gitmodules-unreadable` still exits 1 naming `.gitmodules does not read: it is no regular file`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_isolation`, the dSP-51 rows), the break was a walk running `rev-parse` before the config read: `FAIL [dSP-51] AC3 AC4 fixture isolation submodule-config-malformed exits 1 within 60 seconds, refused naming exits 128, so .git/modules/sub/config or a file it includes does not read` (1 of 9). On this host the `gitmodules-fifo` row prints its skip line, as the arm states. Restored, GREEN: 9 of 9 `ok`.

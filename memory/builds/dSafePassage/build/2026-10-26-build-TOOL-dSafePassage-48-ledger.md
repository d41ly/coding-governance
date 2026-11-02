**Serves:** journal TOOL-dSafePassage-48

# TOOL-dSafePassage-48 — acceptance ledger

The unit as built, at spec rev-3. S1's class is stated once in `tools/govkit/upgrade_steps.py`: after
the `STEP_REFUSED_KEYS` literal, one `+=` derives a `sendemail.<x>.<key>` row from every
`sendemail.<key>` row, so `sendemail.<x>.ccCmd`, `toCmd`, `headerCmd`, `sendmailCmd` and `smtpServer`
(its absolute-path rule carried) are table rows no one types; the hand-typed
`sendemail.<x>.smtpServer` row of TOOL-dSafePassage-45 S6 is gone into that class. S2 adds the
`sendemail.sendmailCmd` row, its "what runs it" naming git-send-email's option table. S3 adds the
`sendemail-identity-cmd` isolation plant. S4: `help/upgrade-steps.md` names the send-email keys,
`sendemail.sendmailCmd` and the identity form; TOOL-dSafePassage-45's §3 hands-off bullet to this
unit already names the reading. §7's arm is in `tools/govkit/selftest.py`'s `check_step_isolation`
(the `[dSP-48]` checks).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, git 2.54.0.windows.1) over this worktree, the fixture's own targets under `%TEMP%`.

Owed at the close: the RED-first observation of the `New arm:` line (the `[dSP-48]` checks), and
`govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `recall
floor arms`, `encoding posture (text IO names its encoding)`, `lexicon naming predicates`, `policy
fixtures` and `spec tokens (a spec's own names resolve)`.

**Evidences:** TOOL-dSafePassage-48
- AC1 — a scratch probe importing `tools/govkit/upgrade_steps.py` by path, grading each of the eight keys through `check_target_local_config` over a one-row `read_target_local_config`, printed `refused True` for `sendemail.sendmailcmd`, `sendemail.work.sendmailcmd`, `sendemail.work.cccmd`, `sendemail.work.tocmd`, `sendemail.work.headercmd` (each `x`) and `sendemail.work.smtpserver = /usr/bin/x`, and `refused False` for `sendemail.work.to = a@example.com` and `sendemail.work.smtpserver = smtp.example.com`. A table copy without the `sendemail.<x>.ccCmd` row printed `wrong [('sendemail.work.cccmd', 'x')]`; one without `sendemail.sendmailCmd` printed `wrong [('sendemail.sendmailcmd', 'x')]`. The class arm's own listing probe over the new table printed `49 kept; neither: []`.
- AC2 — `python3 tools/govkit/upgrade_steps.py fixture isolation --plant sendemail-identity-cmd` exited 1 and printed `fixture/clean · refused · ... sendemail.work.cccmd in .git/config, so nothing was spawned` and `isolation: sendemail canary: absent`, no `isolation: FAILED`. A scratch copy of the govkit folder with the class `+=` removed printed `fixture/clean · up · ok` and two `isolation: FAILED` lines (not refused naming `sendemail.work.cccmd in .git/config`; the step spawned), exit 1.
- AC3 — `awk '/^#+ What a step can reach/{f=1;next} /^#+ /{f=0} f' help/upgrade-steps.md` printed, at its lines 52 and 54, `` `smtpServer` and `sendemail.sendmailCmd`, which `send-email` runs through `sh -c` although `` and `` Each is refused in its identity form `sendemail.<identity>.<key>` too, such as ``.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_isolation`, the dSP-48 rows), the break was the table derived without the `sendemail.<x>.ccCmd` form: `FAIL [dSP-48] AC1 the check refuses sendmailCmd and the identity forms … wrong: ['sendemail.work.cccmd']` and `FAIL [dSP-48] AC2 fixture isolation sendemail-identity-cmd exits 1, refused naming sendemail.work.cccmd …`, where the fixture prints `isolation: fixture/clean · up · ok` (3 of 4). Restored, GREEN: 4 of 4 `ok`.

**Serves:** journal TOOL-dSafePassage-49

# TOOL-dSafePassage-49 — acceptance ledger

The unit as built, at spec rev-6. In `tools/govkit/upgrade_steps.py`: S16's `test_step_row(step_id,
state, failure)` sits beside `set_step_state` and holds §4 "The row rule", S9's type rule first;
`set_step_state` calls it before it records and `read_step_states` calls it per row, so the reader's
own `failure` test, and its `startswith`, are gone, and a `failure` key is legal on a row whenever
the rule admits its value (a `null` read as absent). S5: move 3 marks a `rolled-back` row whose
witness held `"via": "witness"` where it has no image, as TOOL-dSafePassage-39 S3 marks an unrecorded
one; the reverse-walk child takes a fifth argument, a step id it records `rolled-back` after
`derive_reverse_steps` and before `run_reverse_walk`, and the `rollback` family gains
`rolled-back-witness-holds`. S13, S16: the rollback fixture's two `down exit 1:` texts are built from
`DOWN_STOP_PREFIXES[1]` and its stop check compares through `test_step_row`. S7: the walk refuses a
`modules/` candidate whose `git --git-dir=<c> rev-parse --git-dir` exits non-zero, after its config
read (deviation 181). S18: a `.gitmodules` that exists and is no regular file that opens for reading
is a refusal naming it before the `config -f` read. S19: `render_redacted_config` redacts a key's
tested subsection from its first `<scheme>://` to its last `@`, S9's pattern kept for the rest, and
`check_target_local_config` renders the key apart from ` in <file>`. S8: `UNLISTED_EXECUTOR_KEYS`
holds `sendemail.sendmailCmd`. The `isolation` family gains `submodule-format-unknown`,
`gitmodules-unreadable` and `subsection-password-space`. `help/upgrade-steps.md` names S7's, S18's
and S19's behaviour, the `failure` type rule and S5's re-down, and S17's ssh sentence is reflowed.
§7's arm is in `tools/govkit/selftest.py`: the `[dSP-49 AC4]` to `[dSP-49 AC6]` checks and the
`rs-49a`/`rs-49b` rows in `check_receipt_schema`, the `rolled-back-witness-holds` row in
`check_step_rollback`, and the `[dSP-49]` AC9, AC10, AC13 and AC14 checks in `check_step_isolation`.
The `[dSP-3 AC7]` failed-row case now reads the predicate's text, `a failed row's `failure``.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, git 2.54.0.windows.1), 2026-10-28, over this worktree, by the fixture CLI or a scratch
probe importing `tools/govkit/upgrade_steps.py` by path; staged copies were whole govkit-folder copies
under the run's scratch.

Owed at the close: the RED-first observation of the `New arm:` line (each `[dSP-49]` check above and
its staged copy), and `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `govkit
selfcheck`, `recall floor arms`, `encoding posture (text IO names its encoding)`, `lexicon naming
predicates`, `policy fixtures` and `spec tokens (a spec's own names resolve)`.

**Evidences:** TOOL-dSafePassage-49
- AC1 — `fixture rollback --plant down-fails` exited 1 printing `rollback: fx/s3 ('applied', 'down exit 1: fx: s3 down fails by its plant') · stop text opens with an entry of DOWN_STOP_PREFIXES: yes` and `--plant witness-stays` exited 1 printing `rollback: fx/s2 ('applied', 'witness still holds after down') · stop text opens with an entry of DOWN_STOP_PREFIXES: yes`, neither printing `Refusal`, `Traceback` or `rollback: FAILED`; `DOWN_STOP_PREFIXES` read `('down interrupted:', 'down exit ', 'witness still holds after down', 'reverted check exits ')`.
- AC2 — AMENDED at rev-6: struck, nothing of this pass observes it. The relation it guarded is dispatch order, held by `--dispatch`'s edge refusal and shown by `memory/builds/dSafePassage/RUN.md`'s dispatch rows (§8 F1 (d)).
- AC3 — `fixture rollback --plant rolled-back-witness-holds` exited 0 printing `rollback: rows derived ['fx/s4', 'fx/s3', 'fx/s2', 'fx/s1'] · then fx/s2 recorded rolled-back`, then `step fx/s2 · rolled-back`, `rollback: rows {... 'fx/s2': ('rolled-back', None), ...}` and `the target's bytes equal their bytes before the walk`, no `Refusal` and no `rollback: FAILED`.
- AC4 — a scratch probe over the 18 rows of the row rule (each state with `failure` `5` and `""`, `applied` with none, each of five full down stops, `interrupted: started …` and `exit 1: x`, `failed` with and without a text, `rolled-back` with none and with `down exit 1: boom`) printed `wrong: []` for `test_step_row`, `set_step_state` and `read_step_states` over a one-row receipt, each `5` or `""` refused by `Refusal` (`'a/one': `failure` 5 is neither absent nor a non-empty string`). A govkit-folder copy whose `applied` opening test reads `if False:` printed `wrong: [('applied', 'interrupted: started 2026-10-23T00:00:00Z, no exit recorded'), ('applied', 'exit 1: x')]`.
- AC5 — `govkit.py check --target` over a fixture-factory target whose receipt's applied row carries `"failure": 5` exited 1 with one `step record is malformed: 'govkit/receipt-schema-4': `failure` 5 is neither absent nor a non-empty string` line, and `""` likewise, no traceback; the `ast` probe printed `openings: ['test_step_row']`, and over a reader copy restating the rule `['read_step_states', 'test_step_row']`.
- AC6 — the `ast` probe over the module, f-string parts included, printed `literals: []`; over a copy retyping s3's stop as `"down exit 1: fx: s3 down fails by its plant"` it named that literal.
- AC7 — `fixture isolation --plant ssh-scheme-bare-user` exited 0 printing `isolation: fixture/clean · up · ok` and `ssh-scheme bare user · not refused · git add exits 0`; the probe found `remote rows: []` in `STEP_REFUSED_KEYS` for `remote.<x>.url` and `remote.<x>.pushurl`.
- AC8 — a scratch probe of TOOL-dSafePassage-44's AC2 with S11's floor over `tools/runlog/redaction.tsv` printed `(True, "tokens tested ['ssh://git@github.com/o/r.git', 'https://example.com/a/@b']; redacted []")`; over a scratch copy without the `url-userinfo` row it printed `(False, 'no url-userinfo row')`.
- AC9 — `fixture isolation --plant submodule-format-unknown` exited 1 printing `fixture/status · refused · ... C:/Users/daily-agent/AppData/Local/Temp/gk-iso-…/t/.git/modules/sub: git will not open this repository, ... rev-parse --git-dir` exits 128 ... fatal: Expected git repo version <= 1, found 99, so nothing was spawned` and `format-unknown canary: absent`; a walk copy whose `if opened.returncode:` reads `if False:` printed `fixture/status · up · ok` and `isolation: FAILED`, exit 1.
- AC10 — the widened-arm probe over this node's `git help --config` printed placeholder sections `['bundle', 'credential', 'http', 'sendemail']`, widened `['credential.dsp49.helper', 'http.dsp49.extraHeader', 'sendemail.dsp49.ccCmd', 'sendemail.dsp49.headerCmd', 'sendemail.dsp49.smtpServer', 'sendemail.dsp49.toCmd', 'sendemail.dsp49.sendmailCmd']`, unrowed `[]`; without `sendemail.<x>.ccCmd` it named `['sendemail.dsp49.cccmd']`, without `sendemail.sendmailCmd` `['sendemail.sendmailcmd']`. figure: seven widened, the six of the listing plus `sendmailCmd`'s, DERIVED.
- AC11 — `fixture isolation --plant local-recent-objects-hook` exited 1, its refusal line holding `gc.recentobjectshook` and `.git/config` and not `gc.recentObjectsHook`.
- AC12 — `awk '/^#+ What a step can reach/{f=1;next} /^#+ /{f=0} f' help/upgrade-steps.md` printed, at its line 76, `` `ssh://git@host/repo` is not refused under `ssh`, `git+ssh` or `ssh+git`, nor is a ``, and `protocol.ext.allow` at its lines 12 and 18.
- AC13 — `fixture isolation --plant gitmodules-unreadable` exited 1 printing `fixture/status · refused · ... t/.gitmodules does not read: it is no regular file that opens for reading (not a regular file), ... so nothing was spawned`; a copy whose read tests `gm.is_file()` alone printed `fixture/status · up · ok` and `isolation: FAILED`, exit 1.
- AC14 — `render_redacted_config` returned `http.https://<redacted>@h/.sslkey` for `"http.https://u:se\x20cret@h/.sslkey"` and `"http.https://u:se/cret@h/.sslkey"`; `fixture isolation --plant subsection-password-space` exited 1 printing `isolation: the refusal's named entries · http.https://<redacted>@h/.sslkey in .git/config · password pieces in them: none`, and its whole output holds neither `se cret` nor `cret` (grep count 0); a redactor copy whose subsection rule reads `if False:` printed the entries `http.https://u:se cret@h/.sslkey in .git/config` and three `isolation: FAILED` lines.
- Unchanged plants re-run: `rollback` base, `node-witness-refuses`, `witness-only-down-killed`, `unrecorded-witness-down-killed`, and `isolation` `submodule-config-malformed`, `gitmodules-malformed`, `submodule-nested`, `submodule-unpopulated-worktree`, `submodule-nested-name-differs`, `submodule-name-differs`, `submodule-ref-named-config`, `submodule-main-only`, `submodule-name-slashed`, `sendemail-identity-cmd`, `http-url-key-userinfo` and `insteadof-dotted-userinfo` each exited as `tools/govkit/selftest.py` expects, with no `FAILED` line; every staged-copy needle the existing arms replace still occurs once in the module.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_receipt_schema`, the dSP-43 and dSP-49 row-rule arms), the break was the row rule admitting any `failure` on an `applied` row (the opening test made `if False:`): `FAIL [dSP-49 AC4] test_step_row, the writer and the reader agree on the row rule's 18 rows … wrong: [('applied', 'interrupted: started …', ('admitted', 'admitted', 'admitted'))`, `FAIL [dSP-49 AC5] one opening test of DOWN_STOP_PREFIXES in the module … over the module: []` and `FAIL [dSP-43 AC1] the writer refuses a applied row with `failure` 'exit 1: x'` (6 of 26). The line's isolation and rollback arms (`u49i`, 11 arms; `rolled-back-witness-holds`) are untouched by this break and held. Restored, GREEN: 26 of 26 `ok`.

**Serves:** journal TOOL-dSafePassage-45

# TOOL-dSafePassage-45 — acceptance ledger

The unit as built, at spec rev-3. `tools/govkit/upgrade_steps.py`: `STEP_REFUSED_KEYS` loses the
proxy and credential-file rows (S19) and gains `sendemail.<x>.smtpServer` (S6), whose `an absolute
path` rule is git-send-email's own test, a drive letter alone included (S5). `CREDENTIAL_KEY_SUFFIXES`
and `STEP_CREDENTIAL_KEYS` are minted (S10) and `CREDENTIAL_FILE_KEY_RE` is derived from the table's
refused rows; `test_credential_bearing` tests a proxy key's value with the scheme-optional
`PROXY_USERINFO_RE` (S7) and the key's whole subsection (S8); `render_redacted_config` runs
`REDACT_USERINFO_RE` to the last `@` (S9). The `modules/` walk lists a directory by git's own
repository shape, the reading TOOL-dSafePassage-45 §3 hands off to TOOL-dSafePassage-47 and that
unit's S5 names, and a config or `.gitmodules` that does not read refuses naming the file through
the existing raise sites (S12, S13). The fixture's base case asserts the count equals the
`GIT_CONFIG_KEY_<n>` pairs present and finds `protocol.ext.allow` at index 2, and keeps the caller's
`GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM` (S4). Six plants are added. `tools/govkit/selftest.py`
gains `[dSP-45]` checks in `check_step_isolation` and rewrites the `[dSP-37] AC2` bare count.
`help/upgrade-steps.md`, "What a step can reach", gains the count, the proxy, the secret keys, the
send-email test and the walk's refusals.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) by a probe of the changed code: a scratch script importing `upgrade_steps.py` by
path, the fixture CLI, `git grep`, and staged copies of the govkit folder built under the scratch.

Owed at the close: the `New arm:` line's RED-first observation through `govkit selftest` (the four
`[dSP-45]` staged copies), and the §7 legs.

**Evidences:** TOOL-dSafePassage-45
- AC1 — with `GIT_CONFIG_NOSYSTEM=1` and `GIT_CONFIG_GLOBAL` at a scratch config setting `core.autocrlf=true`, `build_step_env` from a scratch directory printed `4 4 ('protocol.ext.allow', 'never') core.autocrlf` (count, pairs present, index 2, index 3); with an empty scratch config `3 3 ('protocol.ext.allow', 'never') None`. Red when, observed: a copy whose fixture asserts `GIT_CONFIG_COUNT` `"3"` exited 1 printing `isolation: FAILED · GIT_CONFIG_COUNT is not the GIT_CONFIG_KEY_<n> pairs present`.
- AC2 — `fixture isolation` under each scratch config exited 0 printing `fixture/clean · up · ok` and `GIT_CONFIG_COUNT 4 · 4 GIT_CONFIG_KEY_<n> pair(s) · pair 2 ['protocol.ext.allow', 'never']` (the scratch target's own local `core.autocrlf` makes it 4 under both); `git grep -n -e "protocol.ext.allow" -- help/upgrade-steps.md` printed lines 45 and 51, inside "What a step can reach" (lines 33 to 138).
- AC3 — `check_target_local_config` over a scratch repository named `sendemail.smtpserver` for `/usr/bin/x`, `C:/x/sendmail.exe` and `c:evil`, and `sendemail.work.smtpserver` for `/x`; for `smtp.example.com` it printed `[]`.
- AC4 — `--plant proxy-schemeless-userinfo` exited 1 refusing `http.proxy in .git/config`; no 3-character piece of `dsppass45` nor `dspuser45` was in the output; `test_credential_bearing("http.proxy", "proxy:3128")` printed `False`.
- AC5 — `--plant insteadof-dotted-userinfo` exited 1 refusing `url.https://<redacted>@host/.insteadof in .git/config`, no piece of the password printed; the predicate printed `True` for the `first.last:pw` key and `False` for `url.ssh://git@github.com/.insteadof`. Red when, observed: a copy testing the key's dot-split segments exited 1 printing `isolation: FAILED · the step was not refused naming url.https://<redacted>@host/.insteadof`.
- AC6 — `render_redacted_config("http.https://u:p@ss@h/.sslkey")` printed `http.https://<redacted>@h/.sslkey`; the two plants above and TOOL-dSafePassage-38's three printed no 3-character piece of `dsppass45` or `dsppass38` (`[]` for each).
- AC7 — `git help --config` listed 1005 keys, 17 secret-suffixed, none matching no row; with the `imap.pass` row out of a copy the probe printed `['imap.pass']`; `test_credential_bearing("sendemail.smtppass", "x")` printed `True` and `("user.signingkey", "ABCD")` `False`.
- AC8 — `take_write_lock` with `read_boot_clock` stubbed to `12345.5` and `read_pid_namespace` to `pid:[4026532221]` wrote the keys `boot_id host pid pid_ns platform started started_boot started_utc verb`, S11's set; an `ast` walk of `tools/govkit/govkit.py` found one dict literal with `started_utc`, line 7239, inside `take_write_lock`; `describe_write_lock` over the three-key subset returned `pid 999999 on host (unrecorded) running `apply`, ...`. No code moved for it.
- AC9 — `--plant submodule-ref-named-config` printed two population rows, `t/.git` and `t/.git/modules/sub`, and `fixture/status · up · ok`, exit 0; `--plant submodule-config-malformed` exited 1 refusing `` `git config --list` over .git/modules/sub exits 128, so .git/modules/sub/config does not read ``. Red when, observed: a walk copy listing any directory holding a `config` and descending into it printed `.../modules/sub/refs/heads` and `.../modules/sub/logs/refs/heads` rows and `isolation: FAILED`, exit 1.
- AC10 — `--plant gitmodules-malformed` exited 1 refusing `<target>/.gitmodules does not read: fatal: bad config line 4 in file .gitmodules`; `--plant submodule-nested-name-differs` refused `filter.canary.clean in .git/modules/nm/modules/in/config (submodule lib/p/q)`, and with `nm` de-initialised `(submodule lib/p/in, by name)`, exit 1. Found while building: a real deinit of the outer removes `lib/p/q`, the inner's `core.worktree`, and git then reads no config of the inner at all, so the check refuses naming that config; the plant recreates the empty directory so the `by name` label is what it grades.
- AC11 — `STEP_REFUSED_KEYS` printed no row among `remote.<x>.url`, `http.sslKey`, `http.cookieFile`, `http.proxy`, `remote.<x>.proxy`, `http.sslCert`; `--plant local-url-userinfo` still exited 1 refusing `remote.origin.url in .git/config`.
- AC12 — `--plant local-recent-objects-hook` exited 1, its refusal line holding `gc.recentobjectshook in .git/config`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_isolation`, every dSP-45 row with the AC3 and AC7 arms), the break was a predicate splitting the key on dots (`for text in (*key.split(".")[1:-1], value or "")`): `FAIL [dSP-45] AC4 AC5 AC6 fixture isolation insteadof-dotted-userinfo exits 1, names url.https://<redacted>@host/.insteadof …` and `FAIL [dSP-45] AC4 AC5 test_credential_bearing … wrong: [(('url.https://first.last:pw@host/.insteadof', 'https://h/'), True)]` (3 of 30). The other three staged copies the line names are covered in-arm and were not staged as separate breaks. Restored, GREEN: 30 of 30 `ok`.

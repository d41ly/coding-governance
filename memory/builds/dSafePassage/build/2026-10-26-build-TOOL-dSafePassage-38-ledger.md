**Serves:** journal TOOL-dSafePassage-38

# TOOL-dSafePassage-38 — acceptance ledger

The unit as built, at spec rev-3. `tools/govkit/upgrade_steps.py` gains `test_credential_bearing`
(the userinfo test over the value and over the key's text between its first and last dot, plus the
credential-file keys of §4) and `render_redacted_config`; `check_target_local_config` refuses every
kept row the predicate holds True for, beside `STEP_REFUSED_KEYS`, and passes each refusal entry
(key, file and submodule path) and a failed read's text through the redactor. TOOL-dSafePassage-35
S8's rows stay in `STEP_REFUSED_KEYS`: their removal is handed to TOOL-dSafePassage-44 and -45 by
§3's Edges. The `isolation` family gains `submodule-url-userinfo`, `insteadof-userinfo` and
`http-url-key-userinfo`; `tools/govkit/selftest.py` gains the `[dSP-38]` arm over them;
`help/upgrade-steps.md` states the class.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) by a probe of the changed code: the fixture CLI, or a `python -c` import of the
module by path.

Owed at the close: the `New arm:` line's RED-first observation (the `[dSP-38]` arm of
`tools/govkit/selftest.py`, red on a copy whose refusal line is built from the raw key, green
restored) and the §7 legs.

**Evidences:** TOOL-dSafePassage-38
- AC1 — `python3 tools/govkit/upgrade_steps.py fixture isolation --plant submodule-url-userinfo` exited 1 and printed `... sends as a credential, submodule.s.url in .git/config, so nothing was spawned ...`; `--plant insteadof-userinfo` exited 1 naming `url.https://<redacted>@example.invalid/.insteadof in .git/config`; `grep -c -e dspuser38 -e dsppass38` over each run's stdout and stderr printed 0, and no `isolation: FAILED` line. Red when, observed: with `test_credential_bearing` replaced by `lambda k, v: False` in the imported module, `submodule-url-userinfo` printed `isolation: FAILED · the step was not refused naming submodule.s.url in .git/config` and `... the refused step spawned`.
- AC2 — `--plant http-url-key-userinfo` exited 1 naming `http.https://<redacted>@example.invalid/.sslkey in .git/config`, with 0 token matches; `--plant local-url-userinfo` exited 1 refusing `remote.origin.url in .git/config` and printed `scp-form remote · not refused · git add exits 0`, 0 matches of `gk-planted`. Red when, observed: with `render_redacted_config` replaced by the identity, the plant printed the raw `http.https://dspuser38:dsppass38@example.invalid/.sslkey` and two `isolation: FAILED` lines.
- AC3 — a `python3 -c` probe importing `tools/govkit/upgrade_steps.py` by path printed `'http.https://<redacted>@h/.extraheader'` for `render_redacted_config("http.https://u:p@h/.extraheader")`, and `True True False False` for `test_credential_bearing` over `("branch.main.remote", "https://u@h/r")`, `("http.proxysslkey", "/k")`, `("remote.origin.url", "git@h:r")`, `("remote.origin.url", "https://github.com/d41ly/coding-governance")`.
- AC4 — `git grep -n -i -e "userinfo" -e "proxySSLKey" -e "never prints" -- help/upgrade-steps.md` printed lines 76, 81, 83 and 84, inside "What a step can reach": the class (a URL carrying userinfo in any value or key name), the credential-file keys with `http.proxySSLKey`, and `a refusal never prints the credential`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_isolation`, the dSP-38 rows), the break was a check copy building the refusal entry from the raw key (`key + …` for `render_redacted_config(key) + …`): `FAIL [dSP-38] fixture isolation insteadof-userinfo exits 1, names url.https://<redacted>@example.invalid/.insteadof in .git/config, so nothing and prints no planted credential` and the same for `http-url-key-userinfo` (2 of 3). The `submodule-url-userinfo` row has no credential in its key and holds before and after. Restored, GREEN: 3 of 3 `ok`.

**Serves:** journal TOOL-dSafePassage-44

# TOOL-dSafePassage-44 — acceptance ledger

The unit as built, at spec rev-3. `tools/govkit/upgrade_steps.py` gains `SSH_BARE_USER_SCHEMES`;
`CONFIG_USERINFO_RE` captures the scheme and the userinfo, and `test_credential_bearing` walks every
match in the key's inner text and the value with `finditer`, skipping a match whose lowercased scheme
is in the constant and whose userinfo holds no `:`. The `remote.<x>.url` and `remote.<x>.pushurl`
rows leave `STEP_REFUSED_KEYS` (§3 Edges, TOOL-dSafePassage-35), so the predicate alone grades a
remote URL. `fixture isolation` gains the `ssh-scheme-bare-user` plant. `tools/govkit/selftest.py`
gains three `[dSP-44]` checks in `check_step_isolation`, the third over a `build_staged_copy` copy
whose exemption is replaced by `True`. `help/upgrade-steps.md`, "What a step can reach", says an
ssh-scheme bare user is not refused.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) by a probe of the changed code: a scratch script importing `upgrade_steps.py` by
path, the fixture CLI, and `git grep`.

Owed at the close: the `New arm:` line's RED-first observation (the `[dSP-44]` staged copy red through
`govkit selftest`) and the §7 legs.

**Evidences:** TOOL-dSafePassage-44
- AC1 — the probe printed `[False, False, False] [True, True]` for the three ssh-scheme bare users and for `ssh://u:p@h/r` and `https://u@h/r`; `python tools/govkit/upgrade_steps.py fixture isolation --plant ssh-scheme-bare-user` exited 0 printing `fixture/clean · up · ok` and `ssh-scheme bare user · not refused · git add exits 0`. Red when, observed: the same plant through a `build_staged_copy` copy with the exemption replaced by `True` (anchor count 1) exited 1 printing `isolation: FAILED · an ssh-scheme remote with a bare user was refused`, naming `remote.origin.url` and `url.ssh://<redacted>@github.com/.insteadof`. `local-url-userinfo` and `insteadof-userinfo` still exit 1 refusing their planted credential.
- AC2 — the `negative` cell of `url-userinfo` in `tools/runlog/redaction.tsv`, read at observation, gave the tokens `ssh://git@github.com/o/r.git` and `https://example.com/a/@b`; the predicate printed `[False, False]`.
- AC3 — `git grep -n -i -e "ssh://" -e "bare user" -- help/upgrade-steps.md` printed lines 85 to 87, inside "What a step can reach" (lines 33 to 122): an ssh-scheme remote with a bare user is not refused.

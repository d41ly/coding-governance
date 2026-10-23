# TOOL-dSafePassage-44 — the credential predicate keeps an ssh-scheme URL's bare user, so an `ssh://git@host` remote is never refused, and holds itself to the repo's redaction negatives

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 10 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-44-deviation-90.md](../build/2026-10-23-build-TOOL-dSafePassage-44-deviation-90.md) | deviation | — |
| [2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-43 TOOL-dSafePassage-45 TOOL-dSafePassage-46 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 36 to 42
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md`)
confirmed finding **id 13** at HIGH, its item **D-2**, whose fix the skeptic REJECTED and corrected.
TOOL-dSafePassage-38 §4 "Data model" (`2026-10-23-spec-TOOL-dSafePassage-38.md:74`) tests userinfo
with `(?i)\b[a-z][a-z0-9+.-]*://[^/\s@]+@`. This unit ran it on node d, 2026-10-23: it matches
`ssh://git@github.com/o/r.git`, `git+ssh://git@h/r` and the key `url.ssh://git@github.com/.insteadof`,
none of which carries a credential, and it does not match the scp form `git@github.com:o/r.git`.
TOOL-dSafePassage-38 S1 and AC2 carry only TOOL-dSafePassage-35 S8's scp-form exemption, and its AC3
False cases cover only the scp and `https` forms. `tools/runlog/redaction.tsv:23` already lists
`git clone ssh://git@github.com/o/r.git` as the `url-userinfo` row's negative example. Built as
written, `update` refuses every step on a target whose remote, submodule or `insteadOf` uses the ssh
scheme form, a common setup carrying no secret. This unit is id 13's promotion, built from the
skeptic's corrected fix: a bare user under an ssh-family scheme is not credential-bearing, every other
scheme's bare user still is, and the predicate is held to the repo's own redaction negatives.

## 2. Scope (IN)

- **S1** — The exemption. `test_credential_bearing` (TOOL-dSafePassage-38 S1) tests every userinfo
  match in a tested text, and a match is exempt when its scheme, lowercased, is in
  `SSH_BARE_USER_SCHEMES` and its userinfo holds no `:`. A text is credential-bearing when it holds a
  match that is not exempt. The scheme is read from the match inside the tested text, the value or a
  key's tested part, so a key's first segment never reads as the scheme. Observed by AC1.
- **S2** — The kept refusals. `ssh://u:p@h/r` is still credential-bearing, and so is every other
  scheme's bare user, as TOOL-dSafePassage-38 AC3's True case `("branch.main.remote", "https://u@h/r")`
  requires. Observed by AC1.
- **S3** — The redaction negatives. The predicate is tested against the `negative` cell of
  `tools/runlog/redaction.tsv`'s `url-userinfo` row, read at observation time, and holds False for each
  URL that cell spells. Observed by AC2.
- **S4** — The texts. TOOL-dSafePassage-38 §5 risks and its §7 "What the check does not cover" are
  read with "the scp form and an ssh-scheme bare user are kept, since neither carries a secret", and
  the "What a step can reach" section of `help/upgrade-steps.md` says an ssh-scheme remote with a bare
  user is not refused. TOOL-dSafePassage-38's §3 hands-off bullet to this unit names the reading.
  Observed by AC3.
- **S5** — The plant. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `ssh-scheme-bare-user`: a target whose `remote.origin.url` is `ssh://git@github.com/o/r.git`
  and whose config holds `url.ssh://git@github.com/.insteadOf = https://github.com/`; its step spawns
  and the run exits 0. Observed by AC1.

## 3. Non-goals (OUT)

- The predicate's other repairs, a scheme-less proxy userinfo, a dotted subsection and a greedy
  redactor among them: `TOOL-dSafePassage-45`, which builds after this unit.
- A bare user under `git://`, `http://` or any scheme outside the ssh family, which stays refused.
- Importing `tools/runlog/runlog_lib.py`. S3 reads the table's cell in AC2's probe only, never
  from `tools/govkit/upgrade_steps.py`.

### Edges

- **consumes-from** `TOOL-dSafePassage-38` — `test_credential_bearing`, its userinfo pattern and AC3, which this unit narrows by one exemption; without them there is no predicate to correct
- **hands-off** `TOOL-dSafePassage-45` — the minors batch, which rewrites the predicate's tested text and redactor and keeps this unit's exemption and its `ssh-scheme-bare-user` plant green
- **consumes-from** `TOOL-dSafePassage-35` — S8's `remote.<x>.url` and `remote.<x>.pushurl` rows of `STEP_REFUSED_KEYS`, which this unit's pass removes so the ssh-scheme plant is refused by nothing; without the removal AC1 is red at order 10
- **hands-off** `TOOL-dSafePassage-49` — AC1 read with `STEP_REFUSED_KEYS` holding no `remote.<x>.url` or `remote.<x>.pushurl` row, AC2 with a floor naming `ssh://git@github.com/o/r.git`, and AC3 scoped to the "What a step can reach" section, findings 3, 6 and 16 of the spec audit of units 43 to 46

## 4. Design

### Data model

```
SSH_BARE_USER_SCHEMES = ("ssh", "git+ssh", "ssh+git")
for m in re.finditer(r"(?i)\b([a-z][a-z0-9+.-]*)://([^/\s@]+)@", tested_text):
    scheme, userinfo = m.group(1).lower(), m.group(2)
    if scheme in SSH_BARE_USER_SCHEMES and ":" not in userinfo:
        continue                        # a bare ssh user, not a credential
    return True
return False                            # then the credential-key table of TOOL-dSafePassage-38 §4
```

| Tested text | Credential-bearing |
|---|---|
| `ssh://git@github.com/o/r.git` | no |
| `git+ssh://git@h/r`, `ssh+git://git@h/r` | no |
| `ssh://u:p@h/r` | yes |
| `https://u@h/r` | yes |
| `git@github.com:o/r.git` | no, no `://` |

The key `url.ssh://git@github.com/.insteadOf`: TOOL-dSafePassage-38 tests its dot segments, of which
`ssh://git@github` carries the match, so the scheme reads `ssh`. A test over the whole key would read
the scheme as `url.ssh`, because the scheme class admits `.`; S1's rule reads the match inside the
tested part only.

### Inventory

Minted: the constant `SSH_BARE_USER_SCHEMES` in `tools/govkit/upgrade_steps.py` and the plant
`ssh-scheme-bare-user`. No function, conf key, gate leg or policy key. No new `raise Refusal` site, so
`tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 10, one above TOOL-dSafePassage-38 (order 9), whose predicate it
corrects. It shares `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with
`TOOL-dSafePassage-42` at order 10, so the build run sequences the two passes by M6's disjointness
rule. Between orders 9 and 10 gov's own `remote.origin.url` is `https` (TOOL-dSafePassage-38 §5), so
gov first is not refused by the defect this unit closes.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Exempting every bare user.** The skeptic's corrected fix keeps every other scheme's bare user
  refused, as TOOL-dSafePassage-38 AC3's `https://u@h/r` case requires, and a token is often written as
  a bare user, `https://<token>@host/`, so a wider exemption would pass that shape.
- **Importing `render_redacted`'s table into the step module.** TOOL-dSafePassage-38 §4 rejects the
  kit boundary; S3 reads the cell in AC2's probe, outside the shipped module, because an adopter's
  govkit may sit beside no runlog kit.

## 5. Production-readiness checklist

- security: an ssh-scheme bare user is kept, and every userinfo carrying a password, or a bare user
  under any other scheme, is still refused.
- perf / scale: one `finditer` per tested text, where one `search` ran before.
- error / empty / loading states: a text holding an exempt match and a refused one is refused.
- observability: the refusal line is unchanged; an exempt URL prints nothing.
- risks: an ssh URL whose user name is itself a secret passes; ssh authenticates by key, so a user
  name is not the credential.
- testing: the plant, the probe of AC1 and the table read of AC2, through §7.
- migration: none.
- user docs: `help/upgrade-steps.md`, S4.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path,
  `test_credential_bearing` holds False for `("remote.origin.url", "ssh://git@github.com/o/r.git")`,
  `("remote.origin.url", "git+ssh://git@h/r")` and `("url.ssh://git@github.com/.insteadof", "https://github.com/")`,
  and True for `("remote.origin.url", "ssh://u:p@h/r")` and `("branch.main.remote", "https://u@h/r")`;
  and `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant ssh-scheme-bare-user` exits 0
  with its step spawned.
  Red when: an ssh-scheme bare user is refused, or a password under the ssh scheme passes.
- **AC2** — When a `python -c` probe reads the `negative` cell of the `url-userinfo` row of
  `tools/runlog/redaction.tsv` and passes each whitespace-separated token holding `://` to
  `test_credential_bearing` as the value of `remote.origin.url`, every call holds False.
  Red when: the predicate refuses a URL the repo's own redactor lists as carrying no credential.
  figure: the tokens are DERIVED from the cell at observation; two were read on 2026-10-23.
- **AC3** — When `git grep -n -i -e "ssh://" -e "bare user" -- help/upgrade-steps.md` runs, the "What a
  step can reach" section says an ssh-scheme remote with a bare user is not refused.
  Red when: the page says every URL with a user before its host is refused.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the self-test runs the five predicate cases of AC1 and the `ssh-scheme-bare-user` plant, its failing case staged by a predicate copy with no exemption, which refuses the plant · none

What the check does not cover: an ssh scheme spelled outside the three names of
`SSH_BARE_USER_SCHEMES`, which stays refused, and a secret carried as an ssh user name.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 36 to 42's id 13 (HIGH,
  item D-2), from the skeptic's corrected fix.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 43 to 46, written by the disposal stage: `TOOL-dSafePassage-35`, `TOOL-dSafePassage-49`; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-38's `test_credential_bearing`, specced and unbuilt at the
base, and the negative example of `tools/runlog/redaction.tsv:23`, which S3 reads as test input.
`python tools/codebase-map/reuse_lookup.py "exempt an ssh url bare user from a credential check"`
ranked `check`, `checks`, `check_line` (`tools/runlog/runlog_lib.py`) and `load_affordance_exempt`,
name-token matches; `check_line` is the runlog scanner over the same table, whose `url-userinfo`
pattern keeps a bare user under 16 characters, a threshold TOOL-dSafePassage-38 §4 rejected, so no
existing seam fits beyond that spec.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's minor findings are batched and their readings carried to the faulted unit" --terms "spec audit minors batch promoted reading hands-off consumes-from order disposal rescope severity"`

# TOOL-dSafePassage-38 — a credential anywhere in a step target's config is refused by one predicate over keys and values, and no refusal line prints it

**Status:** CLOSED · rev-3 · 2026-10-28 · node d · Tier-2 · base 3708a705 · streams tooling · order 9 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-38-deviation-84.md](../build/2026-10-23-build-TOOL-dSafePassage-38-deviation-84.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-38-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-38-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-42-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-42-hygiene-fix.md) | research | TOOL-dSafePassage-39 TOOL-dSafePassage-42 |
| [2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md) | research | TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-38-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-38-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 27 to 35
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md`)
confirmed finding **id 30** at HIGH, its item **D-3**. TOOL-dSafePassage-35 S8 lists the
credential-bearing keys as instances: `remote.<x>.url` and `pushurl`, `http.proxy`,
`remote.<x>.proxy`, and `http.sslKey`, `sslCert` and `cookieFile` with their `http.<x>.` forms. Git
2.54.0's `git help --config` also lists `submodule.<name>.url`, `url.<base>.insteadOf` and
`pushInsteadOf`, `branch.<name>.remote` and `pushRemote`, `remote.pushDefault`, `http.proxySSLKey`,
`http.proxySSLCert`, and `http.<url>.*` keys whose `<url>` segment can carry userinfo; this unit read
each in that listing on node d, 2026-10-23. S8 redacts values only and says the refusal names the key,
so a refusal of an `http.<url-with-userinfo>.sslKey` row, or of TOOL-dSafePassage-29's
`http.<x>.extraHeader` and `credential.<x>` rows, prints the credential the key carries. The charter
keeps secrets out of files, memory and chat. This unit is id 30's promotion: the class is a predicate
over keys and values, and every refusal line passes keys and paths through one redactor.

## 2. Scope (IN)

- **S1** — The predicate. `test_credential_bearing(key, value)` in `tools/govkit/upgrade_steps.py`
  returns True when the value, or any key segment between the first and the last dot, holds a
  `<scheme>://` URL carrying userinfo before its host, or when the key is a credential-file key of §4
  "Data model". `check_target_local_config` (TOOL-dSafePassage-24 S2) refuses every kept row it holds
  True for, beside `STEP_REFUSED_KEYS`. It supersedes TOOL-dSafePassage-35 S8's instance list, whose
  rows it covers, and keeps S8's scp-form rule: `git@host:path` holds no `://` and is not refused.
  Observed by AC1, AC2 and AC3.
- **S2** — The redactor. `render_redacted_config(text)` in the same module returns `text` with the
  userinfo of every `<scheme>://<userinfo>@` written as `<redacted>`, scheme and host kept. Every
  refusal line `check_target_local_config` builds passes each key and each file path through it, the
  submodule rows of TOOL-dSafePassage-30 S3 included, and no refusal line prints a value.
  Observed by AC1, AC2 and AC3.
- **S3** — The plants. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `submodule-url-userinfo`, `insteadof-userinfo` and `http-url-key-userinfo`, each planting the
  user `dspuser38` and the password `dsppass38` in one key or value of the target's `.git/config`.
  Observed by AC1 and AC2.
- **S4** — The docs. The "What a step can reach" section of `help/upgrade-steps.md` says a credential
  in a URL is refused wherever it appears in a key or a value, names the credential-file keys, and says
  a refusal never prints the credential. Observed by AC4.

## 3. Non-goals (OUT)

- Credentials outside git's config, an environment token among them: TOOL-dSafePassage-7's
  environment allowlist already keeps those out of a step.
- `credential.<x>` and `http.<x>.extraHeader`, which TOOL-dSafePassage-29 already refuses by key; this
  unit adds only the redaction of the URL their key can carry.
- Executor keys: `TOOL-dSafePassage-29` and `TOOL-dSafePassage-37`.

### Edges

- **consumes-from** `TOOL-dSafePassage-35` — S8's credential rows and the `local-url-userinfo` plant, which this predicate supersedes and keeps green; without them there is no credential refusal to state as a class
- **consumes-from** `TOOL-dSafePassage-24` — `check_target_local_config` and its refusal line naming each key and its file; without it there is no line to redact
- **hands-off** `TOOL-dSafePassage-44` — the exemption of an ssh-scheme URL's bare user from `test_credential_bearing`, and §5 and §7 read with the ssh-scheme bare user kept, the repair of finding 13 of the spec audit of units 36 to 42
- **hands-off** `TOOL-dSafePassage-45` — the scheme-optional proxy test, the whole subsection as the tested key text, the greedy redactor, `STEP_CREDENTIAL_KEYS` held to a derivation, the refused table holding no credential row, and §10 read with `derive_redacted`, findings 10, 19, 20, 21, 6 and 12 of the spec audit of units 36 to 42

## 4. Design

### Data model

The userinfo test, applied to the value and to each key segment between the first and last dot:

```
(?i)\b[a-z][a-z0-9+.-]*://[^/\s@]+@
```

The credential-file keys, matched case-insensitively on the key git prints, `<x>` any one or more
segments:

| Pattern | Value rule |
|---|---|
| `http.sslKey`, `http.<x>.sslKey` | any |
| `http.sslCert`, `http.<x>.sslCert` | any |
| `http.cookieFile`, `http.<x>.cookieFile` | any |
| `http.proxySSLKey`, `http.<x>.proxySSLKey` | any |
| `http.proxySSLCert`, `http.<x>.proxySSLCert` | any |

The keys the userinfo test reaches, by where the credential sits:

| Where | Keys at writing |
|---|---|
| the value | `remote.<x>.url`, `remote.<x>.pushurl`, `submodule.<name>.url`, `branch.<name>.remote`, `branch.<name>.pushRemote`, `remote.pushDefault`, `http.proxy`, `remote.<x>.proxy`, `url.<base>.insteadOf` |
| a key segment | `url.<base>.insteadOf`, `url.<base>.pushInsteadOf`, `http.<url>.*`, `credential.<url>.*` |

A refusal line after this unit, for `http.https://dspuser38:dsppass38@host/.sslKey`:

```
step <id>: refused, the target's config declares http.https://<redacted>@host/.sslkey in .git/config
```

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: `test_credential_bearing` (cell `py.function`, verb `test`,
OK by `python tools/lexicon/lexicon.py --suggest test_credential_bearing --as py.function` on
2026-10-23) and `render_redacted_config` (verb `render`, OK by the same command); the plants
`submodule-url-userinfo`, `insteadof-userinfo` and `http-url-key-userinfo`. No conf key, gate leg or
policy key. The refusal is TOOL-dSafePassage-24's one `raise Refusal` site, so
`tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 9, after TOOL-dSafePassage-35 (order 8), whose S8 rows it
supersedes.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Extending S8's list with the keys the finding names.** The next key git adds that can hold a URL
  would pass, which is the class-as-a-list defect the finding faults.
- **Importing `render_redacted` from `tools/runlog/runlog_lib.py`.** Its `url-userinfo` rule
  (`tools/runlog/redaction.tsv:23`) redacts a bare user only when it is 16 characters or longer, and
  the step module imports no other kit; the one pattern of §4 is written beside its one caller.

## 5. Production-readiness checklist

- security: a credential in any key or value of the target's config refuses the step, and no refusal
  output carries it.
- perf / scale: one regular-expression test per kept row, inside the one `git config` read.
- error / empty / loading states: a key with no dot segment is tested on its value alone.
- observability: the refusal names the key, redacted, and its file.
- risks: an adopter whose remote URL embeds a token has every step refused until an operator moves the
  token to a credential helper; gov's own `remote.origin.url` carries no userinfo (read 2026-10-23), so
  gov first is not refused.
- testing: the three plants, the probe of AC3 and the arm of §7.
- migration: none.
- user docs: `help/upgrade-steps.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-url-userinfo`
  runs, the step is refused before any spawn naming `submodule.s.url` and `.git/config`, neither
  `dspuser38` nor `dsppass38` appears in stdout or stderr, and the run exits 1; `--plant insteadof-userinfo`
  is refused naming its key with `<redacted>` in place of the userinfo, with the same absence.
  Red when: a URL credential outside S8's list passes, or a refusal prints it.
- **AC2** — When the same family runs with `--plant http-url-key-userinfo`, the step is refused naming
  the `sslkey` key with `<redacted>` in its URL segment, neither planted token appears in the output,
  and the run exits 1; TOOL-dSafePassage-35's `--plant local-url-userinfo` is still refused and its
  scp-form case still is not.
  Red when: a key-borne credential prints in the refusal, or the scp form is refused.
- **AC3** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path,
  `render_redacted_config` returns `"http.https://<redacted>@h/.extraheader"` for the text
  `"http.https://u:p@h/.extraheader"`, and `test_credential_bearing` holds True for
  `("branch.main.remote", "https://u@h/r")` and `("http.proxysslkey", "/k")` and False for
  `("remote.origin.url", "git@h:r")` and `("remote.origin.url", "https://github.com/d41ly/coding-governance")`.
  Red when: the predicate refuses a URL with no userinfo, or misses one in a key segment.
- **AC4** — When `git grep -n -i -e "userinfo" -e "proxySSLKey" -e "never prints" -- help/upgrade-steps.md`
  runs, the "What a step can reach" section states the class, a credential-file key and the redaction.
  Red when: the page lists URL keys as instances and says nothing of keys that carry a URL.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the self-test calls `upgrade_steps.py fixture isolation` with the three plants and asserts neither planted token in the captured output, its failing case staged by a check copy that builds the refusal line from the raw key · none

What the check does not cover: a credential-file key git adds later under a name §4's table does not
carry, and a credential written in a value with no `://`, which no URL rule can tell from a path.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 27 to 35's id 30
  (HIGH, item D-3).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 36 to 42, written by the disposal stage: `TOOL-dSafePassage-44`, `TOOL-dSafePassage-45`; no other section moved.
- rev-3 · 2026-10-26 · AC3 · §7 · AC3 spells the redactor's text and result as string literals; the §7
  leg line gains `policy fixtures`, whose guard a §4 Files touched path trips, per the spec-tokens
  repair handoff
  `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md`; no
  criterion's meaning moved.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-24's `check_target_local_config` and TOOL-dSafePassage-35
S8's rows, both specced and unbuilt at the base. `python tools/codebase-map/reuse_lookup.py "redact
userinfo credentials from a url before printing"` ranked `before`, `print_report` and `render_redacted`
(`tools/runlog/runlog_lib.py:553`); the last is a real redactor over `tools/runlog/redaction.tsv`, read
and rejected in §4 for its threshold on a bare user and its kit boundary, so no existing seam fits the
step module. `git grep -n -i "userinfo"` also found `tools/unattended/unattended.sh:1129`, a shell
normaliser that strips userinfo from a remote URL for comparison, not for printing.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's promoted repairs are placed and sequenced after the unit they repair" --terms "spec audit promoted repair unit order edges hands-off consumes-from minors batch disposal rescope"`

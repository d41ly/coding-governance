# TOOL-dLoggedFlight-5 — one redaction table, applied once on read, with a staged positive per rule

**Status:** CLOSED · rev-3 · 2026-09-14 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-build-TOOL-dLoggedFlight-5-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-dLoggedFlight-5-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The extractor and the narration reader handle command text and prose from transcripts, which can hold
credentials. The only redactor in `tools/` masks `user:pass@` and nothing else. Give the runlog kit one
table of secret patterns, applied once in Python on read, each rule proven by a positive and a
near-miss negative, and cheap enough to run over every command head of a large session.

## 2. Scope (IN)

- **S1** A data table at `tools/runlog/redaction.tsv`, one row per rule, with the columns `id`, `hint`,
  `pattern`, `positive` and `negative`. `hint` is a lowercase substring prefilter, written as one or
  more substrings joined by `|`, and the rule's regex runs only on text whose lowercased form holds at
  least one of them. Observed by AC1 and AC4.
- **S2** The rule set is a CLOSED list of class ids, each covering one class the security review
  measured. It holds 17 ids, and AC5 asserts the table against the list in both directions:

  | id | class |
  |---|---|
  | `url-userinfo` | URL userinfo, both `user:pass@` and colon-less `token@` |
  | `auth-header` | `Authorization:` Bearer, Basic or token values |
  | `github-token` | `ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_` and `github_pat_` |
  | `sk-key` | anchored `sk-` and `sk-ant-` keys of 20 or more characters |
  | `aws-key` | `AKIA` access keys |
  | `pem-block` | PEM private-key blocks |
  | `env-assign` | unspaced `*_TOKEN=`, `*_SECRET=`, `*_KEY=` and `*_PASSWORD=` |
  | `env-table` | a PowerShell name-and-value env row for a secret-named variable |
  | `jwt` | JSON Web Tokens |
  | `cookie` | Cookie and Set-Cookie header values |
  | `json-secret` | JSON-keyed `token`, `password`, `secret` and `api_key` values |
  | `conn-password` | connection-string `Password=` |
  | `azure-key` | storage `AccountKey=` and SAS `sig=` |
  | `vendor-key` | vendor prefixes: `xox`, `AIza`, `sk_live_`, `npm_`, `glpat-`, `hf_` and `pypi-` |
  | `flag-secret` | `--password`, `--token`, `--api-key` and `--secret` values |
  | `lower-assign` | lowercase `token=`, `secret=`, `api_key=` and `password=` |
  | `named-token` | the `CLAUDE_CODE_MESSAGING_TOKEN` variable by name |

- **S3** Two functions, `scan_secrets(text)`, which returns the matched spans with their rule ids, and
  `render_redacted(text)`, which replaces each secret VALUE with `<redacted:<id>>` and keeps the key or
  prefix that names it. Both live in `runlog_lib.py`, the module every consumer already imports, and
  both take an optional `rules` sequence that defaults to the kit's own table: that is the seam AC4's
  counting wrapper uses. Observed by AC1 and AC2.
- **S4** The positives are written as generator templates, for example `{A36}` for 36 alphanumerics,
  and expanded only in the self-test. No committed file under the kit carries text the table itself
  flags, outside the `positive` column's templates. That is the property GitHub push protection needs
  for this public repo, checked with the table as its own scanner. Observed by AC3.
- **S5** Cost: the regex path runs only on strings whose hint matched. Observed by AC4.

## 3. Non-goals (OUT)

- Replacing the gate runner's `redact()` in `tools/run-gates/run-gates.sh`. It stays as it is; two
  kits, two stated scopes.
- Redacting journal values. The producers write no free text and no URL, so a journal line has no
  secret to redact.
- Redacting whole tool results. The extractor persists no free text (`TOOL-dLoggedFlight-6`), so the
  table runs only on text that is printed live or classified in memory.
- Entropy-based detection. It flags hashes and shas, which are this repo's everyday tokens.

### Edges

- **hands-off** `TOOL-dLoggedFlight-6` — the extractor runs this table over command heads and over
  narration printed live.

## 4. Design

Each rule compiles on its own, because one alternation was measured to change which rules match
when inline flags go global. A rule's regex names the secret VALUE with a named group `v`, so the
replacement keeps the prefix, as in `Authorization: Bearer <redacted:auth-header>`. Rules run in table
order, and a span one rule has already redacted is not matched again. The known traps are named
negatives: a `task-` id for `sk-key`, and `PIN_KEY =` and `NOT_A_TOKEN` for `env-assign`. So is
`ssh://git@` for `url-userinfo`: its colon-less form is redacted only from 16 characters, since a
login name is not a token, and every token class this table names is at least 20 long. Every
negative holds one of its own rule's hints, so the pattern, not the prefilter, is what leaves it
alone.

"Not matched again" holds two ways. Within one call, a span overlapping one an earlier rule took is
dropped. Across calls, a value that already reads `<redacted:` is skipped, so a rendered text scans
clean and rendering twice changes nothing. A template token is `{<class><count>}`, the class one of
`A` alphanumeric, `U` uppercase or digit, `L` letter, `a` lowercase or digit, `D` digit, `H` hex, `B`
base64 and `S` URL-safe, plus `{NL}` for a newline; the self-test refuses any other. A positive fits
in 196 characters, so AC4's strings stay 200 long. The loader accepts a CRLF checkout of the table,
refuses a lone CR and every other malformed row by name, and `scan_secrets` raises `TypeError` on
anything that is not a `str`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/redaction.tsv` | data, `.tsv` is a declared lexicon extension | none |
| `scan_secrets`, `render_redacted`, `load_rules` | functions in `runlog_lib.py` | `py.function`, verb-led |
| `Rule` | type | `py.type` |
| `CLASS_IDS` | constant, the 17 ids of S2 | none |

### Alternatives rejected

- A single combined regex: rejected, measured slower and different in its hits.
- Redacting with the gate runner's sed: rejected, since it misses colon-less userinfo such as
  `https://<token>@github.com`, and that was observed.

## 5. Production-readiness checklist

- security — this unit IS the control, and it is scoped: it reduces exposure in machine-local output
  and live prints, and it proves nothing about text it never sees.
- perf / scale — the prefilter keeps most strings off the regex path, which AC4 counts. The wall time
  over a large input is printed report-only; the leg's budget row is the cost verdict.
- error / empty / loading states — an empty string, a non-string input and a malformed table row each
  have a named result, and a malformed row fails the self-test rather than being skipped.
- observability — `scan_secrets` returns rule ids, so a caller can count hits per class without
  seeing a value.
- risks — false negatives for a class nobody listed. Mitigated by the table being data, so a new class
  is one id, one row and its positive.
- testing — one positive and one negative per rule, the class list asserted both ways, and the table
  scanning its own kit.
- migration — none.
- user docs — the table header comment and the kit README.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`, named in placeholder form because the files do not exist yet.

- **AC1** — When `python <kit>/selftest.py` expands each row of `<kit>/redaction.tsv`, every positive
  is changed by `render_redacted` so that its secret value no longer appears, and every negative comes
  back unchanged.
  Red when: a rule's pattern is widened to catch its own negative, or narrowed to miss its positive.
- **AC2** — When `render_redacted` redacts `Authorization: Bearer <value>` and
  `https://<value>@host/x`, the output keeps `Authorization: Bearer ` and `https://` and holds
  `<redacted:` where the value was.
  Red when: the replacement eats the prefix or leaves the value.
- **AC3** — When `scan_secrets` runs over the bytes of every tracked file under `tools/runlog/`, with
  the `positive` column of the table excluded, it finds nothing.
  Red when: a literal positive, or a fixture's planted credential, is committed instead of a template.
- **AC4** — When `scan_secrets` runs over 50,000 generated 200-character strings, 1% of which carry a
  positive, it finds every planted secret, and the count of regex searches equals the count of
  (string, rule) pairs whose hint matched. Counted by wrapping each compiled pattern. The wall time is
  printed, not graded.
  Red when: the prefilter is removed, so every rule runs on every string, or a planted secret is
  missed.
- **AC5** — When the self-test compares `CLASS_IDS` with the table's `id` column, every class id has a
  row with a positive and a negative, and every row's id is a class id.
  Red when: one row is deleted, or a row with an undeclared id is added.

## 7. Gates

`lexicon naming predicates` · `install-prefix (shipped surface)` · `govkit selfcheck` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each rule's positive staged RED by breaking its pattern · floor raised by the rule count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S2 S4 S5 · §3 · AC3 AC4 AC5 · folded round-1 spec audit H8 (the classes become
  a closed id list asserted both ways in AC5), M10 (AC3 scans the kit with the table itself rather than
  a three-shape grep), H9 (AC4's wall-clock floor becomes a count of regex searches against hint
  matches) and H5's scoping note (journal values are out of this unit's scope, since no producer writes
  free text).
- rev-3 · 2026-09-14 · S1 S3 · §3 · §4 · the build pass, before its code. S1: the hint cell holds
  several substrings joined by `|`, since `github-token` and `vendor-key` name prefixes that share no
  substring, and one hint per rule would have to be empty for them. S3: the functions' module, and the
  optional `rules` argument AC4 counts through. §3 and §10: the gate runner's `redact()` is named
  without a line number, which had moved from 117 to 120 under units 3 and 4. §4: the `ssh://git@`
  trap and the 16-character floor on colon-less userinfo, negatives that reach their own regex, the
  two readings of "not matched again", the template grammar, the 196-character bound AC4 needs, and
  the named results for a CRLF table, a lone CR and a non-string input. No criterion changed.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "redact a credential from command text"` finds no redactor beyond
`redact()` in `tools/run-gates/run-gates.sh`, which masks only `user:pass@`. No existing seam fits.
Re-run at the build pass on 2026-09-14 with the same answer. The source disagreed with rev-2 in one
place: the function sits at line 120, not 117, and the masking claim still holds, because its `sed`
needs both halves of `user:pass`.
The rule classes, their measured match counts and the false-positive traps come from the design
research record and the security review summarized in it.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

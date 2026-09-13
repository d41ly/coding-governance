# TOOL-dLoggedFlight-5 — one redaction table, applied once on read, with a staged positive per rule

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The extractor and the narration reader handle command text and prose from transcripts, which can hold
credentials. The only redactor in `tools/` masks `user:pass@` and nothing else. Give the runlog kit one
table of secret patterns, applied once in Python on read, each rule proven by a positive and a
near-miss negative, and fast enough to run over every command head of a large session.

## 2. Scope (IN)

- **S1** A data table at `tools/runlog/redaction.tsv`, one row per rule, with the columns `id`, `hint`,
  `pattern`, `positive` and `negative`. `hint` is a lowercase substring prefilter, and the rule's
  regex runs only on text holding it. Observed by AC1 and AC4.
- **S2** The rule set covers the classes the security review measured. Those are URL userinfo in both
  the colon and colon-less forms, Authorization headers, GitHub tokens, anchored `sk-` keys, AWS access
  keys, PEM private-key blocks, unspaced `*_TOKEN=`/`*_SECRET=`/`*_KEY=`/`*_PASSWORD=` assignments,
  the PowerShell name-and-value env table, JWTs, and Cookie and Set-Cookie values. Also JSON-keyed
  secrets, connection-string `Password=`, storage `AccountKey=` and SAS `sig=`, vendor key prefixes,
  `--password`/`--token`/`--api-key` flags, and lowercase `token=`/`secret=`/`password=`. Observed by
  AC1.
- **S3** Two functions, `scan_secrets(text)`, which returns the matched spans with their rule ids, and
  `render_redacted(text)`, which replaces each secret VALUE with `<redacted:<id>>` and keeps the key or
  prefix that names it. Observed by AC1 and AC2.
- **S4** The positives are written as generator templates, for example `{A36}` for 36 alphanumerics,
  and expanded only in the self-test. No committed file carries a literal that looks like a live
  credential, because GitHub push protection scans this public repo's pushes. Observed by AC3.
- **S5** Throughput: with the hint prefilter, 50,000 strings of 200 characters are scanned in under
  1 s on node `d`. Observed by AC4.

## 3. Non-goals (OUT)

- Replacing the gate runner's `redact()` at `tools/run-gates/run-gates.sh:117`. It stays as it is; two
  kits, two stated scopes.
- Redacting whole tool results. The extractor persists no free text (`TOOL-dLoggedFlight-6`), so the
  table runs only on text that is printed live or classified in memory.
- Entropy-based detection. It flags hashes and shas, which are this repo's everyday tokens.

### Edges

- **hands-off** `TOOL-dLoggedFlight-6` — the extractor runs this table over command heads and over
  narration printed live.

## 4. Design

Each rule compiles on its own, because one alternation was measured to change which rules match
when inline flags go global. A rule's regex names the secret VALUE with a named group `v`, so the
replacement keeps the prefix, as in `Authorization: Bearer <redacted:D2>`. Rules run in table order,
and a span one rule has already redacted is not matched again.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tools/runlog/redaction.tsv` | data, `.tsv` is a declared lexicon extension | none |
| `scan_secrets`, `render_redacted`, `load_rules` | functions | `py.function`, verb-led |
| `Rule` | type | `py.type` |

### Alternatives rejected

- A single combined regex: rejected, measured slower and different in its hits.
- Redacting with the gate runner's sed: rejected, since it misses colon-less userinfo such as
  `https://<token>@github.com`, and that was observed.

## 5. Production-readiness checklist

- security — this unit IS the control, and it is scoped: it reduces exposure in machine-local output
  and live prints, and it proves nothing about text it never sees.
- perf / scale — the prefilter keeps most strings off the regex path. AC4 pins the floor.
- error / empty / loading states — an empty string, a non-string input and a malformed table row each
  have a named result, and a malformed row fails the self-test rather than being skipped.
- observability — `scan_secrets` returns rule ids, so a caller can count hits per class without
  seeing a value.
- risks — false negatives for a class nobody listed. Mitigated by the table being data, so a new class
  is one row and its positive.
- testing — one positive and one negative per rule, with the known traps as named negatives: a
  `task-` id for the `sk-` rule, and `PIN_KEY =` or `NOT_A_TOKEN` for the assignment rule.
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
- **AC3** — When `git grep -nE 'gh[pousr]_[A-Za-z0-9]{36}|AKIA[0-9A-Z]{16}|sk-ant-[A-Za-z0-9_-]{20,}'`
  runs over `tools/runlog/`, it finds nothing.
  Red when: a literal positive is committed instead of a template.
- **AC4** — When `scan_secrets` runs over 50,000 generated 200-character strings, 1% of which carry a
  positive, it finds every planted secret and finishes in under 1 s.
  Red when: the prefilter is removed and the floor is missed, or a planted secret is missed.
  figure: the 1 s floor is PINNED; the measured time is printed.

## 7. Gates

`lexicon naming predicates` · `install-prefix (shipped surface)` · `govkit selfcheck` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each rule's positive staged RED by breaking its pattern · floor raised by the rule count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "redact a credential from command text"` finds no redactor beyond
`redact()` at `tools/run-gates/run-gates.sh:117`, which masks only `user:pass@`. No existing seam fits.
The rule classes, their measured match counts and the false-positive traps come from the design
research record and the security review summarized in it.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry

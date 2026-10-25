# TOOL-dPlacedRequest-31 — consent is bound to the bytes a session typed

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 11 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-31-deviation-311.md](../build/2026-10-25-build-TOOL-dPlacedRequest-31-deviation-311.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 22 at HIGH**. It shares item **H4** with finding 54, which
`TOOL-dPlacedRequest-30` closes at the writer. When two requests key alike, `TOOL-dPlacedRequest-19`
S2 appends the second session to `requests/<key>.typed` beside the first session's words, so the
second session is recorded as consenting to text it never typed, and `check_request_consent` (S5)
passes it: the forged-consent path `TOOL-dPlacedRequest-5` relies on that predicate to block. This
unit repairs `TOOL-dPlacedRequest-19`'s consent at its reader: a `.typed` line names the object id of
the bytes that session submitted, and consent holds only while the stored copy is those bytes.

## 2. Scope (IN)

- **S1** — The `.typed` line. `--request` appends `<session><TAB><blob>`, where `<blob>` is
  `git hash-object <file>` of the bytes this session submitted, once per session and blob. Observed by
  AC3.
- **S2** — The predicate. `check_request_consent <key>` returns 0 only when a line of
  `requests/<key>.typed` carries this session and the blob `git hash-object` reads from
  `requests/<key>.md` now; otherwise it returns 1 printing `TOOL-dPlacedRequest-19` S5's `relayed`
  line. A line of another shape reads as no consent. Observed by AC1 and AC2.
- **S3** — The guide. The verbs guide's `--request` row (`tools/unattended/VERBS.template.md`,
  rendered to `memory/guides/UNATTENDED-VERBS.md`) says consent is bound to the stored words.
  Observed by AC4.

## 3. Non-goals (OUT)

- No refusal of a colliding request: `TOOL-dPlacedRequest-30`'s, which keeps the second session's line
  from being written; this unit holds the boundary at the reader whatever wrote the file.
- No handling of an unset or `absent` session: `TOOL-dPlacedRequest-32`'s, which writes no line for
  one.
- No remote change: the record keeps its three fields.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-19` — `check_request_consent`, `--request` and `requests/<key>.typed`, whose line and predicate this unit binds to the words; without them there is no consent to bind
- **hands-off** `TOOL-dPlacedRequest-43` — the `.typed` blob and `check_request_consent`, which that unit's items for findings 9, 15, 29 and 42 hash with `--no-filters` and observe

## 4. Design

### The line and the read

```
--request <file>:   blob = git hash-object <file>
                    append "<session>\t<blob>" to requests/<key>.typed unless present
check_request_consent <key>:
                    now = git hash-object requests/<key>.md
                    0 if a line == "<this session>\t<now>", else 1 + relayed line
```

A copy replaced after the fact, or a line written for other words, no longer matches, so consent is
evidence of these exact bytes and not of a key.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the `.typed` append and `check_request_consent`
- `tools/unattended/unattended.test.sh`: the consent arms
- `tools/unattended/VERBS.template.md`: the `--request` row
- `memory/guides/UNATTENDED-VERBS.md`: its render

### Alternatives rejected

- **Rely on `TOOL-dPlacedRequest-30`'s refusal alone.** The predicate would still read a session line
  as consent to whatever the store holds, so any other writer of the store re-opens the path.
- **A SHA-256 of the bytes.** `git hash-object` is the object id this repository already names content
  by, and needs no second tool.

## 5. Production-readiness checklist

- security — closes forged consent: a session consents only to the bytes it submitted.
- perf / scale — one `git hash-object` per request and per consent check.
- error / empty / loading states — a missing `requests/<key>.md` reads as no consent.
- observability — the refusal is `TOOL-dPlacedRequest-19` S5's `relayed` line.
- risks — the owner's words edited in place under `requests/` lose their consent until re-recorded;
  that is the boundary working.
- testing — the probes of §6 and the arm in §7.
- migration — none: no `.typed` file exists before this build lands.
- user docs — `memory/guides/UNATTENDED-VERBS.md`; no `help/` page describes the driver's verbs.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-19`'s: a bare remote and two clones under `%TEMP%` with short
names, each a different session.

- **AC1** — When session `s1` runs `--request a.md` on clone A and a probe in `s1` calls
  `check_request_consent <key>`, it returns 0; with `<git-common-dir>/requests/<key>.md` then overwritten by a
  date-differing `b.md` of the same key, it returns 1 printing `relayed`.
  Red when: consent survives a change of the stored words, the planted case being
  `TOOL-dPlacedRequest-19`'s session-only line.
- **AC2** — When a line `s2<TAB><blob of b.md>` is planted in `<git-common-dir>/requests/<key>.typed` beside `a.md`'s
  stored copy, a probe in `s2` gets 1.
  Red when: a session reads as consenting to words it did not submit.
- **AC3** — When `awk -F'\t' 'NF != 2 || $2 !~ /^[0-9a-f]{40}$/' <git-common-dir>/requests/<key>.typed` runs after AC1's
  first request, it prints nothing.
  Red when: a line carries no blob.
- **AC4** — When `grep -n 'consent' tools/unattended/VERBS.template.md` runs, the `--request` row says
  consent is bound to the stored words.
  Red when: the guide omits it.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · a replaced store and a planted foreign line, staged against the session-only `.typed` line · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Where is the consent boundary held?** (a) At the reader, a line binding a session to a blob;
  (b) at the writer only, by refusing a collision; (c) both, the writer's half being
  `TOOL-dPlacedRequest-30`. (b) leaves the predicate trusting any line. RESOLVED (agent, 2026-10-25,
  delegated): (c), this unit building the reader's half, rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 22 (HIGH, item H4,
  shared with finding 54).
- rev-2 · 2026-10-25 · promoted fix brief: AC1 to AC3 write the node-local request files with their
  `<git-common-dir>/` prefix, so they do not read as repository paths.
- rev-3 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-19`'s `check_request_consent` and its `.typed` file; the
object id is `git hash-object`, the content name the repository already uses. `python
tools/codebase-map/reuse_lookup.py "consent bound to the exact bytes a session typed"` ranked
`boundedParallel`, `extract_session`, `measure_typed_counts` and `read_bound_key`, name stems only;
nothing in the tree reads consent, so no existing seam fits beyond the unit this repairs. `python
tools/memory-recall/query.py "how is an owner request keyed and stored on the typing node"` returned
scout B's rows and the audit's H4; none disagrees with the spec.

Recall terms used: request content key derive_content_key collision typed consent verbatim store requests

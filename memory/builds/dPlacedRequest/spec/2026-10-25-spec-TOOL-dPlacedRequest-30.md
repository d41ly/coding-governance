# TOOL-dPlacedRequest-30 — a request whose words key alike but differ is refused, never merged

**Status:** OPEN · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 11 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-30-deviation-301.md](../build/2026-10-25-build-TOOL-dPlacedRequest-30-deviation-301.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 54 at HIGH**. It shares item **H4**, "distinct owner requests share one content key
and the second is silently dropped", with finding 22, which `TOOL-dPlacedRequest-31` closes.
`TOOL-dPlacedRequest-19` S1 keys a request on `derive_content_key(text)`, which drops ISO dates, link
targets and emphasis and folds case (`tools/memory-tree/row_grammar.py:1475-1479`), so two requests
differing only in a date key alike; S2 keeps "the first copy when one exists" and S3 reports the
second's lost create as already recorded, exit 0. The second request's words are never stored,
against that unit's goal "kept verbatim". The key is the brief's shared interface I11, read by units
4, 7, 14 and 21, so re-keying is not the fix (the skeptic's corrected fix). This unit repairs
`TOOL-dPlacedRequest-19`'s writer: a request whose stored copy differs from the new words is refused
with exit 2 and a collision line, and nothing of it is written.

## 2. Scope (IN)

- **S1** — The collision refusal. `unattended.sh --request <file>`, after computing the key and before
  any write, compares the file's bytes with `<git-common-dir>/requests/<key>.md` when that copy
  exists; on any difference it prints `request not written — <key> · collision: a different text keys
  alike, the stored copy is <path>` and exits 2. It copies nothing, appends no `.typed` line, builds no
  commit and pushes nothing. Observed by AC1.
- **S2** — The same words again. Bytes equal to the stored copy keep `TOOL-dPlacedRequest-19` S2 and
  S3 unchanged: the `.typed` line, and the "already recorded" exit 0 on a lost create. Observed by AC2.
- **S3** — The verbs guide's `--request` row (`tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`) names the collision outcome and its exit code. Observed by AC3.

## 3. Non-goals (OUT)

- No new key: I11 and `derive_request_content_key` stand, and AC1 of `TOOL-dPlacedRequest-19` still
  keys a date-only difference alike.
- No consent change: what `check_request_consent` reads is `TOOL-dPlacedRequest-31`'s.
- No cross-node collision check: the record `refs/gov/requests/<key>` carries exactly three fields
  (`TOOL-dPlacedRequest-19` S3) and no digest of the words, so a node whose own store holds no copy
  cannot tell another node's different words from its own. A digest field would widen I12; it is
  recorded in §5 as a risk, not built.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-19` — `--request`, its key and its store `<git-common-dir>/requests/`, whose first-copy rule this unit replaces with a refusal; without them there is no request to refuse
- **hands-off** `TOOL-dPlacedRequest-43` — the collision compare, which that unit's item for finding 39 holds under `write_node_lock` on `requests.lock`

## 4. Design

### The order of `--request`

```
key = request.py key <file>
requests/<key>.md exists and cmp -s fails  -> collision line, exit 2, nothing written
requests/<key>.md absent                   -> copy, .typed, record   (TOOL-dPlacedRequest-19 S2, S3)
requests/<key>.md byte-equal               -> .typed, record         (TOOL-dPlacedRequest-19 S2, S3)
```

The compare is `cmp -s`, before the copy, the `.typed` append and `build_gov_commit`, so a refused
request touches no file and no ref.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `write_request_record`'s first step
- `tools/unattended/unattended.test.sh`: the collision arm
- `tools/unattended/VERBS.template.md`: the `--request` row
- `memory/guides/UNATTENDED-VERBS.md`: its render

### Alternatives rejected

- **Re-key on the raw bytes.** Re-opens I11 for its four consumers, the finder's half the skeptic
  judged unsound.
- **Keep both copies under one key with a suffix.** Every reader of `requests/<key>.md` would have to
  choose between them, and the record names one key.

## 5. Production-readiness checklist

- security — the owner's second request is never silently replaced by the first's words.
- perf / scale — one `cmp` per request.
- error / empty / loading states — a collision is exit 2 with the stored copy's path; the owner can
  reword and re-run.
- observability — the collision line names the key and the stored copy.
- risks — two nodes recording different words under one key each keep their own copy, and the remote
  record names the first; this unit cannot see that case (§3).
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md`; no `help/` page describes the driver's verbs.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-19`'s: a bare remote and a clone under `%TEMP%` with a short name,
the lease switch on, a fixture `fleet.toml`.

- **AC1** — When clone A runs `unattended.sh --request a.md` and then `--request b.md`, the two files
  differing only in an ISO date, the second exits 2 printing `collision`, `<git-common-dir>/requests/<key>.md` is
  byte-identical to `a.md`, `grep -c '' <git-common-dir>/requests/<key>.typed` is unchanged, and the remote ref is
  unmoved.
  Red when: the second request exits 0 or writes anything, the planted case being
  `TOOL-dPlacedRequest-19`'s first-copy rule.
- **AC2** — When clone A runs `--request a.md` twice, the second prints that the request is already
  recorded and exits 0.
  Red when: an identical request is refused as a collision.
- **AC3** — When `grep -n 'collision' tools/unattended/VERBS.template.md` runs, the `--request` row
  names the outcome and exit 2.
  Red when: the guide omits it.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · a date-differing pair and an identical pair, staged against the first-copy rule · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What does a second, different request under one key get?** (a) Refused, exit 2, nothing
  written; (b) re-keyed on its raw bytes; (c) stored beside the first. (b) re-opens I11 for four
  consumers; (c) gives one key two texts. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the
  skeptic's corrected fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 54 (HIGH, item H4,
  shared with finding 22).
- rev-2 · 2026-10-25 · promoted fix brief: AC1 writes the node-local request files with their
  `<git-common-dir>/` prefix, so they do not read as repository paths.
- rev-3 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-19`'s `write_request_record` and its store; the normaliser
it keys on is `derive_content_key` (`tools/memory-tree/row_grammar.py:1475`), read at source. `python
tools/codebase-map/reuse_lookup.py "refuse a second request whose text differs but keys alike"`
ranked `read_text`, `key`, `keys` and `write_text`, name stems only; nothing in the tree stores a
request, so no existing seam fits beyond the unit this repairs. `python tools/memory-recall/query.py
"how is an owner request keyed and stored on the typing node"` returned scout B's rows for units 14
and 19, the audit's H4 and unit 19's §4; none disagrees with source.

Recall terms used: request content key derive_content_key collision typed consent verbatim store requests

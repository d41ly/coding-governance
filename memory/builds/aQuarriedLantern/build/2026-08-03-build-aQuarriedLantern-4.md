# TOOL-aQuarriedLantern — closing-review fixes, group G3 (the alias diagnosis, and the bookkeeping)

**Serves:** journal TOOL-aQuarriedLantern-1  <!-- inferred: this build defines exactly one spec id, so the record can serve nothing else -->

Items F7 and F14 from
`memory/tooling/builds/2026-08-03-TOOL-aQuarriedLantern/reviews/2026-08-03-review-aQuarriedLantern-2.md`.
Every number below came from a command run in-session, against a GREEN baseline of
`MRECALL_NESTED=1 python tools/memory-recall/selftest.py` **19/20, 1 skipped, exit 0** at `812bc3c`.
The shell was probed as `Msys` before anything was scored.

**Applied** 2026-08-03 · node `a` · base `812bc3c`

## F7 — an alias layer that joined to ZERO records was reported nowhere

`query.py:264` was `E.join_aliases(records, E.load_aliases()[0])`, discarding the int that
`extract.py` documents as "how many were augmented" and prints on its own path. The CLI — the path
every session actually uses — printed no equivalent, and `--stats` carried `alias_digest`, a content
hash for cache keying that says nothing about coverage. An adopter authoring aliases against the
wrong id family gets a 100%-dead third FTS5 column whose only symptom is slightly worse ranking.
The dead-plumbing class, one layer inside the tool built to close it.

Four edits, all in `tools/memory-recall/query.py`:

- `_docs` now returns a third value — `{"ids", "joined", "src"}` — instead of dropping the join
  count on the floor.
- `build_cache` carries it into the manifest as `aliases`, beside `alias_digest`. In the MANIFEST
  on purpose: the record arm's diagnosis reads its counts from there so it fires identically on a
  fresh build and on a cache hit, and this one had to behave the same way.
- `dead_alias_diagnosis(man)` prints `DEAD ALIAS LAYER`, the alias source and the resolved
  FAMILIES, in the same shape as the record arm's block, on stderr right behind it.
- `CACHE_VERSION` 2 → 3. A manifest built before this fix has no alias counts at all, so without
  the bump a warm cache keeps the exact silence the fix removes.

Deliberately silent on a PARTIAL join: an alias file written ahead of the records it names is a
normal, healthy state, and a rule that fired there would red the success case.

The fork header's construct (6) now names three diagnoses rather than two; the count stays at six.

### Gate

New selftest arm `t_dead_alias_is_loud` (registered in `main()`'s `order`, so the
declared-vs-ran assertion counts it): one alias id from a foreign family (`ZZZZ-aFoo-1`) against the
two-record fixture, asserting the record arm is UNAFFECTED (2 records), the diagnosis names the
source and the families, the manifest reads `(ids 1, joined 0)`, the SECOND query — the cached path
— still diagnoses, and a hand-doctored pre-fix manifest (no `aliases` key, `version` 2) forces a
rebuild instead of serving the silence.

Both success states are pinned NEGATIVE in the same pass, because a diagnosis that fires on a
healthy corpus is worse than none: `t_empty_alias` (no alias file) and `t_alias_rebuild` (1/1
joined) both assert `DEAD ALIAS LAYER` is absent, and the latter now also asserts the manifest
recorded the live join.

### Mutations — four applied, each asserted APPLIED on disk before scoring, all KILLED

| # | mutation | result |
|---|---|---|
| M1 | the diagnosis is computed but not printed | KILLED — 19/21, `a 100%-dead alias column stayed silent` |
| M2 | `"aliases": {}` in the manifest | KILLED — 18/21, `KeyError: 'joined'` + the silence |
| M3 | the join return discarded again, `joined` assumed = `ids` | KILLED — 19/21, the silence |
| M4 | `CACHE_VERSION` left at 2 | KILLED — 19/21, `a pre-fix manifest was served from cache` |

Post-revert baseline re-run: **20/21, 1 skipped, exit 0**.

## F14 — the spec Status was frozen at SPECCED three commits after the build landed

`spec/2026-08-03-spec-aQuarriedLantern-1.md` line 3 → **INPROGRESS**, with the header tail saying
U1–U3 are built and the closing review folded, and naming why this is not CLOSED.

Not CLOSED, and that is measured, not asserted: flipping the token to `CLOSED` on the same bytes
reds hygiene check 12 with `terminal Status with unresolved §8 Open questions`, **exit 1**; reverting
to INPROGRESS returns **exit 0**. §8 still carries Q1, Q4, Q5 and the deliberately-open Q6 (whether
retrieval earns its keep in a 468 KB corpus), so INPROGRESS is the honest state and check 12 agrees.

Ledger row in `memory/project/in-flight/a.md` updated in the same commit: still `in-flight`, now
reading `U1-U3 landed; closing review aQuarriedLantern-2 folded (F1-F14, 3 groups); pre-push`.

One deviation from the review's fix text, stated: it asks for `merged:<sha>`. This unit commits
directly onto `main` rather than merging a branch, so the only candidate sha is the commit that
carries the row itself — unwritable without an amend that changes it again. Nothing is pushed, and
push-state derives from git ancestry anyway (`pushed:` is retired), so the row stays `in-flight`
until the push lands. Flip it to `merged:<sha>` on the next session's ledger self-prune.

## Gates — all green, run sequentially over the final bytes

The legs ran one after another on purpose: two concurrent kit selftests would both read this repo's
live query log, and the log-identity arm cannot tell a torn read from a gate that wrote to it.

- `bash tools/run-gates.sh` — **18/18 legs passed, 1 skipped** (`manifest-check self-test —
  unchanged vs main`), exit 0.
- `python tools/memory-recall/selftest.py` — **21/21 checks passed, exit 0** (was 20/20 at
  `812bc3c`); the nested adopter-layout run inside it reports `20/21, 1 skipped`.
- `bash tools/check-wiring.sh` — hooks ok · agent-cap ok · recall on its true `skip` (the opt-in is
  not taken in this repo), exit 0.
- `bash tools/check-wiring.test.sh` — **18 passed, 0 failed**, exit 0.
- `bash tools/memory-tree/check-memory-hygiene.sh` — exit 0, silent, and re-run after this file
  existed.
- `bash tools/check-kit-versions.sh` — exit 0.
- `bash tools/memory-recall/recall-opened.test.sh` — **8 passed, 0 failed**, exit 0.
- `python tools/settings-merge.py --selftest` — PASS, exit 0.
- `git diff --cached --stat` byte-identical to `--stat --ignore-cr-at-eol`, so nothing became a
  whole-file CRLF rewrite; `git diff --cached --check` clean.

# TOOL-aFoldedQuarry-4 — U2: the generated build index replaces the authored tree

**Status:** CLOSED · rev-2 · 2026-08-08 · node a · Tier-2 · base 42c3f4dc · streams tooling · ratified 2026-08-08

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-08-review-TOOL-aFoldedQuarry-1-7.md](../../reviews/2026-08-08-review-TOOL-aFoldedQuarry-1-7.md) | diff-review | TOOL-aFoldedQuarry-1 TOOL-aFoldedQuarry-2 TOOL-aFoldedQuarry-3 TOOL-aFoldedQuarry-5 TOOL-aFoldedQuarry-6 TOOL-aFoldedQuarry-7 |
| [2026-08-08-review-TOOL-aFoldedQuarry-4-3.md](../../reviews/2026-08-08-review-TOOL-aFoldedQuarry-4-3.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

Retire `gen-memory-tree.sh` and the directory listing it generates, and replace them with an index
derived from what a build actually declares: its README front matter and the status header of every
spec under it. A build's status becomes a pure function of its unit statuses, so nothing is authored
and nothing rots.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/gen_build_index.py` reads exactly two sources and nothing else: each
  build's README front matter (`slug`, `node`, `opened`, `streams`, `roster`, `ids`) and every
  `**Status:**` header under that build's `spec/`, at any depth.
- **S2** — it renders three things: the generated region inside each build's `README.md`,
  `<MEMORY_ROOT>/LIVE.md`, and `<MEMORY_ROOT>/ledger/<month>.md` shards keyed on the build's
  `opened` month.
- **S3** — a build's status is DERIVED, never authored: `INPROGRESS` if any unit is, else `BLOCKED`,
  else `OPEN`, else `SPECCED`, else `DEFERRED`, else `WONTDO` when every unit is, else `CLOSED`.
  Exactly ONE source of truth per build. When any spec under the build carries a parseable status
  header the status is derived and an authored `status:` in the front matter is an ERROR; when NO
  spec carries one — four builds in this corpus are grandfathered and have none — `status:` is
  REQUIRED and its absence is a named error. The answer is never invented.
- **S4** — `--check` byte-compares every rendered artifact against a fresh render and names each
  stale file; `--write` rewrites them; `--selftest` runs the unit's own fixtures.
- **S5** — the three blind spots upstream found inside this child are closed by construction, each
  with its own armed test: a README with NO marker pair is a NAMED ERROR rather than a silent
  departure from the universe; an ORPHANED generated file (a `<MEMORY_ROOT>/ledger/` shard a fresh
  render would not produce) is reported by `--check` and removed by `--write`, bounded to a path
  matching the month-shard name and nothing else, because a generator that deletes inside the memory
  tree on its own authority is a data-loss path; and an ABSENT or unparseable README produces a named
  error on both `--check` and `--write`, never a traceback.
- **S6** — hygiene check 9 stops delegating to the tree generator and starts delegating to this one.
  `gen-memory-tree.sh` and `<MEMORY_ROOT>/TREE.md` are deleted; `LIVE.md` and `ledger/` join the
  sanctioned root set, the index set, and the size caps.
- **S7** — the seven build folders that have no `README.md` gain one, because a build with no front
  matter cannot be indexed and silence is what this unit exists to remove.
- **S8** — `.gitattributes`, `memory/README.md`, `HYGIENE.template.md`, `SPEC-TEMPLATE.template.md`,
  `adopt-memory-tree.sh`, `AGENTS.md` and `README.md` stop naming the retired generator.
  `memory/README.md` also LINKS it, so that line reds hygiene check 2 if it is missed.
- **S9** — `.gitattributes` REPLACES its `TREE.md` pin with `eol=lf` pins on `LIVE.md` and the ledger
  shards, and the adopter documentation says why: `--check` byte-compares tracked bytes against an
  LF render, so an unpinned generated file on a Windows checkout reds every line, and passes only
  when the working copy happens to have just been rendered.

## 3. Non-goals (OUT)

- A directory listing. The retired file listed paths, which git already lists better. The
  replacement carries STATUS, which git does not.
- Reading anything but the two declared sources. No git history, no file mtimes, no scanning of
  `build/` or `reviews/`. A source the renderer does not read cannot make the render drift.
- Rewriting authored README prose. The generator owns exactly the region between its two markers.
- Month-shard rotation policy. A month shard freezes when the month passes because its inputs stop
  changing; no rotation rule is needed and none is written.

## 4. Design

### Data model

Front matter sits at the top of a build `README.md`, between two `---` lines, keys at COLUMN 0:

```
---
slug: aFoldedQuarry
node: a
opened: 2026-08-08
streams: tooling
roster: TOOL
ids: TOOL-aFoldedQuarry-1..6
---
```

`slug` must equal the folder name. `streams` values must be in the `DISCIPLINES` enum. `roster` is
the `+`-joined FAMILY set. `opened` is the date that selects the month shard. `status:` is the
optional seventh key, legal ONLY when no spec under the build carries a parseable header.

Front matter opens at LINE 1 and nowhere else, and closes at the first subsequent `---`. A `---` is
also a markdown horizontal rule, and one already separates the two merged halves of
`builds/aPrunedCeremony/README.md`; a parser that scans for the first two `---` anywhere would read
that whole half as front matter. A README whose line 1 is not `---` has NO front matter, which is a
named error, not a scan that wanders into the body.

The generated region is delimited by a marker PAIR, and both markers must be present:

```
<!-- gen:build-index -->
… rendered rows …
<!-- /gen:build-index -->
```

### Inventory

| Artifact | Owner | Content |
|---|---|---|
| `builds/<slug>/README.md` region | generator | one row per spec: id, unit title, status, rev, date |
| `<MEMORY_ROOT>/LIVE.md` | generator | every build whose derived status is not terminal |
| `<MEMORY_ROOT>/ledger/<month>.md` | generator | every build opened that month, with its derived status |

### Migration

`gen-memory-tree.sh` and `TREE.md` are deleted in the same commit that adds the generator and its
gate leg, so check 9 is never pointing at a script that is gone. Seven READMEs are authored; the
seven existing ones gain front matter and a marker pair.

### Rollout

One commit. The generator, the seven new READMEs, the front matter on the other seven, the rendered
artifacts, the check-9 swap, the deletions, and the doc updates.

### Files touched (estimate)

Two kit scripts (one new, one deleted), the hygiene gate, fourteen build READMEs, three new generated
artifacts, and six documents.

### Alternatives rejected

- **Keep the directory listing alongside the new index.** Rejected: two generated indexes over one
  tree is two things to keep in sync, and the listing's only content is what `git ls-files` prints.
- **Derive the build status from its backlog row.** Rejected: the backlog is mutable and authored,
  which is exactly the rot this unit removes. The spec headers are the units' own statements.
- **Make the README optional and index only from spec headers.** Rejected: `node`, `opened` and
  `roster` have no other home, and an unindexed build is precisely the silent-departure blind spot
  S5 exists to close.

## 5. Production-readiness checklist

- security — N/A. The generator reads tracked markdown and writes tracked markdown.
- perf / scale — one pass over the tracked file list, one read per README and per spec. Linear.
- a11y — N/A — no user interface.
- i18n — N/A.
- error / empty / loading states — a tree with no builds renders an empty `LIVE.md` and no shards,
  and that is a clean pass, not a crash. Every error names its file.
- observability — `--check` prints one line per stale or orphaned artifact, with the reason.
- risks — the generator OWNS a region inside an authored file. Getting the marker handling wrong
  would eat prose, so the marker pair is validated before any write and the region is replaced by
  exact slice, never by regex substitution over the whole file.
- testing + left-shift gates — `--selftest` plus the hygiene self-test's check-9 arms.
- migration / rollback — one commit; revert restores the old generator and its file.
- user docs — `HYGIENE.template.md` and `SPEC-TEMPLATE.template.md` describe the front matter.

## 6. Acceptance criteria

- **AC1** — When `--check` runs over an unmodified tree it exits 0; when any generated region or
  artifact is edited by hand it exits non-zero naming that file.
- **AC2** — When a build README has an opening marker but no closing one, `--check` and `--write`
  both fail naming that README, and the build does NOT silently vanish from `LIVE.md`.
- **AC3** — When a `<MEMORY_ROOT>/ledger/` shard file exists that a fresh render does not produce,
  `--check` reports it as orphaned and `--write` deletes it; a file inside `ledger/` that does not
  match the month-shard name is reported and LEFT ALONE. `LIVE.md` is excluded from this criterion:
  it is rendered whole every time, so a stale row cannot survive a render and the assertion would be
  unfalsifiable.
- **AC4** — When a build folder has specs but no `README.md`, both modes fail with a named error and
  no traceback.
- **AC5** — When every unit of a build reaches a terminal status, the build leaves `LIVE.md` on the
  next render without anyone editing a status by hand.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it exercises AC2,
  AC3, AC4, AC5 and both arms of the `status:` rule against fixtures in a temporary directory,
  touching no tracked file, and prints its pass line last.
- **AC8** — When a build whose specs carry no parseable header also carries no `status:`, both modes
  fail naming that build; when such a build carries `status:`, it is indexed at that status; when a
  build with parseable headers ALSO carries `status:`, both modes fail naming the conflict.
- **AC7** — When the hygiene gate runs, check 9 delegates to this generator, and `gen-memory-tree.sh`
  and `<MEMORY_ROOT>/TREE.md` are absent from the tree.

## 7. Gates

`bash tools/run-gates.sh` in full. Check 9 inside `tools/memory-tree/check-memory-hygiene.sh` becomes
this generator's `--check`. A new leg runs `--selftest`. The kit/dogfood doc parity leg covers the
two templates this unit rewrites.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — is a build README required?** Options: required for every build, or optional with the
  index derived from spec headers alone. RESOLVED (owner, 2026-08-08): required. Three of the six
  front-matter fields have no other home, and an optional README reintroduces the silent-departure
  blind spot as a supported configuration.
- **Fork B — where the front matter lives.** Options: a `---` block at the top, or HTML comments.
  RESOLVED (owner, 2026-08-08): the `---` block, keys at column 0. It is the shape every other tool
  in this repo already reads, and column 0 is machine-checkable, whereas a key indented under a
  parent is silently dropped by a simple parser — a defect upstream paid for in its own front matter.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 3: G1 adds the `status:` fallback and its two-way error (four
  builds in this corpus have no parseable unit status at all — the review said three and the fourth
  was found by counting); G2 adds S9, the LF pin without which
  the byte-compare gate reds on a Windows checkout; G3 bounds the orphan delete to the month-shard
  name; G4 pins front matter to line 1; G5 narrows AC3 off `LIVE.md`; G6 names the link in
  `memory/README.md`.

## 10. Reuse audit

The generator replaces a kit script rather than joining it: `gen-memory-tree.sh` is deleted, so the
kit keeps exactly one index generator. Check 9's delegation seam already exists — the hygiene gate
already shells out to a sibling generator's `--check` and reports its stdout as drift, so only the
script name changes. The gate leg registers in `tools/gate-legs.json`, which `tools/run-gates.sh`
already iterates. The status vocabulary is the kit's existing seven tokens from HYGIENE check 8, not
a new enum, and the spec status header the generator parses is the one check 12 already validates —
so the generator never has to defend against a malformed header, because a malformed header is
already a hygiene failure. The one genuinely new thing is the marker-pair region write, and its
hazard (owning a slice of an authored file) is why S5 and AC2 exist.

# KICK-dKeptSession-46 — every fill reader passes the projects root it already resolved, so the window is derived under the tree the reader reads

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 14 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-46-deviation-461.md](../build/2026-10-26-build-KICK-dKeptSession-46-deviation-461.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 38 at HIGH**, report item **H1**. Id 28 shares the item and is promoted as
`KICK-dKeptSession-45`, which resolves the default root; this unit removes the default from the
paths that have a root of their own.

`KICK-dKeptSession-30` S2 derives the window two ways: `measure_context_fill` under the
transcript's parent's parent, and `derive_context_fill(ev)` under the default root, so that
`KICK-dKeptSession-9`'s per-stage rows "read the same window with no change to their call". Unit 9
reads its sessions from `<dir>`, the `--orient` argument, yet its `context` column would derive the
window under whatever root the process environment names. In the runlog selftest that is
`build_arm_env`'s decoy (`tools/runlog/selftest.py:1514-1520`), and on a node it is the real tree,
so one transcript reads one share from `runlog.py context` and another from unit 9's column. This
unit makes every caller pass the root it resolved. It repairs `KICK-dKeptSession-30` and builds one
step after it (order 14).

## 2. Scope (IN)

- **S1** — id 38. The signature. `derive_context_fill(ev, *, window=None, root=None)` in
  `tools/runlog/extract.py` takes `window`, or derives it as `derive_context_window(ev["model"],
  root=root)`; with neither, it raises `ValueError("derive_context_fill: pass window= or root=")`.
  It never falls back to a default root. Observed by AC1 and AC3.
- **S2** — id 38. Unit 9's reader. `measure_orient_tree(root, repo, slug)`
  (`KICK-dKeptSession-9` S1) computes each row's `context` as `derive_context_fill(ev, root=root)`,
  `root` being its own first argument, the `--orient <dir>` it reads. Observed by AC1.
- **S3** — id 38. The context verb. `runlog.py context <transcript>` keeps unit 30 S2's root, the
  transcript's parent's parent, passed to `derive_context_window` as `root=`; a transcript under
  `<dir>/<project>/` therefore reads the window under the same `<dir>` unit 9's row reads it under.
  Observed by AC2.
- **S4** — id 38. The sibling text superseded by name. `KICK-dKeptSession-30` S2's "or derives one
  from `ev["model"]` under the default root, so `KICK-dKeptSession-9`'s per-stage rows read the same
  window with no change to their call", and `KICK-dKeptSession-9` S2's call `derive_context_fill(ev)`,
  read as S1 and S2 here, each answered in its unit's acceptance ledger. Observed by AC3.

## 3. Non-goals (OUT)

- The default root itself: id 28, `KICK-dKeptSession-45`.
- How often the window is derived per run: the batch's items for ids 10, 20 and 45,
  `KICK-dKeptSession-56`.
- The window's rungs and observation: `KICK-dKeptSession-30`.

### Edges

- **consumes-from** `KICK-dKeptSession-30` — `derive_context_fill` and `derive_context_window`, whose root this unit makes the caller's (id 38)
- **consumes-from** `KICK-dKeptSession-9` — `measure_orient_tree`'s per-row `context` call, which this unit passes its own root
- **hands-off** `KICK-dKeptSession-56` — the caller-passed root, under which the batch's items for ids 10, 20 and 45 derive the window once per model and root
- **hands-off** `KICK-dKeptSession-62` — the context verb's root and AC1, which the batch's S10 and S26 widen to agent transcripts and re-observe (ids 11, 37)

## 4. Design

### Evidence

- `build_arm_env(base)` copies `os.environ` and aims every `DECOY_VARS` root at the arm's scratch
  (`tools/runlog/selftest.py:1516-1521`), so a reader that resolves its own root inside an arm reads
  the decoy, never the arm's fixture.
- `runlog.py`'s other verbs resolve `resolve_projects_root(override=args.transcripts)` once per
  call (`tools/runlog/runlog.py:300`, `:324`): a reader takes a root it was given, never one of its
  own.
- `KICK-dKeptSession-9` S2 calls `derive_context_fill(ev)` for every main and agent file row.

### The calls

```
measure_context_fill(t)                  -> window under t.parent.parent         (unit 30 S2, unchanged)
measure_orient_tree(dir, ...)            -> derive_context_fill(ev, root=dir)    (S2)
runlog.py context t                      -> measure_context_fill(t)                  (S3)
derive_context_fill(ev)                  -> ValueError                           (S1)
```

### Inventory

No identifier is minted. `derive_context_fill` gains a keyword-only `root`.

### Migration

None: unit 9 and unit 30 are unbuilt at this base, so no tracked caller spells the old call.

### Files touched (estimate)

- `tools/runlog/extract.py`: S1, and S2 in `measure_orient_tree`
- `tools/runlog/selftest.py`: the cases of §6

### Alternatives rejected

- **A default root kept for callers that pass none.** It is the escape this unit closes: a caller
  that forgets reads a tree it never named.
- **The window computed inside unit 9 and passed as `window=`.** It works, but leaves the default
  path open to the next caller; a required root closes the class.

## 5. Production-readiness checklist

- security — transcripts read only, as before.
- perf / scale — unchanged per call; the call count is the batch's item for id 20.
- error / empty / loading states — S1's `ValueError` names the remedy; a root holding no
  observation reads unit 30's bottom rung.
- observability — `runlog.py context` already names the window's source.
- risks — a future caller must pass a root; S1 refuses loudly where it does not.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — none: no page under `help/` names the reader's signature.

## 6. Acceptance criteria

The fixture is unit 9's `--orient` projects dir under `%TEMP%`, holding unit 30's
`context-window-sibling` transcript as a session whose `Edit` follows its 900000-token turn, read
inside `build_arm_env`.

- **AC1** — When `python runlog.py extract --orient <dir> --slug fx --repo <repo>` runs inside
  `build_arm_env`, the row's `context` reads `90%`.
  Red when: the window is derived under the decoy root, which holds no observation and reads `450%`.
- **AC2** — When `python runlog.py context <transcript>` runs inside `build_arm_env` on AC1's
  transcript under `<dir>`, it prints `90%`, the same share as AC1's row.
  Red when: the two readers print two shares for one transcript.
- **AC3** — When a probe calls `extract.derive_context_fill(ev)` with neither `window` nor `root`,
  it raises `ValueError` naming `root=`.
  Red when: the call returns a share derived under a root nobody passed.

## 7. Gates

`runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runlog/selftest.py · covers AC1 AC2 AC3 · the sibling transcript under an `--orient` dir inside the decoy environment, staged red by a copy of `derive_context_fill` that falls back to the default root · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H1 (id 38).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared

## 10. Reuse audit

The seams reused are unit 30's `derive_context_window`, whose `root` argument this unit fills, and
the pattern of `runlog.py`'s verbs, each resolving one root and passing it down
(`tools/runlog/runlog.py:300`); nothing is minted. `python tools/codebase-map/reuse_lookup.py "resolve
the transcripts projects root honouring CLAUDE_CONFIG_DIR"` ranked `resolve`, `repo_root` and
`resolve_kit_dir` by name stem; none resolves a transcripts root, and the source read above is the
seam.

Recall terms used: `python tools/memory-recall/query.py "which projects root does a per-row
context fill read" --terms "derive_context_fill measure_orient_tree root window build_arm_env decoy
resolve_projects_root transcripts orient per-stage"`

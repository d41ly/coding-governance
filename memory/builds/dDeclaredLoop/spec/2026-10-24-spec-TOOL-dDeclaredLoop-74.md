# TOOL-dDeclaredLoop-74 — a FETCH_HEAD counts as a fetch only when it holds the default branch of the resolved remote

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 38 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-75 |
| [2026-10-24-build-TOOL-dDeclaredLoop-74-deviation-741.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-74-deviation-741.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-75 |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-75 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 45 at HIGH**, its item **H7**; its other-branch half is item M6 at medium (id 8),
batched into `TOOL-dDeclaredLoop-75`. `TOOL-dDeclaredLoop-65` S1 takes any `FETCH_HEAD` mtime as the
time of the last fetch, with no look at the file's content. A failed fetch, an unreachable remote or a
branch that does not exist, truncates `FETCH_HEAD` to 0 bytes with a current mtime, so an offline run
reads `remote: fresh · from FETCH_HEAD` and the engine ranks `act` above `stale-remote` on a stale base.
65's AC3 only backdates mtimes and cannot see it.

This unit makes the file's content validate its mtime. It repairs `TOOL-dDeclaredLoop-65`.

## 2. Scope (IN)

- **S1** — A `FETCH_HEAD` joins 65 S1's population only when it is non-empty and holds a line naming
  the default branch of the resolved remote, `<sha>\t<flag>\tbranch '<default>' of <url>`, where `<url>`
  equals the remote's `git remote get-url <remote>` once each is stripped of a trailing `/` and a trailing
  `.git`. Any other `FETCH_HEAD` is skipped, and its path is named on the `--explain` read-set as
  `skipped — <empty | no line for <default> of <remote>>`. Observed by AC1, AC2.
- **S2** — With every `FETCH_HEAD` skipped, the reading falls through to 65's other sources, the tracking
  ref's reflog and the clone entry, unchanged; with none of them it is `unread` and `stale-remote`, as 65
  S2 says. Observed by AC1.
- **S3** — The fixture case `failed-fetch` joins `position.py --fixture`: every source backdated past the
  bound, then `git fetch` against an unreachable URL, and the answer is `stale-remote`. Observed by AC1.

## 3. Non-goals (OUT)

- The other-branch fetch's own plant: the audit's id 8, batched into `TOOL-dDeclaredLoop-75`. S1 already
  skips that file; the plant is that unit's.
- The relative `--git-common-dir` and the fixture's inherited git config: ids 15 and 25, batched into
  `TOOL-dDeclaredLoop-75`.
- A checklist entry that a freshness signal taken from an mtime is validated by content, the finding's
  left-shift: the class is recorded at the close; S3 is this reading's failed-writer fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-65` — the last-fetch population of S1 in `tools/loop/position.py`, whose `FETCH_HEAD` members this unit validates by content
- **hands-off** `TOOL-dDeclaredLoop-75` — the validated population, beside which that unit plants the other-branch fetch, resolves the common directory absolutely and isolates the fixture's git config (ids 8, 15, 25)
- **hands-off** `TOOL-dDeclaredLoop-77` — S1's URL normalisation, which that unit spells as git writes the URL into `FETCH_HEAD`, its user part stripped from both sides (the round-4 spec audit's id 8)

## 4. Design

### Evidence

Probed 2026-10-24 on node `d`, git 2.54.0.windows.1, in a scratch clone under `%TEMP%`: PINNED, that date.

- After `git fetch`, `FETCH_HEAD` held `<sha>\t\tbranch 'main' of C:/Users/.../up` and a
  `not-for-merge` line for the other branch.
- `git fetch origin other` rewrote it to the single line `branch 'other' of ...`, with no `main` line.
- With the remote's URL set to `.../up/`, the line still read `of .../up`, without the trailing slash.
- With the URL pointed at a path that does not exist, `git fetch` exited 128 and left `FETCH_HEAD` at 0
  bytes.

### The reading, restated

```
remote, default = 65's resolved remote and default branch
want  = normalise(git remote get-url <remote>)                   # strip one trailing "/" then ".git"
for f in <common>/FETCH_HEAD, <common>/worktrees/*/FETCH_HEAD:
    lines = f's lines, where f exists
    keep f when some line matches  ^[0-9a-f]{40,64}\t[^\t]*\tbranch '<default>' of (.+)$
                                   and normalise(\1) == want
times = mtimes of kept files + 65's reflog and clone sources, unchanged
```

### Files touched (estimate)

- `tools/loop/position.py`

### Alternatives rejected

- **The size check alone.** A fetch of another branch writes a non-empty file and leaves the default
  branch's tracking ref as stale as before.
- **Matching the branch and ignoring the URL.** A fetch from a second remote names its own `main`.

## 5. Production-readiness checklist

- security — reads only.
- perf / scale — each `FETCH_HEAD` read once, a few lines.
- error / empty / loading states — an empty or unreadable file is skipped and named, never fresh.
- observability — S1's skip line names the file and why.
- risks — a remote URL git rewrites beyond the trailing `/` or `.git` reads skipped, the conservative side;
  `--explain` names it.
- testing — AC1 and AC2 as fixture plants; the arm under §7, observed at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant failed-fetch` backdates every source past the bound
  and fetches from an unreachable URL, the answer is `stale-remote` and the read-set names `FETCH_HEAD`
  as `skipped — empty`.
  Red when: the truncated file's fresh mtime is counted and the answer reads fresh.
- **AC2** — When `--plant quiet-remote` (65 AC2) fetches the default branch of the resolved remote, the
  line still ends `from FETCH_HEAD`.
  Red when: the content check rejects a real fetch of the default branch.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop position fixtures` leg (`TOOL-dDeclaredLoop-7`) green, which
runs `position.py --fixture`; the leg is outside the base manifest.

New arm: tools/loop/position.py · covers AC1 AC2 · the failed-fetch plant beside 65's quiet-remote plant, staged against TOOL-dDeclaredLoop-65's mtime-only reading · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 45 (HIGH, item H7).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-77, written by the round-4 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 65's reading in `tools/loop/position.py`, unbuilt at base, extended by a content check on
the file it already stats. `python tools/codebase-map/reuse_lookup.py "time of the last fetch from
FETCH_HEAD"` ranked `parse_time` (`tools/runlog/extract.py`), `check_time_sources`, `head_sha` and
`read_header_verbs`; none reads `FETCH_HEAD`, so no existing seam fits beyond 65's own reader.

Recall terms used: FETCH_HEAD mtime failed fetch truncated default branch remote url stale-remote freshness position engine

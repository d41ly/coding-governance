# TOOL-dLinkedLibrary-98 — the raw blob read is observed over a blob proved to hold its CR LF bytes

**Status:** DEFERRED · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 38 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-98-deviation-981.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-98-deviation-981.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 92 to 96
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md`) confirmed
finding **id 10 at HIGH**, report item **H2**. Id 29 shares the item and is its own unit,
`TOOL-dLinkedLibrary-101`.

Id 10 is the grounding half of the item. `TOOL-dLinkedLibrary-96` AC8 commits a blob holding `EF BB BF`,
CR LF line ends and a byte `FF` into its own scratch repository and asserts that `read_blobs_at` with
`raw` returns "exactly the committed bytes". It never says how the CRs reach the blob. On this node the
system and global git configs set `core.autocrlf=true`, and git drops every CR at `git add`, the `FF`
byte notwithstanding. The committed blob then holds no CR, and a `raw` mode that still folds CR LF
returns exactly the committed bytes: AC8 certifies CR preservation it never exercised.

This unit writes AC8's blob with every filter off, proves the CRs are in the object before the read, and
compares the raw return with the bytes written rather than with the blob. It repairs
`TOOL-dLinkedLibrary-96` and builds one step after it (order 38).

## 2. Scope (IN)

- **S1** — The blob, written filter-free. AC8's probe writes its bytes to a file in a scratch repository
  made by `tempfile.mkdtemp` under a short absolute scratch root, stores them with `git hash-object -w
  --no-filters <file>`, enters the object with `git update-index --add --cacheinfo 100644,<oid>,<path>`
  and commits. No `git add` touches the bytes, so neither `core.autocrlf`, `core.attributesFile` nor a
  `.gitattributes` can fold them. The probe cleans up the directory after the read. Observed by AC1.
- **S2** — The precondition. Before `read_blobs_at` is called, the probe reads the object with `git
  cat-file -p <rev>:<path>` as bytes and asserts it equals the bytes written, `\r\n` count included: the
  written bytes are `EF BB BF`, `jobs:\r\n`, `# `, `FF`, `\r\n` and `  t:\r\n`, three CRs, each before an
  LF. A failed precondition stops the probe naming it, and no raw verdict is printed. Observed by AC1 and
  AC2.
- **S3** — The compare. `read_blobs_at(root, [(rev, path)], raw=True)` must return the bytes written, held
  in memory by the probe, and the probe prints the CR count of the return, `cr=3`. Observed by AC1.
- **S4** — The record. 96's acceptance ledger carries an amendment line citing this unit, re-answering
  96 AC8 with S1 to S3's observation and its `cr=3`. Observed by AC3.

## 3. Non-goals (OUT)

- The staged red that a folding `raw` branch must fail, and the default path's own discriminating blob:
  id 29, `TOOL-dLinkedLibrary-101`, which reads this unit's blob.
- A fixture-builder check that every scratch repository a criterion commits into sets
  `core.autocrlf=false`: the report's left-shift, a separate mechanism; unit 92 S1 covers the
  `adopt_program.py --fixture` repository only.
- Changing `read_blobs_at`: 96 S8 builds `raw`; this unit corrects how it is observed.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-96` — S8's `raw` keyword and AC8's probe, which S1 to S3 observe over a blob proved to hold its CRs (id 10)
- **hands-off** `TOOL-dLinkedLibrary-101` — S1's filter-free blob and S2's precondition, which unit 101 reuses for its staged folding copy and its no-`FF` default-path blob (id 29)

## 4. Design

### Evidence

- `git config --show-origin --get-all core.autocrlf` on this node printed `true` from both
  `C:/Program Files/Git/etc/gitconfig` and `C:/Users/d41ly/.gitconfig` (PINNED, 2026-10-27).
- The report's skeptic committed `EF BB BF jobs:\r\n# FF\r\n  t:\r\n` in a scratch repository and `git
  cat-file -p HEAD:f.yml | od -c` showed no `\r` (finding ids 10 and 29).
- `tools/memory-tree/tree_lib.py:328` defines `read_blobs_at`; its default path at `:364` decodes UTF-8 and
  applies `.replace("\r\n", "\n")`, and returns None on `UnicodeDecodeError`.
- 96 AC8 (`2026-10-27-spec-TOOL-dLinkedLibrary-96.md`, AC8) names CR LF line ends and sets no config and
  checks no precondition.

### Why `--no-filters` and not only `core.autocrlf=false`

A repository-level `core.autocrlf=false` outranks the system and global values, which is what unit 92 S1
relies on. It does not reach a `core.attributesFile` naming `text`, which folds at `git add` too.
`hash-object --no-filters` writes the object from the bytes as given, so S1 holds on every node, and S2's
precondition names any other path that loses a byte.

### Rollout

Order 38, one step after `TOOL-dLinkedLibrary-96`. The pass writes no product code: it runs S1 to S3's
probe by `python -I -c` and writes S4's line, and `TOOL-dLinkedLibrary-101`'s pass follows it.

### Files touched (estimate)

- `memory/builds/dLinkedLibrary/build/`: S4's amendment line and this unit's acceptance ledger

### Alternatives rejected

- **Comparing the raw return with the committed blob.** It is the defect: a folded blob and a folding
  reader agree.
- **An `od -c` reading typed into the criterion by hand.** S2 compares bytes in the probe itself and
  stops it on a mismatch.

## 5. Production-readiness checklist

- security — keeps 90's and 93's CR handling honest: 96 S8's raw read is the bytes `ci_lines` strips and
  scans.
- perf / scale — one scratch repository, three git calls.
- error / empty / loading states — a blob missing its CRs stops the probe naming the precondition.
- observability — the probe prints the CR count of the raw return.
- risks — none beyond the probe: no product code changes.
- testing — AC1 to AC3 by the probe and a ledger grep.
- migration — none.
- user docs — none under `help/`: no behaviour changes.

## 6. Acceptance criteria

- **AC1** — When the probe of S1 to S3 runs by `python -I -c` on a node whose global `core.autocrlf` is
  `true`, the precondition holds, `git cat-file -p` returns the three-CR bytes written, and
  `read_blobs_at` with `raw=True` returns those bytes, printing `cr=3`.
  Red when: the blob or the raw return holds fewer CRs than were written.
  figure: PINNED, three CRs in the written bytes.
- **AC2** — When the same probe runs with S1's `hash-object --no-filters` replaced by a plain `git add`
  under the inherited `core.autocrlf=true`, it stops at S2's precondition and prints no raw verdict.
  Red when: the probe reaches a verdict over a blob that lost its CRs.
- **AC3** — When `grep 'TOOL-dLinkedLibrary-98'` runs over 96's acceptance ledger, it prints the line
  re-answering 96 AC8 with `cr=3`.
  Red when: 96 AC8 stands answered over a folded blob.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — How does the blob keep its CRs?** Options: (a) `git config core.autocrlf false` in the scratch
  repository before `git add`; (b) `git hash-object -w --no-filters` with `update-index --cacheinfo`.
  Both are the report's. (a) leaves an attributes file able to fold; (b) satisfies every criterion
  either does and leaves no follow-up. RESOLVED (agent, 2026-10-27, delegated): (b), S1. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 92 to 96, id 10 (HIGH, item
  H2, which id 29 shares).

## 10. Reuse audit

The seam extended is 96 AC8's probe of `read_blobs_at` (`tools/memory-tree/tree_lib.py:328`), the kit's
one `<rev>:<path>` bytes reader. `deviation_join.py`'s `check_blob_reader` (`:1450`) builds a scratch
repository through its `Fixture.write_commit` and reads no CR, so it proves nothing about folding.
`python tools/codebase-map/reuse_lookup.py "write a git blob without line ending conversion"` ranked
`git`, `write`, `write_text` and `run_git`, none a filter-free object writer, so no existing seam fits
beyond the probe being corrected.

Recall terms used: `python tools/memory-recall/query.py "how does a scratch repository keep crlf bytes for a raw blob read" --terms "read_blobs_at raw crlf autocrlf scratch repository hash-object no-filters cat-file od precondition"`

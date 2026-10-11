# TOOL-dHomedResolver-1 — check 10 and check 24 resolve a rotated archive's live index at the stem's declared home

**Status:** CLOSED · rev-2 · 2026-10-09 · node d · Tier-2 · base 5a836bf0 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-dHomedResolver-1-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-dHomedResolver-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-dHomedResolver-1-0-run-mandate.md](../prompts/2026-10-09-prompt-TOOL-dHomedResolver-1-0-run-mandate.md) | journal | TOOL-dHomedResolver-2 TOOL-dHomedResolver-3 |
| [2026-10-09-prompt-TOOL-dHomedResolver-1-1-build-brief.md](../prompts/2026-10-09-prompt-TOOL-dHomedResolver-1-1-build-brief.md) | journal | — |
| [2026-10-09-review-TOOL-dHomedResolver-1-2-3-diff-review-round1.md](../reviews/2026-10-09-review-TOOL-dHomedResolver-1-2-3-diff-review-round1.md) | diff-review | TOOL-dHomedResolver-2 TOOL-dHomedResolver-3 |

<!-- /gen:spec-records -->

## 1. Goal

Check 10 finds the index a rotated archive was cut from by searching every tracked file under the
memory root for `<stem>.md`. A build-folder file that happens to share the name joins the result, and
the check then reports the ROTATION as unresolvable. Resolve the stem at its declared home instead,
in both readers of the rule, so a namesake anywhere else is not consulted at all.

## 2. Scope (IN)

- **S1** — Check 10 in `check-memory-hygiene.sh` resolves `DECISIONS` to `$M/DECISIONS.md` and a
  family stem to `$M/backlog/<FAMILY>.md`, through one shell function, `resolve_live_index_home`. A namesake
  elsewhere under `$M/` is never read. Observed by AC1 and AC2.
- **S2** — A home that is not tracked is a NAMED finding naming the archive, the stem and the home,
  never a `continue`. Observed by AC3. Several is impossible by construction, and check 10's header
  says so: that sentence is NOT OBSERVED — header prose no arm reads, checked in the closing review.
- **S3** — Every property the header names is kept: the `builds` deferral and its count line, the
  same-day disambiguator, and the preamble window. Observed by AC4.
- **S4** — `check_rotation` in `row_grammar.py` resolves through `resolve_live_index_home`, a Python function
  with the same rule, and stops searching by basename. Observed by AC5.
- **S5** — The shell prints its resolution with `--print-live-index-home <stem>`, and the row-grammar
  self-test's cross-reader arm compares both readers' homes for every declared stem. Observed by AC6.
- **S6** — The carriers stating the basename rule state the declared-home rule instead: the HYGIENE
  catalogue and its kit template, the memory-tree README (an upgrade note) and the hygiene dossier.
  Observed by AC7 for the catalogue, its template and the dossier. The README's upgrade note is
  NOT OBSERVED — prose an upgrading adopter reads, graded by no arm.

## 3. Non-goals (OUT)

- `row_docs()`'s selection. It already selects by declared location; narrowing its `backlog/`
  prefix to `<FAMILY>.md` would change check 20's row population, which is not this defect.
- Any change in inCMS core or nc, and reverting core's `DECISIONS-LEDGER.md` rename.
- The generator's untracked-archive refusal: `TOOL-dHomedResolver-2`.

### Edges

- **hands-off** `TOOL-dHomedResolver-3` — the gotcha record for the name-search class this unit closes.

## 4. Design

### Evidence

Read at base `5a836bf0`. The shell's loop is under `# 10 — rotation note`, and its `idx=$(…)` walks
`$FILES` outside `archive/` comparing `${f##*/}` to `$stem.md`. Python's `check_rotation` builds
`idx` the same way over `row_docs()`'s non-archive paths. Core at `ca8b51512^` tracked three files
named `DECISIONS.md`: the root index and two build-folder ledgers.

### Data model

`resolve_live_index_home <stem>` returns one path. `DECISIONS` maps to `$M/DECISIONS.md`. Any other stem
maps to `$M/backlog/<stem>.md`. The function takes no mode: under `builds` a family archive never
reaches it in check 10, which defers it first, and never reaches `check_rotation`, whose archive set
`derive_row_stems` already narrows to `DECISIONS`.

### Inventory

- `resolve_live_index_home` — a shell function in `check-memory-hygiene.sh`, and a Python function of the
  same name in `row_grammar.py`.
- `--print-live-index-home` — a print mode of `check-memory-hygiene.sh`, beside
  `--print-rotated-archive-ere`.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/HYGIENE.md`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/README.md`
- `memory/map/features/memory-tree-hygiene.md`

### Alternatives rejected

- **Keep the basename search, but exclude `builds/`.** Rejected: a namesake under `guides/`,
  `project/` or any future folder collides the same way. The search is the defect, not its scope.
- **Shell out from check 10 to `row_docs()`.** Rejected: under `shards` that set is every file under
  `backlog/`, so a namesake in a subfolder of `backlog/` still collides, and it adds a process to a
  check headed `(always; cheap)`.
- TOOL-cSpliceWarden-2 rejected "resolve from the declared FAMILIES" as a tautology. This is not
  that: the home is derived from the stem, and the check then asks the TREE whether that path is
  tracked, so a missing home reds.

## 5. Production-readiness checklist

- security — N/A — a read-only structural check over tracked paths.
- perf / scale — one fixed-string membership test per archive, cheaper than the walk it replaces.
- error / empty / loading states — a missing home is a named finding; the population is unchanged.
- observability — the finding names the archive, the stem and the home it expected.
- risks — the finding text changes, which strands the existing zero-resolution arm. That arm is
  rewritten in this unit, not left to fail.
- testing — new arms in the hygiene suite and the row-grammar self-test, each observed RED at base.
- migration — an adopter whose index sits off its declared home now gets a named finding. The
  three real trees probed hold none.
- user docs — the HYGIENE catalogue entry and an upgrade note in the memory-tree README.

## 6. Acceptance criteria

- **AC1** — When `check-memory-hygiene.sh` runs over a fixture holding the root decision index, a
  flat DECISIONS archive it announces, and a build-folder file named DECISIONS.md, check 10 reports
  nothing for that archive.
  Red when: the stem still resolves by basename and reports three live indexes.
- **AC2** — When the same fixture also holds a build-folder ARCH.md beside a rotated ARCH archive
  that the ARCH shard under backlog/ announces, under `BACKLOG_MODE` shards, check 10 reports
  nothing for it.
  Red when: a family namesake in a build folder joins the resolution.
- **AC3** — When a fixture holds a DEPL archive and no DEPL shard, `check-memory-hygiene.sh` names
  the archive and the expected home, backlog/DEPL.md, in its check 10 finding.
  Red when: the missing home is skipped in silence, or the finding omits the home.
- **AC4** — When `check-memory-hygiene.sh` runs over the existing `rotarchive` fixture, the line-4
  announcement, the same-day `b` archive and the `builds` count line pass as before.
  Red when: the rewrite narrows the preamble window or drops the deferral count.
- **AC5** — When `row_grammar.py --selftest` runs its new arm, a `cut` tree holding a namesake ARCH.md
  in a subfolder of backlog/ beside the ARCH shard grades the archive's exclusivity half.
  Red when: `check_rotation` still matches by basename and reports two live indexes.
- **AC6** — When the cross-reader arm in `row_grammar.py --selftest` runs, it compares the output of
  `--print-live-index-home` with `resolve_live_index_home` for `DECISIONS` and every declared
  family, and prints `JOIN-OK`.
  Red when: either reader's rule changes alone.
- **AC7** — When `git grep -n 'by BASENAME'` runs over `memory/HYGIENE.md`,
  `tools/memory-tree/HYGIENE.template.md` and `memory/map/features/memory-tree-hygiene.md`, it
  prints nothing.
  Red when: a carrier still states the retired rule.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `row-grammar selftest` · `kit/dogfood doc parity` · `check-arms selftest` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 · a namesake build file beside an announced archive, and a family archive with no shard · none
New arm: tools/memory-tree/row_grammar.py · covers AC5 AC6 · a namesake under backlog/sub/, and a reader changed alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §2 S2 and S6: the header sentence and the README note are marked NOT OBSERVED
  instead of claiming AC3 and AC7, which do not read them (closing review round 1, L2; built by
  TOOL-dHomedResolver-5).

## 10. Reuse audit

The seam is check 10's own loop and `check_rotation`'s `idx`, both extended in place. The print-mode
pattern is `--print-rotated-archive-ere`, which the cross-reader arm already drives through
`resolve_shell_ere`; the new mode rides the same shell probe. `reuse_lookup.py` returned no existing
resolver for a rotated archive's index. Recall returned TOOL-cSpliceWarden-2 and
TOOL-cTracedPromise-6, whose properties S3 keeps, and nothing that chose basename over a declared
home for a reason this unit contradicts.

Recall terms used: check 10 rotation note live index basename archive stem backlog shard resolves preamble TOOL-cTracedPromise-6 TOOL-cSpliceWarden-2

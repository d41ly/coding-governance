# TOOL-aMendedFleet-2 — a definition-level census of every merge since 2026-09-01

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-2-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-build-TOOL-aMendedFleet-2-2-merge-census.md](../build/2026-10-04-build-TOOL-aMendedFleet-2-2-merge-census.md) | journal | — |
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

One merge is known to have lost shipped code on main, and `TOOL-aMendedFleet-1` restores it. The
review that found it replayed the merges since 2026-09-01 at definition level and flagged three:
`01c22e155` (confirmed), one documented rewrite, and `e2e840d08`, whose first parent's
`parse_push_class` is absent from the merge (unverified). This unit replays every such merge again,
adjudicates every name a parent added that the merge lacks, restores any confirmed loss nobody else
owns, and records the census as a journal, so "main holds everything its merges were given" becomes
a recorded answer rather than one incident's.

## 2. Scope (IN)

- **S1** — A replay probe reads every merge commit reachable from HEAD whose committer date is on or
  after 2026-09-01, as `git rev-list --merges --since=2026-09-01 HEAD` lists them. For each parent it
  takes the merge-base, the files that parent changed over it, and the definitions in those files at
  the base, at the parent and at the merge. It flags each name the parent added, absent at the base
  and present at the parent, that the merge's copy of the same file lacks. Observed by AC1, AC2.
- **S2** — Definitions are read by the lexicon kit's own parsers in `tools/lexicon/lexicon.py`:
  `parse_shell_defs` for shell, `_python_defs` for Python, and `parse_ts_defs` for JavaScript, never
  a retyped regex. Observed by AC2, AC6.
- **S3** — Every flagged row is adjudicated into exactly one disposition: owned by
  `TOOL-aMendedFleet-1`; restored by this unit; superseded, with the successor name and the commit or
  record that introduced it; or moved, when the name is defined elsewhere in the merge's tree.
  `e2e840d08`'s `parse_push_class` row is one of them. Observed by AC3, AC5.
- **S4** — A confirmed loss that no other unit owns, whose dependencies are all defined at HEAD and
  whose body applies at HEAD unchanged, is restored from the parent that added it. A confirmed loss
  that needs reconciling with later code is not restored here: it becomes its own unit through
  `--rescope --act add`, named in the journal. Observed by AC4.
- **S5** — The census journal carries the probe's source verbatim in a fenced block, its
  population count, every flagged row with its disposition, and the gap the probe cannot see.
  Observed by AC1, AC6.

## 3. Non-goals (OUT)

- `01c22e155`'s restore. That is `TOOL-aMendedFleet-1`; this unit records its row as owned there.
- A gate that refuses such a merge at push time. That is `TOOL-aMendedFleet-3`, which may reuse this
  probe's reading; this unit builds no refusal and wires nothing into the bar.
- Losses below definition level. A merge that keeps a function's name and loses part of its body,
  or loses a prose section, is invisible here: `TOOL-dMendedRecall-3`'s lost verb entry is exactly
  that shape. The journal states the gap. A line-level replay is not the substitute, because the
  review measured it flagging nine merges where three lost a definition, and demanding a 368-line
  list for one documented rewrite.
- Merges on branches main does not reach, node d's unlanded branch included.
- Octopus merges, if any appear: the journal counts them and names them, and adjudicates each
  parent against `git merge-base --octopus`.

### Edges

- **consumes-from** `TOOL-aMendedFleet-1` — the `01c22e155` row is disposed as owned there; without
  that unit the census would report a loss nobody restores.

## 4. Design

### Evidence

Measured at HEAD `af449c0b` (run BASE `7af5f564`), 2026-10-04:

- `git rev-list --merges --since=2026-09-01 HEAD | wc -l` prints 192; 95 of them are first-parent.
  DERIVED: the probe re-reads the count at run time and the journal states the figure it read.
- `parse_push_class` is defined in `tools/push-main.sh` at `5491f7bc6`, the first parent of
  `e2e840d08`, absent at the merge-base `663a0dec` and absent at `e2e840d08` and at HEAD. Its only
  adder is `fdc2dee42` (`TOOL-dDerivedDocket-2`). HEAD's `tools/push-main.sh` classifies a failed
  push in `derive_push_failure`, whose comment cites `TOOL-aHonedRuleset-10` for refusing to read
  `rejected` and `connection` out of push output, which is `parse_push_class`'s method. That makes
  "superseded by `derive_push_failure`" the candidate disposition; the pass confirms or refutes it
  from the commit that introduced `derive_push_failure`.
- The report's "three merges flagged, one confirmed, one documented rewrite, one unverified" is
  PINNED, measured by the review at `ac65de998`; this unit re-derives it.
- `tools/lexicon/lexicon.py` defines `parse_shell_defs` (a tokenizer recognising four function
  forms), `_python_defs` (an `ast` parse that RAISES on a syntax error) and `parse_ts_defs`.

### The probe

One Python script, run from the repository root with the lexicon kit importable. It costs one git
spawn per merge-base and per file listing, at about 0.75 s each on node a, so it reads blobs
through ONE `git cat-file --batch` process rather than one `git show` per blob.

1. List merges with `git log --merges --since=2026-09-01 --format='%H %P' HEAD`.
2. Per merge, per parent: `git merge-base`, then `git diff --name-only <base> <parent>` filtered to
   `.sh`, `.py`, `.js` and `.mjs`.
3. Per file: definitions at base, parent and merge. A file absent at one revision has no definitions
   there. A Python file that does not parse at one revision is a row of its own, never an empty set.
4. Flag `(merge, parent, file, name)` where the name is in the parent's set, not the base's, and not
   the merge's. Then, per flagged name, `git grep -w` at the merge for a definition elsewhere, which
   pre-fills the moved disposition for the adjudicator.
5. Print the population count read, the flagged rows, and the parse-failure rows.

The adjudication is a read: each superseded row names a successor and the commit or record that
introduced it, and each confirmed loss names the CLOSED unit whose code it was.

### Rollout

The census journal lands under this build's `build/` folder as a `journal` record serving this
unit, and the acceptance ledger beside it. A restore under S4 is one commit per restored name.

### Files touched (estimate)

- `memory/builds/aMendedFleet/build/` — the census journal and the acceptance ledger.
- The file of any name S4 restores, unknown until the census runs; the ledger names each.

## 5. Production-readiness checklist

- security — N/A: a read-only probe over the object database; a restore puts back reviewed code.
- perf / scale — a few hundred git spawns, minutes on node a; the probe is run once, by this pass.
- error / empty / loading states — an unparseable revision is reported as a row, never read as zero
  definitions; an empty flagged set is stated beside the population count.
- observability — the journal is the observation.
- risks — a parser blind spot reads as "no loss". AC2's known positive is the liveness assertion.
- testing — no new arm. The probe is an instrument, and `TOOL-aMendedFleet-3` owns the gate.
- migration — none.
- user docs — none; the journal is a record, not a feature.

## 6. Acceptance criteria

- **AC1** — When the probe runs, the census journal states the merge count it read, and that count
  equals what `git rev-list --merges --since=2026-09-01 HEAD` prints at the same commit.
  Red when: the counts differ, which means the probe skipped merges and a clean census proves
  nothing. figure: DERIVED at observation time.
- **AC2** — When the probe's reading of `01c22e155` is printed, it names `write_ask_views` in
  `tools/unattended/unattended.sh`, added by the second parent `ef1dcdb61`.
  Red when: that row is absent, and the census is a DEAD PROBE rather than a clean one.
  The probe reads the merge commit, not HEAD, so `TOOL-aMendedFleet-1`'s restore does not hide it.
- **AC3** — When the journal is read, every flagged row carries exactly one disposition from S3,
  and a row for `parse_push_class` in `tools/push-main.sh` at `e2e840d08` is among them.
  Red when: a flagged row carries no disposition, or the `e2e840d08` row is missing.
- **AC4** — When a row is disposed "restored by this unit", `git grep -n -w` for its name over the
  restored file at the restore commit prints its definition, and any cheap acceptance check its own
  CLOSED unit's spec names is re-run and recorded in the ledger. When no row is so disposed, the
  journal says `none restored here` and names each loss it routed to `--rescope --act add` instead.
  Red when: a restored name is absent from its file, or a confirmed loss has neither a restore nor a
  routed unit.
- **AC5** — When a row is disposed superseded, `git grep -c -w` for the successor name at HEAD over
  the file the journal names prints at least 1. For `parse_push_class` that is `derive_push_failure`
  in `tools/push-main.sh`, unless the pass refutes it and records why.
  Red when: a successor the journal names is not defined at HEAD.
- **AC6** — When the census journal is read, its fenced probe source calls `parse_shell_defs`,
  `_python_defs` and `parse_ts_defs` from `tools/lexicon/lexicon.py`, and a gap section names
  sub-definition and prose losses as unseen.
  Red when: the probe carries its own definition regex, or the gap is unstated.

## 7. Gates

The close's bar runs these; this unit's pass runs only the probe and the direct checks in §6.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `build README slot contract` · `recall floor` · `recall floor arms`

New arm: none. The probe is a recorded instrument; the merge-time refusal and its arms are `TOOL-aMendedFleet-3`'s.

## 8. Open questions

- **FACT-QUESTION · F1** — Is a confirmed loss restored inside this unit, or routed to a unit of its
  own? Probe: for each confirmed loss, does the parent's definition apply at HEAD with every name it
  calls defined there. The observation that decides: a body that applies unchanged is the same
  mechanism as `TOOL-aMendedFleet-1`'s restore, and one that needs reconciling is a second mechanism.
  Liveness: `01c22e155`'s row is a body that applies unchanged, so the probe can answer "restore here".
  RESOLVED (agent, 2026-10-04, delegated): restore here only when it applies unchanged; otherwise
  `--rescope --act add`, per S4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

The definition readers are the lexicon kit's: `parse_shell_defs`, `_python_defs` and `parse_ts_defs`
in `tools/lexicon/lexicon.py`, the same parsers the naming gate grades with, so the census and the
gate agree on what a definition is. `python tools/codebase-map/reuse_lookup.py "list function
definitions a merge parent added that the merge result lacks"` ranked `merge` in
`tools/memory-tree/merge-rows.py` and `tools/settings-merge.py`, which merge rows and settings rather
than replay commits, and `scan_js_definitions` in `tools/codebase-map/map_lib.py`, a regex reader the
lexicon tokenizer supersedes for this use. No existing seam replays merges: the probe is new and is
recorded, not shipped. The recall probe returned only the template's prose rule "diff the merge
against both parents" in the archived playbook snapshots, and no prior census.

Recall terms used: merge dropped definitions parent added lost hunks reconcile auto-took both parents superseded restore replay census

# Run mandate — dHomedResolver

**Serves:** journal TOOL-dHomedResolver-1 TOOL-dHomedResolver-2 TOOL-dHomedResolver-3

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `d`, 2026-10-09. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The prompt

> Repo: coding-governance, primary tree C:/projects/coding-governance, remote origin, node d. Mint your own session slug (TOOL family) with both mint guards; nothing below owns an id.
> The primary tree is busy: on 2026-10-09 its main was ahead 23 / behind 31 of origin/main with a peer's unpushed work. Never land from it. Work in your own worktree off origin/main and land IN PLACE with push-main.sh --prepare --slug <slug> then --land --slug <slug>. Run --carry first and stop on anything FOREIGN. Before any heavy gate, check that no peer push-main or gate is running.
>
> ### Evidence (inCMS core, node d, 2026-10-09)
> Core rotated memory/DECISIONS.md (153,592 B against check 6's 153,600 B cap) with its core-local scripts/rotate_index.py, landed at incms/main a42c9ebfb. Two gov defects surfaced:
> Check 10 resolves a stem's live index by BASENAME anywhere under memory/. See tools/memory-tree/check-memory-hygiene.sh, the idx=$(…) loop under # 10 — rotation note (~line 1340). Once a flat archive/DECISIONS.<date>.md existed, core's check 10 refused: "stem 'DECISIONS' resolves to 3 live index(es)". The extra two were the build-folder files memory/builds/gap-closure/build/{durable-email,staff-sso}-BUILD/DECISIONS.md. Core worked around it by renaming them DECISIONS-LEDGER.md (ca8b51512). The finding blames the rotation for a name collision it did not cause. Any build file named DECISIONS.md, or <FAMILY>.md under shards, reds every future rotation of that stem.
> gen_build_index.py derives each README's ids: from git ls-files, so it reads the index. See tools/memory-tree/gen_build_index.py :706 and :861. Running --write while the new archive was still UNTRACKED re-rendered 17 unrelated build READMEs plus LIVE.md, because every id whose row had moved looked gone. With the archive staged first, it rendered 0 changes. The silent rewrite is the green-by-absence class: no line says an untracked archive/ file was ignored.
>
> ### Goal
> Check 10 resolves by the stem's DECLARED HOME, never a basename search. DECISIONS resolves to $M/DECISIONS.md. A family stem resolves to $M/backlog/<FAMILY>.md under shards; keep the existing deferral under builds. Keep every property its header comment names: TOOL-cTracedPromise-6 (shards under backlog/), TOOL-cSpliceWarden-2 (same-day disambiguator, preamble window), and "none or several is a named finding, never a continue". A missing home is still a finding.
> Keep the second reader in lockstep. ROTATED / row_docs in tools/memory-tree/row_grammar.py (~:224) read the same rule, joined by an arm in the row-grammar self-test. Change both, and keep or extend that arm.
> gen_build_index.py refuses, or at least announces, an untracked file under $M/archive/ before it derives ids:. Prefer refusing --write with the remedy (git add the archive first), because a write over a half-staged rotation is the damage. --check should say so too.
>
> ### Acceptance
> New self-test arms in check-memory-hygiene.test.sh and the generator's self-test. Each arm's failing case is OBSERVED red against today's code before the fix: a build-folder DECISIONS.md beside a flat DECISIONS archive, and an untracked archive under --write.
> Run each new predicate over the REAL trees before wiring it, printing hits and near-misses: gov's own memory/, inCMS core (C:/projects/incms/main, read-only, at incms/main), and nc (C:/projects/incms/main/vendor/nicocares-package, read-only). Neither may red an innocent file.
> Gov's full bar is green and the kit versions are minted per gov's lander.
> A DECISIONS row and a gotcha record for the class, if gov's catalogue has none for it.
>
> ### Non-goals
> Do NOT touch inCMS core or nc. The re-pull into core is a separate run, with its own owner ask. That run should also cover two core-local items: rotate_index.py --write staging the archive it writes, and core backlog row ABL-dSnideCartographer-34 (R5 hard-codes 20 KB / 250 lines instead of reading .memory-tree.conf). Name that run in your wrap-up as the follow-up owed.
> Do not revert core's DECISIONS-LEDGER.md rename. It stays correct after the fix.

## How the run reads it

- The ids the prompt names are properties to keep, not asks to serve: the prompt says so itself
  ("nothing below owns an id"), so this is the prompt path and not the scaffold route.
- "Change both" for the second reader: `row_docs()` already selects by declared location, so the
  Python change is in `check_rotation`, whose own index lookup was the basename search. The
  cross-reader arm is extended to compare the resolved homes, not only the archive sets.
- "None or several" survives as "none": a declared home is one path, so several is impossible by
  construction, and the header says so instead of keeping a dead branch.
- "A gotcha record for the class": two classes surfaced, so two records, one per class.
- No question was asked: ACCEPTANCE and GATES are stated in the prompt.
- Orientation probe, run before this record was written (scratch `probe_homes.py`, read-only):
  gov, core at `incms/main` and nc each resolve every tracked rotated archive identically under
  both predicates, and none holds an untracked file under `memory/archive/`. Core before
  `ca8b51512` held three live files named `DECISIONS.md`, the collision the prompt describes.

# TOOL-dBoundRoles-51 — the round-1 audit of units 37 to 44, its 8 records-and-Skills minors: build order verified, the policy mirror's net diff, append-only records observed by class, one owner per ledger verdict, and the recall Skill off a refused tool

**Status:** INPROGRESS · rev-3 · 2026-11-22 · node d · Tier-2 · base 462d20f3 · streams tooling · order 30 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 |
| [2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md) | research | TOOL-dBoundRoles-43 TOOL-dBoundRoles-45 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 |
| [2026-10-26-build-TOOL-dBoundRoles-51-deviation-511.md](../build/2026-10-26-build-TOOL-dBoundRoles-51-deviation-511.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md) | research | TOOL-dBoundRoles-45 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 |
| [2026-11-22-prompt-TOOL-dBoundRoles-44-reground-o-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-44-reground-o-brief.md) | journal | TOOL-dBoundRoles-44 TOOL-dBoundRoles-50 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 |
| [2026-11-22-prompt-TOOL-dBoundRoles-51-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-51-build-brief.md) | journal | — |
| [2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-49 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-48 TOOL-dBoundRoles-47 TOOL-dBoundRoles-50 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the eight promoted specs 37 to 44
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`) confirmed
21 MEDIUM and 11 LOW findings. BUILD-METHOD M4 batches them into two units because they split into
disjoint write sets by M6; `TOOL-dBoundRoles-50` §4 "Why two units" holds the cut. This unit takes the
8 whose items read only `memory/` records, two acceptance ledgers and the commit log, and write only the
memory-recall Skill and, where a build commit wrote it, the policy mirror: report ids 2, 3, 7, 8, 13, 14,
20 and 31, four MEDIUM and four LOW. Each is its own scope item; ids 8 and 20 share report item L3.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M1 | 2 | units 37 to 41, §4 Rollout | S1 |
| M2 | 3 | unit 44 S8, S9, AC8, AC9 | S2 |
| L2 | 7 | unit 42 S2 | S3 |
| M7 | 13 | unit 42 S2, AC2 | S4 |
| L5 | 14 | unit 42 §4 "The classes" | S5 |
| L3 | 8, 20 | unit 44 S1, AC1 | S6, S7 |
| M14 | 31 | unit 44 S4 | S8 |

## 2. Scope (IN)

- **S1** — id 2. Same-order dependencies built in dependency order. Specs 37 to 41 rest a dependency at a
  shared order on "dispatch sorts a tie by id string". The guarantee the tree gives is `--dispatch`'s:
  its edge refusal holds a consumer until a same-build producer is CLOSED
  (`tools/unattended/unattended.sh@7548da57:18521-18530`), and it refuses a pass whose write set meets an
  open one's (`tools/unattended/unattended.sh@7548da57:17730-17748`); the harness dispatches strictly in
  sequence (`tools/workflows/unattended-build.js@9da9556b:78-82`). Unit 40 declares a `consumes-from`
  edge on unit 39 (spec 40 §3), so the edge refusal holds that pair; unit 38's need of unit 3's card
  binding is declared by no edge. The pass reads `git log --reverse --format=%s <BASE>..HEAD` and
  records in its ledger that unit 3's pass commit precedes unit 38's and unit 39's precedes unit 40's; an
  inversion is returned to the main loop. Observed by AC1.
- **S2** — id 3. The policy mirror ships as its render, and unit 44's two criteria are answered where
  they can be. `python tools/policy/policy.py mirror --check` exits 0 after this pass: where a commit of
  the build left `.governance/policy.json` other than its render at HEAD, this pass regenerates it with
  `policy.py mirror --write` in a commit of its own, the route the guard admits
  (`tools/policy/guard.py@a5d4f958:9-12`, TOOL-dGroundRules-19), and the landing re-renders it as
  `TOOL-dGroundRules-5` S3 gives (§8 F3). Unit 44's ledger answers AC8 by the same check, as that unit's
  rev-5 states it, and AC9 AMENDED, its swap-check half recorded at the close under a `Pass: none`
  commit, where the swap happens. Observed by AC2.
- **S3** — id 7. Unit 42 S2's clause on `memory/builds/` observed as it means. Every file under
  `memory/builds/` outside this build's folder that existed at BASE and names the hook shows zero
  deletions in `git diff --numstat <BASE> HEAD`; this build's own ledgers, specs and renders are written
  by its passes, and the ledger says so. Observed by AC3.
- **S4** — id 13. Unit 42 AC2 observed per record class. Since unit 25's parent:
  `git diff --quiet <P> HEAD -- memory/archive` exits 0; the deletions column of
  `git diff --numstat <P> HEAD -- memory/DECISIONS.md` is 0; and the generated backlog shards are checked
  by regeneration, `python tools/memory-tree/gen_build_index.py --check` exiting 0. Unit 42's ledger
  answers AC2 AMENDED, naming this unit. Observed by AC4.
- **S5** — id 14. `memory/guides/MERGE-BAR.md` classed as what it is. Unit 42's ledger classes it a live
  guide edited in place by unit 25 S8, and only `memory/guides/REVIEW-PROTOCOL.md` as re-rendered from
  `tools/workflows/REVIEW-PROTOCOL.template.md`. Observed by AC5.
- **S6** — id 8. Unit 44 S1's population, given a criterion that can fail. The pass lists the files under
  `memory/` that name `agent-cap.js`, with `TOOL-dBoundRoles-42`'s pathspec, and were added after unit
  42's pass commit, and records each with its class in this unit's ledger. Observed by AC6.
- **S7** — id 20. One owner per verdict, one pathspec per population. Unit 25's ledger holds exactly one
  AC14 answer, AMENDED, naming `TOOL-dBoundRoles-42` S4, and unit 44's ledger cites it rather than
  restating it. The pass re-runs unit 44 S3's reader derivation with 42's pathspec, `memory/ledger/`
  excluded beside `memory/builds/`, and records any file the two filters disagree on. Observed by AC7.
- **S8** — id 31. The memory-recall Skill sends the main loop to shell probes.
  `tools/memory-recall/SKILL.template.md@17553715:12` and `@17553715:63` name shell `grep` and `git grep`
  through Bash where they name the search tools, and `.claude/skills/memory-recall/SKILL.md` is its render. No Skill or
  Skill template in the tree names a tool `TOOL-dBoundRoles-10` refuses to the main loop. Observed by AC8.

## 3. Non-goals (OUT)

- Rewording the specs of units 1 to 49. Each item is closed by what this pass builds or observes; a
  criterion that cannot hold as written is answered AMENDED in that unit's ledger, as the repaired spec's
  hands-off edge to this unit says.
- The 24 minors of `TOOL-dBoundRoles-50` and the HIGH findings `TOOL-dBoundRoles-45` to `-49`.
- Reordering units 38, 39 or 40. Their passes precede this one; S1 verifies the order they ran in.
- The report's left-shift gates: the same-order disjointness check, the earlier-act criterion check, the
  append-only checklist entry, the template-resolution check and the refused-tool Skill leg. No clause of
  this build names them.

### Edges

- **consumes-from** `TOOL-dBoundRoles-42` — S2's append-only clause, AC2 and the class table, whose observations and `MERGE-BAR.md` row S3, S4 and S5 complete (ids 7, 13 and 14)
- **consumes-from** `TOOL-dBoundRoles-44` — S1, S3, S4, S8, S9 and their criteria, which S2, S6, S7 and S8 complete (ids 3, 8, 20 and 31)
- **hands-off** `TOOL-dBoundRoles-57` — S8's re-worded memory-recall description, whose tokens unit 57's `test_skill_description_invariants` asserts (id 29 of the round-1 audit of units 45 to 51)
- **hands-off** `TOOL-dBoundRoles-58` — S1, AC1, AC2, AC5, AC7, AC8 and §3, which unit 58 restates, an inversion parked with `--park` (ids 11, 28, 47, 48 and 49 of the round-1 audit of units 45 to 51)

## 4. Design

### Evidence

Read at HEAD `c93f676e` on 2026-11-22:

- `tools/unattended/unattended.sh@7548da57:18521-18530` is `--dispatch`'s edge refusal, and
  `tools/workflows/unattended-build.js@9da9556b:78-82` records that dispatch is strictly sequential
  within a shared order; `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-38.md` §3
  declares no edge to unit 3, and spec 40's §3 declares one to unit 39.
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md` S8 regenerates the mirror with
  `policy.py mirror --write` in a second commit, and id 51 of the first round's audit records that
  `TOOL-dGroundRules-6` guards `.governance/policy.json` (`tools/policy/guarded-paths.txt@16afba27:6`).
  The guard admits the mirror whose staged bytes are its render at HEAD
  (`tools/policy/guard.py@a5d4f958:9-12`). The mirror records the catalogue's and the policy file's blobs
  (`tools/policy/policy.py@b1894836:930-931`), and the bar refuses a stale one before its first leg
  (`tools/run-gates/run-gates.sh@2e851a92:1607-1637`), as does the policy leg's parity arm
  (`tools/policy/check_policy.py#arm_mirror_parity`).
- `tools/memory-recall/SKILL.template.md@17553715:12` reads "Grep and Glob own those" and `@17553715:63`
  "fall back to `Grep` over `{{MEMORY_ROOT}}/`"; `skills/session-kickoff/SKILL.md@41dedf1f:22` is
  `TOOL-dBoundRoles-44` S4's.
- `git ls-files` lists `memory/guides/MERGE-BAR.md` and no template or renderer for it.

### How an item closes

As `TOOL-dBoundRoles-50` §4 states for both batches: each item states the built tree's end state, and
the pass does what is missing or records that a landed unit already left it.

### Inventory

Minted: none. The items write ledger lines, one Skill sentence pair and, conditionally, the mirror's
render.

### Migration

None: no stored data changes. S2 leaves the mirror at its render at HEAD for the landing to re-render.

### Rollout

Live at landing, at order 30, after every unit it repairs and beside `TOOL-dBoundRoles-50`.

### Files touched (estimate)

- `tools/memory-recall/SKILL.template.md`
- `.claude/skills/memory-recall/SKILL.md`
- `.governance/policy.json`

### Alternatives rejected

- **Restore the mirror's BASE bytes (S2), rev-2's pick.** Once a build commit changed the mirror's
  inputs, its BASE bytes differ from its render at HEAD, which the bar refuses before its first leg;
  §8 F3.
- **Zero diff on the backlog shards (S4).** They are generated and lose a line whenever an ask closes;
  regeneration is their observation.
- **Re-derive unit 44 S1's population unchanged (S6).** At order 30 it is empty by construction.

## 5. Production-readiness checklist

- security — S8 keeps the main loop off a tool the default refuses; S2 keeps the guarded mirror equal to
  its render, never hand-written. No new write path.
- perf / scale — git log, numstat and grep reads, one re-render.
- error / empty / loading states — S1 and S6 record an inversion or a file and return it rather than
  pass it.
- observability — the ledger records S1, S3, S6 and S7.
- risks — S2's regeneration is a write to a guarded path, which the guard admits as the mirror's render
  at HEAD (TOOL-dGroundRules-19); unit 21 S8's second commit takes the same route.
- testing — AC1 to AC8 by git, grep and the Skill's render check.
- migration — none.
- user docs — the memory-recall Skill by S8.

## 6. Acceptance criteria

Every command runs from the repository root.

- **AC1** — When `git log --reverse --format=%s <BASE>..HEAD` runs, the first pass commit naming
  `TOOL-dBoundRoles-3` precedes the first naming `TOOL-dBoundRoles-38`, and `-39`'s precedes `-40`'s, as
  this unit's ledger records. Red when: a consumer's pass ran before its producer's.
- **AC2** — When `python tools/policy/policy.py mirror --check` runs it exits 0, and
  `grep -n 'AC8\|AC9' <unit 44's acceptance ledger>` prints an AC8 line naming that check and an
  `amended` AC9 line. Red when: the guarded mirror ships other than its render, or unit 44's two criteria
  stand unanswered.
- **AC3** — When `git diff --numstat <BASE> HEAD` runs over the pre-existing records of other builds
  that name `agent-cap.js`, every deletions figure is 0. Red when: a record of another build is
  rewritten.
- **AC4** — When `git diff --quiet <P> HEAD -- memory/archive` exits 0, the `memory/DECISIONS.md` deletions
  figure of `git diff --numstat` is 0, and `python tools/memory-tree/gen_build_index.py --check` exits 0,
  `<P>` being unit 25's parent. Red when: an append-only record loses a line, or a shard drifts from
  its generator.
- **AC5** — When `grep -n 'MERGE-BAR' <unit 42's acceptance ledger>` runs, it names the class
  `live guide`, and `git ls-files | grep -ic 'merge-bar'` prints 1. Red when: the ledger records a
  template render no template performs.
- **AC6** — When `git diff --name-only --diff-filter=A <unit 42's pass commit> HEAD -- memory ':!memory/builds' ':!memory/ledger'`
  runs, every file it prints that names `agent-cap.js` has a class line in this unit's ledger. Red when:
  a memory reader added after unit 42 is unclassed.
- **AC7** — When `grep -c 'AC14' <unit 25's acceptance ledger>` runs it prints 1, and that line is
  `amended` and names `TOOL-dBoundRoles-42`. Red when: two units restate one verdict.
- **AC8** — When `grep -nwE 'Grep|Glob' .claude/skills/*/SKILL.md tools/*/SKILL.template.md skills/session-kickoff/SKILL.md`
  runs it prints nothing, and `bash tools/memory-recall/adopt-memory-recall.sh --check` exits 0.
  Red when: a Skill sends the main loop to a refused tool, or the render drifts from its template.

## 7. Gates

`check-wiring self-test` · `memory-recall skill wiring` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause; veto 1 discards
  (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1
  set. widens: none · relaxes: none
- **F2 — Restore the mirror's bytes, or record the in-branch commit and leave it (id 3)?** Options: (a)
  write back BASE bytes so the net diff is empty; (b) leave it for the landing to overwrite. (b) ships
  the guarded path in the branch's diff, the defect id 51 of the first round exists to stop. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the one survivor. widens: none · relaxes: none
  Its premise moved at HEAD; F3 re-decides it.
- **F3 — At HEAD the in-branch mirror is the landed route: what does S2 leave the mirror at (id 3)?**
  The guard admits the mirror as its render at HEAD (`tools/policy/guard.py@a5d4f958:9-12`), and the bar
  and the policy leg's parity arm refuse a mirror that differs from that render
  (`tools/run-gates/run-gates.sh@2e851a92:1607-1637`, `tools/policy/check_policy.py#arm_mirror_parity`).
  Once unit 21 S8 changes the catalogue, the mirror's BASE bytes are such a mirror. Options: (a) F2's
  pick, BASE bytes and an empty net diff; (b) the render at HEAD, regenerated in a commit of its own
  where a build commit left it otherwise, observed by `policy.py mirror --check`. (a) fails the bar on a
  correct build. RESOLVED (agent, 2026-11-22, delegated): (b), rung 3, the one survivor, the route
  `TOOL-dBoundRoles-44` §8 F5 takes for its AC8. widens: none · relaxes: S2 and AC2's empty net diff,
  now "the mirror is its render at HEAD", and AC2's AC8 line, which unit 44's rev-5 answers as written

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the records-and-Skills half of the round-1 minors of units 37 to
  44: 4 MEDIUM and 4 LOW, each id its own item.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-57 and -58, promotions of the round-1 audit of units 45 to 51; nothing else moved.
- rev-3 · 2026-11-22 · S1 · S2 · S8 · §4 · §5 · §6 · AC2 · §8 F2 F3 · §10 · re-grounded at HEAD
  `c93f676e` by `2026-11-22-prompt-TOOL-dBoundRoles-44-reground-o-brief`. S2 and AC2 observe the mirror
  as its render at HEAD by `policy.py mirror --check`, the route the guard admits and the bar requires,
  rather than BASE bytes (F3), and §6 drops the bare-name note, the mirror being tracked at HEAD. S1
  records spec 40's edge on unit 39. Every line citation is re-pointed to a blob-pinned line or a
  symbol. Unit 21 S8, unit 38 §3, unit 40 §3 and unit 44's S1, S3, S4, AC8 and AC9 were checked against
  their specs, not HEAD.

## 10. Reuse audit

The seams are `--dispatch`'s edge refusal (`tools/unattended/unattended.sh@7548da57:18521-18530`), which S1 names
as the guarantee rather than adding one; the index generator's `--check`
(`tools/memory-tree/gen_build_index.py`), which observes the generated shards; the memory-recall
adopter's `--check`, which keeps the Skill's render tied to its template; and the policy kit's
`policy.py mirror --check`, the `[[generated]]` row's check (`tools/policy/kit.toml@a87393a2:55-61`), which
S2 runs rather than a diff of its own.
`python tools/codebase-map/reuse_lookup.py "observe an append-only record by its deletions count rather than a zero diff"`
ranked `counts`, `records`, `extract_records` and `read_records`, none a deletions observation, so no
existing seam fits beyond the three named and git's own `--numstat`.

Recall terms used: `python tools/memory-recall/query.py "how is an append-only record checked during a build that appends to it" --terms "append-only DECISIONS archive backlog shard regenerate numstat deletions ledger AMENDED mirror"`

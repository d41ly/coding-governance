# TOOL-aGraftedHelix-33 — the spec commit stage places every spec a writer authored, named by id or by path, and refuses an entry it cannot place

**Status:** CLOSED · rev-2 · 2026-10-06 · node a · Tier-1 · base 018b5675 · streams tooling · order 17 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-33-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-33-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md](../build/2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md) | journal | TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 TOOL-aGraftedHelix-34 TOOL-aGraftedHelix-35 TOOL-aGraftedHelix-36 TOOL-aGraftedHelix-37 TOOL-aGraftedHelix-38 TOOL-aGraftedHelix-39 TOOL-aGraftedHelix-40 TOOL-aGraftedHelix-41 TOOL-aGraftedHelix-45 TOOL-aGraftedHelix-46 TOOL-aGraftedHelix-47 |
| [2026-10-05-prompt-TOOL-aGraftedHelix-33-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aGraftedHelix-33-1-spec-brief.md) | journal | — |
| [2026-10-06-review-TOOL-aGraftedHelix-29-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aGraftedHelix-29-closing-diff-round1.md) | diff-review | TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 TOOL-aGraftedHelix-34 |

<!-- /gen:spec-records -->

## 1. Goal

The build harness's spec commit stage, `TOOL-aGraftedHelix-15`, matches its writers' `authored`
entries against roster unit ids alone. On its first live use, run `wf_dff1cb65-954`, one writer
returned an id and three returned spec paths, so the stage committed one spec of four, reported
success, and handed out three units with an empty `specPath`. Nothing refused. This unit resolves
every `authored` entry to its roster unit, whether it is spelled as an id, a repo-relative path or
an absolute one. One path normaliser serves the resolution, the commit return and the hand-out's
path fill-back. An entry no unit owns is refused by name, the writers are asked for ids, and the
writer schema holds the three lists to roster ids.

## 2. Scope (IN)

- **S1** — One normaliser, `deriveRepoPath`, turns a path an agent or the caller spelled into the
  repo-relative, forward-slashed form. A non-string or empty value folds to the empty string.
  Otherwise it trims surrounding whitespace, turns every backslash into a slash, and turns a leading
  MSYS drive directory such as `/c/` into `c:/`. When the result, lowercased, opens with the
  template's existing `repoFold` constant and a slash, it strips that prefix by its length, then
  strips any leading `./` segments. It keeps case and every `..` segment, so S2 can refuse a path
  that climbs. `repoFold` is reused as it stands, never re-derived. Observed by AC1, AC2 and AC5.
- **S2** — One resolver, `resolveSpecEntry`, names the roster unit an entry denotes, or none.
  Observed by AC1, AC2 and AC3. An entry that two units match on one arm resolves to none. Three
  arms, tried in this order, the first match winning:
  1. the trimmed entry equals a unit's id;
  2. the entry, folded by S1, equals the folded caller `specPath` of exactly one unit;
  3. the folded entry sits under the build's `specFolder`, carries no `..` segment, and its
     basename routes to exactly one unit. For an id `<F>-<rest>`, where `<F>` is the id's text
     before its first dash, the basename is a date, then `-spec-`, then an optional `<F>-`, then
     `<rest>`, then an optional tail opening with a dash, then `.md`. That is hygiene check 5's
     recording grammar written in terms of the unit's own id. An id carrying no dash routes nothing
     by basename.
- **S3** — The spec stage's merge resolves each writer's `authored` entries through S2 as it merges
  them, before the commit stage runs. It rewrites `specced.authored` to the resolved unit ids,
  deduplicated in first-seen order, and keeps the folded path of every entry spelled as a path, keyed
  by its unit, for S4. It logs one line per such entry carrying `resolved by path`, the entry and its
  id. An entry S2 resolves to none THROWS before the commit stage, naming the writer group, the entry
  as JSON and its folded form, with the phrase `names no roster unit by id and no unit's spec by path`
  and the shared resume remedy. The merge collects every such entry across the writers and throws
  once after it, naming each, so a run with two unplaceable entries is refused for both. Every later reader of `specced.authored` then reads unit ids:
  `authoredIds`, the attended exemption `speccedNow`, and `speccedCount`. `authoredIds` keeps one
  test, the refused exclusion, because the merge settles roster membership and duplicates, and its
  comment says so. `specFolder` is defined once, above the merge, and the commit stage's outside test
  reads that same constant. Observed by AC1, AC3 and AC6.
- **S4** — The commit stage folds each `specs[].path` the commit agent returns through S1 once, where
  `committedSpecs` is read, so its outside test, the path fill and the log all read the folded path.
  After the existing refusals one more runs: for each unit S3 resolved from a path entry, the
  committed row for that id must carry the entry's folded path. Otherwise the stage throws naming the
  entry, the id, the committed path and the commit sha, with `the spec whose H1 defines`, the existing
  `Refusing before any audit or hand-out reads a spec` sentence and the existing remedy. The commit
  agent finds each id's spec by its H1 line, which is the key `gen_build_index.py` reads, so a basename
  route that disagrees with the H1 refuses and never places a file the H1 does not define. Observed by
  AC4 and AC5.
- **S5** — The hand-out's path fill-back, unit 15's S2, compares the caller's `specPath` and the
  committed path, both folded by S1. It writes the committed, folded path onto the unit whenever the
  two differ as written, and it logs `the caller's path differs, and the committed one wins` only when
  they differ after folding. Observed by AC5.
- **S6** — The writers are asked for ids twice. The writer prompt gains the sentence "Name every unit
  in `authored`, `alreadyPresent` and `refused` by its unit id, exactly as this roster spells it,
  never by a path." The three list properties of `SPEC_SCHEMA` take one shared item schema,
  `SPEC_ENTRY`, a string whose `enum` is the roster's unit ids, derived from `units` and never typed.
  A comment above S3's resolution says why it stays beneath that enum: the suite's doubles and a
  resumed run's replay reach the merge without the platform's validation, which is the reason
  `tools/workflows/tier2-review.template.js:458` gives for re-testing its own enums. Observed by AC6
  and AC7.
- **S7** — The build-harness suite gains a GH33 block carrying the arms §7 names. Each writer double
  in it that returns `x` in `authored` returns a unit id of its own fixture instead, because `x` now
  refuses. The number of such doubles is DERIVED by AC7's grep, and it is 5 at writing. Observed by
  AC1 to AC7, which run the block as the slice.
- **S8** — The spec-stage paragraph of `tools/workflows/README.md` gains one sentence stating the S3
  and S4 rule, quoting the S3 refusal phrase. The render is re-made. The review-harness kit version and
  the harness's `unattended-build@` engine identity each move once, after the unit's last move. The
  map's generated symbol index is regenerated for the two new functions. Observed by AC7 and AC8.

## 3. Non-goals (OUT)

- **Resolving `alreadyPresent` and `refused` in the program.** S6's enum holds both to roster ids at
  the platform. Beneath it a `refused` entry still surfaces verbatim in `specRefused` and the DEGRADED
  note, and an `alreadyPresent` entry is only counted, so neither is silent.
- **A unit no list accounts for.** A writer that names a unit in none of the three lists leaves it
  pathless on the roster, and `--dispatch` refuses it as MISSING. That is a different question from
  placing an entry, and it is its own unit if wanted.
- **The commit block.** Units 16, 21 and 32 own its steps, and they are unchanged. S3 changes which
  ids reach the block, never what the block runs.
- **A filename the writers must use.** S2's third arm reads the grammar check 5 already enforces, and
  S6's id sentence makes a path entry the exception rather than the case.
- **Folding the caller's `subjects`, the resolver's returned paths, or `units[].specPath` at entry.**
  Each pins a blob or feeds a compare this unit does not move. S5 folds the caller's path only where
  the fill compares it.
- **A case-sensitive repo prefix.** S1 compares the prefix lowercased, as `repoFold` already does for
  the scratch test. A second repository whose path differs from this one only by case is out of scope.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-15` — the commit stage, its `specs` return, its path fill and
  its refusals with their remedy; without them there is no stage to feed and no fill to fold.
- **consumes-from** `TOOL-aGraftedHelix-21` — the commit block that commits the ids S3 hands it;
  without it the stage has no git sequence to run.

## 4. Design

### Evidence

- The record of run `wf_dff1cb65-954`, read from this session's workflow store on node `a`, holds
  `repo` as `C:/projects/coding-governance/.claude/worktrees/helixir-review-gov-adoption-ce32e1` and
  four units carrying no `specPath`. Its writers returned in `authored`, in turn, the id
  `TOOL-aGraftedHelix-29`, unit 30's spec as that repo path joined to its repo-relative path, and
  units 31 and 32's specs repo-relative. The log read `committed 1 spec(s)`. The hand-out read
  `specced: 4` beside three empty `specPath` values, a count of four specced over one commit, which
  is the `degradation-known-but-unreported` shape.
- `authoredIds` (`tools/workflows/unattended-build.template.js:881`) keeps an entry only when `units`
  carries it as an id, so a path is dropped with no log line. The attended exemption `speccedNow` at
  line 1984 and `speccedCount` at line 864 read the raw list. The path fill at line 1014 compares raw
  strings, and the outside test at line 991 reads the agent's raw path.
- A scratch probe applying the fold and the `-spec-<id>.md` route resolved the four observed entries
  to units 29, 30, 31 and 32, one each.
- Basename routing over every tracked spec file, graded against the file's H1 id, measured on node
  `a` on 2026-10-06 and re-derivable by re-running that probe: 945 tracked spec files, of which 937
  carry an H1 id. A basename ending `-spec-<id>.md` routes 755 of the 937. Check 5's grammar as S2
  writes it routes 934. Neither rule routes any file to an id other than its H1's, and 3 files stay
  unroutable under the grammar. Two near misses routed nothing, as they must: unit 3's basename tried
  against unit 33, and unit 30's basename under another build's folder.
- The suite's `run_wf` strict mode tests required keys and strips undeclared ones, never an item's
  value (`tools/workflows/unattended-build.test.sh:185`). A resume replays the cached answer
  (`tools/workflows/README.md:233`). Both reach the merge with no enum applied.

### The resolution, by spelling

| entry as the writer spelled it | after S1 | S2 arm | outcome |
|---|---|---|---|
| a roster id | unchanged | 1 | that unit |
| a repo-relative path | unchanged | 2, else 3 | the one unit it routes to |
| absolute under the repo, slashes or backslashes | repo prefix stripped | 2, else 3 | the one unit it routes to |
| absolute in the MSYS drive form | drive folded, prefix stripped | 2, else 3 | the one unit it routes to |
| opening with `./` | the `./` stripped | 2, else 3 | the one unit it routes to |
| absolute outside the repo | slashes folded only | none | S3 throws |
| carrying a `..` segment | kept | none from arm 3 | S3 throws unless a caller path equals it |
| matching two units on one arm | — | none | S3 throws |

### Where each step sits

| step | site | on failure |
|---|---|---|
| resolve every `authored` entry | the merge, before the commit stage | throw, nothing committed |
| fold each returned `specs[].path` | where `committedSpecs` is read | the existing outside refusal |
| H1 agreement for path entries | after the existing refusals | throw naming the sha |
| compare the caller and committed paths | the path fill | log on a folded difference |

Under caller `subjects` the commit stage does not run, so S4 does not either. S3's log names each
path entry's id there, and the existing log names the ids left to the caller to commit.

### Inventory

| name | kind | naming cell |
|---|---|---|
| `deriveRepoPath` | function | `js.function` |
| `resolveSpecEntry` | function | `js.function` |
| `SPEC_ENTRY` | constant | none declared for constants |

`python tools/lexicon/lexicon.py --suggest <name> --as js.function` accepted both function names. No
new file, leg or conf key. The map's generated symbol index gains the two functions, and it is not
a ratcheted inventory.

### Rollout

Edit the template, re-render with the protocol-parity suite's renderer mode,
`bash tools/workflows/check-protocol-parity.test.sh --render`, and regenerate the map with
`python tools/codebase-map/gen_map.py --write`. Bump both versions after the last move. One commit.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`, by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/README.md`
- `tools/workflows/tier2-review.template.js`, the version line only
- `tools/workflows/tier2-review.js`, by the render
- `memory/map/generated/symbols.json`, by the map generator

### Alternatives rejected

Each with the test that rejected it, per BUILD-METHOD M12.

- **Resolving at `authoredIds` rather than at the merge.** The attended exemption reads the raw list
  at line 1984, so a path-spelled unit would be graded on its stale MISSING plan state and refused.
  AC6's staged break is that test.
- **The commit agent resolving path entries by their H1 before it commits.** The program would know
  no id for a path entry until the agent returned, so the commit subject, which the program composes
  from `authoredIds` at line 933, and the roster-membership test would both move onto the agent's
  claim. An unplaceable path would then be caught only after a commit.
- **A basename route ending `-spec-<id>.md` only.** It places 755 of 937 tracked specs against the
  grammar's 934, by the probe in Evidence. F2 records the pick.
- **The prompt and the schema alone, with no program resolution.** The suite's doubles and a resume's
  replay reach the merge unvalidated (Evidence), and the brief requires placement whatever the
  spelling.
- **A fold written at each compare.** The fill and the outside test would each derive it, which is
  `two-guards-one-question-two-answers`; S1 is the one derivation.

## 5. Production-readiness checklist

- security — No new write path. The stage commits what the writers wrote, now all of it. S4 refuses a
  routed file the H1 does not define, so a misnamed file cannot ride a unit's commit.
- perf / scale — One regular expression per roster unit per path entry, over a roster of tens, and no
  new agent call.
- error / empty / loading states — An empty or absent path folds to empty and matches nothing. An
  unplaceable entry throws before the commit, naming itself. A routed path the H1 disagrees with
  throws after the commit, naming the sha. A writer the platform's enum defeats returns nothing and
  reads as a dead writer, its units refused and the run DEGRADED, as today.
- observability — One `resolved by path` log line per path entry. Each refusal names the entry as
  JSON beside its folded form.
- risks — S2's third arm copies check 5's grammar into a second language. A drift between the two
  costs a refusal, never a misplacement, because S4 holds the H1 authoritative. Whether the platform
  enforces `enum` on array items is UNVERIFIED; S3 stands beneath it either way.
- testing — The GH33 arms, each observed RED under its own staged break (§6).
- migration — None. A well-formed caller and a writer returning ids see no change.
- user docs — N/A: the stage is internal to the harness; the kit README sentence is S8.

## 6. Acceptance criteria

Criteria AC1 to AC6 run as a slice of the build-harness suite in the session scratchpad, under a name that is
not a suite name: the suite's prologue, whose `run_wf` drives the render through stub agents, and
the GH33 block. Each staged break is made in a scratch COPY of the render and deleted after its run.
Unless a criterion says otherwise, a fixture's units are pathless, carry no `subjects` and no
`specAudit`, and sit at orders 1 upward, so each writer holds one unit. The commit double returns
`committed: true`, a 40-hex `sha`, and one `specs` row per authored id at that unit's spec path
under the build's spec folder.

- **AC1** — When four units `A-tB-1` to `A-tB-4` run against a fixture repo spelled with a drive
  letter, and the four writer doubles return in `authored`, in turn, the id `A-tB-1`, unit 2's spec
  path absolute under the repo with forward slashes, and units 3 and 4's spec paths repo-relative,
  each basename a date then `-spec-` then the id, the trace carries one `agent:commit:specs:tB`. Its
  commit line names `spec(tB): A-tB-1 A-tB-2 A-tB-3 A-tB-4`, the log reads `committed 4 spec(s)` and
  carries three `resolved by path` lines, and every returned roster row carries a non-empty
  `specPath`.
  Red when: the merge does not resolve a path entry to its unit, as in `wf_dff1cb65-954`. Staged: the
  merge's call to the resolver bypassed in a render copy, so every entry passes through as written.
  Because S3 moves the roster-membership test out of `authoredIds`, the raw paths then reach the
  commit line beside `A-tB-1`, and the run throws `named no committed spec` for them, rather than
  committing `A-tB-1` alone as the pre-S3 tree did.
- **AC2** — When five units run against a fixture repo spelled with a drive letter, `A-tB-5` carrying
  a caller `specPath` whose basename follows no recording grammar, and the writers return unit 1's
  spec absolute with backslashes, unit 2's in the MSYS form opening with the drive letter as a
  directory, unit 3's under a basename with no family, unit 4's under a basename with a tail after its
  sequence number, and unit 5's caller path, no `THROW` line is printed and the commit line names all
  five ids.
  Red when: any one spelling is not placed. Staged: four render copies, each disabling one mechanism.
  Without the backslash fold unit 1 refuses; without the drive fold unit 2 refuses; without the second
  arm unit 5 refuses; with the third arm narrowed to a basename ending `-spec-<id>.md`, units 3 and 4
  refuse.
- **AC3** — When one writer returns a single `authored` entry, once per entry of the list below, each
  run ends in `THROW` carrying `names no roster unit by id and no unit's spec by path` and the entry
  as JSON, and its trace carries no `agent:commit:` line. The entries: the id `A-tB-9`, which the
  roster lacks; a spec-folder path whose basename routes to no unit; a path under the build's prompts
  folder; a spec-folder path carrying a `..` segment; an absolute path outside the fixture repo; an
  absolute path under a sibling directory whose name extends the repo's; and, beside units `A-tB-1`
  and `B-tB-1`, a basename with no family that routes to both.
  Red when: an entry nobody can place is dropped and the run goes on. Staged: the throw deleted in a
  render copy, where the `A-tB-9` run reaches `RESULT`.
- **AC4** — When a writer names unit 2's spec by a path whose basename routes to `A-tB-2`, and the
  commit double returns `A-tB-2` at another path under the spec folder, the run ends in `THROW`
  carrying `the spec whose H1 defines`, the entry, both paths and the commit sha, beside
  `Refusing before any audit or hand-out reads a spec`, and no `"roster"` key is printed.
  Red when: a routed file and the file the H1 defines disagree and the commit's file is handed out.
  Staged: the H1 agreement test deleted in a render copy, which reaches `RESULT` with the commit's path
  on the roster.
- **AC5** — When unit `A-tB-1` carries a caller `specPath` absolute under the fixture repo, its writer
  returns the id, and the commit double returns the same spec absolute too, no `THROW` line is
  printed, the roster row's `specPath` is the repo-relative path, and no log line carries
  `the caller's path differs`.
  Red when: either path is compared as written. Staged: the commit return read without the fold, which
  throws `named a path outside`; and the fill comparing raw strings, which logs
  `the caller's path differs`.
- **AC6** — When the attended fixture, unit `A-tB-1` at `planState` `MISSING` with pinned `subjects`
  and a caller `specPath`, runs with a writer that returns that caller path in `authored`, the run
  reaches `RESULT` and the log names `A-tB-1` as left to the caller to commit. Every
  `prompt:spec:tB:` trace line carries `by its unit id`.
  Red when: the attended exemption reads the raw entry and refuses `A-tB-1` as MISSING, or the writer
  prompt loses the sentence. Staged: the resolution moved from the merge to `authoredIds` in one
  render copy, which prints the plan-state refusal naming `A-tB-1`; the sentence deleted in another.
- **AC7** — When the renderer's `--render` mode has run at the build commit,
  `git status --porcelain tools/workflows/` prints nothing, `node tools/workflows/check-workflow-syntax.js`
  reports every script parsed clean, and `grep -c "items: SPEC_ENTRY" tools/workflows/unattended-build.js`
  prints `3`. The line `grep -n "const SPEC_ENTRY" tools/workflows/unattended-build.js` prints carries
  `enum:`. `grep -c '"authored":\["x"\]' tools/workflows/unattended-build.test.sh` prints `0`, and
  `grep -c "names no roster unit by id and no unit's spec by path" tools/workflows/README.md` prints a
  non-zero count.
  Red when: the render is stale, a list of `SPEC_SCHEMA` lacks the enum, a double still authors a
  non-roster placeholder, or the kit README says nothing of the rule. Staged: the enum deleted from a
  scratch copy of the template and re-rendered, which leaves the `const SPEC_ENTRY` line without
  `enum:`.
  figure: `3` is PINNED, the three lists of `SPEC_SCHEMA`.
- **AC8** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no review-harness carrier left behind, and
  `bash tools/check-kit-versions.sh` exits 0. Line 3 of `tools/workflows/unattended-build.js`
  carries an engine identity one minor step above its value at the pass's parent.
  Red when: the kit's shipped bytes moved without its version.
  figure: both versions are DERIVED from the pass's parent at observation time.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · GH33, four writers naming their specs by id, absolute path and relative path reach one commit and four roster paths; stage the merge's resolver call bypassed · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · GH33, five spellings each placed; stage the backslash fold, the drive fold and the second arm each removed, and the third arm narrowed · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · GH33, seven unplaceable entries each throw with no commit stage; stage the throw deleted · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · GH33, a routed path the H1 disagrees with throws after the commit; stage the H1 agreement test deleted · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · GH33, absolute caller and commit paths fold equal; stage each of the two folds removed · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · GH33, an attended path entry passes the plan-state exemption and the writer prompt asks for ids; stage the resolution moved to authoredIds, and the sentence deleted · the suite's floor rises by the arms added

The close runs the legs and the suite. A pass runs the slice of §6 and the commands of AC7 and AC8
as its check.

## 8. Open questions

- **F1 — Does the writer schema hold the three lists to roster ids, beside the prompt asking for
  them?**
  Option A is both: `SPEC_ENTRY`'s `enum` holds the roster's ids, so the platform bounces a path or a
  typo back to its writer as a validation error, and S3 places or refuses whatever arrives by a route
  the platform does not validate. Option B is the prompt alone: the lists stay plain strings, and S3
  alone places or refuses every entry on every route.
  B's case: the four entries of `wf_dff1cb65-954` all resolve under S2, so the enum would only have
  bounced entries the program places, at the cost of a retry turn. Beneath the enum, S3 is reachable
  only from the doubles and a replay, which is `guard-above-a-fold-makes-its-fallback-dead` on the live
  route. A's case: a typo such as a non-roster id becomes a writer retry rather than a run-ending
  throw and a commit by hand, and `refused` and `alreadyPresent`, which S3 does not resolve, are held to
  ids at the boundary. That meets more stated criteria and leaves one follow-up fewer. The fallback's
  reason to stay is written beside it (S6), as `tools/workflows/tier2-review.template.js:458` already
  does for its own enums.
  RESOLVED (agent, 2026-10-06, delegated): A, the prompt sentence and the enum both, by BUILD-METHOD
  M3's most-feature-rich rule. No veto applies: the schema is internal to the harness, and neither
  option widens a write surface.
- **F2 — How wide is S2's basename route?**
  Option A is a basename ending `-spec-<id>.md`, the convention the commit prompt's step 1 already
  states. Option B is check 5's recording grammar written in terms of the unit's id, with the family
  and the tail optional.
  Measured over every tracked spec (§4 Evidence): A routes 755 of the 937 files carrying an H1 id and
  B routes 934, and neither routes a file to an id other than its H1's. B copies a grammar into a
  second language, and S4's H1 agreement makes that copy's drift a refusal, never a misplacement.
  RESOLVED (agent, 2026-10-06, delegated): B, the more feature-rich survivor. No veto applies.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, adopted mid-run from the spec commit stage's first live use,
  `wf_dff1cb65-954`, grounded against the template at `bdc93251` and a basename-routing probe over
  every tracked spec.
- rev-2 · 2026-10-06 · node a · build pass: AC1's red stated what the pre-S3 tree printed, which the
  staged break cannot reproduce once `authoredIds` loses its membership test, so it now states what
  the break prints; S3 says the merge collects every unplaceable entry into one throw. Re-read against
  the template at `0bc5f0f8`, after unit 32's `--only` commit: S1 to S8 still hold as written.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "fold a path an agent returned to repo-relative forward
slashes and match it to a unit id"` ranked name-stem neighbours and printed `unscanned layers: .sh`.
Its nearest real seams are Python: `parse_spec_h1` and `build_spec_path_re` in
`tools/memory-tree/tree_lib.py`, the one predicate for which id a spec defines, and `derive_spec_unit`
in `tools/runlog/model.py`. A workflow script imports nothing, so none of them can be called; S4
reaches the same H1 key through the commit agent's existing step 1 rather than copying it. The seams
extended are the template's own: `repoFold` for S1's prefix, and unit 15's commit stage for S3 to S5.
No existing seam fits a JavaScript resolver from an entry to a unit. The recall probe returned this
unit's brief and its rescope row in the run record, units 15 and 16's specs and unit 15's ledger, and
`TOOL-aHoistedPass-35`, the empty `specPath` ask unit 15 answered. No record covers an entry spelled
as a path.

Recall terms used: authored alreadyPresent refused writer spec commit stage roster unit id path normalise repo-relative specPath fill

The question passed with them: "how does the spec commit stage match what the writers authored to
roster units, and how are agent-returned paths normalised".

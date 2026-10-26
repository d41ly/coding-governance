# TOOL-dBoundRoles-44 — the round-1 audit's 11 docs-and-records minors: memory readers re-derived, frozen receipt waived, gotcha pages re-pointed, two Skills fitted, legacy registry named, workflow suites re-keyed and the close's harness swap checked

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 29 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-37-round1-fix-return.md) | research | TOOL-dBoundRoles-37 TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 |
| [2026-10-26-build-TOOL-dBoundRoles-43-round1-size-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-43-round1-size-return.md) | research | TOOL-dBoundRoles-3 TOOL-dBoundRoles-24 TOOL-dBoundRoles-43 |
| [2026-10-26-build-TOOL-dBoundRoles-44-deviation-441.md](../build/2026-10-26-build-TOOL-dBoundRoles-44-deviation-441.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-44-deviation-442.md](../build/2026-10-26-build-TOOL-dBoundRoles-44-deviation-442.md) | deviation | — |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed
43 MEDIUM and 14 LOW findings. BUILD-METHOD M4 batches them into two units because they split into
disjoint write sets by M6; `TOOL-dBoundRoles-43` §4 "Why two units" holds the cut and its evidence. This
unit takes the 11 whose items write only docs, Skills, the hygiene check, gotcha pages, dead-path rows,
the workflows suites' role maps and the build README, and read no file unit 43 writes: report ids 3, 5,
16, 17, 26, 28, 43, 48, 49, 51 and 62, nine MEDIUM and two LOW. Each is its own scope item; before the
split they were unit 43's S3, S4, S18, S20, S26, S30, S31, S33, S42, S47 and S48. Id 3 is the MEDIUM half
of the defect `TOOL-dBoundRoles-42` closes at HIGH.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M3 | 3 | unit 25 AC14, S8 | S1 |
| M4 | 5 | unit 1 S3, Files touched; unit 18 AC7 | S2 |
| M15 | 26 | unit 25 S8 | S3 |
| M17 | 28 | unit 10 §4 Migration, §5 | S4 |
| M22 | 43 | unit 25 S8, §7 | S5 |
| M26 | 48 | unit 17 S6, Files touched | S6 |
| M27 | 49 | unit 13 S7, AC6, §7 | S7 |
| M29 | 51 | unit 21 S8 | S8 |
| M38 | 62 | unit 25 §4 Rollout | S9 |
| L3 | 16 | unit 11 §4 Migration | S10 |
| L4 | 17 | unit 24 §5 | S11 |

## 2. Scope (IN)

- **S1** — id 3. The `memory/` half of unit 25's readers re-derived. The pass runs unit 25 AC14's grep
  filtered to `memory/` at the build run's base, compares it with `TOOL-dBoundRoles-42` S1's class table,
  and records each file in neither, with its class, in this unit's ledger. Unit 25's ledger answers AC14
  in the AMENDED form, naming `TOOL-dBoundRoles-42` S4 as its population. Observed by AC1.
- **S2** — id 5. The three `tools/workflows/` readers unit 1 S3 re-keys carry no old stem:
  `tools/workflows/README.md`'s examples, and the FULL maps and `OC_ROLES` of
  `tools/workflows/tier2-review.test.sh` and `tools/workflows/unattended-build.test.sh`, name
  `gov-reviewer`. This pass re-keys any spelling unit 1 left. Observed by AC2.
- **S3** — id 26. The frozen receipt stays frozen. `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`
  is never edited; each of its lines `tools/check-dead-paths.sh --list` reports for `agent-cap.js` or
  `agent-cap.test.sh` gets a `tools/dead-path-waivers.txt` row with the reason rows 55-58 already give. The
  pass re-derives unit 25's whole reader list at the build run's base, the base unit 25 S8 derives its own
  list at, with `git grep -l -F 'agent-cap.js'`, only `memory/builds/` excluded, and records each
  difference from unit 25's S8 in this unit's ledger. Observed by AC3.
- **S4** — id 28. The kickoff Skill no longer sends the main loop to a refused tool.
  `skills/session-kickoff/SKILL.md:21` names shell probes (`grep` and `git grep` through Bash) and `Read`,
  not `Grep`. The file measured 18310 of its 18432-byte ceiling at base, so the line grows by at most 122
  bytes. Observed by AC4.
- **S5** — id 43. The gotcha pages name live files. Every page under `memory/gotchas/` that
  `tools/check-dead-paths.sh --list` reports for `agent-cap.js` or `agent-cap.test.sh` names
  `tools/roles/spawn-guard.js`, `tools/hooks/scratch-guard.js` or the moved rule's home instead. A gotcha
  page is served as live, so it is re-pointed, never waived. Observed by AC5.
- **S6** — id 48. The legacy registry is a named kit-shipped case. `tools/memory-tree/check-memory-hygiene.sh`
  check 3 admits `F:work-order-legacy.txt` by name beside `F:role-stand-in-waiver.txt`, with a comment
  naming the roles kit as its shipper; `tools/memory-tree/HYGIENE.template.md` gains its registry row,
  `memory/HYGIENE.md` its render; and `.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA` does not carry it.
  Observed by AC6.
- **S7** — id 49. The unattended Skill fits its ceiling. The `handoff.py facts` line unit 13 S7 adds to
  `tools/unattended/SKILL.template.md` is paid for by a trim of that template, so the render
  `.claude/skills/unattended/SKILL.md` is at most 10240 bytes; it measured 10237 at base. The VERBS
  guide's render `memory/guides/UNATTENDED-VERBS.md` is re-rendered from its template (§8 F2). Observed by
  AC7.
- **S8** — id 51. No in-branch mirror. No commit of this build writes `.governance/policy.json`; the
  mirror is regenerated at the landing, as `TOOL-dGroundRules-5` S3 gives, and unit 21 S8's second commit
  is not made. Observed by AC8.
- **S9** — id 62. A harness swapped for the close is restored and checked. The build README's
  build-level rules gain one rule: a harness this build edited runs at its landed bytes only by writing
  `git show <L>:<rel>` over it inside a shell whose `trap` restores it with `git checkout -- <rel>` on every
  exit, followed by `git diff --quiet -- <rel>`, whose exit unit 25's ledger records (§8 F3). Observed by
  AC9.
- **S10** — id 16. The fork-record cutoff falls after this build's specs. `FORK_RECORD_CUTOFF`, which unit
  11 S2 declares in `.memory-tree.conf`, is later than the filename date of every spec under
  `memory/builds/dBoundRoles/spec/`; six of the 26 unit specs write the `admitted-by:` tail, a fact this
  unit's ledger records for unit 11. Observed by AC10.
- **S11** — id 17. The help page states the anchor refusal. `help/roles.md`, under "How a task reaches an
  agent", says the render refuses a work order whose framing points at a fact it does not hand. Observed
  by AC11.

## 3. Non-goals (OUT)

- Rewording the spec text of units 1 to 26. Each item is closed by what this pass builds or observes;
  where a landed criterion cannot hold as written (unit 25 AC14, S1), that unit's ledger answers it in the
  AMENDED form, naming this unit.
- The 46 minors of `TOOL-dBoundRoles-43`, and the HIGH findings `TOOL-dBoundRoles-37` to `-42`. S1, S3
  and S5 build on `TOOL-dBoundRoles-42`'s class table and do not restate it.
- The report's left-shift gates: the spec-lint joins, the build-order check, the checklist entries and
  the duplicate-constant gate. No clause of this build names them.

### Edges

- **consumes-from** `TOOL-dBoundRoles-1` — the merged roster, whose `tools/workflows/` readers S2 re-keys (id 5)
- **consumes-from** `TOOL-dBoundRoles-10` — `checkDriverRead`'s refusal of the search tool, which S4's kickoff line stops naming (id 28)
- **consumes-from** `TOOL-dBoundRoles-11` — `FORK_RECORD_CUTOFF`, which S10 places after this build's spec dates (id 16)
- **consumes-from** `TOOL-dBoundRoles-13` — the `facts` verb's Skill line, which S7 fits under the Skill's ceiling (id 49)
- **consumes-from** `TOOL-dBoundRoles-17` — the seeded `work-order-legacy.txt`, which S6 admits by name in hygiene check 3 (id 48)
- **consumes-from** `TOOL-dBoundRoles-21` — S8's mirror step, whose second commit S8 leaves unmade (id 51)
- **consumes-from** `TOOL-dBoundRoles-24` — the anchor check's docs promise, which S11 writes into `help/roles.md` (id 17)
- **consumes-from** `TOOL-dBoundRoles-25` — the retirement, S8's readers and the close, whose memory half, frozen receipt, gotcha pages and harness swap S1, S3, S5 and S9 complete (ids 3, 26, 43 and 62)
- **consumes-from** `TOOL-dBoundRoles-42` — the class table, whose memory half S1 re-derives and whose fixture and gotcha rows S3 and S5 dispose (ids 3, 26 and 43)
- **hands-off** `TOOL-dBoundRoles-51` — AC1, AC8, AC9 and S4, which unit 51 completes; this unit's ledger answers AC8 and AC9 AMENDED, naming unit 51, and cites unit 42's AC14 answer rather than restating it (ids 3, 8, 20 and 31 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-58` — AC8 and AC9, which unit 58 bumps with the text unit 51 answers them by (id 48 of the round-1 audit of units 45 to 51)

## 4. Design

### Why this unit stands apart

`TOOL-dBoundRoles-43` §4 "Why two units" holds the cut. This unit's write set is its Files touched below,
none of it in unit 43's, and no criterion here reads a file unit 43 writes: S1 and S3 read the build
run's base, S5's pages name the two hook files by path, AC3 and AC5 read the dead-path checker's lines for
the receipt and the gotcha pages only, and every other criterion reads a file this unit writes or the
commit log. The two build concurrently.

### How an item closes

As unit 43 §4 states for both batches: each item states the built tree's end state, and the pass does
what is missing or records that a landed unit already left it.

### Inventory

Minted: the dead-path waiver rows of S3, check 3's named case and its `HYGIENE.template.md` registry row
(S6), and the README rule of S9. No function, constant or plant.

### Migration

None: no stored data changes. S6's named case is additive for an adopter's hygiene run.

### Rollout

Live at landing, at order 29, after every unit it repairs and beside `TOOL-dBoundRoles-43`.

### Files touched (estimate)

- `tools/workflows/README.md`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/dead-path-waivers.txt`
- `skills/session-kickoff/SKILL.md`
- `memory/gotchas/`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`
- `tools/unattended/SKILL.template.md`, rendered to `.claude/skills/unattended/SKILL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `help/roles.md`
- `.memory-tree.conf`
- `memory/builds/dBoundRoles/README.md`

### Alternatives rejected

- **Keeping these items in `TOOL-dBoundRoles-43`.** The one spec was 60120 bytes against the 49152
  ceiling, and M4 has disjoint minors build concurrently.
- **Waiving the gotcha pages (S5).** A gotcha page is served as live; a waiver leaves it misleading.
- **Raising the unattended Skill's ceiling (S7).** §8 F2.

## 5. Production-readiness checklist

- security — no new write path; S6 admits one registry file by name in check 3, never a pattern.
- perf / scale — greps, byte counts, one dead-path listing and one hygiene run over a fixture.
- error / empty / loading states — S1 records a `memory/` reader no class takes rather than passing it.
- observability — the ledger records S1's classes and S3's differences.
- risks — S9 depends on the main loop following a written rule, whose check unit 25's ledger records;
  S7's trim must keep every line the Skill's readers act on.
- testing — AC1 to AC11 by grep, diff, byte count, the dead-path checker's `--list` and the hygiene check
  on a fixture; the arm of §7 at the close.
- migration — none.
- user docs — `help/roles.md` by S11.

## 6. Acceptance criteria

- **AC1** — When unit 25 AC14's grep filtered to `memory/` runs at the build run's base, every file it
  prints is in `TOOL-dBoundRoles-42`'s class table or on a line of this unit's ledger with its class.
  Red when: a `memory/` reader has neither.
- **AC2** — When `git grep -n -E 'gov-(spec|diff)-reviewer' -- tools/workflows/README.md tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh`
  runs on the built tree, it prints nothing.
  Red when: a suite's role map still spells an old stem.
- **AC3** — When `git diff --quiet <BASE> HEAD -- tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`
  runs it exits 0, and `bash tools/check-dead-paths.sh --list` marks every receipt line naming
  the retired hook or its suite waived.
  Red when: the frozen receipt is edited, or its lines red the dead-path leg.
- **AC4** — When `grep -n 'Read/Grep' skills/session-kickoff/SKILL.md` runs it prints nothing, and
  `wc -c < skills/session-kickoff/SKILL.md` prints at most 18432.
  Red when: the kickoff tells the main loop to use a tool the default refuses, or the file outgrows its
  ceiling.
- **AC5** — When `bash tools/check-dead-paths.sh --list` runs on the built tree, it prints no hit under
  `memory/gotchas/` for the retired hook or its suite.
  Red when: a live gotcha page names the deleted hook.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 3` runs over a scratch fixture tree
  holding the seeded legacy work-order registry under its project folder, it names no finding for that
  file, and `grep -n 'work-order-legacy' .memory-tree.conf` prints nothing.
  Red when: the file is refused, or admitted through the project escape that hides the adopter defect.
  fixture: a scratch tree under the run's scratch path.
- **AC7** — When `wc -c < .claude/skills/unattended/SKILL.md` runs it prints at most 10240,
  `grep -n "facts --build" tools/unattended/SKILL.template.md` names the line, and the VERBS guide's
  render equals its template's render.
  Red when: the line reds the size leg, or the guide drifts from its template.
- **AC8** — When `git log --format=%h <BASE>..HEAD` runs limited to the policy mirror's path, it prints
  nothing.
  Red when: a commit of this build writes the guarded mirror.
- **AC9** — When `grep -n 'git diff --quiet' memory/builds/dBoundRoles/README.md` runs, it names the
  close rule, and unit 25's ledger records that check's exit for each swapped harness.
  Red when: a swapped harness's restore is unchecked.
- **AC10** — When `grep -n FORK_RECORD_CUTOFF .memory-tree.conf` runs, its date is later than every
  filename date under `memory/builds/dBoundRoles/spec/`.
  Red when: the cutoff grades this build's specs that carry no tail.
- **AC11** — When `grep -n "anchor" help/roles.md` runs, it names the refusal under "How a task reaches an
  agent".
  Red when: the docs promise has no line behind it.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `scratch-guard self-test` · `dead-path carriers (deleted files still named)` · `kickoff engine size <=18KiB` · `manifest-check self-test` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `unattended skill size` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC6 · the roles kit's legacy work-order registry under a fixture project folder, staged by a check 3 without its named case, which refuses the file · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause whole or in part;
  veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Trim the template or raise its ceiling (id 49)?** Options: (a) trim the same template; (b) raise
  the 10240 ceiling. (b) is an owner change to a declared ceiling (M3 veto 2). RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the one survivor. widens: none · relaxes: none
- **F3 — A copy outside the tree, or a guarded swap (id 62)?** Options: (a) run the landed harness from a
  scratch worktree; (b) the trap-guarded swap and its check. (a) runs a `scriptPath` outside the declared
  harnesses, which unit 25's admission refuses. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the one
  survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, split from `TOOL-dBoundRoles-43` at rev-1 by the round-1 fix brief's
  R3: the 11 minors whose write set is disjoint from unit 43's, each item and criterion carried as it was
  there, S3 stating the base its re-derivation reads.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dBoundRoles-51, the minors batch of the round-1 audit of units 37 to 44; it names AC8's and AC9's AMENDED answers. Nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.

## 10. Reuse audit

The seams are the dead-path gate's waiver registry (`tools/dead-path-waivers.txt`, whose rows 55-58
already waive the frozen receipt's dead lexicon path), hygiene check 3's named kit-shipped cases
(`tools/memory-tree/check-memory-hygiene.sh:718-745`, the precedent `TOOL-bQuiltedLantern-3` sets in
`memory/DECISIONS.md`), and `TOOL-dBoundRoles-42`'s class table.
`python tools/codebase-map/reuse_lookup.py "admit a kit-shipped registry file by name and waive a frozen fixture's dead path"`
ranked `fixture`, `kit_rel`, `resolve_kit_dir`, `frozen` and `build_fixture`, none a registry admission or
a waiver row, so no existing seam fits beyond the two registries named.

Recall terms used: `python tools/memory-recall/query.py "how is a kit-shipped registry admitted in hygiene check 3 and a frozen fixture's dead path waived" --terms "hygiene check 3 named registry role-stand-in-waiver PROJECT_REGISTRY_EXTRA dead-path waiver frozen receipt gotcha re-point"`

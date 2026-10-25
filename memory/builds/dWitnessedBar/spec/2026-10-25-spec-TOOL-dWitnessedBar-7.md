# TOOL-dWitnessedBar-7 — `test.seen-red` reading one seen-red record per gate a build adds or changes, the acceptance-ledger line standing in for `build.acceptance`

**Status:** DEFERRED · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 26 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0345@72933671 whole
**Carries:** node:item.test.seen-red
**Carries:** node:record-kind.seen-red

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71.md](../build/2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-7-deviation-72.md](../build/2026-10-25-build-TOOL-dWitnessedBar-7-deviation-72.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |

<!-- /gen:spec-records -->

## 1. Goal

"A gate never seen red is not a gate" has no recorder (gap-test-06): the build method tells the main
loop to observe each new arm red and green and to record both in the acceptance ledger
(`memory/guides/BUILD-METHOD.md:280-282`), and nothing keys that observation by leg or reads it
back. This unit fixes the seen-red record's grammar, one record per gate a build adds or changes,
keyed by leg and red SHA, and builds `test.seen-red`, which reads those records and turns red on a
gate with none. Until dScopedBuild lands `build.acceptance` as the record's writer, the main loop's
acceptance-ledger line is the record (the owner's FK-4-12 and FK-5-2).

## 2. Scope (IN)

- **S1** — The seen-red line, the record's one grammar (shared interface I16), a line of an
  `**Evidences:** <unit id>` block of a `journal` record:
  ``- seen-red — `<leg name>` — red `<sha>` — green `<sha>` — <the staged break>``, the leg its
  free-text manifest `name` (I2's join key), each SHA 8 to 40 lowercase hex, the break one line of
  prose. Stated once in `memory/HYGIENE.md`'s "Acceptance ledger" section, rendered from
  `tools/memory-tree/HYGIENE.template.md`. Observed by AC1 and AC6.
- **S2** — `iter_evidence_lines(text)` in `tools/memory-tree/tree_lib.py`: the
  `**Evidences:**`-block walk `tools/memory-tree/deviation_join.py:608-623` does inline, extracted at
  this, its second Python instance, yielding `(line number, unit, line)` for a `journal` record only.
  `deviation_join.py` calls it, its verdicts unchanged. Observed by AC5.
- **S3** — `tools/memory-tree/seen_red.py`, the reader. `read_seen_red_records(root)` returns every
  tracked journal record's seen-red lines as `{leg name: [(red sha, green sha, record path, line)]}`,
  refusing a line that opens `- seen-red` and breaks S1's grammar by naming it. Observed by AC1, AC6.
- **S4** — The gates a build adds or changes, `derive_owed_gates(root, slug, base)`: (a) every leg
  whose `tools/gate-legs.json` row at HEAD is absent at `base` or carries a different `argv`, and
  (b) every `New arm:` line of a spec under `memory/builds/<slug>/spec/`, resolved to the manifest
  legs whose `argv`, `{prefix}` resolved, names the line's suite path; a line resolving to no leg is
  named and owes nothing. Observed by AC2 and AC3.
- **S5** — The join, `test.seen-red`'s check: `python tools/memory-tree/seen_red.py --build <slug>
  [--base <sha>]`, `base` defaulting to the `base:` fact of the build's `RUN.md`. Each owed gate is
  joined to a seen-red line naming it, under any `**Evidences:**` block of a journal record of that
  build; an `(b)` gate is satisfied by a line naming any leg it resolved to. It prints one line per
  gate, `seen-red: <leg> · <red sha8> · <record>` or `seen-red: <leg> · NO RECORD`, and exits 1 on any
  `NO RECORD`, 0 when every gate has one, and 2 when it cannot answer (no base, an unreadable
  manifest). An empty owed set prints `seen-red: <slug> adds or changes no gate · nothing joined` and
  exits 0, never silently. Observed by AC2, AC3 and AC4.
- **S6** — `python seen_red.py --fixture --plant <case>` builds a throwaway repository in the system
  temp directory and runs S5 over it, for the cases `seen`, `unseen-gate`, `unseen-arm`, `bad-line`
  and `empty` of §4. Observed by AC2, AC3, AC4 and AC6.
- **S7** — The item: `item.test.seen-red`'s actor is the command row `seen-red` of the memory-tree
  kit, written through TOOL-dDeclaredLoop-6 S3's factory, `python tools/playbook/core.py new command
  seen-red --kit memory-tree --run seen_red.py`; where TOOL-dDeclaredLoop-12's landed `[[item]]` row
  for `item.test.seen-red` names another actor or a `stand-in:` route, the pass re-points it to
  `command:memory-tree.seen-red`. Observed by AC7.
- **S8** — Check 23 stays blind to the line: its ledger awk
  (`tools/memory-tree/check-memory-hygiene.sh:3135-3160`) closes the open answer at a line opening
  `- seen-red`, so the line's tokens never join an `AC<n>` answer's token list. Observed by AC5.
- **S9** — The method points at the grammar: `BUILD-METHOD.md` M8's "Observe the owed arms" sentence
  records both observations "as a seen-red line", naming `memory/HYGIENE.md`'s "Acceptance ledger",
  and ends naming `seen_red.py --build <slug>` as the read-back, rendered from
  `tools/memory-tree/BUILD-METHOD.template.md` inside M1's 30720-byte budget. Observed by AC7.

## 3. Non-goals (OUT)

- `build.acceptance`, the executor that re-runs a planted red and writes the record: dScopedBuild's
  (packet Non-goals, Later builds named). This unit ships the stand-in and names the hand-over.
- A typed record file for the kind in `tools/memory-tree/build_records.py` (§8 F2).
- Observing any arm: the main loop observes, as M8 says. This unit reads what it recorded.
- Routing a missing record to `build.fix-pass`: the item's route is TOOL-dDeclaredLoop-12's row.
- Grading the leg's guard, ceiling or other fields as a change to the gate (§8 F3).
- A new gate leg: the reader runs as the item's command and at the close, and its arms join the
  memory-hygiene self-test.

### Edges

- **hands-off** `TOOL-dWitnessedBar-28` — `record-kind.seen-red`, read through `read_seen_red_records`, so a repository's leg is counted in its pack once a seen-red line names it
- **hands-off** external — dScopedBuild's `build.acceptance` takes over the write: it emits S1's fields, `Leg`, `Red`, `Green` and `Break`, and `read_seen_red_records` is the one reader it joins
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 11, 17, 20 and 29: `seen_red.py`'s suite-path rule and Gates-bounded arm reader, and the grant for its carrier edits, each a scope item of that unit
- **hands-off** `TOOL-dWitnessedBar-57` — its `memory/HYGIENE.md` and BUILD-METHOD carrier edits, whose commits' grant trailers the resolver and ledger minors batch observes (id 10)

## 4. Design

### The line

```markdown
**Serves:** journal TOOL-dX-4

**Evidences:** TOOL-dX-4
- AC1 — `python gov_tag.py --fixture --plant policy-ns-word` — exits 1 naming the plant
- seen-red — `playbook render selftest` — red `3f2b31b5` — green `3f2b31b5` — the `policy-ns-word` plant with its namespace row deleted
```

`red` is the commit over which the break was staged and observed red; `green` the commit at which the
arm read green once restored, usually the same. The key is `(leg, red)`: a second line for one leg at
another red SHA is a second observation, and both are kept.

### The owed set

```
(a) legs(HEAD) where name not in legs(base) or argv(HEAD, name) != argv(base, name)
(b) for each "New arm: <suite path> · ..." line in builds/<slug>/spec/*.md:
        legs(HEAD) whose argv, {prefix} -> tools, contains <suite path>
```

The manifest at `base` is read with `git show <base>:tools/gate-legs.json`. A `New arm:` line's suite
path is its first field, split on ` · `. Two legs sharing a script (`playbook render wiring` and
`playbook render selftest` both run `adopt-playbook.sh`) make one owed gate satisfied by either name.

### The plants

| Case | Fixture | Exit |
|---|---|---|
| `seen` | a leg added past base, a journal line naming it | 0 |
| `unseen-gate` | a leg added past base, no line | 1, `<leg> · NO RECORD` |
| `unseen-arm` | a spec's `New arm:` line on an existing leg's suite, no line | 1, naming that leg |
| `bad-line` | a `- seen-red` line with no red SHA | 2, naming the record and line |
| `empty` | no leg added, no `New arm:` line | 0, the announced empty line |

### Inventory

Minted: the seen-red line grammar; `iter_evidence_lines`; `tools/memory-tree/seen_red.py` with
`read_seen_red_records`, `derive_owed_gates` and the verbs `--build`, `--base`, `--fixture`,
`--plant`; the command row `seen-red` of the memory-tree kit. Naming cells: each function is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass.

### Migration

Additive. Landed ledgers carry no seen-red line, so `seen_red.py --build` over a closed build names
its unrecorded gates; it is run on a build from this unit on, and is no gate over landed builds.

### Rollout

Live at landing as a command; the memory-tree kit's version moves (`KIT_MEMORY_TREE_VERSION`,
`tools/memory-tree/check-memory-hygiene.sh:68`).

### Files touched (estimate)

- `tools/memory-tree/seen_red.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`
- `tools/memory-tree/BUILD-METHOD.template.md`, rendered to `memory/guides/BUILD-METHOD.md`
- `memory/HYGIENE.md`
- `memory/guides/BUILD-METHOD.md`
- `tools/loop/loop.toml` (the `item.test.seen-red` row's actor, only where S7 re-points it)

### Alternatives rejected

- **A new hygiene check beside check 23.** Check 23 is corpus-wide and runs on every push; the owed
  set is one build's range from its base, which a corpus-wide check has no base for.
- **Keying a record by the suite path.** I2 keys every record by leg `name`, and two legs share a
  suite.

## 5. Production-readiness checklist

- security — no write path: the reader reads tracked records and `git show` blobs; the fixture writes
  only under the system temp directory.
- perf / scale — one `git ls-files`, one read per journal record of the build, two manifest parses.
- error / empty / loading states — an empty owed set is announced and exits 0; no base or an
  unreadable manifest exits 2 naming why; a malformed line exits 2 naming it.
- observability — one line per owed gate, with its record path.
- risks — a gate whose script changed but whose argv did not is owed only through a `New arm:` line,
  so a pass that rewrites a gate script and declares no arm is not caught (§8 F3).
- testing — AC1 to AC7 by fixture and probe; the arm in §7.
- migration — none, per §4.
- user docs — none owed: no page under `help/` describes the ledger; `memory/HYGIENE.md` is.

## 6. Acceptance criteria

- **AC1** — When `python seen_red.py --fixture --plant seen` runs in `tools/memory-tree/`, it exits 0
  and prints `seen-red: <leg> · <red sha8> · <record path>` for the planted leg.
  Red when: the reader does not parse S1's line, so the planted record reads `NO RECORD`.
- **AC2** — When `python seen_red.py --fixture --plant unseen-gate` runs, it exits 1 and prints the
  planted leg with `NO RECORD`, the clause's planted gate with no recorded red.
  Red when: the owed set misses an added manifest row, so the plant exits 0.
- **AC3** — When `python seen_red.py --fixture --plant unseen-arm` runs, it exits 1 naming the leg
  whose `argv` carries the `New arm:` line's suite path.
  Red when: `New arm:` lines are not read, so a moved arm owes nothing.
- **AC4** — When `python seen_red.py --fixture --plant empty` runs, it exits 0 and prints the
  `adds or changes no gate` line.
  Red when: an empty owed set prints nothing, which reads as a green join.
- **AC5** — When `python deviation_join.py --fixture --plant amended` runs in `tools/memory-tree/`,
  its output is byte-identical before and after S2, and the hygiene engine's check 23 over a fixture
  ledger whose `AC1` answer is followed by a seen-red line reports the answer's tokens without the
  seen-red line's.
  Red when: the extraction drops a ledger line, or check 23 joins the seen-red line's tokens to `AC1`.
- **AC6** — When `python seen_red.py --fixture --plant bad-line` runs, it exits 2 naming the record and
  the line.
  Red when: a malformed line is skipped, so a typo reads as a missing record or, worse, as none owed.
- **AC7** — When `grep -n 'seen-red' memory/guides/BUILD-METHOD.md memory/HYGIENE.md` and
  `grep -n 'seen-red' tools/memory-tree/kit.toml` run, M8 names the line and `seen_red.py`, the "Acceptance ledger" section states S1's grammar, and
  the kit descriptor holds the `seen-red` command row; `wc -c memory/guides/BUILD-METHOD.md` prints at
  most 30720.
  Red when: the grammar is stated in two places, or M8 outgrows its budget.

## 7. Gates

`memory-hygiene self-test` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `build-method size` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · each plant of §4 run through `seen_red.py --fixture`, staged red by deleting the owed-set half (a) and by dropping the seen-red flush from check 23's awk · none

## 8. Open questions

- **F1 — Where does `test.seen-red` run?** Options: (a) a command, `seen_red.py --build <slug>`, the
  item's actor and the close's read-back; (b) a hygiene check beside check 23; (c) a bar leg. (b) and
  (c) run over the whole corpus on every push with no build base, so either reds every landed build
  whose ledger predates the grammar. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the item's
  own shape in flow-steps' `test.seen-red` row ("command", reads and writes none). widens: none ·
  relaxes: none
- **F2 — Is the record kind a typed record file now?** Options: (a) the ledger line is the record, its
  grammar and reader in one module, and dScopedBuild's writer emits the same fields; (b) a `seen-red`
  kind in `tools/memory-tree/build_records.py` beside the ledger line, the reader reading both; (c) a
  typed file only. (c) departs from the clause's "recording both in the unit's acceptance ledger"; (b)
  writes one record's grammar twice before a second writer exists. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 1, the clause names the ledger as the record until dScopedBuild lands its
  writer. widens: none · relaxes: none
- **F3 — What makes a gate "changed"?** Options: (a) a manifest row whose `argv` moved, or a `New arm:`
  line on it; (b) any row field moved, the ceiling included; (c) (a) plus any file the leg's argv names
  changed in the range. (b) owes a red for a ceiling re-derivation that changes no verdict; (c) owes one
  for every edit to a shared script such as `run-gates.sh`, which most units touch. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the set the build method already owes arms for (M8 reads the
  `New arm:` lines); the departure from the clause's "one per gate a build adds or changes" is
  `2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71.md`. widens: none · relaxes: none
- **F4 — Which hash does the `**Carries:**` line pin?** Deviation `2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71` amends
  cl-dClosedLoop-0345's text, so the as-built view hashes it `72933671` where the baseline hashed `3265ae12`.
  RESOLVED (agent, 2026-10-25, delegated): rung 1, the line pins `cl-dClosedLoop-0345@72933671`, the view's hash,
  moved by deviation 71. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 7, the brief's shared interfaces I2 and
  I16 and owned-node table, scout A's row for cl-0345 and flow-steps' `test.seen-red` row, at base
  `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; the `**Carries:**` line re-pinned to `72933671`, deviation 71's amended text, with §8 F4; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.

## 10. Reuse audit

The seams extended: the `**Evidences:**` block walk inline at
`tools/memory-tree/deviation_join.py:608-623`, extracted into `tree_lib.py` at its second Python
instance; check 23's ledger awk at `tools/memory-tree/check-memory-hygiene.sh:3135-3160`; and M8's
arm-observation sentence at `memory/guides/BUILD-METHOD.md:280-282`. `python
tools/codebase-map/reuse_lookup.py "read the acceptance ledger lines that record a gate seen red"`
ranked generic `read` stems and `read_journal` (`tools/runlog/runlog_lib.py`), a journal-line reader
for the runlog grammar, not the ledger's markdown, so no seam reads a seen-red observation; the walk in
`deviation_join.py` was found by `git grep Evidences`. Scout A cited check 23 at `:3092-3335`, which
agrees with source; its parse loop is `:3135-3160` at `cdfbd1cf`.

Recall terms used: `python tools/memory-recall/query.py "how is a gate's staged red observation recorded in the acceptance ledger and read back" --terms "seen-red record acceptance ledger staged break arm red green New arm observe Evidences journal"`

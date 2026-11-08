# PLAY-dOrderedCharter-71 — the adopter-name ban reads only the roles an adopter receives

**Status:** CLOSED · rev-2 · 2026-11-08 · node d · Tier-2 · base 9f41230b5 · streams tooling · order 17 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 |
| [2026-11-08-build-PLAY-dOrderedCharter-71-ledger.md](../build/2026-11-08-build-PLAY-dOrderedCharter-71-ledger.md) | journal | — |
| [2026-11-08-prompt-PLAY-dOrderedCharter-71-1-spec-writer.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-71-1-spec-writer.md) | journal | — |
| [2026-11-08-prompt-PLAY-dOrderedCharter-71-build-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-71-build-brief.md) | journal | — |
| [2026-11-08-prompt-PLAY-dOrderedCharter-71-repair-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-71-repair-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`python tools/govkit/govkit.py selfcheck` reports no problem over this tree. Its adopter-name ban stops reading a
`project-owned` source as shipped, because gov supplies no bytes for that role, and it still reds on a shipped file
naming an adopter. The unit also renames the three helpers unit 70 added under undeclared verbs, so the lexicon's
verb-offender count returns to its pin.

## 2. Scope (IN)

Every line below was read at base `9f41230b5`. The Design section holds what a one-line item cannot.

- **S1** — The population of the adopter-name ban in `tools/govkit/govkit.py#selfcheck` keeps a survivor's source only
  when that row's role is in `tools/govkit/govkit.py#EPOCH_ROLES`, the declared set of roles whose bytes an adopter
  receives. A `project-owned` row, and a `forked` or `generated` one, no longer puts its source in the population. A
  source that another surviving row ships under a role in that set stays in it. Observed by AC1 and AC2.
- **S2** — The ban's comment states why the population reads that set, and its DOES NOT CHECK line names the two
  things it now leaves unread. The sentence saying an adopter receives a `project-owned` seed as surely as an engine
  is replaced. The header comment of `tools/govkit/adopters.toml` says the ban reads every file
  `govkit.py shipped --epoch` lists, where it says `govkit.py shipped`. Observed by AC3.
  **Readers:** by name: `tools/govkit/govkit.py` alone spells the sentence. by value: NO VALUE READERS — a comment
  carries no value any reader compares, counts or derives from.
- **S3** — One arm in `tools/govkit/selftest.py`, beside unit 70's source-rows arm in the `gcopy` block. A
  `project-owned` source carrying an adopter's name passes, and the same file under a shipping role reds. Observed by
  AC6.
- **S4** — The nested helper `fold` in `tools/memory-tree/merge-rows.py#resolve_tables` is renamed
  `derive_terminated`, at its definition and its three call sites. Observed by AC4 and AC5.
  **Readers:** by name: `tools/memory-tree/merge-rows.py` is the only tracked file outside the records that spells it.
  by value: NO VALUE READERS — a nested function's name is not read by any other module.
- **S5** — The nested helpers `split_known` and `warn_grown_file` in `tools/run-gates/owed_rows.py#run_selftest` are
  renamed `add_known_twin` and `add_warn_breach`, at each definition and its one row in the `cases` table. Observed by
  AC4 and AC7.
  **Readers:** by name: `tools/run-gates/owed_rows.py` is the only tracked file outside the records that spells
  either. by value: NO VALUE READERS — the case table holds the function object, and the arm label it prints is a
  separate string that does not change.

## 3. Non-goals (OUT)

- **The content of `tools/playbook/positional-refs.txt`.** It keeps every row, its adopter names included. S1
  changes which roles the ban reads, not what a gov-only list holds.
- **Widening `tools/govkit/govkit.py#check_source_rows`.** It keeps its `engine`-only narrowing, which its own
  docstring declares. Grading `seed`, `rendered` and `merged` sources for record rows is a separate question with no
  red asking for it.
- **The copy-install path.** A `cp -r` of a kit directory, as `WIRE-INTO-PROJECT.md` documents for several kits,
  reads no descriptor and carries a `project-owned` file too. That runbook's own `rm -f` steps own it. S2 states the
  gap, and the Design section records why no arm is built for it here.
- **A version bump.** No behaviour of a shipped kit moves. Unit 70 moved the same `merge-rows.py` at `0fb95eeac` with
  no version line change.
- **`.lexicon.conf`.** `VERB_OFFENDER_PIN` stays at 1209. The renames bring the count back to it.

### Edges

none

## 4. Design

### The red, and the contradiction under it

`tools/govkit/govkit.py#selfcheck`'s arm 10 builds `_shipped` from every row of
`tools/govkit/govkit.py#resolve_entry`'s `survivors` that carries a `src`, with no role test. Its comment justifies
that with "an adopter receives a `project-owned` seed as surely as an engine". The role's own entry in
`tools/govkit/govkit.py#UNLANDED_REASON` says "the target authors it — gov supplies no bytes for this source, ever",
and `tools/govkit/govkit.py#LANDABLE_ROLES` leaves it out, so `apply` never writes it. The sentence has stood since
`b050d5dfe`, where the role's definition already read the same.

Unit 70 withheld `tools/playbook/positional-refs.txt` as `project-owned`. That file names the adopter keyed `nc` 104
times and the adopter keyed `ic` 134 times, counted case-insensitively at base (PINNED). It is the only
`project-owned` source in any `kit.toml` under `tools/` that names an adopter, by a scan of each descriptor's
`project-owned` includes at base. So the two reds are this file, and no other withheld file is hidden behind them.

### One reading of a row's role

`resolve_entry` reports a role per row. A `project-owned` rule removes its sources from every EARLIER rule's rows, and
its own row stays in `survivors` under the role `project-owned`. A later rule naming the same source keeps its own row
and role. `writes` holds only `LANDABLE_ROLES` rows, last writer per destination.

`tools/govkit/govkit.py#check_source_rows` reads `writes` and keeps `engine` rows. `tools/govkit/govkit.py#cmd_shipped`
with `--epoch` keeps `survivors` rows whose role is in `EPOCH_ROLES`, and the constant's own comment declares it as
"the roles whose bytes an adopter RECEIVES from gov". That is the question the ban asks, so the ban reads it:

```python
    _shipped = sorted({row["src"] for eid, (d, _p) in descs.items()
                       for row in resolve_entry(root, d, canonical_ctx(eid))["survivors"]
                       if row.get("src") and row["role"] in EPOCH_ROLES})
```

The filter is per row, so a source a `project-owned` row names and a later `seed` or `engine` row also names stays in
the population. `check_source_rows`'s `engine` filter is a subset of the same set, so the two arms never disagree that
a `project-owned` source ships. `EPOCH_ROLES` is defined at module level below `selfcheck`, and `selfcheck` reads it at
call time, as `cmd_shipped` does.

The ban's population becomes the source column of `govkit.py shipped --epoch`, where it was the source column of
`govkit.py shipped`. The note line keeps its shape and its count drops by the sources only a non-receiving role names.

### The comment

The arm-10 comment keeps its first four sentences and its PURE BAN sentences. The population sentence becomes, in
substance: the population is `cmd_shipped --epoch`'s, the survivors whose role is in `EPOCH_ROLES`, because a
`project-owned`, `forked` or `generated` source is one gov supplies no bytes for. The DOES NOT CHECK line gains two
items: a source only a role outside `EPOCH_ROLES` names, and a `project-owned` file a `cp -r` copy install still
carries, which the runbook's `rm -f` steps own.

### The arm

In `tools/govkit/selftest.py#main`, directly after the `[dOC-70 S10]` check and its restore. It plants into
`tools/playbook/positional-producers.txt` in `gcopy`, a `project-owned` list of 17 lines at base that holds no adopter
name and no record row, so flipping its role trips the ban and nothing else.

```python
        # --- PLAY-dOrderedCharter-71 S3: the ban reads only the roles an adopter receives.
        import tomllib  # noqa: PLC0415
        _an = tomllib.loads((gcopy / PFX / KIT_NAMES["govkit"] / "adopters.toml").read_text(
            encoding="utf-8"))["adopter"][0]["names"][0]
        pf = gcopy / PFX / KIT_NAMES["playbook"] / "positional-producers.txt"
        pkt = gcopy / PFX / KIT_NAMES["playbook"] / "kit.toml"
        pfkeep, pktkeep = pf.read_bytes(), pkt.read_text(encoding="utf-8")
        pf.write_bytes(pfkeep + f"# {_an}\n".encode("utf-8"))
        _named = f"'{PFX}{KIT_NAMES['playbook']}/positional-producers.txt' names the adopter"
        rpo = _run_selfcheck(gcopy)
        check("[dOC-71 S3] a project-owned source naming an adopter passes the ban",
              rpo.returncode == 0 and _named not in rpo.stdout and "adopter names:" in rpo.stdout,
              (rpo.stdout + rpo.stderr)[-1500:])
        _pkt = pktkeep.replace('"positional-producers.txt", ', "", 1)
        check("[dOC-71 S3] LIVENESS the staged descriptor really ships the planted list",
              _pkt != pktkeep, "the replace matched nothing in the playbook-render descriptor")
        pkt.write_text(_pkt, encoding="utf-8")
        rsh = _run_selfcheck(gcopy)
        check("[dOC-71 S3] the same file under the engine role reds, naming the file and the adopter",
              rsh.returncode != 0 and f"{_named} `{_an}`" in rsh.stdout, (rsh.stdout + rsh.stderr)[-1500:])
        pf.write_bytes(pfkeep)
        pkt.write_text(pktkeep, encoding="utf-8")
```

The name is read from the copy's `adopters.toml`, never typed, as the ban's own comment requires of gov's code. With
the role flipped, the playbook-render descriptor's `**` engine rule ships the file. The first check's three conjuncts
are each load-bearing: without the rc a refused selfcheck passes, and without the note line an arm that never ran
passes. The plant is a `#` comment line, so `tools/playbook/positional.py` reads no new row from it.

The arm is RED at base by construction: the first check fails, because the ban reads the `project-owned` row today.
The main loop observes that red with S1 reverted and the arm kept, then GREEN with both.

### The renames

| File | Old | New | Sites |
|---|---|---|---|
| `tools/memory-tree/merge-rows.py` | `fold` | `derive_terminated` | the definition in `resolve_tables`, and the three calls on the line under it |
| `tools/run-gates/owed_rows.py` | `split_known` | `add_known_twin` | the definition, and the `two KNOWN copies that differ` row of `cases` |
| `tools/run-gates/owed_rows.py` | `warn_grown_file` | `add_warn_breach` | the definition, and the `a breach the warn mode admits` row of `cases` |

`add_known_twin` and `add_warn_breach` follow the case table's own siblings, `add_leg`, `add_bare_leg` and
`add_grown_file`. `fold`'s trailing comment, which cites unit 70's S6, stays on the definition.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_terminated`, `add_known_twin`, `add_warn_breach` | nested Python functions | `py.function`, each graded OK by `lexicon.py --suggest` at base |
| `[dOC-71 S3]` | selftest arm label prefix | none |

### Migration

N/A — no data shape moves, and the descriptor change that made the red landed in unit 70.

### Rollout

Live at landing. The `govkit selfcheck` leg turns green, and so does `govkit selftest`'s check that the gov copy is
green before any arm is provoked, which reads the same arm over a copy of this tree.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1, S2
- `tools/govkit/adopters.toml`: S2
- `tools/govkit/selftest.py`: S3
- `tools/memory-tree/merge-rows.py`: S4
- `tools/run-gates/owed_rows.py`: S5

### Alternatives rejected

- **A literal `row["role"] != "project-owned"` filter.** It answers the instance. `EPOCH_ROLES` already declares which
  roles an adopter receives, and a second spelling of that fact inside `selfcheck` could part from it. At base the
  two filters differ by one row: the `generated` rule of `tools/govkit/entries/check-agent-cap-restatement.kit.toml`,
  whose own note says gov's waiver file "must not travel". That file names no adopter at base, so neither filter
  reds on it, and only `EPOCH_ROLES` reads it correctly. No tracked descriptor declares a `forked` rule.
- **Reading `writes` as `check_source_rows` does.** `writes` holds only `LANDABLE_ROLES`, so the ban would stop
  reading `rendered` and `merged` sources, whose bytes an adopter does receive.
- **Keeping `project-owned` rows for kits with a `cp -r` install path.** No declaration says which kits have one, so
  the ban would need a new field. The playbook-render kit has no such path in `WIRE-INTO-PROJECT.md`, and no other
  `project-owned` source names an adopter at base.
- **Scrubbing `positional-refs.txt`.** Out of scope by the brief, and it would clear the instance while the
  contradiction stood.

## 5. Production-readiness checklist

- security: the ban narrows by role to the bytes gov sends. A file gov sends under any receiving role is still read.
- perf / scale: the population shrinks by the withheld sources. `positional-refs.txt`, 38,778 lines at base, is no
  longer read by the ban.
- error / empty / loading states: an `adopters.toml` declaring no names still refuses, unchanged.
- observability: the `adopter names:` note line still prints its counts.
- risks: a `project-owned` file that a `cp -r` install carries can name an adopter without a red. None does at base,
  and the comment states it.
- testing: the S3 arm, and AC1 to AC7 by a pass.
- migration: N/A — no data shape moves.
- user docs: N/A — no page under `help/` spells the ban or the three helpers, and nothing user-facing changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs over the tree, it exits 0, no line holds
  `names the adopter`, and the `adopter names:` note line prints.
  Red when: the ban still reads the `project-owned` row of `tools/playbook/positional-refs.txt`, as at base.
  permission: `selfcheck` is a leg's argv, so the main loop observes it.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs in a detached scratch worktree of the tip, with
  `"positional-refs.txt", ` deleted from the `project-owned` include of `tools/playbook/kit.toml`, it exits nonzero
  and names `tools/playbook/positional-refs.txt` with `names the adopter`.
  Red when: the filter drops a source a receiving role ships, so the ban stays silent over an engine file.
  permission: the same as AC1. cost: one scratch worktree.
- **AC3** — When `grep -n "surely as an engine" tools/govkit/govkit.py` runs, it prints nothing, and
  `grep -c 'row\["role"\] in EPOCH_ROLES' tools/govkit/govkit.py` prints `3`.
  Red when: the comment keeps the sentence, or the ban does not read the constant.
  figure: `2` at base is PINNED, the reads in `cmd_shipped` and `derive_epoch_state`.
- **AC4** — When `python tools/lexicon/lexicon.py --check` runs, it prints `lexicon OK`, with `VERB_OFFENDER_PIN` in
  `.lexicon.conf` still `1209`, and `python tools/lexicon/lexicon.py --offenders` prints no row whose identifier cell is
  `fold`, `split_known` or `warn_grown_file`.
  Red when: a new name leads with an undeclared verb, or the pin is moved instead of the names.
  figure: 1212 offenders over the pin of 1209 at base, PINNED from this writer's `--check` run.
- **AC5** — When `python tools/playbook/instructions_edit.py fixture --plant merge-unterminated` runs, it exits 0, and
  the same holds for `--plant merge-moved` and `--plant merge-written`.
  Red when: a call site keeps the old name, so the driver raises `NameError` on its first merge.
- **AC6** — When `grep -c "dOC-71 S3" tools/govkit/selftest.py` runs, it prints `3`, and the arm those labels name is
  observed RED with S1 reverted and GREEN with it, as the gates section declares.
  Red when: the arm is missing, or it passes with the ban still reading `project-owned` rows.
- **AC7** — When `python tools/run-gates/owed_rows.py --selftest` runs, it exits 0 and prints
  `arm ok    two KNOWN copies that differ` and `arm ok    a breach the warn mode admits`.
  Red when: a `cases` row keeps the old name, so `run_selftest` raises before its first case.

## 7. Gates

`govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit selfcheck` · `lexicon naming predicates` · `row-keyed merge driver replay` · `instruction edits selftest` · `run-gates canary`

The first five are what the guards join owes the Files-touched paths: the `{prefix}/govkit/` guard and the two
exact-path guards of `policy fixtures`. `{prefix}/`, `{prefix}/memory-tree/` and `{prefix}/run-gates/` are broad under
`BROAD_LEG_FLOOR` 5 and excluded. The other five run the code this unit moves: the ban, the lexicon count, the merge
driver, its plants, and `owed_rows.py --selftest`, which `run-gates.test.sh` runs.

New arm: tools/govkit/selftest.py · covers AC6 · a `project-owned` list planted with an adopter's name, then the same list flipped to the engine role · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-08 · initial draft, by `2026-11-08-prompt-PLAY-dOrderedCharter-71-repair-brief`, every line read at
  `9f41230b5`.
- rev-2 · 2026-11-08 · S2 · §4 · added the `**Derived:**` binding line its siblings carry, and the
  correction of `tools/govkit/adopters.toml`'s header comment to S2 and Files touched, the builder's finding.

## 10. Reuse audit

The seam is `tools/govkit/govkit.py#EPOCH_ROLES`, read today by `cmd_shipped --epoch` and `derive_epoch_state` and
declared as the roles whose bytes an adopter receives. S1 adds a third reader of that one fact, where a new role test
would have been a second copy of it. The arm extends the `gcopy` block of `tools/govkit/selftest.py#main` and its
`_run_selfcheck`, exactly as unit 70's source-rows arm does. The `reuse_lookup.py` query on the terms line ranked
generic `read_bytes`, `adopt` and `read_shipped_descriptors` symbols and no role set, so the constant was found by
reading `cmd_shipped`. The recall query returned TOOL-aRepatriatedFork-35, which drained the ban's carried sites and
left the population sentence as it stood, and no record that weighed the role question. The renames reuse the
declared verbs `derive` and `add`, which `lexicon.py --suggest` offered.

Recall terms used: `python tools/memory-recall/query.py "the adopter-name ban reads a project-owned source as shipped" --terms "adopter-name ban project-owned shipped survivors EPOCH_ROLES adopters.toml selfcheck arm 10 positional-refs"`, and `python tools/codebase-map/reuse_lookup.py "the roles whose bytes an adopter receives EPOCH_ROLES shipped survivors project-owned"`

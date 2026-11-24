# TOOL-dTotalRecall-58 — the census keep marker is honoured only under the tool root, so no pass writes it into a pinned instrument

**Status:** INPROGRESS · rev-3 · 2026-11-23 · node d · Tier-2 · base 462d20f3 · streams tooling · order 30 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-58-deviation-581.md](../build/2026-10-26-build-TOOL-dTotalRecall-58-deviation-581.md) | deviation | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-58-node-a-resume-brief.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-node-a-resume-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-58-node-a-resume-session.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-node-a-resume-session.md) | log | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-58-reground-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-58-reground-spec-writer.md) | log | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-58-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-58-build-brief.md) | journal | — |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-59 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 24 at HIGH**. It shares item **H1** with ids 4, 15 and 37, which
`TOOL-dTotalRecall-57`, `TOOL-dTotalRecall-56` and `TOOL-dTotalRecall-55` close. As planned,
`TOOL-dTotalRecall-53` S34 and S22 would have the pass write `# census: kept` into the files it keeps.
The packet pins `asbuilt.py` at `97c8f8fb`, `deviations.py` at `30a1f15b` and `packet.py` at `cab3bff1`,
the last repinned by the owner at `399ec42de`
(`memory/builds/dTotalRecall/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, its Pins list).
`memory/builds/dTotalRecall/README.md@69d8787a3:37-38` makes a moved instrument blob a stop, never
re-rendered away. Unit 53 landed at `6db81d070` with no marker in any build folder's script, and units
55 to 57 give such files a keep outside their bytes. Nothing yet stops a later pass from writing the
marker into one anyway. This unit makes the two censuses that read build folders refuse their marker
there, and observes that no instrument blob moved. It repairs `TOOL-dTotalRecall-53`.

## 2. Scope (IN)

- **S1** — The cause census refuses its marker in a build folder. `record_causes.py#check_cause_writers`
  reads the marker only in its tool-root walk at HEAD, through `record_causes.py#read_open_literals`.
  Its build-folder walk, over `record_causes.py#read_build_code_paths`' files, keeps a file only by its
  repository path. That walk now reds every line of each file that carries the `cause-writer` marker
  (`id_grammar.py#read_kept_reason`), before its keep test, so a file kept by `CAUSE_WRITER_KEPT`, by
  the path-keyed row unit 55 moves it to, or by a `CAUSE_WRITER_PINNED` row is red too. The finding
  names the file, the line and the remedy `the marker is the tool root's; a build folder's script is kept
  by its path-keyed row, since its bytes are not this build's`. Observed by AC1.
- **S2** — The instruments' bytes held. No dTotalRecall commit since base `462d20f3` changes a tracked
  code file under `memory/builds/*/build/`, and `packet.py --check dTotalRecall` exits 0, so S34, S22,
  units 55 to 57 and this pass moved no instrument blob. At HEAD no dTotalRecall commit has (DERIVED
  2026-11-23, AC2's `git log`), and each pinned instrument's blob equals its pin (DERIVED 2026-11-23,
  `git hash-object` over the `instrument:` paths of the Pins list). Observed by AC2.
- **S3** — The alias census refuses its marker in a build folder. `record_kinds.py#check_alias_compares`
  reads the marker only in its tool-root walk at HEAD. Its build-folder walk, each tracked
  `<memory root>/builds/*/build/*.py`, keeps a hit only by `ALIAS_COMPARE_KEPT`, or by unit 56's row
  after it. That walk now reds every line of each script carrying the `alias-compare` marker, before
  its keep test, with S1's finding and remedy. Observed by AC3.
- **S4** — The bound holds at HEAD. `read_kept_reason` has three callers (DERIVED 2026-11-23,
  `git grep -n "read_kept_reason(" -- tools`): `id_grammar.py#scan_readers`,
  `record_causes.py#read_open_literals` and `record_kinds.py#check_alias_compares`. The alias and cause
  censuses call it on tool-root files alone. No tracked code file under `memory/builds/*/build/`
  carries a marker (DERIVED 2026-11-23, AC4's `git grep`), so S1 and S3 red nothing on the real tree.
  Observed by AC4.

## 3. Non-goals (OUT)

- The keep table and its rows: units 55, 56 and 57.
- The marker's grammar and its reader, `id_grammar.py#read_kept_reason`: `TOOL-dTotalRecall-53` S34's,
  which this unit calls and leaves as it is.
- The slug census's marker. `id_grammar.py#scan_readers` reads the tool root, `skills/` and
  `.githooks/`, and no build folder. Two of its kept lines sit outside the tool root (DERIVED
  2026-11-23, `git grep -lE "(#|//) census: kept (slug-grammar|alias-compare|cause-writer) " -- .githooks skills`):
  in `.githooks/pre-push.runlog.test.sh` and `skills/session-kickoff/manifest-check.sh`. Both stay
  honoured; `TOOL-dTotalRecall-66` S15 states that census's domain.
- Moving a pin: only the owner's `packet.py --repin` does.

### Edges

- **consumes-from** `TOOL-dTotalRecall-53` — S34's marker reader and S22's widened alias population,
  whose marker this unit bounds to the tool root
- **hands-off** `TOOL-dTotalRecall-66` — the marker's domain and AC2, which that unit sets per census, tests against the derived tool root and reads over this run's own commits (the round-1 audit of units 54 to 60, ids 12, 15, 18, 28 and 43)

## 4. Design

### The rule

The bound lives in the walks, never in the reader. `read_kept_reason(line, census)` reads line text
and takes no path, and its slug caller honours markers outside the tool root on purpose (§3). Each of
the two censuses already walks the build folders apart from the tool root. So each build-folder walk
calls one new function, `check_marker_domain(path, text, census)` in `id_grammar.py`, on each whole
file, binding head included, before the walk skips a file with no hit and before its keep test. It
returns one red finding per line of `text` that `read_kept_reason` reads for
`census`, naming `path`, the line and S1's remedy. The census lists each as
`<census> · <path>:<n> · red · marker in a build folder`. A keep by row never clears that finding.

A flat install, whose tool root is the repository root, puts the build folders in the tool-root walk
too, where the marker reads as a keep. The build-folder walk still reds it, so the census exits 1.

### What it does not check

- A marker no census would honour there: a `slug-grammar` marker in any build-folder file, or an
  `alias-compare` marker in a build folder's `*.sh` or `*.js`, which the alias census does not read.
  Such bytes move no keep, and AC2 catches them in a pinned instrument.
- Whether a marker's lead opens a comment, as `read_kept_reason` states of itself.

### Inventory

Minted: `check_marker_domain` in `tools/memory-tree/id_grammar.py`; the fixture plant
`marker-in-build-script` in `record_causes.py --fixture`; the fixture plant `marker-in-kept-script` in
`record_kinds.py --fixture`. Naming cell: `check_marker_domain` leads with the VERBS table's `check`,
asked of `python tools/lexicon/lexicon.py --suggest check_marker_domain --as py.function` at the pass.
A plant name has no cell.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py`
- `memory/map/generated/` (the codebase map's render, re-rendered by its `--write` at the pass)

`TOOL-dTotalRecall-55`, `-56` and `-57` also write these modules at order 30, so BUILD-METHOD M6
sequences the passes.

### Alternatives rejected

- **Give `read_kept_reason` a path and refuse a marker outside the tool root.** Its slug caller reads
  `skills/` and `.githooks/`, whose two kept lines would red. Setting the domain per census is
  `TOOL-dTotalRecall-66` S15's.
- **Read the pinned paths from `packet.py`'s `INSTRUMENTS` and refuse a marker only there.** The
  unpinned build-folder scripts are outside this build's write set too
  (`memory/builds/dTotalRecall/README.md@69d8787a3:49`), so the folder is the narrower rule.
- **Observe the bytes only, with no refusal.** A marker written into an unpinned script in another
  build's folder moves no pin and `packet.py --check` stays green, so only the refusal catches it.

## 5. Production-readiness checklist

- security — narrows a keep: a build folder's script can no longer exempt itself in its own bytes.
- perf / scale — one marker read per line of each build-folder code file, which both walks already read.
- error / empty / loading states — a marker in a build folder is a red finding naming the line.
- observability — the finding prints the file, line and remedy.
- risks — none beyond S1 and S3: no build-folder file carries a marker at HEAD (S4), so no keep is lost.
- testing — AC1 to AC4 by the pass; the arms of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --fixture --plant marker-in-build-script` runs from
  `tools/memory-tree/`, it writes the fixture's pinned instrument (`PINNED_INSTRUMENT`, its ask filed)
  with `# census: kept cause-writer pinned instrument` on its Serves literal's line. Its `--check` under
  `FIXTURE_PINNED` exits 1 with one red naming that file and line, and the fixture prints PASS and
  exits 0. Red when: the marker in a build-folder script is honoured, or the row keeps the line.
- **AC2** — When `git log --no-merges --format=%s 462d20f3..HEAD -- 'memory/builds/*/build/*.py'
  'memory/builds/*/build/*.sh' 'memory/builds/*/build/*.js' | grep -c dTotalRecall` runs at the pass
  tip it prints 0, and `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --check dTotalRecall`
  exits 0. Red when: a dTotalRecall commit wrote into a build-folder script, or an instrument blob moved.
- **AC3** — When `python record_kinds.py --fixture --plant marker-in-kept-script` runs from
  `tools/memory-tree/`, it plants a raw alias compare carrying `# census: kept alias-compare x` past the
  binding head of a script at the path the alias census keeps by row. Its `--check` exits 1 naming that
  path and line, and the fixture exits 0. Red when: the row or the marker keeps the line.
- **AC4** — When `git grep -c "census: kept" -- 'memory/builds/*/build/*.py' 'memory/builds/*/build/*.sh'
  'memory/builds/*/build/*.js'` runs at the pass tip it prints nothing, and `git grep -n
  "read_kept_reason(" -- tools` lists the definition and the three callers S4 names.
  Red when: a build-folder script carries a marker, or a fourth caller reads one.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/record_causes.py · covers AC1 · the plant `marker-in-build-script`, staged by skipping `check_marker_domain` · none
New arm: tools/memory-tree/record_kinds.py · covers AC3 · the plant `marker-in-kept-script`, staged by skipping `check_marker_domain` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 24
  (HIGH, item H1 shared with ids 4, 15 and 37).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-3 · 2026-11-23 · §1 S1-S4 §3 §4 §5 AC1-AC4 §7 §10 · re-grounded over HEAD per
  `2026-11-23-prompt-TOOL-dTotalRecall-58-reground-brief`: unit 53 built `read_kept_reason` line-only,
  called in the two censuses' tool-root walks alone, so the bound moves into each build-folder walk
  (S1, S3, `check_marker_domain`); the slug census reads `skills/` and `.githooks/`, so §3 corrects its
  non-goal; `packet.py` is pinned at `cab3bff1`; AC2 reads dTotalRecall's commits, since other builds
  moved build-folder scripts after base; AC1 names the census `cause-writer`; S4 and AC4 observe HEAD;
  `tree_lib.py` leaves Files touched.

## 10. Reuse audit

The seams extended are the marker reader `tools/memory-tree/id_grammar.py#read_kept_reason`, the one
place the three censuses test a keep marker, beside which `check_marker_domain` sits; the build-folder
walks of `record_causes.py#check_cause_writers` and `record_kinds.py#check_alias_compares`; and the
fixtures' plant tables, `record_causes.py#PINNED_PLANTS` and `record_kinds.py#ALIAS_PLANTS`. The
observation reuses the packet instrument's own `--check`
(`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py#INSTRUMENTS` lists
what it pins). `python tools/codebase-map/reuse_lookup.py "refuse a census keep marker in a build folder script"`
ranked name-stem neighbours and no path bound on a keep marker, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`

# TOOL-aTrimmedWait-11 — close repair, inherited: the hygiene suite's partition arm sets aside check 26's cache-hit count

**Status:** INPROGRESS · rev-4 · 2026-11-15 · node a · Tier-2 · base 846d51d3 · streams tooling · order 10 · ratified 2026-11-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aTrimmedWait-11-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aTrimmedWait-11-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-11-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-11-2-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-2-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-11-3-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-3-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-11-4-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-4-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-11-promotion.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-promotion.md) | research | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-11-revision-2.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-revision-2.md) | research | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-11-revision-3.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-revision-3.md) | research | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-11-revision.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-revision.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The partition arm of `tools/memory-tree/check-memory-hygiene.test.sh` reads RED on every fresh
clone and GREEN in a tree whose check 26 cache is warm. After this unit it reads one verdict in both,
because what only the cache's state moves, the cache-hit count and the `cache recomputed` lines, is
set aside on both sides of its compare. No other verdict moves.

## 2. Scope (IN)

- **S1** — One function in the suite, `derive_partition_lines`, defined on one line just above the
  partition arm. It turns a text into the line set the arm compares, as the arm's pipeline does
  today, but on check 26's liveness line it writes the count after `cache hits ` as `<n>`, and it
  sets aside every check 26 `cache recomputed` line in the compare, so neither side's set holds
  one. Check 26 still prints them. Observed by AC1, AC2.
- **S2** — The partition arm's compare and its `diff` read both sides through
  `derive_partition_lines`, and no longer through the inline pipeline. Observed by AC3, AC6.
- **S3** — A fixture arm right after the partition arm. It renders three check 26 liveness lines
  through the producer's own `render_liveness` and one `cache recomputed` line through its
  `print_recomputed`, then asserts that the two liveness lines differing only in the cache-hit count
  compare equal, that a pair differing in another field compares unequal, that a pair outside
  check 26 differing only in that count compares unequal, and that a set carrying the recompute line
  compares equal to the same set without it. Observed by AC4.
- **S4** — `FLOOR_ASSERTIONS` rises by the fixture arm's four assertions, with a raise-log comment
  line in the form the floor's existing log uses. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `tools/memory-tree/transition_audit.py`, to check 26's output, or to the engine
  `tools/memory-tree/check-memory-hygiene.sh`.
- No other arm of the suite moves, the partition arm's list of scoped selections included.
- No change to the unattended suite's own partition arm (`tools/unattended/check-unattended.test.sh`,
  the `same "the scoped runs partition the unscoped run's lines"` row). It runs no check 26.
- No cache isolation for the suite, such as pointing check 26 at a fixture repository. The module
  resolves its root from its own file (§4 "Evidence"), and moving that is an engine change.
- No set-aside of any other check 26 line or field: only the liveness line's cache-hit count and the
  `cache recomputed` lines, the latter by F1, resolved for (B) by the owner on 2026-11-15.
- No kit version move. The build README moves kit versions once, after the last code move.

### Edges

none

## 4. Design

### Evidence

- Check 26 resolves its root from its own file, not from the working directory:
  `resolve_root` walks `KIT.parents` for `.memory-tree.conf`
  (`tools/memory-tree/transition_audit.py@419c2700999d:92-105`). The suite's main block runs the
  engine in a fixture repository under `$TMP` (`tools/memory-tree/check-memory-hygiene.test.sh@0c6a20682257:274`,
  `:1204`), so its check 26 lines audit the repository that holds the kit.
- The cache sits under that repository's git common dir, `transition-audit-cache`
  (`tools/memory-tree/transition_audit.py@419c2700999d:628-633`). A merge whose entry is absent
  recomputes with an empty reason and is not counted as recomputed (`:672-674`, `:777-782`). A hit
  adds one to `hits` (`:783-785`).
- The liveness line is rendered by `render_liveness`
  (`tools/memory-tree/transition_audit.py@419c2700999d:796-805`): the `SAY` prefix
  `memory-hygiene: check 26 ` (`:66`), then `transitions examined`, `merges walked`, `pinned`,
  `unpinned` and `cache hits`, each with its count, and the optional tail
  ` · reader cross-check not run`. A reason other than empty prints one
  `cache recomputed <count> (<reason>)` line per reason, through `print_recomputed` (`:815-817`), and
  an entry written under other declared inputs gives the reason `foreign inputs` (`:683-684`).
- The partition arm collects the scoped runs' lines, liveness lines set aside, and compares both
  sides as `printf '%s\n' <text> | grep . | sort -u`, then prints a `diff` of the same pipelines
  (`tools/memory-tree/check-memory-hygiene.test.sh@0c6a20682257:1392-1398`). The unscoped run goes
  first (`:1204`), and `run_scoped 26` runs inside the loop (`:1393`).
- Observed 2026-11-15 on node a, in a `git clone --no-local` of `1a8dd930d` with no cache dir:
  `bash tools/memory-tree/check-memory-hygiene.sh --only 26` printed
  `memory-hygiene: check 26 transitions examined 4 · merges walked 690 · pinned 0 · unpinned 4 · cache hits 0`,
  and a second run printed the same line ending `cache hits 4`. Both exited 0 in 10 s.
- `tools/` is byte-identical between `ff4242f8b` and `1a8dd930d`, and this build moved neither
  `transition_audit.py` nor lines 1392-1398 of the suite since `846d51d39`. The arm came in with
  `TOOL-aSparedSpawn-7` (`11a69b8bc`) and the field with `TOOL-dDerivedDocket-9` (`d267a9c22`), both
  ancestors of `846d51d39`.

### The function

One line, placed just above the `_hs_union=""` line of the partition arm:

```bash
derive_partition_lines() { printf '%s\n' "$1" | grep . | sed -E -e '/^memory-hygiene: check 26 cache recomputed /d' -e 's/^(memory-hygiene: check 26 transitions examined .* cache hits )[0-9]+/\1<n>/' | sort -u; }
```

The first expression deletes a line opening with the `SAY` prefix and `cache recomputed `, so only
check 26's recompute lines go, whatever their count and reason. A line of any other check that
carries those words is kept. The second expression is the count mask. Its pattern is anchored on
the `SAY` prefix and the first field's name, so only check 26's liveness
line matches. It replaces only the digit run after `cache hits `, so every other count and the
optional tail are still compared byte for byte. A line of any other check that carries the words
`cache hits` is untouched. The `sed` sits after `grep .`, never straight after the `printf`, so the
pipeline adds no `var-pipe` site (`tools/gate-lint/sh_hygiene.py@448d62cbd57b:643-647` reads only a
`printf` of one expansion piped straight into the stage). A call to it is no `pure-fn-subst` site,
because its body is a pipeline (`:718-732`). Both were checked on 2026-11-15 by running
`scan_spawn_file` over the planned rev-2 lines, this function and the fourth assertion's compare
included: every match it returned carried `False` as its site flag.

### The partition arm

Lines 1397-1398 become:

```bash
n=$((n+1)); [ "$(derive_partition_lines "$_hs_union")" = "$(derive_partition_lines "$out")" ] \
  || { echo "FAIL the scoped runs do not partition the unscoped run's lines:"; diff <(derive_partition_lines "$out") <(derive_partition_lines "$_hs_union") | head -20; st=1; }
```

A comment line above it names this unit and says that the cache-hit count and the `cache recomputed`
lines are what the cache's state moves. The `diff` reads the same sets the compare reads, so a red prints the lines that
actually differ.

### The fixture arm

Right after the partition arm's liveness-line assertion, before `# ---- check 22`:

```bash
mapfile -t _hs_c26 < <("$_PY" -I -c 'import sys; sys.path.insert(0, sys.argv[1]); import transition_audit as t
r = lambda m, h: t.render_liveness({"registry": [], "transitions": ["a"] * 4, "merges": m, "hits": h}, True)
print(r(9, 0)); print(r(9, 4)); print(r(8, 4)); t.print_recomputed({"recomputed": {"foreign inputs": 1}})' "$HERE")
_hs_cr=$'\r'; _hs_c26=("${_hs_c26[@]%"$_hs_cr"}")
```

The trailing carriage return is stripped, as `resolve_python`'s probe strips it from a Windows
python's output. The pattern is held in `_hs_cr` because the array expansion's `%$'\r'` leaves the
carriage return in place on this node's bash 5.3 (Cygwin), run from a script file, observed
2026-11-15. Four assertions, each `n=$((n+1))` with its own FAIL line:

| Assertion | Compares | Wants |
|---|---|---|
| cold equals warm | `"${_hs_c26[0]-}"` (hits 0) with `"${_hs_c26[1]-}"` (hits 4) | equal |
| another field still counts | `"${_hs_c26[0]-}"` with `"${_hs_c26[2]-}"` (merges walked 8, hits 4) | unequal |
| only check 26's line | `"${_hs_c26[0]+${_hs_c26[0]/check 26/check 12}}"` with `"${_hs_c26[1]+${_hs_c26[1]/check 26/check 12}}"` | unequal |
| a recompute line is set aside | `"${_hs_c26[0]-}"$'\n'"${_hs_c26[3]-}"` (the `cache recomputed 1 (foreign inputs)` line) with `"${_hs_c26[0]-}"` | `"${_hs_c26[3]-}"` non-empty, and equal |

Each side goes through `derive_partition_lines`. The lines come from the producer, so a rename of
the field or the prefix in `render_liveness` reds the first assertion, and a rename in
`print_recomputed` reds the fourth, rather than leaving a `sed` expression to stop matching while
the arm stays green.

The suite runs under `set -u` (`tools/memory-tree/check-memory-hygiene.test.sh@0c6a20682257:14`),
where a read of an unset element ends the whole suite with `unbound variable`: on this node's
bash 5.3.9 (Cygwin), run from a script file, `"${a[0]}"` and `"${a[0]/check 26/check 12}"` over an
empty `a` each printed `a[0]: unbound variable` and exited 1, observed 2026-11-15. So every read of
an `_hs_c26` element takes an unset-safe form, and an unset element reads as empty: the default
form `"${_hs_c26[N]-}"`, and in the third assertion
`"${_hs_c26[N]+${_hs_c26[N]/check 26/check 12}}"`. Bash takes no `-` default and a `/` substitution
in one expansion, and the `+` form expands its word only for a set element, so the substitution
never reads an unset one. That form over an empty `a` printed an empty line and the script ran on,
observed the same day. An empty render then compares equal in the first assertion and reds the
other three, the fourth by its non-empty test. A short render leaves at least `_hs_c26[3]` unset,
so it reds the fourth. Either way the suite runs on to its next arm, and the arm cannot pass over
nothing.

### What it does not check

- The `cache recomputed` lines' counts and reasons. Both sides drop them (F1, resolved for (B)), so
  a recompute that only one side prints goes unseen by this arm. Those lines are graded by
  `tools/memory-tree/transition-audit.test.sh`'s AC9 arms: `cache recomputed 1 (foreign epoch)`
  (`tools/memory-tree/transition-audit.test.sh@6b5b736bf980:210`) and
  `cache recomputed 1 (foreign inputs)` (`:240`).
- Whether the cache-hit count is right. That is `tools/memory-tree/transition-audit.test.sh`'s AC9
  arms (`cache hits 1` on a second run, `cache hits 0` on a foreign epoch).
- The two `sed` expressions spell the producer's formats a second time. The fixture arm is the gate
  that compares them, so it holds only while the arm renders through `render_liveness` and
  `print_recomputed`.

### Inventory

| Minted | Kind | Graded by |
|---|---|---|
| `derive_partition_lines` | suite shell function | cell `sh.function`: `python tools/lexicon/lexicon.py --suggest derive_partition_lines --as sh.function` answered OK, exit 0, on 2026-11-15 |
| `_hs_c26` | suite shell array | none: the lexicon declares no shell variable cell |
| `_hs_cr` | suite shell variable, the carriage-return pattern | none: the lexicon declares no shell variable cell |

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/map/generated/`, the codebase map, re-rendered by the codebase map kit's
  `gen_map.py --write` for the new function: its `symbols.json` lists the suite's shell functions.
- `memory/builds/aTrimmedWait/build/`, for the unit's acceptance ledger, named as its siblings'
  ledgers are.
- `memory/builds/aTrimmedWait/README.md`, `memory/LIVE.md` and
  `memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md`: the generated index
  files check 9 asks for, re-rendered by the memory-tree kit's `gen_build_index.py --write`. They
  are the three that `TOOL-aTrimmedWait-9`'s builder commit `057f26ba4` moved beside its ledger:
  the build index region, the live-builds row, and the spec's status header and records region.

### Alternatives rejected

- **Drop check 26's line from both sides with `grep -v`, in the shape of the liveness-line
  exclusion.** Every other field of that line would go unread, and item 1 keeps them.
- **Run the unscoped check 26 twice first, so both sides read warm.** It costs a 10 s run on every
  suite pass and still fails where an entry of another epoch is rewritten between the runs.
- **Spell the three fixture lines as literals.** A format change in `render_liveness` would then
  leave the fixture green while the `sed` stopped matching.
- **Inline the `sed` in each of the four pipelines.** The rule would be written four times, and the
  fixture arm could not call the one the partition arm uses.

## 5. Production-readiness checklist

- security — N/A — a test-only change. No write path, no new input.
- perf / scale — One python spawn and eight function calls, about four forks each, for the fixture
  arm, and one more `sed` per side for the partition arm. The suite's worst reading is 808 s against
  its 1220 s row in `tools/run-gates/selftest-budgets.txt` <!-- PINNED 2026-11-15 -->.
- error / empty / loading states — The suite runs under `set -u`, so every read of an `_hs_c26`
  element takes an unset-safe form and an unset element reads as empty, rather than ending the
  suite with `unbound variable`. An empty render reds three of the fixture's four assertions, a
  short render the fourth at least, and the suite runs on, §4 "The fixture arm".
- observability — The partition arm's `diff` prints the normalized sets, so a red names only lines
  that really differ.
- risks — F1 is resolved for (B): a cache entry left under other declarations prints a
  `cache recomputed` line both sides now drop. What remains is §4 "What it does not check": a
  recompute only one side prints goes unseen by this arm.
- testing — AC1 and AC2 are probes of the function. AC3 to AC5 are greps and a diff. AC6 is two
  engine runs in a fresh clone. The main loop observes both arms RED then GREEN at the close.
- migration — N/A — no data or declaration moves.
- user docs — N/A — no user-facing surface moves.

## 6. Acceptance criteria

`<def>` is `eval "$(grep '^derive_partition_lines() { ' tools/memory-tree/check-memory-hygiene.test.sh)"`,
run in a bash in this worktree. In that bash, `L` holds the line
`memory-hygiene: check 26 transitions examined 4 · merges walked 9 · pinned 0 · unpinned 4 · cache hits 0`,
which `render_liveness` prints for four unpinned transitions, nine merges and no hit, observed
2026-11-15, and `L4` holds `${L%0}4`. `R` holds
`memory-hygiene: check 26 cache recomputed 1 (foreign inputs)`, which `print_recomputed` prints for
one foreign-inputs entry, observed 2026-11-15.

- **AC1** — When `<def>` runs, `grep -c '^derive_partition_lines() { '` over the suite prints 1, and
  `derive_partition_lines "$L"` and `derive_partition_lines "$L4"` print the same bytes, one line
  ending `cache hits <n>`. `derive_partition_lines "$L"$'\n'"$R"` prints the same bytes as
  `derive_partition_lines "$L"`.
  Red when: the set-aside is missing, as at `ff4242f8b`, so a pair prints different bytes.
- **AC2** — When `<def>` runs, `derive_partition_lines` prints different bytes for `"$L"` and for
  `"${L4/merges walked 9/merges walked 8}"`. It prints different bytes for `"$L"` and for
  `"$L · reader cross-check not run"`. It prints different bytes for `"${L/check 26/check 12}"` and
  `"${L4/check 26/check 12}"`. It prints different bytes for `"$L"$'\n'"${R/check 26/check 12}"`
  and `"$L"`.
  Red when: the function sets aside more than the count and check 26's recompute lines, such as the
  whole line, the tail, or the count or a recompute line outside check 26.
- **AC3** — When `grep -c 'derive_partition_lines "$out"' tools/memory-tree/check-memory-hygiene.test.sh`
  runs, it prints 2, and the same grep for `derive_partition_lines "$_hs_union"` prints 2: the
  compare's line and the `diff`'s line each read both sides through the function.
  `grep -c '"$_hs_union" | grep . | sort -u'` over the suite prints 0.
  Red when: a side of the compare or of the `diff` still reads the inline pipeline.
- **AC4** — When `grep -c 'render_liveness' tools/memory-tree/check-memory-hygiene.test.sh` runs, it
  prints 1, the same count for `print_recomputed` prints 1, and
  `grep -n '_hs_c26' tools/memory-tree/check-memory-hygiene.test.sh` prints the four assertions of
  §4 "The fixture arm" after the partition arm's line. `grep '^FLOOR_ASSERTIONS='` over the suite
  prints `FLOOR_ASSERTIONS=749`.
  Red when: the arm is absent, renders its lines as literals, or the floor was not raised.
  figure: 749 is PINNED, the 745 of `ff4242f8b` plus the arm's four.
- **AC5** — When `git diff --stat ff4242f8b -- tools/` runs after the builder's commit, it names one
  file, the hygiene suite this unit edits. `git diff ff4242f8b -- tools/memory-tree/check-memory-hygiene.test.sh`
  shows removed lines only at the partition arm's compare and `diff`, and at `FLOOR_ASSERTIONS`.
  Red when: the fix moved the engine, the module, or another arm.
- **AC6** — When, in a fresh `git clone --no-local` of the builder's commit with no
  `transition-audit-cache` under its git dir, `bash tools/memory-tree/check-memory-hygiene.sh --only 26`
  runs twice, the two outputs, each with its `HYGIENE --only ` line removed, differ as raw text and
  print the same bytes through `derive_partition_lines`.
  Red when: the set-aside does not cover the line the cold and the warm run print, which is the
  partition arm's red on a fresh clone.
  cost: about 75 s for the clone and 10 s per run on node a, measured 2026-11-15.
  fixture: the clone is made for the observation, and the tree holds none today.

## 7. Gates

`memory-hygiene self-test` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

The suite is the one this unit edits. The two shell hygiene legs grade the new pipeline and the
`mapfile` read, and the lexicon leg grades the new function's name. The two recall floor legs guard
`memory/`, where the map, the ledger and the index files under "Files touched" sit. The main loop
runs the merge bar once, at the close. No leg is added.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC3 AC6 · the partition arm, moved: RED at `ff4242f8b` on a fresh clone, where the unscoped run reads `cache hits 0` and the scoped run `cache hits 4`, GREEN on a fresh clone of the builder's commit · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC4 · the fixture arm after the partition arm: RED with `derive_partition_lines` reduced to `printf '%s\n' "$1" | grep . | sort -u`, the pipeline at `ff4242f8b`, where the cold and warm lines compare unequal and the recompute line is kept · `FLOOR_ASSERTIONS` 745 to 749

## 8. Open questions

- **F1 — Does the partition arm also set aside check 26's `cache recomputed` lines?**
  The goal asks for one verdict on a cold clone and on a warm tree. A tree warmed by a worktree
  whose declarations differ holds entries the unscoped run recomputes and reports as
  `cache recomputed <count> (foreign inputs)`, and the scoped run, reading the rewritten entries,
  prints no such line. Item 1 of the brief keeps every line but the count byte for byte.
  - (A) Keep item 1 as written. The partition arm reds in such a tree until its next run, and the
    residual is stated in §4 "What it does not check".
  - (B) Also drop every line opening `memory-hygiene: check 26 cache recomputed ` on both sides,
    one more `sed` expression in `derive_partition_lines`, and add a fourth fixture assertion: a
    set carrying such a line compares equal to one without it. The floor then rises by four, to 749.
  Recommendation: (B). Both fields are run-order artifacts of the same cache, the partition is
  about which lines a check prints and not about cache state, and the recompute reasons are
  already graded by `tools/memory-tree/transition-audit.test.sh`. It widens item 1, so it is the
  owner's call.
  RESOLVED (owner, 2026-11-15): (B), check 26's `cache recomputed` lines set aside on both sides
  too, with the fourth fixture assertion and the floor at 749.

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.
- rev-2 · 2026-11-15 · §1 · §2 · §3 · §4 · §5 · AC1 · AC2 · AC4 · §7 · §8 · F1 resolved by the owner for (B): check 26's `cache recomputed` lines set aside on both sides, a fourth fixture assertion, the floor 745 to 749.
- rev-3 · 2026-11-15 · S1 · §4 · S1 says the `cache recomputed` lines are set aside in the compare, which the pre-commit memory hygiene had read as a retirement. The fixture arm strips the carriage return through `_hs_cr`, since the array expansion's `%$'\r'` leaves it on this node's bash.
- rev-4 · 2026-11-15 · §4 · §5 · §7 · the fixture arm's element reads take unset-safe forms, since the suite's `set -u` ended the suite on an unset read, the builder's DIVERGENCE of run `wf_0b836e97-5c0` ruled by the owner (2026-11-15-prompt-TOOL-aTrimmedWait-11-revision-3). "Files touched" adds the codebase map, the acceptance ledger and check 9's index files, and §7 names `recall floor` and `recall floor arms`, whose `memory/` guard those paths trip.

## 10. Reuse audit

No existing seam fits. The seam this unit extends is the partition arm itself, whose pipeline
becomes `derive_partition_lines`, and `render_liveness` in `tools/memory-tree/transition_audit.py`,
which the fixture arm calls rather than restating its format. `tools/codebase-map/reuse_lookup.py`
for the query below ranked name-stem matches only (`run`, `before`, `counts`, `field`, `run_git`),
none of which normalizes a line set. The unattended suite's partition arm compares its pipeline raw,
with no normalizer to share. The brief's reuse pointer, the liveness-line exclusion
`grep -v '^HYGIENE --only '`, gave the shape: one filter stage over both sides. The build's reuse
list (`verb_dispatch`, `run_spec_token_check`, check 12's `--only`, `load_session_calls` and the
rest) reads no suite's line set.

Recall terms used: `python tools/codebase-map/reuse_lookup.py "normalise a volatile counter field before comparing two hygiene run outputs as line sets in a shell suite"`

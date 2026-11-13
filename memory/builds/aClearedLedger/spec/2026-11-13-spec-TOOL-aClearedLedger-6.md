# TOOL-aClearedLedger-6 — the hygiene self-test's eight lines: the partition arm folds check 26's cache figure, the override derivation leaves the carried resolver block out, and the conf example declares six recall keys

**Status:** SPECCED · rev-1 · 2026-11-13 · node a · Tier-1 · base 8db6f4be · streams tooling · order 6 · closes TOOL-aNimbleMend-19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |

<!-- /gen:spec-records -->

## 1. Goal

The hygiene self-test prints eight failure lines on a frozen clone, from three causes, so it never
prints its assertion total. This unit fixes each at its cause: one arm compared a figure that
depends on run order, one derivation read a carried block that reads no conf, and one shipped file
fell behind a module that moved into the kit.

## 2. Scope (IN)

- **S1** — The partition arm of `tools/memory-tree/check-memory-hygiene.test.sh` compares both
  sides through one helper, `_hs_lines`, which folds the digits after `cache hits ` to a constant.
  Every other byte of a line still decides the comparison. Observed by AC1 and AC6.
- **S2** — The suite derives the engine's override reads through one helper, `_engreads_of`, which
  leaves out the block between the `# >>> resolve_python` and `# <<< resolve_python` marker lines.
  `_engexempt` loses `GOV_PYTHON` and keeps `MAP_ROOT`. Observed by AC2 and AC6.
- **S3** — Three assertions are added: the engine carries each marker line exactly once, a read
  staged inside a marker block is not derived, and reads staged before and after it are.
  `FLOOR_ASSERTIONS` moves 707 to 708. Observed by AC2 and AC6.
- **S4** — `tools/memory-tree/.memory-tree.conf.example` declares the six `RECALL_` keys
  `tools/memory-tree/id_grammar.py` reads, each blank, each under a comment saying what it does and
  what blank means, beside the `RECALL_CACHE_BUDGET_MB` block. Observed by AC3, AC4, AC5 and AC6.

## 3. Non-goals (OUT)

- Any edit to `tools/memory-tree/check-memory-hygiene.sh`. TOOL-aClearedLedger-8 edits that file
  and follows this unit; this unit only reads it.
- Any edit to `tools/memory-tree/transition_audit.py` or to the line check 26 prints. The cache
  figure is a contract of that module's own suite, which asserts it at `cache hits 1`.
- Any edit to the resolver block or to `tools/lib/resolve-python.sh`. The block is a gated
  byte-identical copy carried by every kit.
- A new name in `_engexempt` or `_pyexempt`. One name leaves; none enters.
- The four keys this repository's own `.memory-tree.conf` leaves undeclared. Absent reads as blank.
- An upgrade step. The example is copied at adoption only, and an absent key keeps its default.
- Any kit version, which the lander's `mint` moves.

## 4. Design

### Evidence

Read at `8db6f4be`. The reproduction is the brief's `a19.out`, taken on a frozen clone of that sha.

| Lines | What they say | Cause, verified |
|---|---|---|
| 1 | the scoped runs do not partition the unscoped run's lines | the two sides differ in one line, check 26's, at `cache hits 0` against `cache hits 4` (PINNED, 2026-11-13) |
| 1 | the example does not declare `OSTYPE` | `tools/memory-tree/check-memory-hygiene.sh@8db6f4be:606`, inside the carried resolver block, landed by `ed135af16` |
| 6 | the example does not declare a `RECALL_` key a module reads | `tools/memory-tree/id_grammar.py#resolve`, moved into this kit by `2d03321ab` |

### S1 — the figure depends on which run came first

`tools/memory-tree/transition_audit.py#render_liveness` prints the count of cached deltas the run
read. The cache sits under the git common directory, and a run writes every delta it computes. The
suite's unscoped run comes first, so on a cold clone it reads none and writes four, and the later
`--only 26` run reads four. On a node whose cache is warm both print four, which is why the arm
passed where it was written. The figure is a fact about the cache, not a verdict, and the arm
compares verdict lines. So the arm is the wrong side.

The helper is one line, spelled exactly so, because AC1 reads it by pattern:

```bash
_hs_lines() { grep . | sed -E 's/(cache hits )[0-9]+/\1N/' | sort -u; }
```

The comparison and the `diff` beside it each pipe `$out` and `$_hs_union` through `_hs_lines` in
place of the `grep . | sort -u` they carry today. No assertion is added or removed.

### S2 and S3 — the resolver block reads no conf

The arm's population is every `${NAME:-}` the engine reads as an adopter override. The engine
carries the launcher resolver inline, a copy of `tools/lib/resolve-python.sh` held byte-identical
by that file's own suite. The block reads the environment and no key a conf declares: the suite's
own comment says so of `GOV_PYTHON`. That name and `OSTYPE` are its two reads, and both appear
nowhere else in the engine. The first is in `_engexempt` by name today; the second arrived with the interpreter floor and nothing named
it. Leaving the block out of the derivation cures both and every later read the resolver gains.

The helper is one line, spelled exactly so, because AC2 reads it by pattern:

```bash
_engreads_of() { sed '/^# >>> resolve_python /,/^# <<< resolve_python$/d; s/[[:space:]]#.*$//; s/^[[:space:]]*#.*$//' "$1" | grep -oE '\$\{[A-Z][A-Z0-9_]+:[-=]' | sed 's/^\${//; s/:[-=]$//'; }
```

`_engreads` becomes the helper's output over the engine, joined with `_engpresets` as today. A
`sed` range whose closing line is missing deletes to the end of the file, and one whose opening
line is missing deletes nothing. Either would pass by reading less or hide nothing, so S3 asserts
both marker lines match exactly once in the engine.

The staged file for S3's other two assertions is written by the suite under its own `$TMP`:

```bash
BEFORE="${EXAMPLE_BEFORE_KEY:-}"
# >>> resolve_python — a staged block
INSIDE="${EXAMPLE_INSIDE_KEY:-}"
# <<< resolve_python
AFTER="${EXAMPLE_AFTER_KEY:-}"
```

The count of executed assertions, by reading the loops: `OSTYPE` leaves the population loop,
`GOV_PYTHON` leaves the exemption loop, and three are added. The net is one more, so the floor
moves by one, with a comment line in the file's own form.

New suite lines add no site of a class `memory/project/spawn-idiom-sites.txt` counts for this
file. Both helpers are reached through a pipe, and the staged file is written by a redirect.

### S4 — six keys, blank

`resolve` reads each of the six with a blank default, so a blank declaration is the absent state:

| Key | Blank means | Source of the comment text |
|---|---|---|
| `RECALL_NODE_TAG_CLASS` | the node-tag class `a-z` | `tools/memory-recall/README.md`, the optional-keys table |
| `RECALL_CITED_FAMILIES` | no cited family | the same table |
| `RECALL_BUILD_QID_CUTOFF` | no build-era boundary | the same table |
| `RECALL_EXPORT_DIR` | the export sits under the common git directory | the same table |
| `RECALL_EXCLUDE` | nothing is left out of the corpus walk | the same table |
| `RECALL_EXTRA_SOURCES` | no declared extra source | the README's paragraph on that key |

Each is written `KEY=""` on its own line. The block opens with the sentence the cache-budget block
carries, that the keys are memory-recall's and safe to delete where that kit is not adopted, and
adds that `id_grammar.py` in this kit is their reader. Each comment is two or three lines and
points at the README for the rest; the README owns the full text.

Probed on 2026-11-13 at `8db6f4be`: a copy of the example with the six blank lines appended and a
copy without them resolve to one `digest()`.

### The probes

Probe P1, the fold, run from the repository root:

```bash
eval "$(grep -E '^_hs_lines\(\) ' tools/memory-tree/check-memory-hygiene.test.sh)"
a='memory-hygiene: check 26 transitions examined 4 · cache hits 0 · x'
b='memory-hygiene: check 26 transitions examined 4 · cache hits 4 · x'
c='memory-hygiene: check 26 transitions examined 5 · cache hits 4 · x'
[ "$(printf '%s\n' "$a" | _hs_lines)" = "$(printf '%s\n' "$b" | _hs_lines)" ] && echo fold-equal
[ "$(printf '%s\n' "$b" | _hs_lines)" = "$(printf '%s\n' "$c" | _hs_lines)" ] || echo verdict-differs
```

Probe P2, the derivation, with `S` naming a scratch file holding the five staged lines above:

```bash
eval "$(grep -E '^_engreads_of\(\) ' tools/memory-tree/check-memory-hygiene.test.sh)"
_engreads_of tools/memory-tree/check-memory-hygiene.sh | sort -u | tr '\n' ' '; echo
_engreads_of "$S" | sort -u | tr '\n' ' '; echo
```

Probe P3, the python parity rule over the real kit, the suite's own pattern and exemption list:

```bash
K=tools/memory-tree
eval "$(grep -E '^_pyexempt=' $K/check-memory-hygiene.test.sh)"
cat $K/*.py | grep -oE "[]A-Za-z0-9_)](\.get\(|\[)[\"'][A-Z][A-Z0-9_]{2,}[\"']" \
  | sed "s/.*[\"']\([A-Z][A-Z0-9_]*\)[\"']\$/\1/" | sort -u | while read -r k; do
  case " $_pyexempt " in *" $k "*) continue ;; esac
  grep -qE "^$k=" $K/.memory-tree.conf.example || echo "undeclared $k"
done; echo done
```

Probe P4, blank against absent, with `A` and `B` naming two empty scratch directories:

```bash
E=tools/memory-tree/.memory-tree.conf.example
cp "$E" "$A/.memory-tree.conf"
grep -vE '^RECALL_(BUILD_QID_CUTOFF|CITED_FAMILIES|EXCLUDE|EXPORT_DIR|EXTRA_SOURCES|NODE_TAG_CLASS)=' "$E" > "$B/.memory-tree.conf"
python -c "import sys, pathlib; sys.path.insert(0, 'tools/memory-tree'); import id_grammar as g; print(g.resolve(pathlib.Path(sys.argv[1])).digest() == g.resolve(pathlib.Path(sys.argv[2])).digest())" "$A" "$B"
```

### What it does not check

- A difference between the two sides in the cache figure alone. That is the point of the fold.
- A conf override read inside the resolver block. The block reads none today, and its bytes are
  another suite's to hold.
- Whether a comment in the example is true. The arm reads `^KEY=` and nothing else.
- A second run-order figure on another check's line. One line differed at `8db6f4be`.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/.memory-tree.conf.example`

### Alternatives rejected

- **Dropping the figure from check 26's line.** It breaks the arms of the module's own suite that
  read it, and the line's prefix is what remote CI greps for liveness.
- **Warming the cache before the unscoped run.** It costs one more engine run in a suite the ask
  measures at 40 minutes (PINNED, 2026-11-13), and it makes the arm pass by ordering, which is
  the state that hid the defect.
- **Deleting the cache directory between the two runs.** The directory is shared by every worktree
  of the repository the suite runs in.
- **Adding `OSTYPE` to `_engexempt`.** One word, and the next read the resolver gains reds the
  suite again; the brief also refuses a waiver that makes a suite pass.
- **Spelling the engine's read as a bare `$OSTYPE`.** The block is a byte-identical copy, so the
  edit lands in the canonical file and every kit that carries it.
- **Declaring the six keys commented.** The arm reads `^KEY=`, so each would join `_pyexempt`. The
  commented form exists for keys an adopter script appends, and none appends these.

## 5. Acceptance criteria

A role agent's hook refuses a suite, so AC6 is the main loop's. The others are probes a builder
runs from the repository root.

- **AC1** — When probe P1 of section 4 runs against the suite file, it prints `fold-equal` and
  then `verdict-differs`, and `grep -o '| _hs_lines' tools/memory-tree/check-memory-hygiene.test.sh | wc -l`
  prints 4.
  Red when: the helper folds nothing, which prints `verdict-differs` alone, or folds a figure other
  than the cache's, which prints `fold-equal` alone, or one side of the comparison bypasses it.
  At `8db6f4be` the `eval` binds nothing and the probe prints `command not found`.
- **AC2** — When probe P2 of section 4 runs, its first line holds `BACKLOG_MODE` and `MAP_ROOT` and
  holds neither `OSTYPE` nor `GOV_PYTHON`, and its second line reads
  `EXAMPLE_AFTER_KEY EXAMPLE_BEFORE_KEY`. And `grep -E '^_engexempt=' tools/memory-tree/check-memory-hygiene.test.sh`
  prints `_engexempt="MAP_ROOT"`.
  Red when: the range is absent, which prints `EXAMPLE_INSIDE_KEY` too, or it does not close, which
  drops `EXAMPLE_AFTER_KEY`, or the stale name is still exempted.
- **AC3** — When `grep -cE '^RECALL_(BUILD_QID_CUTOFF|CITED_FAMILIES|EXCLUDE|EXPORT_DIR|EXTRA_SOURCES|NODE_TAG_CLASS)=""$' tools/memory-tree/.memory-tree.conf.example`
  runs, it prints 6.
  Red when: a key is missing, commented, or shipped with a value. At `8db6f4be` it prints 0.
- **AC4** — When probe P3 of section 4 runs, it prints `done` and no line opening `undeclared`.
  Red when: a module of the kit reads a key the example does not declare and the suite does not
  exempt. At `8db6f4be` it prints six `undeclared` lines, one per key of AC3.
- **AC5** — When probe P4 of section 4 runs over `tools/memory-tree/.memory-tree.conf.example`,
  it prints `True`.
  Red when: a declared key carries a value, or a blank one resolves differently from an absent one.
- **AC6** — When the main loop runs the suite the `New arm:` lines of section 6 name, on a frozen
  clone whose transition cache is cold, it exits 0, prints no line opening `FAIL`, and its last
  line opens `PASS (` with a total of 708 or more.
  Red when: any of the eight lines stands, an arm of S3 is absent and the total falls under the
  floor, or the clone's cache is warm, which hides S1 and proves nothing about it.
  permission: the main loop's; a role agent's hook refuses a suite.
  cost: one whole run of the suite, which the ask's severity row puts at 40 minutes (PINNED, 2026-11-13).
  figure: 708 is DERIVED, the floor `FLOOR_ASSERTIONS` after S3.

## 6. Gates

`memory-hygiene self-test`

The main loop runs the leg's suite at the close, on a frozen clone, with the plain bar after the
last unit. Each arm below is observed RED and then GREEN there.

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · covers AC2 · the range expression removed from `_engreads_of`, so the staged inside key is derived · `FLOOR_ASSERTIONS` 707 to 708
New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · covers AC1 AC6 · the fold removed from `_hs_lines` on a clone with a cold cache, so the partition differs on check 26's line · none, the arm is moved and not added

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 9. Reuse audit

The seams are the suite's own. S1 extends the partition arm's two pipelines. S2 follows the shape
`_pykeys` already has in the same file, a derivation taking its subject as a parameter so a fixture
arm grades a file the suite built. S4 extends the example's existing memory-recall block.
`python tools/codebase-map/reuse_lookup.py "derive the conf keys a shell engine reads as overrides
and compare them with the shipped example conf"` ranked name-stem neighbours only, `load_conf` and
`parse_conf` among them, and named no shared derivation of a shell engine's reads, so for a helper
outside this suite no existing seam fits. `gotchas.py --for-paths` over the estimate selected
`fixture-passes-by-finding-nothing`, which is S3's marker assertion, and
`two-answers-to-one-question`, which is why the example's comments point at the README. The recall
probe returned ask TOOL-aJoinedCanon-13 and the spec of TOOL-aProvenReuse-5, the arm's two earlier
widenings; neither names the carried block.

Recall terms used: `partition scoped unscoped check 26 cache hits conf example engine override
parity RECALL keys id_grammar`

# PLAY-dOrderedCharter-70 — the closing diff review's mediums and low, batched

**Status:** DEFERRED · rev-1 · 2026-11-05 · node d · Tier-2 · base de8d2d3a1 · streams playbook · order 17 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 |
| [2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief.md](../prompts/2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief.md) | research | PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 |
| [2026-11-05-prompt-PLAY-dOrderedCharter-70-build-brief.md](../prompts/2026-11-05-prompt-PLAY-dOrderedCharter-70-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes the rest of the round-1 closing diff review: M1 to M16, M18 and L1. M17 moved to
PLAY-dOrderedCharter-69, because it shares H3's fix. It is the review's minors batch, which the build method excepts
from one mechanism per spec. Each finding is fixed as the report says, the skeptic's correction binding, and two
collisions the report did not foresee are ruled in the open questions.

## 2. Scope (IN)

Every line below was read at `62c5f0c5c`, whose `tools/` and `skills/` equal base `de8d2d3a1`. The Design section
holds what a one-line item cannot.

- **S1** — M1. `tools/playbook/instruction_units.py#render_unit` and `check_statement` refuse a `cmd:` source that names
  no entry of a new `REGISTERED_COMMANDS`. A registered command runs with `cwd` the target, a timeout and
  `GIT_ENV_LEAKS` scrubbed, and multi-line output refuses the render. Observed by AC1 and AC2.
- **S2** — M2. `tools/unattended/unattended.sh#print_drift_delta` captures the reader's output and exit, prints the
  output as now, and carries the outcome on its line: a named line on a nonzero exit, `searched-empty` on exit 0
  with a `drift-delta: skipped` line, else `filled`. It still returns 0. Observed by AC3.
- **S3** — M3. `tools/playbook/tag_index.py#read_toml_tags` places a tag on its row: the `tag =` key line inside the
  nth `[[<table>]]`, and `derive_tag_rows` emits that row's extent as `end_line`. Observed by AC4 and AC5.
- **S4** — M4. `tools/memory-tree/build_records.py#read_records` selects by `derive_record_name(kind)` for every kind but
  deviation, which keeps its instrument's glob as the kind's explicit exception. Observed by AC6.
- **S5** — M5. A new `tools/playbook/instruction_units.py#derive_tool_rel` joins path parts and adds no segment for an empty prefix.
  Every string join of `derive_kit_prefix()` under `tools/playbook/`, and the `prefix` join of `read_manifests`, goes
  through it, which covers `read_manifests` and `run_tag_check`. Observed by AC7 and AC8.
- **S6** — M6. `tools/memory-tree/merge-rows.py#resolve_tables` compares each written chunk against the sides with the
  terminator normalised, keeping the `None` sides of `O.get`. Observed by AC9.
- **S7** — M7. `tools/playbook/tag_index.py#build_overlay` passes `--no-renames`. Observed by AC10.
- **S8** — M8, the key route only. `memory_root` and `charter` fold into the freshness digest and the `path_row` key,
  `INDEX_SCHEMA` moves to 3, the `parsed` lookup and `VIEW_JOIN` filter on that key, and
  `read_live_versions` derives each worktree's digest from that worktree's own conf. Observed by AC11 and AC12.
- **S9** — M9. The `[[regenerate]]` block of `tools/playbook/kit.toml` sets
  `writes = ["AGENTS.md", ".governance/instructions.lock"]`. Observed by AC13.
- **S10** — M10. `tools/playbook/kit.toml` withholds `positional-refs.txt`, `positional-producers.txt`,
  `core-pending.txt` and `instructions-legacy.txt` as `project-owned`. The write mode of
  `tools/playbook/adopt-playbook.sh` writes an empty `positional-refs.txt` and `core-pending.txt` in a target that lacks
  them. `check_positional`'s absent-list red stays. `tools/govkit/govkit.py#selfcheck` gains an arm that reds a shipped
  engine file holding the source repo's own record paths. Observed by AC14, AC15 and AC16.
- **S11** — M11. Every sentence of the Design section's site table re-points to this kit's `id_grammar.py`, and the
  kit-dogfood parity between the two HYGIENE copies holds. Observed by AC17.
- **S12** — M12. `tools/run-gates/owed_rows.py#run_selftest` gains five cases: a leg with no descriptor row, a leg no
  dossier claims, two differing `KNOWN` lines, a warn-mode breach, and a missing ceiling row. Observed by AC18.
- **S13** — M13. `tools/check-install-prefix.test.sh` and `tools/run-gates/run-gates.test.sh` assert the
  `slot point.flow.version` lines. Observed by AC19.
- **S14** — M14. `tools/unattended/check-unattended.test.sh` gains the arm that reaches the foreign-anchor skip.
  Observed by AC20.
- **S15** — M15. `tools/playbook/check_layers.py#check_layers` collects a core file it cannot read or parse, and exits
  2 naming each one. Observed by AC21.
- **S16** — M16. A plant holds each of the two fail-closed postconditions of `tools/memory-tree/merge-rows.py` to its own
  message, and the existing plant asserts the message it really reaches. Observed by AC22.
- **S17** — M18. `tools/playbook/core.py#derive_instruction_row` prints the full command, composed from the row it built.
  Observed by AC23.
- **S18** — L1. The arm `with no recall kit, check 18 reds an undefined decision by name` in
  `tools/memory-tree/gotchas.py#cmd_selftest` runs from a copy of the kit with no `memory-recall` sibling. Observed by AC24.
- **S19** — The checklist lines the report asks for, under the Design section's checklist heading. Observed by AC25.

## 3. Non-goals (OUT)

- **H1, H2, H3 and M17.** Unit 67 owns H1, unit 68 owns H2, and unit 69 owns H3 and M17.
- **Rebuilding the shared `index.db`.** Unit 69 hands that to the main loop.
- **A probe runner.** The `probe:` source keeps refusing. S1 registers commands, and it does not build the runner the
  source's comment defers.
- **`tools/playbook/positional-refs.txt`'s content.** The close carry's adopter-name item stays with the close. S10
  changes who receives the file, not what it holds.
- **The `point.instruction.guard` declaration.** M18 notes that a full command still stops at the guard refusal.
  Declaring that point is not in the report's fix.

### Edges

none

## 4. Design

### M1 — the registry

The first fork rules its shape. `REGISTERED_COMMANDS = ("git rev-parse --abbrev-ref HEAD",)` sits beside `LEGACY_LIST`, and
`CMD_TIMEOUT_S = 30` beside it. `check_statement` adds a red naming the source and the tuple when a `fact` carries
`cmd:<x>` with `x` outside it, and `render_unit` raises `UnitRowError` before any spawn. A registered run:

```python
done = subprocess.run(shlex.split(arg), capture_output=True, text=True, encoding="utf-8", errors="replace",
                      stdin=subprocess.DEVNULL, cwd=root, timeout=CMD_TIMEOUT_S,
                      env={k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS})
```

`render_unit` and `render_units` take `root=None`, and `tools/playbook/render_playbook.py#render_unit_slots` passes its
`target`. `subprocess.TimeoutExpired` joins the refused-run clause, and a `\n` inside the stripped output refuses.
`GIT_ENV_LEAKS` comes from `tree_lib` after `load_memory_tree_path`, as the fixtures take it.
`STATEMENT_ROWS`' `fx.fact` row moves from `git worktree list` to the registered command, and it gains a refused twin.
Plant `cmd-source` checks five cases: the unregistered red; an unregistered render that refuses with a sentinel file
never written; the registered command answering from `root` when the caller's cwd is another repository; a two-line
command refused; a sleeping command refused. The last two patch the tuple and the timeout in process.

### M2 — the outcome

```bash
  local out rc=0
  out=$("$py" "$d/drift_report.py" --delta "$base" HEAD) || rc=$?
  [ -z "$out" ] || printf '%s\n' "$out"
  if [ "$rc" != 0 ]; then
    echo "drift-delta: the reader exited $rc, no delta read"
    return 0
  fi
  case "$out" in
    *"drift-delta: skipped"*) echo "drift-delta: slot point.runtime.reading · searched-empty" >&2 ;;
    *) echo "drift-delta: slot point.runtime.reading · filled" >&2 ;;
  esac
  return 0
```

`case` keeps it off the spawn-idiom list. The report's reason stands: a test for empty output could not work, because
the reader always prints at least the skipped line.

### M3 — the row

`tomllib` keeps row order, so the nth parsed row is the nth `[[<table>]]` header. `read_toml_tags` returns
`(value, line, end_line)`: `line` is the first line matching `^\s*tag\s*=` inside the row's span, and `end_line` the last
non-blank line before the next `[` header or the end. `derive_tag_rows` emits the row's text from `line` through `end_line`,
as `extract_doc` does for a section, so `show` and a bundle serve the row and count its bytes. When the header count differs from the row count, as a header
inside a multi-line string makes it, each row keeps line 1, the fallback the function has today, so no row is dropped.
Plant `toml-row` runs `derive_tag_rows` over a list naming a tag above its row.

### M4 — the selection

```python
named = derive_record_name(kind) if kind != "deviation" else None
keep = (lambda p: named.search(p)) if named else glob.fullmatch
```

The typed-kinds plant of `tools/memory-tree/build_records.py#run_fixture` gains a research record named
`<date>-build-ARCH-tKinds-1-change-plan-2.md`, which `read_records` must not select. A mis-named record claiming a
typed kind still reds at `read_bindings`, so the narrowing hides nothing.

### M5 — the join

```python
def derive_tool_rel(*parts) -> str:
    """`parts` under the tool root, tree-relative; a root install's empty prefix adds no segment."""
    return "/".join(p for p in (derive_kit_prefix(), *parts) if p)
```

`derive_kit_rel(name)` becomes `derive_tool_rel(KIT_DIR.name, name)`. Plant `root-prefix` holds
`iu.derive_kit_prefix` to `""` over a tree with `kitx/kit.toml` and `kitx/instructions.toml`. It asserts
`read_manifests` answers `kitx/instructions.toml`, and that the row is read.

### M6 and M16 — the merge driver's postconditions

M6's fold, at the check in `resolve_tables`:

```python
def fold(t):
    return t if t is None or t.endswith(("\n", "\r")) else t + term
...
    if text not in (fold(O.get(entry)), fold(A.get(entry)), fold(B.get(entry))):
```

The plants, each asserting its own message in the driver's stderr, in `tools/memory-tree/merge-rows.test.sh` through
`check_table_case` and in `tools/playbook/instructions_edit.py`:

| Plant | Input | Asserted |
|---|---|---|
| `merge-parse` (existing) | an indented header after an entry | `is not one array-of-tables entry` |
| `merge-cut` (new) | an indented header in the preamble | `the cut does not reproduce tomllib's read` |
| `merge-unterminated` (new) | O, A, B ending in an unterminated entry, disjoint edits | merges clean |
| `merge-moved` (new) | an unterminated final chunk in ours, an add in theirs | merges clean, per the second fork |
| `merge-written` (new) | the second fork's stub | `byte-identical to no side's` |

### M7 — the plant

Plant `dirty-rename` runs `git mv memory/guides/ALPHA.md memory/guides/BETA.md` and leaves it staged. The view must
resolve `doc.beta` and not `doc.alpha`.

### M8 — the key

```python
def derive_conf_key(memory_root, charter) -> str:
    return hashlib.sha256(f"{memory_root}\n{charter}".encode("utf-8")).hexdigest()[:12]
```

| Site | Change |
|---|---|
| `SCHEMA` | `path_row` gains `conf TEXT NOT NULL` after `version` |
| `INDEX_SCHEMA` | 3, so an old file rebuilds from nothing, printing its existing line |
| `derive_versions_digest(versions, conf)` | the text gains a `conf=<key>` line, so a conf edit misses `tree_built`, committed or not |
| `derive_context` | `ctx["conf"]`, and `digest` built from it |
| `_write_path_rows(con, pairs, versions, conf)` | the `parsed` lookup and the insert carry `conf` |
| `load_view` | a temp table `view_conf`, one row |
| `VIEW_JOIN` | adds `JOIN view_conf c ON p.conf=c.conf` |
| `read_index_rows` | its `path_row` dump filters on `ctx["conf"]` |
| `read_live_versions` | reads each worktree's conf through `id_grammar.load_conf`, derives that digest, and returns the live keys third |
| `remove_dead_versions` | deletes `path_row` rows of a key no live worktree derives |

`blob_row` is keyed by text alone and stays. The module docstring's table and `tools/playbook/README.md` follow.
Plant `charter-warm` commits `CHARTER="CHARTER2.md"` over a built index, and the warm dump must equal a cold one, with
`doc.charter` at the new file only. Plant `charter-dirty` makes the same edit uncommitted, and `doc.charter` must
follow it.

### M9 and M10 — the descriptor

The `project-owned` block follows `windows-only-legs.txt` in `tools/run-gates/kit.toml`:

```toml
[[files]]
include = ["positional-refs.txt", "positional-producers.txt", "core-pending.txt", "instructions-legacy.txt"]
role = "project-owned"
```

`tools/playbook/adopt-playbook.sh` execs `render_playbook.py` for everything but its selftest, so its write mode IS that
script's. A new `write_empty_lists(target)` runs beside `write_charter_lock`. Under `<target>/<prefix>/<kit dir>`, when
that directory exists, it creates each of the two lists if absent, empty, and leaves a present file alone. The report's
"unarmed" reading is `tools/playbook/positional.py#check_positional`'s for a present, empty list. `--check` writes nothing.
The other two lists read as absent-means-none already (`read_producer_rows`, the legacy reader).

The new `selfcheck` arm is `check_source_rows`. For each `shipped` engine file it reds a line whose first tab cell starts
`memory/builds/`, the expansion of `{memory_root}/builds/`, naming the file and the count. Over the tree at
`62c5f0c5c` this predicate hits `tools/playbook/positional-refs.txt` alone, with 38,552 rows (PINNED), so S10's own
withholding clears it. It does not see `core-pending.txt`, whose rows are leg and kind names, and it does not see a
gov path outside the record tree. `tools/govkit/selftest.py` plants a fixture engine file holding such a row.

The M9 arm extends the fixture `kit_rb` of `tools/govkit/selftest.py`: its `writes` gains `.governance/instructions.lock`,
`gen.sh` rewrites that file, and after the rolled-back `update` the lock's bytes equal the snapshot.

### M11 — the sites

Each row names the stale claim. The remedy is the same: this kit's `id_grammar.py`, whose absence is a named refusal.

| Site | Claim |
|---|---|
| `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md`, lines 396, 525, 547, 550, 557 | the grammar, the index builder and the superseded-by map come from the recall kit, and it must be installed |
| `tools/memory-tree/.memory-tree.conf.example`, lines 306 and 310 | the same, for the near-match key |
| `tools/memory-tree/README.md`, rows 19, 23, 40, 42, 49 and line 477 | row 40's `requires_if` rows, which no longer exist, and the install advice |
| `skills/session-kickoff/manifest-check.sh`, line 1046 | exit 3 means memory-tree without memory-recall |
| `tools/check-wiring.sh`, line 1379 | the sibling recall kit owns the anchor grammar |
| `tools/memory-tree/check-memory-hygiene.sh`, line 3182 | the same comment; the report does not list it, and `git grep` found it |

Line 550 and the last row widen the report's list by the same stale sentence. The report spells two paths by base
name; the table holds where they sit. `tools/memory-tree/.memory-tree.conf.example`, line 276, describes a recall-only
key and stays.

### M12 to M14 — the arms

S12's cases follow the report: `add_leg`'s twin with no `[[gate_leg]]` row; a leg `build_fixture_repo` does not
pre-claim; a `KNOWN` line differing from its twin, rc 2; `enforce = "warn"` over the grown file, rc 0 with the count
on the summary line; a leg with no ceiling row, a `deferred —` line at rc 0.

S13: the no-engine arm of `tools/check-install-prefix.test.sh` asserts `slot point.flow.version · not-installed: `. The
unreachable-govkit arm of `tools/run-gates/run-gates.test.sh` hides the stub `govkit.py` so `resolve_kit_dir` raises
`LookupError`, then asserts the slot line and that the `not reachable` line follows it. On the reachable run it
asserts `filled`, which `run_sc_bar`'s `2>&1` carries.

S14's arm removes `$_ig_dst/id_grammar.py` from the `ak` fixture, then asserts
`hit "check 37 SKIPPED for memory/builds/tRun"`, `hit "resolved through neither"` and `miss "found no foreign anchor"`.
`set_ak_pristine`'s `reset --hard` restores the file.

### M15 — the exit

`check_layers` gathers `unread`, in place of each bare `continue` at the `.py` read and the `.sh` decode. A non-empty
list returns `["layers: UNREADABLE <file> (<why>)", ...]` and rc 2, ahead of the verdict, as
`tools/memory-tree/import_walk.py#derive_import_closure` does. Plant `unparsable` appends `def broken(:` to the fixture's
core file. `NOT_READ` keeps its text, because this state is now no longer unread.

### M18 — the command

```python
given = ["--manifest", flags["--kit"], "--tag", f"unit.{name}", "--level", flags["--level"], "--type", flags["--type"],
         *(["--trigger", "always"] if trigger else []), "--budget", budget, "--text", flags["--text"]]
command = " ".join([f"python {prefix}/playbook/instructions_edit.py add", shlex.join(given),
                    "--build <slug> --unit <id> --mark <editorial|semantic>"])
```

Plant `instruction-unit`, new in `tools/playbook/core.py#PLANTS`, runs the factory, parses the printed command through
`instructions_edit.build_parser`, runs `propose add` from it, and asserts each printed row line sits in the proposal's
added lines.

### L1 — the arm

The report offers a copy of the kit or a rename. The copy is taken, because it observes more: `shutil.copytree` of the
kit's `*.py` into `<tn>/tools/memory-tree`, then `subprocess.run([sys.executable, "<copy>/gotchas.py", "--check"], cwd=tn)`.
There is no `tools/memory-recall` under `tn`, so a regained import fails the arm. The second arm of the pair keeps its label.

### The checklist

`memory/gotchas/observed-by-claim-no-arm-discharges.md` gains four lines: a fixture must not pre-satisfy the condition its
arm exists to catch (M12); a rewrite turning a `hit` into a `miss` keeps an arm that still reaches the branch (M14); a
plant asserts the message of the arm it names, never a shared failure string (M16); an arm's label names only the state
its setup creates (L1). `memory/gotchas/amendment-leaves-its-other-half-standing.md` gains one: a spec that removes a
dependency greps its shipped text for the removed kit's name in the same pass (M11).

### The probes

Run from the repo root.

```bash
tk="--set tags.bare-refs=charter-only --set tags.retired-cites=refuse-new"
pdd() { # the reader's exit · its one line -> what print_drift_delta prints
  d=$(mktemp -d); printf 'import sys\nprint(%s)\nsys.exit(%s)\n' "'$2'" "$1" > "$d/drift_report.py"
  { echo 'fact() { _fact=abc; }; resolve_python() { echo python; }'; echo "resolve_kit_dir() { echo '$d'; }"
    sed -n '/^print_drift_delta()/,/^}/p' tools/unattended/unattended.sh; echo 'print_drift_delta x'; } > "$d/p.sh"
  bash "$d/p.sh" 2>&1
}
practice_rows() { python - <<'P'
import sys
sys.path.insert(0, "tools/playbook")
import tag_index as t
rows = t.derive_tag_rows(open("tools/playbook/practices.toml", encoding="utf-8").read(), "practice")
print(len(rows), sum(r[4].startswith("tag =") for r in rows), sum(r[3] > r[2] for r in rows))
P
}
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_tool_rel`, `derive_conf_key`, `check_source_rows`, `write_empty_lists` | Python functions | `py.function`, each graded OK by `lexicon.py --suggest` at `62c5f0c5c` |
| `REGISTERED_COMMANDS`, `CMD_TIMEOUT_S` | module constants | the kit's upper-snake set |
| `cmd-source`, `root-prefix`, `merge-cut`, `merge-unterminated`, `merge-moved`, `merge-written`, `toml-row`, `dirty-rename`, `charter-warm`, `charter-dirty`, `unparsable`, `instruction-unit` | plant names | none |

### Migration

`INDEX_SCHEMA` 3 rebuilds each index from nothing on its next read, about one cold build per host. The four withheld
files have never reached an adopter, because they are new in this unlanded diff, so no upgrade step is owed.

### Rollout

Live at landing. Two legs' populations move: `tags` re-parses, and `govkit selfcheck` gains the arm S10's withholding
satisfies, so S10's two halves land in one pass.

### Files touched (estimate)

- `tools/playbook/instruction_units.py`: S1, S5. Unit 69 touches it too.
- `tools/playbook/render_playbook.py`: S1, S10
- `tools/playbook/tag_index.py`: S3, S7, S8. Unit 68 touches it too.
- `tools/playbook/gov_tag.py`: the plants of S3, S7, S8. Units 68 and 69 touch it too.
- `tools/playbook/adopt-playbook.sh`: plant rows. Units 68 and 69 add rows too.
- `tools/playbook/README.md`: S1, S8. Unit 68 touches it too.
- `tools/playbook/instructions_edit.py`: S5, S16
- `tools/playbook/kit.toml`: S9, S10
- `tools/playbook/check_layers.py`: S15
- `tools/playbook/core.py`: S17
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`: S2
- `tools/unattended/check-unattended.test.sh`: S14
- `tools/memory-tree/build_records.py`: S4
- `tools/memory-tree/merge-rows.py`, `tools/memory-tree/merge-rows.test.sh`: S6, S16
- `tools/memory-tree/gotchas.py`: S18
- `tools/memory-tree/HYGIENE.template.md`, `memory/HYGIENE.md`: S11
- `tools/memory-tree/.memory-tree.conf.example`, `tools/memory-tree/README.md`, `tools/memory-tree/check-memory-hygiene.sh`: S11
- `skills/session-kickoff/manifest-check.sh`, `tools/check-wiring.sh`: S11
- `tools/run-gates/owed_rows.py`, `tools/run-gates/run-gates.test.sh`: S12, S13
- `tools/check-install-prefix.test.sh`: S13
- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`: S9, S10
- `memory/gotchas/observed-by-claim-no-arm-discharges.md`, `memory/gotchas/amendment-leaves-its-other-half-standing.md`: S19

The overlaps with units 68 and 69 are the findings' own: each finding sits in the file that holds its defect, at a
different symbol. This unit builds last of the four, so its passes meet a settled file. `memory/HYGIENE.md` may sit on
the kickoff manifest's watch list, and the builder restamps that manifest if the hook refuses.

### Alternatives rejected

- **Testing `print_drift_delta`'s output for empty.** The report's own refusal, in M2.
- **A row that scopes M8 by deleting stale path rows at build.** The skeptic ruled it unsound, and the key route binds.
- **Softening `check_positional`'s absent-list red for M10.** The skeptic's correction keeps it.

## 5. Production-readiness checklist

- security: S1 narrows a surface: a target's manifest can no longer choose what the renderer executes. The registry lives
  in the kit, so an untrusted target cannot widen it. S10 stops shipping gov's citations to adopters.
- perf / scale: S8 costs one cold build per host. `check_source_rows` reads each shipped engine file once per `selfcheck`.
- error / empty / loading states: every refusal above names its subject. An `unread` file exits 2 and is not a green.
- observability: M2's three outcomes each print, and the layer check names each unread file.
- risks: an adopter already rendering a `cmd:` row of its own is refused. No tracked tree holds one (the report), and
  the refusal names the tuple. S8 is the batch's one data-model change, and its plants compare warm with cold.
- testing: the plants and suite arms named per item, and AC1 to AC25 by a pass.
- migration: the schema stamp (Migration, above).
- user docs: `tools/playbook/README.md` follows S1 and S8, and S11 is itself the shipped text. No page under `help/`
  spells `cmd:` or the schema, by `git grep` at `62c5f0c5c`.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/instruction_units.py fixture --plant cmd-source` runs, it exits 0 and prints
  `fixture · green`.
  Red when: an unregistered command executes, so the sentinel exists, or a registered one answers from the caller's cwd.
- **AC2** — When `grep -n "cwd=root" tools/playbook/instruction_units.py` runs, it prints the line of the one `cmd:` run, and
  `grep -n "render_unit(u, read_key, target)" tools/playbook/render_playbook.py` prints one line.
  Red when: the renderer never hands the target over, so the plant's `root` is unused in a real render.
- **AC3** — When `pdd 0 'drift-delta: skipped — no reading'`, from the Design section's probes, runs, it prints
  `searched-empty`. `pdd 0 'drift-delta: BASE a'` prints `filled`. `pdd 2 'x'` prints
  `drift-delta: the reader exited 2, no delta read` and no `filled`, and each exits 0.
  Red when: a failed or skipped read prints `filled`, as it does at base.
- **AC4** — When `practice_rows` runs, it prints three numbers, the first two equal, and the third above `0`.
  Red when: a row lands on the `foundation` list. At base the second is 3 of 39 and the third 0.
  figure: 39 is DERIVED from the catalogue; 36 misplaced rows are PINNED from the report.
- **AC5** — When `python tools/playbook/gov_tag.py --fixture --plant toml-row $tk` runs, it exits 0.
  Red when: the first quoted mention wins again.
- **AC6** — When `python tools/memory-tree/build_records.py --fixture --plant typed-kinds` runs, it exits 0, with the
  research record outside the selected change records.
  Red when: the wider name still selects it, so `read_change` returns it malformed.
- **AC7** — When `python tools/playbook/instructions_edit.py fixture --plant root-prefix` runs, it exits 0 and prints
  `fixture · green`.
  Red when: an empty prefix yields `/kitx/instructions.toml`.
- **AC8** — When `git grep -n -E "derive_kit_prefix\(\)\}/|\{prefix\}/\{desc" -- tools/playbook` runs, it prints nothing.
  Red when: a join keeps the f-string spelling.
- **AC9** — When `python tools/playbook/instructions_edit.py fixture --plant merge-unterminated` runs, it exits 0.
  Red when: the all-unterminated case raises `StructureDrift` and goes to hand resolution.
- **AC10** — When `python tools/playbook/gov_tag.py --fixture --plant dirty-rename $tk` runs, it exits 0.
  Red when: `doc.alpha` still resolves into a file the worktree no longer has.
- **AC11** — When `python tools/playbook/gov_tag.py --fixture --plant charter-warm $tk` runs, it exits 0 and prints
  `incremental rows equal a cold build's`. The same holds for `--plant charter-dirty`.
  Red when: the old charter keeps serving `doc.charter`, or an uncommitted conf edit applies nothing.
- **AC12** — When `grep -n "^INDEX_SCHEMA = 3" tools/playbook/tag_index.py` runs, it prints one line, and
  `python tools/playbook/gov_tag.py --fixture --plant two-versions` still exits 0.
  Red when: a stale file keeps its old table, or `--gc` leaves rows of a dead key.
- **AC13** — When `python -c "import tomllib; print(tomllib.load(open( 'tools/playbook/kit.toml' , 'rb'))['regenerate'][0]['writes'])"`
  runs, it prints both paths, `.governance/instructions.lock` among them.
  Red when: the lock stays outside the rollback snapshot.
- **AC14** — When `python tools/govkit/govkit.py shipped` runs, no row names any of the four files.
  Red when: an adopter still receives one.
- **AC15** — When `python tools/playbook/gov_tag.py check --base HEAD` runs in a scratch install of the kit, after
  `bash tools/playbook/adopt-playbook.sh --target .` there, it prints `tags: positional · unarmed` and no `stale` row.
  Red when: the empty lists are not written, or gov's rows reach the target.
  cost: one scratch install. permission: a role agent's scratch guard refuses this run, so the main loop observes it.
- **AC16** — When `python tools/govkit/govkit.py selfcheck` runs in a detached scratch worktree of the tip, with the new
  `[[files]]` block deleted from `tools/playbook/kit.toml`, it reds and names `tools/playbook/positional-refs.txt`.
  Red when: the arm stays silent over those rows.
  permission: `selfcheck` is a leg's argv, so the main loop observes it, beside the new arm of `tools/govkit/selftest.py`.
- **AC17** — When `git grep -n -E "requires that kit|no memory-recall kit installed|memory-recall kit's (anchor|own index|index)|recall kit's superseded|without memory-recall|sibling memory-recall|Install the memory-recall|rows naming the memory-recall" -- tools/memory-tree memory/HYGIENE.md skills/session-kickoff/manifest-check.sh tools/check-wiring.sh`
  runs, it prints nothing, and `diff tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md` prints the hunks it printed at base.
  Red when: a site keeps the claim, or the two copies part.
  figure: the sites are PINNED at `62c5f0c5c`.
- **AC18** — When `python -c "import sys; sys.path.insert(0, 'tools/run-gates' ); import owed_rows; sys.exit(owed_rows.run_selftest())"` runs,
  it prints `PASS — the owed-rows fixtures, 12 cases`.
  Red when: a case fails. With the two owed appends for the descriptor and dossier rows deleted, the two new cases
  fail, where at base nothing does.
- **AC19** — When `grep -c "slot point.flow.version" tools/check-install-prefix.test.sh tools/run-gates/run-gates.test.sh`
  runs, each count is above `0`.
  Red when: an arm is missing. The main loop observes each red by deleting the slot line.
- **AC20** — When `grep -c "resolved through neither" tools/unattended/check-unattended.test.sh` runs, it prints a count
  above `0`.
  Red when: no arm reaches the skip. The main loop observes it red with `scan_foreign_anchors` returning 0 on that branch.
- **AC21** — When `python tools/playbook/check_layers.py --fixture --plant unparsable` runs, it exits 2 and prints
  `layers: UNREADABLE`, naming the fixture's core file.
  Red when: the file is skipped, rc 0 with 0 edges, as at base.
- **AC22** — When `python tools/playbook/instructions_edit.py fixture --plant merge-cut` runs, it exits 0, and the same holds
  for `merge-parse`, `merge-moved` and `merge-written`.
  Red when: a plant passes on the shared `merge-rows failed` string, so deleting the check it names stays green.
- **AC23** — When `python tools/playbook/core.py fixture --plant instruction-unit` runs, it exits 0 and prints
  `fixture · green`.
  Red when: the printed command does not parse, or `propose` derives another row.
- **AC24** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree' ); import gotchas; sys.exit(gotchas.cmd_selftest())"`
  runs, it prints `arm ok    with no recall kit, check 18 reds an undefined decision by name`.
  Red when: the arm runs in process again, or the copy cannot run without the recall kit.
  cost: the whole selftest.
- **AC25** — When `grep -c "pre-satisfy\|hit. into a .miss\|shared failure string\|names only the state" memory/gotchas/observed-by-claim-no-arm-discharges.md`
  runs, it prints `4`, and `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: a checklist line is missing, or the edit breaks the catalogue's checks.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `recall floor arms` · `recall floor` · `govkit selftest` · `govkit refusal join` · `kit/dogfood doc parity` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `transition-audit arms` · `straggler-guard arms` · `tags (the resolver's checks)` · `instruction units selftest` · `instruction edits selftest` · `core selftest` · `layer dependencies (the core never depends on an expansion)` · `gotchas selftest` · `row-keyed merge driver replay` · `install-prefix self-test` · `run-gates canary` · `govkit selfcheck`

The first thirteen are what the guards join owes the Files-touched paths, derived by this writer from each leg's
`guard` under `BROAD_LEG_FLOOR` 5. `{prefix}/`, `{prefix}/memory-tree/` and `{prefix}/run-gates/` are broad and excluded.
The rest run a suite or a fixture this unit moves. `unattended.test.sh` and `check-unattended.test.sh` run under the
shards named `unattended driver selftest` and `unattended gate selftest`.

New arm: tools/playbook/instruction_units.py · covers AC1 · plant `cmd-source` stages an unregistered command and a sentinel · none
New arm: tools/unattended/unattended.test.sh · covers AC3 · an empty history and a stub reader exiting 1 · the suite's own floor
New arm: tools/playbook/adopt-playbook.sh · covers AC5 AC10 AC11 AC21 · rows for `toml-row`, `dirty-rename`, `charter-warm`, `charter-dirty` and `unparsable` · the suite's arm count, if a floor reads it
New arm: tools/memory-tree/build_records.py · covers AC6 · the typed-kinds plant stages a research record on a wider name · none
New arm: tools/playbook/instructions_edit.py · covers AC7 AC9 AC22 · the plants the Design section tables · none
New arm: tools/memory-tree/merge-rows.test.sh · covers AC9 AC22 · `check_table_case` twins of those plants, each with its own message · its two floors
New arm: tools/govkit/selftest.py · covers AC13 AC16 · the rollback fixture's lock, and a fixture engine file holding a record row · none
New arm: tools/run-gates/owed_rows.py · covers AC18 · five cases, each a tree that owes what no prior case could · none
New arm: tools/check-install-prefix.test.sh · covers AC19 · the no-engine arm's slot line · its floor
New arm: tools/run-gates/run-gates.test.sh · covers AC19 · the hidden stub govkit · `FLOOR_ASSERTIONS` by the arms added
New arm: tools/unattended/check-unattended.test.sh · covers AC20 · `id_grammar.py` removed from the `ak` fixture · the suite's own floor
New arm: tools/playbook/core.py · covers AC23 · plant `instruction-unit` · none
New arm: tools/memory-tree/gotchas.py · covers AC24 · a kit copy with no recall sibling · none

## 8. Open questions

- **F1 — What is M1's registry? The report says to match "a registered entry", and none exists.**
  - **(A)** A tuple in `tools/playbook/instruction_units.py`, holding the one command the tree's rows use.
  - **(B)** A `[[command]]` table in a new kit file.
  - **(C)** A row in the target's own manifest or overlay.

  (A) needs no new file, reader or schema, and it denies by default. (B) adds a file, a reader and a parity question for
  one row. It is the richer option only if adopters need their own commands, and nothing in the tree or the records
  asks for that. (C) lets the untrusted target widen what its own render executes, the exact surface M1 closes, so the
  fork rule's third veto discards it. The batch can carry (A). A later build that needs adopter commands adds a row
  through the unit's own review.

  Recommendation: A. RESOLVED (agent, 2026-11-05, delegated): A, by `2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief`,
  tie-broken by fewer open questions after (C)'s veto. widens: none · relaxes: none
- **F2 — What does M16's second plant assert, now that M6's fold makes its case merge clean?**
  - **(A)** Keep the postcondition. `merge-moved` asserts the clean merge, and `merge-written` reaches the arm through
    an in-process stub that alters a chunk on the second `read_tables` call.
  - **(B)** Delete the check, as a guard whose fallback the fold made dead.
  - **(C)** Keep the check with no plant, and record it as unarmed.

  The report's M16 says an unterminated chunk moved mid-file raises `byte-identical to no side's`. That is measured before
  M6, and with M6's fold the written chunk equals a folded side, so the case merges, which is M6's purpose. This writer
  found no input that reaches the check after the fold, because `resolve_tables` writes each kept chunk verbatim and cuts
  at the same headers. (B) removes a fail-closed check from a driver that handles merges, a relaxation no finding asks for.
  (C) leaves M16's finding open. (A) keeps the check, gives it a failing case, and answers both findings.

  Recommendation: A. RESOLVED (agent, 2026-11-05, delegated): A, by `2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief`,
  as the option satisfying both findings' criteria. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-05 · initial draft, by `2026-11-05-prompt-PLAY-dOrderedCharter-67-repair-brief`, M1 to M16, M18 and L1,
  with each skeptic's correction, each line read at `62c5f0c5c`.

## 10. Reuse audit

Each item extends the seam its finding names, and none adds a mechanism beside one. M3 follows `extract_unit`'s row span.
M4 reuses `tools/memory-tree/build_records.py#derive_record_name`. M7 follows `tools/run-gates/owed_rows.py`'s
`--no-renames`. M8 extends `derive_versions_digest` and `VIEW_JOIN`. M9 and M10 use the descriptor's `writes` and the
`project-owned` role, as `tools/run-gates/kit.toml` does. M15 follows `tools/memory-tree/import_walk.py#derive_import_closure`.
M18 follows `tools/playbook/instructions_edit.py#render_proposal`. Plants go in the existing tables, and rows in
`run_plant_rows`. M1's registry is the one new data shape: no existing seam fits, because `render_unit`'s own comment
records that no probe registry exists, and
`python tools/codebase-map/reuse_lookup.py "a closed list of commands a render may run"` ranked generic `run` and `render`
symbols and no such list. The recall query returned TOOL-aDistilledCharter-7, an earlier batch of this shape, and no record
of a command registry. Where the report and
the source disagree: M11's two base-name paths, the sentence at line 550 and the comment at
`tools/memory-tree/check-memory-hygiene.sh` line 3182 the report omits, and M16's case, which M6 changes. Each is ruled above.

Recall terms used: `python tools/memory-recall/query.py "the closing review's medium findings, a render runs an unregistered command and a fixture lacks its failing case" --terms "render_unit cmd source registry print_drift_delta read_toml_tags read_records derive_record_name resolve_tables tree_built project-owned check_layers"`

# TOOL-dTotalRecall-114 — the close's first bar: each red of the merged tree is repaired at its cause, converted where a conversion is short and widened through its ledger where the need is real

**Status:** CLOSED · rev-1 · 2026-11-25 · node d · Tier-2 · base e5b7ee15 · streams tooling · order 42

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-dTotalRecall-114-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-1-acceptance-ledger.md) | log | — |
| [2026-11-25-build-TOOL-dTotalRecall-114-deviation-1015.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-deviation-1015.md) | deviation | — |
| [2026-11-25-build-TOOL-dTotalRecall-114-widen-16.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-widen-16.md) | widen | — |
| [2026-11-25-build-TOOL-dTotalRecall-114-widen-17.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-widen-17.md) | widen | — |
| [2026-11-25-build-TOOL-dTotalRecall-114-widen-18.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-widen-18.md) | widen | — |
| [2026-11-25-build-TOOL-dTotalRecall-114-widen-19.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-widen-19.md) | widen | — |
| [2026-11-25-build-TOOL-dTotalRecall-114-widen-21.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-widen-21.md) | widen | — |
| [2026-11-25-build-TOOL-dTotalRecall-114-widen-22.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-widen-22.md) | widen | — |
| [2026-11-25-build-TOOL-dTotalRecall-114-widen-23.md](../build/2026-11-25-build-TOOL-dTotalRecall-114-widen-23.md) | widen | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-114-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-114-build-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-114-spec-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-114-spec-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-114-spec-writer.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-114-spec-writer.md) | log | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's first plain bar, over `e5b7ee15b`, came back red. Its record is
`memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-100-close-bar-reds.md`. This unit
repairs every red of that record but the routed-commits one, in one pass, one scope item per red. It also
repairs the two the bar's log shows and the record does not name, S23 and S27's plant (§4 "The late reds").

## 2. Scope (IN)

A `widen` below is `python tools/memory-tree/ratchet.py widen <population> --key <k> --reason <text> --unit
TOOL-dTotalRecall-114`, its key's fields joined by a TAB. The door writes one record under
`memory/builds/dTotalRecall/build/` and a row counting one, or one above a held row (DERIVED, `ratchet.py#run_widen`);
the pass then sets that row's count to the measured value (§4 "The ledgers").

- **S1** — `drift-audit records`. `tools/drift-audit/drift_signals.py#EVIDENCE_GLOBS` gains
  `":(exclude)*/record-kinds.toml"` after the unscanned-readers exclusion, with its reason (§4). No row of
  `drift-baselines` is added. Observed by AC1.
- **S2** — `marker contracts`. In `tools/memory-tree/marker-contract.test.sh` the fixture slug spells its
  case number in two letters, kept in an array the three greps read (§4). No function and no code line is
  added. Observed by AC2.
- **S3** — `remote literals (kit code names no remote)`. The five fixture lines (DERIVED, that leg) of
  `tools/memory-tree/build_records.py` and `tools/memory-tree/gen_build_index.py` ask the fixture clone its
  one remote's name (§4). Observed by AC3.
- **S4** — `govkit selfcheck`. The marker line of `tools/runlog/memory_measure.py` takes the version of
  `runlog_lib.py`'s constant, `1.19` (PINNED 2026-11-25). Observed by AC4.
- **S5** — `govkit acceptance matrix`. The held-row fixture id of `tools/playbook/render_playbook.py`
  becomes `PLAY-fxHeld-{n} F1`, a slug `instruction_units.py#HOLD_RE` admits. `documents.toml` is not
  edited: the fixture writes it. Observed by AC5.
- **S6** — `transition-audit arms`. `tools/memory-tree/backlog.py` builds its four slug patterns (DERIVED,
  `load_id_grammar().SlugPattern` sites) through a late wrapper, so importing it needs no
  `id_grammar.py` (§4). Observed by AC6.
- **S7** — `layer dependencies (the core never depends on an expansion)`. `tools/memory-tree/kit.toml` gains
  three `optional` rows and `tools/workflows/kit.toml` an `optional` list of two (DERIVED, §4 "The layer
  edges"). Each read is already optional at its site, so no code moves. Observed by AC7.
- **S8** — `core meta-check`. The `principle.p35` row of `tools/playbook/core-pending.txt` is deleted.
  Observed by AC8.
  **Readers:** by name: no name retires, the principle standing in `tools/playbook/principles.toml`; the
  pending list is spelled by `tools/playbook/core.py`
  · by value: `tools/playbook/core.py`, whose meta-check counts the pending rows and reds a stale one.
- **S9** — `docs` and `help reference pages`. `help/reference/policy.md` is rendered by
  `python tools/playbook/render_playbook.py --reference`, which anchors `asks.acceptance`,
  `builds.slug-words`, `builds.slug-style`, `builds.slug-date` and `memory.map-purpose`. No row enters
  `docs-undocumented.txt`. Observed by AC9.
- **S10** — `python reads`, the guard arm. The guards of the twelve suites (DERIVED, that leg) gain the kit
  directories they now import (§4 "The guards"), in `tools/memory-tree/kit.toml` and
  `tools/govkit/registry.toml`. `tools/gate-legs.json` is re-rendered by `python
  tools/run-gates/leg_factory.py --write` and its `pass_leg` field by `python
  tools/run-gates/pass_legs.py --apply`. Observed by AC10.
- **S11** — `python reads`, the params arm. The eight unread parameters (DERIVED, that leg) are dropped or
  renamed to open `_` (§4 "The parameters"). No row enters `unread-params`. Observed by AC11.
  **Readers:** by name: no call passes a renamed parameter by keyword; `rel` of `render_text` is passed by
  position in `tools/memory-tree/build_records.py`, where its calls change with it
  · by value: NO VALUE READERS, because the params arm's defect is that no body reads one.
- **S12** — `ratchet (never gains)`. The five `positional-refs` rows of `RUN.LANDED.bc313f97.md` (DERIVED,
  that leg) are removed and written again by one `widen` naming them: the archived run record is the one
  file the rename compare cannot follow, its source path still tracked. Observed by AC12.
  **Readers:** by name: no key retires, each row being written again; the home is read by
  `tools/playbook/positional.py` and `tools/memory-tree/ratchet.py`
  · by value: `tools/playbook/positional.py`, which compares each row's count with its measure, and
  `tools/memory-tree/ratchet.py#run_never_gains`, which reads the row's `widened:` disposition.
- **S13** — `ratchet (both ways)`. `memory/project/landed-steps.txt` gains the four rows (DERIVED, that leg)
  for `memory-tree/legacy-anchors-retag`, `memory-tree/readme-front-matter-graded`,
  `memory-tree/record-kind-journal` and `memory-tree/serves-journal-read-as-log` (§4). Observed by AC13.
- **S14** — `shell hygiene (a location probe asked from a moved directory)`. The one site (DERIVED, that leg)
  of `tools/memory-tree/check-memory-hygiene.test.sh`, the argument holding `$_gru/unattended.sh`, scrubs
  the two variables inside its own substitution (§4). Observed by AC14.
- **S15** — `shell hygiene (a fork spent on builtin work)`. Every site but the carried ones is converted
  (§4 "The conversions"), in `check-memory-hygiene.test.sh`, `gov-claim.sh`, `tools/push-main.test.sh` and
  `tools/unattended/lib-unattended.sh`. `spawn-idiom-sites` is widened for
  `tools/memory-tree/gov-claim.sh` and `var-pipe` alone. Observed by AC15.
- **S16** — `shell hygiene (a fixed-name temp renamed into place)`. `temp-name-sites` is widened for
  `tools/memory-tree/gov-claim.sh` and `fixed-temp`: the site is in the carried `health_log_sh` block,
  whose canonical file holds the same row. Observed by AC16.
- **S17** — `shell hygiene (a quoting hazard)`. `quoting-sites` is widened for
  `tools/memory-tree/gov-claim.sh` and `tab-ifs-read`: both sites are in the carried `gov_feed_sh` and
  `gov_ref_sh` blocks, whose canonical files hold the same row. Observed by AC16.
- **S18** — `portability (shell lines only shrink)`. `shell-role` is widened once for the 21 paths §4
  lists (DERIVED, that leg), and the three rows whose count fell (DERIVED, that leg) take the measured
  count in place. It runs after every other shell edit. Observed by AC17.
- **S19** — `spawn budget (forks per hot entrypoint)`. `lib-unattended.sh#load_slug_class` asks
  `id_grammar.py` itself and never the hygiene script, and finds its own directory by expansion (§4).
  `fork-ceilings` is then widened for each of `unattended-status`, `unattended-plan-handover`,
  `check-unattended` and `memory-hygiene` that still measures over its row. Observed by AC18.
- **S20** — `cleanup posture (a tree removal that swallows its error)`. The five sites (DERIVED, that leg)
  are converted (§4 "The removals"). No row enters `cleanup-sites`. Observed by AC19.
- **S21** — `kickoff-manifest ratchet`. `memory/guides/SESSION-KICKOFF.md` §B is re-read against the watched
  commits the reconcile brought, updated where stale, and its audit block re-stamped: `last-audit` at this
  pass's `HEAD`, `last-body-change` at `ffa0dcf2da2ba209a820b287660948f7d1a3988a`, the merge that moved
  the body. The stamp is in the commit that moves `tools/gate-legs.json`. Observed by AC20.
- **S22** — `memory hygiene`, check 15. `tools/memory-tree/corpus_ids.py#walk` resolves the path half of a
  `path#symbol` token, the form `memory/TEMPLATE-SPEC.md` asks for (§4). Neither citation is edited.
  Observed by AC21.
- **S23** — `memory hygiene`, check 27, a red the record does not name.
  `memory/gotchas/a-cmd-percent-var-in-a-bash-criterion-stays-literal.md` gains a line carrying
  `coexists-with` and `observed-by-claim-no-arm-discharges`, its near match, and
  `memory/gotchas/INDEX.md` is regenerated. Observed by AC22.
- **S24** — The self-test arms of `check-memory-hygiene.test.sh`: `hit` and `miss` end grep's options, the
  door-header plant's count reads 12 (PINNED 2026-11-25) and the two population literals read
  `findings causes` (§4). Observed by AC23.
- **S25** — The `row_grammar.py --selftest` arms. The generic id is read at the call and the engine-import
  scan passes over an import in a function body (§4). Observed by AC24.
- **S26** — `tags (the resolver's checks)`, ours by `TOOL-dTotalRecall-9`.
  The shape arm's byte cap, which stands, passes over a derived heading anchor and still grades an authored or
  mapped section tag, the `owned` arm passes over a namespace whose
  tags any file mints, and the retired-section arm reads document sections alone (§4 "The tag arms").
  Observed by AC25.
- **S27** — `edges (every declared edge parses, is registered and resolves)`, ours by
  `TOOL-dTotalRecall-9`. A target whose registered namespace defines no tag in the tree is
  `unarmed`, and the `leg-unregistered` plant names a namespace the registry does not hold (§4).
  Observed by AC26.

## 3. Non-goals (OUT)

- The routed-commits red: `d0e02120b`, a `Red-fix:` commit past `routed_commits.py#RED_FIX_MAX_LINES`, whose
  RANGE half reads no waiver. No commit is rewritten, split or waived here.
- The landing, which the main loop holds for the owner.
- A policy key, a catalogue bound or a ceiling of a leg moved so that a red passes. A `widen` is S12's and
  S15 to S19's alone, each for a need its reason states.
- Converting the carried `remote_ladder_sh`, `health_log_sh`, `gov_feed_sh` and `gov_ref_sh` blocks, each
  one a change in every carrier.
- Moving the shell logic of `gov-claim.sh`, or of any file S18 widens, into Python.
- Any `gov:feature` anchor: S27 makes the empty namespace read as empty.
- A kit version, which the lander's `mint` moves, and any edit of a CLOSED spec.
- The units held on owner asks.

### Edges

- **consumes-from** external — the reconcile `ffa0dcf2d`, and the build's landed units whose reds these are
- **hands-off** external — the close's second bar, the held suites and the landing, each the main loop's

## 4. Design

Every site was read at `f4b37f1ad` on 2026-11-25. The drafts `fix1.py`, `fix2.py` and `fix3.py` hold but for
S2's, re-spelled here; S5, S6, S22, S26 and S27 ran beside them in a scratch clone of that commit.

### The late reds

The record gained `tags` and `edges` when the bar's serial retries ended; the first and last rows here are not in it.

| Red | Output (PINNED 2026-11-25, `bar1.log`) | Cause |
|---|---|---|
| `memory hygiene`, check 27 | one near match, none satisfied, mode red | unit 53's gotcha names no relation to its neighbour |
| `tags` | 13262 red: 13202 shape, 41 owned, 19 retired section | unit 9's `section`, `marker` and `feature` rows |
| `edges` | 211 red: 210 `tests=feature.<name>`, one `caused-by` | unit 9 registered `feature`, which no file mints |
| `playbook render selftest` row `leg-unregistered` | the plant prints no `leg rows` line | its plant names `feature`, registered since |

The one `caused-by` red (DERIVED, that leg) names this unit's id and clears when this spec is committed.

### S1, S3, S4, S24, S25 — the drafts

S1 and S24 are `fix1.py`'s edits, S25 `fix2.py`'s with `fix3.py`'s scan, S3 and S4 `fix3.py`'s:

```python
# S1, drift_signals.py, after the unscanned-readers row
    # THE RECORD-KIND REGISTRY, for the size registries' reason (TOOL-dTotalRecall-16). Each row's purpose
    # cites the design record it was read from by FILE PATH, and a record's file name carries its unit id,
    # so a purpose names that id without claiming any of its work shipped.
    ":(exclude)*/record-kinds.toml",
# S3, build_records.py: the lease push, then the claim fixture; gen_build_index.py's set-url
run_git(a, "push", "-q", "-f", run_git(a, "remote").strip(), f"{lease}:refs/gov/leases/dTotalRecall/build")
rem = run_git(c, "remote").strip()      # then `rem` in the push of main and both ls-remote calls
run("git", "remote", "set-url", run("git", "remote", cwd=o).strip(), os.path.join(base, "missing.git")...)
# S25, row_grammar.py, in place of the module-level import and GENERIC_ID; deviation_join.py calls it too
def derive_generic_id_re():
    return re.compile(r"[A-Z][A-Z0-9]{1,9}-(?:" + read_slug_class() + r")-[0-9]+[a-z]*")
# S25, scan_engine_imports: a node inside a function or a lambda is passed over
late = {id(n) for f in ast.walk(tree) if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda))
        for n in ast.walk(f)}
```

The row scan binds the pattern once beside `derive_row_re(conf)`. The scan's arm stages a `late.py` whose one
import sits in a function and asserts it is no hit. S24 is `grep -qF -- "$1"` in both helpers, `PASS door-header
— 12 cases`, `findings causes`, `findings-2 causes`, and the paired `miss` on the same spelling.

### S2 — the fixture slug

`fix1.py` spends a fork per case and a function; the slug is spelled in place instead, one line for one line:

```bash
local l=abcdefghijklmnopqrstuvwxyz d="${5:-2026-08-09}" slug
slug="tMark${l:mark_case_n/26:1}${l:mark_case_n%26:1}"; mkdir -p "$FT/memory/builds/$slug/spec"
```

The first replaces the `local slug=` line and the second the `mkdir` line. `MARK_SLUGS` joins the
`MARK_NAMES=(); MARK_DATES=()` line, and `MARK_SLUGS+=("$slug")` the line that appends both. The greps read
`${MARK_SLUGS[i-1]}-1.md` and `${MARK_SLUGS[_f2-1]}-1.md` where they spelled `tMark$i-1.md` and
`tMark$_f2-1.md`. The last grep, for `tMark`, stands.

### S6 — the late pattern

```python
class LateSlugPattern:
    """The sibling's `SlugPattern`, itself built at first use: an import of `id_grammar` here would stop this
    module, and check 26's named refusal and dormant mode with it, in a tree whose `id_grammar.py` is absent."""

    def __init__(self, build):
        self._build, self._re = build, None

    def __getattr__(self, name):
        if self._re is None:
            self._re = load_id_grammar().SlugPattern(self._build)
        return getattr(self._re, name)
```

It sits after `load_id_grammar`, and `SLUG_RE`, the grammar's id pattern, `GRANT_ID_RE` and `VIEW_ROW_RE`
take it. In a scratch tree with no `id_grammar.py`, `transition_audit.py` then exited 0 and printed `DORMANT`
in a shards-mode tree, and exited 1 naming the file and the remedy under `--expect-builds` (PINNED
2026-11-25). The two other modules that build the pattern at import, `gen_build_index.py` and
`migrate_backlog.py`, are no reader check 26 imports.

### The layer edges

| Kit | `part` | `point` | Fallback the row states |
|---|---|---|---|
| memory-tree | `kit.toml` | `point.memory.consult` | the memory-recall row is a declaration and selects no kit |
| memory-tree | `record_find.py` | `point.memory.consult` | a question exits 2 with one refused line naming memory-recall (PINNED 2026-11-25), and a filter-only find reads no recall kit |
| memory-tree | `record_kinds.py` | `point.runtime.reading` | the Serves-alias join prints unarmed and reds nothing with no runlog kit; its fixture writes a runlog file of its own |
| review-harness | `kit.toml` | `point.runtime.reading` | the runlog row is a declaration and selects no kit |
| review-harness | `replay_scorer.py` | `point.runtime.reading` | the map-replay instance refuses unarmed, and every other instance runs with no runlog kit |

`check_layers.py#derive_edges` admits an edge whose file the source kit's rows name as `part`, so a
`requires_if` edge is admitted by the descriptor's own name. `layer.memory.recall` and `layer.observability`
already list those points under `uses`. The one memory-recall edge of `replay_scorer.py` is its `import
extract`, a module name two kits hold.

### The guards

The five directories are `{prefix}/loop/`, `{prefix}/playbook/`, `{prefix}/memory-recall/`, `{prefix}/roles/`
and `{prefix}/runlog/`; the edge that reaches them all is `tree_lib.py`'s call-time import of `tag_index`.

| Leg | Gains | Where |
|---|---|---|
| `build-index selftest`, `gotchas selftest` | the five, and `{prefix}/policy/` for its three policy files | `[gate_leg.gov]`, memory-tree |
| `corpus-ids selftest`, `row-grammar selftest`, `backlog migration selftest`, `check-arms selftest` | the five and `{prefix}/policy/` | `[gate_leg.gov]`, memory-tree |
| `routed-commits selftest` | the five | `[gate_leg.gov]`, memory-tree |
| `recall floor`, `recall floor arms`, `memory-recall kit selftest` | the five and `{prefix}/policy/`, and `{prefix}/memory-tree/`, each in place of the single files it covers | `[[exempt_leg]]`, the registry |
| `runlog selftest` | `{prefix}/memory-tree/id_grammar.py` | `[[exempt_leg]]`, the registry |
| `policy fixtures` | `{prefix}/loop/`, `{prefix}/memory-tree/`, `{prefix}/playbook/record_extract.py` | `[[exempt_leg]]`, the registry |

Only the gov form moves: an adopter's guard stays `{kit}/`. The legs run more often on gov's bar, the price of
a verdict no longer reused over an edit of what it imports.

### The parameters

| Function | Edit |
|---|---|
| `build_records.py#render_text` | `rel` dropped, and its three calls (DERIVED, `render_text(`) |
| `record_kinds.py#render_template` | `typed_kinds` dropped; no call passes it |
| `design_lib.py#extract_spec_head`, `tree_lib.py#extract_head_lines` | `arg` becomes `_arg`, the leg readers' positional second slot |
| `record_extract.py#extract_feature` | `ctx` becomes `_ctx`, the extractor contract's slot |
| `record_extract.py#extract_marker` | `ctx` and `path` become `_ctx` and `_path` |
| `memory_measure.py#read_slice_bytes` | `agent_path` becomes `_agent_path`, its callers positional |

### The conversions

| File | Site | Form |
|---|---|---|
| `check-memory-hygiene.test.sh` | two `$(date +%Y-%m-%d)` (DERIVED, that leg) | `printf -v _grd_day '%(%Y-%m-%d)T' -1` once above them, then `$_grd_day` |
| the same | `now=$(date -u +…)` | `TZ=UTC0 printf -v now '%(%Y-%m-%dT%H:%M:%SZ)T' -1` |
| the same | `m=$(printf 'gov-claim xLeased…' …)` | `printf -v m '…' …`, the format unchanged |
| the same | `_sg_n=$(printf … \| grep -c …)` | `_sg_n=$(grep -c '…' <<<"$o" \|\| true)` |
| the same, S14 | `$(git -C "$HERE" rev-parse --show-toplevel)` before `/$_gru/unattended.sh` | `$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse --show-toplevel)` |
| `gov-claim.sh` | `HERE=$(cd "$(dirname "$0")" && pwd)` | `case "$0" in */*) HERE=${0%/*} ;; *) HERE=. ;; esac`, then `HERE=$(cd "$HERE" && pwd)` |
| `push-main.test.sh` | two `re_l=$(printf …)` (DERIVED, that leg) | `printf -v re_l '…' "…" "$re_c"` |
| `lib-unattended.sh` | `here=$(dirname -- "${BASH_SOURCE[0]}")` | `case "${BASH_SOURCE[0]}" in */*) here=${BASH_SOURCE[0]%/*} ;; *) here=. ;; esac` |

The `case` is owed: a bare `${0%/*}` over a name with no slash is the name. The `TZ` prefix is owed: a bare
`printf -v` prints local time, and the first row's `date` is local, as `build_records.py` dates its record.

The read AC14 and AC15 make, written to a file under the run's scratch and run with the suite's path:

```python
# spawn_sites <shell file>: the live sites per class, as the fork arm counts them
import sys
sys.path.insert(0, 'tools/gate-lint')
import sh_hygiene as s
f = s.scan_spawn_file(open(sys.argv[1], encoding='utf-8').read())
for k in ('date-fmt', 'printf-subst', 'path-subst', 'var-pipe'):
    print(k, sum(1 for x in f[k] if x[1]))
```

At `f4b37f1ad` it printed 3, 17 and 81 of the first, second and fourth for the hygiene suite, and for the other three
files `path-subst` 1 and `var-pipe` 3, `printf-subst` 2, and `path-subst` 7 (PINNED 2026-11-25).

### S19 — the slug class

`load_slug_class` keeps its resolver call and `top` read, and its inner branch becomes one line:

```bash
re=$("$py" "$top/$d/id_grammar.py" --print slug-re "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" 2>/dev/null) || re=""
```

The hygiene script's `--print-slug-re` is an `exec` of that command over its own `git rev-parse
--show-toplevel`, so the bytes are the same; its prologue's forks, traced in a child bash by
`tools/gate-lint/fork-count.sh`, go. The comment above the branch says so. What remains, one interpreter, one
resolver and two git reads (DERIVED, that function), is the price of one owner of the grammar, as is
`memory-hygiene`'s one fork more (PINNED 2026-11-25, `bar1.log`), the one `id_grammar.py` read of
`check-memory-hygiene.sh#read_slug_ere`. Those are the reason a `widen` states.

### The removals

| File | Edit |
|---|---|
| `tools/codebase-map/selftest.py`, `deviation_join.py#set_fixture_env` | `ignore_cleanup_errors=True` dropped, as the sibling calls spell it |
| `gen_build_index.py`, the leg fixture's `finally` | `remove_tree(t)`, the block the file carries |
| `record_find.py#run_fixture` | `from deviation_join import remove_tree` in the `finally`, as `build_records.py` reaches it, then `remove_tree(top)` |
| `memory_measure.py#print_memory_fixture` | `td = tempfile.TemporaryDirectory(prefix="runlog-memory-")`, `base = pathlib.Path(td.name)`, `td.cleanup()` in the `finally`; the unused `shutil` import goes |

### S22 — the symbol half

```python
SYMBOL_LOCATOR = re.compile(r"(?<=\w)#[A-Za-z_]\w*$")   # `path#symbol`: the path half is what check 15 resolves
cited = SYMBOL_LOCATOR.sub("", LINE_LOCATOR.sub("", tok) if admitted else tok).rstrip("/")
```

A dead path with a symbol still reds, under its path. Whether the symbol exists is the positional arm's
question. No row of `corpus-path-unresolved.txt` carries a `#`, so no row goes stale.

### The tag arms

```python
def derive_tag_fault(head: str, words, cap=TAG_MAX_BYTES) -> str | None:   # its length test under `cap is not None`
# check_tag_shape, its loop unpacking `kind, blob, ex`, after `reason = derive_tag_fault(head, words)`
if reason and kind == "section" and "#" not in tag and derive_tag_fault(head, words, None) is None:
    fold = derive_heading_seg(read_text_of(con, blob, ex, kind, line)[1])
    reason = None if fold and head.startswith("section." + fold) else reason
core_ns = {r["ns"] for r in ctx["namespaces"] if kinds.get(r["layer"]) == "core" and r.get("minted") != "anywhere"}
for tag in sorted(t for t in set(base_sections or ()) - set(tip) - set(aliases) if "#" in t):            # check_retired
```

All three are in `tools/playbook/tag_index.py`, each with its docstring line. A derived
anchor is no authored tag: it is told by its heading's own fold, and an authored `[section.<seg>]` heading folds to
other bytes. Its `<seg>` is a heading's fold, as a document's `#<seg>` is, which the arm already reads past; `record show` and the
`caused-by` addresses compare the whole fold, so it is never cut. A section row with no `#` is a record heading,
which a spec's revision renames freely, and `check_retired`'s docstring states `doc.<name>#<seg>` alone. The
`feature` and `marker` rows of `tools/playbook/namespaces.toml` gain `minted = "anywhere"`, which its header
comment defines: a tag any tracked file mints, so no kit's layer owns it. Run in process over this worktree's
index, the shape arm printed no red over 120129 tags and the `owned` arm none, and over planted rows an authored section
tag and a `practice.` tag past the cap each kept their red (PINNED 2026-11-25).

### S27 — the empty namespace

```python
rc["armed"] = ti.derive_namespace_state(rc["con"], ctx)          # edge_grammar.py#read_tag_rows, after load_view
if not rows and rc["armed"].get(ns) == 0:                        # resolve_edge, before its red
    return "unarmed", f"the namespace {ns} defines no tag in this tree"
```

Run in process over this worktree, `feature.playbook` answered `unarmed`, `practice.land` `resolved` and
`practice.nowhere` `red` (PINNED 2026-11-25). Before this build `check_edges` noted a leg row's `tests` target `unarmed` while no
row registered its namespace; unit 9's `feature` row ended that mark and armed nothing in its place. It is also the
reading `gov_tag.py` already gives a citation into such a namespace. A missing tag of a namespace that
defines one still reds. `PLANTS["leg-unregistered"]` names `nowhere.x`. A resolve plant `leg-unarmed` joins it:
`build_resolve_fixture` appends a `feature` fixture row to its registry for that plant, and the leg manifest
names `feature.x`.

### The ledgers

A `widen` writes the count its door holds, so after the last shell edit the pass reads each population's seed
and sets the counts of the rows it widened. The seeds are `python tools/gate-lint/sh_hygiene.py --shell-role
--measure . :!memory/` and the same with `--quoting`, `--measure` forms both; `spawn-idiom-sites` and
`temp-name-sites` are counted by the sites the bar printed, less S15's conversions:
`var-pipe` 3 and `fixed-temp` 1 (PINNED 2026-11-25, `bar1.log`).

S18's 21 keys (DERIVED, `bar1.log`), one reason, "the slug grammar's readers, the record feed and the claim
door of this build, and the reconcile's shell":

```text
skills/session-kickoff/manifest-check.sh         tools/run-gates/post-merge.sh
tools/lib/gov-feed.sh                            tools/run-gates/run-gates.sh
tools/lib/gov-ref.sh                             tools/unattended/check-brief-recorded.sh
tools/lib/resolve-python.test.sh                 tools/unattended/check-pass-order.sh
tools/memory-tree/check-memory-hygiene.sh        tools/unattended/check-unattended.sh
tools/memory-tree/check-memory-hygiene.test.sh   tools/unattended/lib-unattended.sh
tools/memory-tree/gov-claim.sh                   tools/unattended/unattended.sh
tools/playbook/adopt-playbook.sh                 tools/unattended/unattended.test.sh
tools/push-main.sh                               tools/workflows/check-protocol-parity.test.sh
tools/push-main.test.sh                          tools/workflows/tier2-review.test.sh
tools/roles/adopt-roles.test.sh
```

The rows that fell are the three unattended suites `check-brief-recorded.test.sh`, `check-pass-order.test.sh`
and `check-unattended.test.sh`: each takes the measured count, its sha and disposition as they stand.

S13's rows are appended as `<id> TAB 1 TAB <HEAD's full sha> TAB carried:TOOL-dTotalRecall-20` (DERIVED,
`upgrade_steps.py list --ids`, the form of `govkit/inherited-red-to-verdict-blocks`'s row).

S12 deletes the five rows first, because the door counts a held key one up; its reason is "the spec run's
record retired to RUN.LANDED.bc313f97.md at the build run's preflight, its bytes unchanged".

### Order inside the pass

The Python and TOML edits, then the shell edits, then the regenerators (S9, S10, S23's index,
`python tools/codebase-map/gen_map.py --write`), then the ledgers (S12, S13, S15 to S19), then S21 in the commit
that carries `tools/gate-legs.json`.

### Inventory

Minted: `LateSlugPattern` in `backlog.py` (a class, no naming cell); `derive_generic_id_re` in
`row_grammar.py` (python-function, verb `derive`); `SYMBOL_LOCATOR` in `corpus_ids.py`; the registry key
`minted`; the plant `leg-unarmed`; the shell array `MARK_SLUGS` and variable `_grd_day`; widen records.

### Files touched (estimate)

- `tools/drift-audit/drift_signals.py`
- `tools/memory-tree/marker-contract.test.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/backlog.py`
- `tools/memory-tree/record_find.py`
- `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/gov-claim.sh`
- `tools/memory-tree/kit.toml`
- `tools/runlog/memory_measure.py`
- `tools/codebase-map/selftest.py`
- `tools/playbook/render_playbook.py`
- `tools/playbook/record_extract.py`
- `tools/playbook/tag_index.py`
- `tools/playbook/edge_grammar.py`
- `tools/playbook/gov_tag.py`
- `tools/playbook/namespaces.toml`
- `tools/playbook/adopt-playbook.sh`
- `tools/playbook/core-pending.txt`
- `tools/workflows/kit.toml`
- `tools/govkit/registry.toml`
- `tools/gate-legs.json`
- `tools/push-main.test.sh`
- `tools/unattended/lib-unattended.sh`
- `help/reference/policy.md`
- `memory/project/positional-refs.txt`
- `memory/project/landed-steps.txt`
- `memory/project/spawn-idiom-sites.txt`
- `memory/project/temp-name-sites.txt`
- `memory/project/quoting-sites.txt`
- `memory/project/shell-role.txt`
- `memory/project/fork-ceilings.txt`
- `memory/gotchas/a-cmd-percent-var-in-a-bash-criterion-stays-literal.md`
- `memory/gotchas/INDEX.md`
- `memory/guides/SESSION-KICKOFF.md` (a watched path moves: its `last-audit` re-stamp, S21)
- `memory/map/generated/`
- `memory/builds/dTotalRecall/build/` (the widen records and this unit's ledger)

### Alternatives rejected

- **`SlugPattern` moved to `tree_lib.py` (S6, S25).** It would end both reds with one class, and make
  `id_grammar.py`, which imports no sibling, need one in every install that carries it alone.
- **The section tag cut to the shape arm's cap or dropped (S26).** A cut renames the address a `Caused-by` or `record show`
  already spells in full; a drop loses the heading.
- **The two citations reworded (S22).** The next `path#symbol` in a present-tense record reds again.
- **`gov:feature` anchors for the 210 targets of S27 (PINNED 2026-11-25, `bar1.log`).** A dossier population,
  no repair.
- **Converting the carried blocks of `gov-claim.sh`.** Each is one edit in the canonical file and every carrier.

## 5. Production-readiness checklist

- security — no new write surface; the ledgers' door writes what it already writes.
- perf / scale — twelve suites run on more edits (DERIVED, §4 "The guards"); one hygiene prologue fewer per
  unattended verb; the `tags` leg prints 13262 lines fewer (PINNED 2026-11-25, `bar1.log`).
- error / empty / loading states — an empty namespace is `unarmed`, never a red and never `resolved`.
- observability — every `widen` leaves a record with its reason; the edges line counts the unarmed targets.
- risks — a widened row hides a later regrowth up to its count, so each takes the measured count and no more.
  S26 stops grading the length of a derived heading anchor alone, stated in the docstring.
- testing — AC1 to AC26 by the pass; the arms of §7 by the main loop at the close.
- migration — none; an adopter's guards and namespaces are its own.
- user docs — `help/reference/policy.md`, S9.

## 6. Acceptance criteria

"The bar" is the main loop's second plain bar. Each criterion is the pass's own probe, run from the repository
root with `PYTHONPATH` unset; none runs a leg.

- **AC1** — When `grep -c 'exclude)\*/record-kinds.toml' tools/drift-audit/drift_signals.py` runs, it prints 1,
  and `git grep -l "PLAY-dClosedLoop-1\b" -- tools skills` read through that list names no file the exclusion
  leaves in the evidence.
  Red when: `record-kinds.toml` is still read as evidence, or another evidence file names the id.
- **AC2** — When `grep -cE 'tMark\$(i|_f2|mark_case_n)' tools/memory-tree/marker-contract.test.sh` runs, it
  prints 0, and a bash probe of the two lines of §4 over cases 1 to 60 (PINNED 2026-11-25, above the suite's
  count) prints 60 distinct slugs, each matching `^[a-z][A-Za-z]{2,}$`.
  Red when: a slug carries a digit or two cases share one.
- **AC3** — When `git grep -nE '"origin"' -- tools/memory-tree/build_records.py tools/memory-tree/gen_build_index.py`
  runs, it lists none of the push, ls-remote or set-url fixture lines, and `python build_records.py --fixture
  --plant ask-door` and `--plant door-header` from `tools/memory-tree/` each print their `PASS` line.
  Red when: a fixture names the remote by literal, or the plant cannot push.
- **AC4** — When `grep -rhoE 'gov:kit runlog@[0-9.]+' tools/runlog/memory_measure.py` runs, it prints the version
  `grep -E '^KIT_RUNLOG_VERSION' tools/runlog/runlog_lib.py` holds.
  Red when: the marker reads main's older version.
- **AC5** — When `python -c "import sys; sys.path.insert(0, 'tools/playbook'); import instruction_units as u; print(bool(u.HOLD_RE.fullmatch('PLAY-fxHeld-0 F1')), bool(u.HOLD_RE.fullmatch('PLAY-fx-0 F1')))"`
  runs, it prints `True False`, and `grep -c "PLAY-fxHeld-{n} F1" tools/playbook/render_playbook.py` prints 1.
  Red when: the fixture row is still refused before the map's cap is read.
- **AC6** — When a scratch repository holding a copy of `tools/memory-tree/` with no `id_grammar.py` runs
  `python tools/memory-tree/transition_audit.py` under `BACKLOG_MODE="shards"`, it exits 0 printing `DORMANT`, and
  under `BACKLOG_MODE="builds"` with `--expect-builds` it exits 1 naming `id_grammar.py` and `reinstall the
  memory-tree kit`, with no `Traceback`.
  Red when: the import of `backlog.py` needs the module. At HEAD both print a traceback.
  fixture: built in the run's scratch by the pass, its one commit and one merge its own.
- **AC7** — When `python tools/playbook/check_layers.py --list` runs, no `edge` line of `memory-tree` or
  `review-harness` ends `red`, and its count line reads `0 red`.
  Red when: an edge has no row, or a row names a point no core layer declares.
- **AC8** — When `grep -c 'principle.p35' tools/playbook/core-pending.txt` runs, it prints 0.
  Red when: the stale row stands.
- **AC9** — When `grep -cE 'asks\.acceptance|builds\.slug-(words|style|date)|memory\.map-purpose' help/reference/policy.md`
  runs, it prints at least 5 (DERIVED, the five keys of S9), and a second run of S9's render leaves the page as
  it stands by `git diff --stat`.
  Red when: the page is edited by hand or a key is anchored nowhere.
- **AC10** — When `python tools/run-gates/py_reads.py --guards "<leg>"` runs for each of the twelve legs of §4
  (DERIVED, its table), it prints no gap, and a second `python tools/run-gates/leg_factory.py --write` leaves
  `tools/gate-legs.json` as it stands.
  Red when: an imported module sits outside its leg's guard, or the manifest is edited by hand.
- **AC11** — When `python tools/run-gates/py_reads.py --list-params` runs, it prints none of the eight keys of
  S11 (DERIVED, §4 "The parameters") and no key `memory/project/unread-params.txt` lacks.
  Red when: a parameter is read nowhere, or a row tolerates it.
- **AC12** — When `grep -c 'RUN.LANDED.bc313f97.md' memory/project/positional-refs.txt` runs, it prints 5 (DERIVED,
  S12), each row counting 1 and ending `widened:<stem>` of one record whose Keys name all five.
  Red when: a row's count doubles, or the record names fewer keys.
- **AC13** — When `python tools/govkit/upgrade_steps.py list --ids` runs, every id it prints is a first field of
  `memory/project/landed-steps.txt`, and `git diff` of that file shows four added lines (DERIVED, S13) and none removed.
  Red when: a declared step has no row or a landed row moves.
- **AC14** — When §4's `spawn_sites` read runs over the hygiene suite, it prints `date-fmt` 0, `printf-subst` 16 and
  `var-pipe` 80 (DERIVED, the file's rows), and
  `grep -c '$(git -C "$HERE" rev-parse --show-toplevel)/$_gru' tools/memory-tree/check-memory-hygiene.test.sh` prints 0.
  Red when: a converted site is left, or the probe is asked bare.
- **AC15** — When §4's `spawn_sites` read runs over `tools/memory-tree/gov-claim.sh`, the push-main suite and
  `tools/unattended/lib-unattended.sh`, it prints `path-subst` 0 and `var-pipe` 3 for the first, `printf-subst` 0 for
  the second and `path-subst` 6 for the third (DERIVED, the rows and §4), and
  `memory/project/spawn-idiom-sites.txt` holds `gov-claim.sh` under `var-pipe` at 3 alone (DERIVED, §4).
  Red when: a site of `gov-claim.sh`'s own code is widened, or a converted file rises.
- **AC16** — When `grep -h 'memory-tree/gov-claim.sh' memory/project/temp-name-sites.txt memory/project/quoting-sites.txt`
  runs, it prints one `fixed-temp` row at 1 and one `tab-ifs-read` row at 2 (DERIVED, `bar1.log`), each `widened:`, and
  `cmp` of the carried blocks to their canonical files finds no difference.
  Red when: a carried block is edited, or a row counts more than its sites.
- **AC17** — When `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'` runs, each of its keys
  is a row of `memory/project/shell-role.txt` at the same count, and the record of S18 names 21 keys (DERIVED, §4).
  Red when: a row stands under or over its measure.
- **AC18** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only <id>` runs for each
  id of S19, it prints `ok`, its measured count equal to the row's ceiling or under it, and the ledger sets each count
  beside the one `bar1.log` printed.
  Red when: the hygiene script is still spawned, or a row rises past its count.
  permission: where the guard refuses this to the builder, the main loop runs it and hands the counts in a brief.
  figure: 57, 221, 809 and 193 are PINNED 2026-11-25, `bar1.log`; the pass's are DERIVED.
- **AC19** — When `python tools/gate-lint/encoding_posture.py --cleanup --measure . tools` runs, it prints no key of
  the five files of §4 "The removals", and `python record_find.py --fixture --plant missing-section` from
  `tools/memory-tree/` prints its `exit` line and leaves no `rf-` directory in the temp folder that was not there before.
  Red when: a removal swallows its error, or a fixture tree outlives the plant.
- **AC20** — When `grep -E '^(last-audit|last-body-change):' memory/guides/SESSION-KICKOFF.md` runs after the pass, the
  first names this pass's base sha and the second `ffa0dcf2da2ba209a820b287660948f7d1a3988a`;
  `git rev-list --count --no-merges ffa0dcf2d..HEAD -- <the watch list>` prints under 10 (DERIVED, check 9's bound), and
  the ledger names each watched commit of the reconcile and what §B said of it.
  Red when: the stamp moves with no re-read, or names a commit that is no ancestor.
- **AC21** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import corpus_ids as c; w = c.walk('.', c.load_conf('.')); print(sorted(k for k in w['dead'] if '#' in k[1] or k[1].endswith(('gov-ref.sh', 'id_grammar.py'))))"`
  runs, it prints `[]`, and over a scratch tree whose `memory/README.md` cites a missing file with a `#symbol` it
  prints that file's path.
  Red when: a live `path#symbol` citation reads dead, or a dead one reads live.
- **AC22** — When `python tools/memory-tree/row_grammar.py --check-relations 3d6c1702a` runs after the commit, it prints
  no `check 27:` line, its summary one match and one satisfied (DERIVED, that command).
  Red when: the gotcha names no relation to its near match.
- **AC23** — When `grep -c 'grep -qF -- "$1"' tools/memory-tree/check-memory-hygiene.test.sh` runs, it prints 2 (DERIVED,
  `hit` and `miss`), and `python build_records.py --fixture --plant door-header`, `python record_causes.py --fixture
  --plant legacy` and the same with `--plant none`, from `tools/memory-tree/`, print the literals the three arms now
  hold, the last without `findings causes`.
  Red when: a literal names a line the plant does not print.
- **AC24** — When `python tools/memory-tree/row_grammar.py --selftest` runs, it exits 0 with no `FAIL` line, and
  `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import row_grammar as r; print(r.scan_engine_imports('tools/memory-tree')[0])"`
  prints `[]`.
  Red when: the module imports `id_grammar` at import, or the scan lists a call-time import.
- **AC25** — When a probe script loads the worktree's tag index and calls `tag_index.check_tag_shape` and
  `tag_index.check_owned` over it, each prints no red; a `practice.` row of 65 bytes (DERIVED, the cap plus one)
  and an authored `[section.<seg>]` heading of the same length, planted, each still print one `shape` red, and `check_retired` over a base holding
  `section.gone` and `doc.x#gone` reds the second alone.
  Red when: a record heading reds, a marker in a non-core kit reds, or a document section's retirement is missed.
  cost: one index read, minutes on a cold cache.
- **AC26** — When `python tools/playbook/edge_grammar.py --fixture --plant leg-unregistered` runs, it prints the
  `edges: leg rows · 1 tests target(s)` line and no `is not registered`; `--plant leg-unarmed` prints `edges: green`
  and no `resolves to no row`; and a probe calling `edge_grammar.resolve_edge` over this tree answers `unarmed` for
  `feature.playbook` and `red` for `practice.nowhere`.
  Red when: an empty namespace reds, or a missing tag of a filled one goes unarmed.

## 7. Gates

`drift-audit records` · `marker contracts` · `remote literals (kit code names no remote)` · `govkit selfcheck` · `govkit acceptance matrix` · `transition-audit arms` · `layer dependencies (the core never depends on an expansion)` · `core meta-check` · `docs` · `help reference pages` · `python reads (a name never bound, an import outside its guard)` · `ratchet (never gains)` · `ratchet (both ways)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `shell hygiene (a quoting hazard)` · `portability (shell lines only shrink)` · `spawn budget (forks per hot entrypoint)` · `cleanup posture (a tree removal that swallows its error)` · `kickoff-manifest ratchet` · `memory hygiene` · `memory-hygiene self-test` · `row-grammar selftest` · `tags (the resolver's checks)` · `edges (every declared edge parses, is registered and resolves)` · `gate-leg conformance` · `positional (the citation check alone)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `routed-commits selftest` · `playbook render selftest` · `recall floor` · `recall floor arms` · `memory-recall kit selftest` · `govkit selftest` · `govkit refusal join` · `run-gates gov canary` · `run-gates canary` · `measure-legs selftest` · `drift-audit selftest` · `runlog selftest` · `run-gates run-log line` · `pre-push run-log line` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `policy fixtures`

New arm: tools/memory-tree/row_grammar.py · covers AC24 · a staged `late.py` whose import is in a function body, red on `late` cut from the scan · none
New arm: tools/playbook/adopt-playbook.sh · covers AC25 · the `memory-records` plant's legacy spec gains a heading whose tag is over the cap, the row's section count with it, red on the cap read for a `section` row · none
New arm: tools/playbook/adopt-playbook.sh · covers AC26 · rows for `leg-unarmed`, red on the `armed` test cut from `resolve_edge`; the `leg-unregistered` rows stand over the re-spelled plant · none

## 8. Open questions

- **F1 — Which binding line does a unit the close's bar added carry?** The carries join reds a chain spec
  carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming `PLAY-dClosedLoop-2`, the
  ruling that a chain run carries the units it adds, as `TOOL-dTotalRecall-92` §8 F1; (b) a part of another
  unit's clause, which the parts join reds. Veto 1 discards (b). RESOLVED (agent, 2026-11-25, delegated): (a),
  the one survivor. widens: none · relaxes: none
- **F2 — Does this unit take the reds the record does not name?** Options: (a) yes, S23 and S27's plant; (b) no,
  and `memory hygiene` and the held `playbook render selftest` come back red. The goal
  is one pass that repairs the close's reds, which (b) leaves standing; veto 1 discards it. RESOLVED (agent,
  2026-11-25, delegated): (a). widens: none · relaxes: none
- **F3 — May a section tag pass the 64-byte cap (S26)?** Options: (a) the cap passes over a derived anchor alone,
  as it already passes over a document's `#<seg>`; (b) the tag is cut to the cap; (c) an over-long heading defines
  no tag; (d) `TAG_MAX_BYTES` is raised, a bound moved so that a red passes, which the brief forbids. (b) renames addresses in use and (c) loses them, each against `TOOL-dTotalRecall-9` S1's whole fold.
  RESOLVED (agent, 2026-11-25, delegated): (a), the smallest edit that keeps every address. widens: none ·
  relaxes: none
- **F4 — Is the late pattern of S6 one class in `tree_lib.py` or a wrapper in `backlog.py`?** Options and reasons
  are §4 "Alternatives rejected". RESOLVED (agent, 2026-11-25, delegated): the wrapper, which changes no
  import of `id_grammar.py`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the close's first bar and its record.

## 10. Reuse audit

The seams, each read at `f4b37f1ad`: `tools/memory-tree/ratchet.py#run_widen` and the registered ledgers for
every count; `tools/memory-tree/id_grammar.py#SlugPattern`, which `LateSlugPattern` builds late;
`tools/memory-tree/tree_lib.py#read_slug_class` for S25; `tools/memory-tree/deviation_join.py#remove_tree`;
`tools/playbook/tag_index.py#derive_namespace_state`, which `gov_tag.py` already reads as `armed`; the
`optional` rows and gov guards of the kit descriptors; and the two `case "$0"` and `TZ=UTC0` forms of
`TOOL-aNimbleMend-27`, an earlier close's batch of the same reds.
`python tools/codebase-map/reuse_lookup.py "a pattern bound at first use without importing its module at import time"`
ranked `SlugPattern` first. `tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder walks of
`tools/memory-tree/record_causes.py#check_cause_writers` and `tools/memory-tree/record_kinds.py#check_alias_compares`
are no seam here: no item reads a marker or a build folder.

Recall terms used: `python tools/memory-recall/query.py "how does a red found at a build's close get repaired in one unit, through the ledger widen route and the guards" --terms "close bar red widen ratchet fork-ceilings shell-role guard py_reads optional row layers landed-steps tag shape edges unarmed"`

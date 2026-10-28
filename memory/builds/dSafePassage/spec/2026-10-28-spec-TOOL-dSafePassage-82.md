# TOOL-dSafePassage-82 — the six product lint legs this build's diff turned red, each cleared by the remedy its own message names

**Status:** DEFERRED · rev-4 · 2026-10-28 · node a · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14 · ratified 2026-10-28

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-prompt-TOOL-dSafePassage-82-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-82-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-82-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-82-spec-brief.md) | research | TOOL-dSafePassage-83 |
| [2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-83 |

<!-- /gen:spec-records -->

## 1. Goal

A discovery bar over a frozen clone of `83817478f`, its `origin/HEAD` at main `1a61f21a`, went red
on six product lint legs whose every finding is a line this build added: `encoding posture`,
`install-prefix`, `remote literals`, `harness arms`, `spawn budget` and `shell hygiene (a fork spent
on builtin work)`. This unit applies, at each finding, the remedy that leg's own message names, so
each leg passes at the build's head with no waiver row, no widened exemption and no ceiling the leg
forbids raising. The spawn budget's five ceilings are the owner's to move (§8 F2), so this pass
leaves them untouched and that leg stays red until the owner rules.

## 2. Scope (IN)

Every site below is PINNED at `83817478f`. The builder re-locates each by content, because units
TOOL-dSafePassage-72 to -78 and -80 build before this one and move lines (§4 "Rollout"). A site of
the same class one of them adds in a file listed here is in scope by the same remedy, the class and
not the instance.

- **S1 — encoding posture.** Each of the seven `subprocess.run(..., text=True)` sites with no
  `encoding=` passes `encoding="utf-8"`: `tools/govkit/shims.py:433`,
  `tools/govkit/upgrade_steps.py:2896`, `:2898`, `:2916`, `:2918`, and `tools/lib/python_floor.py:152`,
  `:160`. In `tools/govkit/govkit.py` the one site this build added, the gov-first `rev-parse` at
  `:9427` (commit `45bfa495c`, TOOL-dSafePassage-8), passes it too, so the file measures the 35 its
  row in `memory/project/encoding-posture-sites.txt:23` declares and the row does not move.
  Observed by AC1 and AC11.
- **S2 — remote literals.** No line of the gate's population names a remote by literal; each fixture
  that needs a remote names one of its own through a variable, the remedy the gate's header names for
  a fixture (`tools/check-remote-literals.sh:14-15`). The four sites:
  - `tools/govkit/upgrade_steps.py:2688`, the `fetch.py` step program, takes the remote's name as an
    argument instead of spelling one;
  - `:2940` and `:3054`, the `local-url-userinfo` and `ext-transport` plants, write their remote
    under a fixture-chosen name held in one module constant whose value is not the default remote's
    name, and the refusal text they expect names `remote.<that name>.url`;
  - `tools/govkit/upgrade_walk.py:177` clones with `--origin` set to a name held in one constant, and its
    `remote` call passes that constant.
  `tools/govkit/selftest.py:3560` expects the renamed key; the selftest is outside the gate's
  population and changes only because its expectation follows the plant. Observed by AC2, AC3 and
  AC11.
- **S3 — install-prefix.** None of the 129 lines the leg named spells a kit path, each rewritten by
  the rule of its shape in §4 "The install-prefix shapes": a fixture's scratch layout assembled from
  named values; a sibling kit gov carries routed through `resolve_kit_dir`; declaration data spelled
  with the drained `{prefix}/` token and resolved where it is read; prose in a manifest field spelled
  `<prefix>/`. The floor row's three argvs at `tools/govkit/steps.toml:34-36` name a new program
  in gov's own govkit steps directory, beside the schema row's program. It loads the step module
  by path as `tools/govkit/steps/fanout_cap.py`'s `load_steps` does, finds
  `tools/lib/python-floor.sh` through that module's `resolve_kit_dir`, and runs it under its
  `resolve_bash`; it imports nothing from govkit (§8 F1). Observed by AC4, AC5, AC6 and AC11.
- **S4 — harness arms.** Each of the eight unarmed exit sites is armed or pinned, by the leg's own
  two remedies:
  - `tools/push-main.sh:1319` and `:1325` are armed: arm 39 of `tools/push-main.test.sh` and arm 40
    assert each refusal's full message, which each already drives and asserts only in part;
  - `tools/push-main.sh:1333` and `:1343` gain pin rows in `memory/project/unarmed-branches.txt`, each
    reason naming the precondition no arm stages, as the sibling mint and regeneration commit
    refusals are pinned there (rows 109 and 110);
  - `tools/lib/python-floor.sh:29`, `:30`, `:34` and `:42` gain pin rows whose reasons say no
    sibling suite exists and name what drives each site: `tools/lib/resolve-python.test.sh:193`
    drives the preflight refusal, its arm 1e drives `down`, and `.github/workflows/remote-ci.yml:80`
    runs `floor`.
  Observed by AC7 and AC11.
- **S5 — spawn budget.** NOT BUILT by this pass. `memory/project/fork-ceilings.txt` is left
  untouched: its five red rows, `run-gates-1leg`, `run-gates-2leg`, `memory-hygiene`,
  `manifest-check` and `check-wiring`, keep their ceilings, and the leg stays red until the owner
  rules on §8 F2. The pass builds S1 to S4 and S6. The fork is attributed in §4 "The spawn budget".
  Observed by AC9 and AC11, which name that state.
- **S6 — shell hygiene.** Each risen count falls back to its registry row by converting the sites
  this build added to the no-fork form the lint names, and the one fallen count lowers its row:
  - `tools/lib/resolve-python.test.sh:264` counts the output's non-empty lines with no pipe;
  - `tools/push-main.sh:1015` indents the refusal's lines with no `sed`;
  - `tools/push-main.test.sh` resolves its interpreter once for arms 33, 34, 37 and 40, so one
    `$(resolve_python …)` site remains where four stand; reads `cas37-moved` with `$(<file)`; and
    counts the skip line of arms 25 and 35 with no pipe;
  - the `tools/memory-tree/merge-rows.test.sh` `var-pipe` row of
    `memory/project/spawn-idiom-sites.txt:169` goes from 43 to 42, the count left once
    TOOL-dSafePassage-11 took the suite's PEP 701 check out.
  Observed by AC8, AC10 and AC11.
- **S7 — the manifest re-stamp.** `tools/gate-legs.json` is a `watch:` path of
  `memory/guides/SESSION-KICKOFF.md`, and `.githooks/pre-commit` runs the ratchet's staged leg, which
  refuses a commit staging a watched path with no re-stamp. The commit that stages `gate-legs.json`
  therefore stages the manifest too: its §B claims that `gate-legs.json` feeds are re-read, the
  Gate commands block's single-sourcing line among them, and `last-audit` is re-stamped to the
  pass's parent with an advanced datetime. `last-body-change` does not move; that advance is
  TOOL-dSafePassage-83's. Observed by AC12.
- **S8 — the map.** The floor program mints `main`, a name `memory/map/generated/symbols.json`
  maps, so the pass commit carries `python tools/codebase-map/gen_map.py --write`'s regeneration of
  `memory/map/generated/`, as TOOL-dSafePassage-81 does for its renames. Observed by AC13.

## 3. Non-goals (OUT)

- The legs TOOL-dSafePassage-80 owns, `leg ceilings clear their evidenced maximum` and
  `every held leg is budgeted, every budget row resolves`, and those TOOL-dSafePassage-81 owns,
  `lexicon naming predicates` and `lexicon wiring`.
- The records legs, `memory hygiene` and the manifest ratchet's check 9, which TOOL-dSafePassage-83
  owns, and the two timed-out legs, `routed commits name a specced unit` and `spec tokens`, whose
  ceilings are TOOL-dSafePassage-80's. S7's re-stamp is the one manifest edit this unit makes.
- Draining any registry row this build did not move: the 35 carried `govkit.py` encoding sites, the
  carried spawn-idiom rows, and every pin already in `memory/project/unarmed-branches.txt`.
- Any change to a gate's predicate, its drained-token set or its population. Each leg stays as it is
  and the tree moves to meet it.
- A new suite for `tools/lib/python-floor.sh`, §4 "Alternatives rejected".
- Any change to what a fixture, a plant or a step observes. Every rewrite here keeps its arm's
  verdict and its printed text, except the remote name a plant writes and the key its refusal names.

### Edges

- **consumes-from** external — the owner's pick on §8 F2. Without it the spawn budget stays red, the
  state AC9 and AC11 name.
- **hands-off** external — the pinned exit sites of S4, each armable only by a stage nobody has
  built, left for a later unit that builds it.

TOOL-dSafePassage-8, -11, -13 and -26, which added the sites S1 to S6 change, are CLOSED and read,
so they are named here rather than joined.

## 4. Design

### The reds, reproduced

The leg output below is the discovery bar's, `C:/Users/DAILY-~1/AppData/Local/Temp/dsp-bar-83817478f.log`,
over the frozen clone. This role may not run these six legs (scratch-guard row G1, `tools/hooks/README.md:518`),
so each was re-derived in a `git clone --shared` of `83817478f` under the temp root, `origin/HEAD` set to
`origin/main`, by a probe of this spec's own (below) or by reading the source and its history.

- **encoding posture** — `encoding-posture: 4 finding(s) over 116 tracked *.py`, naming
  `tools/govkit/govkit.py: the registry declares 35 [subprocess] site(s) and the scan measures 36`
  and the seven unregistered sites of S1. `enc_probe.py` printed `govkit.py 36`, `shims.py 1`,
  `upgrade_steps.py 4` and `python_floor.py 2` at `83817478f`, and `govkit.py 35` at the build base
  `60d90cb7`. A source-text diff of the two populations named one added site, the `rev-parse` call
  `git log -S` attributes to `45bfa495c`.
- **install-prefix** — `install-prefix: RED — 449 tracked file(s) graded, 7 render(s) left out as
  matching their template, 136 kit-path spelling(s) on 129 line(s)`, a pure ban with no waiver
  (`tools/check-install-prefix.sh:24-28`). All 15 files are this build's: nine did not exist at
  `60d90cb7` or on main, and `git blame` gives each line in the other six to a build commit
  (`dfcef45a7`, `45bfa495c`, `f8f919882`, `7c51ef25f`). The brief named two of the 15 files.
- **remote literals** — `remote-literals: FAILED — 4 line(s) in 183 file(s) name a remote by literal`,
  the four lines of S2, blamed to `db9060e83`, `f8f919882` and `7c51ef25f`.
- **harness arms** — eight `HYGIENE check-arms:` lines, the four `python-floor.sh` sites ending
  `tools/lib/python-floor.test.sh is missing, so nothing can arm it`, and the four `push-main.sh`
  sites. `tools/push-main.test.sh:1334` asserts `*"gov first could not snapshot the untracked files"*`
  and `:1566` asserts `*"did not hold on gov first"*`, each a slice shorter than its site's signature,
  which `check-arms.py:204-216` takes as the whole literal message.
- **spawn budget** — `fork-count: 2 passed · 5 red`: `run-gates-1leg · measured 56 · ceiling 55`,
  `run-gates-2leg` 58 over 57, `memory-hygiene` 190 over 189, `manifest-check` 76 over 74 and
  `check-wiring` 45 over 44. The brief named the first.
- **shell hygiene** — `sh-hygiene: 6 finding(s)`, the six count lines S6 answers.

### The spawn budget

`fork-count.sh` counts the distinct `BASHPID`s that trace a command (`tools/gate-lint/fork-count.sh:11-16`).
Commit `ed135af16` (TOOL-dSafePassage-11) replaced the canonical resolver's probe
`if "$_rp_c" -c "import sys" >/dev/null 2>&1` with `_rp_out=$("$_rp_c" -I -c '…')`
(`tools/lib/resolve-python.sh`, carried inline into every marked copy). The old form forks for python
and traces in the parent, so the counter never saw it. The new form traces the command inside the
substitution's child, so the counter sees one fork per candidate probed. The number of processes is
the same in both forms. `git log -S'_rp_out=$("$_rp_c"'` names `ed135af16` alone in each of the
four entrypoints: `run-gates.sh:157`, `check-memory-hygiene.sh:479`, `manifest-check.sh:772` and
`check-wiring.sh:471`. Each red row is one `$(resolve_python)` call per counted run. `manifest-check`
is +2 because its fixture run calls the resolver twice (`manifest-check.sh:976`, `:1442`), and the
bar's site list shows `2 manifest-check.sh:772`. `memory/project/fork-ceilings.txt` did not move in
this build. The build edited no gate runner by hand. It edited all four by the resolver's
inline-parity rule.

### The install-prefix shapes

The leg's message names three remedies: derive the path from the file's own location, route a
sibling kit through `resolve_kit_dir`, or spell it through a drained token (`{prefix}/`, `{kit}/`,
`{{TOOL_ROOT}}`, `<prefix>/`, `<tool-root>/`, `check-install-prefix.sh:52-53`). Each line takes the
one its shape admits.

| Shape | Lines at `83817478f` | Remedy |
|---|---|---|
| A fixture laying out its own scratch gov or target | `upgrade_steps.py` 2747-2751, 2818, 3169, 3317, 3600, 3840, 4145, 4162-4168, 4220, 4281, 4284, 4355, 4750, 4762, 4790, 4856, 4869 · `shims.py` all 12 · `selftest.py` 4416, 4418 · `docs_leg.py` 553-556, 563, 598, 638 · `fixture_target.py` 96, 97, 105 · `push-main.test.sh` 1355 | The fixture's prefix and each kit directory it lays out are named once, in a module constant or a suite variable, and every path is joined from those names. That is the form the gate's header gives a fixture laid out at a foreign prefix (`check-install-prefix.sh:59-60`). A scratch directory whose name is only a kit's homonym, `scratch / "hooks"` at `upgrade_steps.py:1368` and `target / "lib"` at `:3169` and `:3317`, takes a name that is no kit's instead. |
| A sibling kit gov carries, read at run time | `docs_leg.py:384` · `upgrade_walk.py:199`, `:495` · `push-main.sh:997` | `gk.resolve_kit_dir(<home>, <anchor>, <here>)` (`tools/govkit/govkit.py:235`), as `govkit.py:283` finds the policy kit. In `push-main.sh` the check reuses the kit and anchor `run_gov_first` already hands `resolve_lander_kit` (`:995`), so the branch tests what the resolver was asked for. |
| Declaration data a reader resolves | `usage.toml` all 59 · `docs_leg.py:501`, `:507` · `tools/govkit/fixtures/release-0/arms.toml:42`, `:59` · `plants.toml` 21, 29, 104, 112, 124 · `deploy.toml` 41, 43, 47, 48 | Spelled `{prefix}/…`, and resolved by `gk.resolve_prefix_token(value, gk.derive_tool_root(root))` (`govkit.py:218`, `:192`) where the file is read and before any join or fingerprint. `docs_leg.read_usage_rows` resolves each `[[usage]]` `id` and `entry`, and stops prepending `"{prefix}/" +` to a class's `rows` (`docs_leg.py:206`), since the value now carries the token. `check_page_command` resolves through the same call where it now substitutes the literal `"tools/"` (`:306`). `upgrade_walk.py` resolves the three fixture files' fields against the pinned clone's tool root. Every resolved id, entry, path and text is byte-identical to today's, so no help page's usage anchor or fingerprint moves. |
| Prose in a manifest field | `gate-legs.json:1480`, the `upgrade-walk` row's `reads.history` | `<prefix>/govkit`. |
| A suite assertion on printed paths | `resolve-python.test.sh:264` | It matches each printed statement by a path assembled from the suite's own variables. The same line is S6's `var-pipe` site, and one edit answers both. |
| A step row's program | `steps.toml:34-36` | The three argvs name a new program in gov's govkit steps directory, python_floor.py. It loads `tools/govkit/upgrade_steps.py` by path as `fanout_cap.py`'s `load_steps` does, because the runner's `-I` drops the step's directory from `sys.path`, then calls that module's `resolve_kit_dir("lib", "python-floor.sh", …)` (`upgrade_steps.py:293`) and runs the script under its `resolve_bash()` (`:347`) with its own arguments, passing the exit through. It imports nothing from govkit, the rule `tools/govkit/steps/receipt_schema_4.py:22` states (§8 F1). |

### The probes

Each runs from the repository root, from a file written to the scratchpad. None imports a gate.

`enc_probe.py`, for AC1, lists every `subprocess.<run|Popen|call|check_call|check_output>` call in
text mode with no `encoding=`:

```python
import ast, pathlib, sys
FNS = {"run", "Popen", "call", "check_call", "check_output"}
for rel in sys.argv[1:]:
    src = pathlib.Path(rel).read_text(encoding="utf-8")
    hits = []
    for n in ast.walk(ast.parse(src)):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in FNS
                and isinstance(n.func.value, ast.Name) and n.func.value.id == "subprocess"):
            kw = {k.arg: k.value for k in n.keywords if k.arg}
            if (any(isinstance(kw.get(f), ast.Constant) and kw[f].value is True
                    for f in ("text", "universal_newlines")) and "encoding" not in kw):
                hits.append(n.lineno)
    print(rel, len(hits))
```

`usage_probe.py`, for AC5, resolves every string value of `tools/govkit/usage.toml` at HEAD and
compares it with the same field at `83817478f`:

```python
import subprocess, sys, tomllib
sys.path.insert(0, "tools/govkit")
import govkit as gk
old = tomllib.loads(subprocess.run(["git", "show", "83817478f:tools/govkit/usage.toml"], capture_output=True,
                                   text=True, encoding="utf-8", check=True).stdout)
new = tomllib.loads(open("tools/govkit/usage.toml", encoding="utf-8").read())
tr = gk.derive_tool_root(".")
fix = lambda v: gk.resolve_prefix_token(v, tr) if isinstance(v, str) else v
moved = [(t, i, k) for t in ("class", "usage") for i, (a, b) in enumerate(zip(old[t], new[t]))
         for k in a if a[k] != fix(b.get(k)) and not (t == "class" and k == "rows" and fix(b[k]) == f"{tr}/" + a[k])]
lit = sum(("tools/" in ln or '"govkit/' in ln) and not ln.lstrip().startswith("#")
          for ln in open("tools/govkit/usage.toml", encoding="utf-8"))
print("rows", len(old["class"]) + len(old["usage"]), len(new["class"]) + len(new["usage"]), "moved", moved, "literal", lit)
```

`fnsubst_probe.py`, for AC8, lists each `$(name` whose name a function in the file defines:

```python
import collections, re, sys
text = open(sys.argv[1], encoding="utf-8").read()
defs = set(re.findall(r"(?m)^[ \t]*([A-Za-z_][A-Za-z0-9_]*)\(\)[ \t]*\{", text))
c = collections.Counter(m.group(1) for line in text.split("\n")
                        for m in re.finditer(r"\$\(([A-Za-z_][A-Za-z0-9_]*)\b", line.split(" #", 1)[0])
                        if m.group(1) in defs)
print(dict(c))
```

Measured at `83817478f` in the clone: `enc_probe.py` printed `tools/govkit/govkit.py 36`,
`tools/govkit/shims.py 1`, `tools/govkit/upgrade_steps.py 4` and `tools/lib/python_floor.py 2`.
`fnsubst_probe.py tools/push-main.test.sh` printed `'resolve_python': 4` beside the base's 1, the
three added calls at `:1249`, `:1390` and `:1558`. The registry row for that file declares 1 and
keeps its reason (`spawn-idiom-sites.txt:183`): the lint reads arm 27's stub `resolve_python() {
echo bash; }` as the body, so every such call counts as a pure-function substitution.
`usage_probe.py` printed `rows 38 38 moved [] literal 59` over the clone's unchanged file. Over a
copy rewritten to `{prefix}/` it printed `literal 0`, and over the same copy with one id's kit
directory misspelled it printed `moved [('usage', 1, 'id')]`, so both halves can fail.

### Inventory

One file is minted, the floor program python_floor.py in govkit's steps directory (§8 F1).
Every other new name is a module constant or a suite variable holding a fixture prefix, a kit
directory name or a fixture remote name, so no function is minted beyond that program's `main`. The pin
rows of S4 and the registry move of S6 are rows in existing declarations. No leg, key, flag or arm
label is added.

### Migration

None. `usage.toml`, `steps.toml`, the release-0 fixture files, `upgrade_walk.py`, `docs_leg.py` and
`shims.py` are gov's own and reach no adopter: govkit is shipped by no descriptor
(`memory/project/encoding-posture-sites.txt:23`). `steps.toml` is on no landed commit
(`git cat-file -e origin/main:tools/govkit/steps.toml` fails), so `step-rows-frozen` freezes none of
its rows yet. The S3 and S6 lines of `push-main.sh` change no output byte, so an adopter that
receives the lander sees no difference.

### Rollout

Order 16, live at landing. This pass builds after TOOL-dSafePassage-72 to -78 and -80, and before
TOOL-dSafePassage-81 and -83. Units -72, -73, -74, -75, -76, -78 and -81 edit
`tools/govkit/upgrade_steps.py`, `govkit.py`, `selftest.py` or `tools/lib/python_floor.py`; -76 edits
`tools/lib/python-floor.sh` and adds arm 1e to `tools/lib/resolve-python.test.sh`; -77 edits
`tools/govkit/upgrade_walk.py` and the release-0 `arms.toml` and `plants.toml`; -80 edits three
`ceiling` lines of `tools/gate-legs.json`, disjoint from `:1480`. Building after them lets one pass
measure every class at the tree they leave. TOOL-dSafePassage-83 builds next and -81 last: -81's
renames must see every sibling's names, this pass's `main` included, and 83's manifest advance
counts watched commits, so it follows this pass's S7 re-stamp of the watched `tools/gate-legs.json`. TOOL-dSafePassage-61 holds order 16, is held
on TOOL-dGroundRules-13, and is not waited for.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/shims.py`
- `tools/govkit/upgrade_steps.py`
- `tools/govkit/upgrade_walk.py`
- `tools/govkit/docs_leg.py`
- `tools/govkit/usage.toml`
- `tools/govkit/steps.toml`
- the new floor program in govkit's steps directory, named in prose because it is not tracked yet
- `tools/govkit/fixture_target.py`
- `tools/govkit/selftest.py`
- `tools/govkit/fixtures/release-0/arms.toml`
- `tools/govkit/fixtures/release-0/plants.toml`
- `tools/govkit/fixtures/release-0/deploy.toml`
- `tools/lib/python_floor.py`
- `tools/lib/resolve-python.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/gate-legs.json`
- `memory/project/unarmed-branches.txt`
- `memory/project/spawn-idiom-sites.txt`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/symbols.json`, and whatever else `gen_map.py --write` rewrites under
  `memory/map/generated/`

### Alternatives rejected

- **Six units, one per leg.** Each leg's remedy is a mechanical conformance of this build's own
  lines to an existing lint, and TOOL-dTrueNorth-27 ("the nine bar legs this build turned red, each
  cleared at its cause", commit `d85890512`) and TOOL-aPrimedIndex-16 (`38e594a6f`) each took a
  close's own reds as one unit. Six units would write six times into `upgrade_steps.py` and
  `push-main.test.sh`.
- **Raising a registry count.** `encoding-posture-sites.txt:9-11` and the shell-hygiene message both
  say the count may fall and never rise, so a raise is the forbidden remedy for S1 and S6.
- **Converting `$(resolve_python)` in the suite to a no-fork call.** The function is the canonical
  inline block. Its output can only be taken by a substitution, so S6 removes three calls rather
  than three forks.
- **A sibling suite, python-floor.test.sh, beside the floor script.** A suite nobody runs arms nothing, and running it is
  a new leg, a unit of its own. `tools/lib/resolve-python.test.sh` already drives the preflight
  refusal and the down. A pin whose reason says so is the form the pin file prescribes for a site no
  sibling suite reaches (`unarmed-branches.txt:12-14`, and the branch-reconcile adopter's rows the
  bar prints).
- **Arming `push-main.sh:1333` and `:1343` here.** Each needs a stage where the walk or the
  regeneration succeeds and the next step fails, which no arm builds. The mint and regeneration
  commit refusals beside them are pinned for the same reason, and the close fixes of `37906b0b7` and
  `38e594a6f` pinned exit sites the same way.
- **Spelling a fixture path with a literal inside a variable's value**, such as `P = "tools/policy"`.
  It moves the literal and keeps the ban's subject, and rule 2 still reads it.

## 5. Production-readiness checklist

- security: S2 renames the remote two isolation plants write and expect; the credential predicate is
  name-blind, so it refuses the same key class. No refusal starts printing a value.
- perf / scale: no runtime path gains work. The resolver is untouched. The F1 program adds one python
  process to the floor step's three runs.
- error / empty / loading states: every refusal keeps its text. S4 adds no exit site and S6 changes
  only how a line is produced.
- observability: the four `python-floor.sh` and two `push-main.sh` pins print as
  `check-arms: waived` lines on every run, each with its reason.
- risks: a path resolved in a reader but not in its writer reads `{prefix}` literally; AC5 and the
  docs leg in AC11 catch that drift. A sibling unit adding a site after this pass reds the leg again
  at the close.
- testing: AC1 to AC10 are direct probes or fixture runs; AC11 is the main loop's run of each leg.
- migration: none (§4 "Migration").
- user docs: N/A. No page under `help/` prints a line S1 to S6 changes. `help/python-floor.md:39`
  and `:74` name `python-floor.sh`'s own modes, which F1 keeps.

## 6. Acceptance criteria

- **AC1** — When `python <scratch>/enc_probe.py tools/govkit/govkit.py tools/govkit/shims.py
  tools/govkit/upgrade_steps.py tools/lib/python_floor.py` runs from the repository root, it prints
  `tools/govkit/govkit.py 35` and a count of 0 for each of the other three files.
  Red when: a site keeps `text=True` with no `encoding=`, as all eight did at `83817478f`.
  figure: 35 is PINNED to `encoding-posture-sites.txt:23`, which this unit does not move.
- **AC2** — When `git grep -nE "(['\"])origin\1|remote\.origin\.|refs/remotes/origin/" --
  tools/govkit/upgrade_steps.py tools/govkit/upgrade_walk.py` runs, it prints nothing.
  Red when: a plant, the `fetch.py` program or the walk's clone still spells the default remote's
  name, as the four lines of S2 did.
- **AC3** — When `python tools/govkit/upgrade_steps.py fixture isolation --plant local-url-userinfo`
  runs, it exits 1 naming `remote.<the fixture's name>.url in .git/config` and printing neither
  planted credential. When `--plant local-ext-transport` runs, its output carries
  `transport 'ext' not allowed` and `ext-transport canary: absent`.
  Red when: the renamed remote is not the one the plant writes or the step fetches, so the step runs,
  or the refusal names the old key.
- **AC4** — When `python tools/govkit/upgrade_walk.py --list` runs, it exits 0, and its `plant`,
  `gov_plant`, `condition` and `arm` lines equal the same lines at `83817478f`, such as
  `upgrade-walk: plant · engine-edit · path tools/memory-tree/README.md · expect carried`.
  Red when: a `{prefix}/` spelling of S3 reaches the walk unresolved, so a line prints the token.
  cost: the listing mode builds the pinned clone (`tools/govkit/upgrade_walk.py:911`, which clones
  at `:173`), about a minute, and applies no target and runs no case.
- **AC5** — When `python <scratch>/usage_probe.py` runs, it prints equal row counts, `moved []` and
  `literal 0`.
  Red when: a rewritten id, entry or `rows` value resolves to something other than its
  `83817478f` value, or a literal kit path is left in `usage.toml`. Over today's file it prints
  `literal 59`.
- **AC6** — When `python tools/govkit/upgrade_steps.py list` runs, the floor row, id
  lib/python-floor-3.15, carries argvs naming the new floor program in govkit's steps directory,
  and no argv in `tools/govkit/steps.toml` spells the path of `tools/lib/python-floor.sh`. That
  program's `preflight` verb, run by `python` from the repository root, prints the `python-floor:` line and exits 0, and with `GOV_PYTHON` naming a fake that reports
  3.14 and `PATH` holding no launcher at the floor, it exits 1 with the resolver's own refusal.
  When the floor row's witness runs through `run_step_isolated` on gov's own tree, as
  TOOL-dSafePassage-75's AC2 runs it, the verdict is `ok`, so the program works under the runner's
  isolated `-I` launch.
  Red when: the row still spells the kit path, the replacement exits 0 below the floor, or it fails
  to load its module under `-I`.
  fixture: the below-floor fake is two lines written to the scratchpad, the shape
  `tools/lib/resolve-python.test.sh:193` already plants.
- **AC7** — When `grep -cP '^tools/lib/python-floor\.sh\texit\t' memory/project/unarmed-branches.txt`
  runs, it prints 4. When `grep -cF 'push-main: gov first could not snapshot the untracked files
  before its walk, so the walk did not run. Aborted (no push).' tools/push-main.test.sh` runs, it
  prints at least 1, and so does the same count of `push-main: the upgrade steps this landing
  declares did not hold on gov first (named above). Aborted (no push).`
  Red when: a pin row is missing, or an arm still asserts only a slice of its site's message.
- **AC8** — When `python <scratch>/fnsubst_probe.py tools/push-main.test.sh` runs, its
  `resolve_python` count is 1. When `grep -cF '| grep -c .' tools/lib/resolve-python.test.sh` runs,
  it prints 3. When `grep -P '^tools/memory-tree/merge-rows\.test\.sh\tvar-pipe\t'
  memory/project/spawn-idiom-sites.txt | cut -f3` runs, it prints 42.
  Red when: an arm keeps its own `$(resolve_python …)` call, so the count stays 4; the seven-statement
  count keeps its pipe, so the grep prints 4; or the fallen row is left at 43.
  figure: 3 and 4 are PINNED counts at `60d90cb7` and `83817478f`; TOOL-dSafePassage-76's arm 1e
  may add to the suite before this pass, and a site it adds is in scope by S6.
- **AC9** — When `git diff 83817478f -- memory/project/fork-ceilings.txt` runs at the pass's commit,
  it prints nothing: the five rows keep their ceilings 55, 57, 189, 74 and 44 until the owner rules
  on §8 F2.
  Red when: the pass moves a ceiling or a reason in the file, a change F2 leaves to the owner.
  figure: the measured counts 56, 58, 190, 76 and 45 are PINNED to the discovery bar on node a at
  `83817478f`.
- **AC10** — When `bash -n tools/push-main.sh` and `bash -n tools/push-main.test.sh` run, each exits
  0, and `grep -cF "| sed 's/^/  /'" tools/push-main.sh` prints 4, the four sites `60d90cb7`
  carried.
  Red when: the indent rewrite breaks the script's syntax, or the fifth site `run_gov_first` added
  remains, as it did at `83817478f`, where the count is 5.
- **AC11** — When the main loop runs each of the six legs' argv from `tools/gate-legs.json` alone, in
  a `git clone --shared` of the pass's head whose `origin/HEAD` points at main, five exit 0:
  `python3 tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills`,
  `bash tools/check-install-prefix.sh`, `bash tools/check-remote-literals.sh`,
  `python3 tools/memory-tree/check-arms.py --check` and
  `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`.
  The sixth, `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt .`, exits 1 with
  `2 passed · 5 red`, naming the same five rows as at `83817478f` and no other, until the owner
  rules on §8 F2.
  Red when: one of the five legs still names a site S1, S2, S3, S4 or S6 covers, or one a sibling
  added in a file of §4; or the spawn budget reds a row other than the five.
  permission: a role agent may not run these six (scratch-guard row G1); the main loop observes them.
  cost: the install-prefix leg's ceiling is 2940 s and the spawn budget's 2400 s.
- **AC12** — When `git show --stat --format= HEAD` runs at the commit that stages
  `tools/gate-legs.json`, it lists `memory/guides/SESSION-KICKOFF.md` too, and that file's
  `last-audit:` line names the commit's parent and a datetime later than the one at `83817478f`,
  while its `last-body-change:` line is unchanged.
  Red when: the commit stages the watched file alone, which the pre-commit ratchet refuses, or the
  re-stamp moves `last-body-change`, the advance TOOL-dSafePassage-83 owns.
- **AC13** — When `python tools/codebase-map/gen_map.py --check` runs at the pass's commit, it exits
  0, and a `python` one-liner loading `memory/map/generated/symbols.json` finds the floor program's
  `main`.
  Red when: the commit mints the program's names with no regeneration, so the check exits 1.

## 7. Gates

`encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `remote literals (kit code names no remote)` · `harness arms (fail branches armed or pinned)` · `spawn budget (forks per hot entrypoint)` · `shell hygiene (a fork spent on builtin work)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `upgrade-walk` · `docs` · `step-rows-frozen` · `python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC7 AC8 · arms 39 and 40 assert their sites' full messages and arms 33, 34, 37 and 40 read one resolution, staged red by shortening either message in tools/push-main.sh · none
New arm: tools/lib/resolve-python.test.sh · covers AC8 · the seven-statement assertion counts lines with no pipe and names paths from the suite's variables, staged red by a check printing six statements · none
New arm: tools/govkit/selftest.py · covers AC3 · the isolation plants expect the fixture's own remote name, staged red by the refusal naming another key · none

The first six legs are the ones this unit closes. Each one's failing case is the discovery bar's
red at `83817478f`, and the main loop observes each GREEN at the close. The next nine are the legs
whose `guard` a path under §4 "Files touched (estimate)" trips, the broad `tools/`, `tools/lib/`,
`tools/memory-tree/` and `.githooks/` guards aside. The rest observe the fixtures, the walk, the
docs rows, the frozen rows, the two suites this unit edits, the manifest S7 re-stamps and the map S8
regenerates.

## 8. Open questions

- **F1 — How does the floor step's row name gov's `tools/lib/python-floor.sh` without a kit path?**
  `steps.toml:34-36` spell `{gov}/lib/python-floor.sh`, and rule 3 bans a kit segment followed by a
  file under any base. The step contract admits only `{gov}`, `{target}`, `{prefix}` and `{to}`
  (`tools/govkit/upgrade_steps.py:18-19`, `:767`), and none of the drained tokens means gov's lib.
  - (a) A placeholder naming the row's own entry directory in gov, so the argv reads
    `{kit}/python-floor.sh`. It changes the step-row grammar, a contract adopters' descriptors use,
    and `help/upgrade-steps.md` with it. M3 veto 2 makes that an owner turn.
  - (b) A program python_floor.py in govkit's steps directory that loads `tools/govkit/upgrade_steps.py`
    by path, as `fanout_cap.py`'s `load_steps` does, finds the lib through that module's
    `resolve_kit_dir("lib", "python-floor.sh", …)`, and runs it under its `resolve_bash()` with its
    own arguments, passing the exit through. It imports nothing from govkit. The row's three argvs name it under `{gov}/govkit/steps/`,
    as the schema row's do. It adds one file and one process per run, and the preflight still runs
    the resolver from bash.
  Recommendation: (b). It is the leg's own named remedy, it changes no contract, and it is the only
  option a delegated resolver may take.
  RESOLVED (agent, 2026-10-28, delegated): (b), the program under `tools/govkit/steps/` resolving
  the floor script through `resolve_kit_dir`, ruled by the build's coordinator; rev-4 takes the
  step module's own copy of it, by the spec audit's L11.
- **F2 — How do the five fork-count rows pass?** The counter now sees a fork the resolver always
  spent (§4 "The spawn budget"). `fork-ceilings.txt:12-14` call the ceilings shrink-only and state no
  terms on which a run may raise one, so by M3 a raise is the owner's.
  - (a) Restore the old trace shape: the resolver lets python print its answer straight to the
    caller and captures output only on the failure path. Every marked inline copy is re-synced. The
    probe then trusts a candidate's exit 0 without parsing what it printed, which TOOL-dSafePassage-11
    added to refuse a stub that exits 0 and runs nothing.
  - (b) Raise each row to its measured count, 55 to 56, 57 to 58, 189 to 190, 74 to 76 and 44 to 45,
    each reason naming `ed135af16` and the unchanged process count, measured three times on the node
    the rows were measured on, as the `TOOL-aSparedSpawn-34` raise was (`e435aafe4`).
  Recommendation: (b). The count is a lower bound that started seeing a real fork; (a) churns every
  inline copy to hide it again and weakens the resolver's probe. Open for the owner: until the
  owner rules, the pass leaves `fork-ceilings.txt` untouched and the leg red (S5, AC9, AC11).

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-82-1-spec-writer.md`,
  grounded at `83817478f` in a shared clone whose `origin/HEAD` is main `1a61f21a`. Each red was
  re-derived by this spec's probes, `git log -S` and `git blame`; no leg but `memory hygiene` was
  run, because the role's allowlist names that leg and the naming lexicon alone. Install-prefix and
  the spawn budget each turned out wider than the brief named, 15 files and five rows, and every
  extra finding is this build's.
- rev-2 · 2026-10-28 · §1 · S3 · S5 · §3 Edges · §4 · §5 · AC6 · AC9 · AC11 · §8 F1 · F2 · §10 ·
  the coordinator's ruling during this dispatch. F1 is resolved (agent, delegated) to the program
  under `tools/govkit/steps/`, so S3 and AC6 lose their conditionals. F2 stays open for the owner:
  S5 is not built, `fork-ceilings.txt` leaves Files touched, AC9 asserts the file unchanged, and
  AC11 expects the spawn budget red on exactly its five rows.
- rev-3 · 2026-10-28 · S3 · §4 · AC6 · §8 F1 · the spec-token checker's path join, relayed by the
  coordinator. The floor program, not yet built and so untracked, is named in prose; the step id
  lib/python-floor-3.15 is written as an id outside backticks; the floor script is spelled by its
  tracked path `tools/lib/python-floor.sh`; the absent sibling suite is named without a path; and
  the release-0 fixture file is spelled from the repository root.
- rev-4 · 2026-10-28 · S3 · S7 · S8 · §3 · §4 · AC4 · AC6 · AC12 · AC13 · §7 · §8 F1 · §10 · folded
  the round-1 spec audit 2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1 (the
  build's reviews folder)
  at the fixes its skeptic judged sound: M1 (S7, AC12, the manifest in Files touched and the ratchet
  on §7), M11 and L5 (S8, AC13, the map in Files touched and its leg on §7), L4 (AC4's clone cost,
  §3's owner of the two timed-out legs), L11 (the floor program loads the step module by path and
  imports nothing from govkit, AC6 runs it under `run_step_isolated`, §10 cites `fanout_cap.py`),
  and L1 (Rollout: 83 next, 81 last). The header's node reads `a`, this host.

## 10. Reuse audit

The seams are the existing ones. Kit paths go through `tools/govkit/govkit.py`'s inlined
`resolve_kit_dir` (`:235`), `resolve_prefix_token` (`:218`) and `derive_tool_root` (`:192`), the
canonical copies being `tools/lib/resolve_kit_dir.py` and `tools/lib/resolve_prefix_token.py`.
`tools/push-main.sh` already routes its kits through `resolve_lander_kit`. The floor program extends
the step-program seam of `tools/govkit/steps/fanout_cap.py`, whose `load_steps` loads
`tools/govkit/upgrade_steps.py` by path and reaches `resolve_kit_dir` and `resolve_bash` there. The registries are
`memory/project/encoding-posture-sites.txt`, `memory/project/spawn-idiom-sites.txt`,
`memory/project/unarmed-branches.txt` and `memory/project/fork-ceilings.txt`, each moved only by its
own header's rule. `python tools/codebase-map/reuse_lookup.py "spell a sibling kit path without a
literal install prefix, resolved at read time"` ranked `resolve_kit_dir` (fan-in 41, installs 103)
and `resolve_prefix_token` (fan-in 9, installs 12) as seams, which S3 extends to three readers that
do not call them yet. The recall probe ranked TOOL-aRoutedQuill-12, an earlier build clearing its
own close's reds in one unit, and the registry rules of TOOL-aRepatriatedFork-20 and
TOOL-aSparedSpawn-20. TOOL-dTrueNorth-27, the other one-unit precedent, was found by `git log`.
No probe found a seam for a step argv naming gov's lib; §8 F1 resolves it through
`resolve_kit_dir`.

Recall terms used: `python tools/memory-recall/query.py "how did a build clear the merge bar's lint reds its own diff introduced without a waiver" --terms "close bar reds own diff encoding posture install-prefix remote literals harness arms spawn budget shell hygiene registry drain"`

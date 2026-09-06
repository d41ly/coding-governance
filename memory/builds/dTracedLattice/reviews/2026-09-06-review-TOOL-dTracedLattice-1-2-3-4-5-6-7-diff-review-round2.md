**Serves:** diff-review TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 TOOL-dTracedLattice-6 TOOL-dTracedLattice-7

# dTracedLattice — Tier-2 CLOSING DIFF review, round 2

*Node `a`, 2026-09-06. The subject is THE FOLD, not the code round 1 already read. This repo's own
`fold-text-is-unreviewed-surface` gotcha records that most round-N findings live in text the previous
fold ADDED, so the finder fan was pointed at the new text: the seven selftest arms the fold landed,
the prose it moved, and the two functions it widened. The seven new arms were graded as hard as the
code they cover — an arm that cannot fail is worse than no arm — and that grading is where most of
this report lands. Every `file:line` below was re-opened in this worktree before it was written down,
and every claim verified by RUNNING something carries its output inside the finding.*

**Range reviewed: `32d8d880415a38d4dc48d6c0a4bdc63f3964e99e...HEAD`** (HEAD = `4ccdca82`, one commit,
branch `branch/unattended-dtracedlattice-2f8f2b`, 25 files, +777/-60).

**Round: 2.**

## Verdict: BLOCKED

One BLOCKER, and it is the fold's own edit. The fold rewrote `tools/memory-recall/bench.py` (F4's
FORKED header, F11's rewritten `run_rm3` comment) without re-stamping its digest pin, so the
`memory-recall kit selftest` leg is RED at HEAD — I ran it: `42/44`, with
`bench.py: b2b8103b9681d835 != 8006144bcb9d0839` failing twice. This is kit work, so its Definition
of Done owes a `GATE_SELFTESTS=1` bar, which is where that leg lives.

Nine distinct defects in total (1 blocker, 3 high, 5 medium, 0 low). Four of the nine are
can't-fail selftest arms: of the seven arms the fold landed to left-shift round 1's findings, four
are graded here as passing over the defect they name — F1's, F2's, F5's and F6's. Three of those
were confirmed by staging the break and watching the arm stay green. The kit suite reports
`59 executed, 0 skipped, PASS` at HEAD while four of its newest arms cannot fail, which is exactly
the green-by-absence shape this build exists to remove. No finding reverses a fold decision; all
nine are small, single-file repairs.

## Review shape

Raw 29 · confirmed 27 · refuted 2 · unverified 0 · precision 0.93.

The 27 confirmed findings carried heavy co-reporting: four lenses independently reached the stale
`verbatim.json` pin, four reached the widened present-layer walk, four reached the F5 arm's
tautology, four reached the F1 arm's header needle, four reached the F6 arm's monkeypatch, three
reached the F7 arm's discarded return code, and two reached the F3 refusal text. Adjudication merges
those into **9 distinct defects**, R1–R9 below; each names the raw ids it absorbs. That merge is
mine, at synthesis, and is separate from the pipeline's own duplicate count in the integrity line.

## Run integrity

- Lenses: **4/4 returned, 0 DIED.**
- Skeptic batches: **5/5 returned, 0 DIED.**
- 0 contradictory verdicts demoted to unverified · 0 spurious verdicts discarded · 0 duplicates
  removed by the pipeline.
- 0 findings left UNVERIFIED. Nothing in this report is outstanding for lack of a skeptic verdict.

The run is COMPLETE: no lens died, so the zero counts above are measurements rather than gaps, and
"no finding in area X" means the area was looked at.

## Findings

| # | Sev | Where | One line | Raw ids |
|---|---|---|---|---|
| R1 | **BLOCKER** | `tools/memory-recall/verbatim.json:2` | the fold edited `bench.py` and left its digest pin stale, so the memory-recall kit selftest is RED at HEAD | 1, 7, 16, 23 |
| R2 | **HIGH** | `tools/codebase-map/map_lib.py:809` | F2's widened present-layer walk has no population bound, so on the primary tree it counts all 16 sibling worktrees as "this repository" | 2, 8, 17, 24 |
| R3 | **HIGH** | `tools/codebase-map/selftest.py:2408` | F5's arm re-implements the fix inside the test and asserts a tautology; reverting the shipped fix leaves it green | 3, 9, 18, 26 |
| R4 | **HIGH** | `tools/codebase-map/selftest.py:2317` | F1's arm needles a substring the unconditional header prints, so it greens over a candidate printer that never ran | 5, 10, 21, 25 |
| R5 | MEDIUM | `tools/codebase-map/selftest.py:2365` | F6's arm monkeypatches away the function F6 changed; reverting that half leaves the whole 59-arm suite green | 4, 12, 19, 28 |
| R6 | MEDIUM | `tools/codebase-map/reuse_lookup.py:527` | F3's no-scan `uncovered: []` renders as an affirmative "every present layer is covered" over a corpus nothing walked | 13, 20 |
| R7 | MEDIUM | `tools/codebase-map/selftest.py:2426` | F7's grep arm discards the return code, so `rc=128` and `rc=1` are one silent pass | 6, 15, 27 |
| R8 | MEDIUM | `tools/codebase-map/selftest.py:2334` | F2's arm drives the new helper directly and never `build_reference_index`, which is where the defect lived | 11 |
| R9 | MEDIUM | `tools/memory-recall/selftest.py:1323` | F4 moved four carriers of the retired Verbatim claim and left the fifth — the one that prints when the pin reds | 14 |

---

### R1 — BLOCKER · `tools/memory-recall/verbatim.json:2` · the fold broke its own merge bar

Raw ids 1, 7, 16, 23.

The fold rewrote `tools/memory-recall/bench.py` in two places — F4's five-line FORKED header at
`bench.py:48-52` and F11's rewritten `run_rm3` comment — and did not re-stamp the digest that pins
the file. `tools/memory-recall/verbatim.json` is untouched by commit `4ccdca82`.

Measured with the arm's own normalisation (`read_bytes().replace(b"\r\n", b"\n")`, sha256, `[:16]` —
`tools/memory-recall/selftest.py:1330-1336`):

- `bench.py` at HEAD → `b2b8103b9681d835`
- `verbatim.json` pins → `8006144bcb9d0839`
- `union.py` at HEAD → `a345199f5d901aae`, which reproduces its pin exactly

At base `32d8d880` `bench.py` hashed to exactly `8006144bcb9d0839`, and `git log -- verbatim.json`
shows that commit re-stamped the pin in the same commit that edited the file. So the maintenance
step exists, and this fold skipped it.

Ran the leg. `python tools/memory-recall/selftest.py` → `memory-recall selftest: 42/44 checks
passed`, with:

```
FAIL bench.py and union.py are byte-identical to the upstream copies they were taken from — AssertionError: bench.py: b2b8103b9681d835 != 8006144bcb9d0839
FAIL the whole selftest passes from the ADOPTER layout (kit at <root>/memory-recall/) — AssertionError: exit 1 from memory-recall/selftest.py:
FAIL bench.py and union.py are byte-identical to the upstream copies they were taken from — AssertionError: bench.py: b2b8103b9681d835 != 8006144bcb9d0839
```

It fails twice because `test_adopter_layout` re-runs the whole suite nested, and that nested failure
is the third red row.

The leg is real and it is guarded on the directory this fold edited:
`{"name": "memory-recall kit selftest", "argv": ["python3", "tools/memory-recall/selftest.py"],
"guard": ["tools/lib/", "tools/memory-recall/"], "chunk": "selftests", "subject": "kit"}` in
`tools/gate-legs.json`. `chunk: selftests` keeps it off the default bar, which is why a routine
branch run did not catch this; `GATE_SELFTESTS=1` surfaces it, and AGENTS.md says a DoD owes that
run for KIT work. This is kit work.

Two aggravations beyond the red row. The pin is the only mechanism that detects a silent fork of
this file, so leaving it stale means the next real fork is indistinguishable from this one. And the
fold's own new prose at `tools/memory-recall/query.py:126` — that the pin still holds the file — is
false in the tree as committed.

**Fix.** Set `"bench.py": "b2b8103b9681d835"` in `tools/memory-recall/verbatim.json`, then run
`python tools/memory-recall/selftest.py` and observe `44/44` before landing. R9 is the paired prose
repair and should land in the same commit.

**Left-shift.** The gate already exists and already fires; what failed is that it was not run. Two
options, and the first is enough: make the fold's Definition-of-Done checklist name
`GATE_SELFTESTS=1` explicitly for any commit whose diff touches a `tools/<kit>/` path, which is the
condition the leg's own guard already encodes. Failing that, add a `subject: repo` leg — one that
runs on every bar — asserting that no file named in `verbatim.json` has a mtime/blob newer than the
pin's own last-touched commit. The first is cheaper and does not add a leg.

---

### R2 — HIGH · `tools/codebase-map/map_lib.py:809` · the widened walk has no population bound

Raw ids 2, 8, 17, 24.

F2 replaced the roots-scoped inline tally with `derive_present_layers(root, skip_dirs)`
(`map_lib.py:809`, called at `map_lib.py:858`). The widening is right — the old tally agreed with
the symbol extractors by construction — but the new walk is bounded by nothing except
`_SKIP_DIRS = frozenset({"__pycache__", "node_modules", ".git", ".venv"})` at `map_lib.py:306`. That
set does not exclude `.claude/`, which is where AGENTS.md §2 pins this project's own worktree root,
and a linked worktree carries a `.git` FILE rather than a directory, so nothing prunes it.

Measured on this machine with the fold's own module:

| root | tally | wall |
|---|---|---|
| this worktree | `{.js: 8, .py: 61, .sh: 94}` | 0.04 s |
| `C:/projects/coding-governance` (primary) | `{.js: 145, .py: 880, .sh: 1579}` | 0.75 s |

Per-top-dir on the primary tree: `.claude` 2444, `tools` 143, `memory` 12, `.githooks` 3,
`skills` 2. That is 2444 of 2604 definition-carrying files — 94% of the population — inside 16
linked worktrees of other branches (`git worktree list` → 18 entries, 16 under `.claude/worktrees`).

Two consequences, and they are different in kind.

The counts are wrong today. `present_counts` is what `render_layer_refusal` prints verbatim as
`<ext> (N file(s))` (`reuse_lookup.py:529`), so the message whose whole job is to say how much went
unread overstates it about sixteen-fold on the primary tree — which is where `main` lives and where
the pre-push bar runs. The same commit answers "what languages are in this repository" two different
ways depending on which checkout you stand in.

The refusal is one file away. `present_extensions` is a set feeding `derive_layer_verdict`, whose
undeclared branch makes `reuse_lookup.main` exit 2 (`reuse_lookup.py:788-791`).
`DEFINITION_CARRYING_EXTS` spans 24 extensions (`.ts .tsx .go .rs .java .c .h .cs .kt .php .swift
.scala …`); this repo covers `.js`/`.py` and declares `.sh` dark. The day any branch checked out
under `.claude/worktrees/` adds one `.ts` file, `reuse_lookup` refuses repo-wide on `main` and
demands the operator declare a layer that is not in the tree it refused about. I checked: no such
extension exists under `.claude/` today, so this half is latent, not live. Reproduced with a fixture
regardless — a root holding `tools/x.py` as the symbol corpus plus
`.claude/worktrees/somebranch/web/app.ts` yields `present ['.py', '.ts']`, `undeclared ['.ts']`,
refusal non-empty.

This is a regression the fold introduced. Confirmed `roots == ['tools']` on this tree, so the old
scoped walk could never enter `.claude/`.

**Fix.** Bound the walk to the repository's own source. One line inside the `os.walk` loop prunes
nested checkouts and generalises to submodules:

```python
dirnames[:] = [d for d in dirnames if d not in skip_dirs and not (Path(dirpath) / d / ".git").exists()]
```

Deriving the population from `git ls-files` is the stronger form — it also drops untracked scratch
and gitignored build output, which are not "in this repository" in any sense — with the walk kept as
a stated fallback for when git cannot answer. Per AGENTS.md §7, run the candidate predicate over the
real primary tree and print the per-directory hits before wiring it.

**Left-shift.** An arm that plants a nested checkout under `<tmp>/.claude/worktrees/x/` carrying an
extension absent from the outer tree, and asserts `derive_present_layers` does not count it. The
fixture is three `mkdir`s and a `write_text`, and it reds today.

---

### R3 — HIGH · `tools/codebase-map/selftest.py:2408` · F5's arm asserts a tautology

Raw ids 3, 9, 18, 26.

F5's fix is inside `render_report`'s `constant` branch: `rank_harness.py:180-182` narrows to
`live_ids`/`live_rows` before calling `run_constant_control`. The arm registered at
`selftest.py:1683` as "rank_harness: control and measurement share a denominator (review F5)" is
`test_the_control_and_the_measurement_share_a_denominator` at `selftest.py:2389`. It loads
`rank_harness` by `importlib` and calls exactly one production function — `rh.measure_ranks` — then
re-derives the filter itself:

```python
live_ids = {sc["id"] for sc in scored}          # selftest.py:2406
live_rows = [r for r in rows if r["id"] in live_ids]
assert len(live_rows) == len(scored), (live_rows, scored)   # selftest.py:2408
```

`live_ids` is derived from `scored`, the fixture's ids are distinct, and `scored`'s ids are a subset
of `rows`' ids — so the closing assertion holds by construction for any such fixture, whatever the
production code does. It is a statement about the test's own two local variables.

`git grep` over `tools/` returns exactly four references to the two functions the fold touched, all
of them inside `rank_harness.py` itself: the `run_constant_control` definition at `:128`, the
`render_report` definition at `:153`, the fixed call at `:182`, and `main`'s print at `:204`. Neither
function is reached by any arm. A skeptic reverted `:182` to `run_constant_control(rows, root, args.k)`
— the exact pre-fold defect — and the arm still returned PASS.

What the arm does grade is `measure_ranks`' dead-probe detection (`dead == ["B"]`,
`len(scored) == 1`), which the fold did not touch. AGENTS.md §7: a guard that shares its derivation
with the thing it guards is not a guard.

**Fix.** Drive the real path. With the same two-row fixture, assert
`rh.run_constant_control(live_rows, root, k) != rh.run_constant_control(rows, root, k)` — the dead
row changes the denominator without adding a hit, so the two differ — then call
`rh.render_report(rows, scored, dead, args, root)` with `args.control == "constant"` and assert the
printed `constant control @k` figure is the live-rows one.

**Left-shift.** This is the gate; the repair is to make it able to fail. Stage the revert of
`rank_harness.py:182` once, confirm RED, unstage — AGENTS.md §7's "a new gate is not landed until its
failing case has been observed", which is the rule the fold skipped for four of its seven arms.

---

### R4 — HIGH · `tools/codebase-map/selftest.py:2317` · F1's liveness needle is in the header

Raw ids 5, 10, 21, 25.

`test_every_advertised_gen_map_mode_runs` (`selftest.py:2293`) runs each advertised read-only mode as
a subprocess and, for the modes flagged `prints`, guards against a silent no-op:

```python
assert proc.stdout.strip(), f"gen_map.py {' '.join(argv)} printed nothing"
assert "fan-in" in proc.stdout, (
    "the printer ran but named no candidate, so this arm would pass over the crash "
    f"it exists to catch:\n{proc.stdout}")        # selftest.py:2317
```

`_seed_affordances` prints that substring in its own header, unconditionally, before the emptiness
check:

```python
print(f"# seed-affordances: top {top} undeclared seams (fan-in >= {corpus.threshold})")  # gen_map.py:192
if not worklist:
    print("(none — every seam at/above the threshold already declares a ## Reuse affordance)")
    return                                                                                # gen_map.py:193-195
```

Ran it. `python tools/codebase-map/gen_map.py --seed-affordances --top 0` → exit 0, stdout:

```
# seed-affordances: top 0 undeclared seams (fan-in >= 3)
(none — every seam at/above the threshold already declares a ## Reuse affordance)
```

Both assertions pass over zero candidate rows. F1's actual break was in the row printer —
`{cand.file}` → `', '.join(cand.files)` at `gen_map.py:198` — which is reachable only on a non-empty
worklist. A skeptic staged exactly that class: forced `worklist = []` AND renamed the printer's
`cand.files` to a dead attribute, and the arm still returned PASS.

The arm has power today only because this tree's worklist happens to be non-empty. It loses that
power the moment the repo converges — which is the stated goal of the affordance worklist — or the
seam threshold rises, or the worklist filter breaks. Nothing announces the degradation. The arm's
own failure message claims it stops the suite "passing over the crash it exists to catch"; that
claim is false.

One correction to the raw reports, for accuracy: the needle is not literally unfirable. The other
early return, `no generated/symbols.json` at `gen_map.py:186-188`, prints no `fan-in` and would still
be caught. The vacuity is specific to the empty-worklist case, which is the case the message names.

**Fix.** Needle a byte only the candidate loop can emit, and refuse the empty-worklist state out
loud rather than passing over it:

```python
assert any(ln.startswith("- ") and "[fan-in " in ln for ln in proc.stdout.splitlines()), proc.stdout
assert "(none —" not in proc.stdout, "the worklist is empty, so this arm exercised no candidate printer"
```

**Left-shift.** The second assertion IS the left-shift: it converts a silent degradation into a named
refusal, per AGENTS.md §7's "a skip must announce itself". If an empty worklist is expected to become
the steady state, the arm should build its own two-seam fixture instead of running against the live
tree, so convergence never disarms it.

---

### R5 — MEDIUM · `tools/codebase-map/selftest.py:2365` · F6's arm stubs out the half it grades

Raw ids 4, 12, 19, 28.

F6 was two edits. `resolve_gate_path` stopped collapsing set-but-missing into `None`
(`check_gate_coverage.py:56-68`, ending `return path if path.is_absolute() else (root / value)`), and
`main` grew the exit-2 branch (`check_gate_coverage.py:94-98`). The arm replaces the first with a
stub:

```python
real = cg.resolve_gate_path
cg.resolve_gate_path = lambda root: missing      # selftest.py:2364-2365
```

so `main` receives a fixture `Path` from a caller that already makes the distinction, and only the
second half is graded. `grep` over the suite finds the function's only two appearances outside its
own definition — `selftest.py:2139-2140` in the pre-existing `_run_gate_coverage` helper, and
`selftest.py:2364-2365` here — and both are monkeypatch sites.

A skeptic reverted the resolver's last line to `return path if path.is_file() else None` — the exact
pre-fold defect — and `python tools/codebase-map/selftest.py` still reported
`59 executed, 0 skipped, PASS`, while production was back to reporting a moved gate as the benign
unset state with exit 0.

One imprecision in the raw reports, corrected here: `test_gate_coverage_is_green_on_this_tree`
(`selftest.py:2206`) does call `cg.main([])` unpatched, so the resolver body IS executed on the
set-and-exists path. The state F6 changed is the one nothing grades. That is the substance and it
holds.

**Fix.** Keep the stubbed `main` arm for the exit code and add three unpatched assertions against a
tmp root with a written `.codebase-map.conf`: `resolve_gate_path` is `None` for an unset `GATE_FILE`,
is a `Path` whose `.is_file()` is False for a set-but-missing one, and is the resolved file for a
set-and-present one.

**Left-shift.** Same repair as R3 and R4, and the same rule: stage the revert of the resolver's
return, confirm RED, unstage. More generally — a monkeypatch of the function under test is a
reviewable smell in this suite, and a cheap standing check is to grep the suite for
`cg.<name> = lambda` patterns whose target is named in a `(review F<n>)` registration line.

---

### R6 — MEDIUM · `tools/codebase-map/reuse_lookup.py:527` · F3's fold stops one function short

Raw ids 13, 20.

F3's early return is correct as far as it goes: with `present_extensions` absent, the verdict carries
empty `stale`/`undeclared` and the legacy migration check still fires
(`reuse_lookup.py:502-504`). But it hardcodes `"uncovered": []`, and the legacy branch of
`render_layer_refusal` reads `[]` as an affirmative:

```python
avail = ", ".join(verdict["uncovered"]) or "(none — every present layer is covered)"   # reuse_lookup.py:527
```

Reproduced verbatim. `derive_layer_verdict({}, ("bash",))` →
`{'uncovered': [], 'undeclared': [], 'stale': [], 'legacy': ('bash',), 'counts': {}}`, and
`render_layer_refusal` on that verdict prints:

> `… The uncovered layers present in this corpus are: (none — every present layer is covered). Set
> RECALL_DARK_LAYERS to the ones you deliberately do not cover.`

Empty-because-unwalked renders identically to empty-because-clean. That is F3's own class — absence
read as emptiness — one function downstream of the fix.

Reachable in production. `reuse_lookup.main` initialises `scan = {}` and fills it only via
`build_reference_index`, which is skipped when `corpus.symbol_files` is empty — the DOSSIER tier, no
`symbols.json`. Any such adopter whose conf still carries the pre-migration `RECALL_DARK_LAYERS=bash`
spelling is told to reset the declaration on the strength of a coverage fact nothing measured.

The fold's arm `test_no_scan_is_not_an_empty_corpus` (`selftest.py:2347`) asserts only that
`derive_layer_verdict({}, ("bash",))["legacy"] == ("bash",)` and never renders the text, so it passes
over the false sentence.

**Fix.** Carry the state rather than inferring it. Add `"scanned": False` to the early-return dict at
`reuse_lookup.py:503-504`, and at `:527`:

```python
avail = ", ".join(verdict["uncovered"]) or (
    "(none — every present layer is covered)" if verdict.get("scanned", True)
    else "(unknown — no corpus walk ran, so nothing was compared)")
```

**Left-shift.** Extend `test_no_scan_is_not_an_empty_corpus` by one line —
`assert "every present layer is covered" not in rl.render_layer_refusal(rl.derive_layer_verdict({}, ("bash",)))`.
It reds today and it costs nothing.

---

### R7 — MEDIUM · `tools/codebase-map/selftest.py:2426` · F7's grep arm cannot tell no-match from no-run

Raw ids 6, 15, 27.

The arm reads only stdout:

```python
out = subprocess.run(["git", "-C", str(root), "grep", "-n", "-F", needle,
                      "--", ":!memory/builds/"],
                     capture_output=True, text=True).stdout        # selftest.py:2423-2425
hits = [ln for ln in out.splitlines() if ln.strip()]               # selftest.py:2426
assert not hits, (...)                                             # selftest.py:2427
```

`git grep` exits 0 on match, 1 on no-match, and 128 on error, and this arm treats 1 and 128
identically. Measured in this tree:

```
bad-root  rc=128  stdout=''  stderr="fatal: cannot change to 'C:/definitely-not-a-repo': ..."
no-match  rc=1    stdout=''
```

Indistinguishable. A predicate that cannot say whether it ran is the reassuring-zero shape AGENTS.md
§7 makes binding, and this grep is the whole gate for F7's destination move — no sibling check covers
the same class. There is also no positive control, so nothing at runtime proves the
needle-and-pathspec combination can match at all.

Reachability is the weaker half of the claim and is stated honestly: this repo's suite always runs
against a real git root, and the `:!memory/builds/` magic pathspec works on the git here (verified —
rc=1 for the built needle, rc=0 with hits for a bare tracked substring under the same pathspec). So
rc=128 needs an unreadable or locked index, a vendored non-git tree under `CODEBASE_MAP_ROOT`, or a
git old enough to reject `:!`. The kit ships this arm as a standing leg into adopter repos
(`tools/codebase-map/kit.toml` declares "codebase-map kit selftest"), where the needle is
content-vacuous by construction and a silent failure would be invisible.

`git` missing from PATH would raise `FileNotFoundError` rather than pass — one raw report claimed
otherwise and that sub-case is wrong. The root, cwd and pathspec failures are real and silent.

**Fix.** Capture the `CompletedProcess` and assert liveness before reading stdout:
`assert proc.returncode in (0, 1), proc.stderr`. Add a positive control in the same arm — grep a
needle known to be tracked (`reinvention-backlog.md` alone returns hits under the same pathspec) and
assert it returns them — so a dead probe reds instead of passing.

**Left-shift.** The positive control IS the left-shift, and it generalises: any arm in this suite
that shells out and reads only stdout is the same defect waiting. A one-line grep over the suite for
`subprocess.run(` calls whose result is immediately `.stdout`-ed would enumerate the population
cheaply. While there, reconcile the arm's docstring — it names `derive_backlog_path`'s fail-open
branch as "the ONE sanctioned mention", but the assertion allows zero hits and that branch's source
does not contain the needle.

---

### R8 — MEDIUM · `tools/codebase-map/selftest.py:2334` · F2's arm grades the helper, not the call site

Raw ids 11.

`test_present_layers_see_outside_the_symbol_roots` (`selftest.py:2322`) calls
`m.derive_present_layers(tmp)` directly at `selftest.py:2334` and hand-builds the `scan` dict it then
feeds to `derive_layer_verdict`. It never calls `build_reference_index` — which is where the defect
lived, and where the fold's fix landed (`map_lib.py:858`).

A skeptic reverted the call site — restored the inline `DEFINITION_CARRYING_EXTS` tally inside the
`for top in roots` walk, leaving the new helper intact — and ran the four layer arms:
`test_present_layers_see_outside_the_symbol_roots`,
`test_every_declared_layer_is_present_on_this_tree`,
`test_undeclared_layer_refuses_with_both_remedies` and
`test_declared_layer_is_named_dark_in_the_banner`. All four PASS. The AC5 arm at `selftest.py:2277`
does drive `build_reference_index` with `stats=scan`, but it asserts only that the declared `.sh` is
present, and `.sh` lives under `tools/`, which IS a symbol root here (`roots == ['tools']`, measured).
So the shipped call-site wiring has no arm at all.

This matters more than a normal coverage gap because the helper's own docstring spends a paragraph
defending the second traversal's cost — which is exactly the pressure someone will later relieve by
re-inlining it.

**Fix.** Replace the hand-built fixture with the real path. The one-line pattern is already
established in this file at `selftest.py:938`:

```python
scan: dict = {}
m.build_reference_index(["src/text.py"], root=tmp, stats=scan)
assert ".ts" in scan["present_extensions"], scan
```

then feed that `scan` to `derive_layer_verdict` as the arm already does.

**Left-shift.** Stage the revert of `map_lib.py:858` once and observe RED. Pair it with R2's nested-
checkout fixture and one arm covers both the call site and the population bound.

---

### R9 — MEDIUM · `tools/memory-recall/selftest.py:1323` · F4 moved four carriers and left the fifth

Raw ids 14.

F4 reclassified `bench.py` from Verbatim to Forked in four places: `tools/memory-recall/README.md`
(the table row and the Maintenance section), `WIRE-INTO-PROJECT.md`, `tools/memory-recall/query.py`,
and `bench.py`'s own header. The fifth carrier — the gate arm that ENFORCES the classification —
still announces the retired claim:

```python
@check("bench.py and union.py are byte-identical to the upstream copies they were taken from")
def test_verbatim_files():
    """...
    These two carry no coupling on the query path, so they are re-pulled WHOLESALE on an upstream
    fix rather than merged. An edit here means somebody forked them without saying so.
    """
```

(`tools/memory-recall/selftest.py:1323-1329`, and the return string at `:1338` reads
`"N file(s) unmodified"`.) Both sentences are false for `bench.py` by the fold's own account:
`README.md` now classes it "Forked, one delta" and warns that a wholesale re-pull would revert the
fix with the pin green over the revert; `query.py:126` says it "is FORKED rather than verbatim since
TOOL-dTracedLattice-7".

This is the carrier attached to the failure. It is the text that prints at the moment the pin reds —
I saw it print verbatim in the R1 run above — so the instruction a maintainer reads while repairing
R1 is precisely the one that reverts TOOL-dTracedLattice-7.

**Fix.** Reword the `@check` label and the docstring to say the pin holds two files for two different
reasons: `union.py` verbatim, so an upstream fix is an overwrite; `bench.py` forked with one delta,
so an upstream fix is a MERGE that keeps the `(-count, term)` sort key in `run_rm3`. Match the new
README Maintenance text rather than paraphrasing it a second time.

**Left-shift.** This class — a claim moved in N carriers and left standing in the N+1th — is already
named in this repo's gotcha corpus, and it caught the fold twice in one commit (R1 and R9 are the
same miss). The cheap gate: the memory-recall suite already reads `README.md` in its surface arms, so
one arm asserting that no file listed in `verbatim.json` is described as "Forked" in `README.md`
without the selftest label saying so would close it. Cheaper still, and the one I would take: fold
the classification into `verbatim.json` itself as a per-file `mode` ("overwrite" / "merge"), so the
label is DERIVED from the data the gate already reads and there is no second copy to rot.

---

## What the fold got right

Stated so the report is not read as a verdict on the whole commit.

- **F4, F7, F8, F9, F10, F11, F12 land clean.** I re-read each against the tree and found nothing to
  add. `render_legacy_note` returns `""` on the same-path case and still fires for a real legacy;
  the `_scan_line` declaration-fallback branch is gone; `measure_phrase` is a single `next(...)` with
  the dead accumulator removed; the dossier now points at `map_imports.py`'s header instead of
  restating its claim; `map_diff.py`'s docstring and `WIRE-INTO-PROJECT.md` name the git-common-dir
  destination.
- **F5's production fix is correct**, including the `not rows` guard returning `nan` at
  `rank_harness.py:147-148`. R3 is about its arm, not the fix.
- **F6's production fix is correct** in both halves. R5 is about coverage of one of them.
- **F2's production widening is the right call** — the old tally agreed with the extractors by
  construction, which is the defect round 1 named. R2 is about the population it now walks, not
  about widening it.
- **The two arms the fold repaired during its own run are correctly repaired.** F7's needle is built
  from parts so the arm's source does not self-match, and F5's fixture derives the kit path via
  `m.kit_rel()` rather than spelling it. Both repairs hold at HEAD, and both were the right instinct;
  R3 and R7 are separate defects in the same two arms.
- **The kit suite runs clean and fast**: `python tools/codebase-map/selftest.py` →
  `59 executed, 0 skipped (0 of 5 guarded)`, `PASS`. Quoted as evidence for R3–R5 and R8 rather than
  as reassurance — it is green over four arms that cannot fail.

## Scope and limits of this review

- Findings are anchored to this worktree at `4ccdca82`. Every `file:line` was re-opened in the tree
  before being written down. Where a claim was verified by RUNNING something, the command and its
  output are inside the finding.
- The measurements in R2 were taken against the PRIMARY tree `C:/projects/coding-governance` as it
  stood on 2026-09-06 with 16 linked worktrees. The counts will differ on another node; the defect
  will not.
- Not covered: the memory-tree, hygiene, manifest, lexicon and template-size legs of the bar. This is
  a diff review, not a gate run. The two kit selftests were run because the fold edits both kits, and
  one of them is R1.
- Not covered: the round-1 findings' *design* — whether each fold was the right repair was settled in
  round 1. This round asks only whether the fold's own new text is correct, and whether the arms it
  added can fail.
- Not re-executed: the acceptance ledgers behind units 5 and 7 (`meas-*.md`, the adversarial scenario
  scoring). R3 is a defect in the instrument's TEST, not a claim that any recorded figure is wrong.

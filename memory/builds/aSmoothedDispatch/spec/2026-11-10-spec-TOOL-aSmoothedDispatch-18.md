# TOOL-aSmoothedDispatch-18 — the three bar legs this build turned red: unit 4's loop read off a one-name local, four test lines respelled off kit paths, and `--help` anchored on a help page

**Status:** SPECCED · rev-1 · 2026-11-10 · node a · Tier-1 · base ae6735c1 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-18-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-18-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-18-bar-reds.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-18-bar-reds.md) | research | — |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-18-re-id.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-18-re-id.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The bar at `e1781668e` failed three legs that this build turned red: `shell hygiene (a loop fed by a
command substitution)`, `install-prefix (shipped surface)` and `docs`. This unit clears all three. It
changes no refusal, no refusal message and no `--writes` split.

## 2. Scope (IN)

- **S1** — Shell hygiene. In `check_spec_token_hits` (`tools/unattended/unattended.sh:14299-14300`),
  `out="$3"` moves off the multi-name `local` line onto a `local out="$3"` line of its own, directly
  below it. The name `out` stays, so the two `printf '%s\n' "$out"` reads below it are not changed.
  Observed by AC1.
- **S2** — Install-prefix, driver suite. The unit 4 cache arm in `tools/unattended/unattended.test.sh`
  holds the run-gates kit's home once in `_sd_home`. It finds the kit's source directory through
  `resolve_kit_dir`, and spells the fixture copy's directory through `_sd_home` at `:7652`, `:7655`,
  `:7707` and `:7747`. The `unattributed` stub at `:7739` prints `spec-tokens: x.md` where it now
  prints `spec-tokens: tools/x.md`. Observed by AC2.
- **S3** — Install-prefix, hook suite. `write_run_state` in `tools/hooks/scratch-guard.test.sh:1180`
  writes the row's reason as `%s/a.js` fed `"$SGP"`, where it now spells `tools/a.js`. Observed by AC3.
- **S4** — Docs. The anchor `<!-- usage: verb:unattended.sh:--help 965e3eb2 -->` goes on exactly one
  page under `help/`, the page §7 F2 picks, beside a sentence saying what `--help` prints. Observed
  by AC4.

## 3. Non-goals (OUT)

- No change to unit 1's split at `tools/unattended/unattended.sh:15197`. The brief asks for that
  split to lose its here-string, but §7 F1 shows the leg does not count that line. Nothing the
  `--writes` arms assert moves, so the brief's region-four acceptance holds without a re-observation.
- No registry edit. `memory/project/substitution-fed-loops.txt` keeps `tools/unattended/unattended.sh`
  at `<<<` 2. Its header says a count may fall with the sites and may not rise.
- No edit to `tools/gate-lint/sh_hygiene.py`. Its `ASSIGNMENT` pattern binds only the first name of a
  `local` line that assigns several, so a later name keeps the credit of an earlier function's
  substitution. That is the scanner's own gap and a separate unit: a follow-up for the main loop's
  left-shift at the close (BUILD-METHOD M8), filed as an ask.
- No row added to `memory/project/docs-undocumented.txt`. The list is shrink-only, and the docs leg
  reds a row count above its low-water.
- No new skip branch in the cache arm. An install with no run-gates kit fails the fixture copy, as
  the arm does today.
- No change to what any refusal refuses or to its message. The refusal ceiling and spec 5's edge are
  done (`0b5c6db20`, `1038ada92`). The inherited suite reds filed as asks 10 to 13 stay out.
- No edit to a CLOSED spec of this build.

## 4. Design

### What the tree holds, read at `e606fb89c`

| Fact | Where |
|---|---|
| The leg gates three classes. One is `loop-var-sub`: a loop fed by a here-string over a variable whose latest assignment above took a command substitution. | `tools/gate-lint/sh_hygiene.py:170-178`, `:335-341` |
| `ASSIGNMENT` captures ONE name per `;`-segment, the first after any `local`. | `tools/gate-lint/sh_hygiene.py:160-162`, `:318-328` |
| The registry pins the driver at `<<<` 2 and compares counts both ways. | `memory/project/substitution-fed-loops.txt:63`, `tools/gate-lint/sh_hygiene.py:462-491` |
| Unit 4 added `done <<<"$out"` in `check_spec_token_hits`. The base `ae6735c1` has no such line. | `tools/unattended/unattended.sh:14314`, commit `8ccb09d91` |
| That function's `out="$3"` is the third name on a multi-name `local` line. | `tools/unattended/unattended.sh:14300` |
| The last single-name assignment of `out` above it is `out=$(awk ...)`. | `tools/unattended/unattended.sh:13763` |
| Unit 1's split line has no `done` and its here-string tail holds no substitution, so no gated class reads it. | `tools/unattended/unattended.sh:15197` |
| The cache arm copies the fingerprint from `$HERE/../run-gates/` into `./${PFX}run-gates/`. It spells that directory four times. | `tools/unattended/unattended.test.sh:7652`, `:7655`, `:7707`, `:7747` |
| The suite's idiom for a sibling kit holds its home once and resolves it, for example `_da_home=drift-audit`. | `tools/unattended/unattended.test.sh:13581-13590` |
| The suite derives the repo root without a fork as `${HERE%/"$KIT_REL"}`. | `tools/unattended/unattended.test.sh:8727` |
| `resolve_kit_dir` prints the kit directory repo-relative. | `tools/unattended/lib-unattended.sh:128-133` |
| The driver finds the fingerprint through `resolve_kit_dir ... run-gates gate-fingerprint.sh "$KIT_DIR"`, whose probe includes `<here>/../<home>/`. | `tools/unattended/unattended.sh:14340` |
| The `unattributed` stub's hit must sit under no build folder. `hitre` takes any non-space path. | `tools/unattended/unattended.test.sh:7739`, `tools/unattended/unattended.sh:14301`, `:14308-14312` |
| scratch-guard reads a dispatch row only up to `· reason `, so the reason text is never read. | `tools/hooks/scratch-guard.js:905` |
| The hook suite spells its product directory as `SGP=tools`. | `tools/hooks/scratch-guard.test.sh:885` |
| The `--help` verb's header line is what the docs leg reads as its usage row. | `tools/unattended/unattended.sh:37`, `tools/govkit/docs_leg.py:115-153` |
| Only `help/spec-audit.md` anchors any driver verb: `--record-round` and `--chain-verdict`. No page documents the driver's verbs as a set, and `command:unattended` is a list row. | `help/spec-audit.md:59`, `:85`, `memory/project/docs-undocumented.txt` |

The brief's three install-prefix counts and its docs finding come from the bar log at `e1781668e`.
They are PINNED there. The scanner count is DERIVED by the probe below.

### S1 — the one-name local

```bash
  local own="$MEMORY_ROOT/builds/$1/" far="$MEMORY_ROOT/builds/" line tail n="" m="" nfar=0
  local out="$3"
```

The scanner now reads `out` as assigned from `"$3"`, which is no substitution, so it clears the name
before line `:14314`. The loop leaves the gated population, and the count returns to 2. This is the
true latest assignment of `out` in that scope, so the change makes the scanner read what bash does.
It does not hide a substitution: the function's caller passes `"$RB_OUT"` as an argument
(`tools/unattended/unattended.sh:14386`), a form the leg leaves ungated by design
(`tools/gate-lint/sh_hygiene.py:79-82`).

### S2 — the cache arm and the stub

At the top of the arm, before `:7652`:

```bash
  # The run-gates kit's <home> is held once and resolved, so no line spells a kit path (install-prefix).
  _sd_home=run-gates
  _sd_rel=$(resolve_kit_dir "$_rkd_py" "$_sd_home" gate-fingerprint.sh "$HERE" 2>/dev/null) || _sd_rel=""
```

Then `:7652` makes `"./${PFX}$_sd_home"`. `:7655` copies
`"${HERE%/"$KIT_REL"}/$_sd_rel/gate-fingerprint.sh"` into `"./${PFX}$_sd_home/"`. `:7707` removes
`"./${PFX}$_sd_home/gate-fingerprint.sh"`, and `:7747` removes `"./${PFX}$_sd_home"`. The fixture
path is the same bytes as before, so the driver still finds the copy through its `<here>/../<home>/`
probe. At `:7739` the stub's first line opens `spec-tokens: x.md [packet]`, and its token and tail
stay as they are. `x.md` sits under neither the own prefix nor `memory/builds/`, so it is still a
counted, unattributed hit.

### S3 — the hook suite's reason

```bash
    for u in "$@"; do printf '2026-11-10T04:00:00Z dispatch · item 0123abcd %s · reason %s/a.js\n' "$u" "$SGP"; done; } > "$SG_RUNMD"
```

The row bytes stay the same. Only the spelling in the source moves.

### S4 — the anchor

The fingerprint 965e3eb2 is DERIVED by the docs leg's own reader through `$SCRATCH/sd10fp.py`. That
probe printed `5fdc7c80` for `--chain-verdict`, which is the anchor `help/spec-audit.md:85` holds,
so the probe agrees with the leg. Under F2's recommendation, a new page `help/unattended.md`
documents the verb, and `help/README.md` gains one index line for it:

```markdown
# The unattended driver's verb list

**What it is.** `unattended.sh --help` prints every verb the unattended driver takes and the guide
that states each verb's contract, then the driver's usage header, and exits 0. `-h` is the same.
<!-- usage: verb:unattended.sh:--help 965e3eb2 -->
```

It is followed by a fenced `bash` block holding `bash tools/unattended/unattended.sh --help`. The
docs leg tests that command against the verb rows, and `--help` is declared for that script.

### The pass probes

`$SCRATCH` is the run's scratch directory. Both probes import a leg's own functions and read. Neither
compares a registry nor returns a leg verdict.

```python
# $SCRATCH/sd10.py <repo root> <file> - the gated `<<<` sites sh_hygiene.scan_file classifies.
import pathlib, sys
root = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(root / "tools" / "gate-lint"))
import sh_hygiene as s
found = s.scan_file((root / sys.argv[2]).read_text(encoding="utf-8"))
sites = sorted((n, k) for k in s.GATED for n, d in found[k] if d == s.HERESTRING)
for n, k in sites:
    print(k, n)
print("gated <<< sites:", len(sites))
```

```python
# $SCRATCH/sd10fp.py <repo root> <id> - the usage fingerprint the docs leg derives for a driver verb.
import pathlib, sys
root = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / "tools" / "govkit"))
import docs_leg
rows = docs_leg.read_verb_usage(root)
print(sys.argv[2], docs_leg.derive_usage_fingerprint(rows[sys.argv[2]]))
```

This spec's author ran both at `e606fb89c`. `sd10.py` printed `loop-var-sub` at 8589, 8676 and
14314, then `gated <<< sites: 3`. On a scratch copy with S1 applied, it printed 8589 and 8676, then
`gated <<< sites: 2`, and `bash -n` passed on that copy.

### The builder's own checks

The builder runs no gate and no suite. It runs `bash -n` over each edited shell file, the two probes,
and the greps of AC1 to AC4. Each RED and GREEN observation of a moved arm belongs to the main loop
at the close.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/hooks/scratch-guard.test.sh`
- `help/unattended.md`
- `help/README.md`

The last two hold under F2 (b). Under (a) the one help path is `help/spec-audit.md`.

### Rollout

One pass, after units 1 to 9, all CLOSED. The driver and both suites are shipped bytes of their
kits, so the lander's `mint` moves the unattended and hooks kit versions, never a hand edit.

### Alternatives rejected

- **Take the here-string out of unit 1's split, as the brief asks.** §7 F1 shows the leg never
  counted that line, so the leg would still red at 3. It would also re-open unit 1's split behaviour
  for no gain.
- **Raise the registry row to 3.** The registry may only shrink, and a new site is never admitted by
  raising a count (`memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-65.md`).
- **Feed the loop `"$3"` directly.** A positional is a name the scanner cannot follow, so this
  clears the count by a blind spot. S1 clears it by making the scanner read the real assignment.
- **Fix `ASSIGNMENT` to bind every name of a `local` line.** That changes the leg's semantics across
  the whole tree, both ways, so it is a separate unit (§3).

## 5. Acceptance criteria

- **AC1** — When `python -I "$SCRATCH/sd10.py" . tools/unattended/unattended.sh` runs from the repo
  root, it prints two `loop-var-sub` lines, the `done <<<"$dirty"` and `done <<<"$rows"` loops, then
  `gated <<< sites: 2`. That equals the driver's `<<<` row in
  `memory/project/substitution-fed-loops.txt`. `grep -c '^  local out="$3"$' tools/unattended/unattended.sh`
  prints 1. `grep -c "read -r -d '' -a _dw <<<" tools/unattended/unattended.sh` prints 1, so unit 1's
  split is unchanged. At the close, the main loop observes the shell hygiene leg exit 0.
  Red when: `out="$3"` stays on the multi-name `local` line, so the probe prints a third site at the
  `check_spec_token_hits` loop and `gated <<< sites: 3`, as it does at `e606fb89c`.
  figure: the two sites and the count are DERIVED by the probe at observation time.
- **AC2** — When `grep -cF 'run-gates/gate-fingerprint.sh' tools/unattended/unattended.test.sh` runs,
  it prints 0, where it prints 2 at `e606fb89c`. `grep -cF '{PFX}run-gates' tools/unattended/unattended.test.sh`
  prints 0, where it prints 4. `grep -cF "spec-tokens: "'tools/x.md' tools/unattended/unattended.test.sh`
  prints 0, where it prints 1. `bash -n tools/unattended/unattended.test.sh` exits 0. At the close,
  the main loop observes the cache arm RED on stagings `u4` and `c3a` and the `unattributed` arm RED
  with `[ "$n" = "$nfar" ]` deleted (staging `s3-unattributed`), each GREEN once restored.
  Red when: the copy no longer lands where the driver resolves the fingerprint, so step a prints
  `spec-token cache off` and its admit assertion fails, or the stub's path falls under a build
  folder, so the arm's refusal turns into an admit.
- **AC3** — When `grep -c 'tools/a\.js' tools/hooks/scratch-guard.test.sh` runs, it prints 0, where it
  prints 1 at `e606fb89c`, and `grep -c "reason "'%s/a.js' tools/hooks/scratch-guard.test.sh` prints 1.
  `bash -n tools/hooks/scratch-guard.test.sh` exits 0. At the close, the main loop observes the D-AC1
  row RED against the hook at `af3ec143c` (staging `g-u6rev`) and GREEN at the tip.
  Red when: the format string loses a `%s`, so `$SGP` lands in the unit field and the row names no
  unit the hook reads.
- **AC4** — When `python -I "$SCRATCH/sd10fp.py" "." unattended.sh:--help` runs, it prints
  `unattended.sh:--help 965e3eb2`. `grep -rlF 'usage: verb:unattended.sh:--help 965e3eb2' help/`
  prints exactly one path, the page F2 picks. At the close, the main loop observes the docs leg exit
  0 with no `UNDOCUMENTED` and no `TWICE` line.
  Red when: the anchor carries another fingerprint, so the leg prints `STALE`, or it sits on two
  pages, so the leg prints `TWICE`, or no page carries it.
  figure: 965e3eb2 is DERIVED from the header line at `tools/unattended/unattended.sh:37`. An edit
  to that line moves it, and the probe re-derives it.

## 6. Gates

`shell hygiene (a loop fed by a command substitution)` · `install-prefix (shipped surface)` · `docs` · `scratch-guard self-test` · `tier2-review self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC2 · the cache arm's steps a and f on stagings `u4` and `c3a`, after the fingerprint copy moved to the resolved source · none
New arm: tools/unattended/unattended.test.sh · covers AC2 · the `unattributed` verdict arm, red with `[ "$n" = "$nfar" ]` deleted (staging `s3-unattributed`) · none
New arm: tools/hooks/scratch-guard.test.sh · covers AC3 · the D-AC1 row fed by `write_run_state`, red against the hook at `af3ec143c` (staging `g-u6rev`) · none

The driver suite is no leg of the manifest. It runs as the shard rows of
`tools/run-gates/selftest-budgets.txt`, and the cache and `unattributed` arms sit in shard 3, so the
main loop re-runs shard 3 and the hook suite, observes each arm RED and then GREEN, and runs the bar
once, at the close. The hook legs on the leg line are owed because `tools/hooks/` guards them, and
`tier2-review self-test` because it guards the driver. This spec's author ran no gate but the memory
hygiene gate and the naming lexicon over this file.

## 7. Open questions

- **FACT-QUESTION · F1 — Which `<<<` site does the leg count as the driver's third: unit 1's split
  at `:15197`, as the brief says, or another?** If the split, the brief's fix clears the leg. If
  another, the fix belongs at that site. Probe: `$SCRATCH/sd10.py` in §4, over
  `tools/unattended/unattended.sh`. Observation: the line numbers it prints. Liveness: the same
  probe on a scratch copy with S1 applied prints two sites, so it can produce a negative.
  Recommendation: fix whichever site the probe names. RESOLVED (agent, 2026-11-10): the third site
  is unit 4's `done <<<"$out"` at `:14314`, credited to `out=$(awk ...)` at `:13763` because the
  `local` line binds only `own`. The split at `:15197` is in no gated class. S1 fixes `:14314`.
- **F2 — Which help page carries the `--help` anchor?** The brief says "the help page that
  documents the driver's verbs", and no such page exists: only `help/spec-audit.md` anchors driver
  verbs, two of them, under the subject of spec-audit chains.
  - (a) `help/spec-audit.md`, a short section beside `--record-round`. No new file. But `--help` has
    nothing to do with spec-audit chains, and `help/README.md` says one page per feature.
  - (b) A new `help/unattended.md` holding only the `--help` paragraph and its command, plus one
    `help/README.md` index line. This is the page the driver's later verbs can join. But a new
    document is its own unit under BUILD-METHOD M2, and here it would ride inside unit 18.
  - (c) Option (b) as a separate unit, with this unit's S4 handed off to it. That keeps M2 whole and
    adds one unit and one pass to the build.
  Recommendation: (b). The build README's roster row for unit 18 already names the anchor as this
  unit's mechanism, and the page carries nothing beyond that anchor and its sentence. The owner
  decides, because the build runs with no mandate.

## 8. Revision log

- rev-1 · 2026-11-10 · initial draft from the brief `2026-11-10-prompt-TOOL-aSmoothedDispatch-18-bar-reds`,
  grounded at `e606fb89c`. A probe of the scanner found that the leg's third driver site is unit 4's
  loop, not unit 1's split, so S1 moves one `local` assignment and the split stays as it is. The
  docs page is F2, left to the owner.

## 9. Reuse audit

The unit extends seams the tree already has and adds no mechanism. S2 reuses the suite's sibling-kit
idiom, a home held once and found by `resolve_kit_dir` (`tools/unattended/unattended.test.sh:13581-13590`),
and its fork-free root derivation (`:8727`). `reuse_lookup.py` for "a suite fixture that copies a
sibling kit's file without spelling the kit path" ranked the `resolve_kit_dir` SEAM first (fan-in 44,
installs 104), with `tools/unattended/unattended.test.sh` among its users, and that is the seam S2
extends. S4 reuses the docs leg's anchor form (`help/docs-leg.md`, "How to answer a stale page").
Recall ranked `TOOL-dDerivedDocket-65`, which states that a new site is never admitted by raising a
count, and the `TOOL-cMendedVintage-12` one-hop widening that makes a variable-fed loop a gated
class. One record disagreed with the code: the brief names unit 1's split as the third site, and the
probe in §4 names unit 4's loop. `gotchas.py --for-paths` over the files touched selected
`fixture-passes-by-finding-nothing` and `staged-break-substitutes-a-synthetic-value`, which is why
each respelled arm is re-observed RED on its recorded staging rather than on a new one.

Recall terms used: `python tools/memory-recall/query.py "how is a loop fed by a here-string over a variable counted against the shell hygiene registry" --terms "here-string loop-var-sub one-hop assignment local registry count substitution-fed-loops shell hygiene widening"`

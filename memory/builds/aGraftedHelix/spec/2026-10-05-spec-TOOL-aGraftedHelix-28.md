# TOOL-aGraftedHelix-28 — a parity gate holds the by-design head the catalogue renders equal to the pattern the review harness parses

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-1 · base 5266d22e · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aGraftedHelix-27-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aGraftedHelix-27-1-spec-brief.md) | journal | TOOL-aGraftedHelix-27 |

<!-- /gen:spec-records -->

## 1. Goal

Unit 3 spelled the head of the by-design block twice. `BY_DESIGN_HEAD` in
`tools/memory-tree/gotchas.py` is the Python format string `render_by_design` prints, and
`BY_DESIGN_HEAD` in `tools/workflows/tier2-review.template.js` is the JS pattern `extractByDesign`
finds it with. They agreed once, in unit 3's AC6 probe, and nothing keeps them agreeing. A head
reworded in either kit makes the harness find no block and log `none supplied`, which a reader takes
for "no invariant touched": the zero-reads-as-clean class. This unit adds a check that renders the
head the way the catalogue prints it, runs the harness's own pattern over it in `node`, and reds when
the pattern stops matching or stops capturing the count. It rides the review-harness kit's existing
parity leg, so every bar runs it.

## 2. Scope (IN)

- **S1** — A new engine file in the review-harness kit, `check_by_design_parity.py`, takes the
  memory-tree kit's directory as its one argument. It imports that directory's `gotchas.py` and
  calls its `render_by_design` over synthetic records at each count in `SAMPLE_COUNTS`. It reads the
  one `const BY_DESIGN_HEAD = /…/` line of the template beside itself and evaluates that literal in
  `node`, calling it the way `extractByDesign` does. It passes only when the pattern matches every
  rendered head, captures exactly that head's count, and does not match the count-12 head behind a
  leading space. It exits 0 on parity, 1 on drift and 2 when it could not run. Observed by AC1, AC2
  and AC3.
- **S2** — The checker's other outcomes. A catalogue whose `KINDS` declares `invariant` and that
  defines no `render_by_design` is drift, exit 1. A catalogue declaring neither prints a `SKIP` line
  and exits 0, since it renders no block and the harness truthfully logs none. Exit 2 with a
  `REFUSING` line covers a template carrying zero or two declarations, a catalogue that cannot be
  imported, an absent `node`, and evaluator output that is malformed or answers fewer heads than were
  sent. Observed by AC2, AC3 and AC4.
- **S3** — `--selftest` runs one arm per outcome in S1 and S2 over fixtures it writes to a temporary
  directory, prints `selftest: <passed>/<declared> arms`, and fails when fewer arms ran than
  `ARMS_DECLARED`. That is the shape `review_replay.py` in the same kit already uses. Observed by AC4.
- **S4** — `tools/workflows/check-protocol-parity.test.sh` runs the checker in the leg's check mode, after
  the pointer arm and before the closing in-parity line, over the `MTD` it already resolves. The
  checker's exit status becomes the leg's. An absent checker file is a `missing shipped copy` red,
  the rule the leg already applies to a template. Where `MTD_SKIP` is set, the leg prints that the
  by-design arm did NOT run and why. Observed by AC5 and AC6.
- **S5** — `tools/workflows/unattended-build.test.sh` copies the checker into every layout its
  `build_layout` writes, so the check-mode layout runs keep their verdicts. It gains arms for the
  leg over a layout holding the real catalogue, the same layout with the head reworded and committed,
  the flat layout's stub catalogue, and the checker's `--selftest`. Its `FLOOR_ASSERTIONS` rises by
  the arms added. Observed by AC6.
- **S6** — The review-harness version moves once after this unit's last move, on the template's
  version line, and `tier2-review.js` is re-rendered. Observed by AC7.
- **S7** — `tools/workflows/README.md` and the review-harnesses dossier each say where the pair is
  held, and `memory/map/generated/` is re-rendered for the new file's symbols. Observed by AC8.

## 3. Non-goals (OUT)

- **No new gate leg** (shared invariant 5). The arm rides `review-protocol parity (kit vs dogfood)`,
  which carries no guard and so runs on every bar.
- **No home in `tools/check-playbook-parity.sh`.** §4 "Where it lives" gives the reasons.
- **No change to either spelling.** Both `BY_DESIGN_HEAD` values stay as unit 3 landed them.
- **The block's entry lines are not held.** A `- ` prefix that drifts makes the harness's count check
  refuse before any agent spawns, which is loud.
- **The checklist item prefix is not held.** It is the other format these two kits share, and its
  drift yields an itemless checklist, which the harness logs as a `WARNING:` and RUN INTEGRITY
  states. That is reported degradation, not the silent class.
- **Prose copies of the head are not graded.** The example in `tools/memory-tree/HYGIENE.template.md`
  and the sentences in the two kit READMEs mislead a reader when they drift, never a review.
- **No bar run of `--selftest`.** It is a kit self-test, which the 2026-08-23 owner ruling keeps off
  the bar. Its standing runner is the build-harness self-test arm S5 adds.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-3` — the two spellings this unit holds equal,
  `render_by_design` with its constant and `extractByDesign` with its pattern; without them there is
  no pair.

## 4. Design

### Evidence

Read at `f0971667`, the run branch's tip carrying unit 3's code; the build's pinned base predates it.

- `tools/memory-tree/gotchas.py:73` declares the format string, `:553` defines `render_by_design`,
  which always prints the head, `0` included, and `:66` declares `KINDS` with `invariant` in it. The
  module imports only the standard library and runs nothing at import.
- `tools/workflows/tier2-review.template.js:291` declares the pattern. `extractByDesign` at `:292`
  right-trims each line, calls `test`, then `exec` on the line found, and reads group 1 as the count.
  With no head found it returns no entries, and the harness logs `none supplied`.
- `cmd_for_paths` prints each item's description indented six spaces (`gotchas.py:547`). A
  description quoting the head must never open a block, which is what the leading-space negative
  asserts.
- `tools/workflows/check-protocol-parity.test.sh:213` resolves `MTD` through `resolve_kit_dir` or
  the `MEMORY_TREE_DIR` override, and sets `MTD_SKIP` when no `gotchas.py` is tracked. The pointer
  arm ends at `:404` and the closing line starts at `:405`. It already resolves python with its
  inlined `resolve_python`.
- `tools/workflows/unattended-build.test.sh:1516` builds fixture layouts from an explicit file list
  with a stub `gotchas.py` holding one comment line, and runs the leg in check mode over them
  expecting exit 0. `tools/govkit/selftest.py` copies the leg into its fixtures too, and runs it in
  `--render` mode only, which never reaches the new arm.
- `tools/govkit/registry.toml` exempts `check-playbook-parity.sh` from shipping.

### Where it lives

The brief named `tools/check-playbook-parity.sh` as the precedent and possible home. It is not the
home, for three reasons. It is gov-only, exempt in govkit's registry, while the one place this drift
can arise outside gov is an adopter holding the two kits at different versions. Its subject is what
the playbook states about this repo, and its value pairs compare `sed` extractions as strings, which
is the comparison the brief rules out. And it would have to resolve two more sibling kits.

The home is the review-harness kit's own repo-subject leg. The harness is the CONSUMER of the head,
and that leg already reaches the producer without a literal: it finds the memory-tree kit's
`gotchas.py` through the sibling-kit resolver, so shared invariant 2 holds. `kit.toml` leaves it
unguarded precisely so a memory-tree edit cannot skip it. It ships, and it already skips out loud
where no memory-tree kit is installed.

The comparison is a separate file beside the leg rather than inline in it. A pass needs a direct
check a criterion may spell, and the spec token checker's bar join refuses a `.test.sh` at command
position in a criterion, while the gate guard refuses one outside its read-only verbs. Python also
imports the catalogue and drives one `node` process more simply than bash does.

### The comparison

1. Import `<dir>/gotchas.py` by file location. With `render_by_design` present, render the block at
   each count in `SAMPLE_COUNTS`, `(0, 12)`, over records carrying a name, an empty sections map and a
   decision id, and take each block's first non-blank line as its head. Zero is the head every miss
   prints; twelve is a second, multi-digit count, so a single-digit capture or a head without its
   count field cannot pass. Without `render_by_design`, S2's rule decides.
2. Hand `node` the heads as ASCII-escaped JSON on stdin and the template path as an argument. The
   escaping keeps every code page away from the em dash, which unit 3's AC4 measured breaking under
   `cp1252`.
3. In `node`, read the template as UTF-8, split on `\r?\n`, and require exactly one line shaped
   `const BY_DESIGN_HEAD = /…/<flags>`. Evaluate that literal, right-trim each head, call `test`, then
   `exec`, and answer one result per head: matched or not, and group 1.
4. In Python, require one result per head sent. Then pass only when every rendered head matched with
   group 1 equal to its count, and the count-12 head behind one leading space did not match.

The JS evaluator is a raw Python string, because the `heredoc-escape-reaches-the-regex` class turns
an escape in a non-raw string into a control byte. Author the file with the Write tool, not a shell
heredoc.

The checker's header states what it does NOT check: the entry lines; the render, whose identity with
the template is the leg's own pair; a pattern loosened but still anchored and capturing digits, whose
mis-cut the harness's count check refuses loudly; and a pattern declared in another shape, which
refuses rather than passes.

### The leg wiring

```bash
if [ -n "$MTD_SKIP" ]; then
  echo "protocol-parity: the by-design arm did NOT run — $MTD_SKIP"
else
  [ -f "$HERE/check_by_design_parity.py" ] || { echo "protocol-parity: missing shipped copy $KITREL/check_by_design_parity.py"; exit 1; }
  _bd_py=$(resolve_python) || exit 2
  "$_bd_py" "$HERE/check_by_design_parity.py" "$MTD" || exit $?
fi
```

It runs in check mode only, since `--render` exits earlier. It changes neither the pair count nor the
closing line, so existing assertions on those keep their verdicts.

### Inventory

| identifier | where | cell |
|---|---|---|
| `check_by_design_parity.py` | the review-harness kit | engine file, shipped under `**` |
| `load_checker`, `render_heads`, `run_pattern`, `check_parity`, `print_verdict`, `build_fixture`, `run_selftest`, `main` | `check_by_design_parity.py` | `py.function` |
| `SAMPLE_COUNTS`, `ARMS_DECLARED`, `EVALUATOR` | `check_by_design_parity.py` | constant |

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
on 2026-10-05 and answered OK. No codebase-map key is minted: `workflow-scripts` enumerates `*.js`
only, so a `.py` file adds symbols to `generated/` and nothing to the ratchet.

### Files touched (estimate)

- `tools/workflows/check_by_design_parity.py`, new
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/tier2-review.template.js`, the version line only
- `tools/workflows/tier2-review.js`, by the render
- `tools/workflows/README.md`
- `memory/map/features/review-harnesses.md`
- `memory/map/generated/`

### Rollout

1. Write the checker and its `--selftest`. Observe each arm red against a scratch copy of the
   checker with that arm's predicate disabled.
2. Wire the leg, then update `build_layout` and add S5's arms. Every new arm spells kits through the
   suite's derived names, because the foreign-prefix leg runs the suite at three prefixes.
3. Write the README and dossier sentences.
4. Bump the review-harness version once, on both ids of the template's version line. Re-render with
   the leg's `--render` mode, then run `python tools/codebase-map/gen_map.py --write`.

Unit 21 shares `order 12` and writes the same version line, the same render and
`unattended-build.test.sh`. The two write sets intersect, so the passes run in sequence, as this
build's rules already make every pass do. Each bumps the version once after its own last move. No
file this unit touches is in the kickoff manifest's `watch:`, so no re-stamp is owed.

### Alternatives rejected

- **Formatting `BY_DESIGN_HEAD` directly instead of calling `render_by_design`.** It cannot see a
  renderer that stops using the constant. AC2's second staged break is the test that separates the
  two.
- **Comparing the two spellings as text.** A format string and a regex source share no syntax, so the
  compare would need a translator, which is a third spelling of the head.
- **Running the pattern through Python's `re`.** `\d` matches Unicode digits there, and `$` matches
  before a trailing newline, so it is not the harness's behaviour.
- **Calling `extractByDesign` itself.** A workflow script runs in a restricted runtime with top-level
  arguments and no exports. Running it needs the stub runtime the kit's suite carries, which makes it
  a suite, not a leg.
- **Skipping on a missing renderer whatever the catalogue declares.** A renamed `render_by_design`
  would then skip forever in gov's own tree. The `invariant` kind separates a renamed renderer from a
  catalogue that predates the block.

## 5. Production-readiness checklist

- security — No new surface. The checker imports a tracked file of this repository, which the bar
  already executes, and evaluates one regex literal from a tracked template. It writes nothing and
  opens no network connection.
- perf / scale — One Python import and one `node` process per leg run. PINNED on node `a` on
  2026-10-05: a bare `node` spawn took 0.05 s and importing `gotchas.py` took 0.10 s. The leg's
  ceiling is 300 s.
- error / empty / loading states — A catalogue without the block skips out loud, and an install
  without the memory-tree kit skips out loud. A refusal exits 2 naming its cause, and drift exits 1
  quoting the head and the pattern.
- observability — One `by-design parity:` line in the leg's log on every run, whether agreement,
  `SKIP`, `DRIFT` or `REFUSING`. The agreement line names the counts it compared.
- risks — A fixture that copies the leg without the checker reds. `build_layout` is the only
  check-mode site, and S5 covers it. An adopter whose memory-tree kit predates invariants skips
  rather than reds.
- testing — `--selftest` over fixtures, each arm observed red. AC2 and AC3 stage breaks on copies of
  the real files, because the `staged-break-substitutes-a-synthetic-value` class says a synthetic
  fixture proves the mechanism only for the synthetic value. S5's suite arms keep the leg-level red.
- migration — None. Adopters receive the arm on update, and it skips where the catalogue predates
  the block.
- user docs — The workflows README and the review-harnesses dossier.

## 6. Acceptance criteria

- **AC1** — When `cd tools/workflows && python check_by_design_parity.py ../memory-tree` runs on the
  built tree, it exits 0 and prints one `by-design parity:` line naming each count in
  `SAMPLE_COUNTS` as matched and captured, and the leading-space head as not matched.
  Red when: the harness's pattern fails to match a head the catalogue renders, captures anything but
  its count, or matches the head behind a leading space.
  figure: the counts are PINNED in `SAMPLE_COUNTS`, and the line prints them from it.
- **AC2** — When a copy of `tools/memory-tree/gotchas.py` in a directory under the run's scratchpad
  has `by design` in `BY_DESIGN_HEAD` changed to `by-design`,
  `cd tools/workflows && python check_by_design_parity.py <scratch-dir>` exits 1 with a `DRIFT`
  line quoting the rendered head. With the constant as shipped and the copy's `render_by_design`
  printing that reworded head as its own literal, it exits 1 the same way. With `render_by_design`
  taken out of the copy, it exits 1 naming the `invariant` kind; with `invariant` also taken out of
  the copy's `KINDS`, it exits 0 with a `SKIP` line.
  Red when: a reworded head, from either the constant or the renderer, exits 0.
  fixture: a copy of the shipped file, so each break is to the real head.
- **AC3** — When a scratch directory holds copies of `check_by_design_parity.py` and
  `tools/workflows/tier2-review.template.js`, with the template copy's pattern loosened to
  `/^(.*)$/`, `python <scratch-dir>/check_by_design_parity.py tools/memory-tree` exits 1 naming a
  capture that is not the count. With only the pattern's leading `^` taken out instead, it exits 1
  naming the leading-space head it matched. With the declaration line taken out, it exits 2 with a
  `REFUSING` line, and with the declaration written twice it exits 2 the same way.
  Red when: a loosened or unanchored pattern exits 0, or a missing or doubled declaration reads as
  parity.
- **AC4** — When `cd tools/workflows && python check_by_design_parity.py --selftest` runs, it prints
  `selftest: <n>/<n> arms` and exits 0. Each arm was observed FAIL once against a scratch copy of the
  checker with that arm's predicate disabled, the result-count check and the `KINDS` test included.
  Red when: an arm passes with its predicate disabled, or fewer arms ran than were declared.
  figure: `<n>` is DERIVED from `ARMS_DECLARED`.
- **AC5** — When the review-harness kit's parity leg runs in its `--check` mode at the pass's commit,
  its output carries the checker's `by-design parity:` agreement line and it exits 0. With
  `BY_DESIGN_HEAD` reworded in `tools/memory-tree/gotchas.py` in the working tree, it exits 1 with the
  `DRIFT` line. Restored, `git diff --quiet -- tools/memory-tree/gotchas.py` exits 0 and the leg
  exits 0 again.
  Red when: the leg passes over a reworded head, or prints no `by-design parity:` line.
  cost: seconds. It is the one leg the bar runs, not a suite, and the gate guard admits `--check`.
- **AC6** — When the build-harness suite's parity block runs as a slice inside the kit directory,
  behind the suite's prologue, it reports four things. The layout holding a copy of the real
  catalogue passes with the agreement line. The same layout with the head reworded and committed
  reds with `DRIFT` and `rc=1`. The flat layout's stub catalogue passes with `rc=0` and the `SKIP`
  line. The checker's `--selftest` exits 0. Each new arm was observed red with the leg's call to the
  checker cut from a scratch copy of the leg, and `FLOOR_ASSERTIONS` is raised by the arms added.
  Red when: the leg runs no checker and those arms stay green.
  permission: the whole suite is the main loop's, run once at VERIFYING; a pass runs the slice only.
- **AC7** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, its `review-harness` line reads `clean` at the bumped version, and
  `bash tools/check-kit-versions.sh` exits 0. After the leg's `--render` mode runs,
  `git status --porcelain tools/workflows/` prints nothing.
  Red when: the kit's shipped bytes moved and its version did not, or the render differs from its
  template.
- **AC8** — When `python tools/codebase-map/test_codebase_map.py` runs at the pass's commit, every
  line reads `ok`. `grep -c "check_by_design_parity.py" tools/workflows/README.md memory/map/features/review-harnesses.md`
  counts at least 1 in each file. `git grep -nE "(memory-tree|workflows)/" -- "*check_by_design_parity.py"`
  prints nothing.
  Red when: the map's generated artifacts are stale, a reader is not told where the pair is held, or
  the checker spells a kit path the install-prefix ban would red.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `shell hygiene (a loop fed by a command substitution)` · `line length` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `govkit selfcheck` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/check-protocol-parity.test.sh · the by-design head pair, red through the checker's exit; stage BY_DESIGN_HEAD reworded in tools/memory-tree/gotchas.py · none
New arm: tools/workflows/unattended-build.test.sh · the leg over the real catalogue, a committed reworded head, the stub catalogue, and the checker's --selftest; stage the leg's call to the checker cut · the suite's FLOOR_ASSERTIONS, raised by the arms added
New arm: check_by_design_parity.py --selftest · each arm's predicate disabled in a scratch copy of the checker · ARMS_DECLARED, set to the arms written

The kit's suites are not on the bar. A pass runs AC1 to AC5 and AC7 to AC8 directly, and the main
loop runs the build-harness self-test once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the unit-27/28 spec brief and unit 3's acceptance ledger,
  grounded against `gotchas.py`, the review harness template, the parity leg and the build-harness
  suite at `f0971667`.

## 10. Reuse audit

The first probe was:

```bash
python tools/codebase-map/reuse_lookup.py "compare a value one kit owns against the copy another kit parses"
```

It ranked name-stem neighbours only, `parse` and `resolve_kit_dir` among them. A second probe,
`"render a template and assert the live copy matches it"`, ranked `render_*` functions in the map
and backlog kits. Both printed `unscanned layers: .sh`, so their miss is no evidence about the
two parity scripts, which are shell, and both were read by hand. The seams extended are
`tools/workflows/check-protocol-parity.test.sh`, whose `MTD` resolution and skip discipline the arm
reuses, `render_by_design` in `tools/memory-tree/gotchas.py`, called and not changed, the
`ARMS_DECLARED` self-test shape of `tools/workflows/review_replay.py`, and `build_layout` in
`tools/workflows/unattended-build.test.sh`. Recall surfaced `TOOL-aRepatriatedFork-46`, which made
the leg find `gotchas.py` through the sibling-kit resolver, and `TOOL-aRepatriatedFork-7`, which made
it the kit's one renderer. It surfaced `TOOL-dDerivedDocket-50`, which rejected a standalone
cross-kit checker because a new leg owes a ceiling, a self-test and a descriptor row, and keeps a
sibling kit a render token, never a literal. And it surfaced `TOOL-aHonedRuleset-11`, a record that
playbook parity's extractions are per-line text, which is the comparison this unit does not use.
`gotchas.py --for-paths` over the files touched selected `two-answers-to-one-question`,
`staged-break-substitutes-a-synthetic-value`, `heredoc-escape-reaches-the-regex`,
`fixture-passes-by-finding-nothing` and `node-check-is-not-a-syntax-gate`; §4 and §5 answer each.

Recall terms used: parity cross-kit sibling-kit literal render token protocol-parity playbook-parity value-pair two-answers drift by-design checklist header

The question passed with them: "where does a gate that holds a value two kits spell identically
live, and should it compare behaviour rather than text".

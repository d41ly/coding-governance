# TOOL-aGraftedHelix-29 — the by-design block is rendered from the invariant records at the review's base, so a change cannot write its own exemption

**Status:** SPECCED · rev-2 · 2026-10-05 · node a · Tier-2 · base 018b5675 · streams tooling · order 13 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aGraftedHelix-29-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aGraftedHelix-29-1-spec-brief.md) | journal | TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 |

<!-- /gen:spec-records -->

## 1. Goal

`gotchas.py --for-diff <base>..<head>` picks the invariant records it prints as the by-design block
from the working tree. A range that adds or edits a `kind: invariant` record therefore hands every
lens and skeptic of its own review an instruction to refute the findings that ruling covers. The
closing review's round 1 measured the live instance: all three by-design entries it was handed were
records its own range added (H1, finding id 1). This unit renders the block from the records as they
stood at the range's base, and lists every invariant the range moved as a checklist item instead.
It gives `--for-paths` the same base through a `--base <rev>` argument, and makes the build harness
pass its pinned base to the spec audit's checker, so the channel the review left open is closed too.
A checklist item can only widen a review, so the class half of the checklist keeps reading the tree
under review.

## 2. Scope (IN)

- **S1** — `cmd_for_diff` resolves the commit its range diffs from: the left side of `A..B`, the
  merge base of `A...B`, and the revision itself for a single-revision range, an empty side read as
  `HEAD` as git reads it. It passes that commit and the range's changed paths to `cmd_for_paths`.
  Observed by AC1, AC2 and AC5.
- **S2** — The invariant records at that commit are read with one `git ls-tree` and one
  `git cat-file --batch`, and each is parsed by `build_record`, the per-file body `records` holds
  today, factored out so both readers build one record shape. A record at the base that does not
  parse is announced on a header line and exempts nothing; it never refuses the checklist. Observed
  by AC2.
- **S3** — The by-design block is built from the base's invariant records alone: each one whose
  base anchors select a path of the subject, less every record whose own path the subject changed.
  `render_by_design` renders it unchanged, in signature and in output shape. Observed by AC1, AC2
  and AC5.
- **S4** — An invariant record whose path is in the subject's changed set, read as an invariant at
  either end, prints as a checklist item when its own path is one of the subject's paths or its
  anchors at either end select one. Under `--for-diff` the changed set IS the paths, so every
  invariant a range moves is itemised whatever its anchors say. The item prints after the class
  items and before the block, in the item shape the checker already uses:
  `- [ ] NEW/CHANGED invariant <name> — verify the ruling before treating it as by design`, then its
  description and its path on indented lines. A record the range took out is named from its base
  text. Observed by AC1 and AC5.
- **S5** — One header line after the two the checker prints today names the base as 12 hex and the
  count of S4 items. `--for-paths` run without a base prints a header line saying the block was read
  from the working tree, so a record the subject added can stand as by design. Observed by AC3, AC5
  and AC6.
- **S6** — `--for-paths --base <rev> <path>...` resolves `<rev>` as a single revision and takes S2
  and S3 at it. Its changed set is every record under the catalogue whose normalised text at the base
  differs from the working tree's, or that exists on one side only, so an uncommitted record counts.
  Observed by AC3 and AC6.
- **S7** — A range or a revision that opens with `-` is refused before any git call, so a value such
  as `--output=<file>` can never reach `git diff` as an option. A range or revision git cannot
  resolve is a named `HYGIENE gotchas:` line at exit 1, where it is a Python traceback today.
  Observed by AC4.
- **S8** — `gotchas.py --selftest` gains the arms AC1 to AC4 name, each observed failing against the
  parent's `gotchas.py` with the arm grafted in. Observed by AC1, AC2, AC3 and AC4.
- **S9** — The build harness's subject resolver runs `gotchas.py --for-paths --base <base> <paths>`
  when the call's `base` has the 7-40 hex shape, and its `checklist from` log line names that base.
  Without one it runs the command as today, and when the stage takes the resolver's checklist it logs
  a `WARNING:` that the audit's by-design block was read from the working tree. The build-harness
  suite gains arms for both. Observed by AC7.
- **S10** — The review suite gains an end-to-end arm. It runs the real checker's `--for-diff` over a
  two-commit fixture whose second commit adds an invariant, and feeds that stdout to the review
  harness as `checklist`, asserting the added invariant never reaches `byDesign` (§8 F2). Observed by
  AC8.
- **S11** — `memory/gotchas/inputs-inside-the-subjects-reach.md` gains this instance under its
  `## Where it bit`, naming `tools/memory-tree/gotchas.py` and
  `tools/workflows/tier2-review.template.js`, so a diff touching either carries the class on its
  checklist. `memory/gotchas/INDEX.md` is re-rendered. Observed by AC10.
- **S12** — The prose that describes the block says where it is read from and that a moved invariant
  is an item. That covers the docstring of `gotchas.py`, its row and its range paragraph in the
  memory-tree README, the catalogue section of the HYGIENE template and its render, the two paragraphs
  of the workflows README, and one sentence in the memory-tree-hygiene dossier. The map's generated
  artifacts are re-rendered. Observed by AC10.
- **S13** — The memory-tree and review-harness kit versions and the build harness's own
  `unattended-build@` engine identity each move once, after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. The renders are refreshed and the kickoff manifest's
  `last-audit` is re-stamped. Observed by AC9.

## 3. Non-goals (OUT)

- **The class half is not moved.** Class and universal records keep reading the tree under review,
  because an item can only widen a review (the brief).
- **`render_by_design` keeps its signature and the I4 shape.** `check_by_design_parity.py` calls it
  over synthetic records and the review harness parses its head; neither changes here.
- **The review harness's parsing is not changed.** `tier2-review.template.js` moves only on its
  version line. A moved invariant reaches it as an ordinary item and the new header lines as preamble.
- **A caller's own `checklist` or `byDesign` argument is not checked.** A caller's word is the
  caller's authority, exactly as a caller's `byDesign` already is. Whether a resolver agent returned
  the checker's stdout unaltered cannot be verified in the restricted runtime, and the build harness
  already says so in its WHAT THIS DOES NOT CHECK line.
- **No skeptic-side guard.** Telling skeptics to distrust a by-design entry whose record the diff
  touches would need the record's path, which the I4 entry line does not carry, and it would rest on
  agents rather than on a check.
- **`base` stays optional on the build harness.** Making it required would refuse every caller that
  omits it today; the stage warns instead (§3 Edges).
- **The by-design head spelled in several places is not consolidated here.** That is unit 32's M2.
- **BUILD-METHOD M6's "always exits 0" is not edited.** It was already false for a range git refuses,
  which exits 1 through a traceback today, and the governance carrier is edited by no unit of this
  build. The memory-tree README, which M6 points at, states the refusal.
- **No new gate leg** (shared invariant 5). Every arm rides `gotchas selftest`, the review suite's or
  the build-harness suite's existing leg.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-3` — the `invariant` kind, `render_by_design` and the
  by-design block the review harness cuts out of `checklist`; without them there is no block to read
  at a base.
- **consumes-from** `TOOL-aGraftedHelix-28` — the parity checker imports `gotchas.py` and calls
  `render_by_design`; this unit keeps that call working, so the parity leg keeps its verdict.
- **hands-off** external — the unattended skill names `scratch` among the build harness's arguments
  and never `base`, so a caller that omits it gets a spec audit whose checklist WARNs that it read the
  working tree. Telling that caller to pass the run's pinned BASE is left outside this build.

## 4. Design

### Evidence

Read at `018b5675`, the rotated run's pinned base. `git diff --stat 018b5675..9024901c` lists four
build records only, so the code read is the code at the run's tip.

- `tools/memory-tree/gotchas.py:566` defines `cmd_for_diff`. It lists the range's paths with
  `git diff --name-only` through `run`, which sets `check=True`, so a bad range raises
  `CalledProcessError`. `main` at `:893` catches only `Problem`, so that is a traceback. Measured on
  node `a`: `--for-diff nosuchrev..HEAD` prints one.
- `cmd_for_paths` at `tools/memory-tree/gotchas.py:526` takes every invariant from `records`, which
  walks the working tree at `:248`, selects it by its anchors, and prints `render_by_design` at
  `:549`. No input names a revision.
- `tools/workflows/tier2-review.template.js:372` cuts the block out of `checklist` into `byDesign`,
  and `:930` tells every skeptic to refute any finding a by-design entry covers. The harness holds no
  filesystem, so it can only trust what its caller hands it.
- The build harness's resolver prompt at `tools/workflows/unattended-build.template.js:1138` runs
  `AUDIT_CHECKLIST <paths>`. `base` at `:280` defaults to the empty string and is otherwise only
  echoed into the return. `checklistFrom` is set at `:1152` and logged at `:1279`.
- `tools/drift-audit/drift_report.py:1175` reads a whole tree at one sha with one `git ls-tree` and
  one `git cat-file --batch`, parsing the batch as bytes. It is another kit's file and cannot be
  imported (shared invariant 2), so the PATTERN is reused, not the function.

### Hits and near-misses over the real tree

Run on node `a` on 2026-10-05 against the checker as it stands.

- **The live hit.** `--for-diff c3ef67429fef..a49d53d5`, the closing review's range, prints
  `# by design — 3 invariant(s) this selection touches`. All three records are paths in that range's
  `--name-only` list, and `git grep -l '^kind: invariant' c3ef67429fef -- memory/gotchas/` finds
  none, so the fixed checker prints a block of 0 and three items there (AC5).
- **A near-miss that must not move.** `--for-paths tools/unattended/unattended.sh` selects
  `concurrent-runs-are-announced-not-refused`. That record is unchanged since `018b5675`, so with
  `--base 018b5675` the block must stay 1 and no item may print (AC6).
- **A near-miss with no invariant.** `--for-diff 018b5675..HEAD` touches four build records and
  prints a block of 0 today; it must print a block of 0 and no item afterwards.

### The base

`resolve_range_base(root, rng)` returns a full sha. Splitting on `...` first and then `..`, it runs
`git merge-base <left> <right>` for the three-dot form, `git rev-parse --verify <left>^{commit}` for
the two-dot form, and the same on the whole string for a single revision. An empty side reads as
`HEAD`. A range or side that opens with `-` raises `Problem` before any git call, and a failed call
raises `Problem` naming the range, never `CalledProcessError`. `cmd_for_diff` calls it after its
`git diff --name-only`, which also moves inside the same `Problem` wrapping, and the `-` refusal runs
before both.

### Reading the records at the base

`load_records_at(root, m, sha)` returns the base's records and the paths that did not parse.

1. `git ls-tree -z <sha> -- <m>/gotchas/` lists the catalogue's direct entries. It keeps blobs ending
   `.md` that are not `INDEX.md`, the same population `records` lists. An empty listing means the
   base predates the catalogue: zero records, no error.
2. One `git cat-file --batch` reads every kept blob. The output is parsed as BYTES by the header's
   size field and decoded `utf-8` with `replace`, with CRLF folded to LF as `read` does, because a
   text-mode read would misalign the sizes on any multibyte character.
3. Each text goes through `build_record(rel, text)`. A `Problem` from one record adds its path to the
   unparsed list and the walk continues.

`build_record` is the body of the loop in `records` today, returning the same keys plus `text`, the
normalised text, which S6's comparison reads. `records` keeps raising on a working-tree record that
does not parse, as it does today.

### Selection, items and the block

`cmd_for_paths(root, conf, paths, label, noun, base=None, changed=None)`. With `base` unset it
behaves as today and adds S5's working-tree header line. With `base` set:

- The class and universal selection is unchanged, from `records`.
- `derive_moved_invariants(recs, at_base, changed, paths, m)` returns the records to itemise: every
  record of kind `invariant` in either list whose path is in `changed`, and whose own path is in
  `paths` or whose anchors in either list select one of `paths`. Each is named from the working
  tree's record where one exists and from the base's otherwise, sorted by path. `m` is the memory
  root, which `selectable` takes to exclude the catalogue.
- The block is every `invariant` record in `at_base` whose path is not in `changed` and whose base
  anchors select one of `paths` through `selectable`, rendered by `render_by_design`.
- For `--for-diff`, `changed` is the normalised `--name-only` list, the same list as `paths`. For
  `--for-paths --base`, it is derived as S6 says.

The own-path clause is what keeps the anchors from deciding. Under `--for-diff` a moved record's
path is always one of `paths`, so a range's moved ruling is itemised whatever anchors it wrote, and
the change cannot choose whether its ruling is reviewed. The anchor clause only matters under
`--for-paths --base`, where the subject is a set of files rather than a diff: it keeps an invariant
the build moved for some unrelated file off a checklist about these, and such a record exempts
nothing either way, because the block is read at the base.

`selectable` excludes every path under the catalogue, so the own-path clause tests membership
directly and never goes through it.

The output order is the two existing header lines, then the new header lines, the class items, the
S4 items, and the block last. The block must stay last: `extractByDesign` ends it at the first line
not opening `- `, and anything after it would continue the last item.

### The header lines

Each is a constant in `gotchas.py`, opens `# `, and so is preamble to the review harness and a head
line to `renderChecklistUnion`. None opens `# by design —`, so neither the harness's pattern nor the
parity checker's can mistake one for the block's head.

| constant | printed |
|---|---|
| `INVARIANTS_AT_BASE` | `# invariants are read at <sha12>; <n> that this subject adds, edits or takes out are listed as items, never by design` |
| `INVARIANTS_UNPINNED` | `# invariants are read from the working tree; with no --base, a record this subject adds or edits can stand as by design` |
| `INVARIANTS_UNPARSED` | `# <n> record(s) at <sha12> did not parse, so none of them is by design: <paths>`, printed only when `<n>` is above 0 |
| `MOVED_INVARIANT_ITEM` | `- [ ] NEW/CHANGED invariant <name> — verify the ruling before treating it as by design` |

### `--for-paths --base`

`main` reads `--for-paths --base <rev> <path>...`. A `--base` with no revision or no path after it
prints the usage line and exits 2. The revision goes through `resolve_range_base` as a single
revision. The changed set compares each record's `text` at the base with the working tree's record
of the same path, so an edit, a new untracked record and a record taken out of the working tree all
count. A base record that did not parse counts too: the working tree's records all parse, or
`records` refuses, so its base text cannot equal a working-tree record of the same path.

### The build harness

In `tools/workflows/unattended-build.template.js`, beside `AUDIT_CHECKLIST`, a constant `auditBase`
holds `base` when it matches `/^[0-9a-f]{7,40}$/`, the shape `badSubject` already tests, and `''`
otherwise. The resolver prompt runs `AUDIT_CHECKLIST + (auditBase ? ' --base ' + auditBase : '') +
' <paths>'`. When the resolver's checklist is taken, `checklistFrom` gains ` at base <first 12>`, and
when it is taken with `auditBase` empty the stage logs `WARNING: the audit's checklist reads
invariants from the working tree — no pinned \`base\` was passed, so an invariant this build added
can stand as by design`. That is the one route on which the audit's by-design block is the stdout of
the `--for-paths` this stage asked for: a caller's own `checklist` is the caller's authority (§3),
and a resolver that returned none already logs its own `WARNING:`. The per-pass `CHECKLIST` and the
spec commit's `--for-diff` are ranges already and are not changed.

The build-harness suite gains three arms beside GH3: with a 40-hex `base` added to the `NOSUBJ`
args, the resolver prompt carries `--for-paths --base <that sha> <paths>` and the log line names the
base; with no `base`, the prompt carries `--for-paths <paths>` and the `WARNING:` line prints; with
`base` set to `origin/main`, nothing is forwarded and the `WARNING:` prints. The existing GH3 prompt
arm keeps its verdict, because its fixture passes no `base`. `FLOOR_ASSERTIONS` rises by the arms
added, if the suite holds one.

### The consumer arm

The review suite holds only `node` today. Before node runs, a new block resolves the memory-tree
kit's `gotchas.py` the way `check-protocol-parity.test.sh` does, through the `MEMORY_TREE_DIR`
override or `resolve_kit_dir`, with inlined canonical copies of `resolve_python` and
`resolve_kit_dir`. It builds a two-commit fixture repository under the suite's own `TMP`:

1. a `.memory-tree.conf` naming `MEMORY_ROOT=memory`, a fixture script, and invariant `bd-base`
   anchored on that script;
2. a second commit adding invariant `bd-new`, anchored on the same script, and editing the script.

It runs `--for-diff HEAD~1..HEAD` there and writes the stdout to a file the node runner reads. The
node arms feed that stdout as `checklist` and assert three things. The run logs `by-design: 1
invariant(s) from the checklist's by-design block`. Every lens prompt carries `bd-base` under the
intended-behaviour label, and no prompt's by-design text names `bd-new`. Exactly one lens's
checklist share carries `NEW/CHANGED invariant bd-new`.

A producer that cannot be resolved FAILS the block and names why. The kit's self-tests ship nowhere,
as `tools/workflows/kit.toml` withholds them, so the one tree that runs this suite always holds the
memory-tree kit, and an absence there is a defect rather than an adopter's choice.
`FLOOR_ASSERTIONS` rises by the assertions added.

### Inventory

| identifier | where | cell |
|---|---|---|
| `resolve_range_base`, `load_records_at`, `build_record`, `derive_moved_invariants` | `gotchas.py` | `py.function` |
| `INVARIANTS_AT_BASE`, `INVARIANTS_UNPINNED`, `INVARIANTS_UNPARSED`, `MOVED_INVARIANT_ITEM` | `gotchas.py` | constant |
| `auditBase` | `unattended-build.template.js` | constant |

Each function name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
on 2026-10-05 and answered OK. No codebase-map inventory key is minted: the functions feed
`memory/map/generated/` only, and no file is added.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/README.md`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`, by the render
- `tools/memory-tree/check-memory-hygiene.sh`, the version constant only
- `tools/memory-tree/BUILD-METHOD.template.md`, `tools/memory-tree/SPEC-TEMPLATE.template.md` and
  `tools/memory-tree/ANNOTATION-STYLE.template.md`, the version marker only
- `memory/guides/BUILD-METHOD.md`, `memory/TEMPLATE-SPEC.md` and `memory/guides/ANNOTATION-STYLE.md`,
  line 1 by the render only
- `memory/gotchas/inputs-inside-the-subjects-reach.md`
- `memory/gotchas/INDEX.md`, by `gotchas.py --write`, in a `Pass: none` records commit after the
  build commit: `--dispatch` refuses the index declared beside its generator (check 49), as it did
  for unit 3, which rode its index re-render the same way
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`, by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/tier2-review.template.js`, the version line only
- `tools/workflows/tier2-review.js`, by the render
- `tools/workflows/README.md`
- `memory/map/features/memory-tree-hygiene.md`
- `memory/map/generated/`
- `memory/guides/SESSION-KICKOFF.md`, the `last-audit` line only

### Rollout

1. Factor `build_record` out of `records`, then add `resolve_range_base`, `load_records_at`,
   `derive_moved_invariants` and the constants, and wire `cmd_for_diff`, `cmd_for_paths` and `main`.
2. Graft the AC1 to AC4 arms onto a scratch copy of the parent's `gotchas.py` and observe each
   `arm FAIL`, then observe them `arm ok` on the built file.
3. Edit the build-harness template, render it with the parity leg's `--render` mode, and add S9's
   arms. Observe each red on a scratch copy of the render with the `--base` forward cut.
4. Add the consumer block to the review suite, and observe it red with `MEMORY_TREE_DIR` pointing at
   a scratch directory holding the parent's `gotchas.py` and `tree_lib.py`.
5. Edit the class record, run `gotchas.py --write`, and write the README, HYGIENE template and
   dossier sentences.
6. Bump the three versions once. memory-tree moves in every carrier `tools/check-kit-versions.sh`
   pairs, which is more than the epoch check's own remedy names. Render with
   `adopt-memory-tree.sh --render` and the parity leg's `--render`, then run
   `python tools/codebase-map/gen_map.py --write`.
7. Re-stamp `last-audit` in the kickoff manifest, because the version constant sits in
   `tools/memory-tree/check-memory-hygiene.sh` and the marker on `memory/guides/BUILD-METHOD.md`,
   both in its `watch:`. The manifest body is not edited, so `last-body-change` does not move.

Unit 32 also writes `tools/workflows/unattended-build.template.js` and the review-harness version
line. Its order is 16 and this unit's is 13, so the passes run in sequence, as this build's rules make
every pass do, and each bumps once after its own last move.

### Alternatives rejected

- **Rendering at the base only the records the range changed.** It still lets a base record the
  range did not touch be read from an uncommitted working-tree edit. Reading every by-design entry at
  the base is one rule, and AC2's uncommitted-edit arm is the test that separates the two.
- **Itemising a moved invariant by its anchors alone.** The anchors are what the same change wrote,
  so a range could choose whether its own ruling is reviewed. AC1's arms put the moved record's own
  path in the range, which is the case the own-path clause decides.
- **Itemising every moved invariant under `--for-paths --base` too.** Over a long build that lists
  every ruling the build moved on every spec's audit checklist, whatever file the spec touches, and
  none of them can exempt anything there.
- **One `git show <base>:<path>` per record.** A spawn per record is the cost
  `memory/gotchas/process-creation-is-the-suite-cost.md` prices, against two spawns for the batch.
- **`git archive` of the catalogue directory.** It honours `export-ignore`, so an attribute could
  drop records from the base silently, and its failure on a missing path is an exit code to
  interpret rather than an empty listing.
- **A fixture-string arm in the review suite.** The harness treats a `- ` line as an item whatever
  it says, so an arm fed a typed copy of the new output passes on the parent as well; it would only
  restate unit 3's arms (§8 F2).
- **Leaving `--for-paths` as an open item.** §8 F1.

## 5. Production-readiness checklist

- security — This narrows what a by-design block can exempt and widens no write surface. Every git
  call takes an argv list and never a shell. S7 closes the option-injection path a caller-supplied
  range has today, where `--output=<file>` reaching `git diff` writes a file. The base sha passed to
  `ls-tree` and `cat-file` is the 40-hex value git returned.
- perf / scale — PINNED on node `a`, 2026-10-05: today's `--for-diff` over the closing review's
  185-file range took 0.56 s wall; `git rev-parse` with `git ls-tree` took 0.22 s; `git ls-tree` with
  one `git cat-file --batch` over the 100-record catalogue took 0.19 s. The added cost is three
  spawns per call, estimated under 0.5 s and UNVERIFIED until built.
- error / empty / loading states — A base with no catalogue reads zero records. A base record that
  does not parse is announced and exempts nothing. A bad range or revision is a named refusal at
  exit 1, and `--for-paths --base` with nothing after it is a usage line at exit 2.
- observability — The header line names the base and the item count on every `--for-diff` and every
  pinned `--for-paths`. An unpinned `--for-paths` says so in its header, and the build harness logs
  the base or a `WARNING:`.
- risks — Every caller's stdout gains a header line. The review harness reads it as preamble and
  `renderChecklistUnion` keeps it as a head line. A frozen spec's criterion that `--for-diff` output
  is byte-identical to its BASE output belongs to a closed build and is not re-run.
- testing — `--selftest` arms red on the parent, two real-tree observations, the build-harness arms,
  and an end-to-end arm in the review suite, each observed red on a staged break.
- migration — None. An adopter receives the behaviour on update. A range whose base predates the
  `invariant` kind prints a block of 0 and itemises every invariant the range added.
- user docs — The memory-tree README, the HYGIENE template and its render, the workflows README, the
  `gotchas.py` docstring and the memory-tree-hygiene dossier.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --selftest` runs at the pass's commit, it
  prints `PASS — gotchas: all arms held`, and three new arms print `arm ok`. A range that adds
  invariant `inv-new` anchored on the fixture script it also edits, over a base holding `inv-one`
  anchored on that script, prints a head of 1 whose only line is `inv-one`'s, and prints
  `- [ ] NEW/CHANGED invariant inv-new` before the block. A range that edits `inv-one` prints a head
  of 0 and its item. A range that takes `inv-one` out prints a head of 0 and its item, named from the
  base text. Each arm was observed `arm FAIL` once against a scratch copy of the parent's
  `tools/memory-tree/gotchas.py` with the arms grafted in.
  Red when: an invariant the range added or edited is counted in the head or printed in the block.
  cost: the self-test builds a scratch repository per fixture; its leg's ceiling is 300 s, and it was
  not timed for this spec.
- **AC2** — When `python tools/memory-tree/gotchas.py --selftest` runs at the pass's commit, four
  more arms print `arm ok`. With the range editing only the fixture script and an uncommitted edit to
  `inv-one`'s `## Actually` in the working tree, the block line carries the committed text. A
  three-dot range from a side branch that added invariant `inv-side` anchored on the script resolves
  its base through the merge base, so the block holds `inv-one` and not `inv-side`. A range whose
  base commit has no `memory/gotchas/` directory, and which adds the catalogue with an invariant
  anchored on the script it edits, prints a head of 0 and itemises that invariant. A base record
  whose front matter does not parse, fixed by the range, prints the `INVARIANTS_UNPARSED` line naming
  it, stays out of the block and is itemised. Each was observed `arm FAIL` against the grafted parent.
  Red when: a block line is rendered from working-tree text, a three-dot base is read at the left
  side, or a base without a catalogue or with an unparseable record refuses or exempts.
- **AC3** — When `python tools/memory-tree/gotchas.py --selftest` runs at the pass's commit, three
  more arms print `arm ok`. `cmd_for_paths` given a base, over a working tree that added `inv-new`
  uncommitted since that base, prints a block holding `inv-one` alone and the `inv-new` item. Without
  a base it prints the `INVARIANTS_UNPINNED` line. `--for-paths --base` with no revision exits 2 with
  the usage line. Each was observed `arm FAIL` against the grafted parent.
  Red when: an uncommitted invariant reaches the pinned block, or the unpinned form says nothing.
- **AC4** — When `python tools/memory-tree/gotchas.py --for-diff nosuchrev..HEAD` runs, it exits 1,
  its stdout opens `HYGIENE gotchas:`, and neither stream carries `Traceback`. When
  `python tools/memory-tree/gotchas.py --for-diff --stat` runs, it exits 1 with a `HYGIENE gotchas:`
  line naming the leading `-`, and prints no diffstat. Two `--selftest` arms assert the same two
  refusals inside a fixture, the second with `--output=` aimed at a file in that fixture, which must
  not exist afterwards.
  Red when: a bad range tracebacks, or a range opening with `-` reaches git.
  fixture: the CLI half uses `--stat` because it writes nothing if it does reach git, so a
  regression observed from the repository leaves no file behind; the write-capable option is
  exercised only inside the self-test's fixture.
- **AC5** — When
  `python tools/memory-tree/gotchas.py --for-diff c3ef67429fef8327a8854a17a77d14e19b39b7fd..a49d53d5700dc9e4229784334528e7475313acc9`
  runs at the pass's commit, it prints `# by design — 0 invariant(s) this selection touches`, an
  `INVARIANTS_AT_BASE` line naming `c3ef67429fef` and 3, and three `NEW/CHANGED invariant` items for
  `canary-waits-on-a-rendezvous-not-a-clock`, `concurrent-runs-are-announced-not-refused` and
  `sweep-issues-no-cost-verdict`.
  Red when: the head still reads 3, as it does at `018b5675`.
  figure: the 3 is PINNED, measured on 2026-10-05 at `9024901c`; both shas are ancestors of the
  run's branch, so the range does not move.
- **AC6** — When
  `python tools/memory-tree/gotchas.py --for-paths --base 018b5675 tools/unattended/unattended.sh`
  runs at the pass's commit, its block reads 1 and names
  `concurrent-runs-are-announced-not-refused`, and it prints no `NEW/CHANGED invariant` item. The
  same command without `--base 018b5675` prints the `INVARIANTS_UNPINNED` line and the same block.
  Red when: an invariant that did not move since the base is itemised or left out of the block, or
  the unpinned form prints no header line.
- **AC7** — When the build-harness suite's GH3 block and its new arms run as a slice inside the kit
  directory, behind the suite's prologue, three outcomes hold. A 40-hex `base` makes the resolver
  prompt carry `gotchas.py --for-paths --base <that sha> <paths>`, and the log carries
  `checklist from --for-paths over 2 path(s) at base` and that sha's first 12 characters. No `base`
  keeps `gotchas.py --for-paths <paths>` and prints the `WARNING:` naming the working tree. A `base`
  of `origin/main` forwards nothing and prints the same `WARNING:`. Each new arm was observed red on
  a scratch copy of `tools/workflows/unattended-build.js` with the `--base` forward cut, and
  `FLOOR_ASSERTIONS` is raised by the arms added where the suite declares one.
  Red when: a pinned base never reaches the checker, or an unpinned audit is silent about it.
  permission: the whole suite is the main loop's, run once at VERIFYING; a pass runs the slice.
- **AC8** — When the review suite's new by-design range block runs as a slice inside the kit
  directory, behind the suite's prologue, it logs
  `by-design: 1 invariant(s) from the checklist's by-design block`, every lens prompt carries
  `bd-base` under the intended-behaviour label, no prompt's by-design text names `bd-new`, and one
  lens's share carries `NEW/CHANGED invariant bd-new`. With `MEMORY_TREE_DIR` pointing at a scratch
  directory holding the parent's `gotchas.py` and `tree_lib.py`, the block reds because `bd-new`
  reaches `byDesign`. `FLOOR_ASSERTIONS` is raised by the assertions added.
  Red when: an invariant a range adds reaches the review harness's `byDesign`.
  permission: the whole suite is the main loop's, run once at VERIFYING; a pass runs the slice.
- **AC9** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, its `memory-tree` and `review-harness` lines read `clean` at the bumped versions,
  and `bash tools/check-kit-versions.sh` exits 0. Line 3 of `tools/workflows/unattended-build.js`
  carries an engine identity one minor step above its value at the parent.
  `git diff <the pass's parent sha> -- memory/guides/BUILD-METHOD.md` changes line 1 only, and
  `bash skills/session-kickoff/manifest-check.sh` exits 0.
  Red when: a kit's shipped bytes moved and a carrier kept the old version, a render differs from
  its template, or the manifest stamp is stale.
  figure: every version is DERIVED from the parent at observation time, because sibling units move
  the same lines.
- **AC10** — When `python tools/memory-tree/gotchas.py --check` runs at the pass's commit, it exits 0.
  `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/gotchas.py` prints
  `- [ ] inputs-inside-the-subjects-reach`, which it does not print at `018b5675`.
  `grep -c "NEW/CHANGED invariant" tools/memory-tree/README.md memory/HYGIENE.md tools/workflows/README.md`
  counts at least 1 in each file, `grep -c "It is never a checklist item" memory/HYGIENE.md` prints
  0, and every line of `python tools/codebase-map/test_codebase_map.py` reads `ok`.
  Red when: the class record does not reach a diff of the checker, a document still says an
  invariant is never an item, or the map's generated artifacts are stale.

## 7. Gates

`gotchas selftest` · `memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `python resolver (behaviour + inline parity + idiom ban)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `line length` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `govkit selfcheck` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py --selftest · the parent gotchas.py with the arms grafted in · none
New arm: tools/workflows/unattended-build.test.sh · a render copy with the --base forward cut · the suite's FLOOR_ASSERTIONS where it declares one
New arm: tools/workflows/tier2-review.test.sh · MEMORY_TREE_DIR at a scratch copy of the parent gotchas.py · the suite's FLOOR_ASSERTIONS

The kit self-tests are not on the bar. A pass runs AC1 to AC6, AC9 and AC10 directly and the two
slices of AC7 and AC8; the main loop runs the whole suites once at VERIFYING.

## 8. Open questions

- **F1 — Is the `--for-paths` spec-audit channel closed here, or named as open?** The review's
  skeptic noted that the fix cures only `--for-diff`, and that `--for-paths` has no range to compare
  against. Option A closes it: `--for-paths --base <rev>`, and the build harness forwards its pinned
  `base`, warning when it has none. Option B adds `--base` but leaves the harness unwired, so the
  one caller that runs `--for-paths` for a review keeps reading the working tree. Option C changes
  nothing and documents the gap. A satisfies the most and leaves the fewest follow-ups. Veto 2 was
  weighed: `--base` is an optional argument on a verb this unit already edits, not a new verb, file,
  kit or install location, and the review itself names the run's pinned BASE as the candidate.
  Veto 3 does not apply, because the change narrows what a block can exempt.
  RESOLVED (agent, 2026-10-05, delegated): option A, as S6 and S9 state.
- **F2 — Where does the consumer-side pin the review's Left-shift line asks for live?** Option A is
  an arm in the review suite fed a typed copy of the new output; the harness treats any `- ` line as
  an item, so it passes on the parent and pins nothing unit 3's arms do not. Option B is an
  end-to-end arm in the review suite that runs the real checker over a fixture range, at the cost of
  two inlined canonical resolver copies and a `python` dependency in a `node`-only suite. Option C
  drops the review-suite arm and lets the build-harness arm stand as the consumer pin. B is the only
  option that satisfies the review's line as written, and no veto removes it: python and the
  memory-tree kit are this repository's own, and `check-protocol-parity.test.sh` in the same kit
  already resolves that kit.
  RESOLVED (agent, 2026-10-05, delegated): option B, as S10 and the consumer-arm design state.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the unit 29-32 spec brief and the closing review's H1,
  grounded against `gotchas.py`, the review and build harness templates and both of their suites at
  `018b5675`.
- rev-2 · 2026-10-05 · before the build, against the tree at `489f1ec7`: every §4 Evidence line held.
  Three design lines did not match the code they describe. `derive_moved_invariants` takes the memory
  root, because `selectable` needs it. The S6 changed set counts a base record that did not parse,
  which the comparison by text could not reach. The build harness's `WARNING:` is logged where the
  stage takes the resolver's checklist, the only route its by-design block comes from the command
  this stage ran, so a caller's checklist no longer draws a false warning; S9 says so. And the
  catalogue index rides a records commit, because `--dispatch` refused it beside its generator.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a file's content as it stood at an earlier commit"`
ranked name-stem neighbours only, `read_text` and `read` among them, none of which reads at a
revision. A second probe, `"render the review's by-design list from the invariant records at the
range base"`, ranked `records` in `tools/memory-tree/gotchas.py` first; that is the seam this unit
extends, by factoring its loop body into `build_record`. Both printed `unscanned layers: .sh`, so
their miss says nothing about the shell suites, which were read by hand. The batched-read pattern is
reused from `tools/drift-audit/drift_report.py:1175`, another kit's function and so not imported.
The other seams extended are `cmd_for_paths` and `cmd_for_diff`, `render_by_design` called
unchanged, `AUDIT_CHECKLIST` and the resolver prompt in `tools/workflows/unattended-build.template.js`,
the GH3 block of the build-harness suite, and the MTD resolution of
`tools/workflows/check-protocol-parity.test.sh`, copied as its canonical helpers. Recall surfaced
this build's own records first: the brief, the review's H1, unit 3's spec, and unit 28's parity spec,
which is why `render_by_design` keeps its signature. It surfaced `TOOL-aFoldedQuarry-6`, which made
`--for-diff` stdout the reviewer's checklist, and `TOOL-aWeighedCompass-14`, which is why the audit
runs `--for-paths` over declared paths rather than a kit root. `gotchas.py --for-paths` over the
files touched selected six universal classes and `degradation-known-but-unreported`,
`node-check-is-not-a-syntax-gate` and four more; §4 and §5 answer each, and
`inputs-inside-the-subjects-reach` is the class this unit extends with its own instance.

Recall terms used: by-design invariant exemption base range for-diff for-paths gotchas checklist review-harness tier2-review self-exempt narrows

The question passed with them: "should the review's by-design exemptions be read from the tree under
review or from the base of the range".

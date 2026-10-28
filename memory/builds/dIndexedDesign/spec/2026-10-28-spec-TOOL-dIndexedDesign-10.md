# TOOL-dIndexedDesign-10 — the playbook record kind: its row, its one resolver, the `repeat` route resolving through it, and `check-playbook` as Design's pack

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 13 · closes TOOL-dIndexedDesign-19 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0392@c9f3c2f0 whole
**Carries:** node:record-kind.playbook

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-d.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-d.md) | research | TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-19 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

A playbook is "a design record kind carrying dScriptedRepeat's canon, which an ordinary build authors
and the `repeat` disposition follows" (night pass, point 6; layer-memory.md:419), yet no registry row
names it and no reader answers "is this path a playbook". The unattended kit already holds every part
of the kind's behaviour: the canon derived from the template's section table
(`tools/unattended/check-playbook.sh:60-67`), the declaration block and its two readers
(`declared_list` :268, `declared_scalar` :343), pieces identified by hash (`record_piece`,
`tools/unattended/unattended.sh:13115`, hashing at :13140), sets identified by the ordered piece hashes
(`verb_record_set`, :13231), and amendment by proposal (`verb_propose`, :12940). This unit registers
the kind, gives it one resolver, routes the `repeat` placement check and the recipe preflight through
that resolver, and tags `check-playbook` as Design's pack, so a `repeat` request names a record of a
kind rather than a path that merely exists (ask TOOL-dIndexedDesign-19, gap-flow-17's seat).

## 2. Scope (IN)

- **S1** — The kind's row. `playbook` appended to `tools/memory-tree/record-kinds.toml` through
  TOOL-dTotalRecall-1 S9's factory, `python record_kinds.py new playbook --tag record.playbook
  --writer hand --check "playbook validity gate" --purpose "a playbook: dScriptedRepeat's twelve-section
  canon and its declaration block, followed by a recipe-mode run and by the repeat disposition; its
  pieces and sets identified by hash, amended by proposal"`, with the columns TOOL-dTotalRecall-18 S1
  requires set through that unit's landed verb: layer `layer.memory`, home `**/*.md` (§8 F1), id-rule
  `""` (keyed by its repo-relative path), schema `{ form = "header" }` (§8 F2), lifecycle
  `current-state`, and `readers = []` with `readers-none = "no work-order read key hands a playbook;
  recipe mode and the repeat check read it by the path a README or a placement names"`. Its node is
  `record-kind.playbook`. Build-run precondition: TOOL-dTotalRecall-1 and -18 landed. Observed by AC6.
- **S2** — The one resolver. The population predicate of `tools/unattended/check-playbook.sh:179-197`
  (a tracked `*.md`, not a `*.template.md` and not `PLAYBOOK-TEMPLATE.md`, carrying a
  `^step_selector[[:space:]]*=` line and a `^```toml` line) becomes one function,
  `check_is_playbook <path> <text>`, which returns 0 or prints one reason and returns 1. The population
  loop calls it for each candidate the batched grep selects, its population unchanged. A new mode,
  `bash check-playbook.sh --resolve <path> [--at <sha>]`, reads the path's tracked bytes at `<sha>`
  (default `HEAD`) through the file's pinned reader `GITSHOW` and prints `playbook: <path>` with exit
  0, or `not a playbook: <path> — <reason>` with exit 1, the reason one of `not tracked at <sha8>`,
  `a template is the canon, never a playbook`, `no step_selector line` and `no toml declaration
  block`. A path carrying a newline, a leading `-` or a `..` segment is refused with exit 2 before any
  read. Observed by AC1, AC2, AC3 and AC4.
- **S3** — The recipe preflight through the resolver. `check_authorization`'s recipe arm
  (`tools/unattended/unattended.sh:4183-4210`) calls `bash "$KIT_DIR/check-playbook.sh" --resolve
  "$AUTH_PLAYBOOK" --at "$base"` before it reads the block, and a non-zero exit is `fail 46` carrying
  the resolver's reason line; the arm's own test for a `toml` fence in the read text is folded into
  that call, so the preflight and the leg answer one predicate. The block reads that follow, `outputs`,
  `grain` and `records`, are unchanged. Observed by AC5.
- **S4** — The `repeat` route resolving a record (ask TOOL-dIndexedDesign-19). The `repeat` fact of
  TOOL-dPlacedRequest-4 §4's facts table, as `tools/loop/placement.py`'s `check` evaluates it, moves from
  "the path exists in the tree at HEAD" to "the path resolves as a `record-kind.playbook` record at
  HEAD": `check` runs S2's `--resolve <path> --at HEAD` as a subprocess, the unattended kit's directory
  found through the inline `resolve_kit_dir` block (`tools/lib/resolve_kit_dir.py`), and a non-zero exit
  fails the fact as `repeat · <the resolver's reason line>`; an absent unattended kit fails it as
  `repeat · no unattended kit, so no playbook record can resolve`. The path stand-in
  KICK-dKeptSession-18 S5 declared is pruned in this landing: the facts-table fact and the one
  sentence of `help/loop.md` (KICK-dKeptSession-18 S6) that says a `repeat` names its playbook by path
  until the kind lands now say it names a `record-kind.playbook` record by its path. The fixture of
  `placement.py --fixture` gains the plants `repeat-playbook` and `repeat-not-playbook`. Build-run
  precondition: TOOL-dPlacedRequest-4 and TOOL-dDeclaredLoop-1's page landed. Observed by AC7 and AC8.
- **S5** — `check-playbook` as Design's pack. The `[[gate_leg]]` row `playbook validity gate` in
  `tools/unattended/kit.toml` (:265-270) carries `pack = "design"`, and `tools/gate-legs.json` is
  rendered from it by `python tools/run-gates/leg_factory.py --write` (TOOL-dWitnessedBar-11 S1, S2,
  S8), the manifest key `pack` being PLAY-dOrderedCharter-19 S12's. Build-run precondition: both
  landed. Observed by AC9.
- **S6** — The docs. `tools/unattended/PLAYBOOK-TEMPLATE.template.md` gains one paragraph under "The
  declaration block": a playbook is the registry's `record-kind.playbook`, keyed by its repo-relative
  path, and `check-playbook.sh --resolve <path>` is the one answer to whether a path is one; rendered
  into `memory/guides/PLAYBOOK-TEMPLATE.md` by the kit's adopter render. `KIT_UNATTENDED_VERSION` in
  `tools/unattended/unattended.sh` moves. NOT OBSERVED by a criterion: prose and a version, graded by
  the `kit/dogfood doc parity` and `unattended skill wiring` legs at the close.

## 3. Non-goals (OUT)

- The playbook set record's kind and the set check that reds at the bar: TOOL-dIndexedDesign-11.
- A third reader of the declaration block. `declared_list` and `declared_scalar` exist twice, in the
  driver and the leg, byte-compared by check 28 of `tools/unattended/check-unattended.sh` (:4916-4923);
  the kind's row names the leg as its grader and adds no Python reader (§8 F2).
- Moving any playbook, or a home every new playbook must live under (§8 F1).
- Running recipe mode end to end. gap-flow-17's "run 0 times" is the recipe half: no
  `memory/builds/*/README.md` declares `playbook:` at base, while the leg runs on every bar over the
  kit's fixture (scout D, disagreement 1). The pieces built as units are dScopedBuild's.
- The `STAND_INS` row for `repeat` in `tools/loop/placement.py` (TOOL-dPlacedRequest-4 S8): it holds
  the Design-entry owner-item stand-in, which Design's entry item arms, not the path stand-in.
- A writer door for the kind: TOOL-dTotalRecall-2's door registers one; until then the writer is
  `hand`, an authoring build.

### Edges

- **hands-off** `TOOL-dIndexedDesign-11` — `record.playbook`, the kind whose declared `records` root homes the set record that unit registers and grades
- **consumes-from** external — TOOL-dTotalRecall-1 S9's factory and registry and TOOL-dTotalRecall-18's columns; TOOL-dPlacedRequest-4's `placement.py check` and its fixture; TOOL-dWitnessedBar-11's leg factory with PLAY-dOrderedCharter-19 S12's `pack` key; TOOL-dDeclaredLoop-1's `help/loop.md`; each DEFERRED at base and an ancestor's, built before this build run
- **hands-off** external — dScopedBuild builds a playbook's pieces as units, the recipe half gap-flow-17 names
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 16, each a scope item of that batch unit

## 4. Design

### Evidence

- The population at `4bf0f400d`, by the predicate of S2 over `git ls-files '*.md'`: four files carry
  both lines, the two templates are excluded, and one playbook remains,
  `tools/unattended/playbook.fixture.md`, with its template twin `playbook.fixture.template.md`
  excluded by the `*.template.md` arm (PINNED, measured at writing).
- No build README declares `playbook:` at `4bf0f400d` (`git grep -l '^playbook:' --
  'memory/builds/*/README.md'` prints nothing; PINNED).
- The recipe preflight and the leg disagree today. The preflight admits any text holding a `toml`
  fence (`unattended.sh:4207-4211`), so a README naming `memory/guides/PLAYBOOK-TEMPLATE.md` passes
  that test, while the leg's predicate calls the template the canon and never a playbook
  (`check-playbook.sh:176-178`, :190). S3 closes the disagreement by one predicate.
- `check-playbook.sh` reads a declared glob, `PLAYBOOK_GLOB` (:126), and only prints it (:204); the
  comment at :70-71 says a playbook is also any file matching it. Nothing applies the glob, so the
  resolver does not either; that gap is recorded, not widened here.

### The resolver

```
bash check-playbook.sh --resolve tools/unattended/playbook.fixture.md
playbook: tools/unattended/playbook.fixture.md                              (exit 0)

bash check-playbook.sh --resolve memory/guides/PLAYBOOK-TEMPLATE.md
not a playbook: memory/guides/PLAYBOOK-TEMPLATE.md — a template is the canon, never a playbook   (exit 1)
```

`--resolve` runs before the population block, prints nothing else and exits; it does not source the
project conf, so a conf that fails to source cannot change its answer. `--at` resolves its argument
with `git rev-parse --verify <sha>^{commit}` and refuses with exit 2 when it names nothing. The mode
and `--counts` are mutually exclusive, refused with exit 2 when both are given.

### The callers

| Caller | Today | After |
|---|---|---|
| the leg's population loop, `check-playbook.sh:179-197` | the predicate inline | `check_is_playbook` per candidate |
| the recipe preflight, `unattended.sh:4183-4211` | `GIT show` resolves, a `toml` fence test | `--resolve` at BASE, then the block reads |
| `placement.py check`, the `repeat` fact | the path exists at HEAD (TOOL-dPlacedRequest-4 §4) | `--resolve` at HEAD |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_is_playbook` | shell function, `check-playbook.sh` | `sh.function`, asked at the pass |
| `--resolve`, `--at` | flags of `check-playbook.sh` | none |
| `playbook` | registry row, node `record-kind.playbook` | none |
| `repeat-playbook`, `repeat-not-playbook` | fixture plants of `placement.py` | none |
| `design` | value of the manifest key `pack` | none |

### Files touched (estimate)

- `tools/unattended/check-playbook.sh`: S2
- `tools/unattended/unattended.sh`: S3, and `KIT_UNATTENDED_VERSION`
- `tools/loop/placement.py`: S4's fact and plants
- `help/loop.md`: S4's sentence
- `tools/memory-tree/record-kinds.toml`: S1's row, written by its factory
- `tools/unattended/kit.toml`: S5's `pack`
- `tools/gate-legs.json`: the render of S5, never the edit
- `tools/unattended/PLAYBOOK-TEMPLATE.template.md` and its render `memory/guides/PLAYBOOK-TEMPLATE.md`: S6
- `tools/unattended/check-playbook.test.sh` and `tools/unattended/unattended.test.sh`: the arms of §7

### Alternatives rejected

- **A Python resolver in the memory-tree kit or the loop kit.** It is a third reader of the block, the
  class check 28 exists for; the leg already owns the predicate, and a subprocess call keeps one.
- **Resolve by path existence plus a `toml` fence, as the preflight does.** It admits the canon
  template, the disagreement S3 closes.
- **Key the kind by a minted id.** The README `playbook:` key (`unattended.sh:4044`) and
  TOOL-dPlacedRequest-4 S4's `playbook:` line already carry a repo-relative path; an id would change
  both grammars for no reader that needs one.

## 5. Production-readiness checklist

- security — `--resolve` takes a caller-supplied path: it refuses a newline, a leading `-` and a `..`
  segment before any read, passes the path after `--` to git, and reads only tracked bytes at a
  resolved commit.
- perf / scale — one `git show` per resolve; the population loop keeps its two batched greps.
- error / empty / loading states — each refusal names its reason; an unresolvable `--at` is exit 2,
  never a `not a playbook` answer.
- observability — the resolver's reason line is the text `fail 46` and the `repeat` refusal carry.
- risks — a playbook that passed the old preflight and fails the predicate now refuses at
  authorization; none exists in gov's tree, since no README declares `playbook:`.
- testing — AC1 to AC9 by the pass; the arms of §7 at the close.
- migration — none: the population is unchanged, and no record moves.
- user docs — `help/loop.md`'s `repeat` sentence (S4) and the playbook template (S6); no `help/` page
  covers recipe mode (`help/README.md`).

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-playbook.sh --resolve tools/unattended/playbook.fixture.md`
  runs at the repo root, it prints `playbook: tools/unattended/playbook.fixture.md` and exits 0.
  Red when: the kit's own fixture does not resolve.
- **AC2** — When `check-playbook.sh --resolve` runs on `memory/guides/PLAYBOOK-TEMPLATE.md`, on
  `tools/unattended/playbook.fixture.template.md` and on `README.md`, each exits 1 printing
  `not a playbook:` with the template reason twice and `no step_selector line` once.
  Red when: a template or a file with no declaration block resolves as a playbook.
- **AC3** — When `check-playbook.sh --resolve tools/unattended/playbook.fixture.md --at 741904ee8~1`
  runs, it exits 1 printing `not tracked at`; with `--at no-such-ref` it exits 2; with a path
  holding a `..` segment it exits 2 before any git call.
  Red when: a path absent at the named commit resolves, or a bad ref or a traversal reads as an answer.
- **AC4** — When `bash tools/unattended/check-playbook.sh` runs at the repo root, its population line
  prints `population 1 playbook(s)`, the count before the function's extraction.
  Red when: the extracted predicate selects another population than the inline one did.
  figure: PINNED at `4bf0f400d` by the measurement in §4 "Evidence".
- **AC5** — When `awk '/^check_authorization\(\)/,/^}/' tools/unattended/unattended.sh | grep -c -- '--resolve'`
  runs, it prints at least 1; and in a scratch clone whose fixture build README declares
  `mode: recipe` and `playbook: memory/guides/PLAYBOOK-TEMPLATE.md`, `bash tools/unattended/unattended.sh
  --authorization <slug>` refuses with `fail 46` carrying `a template is the canon`.
  Red when: the preflight authorizes a recipe run over the canon template.
  fixture: a scratch clone under `%TEMP%`, its build README and run-state written by the pass.
- **AC6** — When `python record_kinds.py --check` runs at the pass tip, it lists `playbook` with tag
  `record.playbook`, home `**/*.md`, form `header`, check `playbook validity gate` and its purpose,
  and exits 0.
  Red when: the row lacks a column TOOL-dTotalRecall-16 or -18 requires, or names no leg.
  fixture: the registry is TOOL-dTotalRecall-1's, absent at base until it lands.
- **AC7** — When `python placement.py --fixture --plant repeat-not-playbook` places a `repeat` whose
  `playbook:` names `README.md` and runs `check`, it exits 1 printing `placement: refused — repeat ·`
  and `no step_selector line`; `--plant repeat-playbook`, naming the fixture playbook, passes.
  Red when: a `repeat` naming a path no playbook record holds passes the check.
  fixture: `placement.py` is TOOL-dPlacedRequest-4's, absent at base until it lands.
- **AC8** — When `grep -c 'record-kind.playbook' loop.md` runs in `help/`, it prints at least 1.
  Red when: the page still says a `repeat` routes by a bare path until the kind lands.
  fixture: the page is TOOL-dDeclaredLoop-1's, absent at base.
- **AC9** — When `python -c "import json, sys; print(sorted(l['name'] for l in json.load(open(sys.argv[1], encoding='utf-8')) if l.get('pack') == 'design'))" tools/gate-legs.json`
  runs at the pass tip, it prints a list holding `playbook validity gate`.
  Red when: the pack is spelled through `chunk` or the leg carries no `pack`.

## 7. Gates

`playbook validity gate` · `unattended kit gate` · `unattended skill wiring` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `measure-legs selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-playbook.test.sh · covers AC1 AC2 AC3 AC4 · the `--resolve` cases over the suite's scratch tree, its failing case staged by `check_is_playbook` admitting a `*.template.md` · none
New arm: tools/unattended/unattended.test.sh · covers AC5 · the recipe preflight case with a README naming the canon template, staged by the preflight testing only for a `toml` fence · none

## 8. Open questions

- **F1 — What is the kind's `home`, when a playbook may live at any tracked path?** Options: (a)
  `**/*.md`, membership decided by the declaration block, the home only admitting; (b) a fixed home
  for new playbooks, `memory/builds/*/build/*-playbook-*.md`, the fixture and any adopter's playbook
  left outside the kind; (c) the conf's `PLAYBOOK_GLOB` as the home. RESOLVED (agent, 2026-10-28,
  delegated): (a), rung 3, the most feature-rich survivor: TOOL-dTotalRecall-42 S5 makes the kind
  decide and the home admit, so a home matching many paths misgrades nothing, and every path recipe
  mode and the `repeat` route already follow stays a record of the kind; (b) fails AC1, the kit's own
  fixture sitting outside it, and breaks every adopter's README `playbook:` value; (c) puts a per-repo
  conf value where the registry holds a literal glob (TOOL-dTotalRecall-18 §4 "Columns"), and nothing
  applies that glob today. widens: none · relaxes: none
- **F2 — Which schema form does the row take, when TOOL-dTotalRecall-25 S4's `fence` form requires a
  memory-tree validator and the block's grader is bash in the unattended kit?** Options: (a) `fence`
  with a thin Python validator of the block's key set (scout D, disagreement 7); (b) `fields`; (c) a
  deviation from the clause; (d) `header`, naming the leg as `check`. RESOLVED (agent, 2026-10-28,
  delegated): (d), rung 3: TOOL-dTotalRecall-1 §4 admits `header` for "a grammar its owner grades" and
  names that owner's arm in `check`, which is what `check-playbook.sh` already is; (a) adds the third
  reader of the block that check 28 forbids, and over a `**/*.md` home a `fence` validator would run
  on every Markdown file; (b) is a grammar of `**Key:**` lines, which a playbook does not carry; (c)
  departs from a clause no option fails. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 10, ask TOOL-dIndexedDesign-19, scout D's
  rows 10 and 19 and disagreements 1, 7, 8 and 10, and the sources read at `4bf0f400d`.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seams extended are the leg's population predicate (`tools/unattended/check-playbook.sh:179-197`),
made one function both the loop and the new `--resolve` mode call, and the file's pinned reader
`GITSHOW` (:236); the recipe preflight (`unattended.sh:4183-4211`) and TOOL-dPlacedRequest-4's `repeat`
fact become its callers; TOOL-dTotalRecall-1 S9's factory writes the row and TOOL-dWitnessedBar-11's
factory renders the pack key. `python tools/codebase-map/reuse_lookup.py "register a playbook as a
record kind resolved by its repo-relative path"` ranked name stems (`resolve` in `policy.py`,
`records` in `gotchas.py`, `resolve_kit_dir`), none of which decides whether a path is a playbook;
`resolve_kit_dir` is the seam S4 uses to find the unattended kit. Scout D's lines held at
`4bf0f400d` for `check-playbook.sh` (:60-67, :179-197, :268, :343) and `unattended.sh` (:4044, :12940,
:13115, :13140, :13231); its product list named `tools/loop/placement.py`'s `STAND_INS` row as pruned,
which this spec keeps (§3), since that row holds the owner-item stand-in, not the path one; and its
shared interface 6 said TOOL-dWitnessedBar-12 must list `design` as a pack, where that unit's `pack`
namespace is derived from each distinct `pack` value of the manifest (its §4 table), so no ask is
owed.

Recall terms used: `python tools/memory-recall/query.py "how is a playbook validated and resolved for a repeat request" --terms "playbook record-kind check-playbook declaration block step_selector recipe repeat placement stand-in pieces hash"`

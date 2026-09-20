# TOOL-dDerivedDocket-50 — the kit's own route to the anchor grammar

**Status:** SPECCED · rev-1 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 13

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The one criterion that grades whether a generated build README anchors a foreign id reaches the
recall kit's `anchor_at` through `RECALL_CLI`, a conf key the unattended kit declares and the
memory-tree kit does not, so a memory-tree self-test would resolve its own dependency through a
sibling kit's conf and would take a named skip for ever in any tree that adopted this kit without
that one. Give the kit the declared in-kit route it already half carries, and an arm that reds the
next module reaching for a key the kit does not own.

## 2. Scope (IN)

- **S1** — `resolve_anchor(root, E=None)` in `tools/memory-tree/corpus_ids.py`, the kit's ONE
  public route from a repository root to the anchor predicate. It returns a callable taking one line
  and answering the record id that line DEFINES, or `None`. It is composed from the two accessors
  that already exist rather than from a second grammar: `grammar(root)`
  (`tools/memory-tree/corpus_ids.py:259`), which binds the sibling kit's alternation to THAT root,
  and `_anchor` (`:460`), which is the call into `extract.anchor_at`. `E` is a bundle the caller has
  already resolved; omitted, the route resolves its own. It exists for the one in-kit caller that
  holds one: `walk()` is re-pointed through the route at `:387` and passes the bundle it resolved at
  the top of the same function (`:363`), so `_anchor` ends this unit with exactly ONE call site and
  the walk pays no second conf resolve (§4). Observed by AC1 and AC2.
- **S2** — the refusal, named, reachable, and TRUE for the caller that receives it. The
  installed-check hoists out of `grammar()` into `_check_grammar_installed(why, cure)`, one helper
  holding the ONE raise site and taking the CAUSE and the REMEDY from its caller; both callers share the kit-absent sentence and neither
  inherits the other's cure. `grammar()` passes the cause and cure it writes today, so its message
  stays byte-identical (`tools/memory-tree/corpus_ids.py:272`); `resolve_anchor` passes its own —
  an anchor route was requested, and the remedy is to install the memory-recall kit beside this one,
  because no conf value of this kit turns the call off. A caller that wants a skip rather than a
  refusal catches that one exception type and prints a skip naming the arm and the kit; nothing
  returns a silent `None` for an absent kit, because an absent kit and a line that anchors nothing
  are the same value otherwise. Observed by AC3.
- **S3** — the example-conf parity arm, widened from one engine to the kit's Python modules. The
  memory-hygiene self-test derives every key `tools/memory-tree/*.py` reads out of a dict — the
  `<receiver>.get("KEY")` and `<receiver>["KEY"]` forms over `[A-Z][A-Z0-9_]{2,}`, with the RECEIVER
  UNCONSTRAINED — and asserts each one is declared in
  `tools/memory-tree/.memory-tree.conf.example`, minus a DECLARED exemption list asserted in BOTH
  directions — an exempt name no module reads reds too. The receiver is unconstrained because a
  module reading a SECOND kit's conf cannot bind it to `conf`, that name being taken by the kit's
  own, so a `conf`-anchored derivation is blind to exactly the shape this unit exists to catch
  (§4, measured both ways). The exemption list absorbs what the widening pulls in, which on this
  tree is the `os.environ` reads and nothing else. The derivation REFUSES when it finds no key at
  all, so the arm cannot pass by scanning nothing. It is written in the idiom the same file already
  uses for the shell engine's two populations
  (`tools/memory-tree/check-memory-hygiene.test.sh:2101-2167`), beside them, reading the same
  `EX` example-conf handle (`:2106`). Observed by AC4 and AC5.
- **S4** — `ARMS_FLOORS` declared in `tools/memory-tree/.memory-tree.conf.example`, blank, with a
  header comment in that file's idiom. It is the ONE miss S3's arm finds on this tree (§4, measured),
  it is read by a gate the kit's own descriptor ships (`tools/memory-tree/kit.toml:202`), and an
  adopter cannot discover it today. Blank is the OFF value the reader already honours
  (`tools/memory-tree/check-arms.py:82` and `:212`). Observed by AC6.
- **S5** — unit 15's AC13 re-pointed. Its `fixture:` line names `resolve_anchor` as the route and
  S2's refusal as the arm's skip condition, `RECALL_CLI` leaves that spec, and the paragraph that
  parks H2 leaves with it. That spec's §10 gains one sentence naming the route it now takes, so the
  next reader extends it instead of deriving a second one. That spec's header rev bumps and its §9
  gains the entry, in this unit's commit. Observed by AC7.
- **S6** — the carriers. `memory/map/features/memory-tree-hygiene.md` refreshes the prose of the
  paragraph naming the self-test's project-key arms, because this unit adds one to that population
  and that dossier's `[paths]` globs claim the suite. `memory/map/generated/` is regenerated for the
  new symbol and staged in the same commit as the `.py`, because the pre-commit fast leg runs the
  codebase-map gate whenever a `.py` is staged and refuses a stale or unstaged artifact. Observed by
  AC8.
- **S7** — the assertion floor. `FLOOR_ASSERTIONS` in the memory-hygiene self-test
  (`tools/memory-tree/check-memory-hygiene.test.sh:2460`) is raised to the count that suite's own
  PASS line prints at this unit's commit, re-read and never predicted, which is the rule that
  constant's own header states. Observed by AC5.

## 3. Non-goals (OUT)

- **A cross-kit key BAN.** The obvious wider rule — no kit file may name a conf key another kit's
  descriptor declares — was run over the real tree before it was written here and returns 29 hits
  across nine kits, nearly all of them legitimate integrations (§4, measured). It would red the
  hygiene engine's own `MAP_ROOT` read, which the existing exemption list already carries with a
  reason (`tools/memory-tree/check-memory-hygiene.test.sh:2154`). Turning those into declared
  integrations is a mechanism of its own and is `TOOL-aJoinedCanon-13`'s backlog row, which asks for
  the same widening from the other side. This unit narrows to the kit that has the defect.
- **The shell engine's two populations.** The arms at `:2112` and at `:2144` are untouched.
  S3's arm sits beside them with its own derivation and its own exemption list, because merging the
  two would make one refusal speak for two populations.
- **The merge driver's own route.** `merge-rows.py` reaches the same two accessors through its own
  cached pair (`tools/memory-tree/merge-rows.py:205-216`) and resolves the sibling kit by probing
  two install layouts (`:168-180`), where `corpus_ids.py` derives one path from the tool root
  (`:47`). Both are correct, both are in-kit, and this unit unifies neither: a merge driver runs
  inside git's merge with no conf of its own and is not a caller this route serves. So the kit keeps
  TWO bound pairs after this unit, and only the second one is new-caller territory.
- **`RECALL_CLI` anywhere else.** It stays correct where an unattended-kit file reads it, unit 18 S3
  included: that leg is an unattended-kit file and the key is that kit's own
  (`tools/unattended/kit.toml:92`).
- **The other verbs' inherited cause.** `grammar()`'s message says a pin is set. That is true for
  the `--check` path, which reaches the grammar only behind `armed(conf)`
  (`tools/memory-tree/corpus_ids.py:1246`), and it is already not true for `--report` (`:683`) and
  `--measure` (`:708`), which call `walk()` whatever the pins say. S2 splits the cause where THIS
  unit's own caller makes it false and leaves that older one alone: `--print-defined-ids` degrades
  with its own line rather than showing it (`:856`), and re-causing two more verbs changes output no
  caller of this unit is behind.
- **The kit version.** This unit moves no version marker. `TOOL-dDerivedDocket-36` moves
  `KIT_MEMORY_TREE_VERSION` once for this build, and these bytes ride that move, the same way unit
  13's check-wiring bytes ride unit 9's.
- **The fixture's id family.** Whether a scratch fixture's own ids can be anchored at all is the
  next unit's question, not this one's. This unit decides the ROUTE.

### Edges

- **consumes-from** external — the memory-recall kit's two accessors, `grammar_for(root)`
  (`tools/memory-recall/extract.py:478`) and `anchor_at(line, g)` (`:457`). Without that kit
  installed beside this one there is no grammar, and S2's named refusal is the whole behaviour.
- **hands-off** `TOOL-dDerivedDocket-51` — the root-bound route its fixture conf feeds. That unit
  declares an example family in a scratch tree's own conf, which buys nothing unless the anchor
  predicate is bound to that root rather than to the one the kit is installed in.
- **hands-off** `TOOL-dDerivedDocket-15` — the in-kit route its AC13 takes instead of `RECALL_CLI`,
  and the parity arm that reds a `gen_build_index.py` reading a key the kit does not declare. That
  spec keeps AC13's text until this unit lands, and this unit is what rewrites it.

## 4. Design

### The route

At HEAD the kit reaches the grammar twice and neither reach is a route a caller can take.
`grammar(root)` is public and returns the bundle; `_anchor(E, line)` is private and is the only
thing that turns the bundle into an answer. A caller outside the module therefore either imports a
private name or re-types the one-line call, and `gen_build_index.py` already imports from this
module by the same path (`tools/memory-tree/gen_build_index.py:283-284`), so it would do exactly
that.

```
resolve_anchor(root, E=None) -> callable(line) -> id | None
    E = E if E is not None else grammar(root)   # corpus_ids.py:259, raises when the kit is absent
    return lambda line: _anchor(E, line)
```

The bundle is resolved ONCE and closed over, because `grammar(root)` re-resolves the conf at that
root on every call (`tools/memory-recall/extract.py:478-505`) and a per-line resolve would re-read
a conf file per line of a README. The root is explicit and has no default: the module-level grammar
in the sibling kit binds to the repo the KIT is installed in (`tools/memory-recall/extract.py:68`
and `:106`), which is the measured wrong-root class both modules' docstrings already record, and a
default here would put it back.

The OPTIONAL bundle is what lets `_anchor` keep exactly one call site, and without it AC2 asserts a
call graph this unit does not reach. At HEAD `_anchor`'s only caller is `walk()`
(`tools/memory-tree/corpus_ids.py:387`), which resolved the bundle at `:363` and keeps it for two
further uses — `E.ID` builds the H1 fallback (`:369`) and `E.ID_RE` scans citations (`:395`) — so
`walk()` cannot simply trade `grammar(root)` for `resolve_anchor(root)`, and holding both would
resolve the conf at that root TWICE per walk, which is the cost this design exists to avoid. It
passes the bundle it already holds instead. `root` is then unused, because the bundle IS a binding
to a root: it records `families` and `memory_root` (`tools/memory-recall/extract.py:504-505`) and
never the root it came from, so a mismatch is not checkable here at any price this unit is willing
to pay, and the only caller that passes one resolved it at the top of that same function, twenty-four
lines above the call site this unit re-points.

### The parity arm

The population is DERIVED, never typed, because a hand-kept list of this shape has already been
wrong twice in this same file for the shell engine. The derivation reads every `*.py` beside the
suite and collects the key of every `<receiver>.get("KEY")` and `<receiver>["KEY"]` form over
`[A-Z][A-Z0-9_]{2,}`. An empty derivation is a refusal, in the shape the file's existing arms use
at `tools/memory-tree/check-memory-hygiene.test.sh:2114` and `:2156`.

**The receiver is unconstrained, and that is the load-bearing half.** Every module that reads an
override at all binds it to a dict called `conf` — five of the six, `merge-rows.py` reading none and
reaching the sibling kit's accessor instead. They share one parser
(`tools/memory-tree/corpus_ids.py:170`) and each module's defaults dict names its own keys, so
anchoring the derivation on that spelling reads every key the kit owns and CANNOT read the one shape
this unit exists to stop. A module reaching for a second kit's conf has the name `conf` already
taken by its own, so the line it writes is `ucfg["RECALL_CLI"]`, or any other receiver, and a
`conf`-anchored arm stays green through it. Measured both ways over `tools/memory-tree/*.py` at HEAD
on 2026-09-20: the narrow form yields eleven names, the wide form yields those same eleven plus
three, and none is lost.

The three are environment reads rather than conf keys, and they go on the DECLARED exemption list:
`GOV_BASH` (`tools/memory-tree/corpus_ids.py:309`, `tools/memory-tree/gotchas.py:541`,
`tools/memory-tree/row_grammar.py:647`), `PATH` (`tools/memory-tree/corpus_ids.py:317`) and
`GIT_DIR` (`tools/memory-tree/gen_build_index.py:2666`). Each is read through `os.environ`, which is
a dict like any other and which text cannot tell from a conf — the same reason the sibling list at
`:2154` carries `GOV_PYTHON`, and the reason that list is asserted in both directions.

The widened receiver also reaches the modules' OWN selftest fixture dicts, including a subscript
write such as `c5b["DEAD_PATH_PIN"] = "1"` (`tools/memory-tree/corpus_ids.py:932`). Measured, every
key those carry is already declared, so the population does not move today; a fixture that invents
a key later reds until it is declared or exempted, which is the direction of error an arm of this
kind should have.

The block takes the module directory and the example-conf path as parameters, defaulting to its own
two, so one arm can point it at a scratch directory holding one module and one deliberately
undeclared key. Without that, every arm would grade the real tree and a fixture arm would pass by
grading something it did not build — the reason `tools/check-kit-placeholders.py` carries a `--root`
flag and states it in the same words.

The same run that measured the two receiver forms is the candidate-predicate run the charter asks
for, made before this arm was written. Its CONF half is the table below — eleven keys, exactly one
of them missing from the shipped example. The three environment names above are the remainder of
what the wide form returns, and they are exempt rather than declared.

| Key | Read by | In the shipped example |
|---|---|---|
| `ARMS_FLOORS` | `check-arms.py` | no |
| `CHARTER` | `corpus_ids.py` | yes |
| `DEAD_PATH_EXCLUDE` | `corpus_ids.py` | yes |
| `DEAD_PATH_PIN` | `corpus_ids.py` | yes |
| `DISCIPLINES` | `gen_build_index.py` | yes |
| `FAMILIES` | `gen_build_index.py`, `row_grammar.py` | yes |
| `MEMORY_ROOT` | five modules | yes |
| `ORPHAN_ID_PIN` | `corpus_ids.py` | yes |
| `READ_PATH_WAIVER` | `corpus_ids.py` | yes |
| `ROTATION_MODE` | `row_grammar.py` | yes |
| `UNIVERSAL_BUDGET` | `gotchas.py` | yes |

The figure is DERIVED at observation time by AC4 and AC5 and is pinned here only as the measurement
that justified the scope: it is a reading of this tree on 2026-09-20 at HEAD, not a constant the
build carries. What the arm buys is the defect this unit exists for: a `RECALL_CLI` read from any
module in that directory enters the derivation WHATEVER dict the module binds it to, is a key no row
of that table carries and no exemption names, so it reds, by name, in the suite that grades the kit.

The exemption list ships with those three environment names and nothing else. It is asserted in
both directions, so an exemption naming a key no module reads reds — the rule the sibling list at
`:2154` already states, and the reason a stale exemption is worse than none.

### The one miss

`ARMS_FLOORS` is read by `check-arms.py`, which the kit's own descriptor ships as a gate leg
(`tools/memory-tree/kit.toml:202`), and it is declared only in this repo's conf
(`.memory-tree.conf:478`). An adopter who installs the kit receives the gate and cannot discover its
key. It is declared blank, which the reader treats as no floors at all, so nothing changes for a
tree that never sets it.

The comment beside it names the reader by BASENAME and writes any command as `<kit>/check-arms.py`,
never as a `tools/`-prefixed path. That file travels into an adopter's tree and
`tools/check-install-prefix.sh` grades exactly that class; a kit path spelled at this repo's prefix
resolves to nothing in a tree that installed the kit at the root.

### Rollout

**Order 13, sharing the step with unit 13.** Unit 15 consumes this route and is order 15, so 13 is
the latest step that leaves it in place before its consumer, and every order from 1 to 38 is taken.
Sharing is legal where it matters: check 12 reds a `consumes-from` target whose order is AFTER the
unit that names it, never one that shares it (`tools/memory-tree/check-memory-hygiene.sh:1795`), and
this unit declares no sibling `consumes-from` at all, so that arm has nothing to compare here.
A shared value declares a parallel group, and M6 in `memory/guides/BUILD-METHOD.md` requires
parallel passes only where disjointness is PROVEN. It is not proven for this pair: the write sets do
not intersect — unit 13 writes `.githooks/`, `tools/check-wiring.sh` and `tools/drift-audit/`,
this unit writes under `tools/memory-tree/` — but both passes close their own spec and re-render the
generated index with `python tools/memory-tree/gen_build_index.py --write`, which is clause 3, the
precedent unit 37's §4 Rollout set for order 6. So the pair runs in sequence, which is what the
driver does anyway: dispatch is strictly sequential including within a shared order
(`tools/workflows/unattended-build.js:70`) over a roster sorted by step and then by id as a STRING
(`:314-318`), which puts unit 13 first and this unit second. This unit has no claim on going first
and needs only to precede unit 15.

1. `resolve_anchor`, the hoisted installed-check helper, and `walk()` re-pointed through the route,
   with each arm observed RED against a staged break before it is allowed to pass.
2. The parity arm and the exemption list, run over the real tree, with `ARMS_FLOORS` still missing,
   so the arm is SEEN RED naming that key. It is the only staged break this unit needs, because the
   tree supplies it.
3. `ARMS_FLOORS` declared in the shipped example; the arm goes green on the same tree.
4. Unit 15's AC13 re-pointed, its rev bumped and its §9 entry written, in this unit's commit.
5. The dossier paragraph and `memory/map/generated/`, staged together with the `.py`.
6. `FLOOR_ASSERTIONS` raised to the count the suite's PASS line prints at that commit.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `resolve_anchor` | module function in `corpus_ids.py` | `py.function`; leads with the declared verb `resolve`, checked with `lexicon.py --suggest` |
| `_check_grammar_installed` | module function in `corpus_ids.py` | `py.function`; leads with the declared verb `check`, checked with `lexicon.py --suggest`. `require` is not a row of the table, which is why the helper is not called that |
| the derived key list and the exemption list | shell locals in the self-test | `sh.function` grades function names; a local is graded by no cell |

### Files touched (estimate)

`tools/memory-tree/corpus_ids.py` (S1, S2, and its selftest arms) ·
`tools/memory-tree/check-memory-hygiene.test.sh` (S3, S7) ·
`tools/memory-tree/.memory-tree.conf.example` (S4) ·
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md` (S5) ·
`memory/map/features/memory-tree-hygiene.md` and `memory/map/generated/` (S6). No kit version
marker moves here; see §3.

### Alternatives rejected

- **Declare `RECALL_CLI` in the memory-tree kit's conf and example.** It would make the arm legal and
  keep the route. Rejected: two kits would then own one key name, the adopter would be told to set
  the same path twice, and the charter's own rule is that a sibling kit is a render token rather
  than a literal. The record's own fix names the in-kit seam for the same reason.
- **A new standalone checker for cross-kit keys.** Rejected on cost and on subject: a new leg owes a
  ceiling, a self-test, a testsuite-count line and a descriptor row, and the question it answers is
  already one the kit's own suite asks about its own keys.
- **Return `None` when the sibling kit is absent.** Rejected: `None` is also what a line that anchors
  nothing returns, so every caller would read an uninstalled kit as a clean corpus — the measured
  wrong-root class, one level up.

## 5. Production-readiness checklist

- security — no new input, no new write path. `resolve_anchor` reads a conf and compiles a regex from
  its declared families; the alternation is an allowlist the sibling kit already builds
  (`tools/memory-recall/extract.py:106`), so a hostile conf widens a match and reaches no execution.
- perf / scale — one conf resolve per call instead of one per line, which is the reason the bundle is
  closed over rather than resolved inside the returned callable. The one in-kit caller pays nothing
  at all: `walk()` hands the route the bundle it already resolved, so re-pointing it adds no second
  resolve per walk (§4).
- error / empty / loading states — three states and each is named: the kit is absent, which raises
  S2's refusal; the grammar resolves and the line anchors nothing, which returns `None`; the
  derivation in S3 finds no key, which refuses rather than passing.
- observability — the skip a caller prints names the arm and the kit, so a green suite row can never
  be read as a verified one.
- risks — the parity arm is the risk, in both directions. Under-reading passes by finding nothing,
  which the empty-derivation refusal and the two-direction exemption assertion bound, and which the
  real-tree run before writing it tested by finding a live miss. Over-reading is what the
  unconstrained receiver buys, and it is priced: the `os.environ` names it absorbs are on the
  declared list, and a fixture dict's invented key would red by name rather than pass in silence.
- testing — arms in the corpus-ids selftest for S1 and S2, arms in the memory-hygiene self-test for
  S3 and S4, each observed RED before it is allowed to pass. The suite stays inside its declared
  ceiling on the `memory-hygiene self-test` row of `tools/gate-legs.json`; the added arms are string
  work over files already read by that block.
- migration — none. No conf value changes meaning, and a blank `ARMS_FLOORS` is the state every tree
  that never declared it is already in.
- user docs — none for an adopter beyond the example-conf comment, which is where that file's other
  keys document themselves. The kit README's check list does not change.

## 6. Acceptance criteria

- **AC1** — When the corpus-ids selftest runs over a scratch tree whose conf declares one family, the
  callable that `resolve_anchor` returns answers that tree's own anchored id on a heading line and a
  table row, and `None` on a line that merely cites one.
  Red when: the returned callable is bound to the repo the kit is installed in rather than to the
  root it was given, so every id in the scratch tree fails to match and the arm reads clean because
  a clean corpus and an unrecognising grammar are the same empty answer.
- **AC2** — When the same selftest asserts this module's own call graph, derived from its own source
  in the idiom `_walk_continues` already uses (`tools/memory-tree/corpus_ids.py:797`),
  `corpus_ids.py` names `extract.anchor_at` exactly once, at `_anchor`; `_anchor`'s only caller is
  `resolve_anchor`; and `walk()` names `grammar(` exactly once, the bundle it hands to the route.
  Red when: a second call site inside this module re-types the bundle-to-answer step, so a change to
  the grammar's calling convention lands in one of them and not the other; or `walk()` reaches the
  route as `resolve_anchor(root)` with no bundle while keeping its own, so the conf at that root is
  resolved twice per walk (`tools/memory-recall/extract.py:478-505`) — the cost §4 gives as the
  reason the bundle is closed over, paid twice and invisible, because both resolves answer the same.
- **AC3** — When `GRAMMAR_DIR` is pointed at a directory that does not exist and `resolve_anchor` is
  called, in the same arm shape the module already uses for its exit-3 degradation
  (`tools/memory-tree/corpus_ids.py:856`), it raises the kit's `Problem`; the message names the
  memory-recall kit, gives the cause as the anchor route the caller asked for, and prescribes
  installing that kit beside this one; and it names neither `DEAD_PATH_PIN` nor `ORPHAN_ID_PIN`,
  which this caller has not set and which turn nothing off for it. In the same fixture `grammar()`
  raises too, and ITS message is byte-identical to the one at this unit's parent commit.
  Red when: the new caller inherits `grammar()`'s message and is told to blank two pins that are not
  set and do not gate this call, so the refusal states a cause the caller does not have and
  prescribes a cure that is a no-op — which a criterion asking only that A remedy be named certifies
  as correct; or the absent kit returns a callable answering `None` for every line, so an
  uninstalled grammar is indistinguishable from a corpus with no records in it.
- **AC4** — When the memory-hygiene self-test's new block derives the conf keys the kit's Python
  modules read, it names more than zero keys, and it names `MEMORY_ROOT` and `ROTATION_MODE` among
  them; with the block pointed at a fixture directory holding one module that reads one key absent
  from a fixture example conf through a dict named `conf`, it reds naming that key; and with it
  pointed at a second fixture module that reads its undeclared key through a dict bound to any OTHER
  name — `ucfg["RECALL_CLI"]` beside a `conf` of its own, which is the only spelling a second kit's
  conf can take — it reds naming `RECALL_CLI` too.
  Red when: the derivation matches nothing and the arm passes by scanning an empty population, which
  is the shape its two sibling arms in the same file were each written to prevent; or it is anchored
  on the receiver spelling `conf`, so the second fixture passes and the arm certifies only the shape
  that was never at risk — this unit's own defect class, one level up.
  permission: the suite that carries this arm is the `memory-hygiene self-test` leg, held under
  `chunk = selftests`, so its run belongs to the orchestrator's VERIFYING bar and not to this pass.
  Each arm's RED is observed by hand against the staged break above before the pass ends.
- **AC5** — When that block runs over the real kit directory at this unit's commit, every key it
  derives is declared in `tools/memory-tree/.memory-tree.conf.example` or is on the exemption list,
  every exemption names a key some module still reads — the `os.environ` names the unconstrained
  receiver pulls in included, graded in that second direction like any other — and the suite's PASS
  line prints an assertion count at or above `FLOOR_ASSERTIONS` as that constant reads in the same
  commit.
  Red when: the exemption list carries a name no module reads any more, so a stale exemption widens
  the surface the arm was written to narrow.
  figure: the assertion count is DERIVED by re-reading the suite's own PASS line at this unit's
  commit; the floor is raised to that number rather than predicted.
  permission: as AC4 — the same held suite, run at VERIFYING.
- **AC6** — When `ARMS_FLOORS` is read out of `tools/memory-tree/.memory-tree.conf.example` at this
  unit's commit, it is present and blank, and the leg that reads it exits 0 over a SCRATCH tree
  whose conf declares it blank — a fixture, because this repository's own conf declares it non-blank
  (`.memory-tree.conf:478`) and could never exercise the OFF value.
  Red when: it is shipped carrying this repo's own floor string, so an adopter inherits paths that do
  not exist in their tree and the leg reds on arrival naming a gate they never had.
- **AC7** — When unit 15's spec is read at this unit's commit, `RECALL_CLI` occurs zero times in it
  outside its §9 revision log, its AC13 `fixture:` line names `resolve_anchor`, its §10 names that
  route once, and the same spec's §9 carries a new rev entry whose scope names AC13. The count
  reaches §3's consumes-from bullet for this unit, whose prose names the key today, and it stops at
  §9, because the rev entry this criterion also requires is the record of the removal and names the
  key it removed. A whole-file count would red on the one line the criterion demands be written.
  Red when: the route is rewritten and the parked paragraph naming `RECALL_CLI` stays, so the spec
  states two routes and the next reader picks either.
- **AC8** — When the codebase-map artifacts are read at this unit's commit, `resolve_anchor` appears
  in `memory/map/generated/symbols.json` and `_check_grammar_installed` does not, that artifact
  carrying no leading-underscore Python function at all, measured on this tree on 2026-09-20; and
  the dossier `memory/map/features/memory-tree-hygiene.md`
  names the added self-test arm in the paragraph that describes that suite's project-key arms.
  Red when: the artifacts are regenerated in a later commit than the `.py`, which the pre-commit map
  leg refuses, or the dossier keeps prose that describes a population one arm smaller than the one
  that ships.

## 7. Gates

`corpus-ids selftest` · `memory-hygiene self-test` · `memory hygiene` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/memory-tree/corpus_ids.py --selftest` · a scratch tree whose conf declares one family, plus `GRAMMAR_DIR` pointed at a directory that does not exist · none
New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · the real kit directory with `ARMS_FLOORS` still absent from the shipped example, and a fixture directory holding two modules, one reading an undeclared key through a dict named `conf` and one reading another through a dict named anything else · `FLOOR_ASSERTIONS`, raised to the count the PASS line prints at this unit's commit

## 8. Open questions

- **F1 — is `ARMS_FLOORS` declared or exempted?** Declaring it tells an adopter to set a key whose
  only useful value is a list of paths in their own tree; exempting it keeps the shipped example
  shorter and leaves a gate the kit ships reading a key nothing documents.
  RESOLVED (agent, 2026-09-20, delegated): declare it, blank. The kit's descriptor ships the gate
  that reads it, and the file's own stated purpose is that an adopter can discover every key the
  engine reads. An exemption would be the first row of that list to hide a SHIPPED reader rather
  than an environment name, which is the distinction the sibling list at `:2154` is careful about.
  The orchestrator may overturn this without touching anything else in the unit: the arm is
  indifferent, and only S4 and AC6 move.
- **F2 — does the derivation read the module files or import them?** Importing would answer with the
  keys actually read at run time and would execute six modules inside a shell suite.
  RESOLVED (agent, 2026-09-20, delegated): read the text. It is the choice both sibling arms in the
  same file already made, it costs no interpreter, and its blind spot is stated rather than
  discovered: a key assembled at run time from a variable is invisible to it, exactly as a path
  assembled at run time is invisible to the install-prefix gate. The OTHER blind spot a reader will
  look for is not one: a key read through a dict the module does not call `conf` is in the
  population, because the receiver is unconstrained — §4 measures what that costs and AC4's second
  fixture is its failing case.
- **F3 — should the two-direction exemption assertion refuse an EMPTY exemption list?** An empty list
  is the honest state once every derived key is declared.
  RESOLVED (agent, 2026-09-20, delegated): no. An empty exemption list is a legal and desirable end
  state, and refusing it would push a tree into declaring a fake exemption to keep the arm quiet.
  The refusal that matters is the empty DERIVATION, which S3 carries.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from the G3 round-2 spec audit's H2 at its BOUNDED
  exit.
- rev-1 · 2026-09-20 · S1 · S2 · S3 · §3 · §4 · §5 · AC2 · AC3 · AC4 · AC5 · F2 · close-out of the
  same rev, against the promotion pass's verifier's three problems. The parity derivation no longer anchors
  on the receiver spelling `conf`, which measurement showed blind to the only shape a cross-kit conf
  read can take, and the environment names the widening absorbs are declared; AC4 gains the fixture
  that fails without it. `resolve_anchor` takes an optional resolved bundle and `walk()` is
  re-pointed through it, so AC2's call-graph assertion is inside the scope that reaches it instead
  of describing a graph nothing moves. The installed-check hoists into one helper taking a cause and
  a remedy per caller, so the new route stops inheriting a refusal whose pin cause and pin cure are
  both false for it, and AC3 grades the remedy the CALLER can act on. §4 Rollout states the shared
  order and what is and is not proven about it. The route, the measured table, S4's `ARMS_FLOORS`
  ruling and every other criterion are unchanged. The close-out's own verifier then corrected three
  measurements in the same rev: the receiver paragraph said all six modules read a `conf` dict when
  `merge-rows.py` reads none, S1 and §4 put `walk()`'s resolve three lines above the call site it is
  twenty-four above, and the empty-derivation refusal was cited as two bare line numbers that resolve
  against the previous paragraph's `extract.py` rather than the suite.

## 10. Reuse audit

The seam exists and this unit extends it rather than adding one: `tools/memory-tree/corpus_ids.py`
already holds `grammar(root)` at `:259` and `_anchor` at `:460`, and
`python tools/codebase-map/reuse_lookup.py "anchor_at grammar_for in-kit route"` ranks
`grammar_for` a SEAM at fan-in 4 and `anchor_at` at fan-in 2, both in
`tools/memory-recall/extract.py`, with `corpus_ids.grammar` at fan-in 1. That last figure is the
map's, and the module's own text carries two calls (`tools/memory-tree/corpus_ids.py:363` and
`:738`) — either reading is small enough to promote cheaply, and the difference is named here
rather than left for a reader to trip over. The dossier
`memory/map/features/memory-tree-merge-driver.md:130` records the same decision for the merge
driver: reach the sibling kit's accessors and never vendor a second copy of the regexes. The
parity arm extends the block at `tools/memory-tree/check-memory-hygiene.test.sh:2101-2167` rather
than minting a checker, and `TOOL-aJoinedCanon-13` is the backlog row that asks for the wider
version of it.

Recall terms used: `kit conf key RECALL_CLI cross-kit literal seam grammar_for anchor_at corpus_ids
memory-tree memory-recall declared route`, passed to
`python tools/memory-recall/query.py "how should one kit reach another kit's grammar without reading a sibling kit's conf key"`.

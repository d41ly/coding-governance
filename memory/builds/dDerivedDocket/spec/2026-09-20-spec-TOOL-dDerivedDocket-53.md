# TOOL-dDerivedDocket-53 — a pinned read pins its conf too

**Status:** CLOSED · rev-1 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-build-TOOL-dDerivedDocket-53-1-acceptance-ledger.md](../build/2026-09-21-build-TOOL-dDerivedDocket-53-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md) | spec-audit | TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-49 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-54 |

<!-- /gen:spec-records -->

## 1. Goal

Unit 15's `--at <rev>` re-points the RECORD reads at a pinned tree and leaves the CONF where it was:
the build-index engine reads `.memory-tree.conf` from the working-tree root, before mode dispatch, so
a pinned read mixes a pinned tree with evaluation-time declarations. Unit 18's §8 F3 resolves a fork
by asserting that a READY call at a pinned rev is a pure function of pinned inputs, and its S8
re-runs that call later and requires equality — a property nobody specified and the conf read breaks.
Give the kit one conf read that can be pinned at a rev, so the DECLARATIONS a pinned answer evaluates
come from that rev, through the kit's one parser, without an enumeration of which keys a grade
depends on.

That is what S1 buys and it is less than reproducibility from the rev alone, which this Goal used to
claim. Pinning the conf moves where a conf-DERIVED path looks without pinning what sits there: the
README contract registry joins the root, `conf["MEMORY_ROOT"]` and `CONTRACT_REGISTRY` and reads the
working-tree file, refusing when it is absent
(`tools/memory-tree/gen_build_index.py:1313-1320`, reached by its callers in the engine). Which of
those reads a pinned READY actually makes is unit 15's `--at` to decide, so the residual is named
rather than absorbed: this unit pins the declarations, and routing the remaining conf-derived
filesystem reads under a pinned rev stays that unit's. Unit 18's S8 equality rule is restored in the
part that depends on declarations and no further.

## 2. Scope (IN)

- **S1** A conf reader in `tools/memory-tree/gen_build_index.py` that takes a rev and returns the
  parsed conf from `.memory-tree.conf` AS OF that rev, through `parse_conf`, the kit's one conf
  parser, and through no second grammar. COUNTING how many declarations that parser yielded is not a
  second grammar and is permitted: it reads no line, accepts every spelling `parse_conf` accepts, and
  decides nothing the shell gate could disagree with. The count is of what the BLOB alone yielded,
  taken from a parse into an EMPTY dict and never from the returned conf's size, because `parse_conf`
  MERGES into the caller's defaults and hands them back (§4). The defaults are applied after the
  count. S2's third refusal needs that count, because `parse_conf` itself cannot fail (§4).
  Observed by AC1 and AC5.
- **S2** THREE named refusals, each printing the rev and the path, each textually distinct from the
  other two, and none of them a silent fall back to the working tree: a rev that does not RESOLVE, a
  rev whose tree carries no `.memory-tree.conf` blob, and a blob that yields ZERO declarations. The
  third is graded on the number of declarations `parse_conf` yields from that blob alone, never on
  the bytes and never on the size of the dict it returns, for the reasons §4 gives. Observed by AC2.
- **S3** The conf SOURCE is announced on every pinned read, one line naming the rev it came from, so
  two pinned reads at different revs are distinguishable in the output. The line is a notice and goes
  to stderr, the channel unit 15's §4 already gives its notices. Observed by AC3.
- **S4** The working-tree read is untouched. `load_conf(root)` keeps its name, signature, body and
  callers; the pinned reader is a sibling and not a defaulted parameter on the existing one.
  Observed by AC4.
- **S5** Selftest arms: a fixture repo whose two commits declare one key differently, a rev that does
  not resolve, a rev with no conf blob, a rev whose conf blob declares nothing, and the unchanged
  working-tree path. Observed by AC1, AC2 and AC4.
- **S6** The generated map artifacts are regenerated for the new symbol and staged in the same commit
  as the module. Observed by AC6.

## 3. Non-goals (OUT)

- Building `--at` itself. That mode is unit 15's. This unit builds the read the mode calls and lands
  first so the mode has something to call; it adds no CLI surface of its own.
- Pinning any other module's conf read. The corpus-id reader, the row grammar, the gotchas reader and
  the shell hygiene gate each read the working-tree conf, and every one of them keeps doing so. This
  unit pins ONE read, the one a pinned mode makes.
- Pinning the files a conf VALUE points at. `read_contract_rows` is the instance
  (`tools/memory-tree/gen_build_index.py:1313-1320`): it joins the root to a pinned declaration and
  reads the working tree anyway. Naming the instance is this unit's job so the next reader does not
  have to find one; routing it is unit 15's, because only `--at` knows which reads a pinned mode
  makes.
- Enumerating which conf keys a grade depends on. That is the other half of the fork H5 offered, and
  §4 says why pinning the whole conf makes it unnecessary; nothing here names `ASK_CUTOFF` or
  `BACKLOG_MODE` as a special case.
- Deciding what a caller does when a pinned grade differs from an evaluation-time one. Unit 18's S8
  states the equality rule and keeps its text.
- Rewriting the conf. No key is added, removed or re-valued by this unit, so no adopter conf and no
  shipped example changes.

### Edges

- **consumes-from** external — the kit's ONE conf parser and the current working-tree read at HEAD:
  `parse_conf` imported at `tools/memory-tree/gen_build_index.py:283-284` and `load_conf` at
  `tools/memory-tree/gen_build_index.py:286-291`. Without that single parser this unit would have to
  re-spell a grammar bash and python must agree on, which is the defect that parser exists to close.
- **hands-off** `TOOL-dDerivedDocket-15` — the conf a read under `--at` evaluates, so its S6 print
  modes take their DECLARATIONS from the pinned rev, and the per-invocation cost its §5 prices.
  Without it `ASK_CUTOFF` and `BACKLOG_MODE` stay evaluation-time inputs whatever the rev names. The
  conf-derived filesystem reads that remain are that unit's to route, which §1 and §3 state rather
  than leave for a reader to notice.
- **hands-off** `TOOL-dDerivedDocket-18` — the pinned conf its S8 reads when it re-runs the declared
  producer at the recorded `m-base:`, which is what keeps its `asks-ready:` equality rule from redding
  a record nobody forged, in the part of that rule which depends on declarations.

## 4. Design

### What is unpinned today, measured

At `fb07ca25` the engine resolves its root from the working tree and reads the conf from it before
any mode runs:

```
root = run("git", "rev-parse", "--show-toplevel").strip()
...
conf = load_conf(root)
```

`tools/memory-tree/gen_build_index.py:2764-2768`, with the read itself at
`tools/memory-tree/gen_build_index.py:286-291` joining `root` to `.memory-tree.conf` on the
filesystem. Both are unconditional and both run above the dispatch that would know a rev had been
named. So every declaration a grade rests on is an evaluation-time value, whatever tree the records
come from.

### The pinned read

One function beside `load_conf`, taking a rev and returning the same dict shape. It reads the conf
BLOB at that rev, hands the bytes to `parse_conf` — the same parser the working-tree read uses — and
returns. Three properties, and each is a scope item rather than an implementation note.

- It never falls back. A rev with no conf blob is a refusal naming the rev and the path (S2). A
  fallback here is the whole defect wearing a different hat: the answer would still be
  evaluation-time and would still look pinned.
- It announces its source (S3). A pinned read that prints nothing about where its declarations came
  from is indistinguishable from an unpinned one, and the caller cannot tell a reader who has taken
  this unit's answer from one who has not.
- It is a SIBLING, not a parameter (S4). Adding a defaulted rev to `load_conf` makes every existing
  caller a pinned read that happens to be pinned at the working tree, which is a wider blast radius
  than this finding asks for and gives the shell gate and the python readers two different meanings
  for one function name.

### Why the third refusal counts declarations instead of reading bytes

`parse_conf` CANNOT FAIL. It splits the text on newlines, keeps whatever `parse_conf_line` returns
and silently ignores every line that yields nothing (`tools/memory-tree/corpus_ids.py:170-181`). So a
blob of arbitrary bytes does not raise — it parses to the caller's own defaults with nothing merged
in, the grade then rests on those defaults, and the answer still reads as PINNED. That is the same
defect S2 exists to close, arriving through the one input a fallback ban does not cover.

A refusal that inspected the bytes would be the second grammar S1 bans, and it would re-open the
split the one-parser rule was written to close. A refusal that counts what the ONE parser yielded is
not a grammar at all: it reads no line and accepts everything `parse_conf` accepts. Zero
declarations is the refusal, and that is the whole of the test.

What is counted is what the BLOB yielded, and that is not the size of the dict `parse_conf` returns.
That function MERGES into the caller's defaults and hands the same dict back, and `load_conf` seeds
three keys before calling it (`tools/memory-tree/gen_build_index.py:287`), so a sibling seeded the
same way gets a conf that is never empty however empty the blob was. A reader grading that dict's
size would never refuse: the all-comment blob would come back carrying `MEMORY_ROOT` and the answer
would read as PINNED, which is this refusal's own defect wearing the mechanism meant to catch it.
Parse the blob into an EMPTY dict, count, refuse at zero, and merge the defaults after.

**Stated residual.** A `.memory-tree.conf` that is legally all comments and blank lines refuses under
this rule. That is deliberate and not an oversight: a file declaring nothing cannot pin anything, and
a pinned read that quietly grades on defaults is the thing this unit exists to stop. It is stricter
than the working-tree `load_conf`, which treats an absent file as defaults
(`tools/memory-tree/gen_build_index.py:286-291`), and S4 keeps that reader's bytes unchanged so the
two never have to agree.

### Why the whole conf, and not a named key set

The alternative H5 offered is to name the conf keys a grade depends on, so a caller pins them beside
its own facts and skips BY NAME when they have moved. It works, and it rots. The set has to be
re-derived every time a later unit adds a key that reaches a verdict, it lives in prose beside the
source that owns it, and nothing joins the two — the failure mode the charter's §6 names and the one
this build keeps re-finding in its own specs. Pinning the whole conf needs no enumeration and cannot
fall behind the declarations it covers.

The consequence worth stating plainly: a read pinned at a rev OLDER than a key's introduction sees
that key absent and grades accordingly. That is correct rather than unfortunate. It is what makes a
re-derivation at a recorded base reproduce what the run computed there, instead of re-grading old
inputs by today's rules — which is the equality unit 18's S8 asks for.

### Cost

One additional object read per pinned invocation, whatever spelling the caller picks for it. Whether
that read is its own process or rides the same batch as the record reads is the caller's choice and
changes the figure by one process, not by an order; unit 15's §5 cost line takes whichever it
implements. No number is written here, because the spelling is not settled (§8 F4).

### Rollout

**Order 14, shared with unit 51 and with the WONTDO unit 14.** Unit 15's `--at` calls this reader, so
it must land before order 15, and every order from 1 to 38 is taken — sharing a step is how a
promoted unit reaches a consumer at all, and it is legal so long as this unit is not LATER than the
unit that consumes it. Unit 14 is WONTDO and builds nothing. The real second pass on this step is
`TOOL-dDerivedDocket-51`, promoted the same day and also at order 14, and the pair is NOT disjoint on
M6's clause 1 in `memory/guides/BUILD-METHOD.md`: both write `tools/memory-tree/gen_build_index.py`
and both stage a regenerated `memory/map/generated/` with their own `.py` commit. So the step is a
parallel GROUP that must run in sequence. The roster is handed out ordered by step and then by id,
which puts unit 51 first and this unit second; neither reads the other's output, so either sequence
is correct and the id tiebreak is what decides. Renumbering the build order to give each a solo step
is the orchestrator's call and not a unit's. Nothing earlier in the build reads or writes
`tools/memory-tree/gen_build_index.py`'s conf seam, so no order below 14 is required either.

Dark by construction. The reader has no caller at this unit's commit and no mode reaches it; the
selftest arms are its entire exercise until unit 15 lands `--at`. Every existing read keeps its
bytes (S4), so no verdict anywhere in the tree changes at this commit.

### Inventory

One python function in `tools/memory-tree/gen_build_index.py` and three refusal messages for S2. No
new conf key, no new mode, no new gate leg. The identifier is RECORDED here rather than left for the
build pass to invent, so the naming leg and `spec tokens (a spec's own names resolve)` both have a
name to grade before the function exists. On 2026-09-20,
`python tools/lexicon/lexicon.py --suggest read_conf_at_rev --as py.function` answered OK.

| Identifier | Cell | Verb, and why |
|---|---|---|
| `read_conf_at_rev` | `py.function` | `read`: it pulls bytes from a named source, the conf blob at that rev, and hands them to the one parser rather than parsing them itself |

`.lexicon.conf:23` declares `py` a `parser` coverage mode and `.lexicon.conf:418` declares the
`py.function snake` cell, so `lexicon naming predicates` (`tools/gate-legs.json:1052`, guarded on
`tools/`) grades this identifier at this unit's commit whether or not the spec claims the leg. §7 now
claims it, which is the leg §4 was already deferring its naming verdict to.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` and its selftest · `memory/map/generated/` regenerated for the
new symbol and staged in the same commit as the module, because the pre-commit fast leg runs the
codebase-map gate whenever a `.py` is staged and refuses a stale or unstaged artifact.

### Alternatives rejected

- **A named key set the caller pins beside its facts.** The rotting enumeration above. It also leaves
  every future key unpinned by default, so the property degrades silently as the build adds keys.
- **A defaulted rev parameter on `load_conf`.** One name, two meanings, and every caller in the kit
  silently becomes a pinned read. S4 refuses it.
- **Reading the conf at the rev with a second, local parser.** The one-parser rule exists because six
  readers held an identical naive body while the shell gate sourced the same file, so a legal
  spelling bash accepted and python mis-read removed coverage with the gate still green
  (`tools/memory-tree/gen_build_index.py:278-284`). A second grammar here would re-open it.

## 5. Production-readiness checklist

- security — the reader takes a rev and a tracked path and returns parsed declarations. It executes
  nothing from the rev and writes nothing, so a rev naming a hostile tree buys a caller no more than
  a conf it could have read by hand.
- perf / scale — one object read per pinned invocation, priced in §4. The working-tree path keeps its
  current cost exactly, because it keeps its current bytes.
- error / empty / loading states — S2's THREE named refusals are the whole of this row: a rev that
  does not resolve, a rev whose tree carries no conf blob, and a blob yielding no declaration each
  name themselves rather than degrading to the working tree. Bytes `parse_conf` mis-reads are not a
  fourth state and cannot be one: that parser cannot fail (§4), so the zero-declaration count is the
  only refusal reachable for them, and no criterion here asks for a content check.
- observability — S3's source line, on every pinned read, on stderr.
- risks — a caller that reads the pinned conf and then re-reads a working-tree value for one key,
  which reintroduces the mix one key at a time. Nothing here can see that; it is why S4 keeps the two
  readers visibly separate rather than merging them behind one name. And S2's zero-declaration
  refusal refuses a legally all-comment conf, which §4 states as a deliberate residual rather than
  leaving it to be met.
- testing — the arms of S5, all over scratch fixture repos inside the module's own selftest; no arm
  reads this repo's conf, so the arms cannot be satisfied by whatever gov happens to declare today.
- migration — none. No stored shape and no declaration changes, and the working-tree path is
  byte-identical.
- user docs — N/A — this unit adds no user-facing surface. The mode that calls it is unit 15's and
  its page is that unit's to write.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, a new arm builds a
  fixture repo whose two commits declare one conf key differently, and the pinned reader at the OLDER
  rev returns the older value while the working tree holds the newer one.
  Red when: the reader joins the key's path to the working-tree root, so the rev changes nothing and
  the arm returns the same value for both revs.
  new arm: staged RED first. The arm may not pass until it has been SEEN RED with the working-tree
  read standing in for the pinned one.
- **AC2** — When the selftest in `tools/memory-tree/gen_build_index.py` points the pinned reader at
  each of three revs in turn — one that does not resolve, one whose tree carries no
  `.memory-tree.conf`, and one whose `.memory-tree.conf` blob is all comments and blank lines — it
  refuses each time naming the rev and the path, returns no conf, and the arm asserts the three
  refusal texts are distinct from one another.
  Red when: the reader falls back to the working tree, so a rev predating the file grades with
  today's declarations and the answer still reads as pinned; or the all-comment blob parses to the
  caller's defaults and returns, so a conf declaring nothing grades on defaults while the answer
  still reads as pinned, which `parse_conf` cannot raise on
  (`tools/memory-tree/corpus_ids.py:170-181`); or the zero test is applied to the dict `parse_conf`
  returned rather than to the blob's own declarations, so the caller's seeded defaults
  (`tools/memory-tree/gen_build_index.py:287`) keep it non-empty and the all-comment blob passes every
  arm; or the three refusals print one text, so an operator cannot tell a rev that does not exist from
  a tree that carries no conf.
  new arm: staged RED first for the zero-declaration blob, because a reader that simply returns what
  `parse_conf` handed it passes every other arm in this criterion.
- **AC3** — When the pinned reader in `tools/memory-tree/gen_build_index.py` runs in the selftest
  fixture, its source line names the rev, and the arm asserts that line is written to stderr rather than to the mode's own output stream.
  Red when: the pinned read is silent about its source, so a caller cannot tell a reader that took
  this unit's answer from one that did not; or the notice lands on stdout, where it joins a
  machine-read projection.
- **AC4** — When `git grep -c "def load_conf(root: str) -> dict:"` runs over
  `tools/memory-tree/gen_build_index.py` at this unit's parent and at its commit, it returns 1 at
  both, and the selftest's existing working-tree arms pass unchanged.
  Red when: `load_conf` gains a rev parameter, so every caller in the kit becomes a pinned read that
  is pinned at the working tree.
- **AC5** — When `git grep -c "parse_conf"` runs over `tools/memory-tree/gen_build_index.py` at the
  two commits, the commit returns MORE than the parent, and no new conf-line regex is added by the
  same diff.
  Red when: the pinned reader re-spells the conf grammar locally, so two parsers disagree on a legal
  spelling and the gate stays green while coverage leaves.
- **AC6** — When the module is staged, `memory/map/generated/symbols.json` carries the new symbol and
  is staged in the same commit.
  Red when: the artifact is stale or unstaged, so the pre-commit fast leg refuses the commit the unit
  is trying to make.
  permission: the codebase-map coverage leg over the real tree is run at the build's one post-build
  bar, not by this pass.

## 7. Gates

`build-index selftest` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `python tools/memory-tree/gen_build_index.py --selftest` · a two-commit fixture repo whose
conf differs in one key, a rev that does not resolve, a rev carrying no conf blob, a rev whose conf
blob declares nothing, and the unchanged working-tree read · none

## 8. Open questions

- **F1** — Pin the conf, or name the keys a grade depends on? Options: (a) read the whole conf at the
  rev; (b) enumerate the grade-bearing keys so a caller pins them beside its facts and skips by name
  when they have moved.
  RESOLVED (agent, 2026-09-20, delegated): (a). (b) is a hand-kept list beside the source that owns
  it, it has to be re-derived whenever a later unit adds a key that reaches a verdict, and it leaves
  every future key unpinned by default. (a) needs no enumeration and restores the property unit 18's
  §8 F3 already asserts.
- **F2** — What happens at a rev with no conf blob? Options: (a) a named refusal; (b) the shipped
  defaults; (c) the working tree.
  RESOLVED (agent, 2026-09-20, delegated): (a). (c) is the defect. (b) is worse than it looks,
  because a defaulted conf grades and looks pinned, and the caller has no way to learn that nothing
  was read. The G7 fold extended that same ruling to the two neighbouring inputs S2 now names, an
  unresolvable rev and a blob yielding no declaration, because (b) is exactly what each of them
  degrades to and the reason for refusing is the same one.
- **F3** — Does the pinned read replace the working-tree read everywhere, or only where a rev is
  named? Options: (a) a sibling reader; (b) a defaulted parameter on `load_conf`.
  RESOLVED (agent, 2026-09-20, delegated): (a), written into S4. (b) gives one name two meanings and
  makes every caller a pinned read, which is a blast radius this finding does not ask for.
- **F4** — Is the conf blob read as its own process, or does it ride the same object read the pinned
  RECORD reads already make? The figure differs by one process per invocation and the answer belongs
  to whatever spelling unit 15's `--at` implements, since that is the only caller that makes both
  reads. Left OPEN: nothing in this unit's scope depends on it, and §4's cost paragraph is written so
  that either answer is consistent with it.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from the G3 round-2 spec audit's H5, and the same
  day's promotion close-out: the Rollout named unit 51 as the real second pass on order 14 and the
  pair as NOT disjoint on `tools/memory-tree/gen_build_index.py` and `memory/map/generated/`, after
  the verifier found the step claiming a disjointness nobody proved; and §1, §3 and the two
  hands-off edges narrowed the claim from a pinned answer reproducible from the rev alone to the
  declarations only, naming `read_contract_rows` as the conf-derived read this unit does not pin.
  Extended on the same pass, same base and rev, by the G7 round-1 spec audit's fold · M3 (8) · S1, S2,
  S5, §4, §5's error and risks rows, AC2, §7 and §8 F2 · §5 promised three refusals where S2 declared
  one, and the third of them was unbuildable through S1's one-parser rule because `parse_conf`
  (`tools/memory-tree/corpus_ids.py:170-181`) cannot fail. The route taken is the widening one: S2
  now declares three refusals, the unparseable case is replaced by a ZERO-DECLARATION count on the
  one parser's own output, §4 says why a count is not a second grammar, and the all-comment conf is
  stated as a deliberate residual.
  M4 (21) · §4's Inventory and §7 · §4 deferred a naming verdict to the python cell while §7 did not
  list `lexicon naming predicates`, and §4 named no identifier for that leg or for `spec tokens` to
  grade. §7 lists the leg and §4 records the identifier with its `--suggest` answer.
  The verifier pass that followed tightened M3's mechanism (S1, S2, §4, AC2): the zero test counts the
  declarations the BLOB yielded, parsed into an EMPTY dict, because `parse_conf` merges into the
  caller's defaults and `load_conf` seeds three of them
  (`tools/memory-tree/gen_build_index.py:287`) — so a reader grading the returned dict's SIZE would
  never refuse the all-comment blob this refusal was added for, and the mechanism would have carried
  the defect it names.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "reading a declared conf at a pinned revision instead of
the working tree"` ranks `load_conf` as a SEAM at fan-in 15, naming ten modules that hold one, with
`parse_conf` beside it at fan-in 4. That is the seam this unit extends, and it extends it by adding a
sibling rather than by changing the seam's own shape (S4). The probe's own header prints
`unscanned layers: .sh`, so the shell gate that sources the same conf file is outside the corpus it
ranked; that gate is untouched here and §3 says so.

Recall terms used: `python tools/memory-recall/query.py "which tree supplies the conf when a reader is
pinned at a revision, and can a pinned read be a pure function of that rev" --terms "load_conf
.memory-tree.conf ASK_CUTOFF BACKLOG_MODE --at pinned rev gen_build_index working-tree root cutoff
evaluation-time purity"`. It returned the recorded root-resolution failures under an inherited
`GIT_DIR`, which are why the working-tree read resolves its root the way it does and why this unit
leaves that resolution alone.

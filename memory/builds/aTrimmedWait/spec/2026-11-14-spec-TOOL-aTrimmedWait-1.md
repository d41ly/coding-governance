# TOOL-aTrimmedWait-1 — `unattended.sh --check-specs` refuses, before the spec commit and through `--dispatch`'s own predicates, every spec defect `--dispatch` refuses from the spec files alone

**Status:** INPROGRESS · rev-1 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md) | research | TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 |

<!-- /gen:spec-records -->

## 1. Goal

`--dispatch` refuses a unit whose spec is MISSING, THIN, carries a malformed `order` verb, or sits
in a build whose consumes-from edges are unreadable or cyclic. It refuses only when the unit is
dispatched, after the spec was committed and often after a builder was spawned, and the measured
session paid about 30 h of re-dispatch for it. This unit adds one read-only driver verb that makes
those five refusals over the specs as they stand in the worktree, tracked or not, through the
functions `--dispatch` itself calls. The spec stage and the spec writer run it before the spec
commit, so the same defect is refused while its author can still fix it.

## 2. Scope (IN)

- **S1** — The spec-file refusals of `verb_dispatch` become two shared functions:
  `check_unit_spec`, holding the MISSING, THIN and own-order refusals, and `check_edge_shape`,
  holding the unreadable-edge and cycle refusals. `verb_dispatch` calls both where the inline code
  stands today, so its refusals, their texts and their order are unchanged. Observed by AC3.
- **S2** — A new inline verb, `unattended.sh --check-specs <slug> <unit> [<unit> ...]`, grades each
  named unit with `check_unit_spec` and the build once with `check_edge_shape`, over the build's
  tracked and untracked specs. It prints every refusal it finds, each in `--dispatch`'s own words
  under check 49, and exits 1. Clean, it prints one line naming the units and exits 0. It needs no
  run-state file. Observed by AC1, AC2 and AC4.
- **S3** — The build harness's spec stage runs the verb twice: each writer's prompt tells it to run
  the verb over its own group's units before returning and to fix what it prints, and the commit
  stage runs it over every authored unit before its git block and returns `committed: false` with
  the verb's output when it exits non-zero. Both edits land in the template and its rendered copy.
  Observed by AC5.
- **S4** — The `gov-spec-writer` role text tells the writer to run the verb when its task names
  the command, and to fix every refusal it prints before returning. The rendered agent file is
  regenerated. Observed by AC6.
- **S5** — The verb is documented: its usage line in the driver header, its entry in the verbs
  guide and its installed twin, and a usage anchor on `help/roles.md`. Observed by AC7.

## 3. Non-goals (OUT)

- No change to what `--dispatch` refuses, in what order, or in what words. The order gate, the
  consumes-from producer refusal, the hold gate, the chain gate, the `--writes` refusals and the
  spec-token check all read run state or the whole tree, and none of them is a spec-file defect.
- No spec-token check in the new verb. The writer already runs `check-spec-tokens.py --spec` over
  its spec, and `--dispatch`'s own token check stays where `TOOL-aSmoothedDispatch-21` put it.
- No FORKED refusal. `--dispatch` does not refuse FORKED, so the verb does not either.
- No sibling-order refusal. `--dispatch` refuses a sibling's malformed `order` verb only while
  dispatching an ordered unit; the verb grades each named unit's own header instead, so a sibling is
  graded when it is named.
- No change to the commit stage's git block, `commitBlock`, which its real-git suite arm extracts
  and runs in a fixture holding no driver. The verb runs as its own step before that block.
- No pre-commit hook wiring. The hook is unit 3's file.
- No change to the disposal stage, whose promoted specs the caller commits.
- No change to the `gov-spec-writer` gate allowlist in `tools/roles/house/policy.toml`. The verb's
  argv is no gate leg, so the role gate admits it already (§4 "The role gate").
- No kit version bump. The build's rule moves versions once, after the last code move.
- The spec-commit refusal on a build README carrying `status: OPEN`, `TOOL-aSmoothedDispatch-14`.

### Edges

none

## 4. Design

### What the code does today, read at `846d51d3`

All citations are to blobs at the base, which the branch tip `a25c84fc0` holds unchanged.

- `verb_dispatch` (`tools/unattended/unattended.sh@95b8f8404cc3:14492`) loads the build's TRACKED
  specs with `load_spec_facts $(GIT ls-files -- "$MEMORY_ROOT/builds/$slug/spec/*.md")` (`:14517`),
  then refuses in this order, each through `fail 49` and `return 1`:

| Line | Refusal | Predicate |
|---|---|---|
| `:14519-14522` | MISSING: no spec carries the unit's id | `SPEC_PATH` from `load_spec_facts` |
| `:14523` | the fork cutoff cannot be read, check 86 | `load_fork_cutoff` |
| `:14524-14527` | THIN | `plan_state` |
| `:14542-14546` | the unit's own `order` verb is malformed | `order_verb_of` |
| `:14631-14634` | a consumes-from line yields no id | `scan_consumes_cycles` |
| `:14635-14638` | the build's consumes-from edges form a cycle | `scan_consumes_cycles` |

- Between the own-order refusal and the edge scan sit the order gate, the terminal note, the
  producer set and the roster read (`:14547-14620`), all reading run state or the README. The edge
  scan's arguments are every id `unit_ids_of` lists that `SPEC_PATH` resolves (`:14621-14624`), and
  `unit_ids_of` reads the generated units region, sorted (`:4852-4857`).
- Each refusal text occurs once in the driver: `grep -n` over the five distinctive phrases at the
  base finds exactly the five `fail 49` lines above.
- The harness already composes driver commands from its rendered `DRIVER` constant
  (`tools/workflows/unattended-build.js@996b9ed7b25b:600`), for `--plan`, `--review`,
  `--record-round` and `--chain-verdict`. The writer prompt's always-present sentence opens
  `AUTHOR ONLY` (`:1095`). The commit prompt's step 1 finds each id's spec (`:1291`), and a return
  of `committed: false` becomes the stage's refusal (`:1344-1345`).
- A role agent's commands are refused only when one is a gate leg's argv word for word, the gate
  runner or a suite (`tools/hooks/scratch-guard.js@7c31933f6258:1694-1699`, the leg compare at
  `:1628`). `bash tools/unattended/unattended.sh --check-specs ...` is none of the three.
- `git ls-files --others --exclude-standard -- '<build>/spec/*.md'` lists an untracked spec, which
  the tracked listing never does. Observed in a scratch clone at `a25c84fc0`.

### S1 — the two shared functions

```text
check_unit_spec <unit>   -> 0, or 1 after check 49 (86 from load_fork_cutoff); sets _cu_spec, _cu_ord
check_edge_shape <unit> <spec> ...   -> 0, or 1 after check 49
```

`check_unit_spec` reads the `SPEC_PATH` map its caller loaded. It holds lines `:14518-14527` and
`:14542-14546` in that order: MISSING, `load_fork_cutoff`, THIN, then the own-order refusal. It
sets `_cu_spec` to the spec path and `_cu_ord` to `order_verb_of`'s value, so `verb_dispatch`
reads `_d_spec` and `_d_ord` from them and its order gate runs as today. `check_edge_shape` holds
lines `:14625-14638`: one `scan_consumes_cycles` call over its arguments and the two refusals.
`verb_dispatch` builds `_c_args` as today and calls it in their place.

Every refusal text moves verbatim. The variable a message interpolates keeps a name the message
spells as a NAME, never a positional, because `check-arms.py` reads a branch's signature up to its
first interpolation (the convention `check_slug` states at `:3109-3111`).

### S2 — the verb, `check_dispatch_specs <slug> <unit> ...`

1. `check_slug` on the slug (check 1).
2. No unit given: `fail 14 "--check-specs was given no unit id, so it would grade nothing and
   print what a clean build prints: $slug"`, and return 1.
3. `load_spec_facts` over the tracked listing `verb_dispatch` reads, then the untracked listing,
   `GIT ls-files --others --exclude-standard` over the same pathspec. The tracked paths come first,
   so a tracked spec wins an id two files carry, as it does in `verb_dispatch`.
4. For each named unit, `check_unit_spec "$unit"`, continuing to the next unit after a refusal. A
   check-86 refusal stops the verb, because every later unit would refuse the same way.
5. Once, `check_edge_shape` over every id `SPEC_PATH` holds that matches `^[A-Z]+-<slug>-[0-9]+$`,
   sorted with `sort -u` as `unit_ids_of` sorts, each with its spec path. Once the spec commit
   renders the index, the generated region lists exactly these ids, so `--dispatch` scans the same
   set in the same order.
6. With no refusal, print
   `unattended: --check-specs <slug> — <units>: none carries a refusal --dispatch makes from its spec files`
   and return 0. Otherwise return 1; the `fail` lines are already printed.

The argv loop gains a `--check-specs` arm beside `--plan`'s. It takes the slug, then every bare
word up to the next `--` flag as a unit, calls `refuse_waive_unless_preflight --check-specs`, then
`check_dispatch_specs`, and exits with its status. The verb joins `VERBS_INLINE`
(`tools/unattended/unattended.sh@95b8f8404cc3:118`), so `--help` lists it and the run log journals
it under the git dir like every verb but `--plan` and `--version` (`:15276-15279`). It reads no
run-state file and writes nothing in the worktree.

### What the verb does not check

- A refusal `--dispatch` makes from run state, the README or the whole tree (§3).
- A sibling's malformed `order` verb, unless that sibling is named.
- A spec under `spec/` whose H1 parses to no id. It is MISSING for whichever unit it was meant to
  carry, exactly as `--dispatch` sees it.
- What the spec commit does next. A spec that passes here can still be refused by the commit's
  hooks or by `--dispatch`'s run-state refusals.

### S3 — the spec stage

Both edits go into `tools/workflows/unattended-build.template.js`, written through `DRIVER`, and
into its rendered copy `tools/workflows/unattended-build.js`, which differs from the template only
in its install placeholders.

- **The writer prompt.** One sentence after the `AUTHOR ONLY` sentence, outside every
  `roles.specWriter` conditional, so typed and untyped writers both receive it. `gUnits` is the
  group's unit list the writer's closure already holds:

  ```js
  'Before you return, run `' + DRIVER + ' --check-specs ' + slug + ' ' +
    gUnits.map(function (u) { return u.id }).join(' ') + '` in ' + repo + '. It prints each ' +
    'refusal `--dispatch` would make from your specs, in its own words; fix every one naming a ' +
    'unit of yours, and name any other in your summary. ' +
  ```

- **The commit prompt.** Step 1 gains a closing sentence: after finding each spec, run
  `DRIVER + ' --check-specs ' + slug + ' ' + authoredIds.join(' ')` in the repo; when it exits
  non-zero, run nothing further and return `committed: false` with its stdout in `why`. The
  existing refusal at `:1344-1345` then names it. `commitBlock` is not touched.

### S4 — the writer's instructions

`tools/roles/agents/gov-spec-writer.agent.md` gains one bullet under "How you design", after the
spec-token sentence: "When your task names the unattended driver's `--check-specs` command, run it
before you return; it prints each refusal `--dispatch` would make from your specs, in its words,
and you fix every one naming a unit of yours." The text names no kit path, because the install-prefix
leg reds a kit segment followed by a file (`TOOL-dPavedRoad-1`, commit `59c386425`).
`python tools/roles/render_agents.py --write` regenerates `.claude/agents/gov-spec-writer.md`.

### The role gate

The writer and the committer run the verb as `bash tools/unattended/unattended.sh --check-specs
...`. `checkGateLeg` compares a command to each leg's argv at equal length, word for word, and no
leg runs the driver: the only legs naming the unattended kit run `check-unattended.sh` and
`adopt-unattended.sh --check` (`tools/gate-legs.json`). The verb is neither the runner nor a suite,
so the gate admits it with no allowlist change.

### Docs

- The driver header gains, beside `--check-commit` (`tools/unattended/unattended.sh@95b8f8404cc3:34`):
  `#   unattended.sh --check-specs <slug> <unit> [<unit> ...]   # --dispatch's spec-file refusals, before the spec commit`.
  Check 26 of the kit gate joins the new flag to this line and to a suite arm.
- `tools/unattended/VERBS.template.md` gains a `--check-specs` entry after `--plan`'s, saying: it
  makes `--dispatch`'s five spec-file refusals over the tracked and untracked specs, through the
  same functions and in the same words, needs no run-state file, and is what the spec stage runs
  before the spec commit. `memory/guides/UNATTENDED-VERBS.md` takes the identical edit; the pair
  is byte-identical at the base and check 10 of the kit gate compares them.
- `help/roles.md`, section "How to use it", gains a sentence that a spec writer runs
  `unattended.sh --check-specs <slug> <unit>` before returning and the spec commit refuses on it,
  with the anchor `<!-- usage: verb:unattended.sh:--check-specs <fingerprint> -->`, the
  fingerprint read from `python tools/govkit/docs_leg.py --fingerprints`. The docs leg reds a new
  member no page anchors, because `memory/project/docs-undocumented.txt` only shrinks
  (`help/docs-leg.md`).

### The pass probe, `$SCRATCH/u1.sh`

`$SCRATCH` is the run's scratch directory. Run the probe from the worktree root. It builds a
fixture repository at `$TEMP/u1`, a short path because a clone under the scratch directory fails on
Windows, holding this repository's two conf files and specs it never commits. Each refusal class
sits in its own build, because the edge scan grades a whole build. The specs' classes were checked
against the base's `plan_state`, `order_verb_of` and `scan_consumes_cycles` while this spec was
written: tA READY with order 1, tB THIN, tC `MALFORMED · order 2x`, tD unreadable, tE the cycle
`TOOL-tE-1 -> TOOL-tE-2 -> TOOL-tE-1`, tG THIN beside a malformed order.

```bash
set -u
G=$(pwd); R="$TEMP/u1"; rm -rf "$R"; mkdir -p "$R"; cd "$R" || exit 2
git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
cp "$G/.unattended.conf" "$G/.memory-tree.conf" . && git add -A && git commit -qm seed
mk() { # slug · seq · header tail · scope body · edges body
  mkdir -p "memory/builds/$1/spec"
  printf '%s\n' "# TOOL-$1-$2 — fixture" "" \
    "**Status:** SPECCED · rev-1 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling$3" "" \
    "## 2. Scope (IN)" "" "$4" "" "## 3. Non-goals (OUT)" "" "### Edges" "" "$5" "" \
    "## 6. Acceptance criteria" "" '- **AC1** — When `x` runs, it prints y.' "" \
    "## 7. Gates" "" '`memory hygiene`' "" "## 8. Open questions" "" "none" \
    > "memory/builds/$1/spec/2026-11-14-spec-TOOL-$1-$2.md"
}
S='- **S1** — a thing. Observed by AC1.'
mk tA 1 ' · order 1' "$S" 'none'
mk tB 1 '' '' 'none'
mk tC 1 ' · order 2x' "$S" 'none'
mk tD 1 '' "$S" '- **consumes-from** TOOL-tD-2 — no backticks'
mk tE 1 '' "$S" '- **consumes-from** `TOOL-tE-2` — one end'
mk tE 2 '' "$S" '- **consumes-from** `TOOL-tE-1` — the other end'
mk tG 1 '' '' 'none'
mk tG 2 ' · order 2x' "$S" 'none'
D="$G/tools/unattended/unattended.sh"
c() { local tag=$1 want=$2 o rc; shift 2; o=$(bash "$D" --check-specs "$@" 2>/dev/null); rc=$?
  echo "$tag rc $rc hit $(grep -cF -- "$want" <<<"$o") fails $(grep -c '^UNATTENDED check' <<<"$o")"; }
c clean   'none carries a refusal --dispatch makes from its spec files' tA TOOL-tA-1
c thin    'for a unit whose spec grades THIN' tB TOOL-tB-1
c order   'spells [· order 2x]' tC TOOL-tC-1
c edge    'Edges block from which no unit id is read' tD TOOL-tD-1
c cycle   'edges form a cycle, so no unit on it can be dispatched' tE TOOL-tE-1 TOOL-tE-2
c missing 'for a unit no tracked spec under this build defines' tF TOOL-tF-1
c every   'UNATTENDED check 49 FAILED' tG TOOL-tG-1 TOOL-tG-2
c nounit  'UNATTENDED check 14 FAILED' tA
c badslug 'UNATTENDED check 1 FAILED' 'a b' TOOL-tA-1
echo "untracked $(git status --porcelain --untracked-files=all | grep -c '^?? memory/')"
```

### Inventory

| identifier | kind | lexicon verb |
|---|---|---|
| `--check-specs` | driver verb, member of `VERBS_INLINE` | — |
| `check_dispatch_specs` | sh function, the verb | check |
| `check_unit_spec` | sh function, shared with `verb_dispatch` | check |
| `check_edge_shape` | sh function, shared with `verb_dispatch` | check |

Each function name was graded `OK` by `python tools/lexicon/lexicon.py --suggest <name> --as
sh.function` at the base. No conf key and no check number is minted; the verb refuses under checks
1, 14, 49 and 86, which exist.

### Rollout

One pass at order 1, before unit 2, because both units edit the `gov-spec-writer` role file and
its rendered agent. The driver suite's `FLOOR_ASSERTIONS` and the harness suite's floor move by the
count of new assertions, and the close confirms each from a real run. The cited line numbers are at
the base and move with this unit's own edits, so the builder finds each site by its text.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/roles/agents/gov-spec-writer.agent.md`
- `.claude/agents/gov-spec-writer.md`
- `help/roles.md`

### Alternatives rejected

- **A new arm in `tools/check-spec-tokens.py`.** It runs at commit time already, but it would grade
  THIN, MISSING, the order verb and the edges with a second, Python copy of four shell predicates.
  The build's rule is that a pre-check calls the driver's own reader, never a copy, and two readers
  of one rule drift: `plan_state`'s own header records the ordinal-keyed reader that disagreed with
  the hygiene engine on every Tier-1 spec.
- **`--dispatch --dry-run`.** `--dispatch` refuses with no run-state file (`check_run_state` at
  `:14497`) and refuses first on the chain verdict, so a dry run could not serve an attended build
  or a spec nobody has committed, which are this unit's two cases.
- **The writer's instructions alone.** An instruction is not a refusal, and the expected
  improvement is that the defect "is refused before the spec commit". The commit step is that
  refusal; the writer's run is the cheap fix loop before it.
- **A line inside `commitBlock`.** Its real-git suite arm runs the block in a fixture with no driver
  and no `.unattended.conf`, so every arm it holds would red. A step before the block refuses with
  nothing staged or rendered just as well.
- **Stopping at the first refusal, as `--dispatch` does.** A writer would then fix one defect per
  run. Reporting every named unit's first refusal and the build's edge refusals costs nothing more.

## 5. Production-readiness checklist

- security — read-only: the verb writes no worktree file and no run state, and its one write is the
  run log under the git dir every verb writes. It runs no command built from spec content.
- perf / scale — one driver start, one `load_spec_facts` over the build's specs, one `plan_state`
  and one `order_verb_of` per named unit, one edge scan. A refused `--release-task` measured 4.748 s
  of driver start at `846d51d39` (the brief), so a run is seconds.
- error / empty / loading states — no unit given refuses under check 14; a malformed slug under
  check 1; an unreadable fork cutoff under check 86, stopping the verb.
- observability — every refusal is `--dispatch`'s own line; a clean run prints one line naming the
  units it graded.
- risks — the edge scan reads every spec in the build folder, so a sibling writer's half-written
  spec can refuse a writer's run. The prompt tells the writer to fix its own units and name any
  other; the commit step then refuses on the sibling, which is the right owner.
- testing — the pass probe above; the driver suite and harness suite arms under §7, observed RED
  then GREEN at the close.
- migration — none: a new verb, and `--dispatch`'s behaviour is unchanged.
- user docs — the driver header, the verbs guide pair and `help/roles.md`, per "Docs".

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/u1.sh"`, the Design section's fenced block,
from the worktree root at the pass commit.

- **AC1** — When `bash "$SCRATCH/u1.sh"` runs, it prints `clean rc 0 hit 1 fails 0`,
  `thin rc 1 hit 1 fails 1`, `order rc 1 hit 1 fails 1`, `edge rc 1 hit 1 fails 1`,
  `cycle rc 1 hit 1 fails 1` and `missing rc 1 hit 1 fails 1`.
  Red when: the verb grades only tracked specs, so every fixture unit reads MISSING and `clean`
  prints `rc 1`; or it carries its own wording, so a `hit` reads 0.
- **AC2** — When `bash "$SCRATCH/u1.sh"` runs, it prints `every rc 1 hit 2 fails 2`,
  `nounit rc 1 hit 1 fails 1`, `badslug rc 1 hit 1 fails 1` and `untracked 8`.
  Red when: the verb stops at its first refusal as `--dispatch` does, so `every` reads `hit 1`; or
  an empty unit list grades nothing and exits 0; or the verb stages or commits a spec, so fewer
  than 8 stay untracked.
- **AC3** — When `grep -c 'for a unit whose spec grades THIN' tools/unattended/unattended.sh` runs it
  prints 1, and the same count over `for a unit no tracked spec under this build defines`,
  `a reader taking its numeric prefix`, `Edges block from which no unit id is read` and
  `edges form a cycle, so no unit on it can be dispatched` prints 1 each.
  `grep -cE '(^|[^_[:alnum:]])check_unit_spec "' tools/unattended/unattended.sh` prints 2, and so
  does the same count over `check_edge_shape "`: one call in `verb_dispatch`, one in the verb. At
  the close the driver suite's existing `--dispatch` arms for these five refusals read green
  unchanged.
  Red when: the verb carries a copy of a refusal beside `--dispatch`'s, so a count reads 2; or
  `verb_dispatch` keeps its inline block, so a call count reads 1.
- **AC4** — When `time bash tools/unattended/unattended.sh --check-specs aTrimmedWait
  TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4
  TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7` runs on node a at the pass's parent
  commit, it prints `UNATTENDED check 14 FAILED — unknown argument`; at the pass commit it prints
  either the clean line or check-49 lines only, and its `real` wall is at most 60 s. The ledger
  records both walls.
  Red when: the verb reads more than the build's specs, a whole-tree scan, and its wall reaches
  minutes as the spec-token check's did.
  figure: 60 s is PINNED as this unit's budget, about 12 times the 4.748 s driver start the brief
  measured at `846d51d39`; both walls are DERIVED at observation.
- **AC5** — When `grep -c "' --check-specs ' + slug" tools/workflows/unattended-build.js` runs it
  prints 2, and the same grep over `tools/workflows/unattended-build.template.js` prints 2. When
  `sed -n '/const commitBlock = \[/,/\]\.join/p' tools/workflows/unattended-build.js | git hash-object --stdin`
  runs it prints `c6ca14b74b2441e87eac15e4094dbbccb49cfa6b`, the hash of the same 21 lines at the
  base. At the close the harness suite reads the writer prompt and the commit prompt carrying the
  command, and a commit double returning `committed: false` with the verb's output refusing by its
  `why`.
  Red when: the sentence sits inside a `roles.specWriter` conditional, so a typed writer never
  receives it; or the step was added to `commitBlock`, so the hash moves.
  figure: the hash is PINNED, computed at `a25c84fc0` over the base's identical bytes.
- **AC6** — When `python tools/roles/render_agents.py --check` runs it exits 0,
  `grep -c -- '--check-specs' .claude/agents/gov-spec-writer.md` prints 1, and
  `grep -cE '[a-z-]+/(unattended|check-memory-hygiene)[.]sh' tools/roles/agents/gov-spec-writer.agent.md`
  prints 0.
  Red when: the role file was edited and the agent not re-rendered, so the check exits non-zero; or
  the sentence names a kit path the install-prefix leg reds.
- **AC7** — When `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs it
  prints nothing, ``grep -c -- '^- `--check-specs`' memory/guides/UNATTENDED-VERBS.md`` prints 1,
  `bash tools/unattended/unattended.sh --help | grep -c -- '--check-specs'` prints at least 2, and
  `python tools/govkit/docs_leg.py --fingerprints | grep -F 'verb:unattended.sh:--check-specs'`
  prints one line naming `help/roles.md`.
  Red when: one guide copy is edited without its twin; or the header line is missing, so `--help`
  lists the verb once; or no help page anchors it, the docs leg's UNDOCUMENTED case.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `scratch-guard self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `roles catalogue` · `roles render wiring` · `install-prefix (shipped surface)` · `docs` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · fixture builds each carrying one refusal class, a clean build and a two-unit build with two refusals, all untracked; staged by making `check_dispatch_specs` return after its first refusal and read tracked specs only, which reds the clean and two-refusal arms · `FLOOR_ASSERTIONS`, raised by the count of new assertions, which the close confirms

New arm: tools/workflows/unattended-build.test.sh · covers AC5 · the writer prompt, typed and untyped, and the commit prompt carry the `--check-specs` command with the right ids, and a commit double returning `committed: false` with the verb's output refuses; staged by deleting the writer sentence and the commit step · the suite's assertion floor, if it declares one, raised by the count

`python tools/check-spec-tokens.py --legs-for` over the files touched, run at `a25c84fc0`, names
the guarded legs above. `docs` reads `help/roles.md`; `install-prefix (shipped surface)` reads the
role text; `harness arms` and the kit gate's check 26 read the new branches and flag. The close runs
the bar once, after the last unit is terminal. This spec's author ran no gate but the memory
hygiene check and the spec-token checker over this file.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft from brief `2026-11-14-prompt-TOOL-aTrimmedWait-1-brief`,
  item 1, grounded at `846d51d3` and read at `a25c84fc0`, whose code is identical. The README's
  "wired into the spec stage and the writer's instructions" is read as both the stage's two prompts
  and the role text, for the reason under Alternatives rejected.

## 10. Reuse audit

The seams this unit extends: the five spec-file refusals of `verb_dispatch`
(`tools/unattended/unattended.sh@95b8f8404cc3:14516-14546`, `:14621-14638`), lifted into two
functions both callers share; their predicates `load_spec_facts`, `plan_state`, `order_verb_of`,
`load_fork_cutoff` and `scan_consumes_cycles` (`tools/unattended/lib-unattended.sh@a3e03db6b9f0:400`),
called unchanged; `--plan`'s inline-verb arm as the parse shape; and the harness's `DRIVER`
constant. `python tools/codebase-map/reuse_lookup.py "refuse a spec that the dispatch verb would
refuse before the spec is committed"` ranked name stems only (`before`, `PolicyRefused`,
`read_spec_revisions`, `parse_spec_h1`), none of which grades a spec as `--dispatch` does, so no
seam fits beyond the driver's own functions. Recall's top hits were the dIndexedDesign reuse scout,
which names `plan_state` and `--dispatch`'s MISSING and THIN refusals at older line numbers
(`:13648-13650`), `TOOL-dTrueNorth-20`'s deviation 6, which added the unreadable-edge and cycle
refusals, and `TOOL-aHoistedPass-6`'s table of what `--dispatch` refuses. The recall records cite
lines that the base places about 870 lines later.

Recall terms used: `python tools/memory-recall/query.py "how can a spec writer check its spec against the dispatch refusals before the spec commit" --terms "dispatch plan_state THIN MISSING order verb malformed consumes-from edges cycle spec commit writer"`

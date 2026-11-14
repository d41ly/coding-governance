# TOOL-aTrimmedWait-2 — hygiene check 12 grades one named spec or one build on request, and the spec writer is told to run it that way

**Status:** SPECCED · rev-3 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 2 · closes TOOL-aSmoothedDispatch-16 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md) | research | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 |
| [2026-11-14-prompt-TOOL-aTrimmedWait-2-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-2-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-2-ruling.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-2-ruling.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

A spec writer checks its spec's format with `check-memory-hygiene.sh --only 12`, which grades all
2991 tracked specs: 401.9 s on node a at `a25c84fc0`, 325.7 s of it CPU. It also never grades the
writer's own spec, because the gate lists tracked files only and the writer does not commit. This
unit lets `--only 12` take `--spec <path>` or `--build <slug>`. Check 12's block, which grades
check 25 too, then grades the named spec or every spec of the named build, tracked or not, and
returns for each the findings the full run returns for it. The writer's role text names that form.
The full run, `--staged` and the bar grade exactly what they grade today.

## 2. Scope (IN)

- **S1** — `check-memory-hygiene.sh --only <sel> --spec <path>` and `--only <sel> --build <slug>`
  are accepted when every id in `<sel>` is 12 or 25. Every other use of either flag refuses with
  exit 2 and grades nothing: without `--only`, beside another check id, beside any further
  argument, on a path check 12's own selector does not select, on an absent file, on a build
  holding no selectable spec, and on a selection the format cutoff leaves empty. Observed by AC3.
- **S2** — Under either flag, check 12's selection is the scope: `--spec` grades the named spec
  and reads the rest of its build's specs for their edges only, as `--staged` reads a staged
  spec's siblings; `--build` grades every spec of the build. Untracked specs under that build's
  `spec/` folder are in the selection. Every per-spec arm runs as on the full run, the `base`
  resolve arm included, and an edge finding is reported when either end of it is graded. Observed
  by AC1 and AC2.
- **S3** — Under either flag the liveness line names the scope:
  `HYGIENE --only <sel> ran checks <ids> over <N> spec(s) of <path or slug>`, and the corpus-wide
  zero-population notices of check 12's block print nothing. Observed by AC1.
- **S4** — The `gov-spec-writer` role text tells the writer to grade each spec it wrote with
  `check-memory-hygiene.sh --only 12 --spec <path>`, and says why the whole-tree gate is the wrong
  tool for it. The rendered agent file is regenerated. Observed by AC5.
- **S5** — The script's header documents both flags beside `--only`. Observed by AC5.
- **S6** — The wall of the writer's command is recorded before and after on node a. Observed by AC4.

## 3. Non-goals (OUT)

- No change to any check's verdict on the full run, under `--staged`, under `--offenders` or under
  `--only` without the new flags. The bar's `memory hygiene` and `memory hygiene (the pass checks)`
  legs run the same argv and grade the same population.
- No scope for any check but 12 and 25. Their block is the one the writer needs, and the
  measurement says it is the whole cost: `--only 11` ran in 19.5 s wall and 2.1 s CPU on the same
  clone, so the producers every `--only` run pays are not the 376 s. <!-- PINNED 2026-11-14 -->
- No change to the producers that run ahead of every check block. They cost the scoped run about
  19 s, and the README asks for seconds. <!-- PINNED 2026-11-14 -->
- No cache of a spec's verdict. Check 12's edge joins read across a build, so a per-spec verdict
  is not a function of the spec's bytes alone.
- No change to the `gov-spec-writer` gate allowlist in `tools/roles/house/policy.toml`. The scoped
  argv is no leg's argv, so the role gate admits it already (§4 "The role gate").
- No change to `--dispatch` or the spec-commit stage. Unit 1 owns those.
- The unbound-variable line under `--staged`, `TOOL-aNimbleMend-21`. It sits in check 23's block,
  which a scoped run never enters.
- No kit version bump. The build's rule moves versions once, after the last code move.

### Edges

none

## 4. Design

### What the code does today, read at `846d51d3`

All citations are to `tools/memory-tree/check-memory-hygiene.sh@f064ddabb88e`, which the branch tip
`a25c84fc0` holds unchanged.

- `--only` is parsed first and refuses any other argument (`:43-59`). `--staged` is read at `:313`.
  Any other unknown argument is ignored: `--spec <path>` alone runs every check today, observed in a
  two-build fixture at `a25c84fc0`.
- `FILES` is `git ls-files "$M/"` (`:316`), so an untracked spec is in no check's population.
- Under `--staged` the narrowing sets `STAGED_SET` to the staged paths and `FILES` to them plus
  every tracked file of their build folders (`:770-808`). `in_scope` admits every file on a full run
  and only `STAGED_SET` under `--staged` (`:810`).
- Check 12's block opens at `:2042`. `c12_all` is `FILES` filtered by the spec-name selector
  (`:2092`), and `pop_guard` reds an empty selection on a full run (`:2093`, defined at `:721`). The
  tagging loop (`:2098-2118`) emits `P` for a graded spec and, under `--staged` with
  `SPEC_EDGES_CUTOFF` set, `J` for a sibling of a staged spec read for its edges (`:2101`). The pass
  awk takes `-v stg="$STAGED"` (`:2125`), and its only read of `stg` is the `base` resolve arm,
  which emits a sha only when `stg == 0` (`:2543`). The edge-join awk takes `-v stg` too (`:2984`)
  and, at 1, reports a finding only when one end of the edge is graded (`:2994`). Eight
  zero-population notices print on a full run only (`:3132-3195`). The liveness line is `:3724`.
- `--staged` reused whole would therefore skip the `base` resolve arm, so a scoped run would pass a
  live spec whose `base` names no commit while the full run reds it. That is why S2 is a scope of
  its own and not `STAGED=1`.

### The measurement

On a clone of `a25c84fc0` at `%TEMP%/tw2`, node a, with sibling writers running beside it: `--only
12` ran 401.9 s wall, 325.7 s user over 2991 tracked specs; `--only 11` ran 19.5 s wall, 2.1 s
user. The brief's reading at `846d51d39` was 376.705 s. Both PINNED. Check 12's cost is CPU in its
selection, about 0.13 s a spec; a build's 10 to 30 specs cost a few seconds above the producers. <!-- PINNED 2026-11-14 -->

### S1 — the parse and its refusals

The `--only` parse admits `$# = 4` when `$3` is `--spec` or `--build`. It stores `SCOPE_KIND`
(`spec` or `build`) and `SCOPE_ARG`, and refuses, exit 2, every id in `ONLY` that is not 12 or 25.
A `--spec` or `--build` anywhere in an argv that is not that shape refuses before any check runs.
Every refusal is one `HYGIENE — cannot run: ...` line, the channel `--only` already refuses on.

The path and slug refusals run after the conf is read, where `M` and the selector exist:

| Refusal | Test |
|---|---|
| `--spec` names no file | `[ -f "$SCOPE_ARG" ]` fails |
| `--spec` names a path carrying a `..` segment | a `/../` or a leading `../` |
| `--spec` names no spec check 12 selects | the path is absent from `c12_all`, the selector's own output |
| `--build` names a malformed slug | not a letter, then letters, digits or dashes |
| `--build` names a build with no selectable spec | `c12_all` holds no path under `$M/builds/<slug>/spec/` |
| the cutoff leaves nothing to grade | the tagging loop emits no `P` line, so the run would print what a clean spec prints |

Testing membership in `c12_all` reuses check 12's selector rather than spelling a second copy of
it. The last row is the gate rule that an empty population is not coverage: a spec dated before
`SPEC_FORMAT_CUTOFF` is never graded, and a scoped run over one says so instead of passing.

### S2 — the selection

With `SCOPE_KIND` set, after the `--staged` narrowing:

1. The build is the slug, or the named path's segment after `$M/builds/`.
2. `FILES` becomes the build's tracked files under `$M/builds/<slug>/spec/`, then its untracked ones,
   `git ls-files --others --exclude-standard` over the same folder.
3. `STAGED_SET` holds the named path under `--spec`, and every path of the new `FILES` under
   `--build`.
4. `SCOPED=1`. `in_scope` reads it beside `STAGED`, so it admits only `STAGED_SET`. `pop_guard`
   returns at once under it, as under `--staged`. The tagging loop builds its `J` set under
   `SCOPED=1` as under `STAGED=1`.
5. `STAGED` stays 0, so the pass awk's `stg` stays 0 and the `base` resolve arm runs. The edge-join
   awk takes `stg=1` under `SCOPED=1`, so a sibling's own finding is not reported.
6. The eight zero-population notices and the edge-join notice at `:2980` are skipped under
   `SCOPED=1`. They describe the corpus, and over one spec they would describe it falsely.

### S3 — the liveness line

Under `SCOPED=1` the line at `:3724` gains ` over <N> spec(s) of <SCOPE_ARG>`, where N counts the
`P` lines. Unscoped, its bytes are unchanged, which the self-test's exact-match arm on
`HYGIENE --only 12 ran checks 12 25` pins.

### What a scoped run does not check

- Every check but 12 and 25: names, bindings, the index and the rest. The full run and the bar
  grade them.
- A finding between two siblings of the named spec. Under `--spec` only an edge with a graded end is
  reported, as under `--staged`.
- Whether a sibling's untracked spec is finished. It is read for its edges as it stands.

### S4 — the writer's instructions

The bullet of `tools/roles/agents/gov-spec-writer.agent.md` that opens "You may run the memory
hygiene gate and the naming lexicon over your specs" (line 36 at `043e61df0427`) becomes:

> You may run the naming lexicon over your specs, and grade each spec you wrote with memory
> hygiene's spec-format check as `check-memory-hygiene.sh --only 12 --spec <path>`. The whole-tree
> gate reads tracked files only, so it never grades a spec you have not committed, and it grades
> every other spec for minutes. Where this repository has it, run the spec-token checker as
> `check-spec-tokens.py --spec <path>` over each spec you wrote. Fix every finding either check
> names before you return. You run no other gate.

It names no kit path, so the install-prefix leg stays green (`TOOL-dPavedRoad-1`, commit
`59c386425`). Unit 1's bullet, added after this one, is untouched.
`python tools/roles/render_agents.py --write` regenerates `.claude/agents/gov-spec-writer.md`.

### The role gate

`checkGateLeg` compares a command to each leg's argv at equal length, word for word
(`tools/hooks/scratch-guard.js@7c31933f6258:1628`). The two hygiene legs run the script bare and
with `--only 9,21,23`, three words and four; the scoped form is six words, so it is no leg, and it
is neither the runner nor a suite (`:1694-1699`). The gate admits it.

### Docs

The script header, below `--only`'s line (`:11`), gains
`#   <this script> --only 12 --spec <path> | --build <slug>   # check 12's block over one spec or one build, tracked or not`,
and the paragraph after it gains two sentences stating S2's population and S1's refusals. No page
under `help/` documents the script's flags: `grep -rn -- '--only' help/` finds only the leg table
of `help/pass-legs.md`, and `python tools/govkit/docs_leg.py --list` lists no row for the script.

### The pass probe, `$SCRATCH/u2.sh`

`$SCRATCH` is the run's scratch directory. Run it from the worktree root. It builds a fixture
repository at `$TEMP/u2` from this repository's conf and two CLOSED builds, which the unchanged
script grades clean in 15 s. It plants a section-canon red in one spec of each build, makes a third <!-- PINNED 2026-11-14 -->
spec live so its `base`, absent from the fixture, reds the resolve arm, and writes an untracked red
spec and an untracked pre-cutoff spec. The unchanged script's full run names the three tracked
plants and neither untracked file, observed at `a25c84fc0`.

```bash
set -u
G=$(pwd); R="$TEMP/u2"; rm -rf "$R"; mkdir -p "$R/memory/builds"; cd "$R" || exit 2
git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
cp "$G/.memory-tree.conf" . && cp -r "$G/memory/builds/aCarriedStop" "$G/memory/builds/aSmoothedDispatch" memory/builds/
git add -A && git commit -qm seed
H="$G/tools/memory-tree/check-memory-hygiene.sh"; S=memory/builds/aCarriedStop/spec; P=TOOL-aCarriedStop
A=$S/2026-11-13-spec-TOOL-aCarriedStop-1.md; C=$S/2026-11-13-spec-TOOL-aCarriedStop-2.md
K=$S/2026-11-13-spec-TOOL-aCarriedStop-3.md; N=$S/2026-11-14-spec-$P-98.md
B=memory/builds/aSmoothedDispatch/spec/2026-11-10-spec-TOOL-aSmoothedDispatch-4.md
sed -i '/^## 7\. Gates$/d' "$A" "$B"
sed -i '0,/^\*\*Status:\*\* CLOSED/s//**Status:** INPROGRESS/' "$C"
sed "s/$P-3 /$P-98 /; /^## 7\. Gates\$/d" "$K" > "$N"
cp "$K" "$S/2026-07-01-spec-$P-97.md"
cnt() { grep -cF -- "$2 (" <<<"$1"; }
F=$(bash "$H" --only 12 2>/dev/null)
echo "full A $(cnt "$F" "$A") B $(cnt "$F" "$B") C $(cnt "$F" "$C") N $(cnt "$F" "$N")"
p() { local tag=$1 o rc x same=yes; shift; o=$(bash "$H" "$@" 2>/dev/null); rc=$?
  for x in "$A" "$C"; do
    if [ "$(cnt "$o" "$x")" -gt 0 ] && [ "$(grep -F -- "$x (" <<<"$o")" != "$(grep -F -- "$x (" <<<"$F")" ]; then same=no; fi
  done
  echo "$tag rc $rc A $(cnt "$o" "$A") B $(cnt "$o" "$B") C $(cnt "$o" "$C") N $(cnt "$o" "$N") same $same live $(grep -c '^HYGIENE --only 12 ran checks 12 25 over ' <<<"$o")"; }
p spec-a --only 12 --spec "$A"
p spec-c --only 12 --spec "$C"
p spec-k --only 12 --spec "$K"
p spec-n --only 12 --spec "$N"
p build  --only 12 --build aCarriedStop
r() { local tag=$1 o rc; shift; o=$(bash "$H" "$@" 2>/dev/null); rc=$?; echo "$tag rc $rc said $(grep -c '^HYGIENE — cannot run' <<<"$o")"; }
r no-only   --spec "$A"
r other     --only 9 --spec "$A"
r extra     --only 12 --spec "$A" --staged
r not-spec  --only 12 --spec memory/builds/aCarriedStop/README.md
r absent    --only 12 --spec "$S/2026-11-14-spec-$P-404.md"
r old       --only 12 --spec "$S/2026-07-01-spec-$P-97.md"
r no-build  --only 12 --build nope
```

### Inventory

| identifier | kind | lexicon verb |
|---|---|---|
| `--spec` | flag of `check-memory-hygiene.sh`, with `--only` | — |
| `--build` | flag of `check-memory-hygiene.sh`, with `--only` | — |
| `SCOPE_KIND`, `SCOPE_ARG`, `SCOPED` | sh variables | — |

No function, conf key or check number is minted.

### Rollout

One pass at order 2, after unit 1, because both edit the `gov-spec-writer` role file and its
rendered agent. The hygiene self-test's `FLOOR_ASSERTIONS`, 707 at the base, rises by the count of
new top-level assertions, and the close confirms it from a real run. Cited line numbers are at the
base; the builder finds each site by its text.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/roles/agents/gov-spec-writer.agent.md`
- `.claude/agents/gov-spec-writer.md`

### Alternatives rejected

Each candidate was tested on the clone at `a25c84fc0` or read against the code before the pick.

- **Tell the writer to stage its spec and run `--staged`.** Lost on two tests. `--staged` over one
  staged spec ran 114.7 s wall, every other check included, against 19.5 s for the producers alone;
  and `--staged` skips the `base` resolve arm (`:2543`), so it passes a spec the full run reds.
  Staging also puts writers on the one git index the harness keeps them off.
- **Reuse `--staged` with the scope as its set, `STAGED=1`.** Lost on the same `:2543` read: the
  scoped verdict would differ from the full run's on a live spec with a dead `base`, which the
  build's first rule forbids. The probe's `spec-c` line is the case.
- **Let `--only` combine with `--staged`.** It answers only for staged files, and writers do not
  stage.
- **Scope every check.** Checks 9, 21, 23 and 29 to 31 read the index, the bindings and the commit
  graph, whose population is the tree. The writer needs check 12, and check 12 is the cost.

## 5. Production-readiness checklist

- security — read-only, as every hygiene run is. The named path is never executed and is read only
  after it passes check 12's own selector, which admits nothing outside `$M/builds/<slug>/spec/`.
- perf / scale — the producers, about 19 s on node a, plus check 12 over one build's specs. <!-- PINNED 2026-11-14 -->
- error / empty / loading states — every bad argument and every empty selection refuses with exit 2
  and grades nothing (S1's table).
- observability — the liveness line names the scope and the count graded.
- risks — the scoped run grades no check but 12 and 25, so a writer who reads its exit 0 as "the
  spec is clean" skips names and bindings; the role text calls it the spec-format check, and the
  commit hook and the bar still grade the rest.
- testing — the pass probe above, and the self-test arms under §7, observed RED then GREEN at the
  close.
- migration — none: new flags, and every existing invocation is unchanged.
- user docs — the script header and the writer's role text; no help page documents the script's
  flags (§4 "Docs").

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/u2.sh"`, the Design section's fenced block,
from the worktree root at the pass commit.

- **AC1** — When `bash "$SCRATCH/u2.sh"` runs, it prints `full A 1 B 1 C 1 N 0`,
  `spec-a rc 1 A 1 B 0 C 0 N 0 same yes live 1`, `spec-c rc 1 A 0 B 0 C 1 N 0 same yes live 1` and
  `spec-k rc 0 A 0 B 0 C 0 N 0 same yes live 1`.
  Red when: the scope reuses `STAGED=1`, so the `base` resolve arm is skipped and `spec-c` reads
  `rc 0` and `C 0`; or the scope is ignored and `spec-a` reads `B 1`.
- **AC2** — When `bash "$SCRATCH/u2.sh"` runs, it prints
  `spec-n rc 1 A 0 B 0 C 0 N 1 same yes live 1` and `build rc 1 A 1 B 0 C 1 N 1 same yes live 1`.
  Red when: the scope reads tracked files only, so the untracked spec reads `N 0`, or `--spec` on
  it refuses as naming no selected spec.
- **AC3** — When `bash "$SCRATCH/u2.sh"` runs, it prints `no-only rc 2 said 1`,
  `other rc 2 said 1`, `extra rc 2 said 1`, `not-spec rc 2 said 1`, `absent rc 2 said 1`,
  `old rc 2 said 1` and `no-build rc 2 said 1`.
  Red when: `--spec` without `--only` still runs every check, as it does at the base, so `no-only`
  reads `rc 1 said 0`; or a pre-cutoff spec grades nothing and exits 0.
- **AC4** — When `time bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec
  memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-2.md` runs on node a at the
  pass's parent commit, it refuses with `--only takes one comma list and no other argument`; at the
  pass commit it grades the spec and its `real` wall is at most 60 s. The ledger also records <!-- PINNED 2026-11-14 -->
  `time bash tools/memory-tree/check-memory-hygiene.sh --only 12` at both commits, whose last line
  reads `HYGIENE --only 12 ran checks 12 25` at both.
  Red when: the scope narrows nothing and the scoped wall approaches the unscoped one, 401.9 s at
  `a25c84fc0`.
  cost: the two unscoped runs take about 7 min each on node a.
  figure: 60 s is PINNED as three times the 19.5 s producer floor measured at `a25c84fc0`; every
  wall in the ledger is DERIVED at observation.
- **AC5** — When `python tools/roles/render_agents.py --check` runs it exits 0,
  `grep -c -- '--only 12 --spec <path>' .claude/agents/gov-spec-writer.md` prints 1,
  `grep -cE '[a-z-]+/check-memory-hygiene[.]sh' tools/roles/agents/gov-spec-writer.agent.md`
  prints 0, and `grep -c -- '--only 12 --spec <path> | --build <slug>' tools/memory-tree/check-memory-hygiene.sh`
  prints 1.
  Red when: the role file was edited and the agent not re-rendered; or the sentence names a kit
  path the install-prefix leg reds; or the header carries no usage line for the flags.

## 7. Gates

`memory hygiene` · `memory hygiene (the pass checks)` · `memory-hygiene self-test` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `roles catalogue` · `roles render wiring` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 · a red tree holding a red and a clean spec in one build, a red spec in a second, a live spec with an unresolvable `base` and an untracked red spec, graded scoped and unscoped, plus each refusal of S1's table; staged by setting `STAGED=1` for the scope, which reds the `base` arm, and by leaving `FILES` tracked-only, which reds the untracked arm · `FLOOR_ASSERTIONS`, 707 at the base, raised by the count of new top-level assertions, which the close confirms

`python tools/check-spec-tokens.py --legs-for` over the files touched, run at `a25c84fc0`, names
`policy fixtures` for the script and `check-wiring self-test` and `lexicon naming predicates` for
the rendered agent; the self-test's own guard is the broad memory-tree folder. The two hygiene legs
are the argv this unit must not move, and `install-prefix (shipped surface)` reads the role text.
The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
the spec-token checker over this file and check 12 over it in a scratch clone.

## 8. Open questions

- **F1 — Does this unit close `TOOL-aSmoothedDispatch-16`?** That ask, OPEN and LOW in
  `memory/builds/aSmoothedDispatch/BACKLOG.md`, reads "role agents run the whole-tree hygiene gate
  for a one-spec edit" and accepts "a role agent's hygiene run is scoped to the files it wrote, and
  its prompt says how". S2 and S4 meet that accept line for the spec writer, the role it measured.
  The roster handed this unit no `closes` list, and a header verb disposes another build's ask.
  - (a) Add `closes TOOL-aSmoothedDispatch-16` to this header, so the unit's CLOSED status closes the
    ask. Cross-build `closes` has precedent, for example `aMendedFleet` closing
    `TOOL-aWeighedCompass-11`.
  - (b) Leave the ask open and let the close dispose it by hand.
  Recommendation: (a). It leaves no follow-up open, and the accept line is met in full for the one
  role the ask measured.
  RESOLVED (owner, 2026-11-14): (a), add `closes TOOL-aSmoothedDispatch-16` to this header.

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft from brief `2026-11-14-prompt-TOOL-aTrimmedWait-1-brief`,
  item 2, grounded at `846d51d3` and measured at `a25c84fc0`, whose code is identical. The scope is
  its own mode rather than `--staged`'s, for the `base` resolve arm `--staged` skips.
- rev-2 · 2026-11-14 · §8 · F1 RESOLVED by the owner's pick (a), and the header gains
  `closes TOOL-aSmoothedDispatch-16`, per ruling `2026-11-14-prompt-TOOL-aTrimmedWait-2-ruling`.
- rev-3 · 2026-11-14 · §3 §4 §5 §6 · each measured figure the pinned-facts arm named is pinned on its
  line, per `2026-11-14-prompt-TOOL-aTrimmedWait-3-writing-practice`. No meaning changes.

## 10. Reuse audit

The seams this unit extends: `--only`'s parse and its liveness line
(`tools/memory-tree/check-memory-hygiene.sh@f064ddabb88e:43-59`, `:3724`); the `--staged`
narrowing's `STAGED_SET`, `in_scope` and `J` sibling read (`:770-810`, `:2098-2118`), which this
unit fills from its arguments instead of the index; and check 12's selector `c12_all` (`:2092`),
reused as the `--spec` path test. `python tools/codebase-map/reuse_lookup.py "grade the spec format
of one named spec instead of every spec in the tree"` ranked name stems only (`tree`,
`read_spec_revisions`, `parse_spec_h1`, `build_spec_path_re`), none of which grades a spec's format,
so no seam fits beyond the script's own. Recall's first hits were `TOOL-aTrimmedHook-2`, which
built the `--staged` narrowing, `TOOL-dPavedRoad-4`, which added the `J` sibling read, and the open
ask `TOOL-aSmoothedDispatch-16`, which this unit answers (§8 F1). Its first two runs failed on a
recall cache another writer held open, and the third answered.

Recall terms used: `python tools/memory-recall/query.py "can hygiene check 12 grade one spec or one build instead of the whole tree" --terms "hygiene check-12 only staged narrowed selection spec format in_scope STAGED_SET build folder writer"`

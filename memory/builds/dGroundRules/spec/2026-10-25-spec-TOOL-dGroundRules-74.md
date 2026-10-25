# TOOL-dGroundRules-74 — the writer-split fallback arm the closed specs TOOL-dGroundRules-25, -30 and -34 claim

**Status:** CLOSED · rev-2 · 2026-10-25 · node d · Tier-1 · base fce5603f · streams tooling · order 26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-25-build-TOOL-dGroundRules-74-ledger.md](../build/2026-10-25-build-TOOL-dGroundRules-74-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-74-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-74-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-74-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-74-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md](../reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md) | diff-review | TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build, round 1, item H1 (finding 9): no suite asserts what
`check-protocol-parity.test.sh --render` does when the installed agent-cap hook refuses the writer
split. That path is the three-span fallback, the hook's reason in a stderr notice, and the exit 2
when the hook denies the fallback too. TOOL-dGroundRules-25 AC18, TOOL-dGroundRules-30 AC1/AC4 and
TOOL-dGroundRules-34 AC6 each record an arm for it, and none exists. This unit adds that arm to the
unattended-build suite's layout section, as the report's skeptic-judged fix gives it, and raises the
suite's floor by the count it adds.

## 2. Scope (IN)

- **S1** — The fallback arm. In `tools/workflows/unattended-build.test.sh`, the block §4 "The arm"
  gives goes in byte for byte. It sits after the last DGR10 arm,
  `same "DGR10 ...and writes no harness"` (`:2098`), and before the header line
  `# ---- AC3: the NESTED layout` (`:2100`). It holds 11 assertions: a liveness arm, six on the
  hook that predates the writer marker, and four on the hook that denies the fallback too. The
  suite's `FLOOR_ASSERTIONS=693` (`:3081`) becomes `FLOOR_ASSERTIONS=704`, with the `RAISED` log
  line §4 "The floor" gives added directly above it. No other byte of the suite changes. Observed by
  AC1 and AC2.

## 3. Non-goals (OUT)

- `tools/workflows/check-protocol-parity.test.sh`. Its fallback is correct as it stands (§4
  "Evidence"), and this unit only grades it.
- `tools/hooks/agent-cap.js`, and `build_layout` itself. The layout keeps copying only `policy.py`
  and `catalogue.toml` of the policy kit. Why that matters is in §4 "Evidence".
- The `New arm:` lines of the closed specs TOOL-dGroundRules-25, -30 and -34, which name
  `check-protocol-parity.test.sh` as the arm's home. This unit does not edit a CLOSED record (§8, rev-2).
- The report's left-shift gate, a spec-to-arm check at a unit's close (§8, rev-2).
- The other findings of the report, any other spec, and the inherited reds the close recorded
  (unattended shards 1, 3, 5 and 7, and the hygiene partition arm).

### Edges

none

This unit adds the arm that `TOOL-dGroundRules-30` (CLOSED) declared and commit `93e4b4d31` did not
add. It changes nothing that unit built.

## 4. Design

### Evidence

The fallback lives in `check-protocol-parity.test.sh`. `render` (`:476-499`) applies three
substitutions when `WRITER_SPLIT` is `0` (`:489-496`): the pool cap, `SPEC_WRITERS`, and the split
line's marker, `// gov:fixed-writers` to `// gov:fixed-verifiers`. The hook's verdict block
(`:571-601`) sets `VERIFY_TOTAL=5` (`:581`) and renders the split. It asks
`check-verifier-fanout.sh` for a verdict on it. On a denial it reads the hook's reason with the awk
at `:588`, the line after the gate's `verifier-fanout: FAILED` header. It prints the stderr notice
naming `govkit update --kits agent-cap` (`:592`) and sets `WRITER_SPLIT=0` (`:593`). It re-renders,
and when the hook denies the fallback too it prints the "denies ... fallback too" line (`:596`) and
exits 2 (`:598`).

The premise holds at `fce5603f8`. Grepping `tools`, `skills` and `.githooks` for the report's own
terms (`does not admit the writer split`, `fallback too`, `writer-fallback`, `kits agent-cap`,
`SPEC_WRITERS = 5`, `WRITER_SPLIT`) hits only `check-protocol-parity.test.sh` itself.

One nuance changes the premise's wording, not its scope. Every layout the suite builds already takes
this fallback, with nothing asserted. `build_layout` (`unattended-build.test.sh:1990`) copies the
policy kit's `policy.py` and `catalogue.toml` only, never `policy-mirror.js`. With no mirror beside
the hooks kit, the hook's `readWriterBound` (`tools/hooks/agent-cap.js:466-467`) bounds the split
at `MAX_VERIFIERS`, 5. The policy reader answers `runtime.agents-in-flight` as 6 at HEAD, its
catalogue default, so the split at 6 is denied. TOOL-dGroundRules-30 recorded this in its own
production-readiness list. The probe was a scratch copy of `build_layout`'s flat layout at
`fce5603f8`. Its `--render` exited 0 and printed the stderr notice, and the harness it wrote carries
`cap = 5)`. The probe also copied in `policy-mirror.js`, and the denial still stood: the mirror needs
`policy-shim.sh` beside it as well. `run_layout` merges stderr into stdout
(`unattended-build.test.sh:2018`), and no arm reads the notice, the three spans or an exit 2. So the
path runs, but no arm grades it, and the exit-2 branch is never reached at all. The report's
consequence stands as written.

### The arm

The block below is S1, byte for byte. It builds its own flat layout, so no sibling arm's state leaks
in.

```
# ---- TOOL-dGroundRules-74: THE WRITER-SPLIT FALLBACK, from an adopter's side. A hook that predates
# ---- `gov:fixed-writers` denies the split, and --render writes the verifier-bounded fallback with one
# ---- stderr notice; a hook that denies the fallback too exits 2 and writes nothing. Gov's own tree
# ---- always takes the split, so only a layout reaches this path. No layout carries the policy mirror,
# ---- so its hook bounds the split at MAX_VERIFIERS and every layout above takes the fallback too, with
# ---- nothing asserted. The old hook is staged by its marker here, never left to that accident.
WS="$LAY/old-hook"; build_layout "$WS" scripts/$WFK scripts/$UNK scripts/gotchas.py
sed -i "s/^const WRITER_MARK = 'gov:fixed-writers'\$/const WRITER_MARK = 'gov:an-older-writer-mark'/" "$WS/scripts/$HOOKS/agent-cap.js"
same "DGR74 LIVENESS the layout's hook no longer carries the writer marker" "$(grep -c "^const WRITER_MARK = 'gov:an-older-writer-mark'\$" "$WS/scripts/$HOOKS/agent-cap.js")" "1"
o=$( (cd "$WS" && bash scripts/$WFK/check-protocol-parity.test.sh --render 2>"$LAY/old-hook.err"; echo "rc=$?") ); e=$(cat "$LAY/old-hook.err")
has "DGR74 a hook that predates the writer marker: --render still renders" "$o" "rc=0"
has "DGR74 ...and stderr carries the hook's own reason" "$e" "does not admit the writer split: BLOCKED by agent-cap:"
has "DGR74 ...and names the update" "$e" "Update it: govkit update --kits agent-cap"
h=$(cat "$WS/scripts/$WFK/unattended-build.js" 2>/dev/null)
has "DGR74 ...and the harness bounds its pool at the verify total" "$h" "async function boundedParallel(thunks, cap = 5)"
has "DGR74 ...and its spec writers too" "$h" "const SPEC_WRITERS = 5"
has "DGR74 ...and judges the split under the verifiers marker" "$h" "Math.ceil(slices.length / SPEC_WRITERS)) // gov:fixed-verifiers"
cp "$WS/scripts/$WFK/unattended-build.js" "$LAY/old-hook.js" 2>/dev/null
printf '%s\n' "process.stdin.resume(); process.stdin.on('end', () => { console.error('a stub hook that denies every script'); process.exit(2) })" > "$WS/scripts/$HOOKS/agent-cap.js"
o=$( (cd "$WS" && bash scripts/$WFK/check-protocol-parity.test.sh --render 2>"$LAY/old-hook.err"; echo "rc=$?") ); e=$(cat "$LAY/old-hook.err")
has "DGR74 a hook that denies the fallback too: --render refuses" "$o" "rc=2"
has "DGR74 ...naming the fallback" "$o" "denies unattended-build.js's verifier-bounded fallback too, so nothing was rendered or graded"
has "DGR74 ...after a stderr notice carrying that hook's reason" "$e" "does not admit the writer split: a stub hook that denies every script. Update it"
same "DGR74 ...and leaves the harness it rendered before unchanged" "$(cmp -s "$LAY/old-hook.js" "$WS/scripts/$WFK/unattended-build.js" && echo same || echo changed)" "same"

```

How it follows the skeptic's fix, and where it goes further:

- **The old hook is staged by its marker.** The block respells the layout hook's `WRITER_MARK`
  declaration (`agent-cap.js:464`), as the fix gives. The layout accident above would deny the split
  anyway. So the liveness arm pins that the respelling matched, and a later respelling of the
  declaration cannot make the stage a silent no-op.
- **stderr is captured apart from stdout.** The fix asserts on stderr, and `run_layout` merges the
  two, so the block runs the parity script directly, as the PV-AC4 override arms do (`:2123`).
- **The reason arms grade the `_ub_why` read.** `BLOCKED by agent-cap:` is the first line of the real
  hook's denial. `a stub hook that denies every script` is the stub's only line. A read that printed
  the gate's header, or fell to the empty-reason default at `:590`, reds both.
- **The stub hook drains stdin before it exits 2.** A first probe stub exited without reading.
  The gate's payload writer then died on EPIPE, and its node stack buried the hook's answer in the
  output. The stub is one `printf` line, so the suite carries no heredoc.
- **"Unchanged" means byte-identical to the render before it.** The stub denies on the layout that
  part (a) already rendered, so the file exists, and `cmp` proves the exit-2 path writes nothing
  over it.

The arm uses only `$LAY`, `$WFK`, `$UNK` and `$HOOKS`, and builds under `scripts/` like its
siblings, so the foreign-prefix leg runs it unchanged at every prefix.

What the arm does not check:

- The writer split admitted in a layout. Gov's own live render takes the split, and the parity leg
  grades it there.
- The `${_ub_why%.}` strip (`:591`) and the empty-reason default (`:590`). The stub prints a reason
  with no trailing stop.
- `cap = 5)` and `SPEC_WRITERS = 5` tell the fallback from the split only while the catalogue
  default of `runtime.agents-in-flight` is not 5. The marker arm tells them apart at any value.

### The floor

S1 adds 11 assertion sites, nine `has` and two `same`, each counting one (`:152-153`). The block sits
at top level with no guard around it, so each runs once at every prefix. `FLOOR_ASSERTIONS` moves
from 693 to 704. The line below goes directly above `FLOOR_ASSERTIONS=` (`:3081`), after the
TOOL-dTrueNorth-13 entry:

```
# RAISED 693 -> 704 by TOOL-dGroundRules-74: its 11 static sites, counted by hand off the DGR74 block —
# the liveness arm (1), the old hook's exit, two stderr lines and three harness spans (6), and the
# denying hook's exit, two lines and the unchanged harness (4). Each runs once. Not measured by a run:
# the pass that wrote it runs no suite.
```

Nothing outside the suite reads its floor: no tracked file under `tools/` other than the suite
carries `693` as a pinned count.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Files touched (estimate)

- `tools/workflows/unattended-build.test.sh`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. AC1 runs the scratch script
`p74.sh`. It takes a workflows directory and reads that directory's `unattended-build.test.sh`. It
pulls the suite's own `same` and `has` helpers, `build_layout`, and the DGR74 block, all by their
anchors, and runs them against gov's own kit names. It prints each `FAIL` line, then the count of
executed assertions and the count of failures:

```
cat > "$TEMP/p74.sh" <<'EOF'
HERE=$(cd "$1" && pwd); SUITE=$HERE/unattended-build.test.sh; ROOT=$PWD
WFK=workflows; UNK=unattended; POLICY_KIT=policy; POLICY_KIT_DIR=tools/policy; HOOKS=hooks; HOOKS_DIR=tools/hooks
st=0; n=0; LAY=$(mktemp -d)
eval "$(sed -n -e '/^same() {/p' -e '/^has()  {/p' "$SUITE")"
eval "$(sed -n '/^build_layout() {/,/^}/p' "$SUITE")"
eval "$(sed -n '/^# ---- TOOL-dGroundRules-74: /,/^# ---- AC3: the NESTED layout/p' "$SUITE")" > "$LAY/arms"
grep '^FAIL' "$LAY/arms"
echo "$n $(grep -c '^FAIL' "$LAY/arms")"
rm -rf "$LAY"
EOF
```

The staged breaks each edit one line of the parity script in a scratch copy of the built
`tools/workflows/`. `p74.sh` then runs on the copy, so the arm judges the broken script:

```
brk() { rm -rf "$TEMP/w74$1"; cp -r tools/workflows "$TEMP/w74$1"; sed -i "$2" "$TEMP/w74$1/check-protocol-parity.test.sh"; bash "$TEMP/p74.sh" "$TEMP/w74$1"; }
brk a '/out=${out\/\/"const SPEC_WRITERS = {{FANOUT_CAP}}"/d'
brk b 's/ Update it: govkit update --kits agent-cap"/"/'
brk c '/_ub_why=$(printf/s#/^verifier-fanout: FAILED/#/^no such header/#'
brk d '/denies unattended-build.js.s verifier-bounded fallback too/{n;n;s/exit 2/:/}'
brk e 's/^VERIFY_TOTAL=5$/VERIFY_TOTAL=4/'
brk f 's#"Math.ceil(slices.length / SPEC_WRITERS)) // gov:fixed-writers"/"Math.ceil(slices.length / SPEC_WRITERS)) // gov:fixed-verifiers"#"x"/"y"#'
```

Every figure below was measured at `fce5603f8` on a scratch copy of `tools/workflows/`. In that copy
the suite carried §4's block before its AC3 header. The floor edit is not part of what AC1 reads.

The whole suite is a self-test this pass may not run. The main loop runs it at the close, and that
run prints no `FAIL` line naming `DGR74`, and no floor failure.

- **AC1** — When `bash "$TEMP/p74.sh" tools/workflows` runs, it prints `11 0` and no `FAIL` line.
  At `fce5603f8` it printed `0 0`, because no block matched the anchor.
  Red when: a fallback behaviour breaks, each break by the names below. Break `a`, the `SPEC_WRITERS`
  substitution dropped, gets the fallback denied too: `11 5`, with
  `a hook that predates the writer marker: --render still renders`, the three harness-span arms and
  the unchanged arm red. Break `b`, the update dropped from the notice, gives `11 2`:
  `...and names the update` and `...after a stderr notice carrying that hook's reason`. Break `c`,
  the reason read broken, gives `11 2`: `...and stderr carries the hook's own reason` and the
  denying hook's notice arm. Break `d`, the fallback-too `exit 2` made a no-op, gives `11 1`:
  `a hook that denies the fallback too: --render refuses`. Break `e`, the verify total at 4, gives
  `11 2`: `...and the harness bounds its pool at the verify total` and `...and its spec writers too`.
  Break `f`, the marker substitution dropped, gives `11 5`, the same five as break `a`.
  permission: the suite that holds the arm is a self-test this pass may not run.
- **AC2** — When `grep -cx 'FLOOR_ASSERTIONS=704' tools/workflows/unattended-build.test.sh` runs, it prints `1`.
  At `fce5603f8` it printed `0`.
  Red when: the floor is left at 693, or moved by a count other than the 11 sites S1 adds.

## 6. Gates

`unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `foreign-prefix parity (every self-test at three prefixes)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The four self-tests are the legs `tools/workflows/unattended-build.test.sh` owes. Run through
`derive_guarded_legs` over `tools/gate-legs.json` at `fce5603f8`, each joins on the non-broad
guard `tools/workflows/`, and every other leg `--legs-for` prints trips only on the broad `tools/`.
The unguarded legs are named because the edit is in what they read. `harness arms` reads the suite's
assertion helpers. The two shell-hygiene scans read it as a tracked shell file. The other two
shell-hygiene scans exclude `*.test.sh`. `foreign-prefix parity` runs the suite at three prefixes,
under the broad `tools/` guard.

New arm: tools/workflows/unattended-build.test.sh · covers AC1 · the old hook's half, the liveness arm and the six arms after it, red at `fce5603f8` by absence and staged red again by AC1's breaks a, b, c, e and f · FLOOR_ASSERTIONS 693 to 704
New arm: tools/workflows/unattended-build.test.sh · covers AC1 · the denying hook's half, the four arms from the stub hook on, red at `fce5603f8` by absence and staged red again by AC1's breaks a, b, c and d · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the build run's rescope add row for this unit and its spec
  brief, grounded at `fce5603f8`. The premise was checked by grep and by a scratch copy of the
  suite's flat layout, never by running a suite. That probe found that every layout already takes
  the fallback, with nothing asserted. The cause is that no layout carries `policy-mirror.js`, which
  TOOL-dGroundRules-30 had recorded. The arm therefore stages the old hook by its marker, with a
  liveness arm, and does not lean on that accident. It adds three things to the skeptic's fix: a
  separate stderr capture, a stub that drains stdin (a non-draining stub buried its answer under an
  EPIPE stack), and a byte comparison for "unchanged". The left-shift gate is named in §7 as a
  follow-up, because it is a separate mechanism. The brief's leg item names §6, which in this Tier-1
  shape is the Gates section. The brief, untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-74-spec-brief.md
```

- rev-2 · 2026-10-25 · §7's two follow-up bullets move here as prose, so §7 reads `none` and check 12 admits a CLOSED flip.
  The main loop files an ask for the report's left-shift gate, a close-time check that each CLOSED
  spec's `New arm:` line matches an arm label in the suite it names.
  It files a second ask for the owner or a records pass to correct the arm lines of
  TOOL-dGroundRules-25, -30 and -34, which name `tools/workflows/check-protocol-parity.test.sh`
  where the arm lands in `tools/workflows/unattended-build.test.sh`.

## 9. Reuse audit

This unit builds no mechanism. It adds one arm block to the suite's existing layout section, and
extends three things already there. `build_layout` (`tools/workflows/unattended-build.test.sh:1990`)
builds the scratch install. The `same` and `has` helpers (`:152-153`) count each assertion. The
direct parity-script call the PV-AC4 override arms use (`:2123`) runs the render. AC1 reuses the
suite's own helpers, layout builder and block by extracting them from the suite at their anchors,
so the fixture is never retyped.
`python tools/codebase-map/reuse_lookup.py "stage an agent-cap hook that refuses the writer split in a scratch layout and render the harness fallback"`
ranked only name stems (`write`, `scratch`, `render`, `resolve_caps`). None of them stages a hook in
a layout. The `render` hit is the parity script's own renderer, which the arm grades and does not
copy. The recall probe returned the report's H1 itself and TOOL-dGroundRules-18, -30 and -68.
TOOL-dGroundRules-30's production-readiness list already named the missing-mirror layout. TOOL-dGroundRules-68 is the
hook suite's writer-split arms, which test the hook directly and never run `--render`.

Recall terms used: `python tools/memory-recall/query.py "writer split fallback arm old agent-cap hook render layout" --terms "WRITER_SPLIT WRITER_MARK gov:fixed-writers build_layout fallback too KIT_AGENT_CAP_VERSION"`

# TOOL-dGroundRules-83 — the govkit selftest's [-PV] adopter targets hold the agent-cap hook again, and a render whose fan-out gate could not ask the hook refuses with the gate's own reason

**Status:** DEFERRED · rev-1 · 2026-10-25 · node d · Tier-1 · base 9437976a · streams tooling · order 30

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-83-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-83-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-83-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-83-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

At the close, the govkit selftest fails 47 `[-PV]` arms that pass at the run's base `3c2b69be4`
(the main loop's count at `59f02fde9`, pinned there).
The first is F2: the review-harness regenerate exits 2 in the fixture's adopter target, and every
later block reds because block 1 did not finish clean. The cause is the fixture, not the product.
The target holds no agent-cap hook, which every real install holds, and since
`TOOL-dGroundRules-30` the render asks that hook. This unit seeds the hook into the fixture again.
It also fixes this build's misleading refusal: a fan-out gate that could not ask the hook was
reported as the hook's denial, with an empty reason.

## 2. Scope (IN)

- **S1** — `tools/govkit/selftest.py` gains `seed_pv_hook`, directly after `seed_pv_policy`
  (`tools/govkit/selftest.py:14678-14686`), in the text §4 "The fixture" gives. It copies the real
  `agent-cap.js` to the target's `.claude/hooks/`. `build_pv_target` and `build_pv_bootstrap` each
  call it on the line after their `seed_pv_policy(t)` (`:14695`, `:14728`). The comment above the
  fan-out gate's copy (`:14636-14638`) names it. Observed by AC1.
- **S2** — The writer-split block of `tools/workflows/check-protocol-parity.test.sh`
  (`:571-601`) branches on the gate's exit, in the text §4 "The render" gives. An exit other than 0
  or 1 refuses at once, exit 2, printing the gate's own answer on stderr. Only exit 1 is a hook
  denial, and its empty-answer notice reads `the agent-cap hook denied it and printed no reason`.
  The block's comment says so. Observed by AC2 and AC3.
- **S3** — Five `DGR83` arms in `tools/workflows/unattended-build.test.sh`, directly after the last
  `DGR74` arm (`:2123`), in the text §4 "The arm" gives. NOT OBSERVED by a criterion here: it is the
  suite arm §6 declares on its `New arm:` line, which the main loop observes RED and then GREEN at
  the close.

## 3. Non-goals (OUT)

- `tools/hooks/agent-cap.js`. No rule of the hook denies the fixture's render (§4 "Evidence").
- `tools/workflows/check-verifier-fanout.sh`. Its exit contract is right as written: 0 clean, 1 a
  rule the hook enforces is broken, 2 misconfigured (`tools/workflows/check-verifier-fanout.sh:12`).
- Admitting the writer split when no hook resolves. `TOOL-dGroundRules-30` ruled that a render with
  no hook or no node exits 2, because the kit requires `agent-cap`
  (`memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-30.md:186-188`). S2 keeps
  that exit and changes only what it says.
- A `requires` row on the fixture's review-harness descriptor. The fixture's registry has no
  agent-cap entry, so govkit's unmet-dependency refusal would refuse the fixture's own apply
  (`tools/govkit/govkit.py:7557-7564`).
- The six inherited govkit selftest failures, and every other `[-PV]` arm's subject.
- Any help page. No page under `help/` describes the render's refusals, and `help/agent-limit.md`
  covers only what the hook refuses.

### Edges

none

## 4. Design

### Evidence

Measured at `9437976a8` with two scratch probes, §5's `p83.py` and `f83.sh`. `p83.py` imports the
selftest and executes its own `[-PV]` builder source, cut from `tools/govkit/selftest.py` by text
anchors. It builds the gov fixture at vintage A, the `pv-t` target (`build_pv_target`) and the
`pv-qo` target (`build_pv_bootstrap` with only the review harness). It then executes the selftest's
vintage-B edits. In each target it runs `govkit update --write` with `GOVKIT_RERENDER=1`, as block
1 does, and then the descriptor's regenerate argv itself.

- In both targets the update printed `ran review-harness: ... -> exit 2  REFUSED` and exited 1. The
  regenerate exited 2, and its stderr was the line the brief quotes, ending
  `the agent-cap hook exited 2 with no reason. Update it: govkit update --kits agent-cap`.
- Its stdout named the real cause, in the fallback's refusal, which govkit does not quote:
  `verifier-fanout: no agent-cap.js through the install receipt, at ... — this gate has no predicate to delegate to`.
- With `agent-cap.js` copied to the target's `.claude/hooks/`, both updates printed `-> exit 0`
  and re-stamped the receipt, and the regenerate exited 0 with nothing on stderr.
- The hook itself, fed the target's rendered `unattended-build.js` as the gate feeds it
  (`--only=scripts`), exited 0 with no output. So no agent-cap rule denies the payload. Under
  `--only=scripts` rules 6, 7 and 0 never run (`tools/hooks/agent-cap.js:1865`, `:1891`, `:1911`),
  and the fixture's three-line template holds no agent call for rules 2 and 5 to judge.

The "denial" is the fan-out gate's exit 2 for a missing predicate
(`tools/workflows/check-verifier-fanout.sh:146`). The render reads any non-zero exit as a hook
denial (`tools/workflows/check-protocol-parity.test.sh:587`). It takes the reason from the line
after `verifier-fanout: FAILED` (`:588`), which only exit 1 prints (`check-verifier-fanout.sh:207`).
So the reason was empty, and `:590` wrote the gate's exit as the hook's.

### The bisect

The regenerate argv ran in the no-hook `pv-t` target with the render script and the fan-out gate
taken from each commit of this build that touches either one. The base itself differs: there the
render asked the hook for `FANOUT_CAP`, and the base fixture seeded the hook (below).

| Commit | Unit | Exit | stderr |
|---|---|---|---|
| `3c2b69be4` | the base | 2 | empty; the hook would not answer `FANOUT_CAP` |
| `2ebafd441` | `TOOL-dGroundRules-10` | 0 | empty |
| `b441f50fc` | `TOOL-dGroundRules-18` | 0 | empty |
| `f6674a6a2` | `TOOL-dGroundRules-21` | 0 | empty |
| `b663756ca` | `TOOL-dGroundRules-25` | 0 | empty; with no hook, `WRITER_SPLIT` stayed 1 silently |
| `93e4b4d31` | `TOOL-dGroundRules-30` | 2 | `does not admit the writer split: verifier-fanout: no agent-cap.js ...` |
| `75b1ffe59` | `TOOL-dGroundRules-34` | 2 | `does not admit the writer split: the agent-cap hook exited 2 with no reason` |
| `9437976a8` | HEAD | 2 | as `75b1ffe59` |

Two commits made the fixture red, and neither was wrong alone. At the base the selftest held
`seed_pv_hook`, which put the hook in `.claude/hooks/` because the render asked it for `FANOUT_CAP`
(`3c2b69be4:tools/govkit/selftest.py:14679-14684`, called at `:14693` and `:14726`).
`2ebafd441` (`TOOL-dGroundRules-10`) moved `FANOUT_CAP` to the policy reader and swapped that
helper for `seed_pv_policy`, correctly for that day. `93e4b4d31` (`TOOL-dGroundRules-30`) made the
render ask the hook again, through the gate, and its spec named no govkit selftest fixture. The
denial dates from `93e4b4d31`. `TOOL-dGroundRules-30` also introduced the misattribution: its
notice called the gate's exit 2 a hook denial, though at that commit it still quoted the gate's
line. The empty reason is `75b1ffe59`, `TOOL-dGroundRules-34` S31
(`memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md:221-223`). It meant an
empty hook answer under exit 1, and it also caught exit 2.

### Which side

The fixture. A real adopter's review-harness install always holds the hook.
`tools/workflows/kit.toml:10` declares `requires = ["agent-cap", "policy"]`. govkit refuses an apply
whose selection names a kit with an unmet dependency (`tools/govkit/govkit.py:7550-7564`). The
fan-out gate resolves the hook through the install receipt first, so a renamed hooks directory is
found too. The suite's own layouts say the same and seed it
(`tools/workflows/unattended-build.test.sh:1999-2010`). The `[-PV]` fixture seeds the policy kit by
hand for the same reason and stopped seeding the hook.

The refusal text is the product's, and this build's, so S2 fixes it. It changes no exit: a target
with no hook exits 2 before S2 and after it, as `TOOL-dGroundRules-30` ruled. The fixture needs
nothing for S2.

### The fixture

S1 inserts this helper directly after the body of `seed_pv_policy`, before `def build_pv_target`.
It is the base's helper with its docstring brought up to date:

```
        def seed_pv_hook(t):
            """The agent-cap hook where inCMS core keeps its only copy, `.claude/hooks/`, which the
            fan-out gate's resolver probes third. The review harness requires the hook kit, so every
            real install holds one, and since TOOL-dGroundRules-30 the renderer asks it, through
            `check-verifier-fanout.sh`, whether it admits the writer split. A fixture without it
            renders nothing (TOOL-dGroundRules-83)."""
            (t / ".claude" / "hooks").mkdir(parents=True, exist_ok=True)
            shutil.copy2(KIT_DIRS["hooks"] / "agent-cap.js", t / ".claude" / "hooks" / "agent-cap.js")
```

In `build_pv_target` and in `build_pv_bootstrap`, the line `            seed_pv_hook(t)` follows
`            seed_pv_policy(t)`, at the same 12-space indent, so the hook is committed with the
policy kit. The comment above the fan-out gate's copy in `build_pv_gov` becomes:

```
            # The verifier fan-out gate ships in the kit as it does in the real one. The renderer read
            # FANOUT_CAP through it until TOOL-dGroundRules-10 re-pointed the token to the policy
            # reader, which is the target's own, see `seed_pv_policy`. Since TOOL-dGroundRules-30 the
            # renderer asks it whether the target's hook admits the writer split, see `seed_pv_hook`.
```

`.claude/hooks/` is the location the base fixture used and its arms passed with. The gate's third
rung reads it (`tools/workflows/check-verifier-fanout.sh:143-144`). No policy mirror sits beside it,
so the hook bounds a writer split at `MAX_VERIFIERS`. The fixture's template carries no writer
marker, so that bound is never read.

### The render

In `tools/workflows/check-protocol-parity.test.sh`, the comment's two lines ending
`... and nothing is written. No` and `... VERIFY_TOTAL is the hook's` (`:577-578`) become:

```
# first line and the update; a hook that denies the fallback too exits 2 and nothing is written. A
# gate exit other than 0 or 1 is no verdict: the gate could not ask the hook, which the kit
# requires as `agent-cap`, for want of the hook, node or a checkout. The fallback would ask the same
# gate, so the render refuses at once with the gate's own answer on stderr (TOOL-dGroundRules-83).
# VERIFY_TOTAL is the hook's
```

The lines from the `_ub_out=$(bash "$HERE/check-verifier-fanout.sh" "$TMPD/writer-split.js" ...`
line through the S31 fallback line (`:586-590`) become:

```
  _ub_out=$(bash "$HERE/check-verifier-fanout.sh" "$TMPD/writer-split.js" 2>&1); _ub_rc=$?
  if [ "$_ub_rc" != 0 ] && [ "$_ub_rc" != 1 ]; then
    printf 'protocol-parity: the fan-out gate exited %s and could not ask the agent-cap hook whether it admits the writer split, so nothing was rendered or graded. Its answer:\n  %s\n' "$_ub_rc" "${_ub_out//$'\n'/$'\n'  }" >&2
    exit 2
  fi
  if [ "$_ub_rc" = 1 ]; then
    _ub_why=$(printf '%s\n' "$_ub_out" | awk 'f { sub(/^ +/, ""); print; exit } /^verifier-fanout: FAILED/ { f = 1 }')
    # An empty hook answer is said as one, never as the gate's header or the render's path (TOOL-dGroundRules-34 S31).
    [ -n "$_ub_why" ] || _ub_why="the agent-cap hook denied it and printed no reason"
```

Every line after it in the block stays as it is. The refusal goes to stderr because govkit quotes a
failed regenerate's stderr, and the fallback's stdout refusal is what nobody saw. It indents the
answer by parameter expansion and not `printf | sed`. A pipe there is a `var-pipe` site, and
`memory/project/spawn-idiom-sites.txt` pins this file's per-class counts in both directions.
`exited 1` came from the gate, which exits 1 whatever the hook exits, so the S31 notice names no
number. The new text carries no word check 7l of `govkit selfcheck` reads as a re-render claim
(`tools/govkit/govkit.py:3615`).

### The arm

S3 inserts these lines directly after the `DGR74 ...and leaves the harness it rendered before
unchanged` arm. The `$WS` layout holds the DGR74 stub hook at that point, and no later arm reads
`$WS`:

```
# ---- TOOL-dGroundRules-83: A GATE THAT COULD NOT ASK THE HOOK IS NO VERDICT. A hook that denies
# ---- printing nothing is said as one. With no hook at all the fan-out gate exits 2 naming why, and
# ---- --render refuses at once with that answer on stderr, never as the hook's denial.
printf '%s\n' "process.stdin.resume(); process.stdin.on('end', () => process.exit(2))" > "$WS/scripts/$HOOKS/agent-cap.js"
( cd "$WS" && bash scripts/$WFK/check-protocol-parity.test.sh --render >/dev/null 2>"$LAY/old-hook.err" ); e=$(<"$LAY/old-hook.err")
has "DGR83 a hook that denies printing nothing: the notice says so" "$e" "does not admit the writer split: the agent-cap hook denied it and printed no reason"
rm -f "$WS/scripts/$HOOKS/agent-cap.js"
o=$( (cd "$WS" && bash scripts/$WFK/check-protocol-parity.test.sh --render 2>"$LAY/old-hook.err"; echo "rc=$?") ); e=$(<"$LAY/old-hook.err")
has "DGR83 no hook at all: --render refuses" "$o" "rc=2"
has "DGR83 ...naming the gate that could not ask the hook" "$e" "the fan-out gate exited 2 and could not ask the agent-cap hook"
has "DGR83 ...and the gate's own reason" "$e" "has no predicate to delegate to"
hasnt_ "DGR83 ...never as the hook's denial" "$e" "does not admit the writer split"
```

The stderr read is `$(<file)`, not `$(cat file)`, so the file's `cat-file` count does not move.
With the hook gone, the layout has no receipt and no `.claude/hooks/`, so the gate's three rungs all
miss. At `9437976a8` four of the five red: the silent hook's notice says `exited 1 with no reason`,
and the no-hook stderr carries the old notice while the gate's reason goes to stdout. The `rc=2` arm
holds on both sides.

### What this does not check

AC1 runs one block's worth of the `[-PV]` flow: the introducing update and the regenerate, in one
`apply` target and one `adopt` target. The 47 arms, including the later blocks, the hooks the
runbook commits through and the restore, are the govkit selftest's. The main loop runs it at the
close and confirms they go green while the six inherited failures stay as they were. Nothing here
checks that a real adopter's hook resolves. The gate's receipt rung and the unmet-dependency refusal
hold that.

### Alternatives rejected

- Seeding the hook at `scripts/hooks/`, the gate's second rung. It passes too (measured), but the
  base fixture modelled inCMS core's only copy under `.claude/hooks/`, and its arms passed there.
- Letting a missing hook admit the writer split, as `b663756ca` did silently. `TOOL-dGroundRules-30`
  ruled it out, and an adopter would ship a harness no hook had judged.
- Keeping the fallback render on a gate exit 2. The fallback asks the same gate and fails the same
  way, and its refusal went to stdout, which govkit does not quote.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
The review-harness kit's shipped render script moves, which `kit epoch` prints as owed at the lander.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/workflows/unattended-build.test.sh`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree, in Git Bash. They use two scratch
scripts under `$TEMP`, whose path is short. Under a deeper directory, measured under this run's
scratchpad, the fixture's git objects passed Windows' 260-character path limit and `apply` failed.
`p83.py` imports the selftest from the tree it is given and executes the selftest's own `[-PV]`
builder source, cut by two pairs of text anchors. A missing anchor raises, so a moved block reds the
probe rather than passing it. Its optional third argument `drop` stages S1's break: it deletes every
`seed_pv_hook(t)` call from the source it executes, leaving the tree alone.

```
cat > "$TEMP/p83.py" <<'EOF'
# p83.py <gov tree> <scratch dir> [drop] -- the selftest's own [-PV] builders, cut from its source.
import json, os, pathlib, re as _re, shutil, subprocess, sys, textwrap
root = pathlib.Path(sys.argv[1]).resolve(); tmp = pathlib.Path(sys.argv[2]).resolve()
if tmp.exists():
    shutil.rmtree(tmp, onexc=lambda f, x, e: (os.chmod(x, 0o700), f(x)))
tmp.mkdir(parents=True)
sys.path.insert(0, str(root / "tools" / "govkit"))
import selftest as st
src = (root / "tools" / "govkit" / "selftest.py").read_text(encoding="utf-8")
if sys.argv[3:] == ["drop"]:
    src = src.replace("            seed_pv_hook(t)\n", "")
def block(a, b):
    i = src.index(a); j = src.index(b, i)
    return textwrap.dedent(src[src.rindex("\n", 0, i) + 1:j])
def check(label, cond, detail=""):
    if not cond: print("FIXTURE FAIL", label, detail[-600:])
def gout(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), *a], capture_output=True, text=True).stdout
ns = dict(vars(st), tmp=tmp, check=check, gout=gout, json=json, os=os, _re=_re)
exec(block("import tomllib as _pvtoml", "# ---- THE CONSUMER'S COMMIT-TIME HOOKS"), ns)
g = ns["build_pv_gov"]()
ts = {"pv-t": ns["build_pv_target"](g, "pv-t"),
      "pv-qo": ns["build_pv_bootstrap"](g, "pv-qo", kits=("review-harness",))}
ns["_pvg"] = g
exec(block('_pvd = _pvg / PFX / KIT_NAMES["workflows"]', "_pvB = gout("), ns)
bash = st.govkit_module().resolve_bash()
for name, t in ts.items():
    print(name, "hook", (t / ".claude" / "hooks" / "agent-cap.js").is_file())
    u = subprocess.run([sys.executable, str(g / st.PFX / st.KIT_NAMES["govkit"] / "govkit.py"), "update",
                        "--target", str(t), "--write"], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=dict(os.environ, GOVKIT_RERENDER="1"))
    ran = [ln.split("->")[-1].strip() for ln in u.stdout.splitlines() if "ran review-harness:" in ln]
    print(name, "update rc", u.returncode, "ran ->", *ran)
    r = subprocess.run([bash, "scripts/workflows/check-protocol-parity.test.sh", "--render", "--tracked-only"],
                       cwd=str(t), capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(name, "regenerate rc", r.returncode)
    for ln in r.stderr.splitlines():
        print(name, "stderr", ln[:160])
EOF
```

`f83.sh` works in the `pv-t` target `p83.py` built, so it runs after a `p83.py` run with no break.
It feeds the target's rendered `unattended-build.js` to the target's hook as the gate does, and
prints the verdict. Then it stages a hook that denies printing nothing, and then no hook at all,
running the regenerate argv after each and printing its stderr. It puts the real hook back at the
end. Its optional second argument `old` stages the break for S2: it writes the render script as it
stood at `9437976a8` into the target first, so run it last.

```
cat > "$TEMP/f83.sh" <<'EOF'
# f83.sh <pv-t target> [old] -- S2 in the target p83.py built: the hook's verdict on the render, then
# a hook that denies printing nothing, then no hook at all. `old` stages the render script at 9437976a8.
t="$1"; P=scripts/workflows/check-protocol-parity.test.sh; H="$t/.claude/hooks/agent-cap.js"
[ "${2:-}" = old ] && git show 9437976a8:tools/workflows/check-protocol-parity.test.sh > "$t/$P"
node -e 'process.stdout.write(JSON.stringify({tool_name: "Workflow", tool_input: {script: require("fs").readFileSync(process.argv[1], "utf8")}}))' "$t/scripts/workflows/unattended-build.js" | node "$H" --only=scripts; echo "hook verdict rc=$?"
cp "$H" "$t/../agent-cap.keep"
printf '%s\n' "process.stdin.resume(); process.stdin.on('end', () => process.exit(2))" > "$H"
(cd "$t" && "$BASH" "$P" --render --tracked-only >/dev/null 2>"$t/../f83.err"; echo "silent rc=$?"); cat "$t/../f83.err"
rm "$H"
(cd "$t" && "$BASH" "$P" --render --tracked-only >/dev/null 2>"$t/../f83.err"; echo "none rc=$?"); cat "$t/../f83.err"
cp "$t/../agent-cap.keep" "$H"
EOF
```

The govkit selftest is a suite this pass may not run. The main loop runs it at the close, and the 47
`[-PV]` failures it printed at `59f02fde9` go green while the six inherited ones stay.

- **AC1** — When `python "$TEMP/p83.py" . "$TEMP/p83"` runs, it prints, after the selftest's vintage pin line, these lines for `pv-t` and then for `pv-qo`: `hook True`, `update rc 0 ran -> exit 0` and `regenerate rc 0`, with no `stderr` line.
  At `9437976a8` each target printed `hook False`, `update rc 1 ran -> exit 2  REFUSED`, `regenerate rc 2`, and one `stderr` line ending `exited 2 with no reason. Update it: govkit update --kits agent-cap`.
  Red when: the seeding is taken away. Then `python "$TEMP/p83.py" . "$TEMP/p83" drop` prints `hook False` and `update rc 1 ran -> exit 2  REFUSED` for both targets.
  The green run and the break were measured on `9437976a8` with S1's two calls and helper applied to the executed source.
- **AC2** — When `bash "$TEMP/f83.sh" "$TEMP/p83/pv-t/target"` runs after AC1, it prints `hook verdict rc=0`, then `none rc=2` followed by the line `protocol-parity: the fan-out gate exited 2 and could not ask the agent-cap hook whether it admits the writer split, so nothing was rendered or graded. Its answer:` and an indented line ending `this gate has no predicate to delegate to`.
  Red when: S2's first branch is absent. Then `bash "$TEMP/f83.sh" "$TEMP/p83/pv-t/target" old` prints, after `none rc=2`, the line `protocol-parity: the agent-cap hook does not admit the writer split: the agent-cap hook exited 2 with no reason. Update it: govkit update --kits agent-cap` and no gate reason.
  Both were measured on `9437976a8` with S1 applied and S2's text copied into the target.
- **AC3** — When the same `bash "$TEMP/f83.sh" "$TEMP/p83/pv-t/target"` runs, it prints `silent rc=2` followed by the line `protocol-parity: the agent-cap hook does not admit the writer split: the agent-cap hook denied it and printed no reason. Update it: govkit update --kits agent-cap`.
  Red when: the S31 notice still names the gate's exit as the hook's. Then the `old` run prints `the agent-cap hook exited 1 with no reason` after `silent rc=2`, for a hook that exited 2.

## 6. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `encoding posture (text IO names its encoding)` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/workflows/unattended-build.test.sh · covers AC2 AC3 · the render script at 9437976a8, which lacks S2, reds four of the five DGR83 arms by name · none

Run through `derive_guarded_legs` at `9437976a8`, `python tools/check-spec-tokens.py --legs-for`
names these non-broad guarded legs. `tools/govkit/selftest.py` trips `govkit selftest`,
`govkit refusal join`, `govkit acceptance matrix` and `recall floor arms` through `tools/govkit/`,
and `policy fixtures` through its own exact line. Both workflows files trip
`verifier fan-out self-test`, `tier2-review self-test`, `unattended-build self-test` and
`review-join self-test` through `tools/workflows/`. Every other leg it prints trips only on the broad
`tools/`.

The unguarded legs named beside them read what this unit changes:

- `review-protocol parity (kit vs dogfood)` runs the render script in gov's own tree. There the hook
  resolves and the gate exits 0, so neither S2 branch is taken.
- Both `shell hygiene` legs read the two shell files. No count moves: S2 indents by parameter
  expansion and adds no pipe, and S3 reads with `$(<file)` and adds no loop. The rows for both files
  in `memory/project/spawn-idiom-sites.txt` and `memory/project/substitution-fed-loops.txt` stay.
- `encoding posture (text IO names its encoding)` pins `tools/govkit/selftest.py` at one `file-io`
  site. S1 adds `mkdir` and `shutil.copy2`, which that class does not count, so no count moves.
- `govkit selfcheck` check 7l reads the review-harness kit's prose, because the kit declares a
  regenerate. The new text names no re-render claim.
- `kit epoch` reads the review-harness kit's shipped bytes and prints the move as owed at the lander.
- `testsuite counts` reads the count the unattended-build suite prints, which S3 raises by five. That
  count is derived and pinned nowhere.

No floor, ceiling or pinned count moves. Each leg's `ceiling` in `tools/gate-legs.json` (700 s and
11750 s, read at `9437976a8`) has room for what changes. S3 adds two renders to the
`unattended-build self-test`, and S1 makes the govkit selftest's later `[-PV]` blocks run again, as
they did at the base.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from this unit's spec brief, grounded at `9437976a8`. The
  diagnosis ran the selftest's own `[-PV]` builder source, never the suite. It reproduced the
  brief's F2 line in both an `apply` target and an `adopt` target, and the hook admitted the render
  when called directly. The bisect over the render script's commits put the denial at `93e4b4d31`
  and the empty reason at `75b1ffe59`. The base selftest's own `seed_pv_hook`, dropped at
  `2ebafd441`, showed the fixture had held the hook. So the fix is on the fixture side, and the
  refusal text, this build's own, is fixed beside it without moving any exit. A follow-up the main
  loop may want: the brief counted 47 `[-PV]` arms, and only the close's selftest run confirms that
  S1 turns all 47 green. The brief and this role's prompt, untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-83-spec-brief.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-83-1-spec-writer.md
```

## 9. Reuse audit

S1 reuses the selftest's own seeding seam: `seed_pv_policy` and its call sites in `build_pv_target`
and `build_pv_bootstrap`. Its helper is the base's `seed_pv_hook`
(`3c2b69be4:tools/govkit/selftest.py:14679-14684`), brought back with its docstring brought up to
date. S2 reuses the fan-out gate's declared exit contract (`tools/workflows/check-verifier-fanout.sh:12`)
and keeps S31's extraction and fallback in place. S3 reuses the DGR74 block's `$WS` layout,
`build_layout` and the suite's `has` and `hasnt_` helpers (`tools/workflows/unattended-build.test.sh:152-154`).
`python tools/codebase-map/reuse_lookup.py "seed the agent-cap hook into a fixture adopter target so the render can ask it"`
ranked only name stems (`seed`, `fixture`, `adopt`, `render`), and none seeds a hook into a
`[-PV]` target. No existing seam fits beyond the selftest's own helper. The recall probe returned
`TOOL-dGroundRules-34` S31, `TOOL-dGroundRules-30` and `-18` for the writer split,
`TOOL-dGroundRules-74`'s brief for the fallback arm, and `TOOL-dRedressedBar-9` for a settings-merge
exit with no hook. None seeds the fixture.

Recall terms used: `python tools/memory-recall/query.py "agent-cap hook missing in adopter fixture writer split render refuses gate exit 2 no reason" --terms "seed_pv_hook seed_pv_policy writer split check-verifier-fanout no predicate _ub_why S31 [-PV] F2 regenerate"`

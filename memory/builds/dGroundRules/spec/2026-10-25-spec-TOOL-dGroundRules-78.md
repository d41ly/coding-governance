# TOOL-dGroundRules-78 — the close sweep of the review's M4 and lows: the policy fixtures leg's figures, agent-cap.js's rule-7 header, policy-mirror.js's bash resolver order, and the stale "lands dark" waiver and help text

**Status:** DEFERRED · rev-2 · 2026-10-25 · node d · Tier-1 · base fce5603f · streams tooling · order 26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-78-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-78-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-78-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-78-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review, round 1, confirmed one medium and three low findings that this unit closes as
one batch. The `policy fixtures` leg's budget and ceiling were sized for 16 cases and the fixture now
runs 146, so the leg is killed at its ceiling. agent-cap.js's header says rule 7 admits a `cwd` in no
checkout, which it refuses. policy-mirror.js tries every `bash` on PATH, while the checker it claims
to match tries only the first. The policy kit's playbook waiver and its help page still say the kit
lands dark. Each scope item is one mechanism, and none changes what a gate decides beyond its own
finding.

## 2. Scope (IN)

- **S1** — The `policy fixtures` leg's figures (finding M4, id 11). In
  `tools/run-gates/selftest-budgets.txt`, the `policy fixtures` row's budget and its reading column,
  and in `tools/gate-legs.json`, that leg's `ceiling`, are set from a reading the builder takes at
  this unit's own base, as §4 "S1" gives. Observed by AC1.
- **S2** — agent-cap.js's rule-7 header (finding L1, id 7). In `tools/hooks/agent-cap.js`, the RULE 7
  paragraph of the file's header comment says that a `cwd` in no checkout refuses, as §4 "S2" gives.
  Observed by AC2 and AC3.
- **S3** — policy-mirror.js's bash resolver order (finding L2, id 8). In
  `tools/policy/policy-mirror.js`, `resolveBash` tries the first `bash` PATH names and no later one,
  and the comment above it states the order. The kit README's sentence on that order, in
  `tools/policy/README.md`, says the same. Observed by AC4, AC5 and AC6.
- **S4** — The policy kit's playbook waiver (finding L3, id 12). `tools/playbook-kit-waivers.txt`
  holds the `lib` row as its only row. Observed by AC7.
- **S5** — The help page's consumer sentence (finding L3, id 14). In `help/policy.md`, the sentence
  naming who re-points the other consumers points at the catalogue's `owner` column, as §4 "S5" gives.
  Observed by AC8.

## 3. Non-goals (OUT)

- Splitting the `policy fixtures` leg, or running its outcome cases in a pool. §4 "Alternatives
  rejected" gives why.
- `tools/run-gates/ceiling-evidence.txt`. This unit writes no evidence row there. The builder's
  reading overstates a single run, and that file only ever rises (§4 "S1").
- `tools/lib/resolve_bash.py` and the inline copy in `tools/policy/check_policy.py`. The skeptic's fix
  leaves both unchanged.
- A `kit:policy` block in the charter template. The charter's text for the policy kit is a later
  build's choice, and S4 does not need it (§4 "S4").
- The "lands dark" paragraph of `tools/policy/README.md` (`:9-14`). It has the same stale wording, but
  the report did not name it, and §7 lists it as a follow-up.
- The other findings of the report, the inherited reds the close recorded (unattended shards 1, 3, 5
  and 7, and the hygiene partition arm), and any other spec.

### Edges

none

This unit repairs text and figures that `TOOL-dGroundRules-1` (CLOSED) wrote, a header that
`TOOL-dGroundRules-10` (CLOSED) wrote and `TOOL-dGroundRules-21` (CLOSED) S38 left behind, and the
resolver that `TOOL-dGroundRules-21` S14 and S16 built. Sibling units 73 and 76 also touch
`help/policy.md`, and unit 73 also touches `tools/hooks/agent-cap.js`. So every edit here is located by
its text, not by its line number.

## 4. Design

### Evidence

Each premise was re-checked at `fce5603f8`. All four still hold.

- **M4.** `python -B "$TEMP/c78.py"` (§5) imported `check_policy` and called `derive_cases` over the
  shipped catalogue. It returned 146 cases: 136 in `CASES` (`tools/policy/check_policy.py:4317`) and
  10 schema-empty cases (`:4373-4375`). `run_fixture` (`:4417`) runs them one after another, and
  every planted case builds a fresh git repository through `build_repo`. The budget row at
  `tools/run-gates/selftest-budgets.txt:82` reads 60 and cites "the fixture's 16 cases". The leg's
  ceiling at `tools/gate-legs.json:1843` reads 300. The finder measured one serial `--fixture` run at
  566s. The skeptic did not re-run it. This pass did not run it either, because it is a gate.
- **L1.** `tools/hooks/agent-cap.js:38-39` says "No policy kit beside this one, or a `cwd` in no
  checkout, adds no rule". `checkSettingsInForce` returns a BLOCKED string when
  `resolveCheckoutRoot` finds no checkout (`:1785`). Its comment at `:1776` and
  `tools/hooks/README.md:213` both describe the refusal.
- **L2.** `resolveBash` (`tools/policy/policy-mirror.js:61`) builds `onPath` from every PATH
  directory's `bash.exe` and `bash` that exist. It spreads all of them into `cands` at `:65`.
  `resolve_bash` (`tools/lib/resolve_bash.py`, copied inline at `tools/policy/check_policy.py:930`)
  takes `GOV_BASH`, then `shutil.which("bash")`, then the two Git for Windows paths, then a bare
  `bash`. AC4's probe at `fce5603f8` recorded the JS trying both PATH directories' `bash`.
- **L3.** `tools/playbook-kit-waivers.txt:15` says no consumer reads the policy file until later
  units re-point one. `help/policy.md:12-14` says "Later dGroundRules units re-point each other
  consumer". Agent-cap rule 7 reads `runtime.agents-in-flight` (`tools/hooks/agent-cap.js:1797`), and
  `budgets.py` reads every cap through `resolve_read` (`tools/policy/budgets.py:233`). So the waiver's
  reason is false. The catalogue's `owner` column assigns the rest of the keys to other builds:
  `owner = "dGroundRules"` holds on 5 of the catalogue's rows, and 20 other builds own the rest.

One more fact for L3 is not in the report. `tools/check-playbook-parity.sh:221-223` counts a kit as
named when `WIRE-INTO-PROJECT.md` spells `<prefix>/<kit>/`. `WIRE-INTO-PROJECT.md:971` spells
`<prefix>/policy/policy.py`. Arm 6 (`:236-237`) reds a waiver row whose kit the playbook does name.
This pass emulated the gate's own derivation (the registry kit set and `named_in_playbook`'s pattern)
at `fce5603f8`: `policy` is in the kit set and is named. So the `playbook parity` leg's arm 6 should
red today, naming `policy`. This pass did not run the leg, so the main loop confirms it (§6).

### S1 — the figures

The figures are not fixed in this spec. Two sibling units grow the fixture before this unit builds,
and this unit builds last of 72 to 78. `TOOL-dGroundRules-75` S7 adds a `zero` run, through a new
`derive_zero_plant`, to every census case of a non-family switch row. That makes existing cases cost
more without adding any. `TOOL-dGroundRules-77` adds three `GUARD_PLANTS` rows. So the case count
cannot scale the finder's 566s. The builder re-measures at this unit's own base, after 75 and 77
land.

**The measuring command.** The whole `--fixture` run is a self-test suite. The spec-token checker's
`BAR` pattern names it so (`tools/check-spec-tokens.py:390-395`), and M6 bars a pass from running
one. Naming one case makes it the direct check a pass may run. So the builder times one single-case
run per case and sums the times:

```
cat > "$TEMP/m78.py" <<'EOF'
import subprocess, sys, time
sys.path.insert(0, "tools/policy")
import check_policy, policy
names = [c[0] for c in check_policy.derive_cases(policy.load_catalogue(check_policy.KIT))]
total, worst, bad = 0.0, (0.0, ""), []
for name in names:
    t = time.monotonic()
    r = subprocess.run([sys.executable, "-B", "tools/policy/check_policy.py", "--fixture", "--strict-from",
                        "memory/builds/dClosedLoop/build/", name], capture_output=True)
    s = time.monotonic() - t
    total, worst = total + s, max(worst, (s, name))
    if r.returncode:
        bad.append(name)
print(f"{len(names)} cases {total:.1f}s worst {worst[1]} {worst[0]:.1f}s wrong {len(bad)} {' '.join(bad)}")
EOF
python -B "$TEMP/m78.py"
```

In cost this is a whole fixture pass, run one case at a time. If the role hook refuses the loop, the
builder returns the need to the main loop, which runs the same script and hands back its output line.
The run takes about ten minutes, so the builder runs it in the background and runs nothing else
beside it. A `wrong` count above 0 stops the unit. A red case is a sibling's defect, and the builder
returns it to the main loop rather than sizing from that run. Measured at `fce5603f8`, the cheapest
case (`shape-no-empty`) took 4.8s alone, so each case's process start and its guard-trace checks are
paid once per case. The sum overstates one serial run by about that much per case. For a hang bound
that errs on the safe side, and the reading says so.

**The rules.** Let `T` be the summed seconds rounded up to a whole second, and `n` the case count,
both from the command's output line.

- The budget is `T` x 1.5, rounded up to the next multiple of 10 and floored at 60. That is the
  calibration in the header of `tools/run-gates/selftest-budgets.txt`, and the rounding is how its
  own rows go: 389 x 1.5 = 583.5 is written as 590.
- The ceiling is `T` + max(F, R x `T`), rounded up to the next multiple of 10. F and R are the floor
  and fraction `tools/run-gates/ceiling-margin.txt` declares at the builder's HEAD, 120 and 1.0 at
  `fce5603f8`. That is the headroom `derive-ceilings.py --check` demands
  (`tools/run-gates/derive-ceilings.py:643`). The skeptic's x1.5 would leave the ceiling short of it,
  and the ceilings leg would red at the first runner reading. With the margin at `fce5603f8` the
  ceiling is 2 x `T`.

**Where each number lands.** The budget is the second tab-separated field of the `policy fixtures`
row in `tools/run-gates/selftest-budgets.txt`. The third field, the argv, stays empty. The fourth
field, the reading, becomes the line below, with the builder's own node tag, the date, and its base
cut to eight hex characters:

```
measured <T>s for <n> cases on node <tag> <YYYY-MM-DD> at <sha8>, the sum of one timed single-case --fixture run per case, which overstates one serial run by each case's process start, x1.5. TOOL-dGroundRules-78
```

The ceiling is the `ceiling` of the `policy fixtures` row in `tools/gate-legs.json`, the one value
that changes there.

**How the reading is recorded.** The command's whole output line goes into this unit's build ledger,
beside AC1. `T` and `n` go into the budget row's reading, as above. No row is written to
`tools/run-gates/ceiling-evidence.txt`. `derive-ceilings.py --write --observed` could write one, but
that file is MONOTONE (its header), so an overstated reading would hold the ceiling's floor above the
real cost until someone runs `--reset`. The ceiling stays UNBACKED until the close's bar run makes
the first runner reading. `--check` reports UNBACKED and does not fail. If that reading is above half
the ceiling, the next `--write` reds `leg ceilings clear their evidenced maximum` by name, and the
main loop re-sizes from it.

### S2 — the header

Header lines 38 and 39 become the two lines below. No other byte of the file changes.

```
 * a value that is not a positive integer, or is above the limit (TOOL-dGroundRules-61). No policy kit beside this one adds
 * no rule; a `cwd` in no checkout refuses, naming it (TOOL-dGroundRules-21 S38). Skipped under `--only=`. A throw inside it refuses.
```

### S3 — the resolver order

In `resolveBash`, the spread `...onPath` in `cands` becomes `onPath[0]`. The existing
`filter(Boolean)` drops it when PATH holds no `bash`. The comment above `let BASH;` becomes:

```
// The bash that can SEE the shim, by RUNNING each candidate, never by its place on PATH, in the order
// the policy kit's checker's `resolve_bash` takes: GOV_BASH, then the first `bash` PATH names, then
// Git for Windows' two paths, then the bare name, each kept only when `test -f` on the shim exits 0
// under it. On Windows the bare name reaches the System32 WSL launcher, which cannot open a `C:/`
// path (gotcha subprocess-resolves-a-different-shell). Found once per process.
```

The file header's sentence at `:33-34` ("by running each candidate as the policy kit's checker finds
it") states no order, and S3 makes it true, so it stays. `runShim`'s refusal text, "GOV_BASH, PATH's
bash and Git for Windows' two were each run", stays true too. In `tools/policy/README.md` (`:316`),
the words `PATH's, then Git for Windows' two,` become
`the first bash PATH names, then Git for Windows' two and the bare name,`.

Readers of `resolveBash`: only `runShim` in the same file. `git grep resolveBash` finds no other
caller, and the module exports only `readPolicy` and `PolicyRefusal` (`:183`). Agent-cap reaches the
resolver through `readPolicy` (`tools/hooks/agent-cap.js:469` and `:1797`). The checker's mirror cases
reach it the same way.

What S3 does not make equal: on Windows `shutil.which` searches the current directory first and
tries each PATHEXT name. The JS tries `bash.exe`, then `bash`, in each PATH directory. The two agree on
the first PATH directory that holds a `bash.exe`, and they can differ when only a `bash.cmd`, or a
`bash` in the current directory, would be found. The skeptic's fix asks for the first-PATH order and
no more.

### S4 — the waiver

The `policy` row of `tools/playbook-kit-waivers.txt` goes. The file keeps its header comment and its
`lib` row. Rewriting the row's reason, the report's second option, would leave arm 6 red, because the
runbook already names the kit. So the row has to go, and with the row gone the waiver needs no charter
block. Nothing else reads the row. `git grep playbook-kit-waivers` finds only the parity gate and its
suite, the guard of `playbook parity selftest` (`tools/gate-legs.json:97`), and the registry's row for
the file (`tools/govkit/registry.toml:276`). The suite writes its own waiver file in every fixture
(`tools/check-playbook-parity.test.sh:191`).

### S5 — the help sentence

In `help/policy.md`, the four lines from "gate that enforces a size cap reads" to "has nothing to
fall back to, below." become:

```
gate that enforces a size cap reads ([the size caps](size-caps.md)). Each other key's consumer is
re-pointed by the build its catalogue row names as `owner`, so a value you set for any other key
today is checked but changes no behaviour. The one exception is an invalid file, which the push gate
refuses when it has nothing to fall back to, below.
```

The page points at the column that owns the fact and does not list the builds. The policy fixture's
help-page reader (`tools/policy/check_policy.py:1343-1371`) reads only the `## Install` section, and
this sentence is above `## How to use it`, so that reader is unaffected.

### Alternatives rejected

- Splitting the leg, so the budgets-cap and limit cases run in a guarded leg of their own. The total
  work stays the same. It needs a case selector that `--fixture` does not have, since it takes one
  case name or none (`tools/policy/check_policy.py:4495-4500`), plus a second leg row, budget row and
  guard. That is a new mechanism.
- Running the outcome cases in a bounded pool. `run_reader_refusals` sets and clears
  `os.environ["GOV_REMOTE"]` (`tools/policy/check_policy.py:2286-2292`). Every case prints to one
  stream, and the guard trace's audit hook reads the module-wide `TRACE_ROOTS`. A pool would race on
  all three.
- Leaving the `policy` waiver row with a rewritten reason. §4 "S4" gives why.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.
No kit version moves in this branch. Both JS files are shipped bytes, and the lander mints the bump at
the push boundary (`tools/govkit/govkit.py:13421`, `cmd_epoch`).

### Files touched (estimate)

- `tools/run-gates/selftest-budgets.txt`
- `tools/gate-legs.json`
- `tools/hooks/agent-cap.js`
- `tools/policy/policy-mirror.js`
- `tools/policy/README.md`
- `tools/playbook-kit-waivers.txt`
- `help/policy.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. Three scratch scripts are written
first, besides §4's measuring script. `c78.py` reads `T` and `n` back out of the budget row's
reading. It applies §4 "S1"'s two rules, with the margin read from `tools/run-gates/ceiling-margin.txt`,
and checks the case count against the live `derive_cases`. It prints `T`, `n`, the budget, the
ceiling, and `ok` or what it wanted:

```
cat > "$TEMP/c78.py" <<'EOF'
import json, math, re, sys
sys.path.insert(0, "tools/policy")
import check_policy, policy
n = len(check_policy.derive_cases(policy.load_catalogue(check_policy.KIT)))
with open("tools/run-gates/ceiling-margin.txt", encoding="utf-8") as fh:
    f0, f1 = next(r.split("\t")[:2] for r in fh if r.split("\t")[0].strip().isdigit())
with open("tools/run-gates/selftest-budgets.txt", encoding="utf-8") as fh:
    row = next(r.rstrip("\n").split("\t") for r in fh if r.startswith("policy fixtures\t"))
with open("tools/gate-legs.json", encoding="utf-8") as fh:
    c = next(leg["ceiling"] for leg in json.load(fh) if leg["name"] == "policy fixtures")
m = re.match(r"measured (\d+)s for (\d+) cases on node \S+ \d{4}-\d\d-\d\d at [0-9a-f]{8},", row[3])
if not m:
    sys.exit(f"{n} {row[1]} {c} WRONG: the reading names no measured seconds and case count")
t, cases = int(m.group(1)), int(m.group(2))
want_b = max(60, -(-3 * t // 20) * 10)
want_c = math.ceil((t + max(int(f0), float(f1) * t)) / 10) * 10
ok = (int(row[1]), c, row[2], cases) == (want_b, want_c, "", n)
print(t, n, row[1], c, "ok" if ok else f"WRONG want {want_b} {want_c} for {n} cases")
EOF
```

`p78.js` stubs `child_process.spawnSync` before it loads the module. Each bash candidate then reads
as unable to see the shim, and the script prints every candidate `resolveBash` tried, in order. PATH
holds two scratch directories, D1 and D2, each holding a file named `bash`:

```
cat > "$TEMP/p78.js" <<'EOF'
const fs = require("fs"), os = require("os"), path = require("path"), cp = require("child_process");
const d1 = fs.mkdtempSync(path.join(os.tmpdir(), "p78a-")), d2 = fs.mkdtempSync(path.join(os.tmpdir(), "p78b-"));
for (const d of [d1, d2]) fs.writeFileSync(path.join(d, "bash"), "");
process.env.PATH = [d1, d2].join(path.delimiter); process.env.GOV_BASH = "GB";
const tried = [];
cp.spawnSync = (c, args) => c === "git" ? { status: 0, stdout: process.cwd() + "\n" } : (tried.push(c), { status: 1 });
const { readPolicy } = require(path.resolve(process.argv[2]));
try { readPolicy("runtime.agents-in-flight", { repo: process.cwd() }); } catch (e) { tried.push("refused:" + (e.constructor.name)); }
console.log(tried.map((c) => c.split(d1).join("D1").split(d2).join("D2").split(path.sep).join("/")).join(" ; "));
EOF
```

After S3, `p78.js` is expected to print this line:

```
GB ; D1/bash ; C:/Program Files/Git/bin/bash.exe ; C:/Program Files/Git/usr/bin/bash.exe ; bash ; refused:PolicyRefusal
```

`w78.sh` applies the parity gate's `named_in_playbook` pattern (`tools/check-playbook-parity.sh:222`)
to every waived kit. It prints the last waived kit the playbook names, or `none`, then the count of
waiver rows:

```
cat > "$TEMP/w78.sh" <<'EOF'
hit=none
for k in $(grep -vE '^[[:space:]]*(#|$)' tools/playbook-kit-waivers.txt | awk '{print $1}'); do
  grep -qE "tools/$k/|<prefix>/$k/|\`$k/\`|<!-- kit:$k -->" coding-governance-agents.template.md WIRE-INTO-PROJECT.md && hit="$k"
done
echo "$hit $(grep -cvE '^[[:space:]]*(#|$)' tools/playbook-kit-waivers.txt)"
EOF
```

The `policy fixtures`, `playbook parity` and `leg ceilings clear their evidenced maximum` legs are
gates this pass may not run. The main loop runs them at the close (§6).

- **AC1** — When `python -B "$TEMP/c78.py"` runs, it prints the `T` and `n` of the builder's
  measuring run, as the ledger records them, then the budget and the ceiling §4 "S1" derives from `T`,
  then `ok`.
  Red when: the row keeps its old reading. The script then exits 1 and prints the line
  `146 60 300 WRONG: the reading names no measured seconds and case count`, as it did at `fce5603f8`. Red also when either figure is
  not the one its rule gives, or when the case count no longer matches `derive_cases`. A scratch copy
  holding a 600s reading for 146 cases, a budget of 900 and a ceiling of 1200 was measured printing
  `600 146 900 1200 ok`.
- **AC2** — When `grep -c 'in no checkout, adds no rule' tools/hooks/agent-cap.js` runs, it prints `0`.
  Red when: the header keeps the fail-open sentence. At `fce5603f8` it printed `1`.
- **AC3** — When `grep -cF 'in no checkout refuses, naming it (TOOL-dGroundRules-21 S38). Skipped under' tools/hooks/agent-cap.js` runs, it prints `1`.
  Red when: the header is reworded other than as §4 "S2" gives, or the sentence is cut rather than
  amended. At `fce5603f8` it printed `0`.
- **AC4** — When `node "$TEMP/p78.js" tools/policy/policy-mirror.js` runs, it prints the expected
  line given above the criteria.
  Red when: `cands` still spreads every PATH `bash`. At `fce5603f8` the line held `D2/bash` after
  `D1/bash`. A copy of the module with `onPath[0]` staged in was measured printing the line above.
- **AC5** — When `grep -c 'PATH names in order' tools/policy/policy-mirror.js` runs, it prints `0`.
  Red when: the comment above `let BASH;` still describes every PATH `bash`. At `fce5603f8` it
  printed `1`.
- **AC6** — When `grep -c "the first bash PATH names, then Git for Windows' two and the bare name," tools/policy/README.md` runs, it prints `1`.
  Red when: the README still reads `PATH's, then Git for Windows' two,`. At `fce5603f8` it printed
  `0`.
- **AC7** — When `bash "$TEMP/w78.sh"` runs, it prints `none 1`.
  Red when: the `policy` row stays, whatever its reason, so the script prints `policy 2`, as it did
  at `fce5603f8`. A scratch copy of the three files without the row was measured printing `none 1`.
- **AC8** — When `grep -c 'Later dGroundRules units' help/policy.md` runs, it prints `0`, and
  `grep -c 'the build its catalogue row names as' help/policy.md` prints `1`.
  Red when: the page keeps the old sentence. At `fce5603f8` they printed `1` and `0`.

## 6. Gates

`policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `playbook parity selftest` · `playbook parity` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `workflow script syntax` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

These legs come from running `derive_guarded_legs` (`tools/check-spec-tokens.py:589`) over
`tools/gate-legs.json` at `fce5603f8`, with `BROAD_LEG_FLOOR = 5` (`:362`). `tools/gate-legs.json`
joins `run-gates canary`, `run-gates gov canary`, `measure-legs selftest` and `policy fixtures`.
`tools/hooks/agent-cap.js` joins the five hooks-kit self-tests through `tools/hooks/` (5 legs, not
broad) and `policy fixtures` through its own row. `tools/policy/policy-mirror.js` and
`tools/policy/README.md` join `policy fixtures` through `tools/policy/`. `help/policy.md` joins it
through its own row. `tools/playbook-kit-waivers.txt` joins `playbook parity selftest`.
`tools/run-gates/selftest-budgets.txt` joins none, since its guards `tools/run-gates/` and `tools/`
are broad.

The unguarded legs are named because the edit is in what they read. `every held leg is budgeted,
every budget row resolves` reads the budget row. `leg ceilings clear their evidenced maximum` reads
the ceiling, with no evidence row for it yet (§4 "S1"). `playbook parity` reads the waiver file, and
the main loop should see its arm 6 go from red, naming `policy`, to green (§4 "Evidence").
`workflow script syntax` parses every tracked `.js`. `kit epoch` reads both JS files as shipped bytes,
and the lander mints their bump.

The `policy fixtures` run at the close is the first runner reading of the leg at its new ceiling, so
it is the observation S1 is for. No arm is added or moved, so this unit declares no new suite arm. No
floor or pinned count moves: no file pins this leg's budget or ceiling (`git grep "policy fixtures"`
over `tools/`), and the leg count does not change.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the closing review's findings M4 (id 11), L1 (id 7), L2
  (id 8) and L3 (ids 12 and 14), and this unit's spec brief, grounded at `fce5603f8`. Every premise
  holds. The case count was measured by calling `derive_cases`, and the resolver order by a stubbed
  `spawnSync` probe against the module and a staged copy. M4 takes the skeptic's first option, as the
  main loop directed. The builder re-measures at this unit's own base, after units 75 and 77 grow the
  fixture, by one timed single-case run per case, so no figure is fixed here. Its ceiling is sized by
  `derive-ceilings.py`'s margin, not by x1.5, which that leg would red. No evidence row is written,
  because the overstated sum would stand in a file that only rises. L2 takes the skeptic's
  corrected fix. L3 takes the deletion half of the first option, because the parity gate's arm 6 reds
  any kept row: the runbook already names the kit. Each left-shift gate goes to §7. The brief's leg
  item names §6; in this Tier-1 shape the Gates section is §6, and the leg lines sit there. The
  review report and the brief, both untracked when this draft was written:

```
memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-78-spec-brief.md
```
- rev-2 · 2026-10-25 · the five follow-up bullets move out of §7 into the prose below, so §7 reads
  `none` and check 12 can grade a CLOSED flip.

Follow-ups the main loop files as asks, none of them one arm of a mechanism here. M4's left-shift
gate is an ask for a check that compares each budget row's recorded case count with its leg's live
`derive_cases` length and goes red past a 25% drift. L1's left-shift gate is an ask for a bug-class
checklist entry, "an amendment leaves its other half standing", under which a unit that changes a
rule's behaviour greps the file header and the kit README for the old wording. L2's left-shift gate
is an ask for a JS-resolver row in the resolver parity table (`tools/lib/resolve-python.test.sh:186`),
compared by candidate order rather than bytes, starting from AC4's probe. L3's left-shift gate is an
ask for each waiver row's reason to carry a machine-checkable condition, such as "no consumer reads
X", that the parity gate re-tests. The last is an ask to rewrite the stale "lands dark" paragraph of
`tools/policy/README.md` (`:9-14`), which still says no consumer calls the reader and no hook reads
the mirror.

## 9. Reuse audit

This unit builds no mechanism. S1 edits the two declared figures in their own files, sized by the
rules those files already state: the x1.5 calibration in the header of
`tools/run-gates/selftest-budgets.txt`, and `derive-ceilings.py`'s margin from
`tools/run-gates/ceiling-margin.txt`. The out-of-band evidence route, `derive-ceilings.py --observed`,
was the seam to extend. It does not fit. The builder's per-case sum overstates one run, and that
route writes into a file that only ever rises (§4 "S1"). The measuring script reuses the
single-case form of `--fixture` that `main` already parses (`tools/policy/check_policy.py:4495-4500`). S3 narrows `resolveBash` to the order of the canonical `resolve_bash` and adds no resolver. S4
and S5 edit text. The probes reuse the module's own `derive_cases` and `readPolicy`, and the parity
gate's own pattern.
`python tools/codebase-map/reuse_lookup.py "resize a gate leg ceiling and its selftest budget row from a measured reading"`
ranked only name stems (`rows`, `row`, `read`, `legs`), and none of them sizes a ceiling. The recall
probe returned this unit's brief and run row, plus the backlog asks `TOOL-dGroundRules-109` to `-111`
on the leg's guard, which do not touch its figures.

Recall terms used: `python tools/memory-recall/query.py "policy fixtures leg budget ceiling stale case count resolveBash first PATH bash waiver lands dark" --terms "selftest-budgets derive-ceilings --observed resolve_bash playbook-kit-waivers"`

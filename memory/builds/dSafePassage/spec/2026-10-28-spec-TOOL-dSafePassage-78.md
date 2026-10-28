# TOOL-dSafePassage-78 — the govkit selftest arms red at the build's head: three arms read against the product they grade, and a walk run over a receipt below schema 3

**Status:** CLOSED · rev-2 · 2026-10-29 · node a · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dSafePassage-78-ledger.md](../build/2026-10-28-build-TOOL-dSafePassage-78-ledger.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-78-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-78-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-78-build-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-78-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-78-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-78-spec-brief.md) | research | — |
| [2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 |

<!-- /gen:spec-records -->

## 1. Goal

The close's New-arm observation of batch b found 17 `tools/govkit/selftest.py` arms of this build's
own units red at `83817478f` whatever break was staged, so the govkit selftest leg is red at the
build's head. This unit makes each pass for the right reason. For each item it reads which side is
wrong: three of the four are arms written against a product their own unit or a later one changed,
and one is the product, which walks a receipt its first step refuses.

## 2. Scope (IN)

- **S1** — `[dSP-2] S2` ×3, the arm is wrong. The in-process block of `check_step_walk`
  (`tools/govkit/selftest.py:4426-4453`) gives each case a scratch target that is no repository
  (`:4428`, `:4441-4443`). Since `015fa02e3` (TOOL-dSafePassage-30) every spawn first reads the
  repositories a step could enter, starting with `git -C <target> rev-parse --absolute-git-dir`
  (`tools/govkit/upgrade_steps.py:1496`), so each case refuses at the witness, before the refusal it
  asserts (`:1703-1707`). Each case's target becomes a `git init` repository, and the `unstaged` case
  holds `.git/index.lock`, so git still refuses the step's writes (`:1932-1934`). The `escaping` case
  asserts its path and not the step id: the containment refusal names the path only
  (`upgrade_steps.py:1044`), as the builder's own probe recorded ("each refused naming the step or
  the path", `f82623237`) and as TOOL-dSafePassage-72 AC3 keeps it. The block's comment
  (`selftest.py:4426-4428`) says three refusals and a repository target. Observed by AC1, over the
  edited block; the block's run is §7's first New arm, observed red then green at the close.
- **S2** — `[dSP-3 AC2]` ×2, the product is wrong. An unscoped `update --write` over a schema-2
  receipt reaches the walk with the receipt still at 2: the lift to 3 is the clean run's re-stamp
  (`tools/govkit/govkit.py:12733-12740`), after the walk, and the pre-walk write (`:11720`) persists
  2. The walk's first step, `govkit/receipt-schema-4`, refuses below 3 by design
  (`tools/govkit/steps/receipt_schema_4.py:46-48`), so every such run stops there, exits 1, and
  leaves the receipt at 2 for the next run to stop at again (`govkit.py:12724-12725`). The walk
  branch (`:11714-11718`) walks no step on a receipt below schema 3, printing `steps: not walked`
  with its reason and the pending count, as it does for `--kits` and a run with findings. The clean
  run's stamp lifts the receipt to 3, and the next `update --write` walks from there. The comment
  above the walk (`:11702-11708`) names the third condition. Both arms then hold as written.
  Observed by AC2.
- **S3** — `[dSP-3 AC9]`, the arm is wrong. TOOL-dSafePassage-3 AC9 observes a clean
  `update --write` "with no walk", and the arm's loop (`selftest.py:4741-4749`) runs an unscoped
  update, which since TOOL-dSafePassage-2 walks the schema step and lifts a schema-3 receipt to 4 by
  design (the `[dSP-15]` `schema-3-update` row, `selftest.py:4390-4392`). The loop's run passes `--kits` with the installed kit, a run
  that walks no step (`govkit.py:11714-11716`), and its comment (`selftest.py:4741`) says so.
  Observed by AC3.
- **S4** — The page. The `--kits` bullet of `help/upgrade-steps.md` (`:218-220`) gains S2's
  sentence, §4 "The page". Observed by AC4.
- **S5** — `[dSP-8] AC3`, the arm is wrong. It compares the source receipt's `files` with every
  `plan` row but `UNRES.` (`selftest.py:5032-5033`), 337 destinations against 231 rows, PINNED as
  measured at `83817478f`. TOOL-dSafePassage-35 S1 and S2 narrowed the receipt to the rows `apply`
  lands, `kind == "write"` with nothing missing (`govkit.py:9372-9374`), so the 87 `ORDER`, 16
  `SIDE` and 3 `BLOCK` destinations are absent by design. The arm reads its destinations through
  `extract_plan_writes(pl.stdout, with_kept=True)` (`selftest.py:250-257`), plan's `write` and
  `KEEP` rows, in place of its own filter. Observed by AC5.
- **S6** — `[dSafePassage-6] AC6 … --expect <other> … missing` ×10, the arm is wrong. Its check
  (`selftest.py:19185`) requires `"MISS" not in _p.stdout` on every case. TOOL-dSafePassage-26 S9
  (`dfcef45a7`) added the ten cases that exit 1 by design (`:19156-19161`), and
  `print_observations` prints `MISS` on every unmatched observation (`tools/govkit/shims.py:485-494`).
  The check asserts `(_rc == 1) == ("MISS" in _p.stdout)`, the form its sibling `_rte_cases` check
  already uses (`selftest.py:19222-19223`). Observed by AC6.

## 3. Non-goals (OUT)

- Any red arm outside these 17, in this suite or another batch's.
- The wording of the refusal a non-repository target meets. TOOL-dSafePassage-76 S8 re-words it.
- `run_step_walk`'s unread sixth parameter. TOOL-dSafePassage-76 S7 takes it out of the signature
  and out of the call S1 edits (`selftest.py:4448`).
- Naming the step in the containment refusal. §4 "Alternatives rejected" says why.
- The page's "Until the deployer runs steps itself" sentence (`help/upgrade-steps.md:184`) is
  TOOL-dSafePassage-76 S9's, which replaces it.

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-2's walk and its in-process
refusal arm; TOOL-dSafePassage-3's receipt schema, its stamp and its AC2 and AC9;
TOOL-dSafePassage-6's shim fixture; TOOL-dSafePassage-8's source receipt; TOOL-dSafePassage-15's
schema-3 walk; TOOL-dSafePassage-26's window cases; TOOL-dSafePassage-30's repository read;
TOOL-dSafePassage-35's filtered population; TOOL-dSafePassage-62's pre-walk write. The edge join
counts CLOSED specs, and a CLOSED spec cannot take the matching line.

## 4. Design

### The items, and the side found wrong

Each red was reproduced at `83817478f` in a `git clone --shared` under the temp root, one check
function or one inline block at a time.

| Item | Red at the head | Side wrong | The line that shows it |
|---|---|---|---|
| `[dSP-2] S2` ×3 | `fx/x witness: ... rev-parse --absolute-git-dir exits 128: fatal: not a git repository` | the arm: its target is no repository | `upgrade_steps.py:1496`, from `015fa02e3`; the arm's comment `selftest.py:4428` |
| `[dSP-2] S2` escaping, once the target is a repository | `'../x.txt' is not a path inside the target, so no step may write it` | the arm: it asks the step id of a refusal that names the path | `upgrade_steps.py:1044`; `f82623237`'s message |
| `[dSP-3 AC2]` ×2 | `walk stopped at govkit/receipt-schema-4: exit 1: ... schema 2 is below 3` | the product: the walk runs before the stamp lifts the receipt | `govkit.py:11720` writes 2, `:12739-12740` lifts after; `receipt_schema_4.py:46-48` |
| `[dSP-3 AC9]` | schema-3 receipt read back at 4 | the arm: it walks where AC9 says no walk | TOOL-dSafePassage-3 AC9 "with no walk"; `selftest.py:4390-4392` |
| `[dSP-8] AC3` | `231 rows, 337 destinations` | the arm: its filter predates TOOL-dSafePassage-35 | `govkit.py:9372-9374`; `selftest.py:5032-5033` |
| `[dSafePassage-6] AC6` ×10 | `exit 1, expected 1: ... MISS` | the arm: `MISS` is the exit-1 case's own line | `shims.py:485-494`; `selftest.py:19185` |

### S1: the walk-refusal block

The block keeps its three cases and its in-process call. Inside `with tempfile.TemporaryDirectory`,
before `(t / ".governance").mkdir()`:

```python
subprocess.run(["git", "init", "-q", str(t)], check=True)
if case == "unstaged":
    (t / ".git" / "index.lock").write_text("", encoding="utf-8")
```

The check's condition becomes `(case == "escaping" or "fx/x" in refused) and needle in refused`. The
`escaping` needle already names its path. A held `index.lock` is git's own refusal of any index
write, so the `unstaged` case reaches `write_step_staged`'s `Refusal` through the same
`git_pathspec` call an adopter's run takes. The comment reads: the walk's three refusals, in process,
over a scratch repository: a step that leaves the receipt unreadable, a step's writes git will not
stage while another process holds the index lock, and a before-image naming a path outside the
target.

### S2: the walk branch

The `elif` at `govkit.py:11714` gains `or schema < 3`, `schema` being the receipt's as loaded
(`:9471`), the value the back-fill reads (`:9659`). Its message adds a third reason after the two it
has:

```
govkit update — steps: not walked — the receipt is at schema <n>, and its first step starts from 3: this run lifts it to 3, and the next `update --write` walks them · <k> pending
```

Nothing else moves. The run is clean, so the stamp lifts the receipt to 3 (`:12739-12740`) with
every row back-filled, and `derive_pending_steps` reads pending from the receipt's `steps` alone
(`upgrade_steps.py:1807-1814`), so the next run walks every step. A run whose role-distrust arm
fired (`govkit.py:10068`) has a finding and is not stamped, as today.

### S3: the AC9 loop

`p = run("update", "--target", str(t), "--write", "--kits", kit)` at `selftest.py:4745`, and the
comment at `:4741` reads: a clean `update --write` that walks no step, a `--kits` run, never moves a
receipt past 3 by itself, and keeps a 4. The labels stay.

### The page

Appended to the `--kits` bullet at `help/upgrade-steps.md:218-220`:

> A receipt below schema 3 is not walked either: the run prints `steps: not walked`, a clean run
> lifts the receipt to 3, and the next `update --write` walks from there.

The parenthesis at `:176-177`, "a receipt below 3 is refused: run `update` first, which lifts it to
3", is what S2 makes true, and stays.

### S5 and S6: the two checks

`dests = extract_plan_writes(pl.stdout, with_kept=True)` at `selftest.py:5032-5033`. The `[hole`
line filter goes with the hand-written set: a hole row is `ORDER`, which the helper never reads
(`selftest.py:263-264`). The shim check at `:19185` becomes
`_p.returncode == _rc and _line in _last and (_rc == 1) == ("MISS" in _p.stdout)`.

### The probes

Each runs from the root of a `git clone --shared` of the build head under the temp root, from a
file written to the scratchpad, and loads no `tools/govkit/selftest.py`.

The schema probe, for AC2 and AC3: `python <scratch>/schema_probe.py <schema> [update args...]`.
It installs `check-wiring` into a scratch target, plants the receipt at `<schema>` with no `steps`
(below 3, one engine row's `gov_oid` taken out), commits, and runs `update --write` with the extra
arguments. It prints the exit, the schema, whether the row's `gov_oid` is back, the first `steps`
row, and the run's `steps:` line; below 3 it commits and runs `update --write` again and prints the
second run's exit, schema and first `steps` row.

```python
import json, pathlib, subprocess, sys, tempfile
sys.path.insert(0, "tools/govkit")
from fixture_target import build_target
schema, extra = int(sys.argv[1]), sys.argv[2:]
gk = pathlib.Path("tools/govkit/govkit.py").resolve()
deploy = ('gov_source = "local"\nprefix = "tools"\nkits = ["memory-tree"]\n\n[answers]\nmemory_root = "memory"\n'
          'playbook_path = "docs/PARALLEL.md"\nplaybook_dir = "docs"\nmanifest_path = "docs/SESSION-KICKOFF.md"\n'
          'user_skills = "~/.claude/skills"\n')
t = build_target(pathlib.Path(tempfile.mkdtemp(prefix="p78-")), deploy)
go = lambda *a: subprocess.run([sys.executable, str(gk), *a], capture_output=True, text=True, encoding="utf-8")
def commit(msg):
    subprocess.run(["git", "-C", str(t), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(t), "commit", "-qm", msg], check=True)
assert go("apply", "--target", str(t), "--kits", "check-wiring").returncode == 0
commit("install")
rp = t / ".governance/install.json"
rec = json.loads(rp.read_text(encoding="utf-8"))
rec["schema"] = schema
rec.pop("steps", None)
row = next(f for f in rec["files"] if f.get("role", "engine") == "engine" and f.get("commit"))
oid = row.pop("gov_oid") if schema < 3 else row.get("gov_oid")
rp.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
commit(f"schema {schema}")
p = go("update", "--target", str(t), "--write", *extra)
rec = json.loads(rp.read_text(encoding="utf-8"))
filled = next(f for f in rec["files"] if f["path"] == row["path"]).get("gov_oid") == oid
print(p.returncode, rec.get("schema"), filled, [(s["id"], s["state"]) for s in rec.get("steps") or []][:1])
print([ln for ln in p.stdout.splitlines() if "steps:" in ln][:1])
if schema < 3:
    commit("first update")
    q = go("update", "--target", str(t), "--write")
    rec = json.loads(rp.read_text(encoding="utf-8"))
    print(q.returncode, rec.get("schema"), [(s["id"], s["state"]) for s in rec.get("steps") or []][:1])
```

The source probe, for AC5. It prints whether the receipt's paths equal plan's `write` and `KEEP`
rows, then whether they equal every row but `UNRES.`, the set the arm compares today:

```python
import json, pathlib, subprocess, sys, tempfile
gov = pathlib.Path.cwd()
c = pathlib.Path(tempfile.mkdtemp(prefix="p78-")) / "gf"
subprocess.run(["git", "clone", "-q", str(gov), str(c)], check=True)
go = lambda *a: subprocess.run([sys.executable, str(c / "tools/govkit/govkit.py"), *a, "--target", str(c)],
                               capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(c))
assert go("update", "--write").returncode == 0
files = {f["path"] for f in json.loads((c / ".governance/install.json").read_text(encoding="utf-8"))["files"]}
rows = [(ln[2:].split("[", 1)[0].strip(), ln.split("]", 1)[1].split("<-")[0].strip())
        for ln in go("plan").stdout.splitlines() if ln.startswith("  ") and "]" in ln and "<-" in ln]
print(files == {d for m, d in rows if m in ("write", "KEEP")}, files == {d for m, d in rows if m != "UNRES."})
```

### Measured at writing time

At `83817478f`, in the clone: the schema probe at `2` printed `1 2 True []`; with S2 staged it printed `0 3 True []`, the not-walked line and
`0 4 [('govkit/receipt-schema-4', 'applied')]`; at `3 --kits check-wiring` it printed
`0 3 True []`; the source probe printed `True False`. With S1 to S3, S5 and S6 staged together,
`check_receipt_schema`, `check_source_mode`, the walk-refusal block and the shim block each printed
no failure.

### Inventory

None minted. No function, flag, key, fixture plant or arm label is added: the labels of S1, S3, S5
and S6 stay, and S2 adds a reason to an existing line. No `Refusal` site is added, so
`tools/govkit/refusal_join.py`'s count does not move.

### Migration

None. A receipt below 3 that a past run left there takes one more `update --write` to reach 4.

### Rollout

Live at landing, at order 16. TOOL-dSafePassage-72 to -76 write `tools/govkit/selftest.py`, and
TOOL-dSafePassage-72, -73, -75, -76 and -77 write `help/upgrade-steps.md`, all at order 16, so M6
sequences this unit after them by order of dispatch. TOOL-dSafePassage-76 S7 edits the same call S1
edits (`selftest.py:4448`), and its S9 adds a no-walk line beside the bullet S4 extends.

### Files touched (estimate)

- `tools/govkit/selftest.py`
- `tools/govkit/govkit.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **The walk names the step on a containment refusal.** It departs from TOOL-dSafePassage-2's own
  record of the case and from TOOL-dSafePassage-72 AC3, which keeps the message, and the receipt
  already names the step: move 3 records it `interrupted` before the up (`upgrade_steps.py:1998-1999`).
- **A walk that accepts a target with no repository.** The walk stages a step's writes with git
  (TOOL-dSafePassage-2 S11), and TOOL-dSafePassage-30 reads every repository a step could enter, so a
  target that is no repository has nothing the walk can stage into or clear.
- **S2 as a lift to 3 in the walk branch, so one run reaches 4.** Measured: the schema probe then
  prints `0 4 True [...]`. It writes schema 3 on the pre-walk write of a run that can still end with
  findings, where `govkit.py:12720-12723` forbids a stamp, and the next run skips both schema-gated
  guards (`:9659`, `:10068`). It also makes the AC2 arm, the page parenthesis and the step row's
  comment (`tools/govkit/steps.toml:12-13`) wrong where S2 makes them true.
- **S2 as the schema step lifting 2 to 3.** TOOL-dSafePassage-3 deviation 165 refused it: it skips
  `update`'s back-fill, so the integrity preamble refuses that receipt forever.
- **The AC2 arms scoped with `--kits`, as S3 does for AC9.** They would pass and hide that every
  unscoped `update --write` over a receipt below 3 stops at the schema step, run after run.
- **S5 through `read_plan_destinations`.** The arm would read the receipt's writer's own filter, a
  guard sharing state with what it guards; `extract_plan_writes` reads plan's printed rows.

## 5. Production-readiness checklist

- security: no new write path. S2 writes less: a run over a receipt below 3 spawns no step.
- perf / scale: S1 adds one `git init` per case; S2 saves the doomed schema-step spawn.
- error / empty / loading states: a receipt below 3 gets `steps: not walked` and its reason in place
  of a stopped walk and exit 1.
- observability: the not-walked line names the schema and the next run that walks.
- risks: a receipt below 3 reaches 4 in two runs, not one; the page says so. S1's `index.lock` is
  inside a scratch repository the block owns.
- testing: the four arms of §7, each staged red by today's code, §6 AC1's grep, and §4's two probes.
- migration: none.
- user docs: S4's sentence.

## 6. Acceptance criteria

- **AC1** — When `git grep -n -F -e '"git", "init", "-q", str(t)' -e '".git" / "index.lock"' -e 'case == "escaping" or "fx/x" in refused' -- tools/govkit/selftest.py`
  runs, it prints three lines, each inside `check_step_walk`.
  Red when: the block still builds its target with no repository, so the first pattern prints
  nothing.
- **AC2** — When §4's schema probe runs as `python <scratch>/schema_probe.py 2`, it prints
  `0 3 True []`, a line holding `steps: not walked — the receipt is at schema 2`, and
  `0 4 [('govkit/receipt-schema-4', 'applied')]`.
  Red when: the walk runs over the schema-2 receipt, and the first line reads `1 2 True []`.
  cost: two installs and three `update` runs, under a minute.
  fixture: a `git clone --shared` of the build head under the temp root.
  figure: PINNED, measured at `83817478f`.
- **AC3** — When the schema probe runs as `python <scratch>/schema_probe.py 3 --kits check-wiring`,
  it prints `0 3 True []`, and
  `git grep -n -F 'run("update", "--target", str(t), "--write", "--kits", kit)' -- tools/govkit/selftest.py`
  prints the AC9 loop's line.
  Red when: the loop still runs unscoped, so the grep prints nothing and its schema-3 case reads 4.
- **AC4** — When `git grep -n -F "A receipt below schema 3 is not walked either" -- help/upgrade-steps.md`
  runs, it prints one line, inside the `--kits` bullet.
  Red when: the page is silent on the not-walked run, so an adopter reads it as a fault.
- **AC5** — When §4's source probe runs, it prints `True False`, and
  `git grep -n -F "dests = extract_plan_writes(pl.stdout, with_kept=True)" -- tools/govkit/selftest.py`
  prints one line.
  Red when: the arm still compares every row but `UNRES.`, so the grep prints nothing; or the receipt
  gains an `ORDER` or `SIDE` destination, so the probe's first value prints `False`.
  cost: a clone of gov, one source-mode `update` and one `plan`, about a minute.
  fixture: a `git clone --shared` of the build head under the temp root.
- **AC6** — When `python tools/govkit/shims.py --fixture --plant window --window 2 --releases 1 --expect allowed`
  runs, it exits 1 printing `MISS` and `0 of 1 observation(s) matched`; with `--expect held` it exits
  0 and prints no `MISS`; and `git grep -c -F '(_rc == 1) == ("MISS" in _p.stdout)' -- tools/govkit/selftest.py`
  prints `2`.
  Red when: the shim check still requires `"MISS" not in _p.stdout`, so the grep prints `1`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the three `[dSP-2] S2` rows of `check_step_walk`, staged red by a working copy whose block builds its target with no `git init`, as at `83817478f` · none
New arm: tools/govkit/selftest.py · covers AC2 AC3 · the `[dSP-3 AC2]` and `[dSP-3 AC9]` rows of `check_receipt_schema`, staged red by a `govkit.py` copy whose walk branch walks a receipt below 3, and by the AC9 loop run unscoped · none
New arm: tools/govkit/selftest.py · covers AC5 · the `[dSP-8] AC3` files row of `check_source_mode`, staged red by the arm's filter at `83817478f`, every row but `UNRES.` · none
New arm: tools/govkit/selftest.py · covers AC6 · the ten `[dSafePassage-6] AC6 ... missing` rows of `main`'s shim block, staged red by the check at `83817478f`, `"MISS" not in _p.stdout` · none

AC4 is a grep. No floor moves: each arm keeps its count of `check` calls.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-78-1-spec-writer.md`. The
  17 reds are the batch-b close observation's, run by
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`;
  each was reproduced at `83817478f` in a `git clone --shared` under the temp root. Two candidates
  for S2 were staged and measured in that clone; §4 "Alternatives rejected" records the one not taken.
- rev-2 · 2026-10-28 · header · S1 · §3 · §4 · §5 · §6 · §7 · AC1 · folded the round-1 spec audit,
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md`,
  at the fixes its skeptic judged sound. L9 (id 17): the walk probe ran its own `git init` and was
  green at base, so AC1 observed nothing S1 edits; AC1 and the walk probe leave the spec, and S1 is
  observed by the grep, now AC1, and by §7's first New arm. AC2 to AC7 renumber to AC1 to AC6, with
  every scope join and `covers` field. The fix's other option, running the block extracted from the
  suite file, was not taken: the gate-guard's D4 row refuses that file by name
  (`tools/unattended/gate-guard.js:32`), and a probe reaching it through a scratch script would only
  hide it from the guard. L12 (id 25): the §3 non-goal on `help/upgrade-steps.md:184` now names
  TOOL-dSafePassage-76 S9 as its owner, with no ask. The header's node is `a`, this host.

## 10. Reuse audit

Each item extends the code its red names. S1 keeps the block's in-process call and its three
fixture argvs (`tools/govkit/selftest.py:4430-4437`). S2 extends the walk branch's own not-walked
`elif` (`tools/govkit/govkit.py:11714-11718`) and leaves the lift to the stamp that owns it
(`:12739-12740`). S3 uses the `--kits` scope that branch already honours. S5 calls
`extract_plan_writes` (`tools/govkit/selftest.py:250-257`), the one reader of plan's write rows. S6
copies no logic: it takes the exit-and-`MISS` form of the sibling `_rte_cases` check
(`:19222-19223`). The schema probe builds its target through `build_target`
(`tools/govkit/fixture_target.py:57-73`), the factory the selftest uses. `python tools/codebase-map/reuse_lookup.py "self-test arm compares plan destinations written against a receipt and grades a fixture's expected miss"`
ranked the shell-suite name tokens `arm`, `fixture` and `miss`, then `read_plan_destinations`
(`tools/govkit/govkit.py`) and other kits' `run_fixture` and `run_plant_arms`; none grades a
fixture's expected miss or a plan's write rows outside the two seams named above, so no further
seam fits. The recall probe ranked TOOL-dSafePassage-3's spec and ledger, TOOL-dSafePassage-62 and
TOOL-dSafePassage-3 deviation 165, which S2's rejected alternative cites, and TOOL-dRetiredFork-38,
a `--kits` update re-stamping the whole receipt, which S3 does not change.

Recall terms used: `python tools/memory-recall/query.py "why does update over a schema-2 receipt stop at the schema step, and which arms assert a clean update stays at schema 3" --terms "receipt schema 2 3 4 back-fill gov_oid stamp walk receipt-schema-4 lifts preamble update"`

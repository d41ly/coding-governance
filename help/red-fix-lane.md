# The red-fix lane

**What it is.** A product change needs a specced unit: the write gate refuses a write under a
product path with no buildable unit behind it, and the commit grader refuses a commit that names
none. The red-fix lane is the one exception. While a gate leg is recorded red, the fix for it may
be written and committed with no spec, and a typed record of the fix follows as the next commit.
Every other product write keeps its route through a specced unit.

The lane is three parts in two kits. The hooks kit's write gate, `scratch-guard.js`, admits the
write. The memory-tree kit's commit grader, `routed_commits.py`, admits the commit and holds it to
four limits. The same kit's `build_records.py` writes the record and joins every fix to its record.

## What opens the lane

A red row of the gate ledger. The ledger is `gate-ledger.tsv` under the worktree's own git dir,
and the bar runner and a [pass-leg run](pass-legs.md) both write it. The lane is open while it
holds a row whose status is `fail` or `timeout`.

The write gate asks the lane only when it is about to refuse a product write, and admits it when
all three hold:

- the switch below reads `on`, or no policy kit resolves beside the hook;
- the ledger holds an open red;
- the writer is the main loop, or a role agent whose role declares `writes = product`.

It then prints one witness line naming the open legs and what the commit owes:

```text
red-fix lane admits this write — open red leg(s): <leg>; its commit owes a `Red-fix: <leg>` trailer beside `Pass: none`
```

The lane closes when the leg next runs green: a ledger row stands until the runner next records
that leg, and the gate itself writes nothing to the ledger. A spec write never reaches the lane,
and a broken role index closes it.

## What the commit owes

A `Red-fix:` trailer naming the leg, one leg name per trailer line, in the final trailer block
beside `Pass: none`:

```text
fix(run-gates): the docs leg's stale anchor on the policy page

Red-fix: docs
Pass: none
```

The commit grader reads the trailer in place of a unit id. Each value must be a leg name of the leg
manifest in that commit's own tree. A value that names no leg, and a commit whose tree holds no
manifest, are violations that say so, and the grader's summary line counts the admitted commits as
`<n> red-fix`. A commit that names a unit as well is routed by its unit as ever, and its trailer is
still graded against the limits.

## The limits

Every commit carrying the trailer is graded against four limits, and a finding reds the grader.

| Limit | Bound |
|---|---|
| `L1 size` | at most 3 product paths and at most 60 lines over them, added plus deleted; a binary path is over |
| `L2 guarded policy file` | no path the policy kit's `guarded-paths.txt` lists; with no policy kit, no path under `.governance/` |
| `L3 spec edit` | no path under any build's `spec/` folder |
| `L4 new surface` | no product path added; a rename counts as a deletion and an addition |

The two figures of `L1` are the constants `RED_FIX_MAX_PATHS` and `RED_FIX_MAX_LINES` of
`routed_commits.py`, read on 2026-11-12. A fix that needs more than the limits allow is a unit, and
takes a spec.

Grade one commit before you push it with
`python tools/memory-tree/routed_commits.py --red-fix-limits <rev>`. It exits 0 inside the limits, <!-- usage: script:tools/memory-tree/routed_commits.py f60a87d3 -->
1 over one, and 2 when `<rev>` names no commit or the commit carries no trailer:

```text
routed-commits: red-fix limits · <sha> is inside all four · bound 3 path(s), 60 line(s)
routed-commits FAILED — a Red-fix commit is outside the inline lane's limits:
```

Under the second line it prints one line per limit the commit is over. The verb reads no waiver.

## The record

The fix's one account is a `red-fix` record in a build's `build/` folder, under the unit whose pass
the red followed or a unit of the build that last changed the fixed file. Write it through the
door, after the fix:

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries placeholders -->
```bash
python tools/memory-tree/build_records.py new red-fix --build <slug> --unit <id> \
  --leg "<leg name>" --red-line "<the failing line>" --commit <rev> --rerun "<command · result>"
```

| Field | Value |
|---|---|
| `Leg` | the leg's name as the trailer spells it, from `--leg` |
| `Red line` | the line of the failure the fix clears, from `--red-line` |
| `Files` | the commit's paths, derived from the commit |
| `Commit` | the fix commit's full sha, derived from `--commit` |
| `Rerun` | the command that showed the leg green, and its result, from `--rerun` |
| `Caused-by` | one unit id |

The door refuses, writing nothing, a rev that names no commit reachable from `HEAD`, a commit with
no `Red-fix:` trailer or none naming `--leg`, and an empty text flag. The record is the next
commit after the fix.

`python tools/memory-tree/build_records.py join red-fix` joins every `Red-fix:` commit reachable <!-- usage: script:tools/memory-tree/build_records.py#join 90d1c185 -->
from `HEAD` to its record, both ways. It exits 0 clean, 1 on a finding and 2 where git or the
records cannot be read, and its last line is the summary:

```text
build-records: red-fix join · <n> fix commit(s) · <n> record(s) · <n> owed
```

A fix at `HEAD` with no record is printed as `owed` and is no finding, because its record is the
next commit. With `--staged` the join grades `HEAD` alone and refuses that same fix, so the commit
after a fix is its record's. The memory hygiene leg runs the join as its check 31, "a red fix has
its record".

## The switch

`bar.inline-red-fixes` in `.governance/policy.toml` turns the lane on or off. <!-- usage: policy:bar.inline-red-fixes 3272585d -->

| Value | What the lane does |
|---|---|
| `on` | the default: an open red admits the write, and a `Red-fix:` commit is admitted with no unit |
| `off` | the write gate's refusal stands as it was composed, and a pushed `Red-fix:` commit that names no unit is refused as `names no unit` |

```toml
[bar]
inline-red-fixes = "off"
```

Turning the key `off` reds nothing that landed: the commit grader applies the key to the pushed
range and never to the history, so a lane commit already in history is still admitted. The key is
read at the landed revision, so a branch cannot flip its own switch. A read the policy reader
refuses, or a value that is neither `on` nor `off`, leaves the write gate's refusal standing with
one line saying why. [The policy file](policy.md) says how a key is set and read.

## What it does not check

- Whether the write fixes the red. While any leg is open the write gate admits any product path,
  and it bounds nothing: the limits are the commit grader's.
- Whether the named leg was ever red. The gate ledger is per clone and untracked, so the commit
  grader reads none, and a trailer naming a real leg passes.
- Whether a red that no run has re-measured is still red, or a ledger edited by hand, which is
  read like the runner's.
- The limits do not see whether the change is a fix, a new surface made inside an existing file, a
  deleted path, a record outside `spec/`, or a guarded list the fix commit itself shortened.
- The join does not check that the record is the fix's direct child, that `Rerun` or `Red line` is
  true, or that the leg was red.
- A leg manifest moved since a `Red-fix:` commit is looked for at the path `HEAD`'s conf names, and
  reads as absent.

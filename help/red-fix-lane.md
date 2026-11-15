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
holds an open red: a row whose status is `fail` or `timeout`, inside the bounds stated below.

The write gate asks the lane only when it is about to refuse a product write, and admits it when
all three hold:

- the switch below reads `on`, or no policy kit resolves beside the hook;
- the ledger holds an open red;
- the writer is the main loop, or a role agent whose role declares `writes = product`.

It then prints one witness line naming the open legs and what the commit owes:

```text
red-fix lane admits this write — open red leg(s): <leg>; its commit owes a `Red-fix: <leg>` trailer beside `Pass: none`
```

A red row is open only on this branch's present state. The runner carries forward every row a run
did not measure, so the gate bounds a row by the row's own head field, and counts it when all of
these hold:

- the row has the runner's nine-field form, which an older five-field row does not;
- its name is a leg of the manifest the conf key `LEG_MANIFEST` names, or, with the key blank, of
  `gate-legs.json` beside the installed run-gates kit; a blank key with no such file closes the
  lane;
- its head is `HEAD`, or an ancestor of `HEAD` that the landed revision does not reach.

So the lane stays open across the fix commit, and closes when a run records the leg green or the
branch lands. A leg a pass-leg run holds stays eligible: a full bar's red at `HEAD` opens the
lane. The gate itself writes nothing to the ledger. A spec write never reaches the lane, and a
broken role index closes it.

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

The grader finds the manifest by the conf key `LEG_MANIFEST` of `.memory-tree.conf`. With the key
blank it falls back to `gate-legs.json` beside the run-gates kit installed beside the memory-tree
kit. Where no such kit resolves inside the repository, a lane commit is a violation that reads
`LEG_MANIFEST is blank`. The write gate takes the same fallback from the hooks kit, as the bounds
above state, so a default install opens both halves of the lane with the key left blank.

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

A path-less commit owes no record. An empty commit and any merge are path-less: the join reads
neither as touching a path, whatever a merge's resolution changed. The record's `Files` is the
change it accounts for, and such a commit holds none. The door refuses it and says why:

```text
commit <sha8> touches no path, so it owes no red-fix record and the join asks none
```

`python tools/memory-tree/build_records.py join red-fix` joins every `Red-fix:` commit reachable <!-- usage: script:tools/memory-tree/build_records.py#join 90d1c185 -->
from `HEAD` to its record, both ways. It exits 0 clean, 1 on a finding and 2 where git or the
records cannot be read, and its last line is the summary:

```text
build-records: red-fix join · <n> fix commit(s) · <n> record(s) · <n> owed · <n> path-less
```

The fix count is the commits that owe a record. A path-less commit is outside it: the join raises
no finding for it at any depth, counts it in the last field, and names it on every run, one line
per trailer value. A record whose `Commit` names a path-less commit is a finding, `J2`.

```text
build-records: red-fix join · path-less · <sha8> · <leg> · touches no path, so it owes no record
```

A fix at `HEAD` with no record is printed as `owed` and is no finding, because its record is the
next commit. With `--staged` the join grades `HEAD` alone and refuses that same fix, so the commit
after a fix is its record's. A path-less `HEAD` passes there, so the next commit is not held for a
record no door writes. The memory hygiene leg runs the join as its check 31, "a red fix has its
record".

That refusal is the pre-commit hook's. The hook runs the staged hygiene leg where the commit stages
a path under the memory root, and `build_records.py join red-fix --staged` by itself where it
stages none, so a product-only commit on top of an unrecorded fix is refused too. A hook copied
before it gained that second branch runs no join on such a commit, and the unrecorded fix is then
found by the next full hygiene run.

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
one line saying why. The write gate reads the key last: with no red open, or for a writer the lane
never admits, it does not read the key and the refusal carries no such line.
[The policy file](policy.md) says how a key is set and read.

Two parts of the lane run whatever the key reads, because they grade history and not the write.
The commit grader's limits pass grades every commit carrying the trailer and prints one
`red-fix limits · graded <n>` line per graded population on every run, `graded 0` included. The
join grades every `Red-fix:` commit against its record and prints its summary line on every run.
With the key `off` both still print, and both can still red.

## What it does not check

- Whether the write fixes the red. While any leg is open the write gate admits any product path,
  and it bounds nothing: the limits are the commit grader's.
- Whether the named leg was ever red. The gate ledger is per clone and untracked, so the commit
  grader reads none, and a trailer naming a real leg passes.
- Whether a later commit of the branch already fixed the red: a row at an unlanded ancestor of
  `HEAD` stays open until a run measures its leg again or the branch lands. Nor whether the tree
  the run graded was clean, nor a ledger edited by hand or a manifest edited in the working tree,
  each read as it stands.
- The limits do not see whether the change is a fix, a new surface made inside an existing file, a
  deleted path, a record outside `spec/`, or a guarded list the fix commit itself shortened.
- The join does not check that the record is the fix's direct child, that `Rerun` or `Red line` is
  true, or that the leg was red. Nor whether a merge's resolution changed a file, or whether a
  path-less commit should carry the trailer at all: nothing refuses it at commit time.
- A leg manifest moved since a `Red-fix:` commit is looked for at the path `HEAD`'s conf names, and
  reads as absent.

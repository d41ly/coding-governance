# wave 2 — WHAT STATE IS THE WORK ACTUALLY IN?

**Serves:** research TOOL-aScouredKit-1

*Node `a`, 2026-08-30, worktree `.claude/worktrees/kit-adversarial-review-15ed31`, HEAD
`66c4891c`, `main` and `origin/main` both `14e21399`. Every figure below was derived by a command
reproduced beside it. Adversarial record audit commissioned as wave 2 of `aScouredKit`; this record
grades records, not code.*

*NOTE, added when this record was bound: the `aPairedLexer` paths quoted below are from ANOTHER
node's tree and that build does not exist here. Their id spellings carry a non-breaking hyphen so
the corpus-id scanner does not read a quoted foreign filename as a citation this tree must
resolve — the same class as the staged-break id quoted in the gates lens.*

## Verdict: BLOCKED

Two of the three answers the owner needs are bad. The index is honest, no LANDED claim is false,
and the `aScouredKit` run's own landing state is recorded straight. But **21 commits of finished,
reviewed work exist on exactly one machine and on no remote**, one of them carrying a fixed
fail-open in the fan-out guard and named nowhere in the memory tree; **one worktree has been sitting
mid-merge with 71 staged paths since 2026-08-27**; and the `aScouredKit` README asserts in its own
canonical exclusion note that three of its own CLOSED units do not exist.

---

## The bottom line first: is there work BUILT, GATED, REVIEWED and LOST?

**Yes. Two branches, 21 commits, on this machine only.**

```
$ git fetch --all -q
$ git rev-parse main origin/main
14e21399f7dd0559224837a2754fcbf9fc4a754b
14e21399f7dd0559224837a2754fcbf9fc4a754b

$ for b in $(git for-each-ref --format='%(refname:short)' refs/heads refs/remotes/origin); do
    n=$(git rev-list --count main..$b); [ "$n" != 0 ] && echo "$b : $n"; done
branch/acollapsedscan-followups          : 15 commits ahead of main
branch/kit-adversarial-review-15ed31     : 16
branch/paired-lexer-followup-9c31a2      :  6
origin/branch/kit-adversarial-review-15ed31 : 16
```

Three branches carry unmerged work. Only ONE of them (`kit-adversarial-review-15ed31`) has a
counterpart on `origin`. The other two exist as local refs on node `a` and nowhere else.

### F1 — `branch/paired-lexer-followup-9c31a2`: a whole build nobody knows about

```
$ git rev-list --count main..branch/paired-lexer-followup-9c31a2   # 6
$ git rev-list --count branch/paired-lexer-followup-9c31a2..main   # 0   <- clean fast-forward
$ git merge-base main branch/paired-lexer-followup-9c31a2
14e21399  (== main)
$ git ls-tree -r --name-only branch/paired-lexer-followup-9c31a2 memory/builds/aPairedLexer/
memory/builds/aPairedLexer/README.md
memory/builds/aPairedLexer/build/2026-08-30-build-TOOL-aPairedLexer‑1-base-measurements.md
memory/builds/aPairedLexer/build/2026-08-30-build-TOOL-aPairedLexer‑4-acceptance.md
memory/builds/aPairedLexer/reviews/2026-08-30-review-TOOL-aPairedLexer‑1-2-3-diff-round1.md
memory/builds/aPairedLexer/reviews/2026-08-30-review-TOOL-aPairedLexer‑1-2-3-spec-audit-round1.md
memory/builds/aPairedLexer/spec/2026-08-30-spec-TOOL-aPairedLexer‑{1,2,3,4}.md

$ grep -rl "aPairedLexer" memory/          # at HEAD: ZERO hits
$ git branch -r | grep paired-lexer        # ZERO hits — not on origin
```

The build's own README (on the branch) states the stakes:

> "a bounded receiver with a cap of **500** DENIES with the template terminated and **ADMITS** below
> an unterminated one. That is a fail-open on the only mechanical control against an unbounded agent
> burst"

Product diff `main..branch/paired-lexer-followup-9c31a2 -- tools/`:

| file | churn |
|---|---|
| `tools/hooks/agent-cap.js` | 223 lines |
| `tools/hooks/agent-cap.test.sh` | 220 lines |
| `tools/codebase-map/map_lib.py` | 125 |
| `tools/codebase-map/selftest.py` | 169 |

Its worktree also holds an untracked review record that is in no commit at all:

```
$ git -C C:/projects/coding-governance/.claude/worktrees/worktrees-branches-cleanup-df15b1 status --porcelain
?? memory/builds/aPairedLexer/reviews/2026-08-30-review-TOOL-aPairedLexer‑1-2-3-4-diff-round2.md
```

The build is `SPECCED` — non-terminal — so had it merged it would appear as a row in `memory/LIVE.md`.
It does not. Nothing in the merged tree records that it exists, who owns it, or that it fixes a
reproduced fail-open. Node `a`'s disk is the only copy.

### F2 — `branch/acollapsedscan-followups`: 15 commits, unpushed, and its worktree is stuck mid-merge

```
$ git rev-list --count main..branch/acollapsedscan-followups   # 15
$ git rev-list --count branch/acollapsedscan-followups..main   # 204   <- badly stale
$ git branch -r | grep acollapsedscan                          # ZERO hits — not on origin

$ p=C:/projects/coding-governance/.claude/worktrees/unattended-check-plan-27c557
$ git -C "$p" status --porcelain | wc -l
71
$ ls C:/projects/coding-governance/.git/worktrees/unattended-check-plan-27c557 | grep MERGE
MERGE_HEAD
MERGE_MODE
MERGE_MSG
$ cat .../MERGE_MSG
Merge branch 'main' into branch/acollapsedscan-followups
$ cat .../MERGE_HEAD
f5dff6aee0b0a0177fac8ec842532b461eeca71f
$ git log -1 --format='%h %cs %s' f5dff6ae
f5dff6ae 2026-08-26 merge(deployer): round 4 — ...
$ ls -l .../MERGE_HEAD
-rw-r--r-- ... Aug 27 04:53 MERGE_HEAD
$ git -C "$p" diff --name-only --diff-filter=U     # empty — every conflict resolved
```

An in-progress merge, **every conflict already resolved**, 71 paths staged, never committed, cold
since **2026-08-27 04:53** — and the `main` it was merging (`f5dff6ae`) is now 204 commits behind the
real `main`. The staged set is a whole `dCarriedReceipt` record folder (15 acceptance ledgers, 11
review records, a `RUN.md`) plus edits to `tools/govkit/govkit.py`, `tools/unattended/unattended.sh`,
`tools/run-gates/run-gates.sh`, `tools/lexicon/lexicon.py` and 17 more.

The branch's own committed work is `aCollapsedScan` units 8–13, closed:

```
$ git log --oneline main..branch/acollapsedscan-followups | head -3
f8993d62 run(aCollapsedScan): close — every declared DoD item met, phase LANDING
913c4655 records(aCollapsedScan): AC5 green — the bar itself halved, 3162 s to 1605 s
509138c6 fix(aCollapsedScan): the kit bump had five carriers, not the three the first refusal named
```

**One** record in the whole tree knows this branch exists — `memory/backlog/TOOL.md:14`
(`TOOL-aSiftedFork-4`), which says "on `branch/acollapsedscan-followups`, so no path to it resolves
from here". Honest as far as it goes. It does not say the branch is unpushed, does not say it is 204
behind, and does not say a resolved merge is sitting in its index.

### F3 — the merged record of `aCollapsedScan` understates the build and reads terminal anyway

| | ids | generated status line |
|---|---|---|
| `memory/builds/aCollapsedScan/README.md` at HEAD | `-1 … -7` (line 7) | `CLOSED · 1 unit(s)` (line 66) |
| same file on `branch/acollapsedscan-followups` | `-1 … -13` (line 7) | `CLOSED · 5 unit(s)` (line 79) |

Both say **CLOSED**. A session reading the merged tree sees a finished 7-id build and has no signal
at all that six more ids and four more units were built, reviewed and closed elsewhere.
`memory/ledger/2026-08.md:12` renders the same understatement (`CLOSED · a · tooling · 7`).

### The one that IS recorded honestly

`branch/kit-adversarial-review-15ed31` (16 commits, this build) is on `origin`, and
`memory/builds/aScouredKit/RUN.md`'s last parked entry says so in plain words: *"The merge to main and the push
have NOT happened … the build is CLOSED with every declared DoD item met and the phase is LANDING"*,
followed by the exact three commands to land it. That is what a parked landing should look like.
It is also the only one of the three that looks like it.

---

## Does the generated index agree with git?

**Yes, on both directions I could test, and it is a byte-identical render.**

```
$ git status --porcelain          # clean
$ python tools/memory-tree/gen_build_index.py --write
build-index: wrote 447 artifact(s)
$ git status --porcelain          # STILL CLEAN
```

447 generated artifacts — `memory/LIVE.md`, both `memory/ledger/*.md`, and every
`<!-- gen:build-index -->` region in every build README — re-render to the committed bytes. Nobody
has hand-edited the index.

**No LANDED claim is false.** Every `memory/builds/*/RUN.md` witness was tested for ancestry:

```
$ for f in memory/builds/*/RUN.md; do w=$(grep -m1 '^witness:' $f | sed 's/witness: //')
    git merge-base --is-ancestor "$w" main || echo "NOT ANCESTOR: $f"; done
memory/builds/aScouredKit/RUN.md      # the only one, and it is at LANDING, not LANDED
```

27 run records. 18 at `LANDED`, all 18 witnesses are ancestors of `main`. 6 `ABORTED`, same. The one
non-ancestor is this build, which is correctly at `LANDING`. **Nothing claims to have landed that
did not.**

Base shas were kept separate from work shas throughout — `RUN.md`'s `base:` and `anchor-sha:` are
ancestors by construction (`tools/unattended/unattended.sh:2506` pins them once) and were excluded
from the ancestry test rather than counted as agreement.

### F4 — one record is at LANDING about work that is already on `main`

`memory/builds/aThawedCorpus/RUN.md:15` reads `phase: LANDING` (witness on line 14), witness
`2416de50ccb05b8caac96b9ed195a263f4026706`.

```
$ git merge-base --is-ancestor 2416de50 main && echo landed        # landed
$ git log -1 --format='%h %cs' 2416de50                            # 2416de50 2026-08-27
$ grep -n aThawedCorpus memory/ledger/2026-08.md
49:| [aThawedCorpus](../builds/aThawedCorpus/README.md) | CLOSED | a | tooling | 5 |
```

The build is CLOSED, the work is on `main`, and the run record still asserts a **non-terminal**
phase (`unattended.sh:1226` — "LANDING stays non-terminal"). The driver knows this class exists and
accommodates it (`unattended.sh:1235-1246` excludes a LANDING record whose witness is an ancestor of
the anchor, printing "a finished run missing a stamp rather than a second live one") — so it does
not corrupt the live-run count. The *file* is still wrong, three days on, and nothing ever fixes it.

### F5 — `--close` writes a phase and leaves the previous phase's witness on it

`memory/builds/aScouredKit/RUN.md:14-15`:

```
witness: 3eaf38d0d57dd0206103835628a27f2c57831547
phase: LANDING
```

`3eaf38d0` is **9 commits behind** this branch's tip and sits *before* `86148e20`, the commit that
created the specs for `-30`, `-31` and `-32`. So the run's LANDING record is witnessed by a tree in
which three of its seventeen units did not exist.

`memory/guides/UNATTENDED-PROTOCOL.md:286`: *"Every phase claim carries a witness … and the witness
must be PRESENT."* `verb_close` (`tools/unattended/unattended.sh:2797`) writes `phase LANDING` and
never touches `witness` — `set_fact "$rel" witness` appears only in `verb_phase` (:2056), the landed
verb (:2235), abort (:2342) and preflight (:2551). Presence holds; correspondence does not. The
field that the LANDING-already-on-the-remote exclusion at :1236 reads is therefore, by construction,
the witness of whatever phase preceded the close.

---

## The `aScouredKit` records themselves

### F6 — the build README's canonical exclusion note is false about three of its own units

`memory/builds/aScouredKit/README.md:51`:

> **Ids `-10` and `-16` through `-34` are NOT units and carry no spec.** They are the findings this
> run reported rather than built, each a row in `memory/backlog/TOOL.md` with its own measurement.

Both halves are false for `-30`, `-31`, `-32`:

```
$ ls memory/builds/aScouredKit/spec/ | grep -E '3[012]'
2026-08-30-spec-TOOL-aScouredKit-30.md
2026-08-30-spec-TOOL-aScouredKit-31.md
2026-08-30-spec-TOOL-aScouredKit-32.md

$ grep -c "TOOL-aScouredKit-3[012] ·" memory/backlog/TOOL.md
0
```

The generated region in the same file lists all three as `CLOSED` units (README.md:99, :100, :101;
`-31` at rev-2). And the ordering is not an accident of drafting:

```
$ git log --oneline --diff-filter=A -- memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-3{0,1,2}.md
86148e20 promote: the closing loop stopped NON-CONVERGENT, and its blockers became units
$ git log -S "are NOT units and carry no spec" --oneline -- memory/builds/aScouredKit/README.md
bfa90c33 records: the exclusion note gets a canonical slot
```

`86148e20` promoted them to units. `bfa90c33`, **the very next commit**, wrote a canonical note
saying they are not units and have no specs. The note was written after the fact it denies.

### F7 — the authored roster omits 3 of 17 units, and `--plan` prints both numbers in one breath

```
$ bash tools/unattended/unattended.sh --plan aScouredKit
TOOL-aScouredKit-1     CLOSED  DONE
… 17 rows, including -30, -31, -32 …
roster: the README roster region, 14 id(s); 0 with no tracked spec
next: none - every tracked spec is terminal
```

Seventeen rows above a footer that says fourteen. The authored region
(`README.md:61-80`) names `-1 … -9, -11 … -15`; `-30/-31/-32` are absent.

This is not merely cosmetic, because the check that exists to catch it cannot:

```sh
# tools/unattended/unattended.sh:1800
local want have; want=$(roster_ids "$1") || return 3
have=$(spec_ids "$2")
comm -23 <(printf '%s\n' "$want") <(printf '%s\n' "$have")
```

`missing_units` is **roster minus specs**. A spec that the roster does not name is in the
`comm -13` direction, which nothing computes. So "the roster names a unit with no spec" reds, and
"the build holds a unit the roster never names" is invisible by construction — the one-directional
shape this repo's own §7 keeps calling out.

The build's Definition of Done is safe: `build-complete` reads `unit_ids_of` (:1689, the GENERATED
region), not the roster. But `--plan` — the verb a resuming session runs to ask what this build is —
under-reports it by three, and the README prose (F6) agrees with the wrong number.

---

## What is STRUCTURALLY UNKNOWABLE from this clone

Named plainly, because an audit that pretends to see these is worse than one that does not.

1. **Nodes `b`, `c` and `d` are other machines.** Their local branches, worktrees, index state,
   stashes and uncommitted files are invisible here. Only what they pushed to `origin` is visible.
   Everything below about "unpushed work" is a statement about node `a` alone.
2. **The remote is clean, and that proves less than it looks.** `origin` carries 13 `branch/*` refs;
   12 are ancestors of `main` and 1 (`kit-adversarial-review-15ed31`) is not. So from the remote's
   point of view there is exactly one outstanding branch. F1 and F2 are the demonstration that this
   is not evidence: a node that never pushes is silent by construction, and this node is silent about
   21 commits.
3. **Absolute worktree paths in records cannot be attributed to a node.** `AGENTS.md` §2 pins the
   primary tree as `C:/projects/coding-governance` for **all four** nodes, so
   `C:/projects/coding-governance/.claude/worktrees/<x>` in a record identifies no machine. 15 such
   citations exist across 14 records, naming 5 distinct worktrees, **none of which resolves here** —
   `build-readme-governance-18d6ea`, `dtieredtribunal-build-spec-7218ea`,
   `playbook-mode-unattended-kit-550410`, `unattended-ascanned-throttle-18a592`,
   `upstream-asks-dScrubbedConduit`. I am **not** reporting these as drift: every one is a
   "measured on" provenance stamp in a review or build record, which is old-but-true, not stale.
4. **Reflog-only work is out of scope.** A branch deleted without merging leaves no ref; four
   `RUN.md` `branch-ref:` values resolve nowhere (`adeclaredbound-unattended`,
   `governance-template-convergence-91c2c6`, `full-gate-bar-performance-828ae8`,
   `unattended-sessions-kit-extend-2e4038`). Three are `LANDED` runs, which is the expected
   post-merge state. One — `aMeteredTurnstile`, `ABORTED` — I could not verify beyond confirming its
   build folder and 6 ids are on `main` as CLOSED.

---

## F8 — the gates that police this cannot see any of it

The commissioning question asked me to interrogate the DEAD PROBE and the two EMPTY-BY-DECLARATION
rows. Both dead rows have the same cause, and it is worse than "not measured yet".

```python
# tools/drift-audit/drift_report.py:1380
self.ledger_dir = root / self.memory_root / "project" / "in-flight"
```

```
$ ls memory/project/in-flight
ls: cannot access 'memory/project/in-flight': No such file or directory
$ ls memory/project/
corpus-path-unresolved.txt  curation-debt.txt  id-orphan-waiver.txt  legacy-files.txt
method-carriers.txt  readme-contract.txt  testsuite-count-waivers.txt  trace-waiver.txt
unarmed-branches.txt
```

`signal_ledger` (:377) and `signal_dangling_pointers` (:586) both read that path and nothing else.
It has never existed here, and per `AGENTS.md` it never will: *"There is no authored session ledger:
the sharded per-node one retired at playbook v2.4 / memory-tree kit 1.8 and its shards sit frozen
under `memory/archive/`."*

The report prints:

```
ledger_rows_contradicting_git        0   0   empty by declaration — nothing to measure here yet
dangling_pointers_in_own_ledger     -1   0   DEAD PROBE — signal cannot move, ignore its value
```

**"yet" is false.** These are not awaiting a population; the population was deliberately retired.
2 of 11 Tier-0 signals are permanently dark in this repo. To the kit's credit, both say so out loud
rather than reporting a reassuring zero — that half of the liveness discipline works.

The part that does not: the two questions those signals ask are, verbatim from
`tools/drift-audit/README.md:106,110`, *"does an in-flight row claim 'not merged' about a landed
sha?"* and *"do this node's own rows point at worktrees that exist?"* — which are precisely the two
questions the owner is asking. A live population that answers both exists and no signal reads it:
**27 `memory/builds/*/RUN.md` records**, each with `phase`, `witness`, `branch-ref`. Hand-auditing it
took one loop and found F4 (a LANDING record whose work is on `main`) and the four unresolvable
`branch-ref` values. There is also no signal anywhere in the kit for an unpushed branch, an
abandoned merge, or a dirty worktree:

```
$ grep -rn "MERGE_HEAD" tools/          # zero hits
$ grep -n "def signal_" tools/drift-audit/drift_report.py   # 8 signals, none about branch state
```

`tools/check-wiring.sh --session` — the SessionStart hook that `AGENTS.md` §3 says "flags the
contested state" — checks `core.hooksPath`, EOL pinning and the skill junction. It does not look at
`git worktree list`, at MERGE_HEAD, or at whether a branch has commits the remote has not seen.

So: **a fully green Tier-0 drift report is compatible with 21 commits of finished work living on one
disk and a worktree frozen mid-merge for three days.** That is the reported symptom, mechanically
explained.

---

## F9 — worktree/branch bookkeeping (tidy-up, listed for completeness)

```
$ git worktree list
C:/projects/coding-governance                                 14e21399 [main]
.../adopter-prefix-a1b2c3           109628c2 [branch/adopter-prefix-a1b2c3]        0 ahead, 19 behind, clean
.../gate-cost-doorway               96ae4f14 [branch/gate-cost-doorway]            0 ahead, 17 behind, clean
.../kit-adversarial-review-15ed31   66c4891c [branch/kit-adversarial-review-15ed31] 16 ahead
.../lexicon-argv-guard              961c6e4c [branch/lexicon-argv-guard]           0 ahead, 25 behind, clean
.../unattended-check-plan-27c557    f8993d62 [branch/acollapsedscan-followups]     15 ahead, 204 behind, 71 staged
.../worktrees-branches-cleanup-df15b1 1255d5d1 [branch/paired-lexer-followup-9c31a2] 6 ahead, 1 untracked
```

- Three worktrees hold branches that are 0-ahead of `main` and clean — they are empty shells, and no
  build record names any of them.
- **Two worktree directory names do not match the branch they hold**
  (`unattended-check-plan-27c557` → `branch/acollapsedscan-followups`;
  `worktrees-branches-cleanup-df15b1` → `branch/paired-lexer-followup-9c31a2`). Both are exactly the
  worktrees holding the lost work, so the naming is not a coincidence — they were re-used.
- `branch/reconcile-branches-worktrees-04f712` exists as a local ref with no worktree and 0 commits
  ahead.
- The primary tree is on `main` and clean, so §3's branch rule holds.

---

## What I did NOT find, stated so it counts as a reading

- The generated index is not hand-edited. Verified by re-render, not by eye.
- No `LANDED` record names a commit that is not on `main`. 24 witnesses tested.
- No build in `memory/LIVE.md` is non-terminal while git shows its units finished on `main`. All 16
  non-terminal builds have a base ancestor and no landed-but-unstamped units that I could detect.
- The `aScouredKit` acceptance ledger covers `-11` and `-13` and calls itself "the two Tier-2 units";
  the generated region grades `-30/-31/-32` as Tier 1, so that scope is correct. I did not grade the
  ledger's evidence quality — that is another lens's subject.
- The 19 new backlog rows are internally consistent with the units: rows exist for `-10`, `-16`
  through `-29`, `-33`, `-34` and NOT for `-30/-31/-32`, which is right, and is exactly what makes
  F6's prose wrong.

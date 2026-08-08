# Review 2 — adversarial pass over the wave-2 sub-specs (V2, V5, V6, V7, V8)

**Scope:** the five remaining sub-specs, reviewed before any code.
**Method:** five independent reviewers, one per spec, then a skeptic per finding. **42 findings.**
Six blockers, and every one was produced by RUNNING something — a probe on this box, a patched copy
of a module, a scratch cache directory. Three of the five specs would have shipped a gate that is
permanently red on a correct tree, and one would have shipped a deletion that leaves a corrupted
directory behind.

| # | Sev | Spec | Finding |
|---|---|---|---|
| N1 | blocker | V5 | `py -3` cannot be a candidate: the probe quotes it as one word, and every consumer uses `"$PY"` |
| N2 | blocker | V5 | a shared `tools/lib/` breaks every ADOPTER — kits are copy-installed as standalone directories |
| N3 | blocker | V5 | the ban's real population contains sites the migration list omits, so the landing commit reds its own tree |
| N4 | blocker | V6 | "no readable manifest = mid-first-build" is false on a REBUILD |
| N5 | blocker | V6 | `shutil.rmtree(ignore_errors=True)` on this platform leaves a PARTIAL directory |
| N6 | blocker | V8 | AC2's green arm passes on the un-widened code, so it cannot detect the widening at all |
| N7 | high | V5 | a SOURCED resolver cannot halt a caller that runs `set -u` without `set -e` |
| N8 | high | V5 | `RECALL_PY` is a PUBLISHED adopter override the migration would silently drop |
| N9 | high | V6 | the three "X survives" arms are all satisfied by the budget pass not running at all |
| N10 | high | V6 | greedy eviction and "nothing is deleted when the budget cannot be met" are incompatible unless the plan is computed first |
| N11 | high | V8 | S8's justification is factually WRONG — resolution never touches the filesystem |
| N12 | high | V8 | the `.claude/worktrees/` arms are vacuous on the fixture the module actually has |
| N13 | high | V7 | the CRLF repair set is 43 files, not "the files a gate renders and byte-compares" |
| N14 | high | V7 | both JS gates BYPASS git for explicit paths, so the widening arms may test nothing |
| N15 | high | V7 | widening to untracked collides with the landing boundary, which deliberately permits untracked files |
| N16 | high | V7 | the parity floor has an undefined empty case, reachable in the exact scenario it exists for |
| N17 | high | V2 | the batching premise is FALSE for the manifest-check harness — its callers short-circuit |

## N1, N2, N3, N7, N8 — V5 was three separate red merge bars

**`py -3` is unusable as specified.** Measured on this box: `"py -3" -c "import sys"` exits 127 —
the probe quotes the candidate as one word — while `py -3 -c "import sys"` works. Word-splitting the
probe does not rescue it, because every consumer uses `"$PY"` as one word, and `run-gates.sh` does
`case "${argv[0]}" in python|python3) argv[0]=$PYBIN ;; esac`, which with a two-word value exits 127
on all ten python legs. On the exact Windows box this row was opened from, WindowsApps supplies
alias stubs for BOTH `python` and `python3`, so the candidate list would exhaust and the resolver
would return its named failure: **the unit fails the one machine it exists to fix.**
Resolved: `py` ALONE is a single word and resolves to Python 3.14 here, measured. The candidate list
is `python3`, `python`, `py`.

**A shared `tools/lib/` breaks every adopter.** `WIRE-INTO-PROJECT.md` copy-installs each kit as a
standalone directory — `cp -r <gov>/tools/memory-tree <project>/memory-tree` — so a `../lib/` source
resolves to nothing in an adopting repo. This is the same constraint that made the drift-audit kit
copy the conf parser rather than share it. Resolved: the canonical file is sourced only by scripts
that are NOT copy-installed, and each copy-installed kit carries the same function INLINE with a
parity gate asserting the copies are identical — copy plus gate, the convention this repo already
has.

**The ban's population is bigger than the migration list.** Measured: `check-memory-hygiene.sh` has
the idiom at three sites, `pytest-parallel-guardrails.test.sh` at another, and
`skills/session-kickoff/manifest-check.test.sh:316` — a live merge-bar leg — carries it verbatim
while sitting OUTSIDE the spec's `tools/**` scope. Meanwhile `.githooks/` contains zero python
references, so half the declared population is empty. Resolved: the population is measured, and the
migration list is derived from the same scan that the ban uses.

**A sourced resolver cannot halt its caller.** Six of the seven target scripts run `set -u` and not
`set -e`, so a `return 1` from a sourced function is ignored. Resolved: the resolver ECHOES the
launcher and returns non-zero, and every call site is `PY=$(resolve_python) || { …; exit 2; }` —
command substitution propagates the status, which is the shape those scripts already use.

**`RECALL_PY` is a published contract**, named in the kit README, in `WIRE-INTO-PROJECT.md` and in
the script's own usage line. Resolved: the recall site passes it as a first candidate rather than
having it silently replaced by `GOV_PYTHON`.

## N4, N5, N9, N10 — V6 would have deleted the wrong things, or nothing, or half

**The mid-build protection was reasoned from a first build only.** `_write_set` unlinks and recreates
both databases on a REBUILD while the previous `manifest.json` stays on disk, so "no readable
manifest" does not characterise the mid-build state at all. Resolved: eviction skips any directory
whose databases are newer than its manifest, and the never-evict rule is stated over that.

**The deletion primitive itself is unsafe here.** Measured on win32: `shutil.rmtree(ignore_errors=True)`
over a directory holding an OPEN sqlite database removes `manifest.json`, KEEPS `records.db`, and
leaves the directory in place. That is strictly worse than not deleting — a cache with no manifest
is exactly the shape the never-evict rule protects, so the tree accumulates undeletable rubble.
Resolved: delete the MANIFEST LAST, verify the directory is gone, and on failure report rather than
retry.

**Three of the six arms are satisfied by the pass not running.** A selftest-shaped cache totals about
57 KB, so any plausible budget leaves the pass inert and "the current cache survives" is trivially
true. Resolved: the arms set a budget BELOW the fixture's own size so the pass must run, and each
survival arm is paired with a demonstration that something else WAS evicted in the same run.

**Greedy eviction contradicts the leave-it-alone rule.** Resolved: the pass computes the whole plan
before deleting anything, and a plan that cannot reach the budget is reported and not executed.

## N6, N11, N12 — V8's arms could not see the change, and its rationale was wrong

AC2's green arm — "a cited directory that resolves is silent" — passes on today's un-widened code,
because an unharvested token is also silent. Measured against the current module. Resolved: the green
arm is paired with a red one over the SAME fixture, so only the widening can produce both.

S8 justified the new conf key with node-dependence: the worktree path "exists on THIS machine and not
on another". That is false about the code. Check 15's resolution never touches the filesystem — it is
membership in `git ls-files` plus a prefix scan over the same index — so `.claude/worktrees/<name>`
classifies as dead identically on every node. The exclusion is still right, for a better reason: a
checkout location is not repo CONTENT, and no resolution rule can express that, because the question
is about meaning rather than existence. Resolved: the key stays, the justification is corrected.

The `.claude/worktrees/` arms were also vacuous on the module's own fixture, whose only tracked
top-level directory is `memory/` — so `.claude/` is not a real root there and the token never becomes
a candidate. Resolved: the fixture gains a tracked `.claude/` path.

## N13, N14, N15, N16 — V7's three items each had a wider blast radius than stated

The `eol=lf` set is 43 files, not the handful the data model describes; both JavaScript gates bypass
git entirely when handed explicit paths, so the arms as drafted would exercise the wrong code path;
widening to untracked collides with `push-main.sh`'s deliberate `-uno`, which permits untracked files
at the landing boundary; and the parity floor's derivation returns exactly one commit here — which is
the flatten itself — with no defined behaviour when it returns none.

## N17 — V2's batching premise is false for the second harness

`fail()` does not abort, but its CALLERS short-circuit: `BLOCK_OK` skips four whole checks once any
check-2 branch fires, and check 3 is a three-way `if/elif` chain. One scratch tree cannot trip many
manifest-check branches. Resolved: that harness gets several small fixtures rather than one batched
tree, and the reason is recorded so the next person does not "optimise" them back together.

## Verification

Every finding went to a skeptic told to refute it. The blockers above all survived; several were
strengthened with a sharper measurement than the reviewer had.

## Disposition

Folded into rev-2 of all five sub-specs before any code.

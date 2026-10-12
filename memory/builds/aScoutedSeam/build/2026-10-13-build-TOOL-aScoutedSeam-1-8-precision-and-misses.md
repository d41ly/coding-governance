**Serves:** research TOOL-aScoutedSeam-1

# Where M1c's wrong MUSTs come from, and why six cases stay missed — an offline reading

Read 2026-10-13 on node `a`, at the owner's request, from the committed results of the benchmark
(`2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`) and the M1c trial (`-1-7-m1c-trial.md`).
No agent ran. The instrument is `-1-8-precision.py`. It reads the committed corpus, results and blind
judge verdicts, and the frozen case trees `bench.py trees` builds, which are machine-local.

```bash
P=memory/builds/aScoutedSeam/build/2026-10-13-build-TOOL-aScoutedSeam-1-8-precision.py
python $P precision m1b m1b@medium m1cA@medium m1cB@medium
python $P misses
python $P expansion
```

## The wrong MUSTs

A wrong MUST is one the blind judge said would mislead the build. The judge's reasons sort into
classes:

| arm | MUSTs | wrong | edits, wiring, regeneration | tests, gates | other |
|---|---|---|---|---|---|
| M1b at `extra` | 97 | 0 | 0 | 0 | 0 |
| M1b at `medium` | 166 | 9 | 8 | 1 | 0 |
| M1c run A | 213 | 19 | 15 | 4 | 0 |
| M1c run B | 210 | 21 | 14 | 6 | 1 |

Every wrong MUST but one names work the build must DO, not code it must reuse. None names code that
does not exist: of M1c's 423 MUSTs, the path and the symbol's lead token are present at the case's
point for all but 7, and none of those 7 is a wrong one. An existence check therefore removes no wrong
MUST.

**What a deterministic demotion removes.** Demoting a MUST to SHOULD keeps the case solved, because
SHOULD counts. It costs only the binding, because the spec join reads MUST lines alone.

| rule | M1c A: wrong removed, ground truth demoted | M1c B | M1b `medium` |
|---|---|---|---|
| existence at the point | 0 of 19, 0 | 0 of 21, 0 | 0 of 9, 0 |
| edit-shaped `how` or symbol | 15, 7 | 14, 6 | 6, 6 |
| MUST cap 5 per case, in the scout's order | 15, 1 | 15, 3 | 5, 2 |
| MUST cap 3 per case | 18, 7 | 21, 6 | 6, 8 |
| MUST only where both runs bind it | 12, 5 | 14, 3 | n/a |

The scout ranks well and binds too much. M1c emits about seven MUSTs per case, and the wrong ones sit
at the tail. A cap of five removes three quarters of them and demotes one to three ground-truth
bindings. Running twice and intersecting does worse at twice the cost.

**Effort.** Paired over the 19 cases M1b answered at both efforts, `extra` bound 97 MUSTs with 1
wrong, and `medium` bound 114 with 8 wrong. The free scout M1 is imprecise at both, 52 of 186 and
49 of 180, paired over 25 cases. At `medium` the checklist keeps its recall and loses its MUST
discipline. The sketch step adds to that, because it asks for the plumbing and the plumbing lands in
the seam list.

## The six misses

Six positives were missed by both M1c runs, by the judge. For each, the table gives where the
ground truth sits relative to what the scout did cite:

| case | ground truth | in the house index | the scout cited its file | found by another arm |
|---|---|---|---|---|
| inCMS DSL design data | `imageField` | no | no | none |
| gov pooled wall | `arm_wall` in `run-gates.sh` | no | yes, both runs | D1 at `extra`, M1 at `medium` |
| gov warded terminal | `PHASES_TERMINAL` in `unattended.sh` | no | yes, both runs | none |
| gov keyed decisions | `parse_dossier` in `map_lib.py` | no | yes, both runs | D1 at both efforts |
| gov conf parser | `load_conf` | yes | a file holding another copy | M1b, by the judge |
| gov batched launcher | `resolve_python` | yes | a file holding a copy | none |

- **Three of the six were in a file the scout had already cited, and two more had a copy in one.**
  It read the file for one symbol and never listed the rest. Expanding every cited file into its
  definitions reaches the ground truth in five of the six in run A and four in run B, where the
  launcher's copy sat only in a cited file's directory. It also reaches one of the two further cases
  that only the path matcher counts as missed. The cost is 181 names per case at the median and 954
  at most. Expanding the cited files' directories costs 1,500
  at the median and is not affordable.
- **The map's symbol inventory alone would miss two of them.** It holds functions, classes and JS
  exports, but not module constants, so `PHASES_TERMINAL` and `DEFAULT_DECISION_ID_RE` are absent
  from it. An expansion has to list constants too.
- **Two were in the index and never searched.** The index named `resolve_python` and `load_conf`.
  The sketch never listed "launch an interpreter from a shell test", and the census bound the copies
  of `load_conf` rather than the canonical one.
- **One is a sibling's choice the census never reached.** `imageField` is how sibling sections declare
  an image prop. The census ran over kinds, not over the one prop the request adds.
- **D1 found two of them by reading code, not a plan.** It reviewed the landed diff and recognised a
  missing wall watcher and a retyped id grammar. A pre-spec arm never sees code, only its sketch.

## What this decides

1. The wrong MUSTs are an output-contract problem, not a search problem: the scout found real code
   and mislabelled build work as reuse. The harness owns the return contract, so the fixes go there:
   the `edits` bucket, a MUST definition naming what the build would otherwise write, and a
   deterministic cap of five MUSTs in the merge.
2. The misses are a granularity problem: the unit of search was a 6 to 15 line sketch, and the
   ground truth sat one level below it. The shape that reaches it lists what a builder would TYPE,
   the definitions in every file the scout cites, and the canonical owner of every literal and
   launcher the code would use.
3. Nothing here was re-run through an agent. Each rule above is simulated on the recorded order, and
   the expansion figures bound reach, not discovery: an agent shown the name can still pass over it.

## Limits

The judge's verdicts are taken as given, and it was one model reading once per case. The edit-shaped
pattern is a heuristic over prose. The case trees are machine-local and rebuilt by `bench.py trees`.

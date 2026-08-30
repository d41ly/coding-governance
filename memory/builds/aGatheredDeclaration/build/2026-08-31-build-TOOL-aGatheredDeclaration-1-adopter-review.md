# The three-corpus gate review — inCMS, NicoCares, coding-governance

**Serves:** research TOOL-aGatheredDeclaration-1

Observed 2026-08-31 on node `a`, against each repository's working tree as checked out at
`C:/projects/incms/main`, `C:/projects/nicocares/main` and this worktree. Every count below was
derived by loading the three manifests and counting, never read from prose.

## The one-paragraph finding

Three repositories run the same governance and have three different gate declarations. inCMS has the
richest schema and the only runner with a real argument surface, and it has already independently
invented two of the three things this build was asked for — an explicit `optIn` key and a
ceiling-enforcement OFF switch. It also demonstrates the cost of JSON: its manifest carries a 1.4 KB
`_doc` STRING and a whole `ceiling_over_policy` OBJECT whose only purpose is to hold the prose
justification for a number, because JSON cannot hold a comment. NicoCares runs this repo's own kit
over a manifest that declares none of the schema the kit understands, so it pays the full bar every
time. That is the flexibility problem, stated as three data points rather than as an opinion.

## S1 — inCMS

**Runner:** `scripts/gate.sh`, 863 lines, with a PowerShell twin `scripts/gate.ps1` ratcheted for
byte-identical machine surfaces by `services/api/tests/test_gate_runners_parity.py`. It is a thin
iterator over `scripts/gate-legs.json` plus `scripts/gate-scope.json`, and hardcodes no leg command.

**Argument surface**, from the header at `scripts/gate.sh:10` and the parse loop at `:26-39`:

| flag | what it does |
|---|---|
| *(none)* | the full authoritative run |
| `--since <sha>` | scoped mode — legs selected by their `scope` against the changed paths |
| `--list` | prints every leg name, one per line, and exits (`:288-291`) |
| `--explain-paths <file>` | prints the tier each path classifies to |
| `--docs-only <file>` | exit 0 iff every path is the `skip` tier; fail-closed on an absent file |
| `--legs <file>` | redirect at another manifest. Deliberately a FLAG and never an env var (`:32-34`) |
| `--backend-only`, `--editor` | selection subsets |

`--list` is the only sharding primitive present, and it names legs rather than running one. **No
adopter runner in this fleet can run a single leg by name.**

**Manifest:** a JSON OBJECT, not an array — 66 rows under `legs`, plus five top-level keys.

| leg key | rows | values observed |
|---|---|---|
| `name`, `argv`, `cwd`, `phase`, `scope`, `tool`, `ceiling` | 66 each | required on every row |
| `optIn` | 26 | all `true` |
| `full_only` | 4 | all `true` |
| `pg_autowire` | 1 | `true` |

`cwd` is repo-root-relative and takes two values: `services/api` on 10 rows, `.` on 56.
`phase` is the LANE: `fast` 5, `heavy` 57, `serial` 4. `scope` is the path-selector: `always` 54,
`python` 11, `memory` 1. `tool` is the binary probed for usability before the run — `bash` 40,
`pnpm` 12, `uv` 10, `node` 4 — and an unusable tool produces a FAIL row rather than a silent skip.

**Lane semantics**, from `scripts/gate.sh:566-679`: `fast` runs SEQUENTIALLY and streams, and a
single `fast` failure SKIP-marks every `heavy` and `serial` leg without launching them. `heavy` runs
through a bounded slot pool whose width is `INCMS_GATE_HEAVY_JOBS`, default 4, glob-validated as a
STRING before it ever reaches an arithmetic context (`:45-52`) — the comment states why, and it is a
command-execution sink in the script that produces the merge verdict. `serial` runs after `heavy`.

**Ceilings.** Declaration is MANDATORY and enforcement is OPTIONAL, and that split is the single
most useful thing in this review. `_ceiling()` at `:134-138` REFUSES the whole run, naming the
offending leg, when a row declares no positive integer `ceiling`. Enforcement is then governed by
`INCMS_GATE_UNBOUNDED`, default `0`, validated to `0|1` and rejected otherwise (`:71-72`). Set to 1
it prints a five-line banner before any leg runs and records the fact in the GATE SUMMARY and in
`gate-last-summary.txt` — announced twice and durably, so a green earned unbounded cannot be
mistaken for one earned bounded. The header's own justification, at `:53-70`, is the argument this
build was handed:

> a ceiling KILLS a leg before it can answer, so a run with ceilings off produces STRICTLY MORE
> evidence than one where a ceiling fired, not less

and it names the measurement that forced it: `playbook-check` at 369 s alone and over 1864 s under
load, 5x, against a bound already set at 5x its measured cost.

**The killed-leg evidence, which is the prompt's claim made specific.** The manifest's
`ceiling_over_policy` object records, in prose, why each ceiling exceeds the 1800 s
`ceiling_policy` default. One entry:

> `unattended-check`: KILLED at 2041 s in the width-4 push bar 20260829T2306 against a 2040 s
> ceiling — by one second.

Its own note continues that the leg's `HEAVY_JOBS=1` column said 664 s, so that column understated
the real cost by at least 3.07x, and that the replacement ceiling is 2x a LOWER BOUND rather than a
measurement, because a killed leg's true cost is unknown. A bar was lost to a one-second margin on a
number nobody could have derived correctly.

**JSON is already failing them, visibly.** Two of the five top-level keys exist only to carry prose
that JSON has no other place for: `_doc`, a single 1.4 KB string documenting the phase order, the
`scope` vocabulary, the `tool` probe and the reason `unattended-check-test` is held; and
`ceiling_over_policy`, an object mapping a leg name to a paragraph. In a commented format both are
comments beside the rows they explain.

**Opt-in has a COVERAGE ledger, and gov has nothing like it.** `scripts/gate.sh:735-786` writes
`<git-dir>/gate-optin-lastrun.tsv` and prints, after every run, an `optIn legs NOT exercised by this
run` block naming each held leg and when it last ran. The header states the defect it answers
(`:737`): an optIn leg that never runs and an optIn leg that passes are otherwise indistinguishable.
That is `TOOL-aGradedDoorway-9` in this repo's backlog, already solved next door.

**Why a leg is held is recorded as COST, measured.** `unattended-check-test` is optIn because it
costs 3188 s of a 63-minute full bar — 248 arms each staging a break and re-running the whole
checker at 13-23 s each.

## S2 — NicoCares

**Runner:** this repository's own kit, `scripts/run-gates/run-gates.sh`, at
`KIT_RUN_GATES_VERSION=1.3` (`scripts/run-gates/run-gates.sh:19`) — current with gov. The install
prefix is `scripts`, not `tools`, which is what `.githooks/pre-push:39` probes for.

**Manifest:** `scripts/gate-legs.json`, a JSON array of 40 rows declaring exactly four keys:
`name` and `argv` and `chunk` on all 40, and `impure` on 4. Chunks are `kits` 18, `package` 13,
`records` 5, `core` 4.

**What it therefore cannot express, and what that costs:**

- **No `subject`.** Every leg defaults to `repo`, so `GATE_SELFTESTS` selects nothing and the
  held-leg mechanism the kit ships is inert in this tree.
- **No `guard`.** No leg is scoped to what it reads, so a records-only commit runs all 40 legs. In
  gov, 50 of 86 legs carry a guard and a records-only commit runs a fraction of the bar.
- **No `ceiling`.** All 40 legs run unbounded. The runner counts them and prints
  `N of M legs declare no ceiling and run unbounded this run` on stderr, then carries on — so
  NicoCares already runs the bar in the state this build is about to make the DEFAULT everywhere.
  That is a useful data point rather than an objection: nobody has reported a wedge there.

**NicoCares is the upgrade tool's first customer**, and the cheapest one: it runs the right runner
over the wrong manifest, so its migration is data rather than a runner swap.

## S3 — coding-governance

`tools/gate-legs.json`, a JSON array of 86 rows: `name`, `argv`, `chunk`, `subject` and `ceiling` on
all 86, `guard` on 50, `impure` on 1. Chunks are `selftests` 43, `declarations` 20, `product` 9,
`wiring` 9, `records` 3, `e2e` 2. Subjects are `repo` 46 and `kit` 40. Ceilings run 300 s to 16040 s
and sum to 147450 s.

Concurrency is NOT in this file. It is in `tools/run-gates/gate-profiles.txt`, a tab-separated table
of `name / min cores / min RAM MB / knobs`, whose three rows all declare `timeout=0` — so the
profile-level bound is already off everywhere and the per-leg `ceiling` is the only one that fires.
The table's comments carry the argument for every threshold in it, which is why the migration must
preserve comments and why JSON was refused.

Opt-in is not a key here either. It is the `subject = "kit"` convention plus `GATE_SELFTESTS=1`, and
`GATE_FULL=1` deliberately does NOT unlock it. The distinction is correct and well-documented; it is
simply not the thing the owner asked to be able to read and adjust in one file.

`tools/unattended/run-unattended-gates.sh` is a second entry point onto gate-shaped work — the seven
`*.test.sh` legs the unattended kit removed from the bar on the 2026-08-23 owner ruling. It is the
concrete instance of the prompt's "THE SINGLE GATE ENTRY POINT" ask.

## S4 — the schema union

Every key observed in any of the three manifests, with the repo that proves it load-bearing and the
ruling for the canonical declaration.

| key | gov | inCMS | nico | ruling |
|---|---|---|---|---|
| `name` | yes | yes | yes | **required** |
| `argv` | yes | yes | yes | **required** |
| `ceiling` | yes | yes | no | **required to DECLARE, opt-in to ENFORCE** — inCMS's split, adopted whole |
| `cwd` | no | yes | no | **adopt**, defaulting to `.`; 10 inCMS legs need it and gov legs would stop wrapping themselves in `cd` |
| `chunk` | yes | no | yes | **adopt** as the reporting group. inCMS's `_doc` does the same job in prose |
| `subject` | yes | no | no | **fold into `opt_in`** — see below |
| `optIn` / opt-in | convention | yes, 26 rows | no | **adopt as an explicit `opt_in` key.** This is the prompt's ask, and inCMS proves the shape |
| `guard` | yes, 50 rows | `scope` | no | **adopt `guard`** (path list). inCMS's `scope` is a fixed enum and does not travel |
| `phase` | no | yes | no | **adopt as `lane`** — this is where declared parallelism lives |
| `impure` | yes, 1 row | no | yes, 4 rows | **adopt.** Two of three repos declare it and it gates reuse |
| `tool` | no | yes | no | **adopt.** A probe that turns a missing binary into a FAIL row rather than a silent pass is the green-by-absence class |
| `full_only` | no | yes, 4 rows | no | **UNVERIFIED whether gov needs it.** Retain as optional; it is 4 rows in one repo and costs one key |
| `pg_autowire`, `pg`, `scoped` | no | yes | no | **DROP.** Product-specific Docker/pytest provisioning. An adopter needing it declares a leg whose argv does it |
| `_doc`, `ceiling_policy`, `ceiling_over_policy` | no | yes | no | **DROP as KEYS, keep as COMMENTS.** All three exist only because JSON cannot hold prose. This is the whole argument for TOML |

**On folding `subject` into `opt_in`.** `subject = "kit"` and `optIn: true` are the same statement —
*do not run this unless asked* — reached by two different arguments. gov's is "a kit's self-tests
have no job in a tree that does not edit the kit"; inCMS's is "this leg costs 3188 s". One key with a
REASON beside it expresses both, and a format with comments is what makes the reason storable. This
is a proposal, not a ruling: it changes what `GATE_SELFTESTS` means and belongs to
`TOOL-aGatheredDeclaration-2`'s §8.

## S5 — the harvest list

| mechanism | observed at | takes it |
|---|---|---|
| declaration REQUIRED, enforcement OPTIONAL, announced twice and durably | `scripts/gate.sh:53-72`, `:134-138` | `TOOL-aGatheredDeclaration-4` |
| the `optIn` coverage ledger and its post-run "NOT exercised" block | `scripts/gate.sh:735-786` | `TOOL-aGatheredDeclaration-3` |
| `--list` as the minimum sharding primitive | `scripts/gate.sh:288-291` | `TOOL-aGatheredDeclaration-3` |
| `--legs` as a FLAG, never an env var, so a hook cannot be redirected | `scripts/gate.sh:32-34` | `TOOL-aGatheredDeclaration-3` |
| the `need2` guard — a two-token flag that validates BEFORE it shifts | `scripts/gate.sh:25` | `TOOL-aGatheredDeclaration-3` |
| lanes with a short-circuit: a `fast` failure never launches the heavy pool | `scripts/gate.sh:566-679` | `TOOL-aGatheredDeclaration-2` |
| a concurrency knob glob-validated as a STRING before any arithmetic context | `scripts/gate.sh:45-52` | `TOOL-aGatheredDeclaration-2` |
| `tool`, probed for usability, an unusable one FAILing rather than skipping | `scripts/gate.sh:149` and `_doc` | `TOOL-aGatheredDeclaration-2` |
| `cwd` per leg | manifest, 66 rows | `TOOL-aGatheredDeclaration-2` |
| per-leg ceiling justification stored beside the number | `ceiling_over_policy` | `TOOL-aGatheredDeclaration-2`, as comments |

## What this review did NOT check

- Whether inCMS's `gate.ps1` twin has the same argument surface. Only the bash runner was read, and
  the parity ratchet's scope was taken from the header comment rather than from the test.
- Whether NicoCares' 40 legs would each survive a guard. Assigning guards is that repo's build.
- Whether `full_only` has a gov analogue. Marked `UNVERIFIED` in the union table rather than ruled.
- inCMS's `gate-scope.json` tier vocabulary beyond the three `scope` values the manifest uses.

# The owner's prompt — the gate bar becomes one declared file and one entry point

**Serves:** research TOOL-aGatheredDeclaration-1

Handed to `/unattended --prompt` on 2026-08-31, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is reproduced VERBATIM below. The bytes travel rather
than a reference: the build folder is the authorization, so it may not point at a file that can be
edited after the run starts.

## Verbatim

> **Several adjustments to the gate bar tooling need to be reviewed, tested, and built per the protocol**:
>
> * This repo should carry a single adoptable gate runner tool (used by push-main, declared to llm
>   sessions, and whatever other tooling is there) that is used to declare per-adopter legs and their
>   format. That should be THE SINGLE GATE ENTRY POINT used to execute gate legs. Gate declaration
>   should happen through a single owner-readable and adjustable file - adopters declare their
>   additional legs themselves. Sharding (calling any individual leg or its check) should be fully
>   supported by the tool. The tool should expose and require a clear manifest from the gates it runs
>   - data structure, how many checks are there, how to execute each individual check, ceilings,
>   concurrency. There has to be a tool to upgrade any adopter repo and its tests to this tool. Opt-in
>   (those that only run on demand) and non opt-in gates should be declared there. Gate parallelism
>   should be declared through that file. The runner should automatically decide how to efficiently
>   execute the gates (profiles) based on available system resources.
> * gate execution ceilings both in-repo and what ships to the adopters - need to be owner opt-in
>   (config variable). Gate ceilings have cost several killed gates, reds, and re-runs today. By
>   default, that gate ceiling enforcement should be off, opt-in by the owner.
> * push main beacon that enqueues parallel pushes should also ship disabled, enabled through a config
>   variable by the owner.
> * Both inCMS gates and NicoCares gates should be reviewed for their current state to make this tool
>   more flexible and efficient.
> * Bring any relevant backlog rows into this build.
> * Review this build requirements and come up with unattended recommendations to properly architect
>   this build aiming for flexibility and performance.

## The clarification turn, and its answers

One `AskUserQuestion` was issued before this folder was written — the only owner turn this run gets.
Two gaps, both material enough that a wrong assumption would rebuild the wrong thing.

**Q1 — what "a single owner-readable and adjustable file" means.** The declaration is split three
ways today: `tools/gate-legs.json` holds the legs and cannot carry a comment,
`tools/run-gates/gate-profiles.txt` holds the concurrency knobs and its argued comments are
load-bearing, and opt-in is not a key at all but the `subject = "kit"` convention.

> **Answered: one commented TOML file.** `gate-legs.toml` replaces BOTH, carrying `[[leg]]` rows with
> an explicit `opt_in`, `ceiling`, `lane` and `guard`, plus the profile table. This is the only
> option that literally satisfies "gate parallelism should be declared through that file". It costs a
> migration of roughly six in-repo readers.

**Q2 — how far into the adopters this build reaches.** inCMS runs its own 863-line `scripts/gate.sh`
over 66 legs; NicoCares runs this repo's `run-gates` kit at 1.3 over a 40-leg manifest declaring no
subject, no ceiling and no guard.

> **Answered: review both, build the upgrader, touch neither.** This build records what each declares
> today, harvests inCMS's proven ideas into the canonical schema, and ships the upgrade tool with its
> tests. Migrating an adopter is that repo's own build, on its own bar. Nothing lands outside
> coding-governance.

## What orientation already established, before any spec

Recorded here because it is what the roster was derived from, and a roster whose derivation lives
only in a transcript is a roster nobody can re-check.

- `tools/run-gates/` is ALREADY an adoptable kit with `kit.toml`, `adopt-run-gates.sh`, a version
  constant and five gate legs of its own. The first ask is largely satisfied; what is missing is the
  single declaration file and the argument surface.
- `run-gates.sh` parses NO arguments. Every knob is an environment variable, and there is no way to
  run one leg. Sharding, in the sense the prompt means, does not exist. A different sense DOES exist
  and must not be confused with it: a suite script may accept `--shard i/n` and be declared as two
  manifest rows, asserted by `run-gates.gov.test.sh:347-403`.
- All 86 in-repo legs declare a `ceiling`, and every `gate-profiles.txt` row declares `timeout=0`, so
  the profile-level bound is already off and the per-leg one is what fires.
- The turnstile ships ENABLED — `GATE_TURNSTILE:-1` at `run-gates.sh:420` — and `GATE_TURNSTILE=0`
  is the only way off.
- `tools/unattended/run-unattended-gates.sh` is a SECOND entry point onto gate-shaped work, which is
  what the "single gate entry point" ask names.
- The `.unattended.conf` `GATE_BOUND="3600"` is a THIRD ceiling, on the whole bar rather than a leg,
  and it is in scope for the opt-in ruling by the same argument.

## Relevant backlog rows, brought in by the prompt's own instruction

Harvested from `memory/backlog/TOOL.md` — 51 OPEN rows name the gate bar; these are the ones a unit
of this build subsumes or must not break.

| row | why it is here |
|---|---|
| `TOOL-aBoundedCeiling-7` | `.githooks/pre-push` HARDCODES `tools/gate-legs.json` and the fingerprint path while the install prefix is configurable — the readers-move unit owns it |
| `TOOL-aBoundedCeiling-12` | the turnstile reaps a dead HOLDER and never a dead WAITER; one killed bar wedged a landing 6858 s |
| `TOOL-aReapedTicket-4` | `ts_try_reap` reaps with a bare `rm -rf` where the design prescribed a rename |
| `TOOL-aGradedDoorway-8` | the shard-join predicate ships only in the gov-only canary, so an adopter that shards is ungraded |
| `TOOL-aGradedDoorway-9` | a run that HOLDS a leg and one that PASSES it are indistinguishable from outside |
| `TOOL-aScannedThrottle-7` | `run-gates evidence` reds under load on a 5-second bound |
| `TOOL-aSiftedFork-6` | the canary's clamp arms use `timeout` unguarded and blame the clamp on a host without it |
| `TOOL-aBoundedVerdict-26` | `run-gates.sh | tail -N` returns tail's status, discarding the verdict |
| `TOOL-aDeclaredCeiling-1` | make a ceiling a DECLARED pin rather than a shell constant — the same shape this build generalises |
| `TOOL-aMeteredTurnstile-3` | the timing cache evicts on the RUN, never on the manifest, so a renamed leg keeps its row forever |
| `TOOL-aCollapsedScan-5` | written when no leg declared a ceiling; all 86 now do, so it needs re-reading against the tree rather than acting on |
| `TOOL-dSpentCeiling-8` | the full bar is nondeterministic under its own concurrency on at least two legs |

## The recall terms used

`python tools/memory-recall/query.py "why are gate ceilings enforced by default and why is the
run-gates turnstile beacon enabled by default" --terms "ceiling timeout leg manifest turnstile beacon
queue run-gates profile concurrency GATE_FULL selftest sharding adopter"` — 40 hits. The load-bearing
ones are `memory/builds/aBoundedCeiling/spec/2026-08-27-spec-TOOL-aBoundedCeiling-1.md`, which states
why `PROF_TIMEOUT` must stay zero, and `memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md`,
which designed the beacon this build is about to default off.

`python tools/codebase-map/reuse_lookup.py "run a single named gate leg on demand and declare per-leg
concurrency and ceilings"` returned the `run-gates` affordance seam `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE`
as its only on-topic hit, which is the seam the declaration reader extends.

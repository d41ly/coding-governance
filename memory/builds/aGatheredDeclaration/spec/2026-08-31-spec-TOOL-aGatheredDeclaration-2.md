# TOOL-aGatheredDeclaration-2 — `gate-legs.toml`, the one declaration the bar is read from

**Status:** OPEN · rev-1 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md](../build/2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md) | research | TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-6 |

<!-- /gen:spec-records -->

## 1. Goal

Replace `tools/gate-legs.json` and `tools/run-gates/gate-profiles.txt` with a single commented
`gate-legs.toml` that declares the legs, their opt-in status, their ceilings, their guards, their
lanes AND the hardware profile table, so an owner adjusts the bar by editing one file whose every
number keeps its argument beside it.

## 2. Scope (IN)

- **S1** — the TOML schema: a `[bar]` table of defaults, `[[profile]]` rows, `[[lane]]` rows and
  `[[leg]]` rows, with the field set ruled by `TOOL-aGatheredDeclaration-1` §S4.
- **S2** — the reader in `tools/run-gates/run-gates.sh`: one python invocation via `tomllib`,
  emitting the same tab-separated table the current JSON path emits, so the dispatch loop below it
  does not change.
- **S3** — DUAL-FORMAT LOADING for one release. `gate-legs.toml` wins where it exists;
  `gate-legs.json` is read otherwise, with a deprecation line on stderr naming the upgrader. An
  adopter's bar must not break on the commit that ships this.
- **S4** — the migration of this repo: 86 legs and the three profile rows become
  `tools/gate-legs.toml`, with every `gate-profiles.txt` comment carried across verbatim and every
  ceiling that exceeds `[bar].default_ceiling` gaining a comment stating why.
- **S5** — `cwd` per leg, defaulting to `.`, resolved against the repo root.
- **S6** — `lane` per leg over the `[[lane]]` rows, each lane declaring `concurrency` and whether a
  failure in it `short_circuit`s the lanes after it.
- **S7** — `tool` per leg, optional: a binary probed for usability before the run, an unusable one
  producing a FAIL row naming the leg rather than a silent pass.
- **S8** — the canary arms that assert the reader, the dual-format branch, and the schema refusals.

## 3. Non-goals (OUT)

- The argument surface. `TOOL-aGatheredDeclaration-3`.
- Ceiling enforcement policy. This unit only DECLARES ceilings; whether they fire is
  `TOOL-aGatheredDeclaration-4`.
- The turnstile default. `TOOL-aGatheredDeclaration-5`.
- Moving the other readers — govkit's emitter, `.githooks/pre-push`, `drift_signals.py`,
  `map_extractors.py`. `TOOL-aGatheredDeclaration-6`. This unit's dual-format loading is what lets
  those move in a later commit instead of the same one.
- The upgrader. `TOOL-aGatheredDeclaration-7`.
- Deleting `gate-legs.json` from this repo. It goes when unit 6 has moved every reader; deleting it
  here would red four legs in the commit that introduces the format.

## 4. Design

### Data model

```toml
# gate-legs.toml — the merge bar, DECLARED. One file: legs, lanes, profiles, defaults.
# Every number here may carry the argument for itself on the line above it. That is the whole
# reason this is not JSON: the file it replaces held a 1.4 KB `_doc` STRING and a
# `ceiling_over_policy` OBJECT in an adopter tree, both of them comments with nowhere to go.

[bar]
# OWNER OPT-IN, default false. A ceiling KILLS a leg before it can answer, so enforcement OFF
# produces strictly more evidence than a ceiling that fired. See TOOL-aGatheredDeclaration-4.
enforce_ceilings = false
# The bound a leg inherits when it declares none. Declaration stays REQUIRED.
default_ceiling = 1800
# OWNER OPT-IN, default false. See TOOL-aGatheredDeclaration-5.
turnstile = false

[[profile]]                  # most-capable first; the first row satisfying BOTH thresholds wins
name = "capable"
min_cores = 8
min_ram_mb = 24000           # a RAM class, not an exact figure: each heavy leg builds its own
                             # mktemp -d scratch repo, so width 8 means eight of them resident
width = 8

[[lane]]
name = "fast"
concurrency = 1              # sequential and streamed
short_circuit = true         # a failure here SKIP-marks every later lane without launching it

[[lane]]
name = "heavy"
concurrency = "profile"      # take the selected profile's width

[[leg]]
name = "kickoff-manifest ratchet"
argv = ["bash", "skills/session-kickoff/manifest-check.sh"]
chunk = "records"
lane = "heavy"
ceiling = 640
opt_in = false
guard = []
```

Optional keys and their defaults: `cwd = "."`, `lane = "heavy"`, `opt_in = false`, `guard = []`,
`impure = false`, `tool` absent, `ceiling` absent meaning `[bar].default_ceiling`.

### Migration

`gate-legs.json`'s 86 rows map field-for-field: `name`, `argv`, `chunk` and `guard` unchanged;
`ceiling` unchanged; `subject = "kit"` becomes `opt_in = true` with a comment naming the reason
(`a kit's self-tests have no job in a tree that does not edit the kit`); `subject = "repo"` becomes
`opt_in = false`. `impure`'s one row keeps its prose as the comment above the leg and becomes
`impure = true`. `gate-profiles.txt`'s three rows become three `[[profile]]` tables and every
comment paragraph in that file lands above the row it argues for.

**`timeout=` does not travel.** All three profile rows declare `timeout=0`, so the profile-level
bound is already off everywhere; carrying a dead knob across a format change is how a knob nobody
can explain survives. Its absence is recorded here and in the file's own header.

### Rollout

The dual-format branch (S3) means one commit ships the reader and the migrated file together and
nothing outside this kit has to move. Rollback is deleting `gate-legs.toml`: the loader falls to the
JSON that is still tracked, which is why S3 exists and why unit 6 is a separate landing.

### Files touched (estimate)

`tools/gate-legs.toml` (new) · `tools/run-gates/run-gates.sh` (loader) ·
`tools/run-gates/run-gates.test.sh` (canary arms) · `tools/run-gates/README.md` ·
`tools/run-gates/kit.toml` (`[[lf_pin]]` for the new file) · `.gitattributes`.

### Alternatives rejected

**Keep JSON and add keys.** Offered to the owner on 2026-08-31 and declined. It cannot satisfy
"gate parallelism should be declared through that file" without either a second file or a `_doc`
string, and the adopter that tried the `_doc` string is the evidence against it.

**YAML.** No stdlib parser, so it needs a dependency in a kit whose whole point is that it travels
with nothing. Refused on that alone.

## 5. Production-readiness checklist

- security — the loader parses declared data and executes `argv`. `tomllib` is stdlib and does not
  execute. The one new sink is `cwd`, resolved against the repo root and refused if it escapes it.
- perf / scale — one python invocation, as today. No regression; the lane short-circuit is a
  reduction.
- a11y — N/A, no user interface.
- i18n — N/A.
- error / empty / loading states — an unparseable file, an unknown lane, a leg naming no profile-
  resolvable concurrency, and an empty leg list each REFUSE with exit 2 naming the offending row.
- observability — the runner already prints its profile line; it gains the source file it read and
  the format it read it as.
- risks — the dual-format branch is the rollback. The real hazard is a partial migration where a
  reader outside this kit still reads JSON, which is why unit 6 exists and why the JSON stays.
- testing + left-shift gates — S8's canary arms, each with its failing case observed RED first.
- migration / rollback — above.
- user docs — `tools/run-gates/README.md` and the charter's merge-bar section.

## 6. Acceptance criteria

- **AC1** — When `tools/gate-legs.toml` exists, `bash tools/run-gates/run-gates.sh` reads it and
  reports the same leg count and the same manifest order as the JSON it replaces, asserted in
  `tools/run-gates/run-gates.test.sh` by comparing both loaders' emitted tables.
- **AC2** — When `gate-legs.toml` is absent and `gate-legs.json` present, the runner runs the JSON
  and prints one deprecation line naming `adopt-run-gates.sh --upgrade` on stderr, asserted by a
  scratch-repo arm in `tools/run-gates/run-gates.test.sh`.
- **AC3** — When a `[[leg]]` declares a `lane` no `[[lane]]` row names, the runner exits 2 naming
  the leg and the lane, observed RED before the arm is written.
- **AC4** — When a leg declares `cwd` resolving outside the repo root, the runner exits 2 naming it;
  a `cwd` inside it runs the leg from there, asserted with a leg whose argv is `pwd`.
- **AC5** — When a leg declares a `tool` that is not executable, its row is `GATE FAIL <leg>` naming
  the missing tool, never `GATE skip`, asserted in `tools/run-gates/run-gates.test.sh`.
- **AC6** — When a lane declaring `short_circuit = true` has a failing leg, no leg in a later lane
  is launched and each is reported with the skip verb naming the short circuit, asserted by
  timing-independent means: the later legs' argv writes a file, and the file is absent.
- **AC7** — When `tools/gate-legs.toml` is compared against `tools/gate-legs.json`, every leg name,
  argv and guard matches and every `subject = "kit"` row carries `opt_in = true`, asserted by a
  parity arm that reads both files.
- **AC8** — `bash tools/run-gates/run-gates.sh` is GREEN on this tree after the migration, with the
  leg count unchanged at its manifest value.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `run-gates adopter e2e` ·
`run-gates wiring` · `profile-bar selftest` · `kit version markers` · the memory hygiene gate. New
legs: none — S8's arms join the existing canary rather than adding a leg, because a new leg on a bar
this build is trying to make cheaper needs its own argument.

## 8. Open questions

- **F1 — does `opt_in` REPLACE `subject`, or sit beside it?** Replacing it is one key with a reason
  beside it and is what the prompt asked for; keeping both is two answers to one question, which is
  a named class in this tree. The cost of replacing is that `GATE_SELFTESTS` changes meaning: it
  becomes "run the opt-in legs" rather than "run the kit self-tests", and an adopter holding a leg
  for COST rather than for kit-ness is then covered by the same switch, which inCMS's 26 rows show
  is the real population. Recommendation: REPLACE, and keep `GATE_SELFTESTS` as an accepted alias
  for the new `GATE_OPTIN` so no adopter's hook breaks.
  RESOLVED (agent, 2026-08-31, delegated): REPLACE, with `GATE_SELFTESTS` kept as an alias. The
  mandate delegates this build's own scope, the option satisfies more stated criteria than keeping
  both, and it trips none of M3's three vetoes — no new dependency, no new public surface beyond a
  key this build was asked to add, and no security or write surface widened.
- **F2 — where does `[bar].enforce_ceilings` live if an adopter wants it per-machine rather than
  per-repo?** A tracked declaration is per-repo by construction, and a slow node may want ceilings
  off where a fast one wants them on. Options: an env override reading the declared value as its
  default, or a second untracked file. Recommendation: the env override, which is one line and is
  how every other knob in this runner already works.
  RESOLVED (agent, 2026-08-31, delegated): the env override, `GATE_CEILINGS`, whose absence takes
  the declared value. Fewest open questions, and it reuses the seam the runner already has.

## 9. Revision log

- rev-1 · 2026-08-31 · initial draft, from `TOOL-aGatheredDeclaration-1`'s schema union.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "run a single named gate leg on demand and declare
per-leg concurrency and ceilings"` returned the `run-gates` affordance seam
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` — `tools/run-gates/run-gates.sh:77-84`, where `LEGS_FILE` is
DERIVED from the kit's own location with `GATE_LEGS` outranking it. **That is the seam this unit
extends**: the derivation gains a `.toml` probe ahead of the `.json` one and nothing else about it
moves, so `GATE_LEGS` keeps outranking both and both harnesses keep their nested-run seam.

`python tools/memory-recall/query.py "why are gate ceilings enforced by default and why is the
run-gates turnstile beacon enabled by default" --terms "ceiling timeout leg manifest turnstile
beacon queue run-gates profile concurrency GATE_FULL selftest sharding adopter"` — 40 hits. The
binding record is `memory/builds/aBoundedCeiling/spec/2026-08-27-spec-TOOL-aBoundedCeiling-1.md`,
which states why `PROF_TIMEOUT` must stay zero: `run-gates.sh` derives the turnstile's holder TTL
from it, so a non-zero profile timeout silently reshapes the turnstile. **Verified against source at
`tools/run-gates/run-gates.sh:430-441` — the derivation is still there**, which is why S4 drops the
knob rather than porting it.

The second reuse seam is OUTSIDE this repo and is recorded because M5 asks for the seam, not for a
gov seam: `C:/projects/incms/main/scripts/gate.sh` already implements lanes, `cwd`, `tool` probing
and an opt-in coverage ledger over a manifest of the same shape. The mechanisms are harvested per
`TOOL-aGatheredDeclaration-1` §S5; the runner is not ported.

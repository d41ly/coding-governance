# TOOL-aGatheredDeclaration-2 — `gate-legs.toml`, the one declaration the bar is read from

**Status:** OPEN · rev-2 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md](../build/2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md) | research | TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-6 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 |

<!-- /gen:spec-records -->

## 1. Goal

Replace `tools/gate-legs.json` and `tools/run-gates/gate-profiles.txt` with a single commented
`gate-legs.toml` that declares the legs, their opt-in status, their ceilings, their guards, their
lanes AND the hardware profile table, so an owner adjusts the bar by editing one file whose every
number keeps its argument beside it. **The migration is behaviour-neutral by construction**: the same
legs, held in the same set, dispatched by the same loop.

## 2. Scope (IN)

- **S1** — the TOML schema: a `[bar]` table of defaults, `[[profile]]` rows, `[[lane]]` rows and
  `[[leg]]` rows. The field set is unit 1 §S4's ruling and includes `full_only`, which rev-1 cited
  that ruling and then omitted.
- **S2** — the reader in `tools/run-gates/run-gates.sh`: one python invocation via `tomllib`,
  emitting the RS/US wire format the JSON path already emits, byte-for-byte and field-for-field.
- **S3** — DUAL-FORMAT LOADING, permanent rather than transitional. `gate-legs.toml` wins where it
  exists AND the resolved interpreter can import `tomllib`; the legacy PAIR — `gate-legs.json`
  together with `gate-profiles.txt` — is read otherwise, with a line on stderr naming which and why.
- **S4** — the INTERPRETER FLOOR: `tomllib` is CPython 3.11+, and the loader states the floor by name
  rather than failing with an import traceback.
- **S5** — the migration of this repo: 86 legs and the three profile rows become
  `tools/gate-legs.toml`, with every `gate-profiles.txt` comment carried across verbatim and every
  ceiling exceeding `[bar].default_ceiling` gaining a comment stating why.
- **S6** — `cwd` per leg, defaulting to `.`, resolved against the repo root.
- **S7** — the ENV SPELLINGS: `GATE_OPTIN` is the new name for the hold override and
  `GATE_SELFTESTS` is its alias. Both write the same run-record byte and satisfy the same pre-push
  predicate.
- **S8** — the STAMP/HOOK PAIR: `run-gates.sh:1430` stamps `manifest_blob` from `$LEGS_FILE` while
  `.githooks/pre-push:203` hashes a hardcoded `tools/gate-legs.json`. This unit keeps the pair
  agreeing across the window before unit 6 moves the hook.
- **S9** — the canary arms: the reader, the dual-format branch, the floor refusal, the schema
  refusals, the empty-guard round trip, the boolean marshalling, and the repointed pinned-knob arm.

## 3. Non-goals (OUT)

- **Lanes and the tool probe.** `TOOL-aGatheredDeclaration-8`. rev-1 carried them here and asserted
  "the dispatch loop below it does not change", which is false: lanes need phase ordering, a per-lane
  width, a skip-marking pass and a per-lane order hint, against a runner with ONE pool at one width
  (`run-gates.sh:372`, `:1272`) fed by ONE global longest-first hint (`:846-870`). The `[[lane]]`
  rows are DECLARED here and every gov leg lands in one lane, so this migration stays neutral.
- The argument surface. `TOOL-aGatheredDeclaration-3`.
- Ceiling enforcement policy. This unit only DECLARES ceilings; whether they fire is
  `TOOL-aGatheredDeclaration-4`.
- The turnstile default. `TOOL-aGatheredDeclaration-5`.
- Moving the other readers — govkit's emitter, `.githooks/pre-push`'s pathspecs, `drift_signals.py`,
  `map_extractors.py`, `check-testsuite-counts.sh`. `TOOL-aGatheredDeclaration-6`.
- The upgrader. `TOOL-aGatheredDeclaration-7`.
- Deleting `gate-legs.json` or `gate-profiles.txt`. Both go in unit 6; deleting either here reds
  legs in the commit that introduces the format.

## 4. Design

### Data model

```toml
# gate-legs.toml — the merge bar, DECLARED. One file: legs, lanes, profiles, defaults.
# Needs CPython 3.11+ to be read at all; below that the runner reads the legacy pair and says so.

[bar]
enforce_ceilings = false     # OWNER OPT-IN. See TOOL-aGatheredDeclaration-4.
default_ceiling = 1800       # what a leg declaring none inherits. Declaration stays REQUIRED.
turnstile = false            # OWNER OPT-IN. See TOOL-aGatheredDeclaration-5.
turnstile_ttl = 1800         # the holder TTL. Was derived from the profile row's `timeout=`.

[[profile]]                  # most-capable first; the first row satisfying BOTH thresholds wins
name = "capable"
min_cores = 8
min_ram_mb = 24000           # a RAM class, not an exact figure: each heavy leg builds its own
                             # mktemp -d scratch repo, so width 8 means eight of them resident
width = 8

[[lane]]                     # DECLARED here, IMPLEMENTED in TOOL-aGatheredDeclaration-8.
name = "heavy"               # every gov leg is in this lane, so the migration changes no behaviour
concurrency = "profile"

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
`impure = false`, `full_only = false`, `tool` absent, `ceiling` absent meaning
`[bar].default_ceiling`.

**Every `[bar]` boolean is marshalled to the bytes `0` or `1` at the loader boundary.** The two
turnstile guards are string tests — `run-gates.sh:420` and `:726` are `[ "${GATE_TURNSTILE:-1}" != 0 ]`
— so a TOML `false` substituted verbatim yields a comparison of the STRING `false` against `0`, which
is true, and ships the mechanism ENABLED. `TOOL-aGatheredDeclaration-5` reuses this marshalling
rather than restating it, and so does unit 4's `GATE_CEILINGS` join.

### The wire format is RS/US and is an INTERFACE

`run-gates.sh:840-901` emits the fields `name`, `guard`, `argv`, `impure`, `chunk`, `subject`,
`ceiling` separated by the RECORD SEPARATOR byte, with `argv` internally joined by the UNIT
SEPARATOR byte, and reads them back at `:905-910` with `IFS` set to that same record separator. Its
own comment states the reason: both bytes are non-whitespace, so an EMPTY guard field survives
`read` where a tab would collapse. **36 of 86 legs carry no guard** — 42%, the common case, not an
edge. The TOML reader reproduces the separators, the field ORDER and the append-only rule
byte-for-byte; a field inserted before an existing one is parsed AS that one by any reader not moved
in the same commit.

### Migration

`gate-legs.json`'s 86 rows map field-for-field: `name`, `argv`, `chunk`, `guard` and `ceiling`
unchanged. `gate-profiles.txt`'s three rows become three `[[profile]]` tables and every comment
paragraph lands above the row it argues for.

**The hold is a UNION, and mapping `subject` alone silently reverts a recorded ruling.** The shipped
predicate at `run-gates.sh:947` holds a leg when its subject is `kit` OR its chunk is `selftests`,
and the comment at `:934-946` records the 2026-08-26 owner ruling behind it. Re-derived at this base:
40 legs carry `subject = kit`, 43 carry `chunk = selftests`, the union is 46, and exactly SIX carry
`subject = repo` with `chunk = selftests` — `branch-guard self-test`, `pre-push self-test`,
`push-main self-test`, `recall floor arms`, `run-gates canary`, `run-gates gov canary`. So the
mapping is **`opt_in = true` iff subject is `kit` OR chunk is `selftests`, 46 legs**, and the TOML
carries `run-gates.sh:934-947`'s reason as its own comment.

**`timeout=` is dropped, and the argument is its CONSUMERS rather than its current value.** rev-1
argued the removal from all three rows reading `timeout=0`, which is a reading and not a consumer
census. `PROF_TIMEOUT` has two live readers and each gets a named replacement:

| consumer | what it does | replacement |
|---|---|---|
| `run-gates.sh:434` | derives the turnstile holder TTL as three times it | `[bar].turnstile_ttl`, declared directly |
| `run-gates.sh:1104` | the per-leg bound fallback | `[bar].default_ceiling` |

`run-gates.sh:431`'s own comment names setting `timeout=` as the PRESCRIBED fix for a leg reaped
mid-run, in preference to raising the constant — which is why the TTL becomes a declared key rather
than disappearing. `TOOL-aGatheredDeclaration-4` §3 must point at `[bar].turnstile_ttl` rather than
at a knob this unit removes.

### The stamp and the hook must not split

`run-gates.sh:1430` stamps `manifest_blob` as the hash of `$LEGS_FILE`; S2 makes `LEGS_FILE` resolve
to the TOML. `.githooks/pre-push:203` compares that against the hash of a hardcoded
`tools/gate-legs.json`. They can never match, and predicate 7 then forces a FULL bar on every
default-branch push until unit 6 lands — a permanent 26-minute floor, which is the cost this build
exists to remove. It is reachable during the window: `ondemand` is its own counter (`:69`, `:1174`)
rather than `skips`, so an ordinary held-selftests push still satisfies the stamp's preconditions.

**The stamp keeps writing the JSON blob until unit 6 moves the hook**, and says so in a comment
naming unit 6. That is one line and it needs no cross-unit ordering guarantee.

### Rollout

One commit ships the reader and the migrated file. Rollback is deleting `gate-legs.toml`: the loader
falls to the legacy pair, which is still tracked.

### Files touched (estimate)

`tools/gate-legs.toml` (new) · `tools/run-gates/run-gates.sh` (loader, marshalling, stamp) ·
`tools/run-gates/run-gates.test.sh` (arms, and the pinned-knob arm repointed) ·
`tools/run-gates/README.md` · `tools/run-gates/kit.toml` (`[[lf_pin]]`) · `.gitattributes`.

### Alternatives rejected

**Keep JSON and add keys.** Offered to the owner on 2026-08-31 and declined. It cannot satisfy
"gate parallelism should be declared through that file" without a second file or a `_doc` string,
and the adopter that tried the `_doc` string is the evidence against it.

**YAML.** No stdlib parser, so it needs a dependency in a kit whose premise is travelling with
nothing.

**Ship a TOML subset parser to dodge the 3.11 floor.** A parser is the category where "just a few
lines" is always wrong, and it would put the declaration's meaning in two implementations that must
agree. S3's permanent dual-format path is the answer instead.

## 5. Production-readiness checklist

- security — the loader parses declared data and executes `argv`. `tomllib` is stdlib and does not
  execute. The one new sink is `cwd`, resolved against the repo root and refused if it escapes it.
- perf / scale — one python invocation, as today. The stamp fix above is what keeps this unit from
  making the bar strictly slower.
- a11y, i18n — N/A.
- error / empty / loading states — an unparseable file, a leg carrying an UNKNOWN KEY, a leg naming
  an undeclared lane, an empty leg list, and a `cwd` escaping the root each REFUSE with exit 2 naming
  the offending row. A missing `tomllib` is its own named refusal per S4 and falls back per S3, never
  a bare import error. The unknown-key refusal is stated here because rev-1 dropped it while unit 7
  S7 kept the same refusal for foreign manifests.
- observability — the profile line gains the source file, the format read, and the interpreter
  version when the floor decided the format.
- risks — a partial migration where an outside reader still reads JSON; unit 6 owns it and the
  legacy pair stays tracked meanwhile.
- testing + left-shift gates — S9's arms, each with its failing case observed RED first.
- migration / rollback — above.
- user docs — `tools/run-gates/README.md` and the charter's merge-bar section.

## 6. Acceptance criteria

- **AC1** — When `tools/gate-legs.toml` exists, `bash tools/run-gates/run-gates.sh` reports the same
  leg count and the same manifest order as the legacy pair, asserted in
  `tools/run-gates/run-gates.test.sh` by comparing both loaders' emitted tables.
- **AC2** — When the TOML is absent, the runner runs the legacy PAIR and prints one line on stderr
  naming both files and the reason, asserted by a scratch-repo arm in
  `tools/run-gates/run-gates.test.sh`.
- **AC3** — When the resolved python cannot import `tomllib`, the runner names the interpreter and
  its version, states the 3.11 floor, and reads the legacy pair — it does NOT exit 2 with zero legs
  run, asserted in `tools/run-gates/run-gates.test.sh` against a stub interpreter. Observed RED first.
- **AC4** — When a leg declares NO guard, its parsed tuple matches field-by-field, asserted by
  feeding `tools/run-gates/run-gates.sh` a leg with every optional field empty and comparing each
  field rather than the line.
- **AC5** — When the held SET is computed from `tools/gate-legs.toml`'s `opt_in` values, it equals
  the set `tools/gate-legs.json`'s union predicate selects — 46 names — asserted by a parity arm in
  `tools/run-gates/run-gates.test.sh` that resolves BOTH rather than comparing a key.
- **AC6** — When a scratch run dispatches, the set of legs the loop actually holds equals the
  declaration's `opt_in = true` set, asserted in `tools/run-gates/run-gates.test.sh` against the
  resolved behaviour rather than the declared key.
- **AC7** — When a `[bar]` boolean is read, it emerges from the loader as exactly the byte `0` or
  `1`, byte-compared for every `[bar]` boolean in `tools/run-gates/run-gates.test.sh`, so a `false`
  can never reach a string comparison as a truthy word. Observed RED first.
- **AC8** — When a leg declares `cwd` resolving outside the repo root, the runner exits 2 naming it;
  a `cwd` inside it runs the leg from there, asserted with a leg whose argv is `pwd`.
- **AC9** — When a leg carries a key the schema does not declare, or names a lane no `[[lane]]` row
  declares, `bash tools/run-gates/run-gates.sh` exits 2 naming the leg and the key. Observed RED
  first.
- **AC10** — When a bar runs and a default-branch push follows in one scratch repo, the push is NOT
  forced to a full bar, asserted in `.githooks/pre-push.test.sh` — the stamp and the hook hash the
  same file across this window.
- **AC11** — When a run sets `GATE_OPTIN` and another sets `GATE_SELFTESTS`, both write the same
  run-record byte and both satisfy pre-push predicate 8, asserted in `.githooks/pre-push.test.sh`
  parameterised over both spellings.
- **AC12** — When `tools/run-gates/run-gates.test.sh`'s pinned-knob arm runs, it grades the
  `[[profile]]` rows in the TOML and FAILS on an unpinned knob key; it may no longer pass by finding
  no `gate-profiles.txt`. Observed RED first.
- **AC13** — `bash tools/run-gates/run-gates.sh` is GREEN on this tree after the migration, with the
  leg count unchanged at its manifest value.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `run-gates adopter e2e` ·
`run-gates wiring` · `profile-bar selftest` · `pre-push hook selftest` · `kit version markers` ·
`testsuite counts` · the memory hygiene gate. New legs: none.

## 8. Open questions

- **F1 — does `opt_in` REPLACE `subject`, or sit beside it?** Replacing it is one key with a reason
  beside it and is what the prompt asked for; keeping both is two answers to one question.
  RESOLVED (agent, 2026-08-31, delegated): REPLACE, with `GATE_SELFTESTS` kept as an alias.
  **AMENDED at rev-2, because rev-1's costing was wrong**: it claimed the alias "breaks no adopter's
  hook" and it breaks gov's own. `.githooks/pre-push:213` gates predicate 8 on `GATE_SELFTESTS`
  against a value read at `:151`, and `run-gates.sh:1435` writes that stamp field from the same
  variable. A push under the new spelling sets neither, so the stamp under-records what the run
  covered and predicate 8 stops firing for exactly the case `TOOL-dUnstalledConvoy-27` wrote it for.
  S7 and AC11 now carry it. The replacement still stands; what changed is that it costs a scope item
  rather than nothing.
- **F2 — where does `[bar].enforce_ceilings` live if an adopter wants it per-machine?**
  RESOLVED (agent, 2026-08-31, delegated): the env override, `GATE_CEILINGS`, whose absence takes the
  declared value. Its boolean join goes through the marshalling rule in §4.
- **F3 — is `full_only` implemented or merely carried?** Unit 1 §S4 rules "retain as optional" on 4
  inCMS rows and gov has none, so implementing selection semantics for it here would be a feature no
  corpus exercises. Recommendation: DECLARE it in the schema, validate it as a boolean, and let it
  select nothing until a corpus needs it — which is what "retain as optional" means and is what unit
  7's mapping needs to have one source to follow.
  RESOLVED (agent, 2026-08-31, delegated): declared and validated, selection unimplemented and said
  so in the schema comment. Fewest open questions, and it closes unit 7's AC2/AC4 contradiction.

## 9. Revision log

- rev-1 · 2026-08-31 · initial draft, from `TOOL-aGatheredDeclaration-1`'s schema union.
- rev-2 · 2026-08-31 · folded round-1 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md`), findings F3, F4,
  F6, F7, F8, F9, F10, F11, F12, F13, F22, F23, F24, F25. Lanes and the tool probe left for
  `TOOL-aGatheredDeclaration-8` (F9). The hold mapping became the union it actually is (F3). The wire
  format was named correctly as RS/US (F8). The `timeout=` removal was re-argued from consumers
  rather than readings, and `[bar].turnstile_ttl` was added (F12). Boolean marshalling was added
  after F19 showed a TOML `false` reaching a string comparison as a truthy word.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "run a single named gate leg on demand and declare
per-leg concurrency and ceilings"` returned the `run-gates` affordance seam
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` — `tools/run-gates/run-gates.sh:77-84`, where `LEGS_FILE` is
DERIVED from the kit's own location with `GATE_LEGS` outranking it. **That is the seam this unit
extends**: the derivation gains a `.toml` probe ahead of the `.json` one, gated on the interpreter
floor, and nothing else about it moves.

`python tools/memory-recall/query.py "why are gate ceilings enforced by default and why is the
run-gates turnstile beacon enabled by default" --terms "ceiling timeout leg manifest turnstile
beacon queue run-gates profile concurrency GATE_FULL selftest sharding adopter"` — 40 hits. The
binding record is `memory/builds/aBoundedCeiling/spec/2026-08-27-spec-TOOL-aBoundedCeiling-1.md`,
which states why `PROF_TIMEOUT` must stay zero. **Verified against source at `run-gates.sh:430-441`
and `:1104`** — and rev-2 records what rev-1's verification missed: the derivation being live is
exactly why the knob cannot simply be dropped, which is F12.

The second seam is OUTSIDE this repo: `C:/projects/incms/main/scripts/gate.sh` already implements
`cwd` over a manifest of the same shape. Its lanes and tool probe move to
`TOOL-aGatheredDeclaration-8` with the rest of the dispatcher work.

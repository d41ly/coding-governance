# TOOL-aGatheredDeclaration-2 — `gate-legs.toml`, the one declaration the bar is read from

**Status:** INPROGRESS · rev-5 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGatheredDeclaration-2-acceptance-ledger.md](../build/2026-08-31-build-TOOL-aGatheredDeclaration-2-acceptance-ledger.md) | journal | — |
| [2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md](../build/2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md) | research | TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-6 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |

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
- **S8** — the STAMP/HOOK PAIR, and it is TWO predicates rather than one. `.githooks/pre-push:195`
  (predicate 6) diffs `tools/gate-legs.json` to catch a push that moves the scoping rules;
  `:203` (predicate 7) hashes the same literal path. rev-2 froze the stamp on the JSON blob,
  which keeps predicate 7 agreeing and leaves predicate 6 BLIND to the file that now scopes the
  bar — the unsafe direction, since a push touching only the TOML would not be forced. Predicate
  6's pathspec gains `tools/gate-legs.toml`, which is additive and waits on nothing.
- **S8b** — predicate 7 stays pinned to the JSON blob until unit 6, and that is a DECLARED
  EXEMPTION with a compensating check: S8's widened predicate 6 catches the same class from the
  diff side for the whole window. Charter §7 requires an exemption to name its compensating
  check, and rev-2 took the exemption without naming one.
- **S9** — the canary arms: the reader, the dual-format branch, the floor refusal, the schema
  refusals, the empty-guard round trip, the boolean marshalling, and the repointed pinned-knob arm.
- **S12** — the COMMENTS are graded, on gov's own migration. S5 carries `gate-profiles.txt`'s
  argued paragraphs across, and after `TOOL-aGatheredDeclaration-6` S7 deletes that file the
  evidence is gone — so the arm belongs to THIS unit, while both files exist. AC16.
- **S13** — the manifest path is derived in ONE place. §10's reuse audit says the derivation is one
  seam and both canaries re-derive it themselves; the loader exports the resolved path and the
  suites read it rather than rebuilding it, or §10's claim is false in the same commit that makes
  it.
- **S10** — REQUIRED versus DEFAULTED, ruled once and here. A TOML declaring NO `[[profile]]` row
  exits 2 naming the file, because there is no defensible default width for unknown hardware.
  `[bar]`'s keys are DEFAULTED, every one of them: `enforce_ceilings` and `turnstile` default
  `false` — that is what *opt-in, default off* means and a refusal on their absence would
  contradict it — and `default_ceiling` and `turnstile_ttl` take the kit's shipped numbers. So a
  `[bar]` may be absent entirely and an adopter's hand-written manifest runs. rev-4 refused a
  partial `[bar]`, which made `TOOL-aGatheredDeclaration-4` AC11 and
  `TOOL-aGatheredDeclaration-5`'s absent-key row unsatisfiable: both require exactly that fixture
  to RUN and report the default taken.
- **S10b** — what holds the two write paths instead is COVERAGE, not refusal: unit 6 AC14 and
  unit 7 AC8c both grade the emitted `[bar]` against the same declared key set, so an emitter
  that drops a key reds at the unit that wrote it rather than at a runner that could have
  defaulted it. The
  second half is what holds both write paths with one check: a loader that reds on a partial
  `[bar]` cannot be satisfied by a partial emitter, so `TOOL-aGatheredDeclaration-6` S1(d) and
  `TOOL-aGatheredDeclaration-7` S10 are held by a refusal rather than by two criteria agreeing
  with each other. A converter that drops
  a table is then caught by the loader on its first run rather than by a wide pool on a small
  machine, and the same refusal covers a hand-written adopter manifest.
- **S11** — `short_circuit` is part of the `[[lane]]` SCHEMA declared here, validated as a boolean
  and defaulting to `false`, both graded by AC17. `TOOL-aGatheredDeclaration-8` READS it. rev-2 dropped it from this
  schema when the example lane set shrank to one row, leaving unit 8 reading a key no unit
  declared.

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
short_circuit = false        # a failing lane does NOT skip the lanes after it. Default.

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
`[bar].default_ceiling`. **`full_only` is validated and SELECTS NOTHING** — §8 F3's resolution,
carried here because the schema is where a reader looks for it, and the shipped file states it
in a comment on the key. **`full_only` is validated and SELECTS NOTHING** — §8 F3's resolution,
carried here because the schema is where a reader looks for it, and the shipped file states it
in a comment on the key.

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
`read` where a tab would collapse. **38 of 86 legs carry no effective guard** — 36 omit the key and 2 declare an
empty list, so 44%: the common case, not an edge. rev-2 said 36, which counted only the omitted
key while the paragraph's own criterion is an empty FIELD on the wire, and both spellings
produce one. The TOML reader reproduces the separators, the field ORDER and the append-only rule
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
| `run-gates.sh:434` | derives the turnstile holder TTL as three times it | `[bar].turnstile_ttl`, declared directly, graded by AC14 |
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

**There are TWO writers of `manifest_blob`, not one, and each is ruled separately.**
`run-gates.sh:1430` writes the `gate-full-green` stamp that predicate 7 reads, and it hardcodes
`tools/gate-legs.json` until unit 6 moves the hook, with a comment naming unit 6.
`run-gates.sh:1021` writes the RUN-RECORD header and keeps `$LEGS_FILE`, so `manifest` and
`manifest_blob` in that record stay consistent with each other and with the file the run actually
read. rev-4 said "the stamp" and cited `:1430` alone; §10 had verified the `LEGS_FILE`
derivation and never the writers.

### Rollout

One commit ships the reader and the migrated file. Rollback is deleting `gate-legs.toml`: the loader
falls to the legacy pair, which is still tracked.

### Files touched (estimate)

`tools/gate-legs.toml` (new) · `tools/run-gates/run-gates.sh` (loader, marshalling, stamp) ·
`tools/run-gates/run-gates.test.sh` (arms, and the pinned-knob arm repointed) ·
`tools/run-gates/README.md` · `tools/run-gates/kit.toml` (`[[lf_pin]]`) · `.gitattributes` ·
`.githooks/pre-push` and `.githooks/pre-push.test.sh` — S8 edits predicate 6's pathspec and three
criteria are asserted in that suite, and rev-3 budgeted neither.

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
- **AC10** — When a bar runs in a scratch repo that DECLARES a `gate-legs.toml` and a
  default-branch push follows, the push is NOT forced to a full bar, asserted in
  `.githooks/pre-push.test.sh`. **The declared TOML is load-bearing in the fixture**: rev-2's
  wording greened on a JSON-only scratch repo, where the defect it grades cannot occur.
- **AC10b** — When a push's diff touches ONLY `tools/gate-legs.toml`, it IS forced to a full bar,
  asserted in `.githooks/pre-push.test.sh` against predicate 6. Observed RED first against the
  unmoved pathspec — this is the direction rev-2 left open.
- **AC14** — When `[bar].turnstile_ttl` is set to a value distinguishable from the default, the
  turnstile's holder TTL takes it, asserted in `tools/run-gates/run-gates.turnstile.test.sh`.
  Without this the key replaces a live consumer of a knob this unit removes and is graded by
  nothing in any of the eight units.
- **AC15** — When `tools/gate-legs.toml` declares no `[[profile]]` row,
  `bash tools/run-gates/run-gates.sh` exits 2 naming the file; when its `[bar]` is PARTIAL or
  ABSENT the run PROCEEDS on the declared defaults and says which it took. Observed RED first in
  both directions.
- **AC19** — When `tools/run-gates/run-gates.sh` loads the manifest it EXPORTS the resolved path,
  and neither `tools/run-gates/run-gates.test.sh` nor `tools/run-gates/run-gates.gov.test.sh`
  re-derives one of its own, asserted by a grep over both suites. Observed RED first against
  today's re-derivation. S13 had no criterion at rev-4.
- **AC20** — When a leg's `ceiling` exceeds `[bar].default_ceiling`, the TOML carries a comment
  above that leg, asserted by parsing the file in `tools/run-gates/run-gates.test.sh`. S5
  required this and AC16 grades only the profile-table comments.
- **AC16** — When `tools/gate-legs.toml` is compared against `tools/run-gates/gate-profiles.txt`,
  every comment paragraph in the source appears in the target, asserted by a normalised
  substring join in `tools/run-gates/run-gates.test.sh` while BOTH files exist. After
  `TOOL-aGatheredDeclaration-6` S7 the source is deleted and this can never be checked again.
- **AC17** — When a `[[lane]]` declares a non-boolean `short_circuit`, the runner exits 2 naming
  the lane; when it declares none, the resolved value is `false`, asserted field-by-field in
  `tools/run-gates/run-gates.test.sh`. Observed RED first.
- **AC18** — When `GATE_OPTIN` is the spelling in use, `python tools/govkit/govkit.py selfcheck`
  is still green: its kit-payload policy guard at `govkit.py:1441` keys on the OLD spelling and
  the rename leaves it matching nothing. Observed RED first.
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
- rev-5 · 2026-08-31 · folded round-4 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md`), the round
  that ended the loop NON-CONVERGENT. Findings B4, H2, H4, M1, M2 and M3. rev-4's
  partial-`[bar]` refusal contradicted two siblings' absent-key rows, so S10 now rules which keys
  are required and which defaulted, and coverage rather than refusal holds the two write paths.
  `manifest_blob` has two writers. S13 was ungraded and cited the wrong section for its own
  premise.
- rev-4 · 2026-08-31 · folded round-3 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md`) findings R4, R7, R9, R10, R12 and R13. The
  emitted `[bar]` was two keys of four with nothing defaulting or refusing the rest, so the
  refusal moved into the loader where one check holds both write paths. The comment carry-across
  — the whole point of the format — was graded by nothing, and its evidence is deleted at unit 6.
  `short_circuit` was declared at rev-3 and ruled by no criterion. The `GATE_OPTIN` rename leaves
  a govkit policy regex on the old spelling.
- rev-3 · 2026-08-31 · folded round-2 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md`). Findings R2, R9, R10, R16 and R18. rev-2's answer to F10 closed
  predicate 7 and left predicate 6 watching a file that no longer scopes the bar, which is the
  unsafe direction; S8 now covers both and S8b names the exemption's compensating check. AC10
  could not fail on a JSON-only fixture. `short_circuit` was dropped from the schema when the
  example lane set shrank, leaving unit 8 reading an undeclared key. The guard count was 38, not
  36, by this paragraph's own criterion.
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

# TOOL-aGatheredDeclaration-7 — the upgrader: any adopter's manifest and its tests, onto the declaration

**Status:** OPEN · rev-5 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-2-closing-diff-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-2-closing-diff-round1.md) | diff-review | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-8 |

<!-- /gen:spec-records -->

## 1. Goal

Ship `bash tools/run-gates/adopt-run-gates.sh --upgrade`, which converts an adopter's existing leg
manifest into `gate-legs.toml` and reports what its tests must change. Without it the format move is
a flag day for two live repositories, and the prompt asks for the tool explicitly.

## 2. Scope (IN)

- **S1** — `--upgrade`: read the target's manifest in either observed dialect and write
  `<prefix>/gate-legs.toml`.
- **S2** — TWO input dialects, both observed rather than imagined: a bare JSON ARRAY of leg objects
  (`nicocares`, 40 rows) and a JSON OBJECT whose `legs` key holds them alongside sibling policy keys
  (`incms`, 66 rows plus `_doc`, `pg`, `scoped`, `ceiling_policy`, `ceiling_over_policy`).
- **S3** — FIELD MAPPING, per `TOOL-aGatheredDeclaration-1` §S4: `subject = "kit"` and
  `optIn: true` both become `opt_in = true`; `phase` becomes `lane`; `scope` is carried as a comment
  rather than translated, because its enum is inCMS's and does not travel; `cwd`, `tool`, `ceiling`,
  `guard`, `chunk` and `impure` map by name; `full_only` maps by name too, which rev-1 omitted
  while citing the ruling that retains it. The table is the SOURCE: a key absent from it is
  UNRULED and refuses, a key ruled DROP is reported and its leg still emitted.
- **S4** — PROSE PRESERVATION: `_doc` becomes the file's header comment and `ceiling_over_policy`'s
  entries become comments above the legs they justify. A migration that drops the reasoning is the
  problem this build exists to fix, performed by the tool meant to fix it.
- **S5** — `--upgrade --dry-run`: print the TOML to stdout and write nothing, so an owner reads the
  result before it lands.
- **S6** — THE TEST REPORT. The prompt asks the tool to upgrade "any adopter repo AND ITS TESTS".
  The tool does not rewrite a foreign suite — it REPORTS, naming every file in the target that greps
  for the old manifest path or for a moved field name, with the replacement for each. A tool that
  edits tests it cannot run is how a green suite starts lying.
- **S7** — REFUSALS: an unrecognised dialect, a leg carrying a key no mapping covers, and an
  existing `gate-legs.toml` are each exit 2 naming the cause. The last is not overwritten without
  `--force`.
- **S8** — the e2e arms in `tools/run-gates/adopt-run-gates.test.sh`, driving both dialects from
  fixtures derived from the two real manifests.
- **S9** — the INTERPRETER PROBE, run BEFORE anything is written. It is ONE CANONICAL SOURCE
  inlined into every shipped caller per this kit's no-gov-internal-dependency rule, gated the way
  `resolve_python` already is — NOT a shared file: `TOOL-aGatheredDeclaration-6` S12's caller is
  `tools/govkit/govkit.py`, which is Python and gov-internal, and this one is
  `tools/run-gates/adopt-run-gates.sh`, which is bash and ships into every target. rev-4 said
  "one shared preflight" and named neither file nor language, which no single file can satisfy: the target's resolved python is
  asked to import `tomllib`, and a failure refuses with exit 2 naming the interpreter and its
  version unless `--force`. Without it `--upgrade` converts a working merge bar into a dead one,
  because `TOOL-aGatheredDeclaration-2` S3 makes the TOML win wherever it exists. It is a SHARED
  preflight every write verb calls, not a probe bolted to this one — a per-verb probe is a probe
  the next verb forgets.
- **S10** — the emitted file carries EVERY top-level table the loader owns, not just the legs.
  Three, and rev-2 named one: the `[[lane]]` rows its mapped `lane` values name; the `[bar]`
  table, seeded from the same defaults `TOOL-aGatheredDeclaration-6` S1(d) emits; and the
  `[[profile]]` rows READ FROM the target's own `gate-profiles.txt`, refusing when that file is
  absent. `TOOL-aGatheredDeclaration-2` S3 defines the legacy pair as the manifest TOGETHER WITH
  the profile table and makes the TOML win wholesale, and `kit.toml:146` pins
  `{kit}/gate-profiles.txt` into every target — so an upgrade that emits legs alone silently
  orphans a real adopter's profile table and drops it to the built-in formula.

## 3. Non-goals (OUT)

- Running the upgrade against inCMS or NicoCares. Owner ruling, 2026-08-31.
- Translating inCMS's `scope` enum into `guard` path lists. A `scope` value is a tier name resolved
  through a second file; guessing a path list from it would produce guards that silently scope legs
  out. S3 carries it as a comment and the report tells the owner to assign guards by hand.
- Migrating `pg`, `scoped` or `pg_autowire`. Product-specific; the report names them as dropped and
  says what to do instead.
- Upgrading a target's RUNNER. `adopt-run-gates.sh` already installs the kit; this verb is about the
  declaration.

## 4. Design

### Data model

```
usage: adopt-run-gates.sh --upgrade [--dry-run] [--force] [--manifest <path>] [--prefix <dir>]
```

Dialect detection is on the parsed value's TYPE — a list is dialect A, a dict with a `legs` key is
dialect B, anything else is S7's refusal. No filename heuristic: both repos call the file
`gate-legs.json` and the shapes differ anyway.

### Migration

Field mapping is a TABLE in the source, not a chain of conditionals, so an unmapped key is a lookup
miss that refuses rather than a branch nobody wrote. That is S7's second refusal and it is what
makes a third dialect fail loudly instead of silently losing a field.

### Rollout

The verb is additive. The deprecation line unit 2 prints on a JSON load is what points an adopter
at it.

### Files touched (estimate)

`tools/run-gates/adopt-run-gates.sh` · `tools/run-gates/adopt-run-gates.test.sh` ·
`tools/run-gates/README.md`.

### Alternatives rejected

**A python script.** The kit's whole payload is shell plus the inlined python resolver, and it
already parses JSON through python from shell. A new python entry point would be a second install
surface for one verb.

**Rewriting the target's tests.** Rejected in S6 and worth restating: the tool cannot run a foreign
suite, so it cannot know whether its edit was correct, and an edit it cannot verify is worse than a
report the owner acts on.

## 5. Production-readiness checklist

- security — the verb WRITES into a target repository. It refuses an existing file without
  `--force`, resolves the prefix against the target root and refuses a path escaping it.
- perf / scale — a one-shot conversion of at most a few hundred rows.
- a11y, i18n — N/A.
- error / empty / loading states — S7's three refusals, plus an empty leg list, which is exit 2
  rather than an empty valid file.
- observability — `--dry-run` is the observability. The test report is written to stdout, never to a
  file in the target.
- risks — silent field loss is the one that matters, and the table-driven mapping plus the
  unmapped-key refusal is the answer.
- testing + left-shift gates — S8's arms over both real dialects.
- migration / rollback — the target's JSON is not deleted, so rollback is deleting the TOML.
- user docs — `tools/run-gates/README.md` gains an upgrade section.

## 6. Acceptance criteria

- **AC1** — When `--upgrade` runs against a dialect-A fixture derived from NicoCares' 40 rows, the
  emitted `gate-legs.toml` declares 40 legs whose names and argv match the source exactly, asserted
  in `tools/run-gates/adopt-run-gates.test.sh` by parsing both and comparing.
- **AC2** — When `--upgrade` runs against a dialect-B fixture derived from inCMS's 66 rows, all 66
  legs are emitted, every `optIn: true` row carries `opt_in = true`, and every `phase` value appears
  as a `lane`, asserted the same way.
- **AC3** — When the source carries `_doc` or `ceiling_over_policy`, the emitted file carries that
  prose as COMMENTS and no prose is lost, asserted by grepping the output for a sentinel phrase
  planted in the fixture.
- **AC4** — When a leg carries an UNRULED key — one absent from S3's mapping table — the verb
  exits 2 naming the key and the leg, asserted in `tools/run-gates/adopt-run-gates.test.sh` and
  observed RED first.
- **AC4b** — When a leg carries a key ruled DROP, the leg is still emitted and the report names
  the dropped key, asserted on the same fixture. **AC2 and AC4 were in direct contradiction at
  rev-1**: `full_only` sits on four real inCMS rows and was unmapped, so an honestly derived
  dialect-B fixture could not satisfy both, and the only way to green them was a fixture with the
  key stripped — the fixture-passes-by-finding-nothing class this spec names in its own
  Section 10.
- **AC4c** — When S3's mapping table is compared against the union of keys in both fixtures, the
  table is a SUPERSET, computed from the fixtures rather than typed, asserted in
  `tools/run-gates/adopt-run-gates.test.sh`. That arm fails the moment a real manifest carries a key
  nobody ruled on.
- **AC4d** — When `--upgrade` runs against a fixture target whose resolved python cannot import
  `tomllib`, it writes NOTHING and exits 2 naming the interpreter and its version, asserted in
  `tools/run-gates/adopt-run-gates.test.sh` by a `git status --porcelain` that stays empty.
  Observed RED first.
- **AC4e** — When the emitted TOML declares a leg in lane `<x>`, it also declares a `[[lane]]` row
  named `<x>`, asserted by parsing the output and comparing the two sets.
- **AC5** — When `gate-legs.toml` already exists, the verb exits 2 and writes nothing; with
  `--force` it overwrites, asserted by the file's mtime and content in both arms.
- **AC6** — When `--dry-run` is passed, nothing is written under the target and the TOML appears on
  stdout, asserted by a `git status --porcelain` that stays empty in a scratch target.
- **AC7** — When the target holds a file grepping for the old manifest path, `--upgrade`'s report
  names that file with its replacement; when it holds none, the report says so explicitly rather
  than printing nothing, asserted in `tools/run-gates/adopt-run-gates.test.sh` in both directions —
  an empty report and a report nobody generated must be distinguishable.
- **AC8** — When the emitted TOML is handed to `bash tools/run-gates/run-gates.sh --manifest`, it
  loads and reports the same leg count the source declared AND the same resolved profile row and
  width the target reported before the upgrade, asserted end to end in a scratch repo. The
  profile half is what rev-2's leg-count-only criterion could not see.
- **AC8b** — When the target holds no `gate-profiles.txt`, `--upgrade` exits 2 naming it rather
  than emitting a manifest with no `[[profile]]` row, asserted in
  `tools/run-gates/adopt-run-gates.test.sh`. Observed RED first. **Scoped so it cannot fire on a
  target gov itself created below the interpreter floor**: `TOOL-aGatheredDeclaration-6` S12
  emits a JSON manifest and no profile table for those, by declared consequence, and a refusal
  that reds on gov's own output is a refusal that gets deleted.
- **AC8c** — When the emitted TOML is parsed, its `[bar]` table carries ALL FOUR declared keys with
  the kit defaults, asserted key-by-key against `TOOL-aGatheredDeclaration-6` S1(d)'s emitted set
  rather than against a list typed here. `TOOL-aGatheredDeclaration-2` S10's partial-`[bar]`
  refusal is the backstop: a converter that drops a key is caught by the loader on the first run,
  so this criterion and unit 6's AC14 are held by one check rather than by agreeing with each
  other.

## 7. Gates

`run-gates adopter e2e` · `run-gates canary` · `run-gates wiring` · `govkit selfcheck`. No new leg —
the arms join `adopt-run-gates.test.sh`, which is already a leg.

## 8. Open questions

- **F1 — should `--upgrade` assign a `lane` to a manifest that declares no `phase`?** NicoCares'
  40 rows have none. Defaulting every leg to `heavy` reproduces today's behaviour exactly, which is
  what a migration should do; guessing lanes from leg names would change the bar's behaviour inside
  a format conversion. Recommendation: default to `heavy` and say so in the report.
  RESOLVED (agent, 2026-08-31, delegated): default to `heavy`, reported. A conversion that changes
  behaviour is a conversion whose green means nothing.
- **F2 — should the report be machine-readable?** A `--report-json` would let a target's own gate
  assert the migration is complete. Recommendation: not now. It is speculative until one adopter has
  actually migrated, and the human report is what the prompt asked for.
  RESOLVED (agent, 2026-08-31, delegated): human report only. Fewest open questions, and the
  machine form costs nothing to add once a real migration says what it needs.

## 9. Revision log

- rev-1 · 2026-08-31 · initial draft.
- rev-5 · 2026-08-31 · folded round-4 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md`), the round that
  ended the loop NON-CONVERGENT. Findings H1 and H3. "One shared preflight" crossed a
  Python/bash and a gov-internal/shipped boundary at once, and AC8b could red on a target gov's
  own below-floor intake produces.
- rev-4 · 2026-08-31 · folded round-3 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md`) finding R4, and the shared-preflight half of R11.
  The emitted `[bar]` was two keys of four; the refusal that holds both write paths now lives in
  `TOOL-aGatheredDeclaration-2` S10 and this criterion cites it.
- rev-3 · 2026-08-31 · folded round-2 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md`) finding R4. The
  fold's S10 had the right argument — emitting the legs alone writes a file the runner rejects —
  and stopped one table short of it, dropping `[bar]` and `[[profile]]`.
- rev-2 · 2026-08-31 · folded round-1 spec audit findings F5, F21 and F29. `full_only` was
  unmapped while the spec cited the ruling that retains it, which put AC2 and AC4 in direct
  contradiction on any honest fixture. The interpreter probe carries this build's own R10, which
  the spec did not hold. Lane emission was added because a mapped `phase` with no `[[lane]]` row
  writes a file the runner refuses.

## 10. Reuse audit

The seam is `tools/run-gates/adopt-run-gates.sh`, which already exists as the kit's adopter and
already holds `--check`, its target resolution and its prefix handling — verified against source at
this revision. `--upgrade` is a second verb on that script rather than a new program, which is why
§3 refuses a python entry point.

The FIXTURES are the reuse that matters here, and they are not gov's: both dialects are derived from
the two real manifests recorded in
`build/2026-08-31-build-TOOL-aGatheredDeclaration-1-adopter-review.md`, with their key censuses
already counted there. Deriving a fixture from an imagined dialect is the
`fixture-passes-by-finding-nothing` class, and this unit's whole job is converting shapes that
actually exist.

`python tools/memory-recall/query.py "how does an adopter kit upgrade a target's declared data
without losing what the target declared" --terms "adopter upgrade migration manifest declaration
govkit receipt descriptor emit prefix dialect fixture parity"` — 37 hits, and it changed this spec.
Three records bind:

- `memory/builds/dUnstalledConvoy/reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-spec-rev2.md:328`
  — on an upgrade re-apply govkit fires `a leg that vanished is not a leg that passed` once per
  MIGRATED leg, naming the wrong cause. **The line numbers that record cited are stale at this
  base and are deliberately not repeated.** **A format move is exactly a migrated-leg
  event**, so an adopter running `govkit apply` after this upgrade will meet that refusal on every
  leg. It is unit 6's problem as much as this one's and is recorded in both.
- `TOOL-aPacedTurnstile-12` — govkit's selfcheck joins descriptor rows to the manifest by NAME only
  and never compares the declared GUARDS, while its emit verb copies a guard verbatim. The format
  move does not fix that and must not appear to: the join moves files, not predicates.
- `TOOL-aFlaggedScaffold-3` — `govkit update` cannot land a source gov started shipping, because its
  classification loop has no arm for a descriptor source with no receipt row. `gate-legs.toml` IS
  such a source. Measured on the inCMS adopter. This is a PREREQUISITE for an adopter taking this
  format through the ordinary channel, and it is not in this build's roster.

**The third one is a genuine blocker for the shipped path and is escalated rather than absorbed**:
without it an adopter takes the new format only by running `--upgrade` by hand, which is the tool
this unit ships, so the build still delivers — but the deployer route stays broken and the report in
S6 must say so.

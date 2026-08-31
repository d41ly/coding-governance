# TOOL-aGatheredDeclaration-3 — the runner's argument surface: `--list`, `--leg`, `--manifest`

**Status:** INPROGRESS · rev-5 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md](../build/2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md) | research | TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-6 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |
| [2026-08-31-review-TOOL-aGatheredDeclaration-2-closing-diff-round1.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-2-closing-diff-round1.md) | diff-review | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 TOOL-aGatheredDeclaration-8 |

<!-- /gen:spec-records -->

## 1. Goal

Give `tools/run-gates/run-gates.sh` a real argument surface so a single leg can be run by name and
the declared manifest can be printed. The runner parses no arguments today, so every check costs the
whole bar — a 26-minute floor on this tree — and there is no way to answer "what does this bar
declare" except by reading a JSON file.

## 2. Scope (IN)

- **S1** — `--leg <name>`, REPEATABLE: run exactly the named legs, in manifest order, ignoring every
  guard and every opt-in hold. A name matching no leg is a refusal naming the closest candidates.
- **S2** — `--list`: print every leg name, one per line, and exit 0. inCMS's spelling
  (`scripts/gate.sh:288-291`), because a fleet with two runners should not have two spellings.
- **S3** — `--manifest`: print the declared manifest as a table — leg count, and per leg its name,
  lane, opt-in status, ceiling, guard count and whether it would run under the current selection.
  This is the prompt's "expose and require a clear manifest from the gates it runs".
- **S4** — `--help` / `-h`: the usage line, exit 0. An unknown argument is exit 2 naming it.
- **S5** — the `need2` guard: every two-token flag validates its value BEFORE it shifts. Ported from
  `scripts/gate.sh:25`, where a `shift 2` with `$#=1` fails without shifting and spins the parse
  loop forever — that repo reproduced it as a hung push gate at exit 124.
- **S6** — the OPT-IN COVERAGE ledger: `<git-dir>/gate-optin-lastrun.tsv`, and a post-run block
  naming every opt-in leg this run did NOT exercise and when each last ran. Harvested from
  `scripts/gate.sh:735-786`; it closes `TOOL-aGradedDoorway-9` in this repo's backlog.
- **S7** — a sharded run NEVER stamps `gate-full-green`, and says so on the line that would have
  stamped it.
- **S8** — the QUERY VERBS are read-only and say so structurally: `--list` and `--manifest` load
  the manifest early, NEVER acquire the turnstile, and write only their payload to stdout. The
  profile line and any queue line go to stderr for these verbs.
- **S9** — `--manifest` joins each declared ceiling against `<git-dir>/gate-ledger.tsv` and prints
  the measured seconds and the ratio, flagging any leg whose ceiling is under 3x its measurement.
  It REPORTS and never reds. This is the surviving half of `TOOL-aCollapsedScan-5` and it is what
  stops the declarations rotting once `TOOL-aGatheredDeclaration-4` turns enforcement off.
  **The ledger is PER-CLONE and often absent**, so the rendering is declared rather than left to
  the implementation: a leg with no ledger row renders its measured column as a DASH and its
  ratio column as a dash, never as a zero, and a run with no ledger at all prints one line
  saying the join found no measurements. A zero for a probe that never ran is a reassuring number
  about nothing, which is the class this repo already names.

## 3. Non-goals (OUT)

- `--since <sha>` scoped mode. The `guard` mechanism already scopes this bar off the merge-base and
  a second selector would be two answers to one question. Named as a follow-up, not built.
- Changing what a leg IS. This unit selects legs; it does not change dispatch, the pool, the run
  record or the report tail contract.
- `--legs <file>` as a flag. `GATE_LEGS` already exists and both harnesses drive it; inCMS's reason
  for preferring a flag (a hook cannot be redirected by an env var) is a real hardening and is
  recorded as a follow-up rather than smuggled in here.
- Running a leg's INNER check rather than the leg. A leg's argv is its check; a suite that shards
  internally already declares `--shard i/n` as separate manifest rows, asserted by
  `run-gates.gov.test.sh:347-403`, and that mechanism is untouched.

## 4. Design

### Data model

**Ordering is an INTERFACE property, not an implementation detail.** `PROF_LINE` is echoed to
STDOUT at `run-gates.sh:405`, the turnstile acquires at `:420` with a bounded wait four times the
TTL, and the manifest is not loaded until `:846`. A query verb that ran in place would therefore
queue behind a running bar for up to two hours to answer a read-only question, and its stdout
would carry the profile line. So the verbs load the manifest early and exit before the turnstile
is touched, and everything that is not their payload goes to stderr.

Argument parsing sits above every existing env read, so nothing already declared changes meaning.
`--leg` accumulates into a bash array; the selection loop that today evaluates `changed()` and the
opt-in hold gains one earlier branch: when the array is non-empty, a leg is selected iff its name is
in it, and no guard or hold is consulted.

```
usage: run-gates.sh [--leg <name>]... [--list] [--manifest] [--help]
```

**The `LEG` row format is an OUTPUT CONTRACT and it is spelled ONCE, here.** Every other unit
CITES this paragraph; a second spelling elsewhere is the defect this whole build exists to
remove, and `TOOL-aGatheredDeclaration-4` had one at rev-3.

```
gate manifest: <n> legs · <n> opt-in · <n> guarded · profile <row> width <w> · ceilings <on|off> from <env|declaration|default>
LEG  <name>  <lane>  <opt-in|always>  <ceiling|none>  <guards>  <would-run|held|guarded-out>  <measured|->  <ratio|->  <enforced|declared-only>
```

The ceiling column stays the DECLARED NUMBER in every state — it is what AC11 computes a ratio
from, so a unit that overwrites it with a word makes two criteria mutually unsatisfiable, which
is exactly what happened. Enforcement is reported by an APPENDED column and by the header's
`ceilings` clause instead. Every new column goes at the END, because one inserted before an
existing one is read AS that one by any reader not moved in the same commit — the same
append-only rule `TOOL-aGatheredDeclaration-2` states for the RS/US wire format.

### Inventory

`--manifest` prints one header line and one row per leg, in the shape the OUTPUT CONTRACT above
pins. **It is not respelled here** — rev-4 declared the contract "spelled ONCE" and then spelled
it again eleven lines below in the pre-fold form, which is what made unit 4's citation of "unit 3
§4's contract" ambiguous between two texts.

The counts are DERIVED at emission from the loaded declaration. No count is written in prose
anywhere, which is the charter's rule and the reason this verb exists at all.

### Rollout

Additive. A run with no arguments behaves exactly as today, which is what `.githooks/pre-push` and
`tools/push-main.sh` invoke.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.test.sh` · `tools/run-gates/README.md`.

### Alternatives rejected

**An env var, `GATE_ONLY=<name>`.** Consistent with the runner's existing style and rejected for
inCMS's stated reason: an env var can be set in a shell that later invokes a hook, so the
authoritative push bar could be silently narrowed to one leg by an exported variable. A flag cannot
reach `.githooks/pre-push`, which invokes the runner with no arguments.

## 5. Production-readiness checklist

- security — the narrowing risk above is why this is a flag. S7 is the second half: a narrowed run
  must not be able to leave evidence that a full one happened.
- perf / scale — this unit IS the performance change. One leg instead of 86.
- a11y, i18n — N/A, no user interface.
- error / empty / loading states — an unknown flag, a missing flag value, and a `--leg` naming no
  leg are each exit 2 naming the offence. `--leg` with an empty manifest is exit 2, not exit 0.
- observability — `--manifest` is the observability. The ledger in S6 is the second half.
- risks — the one real hazard is a sharded green being mistaken for a bar. S7 answers it at the
  stamp; the summary line names the shard.
- testing + left-shift gates — arms in `run-gates.test.sh`, each observed RED first.
- migration / rollback — additive; rollback is not passing the flags.
- user docs — `tools/run-gates/README.md`, and the charter's merge-bar command block.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-gates.sh --leg "<name>"` names one leg, exactly that leg
  dispatches and the summary names one leg, asserted in `tools/run-gates/run-gates.test.sh` by a
  scratch manifest whose other legs write marker files that must be absent.
- **AC2** — When `--leg` is passed twice, both legs run and their `GATE ok` rows are REPORTED in
  manifest order rather than argument order, asserted in `tools/run-gates/run-gates.test.sh` by
  reading the captured report rows. **Not execution order**: `run-gates.sh:16-17` states that
  execution order is a scheduling detail and `:842-844` dispatches longest-first from the timing
  cache, so a marker-file mtime assertion would be a race at any width above 1 and would grade
  the cache at width 1.
- **AC3** — When `--leg` names a leg that is guarded out or opt-in held, it RUNS anyway, asserted
  with a leg carrying a guard on an untouched path and `opt_in = true`.
- **AC4** — When `--leg` names nothing in the manifest, the runner exits 2 and its message names the
  unmatched value, observed RED before the arm is written.
- **AC5** — When `--list` runs, stdout is exactly the leg names in manifest order, one per line, and
  the exit code is 0, asserted by byte-comparing against the names the loader emits.
- **AC6** — When `--manifest` runs, its header counts equal the counts re-derived from
  `tools/gate-legs.toml` by an independent reader in the arm, so a hand-written number cannot pass.
- **AC7** — When a two-token flag is given with no value, the runner exits 2 with a message naming
  the flag and does NOT hang, asserted under `timeout` with the elapsed time compared against an
  untimed control rather than against a literal.
- **AC8** — When a run passes `--leg`, `<git-dir>/gate-full-green` is not written and the summary
  states the run was sharded, asserted by the file's absence plus the summary line.
- **AC10** — When a beacon is PLANTED and the turnstile is enabled, `--list` and `--manifest` each
  complete immediately, asserted in `tools/run-gates/run-gates.turnstile.test.sh` with an
  elapsed-time bound taken against an untimed control rather than a literal.
- **AC11** — When `--manifest` runs, each leg row carries its declared ceiling, the seconds
  `<git-dir>/gate-ledger.tsv` recorded for it, and their ratio, with a flag on any ratio under 3,
  asserted in `tools/run-gates/run-gates.test.sh` against a planted ledger.
- **AC14** — When `--manifest` runs, one recorded row is compared FIELD-BY-FIELD against a fixture
  in `tools/run-gates/run-gates.test.sh` holding the contract above. Any later unit changing a
  column then reds this arm instead of quietly redefining the contract in prose, and AC11's ratio
  arm parses the same fixture.
- **AC12** — When `bash tools/run-gates/run-gates.sh --help` runs, it prints the usage line and
  exits 0; when an unknown argument is passed, it exits 2 naming the argument. Asserted in
  `tools/run-gates/run-gates.test.sh`. S4 had no criterion at rev-2, which left the one
  pure-surface scope item ungraded.
- **AC13** — When `--manifest` runs against a tree with NO `<git-dir>/gate-ledger.tsv`, every
  measured column is a dash and one line says the join found no measurements, asserted in
  `tools/run-gates/run-gates.test.sh`. AC11's planted-ledger arm grades only the populated
  direction.
- **AC9** — When a run holds an opt-in leg, `<git-dir>/gate-optin-lastrun.tsv` carries that leg and
  the post-run block names it with its last-run stamp, asserted across two consecutive scratch runs.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `run-gates turnstile` ·
`run-gates adopter e2e` · `run-gates wiring`. No new leg.

## 8. Open questions

- **F1 — should `--leg` accept a prefix or a glob?** Exact match is unambiguous; a glob is what an
  operator actually wants when a suite is sharded into `foo 1/3`, `foo 2/3`, `foo 3/3`.
  Recommendation: exact match only, with the refusal in AC4 printing the near-misses, which gives
  the operator the glob's benefit without a matching rule to specify and test.
  RESOLVED (agent, 2026-08-31, delegated): exact match with near-misses printed. Fewer open
  questions than a glob dialect, and it reuses the refusal that has to exist regardless.

## 9. Revision log

- rev-1 · 2026-08-31 · initial draft.
- rev-5 · 2026-08-31 · folded round-4 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round4.md`), the round
  that ended the loop NON-CONVERGENT. Finding B3: the Inventory block respelled the contract
  the paragraph above it declares is spelled once, in the shape the fold had just replaced.
- rev-4 · 2026-08-31 · folded round-3 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round3.md`) finding R2. The `LEG` row was spelled here and
  incompatibly in `TOOL-aGatheredDeclaration-4`, whose AC8 overwrote the ceiling column AC11
  computes its ratio from; the two criteria could not both be green. The contract is now spelled
  once, enforcement moved to an appended column and a header clause, and AC14 pins it as a
  fixture.
- rev-3 · 2026-08-31 · folded round-2 spec audit
  (`reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md`) findings R13,
  R14 and R15. The fold-new ledger join had no unmeasured-leg rendering, no empty state and a
  one-armed criterion; `--help` and the unknown-argument refusal had no criterion at all; and the
  new columns needed the append-only rule stating against the pinned row format.
- rev-2 · 2026-08-31 · folded round-1 spec audit findings F14 and F15. AC2 was grading EXECUTION
  order, which the runner explicitly disclaims, by a mechanism that is a race above width 1; it
  now grades reporting order. S8 and S9 were added: the query verbs' turnstile and stdout
  behaviour was unspecified and AC5 and AC6 pulled it in opposite directions, and the ceiling
  join is this build's R5 landing where it costs nothing.

## 10. Reuse audit

The seam is the selection loop in `tools/run-gates/run-gates.sh` around `changed()` at line 151 and
the opt-in hold at lines 927-948 — verified against source at this revision. Both are already the
single place where a leg is chosen, so `--leg` adds one branch above them rather than a second
selector; a second selector is the mechanism `TOOL-aGradedDoorway-9` reports as making a held leg
and a passed leg indistinguishable.

`reuse_lookup.py` returned no gov seam for an argument parser, correctly — the runner has none. The
seam that exists is in an adopter, `C:/projects/incms/main/scripts/gate.sh:25-39`, whose parse loop
and `need2` guard are ported rather than reinvented, with the hang it was written for recorded in S5.

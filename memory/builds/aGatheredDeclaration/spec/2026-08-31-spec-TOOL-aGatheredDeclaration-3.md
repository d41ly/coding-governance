# TOOL-aGatheredDeclaration-3 — the runner's argument surface: `--list`, `--leg`, `--manifest`

**Status:** OPEN · rev-1 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

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

Argument parsing sits above every existing env read, so nothing already declared changes meaning.
`--leg` accumulates into a bash array; the selection loop that today evaluates `changed()` and the
opt-in hold gains one earlier branch: when the array is non-empty, a leg is selected iff its name is
in it, and no guard or hold is consulted.

```
usage: run-gates.sh [--leg <name>]... [--list] [--manifest] [--help]
```

### Inventory

`--manifest` prints one header line and one row per leg:

```
gate manifest: <n> legs · <n> opt-in · <n> guarded · profile <row> width <w> · ceilings <on|off>
LEG  <name>  <lane>  <opt-in|always>  <ceiling|none>  <guards>  <would-run|held|guarded-out>
```

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
- **AC2** — When `--leg` is passed twice, both legs run and they run in MANIFEST order rather than
  argument order, asserted by the marker files' mtime ordering in a scratch repo.
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

## 10. Reuse audit

The seam is the selection loop in `tools/run-gates/run-gates.sh` around `changed()` at line 151 and
the opt-in hold at lines 927-948 — verified against source at this revision. Both are already the
single place where a leg is chosen, so `--leg` adds one branch above them rather than a second
selector; a second selector is the mechanism `TOOL-aGradedDoorway-9` reports as making a held leg
and a passed leg indistinguishable.

`reuse_lookup.py` returned no gov seam for an argument parser, correctly — the runner has none. The
seam that exists is in an adopter, `C:/projects/incms/main/scripts/gate.sh:25-39`, whose parse loop
and `need2` guard are ported rather than reinvented, with the hang it was written for recorded in S5.

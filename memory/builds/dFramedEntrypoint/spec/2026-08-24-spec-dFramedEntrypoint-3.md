# TOOL-dFramedEntrypoint-3 — the declared registry that says which build READMEs the contract binds

**Status:** SPECCED · rev-4 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams tooling

## 1. Goal

The slot canon and its budgets need a population, and every date-keyed candidate exempts all 61
tracked build READMEs on the day it is set while the population guard reports green over the emptiness.
This unit declares the population instead: a tracked registry asserted in BOTH directions, so a new
build README that joins no row reds, and a row naming a path that no longer exists reds too.

## 2. Scope (IN)

- **S1** — `memory/project/readme-contract.txt`, a tracked registry listing one repo-relative build
  README path per row, comments permitted, seeded from the conforming subset.
- **S2** — the FORWARD assertion: every tracked `memory/builds/*/README.md` that is not named by a row
  and not named by an explicit exemption row reds, so a new build cannot silently escape the contract.
- **S3** — the REVERSE assertion: a row naming a path that is not a tracked build README reds, so a
  stale row cannot silently widen the surface it was written to narrow.
- **S4** — an EXEMPTION section within the same file, each exemption row carrying its reason inline,
  for the legacy READMEs that predate the contract. The pin is an EQUALITY, not a ceiling: a pin above
  the measured exempt count reds and names both numbers. A one-sided pin leaves permanent slack after
  a drain, which is how a shrink-only list stops shrinking without anyone noticing — this repo's own
  drift audit reports three of five such lists out of tolerance today.
- **S5** — the registry reader shipped by unit 1 is pointed at this file, and this unit REPLACES unit
  1's absent-file behaviour: unit 1 ships it returning an empty set when the file is absent, which is a
  pass, and from here an absent registry is a refusal. The corresponding unit-1 selftest arm is
  inverted in this unit rather than left contradicting AC5. The two verdict tiers of unit 2 grade only
  rows in the bound set.
- **S6** — the registry is graded by the same `build README slot contract` leg, not by a new one.
- **S6b** — hygiene check 3 grades `memory/project/` against a CLOSED filename allowlist and emits
  anything else as a structure failure, so this unit ALSO adds the registry's name to that case list,
  with its selftest arm and the matching `HYGIENE.template.md` prose. Without it the unguarded `memory
  hygiene` leg reds on the first bar after the file lands. The placement is precedented: the
  method-carriers registry is allowlisted there and owned by a different script.
- **S6c** — `tools/memory-tree/adopt-memory-tree.sh` scaffolds an empty registry into an adopting repo,
  so an adopter is not left with a refusal on a file the kit never created.
- **S7** — selftest arms for both directions, the exemption path, the pin in BOTH directions, a
  malformed row, a row naming a path outside the build-README class, the inverted absent-file arm from
  S5, and the check-3 allowlist arm from S6b.
- **S-EPOCH** — this unit moves `tools/memory-tree/gen_build_index.py`, which is inside the
  verdict-epoch gate's scan set, so its landing carries a `KIT_MEMORY_TREE_VERSION` bump. The carrier
  set is DERIVED, never read off the epoch gate's remedy text: bump the constant and its inline marker
  in the engine, then every carrier `git grep -l 'gov:kit memory-tree@'` returns over tracked paths
  outside `memory/builds/` and `memory/archive/`, then re-render the live copies with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The remedy string names three paths and
  the parity harness three pairs; their union is five, and there are SEVEN carriers — the two it cannot
  reach are kit SOURCES rather than dogfood copies. Following the remedy exactly reds the unguarded
  `kit version markers` leg, which is `TOOL-dSettledRoster-4` in the backlog, recorded as having cost a
  full-bar cycle twice. The rule binds per PUSH RANGE, not per commit: units landing in one push need
  one correctly-placed bump, on the LAST engine-moving commit in that range. It is stated in every
  engine-moving unit rather than once, because a rule written in one spec is a rule the other seven do
  not carry.

## 3. Non-goals (OUT)

- No DATE KEY, and no better date key either. The refusal is not about which date is forgeable; it is
  that every date key exempts the whole corpus on the day it is set, and that the population guard
  counts before the date filter so the resulting emptiness reports clean.
- No AUTOMATIC ENROLMENT of existing READMEs. A path joins the bound set when its build's owner
  conforms it, which is unit 7's work for the seed and the individual builds' work afterwards.
- No SILENCING of other checks. This registry declares which files the SLOT CONTRACT binds and nothing
  else. It is deliberately not the shape of `memory/project/curation-debt.txt`, whose rows silence
  three checks on a whole file to buy one row.
- No migration of the existing curation-debt rows into this file. Those grade byte and line caps that
  this contract does not touch.

## 4. Design

### Data model

One path per row. A leading marker distinguishes a BOUND row from an EXEMPT row, and an exempt row
carries its reason on the same line, because an exemption whose reason lives elsewhere is an exemption
nobody can drain. A pin line declares the exempt count, and the count is shrink-only.

### Inventory

The seed is the conforming subset measured at unit 7's landing. Before that, the bound set is empty
and unit 1's S5 makes that emptiness announce itself, so this unit can land ahead of the corpus work
without shipping a check that reports coverage it does not have.

### Migration

The registry file lands empty of bound rows and full of exempt rows, one per existing README, each
with a reason. That is the honest starting state: it binds nothing yet, says so, and every row that
converts from exempt to bound is a visible diff. The alternative — landing with the whole corpus bound
— is the 32-row waiver the owner ruled against.

### Alternatives rejected

**A `curation-debt.txt`-shaped registry.** Rejected on this repo's own evidence: that file seeded at
zero rows, sits at seven, has never drained one, and its drain condition is another node's prose. Its
rows also silence a whole file's worth of checks rather than one rule. The bidirectional assertion is
what makes this registry different, and it is the property that matters.

**A front-matter opt-in key on each README.** Rejected because it puts the declaration inside the file
being graded, so a file can exempt itself by editing one line, and because the reverse assertion then
has nothing to assert against.

### Files touched (estimate)

`memory/project/readme-contract.txt` (new, tracked, LF-pinned) · `tools/memory-tree/gen_build_index.py`
for the two assertions, the pin and the selftest arms · `tools/memory-tree/check-memory-hygiene.sh` for
check 3's allowlist, with its arm in `check-memory-hygiene.test.sh` ·
`tools/memory-tree/adopt-memory-tree.sh` for the adopter scaffold · `.gitattributes` ·
`tools/memory-tree/HYGIENE.template.md` edited FIRST with `memory/HYGIENE.md` re-rendered · the
`build-readme-surface` dossier.

## 5. Production-readiness checklist

- security — N/A. A tracked list of repo-relative paths.
- perf / scale — two set comparisons against `git ls-files` output already read by the generator.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an absent registry file is a refusal naming the expected path. An
  empty bound set is legal and announced, which is the state this unit lands in.
- observability — the leg prints the bound count, the exempt count and the pin on every run, so the
  three numbers that describe the contract's reach are readable without opening the file.
- risks — the recorded hazard for a registry in this tree is that it never drains. Mitigated by the
  shrink-only pin, which turns a stalled drain into a visible number rather than a silent one, and by
  keeping the drain condition inside the build that owns the file.
- testing + left-shift gates — arms for both directions plus the pin, the malformed row and the
  out-of-class path.
- migration / rollback — rollback is deleting the file, which is a refusal by design.
- user docs — the file's own header states both assertions and the drain condition; the grammar lands
  in `memory/HYGIENE.md` via its template.

## 6. Acceptance criteria

- **AC1** — When a tracked build README is named by neither a bound row nor an exempt row,
  `python tools/memory-tree/gen_build_index.py --check-format` exits 1 and names that path.
- **AC2** — When a row names a path that `git ls-files` does not carry as a build README,
  `--check-format` exits 1 and names that row.
- **AC3** — When a build README moves from an exempt row to a bound row and conforms, `bash tools/run-gates/run-gates.sh` is green
  and the exempt count printed by the `build README slot contract` leg has fallen by one.
- **AC4** — When the exempt count DIFFERS from the declared pin in either direction, `--check-format`
  exits 1 naming the pin and the measured count.
- **AC5** — When `memory/project/readme-contract.txt` is absent, `--check-format` exits 1 naming the
  expected path rather than skipping.
- **AC6** — When the registry carries a malformed row, `--check-format` exits 1 quoting that row.
- **AC7** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, the arms for both
  assertion directions pass, each having been observed RED against a staged break first.
- **AC8** — When the leg runs, its output names the bound count, the exempt count and the pin declared
  in `memory/project/readme-contract.txt`.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs with the registry present, check
  3 passes, observed RED first against the same tree with the allowlist entry removed.

## 7. Gates

`build README slot contract` · `build-index selftest` · `memory hygiene` · the LF discipline check ·
`check-kit-versions.sh` (leg `kit version markers`, unguarded) · `check-verdict-epoch.sh` ·
`kit/dogfood doc parity`.

## 8. Open questions

- **F1 — should the exempt pin start at the full corpus size or at the measured non-conforming count?**
  Starting at the full size means the first conformance does not move the number; starting at the
  measured count makes the pin bind immediately but requires unit 7 to land first.
  Recommendation: start at the full size in this unit and let unit 7 lower it in the commit that seeds
  the bound set, so neither unit depends on the other's ordering.
- **F2 — do build READMEs under a build with a terminal status ever leave the exempt list?** They are
  historical artifacts nobody resumes from, and their two judgement slots cannot be honestly authored
  after the fact. Recommendation: they stay exempt permanently, with the reason recorded once in the
  file's header rather than per row. Owner decision.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the owner's fork-1 ruling and the verification finding that
  every date key exempts the whole corpus on the day it is set.
- rev-2 · 2026-08-24 · folded spec-audit round 1. Check 3's closed allowlist for `memory/project/`
  enters scope: without it the registry file reds the unguarded hygiene leg on its first bar. The
  exempt pin becomes an equality, since a one-sided pin leaves slack a drain never reclaims. The
  absent-registry behaviour is stated as a deliberate REPLACEMENT of unit 1's, rather than as a
  contradiction between two specs. The adopter gains a scaffolded empty registry.
- rev-3 · 2026-08-24 · folded the factual corrections from round 1's LOW tier. The reuse audit no
  longer claims method-carriers is the only registry that reds on a stale row; the claim was checked
  and is false, and the paragraph now rests on the shape match it actually has.
- rev-4 · 2026-08-24 · folded spec-audit round 2. The kit-version carrier set becomes a derivation,
  and `kit version markers` joins the gate list.

## 10. Reuse audit

`memory/project/method-carriers.txt` with `tools/memory-tree/check-method-carriers.sh` is the existing
seam and the shape this unit copies: a declared population asserted in both directions. It is not the
ONLY registry here that reds on a stale row — that claim was checked and is false — but it is the one
whose both-directions assertion is stated as its purpose rather than emerging from its predicate, and
it is the nearest match in subject: a declared list of tracked markdown paths a gate must cover. The check is not
reused as code because its subject is a different file class and its predicate names that class
directly; what is reused is the SHAPE, and the reuse is recorded here so a later reader does not read
the duplication as an oversight.

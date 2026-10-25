# TOOL-dPlacedRequest-18 — the cadence segment of the lease grammar takes any tag-grammar name

**Status:** OPEN · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 7 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0136@c9686488 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

A cadence run's lease, `refs/gov/leases/run/<cadence>/<period>`, takes as `<cadence>` any name the
tag grammar's segment production admits, never a literal list of cadence kinds, so a cadence item an
expansion registers holds a lease the way `maintain` and `review` do (gap-conc-18; P40; Runtime's rule
that a registered name never meets a literal list).

## 2. Scope (IN)

- **S1** — The predicate: `check_cadence_segment <name>` in `tools/unattended/unattended.sh` returns 0
  when `<name>` matches the `seg` production of PLAY-dOrderedCharter-19 S1, `[a-z0-9][a-z0-9-]*`, and
  is at most 64 bytes, and otherwise returns 1 with the rule it broke on one line. It is the one test
  TOOL-dPlacedRequest-1's ref builder `derive_lease_ref run <cadence> <period>` applies to a cadence
  segment, after `check_lease_segment` has held it to a legal ref component; neither the builder nor
  `read_claims`, which parses the cadence back out of each run-lease ref, names a cadence kind.
  Observed by AC1, AC2, AC3.
- **S2** — The parity with the tag grammar: the predicate's answer equals `parse_tag`'s
  (`tools/playbook/tag_index.py`, PLAY-dOrderedCharter-19 S1) over the probe set of §4, each name
  checked as the tag `unit.<name>`. The shell spells the production once, as `RULE_KEY_RE`'s shape
  (`tools/roles/roles_lib.py:65`) less its optional `?`, and the comparison is what keeps the two one
  fact. Observed by AC4.
- **S3** — The slug `run` is reserved: `derive_lease_ref build run` and `derive_lease_ref unit run <id>`
  refuse, because `refs/gov/leases/run/build` and a cadence named `build` cannot both exist (§4
  "The collision"). Observed by AC5.
- **S4** — The documentation: the stops guide's section 7 spells the run-lease form as
  `refs/gov/leases/run/<cadence>/<period>`, `<cadence>` any tag-grammar segment, and names the reserved
  slug. Observed by AC6.

## 3. Non-goals (OUT)

- Registering cadence items, or checking that a cadence name is registered. The clause admits any name
  the grammar admits; the registry of cadence items is dTendedCadence's and the expansions'.
- The `<period>` segment's grammar, the lease record and the acquire, renew and release verbs:
  TOOL-dPlacedRequest-1's.
- Editing `tools/playbook/tag_index.py` or the namespace registry: PLAY-dOrderedCharter-19's.
- Rewriting the design record that spells the literal list (coordination.md:81): a frozen design
  record, outside this build's write set.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — the lease grammar `refs/gov/leases/<slug>/build` with its unit and `run/<cadence>/<period>` forms, `derive_lease_ref`, which calls this unit's predicate for a cadence, and the `--lease` verb; without it there is no cadence lease to narrow
- **consumes-from** external — PLAY-dOrderedCharter-19's `tools/playbook/tag_index.py` and its `parse_tag`, the grammar's owner, which the chain builds before this build's build run
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### Evidence

- No lease grammar exists at `c63aabbb`: the only claim namespace is `CLAIM_NS="refs/gov/runs"`
  (`tools/unattended/unattended.sh:2087`), and `git grep -n "maintain|review"` over
  `tools/unattended/` finds nothing.
- The design spells the run lease with a literal list, `refs/gov/leases/run/<maintain|review>/<period>`
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md:81`), the
  form gap-conc-18 names.
- The segment production is `seg := [a-z0-9][a-z0-9-]*`, at most 64 bytes, compiled in
  `tools/playbook/tag_index.py` with `parse_tag` returning the namespace and segments or the rule broken
  (PLAY-dOrderedCharter-19 S1, its AC1). The same character class already ships as `RULE_KEY_RE`
  (`tools/roles/roles_lib.py:65`, `^[a-z0-9][a-z0-9-]*\??$`).

### The predicate

```
check_cadence_segment <name>
  [[ $name =~ ^[a-z0-9][a-z0-9-]*$ ]]   else "outside seg"
  [ ${#name} -le 64 ]                    else "over 64 bytes"
```

The test runs in the shell, with no process start, because a run-lease ref is built and parsed on the
lease path; S2's comparison is what binds its spelling to the grammar's owner.

### The probe set

| Name | Expected | Why |
|---|---|---|
| `nightly-audit` | admitted | a cadence item no literal list names |
| `maintain` | admitted | today's design kind still holds |
| `9am` | admitted | a digit may lead a segment |
| `Nightly` | refused | an upper-case letter |
| `-x` | refused | a leading dash |
| `a.b` | refused | a dot ends the segment |
| 59 `a` | admitted | the longest name whose tag `unit.<name>` stays within 64 bytes |
| 65 `a` | refused | over 64 bytes |

The parity check feeds each name to the predicate and `unit.<name>` to `parse_tag`, `unit` being a
namespace PLAY-dOrderedCharter-19 registers, and requires one verdict per row. A name between 60 and
64 bytes is admitted by the predicate and refused by the tag's own 64-byte cap; the set leaves that
band out, and §5 names it.

### The collision

A slug named `run` would give its build lease the ref `refs/gov/leases/run/build`, and a cadence named
`build` the ref `refs/gov/leases/run/build/<period>`. Git refuses the second while the first exists,
and the reverse, because one ref name cannot be both a file and a directory (probed at writing:
`git update-ref refs/gov/leases/run/build/2026-10` failed with "'refs/gov/leases/run/build' exists;
cannot create" in a scratch bare repository). With a literal cadence list the two never met; with any
segment admitted they can. Reserving the slug is one comparison; reserving cadence names would be the
literal list the clause forbids.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_cadence_segment` | function | `tools/unattended/unattended.sh` |
| the reserved slug `run` | refusal in `derive_lease_ref` | `tools/unattended/unattended.sh` |

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/STOPS.template.md`, rendered to `memory/guides/UNATTENDED-STOPS.md`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Calling `tag_index.py` on every run-lease build.** It starts a process on the lease path for a
  regular expression, and an adopter without the playbook kit could not build a run lease at all.
- **A registry lookup of cadence names.** It admits fewer names than the grammar, which the clause
  does not ask for, and couples the lease path to a registry another build owns.
- **Reserving the cadence names `build` and `unit`.** That is a literal list on the cadence segment.

## 5. Production-readiness checklist

- security — no new write path; the predicate narrows what reaches a ref name, and every refused
  name is refused before any remote read.
- perf / scale — one bash pattern test per run-lease build or parse; no process start.
- error / empty / loading states — an empty name fails `seg` and is refused with its rule.
- observability — the refusal names the rule broken and the name.
- risks — a name of 60 to 64 bytes is a legal cadence segment and an illegal `unit.<name>` tag, so
  such a cadence can hold a lease no tag can name; no cadence item is that long, and the parity set
  leaves the band out rather than hide it.
- testing — the probe set, a fixture acquisition and the collision case, under AC1 to AC5.
- migration — none: the predicate admits both kinds the design spelled.
- user docs — the stops guide's section 7; no page under `help/` describes leases.

## 6. Acceptance criteria

The unattended kit's own suites are waived for this build's landing (README rule 8), so each probe
below is the observation.

- **AC1** — When a probe sources `unattended.sh` and calls `check_cadence_segment` on each name of
  §4's probe set, each returns the expected verdict, and every refusal line names its rule.
  Red when: `Nightly`, `-x`, `a.b` or the 65-byte name is admitted, or `nightly-audit` is refused.
- **AC2** — When a fixture clone runs `unattended.sh --lease acquire run nightly-audit 2026-10-25`,
  the bare remote holds `refs/gov/leases/run/nightly-audit/2026-10-25`, and `unattended.sh --claims`
  lists it back; `--lease acquire run Nightly 2026-10-25` is refused naming `outside seg`.
  Red when: a cadence outside `maintain` and `review` cannot hold a lease, the reader drops it, or a
  name outside the grammar reaches the remote.
  fixture: a bare remote and one clone under `%TEMP%`, the lease switch on.
- **AC3** — When `git grep -nE "maintain|review" -- tools/unattended/unattended.sh` runs, it prints no
  line of the lease ref builder or reader.
  Red when: either spells a cadence kind.
- **AC4** — When a probe feeds §4's probe set to `check_cadence_segment` and each `unit.<name>` to
  `parse_tag` from `tag_index.py`, the two verdicts agree on every row.
  Red when: the shell's production drifts from the grammar's, as a planted `[a-z][a-z0-9-]*` in the
  predicate does by refusing the set's digit-led `9am`.
- **AC5** — When the fixture runs `unattended.sh --lease acquire build run`, `derive_lease_ref` refuses
  it naming the reserved slug and the remote holds no `refs/gov/leases/run/build`.
  Red when: the slug `run` reaches the remote.
- **AC6** — When `grep -n "run/<cadence>/<period>" tools/unattended/STOPS.template.md` runs, section 7
  names the form and the reserved slug.
  Red when: the guide still spells a cadence list or omits the reservation.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC4 AC5 · the probe set, the parity with `parse_tag` and the reserved slug, staged against the base driver, which has no cadence predicate · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Where does the segment test live?** (a) A bash pattern in the driver, compared with
  `parse_tag` over a fixed probe set; (b) a call into `tag_index.py` on every run-lease build; (c) the
  bash pattern alone. (b) starts a process on the lease path and fails closed in an adopter without the
  playbook kit; (c) is a second spelling of the grammar with nothing comparing the two, against the
  charter's one-fact rule. Rung 3, the most capable surviving option: (a) meets every criterion and
  keeps the production one fact by comparison. RESOLVED (agent, 2026-10-25, delegated): (a).
  widens: none · relaxes: none
- **F2 — How is the slug and cadence collision closed?** (a) Reserve the slug `run` for the cadence
  family; (b) reserve the cadence names `build` and `unit`; (c) leave it. (b) is a literal list on the
  cadence segment, which the clause forbids; (c) lets a legal cadence name and a legal slug refuse each
  other at the remote. Rung 1, the clause's "never a literal list" on the cadence segment.
  RESOLVED (agent, 2026-10-25, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: §7's leg line gains `recall floor` and
  `recall floor arms`, the legs `memory/guides/UNATTENDED-STOPS.md` in Files touched trips.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.

## 10. Reuse audit

No existing seam fits the cadence segment at `c63aabbb`: no lease grammar exists, and
`python tools/codebase-map/reuse_lookup.py "validate a cadence name against the tag grammar instead of
a literal list"` ranked name-stem hits (`grammar`, `build_grammar`, `declared_list`, `check_rule_tags`)
and no segment validator in the unattended kit. The production reused is PLAY-dOrderedCharter-19 S1's
`seg`, read through its `parse_tag` for the parity check, with `RULE_KEY_RE`
(`tools/roles/roles_lib.py:65`) as the shape the shell spells; the predicate hooks
TOOL-dPlacedRequest-1's ref builder `derive_lease_ref`. Scout A's row cited `RULE_KEY_RE` at `:65`, which agreed with
source; its line carries an optional trailing `?` that a cadence segment does not take.

Recall terms used: `python tools/memory-recall/query.py "which names may a cadence run lease take"
--terms "cadence lease grammar tag grammar segment literal list maintain review period registered
name"`

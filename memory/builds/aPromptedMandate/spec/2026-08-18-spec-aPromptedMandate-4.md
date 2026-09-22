# TOOL-aPromptedMandate-4 — the two mode-scoped directives

**Status:** CLOSED · rev-3 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md](../reviews/2026-08-18-review-TOOL-aPromptedMandate-1-spec-audit.md) | spec-audit | TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 TOOL-aPromptedMandate-3 TOOL-aPromptedMandate-5 TOOL-aPromptedMandate-6 |
| [2026-08-18-review-TOOL-aPromptedMandate-1-tier2-diff.md](../reviews/2026-08-18-review-TOOL-aPromptedMandate-1-tier2-diff.md) | diff-review | TOOL-aPromptedMandate-1 TOOL-aPromptedMandate-2 TOOL-aPromptedMandate-3 TOOL-aPromptedMandate-5 TOOL-aPromptedMandate-6 |

<!-- /gen:spec-records -->

## 1. Goal

Bind a prose-started run to the research and solution-test obligations by name, through the directive
layer that already exists — and introduce the layer's first SCOPED member, because the owner ratified
that these bind prompt-mode runs and not slug-mode ones.

## 2. Scope (IN)

- **S1** — two handles join `DIRECTIVES_CORE`: `researched:M12` and `solution-tested:M12`.
- **S2** — each carries a SCOPE. The registry entry grows a third field, `<handle>:<section>:<scope>`,
  over the closed set `all` / `prompt`. An entry with no third field is `all`, so every existing
  handle keeps its meaning without edit.
- **S3** — `DIRECTIVES_FLOOR` moves from 11 to 13.
- **S4** — both rows join the Skill template's directive table, which leg check 16 joins to the
  registry in both directions; the table gains a column naming the scope.
- **S5** — the driver refuses `--waive researched` (or `solution-tested`) on a run whose mode is
  `slug`: the handle is out of scope for that run, and a waiver of a directive that does not bind is
  a record of a relaxation nobody needed.
- **S6** — protocol §10 states what a scoped directive is and that the scope is closed.
- **S7** — ONE splitter, applied at every site that decomposes a registry entry. Rev-1's consumer
  enumeration was wrong against source in both directions and is corrected in §4.

## 3. Non-goals (OUT)

- **Not a second registry.** The scope rides the existing entry, parsed by the existing splitter.
- **No scope other than `all` and `prompt`.** A per-project scope key was considered and cut: the
  conf may EXTEND the directive set and may not narrow the core, and a project-selectable scope is
  narrowing by another name.
- **The waiver semantics do not change.** A scoped directive is still waivable at preflight with a
  reason, still recorded as a parked entry of the `waiver` kind, still never a DoD override and never
  a gate removal. §10's existing paragraph covers all of that unchanged.

## 4. Design

### Data model

```
DIRECTIVES_CORE="minimal-prose:M10 … wrap-up-derived:M9 researched:M12:prompt solution-tested:M12:prompt"
```

The `directives()` composer is untouched. **The rev-1 consumer list was wrong in both directions**,
and a builder working from it ships a red leg. Corrected, against source:

| Site | Rev-1 said | Actually |
|---|---|---|
| the driver's `--waive` membership test | needs the scope reader | needs NOTHING — it is a prefix match on `*" $h:"*`, which a third field cannot disturb |
| leg check 16 **arm A** | (covered by "the both-way join") | builds `core` from WHOLE entries and `comm`s them against the two-field pairs the table awk emits, so `researched:M12:prompt` reds BOTH `only_reg` and `only_tbl` |
| leg check 16 **arm B** | not named at all | derives `sec=${pair#*:}`, yielding `M12:prompt`, and greps `^## M12:prompt` — a heading that cannot exist, so both new handles red |

Three fail branches fire on a correct implementation. **S7's splitter**, applied at arm A's `core`
construction, at arm B's section resolve, and nowhere else it is not needed:

```sh
handle=${e%%:*}; rest=${e#*:}; sec=${rest%%:*}
scope=${rest#*:}; [ "$scope" = "$sec" ] && scope=all
```

The two-field default falls out of the shortest-prefix/longest-prefix pair rather than being tested
for, which is why it cannot disagree with itself.

**The fourth arm must not red an adopter's extra table.** `DIRECTIVES_EXTRA_TABLE` rows are
project-authored, carry no scope column, and are a legal empty set for every adopter today. The
column-exists assertion therefore scopes to the KIT template's own rows; a project table's rows are
joined on handle and section alone, and that exemption is stated in the arm rather than discovered.

### The both-way join, and the vacuity risk

Leg check 16 has three arms today: every registry handle appears in the Skill table, every table row
appears in the registry, and every cited section exists in the build method. The scope adds a fourth:
the table's scope column equals the registry's. That arm is the one at risk of passing by finding
nothing — if the column is absent from the render, a naive comparison of two empty sets is green. The
arm therefore asserts the column EXISTS before comparing, in the shape the lexicon kit's `UNSELECTIVE`
guard and the playbook parity gate's anti-vacuity rule both use, and the arm for that arm is a
fixture whose render drops the column.

### When the scope refusal is evaluated

`check_waivers "$rel"` runs at `unattended.sh:1186`; the BASE blob unit 1 reads the mode from is not
fetched until `check_authorization` at :1200. At `check_waivers` the mode is unset for BOTH modes, so
a refusal keyed on "mode is slug" never fires and one keyed on "mode is not prompt" fires on
prompt-mode runs too. Neither AC5 nor AC6 is satisfiable there, and M2 makes the ordering a decision
some spec must state.

**The decision: the scope arm is evaluated after the authorization block**, in a second pass, for the
reason the existing block ordering already gives — the anchor is observed before anything that
consumes it, and the mode is a product of that observation. **An underivable mode is itself a
refusal**, not a pass: a waiver whose scope cannot be decided is exactly the reason-free relaxation
this layer exists to deny. Every precondition accumulates `status` with `|| true`, so moving the
check changes message ORDER and nothing else.

### Why scoped rather than unconditional

Put to the owner at kickoff and ratified: research and test bind a prose-started run only. A
slug-mode run's solution was chosen by whoever wrote the specs, and forcing a research pass over it
would make the directive a ceremony. The cost accepted is this unit's whole complexity — the layer's
first conditional member, and a scope field every later handle must consider.

### Files touched (estimate)

`tools/unattended/unattended.sh` (registry constant, the `--waive` scope refusal in its second pass;
NOT the membership test) · `tools/unattended/check-unattended.sh` (the S7 splitter at arms A and B,
plus check 16's fourth arm) · `tools/unattended/SKILL.template.md`
and `.claude/skills/unattended/SKILL.md` (the table) · `.unattended.conf` +
`.unattended.conf.example` (`DIRECTIVES_FLOOR`) · both protocol copies (§10) · both test suites.

## 5. Production-readiness checklist

- security — a waiver is a recorded relaxation; the scope narrows which run it can apply to, and
  narrowing is not a new grant
- perf / scale — N/A
- a11y / i18n — N/A
- error / empty / loading states — an unparseable third field is a named refusal, not a default to
  `all`; defaulting a malformed scope to the WIDER value would let a typo bind a run nobody meant
- observability — the run-state file records waivers already; the scope is derivable from the mode
  beside them
- risks — the fourth arm passing vacuously (§4, armed); a scope defaulting the wrong way (refused);
  the Skill render and the registry drifting (the both-way join is the arm)
- testing + left-shift gates — a driver arm per refusal branch, a leg arm per check-16 arm including
  the vacuity fixture, and `check-arms.py` counts the shell fail branches
- migration / rollback — every existing entry keeps its meaning by the two-field default
- user docs — the Skill table and protocol §10

## 6. Acceptance criteria

- **AC1** — When the Skill's directive table is rendered, it carries thirteen rows, and the two new
  ones name `M12` and scope `prompt`.
- **AC2** — When a handle is present in `DIRECTIVES_CORE` and absent from the Skill table (or the
  reverse), `check-unattended.sh` fails by name — the existing both-way join, still armed.
- **AC3** — When the rendered table's scope column disagrees with the registry, `check-unattended.sh`
  fails by name.
- **AC4** — When the rendered table drops the scope column entirely, `check-unattended.sh` fails
  rather than passing on two empty sets.
- **AC4b** — When the registry carries a three-field entry, `bash tools/unattended/check-unattended.sh`
  still resolves its `M12` section and does not report either new handle as absent from the table —
  arms A and B green over a correct implementation.
- **AC4c** — When a project declares a `DIRECTIVES_EXTRA_TABLE` whose rows carry no scope column,
  `bash tools/unattended/check-unattended.sh` exits 0. Measured: zero check-16 failures.
- **AC4d** — When the Skill's table and the registry disagree on any scope,
  `bash tools/unattended/check-unattended.sh` fails by name — ONE branch, because a changed scope
  cell puts the same handle in BOTH set differences and an only-in-table branch is unreachable
  alone.
- **AC5** — When `--preflight --waive researched --reason "<text>"` runs against a slug-mode build,
  the driver refuses BY NAME (the refusal text appears on stdout) and the run-state file is
  byte-unchanged. Both halves: rev-1 asserted only the second, which a driver that never evaluated
  the arm also satisfies.
- **AC5b** — When the mode cannot be derived at the point the scope arm runs,
  `bash tools/unattended/unattended.sh --preflight` refuses by name rather than accepting the waiver.
- **AC6** — When the same runs against a prompt-mode build, it is accepted and the waiver is recorded
  as a parked entry of the `waiver` kind.
- **AC7** — When `DIRECTIVES_CORE` is edited to drop a member, `check-unattended.sh` fails on
  `DIRECTIVES_FLOOR`.
- **AC8** — When `python tools/memory-tree/check-arms.py` runs, every new shell `fail` branch is
  armed.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/check-unattended.test.sh` ·
`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`python tools/memory-tree/check-arms.py` · `bash tools/check-testsuite-counts.sh` ·
`bash tools/run-gates.sh`

## 8. Open questions

none — the forks below are RESOLVED.

- **Scoped, unconditional, or project-declared** — RESOLVED (owner, 2026-08-18): scoped to
  prompt-authorized runs.
- **Where the scope is carried** — RESOLVED (agent, 2026-08-18): a third field on the existing
  registry entry, defaulting to `all`, per §3's one-registry rule.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-3 · 2026-08-18 · built. The both-ways scope join §4 specified collapsed to ONE branch on
  measurement: a single changed scope cell lands the same handle in both differences, so the second
  branch could never fire alone and its arm would have proved nothing — arm A already covers the
  handle set in both directions. The audit's predicted breakage was reproduced BEFORE the fix: fed
  three-field entries, arms A and B produced exactly four refusals over a correct implementation.
- rev-2 · 2026-08-18 · folded the M4 spec audit. §4's consumer enumeration was wrong in both
  directions — the `--waive` test needs no change and leg arms A and B both break on a three-field
  entry (ids 7, 30, 42); S7 and the splitter added. The evaluation ORDER of the scope refusal was
  unstated and made AC5/AC6 unsatisfiable (id 31). AC4b, AC4c, AC5b added.

## 10. Reuse audit

Satisfied for the SET in unit 1's §10. The seam extended is the `directives()` composer and leg check
16's both-way join in `tools/unattended/check-unattended.sh` — both already exist and both already
handle the two-field entry shape, so the scope is a field on an existing parse rather than a new
registry. The anti-vacuity shape in §4 is reused rather than invented: `tools/lexicon/lexicon.py`'s
`UNSELECTIVE` verdict and `tools/check-playbook-parity.sh`'s unresolvable-pair refusal are the two
existing implementations of "a comparison that matched nothing is a failure, not a pass", and the
`assertion-between-two-derived-values` and `fixture-passes-by-finding-nothing` gotcha classes are
both on this diff's checklist.

Rev-1 claimed both consumers "already handle the two-field entry shape". They do — that is precisely
why they break on a THREE-field one, and the claim was a stale reading rather than a verified one.
M5's staleness rule names this exactly: a hit can be stale, verify any claim about current code
against source. The rev-2 table in §4 is that verification.

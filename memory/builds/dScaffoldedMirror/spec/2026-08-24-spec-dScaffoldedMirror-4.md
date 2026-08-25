# TOOL-dScaffoldedMirror-4 — waiver keying and the mandatory reason

**Status:** DEFERRED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling · purpose is preparing TOOL-dScaffoldedMirror-9, which is itself deferred

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md](../build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md) | spec-audit | TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 |

<!-- /gen:spec-records -->

## 1. Goal

`load_waivers` (`lexicon.py:195-208`) does `s.split(None, 1)` and never validates the second field,
so a waiver row with no reason is accepted silently. P1's `Offender.text` is the bare identifier, so
one row waives that name in every file forever: re-derived at `af4de2d5`, 44 of 395 distinct
offender names span more than one file, covering 109 of the 463 occurrences. Re-key all three
registries to `path::name` and require a non-empty reason. This is a hard prerequisite for
`TOOL-dScaffoldedMirror-9`, which removes the pin and thereby makes the waiver the only remaining
dodge — all the pressure the pin used to leak lands on a file whose rows are currently unreasoned
and repo-wide.

## 2. Scope (IN)

- **S1** — the waiver key becomes `<repo-relative-path>::<name>` for all three registries.
  `load_waivers` returns `{(path, name): reason}` and the verdict loop matches on the pair, so a
  waiver covers one definition in one file.
- **S2** — a row whose reason is empty after stripping REDS, naming the file and the row. The
  refusal replaces the silent `parts[1] if len(parts) > 1 else ""` fallback.
- **S3** — a row that is not exactly `<path>::<name><whitespace><reason>` REDS, naming the row. A
  malformed key is a refusal rather than a key nothing will ever match.
- **S4** — `Offender.text` for P3 narrows from `f"{rel}->{target}"` to `target`. The path moves into
  the key, where it belongs; carrying it in both would spell the same fact twice and make the P3 key
  read `<path>::<path>-><target>`.
- **S5** — the three registry headers are rewritten. The existing header states the OLD design and
  its reason ("Keyed on the matched TEXT, not on `<path>:<line>`"); it must state the new one and
  why it is not the refused positional keying (§4).
- **S6** — a `drift-audit` watermark: `signal_lexicon_waiver_rows`, the total live row count across
  the three registries, `gateable: False`, seeded in `PINS` at its measured value. Its RATCHETS row
  uses the mechanism `TOOL-dScaffoldedMirror-5` owns, and that edge is new (§4).

## 3. Non-goals (OUT)

- **No line numbers, ever.** `TOOL-aLoosenedCeiling-5` refused `<path>:<line>` keying and the
  refusal stands. §4 states why `path::name` is not that design rather than assuming a reader will
  see it.
- **No reason GRAMMAR.** The rule is non-empty and nothing more. §4 says why a length or
  content-shape rule buys nothing.
- **No waiver-count ceiling that reds.** The watermark is `gateable: False`. A gateable row count is
  a pin on the escape hatch, and this build is about deleting pins rather than adding one.
- **No change to which definitions are offenders.** Every predicate grades what it grades today.
  Re-keying changes only which findings a row can excuse.
- **No migration tooling.** §4's inventory shows there is nothing to migrate.

## 4. Design

### Why `path::name` is not the keying `TOOL-aLoosenedCeiling-5` refused

A reviewer will read this unit as overturning a settled decision, and the objection deserves an
answer before it is raised. The record is two-sided: the backlog row for `TOOL-aLoosenedCeiling-5`
says `tools/install-prefix-waivers.txt` keys on `<path>:<line>`, so any insertion above a waived hit
unpins it silently — it unpinned the same two rows TWICE in one build — and it closes with "the
lexicon's waivers key on the matched TEXT for exactly this reason". The `Offender` docstring
(`lexicon.py:111-114`) says the same thing in the code.

The refused defect is POSITIONAL FRAGILITY. A line number is a coordinate the waived thing does not
control: adding an import at the top of a file moves every waived line in it, and the waiver reds a
merge that touched nothing it guards.

`path::name` carries no coordinate. Adding, deleting or reordering anything in the file leaves the
key matching, because the key names the definition rather than its position. The properties are
different in the exact dimension the refusal was about:

| | `<path>:<line>` | bare `<name>` | `<path>::<name>` |
|---|---|---|---|
| survives an edit above the waived site | no | yes | yes |
| covers one site | yes | no | yes |
| survives a rename of the waived definition | yes, wrongly | no | no |
| survives a move to another file | yes, wrongly | yes, wrongly | no |

The last two rows are the residual and are stated rather than argued away. A waiver whose subject is
renamed or moved stops matching, and the existing `STALE WAIVERS` refusal (`lexicon.py:526-529`)
names it out loud rather than passing silently. That is the correct behaviour: a waiver asserts
"this exception is deliberate, HERE", and a definition that moved to another file is no longer the
thing the reason described. The two rows where `<path>:<line>` scores "yes" are marked "wrongly" for
the same reason — it keeps excusing a site whose identity changed under it.

### The multiplicity this closes, measured

The research pass reports 46 of 395 distinct offender names spanning multiple files, covering 114 of
463 occurrences (24.6%). Re-derived through the kit's own extractor at `af4de2d5` the same predicate
gives 44 names over 109 occurrences (23.5%); the two differ by two names and the conclusion does not
move. The worst keys are concrete: `repo_root` and `git` each appear in five files, and
`do_selftest` in five kits' selftests. Under today's keying, one row reading `git it is a subcommand
namespace` waives all five, and a sixth arrival is waived before it is written.

### The reason, and what a stricter rule would buy

The rule is: non-empty after stripping. Nothing more, and the negative is worth writing down. A
minimum length is satisfied by padding. A required id is satisfied by citing an unrelated one. A
required sentence is satisfied by a sentence. Every content rule available here is satisfiable by an
author who did not want to write a reason, and each one adds a refusal that reds on an honest row.
What actually binds is that the row exists at all, that it names one site, and that `STALE WAIVERS`
deletes it when its subject goes.

### Inventory

Measured 2026-08-24 on this worktree: `lexicon-verb-waivers.txt`, `lexicon-suffix-waivers.txt` and
`lexicon-layer-waivers.txt` each carry ZERO non-comment rows. All three are comment-only headers. So
the key migration is EMPTY — there is no row in this repo to re-key, no compatibility window to hold
open, and no reader of an old key to keep working. That is the cheapest moment this change will ever
have, and it is the argument for doing it in Phase 0 rather than beside `-9` in Phase 4.

### The watermark, and the shape it borrows

`signal_lexicon_waiver_rows` counts live rows across the three registries and reports them with
`gateable: False`, exactly as `live_backlog_rows_per_shard` does. It seeds in `PINS` at 0, which is
the measured value. The point is not the number: it is that RAISING the watermark lands in
`RATCHETS` and therefore needs a reason written in place, so the first waiver this kit ever accepts
arrives with an explanation beside the count rather than only inside the registry.

The RATCHETS row itself uses the mechanism `TOOL-dScaffoldedMirror-5` defines, and this unit does
not restate that design. **The edge is new and is not in the build's declared set**: `-4` needs a
fourth `RATCHETS` row, and `-5` owns the shape. The row is declared here rather than there because
`-5`'s three rows are deleted by `-9` and this one is not; filing it with `-5` would put it in the
same delete.

`live` for this signal is `True` when all three registry files were readable, and `False` when any
was missing — an unreadable registry must print DEAD PROBE rather than a reassuring 0, which is the
same trap the count itself would otherwise walk into.

### Files touched (estimate)

`tools/lexicon/lexicon.py` (~40 lines: `load_waivers`'s parse and refusals, the verdict loop's key
construction, P3's `text`), the three `lexicon-*-waivers.txt` headers (S5),
`tools/lexicon/selftest.py` (the arms in §6), `tools/drift-audit/drift_report.py` and
`tools/drift-audit/drift_signals.py` (S6). No conf grammar change.

### Alternatives rejected

- **Keep the bare-name key and require the reason only.** It fixes the cheaper half and leaves the
  one that matters: under `-9` a single unreasoned-free row still covers 24% of the debt's
  occurrences by name.
- **Key on `path::name::line` for extra precision.** That is the refused design with two extra
  characters.
- **A separate per-predicate key shape.** P1 keys on a definition name, P2 on a type name, P3 on an
  import target; one `path::text` shape covers all three once S4 narrows P3's text, and three shapes
  would be three parsers for one file format.

## 5. Production-readiness checklist

- **security** — the registries are in-repo files edited by the same people who edit the code, so
  there is no new trust boundary. The parser splits once and never evaluates either field.
- **perf / scale** — three small file reads per run, unchanged in count. The key becomes a tuple
  rather than a string; the lookup stays a dict hit. No measurable change against the 0.44 s warm
  check.
- **a11y** — N/A, a CLI checker.
- **i18n** — N/A. Keys are repo paths and identifiers; a reason is free text and is never parsed.
- **error / empty / loading states** — the empty registry is the state this repo is in today and it
  stays legal: a kit demanding a waiver file could not be adopted into a clean tree, which is the
  existing docstring's rule and it survives. The new refusals are the empty reason and the malformed
  key.
- **observability** — the S6 watermark, plus the refusals naming the offending row rather than the
  file.
- **risks** — the interaction risk is with `-9`, not with this repo: `-9`'s assert D requires
  grandfathered ∩ waived = ∅, and that intersection is only computable once both sets use the same
  key. Landing `-4` after `-9` would make assert D compare a `path::name` set against a bare-name
  set, which is the two-answers-to-one-question class inside a security-shaped assert. The build
  order already puts this in Phase 0; the risk is that the order slips, and it is named here so that
  slipping is visible.
- **testing + left-shift gates** — five arms in `tools/lexicon/selftest.py` (§6). The class is
  `memory/gotchas/structured-record-split-on-whitespace.md`, of which the empty-reason fallback is a
  direct instance.
- **migration / rollback** — no migration: all three registries are empty (§4). Rollback is the
  revert, and it cannot strand a row because there is none.
- **user docs** — S5, the three registry headers, which are where a person writing a waiver actually
  reads the rule. `tools/lexicon/LEXICON.md`'s waiver paragraph moves with them.

## 6. Acceptance criteria

- **AC1** — When a waiver row carries a key and no reason, `python tools/lexicon/lexicon.py` exits 1
  and the message names the registry file and the row. Staged, because all three registries are
  empty today.
- **AC2** — When a waiver row reads `tools/a/x.py::enc deliberate` and the same name `enc` is an
  offender in `tools/b/y.py`, the run still reports the `tools/b/y.py` occurrence as unwaived.
  Asserted by a `selftest.py` arm over a two-file fixture.
- **AC3** — When a waiver row's key has no `::` separator, the run exits 1 naming that row rather
  than accepting a key that can never match.
- **AC4** — When a waived definition is renamed, `python tools/lexicon/lexicon.py` reports
  `STALE WAIVERS` naming the now-absent key, and exits 1.
- **AC5** — When lines are inserted ABOVE a waived definition and nothing else changes, the run is
  unchanged in output and exit code. This is the arm that distinguishes this keying from the one
  `TOOL-aLoosenedCeiling-5` refused, and it fails under `<path>:<line>` by construction.
- **AC6** — When `python tools/drift-audit/drift_report.py` runs, it reports
  `lexicon_waiver_rows` with a value of `0` and `gateable: False`; when a registry file is deleted,
  the same signal reports DEAD PROBE rather than 0.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `drift-audit
selftest`, `drift-audit records`, `memory hygiene`. Adds no new gate leg — S2 and S3 are new
refusals inside `lexicon naming predicates`, and S6 rides the existing `drift-audit records` leg.
The leg count is not the coverage.

## 8. Open questions

- **F1 — is `path::name` sufficient for a method, where two classes in one file may define the same
  method name?** Measured on this repo: no offender name collides within a single file, so the
  ambiguity has no live instance. The precise key would be `path::Class.method`, which the current
  extractor cannot produce because `_python_defs` walks with `ast.walk` and is scope-blind by
  construction. RECOMMENDATION: ship `path::name` now and let `TOOL-dScaffoldedMirror-11` widen it,
  since that unit replaces the walk with a scoped visitor emitting the qualifying scope and the key
  can gain a segment without changing its grammar. RESOLVED (agent, 2026-08-24, delegated):
  `path::name` now; the qualified form is `-11`'s to add, and the empty registries mean widening it
  later re-keys nothing.
- **F2 — does the reason field need to survive a `::` inside it?** The split is on the FIRST
  whitespace run, so a reason may contain anything including `::`; only the key is constrained.
  RECOMMENDATION: state it in the header rather than restricting it, because a reason that cannot
  quote a path is a reason that cannot cite its own evidence. RESOLVED (agent, 2026-08-24,
  delegated): unconstrained reason text, documented in the three headers under S5.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on recommendation R3 of the `dScaffoldedMirror`
  research pass (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`)
  and on the read-only probe of `incms/main` taken the same day. R3's third clause — "add the
  waiver-row count to `RATCHETS`" — is **narrowed here rather than taken as written**: a derived
  count has no authored scalar for `_scalar_at` (`drift_report.py:166-186`) to read, so what enters
  `RATCHETS` is the signal's PINS watermark, in the shape `live_backlog_rows_per_shard` already
  uses. Ratcheting the count itself would require authoring it beside the registries, which is the
  hand-kept-inventory class this kit is being repaired for.
- rev-1 status 2026-08-24 · DEFERRED with `-9`. Its standalone value is real but small - 40 lines against three EMPTY registries - and its stated purpose is preparing the pressure unit. It also carries an unreported fourth claim on the 463 offender count.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py waiver registry reason key path` returns `key`
(`tools/memory-tree/merge-rows.py`, fan-in 28, SEAM), `registry.toml [govkit]`,
`check-testsuite-counts.sh [testsuite-counts]` matched on `registry` and `waiv`, and `_resolve_cap
[memory-tree-hygiene]`. None is a seam this unit wires through. `merge-rows.py::key` is the highest
fan-in hit and it keys memory-tree backlog ROWS for a merge driver on an id grammar that has nothing
in common with a `path::name` pair. The genuinely related artifact is the one the map does not rank:
`tools/install-prefix-waivers.txt`, the sibling registry whose `<path>:<line>` keying
`TOOL-aLoosenedCeiling-5` refused — related as the design this unit must be shown NOT to be, which
§4's table does. The reusable seam that DOES apply is internal: `lexicon.py`'s existing
`STALE WAIVERS` scan already compares waiver keys against the keys the run observed, and it keeps
working unchanged once both sides are pairs. No new helper is introduced.

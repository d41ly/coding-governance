# TOOL-dBoundRoles-41 — the anchor check grades the text a work order authors, never the content it hands, by the block extents the render assembled

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 20 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-41-deviation-411.md](../build/2026-10-26-build-TOOL-dBoundRoles-41-deviation-411.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-41-deviation-412.md](../build/2026-10-26-build-TOOL-dBoundRoles-41-deviation-412.md) | deviation | — |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed finding **id 22 at
HIGH**, report item **H2**. Id 53 is the same defect at MEDIUM, report item M30, and takes its own scope
item in `TOOL-dBoundRoles-43`.

`TOOL-dBoundRoles-24` S3 runs `check_anchors` over the whole `## Task` section, and its S2 strips only
fenced blocks. Its claim of no false red was measured over `memory/builds/*/prompts/` at base, where
handed inputs are paths. After `TOOL-dBoundRoles-13`, specs, briefs and cards are handed as content
inside `## Task`. The skeptic's grep found 27 backticked `blob:`, `record:` and `cmd:` spans in six
tracked specs that fail `KEY_FORMS`, spec 13 and spec 24 among them, so the render refuses the builder
work order for unit 24, for unit 13, and for any spec that quotes the key grammar. Spec 24's Migration
line, that the first render after landing refuses nothing that rendered before, is false.

This unit hands `check_anchors` the task section with the content of every handed block left out, by the
extents `render_handoff` itself assembled, so only the text the work order authors is graded. It repairs
`TOOL-dBoundRoles-24` and builds one step after it (order 20).

## 2. Scope (IN)

- **S1** — Two texts from one assembly. `render_handoff` (`tools/roles/handoff.py:312`), where it builds
  the task section from its block list (`:381-416`), builds beside it the graded text: the same section
  with the content of every handed block left out and that block's `### <key>` heading and fact line
  kept. It is built from the parts the render appended, never by re-reading headings or fences in the
  composed bytes. Observed by AC1 and AC3.
- **S2** — What is handed and what is authored. A handed block is one whose content the render cut from
  a file or a record: the path inputs `spec` and `prompt` (`PATH_INPUTS`, `handoff.py:99`), the card's
  `task:` and `card:` values, the brief's `brief:` sections, every excerpt `TOOL-dBoundRoles-3` cuts, and
  the destination's work order handed under `input:work-order` by `TOOL-dBoundRoles-4`. Authored text is
  the opening, every charter block, every `### framing:` block, every upstream row, and the value of
  every typed `--input` that is not a path input. Observed by AC1 and AC2.
- **S3** — The call. `TOOL-dBoundRoles-24` S3's `check_anchors` call takes the graded text in place of
  the whole section, with `handed` unchanged. The marker still hashes the full section. Observed by AC1,
  AC2 and AC3.
- **S4** — The docs: `tools/roles/README.md`'s anchor paragraph (`TOOL-dBoundRoles-24` S5) names the text
  the check grades and the content it leaves out, and that a grammar span quoted in a typed `--input`
  value is graded, because that value is authored for the order. Observed by AC4.

## 3. Non-goals (OUT)

- `ANCHOR_RE`, `KEY_FORMS` and `check_anchors` themselves: `TOOL-dBoundRoles-24`'s, unchanged.
- The fence around handed content: `TOOL-dBoundRoles-38`'s. This unit does not lean on it, so a handed
  block the check must skip is skipped whether or not its fence parses.
- The corpus measurement re-taken over specs and briefs, and the render that hands spec 24 itself:
  `TOOL-dBoundRoles-43`'s item for id 53.
- The report's left-shift text as a general rule for every refusal predicate. S1's graded text is the
  regression for this one.

### Edges

- **consumes-from** `TOOL-dBoundRoles-24` — `check_anchors` and its call inside `render_handoff`, whose argument S3 narrows to the graded text (id 22)
- **hands-off** `TOOL-dBoundRoles-43` — the graded text, over whose population id 53's item re-measures the false-red rate and through which it renders a work order handing spec 24 itself (id 53)
- **consumes-from** `TOOL-dBoundRoles-45` — a typed value written raw, so S2's authored block and §4's graded block are the value itself, with no fence for unit 24's strip to remove (id 17 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-47` — the graded text, which unit 47's cross-unit case renders through (id 9 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-50` — AC3, whose baseline unit 50 restates; this unit's ledger answers AC3 AMENDED, naming unit 50 (ids 11 and 26 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-58` — the graded text, which unit 58 builds from one extents record, and AC3, which unit 58 bumps for unit 50's amended answer (ids 23 and 48 of the round-1 audit of units 45 to 51)

## 4. Design

### Evidence

- The skeptic re-ran the grep at the report's base: 27 backticked `(blob|record|cmd):` spans across six
  tracked specs, including `TOOL-dBoundRoles-13` (its S1 spells `blob:<path>@<blob12>:<lo>-<hi>`),
  `TOOL-dBoundRoles-24`, `PLAY-dOrderedCharter-9:51` (`cmd:<command>`) and `aEvidencedLens-3:223`
  (report, finding 22).
- `render_handoff` at base assembles the task as `"\n\n".join(["## Task", opening] + blocks)`
  (`tools/roles/handoff.py:416`) from a list it appended block by block (`:381-409`), so the render
  knows each block's extent without reading its own output.

### The graded text

```
task section   = ## Task, opening, block 1, block 2, …          hashed into the marker
graded text    = ## Task, opening, block 1', block 2', …       read by check_anchors
block'         = the block itself                when it is authored (S2)
               = its ### heading and fact line   when it is handed
```

### Why extents and not headings or fences

The skeptic judged the finder's two options unsound. Skipping to the next `### ` heading fails because a
handed spec holds its own `### ` subsections: spec 24's grammar spans sit under its own
`### What an anchor is`. Skipping only spans outside `handed` still refuses a well-formed example key that
is not in the handed set, such as spec 24 AC1's `blob:roles_lib.py@0123456789ab:1-4`. The render's own
parts carry no such ambiguity.

### What the check still sees, and does not

- A typed `--input` value is graded, so `TOOL-dBoundRoles-24` AC2's planted anchor in `--input question=`
  still refuses. A diff handed as `--input diff=` that quotes a grammar span refuses too; its remedy is to
  hand the file as `input:spec` or to fence the quotation.
- A handed block's heading and fact line are graded, and a fact line's key resolves by construction.

### Inventory

Minted: the graded text, a local of `render_handoff`. No new function; if the pass lifts the assembly
into one, its name is asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Migration

None: no stored data changes. `TOOL-dBoundRoles-24`'s Migration sentence holds after this unit for
every handed spec and brief.

### Rollout

Live at landing, at order 20. Dispatch sorts a tie by id string (`tools/workflows/unattended-build.js:608-613`),
so `TOOL-dBoundRoles-12` builds before this unit.

### Files touched (estimate)

- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`

### Alternatives rejected

- **Grade only the framing block.** `TOOL-dBoundRoles-24` §8 F1 discarded it: it keys the check to a
  block name two other units own and passes an anchor placed one block over.
- **Leave out every reads value, typed arguments included.** It passes an anchor to nothing planted in
  `--input question=`, which `TOOL-dBoundRoles-24` AC2 exists to refuse.

## 5. Production-readiness checklist

- security — no new write path; the render still refuses before its only write.
- perf / scale — one more string join per render.
- error / empty / loading states — a work order handing nothing grades the whole section, as before.
- observability — each refusal names the anchor span, as `TOOL-dBoundRoles-24` §4 gives.
- risks — an anchor written inside handed content is never graded; handed content is not the work
  order's to author, and `TOOL-dBoundRoles-13`'s re-cut keys it.
- testing — AC1 to AC4 by render and grep; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; the README changes by S4.

## 6. Acceptance criteria

- **AC1** — When the roles adopter fixture renders `handoff.py render --role gov-builder` with
  `--input spec=` naming a scratch spec whose prose, outside any fence, holds the backticked spans
  `cmd:<command>` and `blob:roles_lib.py@0123456789ab:1-4`, the render exits 0 and writes its prompt file.
  Red when: the render refuses a span inside the handed spec's content.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC2** — When the same render also passes `--input question=` holding a backticked `record:` anchor the
  order does not hand, it exits non-zero naming that anchor and writes no file.
  Red when: the graded text drops the typed argument, so an anchor to nothing in authored text passes.
- **AC3** — When the AC1 render's prompt file is compared with a render of the same inputs before this
  unit's change, its `## Task` bytes and its marker's task-sha are equal.
  Red when: building the graded text changes the hashed section.
- **AC4** — When `grep -n "graded" tools/roles/README.md` runs, it names the authored text and the handed
  content left out, on the anchor paragraph.
  Red when: the README still says the whole task section is graded.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `roles render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · a builder render handing a spec that quotes `cmd:<command>` and a well-formed example key in prose, staged by a `render_handoff` that passes the whole section to `check_anchors` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 24 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Is a typed `--input` value graded or left out?** Options: (a) graded, as the skeptic's corrected
  fix says ("only framing, upstream and typed-argument text is graded"); (b) left out with the other
  reads values. (b) fails `TOOL-dBoundRoles-24` AC2, a criterion already written; veto 1 discards it.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 26 unit specs, id 22
  (HIGH, item H2; id 53 shares the defect at MEDIUM, item M30), on the skeptic's corrected fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-45, -47 and -50, promotions of the round-1 audit of units 37 to 44; the -50 bullet names AC3's AMENDED answer. Nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.

## 10. Reuse audit

The seam is `render_handoff`'s own block list (`tools/roles/handoff.py:381-416`) and
`TOOL-dBoundRoles-24`'s `check_anchors` call inside it. `python tools/codebase-map/reuse_lookup.py "omit handed content from a check over a rendered prompt"`
ranked `check`, `checks`, `check_line` and `check_convention`, none an extent-aware scan, so no existing
seam fits beyond the render's list.

Recall terms used: `python tools/memory-recall/query.py "how is the prompt writer framing checked against the facts a work order hands" --terms "prompt writer framing anchor fact key handed content work order render_handoff trust witnessed"`

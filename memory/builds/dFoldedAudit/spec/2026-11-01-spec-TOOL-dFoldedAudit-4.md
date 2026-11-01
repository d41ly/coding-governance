# TOOL-dFoldedAudit-4 — a repair unit edits its unbuilt sibling's spec with a rev bump

**Status:** CLOSED · rev-3 · 2026-11-02 · node d · Tier-2 · base 74274869 · streams tooling · order 40

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-7-1-token-fold-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-7-1-token-fold-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 |
| [2026-11-02-build-TOOL-dFoldedAudit-4-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-4-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-fix-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-4-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-4-build-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-4-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-4-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Where a promoted unit corrects text in a sibling spec, the disposal rewrites the sibling's text
itself, with a rev bump and a §9 line naming the repair unit, instead of overriding it from outside.
A built sibling stays frozen, and a class gate keeps the old phrase from returning. This ends the
class the scout recorded, where a one-line correction to spec A became a unit B that overrode A's
text while A stayed wrong.

## 2. Scope (IN)

- **S1** — The prompt. Under `disposal: 'by-nature'` the disposal prompt orders the sibling edit, its
  rev bump and its §9 line, forbids the override from outside, and sends a correction to a terminal
  spec to a new unit. Observed by AC1 and AC4.
- **S2** — The return. `DISPOSAL_SCHEMA` declares `siblingEdits`, shaped `[{unit, rev}]` as [repair]
  fixes it, and the stage returns it under `by-nature`, `[]` when it edited none. It rides the hoist
  beside `dispositions` onto the hand-out, the DEGRADED return and the attended every-unit-terminal
  return. Observed by AC1 and AC3.
- **S3** — The sibling refusals. Under `by-nature` the reconciliation refuses a `siblingEdits` that is
  absent, malformed, at a rev not above the one the audit read, naming a unit outside the roster, or
  standing beside no promoted unit. Observed by AC3.
- **S4** — The frozen join. Under `by-nature` the reconciliation refuses a `siblingEdits` entry or a
  `local` entry of `dispositions` naming a terminal unit, read from `planState` by the `DONE` prefix
  the harness already matches, and refuses one naming a unit that carries no `planState`. Observed by
  AC2 and AC4.
- **S5** — The class gate. `scan_supersede` in `tools/check-spec-tokens.py` reds a live spec dated at or
  after `SPEC_SUPERSEDE_CUTOFF` that carries the phrase in its prose. Observed by AC5 and AC6.
- **S6** — The report and the waiver. Every run prints the join's line, on and off, and no waiver row
  can silence one of its hits. Observed by AC7.
- **S7** — The key. `.memory-tree.conf` declares `SPEC_SUPERSEDE_CUTOFF` with its reason and its value,
  which the build commit derives by the relation the sibling keys record. Observed by AC6.
- **S8** — The carriers of the join. The checker's docstring and the `spec-tokens` map dossier state
  the join and what it does not check. NOT OBSERVED: prose has no grader beyond its own legs.
- **S9** — The render. `tools/workflows/unattended-build.js` is regenerated from the template in the
  same commit. Observed by AC1.

## 3. Non-goals (OUT)

- A built sibling's spec. A correction to it is a new unit built on top, and nothing here edits one.
- Retiring, refolding or rewriting the specs that already carry the phrase. They are frozen history,
  and the cutoff exempts them.
- The disposal predicate, `dispositions` and the record order, which TOOL-dFoldedAudit-3 owns.
- The chain's folded set. This unit hands the list out, and the verdict reads it.
- `promote-all` and the undeclared path. Neither carries a sibling edit, and neither prompt changes.
- A §3 mirror. The prompt's existing rule at `unattended-build.template.js:2094-2096` stays its own
  thing and does not enter `siblingEdits`, because it records a new edge and corrects no text.
- A cutoff shared with the build's row rule. §4 "The key" says why the two are separate facts.
- Every prose carrier, M4's "by anything but that review's own fold" included.

### Edges

- **consumes-from** `TOOL-dFoldedAudit-3` — `disposal`, `dispositions`, `deriveDispositionFault`, `deriveReadRev` and the hoist; without them there is no by-nature prompt to extend, no reconciliation to join, and no rev the audit read.
- **hands-off** `TOOL-dFoldedAudit-5` — `siblingEdits` on the hand-out, which enters that round's folded set.
- **hands-off** `TOOL-dFoldedAudit-6` — the §9 line a sibling edit writes, naming the repair unit and the review record by its file stem.
- **hands-off** `TOOL-dFoldedAudit-1` — the sentence telling a caller to copy each unit's `planState` into the harness args, and M4's sentence gaining the disposal's sibling edit.
- **hands-off** external — the main loop re-derives the cutoff's value at landing, as the sibling keys' comments require, and a commit on a later day re-derives it again.

## 4. Design

### The sibling edit

[repair] places the edit in the DISPOSAL stage, which already holds authority over the whole spec set
(`unattended-build.template.js:2005-2008`) and already licenses one sibling edit, the §3 mirror
(`unattended-build.template.js:2094-2096`). Under `by-nature` this clause joins the prompt after the
placement sentences. The undeclared and `promote-all` prompts do not change.

```
WHERE A PROMOTED UNIT CORRECTS TEXT IN A SIBLING SPEC, REWRITE THE SIBLING'S TEXT ITSELF: bump that
spec's rev and add a section 9 line naming the repair unit and `<report stem>`. Do not state in the
repair spec that the sibling's text stands overridden. Only an UNBUILT sibling: a spec at CLOSED or
WONTDO stays frozen, a finding whose fix would change one is never folded there, and it is PROMOTED
to a new unit built on top, its `dispositions` entry reading `new-mechanism`. Return every spec so
edited in `siblingEdits` as {unit, rev}, and `siblingEdits: []` when you edited none. Every section 9
line this stage writes names `<report stem>`.
```

`<report stem>` is TOOL-dFoldedAudit-3's: the file name `lastReport` ends in, less `.md`. The §9 line
names both, because the citation is what TOOL-dFoldedAudit-6's predicate joins and the repair unit is
what [repair] requires. A §3 mirror's §9 line takes the stem too, or that predicate reports its rev
move.

A sibling edit is a fold for [chain] purposes. This unit carries the list out and does not merge it
into `dispositions`, because [repair] fixes its shape as `{unit, rev}` and an entry of `dispositions`
needs a finding id and a severity that list does not hold.

### The frozen join

This runtime cannot read a status. It holds one fact per unit: `planState`, which the caller copies
from `--plan --paths`, whose third TAB field is the state (`unattended.sh:5830-5838`). A terminal
unit reads `DONE` or `DONE (<grade>)` (`unattended.sh:6071`), so the harness matches the prefix, as
its own grading does at `unattended-build.template.js:2353`. That covers CLOSED and WONTDO alike.
[repair] names CLOSED, and a retired spec is as frozen as a landed one.

`planState` is required in attended mode only today (`unattended-build.template.js:172`). Under
`by-nature` a unit a return names must carry one, because an absent state would read as unbuilt, which
is the false-clean shape this file refuses by name. So the join refuses it rather than defaulting,
and the comment at line 172 says so. The refusal fires only on a unit the stage named, so a caller
that passes no `planState` and folds nothing is not touched. The entry-time state cannot go stale
inside the call, because the DISPOSAL stage runs before any unit is dispatched.

A spec this invocation authored reads `MISSING` at entry and is not terminal, so it passes.

The reconciliation rows extend the table in TOOL-dFoldedAudit-3 §4, inside `deriveDispositionFault`,
under `by-nature` only:

| # | Refused | Why |
|---|---|---|
| 11 | `siblingEdits` not an array | An absent list and a declared empty one are different answers. |
| 12 | an entry whose `unit` or `rev` is missing, or whose `rev` is not above `deriveReadRev(unit)` | A sibling edit is a rev bump. |
| 13 | an entry whose `unit` is not in `ordered` | A promoted unit's own spec is no sibling, and a stray names no spec of this build. |
| 14 | a non-empty list beside an empty `promotedIds` | A correction with no repair unit is a fold, and it belongs in `dispositions`. |
| 15 | an entry, or a `local` entry of `dispositions`, naming a unit with no `planState` | The state is the only fact here, and an absent one cannot read as unbuilt. |
| 16 | an entry, or a `local` entry of `dispositions`, naming a unit whose `planState` opens `DONE` | A built spec stays frozen. The reason names the unit and says a correction is a new unit on top. |

Row 16's reason is what an operator reads, so it spells `frozen`. `rev` is spelled
`{ type: 'integer', minimum: 1 }`, keeping the arm at `unattended-build.test.sh:1289` at its 3.

TOOL-dFoldedAudit-3's by-nature fixtures carry no `planState`, so rows 15 and 16 reach them. This
unit's pass adds `planState` to the fixture units those arms use, in the same commit.

### The class gate

**Home: `tools/check-spec-tokens.py`.** It is the join over a spec's text, it holds the cutoff
helpers, the date reader and the waiver pass, and it is a repo-root tool of this repo. The phrase is
this repo's own idiom, so the gate belongs where only this repo reads it. This is where
TOOL-dDerivedDocket-37 placed the hands-off join, for the same reason (§4 Alternatives rejected of
that spec).

`scan_supersede(root, specs, cutoff)` is the eleventh join. Over each live spec dated at or after the
cutoff it renders the text with fenced blocks blanked line for line, then blanks code spans with
`TICK` and double-quoted spans, and searches `superseded\s+by\s+name` ignoring case. The `\s+` is
what reads a phrase the house width wrapped. The blanking follows the precedent of §8's marks, where a
mark quoted in backticks or double quotes resolves nothing, so a spec may name the class it forbids.

The fence machine at `check-spec-tokens.py:1146-1154` is the join's second need of it, so it moves
into `render_unfenced(text)` and `scan_claims` calls that, with no change to its output.

A hit is `(f, "supersede", "supersede <- line <n>", SUPERSEDE_WHY)`. It joins `hits` for `--list` and
is exempt from the filter at `check-spec-tokens.py:1719`, so no row of
`memory/project/spec-token-waivers.txt` can silence it. [repair] says to exempt by cutoff and never by
list, and a waiver is a list.

The report line prints on every run and carries the text `live spec(s) ·`, which `--dispatch`'s
refusal diagnosis filters on, as the hands-off line's comment at `check-spec-tokens.py:1786-1790`
says:

```
spec-tokens: supersede join · <n> live spec(s) at/after SPEC_SUPERSEDE_CUTOFF <value> · <h> hit(s) · <c> pre-cutoff live spec(s) carry it and are not graded
```

Blank, it prints `SPEC_SUPERSEDE_CUTOFF blank (arm off)` with the same carrier count. So the day-one
zero cannot read as coverage.

### The predicate over the real tree

PINNED, measured at dccdeaa8 over every tracked spec, 2540 of them, with the §4 predicate before this
spec was written. The specs of this build were not on the tree at that measure, and each spells the
phrase inside backticks or double quotes, which the predicate blanks.

| Build | Filename date | Specs carrying it | Status |
|---|---|---|---|
| dLoggedFlight | 2026-09-13 | 2 | CLOSED |
| dWitnessedBar | 2026-10-25 | 4 | DEFERRED |
| dKeptSession | 2026-10-26 | 33 | DEFERRED |

So 39 specs carry it and none sits at or after the cutoff, and blanking moved no spec out of the
population. No live spec carries it, so the pre-cutoff count reads 0 today. A case-sensitive
single-line search finds 36 of the 39. The two dLoggedFlight specs open `Superseded by name` and
`TOOL-dWitnessedBar-94` wraps the phrase across two lines, so the case fold and the `\s+` each catch
a real instance.

### The key

`SPEC_SUPERSEDE_CUTOFF` joins `.memory-tree.conf` beside `SPEC_HANDOFF_CUTOFF`, read through
`read_cutoff_key` and asserted through `check_cutoff_relation`. The value is DERIVED at the build
commit: the day after the later of the newest spec filename date on any ref or live worktree and the
setting commit's own date. The reading on 2026-11-01 returns 2026-11-02 for a commit that day. It is
re-derived at landing, as `SPEC_HANDOFF_CUTOFF`'s comment records.

A `_CUTOFF` key owes no row in `tools/policy/legacy-homes.txt`, because `derive_legacy_homes` skips
`RETROFIT_KEY` (`policy.py:1125`, `policy.py:1213`). The shipped example conf is not touched, as
TOOL-dDerivedDocket-37 §8 F5 decided for its key, because an adopter does not receive this tool.

This is not [cutoff]'s key, `SPEC_FOLD_CUTOFF`. That one keys on the date a run was preflighted and
lives in `.unattended.conf`, and it answers which rule a run finishes under. This one keys on a spec's filename
date and answers which specs the join grades. The relation also forces this value strictly past its
setting commit. One date in two roles would be wrong for one of them.

### What the gate does not check

- A synonym. It reads one phrase, so "overridden here" or "reads as" pass. The class is the idiom this
  repo actually wrote, measured above.
- A DEFERRED or terminal spec. The join reads the live population, as `scan_handoffs` does, so a spec
  is graded while it is authored and frozen once it lands.
- A spec quoting the phrase in a code span or double quotes, on purpose.
- Whether a sibling was actually edited. That is the prompt and the `siblingEdits` return, and the
  rev move itself is what TOOL-dFoldedAudit-6 reads from the tree.
- `siblingEdits` beyond what the stage says. This runtime has no filesystem, as
  `unattended-build.template.js:836-840` states of `edges`.

### Inventory

| Minted | Cell | Grade |
|---|---|---|
| `scan_supersede` | `py.function` | `lexicon.py --suggest` answers OK |
| `render_unfenced` | `py.function` | `lexicon.py --suggest` answers OK |
| `SUPERSEDE_KEY`, `SUPERSEDE_WHY`, `SUPERSEDE_PHRASE` | module constants | beside `HANDOFF_KEY` and `HANDOFF_WHY` |
| `SPEC_SUPERSEDE_CUTOFF` | `.memory-tree.conf` key | `read_cutoff_key`, `check_cutoff_relation` |
| `siblingEdits` | schema key and hand-out key | `DISPOSAL_SCHEMA` |

### Rollout

The harness marker stays at the 1.13 TOOL-dFoldedAudit-3 moves it to. The join grades zero tracked
specs on the landing day, the state each of its sibling joins shipped in, and the fixtures are its
coverage until a spec is written on or after the value.

### Files touched (estimate)

`tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js`,
`tools/workflows/unattended-build.test.sh`, `tools/check-spec-tokens.py`,
`tools/check-spec-tokens.test.sh`, `.memory-tree.conf` and `memory/map/features/spec-tokens.md`.

### Alternatives rejected

- **The gate as an arm of hygiene check 12.** The engine is a copy-installed kit, so the arm would
  reach every memory-tree adopter's bar on upgrade, a shipped surface this unit did not price (M3 veto
  2), for a phrase measured only in this tree.
- **A list of exempt specs.** [repair] refuses it, and 39 rows of a shrink-only registry would pay for
  what one date states.
- **Grading every status, as the carries join does.** A DEFERRED spec is frozen text, and the row of
  37 specs above is why a live-only population costs nothing here. Past the cutoff a spec is graded
  while it is live.
- **The stage reports each unit's status in its return.** That is the same agent's claim as the edit.
  `planState` comes from the caller's `--plan` read, which reads the tree.
- **A `repair` field on `siblingEdits`.** [repair] fixes the shape, and the §9 line carries the repair
  unit where a reader of the spec finds it.
- **Merging sibling edits into `dispositions`.** An entry there needs a finding id and a severity, and
  a list of two keys does not hold them.

## 5. Production-readiness checklist

- security: no new write path. The stage already writes specs as `gov-spec-writer`, whose `spec` write
  class admits any spec (`scratch-guard.js:1097-1106`). The frozen join narrows what the stage's
  return may claim, and it is a refusal after the write, so a frozen spec a stage edited stays
  edited until the caller reverts it. The hand-out carries no roster on that path.
- perf / scale: the join reads each live spec dated past the cutoff once, at the cost of a regex over
  one file, inside a leg whose population is 37 live specs today.
- error / empty / loading states: an empty `siblingEdits` is the common case and is stated, never
  absent. A blank key prints the OFF line.
- observability: the report line prints on every run, and `siblingEdits` rides every return past the
  stage.
- risks: an unattended caller that omits `planState` meets rows 15 and 16 on its first fold, and
  TOOL-dFoldedAudit-1's carrier sentence is what prevents it. A future spec can reword around the
  phrase, which §4 states as a limit and which no phrase gate can close.
- testing: arms extend `tools/workflows/unattended-build.test.sh` and `tools/check-spec-tokens.test.sh`,
  one scratch repo per case on the second.
- migration: none. No landed spec moves, and the key gates forward only.
- user docs: N/A here. TOOL-dFoldedAudit-1 owns the prose.

## 6. Acceptance criteria

Cases 1 to 4 run `node disposal-fixture.js <case>`, the stub runner TOOL-dFoldedAudit-3 §6 defines, with
its fixture units carrying `planState: 'READY'`. Cases 5 to 7 run `python supersede-probe.py <case>`, a
probe the pass writes under the run's scratch, which loads `tools/check-spec-tokens.py` by path with
`importlib` and either calls `scan_supersede` directly or calls `main([])` from a fixture repository.

- **AC1** — When `node disposal-fixture.js sibling-unbuilt` runs `disposal: 'by-nature'` with one
  new-mechanism HIGH promoted to `A-tB-4` and `siblingEdits` naming `A-tB-1` at rev 2, the trace holds
  `disposal: done`, the RESULT carries `"siblingEdits":[{"unit":"A-tB-1","rev":2}]`, and the `dispose`
  prompt carries `REWRITE THE SIBLING'S TEXT ITSELF` and `naming the repair unit`.
  Red when: the return drops the list, or the prompt still leaves the correction in the repair spec.
- **AC2** — When `node disposal-fixture.js sibling-built` runs AC1 with `A-tB-1` at `planState: 'DONE'`
  and again at `planState: 'DONE (THIN)'`, each trace holds `disposal: NOT done` and `frozen`, the
  reason names `A-tB-1`, and the RESULT carries `"roster":[]`.
  Red when: the match tests `DONE` by equality and misses the graded form the driver prints.
- **AC3** — When `node disposal-fixture.js sibling-shape` runs AC1's return five ways, with
  `siblingEdits` absent, with `rev: 1`, naming `A-tB-4`, beside an empty `promotedIds`, and naming a
  unit with no `planState`, each trace holds `disposal: NOT done`.
  Red when: any of the five reaches the hand-out.
- **AC4** — When `node disposal-fixture.js fold-built` runs a `local` entry into a unit at
  `planState: 'DONE'`, the trace holds `disposal: NOT done` and `frozen`, and the `dispose` prompt
  carries `a new unit built on top`. Promoting the same finding to `A-tB-4` as `new-mechanism` holds
  `disposal: done`.
  Red when: only `siblingEdits` is joined, so a fold reaches a built spec through the other list.
- **AC5** — When `python supersede-probe.py scan` runs `scan_supersede` over fixture specs at the
  cutoff date, an OPEN spec with the phrase in prose returns one hit, and the same phrase wrapped
  across two lines returns one hit naming the first line. The phrase in a code span, in double quotes
  and in a fence returns none, and the same prose in a spec dated the day before returns none.
  Red when: a line-at-a-time search misses the wrap, or the blanking shifts the line number.
- **AC6** — When `python supersede-probe.py tree` runs the join's predicate over every tracked spec
  with the key in `.memory-tree.conf`, it prints at least 39 carriers before the date filter and 0
  hits after it.
  figure: 39 is PINNED at dccdeaa8 as a floor. The carriers are DERIVED at observation.
  Red when: the population reads 0, a filter that matched nothing, or a pre-cutoff spec is graded.
- **AC7** — When `python supersede-probe.py main` calls `main([])` in a fixture repository holding one
  hit and a waiver row naming its `supersede <- line <n>` token, the exit is 1 and the output holds
  `supersede join`. A blank key exits 0 and holds `SPEC_SUPERSEDE_CUTOFF blank (arm off)`.
  Red when: the waiver silences the hit, or the OFF state prints nothing.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `policy fixtures` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC3 · a sibling edit admitted, and its five malformed returns, the failing case the `siblingEdits` rows cut from `deriveDispositionFault`, which hands the roster out · none
New arm: tools/workflows/unattended-build.test.sh · covers AC2 AC4 · the frozen join over both lists, its failing case the `DONE` prefix test changed to equality, which admits `DONE (THIN)` · none
New arm: tools/check-spec-tokens.test.sh · covers AC5 AC7 · a scratch repo holding the phrase in prose, wrapped, quoted and fenced, its failing case the search run per line, which misses the wrap · `FLOOR_ASSERTIONS` raised by the arms added
New arm: tools/check-spec-tokens.test.sh · covers AC7 · a planted waiver row beside a hit, its failing case the exemption cut from the filter, which silences the hit · `FLOOR_ASSERTIONS` raised by the arms added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from `build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`
  tag [repair]. Its DERIVE, the gate's home, resolves to `tools/check-spec-tokens.py` with a key of its
  own, for the reasons §4 records.
- rev-2 · 2026-11-01 · §3 · M2's cross-read: the hand-off to `TOOL-dFoldedAudit-1` said "plan state"
  in prose where every other spec spells `planState`, and the hands-off join reads backticked
  tokens only, so no gate read that hand-off. The bullet now carries the token.
- rev-3 · 2026-11-01 · §7 · the fix brief's item 2. `memory/map/features/spec-tokens.md` under Files
  touched trips the guard `memory/`, which `recall floor` and `recall floor arms` both carry. §7
  already named the first, so the guards join's one hit was the second, and the leg line now names it.

## 10. Reuse audit

The seams extended are TOOL-dFoldedAudit-3's `deriveDispositionFault`, the existing `planState` DONE
match at `tools/workflows/unattended-build.template.js:2353`, and the join shape of `scan_handoffs` at
`tools/check-spec-tokens.py:777` with `read_cutoff_key` at `:732` and `check_cutoff_relation` at `:676`.
The fence machine at `:1146` is extracted rather than copied, because this is its second need.
`tools/codebase-map/reuse_lookup.py` over the phrase below ranked name-stem helpers and `read_spec_edges`,
and no seam that rewrites a sibling or grades a phrase, so no existing seam fits the phrase gate beyond
that join shape. `tools/memory-tree/gotchas.py --for-paths` selected
`fixture-passes-by-finding-nothing`, which AC6's population floor answers, and
`staged-break-substitutes-a-synthetic-value`, which is why AC5 uses the house wrap and not a planted
token. The recall probe surfaced the scout's Q3 class, the dKeptSession and dWitnessedBar carriers the
measure above confirms, and TOOL-dDerivedDocket-37's home decision. The hit and the source disagreed
in one place: the scout's grep reached 36 specs, and the predicate over the real tree found the three
§4 names.

Probe phrase: `a promoted repair unit rewrites its sibling spec instead of superseding it by name`.

Recall terms used: `python tools/memory-recall/query.py "where does a repair unit correct a sibling spec superseded by name and how is a frozen closed spec protected" --terms "sibling superseded-by-name repair unit rev-bump frozen CLOSED spec amendment hygiene class-gate deviation"`

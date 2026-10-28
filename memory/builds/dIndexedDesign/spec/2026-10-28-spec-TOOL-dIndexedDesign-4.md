# TOOL-dIndexedDesign-4 — reuse and alternatives backed by recorded probes: the §10 outcome joined to its scout record, each rejected candidate to its test

**Status:** OPEN · rev-3 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 11 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0386@1f72161f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md) | research | TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

A spec's reuse audit is prose that nothing checks against a probe, and its rejected candidates are
unchecked. Check 12's §10 arm asserts that one of five phrases is present before the terms marker
(`tools/memory-tree/check-memory-hygiene.sh:2705-2707`), and the template says it "cannot see whether
either fact is TRUE" (`memory/TEMPLATE-SPEC.md:318-322`). This is gap-design-05, 142 of 978 specs
citing no probe, and gap-design-06, 95 of 978 Tier-2 specs recording no rejected candidate
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:353-354`). The
clause asks for "reuse and alternatives backed by recorded probes". This unit gives §10 one
machine-read outcome line, joins it to the reuse scout's record of the probe that decided it, and
joins each `### Alternatives rejected` bullet to the test that rejected it. Check 12 grades the join
past a new cutoff.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: `read_spec_section` with the tags
`section.reuse-audit` and `section.design` (TOOL-dIndexedDesign-9, I1); `read_reuse_scouts(root,
slug)` widened to return each record's sections (TOOL-dIndexedDesign-13, I10), over the scout record
named `<date>-build-<unit id>-reuse-scout[-<x>].md` (TOOL-dLinkedLibrary-2 S6); `derive_owed_units`
in `tools/memory-tree/reuse_entries.py` (TOOL-dLinkedLibrary-1 S4); and the derived cutoff
TOOL-dLinkedLibrary-3 S2 puts on `hasP`, which this unit's later cutoff sits beyond.

The record this unit reads is the `record-kind.seams` kind unit 13 owns, and the spec is the
`record-kind.spec` kind unit 7 owns; this unit owns no node.

- **S1** — The one §10 reader, `read_spec_reuse(text)` in `tools/memory-tree/design_lib.py`, beside
  `read_spec_writes` and `read_spec_edges` (`tools/memory-tree/design_lib.py:528`, `:543`) (I11). It
  reads §10 through `read_spec_section(text, "section.reuse-audit")` and §4's
  `### Alternatives rejected` sub-head through `read_spec_section(text, "section.design")`. It returns
  a dict with `outcome`, `record`, `detail`, `legacy`, `alternatives` and `malformed`, per §4 "The
  grammar".
  - The outcome comes from one column-0 line in §10, `**Outcome:** <outcome>`, whose outcome is
    `seam <record path>`, `no existing seam fits <record path>` or `reuse-first <record path>`.
  - A §10 with no such line yields `legacy: True`. Its `outcome` is `no existing seam fits` when
    that exact phrase sits before the first terms marker, as check 12's probe blob is cut today
    (`:2700-2702`), and `None` otherwise.
  - Each bullet under the sub-head yields `(candidate, test, evidence)` from
    `- <candidate> — lost to <test> · <evidence>`. A bullet missing `lost to` or the ` · <evidence>`
    tail is listed in `malformed`.

  Observed by AC1.
- **S2** — The probe join, `check_spec_reuse(root, path, text)` in `design_lib.py`. It returns one
  finding per broken fact, each naming the spec and the fact:
  - no `**Outcome:**` line, or two of them;
  - a `seam` or `no existing seam fits` record that is not one of the `seams`-bound records
    `read_reuse_scouts(root, slug)` returns with parsed sections for the spec's own build, or whose
    ids do not hold the unit id the spec's H1 defines (`parse_spec_h1`,
    `tools/memory-tree/tree_lib.py:206`); a `research`-bound scout record carries no parsed sections
    and backs no outcome;
  - a `seam` outcome whose record's `matches` is empty, its `## Matches` reading `none`;
  - a `no existing seam fits` outcome whose record holds a match of `binding` `MUST`, which is an
    existing implementation new code would duplicate;
  - a `no existing seam fits` outcome whose record holds a `SHOULD` match whose `path` no
    alternative names as its candidate;
  - a `reuse-first` record that is untracked or does not spell `reuse-first`.

  Observed by AC2 and AC3.
- **S3** — The alternatives join, in the same function.
  - Each `malformed` bullet is a finding: a rejected candidate with no test.
  - Each `evidence` must resolve. A path must be tracked. A backticked command must name, as its
    first token ending `.py`, `.sh` or `.js` or holding a `/`, a tracked script.
  - Under `no existing seam fits`, the sub-head must hold at least one bullet. The one admitted
    absence is the bullet `- none — lost to only one mechanism exists · <evidence>`, M12's "Only one
    mechanism exists here", which owes evidence like any pick (`memory/guides/BUILD-METHOD.md:345-348`).

  Observed by AC4 and AC5.
- **S4** — The CLI, `python design_lib.py --reuse <cutoff> <spec>...`. It grades each named Tier-2
  spec whose filename date is on or after `<cutoff>` and passes over the rest. It prints each
  finding as `<spec> (§10 <fact>)` and a closing count line, and exits 1 on any finding. The usage
  line at `tools/memory-tree/design_lib.py:719` names the verb. Observed by AC6.
- **S5** — Check 12's §10 arm, past a new key `SPEC10_PROBE_CUTOFF`. The key is declared in
  `.memory-tree.conf` with its comment block and blank in `tools/memory-tree/.memory-tree.conf.example`.
  Its default sits beside `SPEC10_EVIDENCE_CUTOFF` (`tools/memory-tree/check-memory-hygiene.sh:108`).
  Blank means off, and a set value that is not a real ISO date is refused as the sibling keys are.
  - For a spec dated on or after the key, the outcome line answers the probe half in place of
    `hasP`'s phrase test, and the terms half (`hasT`) is graded as before.
  - One `"$_PY" "$HERE/design_lib.py" --reuse "$SPEC10_PROBE_CUTOFF" <specs>` call grades the
    selection, the way check 29 delegates to `gen_build_index.py` (`:1810`). Its lines join check
    12's findings.
  - A run that grades no spec past the key prints one announce line, as the evidence arm does
    (`:2930-2933`).
  - At landing the key is set to the day after the newest spec filename date on any ref, so no
    landed spec goes red.

  `tools/memory-tree/README.md` names the key. Observed by AC6 and AC7.
- **S6** — One reader for `reuse.propose`. `derive_owed_units` reads each spec's `outcome` through
  `read_spec_reuse`, so a spec owes a reuse entry under `new-seam` exactly when its outcome is
  `no existing seam fits`, the legacy phrase included. `reuse.propose` and check 12 then read one §10
  grammar. Observed by AC8.
- **S7** — The format. The §10 rules section of `tools/memory-tree/SPEC-TEMPLATE.template.md` (render
  `memory/TEMPLATE-SPEC.md:290-322`) states the `**Outcome:**` line, its three outcomes, the cutoff,
  what the join checks and what it cannot see. The recurring sub-head row (render
  `memory/TEMPLATE-SPEC.md:151-154`) gains the alternatives bullet grammar. Observed by AC9.

## 3. Non-goals (OUT)

- Re-deriving the scout's house index from the record's `**Index:**` sha. That is the seams' probe
  digest the executor re-derives at `design.seams` (TOOL-dIndexedDesign-13). This unit reads the
  committed record and trusts its sections.
- The scout's return grammar, its caps and its reader: TOOL-dIndexedDesign-13's.
- `check-recall.py`'s §10 reader (`tools/memory-recall/check-recall.py:447-497`). It reads the recall
  query and its terms, a different fact from the outcome, and stays as it is.
- Re-grading or rewriting any landed spec. The cutoff grandfathers them, and records are frozen.
- BUILD-METHOD M5 and M12. Their prose points at the template, so no carrier but TEMPLATE-SPEC moves.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-9` — `read_spec_section`, through which S1 finds §10 and §4 by tag in either tier's headings; without it the reader keys on the ordinal
- **consumes-from** `TOOL-dIndexedDesign-13` — `read_reuse_scouts`, widened to return each `seams` record's parsed `matches` and `unmet`, which S2 joins the outcome against; without it no record can back an outcome
- **consumes-from** external — dLinkedLibrary: the scout record's name and binding (TOOL-dLinkedLibrary-2 S6), `derive_owed_units` (TOOL-dLinkedLibrary-1 S4) and the derived cutoff on `hasP` (TOOL-dLinkedLibrary-3 S2)
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 32 and 46, each a scope item of that batch unit
- **hands-off** `TOOL-dIndexedDesign-40` — S5's `SPEC10_PROBE_CUTOFF`, which that unit's S3 writes blank in this unit's pass commit, armed only in this unit's fixture confs (id 2)

## 4. Design

### Evidence

- Check 12's probe half at base accepts `reuse_lookup`, `reuse-lookup`, `no existing seam`,
  `no seam fits` or `reuse-first` anywhere before the terms marker
  (`tools/memory-tree/check-memory-hygiene.sh:2705-2707`). TOOL-dLinkedLibrary-3 S2 drops the two
  lookup spellings past its derived cutoff and adds `-reuse-scout`. Neither form asks whether the
  cited thing exists or agrees.
- `### Alternatives rejected` is a recurring sub-head (`memory/TEMPLATE-SPEC.md:154`), and `git grep -n
  "Alternatives rejected" -- tools/` finds only the template source's two lines, so no reader exists.
- The phrase `no existing seam fits` is what `derive_owed_units` keys on (TOOL-dLinkedLibrary-1 S4).
  gap-design-05 measured the split this unit closes: the trigger's exact phrase in 236 specs, the
  hygiene check's three admitted phrasings in 302.
- Check 12 already delegates to Python (`:1363`, `:1810`, `:1851`) through `$_PY` and `$HERE`.

### The grammar

```
**Outcome:** seam <record path>
**Outcome:** no existing seam fits <record path>
**Outcome:** reuse-first <record path>

### Alternatives rejected
- <candidate> — lost to <test> · <record path, or a backticked command>
- none — lost to only one mechanism exists · <evidence>
```

`<record path>` is repo-relative. The line sits at column 0 anywhere in §10. The ` — ` is an em dash
between spaces, as `read_spec_edges` reads its bullets; a continuation line indented two spaces joins
its bullet.

| Key | Value |
|---|---|
| `outcome` | `seam`, `no existing seam fits`, `reuse-first`, or `None` |
| `record` | the cited path, or `None` |
| `detail` | the rest of the line, for a message |
| `legacy` | `True` when §10 holds no `**Outcome:**` line |
| `alternatives` | `[(candidate, test, evidence)]` in order |
| `malformed` | the bullet texts that do not parse, and a second outcome line |

### What the join cannot see

It proves the cited record exists, binds the unit and does not contradict the outcome. It does not
prove the scout searched well, that the evidence of an alternative shows what the bullet says, or
that a command still runs. A `seam` outcome is never compared with the code the unit later writes.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_spec_reuse`, `check_spec_reuse` | functions, `design_lib.py` | `py.function`, both answered OK by `lexicon.py --suggest` |
| `--reuse` | `design_lib.py` flag | none: the lexicon declares no flag cell |
| `SPEC10_PROBE_CUTOFF` | `.memory-tree.conf` key | none: the lexicon declares no conf cell |
| `**Outcome:**` | §10 line | none |

### Migration

None for landed specs: the cutoff sits past every one. `derive_owed_units` keeps its population,
because the legacy reading returns the same outcome the phrase search did.

### Rollout

Live behind the cutoff. The landing sets it to the day after the newest spec on any ref, and the
first spec written past it is graded.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1 to S4
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`: S5 and the arm §7 declares
- `.memory-tree.conf`, `tools/memory-tree/.memory-tree.conf.example`, `tools/memory-tree/README.md`: S5
- `tools/memory-tree/reuse_entries.py`: S6
- `tools/memory-tree/SPEC-TEMPLATE.template.md`, its render `memory/TEMPLATE-SPEC.md`: S7

### Alternatives rejected

- the join written in awk inside check 12 — lost to S6's reader count: `derive_owed_units` is Python, so an awk grammar is a second parser of the same line, the twin I1 must hold by a case table · `tools/memory-tree/check-memory-hygiene.sh`
- the join as a `check-spec-tokens.py` arm at spec-write — lost to the tie-break of M3, reuse of the seam M5 found: scout B's row and the template both place §10's grading in check 12's arm · `memory/builds/dIndexedDesign/build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md`
- re-running the scout's probe at grading time — lost to cost: one house index render per graded spec inside a bar leg, where `design.seams` already re-derives the digest once · `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`

## 5. Production-readiness checklist

- security — it reads tracked text only. Every git call is an argv list, and a cited path is
  resolved against `git ls-files` and never opened outside the tree.
- perf / scale — one Python process per hygiene run, one `read_reuse_scouts` call per build graded,
  and one `git ls-files` per run.
- error / empty / loading states — a spec with no §10 is check 12's existing red. An empty
  selection prints its announce line. A record that does not parse is a finding naming it.
- observability — each finding names the spec, the fact and the cited path.
- risks — a scout record serving several units is accepted for each. The join cannot tell which of
  its matches belongs to which unit, and the page says so.
- testing — fixture specs and records for each finding, red and green.
- migration — none; the cutoff grandfathers the corpus.
- user docs — the template's §10 section, S7; no `help/` page covers the spec format.

## 6. Acceptance criteria

- **AC1** — When a `python -c` call runs `design_lib.read_spec_reuse` over three planted spec texts,
  it returns three readings. The first, with `**Outcome:** seam <path>` and two bullets, returns that
  outcome, that path and two alternatives. The second, with no outcome line and the legacy phrase,
  returns `legacy` true and `no existing seam fits`. The third, holding a bullet without `lost to`,
  lists that bullet in `malformed`.
  Red when: the legacy phrase is missed, or a malformed bullet is read as an alternative.
- **AC2** — When `python design_lib.py --reuse 2026-01-01 <spec>` runs in a scratch repository whose
  planted spec's §10 cites no probe, it exits 1 with a line naming the missing outcome. It reds the
  same way when the outcome names a path that is no reuse scout record of the build, and when it
  names a record serving another unit.
  Red when: a §10 citing no recorded probe exits 0.
- **AC3** — When the same `--reuse` call runs over planted pairs, it reds a `no existing seam fits`
  outcome whose record holds a `MUST` match, and a `seam` outcome whose record reads `none`. It reds a
  `no existing seam fits` outcome whose record's `SHOULD` seam no alternative names, and it exits 0
  once a bullet names that seam.
  Red when: an outcome contradicting its record passes.
- **AC4** — When the same `--reuse` call runs over a planted spec whose `### Alternatives rejected`
  bullet reads `- a cache — slower`, it exits 1 naming a rejected candidate with no test. A bullet
  whose evidence names an untracked path is red too.
  Red when: a rejected candidate with no test, or with unresolvable evidence, passes.
- **AC5** — When the same `--reuse` call runs over a planted `no existing seam fits` spec with no
  `### Alternatives rejected` bullets, it exits 1. With the single
  `- none — lost to only one mechanism exists · <tracked path>` bullet, it exits 0.
  Red when: an empty sub-head passes under `no existing seam fits`.
- **AC6** — When `bash check-memory-hygiene.sh --only 12` runs in a scratch clone with
  `SPEC10_PROBE_CUTOFF` set and a planted Tier-2 spec past it whose §10 spells `no existing seam fits`
  with no outcome line, check 12 prints that spec with the `§10` finding. The same spec dated before
  the cutoff is not graded.
  Red when: a spec past the cutoff passes on the phrase alone.
  fixture: the scratch conf arms `SPEC10_EVIDENCE_CUTOFF` and `SPEC10_PROBE_CUTOFF`, because the
  probe arm sits inside the evidence arm's guard.
- **AC7** — When `bash check-memory-hygiene.sh --only 12` runs in a scratch clone with
  `SPEC10_PROBE_CUTOFF="2026-13-01"`, it refuses before grading and names the key. With the key blank,
  it grades as at base, and `grep -n SPEC10_PROBE_CUTOFF .memory-tree.conf.example` in
  `tools/memory-tree/` prints the blank declaration.
  Red when: an invalid date is read as off, or the example omits the key.
- **AC8** — When `python reuse_entries.py owed tFix` runs over a planted build of three units under
  `new-seam`, it prints the unit whose outcome line reads `no existing seam fits` and the unit whose
  legacy §10 spells the phrase. It does not print the unit whose outcome is `seam`.
  Red when: the two readers disagree on any of the three.
- **AC9** — When `grep -n "\*\*Outcome:\*\*" TEMPLATE-SPEC.md` runs in `memory/`, it finds the §10
  rules naming all three outcomes, and `grep -n "lost to" TEMPLATE-SPEC.md` finds the alternatives
  grammar.
  Red when: the render omits either grammar.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 AC4 AC5 AC6 AC7 · a scratch clone planting a §10 citing no probe and a rejected candidate with no test past `SPEC10_PROBE_CUTOFF`, staged by dropping the `--reuse` call from check 12 · none

## 8. Open questions

- **F1 — Where does the join run?** Options: (a) in awk inside check 12; (b) in `design_lib.py`,
  called once by check 12; (c) as a `check-spec-tokens.py` arm. (a) leaves two parsers of one line,
  because `derive_owed_units` is Python. (c) places §10's grading away from the arm the template and
  scout B name. RESOLVED (agent, 2026-10-28, delegated): (b), rung 3, the most feature-rich survivor,
  tie-broken by reuse of the seam M5 found. grants: PLAY-dClosedLoop-3 check 12's §10 arm and the
  §10 section of TEMPLATE-SPEC. widens: none · relaxes: none
- **F2 — What does `no existing seam fits` require of its record?** Options: (a) `## Matches` reads
  `none`; (b) no `MUST` line, any `SHOULD` admitted; (c) no `MUST` line, and each `SHOULD` seam named
  as a rejected candidate. (a) refuses a scout that found a seam worth weighing and the spec rightly
  turned down. (b) lets a weighed seam vanish from the record of choices. RESOLVED (agent, 2026-10-28,
  delegated): (c), rung 3, the most feature-rich option: it backs both the outcome and the
  alternatives by the same probe, which is the clause's text. widens: none · relaxes: none
- **F3 — How is the outcome spelled?** Options: (a) a column-0 `**Outcome:**` line; (b) the existing
  free phrases, kept; (c) a `### Outcome` sub-head. (b) is the split gap-design-05 measured. (c) adds a
  heading the section canon would have to admit. RESOLVED (agent, 2026-10-28, delegated): (a), rung
  3, the binding-line shape the spec already uses for `**Carries:**`, read by one line regex.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 4, gap-design-05 and gap-design-06,
  I11, I10 and scout B's row for this unit.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from edge of TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.
- rev-3 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-40, promoted by the round-1 spec audit of units 31 to 38; nothing else
  moved.

## 10. Reuse audit

The seams extended are check 12's §10 arm (`tools/memory-tree/check-memory-hygiene.sh:2680-2718`,
`hasP` at :2705-2707), its Python delegation precedent (`:1810`), and the spec readers
`read_spec_writes` and `read_spec_edges` (`tools/memory-tree/design_lib.py:528`, :543), each verified
at base. `python tools/codebase-map/reuse_lookup.py "check that a spec's reuse audit cites a recorded
probe and each rejected alternative names its losing test"` ranked name stems (`check`, `probe`,
`records`, `read_spec_revisions`). None reads a §10 outcome or an alternative, so no existing seam
fits the join, and S1 adds it beside the readers. Scout B cited the arm as :2680-2715; it closes at
:2718 at base. Scout B cited BUILD-METHOD M12 at :362-364; the render's M12 runs :335-362.

Recall terms used: `python tools/memory-recall/query.py "how is a spec's reuse audit checked against the probe it recorded and its rejected alternatives" --terms "reuse audit section 10 probe result no existing seam fits reuse-first alternatives rejected losing test scout record"`

# TOOL-aHonedRuleset-1 — prose census over the load-bearing governing documents

**Serves:** research TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6

**Commissions:** TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6

**Status:** INPROGRESS · Tier 1 · streams tooling+playbook · node a · 2026-09-04 · base `c4fcf5ad`

Every figure below is emitted by the script beside this file and none is typed here as a standing
claim:

```bash
python memory/builds/aHonedRuleset/build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py
```

If that output disagrees with a number quoted here, the output is right and this report is stale.
Section references (`§1`..`§5`) are its sections, not the charter's.

---

## The headline: five carriers are edit-locked, three of them within twelve bytes

`TOOL-dFoldedVerdict-7` recorded three carriers sitting on their declared ceilings in one build and
called it a pattern rather than a coincidence. It never enumerated the population. Measured (`§1`):

| carrier | free | ceiling written in |
|---|---|---|
| `AGENTS.md` | 6 B | `tools/template-size-limits.txt` |
| `coding-governance-agents.template.md` | 8 B | `tools/template-size-limits.txt` |
| `tools/memory-tree/BUILD-METHOD.template.md` | 12 B | **its own prose, gated nowhere** |
| `skills/session-kickoff/SKILL.md` | 207 B | `tools/template-size-limits.txt` |
| `memory/guides/UNATTENDED-PROTOCOL.md` | 6668 B (89.1%) | `GUIDE_CAP_BYTES` |

The first four cannot take a one-sentence addition. That is the finding that reframes this build:
prose optimization here is not tidiness, it is the precondition for any future rule landing in the
four documents that carry the most rules. The charter's own size gate already WARNs that the
template grew 766 B past its recorded high-water.

`BUILD-METHOD` is the interesting one. It declares `≤24 KB, ≤350 lines` in its own second paragraph,
states at its line 16 that **no gate enforces the pair**, and sits twelve bytes under it. It is a
real ceiling with no enforcement and no row in the registry, so it binds only whoever remembers to
read the paragraph. The census resolves it by reading the sentence rather than copying the number,
and reports it as `PROSE (ungated)`.

## What the two cheap theses were worth

**Divergence: refuted.** Every rendered guide is byte-identical to its template modulo `{{TOKEN}}`
substitution. `PROTOCOL`, `VERBS` and `PLAYBOOK-TEMPLATE` carry no placeholders at all, so the
template *is* the shipped document. Parity legs hold each pair, and an adopter-leakage probe over
all eight kit templates found no `coding-governance`-specific literal, id family, node tag or build
path. The templates already carry what an adopter needs; nothing here needs repatriating.

The practical consequence is a working rule, not a reassurance: **cuts are made in the template and
rendered down.** Hand-editing a copy under `memory/guides/` reds a parity leg and the edit is lost
at the next render.

**Adopter completeness, the other direction.** "Does the template carry everything the adopter
needs" was asked alongside divergence, and for these pairs it is structurally closed rather than
merely observed: the rendered copy is produced *from* the template, so no instruction can exist in
the rendered copy and be missing from the template. Byte-parity is what makes that an argument
instead of a spot check. `tools/check-placeholders.sh` reports a single marker carrier, so no
placeholder is left for an adopter to discover unfilled. The one genuine gap is by design, not by
omission — adopter-specific wiring lives in `WIRE-INTO-PROJECT.md`, which is a runbook and not a
rendered artifact, and is therefore the one document in this corpus where the completeness question
stays open to reading rather than to a gate.

**Copy-paste redundancy: refuted, and this is the load-bearing negative result.** Total verbatim
overlap across the whole authored corpus is **3870 bytes over sixteen pairs** (`§2`) — under one
percent. Deleting every duplicated passage in the corpus recovers about four kilobytes spread across
sixteen files, and recovers eight bytes in the charter, which is where the pressure is.

So the cheap strategy is dead. The redundancy that costs real bytes is **restatement in different
words**, which a shingle matcher cannot see and which the script's own header says it is blind to.
The cut list below therefore comes from reading, and each entry names the mechanism that makes the
prose removable rather than asserting that it reads long.

The overlap that does exist is mostly legitimate — the sealed task skeleton the checker emits, a
recall caveat, a stamp rule — with one exception worth a row of its own.

## Confirmed duplication, by name

- **The `last-audit` stamp rule has four copies in three files** — `skills/session-kickoff/SKILL.md:118`,
  `skills/session-kickoff/MANIFEST-TEMPLATE.md:29` and `:121`, `WIRE-INTO-PROJECT.md:437`. One rule,
  four carriers, one of them inside the file with 207 bytes free. The checker already owns the field
  set it sits next to (`--task-skeleton`); it does not own this.
- **The lexicon scoping rule** is stated in the charter `§12` and again in `tools/lexicon/SKILL.template.md`
  at 34 and 18 word runs. The charter block is already marked kit-conditional, so the SKILL is the
  natural single home.
- **The agent-cap environment rule** ("no environment override, a set `AGENT_CAP` is refused") sits in
  both `REVIEW-PROTOCOL.template.md:170` and `WIRE-INTO-PROJECT.md:559`.
- **`HYGIENE.template.md` states its whole cap table twice**, at lines 70–71 and again at 141–144,
  in different phrasing. Both describe the kit defaults; this repo's `.memory-tree.conf` overrides
  `INDEX_CAP_BYTES` to a different value than either passage names, so a reader who takes the prose
  for this tree's configuration is misled by both copies.

## Ranked cut list

Ranked by bytes recovered **in a carrier that has none to spare**. A recovery in a file with 36 KB
free is worth nothing and is not listed. Estimates are from reading and are marked as such; the
section weights they are drawn from are derived (`§5`).

**1 — the charter's micro-format grammar paragraph (`§16`, "The grammar, one statement"). Est. 900–1150 B.**
`tools/check-microformats.sh` grades the definition block against exactly this grammar with six
discriminating predicates and a pinned liveness sentinel. This is the charter's own "point at the
source, or gate the pair" rule, with the pair already gated. `§16` is the largest section in the file
at 8617 B, 17.5% of the whole template.
*The half that must survive:* the gate's own header says it holds the **syntax of the definitions**
and has no opinion on emissions. The pinned-glyph sentence and the R1 bare-list-item rule govern
emission and are not gated — cutting them is the `amendment-leaves-its-other-half-standing` class,
which is on this diff's checklist.

**2 — the kickoff engine's Step 5b exit enumeration. Est. 1200–1400 B, moved not deleted.**
`Step 5b` is 3395 B, the largest section in a file with 207 bytes free, and its six numbered
interactive exits are unattended-kit content living in the universal engine. The engine defers
everything else project-specific to the manifest. The natural home is
`tools/unattended/PROTOCOL.template.md`, which has 6668 B free.
*Coupling to check first:* the unattended kit already declares `KICKOFF_EXITS`, "a shrink-only floor
on how many interactive exits that engine resolves without an owner turn". A move changes where they
are counted, so that floor and its checker are part of the unit, not an afterthought.

**3 — the charter's `§8` agent-cap paragraph. Est. 300–400 B.**
It states that the marker spellings and the resolvable-bound grammar "are the hook's own, in
`tools/hooks/README.md`", then spends a third of its length on that grammar anyway. The pointer is
already written; the restatement behind it is the removable half. Note that five values in this
paragraph are machine-compared by `tools/check-playbook-parity.sh` — read its refusal before editing
here, because retyping one wrong reds the bar rather than drifting.

**4 — the four-copy stamp rule. Est. 250–400 B in the kickoff engine.**
Keep the copy in `MANIFEST-TEMPLATE.md` (the adopter fills it) and point the other three at it.

**5 — `HYGIENE.template.md`'s duplicated cap table. Est. 340 B, low urgency.**
The file has no ceiling at all, so this recovers nothing under pressure. It is listed because one of
the two passages will drift from the other and both already mislead about this tree's conf.

Not listed, deliberately: `WIRE-INTO-PROJECT.md` is the largest document measured at 69030 B and has
no ceiling anywhere. It is not on the cut list because nothing forces a cut there, and inventing a
ceiling for it is `TOOL-aScouredKit-23`'s question, not this census's.

## Proposed drops — an owner call, listed separately on purpose

Each of these removes a rule rather than a restatement. None is a cut this build should make on its
own judgment.

**D1 — the charter's `§0` TL;DR.** Roughly 1100 B that restates `§3`, `§5`, `§7`, `§8`, `§12` and
`§16` in the same file that states them. It is the corpus's clearest two-answers-to-one-question
instance and it is deliberate: a TL;DR is a summary, and a summary is a copy. *Against dropping it:*
a 49 KB ruleset with no entry point is read worse, and the last bullet ("when no rule below covers
it, decide by these") is not a summary of anything — it is the only statement of the residual rule
and would have to survive.

**D2 — moving the charter's `§11` OS-specific traps into the gotchas corpus.** They are
incident-shaped and `gotchas.py --for-diff` serves that shape exactly when relevant instead of on
every read. **I recommend against it,** and the objection is the charter's own `§10`: the recurring
classes are "the PROJECT's, derived from its own failures, never a generic list carried in from
somewhere else". The charter is a template for adopters; this repo's gotcha corpus does not ship to
them. Moving universal cross-OS hygiene into a per-project corpus deletes it for every adopter. It
is listed so the option is on the record as considered and refused, not so it gets done.

**D3 — `BUILD-METHOD`'s self-declared budget becomes a registry row, or goes away.** Today it is a
ceiling that binds by memory. Either make it a `tools/template-size-limits.txt` row, or delete the
paragraph and let `GUIDE_CAP_BYTES` govern. The status quo — a real constraint the file admits
nothing enforces — is the one option with no argument for it. Parked in the build README because it
touches the uncapped-set question that `TOOL-aScouredKit-23` owns.

## What this census does not establish

- It measured textual overlap and ceilings. It did not read all 420 KB, so the cut list is the
  product of targeted reading over the files under pressure and is not exhaustive.
- Section 4 lists 92 lines carrying a typed magnitude, across 15 files. That scan is deliberately
  over-inclusive — dates, versions and justified measurements all match it — and it is a candidate
  list, not a finding. Four of its hits became rows above; the rest are unadjudicated.
- No claim is made that a pair reported at zero shared bytes shares no meaning. That is precisely the
  blindness the method has.

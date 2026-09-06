<!-- gov:kit memory-tree@2.66 -->
# TEMPLATE-SPEC — the canonical spec / design-pass format (memory-tree kit)

Every spec file under `<MEMORY_ROOT>/builds/*/spec/` (at any depth — sub-spec folders are scanned
too) whose filename date is on or after this repo's `SPEC_FORMAT_CUTOFF` (`.memory-tree.conf`)
follows this shape. Machine-enforced by check 12 of `check-memory-hygiene.sh`: the status header
must parse; a Tier-2 spec must carry exactly the ten canonical `##` sections in order (§10 is
date-gated by `SPEC10_CUTOFF` — specs dated before it keep the NINE-section canon), with no
empty section bodies, its header `rev-N` logged in §9, and a resolved §8 before a terminal status;
both tiers must be free of skeleton placeholders. Specs dated before the cutoff are grandfathered
by filename date — never retrofit them.

## SPEC10_CUTOFF — how §10 is phased in

`§10 Reuse audit` is required only for specs whose FILENAME date is on or after `SPEC10_CUTOFF`,
DECLARED in `.memory-tree.conf` beside the three other cutoffs and shipped at `2026-08-04`. Specs
dated before it keep the nine-section canon, so adopting the reuse audit never retroactively reds
landed work. Raising it grandfathers more; lowering it is how you ratchet an existing corpus
forward. It is a merge-bar knob: changing it changes what the gate demands, so change it in a commit
that says why.

Unlike its three siblings, a BLANK declaration does not turn anything off — it resolves FORWARD to
the shipped date. Those three each switch a rule on or off, while this one SELECTS between two
section canons and the check must pick one for every spec it grades; an empty string compares
earlier than every date, so blank-means-off would silently demand the ten-section canon of every
grandfathered spec in the tree.

There is no environment override. There was one until `TOOL-aDeclaredBound-2`, and it was the only
one of the four cutoffs to have it: the read sat AFTER the conf was sourced, so a conf declaration
already won and the env form bought nothing except a second channel that leaves no diff behind.

## STREAMS_CUTOFF — the discipline is a header field, not a directory

The tree is flat: a build folder is `<MEMORY_ROOT>/builds/<slug>/` and carries no discipline segment.
Which discipline(s) a spec served is declared in its status header as `· streams <value>[+<value>]`,
over the CLOSED enum `.memory-tree.conf` declares as `DISCIPLINES`. The segment is validated whenever
present, on either tier. It is REQUIRED for specs whose FILENAME date is on or after
`STREAMS_CUTOFF`, which is set strictly ahead of the corpus at adoption so no landed spec is
retroactively red — and which means every spec written from that date onward must carry it.

## The records region (GENERATED — do not hand-edit, do not move)

A `<!-- gen:spec-records -->` pair sits between the status header and `## 1. Goal`, listing every
record whose `**Serves:**` line names this spec's id, with its kind and the other ids it also serves.
`gen_build_index.py --write` creates and fills it; `--check` never demands one, so a spec that has
not been rendered yet is legal and nothing has to be back-filled.

It is ABOVE the first numbered section deliberately. Check 12 collects `## ` headings for its
section-equality compare and this pair is not one, and its empty-body walk has not started there — so
the region needs no eleventh section, no new canon and no dated cutoff, and every landed spec can
carry it. A spec no record names renders an explicit empty line rather than an absent region, because
an absent region cannot be told from a spec nobody has recorded against.

## The status header (required, within the first 5 unfenced lines)

```
**Status:** <TOKEN> · rev-<N> · <YYYY-MM-DD> · node <tag> · Tier-<1|2> · base <sha8>[ · streams <v>[+<v>]][ · <pointer tail>]
```

- `TOKEN` is the shared status vocabulary (HYGIENE.md check 8), with these meanings ON a spec:
  `OPEN` drafting · `SPECCED` complete, awaiting owner scope approval · `BLOCKED` waiting on an
  external prereq · `INPROGRESS` approved, build underway · `DEFERRED` approved but parked ·
  `CLOSED` built and landed · `WONTDO` abandoned or superseded — the tail MUST then carry the
  successor id or a reason pointer (machine-checked).
- Update the header **in place** on every state change; the date is the last-change date.
- `rev-<N>` bumps on ANY material content change (review fold-ins included) and every rev gets a
  §9 line — §9 is the rev high-water a resumed session reads; the header rev being absent from §9
  is machine-checked. A pure status flip moves the date, not the rev.
- `base` is the immutable default-branch sha (8+ hex chars) the design was grounded against.
- `streams` names the discipline(s) this spec served, `+`-joined, each one a legal `DISCIPLINES`
  value. See the cutoff section above for when it becomes mandatory.
- The tail holds POINTERS and DECLARED VERBS only — a review workflow id, `ratified <date>`,
  `order <n>` — never prose.
- `order <n>` is the BUILD-ORDER verb: a positive integer, at most once, declaring this unit's step
  within its build. Units sharing a value are the parallel group; gaps are permitted, because a gap
  is how a retired unit leaves an order without renumbering the rest. It is PERMITTED, never
  required, so no landed spec goes retroactively red — and a malformed value is a REFUSAL rather
  than a silent misread: the generator anchors the verb on both sides and raises on anything that
  looks like it and does not conform. The build README's roster and its build-order region are both
  DERIVED from this field, which is why the order belongs on the spec and not in README prose.
- Fleet inventory (merged state only — unpushed specs on other nodes are invisible):
  `git grep -lE '^\*\*Status:\*\* (SPECCED|INPROGRESS)' -- '<MEMORY_ROOT>/builds/*/spec/'` lists
  every open spec; swap the token set to taste.

## Writing rules (LLM-optimized AND human-readable — both, always)

- One idea per sentence. Complete sentences, normal punctuation and spacing; hard-wrap ~100 cols.
- Brevity comes from **omitting** what doesn't change the build, never from compressing the
  survivors — no `·`-chains in prose, no parenthetical inventories (parens hold ≤3 items).
- Tables for enumerable facts (inventories, field maps, option menus); prose for reasoning;
  fenced blocks for commands, code, and schemas.
- Name things by repo identifier — a file path, flag key, decision id — never "the helper above".
- Number scope and acceptance items (`S1`, `S2`… / `AC1`, `AC2`…) so reviews and build summaries
  can cite them stably — and JOIN them: each scope item names the criterion that observes it, or says
  `NOT OBSERVED` and why. See the §2 body below; machine-checked from `SCOPE_JOIN_CUTOFF`.
- No narration, no restating the heading as its first sentence, no marketing adjectives.
- Verify every claim about existing code against source at writing time; mark the rest `UNVERIFIED`.
- A measured number a spec pins says whether it is PINNED or DERIVED. The rule above verifies at
  WRITING time, so a number true when written goes stale in place and nothing re-checks it: a pinned
  one names when it was measured, a derived one names what re-derives it. This binds every section,
  §4's inventories and estimates included; §6's `figure:` sub-field is where an acceptance criterion
  answers it.
- A section that genuinely doesn't apply keeps its heading with the single line `N/A — <why>`.
  Headings never disappear, and empty bodies are machine-rejected: an absent or hollow section is
  indistinguishable from a forgotten one.
- Sub-structure nests as `###` under the ten sections; no additional `##` headings, and no
  annotations on a `##` line (`## 4. Design (rev-2 …)` fails the gate — rev notes live in §9).

## Tier profiles, sub-specs, and where recurring content lives

- **Tier-2** uses the full ten-section skeleton below (§10 date-gated by `SPEC10_CUTOFF`).
- **Tier-1** (light profile): the status header + placeholder rules are enforced; the nine-section
  canon is not — keep it anyway when it helps, or write the few sections that matter. This is
  HYGIENE.md's "ceremony is conditional" applied to specs.
- **Multi-spec builds:** each sub-spec is its own conforming file (dated recording name, any depth
  under `spec/`); the master overview and the owner decision menu live in the build-root
  `README.md` (hygiene check 5 bans free-named files inside `spec/`).
- **One slug, two families:** a build that served two disciplines is ONE folder. Where two families'
  recordings would collide on a filename, the optional `-<FAMILY>-` qualifier separates them:
  `<date>-spec-<FAMILY>-<slug>-<seq>.md`.
- **Recurring §4 sub-heads** — use these names, don't invent synonyms: `### Data model` ·
  `### Inventory` (name every identifier the unit will MINT, and where this repo declares naming
  cells, name each one beside the cell that grades it) · `### Migration` · `### Rollout` ·
  `### Files touched (estimate)` · `### Alternatives rejected`.
- **Resolved forks:** mark each fork in §8 in place, naming the RESOLVER — `RESOLVED (owner,
  <date>): <pick>` for the owner's own decision, `RESOLVED (agent, <date>, delegated): <pick>` when a
  standing mandate delegated the resolver authority. Never sign as the owner for a decision the owner
  did not make; the two are indistinguishable afterwards otherwise. The mark is prose — the hygiene
  gate reads only §8's first non-blank line —
  and add the `ratified <date>` pointer to the header tail. §8 must read `none` or be fully
  RESOLVED before the status may go CLOSED/WONTDO (machine-checked).

## §3 Edges — what this unit takes, and what it leaves

Required on a Tier-2 spec whose FILENAME date is on or after `SPEC_EDGES_CUTOFF` (`.memory-tree.conf`;
blank turns it off). A `### Edges` sub-head inside `## 3. Non-goals (OUT)`, holding one bullet per
edge or the single word `none` — an absent declaration and a declared absence are different bytes.

```markdown
### Edges

- **consumes-from** `<unit-id>` — what this unit takes, and what breaks without it
- **hands-off** `<unit-id>` — what this unit leaves for that unit to do
- **consumes-from** external — the precondition this unit does not build
- **hands-off** external — the work this unit defers outside this build
```

Two verbs, one payload rule: a backticked unit id whose spec sits under the same
`builds/<slug>/spec/` prefix, or the bare token `external` followed by prose. The marker bytes are
ASCII on purpose — a multibyte dash crosses the writing tool, the shell and the gate's regex parser,
and only the last of the three has an opinion about encoding.

`order` is not an edge. It expresses SEQUENCE, and the defects this closes are edges: a criterion
resting on something the unit does not build. The measured case is one spec whose AC1, AC2, AC3 and
AC5 all rested on a verb the owner had cut from its scope; two of the four never spell the verb,
which is why an edge is DECLARED and not grepped.

**Three of the four arms are JOINS and are HELD under `--staged`**, with an announce line, because
there the selection is the staged set and one end of a correctly declared pair would report the other
as missing. The shape arm reads one file and stays live. A join whose target is outside the graded
population — a Tier-1 sibling, or a spec the cutoff grandfathered — is silent by design: absence is
not disagreement. And reciprocity proves the other author WROTE the line, never that their scope
covers the work; a rubber-stamped reciprocal passes, and it is worth having because writing the line
requires reading the handoff.

## §7 Gates — the shape the leg join reads, and where a new arm lives

`tools/check-spec-tokens.py` resolves a §7 gate name against `tools/gate-legs.json`, and
it reads only lines that ARE the list: a line carrying nothing but backticked names and `·` or `,`
separators. A line with a `- ` bullet marker, a prose prefix or a trailing clause is NOT read. Prose
may sit above or below that line freely.

The section is found by its HEADING TEXT, not by its number. A Tier-1 spec that drops the
production-readiness checklist slides every later section up one, so an ordinal read would grade
whatever sits seventh. A spec carrying no Gates heading at all is not graded; a Gates section at
another ordinal still is.

Only a NON-TERMINAL spec is graded. A landed record is frozen and this repo does not rewrite one to
clear a hit.

Once a spec's filename date reaches `SPEC_LEGLINE_CUTOFF` (`.memory-tree.conf`; blank turns it off),
a spec that DOES carry a Gates heading must carry such a line. From that date the shape is a
requirement rather than only a reading rule — and the heading precondition is the whole of the
Tier-1 accommodation, so the only spec this can red is one that wrote a Gates section and named no
leg in it.

**Where a new arm lives.** When a unit adds or moves a gate arm, §7 carries one line per arm:

```
New arm: <suite path> · <what stages its failing case> · <assertion floor to move, or none>
```

It is prose, it is not machine-graded, and it never satisfies the rule above — the `New arm:` prefix
is exactly what keeps it out of the leg join. A §7 carrying only an arm-home line still names no leg.

## §10 Reuse audit — the two facts, and what satisfies each

Required on a Tier-2 spec whose FILENAME date is on or after `SPEC10_EVIDENCE_CUTOFF`
(`.memory-tree.conf`; blank turns it off). Check 12 refuses the section naming whichever is absent.
It lives HERE rather than in the skeleton because the skeleton is COPIED, and a body explaining the
predicate necessarily contains the words that satisfy it.

- **The probe result** — one of: a `tools/codebase-map/reuse_lookup.py` citation naming the
  seam this unit extends; the phrase "no existing seam fits" with the evidence; or a named
  `reuse-first` waiver, where a run was granted one.
- **The recall terms you used**, on a line naming them (`Recall terms used: ...`, or the `--terms`
  invocation). Composing 8-14 terms in this corpus's own jargon is the expensive half of the probe,
  and BUILD-METHOD M7's regrounding step 5 re-runs the query FROM that line — a §10 without it makes
  that step resolve to nothing.

**RECORD THE PROBE RESULT BEFORE THE TERMS.** That order is the rule, not a style note: the probe
half is scanned over the section TRUNCATED AT THE FIRST TERMS MARKER, so a probe token written after
that marker is not seen. The ordinary one-line form — the finding, then the terms — satisfies both,
and so does a finding paragraph followed by a terms line.

Why the truncation exists: a terms list is 8-14 words of this corpus's own jargon and those words
routinely include `reuse-first` or `reuse_lookup`, so scanning the whole section let a terms line
alone satisfy BOTH arms and the probe half could not fail. Cutting only to end-of-LINE was tried and
leaked, because a terms list that WRAPS puts its tail on a line carrying no marker.

What it still cannot see, said plainly rather than left for a reader to discover: a section that
writes the terms VALUES first and the marker last puts those values in the probe blob, so one such
line can satisfy both arms. Nothing in this corpus is written that way and no gate catches it.

Before this arm existed the section was graded on presence and non-emptiness alone, which made
`N/A — none` a passing reuse audit. What the check still cannot see is whether either fact is TRUE:
a citation naming the wrong seam satisfies it. That liveness belongs to whatever observes that a
probe actually ran, which is outside this file.

## REV_SCOPE_CUTOFF — a revision entry names what it MOVED

Required on a spec of EITHER tier whose FILENAME date is on or after `REV_SCOPE_CUTOFF`
(`.memory-tree.conf`; blank turns it off). An entry is one rev line plus every non-blank line that
follows it, so a scope token may sit on a wrapped continuation and still counts.

```
- rev-<N> · <YYYY-MM-DD> · <scope> · <what moved>
```

`<scope>` is one or more `§<n>`, `S<n>` or `AC<n>` tokens, separated by spaces, commas or the `·`
this corpus already writes its status fields with. The separator is house style rather than grammar:
the gate reads PRESENCE. The field sits AFTER the date and never before it — `drift_report.py`
anchors its revision-log signal on the rev number followed by the date, so a scope field inserted
ahead of the date drops the entry out of that population.

**rev-1 is exempt.** A first draft moved the whole document, so a scope list on it names everything
and says nothing. Every entry numbered rev-2 or higher is graded.

**SHAPE ONLY.** The arm asserts an entry NAMES a section, a scope id or an acceptance id — never
that the fold actually touched what it names, exactly as the acceptance-witness arm grades a
backticked token and not the thing the token points at. What it buys is that a resumed session, or
the next round's folder, can re-read what a fold invalidated instead of re-reading the whole spec.

## The skeleton (copy everything below this line)

```markdown
# <FAMILY-slug-seq> — <title>

**Status:** OPEN · rev-1 · YYYY-MM-DD · node <tag> · Tier-<1|2> · base <sha8> · streams <value>

## 1. Goal

One or two sentences: the change and why it's worth building.

## 2. Scope (IN)

What this unit builds, as a bounded numbered list (S1, S2, …). Every item is verifiable at DoD.

Once a spec's filename date reaches `SCOPE_JOIN_CUTOFF` (`.memory-tree.conf`; blank turns it off),
every item here NAMES the acceptance criterion that observes it, spelled `AC` followed by digits —
or carries the marker `NOT OBSERVED` and the reason none does. One escape spelling and no synonyms:
a false red names its own remedy, a false pass is silent. An item is the column-0 bullet plus every
line beneath it, so listing the criteria as sub-bullets satisfies it. The arm is silent unless the
spec carries BOTH this heading and an Acceptance criteria heading, found by heading TEXT rather than
by number, so a Tier-1 spec that legitimately writes no acceptance section is untouched. SHAPE only:
it asserts the item names a label, never that the criterion so named actually observes it.

## 3. Non-goals (OUT)

The explicit cut-line: what an eager builder might include but must not. Name follow-ups.

### Edges

- **consumes-from** `<unit-id>` — what this unit takes, and what breaks without it
- **hands-off** `<unit-id>` — what this unit leaves for that unit to do

Or the single word `none`. Rules: the §3 section above this skeleton.

## 4. Design

The mechanism: data shapes, contracts, flows. Use the canonical ### sub-heads (Data model ·
Inventory · Migration · Rollout · Files touched (estimate) · Alternatives rejected) as needed.
Review corrections fold in here; bump the header rev and log it in §9.

## 5. Production-readiness checklist

The cross-cutting sweep, one line each (what's needed, or N/A — <why>):

- security
- perf / scale
- a11y
- i18n
- error / empty / loading states
- observability
- risks (concurrency, data-loss, rollback hazards)
- testing + left-shift gates
- migration / rollback
- user docs

For Tier-2, unresolved items become the owner scope menu.

## 6. Acceptance criteria

Numbered (AC1, AC2, …). Phrase each as "When <action>, <observable result>" — an observation that
proves THIS change works: a test it adds, a gate it moves, a browser observation. Never an
unrelated green gate.

Once a unit is BUILT, each criterion here is answered by a line in that unit's acceptance ledger — the grammar is `HYGIENE.md`, "Acceptance ledger", and it is not restated here. Numbering the criteria is what makes that answerable.

Once a spec's filename date reaches `SPEC_WITNESS_CUTOFF` (`.memory-tree.conf`), every acceptance
bullet must carry at least one **backticked token** — the command, file, flag or test that makes the
observation. The gate reads SHAPE only: it asserts the bullet names something, never that the named
thing exists or that the build satisfied it. The label may be written `- **AC1** — `, `- AC1. ` or
`**AC1** `; the rule does not care which, and does not require the bold.

Once a spec's filename date reaches `SPEC_FAILURE_MODE_CUTOFF` (`.memory-tree.conf`; blank turns it
off), every numbered criterion also names the BREAK that would turn it red, in a clause marked
`Red when:`. The clause may sit on the bullet's opening line or on any continuation line beneath it,
which is the latitude the witness rule already grants and matches this corpus's wrap style. There is
no `N/A` and no second form: a criterion whose break is merely its own negation costs one clause to
write, and an author discovering that the negation is all there is has found something.

```markdown
- **AC1** — When `check-memory-hygiene.sh` runs over the fixture tree, it names `tFixture-120`.
  Red when: the fixture carries no clause and the arm stays silent.
```

A criterion that cannot be observed for free, by this run, or against today's tree says so with the
criterion instead of leaving the next session to discover it. Four things go unsaid and get paid for
in build-time amendments. Declare whichever of them apply as named lines under the criterion's own
bullet:

- `cost:` — what the observation costs, when it is not seconds.
- `permission:` — the suite, boundary or credential that observes it is one THIS run may not execute.
- `fixture:` — the live instance or path the observation needs, and whether the tree holds one today.
  A criterion observing a gate arm names every cutoff key its fixture conf arms: an arm sitting
  inside a second key's guard is graded by nobody when that second key is blank, and the fixture
  that arms both cannot tell you so.
- `figure:` — whether a number the criterion states is DERIVED at observation time or PINNED as a
  literal. The writing rule on measured numbers states the obligation; this field is where a
  criterion answers it.

Write only the fields that apply and OMIT the rest. A field written as `none` is a blank being
filled rather than a question being answered, and a criterion whose preconditions are all trivial
carries no fields at all — the common case. Nothing grades these lines.

## 7. Gates

The named gate legs this unit must keep green, plus any new gate it adds. Put the names on a
line of their own carrying nothing but backticked names and separators — that line is what the
leg join reads, and from `SPEC_LEGLINE_CUTOFF` onward a spec with this heading must have one.
Add `New arm: <suite path> · <what stages its failing case> · <floor to move, or none>` per arm
this unit adds or moves. The rules are the §7 section above this skeleton.

## 8. Open questions

One fork per bullet or ### sub-head; options and tradeoffs may span lines. Each fork carries a
recommendation. When resolved, mark it in place: RESOLVED (owner, <date>): <pick>, or
RESOLVED (agent, <date>, delegated): <pick> under a mandate. Write `none`
when clear.

**The mark is a SHAPE a machine reads.** Two readers grade it — the
hygiene gate for a spec at a terminal status, and the planning verb for a live build — and both
require the word followed by a parenthesised attribution whose first field is `owner` or `agent`,
whose second is a date, and whose optional third is `delegated`. Anything else is prose: a bare
`RESOLVED:` resolves nothing, and neither does a resolver name outside that pair.

The mark may sit ANYWHERE in the section — an item's opening line or any continuation line, and it
may WRAP across a line break, which is this corpus's house style at its width. What the readers grade
is the section as one whitespace-squeezed string: a section carrying items and no conforming mark
anywhere is unresolved, and a first line that merely CONTAINS the word no longer resolves it. A §8
with neither an item nor a `none` form is a refusal, not a pass.

**What they do NOT grade, stated because the obvious tightening is wrong here.** They do not grade
PER ITEM. That needs a fork bullet to be distinguishable from an OPTION bullet, and this corpus does
not distinguish them — measured: of 287 §8 bullets, 69 carry descriptive labels, and among those are
both resolved forks and genuinely open ones. So a label-shape discriminator UNDER-counts and lets a
real open fork pass, which is worse than the over-counting it would replace; the over-counting was
measured too, calling a RESOLVED fork unresolved on a live tracked spec whose three option bullets
each demanded their own mark. The consequence to know: an unresolved fork sitting below an honest
`none` opening line is NOT detectable, and is pinned as a gap in both readers' fixtures rather than
implied away. Closing it needs §8 to have a regular shape, which is a scope change.

A fork that a stated PROBE decides, rather than a judgment call, may carry `FACT-QUESTION · ` at the
head of its bolded label, before the fork id. The prefix is transparent to resolution: it never marks
an item resolved and never suppresses a mark on the same item.

## 9. Revision log

- rev-1 · YYYY-MM-DD · initial draft.
- rev-2 · YYYY-MM-DD · §4 · AC3 · folded review wf_<id> corrections.   <!-- example shape -->

## 10. Reuse audit

Two facts, and check 12 refuses this section naming whichever is absent, for any Tier-2 spec dated
at or after `SPEC10_EVIDENCE_CUTOFF`. **What each is, and what satisfies it, is the section ABOVE
this skeleton — deliberately, and the reason is worth one line: every word that satisfies this
predicate is a word an explanation would have to contain, so an instructional body sitting inside
the copyable skeleton passes the gate on its boilerplate alone and an author who never fills the
section is never told. Read the rules there; write your own findings here.**

REPLACE both bullets. Delete this paragraph.

- The seam, by path, or that none fits, with the evidence.
- The retrieval arguments you actually passed, verbatim, so the next session can re-run them.
```

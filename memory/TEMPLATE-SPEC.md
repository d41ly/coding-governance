<!-- gov:kit memory-tree@2.48 -->
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
  can cite them stably.
- No narration, no restating the heading as its first sentence, no marketing adjectives.
- Verify every claim about existing code against source at writing time; mark the rest `UNVERIFIED`.
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
  `### Inventory` · `### Migration` · `### Rollout` · `### Files touched (estimate)` ·
  `### Alternatives rejected`.
- **Resolved forks:** mark each fork in §8 in place, naming the RESOLVER — `RESOLVED (owner,
  <date>): <pick>` for the owner's own decision, `RESOLVED (agent, <date>, delegated): <pick>` when a
  standing mandate delegated the resolver authority. Never sign as the owner for a decision the owner
  did not make; the two are indistinguishable afterwards otherwise. The mark is prose — the hygiene
  gate reads only §8's first non-blank line —
  and add the `ratified <date>` pointer to the header tail. §8 must read `none` or be fully
  RESOLVED before the status may go CLOSED/WONTDO (machine-checked).

## The skeleton (copy everything below this line)

```markdown
# <FAMILY-slug-seq> — <title>

**Status:** OPEN · rev-1 · YYYY-MM-DD · node <tag> · Tier-<1|2> · base <sha8> · streams <value>

## 1. Goal

One or two sentences: the change and why it's worth building.

## 2. Scope (IN)

What this unit builds, as a bounded numbered list (S1, S2, …). Every item is verifiable at DoD.

## 3. Non-goals (OUT)

The explicit cut-line: what an eager builder might include but must not. Name follow-ups.

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

## 7. Gates

The named gate legs this unit must keep green, plus any new gate it adds.

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
- rev-2 · YYYY-MM-DD · folded review wf_<id> corrections.   <!-- example shape -->

## 10. Reuse audit

The reuse-discovery result: the existing seam this unit wires through (from a
`tools/codebase-map/reuse_lookup.py` pass), or an explicit "no existing seam fits" with the evidence.
Records the reuse decision so an author cannot silently skip it — the machinery already ships in
this kit, and a checklist item nobody is asked to answer is not a checklist item.
```

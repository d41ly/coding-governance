# TOOL-aHonedRuleset-4 — the charter's agent-cap bullet keeps its pointer and drops the restatement

**Status:** SPECCED · rev-4 · 2026-09-04 · node a · Tier-2 · base 102e98f0 · streams tooling+playbook · order 3 · ratified 2026-09-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |
| [2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md) | spec-audit | TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-5 TOOL-aHonedRuleset-6 |

<!-- /gen:spec-records -->

## 1. Goal

The `§8` agent-cap bullet in `coding-governance-agents.template.md` already states that the marker
spellings and the full resolvable-bound grammar belong to `tools/hooks/README.md`, and then restates
that grammar behind its own pointer. Two neighbouring `§8` bullets then restate the enforcement
location a third and fourth time. Delete the restatement, fold those two bullets into one, and keep
the two rules, the parity-pinned values and the pointer, recovering 533 measured bytes. The file had
8 bytes free at base `102e98f0`; `TOOL-aHonedRuleset-2` is `order 1` on the same carrier, so this
unit starts from whatever headroom that unit leaves rather than from the base figure.

The same pass corrects the wrong array-literal sentence on both of its carriers, closing the OPEN
backlog row `TOOL-dFramedEntrypoint-1`.

## 2. Scope (IN)

- **S1** — Rewrite the bullet occupying `coding-governance-agents.template.md:230-245` so the
  surviving text carries only: the two-rules sentence, the gloss separating the two bounds, the
  rate-limiter rationale, the CONSOLIDATE rule, the route-through instruction, the fact that
  enforcement happens at the tool call on the exact matcher pair, the parity sentence, and the
  pointer at `tools/hooks/README.md`.
- **S2** — Every one of the five phrases `tools/check-playbook-parity.sh` extracts from this bullet
  survives verbatim, each intact on a single line, because the gate's extractions are `sed`
  substitutions applied line by line and a phrase split across a wrap resolves to nothing.
- **S3** — Re-render this repo's own charter in the same commit with
  `bash tools/playbook/adopt-playbook.sh --target .`, because `AGENTS.md` carries the same bullet
  from a rendered region and the `playbook render wiring` leg compares it against a fresh render.
- **S4** — The text `at most 5 verify agents TOTAL` stays live in the tree, because
  `tools/agent-cap-restatement-waivers.txt` keys a waiver row on exactly that string and the gate
  reds on a row whose text matches nothing.
- **S5** — The array-literal clause in the charter stops asserting a bare `passes unmarked`
  exemption. It is rewritten to say the literal is a receiver the hook can size, which is what
  `tools/hooks/agent-cap.js` actually applies and what the README's own `What the hook DENIES`
  section already describes as one of the three ways a receiver branch qualifies.
- **S6** — `memory/guides/SESSION-KICKOFF.md` gets its `last-audit` re-stamp in the same commit,
  because `coding-governance-agents.template.md` is a watched pathspec on line 6 of that file and
  `.githooks/pre-commit:53-55` runs `manifest-check.sh --staged` unconditionally. Its staged arm at
  `skills/session-kickoff/manifest-check.sh:412-421` fails check 5 whenever a watched file is staged
  and the staged manifest's block stamp still equals HEAD's, so the bundle is the only green path
  through a blocking pre-commit. The §B claims those two files feed are re-verified before the
  re-stamp; this is unit 5's S8 mechanism applied to this unit's own watched carrier.
- **S7** — The two neighbouring `§8` bullets at `coding-governance-agents.template.md:251` and
  `:252` collapse into one. What survives is the restricted-runtime fact, the instruction to inline
  the schema discipline as a snippet, the fact that a sidechain agent holds NEITHER tool so the
  capability is ABSENT rather than policed, that it inherits the governing doc and that hooks fire in
  it, and the reason the cap sits at the main loop. What goes is their third and fourth statement of
  the enforcement location, which S1's surviving text already carries once. The `PreToolUse`
  parenthetical goes with them: `tools/hooks/README.md:3` and `memory/guides/REVIEW-PROTOCOL.md:98-102`
  both hold that mechanism, so this is a restatement dropped and not a fact deleted.
- **S8** — `tools/hooks/README.md:117` is corrected to the same fact S5 states. The sentence today
  reads `An array LITERAL of ≤5 elements — the finder-lens fan — passes unmarked and needs no
  helper.`, which asserts a blanket exemption; the allowance the hook applies is a property of the
  RECEIVER of an `agent(` fan, and a raw `parallel([...])` over five literal elements is still denied.
  This is ONE correction written into the two files that carry it, not two mechanisms: both sentences
  are copies of a single wrong claim about `tools/hooks/agent-cap.js`, and correcting one carrier
  while leaving the other is the `amendment-leaves-its-other-half-standing` class this build audits.
  That is what separates S8 from S7, which folds two independent bullets.
- **S9** — The backlog row `TOOL-dFramedEntrypoint-1` in `memory/backlog/TOOL.md:40` flips from
  `OPEN` to `CLOSED` in the same commit, with a pointer at `builds/aHonedRuleset/`. Its stated fix is
  "two sentences, in the file that owns each", and S5 and S8 are those two sentences, so the row has
  nothing left open. The flip is part of this unit, not a follow-up.

## 3. Non-goals (OUT)

- Editing `tools/hooks/README.md` beyond the one sentence at `:117`. The grammar already lives there
  in full and is correct where it is stated properly, including the three receiver-qualifying shapes
  in its `What the hook DENIES` section. S8 corrects a sentence; it does not restructure the file.
- Bumping `KIT_AGENT_CAP_VERSION`. `tools/check-kit-versions.sh` requires the constant to be present,
  well-formed and in agreement with its paired markers, and demands no bump when a kit file changes.
  A README correction moves no shipped behaviour.
- Touching `§0`'s TL;DR line at `coding-governance-agents.template.md:22`, which repeats the
  two-rules sentence and the batching clause. That is the census's proposed drop `D1` and an owner
  call.
- Changing `MAX_VERIFIERS`, `MAX_LENSES`, the wired matcher in `.claude/settings.json`, or any other
  owning source behind a parity pair. This unit moves the playbook's stated side of nothing.
- Re-recording `tools/template-size-highwater.txt`. The gate's `--bump` records intended GROWTH, and
  a shrink owes it nothing.
- `memory/guides/REVIEW-PROTOCOL.md` and `tools/workflows/REVIEW-PROTOCOL.template.md`, which state
  the same two bounds by pointer already.

## 4. Design

### Inventory — the bullets, claim by claim

Measured at base `102e98f0` with `wc -c`. The cut spans two non-adjacent regions of `§8`. The cap
bullet is `sed -n '230,245p' coding-governance-agents.template.md` at 1488 bytes across sixteen
lines, and the two sidechain bullets are `sed -n '251,252p'` at 580 bytes, 313 and 267 individually.
The five bullets between them, `246,250p` at 863 bytes, are untouched, and 1488 + 863 + 580 = 2931
confirms the three regions partition `230,252p`. The edited source is therefore 2068 bytes.

Fragments `A` through `M` are the cap bullet; each was extracted and measured individually and the
thirteen sum to 1470 bytes, the missing 18 being joining whitespace. Fragments `N` and `O` are the
two sidechain bullets, measured whole because each is a single unwrapped line.

| # | Fragment | Bytes | Already stated in `tools/hooks/README.md` | Verdict |
|---|---|---|---|---|
| A | the two-rules headline | 99 | `:9-12`, as two bullets | KEEP — it is the rule |
| B | the server rate limiter and the harness auto-cap | 130 | nowhere | KEEP — the only statement of why |
| C | concurrency bounds together, total bounds existence | 76 | `:11-12` | KEEP — the rule's distinction |
| D | CONSOLIDATE, batching, `at most 5 verify agents TOTAL` | 120 | `:9-10` for the batching clause only | KEEP — parity and waiver both pin it |
| E | route through the bounded helpers, inlined, no imports | 149 | `:50-52`, near verbatim | COMPRESS to the pinned token |
| F | enforce at the tool call, not inside the script | 95 | `:3` | COMPRESS |
| G | denies a raw primitive and an unproven receiver | 101 | `:50` and `:53-60` | DELETE |
| H | counts direct spawns, the only enforcement outside a script | 110 | `:119-123`, near verbatim | DELETE |
| I | resolves a bound wherever written, denies an unresolvable K | 99 | `:94-96` | COMPRESS to the pinned token |
| J | array literal of five, the lens fan, passes unmarked | 68 | `:117`, and disputed there | REWRITE to the pinned token |
| K | fires on the exact matcher pair, `Workflow` alone is blind | 112 | `:16-17` | COMPRESS to the pinned token |
| L | five values machine-compared, retyping reds the bar | 170 | nowhere | KEEP, minus the count |
| M | the pointer at the README, and the harness beside it | 141 | n/a — it is the pointer | KEEP |
| N | sidechain restricted runtime, schema snippet, and the cap enforced at both tool calls | 313 | `:3` for the `PreToolUse` mechanism | COMPRESS — the enforcement clause is `F` and `K` again |
| O | a sidechain holds neither tool, inherits the doc, hooks fire, cap at the main loop | 267 | nowhere | KEEP, merged into `N` |

Fragments `G` and `H` are pure restatement and come out whole, which is 211 bytes. A further 167
bytes come from compressing `E`, `F`, `I`, `J`, `K`, `L` and `M` around the tokens that must survive,
which is the 378 bytes this unit was scoped against before `§8` `F3` was resolved. Folding `N` and
`O` into one bullet recovers 155 more: 580 bytes of source become 425.

### The five parity-compared values, individually

`tools/check-playbook-parity.sh` declares a `PAIRS` list. Five of its rows read their stated
side out of `coding-governance-agents.template.md`, and all five extractions land inside this one
bullet. Verified by running each extraction against the file at base and by
`bash tools/check-playbook-parity.sh`, which reports
`playbook-parity OK — 15 kit(s) documented or waived · pairs in agreement`.

| Pair label | Phrase the charter must keep | Charter line | Owning source | Owned value |
|---|---|---|---|---|
| `lens-array bound` | `array LITERAL of ≤5 elements` | 240 | `tools/hooks/agent-cap.js:408` | `MAX_LENSES = 5` |
| `agent-cap hook matcher` | ``matcher `Workflow|Agent` `` | 241 | `.claude/settings.json:5` | `"matcher": "Workflow|Agent"` |
| `verify-agent total` | `at most 5 verify agents TOTAL` | 234 | `tools/hooks/agent-cap.js:403` | `MAX_VERIFIERS = 5` |
| `bounded-helper width` | `boundedParallel(thunks, 5)` | 235 | `tools/hooks/agent-cap.js:403` | `MAX_VERIFIERS = 5` |
| `resolved-K ceiling` | `cannot resolve to an integer ≤5` | 240 | `tools/hooks/agent-cap.js:403` | `MAX_VERIFIERS = 5` |

Each phrase occurs exactly once in the whole template, confirmed by `grep -n` on each of the five
patterns. Three properties of the extraction bind the rewrite and none of them is obvious from
reading the gate's output.

First, `sed` applies each substitution per LINE, so a surviving phrase must not be broken by a wrap.
Second, the gate takes `head -1`, so a second occurrence introduced anywhere earlier in the file
would silently become the compared value. Third, an extraction that matches nothing does not pass —
`tools/check-playbook-parity.sh:138` reds it as `an extraction matched NOTHING`, which is the arm
`tools/check-playbook-parity.test.sh:111-113` proves by deleting the array-literal sentence from its
own synthetic fixture.

That self-test builds its own charter at `tools/check-playbook-parity.test.sh:51-52` rather than
copying this repo's, so nothing in this rewrite reaches its arms.

**A quoting trap, recorded because it cost a false alarm during this design pass.** The matcher
extraction contains backticks, and the script carries it inside a double-quoted `PAIRS` heredoc
where `\`` means a literal backtick. Re-typing that pattern into a single-quoted shell string instead
hands GNU `sed` the `\`` start-of-buffer anchor, and the pair silently extracts empty. Test the
extractions by `eval`-ing the field the way `tools/check-playbook-parity.sh:135` does, never by
re-typing the regex.

### The second gate on this bullet

`tools/check-agent-cap-restatement.sh` bans a fan-out bound written as a bare number in live
markdown. Run at base it reports `agent-cap-restatement: clean — 83 markdown file(s) scanned, 2
waiver(s)`. Reproducing its pattern over the template finds exactly ONE hit, at line 234, and
`tools/agent-cap-restatement-waivers.txt:8` waives it on the text `at most 5 verify agents TOTAL`.

The registry is shrink-only and a row whose text appears nowhere REDS as stale
(`tools/check-agent-cap-restatement.sh:167-176`). So that phrase is pinned twice over, by parity and
by the waiver, and the two other digits in the bullet survive only because their neighbouring nouns
are outside the gate's noun list. `elements` and `integer` are not bound nouns, which is why
`array LITERAL of ≤5 elements` and `an integer ≤5` do not fire. Any rewrite that put a listed noun
next to one of those digits would create a NEW unwaived hit. The replacement text was checked
against the reproduced pattern and produces the same single hit and no other.

### The replacement, measured

The candidate text is two bullets, 1110 and 425 bytes on disk, against the 1488 and 580 they replace.
That is 1535 against 2068, a recovery of **533 bytes**. Both halves were written to a file and
measured with `wc -c`; the widened figure is a fresh measurement and not the old 378 scaled up.

The census estimated 300-400 B for the cap bullet alone, and the 378 bytes fragments `A` through `M`
account for lands inside that range and supersedes it. The census also says the bullet "spends a
third of its length" on the grammar; measured over the whole edited region, the removable share is
25.8%, and that figure supersedes the estimate too.

The five bullets at `246,250p` sit between the two replacements and are not reproduced here. The
second bullet takes the position the pair at `:251-252` occupies today, so the diff stays local and
nothing between them moves.

```markdown
- **CONCURRENCY IS CAPPED, ALWAYS, and the verify-stage TOTAL is capped too — two rules, not one.**
  Concurrency bounds how many run together; the total bounds how many exist. A wide fan trips the
  SERVER rate limiter and kills whole phases for millions of tokens; a harness auto-cap does NOT
  protect you. **CONSOLIDATE before you fan out:** batching grows the batch, never the agent count —
  at most 5 verify agents TOTAL. Route Workflow fan-out through `boundedParallel(thunks, 5)` and its
  pipeline sibling. Enforcement sits at the tool call, never inside the script where no hook reaches:
  the `agent-cap` hook fires on matcher `Workflow|Agent`, the exact pair, and denies any K it
  cannot resolve to an integer ≤5 — an array LITERAL of ≤5 elements is a receiver it can size.
  These values are machine-compared against the sources that own them by
  `tools/check-playbook-parity.sh`, so retyping one wrong reds the bar rather than drifting. What the
  hook denies, how a bound is spelled and the marker grammar are its own, in
  `tools/hooks/README.md`; a ready harness ships beside it.
```

```markdown
- Orchestration scripts run in sidechains, in a restricted runtime (plain JS — no type syntax, no imports), so inline the schema discipline as a snippet. A sidechain agent holds NEITHER tool and cannot fan out at all — the capability is ABSENT, not policed — though it DOES inherit the governing doc and hooks DO fire in it, both measured. That is why the cap sits at the main loop, where the fan-out decision is MADE.
```

The first block's longest line is 102 bytes and the second is one unwrapped line of 424, both against
the 450 declared for this file in `tools/line-length-limits.txt`. The second is left unwrapped
because its five neighbours at `246,250p` are unwrapped single lines and it takes their position. The
builder may re-wrap freely subject to S2, which binds the first block only.

`tools/hooks/README.md:117` is replaced by one sentence stating the same fact S5 states: the
array-literal allowance sizes the RECEIVER of an `agent(` fan and is not an exemption from the
raw-primitive ban above it. That file carries no size ceiling in `tools/template-size-limits.txt` and
no row in `tools/line-length-limits.txt`, so the sentence is not measured here.

### Why this cut was planned once and did not land

`memory/builds/aFusedCharter/README.md:75-77` already resolved that this bullet's grammar "moves to
that hook's own README, leaving the two caps and the fact that a hook enforces them". What landed did
not do that. Measured: the pre-convergence bullet at `c65f2f9d:parallel-coding-governance.template.md:150`
was a single 1499-byte line, the bullet since `056331ba` flattens to 1457 bytes, and the whole
recorded move therefore recovered 42 bytes. What it removed was the marker spellings and the
`chunk`/`splitInto` spellings; what it left was a paraphrase of the same grammar plus a new pointer
sentence and a new parity sentence. `git log -L 230,245:coding-governance-agents.template.md` shows
the bullet byte-identical from that merge to base.

This is the `amendment-leaves-its-other-half-standing` class the census names, applied to a cut
rather than to a rule. Stated here so the unit is understood as finishing a landed decision rather
than proposing a new one.

### Files touched (estimate)

This unit is `order 3` and `TOOL-aHonedRuleset-2` is `order 1` on the same two carriers, so the
absolute figures below are stated against the post-unit-2 tree, not against base. Unit 2's own §8
moves that starting point, so the table is given on its recommended branch and the other two branches
are stated underneath. This unit's own delta is −533 bytes per carrier under every branch, because
neither edited region contains a `{{…}}` placeholder and the render therefore moves byte for byte.

| File | Before this unit | After | Ceiling | Free after |
|---|---|---|---|---|
| `coding-governance-agents.template.md` | 49018 | 48485 | 49152 | 667 |
| `AGENTS.md` (regenerated, not hand-edited) | 64380 | 63847 | 64512 | 665 |

Three more files are touched and are absent from the table because none carries a size ceiling:
`memory/guides/SESSION-KICKOFF.md`, where S6 re-verifies the §B claims and re-stamps `last-audit`;
`tools/hooks/README.md`, where S8 corrects one sentence; and `memory/backlog/TOOL.md`, where S9 flips
the row.

Both ceilings are declared in `tools/template-size-limits.txt` and were read there. Base was measured
with `wc -c` at `102e98f0` as 49144 and 64506, which is 8 and 6 bytes free; unit 2 recommends a
126-byte recovery per carrier, which is the 49018 and 64380 above. Everything right of that column is
arithmetic, not a measurement. If unit 2 does not land, this unit lands at 48611 and 63973 with 541
and 539 free; if unit 2 also drops its 86-byte connective, at 48399 and 63761 with 753 and 751 free.

The advisory `TEMPLATE-SIZE WARN` about growth past the recorded high-water of 48378 survives this
cut on every one of those branches, because the smallest of them, 48399, is still above it. The
margin is 21 bytes, down from 178 before `F3` widened the cut, so a fourth cut on this carrier could
take the template under its high-water and clear the WARN as a side effect. Clearing it is still not
this unit's job, and dropping below a high-water reds nothing.

### Alternatives rejected

- **Move the whole bullet to `tools/hooks/README.md` and leave a bare pointer.** Rejected: the two
  rules are the RULESET's job, and five parity pairs read their stated side out of this file. Moving
  them would either red five pairs or force the parity gate to be rewritten, which is a larger change
  than the one that pays for itself here.
- **Delete the parity sentence too, for the 170 bytes fragment `L` measures.** Rejected: it is the only warning an
  editor gets that five tokens in the paragraph are machine-compared, and this pass exists because
  the last editor of this bullet did not have that warning.
- **Keep `passes unmarked` verbatim to minimise the diff.** Rejected: `TOOL-dFramedEntrypoint-1`
  reproduced a five-thunk literal fan being DENIED, so the sentence is wrong, and rewriting the
  words around a known-wrong clause while leaving the clause is the class this build is auditing for.
- **Correct the charter carrier only and leave `tools/hooks/README.md:117` to its backlog row.** This
  spec recommended it at `§8` `F2` and the owner overruled it on 2026-09-04. The recommendation was
  scope hygiene; the ruling is that a half-applied correction leaves the wrong sentence live in the
  file that OWNS the rule, which is the worse of the two carriers to leave standing.
- **Leave the two sidechain bullets at `:251-252` for a follow-up.** This spec recommended it at
  `§8` `F3` and the owner overruled it on 2026-09-04. The recommendation weighed diff hygiene; the
  ruling weighed that the third and fourth statements of one enforcement location are the same defect
  as the first, and a follow-up that never gets raised leaves them standing forever.

## 5. Production-readiness checklist

- security — N/A. The enforced bound lives in `tools/hooks/agent-cap.js` and is untouched; this edit
  moves prose only, and the hook keeps denying whatever it denied before.
- perf / scale — N/A. No runtime code, and the affected gate legs are markdown scans.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — N/A. No program.
- observability — the change is observable through `bash tools/check-playbook-parity.sh` and
  `bash tools/check-template-size.sh`, both of which name the file and print the value they compared.
- risks — the real one is a silent parity break: a phrase re-wrapped across a line resolves to empty,
  and `tools/check-playbook-parity.sh` reds that by name rather than reporting agreement, so the
  failure is loud. The second risk is forgetting the re-render, which `playbook render wiring`
  catches. The third is forgetting S6's re-stamp, which the pre-commit hook blocks on rather than
  letting through. The fourth arrived with `F2`: S5 and S8 must say the same thing, and nothing gates
  the agreement of two prose carriers, so the builder writes both in one edit and reads them side by
  side. Rollback is `git revert` of one commit touching five files.
- testing + left-shift gates — no new gate. Two gates already hold this bullet, which is why this
  spec enumerates their pins rather than adding a third. `tools/check-agent-cap-restatement.sh`
  cannot see a bound written with no noun beside it and says so in its own header, and that blind
  spot is unchanged by this edit.
- migration / rollback — none. Adopters receive both files on their next `govkit` update, and the
  removed sentences are already carried by `tools/hooks/README.md`, which ships in the same kit. No
  version constant moves, so nothing changes about how a target detects the kit.
- user docs — `tools/hooks/README.md` is the doc, and S8 corrects one wrong sentence in it. Nothing
  else moves there: the grammar the charter points at is already stated in full and correctly.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-playbook-parity.sh` runs on the edited tree, it exits `0` and
  prints `pairs in agreement`, so all five stated values still extract and still match their owners.
- **AC2** — When the `PAIRS` rows labelled `lens-array bound`, `agent-cap hook matcher`,
  `verify-agent total`, `bounded-helper width` and `resolved-K ceiling` in
  `tools/check-playbook-parity.sh` each have their stated-side extraction run against
  `coding-governance-agents.template.md` on its own, each returns a NON-EMPTY value, proving no
  phrase was broken by a wrap rather than merely proving the gate is green. The rows are cited by
  label because `TOOL-aHonedRuleset-5` shares this unit's `order 3` and its S7 adds two rows and two
  header lines to that same list, which moves every line number in it.
- **AC3** — When `bash tools/check-agent-cap-restatement.sh` runs, it exits `0` and reports `clean`,
  with the waiver count unchanged at `2`, so the `at most 5 verify agents TOTAL` row is still live
  and no new bare-number carrier was introduced.
- **AC4** — When `bash tools/check-template-size.sh` runs, `coding-governance-agents.template.md`
  measures at most `48611` bytes, which is at least `533` below its base measurement of `49144`. The
  bound is stated against base rather than against the post-unit-2 tree so that it holds whichever
  branch `TOOL-aHonedRuleset-2` lands on.
- **AC5** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, it prints
  `region matches a fresh render`, proving `AGENTS.md` was regenerated in the same commit.
- **AC6** — When `bash tools/check-line-length.sh coding-governance-agents.template.md` runs, it
  exits `0` against the declared `450` in `tools/line-length-limits.txt`.
- **AC7** — When `grep -rc 'passes unmarked' coding-governance-agents.template.md AGENTS.md
  tools/hooks/README.md` runs, every one of the three returns `0`, and
  `grep -n 'array LITERAL of ≤5 elements' coding-governance-agents.template.md` still returns exactly
  one line. Both carriers of the wrong claim are corrected, which is what closes
  `TOOL-dFramedEntrypoint-1`.
- **AC8** — When `git diff --stat` is read on the landing commit, exactly five files are touched:
  the two carriers `coding-governance-agents.template.md` and `AGENTS.md`, S6's bundled re-stamp of
  `memory/guides/SESSION-KICKOFF.md` which the pre-commit hook requires, S8's
  `tools/hooks/README.md`, and S9's `memory/backlog/TOOL.md`. No sixth file appears — in particular
  no kit version constant and no waiver registry moves.
- **AC9** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary, it exits green.
- **AC10** — When `grep -c 'both fire a main-loop' coding-governance-agents.template.md` runs it
  returns `0`, and the `§8` bullets between `- Persist each Tier-2 run` and `- Verify before "done"`
  number exactly one. That observes the widened cut `F3` ordered: two bullets became one, and the
  third and fourth statements of the enforcement location are gone rather than merely reworded.
- **AC11** — When `grep -n 'TOOL-dFramedEntrypoint-1' memory/backlog/TOOL.md` runs, the row reads
  `CLOSED` and points at `builds/aHonedRuleset/`, and `bash tools/memory-tree/check-memory-hygiene.sh`
  exits `0` over the edited backlog.

## 7. Gates

- `playbook parity` — `tools/check-playbook-parity.sh`, `subject = repo`, unguarded, so this diff
  runs it. The five pairs are the load-bearing legs of this unit.
- `agent-cap restatement` — `tools/check-agent-cap-restatement.sh`, `subject = repo`, unguarded.
- `template size <=48KiB` — `tools/check-template-size.sh`, the ceiling this cut exists to buy back.
- `charter size` — `tools/check-template-size.sh AGENTS.md`, which moves with the re-render.
- `playbook render wiring` — `tools/playbook/adopt-playbook.sh --target . --check`, the leg that
  fails if `AGENTS.md` is not regenerated.
- `line length` — `tools/check-line-length.sh`.
- `playbook placeholder catalogue` — `tools/check-placeholders.sh`, because the edited region sits
  inside a template whose markers that gate counts.
- `kickoff-manifest ratchet` — `bash skills/session-kickoff/manifest-check.sh`. Owed because
  `coding-governance-agents.template.md` is a watched pathspec, and satisfied by S6.
- `memory hygiene` — `bash tools/memory-tree/check-memory-hygiene.sh`. Owed because S6 and S9 both
  put a `memory/` file in the commit, which is also what arms the hook's staged leg.
- `kit version markers` — `tools/check-kit-versions.sh`, `subject = repo`, unguarded. Named because
  S8 edits a file under `tools/hooks/`, and to record what it does NOT demand: the constant must be
  present, well-formed and in agreement with its paired markers, never bumped because a kit file
  changed.
- The five self-test legs guarded on `tools/hooks/` in `tools/gate-legs.json` — `agent-cap
  self-test`, `scratch-guard self-test`, `verifier fan-out self-test`, `review-join self-test` and
  `hook destinations self-test`. S8 puts a file under that guard, so this diff arms them. They are
  `chunk = selftests`, which the ordinary bar and `GATE_FULL=1` both hold, so the DoD runs
  `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` once. None of them reads the sentence S8
  edits — they build synthetic fixtures — so this is a guard being honoured, not a real coupling.
- No new gate. Both pins on the cap bullet already exist and both were run at base. Every leg above
  the `tools/hooks/` group carries no `guard` in `tools/gate-legs.json` and so cannot be skipped by
  this diff's shape; that is a property of the manifest and not of this change, which is why no
  acceptance criterion asserts it.

## 8. Open questions

- **F1 — does the count word `FIVE` come out of the parity sentence?** The bullet currently opens
  that sentence with `FIVE of these values are machine-compared`. Nothing gates the word, and
  the `PAIRS` list is a derived population, so `§7`'s rule that no count of
  a derived population is written in prose applies to it. The count is also not actionable on its
  own, because it does not say WHICH five and an editor must open the script regardless. *Recommend
  dropping the word*, which the §4 candidate text does, saving 5 bytes and one ungated number. The
  owner may prefer to keep it as a louder warning.
  RESOLVED (owner, 2026-09-04): drop the word FIVE. This matches the recommendation, so the §4
  candidate text stands unchanged and S1 keeps the parity sentence without its count.
- **F2 — how far does the array-literal correction reach?** `TOOL-dFramedEntrypoint-1` is OPEN and
  names two carriers, `AGENTS.md §8` and `tools/hooks/README.md:117`, and its stated fix is "two
  sentences, in the file that owns each". S5 rewrites the charter carrier as a side effect of the
  cut, because leaving a clause the corpus records as wrong while rewriting its neighbours is exactly
  the defect class this build audits. That leaves that row half-addressed. *Recommend landing S5 and
  leaving the row OPEN against its README half*, rather than either widening this unit into the
  hooks kit or preserving a known-wrong sentence to keep the row tidy. The owner may prefer this unit
  make no correction at all and hand both carriers to that row.
  RESOLVED (owner, 2026-09-04): fix BOTH carriers and close `TOOL-dFramedEntrypoint-1`. This goes
  AGAINST the recommendation above, which is left standing as written. §2 gains S8 for
  `tools/hooks/README.md:117` and S9 for the row's status flip, §3 drops the non-goal that forbade
  the README, AC7 now checks all three carriers of the phrase, AC8 counts five files, and AC11
  observes the closed row. The two edits are ONE correction on two carriers of a single wrong claim
  about `tools/hooks/agent-cap.js`, not two mechanisms — which is why they belong in one diff, and
  why this ruling reads differently from `F3`'s.
- **F3 — do the neighbouring `§8` bullets at `:251` and `:252` join this unit?** They restate the
  enforcement location a third and fourth time, and `:251` also repeats the matcher pair in prose.
  Folding them in would recover more, and would also put two mechanisms in one diff.
  *Recommend leaving them out* and raising a follow-up if the recovered bytes are wanted; the
  measured 378 already clears the pressure this unit was scoped against.
  RESOLVED (owner, 2026-09-04): fold them in. This goes AGAINST the recommendation above, which is
  left standing as written. §2 gains S7, §4's byte arithmetic was re-measured over the widened
  `230,252p` range with `wc -c` rather than scaled from the old figure — 2068 bytes of source become
  1535, a recovery of 533 — and AC10 observes the widened cut directly rather than inferring it from
  the size gate.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Every figure in `§4` measured at base `102e98f0` rather than
  carried from the census; where the two disagree, the disagreement is stated in place.
- rev-2 · 2026-09-04 · folded the four findings the spec audit
  `2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md` addresses to this unit. B2: AC8 forbade the
  third file `.githooks/pre-commit` requires, so it now names `memory/guides/SESSION-KICKOFF.md`
  alongside the two carriers, S6 adds the bundled `last-audit` re-stamp, and §7 gains the
  `kickoff-manifest ratchet` and `memory hygiene` legs that commit owes. P1: AC2 cited
  `tools/check-playbook-parity.sh:113-117`, a span `TOOL-aHonedRuleset-5`'s S7 moves at the same
  `order 2`, so it now cites the five `PAIRS` rows by label. P5: §1 and §4's ceiling table were
  arithmetic against base while `TOOL-aHonedRuleset-2` is `order 1` on the same carriers, so the
  table is restated against the post-unit-2 tree with both other branches of that unit's unresolved
  §8 given underneath. P8: AC9's second clause asserted six legs run unskipped, which is a `guard`-free
  property of `tools/gate-legs.json` rather than of this change, so it is dropped and the manifest
  fact is stated in §7 instead. Every figure touched was re-measured at base: 49144, 64506, 8 and 6
  free against the ceilings in `tools/template-size-limits.txt`, the bullet at 1488 bytes and the §4
  candidate at 1110. No §8 fork is resolved by this revision.

- rev-3 · 2026-09-04 · fold-verification nit: §4 and §8 F1 cited
  `tools/check-playbook-parity.sh` by line span, the citation style rev-2 removed from AC2 for the
  same reason — `TOOL-aHonedRuleset-5`'s S7 moves that span at the same `order 2`. Both now name
  the `PAIRS` list without a span.

- rev-4 · 2026-09-04 · owner rulings applied; header stamped `ratified 2026-09-04` and the order verb
  moved from `order 2` to `order 3`, which changes AC2's and §4's citation of the unit this one runs
  beside without changing that it is `TOOL-aHonedRuleset-5`. F1 resolved to dropping the word `FIVE`,
  matching the recommendation, so nothing downstream moved. F2 resolved AGAINST the recommendation:
  both carriers are fixed and `TOOL-dFramedEntrypoint-1` closes, which added S8 and S9, deleted the
  §3 non-goal forbidding `tools/hooks/README.md`, added a §3 non-goal against a version bump and
  against restructuring that file, widened AC7 to all three carriers of the phrase, moved AC8 from
  three files to five, added AC11, added the `kit version markers` leg and the five `tools/hooks/`
  guarded self-test legs to §7 with the `GATE_SELFTESTS=1` run they oblige, added the two-carrier
  agreement risk to §5, and widened §10's dossier-staleness claim to cover the README. F3 also
  resolved AGAINST the recommendation: the bullets at `:251` and `:252` fold in, which added S7,
  added inventory rows `N` and `O`, added the second candidate block, and forced §4's arithmetic to
  be RE-MEASURED rather than scaled. Every figure touched was re-measured with `wc -c` at base
  `102e98f0`: the cap bullet 1488, the sidechain pair 580 as 313 plus 267, the untouched five 863,
  the three summing to 2931 over `230,252p`; the replacements 1110 and 425 for 1535; recovery 533,
  which is 25.8% of the edited region. Ceilings 49152 and 64512 read from
  `tools/template-size-limits.txt`, high-water 48378 from `tools/template-size-highwater.txt`,
  leaving 21 bytes of margin on the narrowest branch instead of the previous 178.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "charter bullet restating the agent-cap hook grammar that
tools/hooks/README.md owns"` returned the `agent-cap` affordance seam and named the inventory keys
`agent-cap restatement` and `agent-cap restatement self-test`. That is the seam this unit extends:
`tools/check-agent-cap-restatement.sh` and its text-keyed waiver registry already police bare fan-out
numbers in this exact bullet, and `tools/check-playbook-parity.sh` already pins its five values, so
this unit adds no mechanism and instead edits prose inside two existing ones. The dossier for that
seam is `memory/map/features/agent-cap.md`; `grep -n "charter|AGENTS.md|§8"` over it finds only a
pointer at `memory/guides/REVIEW-PROTOCOL.md` and no description of the charter's wording, and
`grep -n "README"` over the same file returns nothing, so neither S5 nor S8 makes dossier prose stale
and no new inventory key is claimed. What the dossier does describe is the hook's array-literal
element counter, which this unit does not touch — the mechanism was always right and only the two
prose copies of it were wrong.

The recall probe surfaced the two records that changed this spec's shape, neither of which the census
cites: `memory/builds/aFusedCharter/README.md:75-77`, which already ruled this cut and did not land
it, and the OPEN backlog row `TOOL-dFramedEntrypoint-1`, which records the surviving array-literal
sentence as wrong in this very file.

Recall terms used: `python tools/memory-recall/query.py "why does the charter restate the agent-cap
hook's resolvable-bound grammar when tools/hooks/README.md owns it" --terms "agent-cap restatement
charter bullet fan-out cap parity pair resolvable-bound grammar hook README pointer duplication
playbook-parity waiver"`

# TOOL-aBoundedVerdict-19 — the protocol pair says what the code does, and one closed AC is settled

**Status:** SPECCED · rev-2 · 2026-08-20 · node c · Tier-1 · base 098bebd9 · streams tooling

## 1. Goal

Three documented claims about the close path are false against the code, and the parity legs cannot see
any of them because they compare the shipped copy to the installed copy rather than either to reality:
the `records-current` Asserts cell describes retired semantics, no artifact an agent reads at close time
names the one item that cannot be overridden, and a CLOSED spec's acceptance criterion asserts a grep
returns zero where it returns two. Correct all three, and record the third as a finding rather than
quietly fixing it.

## 2. Scope (IN)

- **S1** — the `records-current` Asserts cell is rewritten to the implemented invariant in BOTH halves
  of the protocol pair. It currently describes a fresh-render comparison and unit status headers the
  driver never reads; what the item actually asserts is the ABSENCE of a second copy plus both marker
  pairs being well-formed. The `build-complete` clause beside it is qualified with WHICH file's region
  it reads, which is the ambiguity that made the whole item unreadable.
- **S2** — the non-overridable item is named where an agent meets it. Protocol §4's override paragraph
  carves out only the two attested items; the sole statement that `authorization-reachable` cannot be
  overridden sits in §1 line 71, scoped there to run START. One sentence in §4 and one in the Skill's
  Close section, because the Skill is the artifact an agent actually reads when a close refuses.
- **S3** — `TOOL-cBriefedPilot-18`'s AC9 is settled on the record. It reads *"§1's roster bullet in both
  halves no longer reads `Opt-in by presence`, grepped and found zero"*; the phrase is present in both
  halves, and `git log -S` over the template returns exactly one commit — the one that ADDED it, five
  days before that spec closed. The AC was never met. This unit does not reopen a closed spec: it files
  a backlog row naming the unmet AC and its evidence, so the falsity is recorded where the next reader
  of that spec will find it.
- **S4** — the roster bullet itself is corrected as part of `TOOL-aBoundedVerdict-11`'s scope, not here.
  S3 records the record-keeping defect; the text change belongs with the mechanism that makes the roster
  mandatory, or the two would disagree for however long they were split.
- **S5** — a note in the protocol pair's own header, or in the parity legs' source, stating what those
  legs do and do not check: they compare the two copies to each other, so a claim false in both is
  green. This is the reason all three defects survived, and it is worth one sentence where the next
  author looks.

## 3. Non-goals (OUT)

- No mechanism change. Every scope item is prose, a backlog row, or a sentence. If a document and the
  code disagree and the CODE is wrong, that is another unit's finding — here the documents are wrong.
- Not reopening `TOOL-cBriefedPilot-18`. It is CLOSED and on another node; S3 records the unmet AC as a
  backlog row rather than reverting a status, which is what this repo's append-only discipline asks for.
- Not the roster bullet's text, which is `TOOL-aBoundedVerdict-11`'s (S4).
- Not a general audit of the protocol pair's other cells. The audit examined the close path; the rest is
  named as uncovered in its own coverage section.
- No new gate. S5 is a comment, not a check — a parity leg that compared a document to code would be a
  different and much larger unit, and pretending one sentence achieves it would be the same class of
  defect this unit is fixing.

## 4. Design

### The three claims, and what each is measured against

| claim | where | reality |
|---|---|---|
| `records-current` asserts a fresh render and reads unit status headers | protocol §4's Asserts cell, both halves | the driver asserts the region is EMPTY and both marker pairs are well-formed; it reads no status header |
| the overridable carve-out covers the two attested items | protocol §4's override paragraph | `authorization-reachable` is also non-overridable, refused by `fail 21`, and §4 does not say so |
| the roster bullet no longer reads `Opt-in by presence` | `TOOL-cBriefedPilot-18` AC9, CLOSED | present at `memory/guides/UNATTENDED-PROTOCOL.md:33` and `tools/unattended/PROTOCOL.template.md:33`; `git log -S` returns only the ADDING commit |

### Why the parity legs are green over all three

`check-unattended.sh` check 10 byte-diffs the shipped protocol against the installed one, and check 16
joins the DoD item NAMES in the document to the driver's constant. So a cell whose Asserts prose is
wrong in both copies passes check 10 (they match) and passes check 16 (the name is right). The legs
verify internal consistency, not correspondence — and nothing in the tree verifies correspondence for
this document.

That is worth stating in source (S5) because it is the reason three false claims coexisted with a green
bar, and because a later author will otherwise assume the legs cover more than they do. It is the same
distinction the playbook parity gate's own header already draws for itself: structural only, and a
fluent paraphrase that is subtly wrong still passes.

### Inventory

| Concern | Today | After |
|---|---|---|
| `records-current`'s documented claim | retired semantics, in both copies | the implemented invariant |
| which file's region `build-complete` reads | unqualified | named |
| the non-overridable item | stated once, in a run-START context | stated in §4 and in the Skill's Close section |
| the closed AC9 claim of `TOOL-cBriefedPilot-18` | closed, asserting a grep that returns two | a backlog row naming the unmet AC and its evidence |
| what the parity legs check | unstated; assumed to be more | stated in source |

### Migration

None. Prose in two files that a leg byte-compares, so both halves move together in one commit or the leg
reds — which is the one mechanical constraint this unit has and is why S1 says BOTH halves.

### Rollout

S3 first and alone: a backlog row costs nothing and stops the false AC being inherited by the next reader
while the rest of this unit is still open. Then S1, S2 and S5, which are one edit across the pair plus the
rendered Skill. S4 is not this unit's to roll out.

### Files touched (estimate)

`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (S1, S2, S5) ·
`tools/unattended/SKILL.template.md` and the rendered `.claude/skills/unattended/SKILL.md` (S2) ·
`memory/backlog/TOOL.md` (S3's row) · possibly `tools/unattended/check-unattended.sh` if S5's note lands
in the leg's source rather than the document's header · the kit version constant if the protocol version
moves.

### Alternatives rejected

- **Fix the roster bullet here, since it is one string.** Rejected in S4: it would land the text before
  the mechanism that makes it true, so the document would claim a mandatory roster the code does not
  enforce — trading a false claim for a different false claim.
- **Reopen `TOOL-cBriefedPilot-18` and reset its status.** Rejected: it is closed, it is another node's,
  and this repo's discipline is append-only. A backlog row naming the unmet AC is the recorded form.
- **Add a leg that compares the protocol's Asserts cells to the driver's behaviour.** The right idea and
  the wrong unit: it is a substantial mechanism, it needs a machine-readable statement of each item's
  invariant, and pretending S5's sentence approximates it is the defect being fixed. If the owner wants
  it, it is its own spec.
- **Say nothing about the parity legs' scope.** Rejected: three false claims survived a green bar
  precisely because their scope was assumed rather than stated.

## 5. Production-readiness checklist

- **security** — S2 is security-adjacent: an agent that does not know `authorization-reachable` cannot be
  overridden may spend effort trying, or may reach for a bypass. Naming the carve-out where the agent
  reads it is the mitigation.
- **perf / scale** — N/A.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — N/A; no code path.
- **observability** — S5 is the deliverable: the legs' scope becomes readable at the place a later author
  looks.
- **risks** — the honest one is that this unit fixes documents and the next drift is unprevented, because
  S5 is a sentence and not a gate. Stated in §3 and in the rejected alternative rather than implied away.
- **testing + left-shift gates** — no new test. The existing parity legs enforce that both halves move
  together, and `adopt-unattended.sh --check` enforces that the rendered Skill matches its template — so
  S2's Skill edit is gated even though the prose is not.
- **migration / rollback** — none.
- **user docs** — this unit IS the user docs.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'records-current' memory/guides/UNATTENDED-PROTOCOL.md` and the same over
  `tools/unattended/PROTOCOL.template.md` are read, the Asserts cell describes the empty-region and
  well-formed-marker invariant and mentions no fresh render and no status header, in both.
- **AC2** — When the `build-complete` clause is read, it names which file's region the item reads.
- **AC3** — When protocol §4 and `.claude/skills/unattended/SKILL.md`'s Close section are read, each
  states that `authorization-reachable` cannot be overridden.
- **AC4** — When `bash tools/unattended/adopt-unattended.sh --check` runs after the Skill edit, it is
  clean — the rendered Skill still matches its template and carries no surviving `{{`-shaped
  placeholder.
- **AC5** — When `bash tools/unattended/check-unattended.sh` runs, check 10's shipped-vs-installed
  byte-diff is clean, proving both halves moved together.
- **AC6** — When `memory/backlog/TOOL.md` is read, it carries a row naming `TOOL-cBriefedPilot-18`'s
  unmet AC9 with the two file:line hits and the `git log -S` evidence, and
  `bash tools/memory-tree/check-memory-hygiene.sh` is clean over it.
- **AC7** — When the parity legs' scope note is read, it states that they compare the two copies to each
  other and verify no claim against code — found by `grep -n 'byte-diff\|correspondence'` at the site S5
  chose.

## 7. Gates

`tools/unattended/check-unattended.sh` + `tools/unattended/check-unattended.test.sh` ·
`bash tools/unattended/adopt-unattended.sh --check` ·
`tools/workflows/check-protocol-parity.test.sh` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/check-kit-versions.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — does S5's note live in the protocol document's header or in the leg's source?** The document is
  what an author edits; the leg is what makes the claim. **Recommendation: the leg's source**, beside
  check 10, because that is where someone about to trust the check is standing — and the protocol pair
  is byte-compared, so a note in it must be written twice.
  RESOLVED (agent, 2026-08-19, delegated): the leg's source. Mechanism-only, and the alternative
  duplicates the note into a byte-compared pair.

- **F2 — should S3's backlog row be filed under TOOL, or raised with the node that owns
  `TOOL-cBriefedPilot-18`?** The id's slug is node `c`'s and this session is on node `c`, so there is no
  cross-node hand-off to make. **Recommendation: a TOOL row here**, which is the shard the id already
  belongs to.
  RESOLVED (agent, 2026-08-20, delegated): a TOOL row, filed here. Mechanism-only. Re-verified at
  this run's base rather than inherited: the id's slug is node `c`'s and this run is on node `c`, so
  the bullet's premise still holds and there is still no cross-node hand-off to make. A row in the
  shard the id already belongs to is where a reader of that id looks.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's mediums 30 and 33, plus a
  defect the design pass found independently and verified with `git log -S`: `TOOL-cBriefedPilot-18`
  closed asserting a grep returned zero where it returns two, and the phrase was never removed. Kept as
  one Tier-1 unit because all three are documents that disagree with code and all three survived for one
  reason — the parity legs compare the copies to each other, which S5 records. F1 and F2 resolved under
  the delegated fork rule.

- rev-2 · 2026-08-20 · M3 fork sweep, before any code. F2 RESOLVED as recommended, a TOOL row filed
  here — and its premise was RE-VERIFIED rather than inherited, because "this session is on node c" is
  exactly the kind of claim that is true when written and false when read. It is still true. §8's
  first non-blank line is now the machine-legal `none` form.

## 10. Reuse audit

No code seam: this unit changes prose, a backlog row and one comment. The seams it RELIES on are the
existing parity legs — check 10's shipped-vs-installed byte-diff and
`adopt-unattended.sh --check`'s render comparison — which together guarantee that a document edit here
cannot land in one copy only. That guarantee is why §4's Migration has one constraint and no procedure.

The backlog shard `memory/backlog/TOOL.md` is the recorded form for S3, and the hygiene gate's id
resolution is what makes the row's citation of a closed spec legal — an id resolves against the set
defined by a spec H1, and `TOOL-cBriefedPilot-18` has one.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict adversarial
diff fold unattended close build-complete DoD stall halt`.

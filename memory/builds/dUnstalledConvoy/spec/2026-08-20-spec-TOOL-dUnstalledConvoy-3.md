# TOOL-dUnstalledConvoy-3 — the contract states the relaxed terminal, its two anchors, and what the weaker one cannot buy

**Status:** SPECCED · rev-2 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling

## 1. Goal

`memory/guides/UNATTENDED-PROTOCOL.md` is the binding contract and the Skill is its operating
summary. Both describe a `LANDED` phase reachable only by observing the remote. This unit states the
second anchor, the fact that records which one answered, and the boundary the weaker anchor sits
outside — before either the driver or the leg implements it.

## 2. Scope (IN)

- **S1** — protocol section 3 states that `LANDED` is reachable on either anchor and that the
  run-state file records which. The phase vocabulary itself does not grow.
- **S2** — protocol section 6 gains the two-anchor rule: the remote observation is attempted FIRST
  and a local ancestry assertion is the fallback, never the reverse.
- **S3** — protocol section 8's key table gains `LANDED_ANCHOR_CUTOFF`, and the shipped
  `.unattended.conf.example` gains it with the same comment.
- **S4** — protocol section 9 gains one paragraph naming what a local anchor cannot buy: the ref is
  inside the run's reach, so a local-anchored `LANDED` is a record of a merge rather than an
  observation of one, and the recorded anchor kind is what keeps the two distinguishable.
- **S5** — the Skill's `Mark it landed` section states the fallback and the two new facts, in the
  Skill's own voice, pointing at the protocol rather than restating section 9's paragraph.
- **S6** — both templates move in the SAME commit as their installed copies, but the two pairs are
  graded by DIFFERENT mechanisms and this unit must not conflate them. Review fold: H13. The kit
  gate's check 10 compares exactly ONE pair — the shipped protocol against this repo's installed copy
  — and says so in its own header. The Skill template is NOT byte-identical to its render: it carries
  interpolated deploy tokens, so a byte comparison of that pair can never pass. The Skill pair is
  graded by re-running the adopter in its check mode, wired as its own gate leg, and that leg is the
  one this build must name.
- **S7** — the change is measured against `READ_PATH_CEILING` before it is committed. The protocol is
  a read-path file and the margin at BASE is 7 152 bytes across all six.

## 3. Non-goals (OUT)

- Implementing either arm. The driver is `TOOL-dUnstalledConvoy-1` and the leg is
  `TOOL-dUnstalledConvoy-2`.
- Adding a phase. The owner chose to relax `LANDED` over adding a terminal, and this document must
  not reintroduce the rejected shape as vocabulary.
- Restating the cost paragraph in the Skill. The Skill points; the protocol states. A paraphrase and
  its source are two answers to one question, and the paraphrase is the copy that rots.
- Touching `memory/guides/BUILD-METHOD.md`. Its M10 already says the contract is deliberately not
  paraphrased there, and that stays true.

## 4. Design

### Inventory

| Carrier | Section | Change |
|---|---|---|
| `PROTOCOL.template.md` and its render | 3 | `LANDED` reachable on either anchor; the recorded kind |
| the same pair | 6 | the ordered two-anchor rule |
| the same pair | 8 | the `LANDED_ANCHOR_CUTOFF` row |
| the same pair | 9 | what the local anchor cannot buy |
| `SKILL.template.md` and its render | `Mark it landed` | the fallback, the two facts, a pointer to section 9 |
| `.unattended.conf.example` | the cutoff block | the key and its comment |

### The ordering rule is the substance

Section 6 must state that the remote arm is attempted FIRST, not merely that both exist. A contract
that lists two anchors without ordering them permits an implementation that takes the cheaper one
always, which would retire the observation entirely while satisfying every word of the document. The
ordering is what preserves the strong claim wherever the strong claim is available.

### What section 9 gains, and why it belongs there and not in section 6

Section 9 is where this kit already states the boundary it claims — what a check running under the
run's own uid can and cannot buy. The local anchor is a new instance of exactly that, not a new kind
of thing, so it extends the existing paragraph's argument rather than opening a second place where
the kit discusses its own limits.

Section 6 says what the rule IS. Section 9 says what it COSTS. Splitting them that way is how the
document is already organised, and merging them would put a caveat where an operator is looking for
a procedure.

### Byte budget

The protocol is 32 258 bytes at BASE and is one of six read-path files summing 105 835 against a
ceiling of 112 987. This unit's four sections plus the Skill edit are prose additions. The margin is
7 152 bytes and three other units in this build also write read-path files, so this unit measures
with `python tools/memory-tree/corpus_ids.py --report` before committing and states the figure in its
commit message. If the build as a whole does not fit, raising the ceiling is a declared movement with
its justification beside the number, which is this repo's established idiom and an owner turn.

### Alternatives rejected

- **Stating the two anchors only in the Skill.** The Skill says the protocol wins on any difference
  and calls a divergence a bug in the render. A rule that exists only in the render is a rule the
  binding document does not carry.
- **A new protocol section for the anchors.** Rejected: sections 3, 6, 8 and 9 already own the four
  facts, and a fifth home would make section 6 incomplete on its own subject.

## 5. Production-readiness checklist

- security — S4 IS the security statement, and its placement in section 9 is the design decision.
- perf / scale — N/A — documentation.
- a11y — N/A — documentation.
- i18n — N/A — documentation.
- error / empty / loading states — N/A — documentation. The refusal texts belong to the two
  implementing units.
- observability — the recorded anchor kind is what makes a landed record readable, and this unit is
  where that becomes a stated contract rather than a driver detail.
- risks (concurrency, data-loss, rollback hazards) — the read-path ceiling is the live risk and S7
  is the control. A ceiling breach reds hygiene check 16 on a records-only commit.
- testing + left-shift gates — check 10's byte comparison is the gate, and it already exists. The
  conf-axis check that pairs a read key with the protocol table and the example covers S3.
- migration / rollback — none. Documentation lands with the units it describes.
- user docs — this unit IS the user docs.

## 6. Acceptance criteria

- **AC1** — `bash tools/unattended/check-unattended.sh` stays green, which is check 10 asserting the
  shipped template and the installed copy are byte-identical after the edit.
- **AC2** — Protocol section 6 states the remote arm is attempted first, and a reader can answer
  "which anchor wins when both would succeed" from that section alone, observed in `memory/guides/UNATTENDED-PROTOCOL.md`.
- **AC3** — Protocol section 9 names the `git update-ref` lever explicitly as the reason a local
  anchor is a record rather than an observation.
- **AC4** — `grep -c LANDED_ANCHOR_CUTOFF` returns a non-zero count in `.unattended.conf.example` and
  in the protocol's section 8 table.
- **AC5** — `python tools/memory-tree/corpus_ids.py --report` shows the read path below
  `READ_PATH_CEILING` after the edit, and the figure appears in the commit message.
- **AC6** — The rendered Skill matches what the adopter renders, observed by
  `bash tools/unattended/adopt-unattended.sh --target . --check` exiting 0. Review fold: H13. The
  first draft named `tools/check-wiring.sh --check`, which does not compare that pair at all — its
  Skill check reads line endings and NUL bytes only, and it reports on hooks, the merge driver, EOL
  and the kickoff engine, never the unattended Skill render.
- **AC7** — `grep` over the installed `memory/guides/UNATTENDED-PROTOCOL.md` finds section 3 naming
  BOTH anchors and naming the recorded anchor-kind fact. Review fold: M3, the scope item that had no
  observation and whose absence the parity criteria could not detect.
- **AC8** — `grep` over the rendered `.claude/skills/unattended/SKILL.md` finds its landing section
  naming the local fallback, both new facts, and the pointer to the protocol's boundary section.
  Review fold: M3.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `memory-tree hygiene` (check 16, the read path) ·
the full bar at the push boundary. Review fold: H13 — `memory-recall skill wiring` belongs to a
different kit entirely and was named here by mistake.

## 8. Open questions

none — the forks this unit could have carried were resolved by the owner at kickoff, and the
placement questions are settled in §4 against the document's existing organisation.

## 9. Revision log

- rev-2 · 2026-08-20 · folded the spec audit: H13 (the protocol pair and the Skill pair are graded by
  DIFFERENT mechanisms; AC6 named a script that does not compare the Skill pair, and §7 named a leg
  belonging to another kit), M3 (two scope items had no criterion, and the parity criteria standing in
  for them are true of an untouched pair).
- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the unattended protocol document and the Skill render it
ships beside"` returns the `unattended` dossier and `.unattended.conf` as the affordance seam. The
seam this unit extends is the existing template-and-render pair, joined by check 10's byte
comparison, which is why §4 treats each pair as one artifact rather than two documents.

`python tools/memory-recall/query.py "why does the unattended kit state its own boundary rather than
implying it, and where" --terms "protocol section boundary uid claim observation record anchor
landing skill render byte compare paraphrase pointer"` returns the boundary-section records and the
pointer-not-copy rule the method's M1 enforces. Verified at writing time: the protocol's section
headers are the eleven this spec cites, and the Skill carries the sentence saying the protocol wins
on a difference.

Recall terms used: protocol section boundary uid claim observation record anchor landing skill render
byte compare paraphrase pointer.

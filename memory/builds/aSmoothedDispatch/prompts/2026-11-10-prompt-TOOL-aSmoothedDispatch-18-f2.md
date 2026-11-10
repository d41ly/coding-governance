# Revision brief — aSmoothedDispatch: spec 18's fork F2, resolved by the owner

**Serves:** research TOOL-aSmoothedDispatch-18

## The brief

### Goal
Unit 18's builder stopped with a divergence record: spec 18's §7 F2, "Which help page carries the `--help` anchor?", carries no RESOLVED mark, so the unit is FORKED and not buildable. The owner answered on 2026-11-10 with "(a) spec-audit.md". Record the resolution in place in the §7 shape the template states, with a rev-2 bump and a revision-log line naming this record. Then make the parts of the spec that depend on F2 name that one page: §4 S4, §4 "Files touched" and AC4's "the page F2 picks". `help/spec-audit.md` gains a short `--help` section beside its existing `--record-round` anchor. No `help/unattended.md` is created and `help/README.md` gains no line.

### Items
1. §7 F2 marked RESOLVED by the owner, 2026-11-10, option (a), in the template's shape.
2. §4 S4, §4 "Files touched" and AC4 name `help/spec-audit.md` as the page that carries the anchor, and drop the paths that only (b) or (c) needed.
3. A rev-2 revision-log line naming F2, S4 and AC4 and this record.
4. Run `python tools/check-spec-tokens.py --spec` on the spec and fix any hit.

### Acceptance
§7 shows F2 resolved, with no unresolved item left in §7. Nothing in the spec names `help/unattended.md`. The one-spec token check exits 0.

### Gates
Spec tokens (`--spec`), run by the writer. The commit and the re-dispatch are the main loop's.

### Non-goals
Any change to S1, S2, S3, their criteria, or anything else F2 does not touch. The spec's status header stays INPROGRESS, which the main loop set before the first dispatch.

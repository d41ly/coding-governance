**Serves:** research PLAY-dOrderedCharter-75

# Brief: spec 75 rev-2 — resolve F2 and pin one count, so its pass can commit CLOSED

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. Unit 75 built as spec 75 says, but the pre-commit hook refused the CLOSED commit: memory hygiene's fork check
reads section 8 F2 as carrying no conforming resolution mark, which a terminal status may not leave. The builder saved its pass as a
patch and restored the tree.

## The brief

### Goal

Revise spec 75 so its pass commits CLOSED, changing nothing the builder built.

### Items

1. **F2.** Mark it resolved in place, in the section 8 shape `memory/TEMPLATE-SPEC.md` gives, for the option its own text recommends
   and section 3 already carries: (b), the dependencies named in prose with the edges written `none`. Keep its options and vetoes.
2. **The unpinned count.** The alternatives table's row for a pending or waiver row per declared selector states `42 rows` with no pin;
   `python tools/playbook/writing_practice.py check pinned-facts` reds it. Pin, key or mark it as the spec's other counts are.
3. Edit the spec in the repository directly; no builder is running.

In the spec: bump the **Status:** rev by one, dated 2026-11-10, status kept `DEFERRED`, with one revision-log line naming this brief
and saying no design text moved. Edit nothing else.

### Acceptance

- Spec 75's F2 carries a conforming resolution mark, the pinned-facts check names nothing in spec 75, and a rev-2 log line exists.

### Gates

Run `python tools/playbook/writing_practice.py check pinned-facts` and memory hygiene's fork check over the spec, and report each.

### Non-goals

- No code. No edit to any other file.

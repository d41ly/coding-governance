**Serves:** research PLAY-dOrderedCharter-77

# Brief: spec 77 rev-2 — pin its two ceiling figures

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. The main loop's pre-dispatch check runs `python tools/playbook/writing_practice.py check pinned-facts`, and it
reds spec 77 on two figures that carry no pin on their own line: the tags leg's measured wall and its new ceiling.

## The brief

### Goal

Pin both figures so the pinned-facts check names nothing in spec 77, moving no design text.

### Items

1. Mark the tags leg's measured wall as derived at the commit the main loop measured it at, `de36424bf`, and the new ceiling as the
   value the ceiling-margin file requires, on each figure's own line, in the shapes the spec's other counts use.
2. Edit the spec in the repository directly; no builder is running.

In the spec: bump the **Status:** rev by one, dated 2026-11-10, status kept `DEFERRED`, with one revision-log line naming this brief
and saying no design text moved. Edit nothing else.

### Acceptance

- The pinned-facts check names nothing in spec 77, and a rev-2 log line exists.

### Gates

Run `python tools/playbook/writing_practice.py check pinned-facts` and report it.

### Non-goals

- No code. No edit to any other file.

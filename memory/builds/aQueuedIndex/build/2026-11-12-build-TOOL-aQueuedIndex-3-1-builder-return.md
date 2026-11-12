# aQueuedIndex — unit 3's builder return

**Serves:** journal TOOL-aQueuedIndex-3

Run wf_608ab835-1ff, summarized from its return.

- What landed: pass commit `73813cae8`. The `queued-writers` plant prints the busy timeout after writer one's line, and its green
  verdict requires the timeout at 600 or more; the index module is unchanged.
- No deviation.
- Probes it ran, none a gate: the plant green over the pass; the plant over a scratch copy with the timeout at 60, red with no
  green line, and green restored; the lexicon's offenders.
- The main loop then observed the arm red at 60 and green restored over the pass commit.

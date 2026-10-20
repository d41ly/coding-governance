---
name: fallback-drain-strands-its-witnesses
description: a fallback stands in until a mechanism lands and is drained when it does, but the drain is global while the mechanism exists only on some adapters, and the witnesses written under the fallback stop being read
kind: class
universal: false
---

# A fallback's drain strands what it covered

## Symptom

A design puts a fallback in place until a mechanism lands, then drains it. Two things go wrong at the drain.
- The mechanism depends on a capability not every adapter has, such as an event one harness lacks, yet the drain
  removes the fallback everywhere.
- The records written under the fallback are now read by readers that know only the new witness. So the builds that
  crossed the drain re-derive as unratified or unplaced.

## Where it bit

dClosedLoop's whole-design audit, 2026-10-18
(`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`, M14 and M15). RC-9's
intake fallback drained globally, though Codex has no prompt-submit event. And builds witnessed "intake not
installed" had no reader once the readers were re-pointed.

## The fix

- Drain per adapter: only where its capability table declares the event, keeping the fallback in force for any other.
- Keep the fallback's witnesses readable, keyed per adapter. The readers accept the fallback witness at any time
  from an adapter without the capability, and from any other only before that adapter's own drain landing. Or the
  drain backfills marked records.
- Probe a planted adapter without the capability, and a build that crosses the drain.

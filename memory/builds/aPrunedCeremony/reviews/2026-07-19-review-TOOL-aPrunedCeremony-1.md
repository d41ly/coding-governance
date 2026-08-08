# Pre-code build-readiness review — aPrunedCeremony (wf_539c5419)

**Status:** pre-code review · 2026-07-19 · 3 code/new-scope specs (PLAY-4, TOOL-1, TOOL-2) × review →
skeptic · 8 raw, 7 confirmed (2 HIGH, 4 MED, 1 LOW), all folded before any code was written.

Two HIGHs were genuine build-breakers the specs would have shipped:

- **PLAY-4 HIGH** — `tools/memory-tree/adopt-memory-tree.sh:50` is the GENERATOR that scaffolds
  `IN-FLIGHT.md` into every adopter, carrying the retired `pushed:<sha>` vocab verbatim (the same
  generator→artifact relationship as `HYGIENE.template.md`→`HYGIENE.md`). S2 missed it → the next
  `--scaffold` resurrects the vocab. AC2's literal-`pushed:<sha>` grep also missed the
  `pushed:/merged:<sha>` self-prune spans. → PLAY-4 rev-4: added the generator + kit-version bump,
  broadened AC2 to `grep -rIn "pushed"`.
- **TOOL-1 HIGH** — the two Python self-test legs run under a dynamically-resolved `$PYBIN`; the
  `{name,argv}` model + canary launcher-set can store neither `"$PYBIN"` (canary-illegal) nor a fixed
  `"python3"`/`"python"` literal (reds on Windows / Debian CI respectively). → TOOL-1 rev-4: added a
  `$PYBIN` substitution rule (store `"python3"`, substitute the resolved `$PYBIN` at exec) + AC5.

MED/LOW folded: PLAY-4 S3 corrected (live rows are bare `merged`, migrate to `merged:<sha>`, not a
nonexistent `pushed:<sha>`); TOOL-1 canary grep pinned to `argv[1..]` script paths; TOOL-1 canary is
a `gate-legs.json` entry not a `run-gates.sh` leg; TOOL-2 named the `GOV_GATE_CMD` seam and pinned
ref-classification to the 3rd field with a differently-named-local-ref fixture case.

Refuted (1): not enumerated. PLAY-1/2/3 (doc rewords) were reviewed at rev-2 (wf_2f11fd07) and not
re-reviewed here — no new mechanism.

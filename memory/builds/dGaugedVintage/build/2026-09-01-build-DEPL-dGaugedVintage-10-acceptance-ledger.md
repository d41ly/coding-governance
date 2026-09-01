**Serves:** journal DEPL-dGaugedVintage-10

# Acceptance ledger — DEPL-dGaugedVintage-10, the measurer's own currency

**Evidences:** DEPL-dGaugedVintage-10

- AC1 — `python tools/govkit/govkit.py update --target <adopter> --to origin/main` — prints
  `measurer: this gov checkout IS the remote's advertised head (3fb57da7)` and proceeds.
- AC2 — `python tools/govkit/govkit.py update --target <adopter>` — from this feature branch it
  prints `measurer WARNING: diverged — measuring at 8c02ce3a, origin advertises 3fb57da7`, naming
  both shas. `origin/main` really had moved past this build's base, so the verdict is correct.
- AC3 — `resolve_measurer_currency` — called directly against a scratch repo whose `origin` points
  at a path that does not exist: returns `unverified | origin did not answer (exit 128)`, and the
  `current` verdict is False. Unreachable is announced, never read as current.
- AC4 — `git update-ref refs/remotes/origin/main d65da7ab~5` — moving the tracking ref backwards
  without fetching changed the verdict not at all: the probe still reported against `3fb57da7`. It
  reads the advertisement, not the ref.
- AC5 — amended rev-3 — `merge-base --is-ancestor` IS called, but only behind a `git cat-file -e`
  presence check; when the advertised object is absent that absence is the verdict and no
  object-walking command runs. `grep -c rev-list` over the probe returns 0.

- S3 gate — `python tools/govkit/selftest.py` — four permanent arms drive the probe directly: an
  unreachable remote is `unverified` and never `current`, the verdict names the remote, the memo
  serves a second call, and the test seam yields `unverified` rather than a clean answer.

## Two defects this unit introduced, both caught before landing

- The probe spawns one `ls-remote` per PROCESS and `selftest.py` spawns a fresh `update` dozens of
  times, so the suite blew its 600 s ceiling on network round-trips. A named seam,
  `GOVKIT_NO_REMOTE_PROBE`, turns it off for the harness and yields `unverified` — announced, never
  read as up to date, so a run with the probe off cannot pass for a clean one.
- The first message contained the word `current`, and an existing arm asserts that string appears
  NOWHERE in an update run. Reworded. That is this repo's `absence-assertion-over-whole-file-text`
  class, hit by a new message colliding with somebody else's absence assertion.

## What this ledger does not claim

No distance. The probe answers ahead / behind / diverged / unverified and never how far, because an
advertisement returns a sha and not objects. It WARNS and never refuses (§8 F1), so a red bar will
not stop an operator measuring from a stale clone — only tell them they are.

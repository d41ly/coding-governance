# Acceptance ledger — aReapedTicket

**Serves:** journal TOOL-aReapedTicket-1 TOOL-aReapedTicket-2 TOOL-aReapedTicket-3

One line per numbered criterion, in the two forms `memory/HYGIENE.md` allows and no third. Every
OBSERVED token below names something that was actually run in this build; the two AMENDED lines name
the revision that changed the criterion and the §9 entry that logs it.

The suite figures come from one full run of `bash tools/run-gates/run-gates.turnstile.test.sh` on
node `a`, 2026-08-27: **PASS, 63 assertions, rc 0, 821 s**. The red side comes from the same arms run
against the runner at this build's pinned BASE `f1be0b49`: **11 of 20 assertions FAILING**.

**Evidences:** TOOL-aReapedTicket-1
- AC1 — `run-gates.turnstile.test.sh` arm 15 — a waiter interrupted with `SIGINT` while queued leaves
  no ticket. Red at BASE, where the same fixture left one.
- AC2 — `run-gates.turnstile.test.sh` arm 15 — the same for `SIGTERM` and `SIGHUP`; all three signals
  are exercised, not one.
- AC3 — `run-gates.turnstile.test.sh` arm 8 — an uncontended run still releases its beacon on every
  signal the trap catches, unchanged, so the added trap is superseded rather than competing.
- AC4 — `run-gates.turnstile.test.sh` arm 21 — the ticket line number is below the trap's, which is
  below the acquire loop's; graded structurally, never against a comment.
- AC5 — `timeout -s INT -k` — the runner EXITS on the signal instead of resuming the loop, observed
  as the absence of a `SIGKILL` escalation. rev-1's spelling failed this on all three signals, which
  is what produced rev-2.
- AC6 — `run-gates.turnstile.test.sh` arm 8 — the claim-time beacon trap re-exits too, so an
  interrupt in that window cannot leave the run holding a lock it has given away.

**Evidences:** TOOL-aReapedTicket-2
- AC1 — `run-gates.turnstile.test.sh` arm 16 — a dead-PID ticket with no beacon at all is swept and
  the bar acquires. Red at BASE, where the same fixture reached `WAIT EXPIRED` and left the ticket.
- AC2 — `run-gates.turnstile.test.sh` arm 17 — a ticket whose PID is ALIVE and whose stamp is past
  the bound is swept, and the reason names the age rather than the PID. Against the unmodified runner.
- AC3 — `run-gates.turnstile.test.sh` arm 18 — a LIVE waiter's fresh ticket is NOT swept. The
  negative control, and it passes against BOTH the base and the fixed runner, as a control must.
- AC4 — `run-gates.turnstile.test.sh` arms 16 and 17 — each sweep prints its reason, and the two
  reasons are asserted to be distinguishable, so a silent reaper cannot pass.
- AC5 — `run-gates.turnstile.test.sh` arm 19 — with no beacon held the queued line reports the queue
  instead of claiming a holder, and the greppable `queued at position` tail is unchanged.
- AC6 — `run-gates.turnstile.test.sh` arm 20 — a run that cannot take a ticket fails open at once:
  measured 35 s against the 7200 s bound it would otherwise have burned, and 182 s-and-still-waiting
  at BASE.
- AC7 — `hdrkey queued_from` — the same run records `unticketed`, distinct from `expired`, so the
  "an expired run is never 0" invariant stated beside that block stays true.

**Evidences:** TOOL-aReapedTicket-3
- AC1 — `git show f1be0b49:tools/run-gates/run-gates.sh` — the arms were run against the runner at
  BASE before they landed and 11 of 20 assertions FAILED, including the ticket leaking on all three
  signals and the no-ticket run caught still waiting after 182 s.
- AC2 — `bash tools/run-gates/run-gates.turnstile.test.sh` — PASS, 63 assertions, above the raised
  `FLOOR_ASSERTIONS` of 62.
- AC3 — `skipped` — arms 19 and 20 carry counted skip branches, so an arm that cannot establish its
  fixture announces itself rather than shrinking the total. Observed live: arm 19 reported two SKIPs
  under full-suite load at its original 15 s window, which is what moved the window to 45 s.
- AC4 — `bash tools/check-testsuite-counts.sh` — clean; the suite still satisfies the executed-count
  shape that leg derives from `tools/gate-legs.json`.

## What this ledger does NOT evidence

Two things, stated because a ledger that quietly omits them is worth less than one that does not.

**The closing Tier-2 diff review did not run.** This session's operating instructions forbid invoking
the agent and workflow tools without an explicit request, and `memory/guides/BUILD-METHOD.md` M8's
review is exactly that. So the units are gate-verified and self-reviewed, and the adversarial pass
the method asks for at a Tier-2 landing is owed.

**The landing is not this build's own.** `--preflight` refused to start a run at all — two other
builds held non-terminal run-state files — so there is no `RUN.md`, no phase witness and no `--close`
for this build, and the merge to `main` was made on an explicit owner instruction rather than under
the unattended mandate. `TOOL-aReapedTicket-5` records the refusal's cause.

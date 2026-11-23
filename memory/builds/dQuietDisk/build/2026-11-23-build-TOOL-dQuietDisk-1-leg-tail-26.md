# TOOL-dQuietDisk-1 leg-tail 26 — run-gates turnstile failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** run-gates turnstile
- **Hash:** a320bd6259693e7086d4d71d36a7475ebe180382
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
  ok   — the third bar's queue line counts two of two slots held and names both holders' pids
  ok   — the third bar's header records slots 2
  ok   — the two holders' headers record slots 1 and 2
  ok   — the dead slot was reaped once
  ok   — the bar behind it claimed and ran
  ok   — the live holder of slot 1 ran on, its nonce untouched
  ok   — a run whose slot was re-claimed left the successor's beacon
  ok   — a release left the other slot's holder in place
  ok   — the outer bar held slot 2 beside slot 1's holder
  ok   — a runner started by the slot-2 holder's leg nests
  ok   — a bar at the default count writes neither slots nor slot
  ok   — a bar at the default count printed no slots clause
  ok   — half: the bar beside a holder dispatched at width 2 and its header records 2
  ok   — full: the bar beside a holder dispatched at width 4 and its header records 4
  ok   — half beside a holder: GATE_JOBS=3 dispatched at 3
  ok   — a bar holding the only held slot printed no dispatch line
  ok   — and its header records the profile's width 4
  ok   — bar memA paused on the shared host reading
  ok   — bar memB paused on the shared host reading
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
template: 115d1da4 built
  ok   — a doc-only bar was admitted on the docs key and finished while the non-doc holder still ran
  ok   — the doc-only bar took no place in the queue
  ok   — its header records queued_from docs
  ok   — the live doc-only bar's beacon stood while its neighbour released
  ok   — the finished doc-only bar's own beacon is gone
  ok   — a runner started by a doc-only bar's leg nests
  ok   — a non-doc bar beside a doc-only holder waited 0s and took no shared width
  ok   — a full bar with GATE_DOCS_BASE set took a slot as a non-doc bar
  ok   — a dead docs beacon was swept by the next doc-only bar
  ok   — two bars in one worktree never held at once (peak 1)
  ok   — the second bar's queue line names this worktree's holder
  ok   — two worktrees of one repository held at once (peak 2)
  ok   — a slot whose nonce changed after its pid was read survived the reap
  ok   — a docs beacon whose nonce changed after its pid was read survived the sweep
  ok   — a one-slot bar never ran beside its worktree's slot-2 holder (peak 1)
  ok   — its queue line names the slot-2 holder in its own worktree
  ok   — a doc-only bar never ran beside its worktree's holder (peak 1)
  ok   — the doc-only bar said it waits for its worktree's holder, naming it
  ok   — a non-doc bar never ran beside its worktree's doc-only bar (peak 1)
  ok   — its queue line names the docs key its worktree holds
  ok   — a docs beacon with no pid and no heartbeat, older than the ttl, was swept
  ok   — a docs beacon whose live holder's heartbeat outlived its ttl was swept

FAIL (run-gates turnstile, 148 assertions)
```

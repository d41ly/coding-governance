# Acceptance ledger — TOOL-aHonedRuleset-8

**Serves:** journal TOOL-aHonedRuleset-8

Tier-2 · node a · 2026-09-06

`check-microformats` was declared, tracked, and reached NOBODY for its entire life: the conditional
mark put it behind an operator typing its id, which no default and no runbook led anyone to do. It
joins the default selection, gets an anchored runbook section, and the unit builds the two selfcheck
arms that would have caught the state it fixes.

## Acceptance criteria

**Evidences:** TOOL-aHonedRuleset-8

- AC1 — MET, two-sided — `resolve_selection(reg, descs, 'default', [], None)` returns **7** ids and
  `check-microformats` is one, against 6 and absent at base; and `all_kits(descs)` now reaches it,
  which the conditional mark used to block
- AC2 — MET — `grep -c '^selectable'` on the descriptor returns 0
- AC3 — MET — `requires = ["playbook"]` is untouched, present in the descriptor
- AC4 — MET — the id appears in `tools/govkit/registry.toml`
- AC5 — MET, with the arm RENAMED at rev-9 to `exactly 5 SIDE|rendered rows`. The selftest
  arm `the default selection previews exactly 5 SIDE|rendered rows` is `ok`. FIVE, not the four
  every earlier rev wrote: that count and its sibling `ORDER|project-owned` are declared
  tree-state snapshots — the arm's own comment says the count moves when the tree does — so S1
  adding an entry moves them by construction. No rev caught it, and it would have red this
  unit's own landing on two arms behaving correctly
- AC6 — MET — `bash tools/check-install-prefix.sh` reports `carried-prefix clean — 118 recorded
  file(s), 5 hand-justified, none rising`. The wiring sentence uses the descriptor's `{prefix}` argv
  precisely so it does not raise the count
- AC7 — MET — `git diff` over `coding-governance-agents.template.md` and `AGENTS.md` across this
  unit's commit is empty: no charter byte moved
- AC8 — MET — `python tools/govkit/refusal_join.py` reports **246** branches, exit 0
- AC9 — MET — `grep -c 'check-microformats' WIRE-INTO-PROJECT.md` returns **4**: the `--kits` id, the
  anchor, the body sentence and the wiring instruction. S3 REQUIRES the `{prefix}` argv form for that
  fourth line; the leg-name-only spelling carries no `check-microformats` substring, and rev-7
  offering the two with an `and/or` made this threshold unreachable
- AC10 — **NOT MET AS WRITTEN, and its `GATE_SELFTESTS=1` clause SKIPPED on an explicit owner
  directive mid-run.** The ordinary bar came back RED on four legs; three reproduce at base and the
  fourth was check 23. What compensates for the skipped clause: `python tools/govkit/selftest.py` was
  run in full and reports **all arms held**, which is the suite AC16 names
- AC11 — MET in all three halves — NO `runbook-parity:` line names `check-microformats`, the census
  reports **8 anchored section(s)** against 7 at base, problems fall **18 to 17**, and the `playbook`
  section's derived body still contains `What the renderer cannot decide for you`, so it was not
  re-parented
- AC12 — MET, both halves, staged on `check-placeholders.kit.toml`, a descriptor this unit does
  not otherwise edit. With `why_conditional` removed, selfcheck exits non-zero naming
  `check-placeholders`; restored, exit 0. The arm is proven over the population, not over its
  own fix
- AC13 — MET — S4's arm found `check-line-length` the moment it was wired, which is the violator the
  original defect never pointed at. The descriptor gained a `why_conditional` lifted from its own
  header argument, and selfcheck returned to exit 0
- AC14 — MET — restoring this unit's OWN base state in `tools/govkit/registry.toml` and its
  descriptor — the id out of the default set, the conditional mark back — makes selfcheck exit
  non-zero naming `check-microformats` as required-by-a-default-member and reached by no
  declared selection; restored, exit 0
- AC15 — MET — over the live registry S5's violating set is EMPTY, naming none of `drift-audit`,
  `playbook-render` or `unattended`. That is what proves the specified quantifier shipped rather than
  the literal `default-reachable` reading, which would have red four innocent entries
- AC16 — MET — `python tools/govkit/selftest.py` reports **all arms held** over 1127 lines with 0
  failures, including all four new arms and the liveness half asserting the gov copy is green BEFORE
  either break is provoked
- AC17 — MET, and the round-3 audit rewrote it after EXECUTING `govkit.py intake`. §2's literal
  three lines do not run: `intake` exits 2 with *the selected kits need answer(s)
  playbook_path*, and `grep -c -- '--answer' WIRE-INTO-PROJECT.md` is 0, so the runbook's own
  line refuses identically. With the answer supplied `intake` exits 0, the payload is ABSENT —
  the third outcome, which rev-6's two-outcome form could not report — and `apply` then prints
  `gate legs: ORDERED, not emitted`
- AC18 — MET — `python tools/govkit/refusal_join.py` reports 246 against the 244 measured
  before, an exact **+2**, with `BRANCH_PIN` unmoved at 217 and S6's ledger entry naming both
  branches, their armed status, and the sibling ruling that defers the raise

## The three rounds this spec cost

Round 1 BLOCKED with 2 blockers, round 2 with 1, round 3 with 1 — not strictly smaller, so the loop
was NON-CONVERGENT and stopped, with the surviving blocker DISPOSED by fold. Twice the blocker was
introduced by the previous round's own fold: rev-6 answered a correct mechanism on the wrong command,
and rev-7's two folds graded each other into an unsatisfiable pair. The liveness half of AC16's
fixture is what caught my first copy of gov omitting `.git`.

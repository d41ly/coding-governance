# Acceptance ledger — TOOL-aHonedRuleset-5

**Serves:** journal TOOL-aHonedRuleset-5

Tier-2 · node a · 2026-09-06

One rule — how to compute the sha for a kickoff manifest's `last-audit` stamp — was written out in
seven places across five files in two spellings that already disagreed. Commit A gave it one prose
home and one machine home and armed a parity row across them, changing nothing about what the rule
says. Commit B changed what it says: `sha = HEAD on any branch`.

## Acceptance criteria

**Evidences:** TOOL-aHonedRuleset-5

- AC1 — MET — `grep -c 'merge-base <remote>/<default> HEAD'` returns 0 in all four carriers: the
  engine, the manifest template, the runbook and `manifest-check.sh`
- AC2 — MET — the engine is **143 bytes** smaller than before this unit, against a floor of 90, and
  the `skills/session-kickoff/SKILL.md` row of `tools/template-size-highwater.txt` was bumped DOWN to
  match with no `TEMPLATE-SIZE WARN`. The first pointer draft came in at 84 and was tightened rather
  than the criterion moved
- AC3 — MET — `grep -c 'STAMP_SHA_RULE=' skills/session-kickoff/manifest-check.sh` returns 1: one
  machine home, hoisted above `RETROFIT` so that string interpolates it instead of re-typing it
- AC4 — MET, **the FIRST observed RED**, in commit A and over text commit A does not semantically
  change. One word of the template's expression changed and `check-playbook-parity.sh` exits 1:
  *the playbook states `gitmerge-fake…` where `manifest-check.sh` owns `gitmerge-base…`*
- AC5 — MET, **the SECOND observed RED**, in commit B and over the pattern that ships. `HEAD` changed
  to `TAIL` and the gate exits 1 naming both sides; restored, exit 0. A third, unplanned observation
  fell out of the intermediate state: with both sources moved and the row not yet re-anchored, the
  anti-vacuity arm fired with *an extraction matched NOTHING, so the pair was never compared*
- AC6 — MET — `bash tools/check-playbook-parity.sh` exits 0 on the unmodified tree, six pairs
- AC7 — MET — both pinned header anchors are present exactly once: `no longer playbook-only` and the
  scope-limit line. Both were worded to survive S11's rewrite, and did
- AC8 — MET in BOTH halves, and the positive half is what proves S12 ran. The three old spellings —
  including the CONCRETISED `merge-base origin/main HEAD` that the rev-5 fold added this criterion
  for — return 0 across `skills/`, the runbook and the instantiated manifest; and `on any branch`
  returns exactly 1 in each of the three carriers
- AC9 — MET — `bash skills/session-kickoff/manifest-check.test.sh` reports **PASS (62 assertions)**,
  0 failures, so the constant's hoist and its rewrite broke no fixture
- AC10 — MET, and this is the unit's own dogfood. `bash skills/session-kickoff/manifest-check.sh`
  exits 0 after commit B **on this FEATURE branch**, with a stamp written by the new rule. That is
  the exact run `KICK-cSettledDocket-1` records failing three times under the old rule
- AC11 — MET — `KICK-cSettledDocket-1` reads CLOSED naming `builds/aHonedRuleset/`, and one new row,
  `KICK-aHonedRuleset-1`, names `AGENTS.md` and its source template as the carriers the fix leaves
  stale. Both rows had to be rewritten twice to fit check 7's entry cap
- AC12 — **NOT MET AS WRITTEN.** The push-boundary bar came back RED on four legs, none on this
  unit's subject; `playbook parity` and `kickoff-manifest ratchet` are both green
- AC13 — MET — the new row's STATED side resolves ALONE to a non-empty value equal to what
  `STAMP_SHA_RULE` owns. Run before the gate, because a row whose two sides are both empty AGREES

## What the entry cap taught

Check 7 caps an index entry at 300 and the awk that grades it counts BYTES here — the gate's own
header says it does not pin which. A 300-CHARACTER row carrying `·`, `§` and `→` measures 305 and
reds. Both KICK rows were rewritten twice before they fit.

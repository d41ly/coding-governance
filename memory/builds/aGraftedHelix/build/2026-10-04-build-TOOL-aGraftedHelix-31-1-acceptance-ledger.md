# Acceptance ledger — TOOL-aGraftedHelix-31

**Serves:** journal TOOL-aGraftedHelix-31

Node `a`, 2026-10-05. The build commit is `d65ee07d`, over the pass's parent `c54278c1`; the spec
stayed at rev-1, because nothing built diverged from it. No merge bar and no self-test suite ran in
this pass. Both self-tests' new arms ran as slices generated into the session scratchpad with the
kit dir pinned: the driver suite's prologue, its `seed_handoff_bar` and the `--settle` block's
fixture with the five new arms; the kit gate suite's prologue with check 51's block. Their fixture
repositories sat under `%TEMP%`. Every staged break of the driver was a scratch copy of the driver
beside a copy of its library, never an edit in the kit. The whole suites, and the bar, are the main
loop's, at VERIFYING.

**Evidences:** TOOL-aGraftedHelix-31
- AC1 — `--settle tRun` — the driver slice at the build bytes printed `PRE n=20` then `SLICE n=39 st=0`: after `--handoff tRun` the claim read `held`; the settle under `CLAUDE_CODE_SESSION_ID=owner-session` exited 0 and staged the record at `LANDED`; the claim then read `landed` with the record's keepalive and its `fixture-session`, and `--claims` printed `landed terminal` for the slug.
- AC1 — `held` — the same slice against the parent's driver printed `FAIL GH31 AC1 the claim reads landed: expected [landed], got [held]` and `--claims` read `held held`.
- AC2 — `--settle tAwork` — green in the same slice, the claim reading `aborted`; against the parent's driver it printed `FAIL GH31 AC2 the dead holder's claim reads aborted: expected [aborted], got [live]`.
- AC3 — `--settle tAkept` — green in the same slice, `work-landed-at` written and the claim ref at its seeded sha; a scratch driver writing `aborted` on the legacy branch printed `FAIL GH31 AC3 the legacy settle left the claim unmoved` with the sha moved.
- AC4 — `unattended: claim not written — tRun is held live by session` — green in the same slice, exit 0, `LANDED` staged and the foreign claim ref unmoved; against the parent's driver the line was missing.
- AC5 — `RUN_CLAIMS` — green in the same slice, `for-each-ref refs/gov` empty on the origin; a scratch driver with the status write outside its `RUN_CLAIMS` guard printed `FAIL GH31 AC5 the switched-off settle created no claim` naming the created `refs/gov/runs/tRun`.
- AC6 — `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh --skip 28` — over the real tree with the parent's driver, 541 s: `check 51 graded 359 function(s) in 10 shell file(s) of this kit, 4 writing a terminal phase, 0 exempt`, then the findings failure naming `tools/unattended/unattended.sh:6011 run_settle()`.
- AC6 — `run_settle` — the same command over the fixed driver, 518 s: the same report line, no check 51 failure, and check 48's report line with no hit naming `run_settle`. Both runs also printed four check 24 roster lines, identical before and after, which are this run's own record and not this unit's.
- AC7 — `ghostfn()` — the kit gate slice printed `SLICE n=13 st=0`: the staged writer of `phase ABORTED` redded the findings failure naming it, the same function on `TERMINAL_CLAIM_EXEMPT_FNS` was silent, `ghostfn` redded by name, the respelled `"phase"` key redded the liveness failure, and the control printed neither failure with `writing a terminal phase, 0 exempt`.
- AC7 — `TERMINAL_CLAIM_EXEMPT_FNS` — the same slice with check 51's block deleted from the fixture's leg printed `SLICE n=13 st=1`, every red arm failing and both list `mutate` calls reading as fixture no-ops.
- AC8 — `grep -n -- '--settle' memory/guides/UNATTENDED-STOPS.md` — line 235 opens the section 7 sentence naming `--settle` with `landed` and `aborted`; `bash tools/unattended/adopt-unattended.sh --check` printed `in sync` and exited 0; the template's diff from `c54278c1` is `@@ -1 +1 @@` and `@@ -235,2 +235,4 @@` alone.
- AC9 — `bash tools/check-kit-versions.sh` — at `d65ee07d` printed `kit-versions: clean — 16 declared carrier(s) under tools/`, and `python tools/govkit/govkit.py epoch --base c54278c13` printed `epoch: unattended · clean · 1.78`; the protocol and verbs templates each show `@@ -1 +1 @@` alone.
- AC10 — `python tools/memory-tree/check-arms.py --check` — printed nothing and exited 0 after the liveness message lost its interpolated tail; `grep -c 'check-unattended.sh' tools/unattended/unarmed-branches.txt` printed 8 at the parent and at the build commit.

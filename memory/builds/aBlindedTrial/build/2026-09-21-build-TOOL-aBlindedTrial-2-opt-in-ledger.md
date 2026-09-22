# The spec audit becomes opt-in — what was built, and the acceptance ledger for units 2–5

**Serves:** journal TOOL-aBlindedTrial-2 TOOL-aBlindedTrial-3 TOOL-aBlindedTrial-4 TOOL-aBlindedTrial-5

Node `a`, 2026-09-20/21, branch `branch/spec-audit-opt-in` off `b7dee206`. Four units built in
parallel by four agents with disjoint write sets, committed per unit by the main loop, then one
closing diff review in two rounds (`reviews/…closing-diff-round1.md` CLEAN WITH FIXES, 0 blockers,
2 highs raw, 8 confirmed; `…round2.md` CLEAN WITH FIXES, 0 blockers, 0 highs, 5 items) and two
folds. The build took no spec audit: the owner ruled the audit opt-in in the session of
2026-09-20 and this is the first build not to declare it.

## The shape that shipped

A build README declares `spec-audit: <date>` in its front matter or it does not. The driver reads
the key at the pinned BASE beside `authorized-by:`, pins it once as the run fact `spec-audit`, prints
what it found at preflight (with a recommendation for two or more units or a FORKED spec), and its
`specs-audited` grader keys a term zero on the BASE-derived value: undeclared → `not owed`,
announced; declared → today's rule; a RUN.md fact that disagrees with BASE → `fail 53`. `DOD_CORE`
and `DIRECTIVES_CORE` did not move, so no adopter floor moves. The harness runs its AUDIT stage only
when the caller passes `specAudit`, and says `NOT-OWED` with null counts otherwise. The fan-out hook
denies a direct `Workflow` call with `kind: "spec-audit"` unless the README under `args.repo` at
`dirname(reviewDir)` declares the key, ties every subject to that build, and fails closed on a call
it cannot place. M4 reads "owed only where the build declares it", the tier rule no longer equates
Tier 2 with a pre-code adversarial review, and `TOOL-aBlindedTrial-6` records the supersession.

Cost of the build itself: 4 scouts (1.44 M tokens), 4 builders (0.96 M), two review rounds (1.75 M
and 1.51 M), two folds (0.26 M and 0.30 M) — about 6.2 M tokens of workflow agents, main loop not
counted.

## Evidence per unit

**Evidences:** TOOL-aBlindedTrial-2
- AC1 — `--status` — after `--preflight` on a fixture whose README at BASE carries `spec-audit: 2026-09-20`,
  the status line carries `spec-audit 2026-09-20`; the key on the run branch only pins nothing.
- AC2 — `--preflight` — a second preflight leaves one `spec-audit` fact row (`grep -c` 1).
- AC3 — `--close` — undeclared build, CLOSED unit, no record: stdout carries `specs-audited — not owed`
  and not `a CLOSED unit is named by no tracked spec-audit record`.
- AC4 — `--close` — declared at BASE, no record: the close blocks and names the missing record.
- AC5 — `fail` 52 — `spec-audit: later` refuses at `--preflight`; the arm is a positive `hit`, and
  the same branch takes a bare `spec-audit:` (round-1 F4).
- AC6 — `--preflight` — `unattended: spec-audit — not owed (opt-in)` on an undeclared build, the
  recommendation clause on two units and on a FORKED spec, `opted in by README spec-audit:` when declared.
- AC7 — `grep -n TOOL-aBlindedTrial-6 tools/unattended/unattended.sh` — the ruling comment at :459;
  `grep -c MUST-by-default` over the `specs-audited` grader's non-comment lines is 0.
- AC8 — `bash tools/check-kit-versions.sh` — exit 0 with every `KIT_UNATTENDED_VERSION` carrier at
  1.25, after `bash tools/unattended/check-unattended.sh` exit 0.

**Evidences:** TOOL-aBlindedTrial-3
- AC1 — `run_wf` — `"specAudit":1` ends in `THROW` naming `specAudit` and the date shape.
- AC2 — `run_wf` — `UNITS` without `specAudit`: `log:audit stage: OFF by declaration`, no `workflow` line.
- AC3 — `"roster":[{` — present on the OFF run, `phase:Disposal` present, no `HELD AT HAND-OUT`.
- AC4 — `RESULT` — `"verdict":"NOT-OWED"`, `"ran":false`, `"blockers":null`, no DEGRADED in the note.
- AC5 — `run_wf` — `subjects` beside no `specAudit` ends in `THROW` naming the pairing; `round: 2`
  too since round-1 F6.
- AC6 — `run_wf` — `UNITS` with `"specAudit":"2026-09-20"` carries `workflow:` and `wargs:` with the
  spec-audit kind as before.
- AC7 — `node tools/workflows/check-workflow-syntax.js` — exit 0; `bash tools/workflows/check-verifier-fanout.sh`
  exit 0; `diff` between `unattended-build.template.js` and the render shows only the token lines;
  both carriers read `unattended-build@1.2`.

**Evidences:** TOOL-aBlindedTrial-4
- AC1 — `node tools/hooks/agent-cap.js` — `kind: "spec-audit"` with a valid `repo` and a `reviewDir`
  under the undeclared fixture build exits 2 naming `TOOL-aBlindedTrial-6` and `spec-audit:`.
- AC2 — `spec-audit: 2026-09-20` — the same payload exits 0 once the README declares it.
- AC3 — `spec-audit: yes` — exits 2; a key only inside a fenced body block exits 2.
- AC4 — `args` — as a JSON string, AC1 and AC2 hold; `kind` `diff-review` or absent exits 0 on the rule;
  `["spec-audit"]` exits 2 since round-1 F1.
- AC5 — `repo` — a number exits 2 naming the field; a `reviewDir` with no `builds/<slug>/` segment or
  a `..` segment exits 2; a subject under another build or spelled absolute exits 2 (rounds 1 and 2).
- AC6 — `agent-cap.js` — an unreadable README path exits 2 with a deny, never a stack trace.
- AC7 — `bash tools/check-kit-versions.sh` — exit 0, both halves of `agent-cap@` moved;
  `grep -c 'tools/' tools/hooks/agent-cap.js` unchanged against the install-prefix registry's pin.

**Evidences:** TOOL-aBlindedTrial-5
- AC1 — `grep -n 'spec-audit' memory/guides/BUILD-METHOD.md` — four hits, M1's loop sentence and M4's
  opening among them; `grep -c 'review every unreviewed spec'` is 0.
- AC2 — `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` — `template-size OK`, 27275
  of 27648 bytes, under the 27278 the render measured before.
- AC3 — `bash tools/check-kit-versions.sh` — exit 0, every `memory-tree@` marker at 2.80; the parity
  gate renders `BUILD-METHOD.template.md` byte-identical to the live copy.
- AC4 — `bash skills/session-kickoff/manifest-check.sh` — exit 0 after the `last-audit` re-stamp at
  85d930a9 with its delta line in the unit-5 commit.
- AC5 — `grep -n 'TOOL-aBlindedTrial-6' memory/DECISIONS.md` — one row at :183 naming
  `specs-reviewed`, `spec-audit:` and the trial report.

## Left-shifts the reviews asked for and this build did not take

- A class-level check that a spec's §7 leg line names every leg whose `guard` its §4 files trip
  (round 1, F7). Both inputs are machine-readable; it is a `check-spec-tokens` sibling. Backlog row.
- A project-wide "audits owed by default" declaration for an adopter that wants today's rule on
  every build without a per-README key (spec 2, §3). Backlog row.
- The driver suite's assertion floors were not raised for the +11 arms this build added (they are
  `-ge` floors and stay green); the file's convention is a per-fold raise.

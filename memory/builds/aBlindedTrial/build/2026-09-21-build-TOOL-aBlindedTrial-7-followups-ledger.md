# The three follow-ups — what was built, and the acceptance ledger for units 7, 8 and KICK-1

**Serves:** journal TOOL-aBlindedTrial-7 TOOL-aBlindedTrial-8 KICK-aBlindedTrial-1

Node `a`, 2026-09-21, branch `branch/spec-audit-followups` off `0e61932d`. Three units built in
parallel by three agents with disjoint write sets, committed per unit, then one closing diff review in
three rounds (`reviews/…kick1-closing-diff-round1.md` CLEAN WITH FIXES 0/1/5/6, `…round2.md` CLEAN WITH
FIXES 0/1/4/7, `…round3.md` CLEAN WITH FIXES 0/0/1/6 by blocker/high/medium/low) and three folds. No
spec audit was declared for this build.

## The shape that shipped

**Unit 7.** `SPEC_AUDIT_DEFAULT="<date>"` in `.unattended.conf`: `check_authorization` sources the
BASE conf blob in a subshell — blanked first, the eval proving it finished through a sentinel on fd 3 —
when the README front matter carries no `spec-audit=` line; a non-date is `fail 54`, an unfinished eval
`fail 55`, a README key even malformed still wins (`fail 52`), and `AUTH_SPEC_AUDIT_DERIVED` is set only
after both halves. Third preflight spelling `opted in by project default`; the key in four carriers for
check 22; `agent-cap.js` rule 0 re-parses the worktree conf last-wins. Unattended 1.27, agent-cap 1.17.

**Unit 8.** `check-spec-tokens.py` gains a `guards` arm behind `SPEC_GUARD_LEGS_CUTOFF` (2026-09-22):
the §4 Files touched sub-head's path-shaped tokens, joined against every manifest guard carried by
`BROAD_LEG_FLOOR` (5) or fewer legs — breadth, not depth, after round 1 — with git-pathspec semantics; a
directory token declares a prefix only with two or more real segments, so the corpus's "No file under
`tools/` is touched" sentence declares nothing and is a NEAR row; a spec with no Gates heading is never
joined; the hit token is `<leg> <- <path>`. Memory-tree 2.81.

**KICK-1.** The kickoff engine's Step 3 puts one `AskUserQuestion` when the DoR is a design pass and the
project's method makes the audit opt-in, recommending by roster size or an open fork, writing the key
on a yes; it does not ask when the README already carries the key or the project declares a default;
Step 5's `## open` line records the answer in three spellings; Step 5b never asks. 18428 of 18432 bytes.

Cost: 2 scouts (0.43 M tokens), 3 builders (0.62 M), three review rounds (1.81 M, 1.67 M, 1.56 M),
three folds (0.30 M, 0.44 M, 0.48 M) — about 6.9 M tokens of agents, main loop not counted.

## Evidence per unit

**Evidences:** TOOL-aBlindedTrial-7
- AC1 — `--preflight` — with `SPEC_AUDIT_DEFAULT="2026-09-21"` at BASE and no README key, the line
  reads `opted in by project default SPEC_AUDIT_DEFAULT: 2026-09-21` and the fact is pinned.
- AC2 — `--preflight` — the default on the run branch only: `not owed (opt-in)`; the subshell blanks
  the key first so a working copy cannot leak in.
- AC3 — `fail 54` — `SPEC_AUDIT_DEFAULT="later"` at BASE refuses; `spec-audit: later` beside a valid
  default takes `fail 52`; an eval that does not finish takes `fail 55` (round 1, R2).
- AC4 — `--close` — declared by default, no record: the close blocks naming the unit.
- AC5 — `grep -c SPEC_AUDIT_DEFAULT` — ≥ 1 in `unattended.sh`, `.unattended.conf`, the example, the
  protocol template and its render; check 22 observed RED with the §8 row removed, then restored.
- AC6 — `node tools/hooks/agent-cap.js` — dated conf admits in both quote styles and with a trailing
  comment; a missing conf denies; a glued `#` denies (round 1, R8).
- AC7 — `SPEC_AUDIT_DEFAULT` — a non-date at the hook denies naming the key.
- AC8 — `bash tools/check-kit-versions.sh` — exit 0, `unattended@` 1.27 on every marker, `agent-cap@`
  1.17 on both halves.

**Evidences:** TOOL-aBlindedTrial-8
- AC1 — `python tools/check-spec-tokens.py` — with the cutoff blank the guards line announces OFF.
- AC2 — `scratch-guard self-test` — a post-cutoff fixture spec touching `tools/hooks/scratch-guard.js`
  reds without the leg named and passes with it.
- AC3 — `### Files touched` — the short spelling behaves as the long one.
- AC4 — `BROAD_LEG_FLOOR` — a guard carried by more than five legs is excluded and printed with its
  count; a one-segment root is a `NEAR` row and never joined (round 2, R1).
- AC5 — `<leg> <- <path>` — the composite waiver row consumes the hit; a bare `[leg]` row does not.
- AC6 — `[guards]` — a pre-cutoff spec prints no row; the summary counts what the arm graded.
- AC7 — `bash tools/check-kit-versions.sh` — exit 0, every `memory-tree@` marker at 2.81;
  `grep -c SPEC_GUARD_LEGS_CUTOFF memory/TEMPLATE-SPEC.md` is 2.

**Evidences:** KICK-aBlindedTrial-1
- AC1 — `AskUserQuestion` — Step 3 lines 153–158 carry the question, the recommendation and the
  write-on-yes.
- AC2 — `spec-audit:` — the same paragraph names the opt-in condition and the skip.
- AC3 — `## open` — Step 5 lines 208–209 carry `declared <date>`, `not declared (owner)` and `project
  default <date>`.
- AC4 — `grep -n 'never ask' skills/session-kickoff/SKILL.md` — line 231, inside Step 5b.
- AC5 — `template-size OK` — 18428 of 18432; `bash tools/check-wiring.sh --check` reports the installed
  engine matching tracked only in the primary tree, so its half is observed after landing (the
  junction points at the primary checkout).

## Left-shifts the reviews asked for and this build did not take

- The unattended driver's S6 init-block arm names `CORE_FLOOR`, `DISPOSITION_CUTOFF` and
  `RUNLOG_SESSION_VARS` as undefaulted at HEAD independently of this build (a pre-existing observation
  from unit 7's builder; region one of the suite was not run).
- `unattended-build.template.js` prose still names only the README key as the opt-in source; the
  harness's behaviour is unchanged by unit 7 (the caller passes `specAudit`), so it is a wording debt.
- With the leg-count floor at 5, `memory/` (2 legs) and `.claude/` (2 legs) now join, so a post-cutoff
  spec touching `memory/…` owes `recall floor` and `recall floor arms`; this is the rule working, stated
  here because it will be the first thing a session notices tomorrow.

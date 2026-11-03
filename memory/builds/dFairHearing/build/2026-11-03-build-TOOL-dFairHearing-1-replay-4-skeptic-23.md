# TOOL-dFairHearing-1 — replay 4's staged input for aRoutedQuill #23: the skeptic prompt under `fixJudge: 'class'`

**Serves:** research TOOL-dFairHearing-1

Replay 4 (spec S8, §4 Fix verdict, AC8) hands this prompt, verbatim, to ONE real skeptic (`gov-skeptic`,
medium effort), with the schema below. The main loop runs it, writes the agent's raw return beside this
file, and adjudicates against the bar. This pass staged it and ran no agent.

## The bar

- **Hit:** the skeptic's returned verdict for id 1 carries `fixVerdict` `instance`: #23's fix, the range
  `ff0b3dc3..5b4f964d5`, judged to cure the cited instance and leave its class standing. The verdict
  record quotes that returned `fixVerdict`.
- **Paired with the control** (`2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-control`), which must
  come back not flagged: a skeptic that flags both reads as one that flags every fix.
- The claim's own `verdict` is not the bar: the prompt's SCOPE line can lead a skeptic to refute a defect
  present at the range's base, and the fix question is judged on its own whatever the claim's verdict.

## How it was rendered

- `node fh1-render.js fix 23 <head> <out>`, run from the repository root at the commit that adds this
  file; its source is in `2026-11-03-build-TOOL-dFairHearing-1-calibration`. It drives
  `tools/workflows/tier2-review.js` whole under stub agents, as `tier2-review.test.sh`'s `runReview`
  does, and this file holds the one `verify:` call's prompt read from the trace.
- **Arguments:** the diff kind, `base` `ff0b3dc327514e020eb47009de931d4dfd78c608` and `head`
  `5b4f964d50a85656029a7bd6a58f795f7717661a` (round 2's range, whose one fix commit is `5b4f964d5`),
  `round` 1, `fixJudge: 'class'`, `repo` this worktree, `roles.skeptic` `gov-skeptic` at medium effort, a
  one-line context naming the fix and the finding, and a one-item stand-in checklist, which reaches the
  finders only.
- **The stubs:** the `intent` finder, the lens of appendix row 23 of
  `memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md`,
  returns the one finding; every other finder returns none, so the harness numbers it id 1. Its `file`
  `.memory-tree.conf` and `line` 18 split the row's ref, `severity` is the row's `blocker`, and its claim,
  impact and fix are item B1's `Defect:`, `Impact:` and `Fix (judged SOUND by the skeptic):` bullets,
  the parenthetical dropped with the label, each line's markdown indentation dropped and the bullet
  folded by the harness's own `renderPromptLine` (spec §4 Fix verdict, §8 F7). The diff kind renders
  no evidence.
- The render line: `fix 23: 5372 bytes · sha256 711f0b2a4f27bfa1973ba8e6368d162e8b4fe6c790b35371f7d5236587dc7476 · finder lens intent · ref .memory-tree.conf:18 · threw no`.

## The prompt, verbatim

The bytes between the two fence lines, the newline before the closing fence excluded.

````text
REPO: C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c — run every git command as `git -C C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c …`; every path below is relative to it.
SUBJECT: the diff `git -C C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c diff ff0b3dc327514e020eb47009de931d4dfd78c608...5b4f964d50a85656029a7bd6a58f795f7717661a`.
CONTEXT: the fix ff0b3dc32..5b4f964d5 of the finding .memory-tree.conf:18 that memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md confirmed as id 23
INTENT — what this change was meant to do.
Read the range's commit messages, `git -C C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c log --format=%B ff0b3dc327514e020eb47009de931d4dfd78c608..5b4f964d50a85656029a7bd6a58f795f7717661a`, and any spec or design document the diff touches or those messages name. No spec was supplied, so these are the statement of intent.
REVIEW ROUND: 1
SCOPE: a finding is in scope only if this diff introduced its defect or made it reachable. A defect present unchanged at the base is PRE-EXISTING: refute it. Check with `git -C C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c show ff0b3dc327514e020eb47009de931d4dfd78c608:<path>`.
BY DESIGN (refute any finding one of these covers): none supplied
PRIOR ROUND'S FINDINGS: none - this is a first-round review of the whole diff.

For EACH finding below, read the actual code (Read/Grep the cited file:line and callers) and decide "confirmed" (real, reachable, impactful) or "refuted" (not reachable / not a bug / by-design / duplicate).
A DUPLICATE opens `reason` with `duplicate of id=<n>` for another finding in this batch that you CONFIRM in this same answer.

WHEN YOU CANNOT ESTABLISH A FINDING either way: one the finder graded medium or low (the bracketed grade) is "refuted"; one the finder graded blocker or high is answered "uncertain", and its reason says what you could not establish. "uncertain" is never a substitute for a judgment you can make.

SEVERITY RUBRIC - grade every finding by its CONSEQUENCE. blocker: on a reachable path it ships a wrong result, a security hole or data loss, or a check that certifies what it does not check. high: the same consequence on a narrow or unlikely path, or a defect that will mislead the next change. medium: a real defect whose effect is contained. low: cosmetic, or a comment, with no effect on behaviour. A grade follows the consequence, never the confidence or how alarming the defect looks.
For each finding you CONFIRM, also return `severity`, graded by this rubric against what you read, independent of the finder's bracketed grade.

Findings to judge:
id=1 [blocker] lens=intent .memory-tree.conf:18 — `ROUTED_COMMIT_WAIVED` was written before the merge of origin/main 76b9c451 (8dea35478). That merge brought in 3d05f1ea, 4e49aeb5 and d31d7bc9. All three were committed on 2026-10-09, which is not before the cutoff, they touch `tools/`, and they name no unit. None is on the waiver list. | impact: At ff0b3dc3, `python tools/memory-tree/routed_commits.py` with GATE_PUSH_BASE unset prints `routed-commits FAILED` naming all three, and exits 1. The leg has `guard []` and `history_depth full`, so it runs on every bar. Remote CI runs `GATE_FULL=1 run-gates.sh` on every push to main with no GATE_PUSH_BASE, which is WHOLE mode. The pre-push RANGE run excludes origin's commits, so the landing push passes and the breakage shows up only afterwards. From then on every branch bar and gov's remote CI go red on commits no session can change. TOOL-aRoutedQuill-3 AC10 requires the WHOLE run over this repo to exit 0, and its Rollout says the landing commit waives every cutoff-day commit. | fix: Add 3d05f1ead, 4e49aeb53 and d31d7bc96 as 12-hex prefixes to `ROUTED_COMMIT_WAIVED` and extend its comment. Re-run `python tools/memory-tree/routed_commits.py` with GATE_PUSH_BASE unset after every reconcile merge until it exits 0, and do this before the mint commit.

THE FIX, A SECOND AND SEPARATE QUESTION. For each finding also judge its proposed fix by the defect's CLASS, as `fixVerdict`: "sound" when applying it cures the defect's class, every instance of the pattern the claim names in the subject and the code or specs it reaches, and introduces none you can see; "instance" when it cures the cited instance and leaves another of its class standing; "unsound" when it does not cure the cited instance, breaks a caller, an invariant or a sibling path, or introduces a defect of its own; "none" when no fix was proposed. For "unsound", `fixNote` holds ONLY the corrected fix, and for "instance" ONLY the class-level fix; either is empty when you have none. Say why in `reason`, never in `fixNote`. The fix verdict NEVER changes the finding's verdict: judge the claim on its own, then the fix on its own.

Write no file. Set path to an empty string.

Return JSON {path, verdicts:[{id:<the integer id shown above>, verdict:"confirmed"|"refuted"|"uncertain", reason, severity:"blocker"|"high"|"medium"|"low" (on a confirmed verdict), fixVerdict:"sound"|"unsound"|"none"|"instance", fixNote}]}. Emit EXACTLY one verdict per finding above (1 verdicts, ids 1). Copy the integer id — do NOT re-type the file path, and do not renumber.
````

## The schema the harness passed with it

````json
{
 "type": "object",
 "required": [
  "path",
  "verdicts"
 ],
 "properties": {
  "path": {
   "type": "string"
  },
  "key": {
   "type": "string"
  },
  "batch": {
   "type": "string"
  },
  "verdicts": {
   "type": "array",
   "items": {
    "type": "object",
    "required": [
     "id",
     "verdict",
     "reason"
    ],
    "properties": {
     "id": {
      "type": "integer"
     },
     "verdict": {
      "type": "string",
      "enum": [
       "confirmed",
       "refuted",
       "uncertain"
      ]
     },
     "reason": {
      "type": "string"
     },
     "fixVerdict": {
      "type": "string",
      "enum": [
       "sound",
       "unsound",
       "none",
       "instance"
      ]
     },
     "fixNote": {
      "type": "string"
     },
     "severity": {
      "type": "string",
      "enum": [
       "blocker",
       "high",
       "medium",
       "low"
      ]
     }
    }
   }
  }
 }
}
````

# TOOL-dFairHearing-1 — replay 4's staged input for the control fix: the skeptic prompt under `fixJudge: 'class'`

**Serves:** research TOOL-dFairHearing-1

Replay 4's control (spec S8, §8 F4, AC8): this prompt goes, verbatim, to ONE real skeptic (`gov-skeptic`,
medium effort), with the schema below. The main loop runs it, writes the agent's raw return beside this
file, and adjudicates against the bar. This pass staged it and ran no agent.

## The pick, by §8 F4's rule

The first round-1 confirmed finding, in `review_replay.py --corpus memory/builds` order, whose fix commit
the next round of the same build reviewed with no confirmed finding sharing its `classes` cell:

- **The finding:** id 23, item B1, `classes` `C10`, lens `intent`, ref
  `tools/branch-reconcile/branch_reconcile.py:268`, of
  `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`.
- **The fix:** `f0e00195e` ("fold(dSweptBranches): TOOL-dSweptBranches-3 rev-3 — the closing review's two
  blockers"), whose body names B1, the one commit of the range `0ac2418c..f0e00195`.
- **The next round:**
  `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md`,
  range `0ac2418c05fad32467e20a93f04b8546383a1c4d..f0e00195e8b4745a2165baadd4444cb32b735591`, whose
  confirmed findings carry no `C10`.
- **The rule as the probe reads it** (`fh1-control.py`, in the calibration record): the next round is a
  listed round-2 record of the same build whose range head descends from round 1's head; a fix commit is
  a `fix(` or `fold(` commit inside that range and not reachable from round 1's head whose subject or
  body names the report item holding the finding's id; and a finding whose `classes` cell is `-` names
  no class a fix could cover, so it is passed over. Every earlier round-1 record in corpus order was
  passed over on one of those three, the probe's output naming each finding it weighed.

## The bar

- **Not flagged:** the skeptic's returned verdict for id 1 carries a `fixVerdict` other than `instance`.
  The verdict record quotes it beside #23's
  (`2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-23`), which must come back `instance`.
- As for #23, the claim's own `verdict` is not the bar.

## How it was rendered

- `node fh1-render.js fix control <head> <out>`, as #23's file states, with `base` and `head` the range
  above. The `intent` finder returns the one finding, id 1: `file` and `line` split from the row's ref,
  `severity` `blocker`, and the claim, impact and fix from item B1's `Defect:`, `Impact:` and
  `Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):` bullets, by the labels spec §4
  Fix verdict names, folded the same way. The fix is the item's corrected fix, the one the fold applied.
- The render line: `fix control: 5526 bytes · sha256 a01fb234597cb313e270cc07473740126ae6aeef143ffe3d1fe2a9f876dae486 · finder lens intent · ref tools/branch-reconcile/branch_reconcile.py:268 · threw no`.

## The prompt, verbatim

The bytes between the two fence lines, the newline before the closing fence excluded.

````text
REPO: C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c — run every git command as `git -C C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c …`; every path below is relative to it.
SUBJECT: the diff `git -C C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c diff 0ac2418c05fad32467e20a93f04b8546383a1c4d...f0e00195e8b4745a2165baadd4444cb32b735591`.
CONTEXT: the fix 0ac2418c0..f0e00195e of the finding tools/branch-reconcile/branch_reconcile.py:268 that memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md confirmed as id 23
INTENT — what this change was meant to do.
Read the range's commit messages, `git -C C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c log --format=%B 0ac2418c05fad32467e20a93f04b8546383a1c4d..f0e00195e8b4745a2165baadd4444cb32b735591`, and any spec or design document the diff touches or those messages name. No spec was supplied, so these are the statement of intent.
REVIEW ROUND: 1
SCOPE: a finding is in scope only if this diff introduced its defect or made it reachable. A defect present unchanged at the base is PRE-EXISTING: refute it. Check with `git -C C:/projects/coding-governance/.claude/worktrees/unattended-dfairhearing-fe4e9c show 0ac2418c05fad32467e20a93f04b8546383a1c4d:<path>`.
BY DESIGN (refute any finding one of these covers): none supplied
PRIOR ROUND'S FINDINGS: none - this is a first-round review of the whole diff.

For EACH finding below, read the actual code (Read/Grep the cited file:line and callers) and decide "confirmed" (real, reachable, impactful) or "refuted" (not reachable / not a bug / by-design / duplicate).
A DUPLICATE opens `reason` with `duplicate of id=<n>` for another finding in this batch that you CONFIRM in this same answer.

WHEN YOU CANNOT ESTABLISH A FINDING either way: one the finder graded medium or low (the bracketed grade) is "refuted"; one the finder graded blocker or high is answered "uncertain", and its reason says what you could not establish. "uncertain" is never a substitute for a judgment you can make.

SEVERITY RUBRIC - grade every finding by its CONSEQUENCE. blocker: on a reachable path it ships a wrong result, a security hole or data loss, or a check that certifies what it does not check. high: the same consequence on a narrow or unlikely path, or a defect that will mislead the next change. medium: a real defect whose effect is contained. low: cosmetic, or a comment, with no effect on behaviour. A grade follows the consequence, never the confidence or how alarming the defect looks.
For each finding you CONFIRM, also return `severity`, graded by this rubric against what you read, independent of the finder's bracketed grade.

Findings to judge:
id=1 [blocker] lens=intent tools/branch-reconcile/branch_reconcile.py:268 — read_dirt drops an untracked path that IS another worktree, for every worktree. Spec 1 scoped that drop to the primary. It is checked one way only. Write mode never asks whether a worktree it removes CONTAINS a kept worktree. | impact: reproduced on a throwaway fixture with the shipped CLI. Linked worktree X (MERGED, old) held worktree Y at `X/.claude/worktrees/Y`, and Y held an untracked `precious.txt`. The report graded Y `UNMERGED-LIVE · keep` and X `MERGED · remove worktree`. `--write` printed `removed — worktree X · git worktree remove`, and `precious.txt` was gone. The recovery manifest records HEAD shas only. | fix:  1. In build_rows, compute each worktree row's base action with derive_action first. 2. Before building the `kept` branch set, demote every `remove worktree` row to `keep · contains kept worktree <name>` when `check_under(other_path, its_path)` holds for any worktree row whose base action is not `remove worktree`. Containment is transitive, so one pass suffices. 3. Only then build `kept` from the final worktree actions and derive the local-branch actions. Doing it after the actions are assigned, as the finder proposed, leaves X's branch reading `delete branch` in the report while write mode keeps it as still checked out. 4. Add a selftest arm with the nested-in-linked fixture, and observe it red first.

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

# Acceptance ledger — KICK-aReplayedCard-3, the engine consumes and appends

**Serves:** journal KICK-aReplayedCard-3

Every observation below was made at the dispatched base tree (`39df2b1a`, the branch tip the unit
was handed) with the unit's working-tree changes applied. No figure is copied from the brief or the
spec; where the spec's method was changed before the code, the rev-4 line in its section 9 says what
and why.

## What was built

- `skills/session-kickoff/SKILL.md`, prose only. Step 1 names what a card opening `orientation —`
  in context satisfies (node tag, tree kind, worktree count, recent subjects) and keeps
  `git branch --show-current`, `status --short`, the fast-forward and `rev-parse HEAD` as the BASE
  in its one batch, never the card's branch or BASE; no card adds `git worktree list` when
  multi-tree. Step 2b repairs and STAGES; Step 5 commits after the append. Step 5 folds its field
  list into the six sections (`## task` · `## manifest` · `## read` · `## records` with the
  `Recall terms used:` line · `## classes` · `## open`) closed by the READY micro-format at
  `base` = BASE, pipes them into `bash <check-script> --card --append --session <sid>` with `<sid>`
  from the `orientation —` header, reports a refusal on the card and still stops, commits the staged
  repair AFTER the append and THEN hands control back. Step 5b appends the same way plus the build
  and run-state line, commits the staged repair after the append, and continues. The prompt string
  `Ready — say go and I'll start, or adjust any field.` sits on one physical line, because
  `check-unattended.sh` check 12 greps it as a fixed string and a wrap broke it once here.
- The budget. The three clauses measured 19191 B on first write, 759 over the 18432 ceiling, with
  the Step 1 batch prose already trimmed; the fit came from folding Step 5's enumeration into the
  six sections (every field kept), trimming Step 1's map-diff and STOP wording, and compressing
  rationale sentences in Step 5b — every rule, every inline command, all six numbered exits and the
  `BUILD-METHOD.md` pointer kept. Final `wc -c`: **18369**, 63 under. The split fallback stays the
  next unit's. `tools/template-size-highwater.txt`: the engine's row bumped 18215 → 18369 by
  `--bump`, so the growth is priced rather than warned about on every run.
- `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped `2026-09-14T10:10:45+03:00 @ c4f02308…`,
  the merge-base of `origin/main` and HEAD; `last-body-change` unchanged, the body did not move.
  `watch-commits-since-stamp: 4`, counted by `git rev-list --count` over the `watch:` list before
  re-stamping.
- `memory/map/features/session-kickoff.md`: one paragraph in the card seam saying Step 1 consumes
  and Step 5 appends before the repair commit.
- The spec: rev-4, status CLOSED, S5 and §4 and §10 amended before the code.

## RED before it landed

- **AC3** — the size gate was observed RED at 19191 B (`TEMPLATE-SIZE check 2 FAILED — … 759 over
  18432`, exit 1) before the trims, green at 18369 after.
- **AC4** — `manifest-check.sh --staged` was observed RED with `SKILL.md` staged and the stamp
  untouched (`MANIFEST check 5 FAILED — staged changes touch watched files: skills/session-kickoff/SKILL.md`,
  exit 1), then RED a second time when a `grep -c` returning 0 broke the `&&` chain before the
  `git add` of the manifest — the passing-zero-reads-as-failure class, caught by reading the index
  stamp against HEAD's — then green once the re-stamped manifest was actually staged.
- **check 12's prompt-string anchor** — `grep -cF` of the READY prompt string read 0 after the first
  Step 5 rewrite wrapped it across two lines; rewrapped, 1.

## What `tools/check-wiring.sh --check` reports

At the tip it exits 1 for ONE line outside this unit, `UNWIRED skill — the installed engine differs
from tracked in: SKILL.md MANIFEST-TEMPLATE.md manifest-check.sh`: the machine-global junction points
at the primary tree's engine on `main` while this branch edits all three. Expected; clears when the
branch lands and the junction's target moves. Not chased.

**Evidences:** KICK-aReplayedCard-3

- AC1 — `/session-kickoff` — OWED TO THE ORCHESTRATOR, NOT OBSERVED HERE: the installed skill on this node is a junction to the PRIMARY tree's engine on `main`, and no session inside this unattended run can re-point it. In a session started after this unit lands, with a card in context and a new branch checked out after the card was written, run one kickoff and read the transcript: the Step 1 batch shows no `git worktree list` and no `git log`, one `git branch --show-current`, one `git rev-parse HEAD` and one `status --short`, and the READY card's BASE and branch equal those two commands' output at that moment, not the card's `tree —` cell. Record the session id and `tools/check-wiring.sh --session`'s tracked-versus-installed line beneath this line. Red as written: the engine re-derives what the card carried, or pins the session-start BASE or branch.
- AC2 — `bash skills/session-kickoff/manifest-check.sh --card --check` — OWED TO THE ORCHESTRATOR, NOT OBSERVED HERE, same session as AC1: when that kickoff reaches Step 5, the card on disk ends with the READY line the transcript printed, and the check over it with that session's id exits 0. Red as written: the READY line is printed and never appended, so the next commit is denied.
- AC3 — `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` — at the tip: `template-size OK — SKILL.md: 18369 / 18432 bytes (63 under, 99.7%)`, exit 0, no high-water WARN after the bump. Red at 19191 B before the trims, as staged above.
- AC4 — `bash skills/session-kickoff/manifest-check.sh` — plain: exit 0 at the tip; `--staged` with `SKILL.md` and the re-stamped manifest staged: exit 0; the commit carries `manifest-audit: delta none · watch-commits-since-stamp: 4`. Red before the re-stamp, as staged above.
- AC5 — `skills/session-kickoff/SKILL.md` — read at the tip: Step 5 says "Commit Step 2b's staged repair AFTER that append, THEN hand control back", Step 5b says "commit the staged repair after that append, and continue without halting", and `awk '/^## Step 0/{f=1} /^## Step 5/{f=0} f' | grep -o '\`[^\`]*git commit[^\`]*\`'` over the file prints nothing (exit 1); the nine inline `git` spans between Step 0 and Step 5 are `rev-parse --show-toplevel`, `remote`, `symbolic-ref`, `-C`, `branch --show-current`, `worktree list`, two `merge-base` forms and `rev-list --count`, none a commit.

# KICK-aOrientedCast-1 — acceptance ledger

**Serves:** journal KICK-aOrientedCast-1

Direct checks only; no suite ran in the pass. AC1 to AC8 ran over the fixture the spec names, a
`git clone --local` of the pass's base at `%TEMP%/k1c` with a card written under session `k1fx`, once
with the base checker installed and once with this pass's. RED on the base checker: the skeleton
printed six field lines; the six-field body, the five placeholder bodies, the skeleton itself, the
plain-label body and the twice-carried Reuse all landed with exit 0; the format-1.4 region printed no
WARN and no NOTE under a 1.4 marker, and passed check 10 under a 1.5 marker. GREEN on this pass's
checker, every refusal leaving the card byte-identical by `cmp`, as each line below records. AC9 to
AC11 ran in the worktree. The self-test arms that encode the same observations (the KC block and
C10's three format-1.4 arms) are owed to the close's `manifest-check self-test` leg, with the
`codebase-map coverage + freshness` leg for the regenerated symbols and the dossier.

**Evidences:** KICK-aOrientedCast-1
- AC1 — `bash skills/session-kickoff/manifest-check.sh --task-skeleton` — run from a directory under a `GIT_CEILING_DIRECTORIES` root, it exited 0 and printed eight field lines: Title, Goal, IN scope, OUT / non-goals, `**To-do:**`, `**Reuse:**`, Acceptance check, Gates it must pass.
- AC2 — `--card --append --session k1fx` — the eight-filled body exited 0 with its `appended —` line, and the card's tail carried the eight field lines.
- AC3 — `--card --append --session k1fx` — the six-field body exited 1 in one refusal naming both "has no To-do field; has no Reuse field", the card byte-identical.
- AC4 — `…` — Reuse `…`, an empty To-do, Gates `TBD`, IN scope `<the scope>` and OUT `none`, each its own append, each exited 1 naming that field empty or a placeholder, the card byte-identical.
- AC5 — `--task-skeleton` — its output as the task section exited 1 naming all eight fields as placeholders ('…').
- AC6 — `**OUT / non-goals:**` — the `> `-prefixed body with every qualifier and a two-line Acceptance qualifier exited 0, as did the unprefixed body with that OUT label; the plain `- Title: x` labels exited 1 naming all eight absent; a second Reuse line exited 1 with "carries Reuse twice".
- AC7 — `## task` — a token-free READY body exited 1 on DEAD PROBE; a READY body with no `## task` exited 1 on the presence refusal; eight fields under a stale base exited 2 on the stale-BASE refusal; a body with no READY line and no `## task` on a card with a real READY line exited 0.
- AC8 — `check 10 FAILED` — with `memory/guides/SESSION-KICKOFF.md` at marker `v1.4` and the region from `646d4a73`, `bash skills/session-kickoff/manifest-check.sh` printed no `check 10 FAILED`, one format `WARN` naming v1.5 and one check 10 `NOTE`; at `v1.5` it printed `check 10 FAILED` with the "differs" message; back at `v1.4` with one character edited, `check 10 FAILED` again.
- AC9 — `WARN: manifest format` — `bash skills/session-kickoff/manifest-check.sh` in the worktree exited 0 with no `WARN: manifest format` line, after the §A intro prose was cut to bring the manifest back under check 7's 25600-byte cap, which the two new region lines had crossed by 159 bytes.
- AC10 — `bash tools/check-kit-versions.sh` — exited 0 ("kit-versions: clean"), and `grep -c "kickoff-manifest: v1.5" skills/session-kickoff/MANIFEST-TEMPLATE.md` printed 1.
- AC11 — `grep -n "v1.5" WIRE-INTO-PROJECT.md` — found the 5c re-paste step, the step-6 marker bump and the result tree; `grep -c "kickoff-manifest: v1.4" WIRE-INTO-PROJECT.md` printed 0.

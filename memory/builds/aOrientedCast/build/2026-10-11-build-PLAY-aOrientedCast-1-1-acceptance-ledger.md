# PLAY-aOrientedCast-1 — acceptance ledger

**Serves:** journal PLAY-aOrientedCast-1

Direct checks only; under the owner's rule for this run no gate, suite or self-test ran in this
pass, and the size, line-length, parity, render, manifest and epoch legs are owed to the main loop's
bar at the close. What ran were plain reads (`grep -c`, `wc -c`, an `awk` line-length scan) and the
playbook renderer, which this pass may run because its output is committed. AC1 was observed RED at
the parent `6855d6ae7` (each file: the bullet 0 times, the inheritance clause once) and GREEN on the
pass's tree. AC3 is RED-and-GREEN by construction: two scratch fixtures that differ only in the
`roles` member of their `kits` array render the bullet 0 and 1 times. One deviation: the pass also
ran `adopt-playbook.sh --target . --check` once while listing the renderer's derived placeholders; it
exited 0, but that is the render-wiring leg and AC2 stays owed to the main loop rather than being
claimed from that run. The two high-water rows were re-recorded by hand to the measured byte counts,
because `check-template-size.sh --bump` is a gate-leg command this run reserves; the edit writes the
same tab-separated, sorted rows that `--bump` writes. After the pass commit `ed5785a50` a grep for
the retired clause outside the memory tree found it in four rendered agent types under
`.claude/agents/`, which embed charter sections read from `AGENTS.md`; the spec's S2 Readers clause
names only the template and its render, so it missed them. A follow-up commit re-rendered the agent
types with `adopt-roles.sh --scaffold`: six changed, the clause now appears in none, and the new
bullet appears in `gov-orienter.md` and `gov-spec-writer.md`, whose roles carry charter §1. The
`roles render wiring` leg that compares them is owed to the main loop.

**Evidences:** PLAY-aOrientedCast-1
- AC1 — `grep -c "It DOES inherit the governing doc"` — 0 in `coding-governance-agents.template.md` and in `AGENTS.md` (1 each at the parent), while `grep -c "Hooks DO fire in it, measured;"` is 1 in each and `grep -n "Every agent is handed a rendered role"` shows the bullet once, at template line 44 and `AGENTS.md` line 99, each directly after the write-gate bullet.
- AC2 — owed to the main loop — `bash tools/playbook/adopt-playbook.sh --target . --check` must report the region in sync; the plain-read half is observed: `grep -c "kit:roles" AGENTS.md` returns 0 after the render.
- AC3 — `adopt-playbook.sh --target` — two fixtures under the pass's scratch root, each a `deploy.toml` copied from gov's with `gov_source` pointing at this worktree and the derived keys answered: the one whose `kits` omits `roles` rendered the bullet 0 times, the one keeping it rendered it once, and both rendered the write-gate bullet once and no `kit:roles` marker, as their `agent-cap` selection says.
- AC4 — owed to the main loop — `bash tools/check-template-size.sh` and `bash tools/check-template-size.sh AGENTS.md` must print OK with no high-water warning; `wc -c` measured 49006 and 54795 bytes, matching the spec's pinned figures, and `tools/template-size-highwater.txt` now records exactly those two values.
- AC5 — owed to the main loop — `bash tools/check-line-length.sh` and `bash tools/check-playbook-parity.sh` must report clean; an `awk` scan measured the longest line of both files at 448 characters, the existing one, and the new bullet at 209.
- AC6 — owed to the main loop — `bash skills/session-kickoff/manifest-check.sh` must pass after the commit; the commit's `last-audit` names its parent `6855d6ae7` and differs from the parent's, and the stall count since `last-body-change` is 2 watched non-merge commits before this one, under check 9's 10.
- AC7 — owed to the main loop — `python tools/govkit/govkit.py epoch --base 646d4a73` must read the `playbook` row as owed and not `broken` on this commit, and `clean` after the run's mint commit, where the marker and banner move to v3.7; this commit leaves both at v3.6.

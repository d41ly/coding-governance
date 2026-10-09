# TOOL-aFrugalTurnstile-1 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-1

No merge bar, no runner and no self-test suite ran in this pass. One driver script built scratch
repositories under the user temp directory, with the run-gates kit at `tools/` and a stub bar under
the declared test escape. It invoked `pre-push.base`, the hook from `bef97330`, and then
`pre-push.new`, the working file, directly with a ref line on stdin. Every new behaviour was RED on
the base copy and GREEN on the new one; AC2 and AC5 are the controls that both copies agree on.
The runner's S3 block was evaluated lifted from the working `run-gates.sh`, because a unit pass
starts no runner (spec rev-2). The close still owes the `.githooks/pre-push.test.sh` arms 12, 12b,
12c, 25b and DOCS AC7, the `run-gates.evidence.test.sh` stamp arm, and every §7 leg.

**Evidences:** TOOL-aFrugalTurnstile-1
- AC1 — `2 first-parent landing(s) back` — on the F2 shape the probe counted all=14 and
  first-parent=2. The base line read FULL with "14 commits behind the tip"; the new line read scoped
  with "2 first-parent landing(s) back, within 10".
- AC2 — `11 first-parent landings behind the tip (bound 10)` — both copies printed FULL after 11
  linear commits; the base named "11 commits behind", the new copy the first-parent wording.
- AC3 — `tools/gate-legs.json` — with `manifest elsewhere/legs.json` in the stamp, the base line
  was scoped and the new line was FULL, naming `elsewhere/legs.json` and `tools/gate-legs.json`.
- AC4 — `is not this kit's runner` — with a committed `tracked-bar.sh` declared in `.unattended.conf`
  and no test escape, the base line was scoped and the new line FULL with the S6 reason.
- AC5 — `scoped gate` — a stamp with no `manifest` key at the tip scoped on both copies.
- AC6 — amended rev-2 — the S3 block is evaluated lifted from the runner rather than by a runner run;
  it gave `tools/gate-legs.json`, `gate-legs.json`, `tools/gate-legs.json` for both the `/tmp` and
  git spellings of the in-tree path, and the out-of-tree path absolute. `pre-push.new` scoped from
  the nested and root-install stamps and forced FULL on the out-of-tree one, which the base scoped.
- AC7 — `manifest` — the awk range over the working runner prints the `LEGS_REL` line the
  full-green block writes, byte for byte; at `bef97330` the same range prints no such line.
- AC8 — `DOES NOT CHECK` — the old-wording grep printed nothing (rc 1), `first-parent landing`
  counted 6 (2 at base), and both S7 sentences were named, at lines 1072 and 1243.
- AC9 — `grep -n 'first-parent landings behind' memory/guides/MERGE-BAR.md` — hit line 17; the
  README's `manifest` grep hit the S8 sentence at lines 355 and 356.
- AC10 — `grep -n 'commits behind' .githooks/pre-push.test.sh` — printed nothing (rc 1); 2 hits at
  `bef97330`.

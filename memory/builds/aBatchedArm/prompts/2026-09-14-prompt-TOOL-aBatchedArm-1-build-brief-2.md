**Serves:** journal TOOL-aBatchedArm-1

# Build brief, pass 2 — TOOL-aBatchedArm-1, the nineteen groups under the owner's ruling

The spec is `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-1.md` at rev-6,
REOPENED by an owner ruling on the question the first pass parked. The first pass's brief
(`2026-09-14-prompt-TOOL-aBatchedArm-1-build-brief.md`) still binds for everything it says about
the rulings, the four facts, the traps and the static discipline — read it first — EXCEPT its rule
"every existing `hit` line stays byte-identical", which the owner overrode. This brief carries only
the delta.

## The owner's ruling, 2026-09-14

1. The one token change `hit "$(run)" "…"` → `hit "$out" "…"` is ALLOWED. The literal stays
   verbatim; only the capture token moves.
2. Convert the NINETEEN candidate groups the first pass classified — enumerated by line range at
   `46b12b93` in `memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-1-1-acceptance-ledger.md`
   ("The 19 candidate groups under the spec's reading"). The file is now at `97abf7e1` (+53 lines,
   the helper), so re-locate each group by TEXT, not by those line numbers, and paste the new
   ranges in the pass-2 ledger beside the old.
3. Each group's expected set is written from the OBSERVED run at the build's final gate pass — not
   now, and not from the arms. Until then every `emitted` call carries the SENTINEL `"?"`.

## What this pass does

- `emitted` gains one refusal: an expected-set argument of `"?"` REDS by name (`emitted: expected
  set not yet observed — owed at the final pass`), so a converted file cannot pass in the window.
  Probe it alone over a literal string as the first pass probed the helper.
- Convert the nineteen groups, each into the spec's §4 shape: one `reset_tree`, the mutations in
  sequence, one `out=$(run)`, one `emitted "?" "$out"`, then the group's `hit "$out" "<literal>"`
  lines with every literal byte-identical to before. A group whose mutations turn out to touch the
  same file or ref, or whose blocks are no longer contiguous at `97abf7e1`, is NOT converted and is
  named in the ledger with the reason — the count converted is derived, and nineteen is the
  first pass's figure, not a target.
- Nothing else in the file moves: the SOLO blocks, the counted block, the seams, the floors.
- Commit per region tranche, unit id in the subject, the trailer.

## Static observations you take (no suite runs)

- AC4 and AC7 by the first pass's static scan, re-run over the converted file: no group carries a
  `miss` or `same`; every S3 class is located and alone. Paste the output.
- AC8's first half: every `emitted` carries `"?"`, and the helper refuses it — the probe.
- AC3's recipe, amended: the allowed `n` delta is the number of `emitted` calls you added (paste
  it); the `FAIL` set at the final pass must equal unit 3's 21 lines PLUS one `emitted` refusal
  line per group until the sets are written, and equal the 21 exactly after.
- `bash -n`; `python tools/memory-tree/check-arms.py --check` green; install-prefix and
  line-length green; `grep -c '\$(run)'` before and after, pasted (285 before).

## What done looks like

- The nineteen groups (or the derived count, with the exceptions named) converted with sentinels;
  the helper's `"?"` refusal in place; every other line of the file byte-identical.
- The pass-2 ledger at `memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-1-2-acceptance-ledger.md`
  with `**Evidences:** TOOL-aBatchedArm-1` — AC4, AC7 and AC8's first half OBSERVED by the static
  scan and the probe; AC1, AC2, AC3, AC5, AC6 and AC8's second half AMENDED rev-6, each naming its
  final-pass command and, for AC8, the golden-writing step: run the eight shards once, paste each
  group's fired set from `UNATTENDED check N FAILED — <text>` lines into its `emitted` call with the
  run named beside it, re-run the shard, `FAIL` set equal to the 21.
- The spec header CLOSED at rev-6 in the last commit (a rev-7 line only if something diverged).
- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` after each commit.

Do NOT run the suite in any mode, any shard, the bar, or `run-unattended-gates.sh`.

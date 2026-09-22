# TOOL-aWokenSentinel-20 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-20

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule three. The pass verified with the direct checks the spec's
section 7 names for it — the greps of AC1, AC3 and AC4 over the working tree, over the files at
the tip of unit 2's pass (`0e3f3fe2`, the newest commit whose subject carries
`TOOL-aWokenSentinel-2`) and over the status header's base `12513c25`; and AC2's bare-shell call
through a scratch repository under `%TEMP%/aws20` with one linked worktree, plus a plain directory
outside any repository. `bash -n` over both edited files, and `unattended.sh --liveness
aWokenSentinel` against this run's own record, which printed thirteen `key: value` lines and no
dead probe named `resolve_sidecar_dir`, so the driver resolves the moved function through the lib
it sources. Those stand in for the `unattended kit gate` leg, whose unit-11 arm reads this unit's
population at the close and does not exist at this order.

**Evidences:** TOOL-aWokenSentinel-20
- AC1 — `grep -cE '^[^#]*rev-parse --git-dir' tools/unattended/lib-unattended.sh` printed `1` and the same grep over `tools/unattended/unattended.sh` printed `0` at the working tree; over `git show 0e3f3fe2:<file>` the two printed `0` and `1`; over `git show 12513c25:<file>` both printed `0`, as the spec says of that sha, and no reading is taken there. OBSERVED.
- AC2 — from a bare `bash -c ". <lib>; resolve_sidecar_dir"` inside the scratch repository the call printed `.git/unattended`, exit 0, equal to `$(git rev-parse --git-dir)/unattended` read beside it; inside the linked worktree it printed `<repo>/.git/worktrees/wt/unattended`, exit 0, which is the worktree's git dir and not the common dir `<repo>/.git`; from `%TEMP%/aws20n`, where `git rev-parse --git-dir` printed `fatal: not a git repository`, the same call printed nothing (`out=[]`) and exited 1, the `return 1` branch; `grep -cE '^[^#]*\$\(resolve_sidecar_dir\)' tools/unattended/unattended.sh` printed `1`; `diff` of `sed -n '/^resolve_sidecar_dir()/,/^}/p'` over `git show 0e3f3fe2:tools/unattended/unattended.sh` against the same extraction over the working-tree lib printed nothing, exit 0. OBSERVED.
- AC3 — `sed -n '/^[^#]/q;p' tools/unattended/lib-unattended.sh | grep -c 'resolve_sidecar_dir'` printed `1` at the working tree and `0` over `git show 12513c25:tools/unattended/lib-unattended.sh`; `grep -c 'resolve_sidecar_dir' tools/unattended/lib-unattended.sh` printed `2`, the top header's `WHAT IT HOLDS` sentence and the definition line. OBSERVED.
- AC4 — `grep -ci 'code.line'` over spec 11 printed `11`; `grep -c "resume-log root is that function's answer"` over spec 5 printed `1`; `grep -c 'aWokenSentinel-20'` over spec 2 printed `2`. All three folds were landed by the disposal that authored this spec; this pass wrote none of them. OBSERVED.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, lexicon leg or install-prefix leg ran inside this pass;
every one is `--close`'s and each row above says so. Unit 11's check — the count across driver,
lib and tick — is not built at this order, so the population it will read is asserted here by
AC1's greps and by nothing that grades it on a bar. `tools/unattended/kit.toml` was not edited:
the lib is already a shipped file, as S3 says. No identifier was minted, so no lexicon query was
owed. The build README's authored roster row for this unit moved `PLANNED` to `CLOSED` beside the
spec header.

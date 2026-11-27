# TOOL-dTotalRecall-3 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-3

No merge bar, no self-test suite and no gate leg ran in this pass. Every probe ran on node d, 2026-11-22,
from base `e1ae60af8` with the pass applied in the working tree. The fixture remotes and clones sat under
the system temp directory. The probe of the two-clone arms imported `gen_build_index.py` and called its
`#test_slug_claims` alone with a stand-in arm printer, over the scaffold's home tree; the whole
`build-index selftest` leg, the other gates of §7 and both `New arm:` RED-first observations are OWED to
the close, after the last unit is terminal.

**Evidences:** TOOL-dTotalRecall-3
- AC1 — `claimed` — two clones of a bare fixture remote each ran `gov-claim.sh slug dSame` at once under their own keys: one printed `claimed refs/gov/claims/dSame <sha>` and exited 0, the other printed `taken refs/gov/claims/dSame by <the winner's key>` and exited 1; the remote's `git log -1 --format=%B refs/gov/claims/dSame` read the header `gov-claim claims/dSame` and the winner's `claimant-key:` line; `check_slug_claimed` for `dSame` in the losing clone before the claim returned the empty string. The first run, before the write-not-completed re-read, printed `refused … (reference already exists)` for the loser, deviation 35.
- AC2 — `TOOL-dSame-15` — five rounds of two parallel `gov-claim.sh ask TOOL dSame` mints, one per clone, printed `TOOL-dSame-1` to `TOOL-dSame-10` with no repeat; a default branch naming `TOOL-dFloor-14` minted `TOOL-dFloor-15` next (the fixture's id moved from `dSame` to `dFloor` so AC4's third clone finds no tracked file naming `dSame`).
- AC3 — `claimant-key:` — a mint replayed under a round-one key printed that round's id again and the counter's tip did not move; its tip's message carried a `claimant-key:` line; `gov-claim.sh slug dSame` run twice under the winner's key exited 0 both times with the claim's tip unmoved.
- AC4 — `refs/gov/claims/dSame` — `cmd_new_build` for `dSame` in a third clone that fetched no claim ref exited 1 naming `refs/gov/claims/dSame was not claimed`, the CLI's `taken` line beside it, and wrote no README; in a fourth clone `--new-build dOther` claimed `refs/gov/claims/dOther` and wrote its README, `git reset -q --hard` removed both writes, and the re-run exited 0 with the claim's tip unmoved and the README written again, `read_own_claim` skipping the local pre-check.
- AC5 — `GOVREF_WHY` — a probe sourcing `gov-ref.sh` and `gov-feed.sh` over a fixture remote: `remove_gov_ref refs/gov/claims/dSame <sha>` returned 2 with `GOVREF_WHY` naming `refs/gov/claims/` and the remote still named `<sha>`; `remove_gov_ref refs/gov/runs/tFix <sha>` returned 0 and the ref was gone. The `blk` cut of `gov_ref_sh`, and of every other block the CLI carries, compared equal across `gov-ref.sh`, `gov-claim.sh`, `unattended.sh` and `post-merge.sh`. Part 2p's new arm in `resolve-python.test.sh` and its RED-first observation are OWED to the close as the first `New arm:` line.
- AC6 — `refused offline` — with the clone's remote URL at a missing path, `--offline refuse` exited 2 printing `refused offline`, `warn` and `follow-leases` each exited 4 printing `waiting offline`, and after the three no `gov-queue.log` existed in the common dir and no `refs/gov/remote/claims/asks/TOOL-dSame` ref existed.
- AC7 — `record-kinds.toml` — a `tomllib` probe found one row named `claim`, its `writer` `gov-claim.sh` and its `home` `refs/gov/claims/**`; `record_kinds.check_row` over it returned no red, and `record_kinds.py --write` re-rendered the template's region, its count line one row up.
- AC8 — `local refs/gov/claims/dSame · no remote` — a clone with no remote exited 0 printing that line, and `git for-each-ref refs/gov` listed nothing; `cmd_new_build` in a remote-less scaffold fixture exited 0, wrote its README and printed the same `local` line.

# PLAY-aDistilledCharter-6 — the landing, and what it still owes

**Serves:** journal PLAY-aDistilledCharter-6

The unit LANDED on 2026-10-12: `origin/main` fast-forwarded `13fe6a04..fcba0600`, 11 commits. The
owner chose `git push --no-verify` after the gated landing was refused, so no bar passed on the
landed tree.

## The gated attempt

`push-main.sh --land` ran the pre-push bar over the landing prepared onto `23c08f73`. It was RED on 7
of 65 legs and pushed nothing.

- Three legs timed out twice on the host: `pass-order history`, `brief-recorded` and
  `straggler-guard arms`, at spawn costs 14 to 32 times the clone's floor. The node had been up
  169.5 hours with 26.7 GB in the kernel pools.
- Four legs were red on lines outside this landing's diff, which was eight files against its base:
  `install-prefix (shipped surface)` on two test files of other kits, `harness arms` on
  `tools/run-gates/post-merge.sh:405`, and both lexicon legs on verb offenders over their pin.
  Attribution read three of them OWN because the diff touched a file in each leg's comparator set,
  `.memory-tree.conf` or `tools/template-size-highwater.txt`, and an OWN red does not land.

## What the landing carries

- `05b48c3cb`: the micro-format block moved into section 1, with `[never-omit]` and `[events]`, and
  `[formats]` and `[pair]` binding every final message.
- `e173eff12`: `ROUTED_COMMIT_WAIVED` re-derived, so main's routed-commits leg reads green.
  aPrimedIndex re-derived the same twenty shas independently, and the reconcile kept that value.
- The charter marker minted v4.2 to v4.3, and `AGENTS.md` re-rendered over it.

## Still owed

- A bar on `main` at or after `fcba0600`. The four inherited reds belong to the builds that wrote
  those lines.
- The adopter rollout, one `govkit update` per repository.

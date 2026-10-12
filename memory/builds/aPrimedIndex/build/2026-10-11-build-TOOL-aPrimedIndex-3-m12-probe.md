**Serves:** research TOOL-aPrimedIndex-3

# M12 probe — where regeneration is enforced, and what each candidate cost

Run 2026-10-11 on node `a`, against base b726385f, in a `git clone --local` of this worktree under a
short root in `TEMP` (`pi1`), whose `origin/HEAD` was set to `main` so the playbook render reads the
real default branch. The probe READ the bar's entry points and MEASURED a draft of the reader; it
built no arm of the fork into the tree.

## The candidates

| | Mechanism | Where it binds |
|---|---|---|
| A | the runner proves every declared output fresh before its queue and refuses, exit 2, naming one regeneration command | every caller of the runner |
| B | the runner regenerates the outputs in place, then grades the regenerated tree | every caller of the runner |
| C | a PreToolUse hook denies an agent's bar command while an output is stale | an agent's tool call |
| D | each entry point regenerates on its own: the lander, the close and the pre-commit hook | three call sites |

## What would make each lose, written before the reads

- A loses if a stale output cannot be told from a fresh one before the legs run, or if proving it
  costs a large share of a bar.
- B loses if a bar that writes the tree it grades cannot certify a pushable commit.
- C and D lose if they leave an entry point to the bar unbound.

## The reads and measurements

1. **Entry points.** The runner is reached from five places: a session running it by hand;
   `.githooks/pre-push`, which runs `${GOV_GATE_CMD:-bash $GATE_RUNNER}` for a default-branch push;
   `tools/push-main.sh`, which pushes through that hook; `tools/unattended/unattended.sh`'s
   `gates-green` item, which runs `$GATE_CMD` as a subprocess; and `.github/workflows/remote-ci.yml`.
   C binds only the first, and the lander when an agent types it: the hook sees tool calls, and the
   close's bar, a plain `git push` and CI are not tool calls. D binds the lander and the close and
   leaves the hand-run bar and CI unbound. Neither covers what the prompt asks, "any merge/landing
   bars". **C and D lose.**
2. **The push boundary.** `.githooks/pre-push` refuses a dirty tree before its bar (`_tree_dirty`,
   the one definition of dirty it shares with the lander) and a HEAD that moved during it, and
   `tools/run-gates/gate-fingerprint.sh` states that a green is recorded only from a clean tree. A
   bar that regenerated in place is therefore refused at the boundary when anything moved, and its
   green is never reusable by the push. **B loses**: it costs the hour it was meant to save.
3. **A's discrimination.** The draft reader over the clone, with nine descriptors carrying the new
   keys: 11 items, every check fresh in 49 s concurrently at width 4. With one row deleted from
   `memory/gotchas/INDEX.md` the gotchas item read `STALE` and the runner, over a one-leg manifest,
   exited 2 after 56 s with no `gate queue:` and no `GATE` line. `--regen` restored the file in
   80 s and the next check read fresh. The same clone's one-leg bar took 3 m 26 s end to end, so
   the check is under half of a bar that runs no real leg. **A survives.**
4. **Why the lander still writes.** A alone refuses every landing whose reconcile merge leaves a
   `merge=ours` index stale (`memory/LIVE.md`, the ledger shards and the gotchas index carry that
   driver in `.gitattributes`), and the lander's `--prepare` already rewrites its merge with the
   versions `run_minter` writes. D's lander half therefore joins A as its own unit; D's close and
   pre-commit halves stay out, because A binds both of their bars.

## The pick

A, with the lander's regeneration from D, by M3's rule: the most feature-rich survivor, and it
reuses two seams the reuse probe found, the `[[generated]]` declarations and the lander's
write-over-the-merge.

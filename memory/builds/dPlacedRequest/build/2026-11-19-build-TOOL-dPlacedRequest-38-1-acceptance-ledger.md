# TOOL-dPlacedRequest-38 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-38

The unit was built from its spec at rev-6 on base `9152c6068`. Section 2a of (PINNED)
`tools/lib/resolve-python.test.sh` sits right after the `PARITY_ROWS` loop:
`tools/lib/resolve-python.test.sh#check_feed_copies` takes the carrier files, cuts each one's
`gov_feed_sh` block with the file's own `blk`, and sources it after the canonical `health_log_sh` cut
under `env -i PATH="$PATH" HOME="$HOME" bash -c 'set -u; …'` inside a scratch repository: a fresh
take of `gov-feed.lock` and its release, the break of a planted lock whose `until` reads the clock
less one and its release, then `add_feed_event refs/gov/bar-red` of the scratch commit. A non-zero
exit, `unbound variable` or `command not found` on stderr, or a lock or guard directory left behind
prints `<file>: <first stderr line>`; no file at all prints `no inline copy of 'gov_feed_sh'` (S2).
The arm runs it over `git grep -l '^# >>> gov_feed_sh'` from the root, then over plants made by
`tools/lib/resolve-python.test.sh#write_feed_plant`, which replaces one exact line of the canonical
cut and returns 1 when no line matched, so no plant is a no-op. No gate, suite or bar ran in this
pass. Each observation below is a probe: section 2a cut from the suite by its two headers and
sourced alone with the suite's own `blk`, `ok` and `bad`, `TMP` under the session scratch.

**Evidences:** TOOL-dPlacedRequest-38
- AC1 — over a plant whose bound line reads `NODE_LOCK_BOUND=$(( REMOTE_BOUND + 10 ))`, the function
  printed one line, that plant's path, then the cut's `REMOTE_BOUND: unbound variable`, and returned (DERIVED)
  `rc=1`; no `gov-feed.lock` remained in the scratch common dir. (DERIVED)
- AC2 — over a plant that is the canonical cut unchanged, the function printed nothing and returned
  `rc=0`; the err file held 0 bytes, the common dir held `gov-feed.log` and `gov-feed.seq` and no (DERIVED)
  lock, the feed held 1 line for `refs/gov/bar-red`, and `health.log` held 1 `node-lock-broken` (DERIVED)
  line, so the stale break and the append both ran.
- AC3 — with no file, the function printed `no inline copy of 'gov_feed_sh' found — the carrier arm
  would be judging an empty population` and returned `rc=1`. (DERIVED)
- The tree — the population was 3 files, the canonical `tools/lib/gov-feed.sh`, (DERIVED)
  `tools/run-gates/post-merge.sh` and `tools/unattended/unattended.sh`; all 3 ran alone green after (DERIVED)
  TOOL-dPlacedRequest-36 and TOOL-dPlacedRequest-37. The whole section read `st=0` over 10 (DERIVED)
  assertions: the tree, 4 plants each with its no-op guard, and the empty population. (DERIVED)
- The plants — besides AC1's bound, the base's bare `$ROOT` in the break's health append before
  TOOL-dPlacedRequest-36 reds on `ROOT: unbound variable` though its `$( )` exits 0, a final release
  renamed to no command reds on `command not found`, and a final release replaced by `:` reds on the
  lock left behind; a plant line in no canonical returned 1 from `write_feed_plant`.
- Map — the pass minted 2 functions the symbol extractor reads, so `gen_map.py --write` regenerated (DERIVED)
  `memory/map/generated/symbols.json`, adding exactly those 2 ids. (DERIVED)

## Owed at the close

- The spec's `New arm:` line: `tools/lib/resolve-python.test.sh` section 2a, covering AC1 to AC3. Its
  RED-first observation inside the suite is the close's: stage a carrier whose bound reads the
  driver's `REMOTE_BOUND`, observe the arm red, restore, observe it green.
- The legs the spec's Gates section names, run once by the main loop.

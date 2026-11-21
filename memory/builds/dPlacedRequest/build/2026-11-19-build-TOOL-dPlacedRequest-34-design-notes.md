**Serves:** research TOOL-dPlacedRequest-34

# TOOL-dPlacedRequest-34 — the design record its §4 points at

Moved whole out of `TOOL-dPlacedRequest-34`'s §4 at rev-12, on 2026-11-19, by the disposal of
`2026-11-19-review-dPlacedRequest-spec-audit-round-1` (finding 2, H1), so the spec measures under its
48128-byte ceiling before it leaves DEFERRED. Nothing here was re-decided by the move; the spec's items
S28, S43, S56 and S57 and its criteria AC56 and AC57 point here.

## Evidence

- Minted code is cited by unit and item, base code by path and line, each read when the spec was
  written.
- `derive_claims_line` ranks `live held unknown stale terminal`
  (`skills/session-kickoff/manifest-check.sh@0784ef8f:662`), any other verdict falling to `skipped:`.
- `read_files_touched`'s `awk` sets `term` on CLOSED or WONTDO (`tools/unattended/unattended.sh@875eaadf:3398`),
  reads only `ft && !term` (`:3400`), and tests tokens at `:3404`.
- `resolve_node_tag` honours `GOV_NODE` against the registry tags and lower-cases the user
  (`tools/run-gates/run-selftests.sh@fa74eed8:293-310`); `derive_node_tag` matches `USERNAME` against the
  `## Node registry` Machine/user cell (`skills/session-kickoff/manifest-check.sh@0784ef8f:375-400`). Both stay
  on that table, a different registry from `fleet.toml`, which S30's `resolve_fleet_tag` reads.
  `read_fleet` is `tools/playbook/render_playbook.py@34871ed5:347` and `check_user_clash` `:381`; `fleet.toml`
  spells one host `COMPEETO-AGENT` (`:23`) and leaves one empty (`:44`).
- `readCard` is `tools/hooks/scratch-guard.js@223ae5f5:667`, called at `:774`; `resolve_bash`'s MSYS fold is
  `tools/roles/handoff.py@12ca1202:279`.
- `symbols.json` indexed the four claim-push lock functions (`memory/map/generated/symbols.json@36060d31:3826`,
  `:3831`, `:15301`, `:24166`) before TOOL-aPiecewiseGrade-6 renamed them on 2026-11-16 to
  `write_dir_lock`, `check_dir_lock_stale` and `remove_dir_lock`.
- Sizes, measured 2026-11-19 with CR stripped (PINNED): S36's `SKILL.md` 18364 of its row's 18432
  bytes, S37's protocol 68288 of its row's 68288, zero headroom. The criteria read the row, never
  these figures.
- `derive_content_key` is `tools/memory-tree/row_grammar.py@2b622305:1475` at the pinned base; `git ls-files
  tools/loop` prints nothing at `c63aabbb`.
- The pre-push hook's comment at `.githooks/pre-push:845-847` names both claim shapes S24 and S25
  test, and unit 21's patch and repeat claim proceeds leaseless under S23's `off`.

## The bounded walk (S43)

`git log --first-parent --format='%x01%H%n%B' <cached lease and legacy refs> | awk`, the `awk` loading
each commit's feed `seen-utc` against a threshold of now less `leases.expiry-hours`, an ISO string, and
walking with no `--topo-order`. In one first-parent chain `git log` emits a child before its parent
whatever the dates, as a parent enters the walk only after its child; across chains, date order costs
interleaving only. A commit sighted before the threshold makes the verdict `stale` whatever lies
further back, since on one node a parent is sighted no later than its child. The walk reads at most
each lease's commits sighted within `leases.expiry-hours`, plus that interleaving, and `git log` stops
on the closed pipe once every tail resolves.

## Measured sizes (S56)

Measured 2026-10-25 (PINNED) by `git cat-file -s` over five `refs/gov/remote/runs` tips: a parentless
claim commit is 380 to 390 bytes, so a parented one, a 48-byte `parent` line more, is about 430, not (DERIVED)
"sub-400" (unit 11's §4); a lease commit, nine keys more, is about 630, so one written each minute for
a day is about 0.9 MB of loose objects, not "under 0.6 MB" (unit 17's §4). Nothing in either unit
branches on the figure.

## The one deletion outside leases (S57)

Correcting unit 16's §10, which finds no `refs/gov` deletion outside fixtures: post-merge's
`remove_red_ref` (`tools/run-gates/post-merge.sh@a0462621:301`, called at `:392`) deletes `refs/gov/bar-red` on
every green after a red. Unit 11 keeps it, through `remove_gov_ref`, the one deletion form its S1
admits since the same audit's finding 28, outside the lease namespace unit 16's S7 guards.

## `readCard`'s cost (S28)

One `bash manifest-check.sh --card --path --session <sid>` per guarded write, about 0.3 s on a
Git-for-Windows node (the review's measurement, PINNED 2026-10-25), under the hook's existing spawn
bound; a node where bash does not resolve reads no card, named.

## Alternatives rejected

- **Two batches.** Nearly every item shares `unattended.sh`, the `gov_feed_sh` block or the kickoff
  engine, so no split gives M6 two disjoint write sets.
- **A `renewed-by` key (S43) or a backslash token (S48).** The spec's F3 and F4 record why.
- **A high-water row holding the spec over its ceiling.** A row is the owner's to add, and S22's
  ceiling in unit 43 reads the spec at 48128, so moving this text cost no item.

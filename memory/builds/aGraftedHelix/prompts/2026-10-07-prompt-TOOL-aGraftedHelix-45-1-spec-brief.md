**Serves:** journal TOOL-aGraftedHelix-45..47

# Spec brief — TOOL-aGraftedHelix-45 to -47, adopted by owner decision

On 2026-10-07 the owner ruled on the run's open decisions. The build rides local main and is not
pushed by this run. Three items the run had parked or found are adopted as units now. Spec `order`
values: 45 is 26, 46 is 27, 47 is 28. The shared brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states twelve invariants that bind all
three units. In your OWN return, name the specs you author in `authored` by their unit ids, never by
their paths.

Owner ruling of 2026-10-06: no whole kit self-test suite runs in this session; the owner runs them
by hand from the merged tree. So a spec here names slices and direct checks for its pass, and leaves
whole-suite verification to that manual run. The evidence each unit needs is quoted below. Read it
here instead of re-deriving it, and do not re-run a check whose output this brief quotes.

## TOOL-aGraftedHelix-45 — Tier-2 — the location-probe class gate

Source: unit 27's spec, `memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-27.md`,
§3's hands-off item and §4's "The kit's location probes, fixed and left". The class record is
`memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`.

Unit 27 ran this predicate over the real tree at `f0971667`:

```bash
git grep -nE '(git|GIT) +(-c [^ ]+ +)*-C +[^ ]+ +rev-parse +(--[a-z-]+ +)*--show-(prefix|toplevel|cdup)' -- '*.sh' '.githooks/*' ':!*.test.sh'
```

It printed 26 lines: 2 comments, 2 already scrubbed (`tools/workflows/check-review-join.sh` and
`tools/workflows/check-verifier-fanout.sh`) and 22 unscrubbed code lines. Unit 27 fixed the two
reached at `commit-msg`, so 20 remain. Its parked reasoning: "no line predicate discriminates the
class, since 26 probes measured differ only in whether a hook can reach them, a question about
callers".

The owner has now ruled: build the gate. The obvious design does not try to decide reachability.
It is a BAN on the unscrubbed spelling: every hit either uses the scrubbed form the two
`tools/workflows/` files already use, or sits on a waiver registry with a reason the gate prints.
Scrub the 20 where scrubbing is cheap; waive only what cannot be scrubbed.

Decide the design. Under `a-new-leg-trips-a-growing-set-of-meta-gates`, decide whether the gate is a
new leg or an arm of an existing one. Before wiring the predicate, run it over the tree and print hits
AND near-misses; unit 27 names the `--git-common-dir` near-miss in `adopt-unattended.sh`.

## TOOL-aGraftedHelix-46 — Tier-1 — govkit's conf reader and a commented quoted value

Found by unit 40, which left it open. `read_conf_key_gaps` in `tools/govkit/govkit.py` (near line
4623) states in its own docstring: "one layer of quotes is stripped, and an unquoted value keeps any
trailing comment". A QUOTED value followed by a comment, such as
`BYPASS_BAN="--no-verify"   # the flag the lander bans`, therefore keeps its quotes. Shell, which
every kit adopter sources, reads it as `--no-verify`. govkit then reports a different value from the
one the kit reads.

The unattended kit's playbook selftest pins both legal spellings in its BLOCKER 3 loop
(`tools/unattended/check-playbook.test.sh`):

- `BYPASS_BAN='--no-verify'`
- `BYPASS_BAN="--no-verify"   # the flag the lander bans`

Make govkit's reader agree with the shell on every spelling the kits accept. Under
`two-readers-of-one-config-one-re-derived`, find every other conf reader in govkit and in the
memory-tree kit's `parse_conf_line`. Either make them one derivation, or pin each to the same
spellings with an arm.

## TOOL-aGraftedHelix-47 — Tier-2 — check-arms.py's second discovery signature

This closes the open ask `TOOL-aDeferredBar-8`, filed in `memory/builds/aDeferredBar/BACKLOG.md`
and given the KEEP triage by dDerivedDocket. Its text: `tools/memory-tree/check-arms.py` discovers
gates by a `fail() {` helper. A bar-leg adopter that exits 1 with a printed reason
(`adopt-unattended.sh` and its two siblings) therefore sits outside the arms floor. Its UNWIRED
refusal had no failing case until a closing fold wrote one by hand. The ask: add a second discovery
signature for that shape, so every adopter's `--check` is graded for an armed sibling test.

The previous run record parked a wider version of this: "a check-arms.py class gate that discovers a
delegated dispatch block setting status=1 with no fail call (checks 24, 27, 28 share the shape)".
It was refused then because it "would red check 24's block, which no unit here touches". The owner
has now adopted it. So this unit arms every block the new signature discovers in the same commit,
check 24's included, or waives one with a printed reason. Observe the signature red on a block with
no arm before adding the arms. The unit's spec names `TOOL-aDeferredBar-8` in its status header as
the ask it closes.

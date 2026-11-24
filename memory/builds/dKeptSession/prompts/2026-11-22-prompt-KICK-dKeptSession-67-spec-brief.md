**Serves:** research KICK-dKeptSession-67

# Brief — dKeptSession: a pass that changes a policy-mirror input merges through pass-tree.sh

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-16's pass changes `tools/policy/catalogue.toml` and carries its re-rendered `.governance/policy.json`
(commit `4ee5af863` on `worktree-wf_ce213496-950-1`, where `policy.py mirror --check` prints `policy: mirror fresh`).
Its pass legs are green. Even so, `bash tools/unattended/pass-tree.sh --merge dKeptSession --pass KICK-dKeptSession-16
--branch worktree-wf_ce213496-950-1 --from b4b570ef771580c665b07105eb9c85d33ae89926` refuses every time, with the
following lines:

- `regen: FAILED · stage 2 · policy · .governance/policy.json · write: python tools/policy/policy.py mirror --write (exit 2, 0s)`
- `policy: refused · tools/policy/catalogue.toml@9d43738c:0 · uncommitted changes; the mirror renders a revision, commit first`
- `pass-tree: REFUSING - the regeneration failed, as its lines above say, so the merge was undone`

The cause: `run_pass_tree_regen` in `tools/unattended/pass-tree.sh` runs `regen.py --write` over the merge before it
is committed. `policy.py`'s `cmd_mirror` refuses `--write` and `--check` alike while any mirror input (the policy file,
the catalogue, or a `derive_mirror_inputs` file) differs in the working tree from HEAD. So no pass that changes a mirror
input can ever merge. These open specs name `tools/policy/catalogue.toml` or `tools/policy/presets.toml`: 6, 7, 8, 9,
10, 11, 13, 14, 17, 21, 24, 35, 41 and 44. Protocol §11 and the verbs' "A BLOCKER between you and your own landing is
a discovery" adopt this as a unit of this build: KICK-dKeptSession-67, added by `--rescope --act add`.

Write its spec as a new file, `memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-67.md`, to
`memory/TEMPLATE-SPEC.md`. Header: Status `INPROGRESS`, rev-1, 2026-11-22, node d, Tier-2, base `ce776cccc`, streams
tooling, order 7, advances KICK-dKeptSession-29. Read the other specs of this build for the header's exact shape.

### Items

1. F-design: choose where the fix lives, with the alternatives in §4's rejected list. Candidates:
   - pass-tree's regen judges the merge as it will be committed, not against HEAD;
   - pass-tree commits the merge and then regenerates in a follow-up commit;
   - the policy kit's `[[generated]]` row, or `cmd_mirror`, accepts a staged mirror equal to the render of the staged inputs.

   The fix must keep the reasons the refusal exists (TOOL-dGroundRules-25 S20: never render a revision other than the one
   committed). It must not loosen a mirror check that the push boundary or the policy guard relies on, and it must not
   make the lander's merge behave differently from this one. Read `tools/push-main.sh` and the lander's `run_regen` for
   how a landing regenerates. If a governance carrier would need changing, say so in §8 as an open fork rather than
   ruling it.
2. F-behaviour: the criteria observe the fix on a fixture, never by hand. Use the pass-tree suite where one exists (find
   it by grepping `pass-tree` under `tools/unattended/`). The fixture repository changes a mirror input in a pass and
   carries its re-rendered mirror. Show the merge commits on the new code and is refused at the base. Add a second case:
   a pass that changes a mirror input but carries a stale mirror is still refused. Name the `New arm:` line, and give
   each criterion's command its exact exit and output.
3. F-hook-paths: Files touched names every path the commit hook moves. That includes `memory/map/generated/symbols.json`
   for a new function; a suite budget row in `tools/run-gates/selftest-budgets.txt` where a `plants=<n>` token moves; and
   the guarded legs the touched paths trip, on the §7 leg line. No shipped file may spell a kit path such as
   `tools/policy/README.md`, which the install-prefix leg bans.
4. Pin every figure (DERIVED or PINNED), cite code as `path#symbol` (no `path:number` token unless it is a blob pin), keep
   within the live-spec size cap, and leave no fork open except a governance-carrier one. Rule a fork as
   `RESOLVED (agent, 2026-11-22, delegated): <option>, rung <n>; <reason>. widens: <value|none> · relaxes: <value|none>`.

### Acceptance

The new spec exists. `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`,
`python tools/check-spec-tokens.py --spec <path>`, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
and `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-67` report nothing for it.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than the new one. Never edit
`memory/builds/dKeptSession/README.md`; the main loop renders it.

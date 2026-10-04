# Run mandate — dUnstuckLanding

**Serves:** journal TOOL-dUnstuckLanding-1 TOOL-dUnstuckLanding-2

node d · 2026-10-04 · order 0 · streams tooling · authorized-by prompt

## The prompt, verbatim

The owner invoked `/unattended` with `--prompt` and this value. It is taken as the prompt itself,
because it carries whitespace and names no readable file:

```
Closing unattended builds often faces a multitude of problems and frequently leads its session to set them to ABORTED status which they remain in forever, because they land attended. One of the more frequent problems would be pre-existing red gates, inherited from the main tree or another build, which do not get resolved in the unattended build automatically (why?). Another problem would be closing decisions that sometimes agents refuse to take and leave it to the owner, even though the builds are unattended. This leads to an ambiguous status and confusing records afterwards. Review the historical problems unattended builds face at closing times (in this repo, inCMS or NicoCares). Research and design improvements to the unattended kit so runs can close their builds efficiently, fully unattended, without interruption. Additionally, design another, separate verbs for builds that are interrupted and then land attended, other than ABORTED.
```

The prompt bytes are copied here rather than referenced, because the build folder is the
authorization and must not point at a file that can be edited after the run starts.

## What it resolves to

- **Scope.** Research the closing-time failures, then design. "Research and design" is read
  literally: the deliverables are records, and the kit itself is not edited here. Each design
  mechanism becomes an ask with `seen` and `accept` clauses, filed in this build's `BACKLOG.md`.
- **Repositories read.** `C:/projects/coding-governance` (origin/main), `C:/projects/incms/main` and
  `C:/projects/nicocares/main`, together with their worktrees. These are read-only sources.
- **The "why" the owner asked.** The census answers why an inherited red is not resolved
  in-run. The answer comes from the driver and the contract, and is cited.
- **No owner question was asked.** The prompt names the acceptance (a cited census, a design, and
  verbs other than `ABORTED` for an attended landing). The gates are the memory-tree hygiene leg
  over the records, and the bar at `--close`.

# dOrderedCharter — the landing handed to the owner

**Serves:** journal PLAY-dOrderedCharter-1

## Why the run cannot land itself

After the reconcile merge (PLAY-dOrderedCharter-83) the lander's `push-main.sh --prepare` got past the conflicts and stopped
at its regeneration. Its own update applied the upgrade step `playbook/adopter-rules-to-overlay`, which this build's unit 31
ships: the step takes `[charter] adopter_rules` out of `.governance/deploy.toml` and writes the rules as level-0 units of
`.governance/instructions.toml`. The regeneration then refused at the policy mirror, because `policy.py mirror --write`
renders only a committed revision and `.governance/instructions.toml` was not committed. The lander restored the branch and
changed nothing.

Committing the step's output is the owner's: `tools/policy/guarded-paths.txt` lists both `.governance/deploy.toml` and
`.governance/instructions.toml`, and the policy guard refuses an agent's commit that changes either.

## What the owner runs, from a terminal, on the run branch

The main loop rehearsed steps 1 and 2 in the working tree at `6241e72bb` and restored it: the patch's deploy hunk applies, the
step moves the nine adopter rules, and its witness reports applied.

1. Apply the deploy-rule edit the owner ordered mid-run (`2026-11-11-build-PLAY-dOrderedCharter-1-owner-waiting-items.md`), its
   deploy hunk only: the third adopter rule names the playbook renderer, `playbook-render`, where it named the retired
   agent-instructions kit.
2. `python tools/govkit/steps/adopter_rules_to_overlay.py up .`
3. Commit `.governance/deploy.toml`, `.governance/instructions.toml` and the before-image under `.governance/steps/` from the
   terminal.
4. Then land: `bash tools/push-main.sh --prepare --slug dOrderedCharter`, `bash tools/unattended/unattended.sh --authorization
   dOrderedCharter`, `--close dOrderedCharter` with its bar run without the unattended kit gate and without self-tests, as the
   owner ruled, `bash tools/push-main.sh --land --slug dOrderedCharter`, and `--settle dOrderedCharter`. Or say "resume" and the
   session runs step 4.

## The defect it shows

`push-main.sh --prepare` applies upgrade steps and then regenerates, and the policy mirror refuses an uncommitted input, so any
pending step that writes `.governance/instructions.toml` stops every lander, attended or not. Under an agent the step's output
cannot be committed at all, because both files it writes are guarded. Either the prepare commits a step's output before its
regeneration, under an owner-only path, or a step that writes a guarded file is refused at `--prepare` with the owner's remedy
named. This is the owner's call; no unit is opened for it.

## Owed after landing

- The ask spec 83's F1 named: the memory-tree kit's closing-review drive row restates the lookup main retired.
- Every earlier owner-facing item stays as the close records it: ask 66, the unarmed refusal sites, the RED-first observations,
  and the inherited policy-check red.

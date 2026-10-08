---
name: a-grep-for-a-word-is-a-presence-probe
description: a grep for a word over a source file proves the word is there, not that the code around it runs, so a comment or a dead block satisfies the criterion it was written to observe
kind: class
universal: false
---

# Finding the word is not watching the code

## Symptom

An acceptance criterion observes a new branch of a gate by grepping the gate's source for a word
the branch must contain: the mode it calls, the check number it keys, the flag it passes. The grep
prints a line number and the criterion reads as held. But a comment spelling the mode satisfies it,
and so does a block that calls the mode and then discards its exit status. The criterion observed
that the word was written down, not that the gate reds.

This is the mirror of `absence-assertion-over-whole-file-text`: there a ban over whole-file text
reds on the comment documenting its own fix; here a presence probe passes on it.

## Where it bit

`TOOL-aGraftedHelix-6` wired hygiene check 28 into `tools/memory-tree/check-memory-hygiene.sh` as a
block delegating to `row_grammar.py --check-content`. Its one criterion on that block was a grep for
`check-content`, which printed one line; every other criterion ran the module directly, never the
engine. A block that swallowed the module's exit would have left the `memory hygiene` leg green over
a duplicated record. Check 27's block, from `TOOL-aGraftedHelix-9`, shipped with the same single
grep. The round-1 spec audit of that build named the class (finding 20), and
`TOOL-aGraftedHelix-13` and `TOOL-aGraftedHelix-14` added engine arms to
`tools/memory-tree/check-memory-hygiene.test.sh` that run the gate over a fixture and read its exit,
its finding line and its `--offenders` key, each observed red with one line of the block deleted.

## The fix

Observe a gate's branch by RUNNING the gate: a fixture that should red it, the exit code and the
finding line read back, and the same run on a clean tree reading the green summary. Then stage the
break the probe would miss, a deleted `status=1` or a deleted print, and watch the arm go red. A grep
may locate the block for a reader; it is never the observation.

**Gated by `python tools/memory-tree/check-arms.py --check`, under `ARMS_REFUSALS`.** Its second
discovery signature, from `TOOL-aGraftedHelix-47`, counts a delegated dispatch block, one that
prints a module's capture and sets `status=1` with no `fail <n>` call, as a refusal site. The site
reads ARMED only when the block's `# arm-signature:` marker names text that a positive assertion in
the engine's sibling suite carries, which an engine arm is the only natural place to write; check
24's block gained its arm in that unit. Otherwise the site is pinned in
`memory/project/unarmed-branches.txt` with a reason the gate prints on every run. The gate trusts
the marker: it does not check that the arm RUNS the engine or has been seen red, so a review of a
diff adding a delegated block still asks both.

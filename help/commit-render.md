# The commit render

**What it is.** A commit that stages a memory change without re-rendering the build index is
refused by the memory hygiene leg's check 9, and the usual remedy is to run the generator's
`--write`, stage what it wrote and commit again. With the switch below on, the pre-commit hook
takes that remedy itself: it renders the moved index artifacts, stages them into the same commit
and grades the hygiene leg again. That second grading decides, so the verdict is the one the
manual remedy gets.

## Turn it on

The switch is `STAGED_RENDER` in the repository's `.memory-tree.conf`. It is blank, which is off,
in the memory-tree kit's example conf, because a hook that adds paths nobody staged is new
behaviour in an adopter. Set it to `1` to turn it on:

```text
STAGED_RENDER="1"
```

Any value other than blank or `1` is refused by name, and the commit is refused as before.

## What the hook does

1. It runs the staged hygiene leg and holds its output, then prints it.
2. When the leg failed with a line opening `HYGIENE check <N> FAILED`, N = 9, it runs the generator's
   `--write-staged` mode under the index git handed it. Any other failure refuses as before.
3. The mode writes only the artifacts whose bytes moved and stages them, with any orphaned ledger
   shard it removes, and prints one `build-index: staged <path>` line per path.
4. When the mode staged a path, the hook prints one line and grades the hygiene leg again, and
   that run's exit is the leg's verdict.

```text
pre-commit: the build index was rendered and staged; grading the memory hygiene leg again.
```

## When it declines

The mode writes nothing, prints `build-index: render NOT staged — <why>`, exits 1, and the hook
refuses the commit as it does today, when:

- `STAGED_RENDER` is blank;
- the hook's index is neither the repository's own index nor its `.lock`. A partial commit,
  `git commit <path>`, hands the hook a separate index, so the render is never staged there;
- a render input, a path under the memory root, the conf or the kit, carries an unstaged change,
  since the render would then not be what the commit carries;
- the data-loss guard holds a backlog view;
- no artifact's bytes moved, so check 9's refusal is not drift a render cures.

## What it does not check

- Under `git commit -a` the hygiene leg reads the repository's index, not the hook's, so check 9
  may not refuse at all, and the render is never reached.
- The second grading proves the commit is clean as staged. It does not prove the render was
  needed.

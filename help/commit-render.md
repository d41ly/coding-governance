# The commit render

**What it is.** A commit that stages a memory change without re-rendering the build index is
refused by the memory hygiene leg's check 9, and the usual remedy is to run the generator's
`--write`, stage what it wrote and commit again. With the switch below on, the pre-commit hook
takes that remedy itself: it renders the moved index artifacts, stages them into the same commit
and grades the hygiene leg again. That second grading decides, so the verdict is the one the
manual remedy gets.

## Turn it on

`memory.staged-render` in `.governance/policy.toml` turns the render on or off. <!-- usage: policy:memory.staged-render e73726fb -->
Its default is `off`, because a hook that adds paths nobody staged is new behaviour in an adopter.
Set it to `on` to turn it on:

```toml
[memory]
staged-render = "on"
```

The key is read at the landed revision, the default branch as the remote holds it, so a branch
cannot turn its own render on: the hook declines until the line reaches the default branch. Where
no policy kit is installed beside the memory-tree kit, the switch reads off.

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

- `memory.staged-render` reads anything but `on`, or the policy reader refuses, which the line
  names with the reader's own words;
- the hook's index is neither the repository's own index nor its `.lock`. A partial commit,
  `git commit <path>`, hands the hook a separate index, so the render is never staged there;
- a render input, a path under the memory root, the conf or the kit, carries an unstaged change,
  since the render would then not be what the commit carries;
- the data-loss guard holds a backlog view;
- the as-built view cannot be rendered, so the render has nothing to stage;
- no artifact's bytes moved, so check 9's refusal is not drift a render cures.

A refusal while the mode renders or stages puts back every file it wrote, and the hook refuses the
commit as before.

## What it does not check

- Under `git commit -a` the hygiene leg reads the repository's index, not the hook's, so check 9
  may not refuse at all, and the render is never reached.
- The second grading proves the commit is clean as staged. It does not prove the render was
  needed.

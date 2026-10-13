# Range-reader audit — does a gov check read a merge of the default branch as additions?

**Serves:** journal TOOL-dSweptBranches-20

node d · 2026-10-13 · closes ask `TOOL-dSweptBranches-6`. inCMS's memory-local check 21 reads a
merge of the default branch into a feature branch as adding every `memory/` file the default branch
gained; its sibling check 29 skips merge commits. This record names every gov site that reads added
files or per-commit diffs, decides each by its invocation's SHAPE and BASE, and keeps the probe that
measured the shapes beside its output.

## Verdict

No gov check grades a merged-in file as this branch's new work in a way that changes a verdict. Two
sites read the staged set, which a merge in progress fills with every file the default branch gained:

- `tools/hooks/scratch-guard.js:680` exempts a commit that ADDS a prompt-authorized build README
  from the kickoff gate, so a merge that brings one in is exempted too. Filed as
  `TOOL-dSweptBranches-22`.
- `tools/unattended/unattended.sh:7623` (`read_pinned_base`) reads a staged run-state archive as a
  rotation in doubt. It fails closed, refusing a landing as a doubt; filed under the same ask.

The pre-commit hygiene leg reads the merged-in `memory/` files too, and the probe measured it
harmless: it grades their content, which the default branch already holds (exit 0, 0 FAILED).

## The probe and its output

The fixture is gov itself: a feature branch cut at `6e8f8b1d` (main before the cListedCensus
landing) with one commit outside `memory/`, merging `2b852f5f`, which added seven `memory/` files.
The probe asserts that liveness first.

```text
fixture: 2b852f5fd87147540a0a73d310354440c84c72ea added 7 memory/ file(s) after 6e8f8b1da4dc036b7fce23555b78fb4b5db0e60c; the feature commit added none
== S-staged  git diff --cached --diff-filter=A -- memory (a merge in progress): 7
== S-staged  gov's own check-memory-hygiene.sh --staged over that index:
   exit 0 · 0 FAILED line(s)
== S-log     git log --diff-filter=A --name-only FROZEN-BASE..HEAD -- memory (no -m): 7
== S-log     git log --diff-filter=A --name-only DEFAULT..HEAD -- memory (no -m):      0
== S-log-m   git log -m --diff-filter=A --name-only DEFAULT..HEAD -- memory:          7
== S-fp      git log --first-parent --diff-filter=A FROZEN-BASE..HEAD -- memory:      7
== S-3dot    git diff --diff-filter=A DEFAULT...HEAD -- memory:                       0
== S-tree    git diff-tree -r --diff-filter=A MERGE -- memory (no -m):                0
== S-tree-m  git diff-tree -m -r --diff-filter=A MERGE -- memory:                     7
== S-anc     git log --ancestry-path --diff-filter=A ^FEATURE HEAD -- memory:         0
```

`--first-parent` reads the merged-in files: since git 2.31 it diffs a merge against its first
parent, so it is not the fix it looks like. The class record,
`memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`, carries the shape table.

```bash
#!/usr/bin/env bash
# range-probe.sh <repo> <scratch dir> <old default> <new default>
# TOOL-dSweptBranches-20: does each invocation shape read a merge of the default branch as additions?
# A feature branch is cut at <old default>, gains one commit outside memory/, and merges
# <new default>, which added memory/ files after <old default>. Every shape then runs over it.
set -u
REPO=$1 WT=$2/probe OLD=$3 NEW=$4
git -C "$REPO" worktree add -q --detach "$WT" "$OLD" || exit 2
cd "$WT" || exit 2
git checkout -q -b probe-feature
printf 'feature work\n' > probe-feature.txt
git add probe-feature.txt
git -c core.hooksPath=/dev/null -c user.name=probe -c user.email=probe@example.invalid commit -q -m "probe: feature work"
FEAT=$(git rev-parse HEAD)
gained=$(git diff --name-only --diff-filter=A "$OLD" "$NEW" -- memory | wc -l)
echo "fixture: $NEW added $gained memory/ file(s) after $OLD; the feature commit added none"
[ "$gained" -gt 0 ] || { echo "fixture: LIVENESS FAILED — the merge would bring nothing in"; exit 1; }

git merge -q --no-ff --no-commit "$NEW" >/dev/null 2>&1
echo "== S-staged  git diff --cached --diff-filter=A -- memory (a merge in progress): $(git diff --cached --name-only --diff-filter=A -- memory | wc -l)"
echo "== S-staged  gov's own check-memory-hygiene.sh --staged over that index:"
bash tools/memory-tree/check-memory-hygiene.sh --staged > ../hygiene-staged.txt 2>&1
echo "   exit $? · $(grep -c 'FAILED' ../hygiene-staged.txt) FAILED line(s)"
grep 'FAILED' ../hygiene-staged.txt | cut -c1-200 | sed 's/^/   /'
git -c core.hooksPath=/dev/null -c user.name=probe -c user.email=probe@example.invalid commit -q -m "probe: merge the default branch"
MERGE=$(git rev-parse HEAD)

echo "== S-log     git log --diff-filter=A --name-only FROZEN-BASE..HEAD -- memory (no -m): $(git log --diff-filter=A --name-only --format= "$OLD..HEAD" -- memory | grep -c .)"
echo "== S-log     git log --diff-filter=A --name-only DEFAULT..HEAD -- memory (no -m):      $(git log --diff-filter=A --name-only --format= "$NEW..HEAD" -- memory | grep -c .)"
echo "== S-log-m   git log -m --diff-filter=A --name-only DEFAULT..HEAD -- memory:          $(git log -m --diff-filter=A --name-only --format= "$NEW..HEAD" -- memory | grep -c .)"
echo "== S-fp      git log --first-parent --diff-filter=A FROZEN-BASE..HEAD -- memory:      $(git log --first-parent --diff-filter=A --name-only --format= "$OLD..HEAD" -- memory | grep -c .)"
echo "== S-3dot    git diff --diff-filter=A DEFAULT...HEAD -- memory:                       $(git diff --name-only --diff-filter=A "$NEW...HEAD" -- memory | wc -l)"
echo "== S-tree    git diff-tree -r --diff-filter=A MERGE -- memory (no -m):                $(git diff-tree -r --no-commit-id --name-only --diff-filter=A "$MERGE" -- memory | wc -l)"
echo "== S-tree-m  git diff-tree -m -r --diff-filter=A MERGE -- memory:                     $(git diff-tree -m -r --no-commit-id --name-only --diff-filter=A "$MERGE" -- memory | wc -l)"
echo "== S-anc     git log --ancestry-path --diff-filter=A ^FEATURE HEAD -- memory:         $(git log --ancestry-path --diff-filter=A --name-only --format= "^$FEAT" HEAD -- memory | grep -c .)"
cd / && git -C "$REPO" worktree remove --force "$WT"
```

## Every hit, decided

The population is `git grep -n -E "diff-filter=[A-Z]*A|--name-status|diff-tree"` over `tools/`,
`.githooks/` and `skills/`, test suites, self-tests, fixtures and Markdown excluded.

| Site | Invocation | Shape | Verdict |
|---|---|---|---|
| `.githooks/pre-commit:180` | `diff --cached --diff-filter=ACMR -- memory/**` | staged | reads merged-in files; measured harmless, the hygiene leg grades content |
| `skills/session-kickoff/manifest-check.sh:1220` | a comment | — | no invocation |
| `tools/branch-reconcile/branch_reconcile.py:555`, `:562` | `diff-tree --cc -p <merge>` | combined | reads only the merge's own hunks, by design (unit 14) |
| `tools/check-dead-paths.sh:131` | `log --diff-filter=R` over all history | renames | reads renames, not additions |
| `tools/drift-audit/drift_report.py:835`, `:1488`, `:2790` | `log --diff-filter=A -- <path>`, full history, no `-m` | log, no base | safe: a merge carries no diff, the original add is read |
| `tools/drift-audit/drift_report.py:1494` | a comment | — | no invocation |
| `tools/govkit/govkit.py:8419` | `diff --name-status <receipt> <to>` | two trees | renames between two snapshots; no commit walk |
| `tools/govkit/govkit.py:13004` | `diff-tree -r <w>` | tree, no `-m` | safe: prints nothing for a merge |
| `tools/hooks/scratch-guard.js:680` | `diff --cached --diff-filter=A -- *builds/*/README.md` | staged | FINDING: a merge bringing a prompt-authorized README is exempted (ask 22) |
| `tools/memory-tree/check-memory-hygiene.sh:517` | `diff --cached --diff-filter=ACMR -- memory/**` | staged | as pre-commit: measured harmless |
| `tools/memory-tree/check-verdict-epoch.sh:266` | `diff-tree -U0 -r -p <c>` | tree, no `-m` | safe: a merge prints nothing |
| `tools/memory-tree/migrate_backlog.py:416` | `log --reverse --diff-filter=A`, full history | log, no base | safe |
| `tools/memory-tree/row_grammar.py:831`, `:1237`, `:1365` | comments | — | no invocation |
| `tools/memory-tree/row_grammar.py:1393` | `log --reverse -m --diff-filter=A`, full history | log `-m` | reads merges, but the earliest add wins and the original commit is in the walk |
| `tools/runlog/model.py:352` | `log --diff-filter=A -- RUN*.md`, full history | log, no base | safe |
| `tools/runlog/model.py:600` | `log --name-status`, over `--ancestry-path ^<start>` or tips | ancestry / log | safe: the merged-in commits are not descendants of the run's start |
| `tools/unattended/check-unattended.sh:715`, `:2688` | `log --diff-filter=A -- <path>`, full history | log, no base | safe |
| `tools/unattended/check-unattended.sh:1444`, `:1709`, `:1786`, `:2683`, `:4163`, `:5836`, `:5842`, `:5846`, `:5850`, `:5853` | comments, or this kit's scan of its own shell | — | no invocation over a range |
| `tools/unattended/check-unattended.sh:1726` | `diff-tree --stdin -p --cc` | combined | reads only a merge's own hunks |
| `tools/unattended/check-unattended.sh:1792` | `diff-tree --stdin -c --name-only` | combined | lists only paths a merge changed against every parent |
| `tools/unattended/check-unattended.sh:4103`, `:4173` | `diff-tree -r <c>` | tree, no `-m` | safe |
| `tools/unattended/check-unattended.sh:5057` | a verb list | — | no invocation |
| `tools/unattended/lib-unattended.sh:977` | `diff-tree -r <c>` | tree, no `-m` | safe |
| `tools/unattended/lib-unattended.sh:1611` | `log --follow --diff-filter=A`, full history | log, no base | safe |
| `tools/unattended/unattended.sh:3057`, `:3080` | `diff --name-status <anchor>...HEAD` | three dots | safe: the merge moves the merge base |
| `tools/unattended/unattended.sh:7623` | `diff --cached --diff-filter=A -- RUN.*.md` | staged | FINDING, fails closed: a merge staging this build's archive reads as a doubt (ask 22) |
| `tools/unattended/unattended.sh:7629` | `log -1 --diff-filter=A -- RUN.*.md` | log, no base | safe |
| `tools/unattended/unattended.sh:7660` | `diff-tree -r --diff-filter=A <c>` | tree, no `-m` | safe |
| `tools/unattended/unattended.sh:12954` | `diff-tree -r <c>` | tree, no `-m` | safe |
| `tools/unattended/unattended.sh:13030` | a comment | — | no invocation |

## What this does not check

A git invocation assembled at run time, or spelled without any of the three tokens, is outside the
grep's population. A check that walks a frozen base, which the table marks unsafe, is safe at every
site above only because none of them walks one over added files.

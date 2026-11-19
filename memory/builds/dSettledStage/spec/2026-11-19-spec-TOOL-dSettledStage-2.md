# TOOL-dSettledStage-2 — a commit after a stage nothing tested is gated: a fifth shell-hygiene mode

**Status:** CLOSED · rev-2 · 2026-11-19 · node d · Tier-2 · base 12764ec2 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dSettledStage-1-agent-ledger.md](../build/2026-11-19-build-TOOL-dSettledStage-1-agent-ledger.md) | journal | TOOL-dSettledStage-1 |
| [2026-11-19-build-TOOL-dSettledStage-2-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dSettledStage-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dSettledStage-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dSettledStage-1-brief.md) | research | TOOL-dSettledStage-1 |
| [2026-11-19-prompt-TOOL-dSettledStage-2-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dSettledStage-2-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dSettledStage-2-pass-legs-fix.md](../prompts/2026-11-19-prompt-TOOL-dSettledStage-2-pass-legs-fix.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Landing `12764ec21` aborted before its bar. The lander staged a tree that was dirty only by line
endings, the stage held no change, and the commit after it failed. The defect is a commit placed
after a `git add` with nothing between them testing that the stage left a diff.
`TOOL-dSettledStage-1` fixes the four lander sites. This unit gates the class, the brief's item 3
(`prompts/2026-11-19-prompt-TOOL-dSettledStage-1-brief.md`), so the next such site in any tracked
product shell source reds instead of aborting a landing.

The brief chose between a scan in `tools/gate-lint/sh_hygiene.py` and a `memory/gotchas/` class.
Its rule was a scan if its predicate is precise over the real tree, and a gotcha otherwise. The
probe in §4 ran the predicate over the tree at `12764ec21`.
It found 7 sites in 4 files, PINNED at `12764ec21`.
Every hit is a live `git add` followed by a live commit in one scope. None is in quoted text, in a
comment or in a quoted heredoc. So this unit is the scan: a fifth mode, `--stage-commits`, with its
own leg and a shrink-only registry.

## 2. Scope (IN)

- **S1** — Two parsers shared with the temp-name mode. `scan_temp_file`
  (`tools/gate-lint/sh_hygiene.py#scan_temp_file`) computes two things inline that the new mode
  needs too. One is a code line with its quoted characters blanked and its length kept. The other
  is the span of each function body. This is the second instance of each, so both are extracted.
  `build_blanked(code, keep_substitutions=False)` returns the blanked line. With
  `keep_substitutions=True`, a `$( … )` inside double quotes stays code, its own quoting tracked
  inside it. `read_function_spans(code_lines)` returns each function's `(first, last)` index, as
  `scan_temp_file` finds them today. `scan_temp_file` calls both with its present behaviour, and no
  temp-mode verdict moves. Observed by AC7.
- **S2** — The predicate, in `scan_stage_file(text)`, over `read_code_lines`, with §4's rules.
  `read_stage_helpers(code_lines)` finds the same-file functions whose bodies stage, and records
  for each whether a staged test follows its last stage. `scan_stage_tree(root, pathspecs)` runs the
  predicate over `read_shell_sources`. Observed by AC1, AC2, AC3 and AC6.
- **S3** — The mode, `sh_hygiene.py --stage-commits [registry] [root] [pathspec ...]`, in
  `run_stage_scan`. It is dispatched from `main` beside `--temp-names`. It exits 0 clean, 1 on
  findings and 2 on a refusal. It takes the registry argument's three states from
  `resolve_declaration`, and `check_registry` grades set equality with counts. Every run prints the
  scanned count, the commit count, each class's sites and files, each unpaired and empty-ok site,
  and each registered row's reason. A failing key is one finding that lists `path:line  <code>` for
  each site, followed by the remedy line. An empty population is a refusal and exits 2, as the
  sibling modes do. The module docstring gains the usage line and a paragraph naming the fifth
  class. `run_stage_scan`'s docstring states what the mode does not check, one entry per row of
  `STAGE_BOUNDARY`. Observed by AC1, AC2, AC3 and AC4.
- **S4** — The selftest. `run_selftest` gains one row per fixture in §4's table, one row per
  `STAGE_BOUNDARY` entry, and a registry arm. The boundary arm checks three things for each row:
  the example lands in its class, the label is named in the docstring, and the label is named in
  the README's `--stage-commits` section. `FLOOR_ASSERTIONS`
  (`tools/gate-lint/sh_hygiene.py@448d62cb:231`) rises from 125 to the count the selftest prints.
  Its comment names this unit and the arms counted. Observed by AC6.
- **S5** — The registry, `memory/project/stage-commit-sites.txt`, in `temp-name-sites.txt`'s header
  form, keyed on the path and the one class `unchecked-stage`. It declares §4's three rows, each
  with its reason. `.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA`
  (`.memory-tree.conf@17effb7c:956`) gains `stage-commit-sites.txt` after `unpinned-facts.txt`. A
  member comment above it takes the form of the comments already there, naming this unit.
  Observed by AC4.
- **S6** — The leg declarations. `tools/gate-legs.json` gains the row `shell hygiene (a stage
  committed with no staged-diff test)` after `shell hygiene (a fixed-name temp renamed into place)`.
  Its argv is `python3 {prefix}/gate-lint/sh_hygiene.py --stage-commits
  memory/project/stage-commit-sites.txt . :!*.test.sh :!memory/`. It has chunk `product`, subject
  `repo`, ceiling 300, stage `step.test` and no guard. `tools/gate-lint/kit.toml` gains a
  `[[gate_leg]]` of that name with subject `repo`, argv `["python3", "{kit}/sh_hygiene.py",
  "--stage-commits"]`, `guard = []` and stage `["step.test"]`, plus a comment in the temp-name
  leg's form (`tools/gate-lint/kit.toml@61946391:97-108`). The gate-lint dossier,
  `memory/map/features/gate-lint.md`, lists the leg's name under its `gate-legs` key. Its
  Affordances gain the mode and the registry, in the temp-name entries' form. `tools/gate-lint/README.md`
  gains a `--stage-commits` section after the `--temp-names` one. `tools/govkit/subject-pins.tsv`
  takes its row from `python tools/govkit/govkit.py selfcheck --write`, which generates that file.
  Observed by AC5.
- **S7** — The record. `python tools/codebase-map/gen_map.py --write` runs before the product commit
  `<p2>`, because the unit mints Python functions. `tools/gate-legs.json` and `.memory-tree.conf`
  are on the kickoff manifest's `watch:` line (`memory/guides/SESSION-KICKOFF.md@22b6155f:7`). So
  `<p2>` moves the manifest's `last-audit:` stamp, which the manifest check's staged leg requires.
  A second commit, `<p2m>`, re-stamps it at `<p2>` after a section B re-read, with a
  `manifest-audit:` line in its body. `be022852d` did the same for the temp-name leg. The readings
  go to an acceptance ledger under `memory/builds/dSettledStage/build/` carrying
  `**Serves:** journal TOOL-dSettledStage-2`. The build edits no spec but this one's status and
  date cells. Observed by AC8.

## 3. Non-goals (OUT)

- Fixing the lander's four sites. That is `TOOL-dSettledStage-1`, which this unit is ordered after.
- Fixing the three registered sites (§4). The brief makes a `tools/unattended/` site a recorded
  follow-up and not a fix here. `pass-tree.sh` concludes a merge, and the fixture writes a fresh
  repository's first commit, so neither can commit an empty stage.
- Commit sites in Python. The population is shell sources alone, as for every `sh_hygiene.py` mode.
  Measured at `12764ec21`, product Python stages with `git add` in `tools/govkit/govkit.py` and
  `tools/codebase-map/map_lib.py` and commits nowhere, so no Python instance of the class exists
  today.
- Suites. The leg excludes `*.test.sh`, as the spawn-idiom and temp-name legs do. Every suite builds
  fixture repositories whose commits stage new files.
  The probe read 977 such sites in 54 files, PINNED at `12764ec21`.
- A `memory/gotchas/` class. It was the brief's fallback, and the probe in §4 decided against it.
- A help page. No page under `help/` documents gate-lint. `entry:gate-lint` is a row of
  `memory/project/docs-undocumented.txt`, and the docs leg's members are kits, verbs, hooks and keys,
  not individual legs. A page is a separate document (M2).
- No kit version moves. `tools/gate-lint/kit.toml` declares `version_from = { none = … }`
  (`tools/gate-lint/kit.toml@61946391:7`).

### Edges

- **consumes-from** `TOOL-dSettledStage-1` — the lander's four commit sites, each staging through
  `write_staged_change`, the same-file helper that runs `git diff --cached --quiet` after its
  `git add -A`. AC3 and AC4 read the fixed tree, where the four commits read admitted. Without that
  fix the new leg reds on `tools/push-main.sh` at the bar.
- **hands-off** external — the `write_run_record` commit in `tools/unattended/unattended.sh`. It is a
  true instance: a render that leaves the record's bytes unchanged stages nothing, and the commit
  fails with a printed line. It is registered here and drained by deleting its row in the commit
  that fixes it, for the owner to promote as a unit.

## 4. Design

### Evidence, read at `12764ec21` on 2026-11-19

`0563a02ee`, this worktree's HEAD, changes no file under `tools/`, `skills/` or `.githooks/` from
`12764ec21` (`git diff --stat 12764ec21 HEAD -- tools skills .githooks` prints nothing). The
lander's blob is `cd8cf562` at both.

The lander's four sites are `write_merge_fold` (`tools/push-main.sh@cd8cf562:1062-1066`) and the
mint, gov-first and regen blocks (`tools/push-main.sh@cd8cf562:1344-1351`, `:1369-1376`,
`:1393-1400`). Each tests `git status --porcelain` non-empty, runs `git add -A`, and commits with
`git commit` or, in `write_merge_fold`, `git commit-tree "$(git write-tree)"`. The status test is not
the defect. Staging can normalise a dirty file back to its committed bytes, and only a test of the
stage itself sees that.

### The class, probed

A read-only probe was built on `sh_hygiene.py`'s own parsers: `read_shell_sources`,
`read_code_lines`, `read_function_bodies`, `FUNCTION_DEF` and `PROBE_WORD`. It applied the
predicate below to the leg's population, `. :!*.test.sh :!memory/`, at `12764ec21`. All counts are
PINNED there on 2026-11-19 and DERIVED at observation.

| Reading | Count | Sites |
|---|---|---|
| sources scanned | 75 | — |
| unchecked, GATED | 7 in 4 files, PINNED | `tools/push-main.sh` lines 1065, 1347, 1372 and 1396; `tools/unattended/unattended.sh` line 16592; `tools/unattended/pass-tree.sh` line 271; `skills/session-kickoff/card-compaction.fixture.sh` line 44 |
| admitted | 0 | — |
| unpaired | 2 in 1 file | `tools/unattended/unattended.sh` lines 2789 and 11434 |
| empty-ok | 0 | — |

The same predicate run on raw code halves, with no quote blanking, read 8 unchecked sites. Two were
`echo` text naming `git add` and `git commit`, and the probe's own regex dropped one live
`git -c "<quoted>" commit`. Blanking quoted text while keeping `$( )` inside double quotes as code is
what made the reading exact. Following stagers one hop changed no count on the tree: no stager is
called in a scope that commits. The follow is kept for the shape `TOOL-dSettledStage-1` builds.
Its spec's S1 to S3 define `write_staged_change`, which runs `git add -A` and then
`git diff --cached --quiet`, and its four callers commit. Under the follow each call is a stage
followed by a staged test, so the four commits read admitted. Without the follow they would read
unpaired, and the lander would pass for the wrong reason.

Two readings of git's behaviour, taken on 2026-11-19 in a fixture repository under `%TEMP%`, back
the registry's reasons. After `git merge --no-commit --no-ff side` and `git add -A`,
`git diff --cached --quiet` exits 0, yet `git commit` exits 0 and records two parents. A merge
conclusion therefore never fails empty. The fixture at
`skills/session-kickoff/card-compaction.fixture.sh@b79ea803:39-44` runs `git init`, writes two files,
stages them and commits, so its stage is never empty.

### The predicate

Each tracked shell source is read through `read_code_lines`, so comment halves and quoted heredoc
bodies are never graded.

| Step | Rule |
|---|---|
| a git word | `git` or `GIT` not preceded by a word character, `$`, `.` or `-`, followed by any run of `-c <word>` or `-C <word>`, with `<word>` as `PROBE_WORD` reads it. So `run_bounded git -c "$K" commit` and `GIT add` are read |
| an event | a git word, then `add`, `commit`, `commit-tree`, `diff` or `diff-index` as a whole word, matched on the code half. It counts only where `build_blanked(code, keep_substitutions=True)` leaves both the git word and the verb unblanked, so text inside quotes is data and a `"$(git … )"` is code |
| a staged test | a `diff` or `diff-index` event whose arguments, up to the next `;`, `&`, `\|` or `)`, carry `--cached` or `--staged`, whatever its output form |
| a stage | an `add` event, or a call to a stager: an unblanked whole-word name of a same-file function whose body holds an `add` event. The name may not follow `$`, and may not be followed by `=`, `+=` or `[`, so a same-named variable is not a call. A function's own definition line is not a call |
| a checked stager | a stager whose body holds a staged test after its last `add` event. Its call counts as a stage followed at once by a staged test |
| scope | the innermost function whose span, from `read_function_spans`, holds the line; else the top level |
| a commit | a `commit` or `commit-tree` event |
| verdict | events in one scope are read in line and column order. A commit carrying `--allow-empty` is `empty-ok`. A commit with no stage above it in its scope is `unpaired`. A commit after a stage with a staged test between them is `admitted`. Any other commit is `unchecked`, the one GATED class |

The taxonomy is `STAGE_CLASSES`, in report order: `unchecked` GATED, then `admitted`, `unpaired` and
`empty-ok`, the last three counted and never gated. The registry is `read_registry`'s grammar,
`<path>\tunchecked-stage\t<count>\t<reason>`, with the key shape `STAGE_KEY_SHAPE`, the pattern
`\Aunchecked-stage\Z`. A line number is refused as malformed. `STAGE_UNDECLARED` is a key's
undeclared text. `STAGE_REMEDY` reads: test the stage before committing it, with
`git diff --cached --quiet` after the `git add`, and skip the commit when it exits 0.

### What the mode does not check: `STAGE_BOUNDARY`

One row per form: a label, a shell example, and the class it lands in. `unread` means no commit is
counted. The selftest runs each example, and the docstring and the README name each label, as
`TEMP_BOUNDARY` does for the temp-name mode.

| Label | Example | Class |
|---|---|---|
| a stage in another scope | `git add -A` in one function, `git commit -q -m x` in another that does not call it | unpaired |
| a stager in a sourced library | `. ./lib.sh`, then `stage_all`, then `git commit -q -m x` | unpaired |
| a commit that stages with -a | `git commit -qam x` | unpaired |
| a staged test whose answer does not gate the commit | `git add -A`, then `n=$(git diff --cached --name-only \| wc -l)`, then `git commit -q -m x` | admitted |
| a stage and a test in two repositories | `git -C a add -A`, then `git -C b diff --cached --quiet \|\| git -C b commit -q -m x` | admitted |
| a git verb behind a variable | `git add -A`, then `$GITCMD commit -q -m x` | unread |
| a commit inside a quoted string or under eval | `git add -A`, then `eval "git commit -q -m x"` | unread |
| a git verb split across a line continuation | `git add -A`, then `git -c a=b \` with `commit -q -m x` on the next line | unread |
| a merge conclusion | `git merge --no-commit -q side`, then `git add -A`, then `git commit -q -m m` | unchecked |
| a first commit in a fresh repository | `git init -q .`, then `git add -A`, then `git commit -q -m first` | unchecked |

The last two are the mode's known false reds. Both commit successfully on an empty stage, as the
probe above read for the first, and the registry is where a site of either shape lands. Python
inside a shell string, and any commit in another language, has no shell example and is named in the
docstring alone.

### The selftest's fixture rows

| Fixture | Expected |
|---|---|
| the regen shape: a `git status --porcelain` test, `git add -A`, `git commit -q -m x` | 1 unchecked |
| `git add -A`, then `if ! git diff --cached --quiet; then git commit -q -m x; fi` | 1 admitted |
| a staged test above the `git add -A`, then `git commit -m x` | 1 unchecked |
| a checked stager, `stage_tree() { git add -A; ! git diff --cached --quiet; }` on three lines, then `if stage_tree; then git commit -q -m x; fi` | 1 admitted |
| an unchecked stager, whose body is `git add -A` alone, called before `git commit -q -m x` | 1 unchecked |
| `git add -A` then `t=$(git commit-tree "$(git write-tree)" -p "$1" -m m)` in one function | 1 unchecked |
| the same with `git diff --cached --quiet && return 0` between them | 1 admitted |
| `git add -A` then `git commit --allow-empty -m x` | 1 empty-ok |
| `echo "run git add -A && git commit"` | no commit counted |
| `# git add -A; git commit -m x` | no commit counted |
| the same two commands in a `<<'EOF'` body | no commit counted |
| `GIT add -A -- "$p"` then `run_bounded git -c "$K" commit -q -m x` | 1 unchecked |
| `git add -A` then `[ -n "$(git diff --cached --name-only)" ] && git commit -m x` | 1 admitted |
| `git add -A` then `git diff-index --quiet --cached HEAD \|\| git commit -m x` | 1 admitted |
| a function `stage` that stages, then `stage=1` and `git commit -q -m x` | 1 unpaired |
| registry: `check_registry` with `STAGE_UNDECLARED` over one undeclared key and one stale row | two findings, the first in the mode's words |

The probe ran every row but the last two through the candidate predicate on 2026-11-19, and each
read as the table says.

### The registry's rows

| Path | Count | Reason |
|---|---|---|
| `skills/session-kickoff/card-compaction.fixture.sh` | 1 | a fixture's first commit in the repository it just created, after staging the two files it wrote, so the stage is never empty |
| `tools/unattended/pass-tree.sh` | 1 | concludes a merge in progress, which commits on an empty stage |
| `tools/unattended/unattended.sh` | 1 | `write_run_record`'s close commit, a true instance: an unchanged record stages nothing and the commit fails with a printed line; the follow-up the dSettledStage brief records |

Every reason closes with "predates the lint; drained by deleting this row in the commit that fixes
it".

### Order

**Order 2**, after `TOOL-dSettledStage-1`'s order 1. The leg's population holds `tools/push-main.sh`,
and the leg is green there only once unit 1 has landed its staged-diff tests. The two units share no
written path but the ledger folder.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `build_blanked`, `build_stage_measured` | functions in `sh_hygiene.py` | `py.function`, `build` |
| `read_function_spans`, `read_stage_helpers` | functions in `sh_hygiene.py` | `py.function`, `read` |
| `scan_stage_file`, `scan_stage_tree` | functions in `sh_hygiene.py` | `py.function`, `scan` |
| `run_stage_scan` | a function in `sh_hygiene.py` | `py.function`, `run` |
| `print_stage_populations` | a function in `sh_hygiene.py` | `py.function`, `print` |
| `STAGE_EVENT`, `STAGE_CLASSES`, `STAGE_BOUNDARY`, `STAGE_KEY`, `STAGE_KEY_SHAPE`, `STAGE_UNDECLARED`, `STAGE_REMEDY` | constants in `sh_hygiene.py` | `py.constant`, screaming |
| `--stage-commits` | a mode flag | none |
| `unchecked-stage` | a registry class key | none |
| `shell hygiene (a stage committed with no staged-diff test)` | a gate leg | none |
| `stage-commit-sites.txt` | a registry under `memory/project/` | `PROJECT_REGISTRY_EXTRA` |

Each function name answered OK under `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` on 2026-11-19. A `git grep` outside `memory/builds/` for each identifier above found
none at `12764ec21`.

### Files touched (estimate)

- `tools/gate-lint/sh_hygiene.py`
- `tools/gate-lint/kit.toml`
- `tools/gate-lint/README.md`
- `tools/gate-legs.json`
- `tools/govkit/subject-pins.tsv`
- `memory/project/stage-commit-sites.txt`
- `.memory-tree.conf`
- `memory/map/features/gate-lint.md`
- `memory/map/generated/`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/dSettledStage/build/`

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| A `memory/gotchas/` class claimed in a dossier, the brief's fallback | the probe read every hit as a live stage-then-commit, so the brief's precision condition for the scan holds, and a checklist entry reds nothing | Rejected |
| Requiring the `git status --porcelain` test as part of the class | `unattended.sh` line 16592 stages a list derived from dirty paths and has no porcelain test in its scope, yet fails the same way | Rejected; the class is the commit, not the status test |
| Matching on raw code halves | read 8 sites, two of them `echo` text | Rejected; quoted text is blanked |
| `build_unquoted` (`tools/gate-lint/sh_hygiene.py#build_unquoted`) as the blanker | it collapses each quoted run and each `$( )` to one character, so offsets move and `t=$(git commit-tree …)` disappears | Rejected; S1 extracts the temp mode's blanker |
| A fourth copy of the inline blanker and span loop | the charter's [reuse] rule: the second instance extracts the factory | Rejected; S1 |
| A check inside an existing shell-hygiene leg | each of the four legs is named for its own class, and the registry rows and the dossier claim name the class | Rejected; S6 adds a leg, as `TOOL-dRedressedBar-24` did |
| `*.test.sh` in the population | 977 fixture commits in 54 suite files | Rejected; the leg excludes suites |
| Excluding `*.fixture.sh` by pathspec | one site, and a registry row states its reason on every run where a pathspec says nothing | Rejected; registered |

## 5. Production-readiness checklist

- security — No write path, surface or egress. The mode reads tracked files through `git ls-files`
  and writes nothing.
- perf / scale — One more pass over the 75 product shell sources the temp-name leg already reads,
  two regex scans per code line. Ceiling 300, as the sibling legs have.
- error / empty / loading states — An empty population, a failed `git ls-files` and a supplied
  registry that does not resolve each exit 2 with a named refusal, through the paths the sibling
  modes use.
- observability — Every run prints the population, each class's counts, each unpaired and empty-ok
  site, and each registered reason. A failing key lists its sites.
- risks — A known false red on a merge conclusion and on a fresh repository's first commit, each
  costing a registry row. An adopter's first run reds on every site it carries, because the
  `[[gate_leg]]` argv passes no registry. That is the posture of the four sibling legs. A
  stage tested some other way than `git diff --cached` or `diff-index --cached`, such as a second
  `git status`, reads as unchecked. `TOOL-dSettledStage-1`'s `write_staged_change` uses
  `git diff --cached --quiet`, the form the brief names.
- testing — AC1 to AC8 are scanner runs over fixture repositories, a `<base>` clone and the tree,
  its `--selftest`, a python read of the leg manifest, greps and `git` reads.
- migration — None.
- user docs — `tools/gate-lint/README.md`'s new section, where the four earlier modes are
  documented. No `help/` page covers gate-lint (§3).

## 6. Acceptance criteria

`<p2>` is the product commit and `<p2m>` the manifest re-stamp, each named in the ledger. `<sh>` is
`python tools/gate-lint/sh_hygiene.py` as committed at `<p2>`. `<reg>` is the registry S5 writes,
spelled through a placeholder because the file does not exist before `<p2>`. `<t>` is a fresh
directory under `%TEMP%`, and `<t>/empty.txt` is an empty file, which `resolve_declaration` reads
as an empty declaration. `<base>` is a local `git clone` of gov under `%TEMP%`, checked out at
`12764ec21`. Commands run from the worktree root on node d.

- **AC1** — `<t>/r` is a fixture repository. It holds a tracked `a.sh` with the regen shape: a
  `git status --porcelain` test opening an `if`, then `git add -A`, then `git commit -q -m x`. It
  also holds `b.sh` with `if ! git diff --cached --quiet; then` around the same commit. When
  `<sh> --stage-commits <t>/empty.txt <t>/r` runs, it exits 1. Its one finding names `a.sh` with 1
  `unchecked-stage` site and lists line 3 of `a.sh`. The class lines read 1 unchecked and 1 admitted, and
  `b.sh` appears in no finding.
  Red when: a copy of `<sh>` whose staged-test step is taken out names `b.sh` as well.
- **AC2** — When `<sh> --stage-commits <t>/empty.txt <base> tools/push-main.sh` runs, it exits 1. Its
  finding names `tools/push-main.sh` with 4 sites, listing lines 1065, 1347, 1372 and 1396. This is
  the RED on the lander that aborted landing `12764ec21`.
  Red when: a copy of `<sh>` that reads no `commit-tree` event names 3 sites and omits line 1065.
  figure: 4 sites and their lines PINNED at blob `cd8cf562` of `tools/push-main.sh`.
- **AC3** — When `<sh> --stage-commits <t>/empty.txt . tools/push-main.sh` runs at `<p2>`, it exits 0.
  Its unchecked line reads 0 sites, its admitted line 4 sites and its unpaired line 0.
  Red when: a copy of `<sh>` with the stager follow taken out reads the four commits as unpaired,
  and the same run over `<base>` exits 1, which is AC2.
  fixture: needs `TOOL-dSettledStage-1`'s fix in the tree, order 1, whose four sites call
  `write_staged_change`.
  figure: 4 PINNED from `TOOL-dSettledStage-1` rev-1's S2 and S3; DERIVED at observation.
- **AC4** — When `<sh> --stage-commits <reg> . ':!*.test.sh' ':!memory/'` runs at `<p2>`, it exits 0.
  Its OK line counts 3 registered sites in 3 rows, DERIVED at observation.
  Each row's reason prints, and the unpaired list names `tools/unattended/unattended.sh`.
  The same run with `<t>/empty.txt` exits 1, with 3 sites in 3 files, DERIVED at observation.
  `grep -n 'stage-commit-sites.txt' .memory-tree.conf` prints the `PROJECT_REGISTRY_EXTRA` line.
  Red when: the run with `<reg>` and root `<base>` exits 1, with `tools/push-main.sh` undeclared
  at 4 sites.
  figure: 75 sources, 3 in 3 and 7 in 4 PINNED at `12764ec21` on 2026-11-19; DERIVED at
  observation.
- **AC5** — A python program loads `tools/gate-legs.json`. One row's argv carries `--stage-commits`,
  `stage-commit-sites.txt`, `.`, `:!*.test.sh` and `:!memory/`, with chunk `product`, subject `repo`
  and no guard. Its name is the name of a `[[gate_leg]]` in `tools/gate-lint/kit.toml`, whose argv
  is `["python3", "{kit}/sh_hygiene.py", "--stage-commits"]`. The dossier
  `memory/map/features/gate-lint.md` lists that name under `gate-legs`.
  `tools/gate-lint/README.md` carries a section heading naming `--stage-commits`.
  `tools/govkit/subject-pins.tsv` carries the name with `repo` and `product`.
  Red when: at `12764ec21` no row's argv carries `--stage-commits`.
- **AC6** — When `<sh> --selftest` runs, it exits 0, and its printed assertion count is at least the
  raised `FLOOR_ASSERTIONS`. Every row of §4's fixture table and every `STAGE_BOUNDARY` row runs.
  Red when: a copy with the stager follow taken out reads the checked-stager fixture as unpaired,
  and a copy that matches on unblanked code reads the `echo` fixture as a commit.
- **AC7** — The temp-name mode reads as before. Run
  `<sh> --temp-names memory/project/temp-name-sites.txt . ':!*.test.sh' ':!memory/'`, and the same
  command with `<base>`'s `tools/gate-lint/sh_hygiene.py` from the worktree root. The two outputs are
  identical. `grep -c 'build_blanked\|read_function_spans'` over `<sh>`'s file prints at least 4: two
  definitions and the two calls in `scan_temp_file`.
  Red when: a `build_blanked` that blanks nothing makes the temp selftest's `two prefix assignments`
  row read `B="x y" mv` as two words.
- **AC8** — `git log -1 --format=%B <p2m>` carries `manifest-audit:`. The `last-audit:` line of
  `memory/guides/SESSION-KICKOFF.md` names a commit at which `git show <sha>:tools/gate-legs.json`
  carries `--stage-commits`. `python tools/codebase-map/gen_map.py --check` exits 0 at `<p2m>`.
  `git diff --name-only <p2>~1 <p2> -- memory/builds/dSettledStage/spec/` names no spec but this one.
  The ledger S7 names exists and carries `**Serves:** journal TOOL-dSettledStage-2`.
  Red when: the stamp names a commit before `<p2>`, or `<p2m>` carries no `manifest-audit:`.

## 7. Gates

`shell-hygiene selftest` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `kickoff-manifest ratchet` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `testsuite counts (every bar self-test prints one)` · `kit/dogfood doc parity` · `straggler-guard arms` · `recall floor` · `recall floor arms` · `transition-audit arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures`

The line joins §4's Files touched against the guards in `tools/gate-legs.json`, with the checker's
broad-guard floor applied. The leg manifest owes the two canaries and `measure-legs selftest`, the
subject pins the three govkit legs, the kit descriptor `policy fixtures`, and `.memory-tree.conf`
the four legs it guards. The line adds the unguarded legs the change moves: the shell-hygiene legs,
the manifest, record, naming, map, kit and suite-count legs. The leg S6 adds, `shell hygiene (a stage
committed with no staged-diff test)`, joins this line in a revision once its manifest row exists.

New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC6 · the `--stage-commits` arms over a copy with the staged-test step, the stager follow and the quote blanking each taken out · raise `FLOOR_ASSERTIONS` from 125 to the count printed
New arm: tools/gate-lint/sh_hygiene.py --stage-commits · covers AC2 AC3 · the new leg over a `<base>` clone of `12764ec21`, where the lander's four sites are unchecked · none

The main loop observes each arm red, then green, at the close, and runs the bar once after the
last unit is terminal.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft, from the dSettledStage brief's item 3 and the owner's "go, no
  audit". The brief's scan-or-gotcha rule was decided by a probe of the predicate over the tree at
  `12764ec21`. It read 7 sites in 4 files, PINNED at `12764ec21`, every one a live stage-then-commit.
  The gate is a fifth `sh_hygiene.py` mode with its own leg.
  It registers 3 sites in 3 files after unit 1's fix, DERIVED at observation.
  The temp mode's quote blanker and function-span loop are extracted for the new mode to share.
- rev-2 · 2026-11-19 · the pass-leg fix `2026-11-19-prompt-TOOL-dSettledStage-2-pass-legs-fix`, after
  `864d85d42`. It pins the counts the `pinned-facts` arm read unpinned, `4 files`, `54 files`,
  `3 rows` and `3 files`, on their own lines in §1, §3, §4's probe table, AC4 and this log. It
  rewords AC1's fixture line so `positional` reads no citation in it. No meaning, criterion, figure
  or status moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "check that a git stage left a diff before committing"`
ranked name-stem neighbours only (`git`, `check`, `run_git`, `GIT`), with no staged-diff check. No
existing seam fits that half: the class has no checker anywhere in the tree. `python
tools/codebase-map/reuse_lookup.py "static scan of shell sources that reds a new spelling against a
shrink-only registry"` ranked `scan` and `load_registry`, both name stems. Each miss is recorded as
a miss. The seam this unit extends was found by reading the code and the precedent: the mode family
of `tools/gate-lint/sh_hygiene.py`, whose fourth mode `TOOL-dRedressedBar-24` added. S2 and S3 reuse
`read_shell_sources`, `read_code_lines`, `read_function_bodies`, `FUNCTION_DEF`, `PROBE_WORD`,
`read_registry`, `resolve_declaration` and `check_registry`, and add only the predicate. S1 extracts
`scan_temp_file`'s inline blanker and span loop as their second instance. S6 follows the temp-name
leg's declarations: its manifest row, `[[gate_leg]]`, dossier entries, README section and pin row.
S5 follows `temp-name-sites.txt` and its `PROJECT_REGISTRY_EXTRA` member, and S7 follows
`73b80ed31` and `be022852d`.

The recall probe returned the brief and the build README, which state the class. It also returned
`TOOL-dTieredTribunal-21`, a `git add -A` that staged a fixture's stray file, which is a different
class. `TOOL-dGroundRules-72`'s brief names `git commit -am`, which §4's boundary lists. The records
and the code agree on every citation re-read.

The gotchas these paths select, each answered here. Under `fixture-passes-by-finding-nothing`, AC1
asserts one site and one admitted commit, AC3 asserts 4 admitted commits, and AC4 asserts the
population. Under `a-new-leg-trips-a-growing-set-of-meta-gates`, §7 names the kit descriptor, the
dossier claim, the subject pin, the registry admission and the suite floor. Under
`staged-break-substitutes-a-synthetic-value`, AC2's red reads the lander's own bytes at
`12764ec21`, not a stand-in. Under `heredoc-escape-reaches-the-regex`, the probe for this spec hit
that class once while being patched through a heredoc, and was rewritten as a file.

Recall terms used: `python tools/memory-recall/query.py "how is a commit after git add gated when
staging may leave nothing to commit" --terms "git add commit empty stage diff cached quiet lander
regen sh_hygiene registry class"`

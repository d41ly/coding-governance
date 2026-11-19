# TOOL-dSettledStage-4 — the stage scan reads past a quoted substitution, every git global option and a stager's wrappers, and arm 43 proves its shape

**Status:** CLOSED · rev-1 · 2026-11-19 · node d · Tier-2 · base 12764ec2 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dSettledStage-4-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dSettledStage-4-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dSettledStage-3-promotion-brief.md](../prompts/2026-11-19-prompt-TOOL-dSettledStage-3-promotion-brief.md) | research | TOOL-dSettledStage-3 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing review of this build (`reviews/2026-11-19-review-TOOL-dSettledStage-1-2-closing-diff-round1.md`)
confirmed three MEDIUM defects in the `--stage-commits` scan and two LOW gaps. The build method's
severity rule batches every MEDIUM and LOW item into one unit, and the promotion brief
(`prompts/2026-11-19-prompt-TOOL-dSettledStage-3-promotion-brief.md`, item 2) names this unit for the
review's items 2 to 6. After it, a quoted `$( … )` no longer hides the flags after it, a commit
behind any literal git global option is read, a stager called through a same-file wrapper still
stages, and arm 43 of `tools/push-main.test.sh` reds when its fixture never builds the shape it tests.

## 2. Scope (IN)

- **S1** — The argument end, the review's item 2. `read_stage_events`
  (`tools/gate-lint/sh_hygiene.py#read_stage_events`) ends an event's arguments at the first `;`,
  `&`, `|` or `)` of a walk over its blank from the verb's end. At a `$(` the walk jumps past the
  substitution `read_substitution` reads, and its closing `)`. So the `)` of a quoted `"$(date)"`
  no longer ends the arguments, and the `)` of an enclosing `$( … )` still does. The docstring's
  argument sentence names the walk. Observed by AC1.
- **S2** — The git word, the review's item 3. `STAGE_EVENT` reads every literal global-option
  spelling git accepts before the verb, in §4's table. One `STAGE_BOUNDARY` row names what stays
  unread: a global option behind an expansion or in quotes. The module docstring's fifth-class
  paragraph, `run_stage_scan`'s docstring and the README's `--stage-commits` section state the
  widened git word and the new row. Observed by AC2 and AC5.
- **S3** — The stager closure, the review's item 4. `read_stage_helpers` closes transitively: a
  function whose body holds an `add` event, or a call to a stager, is a stager. Its checked flag is
  the body's own `[staged, tested]` walk, the one `scan_stage_file` runs, ending tested. The call
  reading is extracted as `read_stage_calls(code, helpers)`, its second instance, and
  `scan_stage_file` calls it. The README's and the module docstring's stager sentences say
  "directly or through another stager". Observed by AC3.
- **S4** — The selftest. `run_selftest`'s `stage_cases` gains the 13 rows, PINNED by §4's fixture
  table, and `STAGE_BOUNDARY` gains its one row, which the boundary arm already runs.
  `FLOOR_ASSERTIONS` (`tools/gate-lint/sh_hygiene.py#FLOOR_ASSERTIONS`) rises from 151, PINNED at
  blob `19e87517`, to the count the selftest prints, DERIVED at observation. Its comment gains a
  `RAISED` line naming this unit and the arms counted. Observed by AC4.
- **S5** — The registry re-measured. `memory/project/stage-commit-sites.txt` is re-read against the
  widened scan at the product commit `<p4>`. A row whose count moves is rewritten in that commit,
  and a new key gets a row with its reason. Observed by AC6.
- **S6** — Arm 43's liveness, the review's item 5. Arm 43 of `tools/push-main.test.sh` echoes
  `eol-empty=1` when staging its line-ending shape leaves the stage empty, and `eol-dirty=1` when
  status names `f.txt` right before the fold runs, as arm 42 does. Both join its `w43` want list.
  Observed by AC7.
- **S7** — The record. `python tools/codebase-map/gen_map.py --write` runs before `<p4>`, because
  `read_stage_calls` is a new Python function. The readings go to an acceptance ledger under
  `memory/builds/dSettledStage/build/` carrying `**Serves:** journal TOOL-dSettledStage-4`. The
  build edits no spec but this one's status and date cells. Observed by AC8.
- **S8** — The review's item 6. `TOOL-dSettledStage-2`'s §7 Gates line leaves out its own leg,
  `shell hygiene (a stage committed with no staged-diff test)`, and that spec is CLOSED, so it stays
  frozen. This spec's §7 names the leg, and its revision log records the correction. Observed by AC9.

## 3. Non-goals (OUT)

- `write_staged_change`, its callers and the index-lock arm. They are the review's item 1, the HIGH,
  which the promotion brief gives `TOOL-dSettledStage-3`. So is the new gotcha class it names.
- A scan that reds a `git add` whose exit status a stager never reads. The review offered it as
  item 1's left-shift, and the brief gives item 1 a gotcha class instead.
- `run_regen`, the generators, `.gitattributes`, `.githooks/pre-push` and the bar, per the brief.
- Any edit to the CLOSED specs of units 1 and 2. Item 6 is corrected in this spec alone (S8).
- The `tools/unattended/` registry row, a follow-up for the owner, per the brief.
- A new leg, or a change to any leg's argv. Every fix lands in the scanner the existing leg runs.
- The `harness arms` requirement the review floated for item 5, a shape-liveness marker in every
  arm claiming "red at the base". It would be a new gate, a separate unit (M2). This unit fixes
  arm 43 alone.
- `memory/gotchas/` entries for the review's new class slugs on items 2 to 4. Each is gated by the
  selftest rows S4 adds, which is the left-shift the review names for each.
- A help page. No page under `help/` documents gate-lint, as `TOOL-dSettledStage-2` states in its §3.

### Edges

none

## 4. Design

### Evidence, read at `ce7e513b9` on 2026-11-19

`tools/gate-lint/sh_hygiene.py` is blob `19e87517` at `ce7e513b9` and at `41e57fca5`, the head the
review read. `tools/push-main.test.sh` is blob `a4ace06a` at both. A read-only probe imported the
module and ran `scan_stage_file` over the review's inputs. Each reading below is PINNED at blob
`19e87517` on 2026-11-19, as (unchecked, admitted, unpaired, empty-ok).

| Input | Reads | Should read |
|---|---|---|
| `git add -A`, then `git commit -q -m "$(date)" --allow-empty` | (1, 0, 0, 0) | (0, 0, 0, 1) |
| `git add -A`, then `git diff "$(echo x)" --cached --quiet \|\| git commit -m x` | (1, 0, 0, 0) | (0, 1, 0, 0) |
| `git add -A`, then `git --no-pager commit -q -m x` | (0, 0, 0, 0) | (1, 0, 0, 0) |
| `git add -A`, then `git -p commit -q -m x` | (0, 0, 0, 0) | (1, 0, 0, 0) |
| `git --git-dir=.git add -A`, then `git --git-dir=.git commit -q -m x` | (0, 0, 0, 0) | (1, 0, 0, 0) |
| `s1() { git add -A; }`, `s2() { s1; }`, `s2`, `git commit -q -m x` | (0, 0, 1, 0) | (1, 0, 0, 0) |

The same probe applied the candidate design of S1 to S3 to the leg's population,
`. :!*.test.sh :!memory/`, which holds 75 sources, PINNED at `ce7e513b9`. The readings did not move.
They are 3 unchecked sites in 3 files, 4 admitted, 2 unpaired and 0 empty-ok, PINNED at `ce7e513b9`.
A `git grep` read 6 product lines spelling a git global option, PINNED at `ce7e513b9`, and none of
them names a stage verb. So S5's re-measure is
expected to leave the registry's rows as they are, and the count at `<p4>` is DERIVED at observation.

### S1 — the walk that ends the arguments

`read_stage_events` keeps its blank, `build_blanked(code, keep_substitutions=True)`. On that blank a
quoted `$( … )` is code and the rest of the quoted text is `_`. The walk starts at the verb's end.
At `$(` it reads the substitution with `read_substitution(blank, k)` and moves past it and its `)`.
Otherwise the first `;`, `&`, `|` or `)` is the end, and the end of the line when none appears.

An event inside a substitution still ends at that substitution's `)`. The walk starts inside it,
where its `$(` lies behind the start. So `n=$(git diff --cached --name-only | wc -l)` and
`t=$(git commit-tree "$(git write-tree)" -p "$1" -m m)` read as before. A `$((` arithmetic form is a
balanced substitution to `read_substitution`, so it is skipped the same way. Only
`read_stage_events` searches a `keep_substitutions` blank for a terminator, so the review's
"every scan" left-shift is the two item-2 rows here. `scan_stage_file` reads that blank only to test
that a call's name is code.

### S2 — every literal global option before the verb

The probe ran each form in a fixture repository under `%TEMP%` on 2026-11-19, with git 2.54.0, as
`git <option> status`. The pattern between `git` and the verb becomes any run of these:

| Form | Spelling | How it is read |
|---|---|---|
| config | `-c <word>` | as today |
| directory | `-C <word>` | as today |
| pager | `-p`, `-P` | a bare flag |
| a long option | `--<name>` or `--<name>=<word>` | `_PROBE_FLAG`, the location-probe mode's flag fragment |
| a separate argument | `--git-dir <word>`, `--work-tree <word>`, `--namespace <word>`, `--config-env <word>` | the name, then one `PROBE_WORD` |

`<word>` is `PROBE_WORD` throughout, as the `-c` form reads it today. `--exec-path` is not a
separate-argument form: `git --exec-path /x status` printed the exec path and exited 0, running no
`status`. The review listed it as one, and the probe disagreed, so the table follows the probe. The
form `--exec-path=<path>` is a long option and is read. `-v` and `-h` print and exit without running
the verb, so they are not read, and no commit is missed.

What stays unread is an option git receives from an expansion or a quoted word, such as
`git $GIT_OPTS commit` or `git "--no-pager" commit`. Both read as no event in the probe.
`STAGE_BOUNDARY` gains the row (`a git global option behind an expansion or in quotes`,
`git add -A` then `git $GIT_OPTS commit -q -m x`, `unread`), after the row for a git verb behind a
variable. The boundary arm then requires its label in `run_stage_scan`'s UNREAD paragraph and in the
README section. That arm already exists.

### S3 — the stager closure

`read_stage_calls(code, helpers)` returns `[(column, "call", name)]` for each call on one code half
to a name in `helpers`. A call is the name as a whole word, unblanked on the `keep_substitutions`
blank, not after `$`, `.`, `/` or `-`, and not before `=`, `+=` or `[`. The name on its own
`FUNCTION_DEF` definition line is not a call. That is the reading `scan_stage_file` does inline
today, moved unchanged, and it returns `[]` for an empty `helpers`.

`read_stage_helpers` starts from an empty mapping and re-walks every body from
`read_function_bodies` until the mapping stops changing. It stops after one pass more than there are
functions in any case, so a call cycle cannot loop it. In each pass, each body's events and calls to
the stagers known so far are walked in order, line by line and column by column, with the state
`scan_stage_file` keeps. An `add` sets `[True, False]`, a call sets `[True, checked]` for the callee,
and a test sets tested to staged. A body that ends staged is a stager, checked when it ends tested.
With no call in a body this is today's rule, a test after the last `add`. The stager set only grows
from pass to pass, and a cycle with no `add` in it stages nothing.

### The selftest's new fixture rows

Each row is a `stage_cases` entry graded on all four counts. Every row the evidence table above
also lists reads a different tuple at blob `19e87517`.

| Label | Fixture | Expected |
|---|---|---|
| a quoted substitution before `--allow-empty` | `git add -A`, then `git commit -q -m "$(date)" --allow-empty` | (0, 0, 0, 1) |
| a quoted substitution before `--cached` | `git add -A`, then `git diff "$(echo x)" --cached --quiet \|\| git commit -m x` | (0, 1, 0, 0) |
| `-p` | `git add -A`, then `git -p commit -q -m x` | (1, 0, 0, 0) |
| `-P` | `git add -A`, then `git -P commit -q -m x` | (1, 0, 0, 0) |
| `--no-pager` | `git add -A`, then `git --no-pager commit -q -m x` | (1, 0, 0, 0) |
| `--git-dir=` | `git --git-dir=.git add -A`, then `git --git-dir=.git commit -q -m x` | (1, 0, 0, 0) |
| `--git-dir` apart | `git add -A`, then `git --git-dir .git commit -q -m x` | (1, 0, 0, 0) |
| `--work-tree` apart | `git add -A`, then `git --work-tree . commit -q -m x` | (1, 0, 0, 0) |
| `--namespace` apart | `git add -A`, then `git --namespace n commit -q -m x` | (1, 0, 0, 0) |
| `--config-env` apart | `git add -A`, then `git --config-env core.pager=HOME commit -q -m x` | (1, 0, 0, 0) |
| a two-hop unchecked stager | `s1() { git add -A; }`, `s2() { s1; }`, `s2`, `git commit -q -m x` | (1, 0, 0, 0) |
| a two-hop checked stager | `s1` with `git add -A` and `! git diff --cached --quiet` on its own lines, `s2() {` `s1` `}` on three lines, then `if s2; then git commit -q -m x; fi` | (0, 1, 0, 0) |
| a call cycle with no stage | `a() { b; }`, `b() { a; }`, `a`, `git commit -q -m x` | (0, 0, 1, 0) |

The probe ran every row through the candidate design on 2026-11-19, and each read as the table
says. It ran the new boundary row too, which read no commit. So the selftest gains 14 executed
assertions, PINNED by this table, and the floor moves from 151 to at least 165, DERIVED from the
printed count at observation.

### S6 — arm 43's two markers

Arm 43 builds its shape from three steps: `rm f.txt`, `git checkout -q -- f.txt` under
`GIT_CONFIG_VALUE_0=true`, and the LF rewrite `printf 'one\ntwo\n' > f.txt`. After those steps and
before the first `write_merge_fold` call, the arm gains two checks. First,
`git add -A; git diff --cached --quiet && echo eol-empty=1; git reset -q`. That stage refreshes the
index, so the arm then repeats the three steps to rebuild the dirty shape. Second, right before the
fold, `[ -n "$(git status --porcelain -- f.txt)" ] && echo eol-dirty=1`. The `w43` list becomes
`eol-dirty=1 eol-empty=1 eol-rc=0 eol-head=same real-rc=0 real-moved=1`. Where the CRLF checkout
does not happen, status is clean before the fold, no `eol-dirty=1` prints, and the arm reds instead
of passing on both the base and the built lander. The arm's comment names the two markers.

### Order

**Order 4**, after `TOOL-dSettledStage-3`'s order 3. Both units write `tools/push-main.test.sh`,
the promotion brief's stated reason, so this unit is built on the tree unit 3 leaves. No criterion
here rests on unit 3's lander change. S5's re-measure reads whatever lander that unit lands, and
the stage leg's own pass at unit 3 is what holds the lander's sites admitted. So §3 declares no edge, and
order is not one.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `read_stage_calls` | a function in `sh_hygiene.py` | `py.function`, `read` |
| `a git global option behind an expansion or in quotes` | a `STAGE_BOUNDARY` label | none |
| `eol-dirty=1`, `eol-empty=1` in arm 43 | suite markers, arm 42's spelling | none |

`python tools/lexicon/lexicon.py --suggest read_stage_calls --as py.function` answered OK on
2026-11-19. `git grep read_stage_calls` outside `memory/builds/` found none at `ce7e513b9`.

### Files touched (estimate)

- `tools/gate-lint/sh_hygiene.py`
- `tools/gate-lint/README.md`
- `tools/push-main.test.sh`
- `memory/project/stage-commit-sites.txt`, only where S5's re-measure moves a row
- `memory/map/generated/`
- `memory/builds/dSettledStage/build/`

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| End the arguments on `build_blanked(code)` with no kept substitutions | an unquoted `$(date)` inside the arguments still ends them at its `)`, so the class stays open for the unquoted spelling | Rejected; S1 walks past every `$( … )` |
| Widen the prefix to `--<opt>[=<word>]` alone, the finder's proposal | the probe's `-p`, `-P` and `--git-dir .git` rows still read no event | Rejected; the review's skeptic judged it INSTANCE-ONLY |
| A `STAGE_BOUNDARY` row for every global option, with no widening | every literal spelling of the class would pass green with a stated reason, though a regex reads it exactly | Rejected; only the expansion form is a row |
| Treat any `--<opt> <word>` as an option taking an argument | `git --no-pager commit` would spend `commit` as the argument and need backtracking to recover | Rejected; the separate-argument names are listed |
| Keep one hop and add a boundary row for a same-file wrapper | the two-hop fixture is a shape the lander's own helper is one refactor away from, and a fixed point costs one loop | Rejected; S3 closes the set |
| A second copy of the call regex inside `read_stage_helpers` | the charter's [reuse] rule: the second instance extracts the factory | Rejected; S3 extracts `read_stage_calls` |

## 5. Production-readiness checklist

- security — No write path, surface or egress. The scanner reads tracked files through `git ls-files`
  and writes nothing. The suite edit writes only inside its own temp directory.
- perf / scale — The stager closure re-walks function bodies until it settles. It takes one pass more
  than the per-file stager depth, at most one more than the function count, over the same 75 sources,
  PINNED at `ce7e513b9`. The leg's ceiling in `tools/gate-legs.json` does not move.
- error / empty / loading states — No new refusal path. An empty population and a failed
  `git ls-files` still exit 2 through `run_stage_scan`.
- observability — The new boundary row prints nowhere but the docstring and README, as every row
  does. Arm 43's failure message carries `$out43`, which now holds both markers.
- risks — The widened git word reads more events, so a product site behind a newly read option
  would red. The probe read none at `ce7e513b9`, and S5 re-measures at `<p4>`. A cycle through a
  stager is read by the pass bound, not a proof of convergence.
- testing — AC1 to AC9 are classifier reads over fixtures, a base copy of the scanner, the
  `--selftest` flag, a run over the tree, an arm 43 extract and greps.
- migration — None. The registry keeps its grammar.
- user docs — `tools/gate-lint/README.md`'s `--stage-commits` section (S2, S3). No `help/` page
  covers gate-lint (§3).

## 6. Acceptance criteria

`<p4>` is the product commit, named in the ledger. Commands run from the worktree root on node d.
`<t>` is a fresh directory under `%TEMP%`. `<t>/base/sh_hygiene.py` is
`git show 41e57fca5:tools/gate-lint/sh_hygiene.py`, the scanner the review read. `<cls> <dir> <f>`
is `python -c` over a program that puts `<dir>` first on `sys.path`, imports `sh_hygiene`, reads
`<f>` as UTF-8 and prints `tuple(len(found[k]) for k, _m, _l in STAGE_CLASSES)` for
`found = scan_stage_file(text)`. `<dir>` is `tools/gate-lint` for the built scanner and `<t>/base`
for the base. Each fixture file under `<t>` holds the matching row of §4's fixture table, one command
per line.

- **AC1** — When `<cls> tools/gate-lint` runs over the two quoted-substitution fixtures, it prints
  `(0, 0, 0, 1)` for the `--allow-empty` one and `(0, 1, 0, 0)` for the `--cached` one.
  Red when: `<cls> <t>/base` prints `(1, 0, 0, 0)` for both, PINNED at blob `19e87517`.
- **AC2** — When `<cls> tools/gate-lint` runs over the eight option fixtures, each prints
  `(1, 0, 0, 0)`. The fixture `git add -A` then `git $GIT_OPTS commit -q -m x` prints
  `(0, 0, 0, 0)`.
  Red when: `<cls> <t>/base` prints `(0, 0, 0, 0)` for each option fixture, PINNED at blob `19e87517`
  for `-p`, `--no-pager` and `--git-dir=`.
- **AC3** — When `<cls> tools/gate-lint` runs over the three stager fixtures, it prints
  `(1, 0, 0, 0)` for the two-hop unchecked one, `(0, 1, 0, 0)` for the two-hop checked one and
  `(0, 0, 1, 0)` for the call cycle, and each run returns within seconds.
  Red when: `<cls> <t>/base` prints `(0, 0, 1, 0)` for the two-hop unchecked fixture, PINNED at
  blob `19e87517`.
- **AC4** — When `python tools/gate-lint/sh_hygiene.py --selftest` runs at `<p4>`, it exits 0, and the
  count in its `PASS` line equals the `FLOOR_ASSERTIONS` value at `<p4>`. That value is at least 165,
  DERIVED from §4's table.
  `grep -n 'TOOL-dSettledStage-4' tools/gate-lint/sh_hygiene.py` prints the floor's `RAISED` line.
  Red when: a copy whose `read_stage_helpers` makes one pass reads the two-hop unchecked row as
  `(0, 0, 1, 0)`, and the selftest prints `RED`.
  figure: 151 PINNED at blob `19e87517`; 14 new assertions PINNED by §4's table; the floor DERIVED
  at observation.
- **AC5** — A python program imports the built `sh_hygiene` and reads the README section that opens
  at the heading naming `--stage-commits`. `run_stage_scan.__doc__` and that section each carry the
  label `a git global option behind an expansion or in quotes`. The module docstring carries
  `--git-dir`, and `STAGE_BOUNDARY` holds the label with the class `unread`.
  Red when: at `41e57fca5` the label is in none of the three.
- **AC6** — When `python tools/gate-lint/sh_hygiene.py --stage-commits memory/project/stage-commit-sites.txt . ':!*.test.sh' ':!memory/'`
  runs at `<p4>`, it exits 0, and its OK line's site and row counts equal the registry's rows.
  The same run with `<t>/empty.txt`, an empty file, exits 1 and names each registry path.
  Red when: a registry row's count is lowered by one, and the run exits 1 naming that path.
  figure: 3 sites in 3 rows PINNED at `ce7e513b9` by the candidate probe; DERIVED at observation.
- **AC7** — `<a43>` is a script under `<t>`. It opens with the suite's two fixture-identity `export`
  lines, the ones setting `GIT_AUTHOR_NAME` and `GIT_CONFIG_COUNT`, then `lander=` the worktree's
  `tools/push-main.sh` and `tmp=<t>/a`. Then come the lines
  `sed -n '/^out43=\$(/,/^done$/p' tools/push-main.test.sh` prints, from `<p4>`, and last
  `echo "l43=$_l43"`. When `bash <a43>` runs, it prints `l43=0`, and `$out43` holds `eol-dirty=1`
  and `eol-empty=1`. With the arm's `GIT_CONFIG_VALUE_0=true` rewritten to `false` in the copy, it
  prints `l43=1`.
  Red when: the same extract from `41e57fca5` with the same rewrite prints `l43=0`, the vacuous pass
  the review reported.
  fixture: needs the tree `TOOL-dSettledStage-3` leaves, order 3, which also writes this suite.
- **AC8** — `python tools/codebase-map/gen_map.py --check` exits 0 at `<p4>`.
  `git diff --name-only <p4>~1 <p4> -- memory/builds/dSettledStage/spec/` names no spec but this one.
  The ledger S7 names exists and carries `**Serves:** journal TOOL-dSettledStage-4`.
  Red when: `<p4>` mints `read_stage_calls` with no `gen_map.py --write`, and the check exits 1.
- **AC9** — `grep -c 'shell hygiene (a stage committed with no staged-diff test)'` over this spec's
  §7 leg line prints 1, and §9's rev-1 entry names the review's item 6.
  Red when: the same grep over `TOOL-dSettledStage-2`'s §7 leg line prints 0, the omission item 6
  reported.

## 7. Gates

`shell-hygiene selftest` · `shell hygiene (a stage committed with no staged-diff test)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `push-main self-test` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `writing practice (records and units)` · `positional (the citation check alone)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms`

The line names the shell-hygiene legs that run the changed scanner, the stage leg among them. That
leg is the one `TOOL-dSettledStage-2`'s §7 omitted, the review's item 6. The suite leg runs arm 43,
and `harness arms` grades its want list. The record, citation, map, naming, encoding and
suite-count legs cover the records and the new function. The two recall-floor legs guard the
registry, which S5 rewrites only where its re-measure moves a row.

New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC1 AC2 AC3 AC4 · the 13 new `stage_cases` rows and the new boundary row over a copy with the walk, the widened git word and the closure each taken out · raise `FLOOR_ASSERTIONS` from 151 to the count printed
New arm: tools/push-main.test.sh · covers AC7 · arm 43 with `GIT_CONFIG_VALUE_0=false` in place of `true`, so no CRLF checkout builds the shape · none

The main loop observes each arm red, then green, at the close, and runs the bar once after the
last unit is terminal.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft, from the promotion brief's item 2 and the owner's "go, no
  audit". It disposes the round-1 closing review's items 2 to 6, findings 2, 4, 6, 8, 9 and 10.
  The review's item 6 is corrected here: `TOOL-dSettledStage-2` is CLOSED and frozen, its §7 Gates
  line leaves out `shell hygiene (a stage committed with no staged-diff test)`, and this spec's §7
  names that leg. A probe at `ce7e513b9` read the review's inputs as the review states, and read
  the candidate design leaving the tree's counts unmoved. It read `--exec-path` as no
  separate-argument form, against the review's list.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "close a set of shell functions transitively over calls until it stops changing"`
ranked name-stem neighbours only (`changed`, `set_env_aside`, `write_change`). No existing seam
fits the closure as a general helper, so it is recorded as a miss.
`python tools/codebase-map/reuse_lookup.py "match git global options before the subcommand verb"`
ranked `git`, `run_git` and `GIT`, all name stems, with no option reader. Also a miss.
The seams this unit extends were found by reading the code. The first is the stage mode of
`tools/gate-lint/sh_hygiene.py`, which `TOOL-dSettledStage-2` added: S1 extends `read_stage_events`
with `read_substitution`, S2 extends `STAGE_EVENT` with `_PROBE_FLAG` and `PROBE_WORD` and adds a
`STAGE_BOUNDARY` row, and S3 extends `read_stage_helpers` and extracts `read_stage_calls` from
`scan_stage_file`. The second is arm 42's liveness markers, which S6 copies into arm 43.

The recall probe returned the review and the promotion brief, which state the defects, and
`TOOL-dSettledStage-2`'s spec and ledger, which state the mode. It also returned
`TOOL-aGraftedHelix-36`, whose checker lists "a global option other than `-c`" as a boundary, the
same class in another scan. The records and the code agree on every citation re-read, except the
review's `--exec-path` separate form, which §4 corrects from the probe.

The gotchas these paths select, each answered here. Under `fixture-passes-by-finding-nothing`, S6
is that class's fix for arm 43, and every new `stage_cases` row is graded on all four counts. Under
`staged-break-substitutes-a-synthetic-value`, AC1 to AC3 read the base scanner's own bytes at
`41e57fca5`, not a stand-in. Under `heredoc-escape-reaches-the-regex`, the probes for this spec were
written as files. Under `two-answers-to-one-question`, the new boundary label is checked in the
docstring and the README by the existing boundary arm.

Recall terms used: `python tools/memory-recall/query.py "how does the stage-commit scan read git
global options, quoted substitutions and stagers called through wrappers" --terms "stage-commits
sh_hygiene STAGE_EVENT STAGE_BOUNDARY read_stage_helpers read_substitution keep_substitutions global
option wrapper transitive"`

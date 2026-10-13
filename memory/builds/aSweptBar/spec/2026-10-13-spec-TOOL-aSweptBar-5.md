# TOOL-aSweptBar-5 — fork idioms re-grown past the spawn-idiom registry, converted

**Status:** INPROGRESS · rev-1 · 2026-10-13 · node a · Tier-1 · base 53b25884 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aSweptBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-aSweptBar-1-brief.md) | research | TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-6 |

<!-- /gen:spec-records -->

## 1. Goal

The `shell hygiene (a fork spent on builtin work)` leg reds at `53b25884` on 24 findings, 19 of them
outside `tools/roles/` (PINNED, the bar's leg log of 2026-10-13). All but one are sites a landing
that merged without a bar added past `memory/project/spawn-idiom-sites.txt`; the last is a row left
above a count that fell. This unit converts every re-grown site to its no-fork form and sets the
registry to the scan, so the leg reds only on the roles kit's findings, which aOrientedCast owns.

## 2. Scope (IN)

- **S1** — `getval` in `skills/session-kickoff/manifest-check.sh` assigns its answer to a variable
  its caller names, and its seven callers pass that name instead of capturing it by substitution.
  Observed by AC1 and AC2.
- **S2** — every counted turnstile beacon read in `tools/run-gates/run-gates.sh` reads by the
  builtin, save the one inside `render_same_holder` (§4 says why). Observed by AC3 and AC5.
- **S3** — in each suite whose (path, class) measures above its row, the excess converts through the
  §4 forms table; in `tools/hooks/format-guard.test.sh`, which carries no row, every site converts.
  Observed by AC4 and AC5.
- **S4** — every row of a touched (path, class) equals the scan, the `var-pipe` row of
  `tools/memory-tree/check-memory-hygiene.sh` lowered to its measured count, and no row rises or is
  added beyond the one escape §4 names. Observed by AC5 and AC6.

## 3. Non-goals (OUT)

- Nothing under `tools/roles/`, `.claude/agents/`, `.claude/skills/build/` or `tools/playbook/`,
  and no registry row for a `tools/roles/` path: aOrientedCast lands those findings at its close.
- No registry row rises to absorb a site a conversion can fix (the brief's non-goal,
  `memory/builds/aSweptBar/prompts/2026-10-13-prompt-TOOL-aSweptBar-1-brief.md:130`).
- No suite drain past the excess. A row that already equals its scan stays, for the follow-up its
  reason names.
- No change to `tools/gate-lint/sh_hygiene.py`, its classes or its remedies. The left-shift that
  would catch regrowth at the unit causing it is the open ask TOOL-aSparedSpawn-20.
- No row of `memory/project/fork-ceilings.txt`. No kit version mint: `kit epoch` reads a moved kit
  as owed at the lander.
- No new function and no renamed one, so the codebase map's symbol tier and the lexicon read
  nothing new.

### Edges

- **consumes-from** `TOOL-aSweptBar-4` — the `memory/project/spawn-idiom-sites.txt` rows for the
  remote ladder that unit inlines into `tools/run-gates/run-held-wsl.sh`; without them AC5 reds on a
  product file this unit does not touch.
- **hands-off** `TOOL-aSweptBar-6` — the `manifest-check` row of `memory/project/fork-ceilings.txt`
  is lowered over the tree this unit leaves; the `getval` conversion takes that entrypoint's fork
  count below its 53b25884 reading.

## 4. Design

The leg's two rules decide every site. A count may fall and may not rise, and a (path, class) with
no row is converted or declared (`check_registry` and the undeclared text,
`tools/gate-lint/sh_hygiene.py:444` and `:928`). The brief's non-goal takes the declaring half
away, save where the registry header admits a callee that keeps its substitution
(`memory/project/spawn-idiom-sites.txt:15`). So this unit converts, and the registry only falls.

### The working set is derived at the unit's start

Units 1 to 4 edit several of these files first, so the builder runs the AC5 command before any edit
and takes every finding outside `tools/roles/`. At `53b25884` that set was this (PINNED, measured
2026-10-13 by the full bar, leg log under `.git/worktrees/bar-53b2/gate-logs/`):

| path | class | row | scan |
|---|---|---|---|
| `.githooks/pre-push.test.sh` | `cat-file` | 17 | 19 |
| `skills/session-kickoff/manifest-check.sh` | `pure-fn-subst` | 2 | 9 |
| `skills/session-kickoff/manifest-check.test.sh` | `printf-subst` | 10 | 11 |
| `skills/session-kickoff/manifest-check.test.sh` | `pure-fn-subst` | 20 | 21 |
| `tools/check-wiring.test.sh` | `var-pipe` | 162 | 183 |
| `tools/hooks/format-guard.test.sh` | `cat-file` | none | 3 |
| `tools/hooks/format-guard.test.sh` | `path-subst` | none | 3 |
| `tools/hooks/format-guard.test.sh` | `printf-subst` | none | 1 |
| `tools/hooks/scratch-guard.test.sh` | `path-subst` | 5 | 6 |
| `tools/memory-tree/check-memory-hygiene.sh` | `var-pipe` | 26 | 25 |
| `tools/run-gates/run-gates.runlog.test.sh` | `cat-file` | 5 | 6 |
| `tools/run-gates/run-gates.sh` | `cat-file` | 23 | 38 |
| `tools/run-gates/run-gates.test.sh` | `var-pipe` | 141 | 145 |
| `tools/run-gates/run-gates.turnstile.test.sh` | `cat-file` | 15 | 29 |
| `tools/run-gates/run-gates.turnstile.test.sh` | `pure-fn-subst` | 20 | 21 |
| `tools/run-gates/run-gates.turnstile.test.sh` | `var-pipe` | 36 | 38 |
| `tools/workflows/unattended-build.test.sh` | `printf-subst` | 66 | 73 |
| `tools/workflows/unattended-build.test.sh` | `pure-fn-subst` | 28 | 30 |
| `tools/workflows/unattended-build.test.sh` | `var-pipe` | 62 | 78 |

### Product sources

**`getval`** (`skills/session-kickoff/manifest-check.sh:361`). KICK-aTrimmedHook-1 rewrote its
body from `sed | head | sed` to a builtin loop, which made it pure, so its seven existing callers
(`:515`, `:1249` twice, `:1354` three times, `:1355`) became counted sites: the whole excess.
`getval` takes the target variable's name as a second argument and assigns with `printf -v`, the
shape of `read_phase_into` (`tools/unattended/unattended.sh:13856`). It assigns the empty string
when no line matches, because `LBC` (`:1355`) has no initialiser and would otherwise keep an
inherited value. Its locals `_gl` and `_gre` are names no caller passes, since a `printf -v` into a
name the callee also declares writes the callee's copy. It stays above the first
`BLOCK=$(read_block …)` (`:515`): the loop leg follows the latest assignment textually above a loop,
and below one it would grade the here-string in `getval` as substitution-fed.

**The turnstile beacon reads** (`tools/run-gates/run-gates.sh`). The excess of 15 is the aPairedSlots
landing's slot and docs beacons. Every counted `$(cat "<dir>/<nonce|pid|heartbeat|ttl|run|repo>"
2>/dev/null)` reads by the builtin form `ts_tick_start` already uses on the nonce file (`:1683`):
`v=""; { IFS= read -r v < "<file>"; } 2>/dev/null`. Each beacon file is one line written by
`printf '%s'` (`:1859`-`:1864`, `:1940`-`:1947`), so `read` assigns its bytes, and a missing file
leaves the empty value the substitution gave. No converted site reads the exit status, which differs:
`read` returns 1 on a line with no newline. A re-read inside a `[ … = "$hn" ]` test reads into a
local first, and a function gains the locals it reads into. `render_same_holder` (`:1603`) keeps its
reads: converting them makes its body pure, and its three callers (`:1847`, `:2057`, `:2065`) would
become counted `pure-fn-subst` sites. One counted beacon read remains, so the `cat-file` row falls
to 13 on the `53b25884` bytes (PINNED); the builder sets it to the scan.

**`tools/memory-tree/check-memory-hygiene.sh`** measures 25 `var-pipe` sites against a row of 26.
The row lowers and no code moves.

### The suites, and the forms table

Each excess converts through one row of the table below. The builder picks which sites in a
(path, class) convert, because the registry reads the count, and takes rows the table holds. A site
no row covers stays, `grep -c` and `wc -l` over a multi-line value among them: a line count has no
single builtin test, and a `while read` over the value is a loop the loop leg grades.

| class | forking spelling | no-fork form | exact only when |
|---|---|---|---|
| `cat-file` | `$(cat "$f")` | `$(<"$f")` | always; both strip trailing newlines |
| `cat-file` | `$(cat "$f" 2>/dev/null)` | `v=""; { IFS= read -r v < "$f"; } 2>/dev/null` | `$f` holds one line and the site reads no exit status |
| `cat-file` | `v=$(cat "$f" 2>/dev/null)` | `{ v=$(<"$f"); } 2>/dev/null` | the command is that assignment alone |
| `printf-subst` | `$(printf 'LIT')` | `$'LIT'` | LIT holds no `%` and no escape but `\n`, `\t`, `\\` or octal |
| `printf-subst` | `v=$(printf FMT ARGS)` | `printf -v v FMT ARGS` | the output cannot end in a newline |
| `path-subst` | `$(basename "$p")` | `${p##*/}` | `$p` carries no trailing `/` |
| `path-subst` | `$(dirname "$p")` | `${p%/*}`, or `.` when `$p` holds no `/` | `$p` carries no trailing `/` and is not `/x` |
| `var-pipe` | `… "$v" \| grep -q 'LIT'` | `[[ $v == *'LIT'* ]]` | the flags are `-q` and at most `-F`; LIT holds no regex metacharacter unless `-F` |
| `var-pipe` | `… "$v" \| grep -q '^LIT'` | `[[ $'\n'$v == *$'\n''LIT'* ]]` | the only flag is `-q`; LIT holds no regex metacharacter |
| `var-pipe` | `… "$v" \| sed 's#A#B#'` | `${v/'A'/'B'}` | `$v` is one line; A holds no regex metacharacter, B no `&` or `\` |
| `pure-fn-subst` | `x=$(f …)` | `f` sets a variable, the caller reads it | every call of `f` in the file converts together |

In the `var-pipe` rows, `…` is the `printf '%s'`, `printf '%s\n'` or `echo` of the one expansion
the class admits, and `#` stands for any `sed` delimiter. A `pure-fn-subst` callee converts at every
call in its file, so one callee is never spelled two ways. The suites already carry the shape: `rec` and `review_out`
(`tools/workflows/unattended-build.test.sh:262`, `:265`) set a global beside printing, and `beacon`
(`tools/run-gates/run-gates.turnstile.test.sh:223`) prints a constant path. A converted predicate
keeps its negation and its place in the arm, so no `ok`/`nope` count and no assertion floor moves.

When a (path, class) cannot reach its row through the table, the builder stops and returns that
(path, class) to the main loop. The row does not rise.

### The registry

After the conversions every row of a touched (path, class) equals the scan. A `pure-fn-subst` row's
callee list names the callees it still carries, with their counts. No row rises and none is added,
save one escape: a `pure-fn-subst` callee that keeps its substitution for a reason the header names,
a side effect the caller's shell must not take or a gate that reads the spelling, carried on a row
naming the callee and that reason. The rows TOOL-aSweptBar-4 adds for `tools/run-gates/run-held-wsl.sh`
are that unit's; this unit grades them through AC5 and writes none of them.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `tools/run-gates/run-gates.sh`
- `memory/project/spawn-idiom-sites.txt`
- `.githooks/pre-push.test.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `tools/check-wiring.test.sh`
- `tools/hooks/format-guard.test.sh`
- `tools/hooks/scratch-guard.test.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/workflows/unattended-build.test.sh`

### Alternatives rejected

- Declaring the arrived suite sites with an "arrived with" reason, as the TOOL-aSparedSpawn-32
  reconcile did at `51beae61f`. The brief's non-goal refuses a raise a conversion can fix, and the
  scanner calls the registry shrink-only (`tools/gate-lint/sh_hygiene.py:16`).
- Converting only the 15-site excess in `tools/run-gates/run-gates.sh`. The turnstile would read one
  file kind two ways, and AC3 would have no single spelling to count.
- Converting `render_same_holder` to assign into a variable. It moves the `pure-fn-subst` row and
  three callers to save a fork on a line printed only while a bar waits.
- Following TOOL-aSparedSpawn-16 rev-3, which raised a `var-pipe` row because no builtin test reads
  a match over multi-line output. The anchored-literal row of the table reads one; the claim holds
  for counts only, which is why `grep -c` sites stay.
- Committing the AC4 probe under `memory/builds/aSweptBar/build/`. The aSparedSpawn instruments
  committed there are what TOOL-aSweptBar-6 now repairs; the acceptance ledger records the probe's
  output instead.

## 5. Acceptance criteria

- **AC1** — When `grep -c '\$(getval' skills/session-kickoff/manifest-check.sh` runs, it prints
  `0`. Red when: any caller still captures `getval` by substitution.
  figure: 4 lines holding seven calls at `53b25884`, PINNED; the grep counts lines.
- **AC2** — When `bash "$REPO/skills/session-kickoff/manifest-check.sh" memory/guides/SESSION-KICKOFF.md`
  runs in a fixture repository, `$REPO` naming this worktree, with the manifest's `last-audit:` value
  padded to `  not-a-stamp  `, it prints `last-audit value malformed ('not-a-stamp')`. Run again with
  the `last-body-change:` line deleted and `LBC=f5a63b77` exported, it prints
  `lacks a last-body-change value`. Red when: the value keeps its padding or reads empty, or the
  exported `LBC` survives an absent key.
  fixture: none in the tree; the setup column of the `manifest-check` row of
  `memory/project/fork-ceilings.txt` builds it, under a short `%TEMP%` path.
- **AC3** — When
  `grep -oE '\$\(cat "\$[A-Za-z_]+/(nonce|pid|heartbeat|ttl|run|repo)" 2>/dev/null\)' tools/run-gates/run-gates.sh`
  runs, it prints exactly one match, the `repo` read inside `render_same_holder`. Red when: a
  turnstile beacon read outside `render_same_holder` still forks.
  figure: 26 matches at `53b25884`, PINNED.
- **AC4** — When the forms probe runs each row of the §4 table, forking spelling against no-fork
  form, over a match, a non-match and a specimen at the boundary its `exact only when` cell names,
  every row reports the same output, and the same exit status wherever that cell does not exempt
  it. The staged wrong form, `${p%/*}` alone on the slash-free `c`, reports a difference. Red when:
  a row's two spellings disagree on a specimen, or the staged wrong form reports none.
  fixture: the probe lives in the session scratchpad and its output goes to the unit's acceptance
  ledger; nothing is committed.
- **AC5** — When
  `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/' ':!tools/roles/'`
  runs, every line under its `finding(s)` header names a path under `tools/roles/`, or it prints its
  `OK` line. Red when: a (path, class) outside `tools/roles/` measures other than its row, or has
  no row.
  figure: 19 finding lines outside `tools/roles/` at `53b25884`, PINNED from the bar's leg log; the
  checker derives every count at observation time.
- **AC6** — When `git diff -U0 <pass>~1 <pass> -- memory/project/spawn-idiom-sites.txt` is read at
  this unit's pass commit, no `+` row carries a count above the `-` row of its (path, class), and no
  `+` row opens a (path, class) the `-` side lacks, save a `pure-fn-subst` row naming a callee that
  keeps its substitution for a reason the registry header admits. Red when: a row rises, or a row
  appears for a site the forms table converts.

## 6. Gates

`shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `pre-push self-test` · `check-wiring self-test` · `run-gates canary` · `run-gates turnstile` · `run-gates run-log line`

The main loop runs these at the close; the first is this unit's own leg, and the suites on the line
are the ones whose predicates this unit rewrites. The `spawn budget (forks per hot entrypoint)` leg
is red at `53b25884` on three stale rows and stays red until TOOL-aSweptBar-6 lowers them over this
tree, so it is not on the line. This unit adds and moves no suite arm and declares none.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft, from item 5 of the build brief.

## 9. Reuse audit

The seams are the house no-fork forms already in the tree. The builtin beacon read is in
`ts_tick_start` (`tools/run-gates/run-gates.sh:1683`), the `printf -v` reader is `read_phase_into`
(`tools/unattended/unattended.sh:13856`), and the global-setting fixtures are `rec` and `review_out`
(`tools/workflows/unattended-build.test.sh:262`). The registry `memory/project/spawn-idiom-sites.txt`
is extended by lowering rows under its own grammar. `tools/codebase-map/reuse_lookup.py` with the
phrase "read a one-line file into a variable without forking a subshell" ranked only Python and
JavaScript readers (`read`, `read_text`, `readConfKey`): its symbol tier indexes functions, and
these forms are inline idioms, so no existing seam fits from the map and the seams above are cited
from source. The recall hit TOOL-aSparedSpawn-16 S2 says no builtin test reads a match over
multi-line output; the code disagrees for an anchored literal and agrees for a count (§4).

Recall terms used: `python tools/memory-recall/query.py "how were fork idioms converted to no-fork builtin forms and registry counts lowered" --terms "spawn-idiom registry fork no-fork builtin printf -v cat-file pure-fn-subst var-pipe sh_hygiene shrink-only"`

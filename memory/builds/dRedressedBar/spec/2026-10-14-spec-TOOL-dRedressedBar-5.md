# TOOL-dRedressedBar-5 — fork idioms past the spawn-idiom registry, converted to their no-fork forms

**Status:** CLOSED · rev-5 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md](../build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |
| [2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 |
| [2026-10-14-prompt-TOOL-dRedressedBar-5-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-5-2-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-5-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-5-3-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-5-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-5-4-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-5-5-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-5-5-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-5-6-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-5-6-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-5-7-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-5-7-spec-writer.md) | journal | — |
| [2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 |

<!-- /gen:spec-records -->

## 1. Goal

The `shell hygiene (a fork spent on builtin work)` leg reds at `ebce889c` on ten findings (PINNED,
the leg log of the 2026-10-13 profiled bar). Four files carry sites with no row in
`memory/project/spawn-idiom-sites.txt`, and `tools/workflows/unattended-build.test.sh` measures
above two of its rows. Every one arrived with a landing that merged without a bar. This unit converts
each counted excess to the no-fork form the leg names, so the leg reads green with no row added and
none raised.

## 2. Scope (IN)

- **S1** — The three `path-subst` sites and three `var-pipe` sites of
  `tools/branch-reconcile/adopt-branch-reconcile.sh` convert through the §4 forms table, each on
  its own line. Observed by AC1, AC2, AC5 and AC6.
- **S2** — The three `path-subst` sites and one `var-pipe` site of `tools/roles/adopt-roles.sh`
  convert the same way, each on its own line. Observed by AC1, AC2, AC5 and AC7.
- **S3** — The one `date-fmt`, two `path-subst` and twelve `var-pipe` sites of
  `tools/roles/adopt-roles.test.sh` convert, and each converted assertion keeps its negation and its
  place in its arm. Observed by AC1, AC2 and AC4.
- **S4** — The one `path-subst` site of `tools/hooks/format-guard.test.sh` converts.
  Observed by AC1.
- **S5** — In `tools/workflows/unattended-build.test.sh`, exactly the excess over each row
  converts: five `printf-subst` sites and eight `var-pipe` sites at `ebce889c`. Observed by AC2, AC3
  and AC4.
- **S6** — `memory/project/spawn-idiom-sites.txt` gains no row and no row rises.
  Observed by AC8.
- **S7** — Row 178 of `memory/project/unarmed-branches.txt`, the pin of the delegated refusal site
  at `tools/branch-reconcile/adopt-branch-reconcile.sh:142`, is re-keyed in the pass commit to the
  converted line's signature. Its gate, kind, occurrence and reason stay as they are, and the file
  keeps its row count. Observed by AC9 and AC10.

## 3. Non-goals (OUT)

- No registry row for any of the four files that carry none today, and no row raised. The brief
  says "register nothing new" (item 5), and its non-goal refuses a raise a code change can fix.
- No pin added to or raised in `memory/project/unarmed-branches.txt`. Re-keying row 178 (S7) is not
  raising a pin. The row count, and the row's gate, kind, occurrence and reason, stay the same. Only
  its signature changes, because the code it keys moved. An unmarked delegated site is keyed by its
  own source line with the whitespace squeezed (`tools/memory-tree/check-arms.py:551`), so the
  `:142` conversion changes the key while the site, its line and the reason it is waived stay put.
  No no-fork spelling keeps the old key, so the re-key goes with the conversion (§4, Alternatives
  rejected).
- No drain of `tools/workflows/unattended-build.test.sh` past the excess. A row that equals its
  scan after this unit stays, for the follow-up its reason names. This is the precedent
  TOOL-aSweptBar-5 set for the same leg.
- No change to `tools/gate-lint/sh_hygiene.py`, its classes, its remedies or the leg's argv. The
  left-shift that would catch regrowth at the unit causing it is the open ask TOOL-aSparedSpawn-20.
- No change to any message, exit status or written byte of either adopter. Both refusal sites of
  `tools/roles/adopt-roles.sh` that TOOL-dRedressedBar-6 arms keep their text and their line.
- No new function and no renamed one, so the lexicon and the codebase map's symbol tier read
  nothing new.
- No row of `memory/project/fork-ceilings.txt`; none names a touched file. No kit version bump.
- No edit to anything TOOL-dRedressedBar-1, TOOL-dRedressedBar-4 or TOOL-dRedressedBar-6 owns in
  the shared suites: the probe stop, the GH33 call sites, the arm-9 fixture program, arm 13 and the
  floor.

### Edges

- **hands-off** `TOOL-dRedressedBar-6` — `tools/roles/adopt-roles.test.sh` is left carrying no
  counted fork site and no registry row. The arm-4 remedy assertion that unit rewrites, and the arm
  13 it adds, stay in builtin forms or the leg reds on that file again.
- **hands-off** `TOOL-dRedressedBar-7` — the version bumps for the branch-reconcile and roles kits,
  whose shipped adopters this unit moves; the three suites it touches are withheld from every
  payload, so they move no kit.
- **hands-off** `TOOL-dRedressedBar-10` — two things the round-1 spec audit found (report ids 14 and
  15). §4 cites `tools/roles/adopt-roles.test.sh` sites by `ebce889c` line numbers, which units 1 and
  4 shift before this unit starts, while each site is also named by its content. AC1's path-subst
  and date-fmt half and AC2 count with a re-typed regex, not the leg's `scan_spawn_file`. That unit
  corrects §4 and counts the converted files through the leg's classifier.

## 4. Design

The leg's two rules decide every site. A (path, class) with no row is converted or declared, and a
count may fall and may not rise (`check_registry` and the undeclared-site text,
`tools/gate-lint/sh_hygiene.py:444` and `:928`). Every tracked `*.test.sh` is scanned for the
registry classes whatever the leg's pathspecs exclude (`scan_spawn_tree`, `:845-850`). The brief
takes the declaring half away, so this unit converts and the registry does not move.

### The working set, and why it is measured at the start

The set at `ebce889c` (PINNED from the leg log, 2026-10-13, and re-read from source at spec time,
where all five files are unchanged since `ebce889c`):

| path | class | row | scan | sites at `ebce889c` |
|---|---|---|---|---|
| `tools/branch-reconcile/adopt-branch-reconcile.sh` | `path-subst` | none | 3 | `:25`, `:125`, `:142` |
| `tools/branch-reconcile/adopt-branch-reconcile.sh` | `var-pipe` | none | 3 | `:74`, `:84`, `:114` |
| `tools/roles/adopt-roles.sh` | `path-subst` | none | 3 | `:45`, `:53`, `:55` |
| `tools/roles/adopt-roles.sh` | `var-pipe` | none | 1 | `:165` |
| `tools/roles/adopt-roles.test.sh` | `date-fmt` | none | 1 | `:132` |
| `tools/roles/adopt-roles.test.sh` | `path-subst` | none | 2 | `:36`, `:69` |
| `tools/roles/adopt-roles.test.sh` | `var-pipe` | none | 12 | `:83`, `:90`, `:97`, `:98`, `:106`, `:107`, `:113`, `:160`, `:183`, `:185`, `:245`, `:251` |
| `tools/hooks/format-guard.test.sh` | `path-subst` | none | 1 | `:166` |
| `tools/workflows/unattended-build.test.sh` | `printf-subst` | 66 | 71 | builder's pick, below |
| `tools/workflows/unattended-build.test.sh` | `var-pipe` | 62 | 70 | builder's pick, below |

Units 1 and 4 edit two of these files first. Neither edit is expected to add or remove a site:
unit 1 splits the arguments of `$(build_gh33_writer …)` calls and adds a probe stop, and unit 4
renames a literal inside the single-quoted `A9_WRITE` program. The builder confirms this before any
edit with `git diff ebce889c -- <the five files>`, reading every `-`/`+` line that spells
`$(basename`, `$(dirname`, `$(date`, `$(printf` or a `printf`/`echo` piped into a filter. A diff that
moves a site changes the excess, and the builder stops and returns that to the main loop.

### The forms table

Each site converts through one row. The probe in AC4 runs every row.

| class | forking spelling | no-fork form | exact only when |
|---|---|---|---|
| `path-subst` | `X="$(cd "$(dirname "$0")" && pwd)"` | `X=.; [[ $0 == */* ]] && X=${0%/*}; X="$(cd "$X" && pwd)"` | always; it is the house form at `tools/hooks/format-guard.test.sh:17` |
| `path-subst` | `$(dirname "$p")`, `$p` relative and maybe slash-free | `d=.; [[ $p == */* ]] && d=${p%/*}` | `$p` carries no trailing `/` |
| `path-subst` | `$(dirname "$p")`, `$p` absolute | `d=${p%/*}; d=${d:-/}` | `$p` carries no trailing `/` other than `/` itself |
| `path-subst` | `$(basename "$p")` | `${p##*/}` | `$p` carries no trailing `/` |
| `date-fmt` | `$(date +%F)` | `printf -v v '%(%F)T' -1` | always; both read local time |
| `var-pipe` | `printf '%s' "$v" \| grep -q 'LIT'` | `[[ $v == *'LIT'* ]]` | the flags are `-q` and at most `-F`; LIT holds no regex metacharacter unless `-F` |
| `var-pipe` | `… \| grep -q '^LIT'` | `[[ $'\n'$v == *$'\n''LIT'* ]]` | as above |
| `var-pipe` | `… \| grep -q 'LIT$'` | `[[ $v$'\n' == *'LIT'$'\n'* ]]` | as above; a literal `.` in LIT narrows the match, never widens it |
| `var-pipe` | `… \| grep -qx 'LIT'` | `[[ $'\n'$v$'\n' == *$'\n''LIT'$'\n'* ]]` | as above |
| `var-pipe` | `… \| grep -q 'A.*B'` | `re=$'A[^\n]*B'; [[ $v =~ $re ]]` | A and B are escaped for ERE |
| `var-pipe` | `printf '%s\n' "$v" \| sed 's/^/P/'` | `printf 'P%s\n' "${v//$'\n'/$'\n'P}"` | P holds no `%`, `&` or `\` |
| `var-pipe` | `printf '%s' "$v" \| sed 's#A#B#'` | `w=${v/'A'/'B'}`, then `"$w"` | `$v` is one line; A holds no regex metacharacter; B holds no `&` or `\` after expansion |
| `var-pipe` | `printf '%s' "$v" \| tr -d '\r'` | `${v//$'\r'/}` | written outside every command substitution, since under the bar's MSYS bash a `$'\r'` inside `$( )` expands to nothing and the strip there removes nothing; `$v` holds no newline directly before a CR at its end |
| `var-pipe` | `[ "$(printf '%s\n' "$v" \| wc -l …)" = N ]` | `nl=${v//[!$'\n']/}; [ "$(( ${#nl} + 1 ))" = N ]` | always |
| `var-pipe` | `[ "$(printf '%s\n' "$v" \| grep -c .)" = 1 ]` | `[[ -n $v && $v != *$'\n'* ]]` | `$v` holds no empty line, which `ls` output never does |
| `var-pipe` | `n=$(printf '%s\n' "$v" \| … \| grep -c 'RE')` | `n=0; mapfile -t a <<< "$v"; for x in "${a[@]}"; do [[ $x =~ $re ]] && n=$((n+1)); done` | RE carries over to ERE unchanged |
| `printf-subst` | `"$(printf FMT ARGS)"` as an argument | `printf -v w FMT ARGS`, then `"$w"` | the output cannot end in a newline |

In the `var-pipe` rows, `…` is the `printf '%s'`, `printf '%s\n'` or `echo` of the one expansion the
class admits. The `sed 's#A#B#'` form is written as a plain assignment, never inside double quotes,
and its pattern and replacement are single-quoted. That is the spelling the AC4 probe observed equal
to `sed` on bash 5.3.9, and quoting the replacement keeps bash 5.2's `patsub_replacement` from
reading a `&` in it. The `mapfile` row is the one count the leg admits no expansion for, and the
loop leg grades it by where its lines fall. `scan_file` reads a line as a loop when `done` appears
anywhere on it (`DONE`, `tools/gate-lint/sh_hygiene.py:135`, applied at `:314`). On such a line it
grades a `<<<` whose tail expands a name last assigned from a command substitution as
`loop-var-sub` (`:317-322`). So the row written on one line, fed a `$v` captured by `$( )`, reds
that leg. On a line with no `done`, a `<<<` is graded only when its own tail holds a substitution
(`:319-320`), and `"$v"` holds none. The row is therefore written across two lines:
`mapfile -t a <<< "$v"` on a line with no `done`, and the `for … done` count on the next. The
`mapfile` assigns nothing the follow records (`:101`), so the `for` line reads no fed name.

### The adopters

Each conversion replaces its line in place, so no line of either adopter moves. That keeps the
refusal sites `tools/roles/adopt-roles.sh:209` and `:217`, which TOOL-dRedressedBar-6 cites, where
they are.

- **`tools/branch-reconcile/adopt-branch-reconcile.sh`.** `:25` takes the house form and keeps its
  `|| exit 2`. `:125` and `:142` take `${OLD%/*}` and `${SKILL%/*}`: both values are
  `"$ROOT/<relative path>"` (`:46`, `:109`), absolute and never `/x`. `:74` and `:84` print each hit
  line behind two spaces through the prefix row. `:114` takes the whole-line row, reading `front`,
  which `tr -d '\r'` already stripped (`:113`).
- **The pin that follows `:142`.** `mkdir -p "$(dirname "$SKILL")" || exit 1` is a refusal site
  whose left side is a command, so check-arms reads it as DELEGATED. It is unmarked, so its key is
  its squeezed source line (`tools/memory-tree/check-arms.py:86-91`, `:551`).
  `memory/project/unarmed-branches.txt:178` pins it under that key, and the pins are graded
  (`ARMS_REFUSALS="graded"`, `.memory-tree.conf:639`). Converted, the line keys as
  `mkdir -p "${SKILL%/*}" || exit 1`. Without a re-key, check-arms reports row 178 as a pin "which
  no live site carries" (`:866-871`) and the new key as a site that "is not pinned" (`:863-865`).
  The pass commit therefore rewrites field 4 of row 178, and only that field, from
  `mkdir -p "$(dirname "$SKILL")" || exit 1` to `mkdir -p "${SKILL%/*}" || exit 1`. Fields 1-3
  (`tools/branch-reconcile/adopt-branch-reconcile.sh`, `exit`, `1`) and the reason in field 5 stay
  byte for byte. The reason still holds: `tools/branch-reconcile/adopt-branch-reconcile.test.sh`
  still does not exist. The probe at spec time (PINNED, 2026-10-14) ran check-arms' own
  `scan_refusal_sites` over the `ebce889c` adopter and over the converted one, with all six §4
  conversions applied. Against the `ebce889c` rows, the converted adopter has one stale pin and one
  unpinned site, which are exactly row 178's key and the new one. With row 178 re-keyed, all 11
  rows for that gate are live and no site of it is unpinned. The `:25` conversion moves no key,
  because `exit 2` is outside the population (`EXIT_RE`, `:146`). The two
  `tools/roles/adopt-roles.sh` sites keep their keys, and TOOL-dRedressedBar-6 arms them.
- **`tools/roles/adopt-roles.sh`.** `:45` takes the house form. The walk at `:53` takes the absolute
  `dirname` row: `_p` starts at `KIT_DIR`, which `pwd` prints with no trailing `/`, so `${_p%/*}`
  differs from `dirname` only on `/x`, where it is empty and `${_parent:-/}` restores `/`. That
  keeps the `[ "$_parent" = "$_p" ]` stop at `/`. `:55` takes `${_p##*/}`. `:165` prints each
  surviving-token line behind `    line ` through the prefix row, on stderr as before.

### The suites

- **`tools/roles/adopt-roles.test.sh`.** `:36` takes the house form. `:69` sits inside
  `build_fixture` and reads `CH`, the `CHARTER` conf value, which is `AGENTS.md` in this repository
  (`.memory-tree.conf:445`): slash-free, so `dirname` answers `.`. `${CH%/*}` alone would answer
  `AGENTS.md` and make the fixture create a directory where the charter file goes. It takes the
  slash-free row, on the same line: `_chd=.; [[ $CH == */* ]] && _chd=${CH%/*}; mkdir -p … "$FX/$_chd"`.
  `:132` takes the `date-fmt` row into `_a6day`, on the line that builds `A6P`. The twelve
  `var-pipe` sites take the rows their filters name. `:83`, `:97`, `:98` and `:106` take the
  substring row, `:113` the start-anchored one, and `:107` the end-anchored one. `:90` takes the
  `A.*B` row with `_re2`. `:160` and `:245` sit inside the `"$( … )"` argument of `check_arm`,
  where the CR row's `exact only when` cell rules the strip out. Their strip moves to the capture
  line above each: `:158` and `:243` each end `; rc=$?; out=${out//$'\r'/}`, after `rc=$?`, so `rc`
  still holds the substitution's status. Only `:160` and `:245` read those values of `out` before
  `:168` and `:266` reassign it. `:160` then takes the end-anchored row over `out`, as
  `[[ $out$'\n' == *" task-sha=$msha"$'\n'* ]]`, and `:245` compares `"$out"` itself. A `$'\n'`
  inside `$( )` keeps its newline, as `:245`'s own `"$A9L1"$'\n'"$A9L2"` already relies on.
  `:183` counts through the `mapfile` row into `_nl`, with `_l8`, `_x8` and `_re8`, across two
  lines: `mapfile -t _l8 <<< "$out"` goes at the end of the `:182` capture line, after its `rc=$?`,
  and the `for … done` count stays on `:183`. That count needs no CR strip while each CR sits at a
  line's end, the shape the fixture's CRLF lines give it (the `\r\{0,1\}` the arm's own `sed` at
  `:187` allows for): `mapfile -t` leaves the CR at the end of its element, and `_re8` anchors only
  at the line's start. `:185` counts lines through `_nb`. `:251` takes the one-line row.
- **`tools/hooks/format-guard.test.sh`.** `:166` takes `${2##*/}`, the spelling `check_empty`
  already uses two lines above it.
- **`tools/workflows/unattended-build.test.sh`.** The builder converts exactly five `printf-subst`
  sites and eight `var-pipe` sites, so both counts land on their rows, 66 and 62. A site qualifies
  only when it is a top-level statement on one line. The candidates at `ebce889c` (PINNED) are these.
  For `printf-subst`, the single-line JSON or `"$CHILD_ARGS"` arguments at `:1047`, `:1048`, `:1440`,
  `:1860`, `:2812` and `:2815`, five of them taken, each through `printf -v _wfj`. For `var-pipe`,
  the literal-replacement `sed 's#"slug":"tB",#…#'` sites at `:1902`, `:1904`, `:1909`, `:2698`,
  `:2711`, `:2757`, `:2768` and `:2771`, each through `_wfu`. `:2711` assigns `OC_CT` directly. The
  new assignment goes on the site's own line, ahead of the statement, joined by `;`. It also goes
  after any `rec` or `review_out` call on that line whose global (`_rec`, `_review_out`) its
  arguments read. A converted line keeps the exit status `o=$(run_wf …)` gave, because the last
  command on it is still that assignment.

### Inventory

Shell variables only; no function, file or key is minted. The `lexicon naming predicates` leg reads
shell sources through `parse_shell_defs`, which yields function definitions only
(`tools/lexicon/lexicon.py:747-758`), so no naming cell grades these. Every name was checked absent from its file at spec
time.

| name | file | holds |
|---|---|---|
| `_chd` | `tools/roles/adopt-roles.test.sh` | the charter's directory, `.` when `CH` is slash-free |
| `_a6day` | `tools/roles/adopt-roles.test.sh` | today's date for arm 6's prompt record name |
| `_re2` | `tools/roles/adopt-roles.test.sh` | arm 2's refusal as an ERE |
| `_l8`, `_x8`, `_re8` | `tools/roles/adopt-roles.test.sh` | arm 8's roster lines, the loop variable, the line ERE |
| `_nb` | `tools/roles/adopt-roles.test.sh` | arm 8's output reduced to its newlines |
| `_wfj` | `tools/workflows/unattended-build.test.sh` | a converted `printf -v` JSON argument |
| `_wfu` | `tools/workflows/unattended-build.test.sh` | a converted `sed` replacement |

### Files touched (estimate)

- `tools/branch-reconcile/adopt-branch-reconcile.sh`
- `tools/roles/adopt-roles.sh`
- `tools/roles/adopt-roles.test.sh`
- `tools/hooks/format-guard.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `memory/project/unarmed-branches.txt`

### Alternatives rejected

- A no-fork spelling of `tools/branch-reconcile/adopt-branch-reconcile.sh:142` whose squeezed line
  still equals row 178's key. None exists. That key holds `$(dirname "$SKILL")`, and sh_hygiene
  classifies any `$( )` whose first word is `dirname` as a `path-subst` site
  (`tools/gate-lint/sh_hygiene.py:786-787`), whatever `dirname` resolves to. A `$( )` forks a
  subshell in any case.
- An `# arm-signature: mkdir -p "$(dirname "$SKILL")" || exit 1` marker above the converted line,
  which would make the site's key equal the old row again. A marker declares the text the callee
  prints on that refusal path (`tools/memory-tree/check-arms.py:88-90`). `mkdir` prints none of
  that text, so the marker would put a false fact in the file to keep a stale key. It would also add
  a line to the adopter, which §4 says no conversion does.
- Leaving `:142` unconverted. The file would keep one `path-subst` site with no row in
  `memory/project/spawn-idiom-sites.txt`, so the fork leg would stay red, and a row for it is the
  raise §3 refuses.

- Declaring rows for the four row-less files, as the TOOL-aSparedSpawn-32 reconcile did with its
  "arrived with" reasons. The brief refuses it, and the scanner calls the registry shrink-only
  (`tools/gate-lint/sh_hygiene.py:16`, `:108`).
- `grep -c 'RE' <<< "$v"` for the arm-8 count. It reads clean to the scanner and still forks
  `grep`, so it satisfies the leg without removing the fork the leg exists to remove.
- `${CH%/*}` alone at `tools/roles/adopt-roles.test.sh:69`, the bare form of the precedent's table.
  It is wrong on the slash-free `AGENTS.md` this repository declares, and AC4 stages exactly that.
- Converting more than the excess in `tools/workflows/unattended-build.test.sh`. Each extra site
  would force its row down in the same commit, which moves a shared registry this unit otherwise
  leaves untouched, and the precedent refused the drain for the same leg.
- Lifting the new assignments onto their own lines. It would shift every later line of the suites
  and of `tools/roles/adopt-roles.sh`, which TOOL-dRedressedBar-6 cites by number.
- A CR held in a variable set at top level, such as `_cr=$'\r'`, expanded inside the substitution
  as `${out//$_cr/}` at `:160` and `:245`. It works under MSYS bash, but it mints a name and an
  Inventory row for what one expansion on each capture line already does.
- Declaring the one-line `mapfile` row in `memory/project/substitution-fed-loops.txt`. The brief
  refuses a row a code change can fix, and moving the `mapfile` onto the capture line is that
  change.

## 5. Production-readiness checklist

- security — N/A — no write path, input or surface is added. The adopters write the same files,
  and the scaffold's withdrawal still removes only a recognised render (AC6).
- perf / scale — each adopter run spends fewer forks. The walk at `tools/roles/adopt-roles.sh:52-58`
  loses two per level, and each `--check` loses the `dirname` fork. The leg's own figure is 89 to
  315 ms a fork under MSYS (`tools/gate-lint/sh_hygiene.py:11-12`).
- error / empty / loading states — unchanged and observed. The withdrawal's kept-file refusal, the
  literal-`tools/` refusal and the surviving-token refusal print the same bytes (AC6, AC7). An empty
  `hits` or `left` is never printed: both sit behind a non-empty test.
- observability — N/A — no message, log line or exit status changes.
- risks — A conversion that is not exact turns a suite assertion false-green or false-red, or moves
  an adopter's derived path. The traps are a slash-free `$0` or `CH`, `dirname` of `/x`, and a CR in
  captured output. Each is a row of the forms table, and AC4 stages the first and the CR strip
  written inside `$( )`. A second risk is a
  sibling unit adding a site to `tools/roles/adopt-roles.test.sh`, which now has no row; the
  hands-off to TOOL-dRedressedBar-6 names it.
- testing — AC4's probe runs every form against its forking spelling. AC5, AC6 and AC7 run both
  adopters over a fixture. At the close, the `roles adopter self-test`, `branch-reconcile selftest`,
  `format-guard self-test` and `unattended-build self-test` legs re-run every converted assertion.
- migration — N/A — no data, conf or receipt shape changes. Both adopters are idempotent, and an
  adopter receives their bytes on its next apply once unit 7 bumps the two kits.
- user docs — N/A — no behaviour changes, so no page under `help/` moves.

## 6. Acceptance criteria

- **AC1** — When
  `grep -nE '\$\((basename|dirname|date) ' tools/branch-reconcile/adopt-branch-reconcile.sh tools/roles/adopt-roles.sh tools/roles/adopt-roles.test.sh tools/hooks/format-guard.test.sh`
  runs, it prints nothing. Red when: any `path-subst` or `date-fmt` site in those four files still
  forks.
  figure: 10 lines at `ebce889c`, PINNED at spec time.
- **AC2** — When
  `grep -oE '(printf .%s(.n)?.|echo) +"?\$[{A-Za-z_][^|]*\| *(grep +-[A-Za-z]*[qc]|wc +-l|tr |sed +(-e +)?.?s|head +-(n *)?1|cut )' <file> | wc -l`
  runs per file, it prints `0` for `tools/branch-reconcile/adopt-branch-reconcile.sh`,
  `tools/roles/adopt-roles.sh` and `tools/roles/adopt-roles.test.sh`. For
  `tools/workflows/unattended-build.test.sh` it prints the `var-pipe` count that file's row in
  `memory/project/spawn-idiom-sites.txt` declares. Red when: a `var-pipe` site survives in a
  row-less file, or the suite lands above or below its row.
  figure: 3, 1, 12 and 70 at `ebce889c`, PINNED at spec time, equal to the leg log's scan for
  each; the row is DERIVED by reading it at observation time, 62 at `ebce889c`.
- **AC3** — When `git diff -U0 <pass>~1 <pass> -- tools/workflows/unattended-build.test.sh` is read
  at this unit's pass commit, exactly five `-` lines spell `$(printf ` with no `|` inside that
  substitution, and their `+` lines spell `printf -v _wfj` and no `$(printf `. Run before and after
  the pass, `grep -o '\$(printf ' tools/workflows/unattended-build.test.sh | wc -l` falls by exactly
  thirteen: one for each of the five `printf-subst` sites, and one for the
  `$(printf '%s' … | sed …)` each of the eight `sed` sites §4 pins carries, which the
  `w=${v/'A'/'B'}` row removes. Red when: a `printf-subst` site stays unconverted, a sixth converts
  and its row drifts below the scan, a `var-pipe` conversion leaves its `$(printf ` behind, or a
  `var-pipe` site other than the eight pinned `sed` sites converts in place of one. Each moves the
  fall off thirteen or the `-` lines off five.
  figure: 288 occurrences at `ebce889c` and 275 after the pass, PINNED at spec time. Each of the
  fourteen §4 candidate lines carries exactly one, so the six `printf-subst` candidates and eight
  `sed` sites hold 14 of the 288. The fall of 13 holds only while the start-of-unit diff in §4 moves
  no `$(printf ` line.
- **AC4** — When the forms probe runs each row of the §4 table, forking spelling against no-fork
  form, over a match, a non-match and a specimen at the boundary its `exact only when` cell names,
  every row reports the same output and exit status. Its specimens include `AGENTS.md`, `docs/x.md`,
  `/c` and `/c/x` for the path rows, a value ending in `\r` for the CR row, and each `sed` site's own
  one-line JSON value from `tools/workflows/unattended-build.test.sh`, read at the converted line. The
  CR row also runs a CRLF capture through arm 9's shape: the strip at top level on the capture line,
  then the compare inside `$( )`. Two staged wrong forms each report a difference: `${CH%/*}` alone
  on `AGENTS.md`, and the CR strip written inside `$( )` on a value ending in `\r`. Red when: a
  row's two spellings disagree on a specimen, or a staged wrong form reports none.
  fixture: the probe lives in the session scratchpad and its output goes to the unit's acceptance
  ledger; nothing is committed. Run under the bash the bar runs.
- **AC5** — When `bash tools/roles/adopt-roles.sh --check` and
  `bash tools/branch-reconcile/adopt-branch-reconcile.sh --check` run from a fixture clone's root,
  and again as `bash adopt-roles.sh --check` and `bash adopt-branch-reconcile.sh --check` from their
  own directories, each prints the same lines and exits with the same status as the same run of the
  `ebce889c` adopter in that clone. Red when: a slash-free `$0` derives the kit directory as the
  script's own name, or the walk derives a `KIT_REL` other than `tools/roles`.
  fixture: a `git clone` of this worktree under `%TEMP%/<short-name>`, with `TMPDIR` set to the
  session scratchpad, since `tools/branch-reconcile/adopt-branch-reconcile.sh:97` calls `mktemp`.
  None is in the tree; where the isolation hook refuses the clone, the criterion is returned to the
  main loop as owed.
- **AC6** — When the same clone holds a recognised old render at
  `.claude/skills/branch-reconcile/SKILL.md` and
  `bash tools/branch-reconcile/adopt-branch-reconcile.sh --scaffold` runs, it prints `withdrew
  .claude/skills/branch-reconcile/SKILL.md` and both the file and its directory are gone. With an
  unrecognised file planted there, it prints `is not this kit's old render, so it is kept` and
  exits 1. With `tools/x` appended to `tools/branch-reconcile/SKILL.template.md`, it exits 1 and the
  hit prints as one line opening with two spaces and the line number. Red when: the withdrawal
  leaves the directory, the whole-line test keeps a recognised render or withdraws a foreign one, or
  a hit line loses its indent.
  fixture: as AC5; the recognised render is the fresh render with `name: cleanup` replaced by
  `name: branch-reconcile`, the shape `tools/branch-reconcile/selftest.py` `arm_old_render` plants.
- **AC7** — When `{{UNKNOWN_TOKEN}}` is appended to the clone's `tools/roles/SKILL.template.md` and
  `bash tools/roles/adopt-roles.sh --scaffold` runs, it exits 1, and stderr carries
  `roles: a token survived the render` and then a line `    line <n>:{{UNKNOWN_TOKEN}}`. Red when:
  the prefix row drops the `    line ` head or prints the token line without it.
  fixture: as AC5.
- **AC8** — When `git diff <pass>~1 <pass> -- memory/project/spawn-idiom-sites.txt` runs at this
  unit's pass commit, it prints nothing. Red when: a row is added for a site the forms table
  converts, or a row moves to absorb a miscount.
- **AC9** — When `git diff -U0 <pass>~1 <pass> -- memory/project/unarmed-branches.txt` is read at
  this unit's pass commit, it holds one hunk with one `-` line and one `+` line. The `-` line is the
  row whose first field is `tools/branch-reconcile/adopt-branch-reconcile.sh` and whose fourth is
  `mkdir -p "$(dirname "$SKILL")" || exit 1`. Split at tabs, the two lines have five fields each and
  agree on fields 1, 2, 3 and 5. The `+` line's field 4 reads `mkdir -p "${SKILL%/*}" || exit 1`.
  `git show <pass>:memory/project/unarmed-branches.txt | wc -l` prints the same count as the same
  command at `<pass>~1`. Red when: the row is left on its old signature, is re-keyed to a spelling
  the converted line does not carry, or has its gate, kind, occurrence or reason changed, or a row
  is added or removed.
  figure: row 178 of 181 lines, and 11 `exit` rows for that gate, at `ebce889c`, PINNED at spec
  time. The row is named by its content, so a sibling edit that moves its line number does not
  break the criterion.
- **AC10** — When a probe imports `tools/memory-tree/check-arms.py` and calls its own
  `scan_refusal_sites` over the pass tree, it keys every site of
  `tools/branch-reconcile/adopt-branch-reconcile.sh` as (gate, kind, occurrence, `key_sig`). Every
  pass `exit`/`status` row of `memory/project/unarmed-branches.txt` for that gate then matches a live
  site, and no site of that gate lacks a row. Run with the `<pass>~1` adopter against the pass rows,
  the same probe reports row 178 stale and the `mkdir -p "$(dirname "$SKILL")" || exit 1` site
  unpinned. That is the staged red, and it shows the probe can move. The two
  `tools/roles/adopt-roles.sh` sites have the same keys at `<pass>~1` and at the pass. Red when:
  any pin of that gate is stale, any of its sites is unpinned, or the staged run reports nothing.
  fixture: the probe lives in the session scratchpad and its output goes to the unit's acceptance
  ledger; nothing is committed. The population comes from the probe's file list, not from
  `git ls-files` in a scratch clone, because the isolation hook refuses git outside the worktree.
  figure: 11 rows live and 13 sites across both adopters (11 + 2), PINNED at spec time from the
  same probe over `ebce889c` with the six §4 conversions applied.

## 7. Gates

`shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `roles adopter self-test` · `branch-reconcile selftest` · `format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The main loop runs these at the close. The first is the leg this unit turns green; its red was
observed by the full bar over `ebce889c`. The second grades every line this unit writes. It would
grade the `mapfile` row's `<<< "$out"` as `loop-var-sub` were it written on the `:183` loop line,
and on the `:182` capture line, which holds no `done`, it grades nothing. The suites on the line are the ones whose files or guarded directories this unit
touches. `harness arms (fail branches armed or pinned)` grades every `exit 1` site of both adopters
against `memory/project/unarmed-branches.txt`. Every site keeps its line, but `:142`'s
delegated key changes with the conversion, and row 178 is re-keyed with it (S7). That leg reads
green for `tools/branch-reconcile/adopt-branch-reconcile.sh` only when the conversion and the
re-key land in the same commit. `recall floor` and `recall floor arms` are on the line because their
`memory/` guard covers the pin file. `spawn budget (forks per hot entrypoint)` is not owed: no touched file has a
row in `memory/project/fork-ceilings.txt`. This unit adds and moves no suite arm and declares none.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft, from item 5 of the build brief.
- rev-2 · 2026-10-14 · §3 · Edges gain the hands-off to TOOL-dRedressedBar-10, the batch the round-1
  spec audit's minors were promoted into, for report ids 14 and 15. No scope, design or criterion
  moves.
- rev-3 · 2026-10-14 · AC3 · the whole-file `$(printf ` count falls by thirteen, not five: each of
  the eight `sed` sites S5 converts carries one inside its `$(printf '%s' … | sed …)`, which the
  builder's divergence report found. The whole-file count is kept over a pipe-free one because a
  pipe-free count never sees a `var-pipe` conversion that leaves its `$(printf '%s' … |` behind. Its
  "Red when" and figure lines follow. No scope, design or other criterion moves.
- rev-4 · 2026-10-14 · §4 · §5 · AC4 · §7 · the builder's second divergence report, both findings
  probed again under Git Bash 5.3.9. (1) A `$'\r'` inside `$( )` expands to nothing there, so the
  CR strip for `:160` and `:245` moves to the `:158` and `:243` capture lines as
  `out=${out//$'\r'/}`. The CR row's `exact only when` cell excludes a command substitution, and
  AC4 adds arm 9's shape and the strip inside `$( )` as a staged wrong form. (2) `scan_file` reads
  any line holding `done` as a loop and grades the one-line `mapfile` row as `loop-var-sub`, so
  `mapfile -t _l8 <<< "$out"` moves onto the `:182` capture line. The paragraph under the forms
  table and the §7 note now say what `scan_file` grades. Alternatives rejected gains the `_cr`
  variable and the loop-registry row. No other scope or criterion moves.
- rev-5 · 2026-10-14 · §2 · S7 · §3 · §4 · AC9 · AC10 · §7 · the builder's third divergence report.
  `memory/project/unarmed-branches.txt:178` pins the unmarked delegated site at
  `tools/branch-reconcile/adopt-branch-reconcile.sh:142` under its squeezed source line, so the
  `${SKILL%/*}` conversion changes its key. A probe found no no-fork spelling that keeps the key, so
  S7 re-keys row 178 in the pass commit, changing field 4 only. §3 states that a re-key is not a
  raise. §4 gains the paragraph on the pin, the pin file in Files touched, and three rejected
  alternatives. AC9 observes the diff of the pin file and AC10 runs the check-arms probe. §7 corrects
  what `harness arms` reads and adds `recall floor` and `recall floor arms`, which the pin file's
  `memory/` guard requires. No other scope, design or criterion moves.

## 10. Reuse audit

The seams are the no-fork forms already in the tree, and the registry is extended by not moving.
The house `dirname` form is `tools/hooks/format-guard.test.sh:17`, landed by TOOL-aSweptBar-5. The
forms table extends that unit's §4 table
(`memory/builds/aSweptBar/spec/2026-10-13-spec-TOOL-aSweptBar-5.md`) with the rows this set
needs: the slash-free and absolute `dirname` cases, `date-fmt`, the whole-line, end-anchored and
`A.*B` tests, the per-line prefix, and the two counts. The builtin `${2##*/}` is already
`check_empty`'s spelling in `tools/hooks/format-guard.test.sh`. `tools/codebase-map/reuse_lookup.py`
with "derive a script's directory or a path's parent without forking dirname" ranked only
name-stem matches, `derive_*` functions and `resolve_charter_path` among them, none a shell idiom.
Its symbol tier indexes functions and these forms are inline, so no existing seam fits from the map
and the seams above are cited from source. Recall ranked TOOL-aSweptBar-5 first, then
TOOL-aSparedSpawn-8, which made the registry shrink-only, and TOOL-aSparedSpawn-20, the left-shift
ask that would have caught these at their landings. `gotchas.py --for-paths` over the adopters
selected `fixture-passes-by-finding-nothing`, which is why AC4 stages a wrong form and AC6 plants
both a recognised and a foreign file.

Recall terms used: `python tools/memory-recall/query.py "how were fork idioms past the spawn-idiom registry converted in adopters and suites" --terms "spawn-idiom registry fork no-fork path-subst var-pipe date-fmt printf-subst sh_hygiene shrink-only adopter"`

# TOOL-dRedressedBar-24 — the runner scripts' fixed-name temp writers take unpredictable temps, and a shell-hygiene mode reds a new one

**Status:** INPROGRESS · rev-1 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-prompt-TOOL-dRedressedBar-24-1-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-24-1-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-24-brief.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-24-brief.md) | research | TOOL-dRedressedBar-21 |

<!-- /gen:spec-records -->

## 1. Goal

H1 of the round-1 closing diff review (`reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md`)
is a temp file written at a fixed name and renamed over its destination. A process that can write
the temp dir plants a link at that name, and the write goes through it. `TOOL-dRedressedBar-21`
closes the class in the run-gates kit's Python. Its F1 found the class in the kit's bash, and the
owner resolved F1 as (a) on 2026-10-15: this unit takes it (README, Build-level rules). Its brief
is `prompts/2026-10-15-prompt-TOOL-dRedressedBar-24-brief.md`.

This unit gives every temp-then-rename writer in `run-gates.sh`, `post-merge.sh` and
`run-selftests.sh`, and the Python writer in a `run-gates.sh` heredoc, a temp name nobody can know
before the write creates it, in the destination's own directory. It adds a fourth mode to
`tools/gate-lint/sh_hygiene.py` and a leg that runs it, so a new fixed-name temp-then-rename writer
in any tracked product shell source reds.

The brief counted 19 `mv` sites and one heredoc writer. Enumerated from the tree (§4), the class
holds 22 `mv` sites in the three files and the heredoc writer. Four of them write in `$WORK`, which
the planter H1 describes can write. One of the 22, the health log's trim, is a parity-gated copy of
a shared block, and this unit registers it rather than fixing it (§3).

## 2. Scope (IN)

- **S1** — One temp-name helper in the runner. `run-gates.sh` gains `derive_temp_path <name> <dest>`,
  one line at column 0 directly below `# <<< health_log_sh` (`run-gates.sh:777`), outside every
  inline block. It assigns the variable `<name>` through `printf -v`. With `$SRANDOM` non-empty, the
  value is `<dest>.<SRANDOM><SRANDOM>.tmp`, and the helper forks nothing. With it empty, as on bash
  5.0, the value is `$(mktemp -u "<dest>.XXXXXXXX")`, and the helper returns 1 when that is empty.
  It creates no file: the site's own `>` creates the temp, so the open that creates it is the open
  that writes it. Observed by AC1.
- **S2** — The runner's 18 sites take the helper. Each site in §4's table, rows R1 to R18, calls
  `derive_temp_path _tp "<dest>"` ahead of its write, writes to `"$_tp"`, moves `"$_tp"` onto its
  destination, and spells `"$_tp"` wherever it cleaned its fixed temp on failure. Inside a function
  `_tp` is declared `local`. R11 and R15 keep their variables, `merged` and `_vtmp`, as the helper's
  first argument. R11's ledger temp moves out of `$WORK` to beside `$LEDGER`; after `mv` and its
  `cp` fallback, a temp still present is deleted. R15's `GATE_VERDICT_FAULT` seam names
  `"$RUNDIR/verdict-fault/verdict"` as the helper's destination, so its write still fails in a
  directory that does not exist. Observed by AC2, AC4 and AC5.
  - **Readers:** S2 retires the runner's fixed temp names, `$WORK/owner.tmp` and the 17 others §4
    lists, and `$WORK/ledger.merged`.
    by name: `tools/run-gates/run-gates.test.sh`, whose 9h arm plants a directory at the spawn
    floor's fixed temp, held.tmp (`run-gates.test.sh:3237`); `tools/run-gates/run-gates.runlog.test.sh`,
    whose TWO arm finds the shared-green statement by its fixed staging name and counts leftovers
    by it (`:1066`, `:1068`, `:1079`). S8 re-arms both. A grep of the tree outside `memory/` finds no
    other reader that spells one of the names.
    by value: `tools/run-gates/run-gates.turnstile.test.sh`, whose R6 arm runs the shipped
    `ts_tick_start` from a `sed` extraction (`:382`), so the ticker's write needs the helper beside
    it (S8). The run-record readers read `*.leg`, `*/verdict`, directories or exact names
    (`derive-ceilings.py:267`, `drift_report.py:3131`, `:3250`), and the runner's own globs are
    `*.pid`, `*.leg` and `*.defer` (`:2322`, `:2438`, `:4577`); none matches `<name>.<digits>.tmp`.
    The retention prune at `:5660-5663` deletes a stray `current.<digits>.tmp` as it deleted
    `current.tmp`.
- **S3** — The heredoc writer takes `tempfile.mkstemp`. The reuse-cache program (`run-gates.sh:5463-5488`)
  imports `tempfile`, opens each entry's temp with `tempfile.mkstemp(dir=d, prefix=key + ".",
  suffix=".tmp")`, writes it through `os.fdopen(fd, "w", encoding="utf-8", newline="\n")`, and calls
  `os.replace`. An `OSError` after the temp exists deletes the temp, and the entry is skipped as now.
  Observed by AC6.
  - **Readers:** S3 retires the temp name `<key>.tmp.<pid>`.
    by name: `tools/run-gates/run-gates.sh`, the one file that spells it (`:5472`).
    by value: NO VALUE READERS — no code opens the temp by name. The cache reader reads
    `<k[0:2]>/<key>` by key, and the 30-day prune in the same program deletes by mtime any file
    under a two-character directory, a stray temp included.
- **S4** — The other two scripts name their temps with `mktemp -u`. `write_post_merge_record` and
  `write_bar_green` in `post-merge.sh` (`:55-61`, `:346-349`) and the baseline write in
  `run-selftests.sh` (`:1972-1975`) take `t=$(mktemp -u "<dest>.XXXXXXXX")` ahead of the write and
  spell `"$t"` for the temp. A failed write deletes `"$t"` when it is non-empty. Both are cold paths,
  run once per bar or per attributed suite, so the fork is paid there and nowhere hot. Observed by
  AC2, AC4 and AC5.
  - **Readers:** S4 retires `gate-post-merge.tmp`, `gate-bar-green.shared.tmp` and the baseline's
    `.tmp.$$` suffix.
    by name: `tools/run-gates/post-merge.sh` and `tools/run-gates/run-selftests.sh`, the files that
    spell them. A grep of the tree outside `memory/` finds no reader of either `post-merge.sh` name,
    and none of the baseline suffix.
    by value: NO VALUE READERS — the pre-push hook and the lander read `gate-bar-green.shared` and
    `gate-post-merge` by their final names, and the baseline reader reads `<key>.<blob>.fails`.
- **S5** — The class gate: `sh_hygiene.py --temp-names [registry] [root] [pathspec ...]`, a fourth mode
  beside `--spawn-idioms`, with the predicate §4 defines. A `fixed-temp` site is an `mv` whose
  source names a temp no unpredictable part names. The registry is shrink-only, keyed on the file
  and the class. The module docstring gains the mode's usage line and a paragraph, and
  `run_temp_scan`'s docstring states what the mode does not check. `--selftest` gains the arms
  §4 lists, and `FLOOR_ASSERTIONS` (`sh_hygiene.py:213`) rises to the count it prints. Observed by
  AC2, AC3 and AC7.
- **S6** — The registry, `memory/project/temp-name-sites.txt`, declaring the 20 sites in 14 files that
  §4 lists, each row with its reason, under a header in `spawn-idiom-sites.txt`'s form. `.memory-tree.conf`'s
  `PROJECT_REGISTRY_EXTRA` (`:888`) gains `temp-name-sites.txt` as its ninth member, with a comment
  in the form of the members above it. Observed by AC3.
- **S7** — The leg declarations. `tools/gate-legs.json` gains, after `shell hygiene (a fork spent on
  builtin work)` (`:187`), the row `shell hygiene (a fixed-name temp renamed into place)`: argv
  `python3 {prefix}/gate-lint/sh_hygiene.py --temp-names memory/project/temp-name-sites.txt .
  :!*.test.sh :!memory/`, chunk `product`, subject `repo`, ceiling 300, no guard.
  `tools/gate-lint/kit.toml` gains a `[[gate_leg]]` of that name, subject `repo`, argv
  `["python3", "{kit}/sh_hygiene.py", "--temp-names"]` and `guard = []`, with a comment in the form of
  the spawn-idiom leg's (`kit.toml:79-91`). The gate-lint dossier, `memory/map/features/gate-lint.md`,
  lists the leg's name under its `gate-legs` key (`:11-18`), and its Affordances gain the mode and
  the registry. `tools/gate-lint/README.md` gains a `--temp-names` section after the
  `--spawn-idioms` one (`:131-157`). Observed by AC8.
- **S8** — The three suites that read a retired name or the ticker's write are re-armed, each keeping
  what it observes. 9h in `run-gates.test.sh` stages its write failure with a floor file whose name
  is 250 characters: the file exists, and every temp the helper names beside it is at least 257
  characters, past the 255 a name component may hold. TWO in `run-gates.runlog.test.sh` finds the
  statement by its `derive_temp_path _tp "$_gcd_abs/gate-full-green.shared"` call, runs it with the
  helper's line prepended, and checks distinct staging names by running the helper in two processes.
  It counts leftovers as names matching `gate-full-green.shared.*.tmp`. R6 in
  `run-gates.turnstile.test.sh` adds `/^derive_temp_path()/p` to its `sed`. It gains one check that
  `heartbeat` holds a number after the ticks, so an extraction that drops the helper reds, and its
  `FLOOR_ASSERTIONS` (`:164`) rises from 144 to 145. Observed by AC5 and AC9.
  - **Readers:** S8 retires each arm's spelling of `held.tmp` and `gate-full-green.shared.tmp`.
    by name: `tools/run-gates/run-gates.test.sh` and `tools/run-gates/run-gates.runlog.test.sh`,
    which S8 itself edits.
    by value: NO VALUE READERS — each arm's assertion strings and counts are its own, and no other
    suite reads them.
- **S9** — A new canary arm, 9e2 in `run-gates.test.sh`, below 9e and above the `HAVE_TIMEOUT` block
  (`:3154`). Through `build_hv_repo` and `run_hv_bar` (`:3013-3030`) it runs a one-leg bar whose leg
  derives `$WORK` from its `TMPDIR` (`run-gates.sh:2275`). The leg hard-links `$WORK/0.rc.tmp` and
  `$WORK/ledger.merged` to a secret file outside the repo, and writes a marker naming both. After
  the bar it checks four things: the marker exists, the secret still holds its bytes, the bar exited
  0, and the ledger carries the leg's row. `FLOOR_ASSERTIONS` (`:142`) rises from 401 by the arm's
  four. Observed by AC5, which stages the same plants on the extracted writers; the arm re-observes
  them inside a bar at the close (§7).
- **S10** — The record. The product commit `<p24>` carries the kickoff-manifest re-stamp at its
  parent that the ratchet's staged check requires, as `809f794e4` did. A second commit, `<p24m>`,
  re-stamps `last-audit:` in `memory/guides/SESSION-KICKOFF.md` at `<p24>` after a section B
  re-read, with a `manifest-audit:` line in its body, as `cafbbc460` did. `python
  tools/codebase-map/gen_map.py --write` runs before `<p24>`, since the unit mints a shell function
  and Python functions. The readings go to an acceptance ledger under
  `memory/builds/dRedressedBar/build/` carrying `**Serves:** journal TOOL-dRedressedBar-24`. The
  build writes no spec but this one's status and date cells. Observed by AC10.

## 3. Non-goals (OUT)

- Every direct write at a fixed name in `$WORK`, the class one step wider than this unit's. 34
  lines of `run-gates.sh` redirect into `"$WORK/` or `"$_work/` (PINNED at `2aa18f2a3`), and three
  of them are S2's temps. The rest write their file in place, `$WORK/ledger.new` and
  `$WORK/cache.writes` among them, and a link planted at one is written through. The same holds for
  `run-selftests.sh`'s `$ATTR_TMP/r.set` (`:1796`) and `manifest-check.sh`'s `$CARD_TMP`. No temp
  name closes those: the remedy is a scratch dir the planter cannot write, or an exclusive open per
  file, and either is its own unit.
- The 20 registered sites. Five are the health log's trim, the `health_log_sh` block that
  `tools/lib/health-log.sh` holds canonically and four kits carry byte-identically under the parity
  table in `tools/lib/resolve-python.test.sh:175`. `health_log.py` and `process-monitor/reap.py`
  carry its Python twin with a `.trim.<pid>` temp. The trim is open ask `TOOL-aPairedSlots-10`, left
  there by `TOOL-aPairedSlots-7` for the same reason, and it writes the git common dir, which H1's
  planter cannot write. The other 15 sit in nine files of other kits, and none is H1-reachable (§4).
- The retry-to-tail rename at `run-gates.sh:4507-4509`. It moves a finished record, and no temp is
  involved.
- No exclusive open in bash. `set -C` would refuse a planted entry, but an unpredictable name
  leaves nothing to plant before the write creates it (§4).
- No kit version moved. Run-gates' shipped bytes move: `run-gates.sh`, `post-merge.sh` and
  `run-selftests.sh`. Its value stays 1.41 on this branch (`run-gates.sh:36`, set by unit 18). The
  lander's `govkit.py mint` dates the move at the landing (`tools/govkit/govkit.py:13381`, "WHERE THE
  BUMP IS MADE"), and off the boundary `kit epoch` prints `owed at the lander`. Gate-lint declares
  no version (`tools/gate-lint/kit.toml:6`), so `kit epoch` prints its announced skip for it.
- No change to `memory/project/fork-ceilings.txt`. S1 forks nothing on bash 5.1 and later, and the
  rows declare bash 5.3 alone, so `run-gates-1leg` and `run-gates-2leg` keep 55 and 57.
- Python inside a shell string. Neither this mode nor unit 21's `*.py` arm reads it; S3 is observed
  by AC6 alone.

### Edges

- **consumes-from** `TOOL-dRedressedBar-21` — the hand-off of the bash fixed-name temp writers and the
  heredoc writer, F1 resolved as (a). It also takes the shape of that unit's `write_replace`: a
  `tempfile.mkstemp` temp in the destination's directory, `os.replace`, the temp deleted on
  failure. S3 spells that shape inline, because the `-c` program imports no kit sibling and a
  fixture runner carries none. Without the hand-off, the bash sites would sit in both units' scope.
- **hands-off** external — the direct fixed-name writes in `$WORK` and the other `mktemp -d` scratch
  dirs (§3), for the owner to promote as a unit or record.
- **hands-off** external — the registered sites: the `health_log_sh` trim, ask `TOOL-aPairedSlots-10`,
  and the 15 sites in other kits, each drained by deleting its registry row in the commit that fixes it.

## 4. Design

### Evidence, read at `2aa18f2a3` on 2026-10-15

`2aa18f2a3`'s `tools/`, `help/`, `skills/`, `.githooks/` and `.memory-tree.conf` equal
`e114f1356`'s, the reviewed range's tip (`git diff --stat e114f1356 2aa18f2a3 -- tools help .githooks
skills .memory-tree.conf` prints nothing). Units 21 to 23 share only `tools/gate-legs.json`, the
kickoff manifest, the generated map and the ledger folder with this unit, and order sequences those.

**Who can write each directory.** H1's planter is a process of the operator's own user confined to
the temp dir: a sandboxed agent, or any writer of a shared `TMPDIR`. On this host `/tmp` is the
operator's own `%TEMP%`, under `$HOME` (`TOOL-aTetheredScratch-2`). `$WORK` is `mktemp -d` under
`${TMPDIR:-/tmp}` (`run-gates.sh:2211-2212`), so the planter can write it. The git dir, the git
common dir and `$HOME/.gov/gate-turnstile` (`:1516`) sit outside the temp dir, so it cannot. No
directory below is writable by another OS user by default. An operator who points
`GATE_TURNSTILE_DIR`, `GATE_SPAWN_FLOOR` or `TMPDIR` into a shared directory moves those rows
into the planter's reach, and the fix covers them there too.

**The class, enumerated.** A probe built on `sh_hygiene.py`'s own parsers applied S5's predicate to
every tracked product shell source (`. :!*.test.sh :!memory/`, 67 files). It found 41 `fixed-temp`
sites in 16 files, 7 sites admitted (all `$(mktemp` in `unattended.sh` and `adopt-unattended.sh`),
and 1 unfollowed (`run-gates.sh:4508`). All are PINNED at `2aa18f2a3`. The three runner files hold
22 of the 41: 19 in `run-gates.sh`, 2 in `post-merge.sh`, 1 in `run-selftests.sh`. The brief's 19
was the narrow `grep -cE 'mv -f? ?"[^"]*\.tmp'`, which misses `.trim.$$` (`:766`), `"$merged"`
(`:5259`) and `"$_vtmp"` (`:5542`).

### The sites

`run-gates.sh` unless named. H1 marks a row whose temp sits where the planter writes.

| # | Lines | Destination, and where its directory comes from | H1 | Runs |
|---|---|---|---|---|
| R1 | 1349-1354 | `gate-host-calibration` in the common dir (`:930`) | no | `--calibrate-width` |
| R2 | 1641, `ts_hb` | `heartbeat` in the turnstile slot dir (`:1516-1522`) or the docs beacon (`:1871`) | no | each leg's end |
| R3 | 1694-1695, the ticker in `ts_tick_start` | the same `heartbeat` | no | each tick |
| R4 | 2220-2221, `write_work_owner` | `$WORK/owner` | yes | once |
| R5 | 2596 | `gate-run/current` in the git dir (`:2591`) | no | once |
| R6 | 3540 | `$RUNDIR/header` | no | once |
| R7 | 3792-3796, `write_spawn_floor` | `gate-spawn-floor` in the common dir (`:3735`) | no | once, when measured |
| R8 | 3941-3942, `runleg` | `$RUNDIR/<i>.leg` | no | each leg |
| R9 | 3955, `runleg` | `$WORK/<i>.rc` | yes | each leg |
| R10 | 4279-4280, the census loop | `$WORK/spawn-now` (`_work`, `:4262`) | yes | each tick of a live spawn pause |
| R11 | 5218, 5257-5259 | `gate-ledger.tsv` in the git dir (`:454`), staged at `$WORK/ledger.merged` | yes | once |
| R12 | 5351 | `$RUNDIR/verdict`, RED | no | once |
| R13 | 5378 | `$RUNDIR/verdict`, REFUSED | no | once |
| R14 | 5415-5416 | `gate-selftest-last/<key>` in the common dir (`:2961`) | no | each held leg |
| R15 | 5524-5542 | `$RUNDIR/verdict`, final, and the fault seam | no | once |
| R16 | 5599-5600 | `gate-full-green` in the git dir | no | once |
| R17 | 5615-5617 | `gate-full-green.shared` in the common dir | no | once |
| R18 | 5651-5652 | `gate-inherited-green` in the git dir | no | once |
| H | 5463-5488, the heredoc | `gate-cache/<k[0:2]>/<key>` in the common dir (`:3309`) | no | each cached leg |
| P1 | `post-merge.sh:55-61` | `gate-post-merge` in the common dir (`post-merge.sh:85`) | no | once |
| P2 | `post-merge.sh:346-349` | `gate-bar-green.shared` in the common dir | no | once |
| S | `run-selftests.sh:1972-1975` | `<key>.<blob>.fails` under the common dir (`run-selftests.sh:1779`, `:1943`) | no | each attributed suite |
| — | 766-767, `add_health_event` | `health.log` in the common dir | no | registered (§3) |

### The helper, and why it is not `mktemp` at every site

R2, R3, R8, R9 and R10 run per leg or per tick. The ticker's own comment rules out any fork but
its `sleep` and its `mv` (`run-gates.sh:1681-1686`, TOOL-aSparedSpawn-15 S3). Forks under MSYS cost
89 to 315 ms each (`sh_hygiene.py:13`). `run-gates-1leg` and `run-gates-2leg` in
`memory/project/fork-ceilings.txt` hold the runner to 55 and 57, so a `$(mktemp)` per site would
raise both. `$SRANDOM` is a builtin, with no fork. The runner already pairs each newer builtin with
a fallback, as `EPOCHREALTIME` does at `:2405` and `:3843`, so bash 5.0 keeps working here at
`mktemp -u`'s cost.

```bash
# derive_temp_path <name> <dest> — sets <name> to an unpredictable sibling of <dest>; creates nothing (TOOL-dRedressedBar-24)
derive_temp_path() { if [ -n "${SRANDOM:-}" ]; then printf -v "$1" '%s.%s%s.tmp' "$2" "$SRANDOM" "$SRANDOM"; else printf -v "$1" '%s' "$(mktemp -u "$2.XXXXXXXX" 2>/dev/null)"; [ -n "${!1}" ]; fi; }
```

Probes, PINNED, run on node d under bash 5.3.9 (MSYS) on 2026-10-15:

| Probe | Reading |
|---|---|
| `$SRANDOM` in two subshells and the parent | three different values |
| `grep -c getrandom /usr/bin/bash.exe` and the same for `arc4random` | 1 and 1 |
| `unset SRANDOM`, then `$SRANDOM` | empty, so the fallback branch can be exercised |
| `mktemp -u "<d>/dest.XXXXXXXX"` twice | two different names, and `<d>` holds no file |
| `mktemp -u` with a directory that does not exist | prints a name and exits 0, so the `>` is what fails |
| `ln secret.txt w/0.rc.tmp`, then `printf 0 > w/0.rc.tmp` and `mv` to `w/0.rc` | `secret.txt` reads `0`, and both names share one inode, link count 2 |
| a file whose name is 250 characters, then `> "<it>.1.tmp"` | the file is made; the temp fails, `File name too long` |

The fifth row is why R15's fault seam keeps working. The sixth is the red half of S9's arm, and
the seventh is how S8 stages 9h's failure.

The name is unknown until the write creates it, so there is nothing at it to follow. An entry
swapped in after the write and before the `mv` moves onto the destination. That is a write the
planter could make at the destination directly, in a directory it can write. A temp left by a
crash between write and rename is a stray file, not one overwritten next run. It sits in a
directory the operator owns.

### The class gate: `--temp-names`

The population is the one `read_shell_sources` derives (`sh_hygiene.py:821`): tracked `*.sh` files
and extensionless shell-shebang files under the pathspecs. Each file is read through
`read_code_lines` (`:723`), so comment halves and quoted heredoc bodies are never graded.

| Step | Rule |
|---|---|
| an `mv` | the word `mv` in a code half, at the start or after `;`, `&&`, `\|\|`, `\|`, `{`, `(` or `!`, or after the word `then`, `do` or `else` |
| its source | the first word after `mv` that does not open with `-` |
| scope | the innermost function whose span holds the line, by `FUNCTION_DEF` (`:628`) and its closing brace, as `read_function_bodies` finds them; else the top level |
| a binder | a function in the same file whose body holds `printf -v "$1"`; it admits when the body also holds a `SRANDOM` expansion or `mktemp`, and is fixed otherwise |
| the scope's table | in line order, each `;`, `&&` or `\|\|` segment: an `ASSIGNMENT` (`:146`) binds its name to its value, and `<binder> <name>` binds the name to that binder |
| follow | a source that is exactly one expansion, `"$n"`, `"${n}"` or `$n`, takes the latest binding of `n` in its scope; with none it is `unfollowed`, counted and printed, never gated |
| verdict | a binder binding takes the binder's verdict; a word or value holding `$(mktemp` or a `SRANDOM` expansion is admitted; anything else is a `fixed-temp` site |

The registry is `read_registry`'s grammar (`:384`), `<path>\tfixed-temp\t<count>\t<reason>`, with the
key shape `\Afixed-temp\Z`. `resolve_declaration` (`:421`) and `check_registry` (`:444`) give it
the optional argument's three states and set equality with counts. Every run prints the scanned
count, the `mv` count, and the fixed, admitted and unfollowed counts with their files. It prints
each registered row's reason, and lists `path:line  <source>` for each site of a failing key. The
remedy line names the three admitted forms. An empty population, a failed `git ls-files` and a
supplied registry that does not resolve each exit 2.

What it does not check, written into `run_temp_scan`'s docstring: a temp passed in as an argument
or bound in another scope (unfollowed); a binder in a sourced library; `mv` inside a quoted string,
under `eval` or split across a line continuation; a temp admitted by `$(mktemp)` in another
directory, whose `mv` is a copy and not a rename; a fixed name written without a `mv`, which is
§3's wider class; and Python inside a shell string.

| Selftest arm | Fixture | Expected |
|---|---|---|
| literal tail | `mv -f "$f.tmp" "$f"`, and `mv -f -- "$a.new" "$a"` | two sites |
| pid suffix | `mv "$x.tmp.$$" "$x"` | a site |
| one hop | `t="$WORK/owner.tmp"` then `mv -f "$t" "$WORK/owner"` | a site |
| `mktemp -u` | `t=$(mktemp -u "$f.XXXXXXXX")` then `mv -f "$t" "$f"` | admitted |
| `SRANDOM` | `t="$f.$SRANDOM$SRANDOM.tmp"` then `mv -f "$t" "$f"` | admitted |
| binder | a `derive_temp_path` body as above, then `derive_temp_path t "$f" && mv -f "$t" "$f"` | admitted |
| fixed binder | `fake() { printf -v "$1" '%s.tmp' "$2"; }` then `fake t "$f"; mv "$t" "$f"` | a site |
| scope | `t="$x.tmp"` in one function, `mv "$t" "$x"` in another | unfollowed, no site |
| loop rename | `for f in a.*; do mv -f "$f" "$f.bak"; done` in a function | unfollowed |
| comment and data | `# mv x.tmp x`, and the same line in a `<<'EOF'` body | no site |
| registry | `check_registry` with the mode's explained text over one undeclared key and one stale row | two findings |

The red half on today's tree: the mode, with no registry, over S7's population at `2aa18f2a3`
reports §4's 41 sites in 16 files.

### The registry's rows

| Path | Count | Reason |
|---|---|---|
| `.githooks/pre-push` | 2 | the bar-green stamp, git dir and common dir |
| `skills/session-kickoff/manifest-check.sh` | 3 | the `health_log_sh` trim; two card rewrites in its `mktemp -d` scratch |
| `tools/branch-reconcile/adopt-branch-reconcile.sh` | 1 | the rendered skill in the target |
| `tools/check-template-size.sh` | 1 | the high-water file, `.tmp.$$` |
| `tools/check-wiring.sh` | 2 | the `health_log_sh` trim; an EOL rewrite in the target |
| `tools/codebase-map/adopt-codebase-map.sh` | 1 | a rendered file in the target |
| `tools/lib/health-log.sh` | 1 | the canonical `health_log_sh` trim |
| `tools/memory-recall/adopt-memory-recall.sh` | 1 | the rendered skill in the target |
| `tools/memory-tree/adopt-memory-tree.sh` | 2 | a rendered file and the slot-limits file in the target |
| `tools/run-gates/run-gates.sh` | 1 | the `health_log_sh` trim |
| `tools/runlog/adopt-runlog.sh` | 1 | the rendered skill in the target |
| `tools/unattended/adopt-unattended.sh` | 1 | the conf rewrite in the target |
| `tools/unattended/lib-unattended.sh` | 1 | the `health_log_sh` trim |
| `tools/unattended/unattended.sh` | 2 | the bar-green stamp, git dir and common dir |

Every reason closes with "predates the lint; drained by deleting this row in the commit that fixes
it", and each `health_log_sh` row names `TOOL-aPairedSlots-10`.

### The new arm, and the order of the build

**The two runner hazards.** Bash reads a script by byte offset as it runs it, so editing
`run-gates.sh` or `run-selftests.sh` under a live run corrupts that run
(`memory/gotchas/suite-edited-while-bash-executes-it.md`). A commit under a bar moves its
fingerprint, and its verdict reads TREE MOVED. So before the first edit, the build pass reads
`$HOME/.gov/gate-turnstile` and the git dir's `gate-run/current` and runs no bar. A holder naming
this worktree defers the edit, and no bar starts from this worktree until `<p24>` is committed.
The second hazard is bash 5.3 on Cygwin segfaulting in one compound command past about 3000
commands (`tools/unattended/unattended.test.sh:2284-2290`). S1 is one line, and S2 to S4 add one
simple command per site and no compound command. Measured by an `awk` over column-0 openers and
closers at `2aa18f2a3`, the largest function is 312 lines (`fingerprint`) and the largest
top-level block 253. `run-selftests.sh`'s site sits in a 272-line block, and the canary's 9h in a
194-line subshell.

**Order 18**, one after unit 23's 17. Units 21 and 23 edit `tools/gate-legs.json` and re-stamp the
kickoff manifest, and this unit re-stamps after them; that is sequence, not an edge.
`.memory-tree.conf`, `run-gates.sh`, `run-selftests.sh` and `tools/gate-legs.json` are all on the
manifest's `watch:` line (`memory/guides/SESSION-KICKOFF.md:6`).

**KF3 at the close.** A diff that edits `run-gates.sh` makes the close's bar attribute every red to
this run (`memory/builds/aPairedSlots/RUN.md:18`). The main loop reads the attribution with that in
view.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `derive_temp_path` | a shell function in `run-gates.sh` | `sh.function`, `derive` |
| `run_temp_scan`, `scan_temp_file`, `scan_temp_tree` | functions in `sh_hygiene.py` | `py.function`, `run`, `scan` |
| `read_temp_binders`, `check_temp_source` | functions in `sh_hygiene.py` | `py.function`, `read`, `check` |
| `build_temp_measured`, `print_temp_populations` | functions in `sh_hygiene.py` | `py.function`, `build`, `print` |
| `--temp-names` | a mode flag | none |
| `fixed-temp` | a registry class key | none |
| `shell hygiene (a fixed-name temp renamed into place)` | a gate leg | none |
| `temp-name-sites.txt` | a registry under `memory/project/` | `PROJECT_REGISTRY_EXTRA` |
| `_tp` | the runner's temp variable, `local` in a function | none |

Each function name answered OK under `python tools/lexicon/lexicon.py --suggest <name> --as
<cell>` on 2026-10-15. A grep of the tree for every identifier above found none at `2aa18f2a3`.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/post-merge.sh`
- `tools/run-gates/run-selftests.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/gate-lint/sh_hygiene.py`
- `tools/gate-lint/kit.toml`
- `tools/gate-lint/README.md`
- `tools/gate-legs.json`
- `memory/project/temp-name-sites.txt`
- `.memory-tree.conf`
- `memory/map/features/gate-lint.md`
- `memory/map/generated/`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/dRedressedBar/build/`

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| `$(mktemp "<dest>.XXXXXXXX")` at every site, the brief's usual shape | five sites are per leg or per tick, the ticker forbids a fork (`:1681-1686`), and the fork ceilings would rise | Kept for S4's cold sites, as `mktemp -u` |
| `mktemp` without `-u` at S4's sites | it creates the file 0600 and the `>` reopens it by path, so two files read by the pre-push hook and the lander change mode, and a name exists before the write | Rejected |
| `set -C` with the fixed names | a planted entry is refused, so the planter can stop every heartbeat and record write | Rejected |
| Refusing to run on bash 5.0 | raises the runner's floor, which `EPOCHSECONDS` puts at 5.0 (`:1682-1684`) | Rejected; S1 falls back |
| The helper in a sourced library shared by the three scripts | fixtures copy `run-gates.sh` alone (`run-gates.test.sh:712`), and `lib-attribute.sh` is sourced only on the attribution path for that reason | Rejected; S4 uses the primitive |
| Fixing the five `health_log_sh` copies here | the block is byte-identical under a parity table across four kits, with a Python twin, and is ask `TOOL-aPairedSlots-10` | Registered (§3) |
| A check inside an existing leg | the gotcha prefers it, but every shell-hygiene leg is named for its own class, and a name that states a class is what the registry rows and the dossier claim | Rejected; S7 adds a leg |
| The class check as an arm inside the run-gates canary | its population would be the runner kit alone, so a fixed-name writer added in another kit passes | Rejected; S5 reads the tree |
| `*.test.sh` in the population | a suite's temps live in its own `mktemp -d` scratch, and the canary alone holds dozens of fixture writers | Rejected; the leg excludes suites as the spawn-idiom leg does |
| The static check as its own unit (M2) | the owner's ruling of 2026-10-15 names one unit for the fix and its gate | Followed the ruling |

## 5. Production-readiness checklist

- security — Closes H1's class for the four sites in `$WORK` (R4, R9, R10, R11): a link planted at
  their old names is never opened. The other 19 writers in the three scripts and the heredoc
  writer take the same names, so no temp they write can be known before it exists. What it does
  not check: §3's direct fixed-name writes, in `$WORK` and elsewhere, which a link still redirects;
  the 20 registered sites; a swap made between the write and the `mv`; and the gate's blind spots
  listed under the class gate. A fixed name written without a `mv` is not in its population.
- perf / scale — S1 runs two builtin expansions and a `printf -v`, and forks nothing on bash 5.1 and
  later. S4 adds one `mktemp -u` fork at each of three cold sites. The new leg reads 67 files, as
  the spawn-idiom leg does.
- error / empty / loading states — A helper that cannot name a temp leaves `_tp` empty, the `>`
  fails, and the site takes its existing failure branch: the same note, the same kept file. R11's
  `cp` fallback stays, and the temp is deleted after it.
- observability — Unchanged lines. The new leg prints its counts and each registered reason on
  every run.
- risks — A crash between write and rename leaves a `<dest>.<digits>.tmp` that nothing reuses. The
  run record's prune, the cache's prune and the beacon's removal sweep three of the directories,
  and the git dir's stamps are overwritten by name. The edit hazards and KF3 are §4's. A new leg
  ships to adopters through `[[gate_leg]]` with no registry argument, so an adopter's first run
  reds on every site it carries, the posture of the three sibling legs.
- testing — AC1 to AC10 are bash and python probes over extracted runner functions, the scanner run
  on the tree and on a `<pre>` clone, its `--selftest`, greps and `git` reads. The arms are §7's.
- migration — None. Old temps named `*.tmp` from an earlier runner are not read.
- user docs — `tools/gate-lint/README.md`'s new section, which is where the three earlier modes are
  documented. No `help/` page covers gate-lint, and a new page is a separate document (M2).

## 6. Acceptance criteria

`<p24>` is the product commit and `<p24m>` the manifest re-stamp, each named in the ledger. `<pre>`
is `<p24>~1`. `<rg>`, `<pm>` and `<rs>` are the three runner files, run-gates.sh, post-merge.sh and
run-selftests.sh under tools/run-gates/, spelled through placeholders because the spec-token
checker reads a backticked runner path as an invocation. `<sh>` is `python
tools/gate-lint/sh_hygiene.py`. `<t>` is a fresh dir under `%TEMP%`, and `<secret>` is
`<t>/secret.txt` holding `SECRET-TOKEN=abc123`. A file "over `<pre>`" is `git show <pre>:<path>`
written into `<t>`. A `<pre>` clone is a local `git clone` of gov under `%TEMP%`, checked out at
`<pre>`. Commands run from the worktree root on node d.

- **AC1** — A bash probe evaluates the one line `sed -n '/^derive_temp_path()/p'` prints from `<rg>`,
  then runs `set -x; derive_temp_path t "<t>/dest"` twice. Each value is `<t>/dest.<digits>.tmp`
  with digits alone between the dots, the two differ, no trace line opens with `++`, and `<t>`
  holds nothing. After `unset SRANDOM`, each value is `<t>/dest.<eight letters or digits>` and the
  two differ.
  Red when: a copy whose value is `<dest>.tmp` gives two equal names, and a copy whose first branch
  spells `$(` prints a `++` line.
- **AC2** — `<sh> --temp-names` with no registry, root `.` and the pathspecs `<rg>`, `<pm>` and `<rs>`
  exits 1. Its one failing key is `<rg>` with one site, the `$_hl_log.trim.$$` line in
  `add_health_event`. It prints one unfollowed source.
  Red when: `<p24>`'s scanner, run with root at a `<pre>` clone, names 19 sites in `<rg>`, 2 in
  `<pm>` and 1 in `<rs>`.
  figure: 19, 2 and 1 PINNED at `2aa18f2a3` on 2026-10-15; DERIVED at observation.
- **AC3** — `<sh> --temp-names` with S6's registry, root `.`, and the pathspecs `:!*.test.sh` and
  `:!memory/` exits 0. Its OK line counts 20 registered sites in 14 rows, and each row's reason
  prints. `grep -c 'temp-name-sites.txt' .memory-tree.conf` prints at least 1, on the
  `PROJECT_REGISTRY_EXTRA` line.
  Red when: the same run with no registry exits 1 with 20 sites in 14 files, and with root at a
  `<pre>` clone, 41 in 16.
  figure: 67 sources, 20 in 14 and 41 in 16, PINNED at `2aa18f2a3`; DERIVED at observation.
- **AC4** — `grep -nE '\$[A-Za-z_]+(/[A-Za-z0-9_.$-]*)*\.(tmp|trim|merged)'` over `<rg>`, `<pm>` and
  `<rs>` prints exactly two lines, both in `add_health_event` and spelling `$_hl_log.trim.$$`.
  Red when: over `<pre>` it prints 39 lines, 34 in `<rg>`, 2 in `<pm>` and 3 in `<rs>`.
  figure: 39 PINNED at `2aa18f2a3`.
- **AC5** — A bash probe builds `<t>/fn.sh` from `<rg>` with `sed -n
  '/^derive_temp_path()/p;/^ts_hb()/p;/^write_work_owner() {/,/^}$/p;/^write_spawn_floor() {/,/^}$/p'`,
  and appends `write_post_merge_record` from `<pm>`. It hard-links
  `<t>/w/owner.tmp`, `<t>/b/heartbeat.tmp`, `<t>/f/floor.tmp` and `<t>/c/gate-post-merge.tmp` to
  `<secret>`. It sources the file and calls each writer with `WORK`, `TS_DIR` and `CDIR` set to
  `<t>/w`, `<t>/b` and `<t>/c`, and `write_spawn_floor <t>/f/floor 1500`. Afterwards `<secret>`
  reads `SECRET-TOKEN=abc123`, each destination holds its writer's line, and each directory holds
  exactly the plant and the destination. Then `write_spawn_floor` onto a 250-character name in
  `<t>/g`, holding `9999.000` and a stamp, prints `could not be written` and leaves the line as it was.
  Red when: the same over `<pre>` leaves `<secret>` holding the last writer's line, with `stat -c %i`
  equal on `<secret>` and a destination, and the 250-character write succeeds.
- **AC6** — A python probe takes the program between `<rg>`'s line opening `' "$REUSE_CACHE"` and
  the nearest line above it ending `"$PYBIN" -c '`, which is `run-gates.sh:5462` at `2aa18f2a3`. It
  runs the program with argument
  `<t>/cache` and the stdin row `abcdef`, `3`, `r1`, `sha`, `1700000000`, `0`, tab-separated.
  `<t>/cache/ab/` lists exactly `abcdef`. With `<t>/cache2/ab/abcdef` made a directory, the run
  exits 0, and `<t>/cache2/ab/` lists exactly `abcdef`. `ast.parse` of the program finds a
  `tempfile.mkstemp` call with a `dir` keyword and no `getpid`.
  Red when: over `<pre>`, the directory case leaves `abcdef.tmp.<pid>` in `ab/`, and the program
  calls `os.getpid`.
- **AC7** — `<sh> --selftest` exits 0, and its printed assertion count is at least the raised
  `FLOOR_ASSERTIONS`. Each arm in §4's selftest table runs.
  Red when: a copy with the one-hop follow taken out passes the one-hop fixture, and a copy that
  treats every `printf -v "$1"` function as admitting passes the fixed binder.
- **AC8** — A python program loads `tools/gate-legs.json`. One row's argv carries `--temp-names`,
  `temp-name-sites.txt`, `.`, `:!*.test.sh` and `:!memory/`, with chunk `product`, subject `repo` and
  no guard. Its name is the name of a `[[gate_leg]]` in `tools/gate-lint/kit.toml` whose argv is
  `["python3", "{kit}/sh_hygiene.py", "--temp-names"]`. The dossier `memory/map/features/gate-lint.md`
  lists it under `gate-legs`, and `tools/gate-lint/README.md` carries a `--temp-names` heading.
  Red when: at `<pre>` no row's argv carries `--temp-names`.
- **AC9** — `grep -cF '/^derive_temp_path()/p' tools/run-gates/run-gates.turnstile.test.sh` prints 1.
  `grep -c 'derive_temp_path _tp "$_gcd_abs/gate-full-green.shared"'` over `<rg>` prints 1.
  `grep -c 'gate-full-green.shared.tmp' tools/run-gates/run-gates.runlog.test.sh` and
  `grep -c 'held.tmp' tools/run-gates/run-gates.test.sh` each print 0.
  Red when: at `<pre>` the first two print 0 and the last two print at least 1.
- **AC10** — `git log -1 --format=%B <p24m>` carries `manifest-audit:`. The `last-audit:` line of
  `memory/guides/SESSION-KICKOFF.md` names a commit at which `git show <sha>:tools/gate-legs.json`
  carries `--temp-names`. `git diff --name-only <p24>~1 <p24> -- memory/builds/dRedressedBar/spec/`
  names no spec but this one. The ledger S10 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-24`.
  Red when: the stamp names a commit before `<p24>`, `<p24m>` carries no `manifest-audit:`, or the
  build pass writes another spec.

## 7. Gates

`measure-legs selftest` · `run-selftests self-test` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` · `run-gates run-log line` · `run-gates evidence` · `shell-hygiene selftest` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `spawn budget (forks per hot entrypoint)` · `kit/dogfood doc parity` · `straggler-guard arms` · `transition-audit arms` · `recall floor` · `recall floor arms` · `kickoff-manifest ratchet` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `testsuite counts (every bar self-test prints one)`

The line is a floor. It joins §4 Files touched against the guards in `tools/gate-legs.json` with
`BROAD_LEG_FLOOR` (`tools/check-spec-tokens.py:262`) applied. That owes `measure-legs selftest`,
`run-selftests self-test`, the two canaries, `shell-hygiene selftest`, the four legs guarded by
`.memory-tree.conf` and `recall floor arms`. It adds the suites S8 and S9 edit, the unguarded
shell-hygiene, fork, manifest, record, naming, map, kit and resolver legs the change moves, and the
suite counts. The leg S7 adds, `shell hygiene (a fixed-name temp renamed into place)`, joins this
line in a revision once its manifest row exists, as unit 18 did for its leg.

New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC7 · the `--temp-names` arms over a copy with the one-hop follow, the function scope and the binder test each taken out · raise `FLOOR_ASSERTIONS` from 81 to the count printed
New arm: tools/run-gates/run-gates.test.sh · covers AC5 · 9e2 over `<pre>`'s runner, where leg 0's hard links at `$WORK/0.rc.tmp` and `$WORK/ledger.merged` carry the rc and the ledger rows into the secret · raise `FLOOR_ASSERTIONS` from 401 by 4
New arm: tools/run-gates/run-gates.test.sh · covers AC5 · 9h's write failure on a 250-character floor name, over `<pre>`'s runner, where the write succeeds and the held line moves · none
New arm: tools/run-gates/run-gates.runlog.test.sh · covers AC9 · TWO over `<pre>`'s runner, where the helper's call finds no statement · none
New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC9 · R6 with `/^derive_temp_path()/p` taken out of its `sed`, so `heartbeat` stays unwritten · raise `FLOOR_ASSERTIONS` from 144 to 145

The main loop observes each arm red, then green, at the close, and runs the bar once after the
last unit is terminal.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-15 · initial draft, from the owner's resolution of `TOOL-dRedressedBar-21` F1 as (a)
  on 2026-10-15. Enumerated from the tree at `2aa18f2a3`: 22 `mv` sites in the three runner files
  against the brief's 19, plus the heredoc writer. The health log's trim is registered on the
  precedent of `TOOL-aPairedSlots-7`. The hot sites take a builtin `$SRANDOM` name, because the
  ticker forbids a fork and the fork ceilings hold the runner. The gate is a fourth `sh_hygiene.py`
  mode over every tracked product shell source, with 20 registered sites in 14 files.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "write a shell file through an unpredictable temp name
and rename it into place"` ranked name-stem neighbours only (`write`, `write_text`, `write_record`,
`write_bar_green`), with no temp writer. `python tools/codebase-map/reuse_lookup.py "static scan of
shell sources that reds a new spelling against a shrink-only registry"` ranked `scan` and
`load_registry`, both name stems. Each miss is recorded as a miss. The seam this unit extends was
found by reading the code and the dossier: `tools/gate-lint/sh_hygiene.py`, whose dossier names
`sh_hygiene.scan_file` as the reuse affordance for a per-line shell classifier
(`memory/map/features/gate-lint.md:168`). S5 reuses `read_shell_sources`, `read_code_lines`,
`read_function_bodies`, `ASSIGNMENT`, `FUNCTION_DEF`, `read_registry`, `resolve_declaration` and
`check_registry`, and adds only the predicate. S7 follows the spawn-idiom leg's three declarations,
and S6 follows `spawn-idiom-sites.txt` and its `PROJECT_REGISTRY_EXTRA` member. S1 follows the
runner's builtin-with-fallback pattern for `EPOCHREALTIME` (`run-gates.sh:2405`) and its one-line
helpers at column 0 that arms extract with `sed` (`ts_alive`, `run-gates.turnstile.test.sh:382`).
S3 follows unit 21's `write_replace`. S9 reuses the canary's `build_hv_repo` and `run_hv_bar`, and
S10 follows `809f794e4` and `cafbbc460`.

The recall probe returned unit 21's spec and F1, H1's record, `TOOL-aTetheredScratch-1` and `-2` on
the temp dir sitting under `$HOME`, and `TOOL-aPairedSlots-5`'s shared-path audit. That audit's
table classifies the runner's `owner` and green-stamp writers and defers the health log's trim to
ask `TOOL-aPairedSlots-10`, which §3 follows. The record and the code agree on every citation
re-read.

The gotchas this unit's paths select, each answered here. `suite-edited-while-bash-executes-it`
is the first runner hazard, under "The new arm, and the order of the build". The canary's
compound-block ceiling is the second, answered by S1 being one line. Under
`fixture-passes-by-finding-nothing`, AC3 and AC7 assert non-empty populations, AC5 checks each plant
still exists, and S9's arm checks its marker. Under `a-new-leg-trips-a-growing-set-of-meta-gates`,
§7 names the kit descriptor, the dossier claim, the registry admission and the suite floors. Under
`guard-above-a-fold-makes-its-fallback-dead`, AC1 exercises the fallback branch by unsetting
`SRANDOM`.

Recall terms used: `python tools/memory-recall/query.py "how should a shell script write a file
through a temp name another process cannot plant a link at, and how is a fixed temp name gated"
--terms "mktemp SRANDOM tmp mv rename planted hard link symlink WORK TMPDIR sh_hygiene registry
fork"`

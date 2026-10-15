# TOOL-dRedressedBar-26 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-26

This is the build pass of the round-2 closing diff review's temp-name batch, report ids 22, 6, 7,
10, 21, 8, 19 and 13, built from spec 26 rev-1. `<w26>` is `3e2f387a6`, the spec-writer pass that
corrected spec 24. `<p26>` is `f8bbdc85d`, the product commit, and `<p26m>` is `db2303a86`, the
kickoff-manifest re-stamp at it. `<pre>` is `3e2f387a6`, the code the build pass started from, whose
`tools/gate-lint/` equals `5b30e4b47`'s.

The product commit changes the temp-name mode of `sh_hygiene.py` and its selftest, the kit README's
`--temp-names` section, the gate-lint dossier's line, the reuse-cache writer's interpreter flags in
the runner, and the runlog suite's TWO arm and floor, and re-stamps the kickoff manifest at its
parent. The build README's rows and `memory/LIVE.md` came from `gen_build_index.py --write` over
spec 26's dispatched INPROGRESS header, committed with them. No function was minted, so the symbol
index did not move. The pre-commit hook's staged legs, memory hygiene and the manifest ratchet among
them, passed both commits. Before the first edit the gate turnstile's queue was empty, the common
dir's `gate-run/current` named an October 9 push run, and no runner process was alive.

No merge bar, gate leg or self-test suite was run by this pass, and no arm of `sh_hygiene.py
--selftest` or of the runlog suite was called: the new arms were compiled and read, never executed,
so the close's runs are their first execution. The floor of 125 is counted off the arms, 92 before
and 33 added, every one unconditional. The naming lexicon answered OK over the tree.

Every criterion was observed by a direct probe written apart from the arms, on node d under Python
3.12.10 and MSYS bash 5.3.9. Each probe loaded `sh_hygiene` from the worktree, or from `<pre>`'s copy
written under the session scratchpad. Each scratch repository and planted directory sat under
`%TEMP%` and was removed after.

**Evidences:** TOOL-dRedressedBar-26
- AC22 — `LC_ALL=C` — `scan_temp_file` read `([1], 0, 0)` for each of `command mv`, `builtin mv`,
  `exec mv`, `LC_ALL=C mv -f` and `A=1 B="x y" mv -f`, each over `"$f.tmp" "$f"`, and `([], 0, 0)`
  for `echo then mv x.tmp x`. `scan_temp_tree` over `.` with `:!*.test.sh` and `:!memory/` read 68
  sources, 49 `mv`, 20 fixed sites in 14 files, 28 admitted and 1 unfollowed, and
  `build_temp_measured` equalled `read_registry` over `memory/project/temp-name-sites.txt`, 20 sites
  in 14 rows. Red: over `<pre>` each of the five read `([], 0, 0)`, and the `echo then` text read
  `([1], 0, 0)`. The leg's own run and its OK line are owed to the close below.
- AC6 — `TEMP_KEYWORDS` — `scan_temp_file` read `([1], 0, 0)` for the `if`, `elif`, `while` and
  `until` texts. An `ast` walk found the module-level assignments to `TEMP_MV` and `TEMP_LEAD` each
  holding the name `TEMP_KEYWORDS` and no string constant spelling `elif`. For each of the seven
  words `TEMP_LEAD.match(word + " t=x").end()` equalled `len(word) + 1`. Red: over `<pre>` the four
  read `([], 0, 0)`, neither assignment holds `TEMP_KEYWORDS`, and `TEMP_LEAD`'s one string constant
  spells the seven words.
- AC7 — `rename_into()` — `scan_temp_file` read `([], 0, 1)` for `rename_into() { mv -f "$1" "$2"; }`,
  the four-line `local src=$1` function, `h() { mv -f "${1}" "$2"; }` and `h() { mv -f "$@"; }`,
  and `([1], 0, 0)` for `mv "$1.tmp" "$1"`. Red: over `<pre>` the first two read `([1], 0, 0)` and
  `([3], 0, 0)`.
- AC10 — `TEMP_REMEDY` — with `SRANDOM` unset in the shell, `t="$f.$SRANDOM$SRANDOM.tmp"` over
  `f=/x/d` printed `/x/d..tmp`. `scan_temp_file` read `([2], 0, 0)` for the bare form and for the
  unguarded `dt()` binder, and `([], 1, 0)` for the runner's own `derive_temp_path()` line, read out
  of `run-gates.sh`, then its call and `mv`. `TEMP_REMEDY` carries `mktemp -u` and `${SRANDOM:-`
  and no `$SRANDOM$SRANDOM`. The README's `--temp-names` section, joined, carries no
  `$SRANDOM$SRANDOM`, and `grep -c 'three admitted forms'` over the dossier prints 0. Red: over
  `<pre>` the bare form and the unguarded binder each read `([], 1, 0)`, and its `TEMP_REMEDY`
  carries `$SRANDOM$SRANDOM`.
- AC21 — `TEMP_BOUNDARY` — `scan_temp_file` read `([], 0, 1)` for the three-line two-hop text and
  `([1], 0, 0)` for `command mv "$x.tmp" x`. `TEMP_BOUNDARY` holds 13 rows, and each row's example
  landed in its class alone, six unfollowed, five unread, one admitted and one fixed. Each label sat
  in `run_temp_scan.__doc__`, joined, and in the README's `--temp-names` section, cut from its
  heading to the next `## ` line and joined. The docstring carries `false red` and no
  `never a false red`. Red: over `<pre>` the two-hop text read `([3], 0, 0)`, `command mv` read
  `([], 0, 0)`, the module holds no `TEMP_BOUNDARY`, and the docstring carries
  `each a MISS and never a false red`.
- AC8 — `tempfile.py` — a python program read `run-gates.sh`, found the line opening
  `' "$REUSE_CACHE"` and the nearest line above it ending `-c '`, `"$PYBIN" -I -c '`, and took
  the flags between `"$PYBIN"` and `-c`, `['-I']`. Run by `sys.executable` with those flags, `-c`,
  the program and `<t>/cache`, in a cwd holding a `tempfile.py` that raises `SHADOWED`, with the
  stdin row `abcdef 3 r1 sha 1700000000 0` tab-separated, it exited 0 and `<t>/cache/ab/` listed
  exactly `abcdef`. Red: the same run with no flags, as at `<pre>`, into `<t>/cache2`, exited 1
  printing `SHADOWED`, and `<t>/cache2/ab/` did not exist.
- AC19 — `unset SRANDOM` — `sed -n "s/^  stg='\(.*\)'$/\1/p"` over the runlog suite printed
  `^gate-full-green\.shared\.`. Over a directory holding `gate-full-green.shared`,
  `gate-full-green.shared.1234567890.tmp` and `gate-full-green.shared.AbCd1234`, `ls | grep -c` over
  that pattern printed 2. The runner's `derive_temp_path()` line matched, by `grep -cxF`, the
  literal whose `else` branch is `mktemp -u "$2.XXXXXXXX"`; that command over
  `$TEMP/gate-full-green.shared` printed `gate-full-green.shared.c0WHdM2s`, which the pattern
  matched. `sed -n '/^check_two_writers()/,/^}/p'` piped to `grep -c 'unset SRANDOM'` printed 5,
  and `grep -c '^FLOOR_ASSERTIONS=230$'` printed 1. Red: the pattern as at `<pre>`,
  `^gate-full-green\.shared\..*\.tmp$`, counted 1 of the planted pair and did not match the
  `mktemp` name. The helper run whole in a shell with `unset SRANDOM` was refused by the session's
  isolation hook, whatever its spelling, so the shipped helper's own run on that branch is the
  close's TWO arm.
- AC13 — `1 finding(s)` — with `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE` held out, a scratch
  repository whose one tracked file `t.sh` holds `mv -f "$f.tmp" "$f"` and the registry row `t.sh`,
  `fixed-temp`, `2`, `drifted` gave `sh_hygiene.py --temp-names <t>/reg.txt <t>/r` exit 1 and the
  line `sh-hygiene: 1 finding(s).`, and that one finding carries `the scan measures 1` and, on its
  next line, `t.sh:1`. `inspect.signature(check_registry)` names `measured`, `declared`,
  `explained` and `listing`. Red: over `<pre>` the same run printed `2 finding(s)`, the second
  naming the one `fixed-temp` site the scan measures, with the listing under it.
- AC24 — `manifest-audit:` — `git diff 3e2f387a6~1 3e2f387a6` under the spec dir shows spec 24,
  CLOSED at `<w26>~1`, with one header rev change, rev-1 to rev-2, one new revision line naming
  `TOOL-dRedressedBar-26` and ids 22, 6, 7, 10, 21, 8 and 19, and a §3 bullet `hands-off`
  `TOOL-dRedressedBar-26`; spec 26 moves there only in its generated records rows. `git diff
  --name-only` over `<p26>` under `memory/builds/dRedressedBar/spec/` names this spec alone, for
  its dispatched header, and over `<p26m>` names nothing. `git log -1 --format=%B db2303a86`
  carries one `manifest-audit:` line, and the `last-audit:` line of
  `memory/guides/SESSION-KICKOFF.md` names `f8bbdc85d`, at which `run-gates.sh` carries
  `"$PYBIN" -I -c` once. This ledger carries `**Serves:** journal TOOL-dRedressedBar-26`.

## Owed to the close

The section 7 gates, run once by the main loop as the bar. `shell-hygiene selftest` is the first
execution of the 33 new assertions and the check of the floor of 125 against the count it prints;
`run-gates run-log line` is the first execution of TWO's four new checks and the floor of 230; and
`shell hygiene (a fixed-name temp renamed into place)` is AC22's leg run and its OK line, 20
registered sites in 14 rows. And the RED-first observation of the five `New arm:` lines: the
lead-word arm and the `if`, `LC_ALL=C` and `command` rows over a copy whose `TEMP_MV` is `<pre>`'s
(AC22, AC6); the two positional rows, the two-hop row and the boundary arm over a copy whose follow
step is `<pre>`'s, and the boundary arm again with one label taken out of `run_temp_scan`'s
docstring (AC7, AC21); the `SRANDOM` row and the unguarded-binder row over a copy whose
`TEMP_UNPREDICTABLE` and binder test are `<pre>`'s (AC10); the one-line-per-key unit row and the
scratch-repository run over a copy whose `run_temp_scan` appends its second mismatch line (AC13);
and TWO with its leftover pattern as at `<pre>` (AC19). The boundary arm reads `README.md` beside the
scanner it runs from, so a staged copy without the README beside it reds every boundary row on the
README half, not on the staged break.

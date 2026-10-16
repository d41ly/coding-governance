# TOOL-dRedressedBar-24 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-24

This is the build pass of spec 24 rev-1: the bash half of H1's class, which unit 21's F1 handed to
this unit. `<p24>` is `73b80ed31`, the product commit, and `<p24m>` is `be022852d`, the
kickoff-manifest re-stamp at it. `<pre>` is `b7d685c0d`, unit 23's closing commit. The three runner
files, their three suites and `tools/gate-lint/sh_hygiene.py` are byte-identical at `2aa18f2a3` and
at `<pre>`, so every line the spec cites held until this pass. No bar ran from this worktree while it
was edited: the turnstile had no holder and the git dir had no `gate-run/current`.

The product commit changes the three runner files, the three suites, the gate-lint scanner, its
descriptor and README, the leg manifest, the subject pin, the new registry, the memory-tree conf and
the gate-lint dossier, and re-stamps the kickoff manifest at its parent.
`memory/map/generated/` came from `gen_map.py --write`, run alone, and the build README's rows and
`memory/LIVE.md` from `gen_build_index.py --write` over spec 24's dispatched INPROGRESS header,
committed with them. The pre-commit hook's staged legs, memory hygiene and the manifest ratchet among
them, passed both commits.

No merge bar, gate leg or self-test suite was run by this pass. The `--temp-names` mode was run over
the tree, which AC2 and AC3 name as their observation; no bar has run its leg yet.
`sh_hygiene.py --selftest` was not run: its eleven new arms were classified by a direct probe that
rebuilt the fixture table from the selftest's own source and called `scan_temp_file` and
`check_registry`, so the close's `shell-hygiene selftest` run is their first execution. The canary's
9e2 and 9h, the runlog suite's TWO and the turnstile suite's R6 were parsed with `bash -n` and never
run; R17's statement and R3's ticker were probed directly, apart from the arms. The naming lexicon
answered OK for `derive_temp_path` as `sh.function` and for the seven new Python functions as
`py.function`.

Every criterion was observed on node d, Windows, under bash 5.3.9 (MSYS) and Python 3.12.10. `<t>` is
a fresh directory under the session scratchpad, itself under `%TEMP%`. A red half "at `<pre>`" read
the files of a local `git clone` of gov under `%TEMP%`, checked out at `<pre>`. The mode's positional
grammar puts the registry first, so a run "with no registry" over a root and pathspecs passed an
empty registry file, which `resolve_declaration`'s docstring states grades byte-identically to an
absent argument; only the line naming the posture differs. The tip's tree holds 68 shell sources
where the spec counted 67 at `2aa18f2a3`: unit 19 added `fixtures/measure-legs/orphan.sh`, which
holds no `mv`.

**Evidences:** TOOL-dRedressedBar-24
- AC1 — `<t>/dest.<digits>.tmp` — the one line `sed` printed from the runner, evaluated alone and
  called twice under `set -x`, set two values of that shape that differ; the trace held 7 lines,
  none opening `++`, and `<t>` held nothing. After `unset SRANDOM` the two values were
  `<t>/dest.` plus eight letters or digits, they differ, both calls returned 0, and `<t>` still
  held nothing. Red: a copy whose format is `'%s.tmp'` named equal temps, and a copy whose first
  branch spells `$(` printed 2 `++` lines in a 9-line trace.
- AC2 — `$_hl_log.trim.$$` — the mode with no registry, root `.` and the three runner files read 3
  sources and 23 `mv` commands, and exited 1 on one key, `run-gates.sh`, with one site, its line
  766 in `add_health_event`. It printed one unfollowed source, `"$f"` at the retry-to-tail rename,
  and counted 21 admitted. Red: the same scanner with root at the `<pre>` clone named 19 sites in
  `run-gates.sh`, 2 in `post-merge.sh` and 1 in `run-selftests.sh`, and none admitted.
- AC3 — `PROJECT_REGISTRY_EXTRA` — the mode with `memory/project/temp-name-sites.txt`, root `.` and
  the two exclusions read 68 sources and 49 `mv` commands and exited 0. Its OK line counts 20
  registered sites in 14 rows, and each row's reason printed. 28 sites in 5 files were admitted.
  `grep -c 'temp-name-sites.txt' .memory-tree.conf` printed 2: the `PROJECT_REGISTRY_EXTRA` line,
  and the comment above it naming the ninth member. Red: the same run with no registry exited 1
  with 20 sites in 14 files, and with root at the `<pre>` clone 41 sites in 16 files.
- AC4 — `add_health_event` — the criterion's `grep -nE` over the three runner files printed two
  lines, 766 and 767 of `run-gates.sh`, both in `add_health_event` and both spelling
  `$_hl_log.trim.$$`. Red: in the `<pre>` clone it counted 34 in `run-gates.sh`, 2 in
  `post-merge.sh` and 3 in `run-selftests.sh`, 39 lines.
- AC5 — `write_post_merge_record` — `<t>/fn.sh`, built by the criterion's `sed` and the appended
  writer, defined the helper, `ts_hb`, `write_work_owner`, `write_spawn_floor` and
  `write_post_merge_record`. With the four plants hard-linked to the secret (5 links), each writer
  returned 0. The secret still read `SECRET-TOKEN=abc123`, and each destination held its writer's
  line under an inode of its own. Each of the four directories held exactly the plant and the
  destination. `write_spawn_floor` onto a 250-character name holding `9999.000` and a stamp printed
  `could not be written`, left the line byte-identical, and left one entry in its directory. Red,
  over the `<pre>` clone's two scripts: the secret held the post-merge record, the last writer's
  line, and `stat -c %i` read one inode for the secret and all four destinations. The
  250-character write succeeded and the held line moved to `1.500`.
- AC6 — `tempfile.mkstemp` — the program between the opener line and the nearest line above it
  ending the `-c` quote, 31 lines, exited 0 with argument `<t>/cache`. `ab/` listed `abcdef`
  alone, reading the row's four fields and `0`. With `<t>/cache2/ab/abcdef` a directory it exited
  0, and `ab/` listed `abcdef` alone. `ast.parse` found one `tempfile.mkstemp` call with a `dir`
  keyword and no `getpid`. Red: over the `<pre>` clone's program, the directory case left
  `abcdef.tmp.20356` beside it, and the program references `getpid` once.
- AC7 — `FLOOR_ASSERTIONS` — the selftest's ten fixture cases, rebuilt from its source, each read
  as the table says through `scan_temp_file`. The registry arm's `check_registry` call returned
  two findings, the first equal to the mode's undeclared text and the second a stale-row line.
  `FLOOR_ASSERTIONS` reads 92, 81 plus the 11 new unconditional assertions, counted off the arms.
  Staged on in-memory copies: with the one-hop follow taken out, 5 of the 10 cases turn, the
  one-hop and fixed-binder cases among them. With the function scope taken out, the scope case
  turns, and a copy that admits every `printf -v "$1"` binder turns the fixed binder. The
  `--selftest` run and its printed count are owed to the close.
- AC8 — `tools/gate-legs.json` — one row's argv carries `--temp-names`, the registry path, `.`,
  `:!*.test.sh` and `:!memory/`, with chunk `product`, subject `repo` and no guard. Its name,
  `shell hygiene (a fixed-name temp renamed into place)`, is a `[[gate_leg]]` in the gate-lint
  descriptor whose argv is `["python3", "{kit}/sh_hygiene.py", "--temp-names"]`, subject `repo` and
  guard empty. The dossier lists it under `gate-legs`, and the kit README carries a `--temp-names`
  heading. `tools/govkit/subject-pins.tsv` equals the body rebuilt from the manifest, 142 rows.
  Red: at the `<pre>` clone no row's argv carries `--temp-names`, and the README has no such
  heading.
- AC9 — `grep -c 'held.tmp' tools/run-gates/run-gates.test.sh` — printed 0, and the runlog suite's
  count of the old shared-green staging name printed 0. The turnstile suite's fixed-string count
  of the helper's `sed` address printed 1, and the runner's count of the shared-green helper call
  printed 1. Red: at the `<pre>` clone those four printed 1, 1, 0 and 0. R17's statement, extracted
  from its helper call to the first line that does not continue and run with the helper line
  prepended, stamped a whole `gate-full-green.shared` and left nothing else. Run after a failed
  `cp`, it left the common dir empty.
- AC10 — `manifest-audit:` — `git log -1 --format=%B be022852d` carries one `manifest-audit:` line,
  and so does `73b80ed31`'s body. The `last-audit:` line of `memory/guides/SESSION-KICKOFF.md`
  names `73b80ed31`, whose `tools/gate-legs.json` carries `--temp-names` once; `<pre>`'s carries
  it nowhere. `git diff --name-only` over `<p24>` under `memory/builds/dRedressedBar/spec/` names
  this spec alone, for its dispatched header, and over `<p24m>` names nothing. This ledger carries
  `**Serves:** journal TOOL-dRedressedBar-24`.

## Owed to the close

The section 7 gates, run once by the main loop as the bar, and the new leg
`shell hygiene (a fixed-name temp renamed into place)` with them. Its manifest row exists from
`<p24>` on, so the section 7 line owes the revision the spec names, which is the spec writer's
edit and not this pass's. And the RED-first
observation of the five `New arm:` lines: the `--temp-names` selftest arms (AC7), the canary's 9e2
over `<pre>`'s runner (AC5), 9h's 250-character floor over `<pre>`'s runner (AC5), the runlog
suite's TWO over `<pre>`'s runner (AC9), and R6 with the helper taken out of its `sed` (AC9). TWO
counts leftovers by the spec's `gate-full-green.shared.*.tmp` shape, which the helper's bash 5.0
`mktemp -u` names do not take, so on bash 5.0 that one count cannot see a leftover. The three
floors rise to 92, 405 and 145, each counted off its arms and not read off a run.

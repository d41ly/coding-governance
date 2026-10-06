# The vague-brief arm — the brief, the full brief it was cut from, and the held-out decisions

**Serves:** journal TOOL-aMendedFleet-73

What every cell of this unit's trial is handed, and what only the graders see. The builders receive
the VAGUE brief below and nothing else from this file. The hidden suite is written from the FULL
brief, the probe agents work from the DECISION LIST, and the blind scorers read the probes'
observations against the full brief. The harness beside this file freezes the sha256 of the decision
list before any arm runs, so a row edited after the arms ran is a hash mismatch rather than a quiet
re-grading.

## The vague brief, verbatim — byte-identical to the spec's section 4

> Our kits live as subdirectories of `tools/`, and a `kits.toml` at the repository root lists them
> as `[[kit]]` rows, each with a `name` and a `path`. Write `declared.py`, a Python 3
> standard-library-only checker we can run as a merge-bar leg, that tells us when the directories and
> the registry have drifted apart. A few kits are deliberately unlisted, so give us a way to exempt
> them.

It pins only what any test needs in order to reach the tool: the file name `declared.py`, the
registry `kits.toml` with its `[[kit]]` rows carrying `name` and `path`, and the `tools/` directory.

## The full brief it was cut from — Task A of the first trial, copied from its briefs journal

The source is `memory/builds/aBlindedTrial/build/2026-09-20-build-TOOL-aBlindedTrial-1-briefs.md`,
section "Task A", copied byte for byte except that its headings sit one level lower. The first trial's `fixtures/` directory did not survive and
is not part of this arm: no cell receives fixtures.

### Task A — `declared.py`: a declared-population checker

Build `declared.py`, a Python 3 standard-library-only command-line checker, in this directory.

#### What it is for

A tools directory holds "kits" as subdirectories. A registry file declares which kits exist. The
checker asserts that the two agree in BOTH directions: a kit directory nobody declared is a finding,
and a declaration naming a directory that does not exist is a finding. It is meant to run as a
merge-bar leg, so its exit codes and its output lines are contracts.

#### Inputs

- `kits.toml` at the root of the tree being checked: a TOML file with an array of tables `[[kit]]`,
  each carrying `name` (string) and `path` (string, relative to the tree root, forward slashes).
- The tools directory: `tools/` under the tree root. Every immediate subdirectory of `tools/` is a
  kit.
- Optional `waivers.txt` beside `kits.toml`: one relative path per line; blank lines and lines
  starting with `#` are ignored. A waived path is an undeclared kit directory that is allowed to stay
  undeclared.

#### Behaviour

- `python declared.py [--root DIR] [--preview]` — `--root` defaults to the current directory.
- Exit 0 when every kit directory is declared (or waived) and every declaration names an existing
  directory. Print nothing on exit 0 except a single summary line.
- Exit 1 on any finding. One line per finding on stdout, each starting with exactly one of three
  tokens:
  - `UNDECLARED <path>` — a kit directory with no `[[kit]]` row and no waiver;
  - `MISSING <name> <path>` — a `[[kit]]` row whose path is not an existing directory;
  - `STALE-WAIVER <path>` — a waiver row that no longer waives anything, because its path is
    declared or does not exist. A stale waiver is a finding because an exemption that has outlived
    its reason silently widens the surface it was written to narrow.
- Exit 2 on misconfiguration: no `kits.toml`, unparseable TOML, a `[[kit]]` row missing `name` or
  `path`, or `--root` not a directory. Say what is wrong on stderr.
- `--preview` prints the same finding lines but always exits 0 when the tree could be read. It exists
  so a candidate predicate can be run over a real tree before the leg is wired. Findings are never
  suppressed.
- Output must be deterministic: same tree, same bytes.

#### Constraints

- Python 3.11+, standard library only. One file. Runs on Windows and POSIX.
- `fixtures/` in this directory shows one clean tree and one tree with findings. They are examples,
  not the acceptance suite.

## The decision list — what the full brief pins and the vague brief leaves open

One row per behaviour. A probe agent turns each row into a command against a tool's OWN interface,
discovered from the tool's source and `--help`, never from the full brief's spellings: a tool that
spells its exemption file `exempt.txt` meets D6 if exemptions live in a file beside the registry,
one path per line. The probe hint says what to build and what to observe.

| D | the full brief pins | probe hint |
|---|---|---|
| D1 | exit 0 on a clean tree | a tree whose every `tools/` subdirectory is declared and every row's path exists; observe exit status |
| D2 | a non-zero exit on any finding | add one undeclared `tools/` subdirectory to the clean tree; observe exit status |
| D3 | a misconfiguration exit distinct from a finding exit | compare the exit of an unparseable `kits.toml` against the exit of one undeclared kit |
| D4 | an undeclared kit directory is a finding naming its path | one undeclared `tools/zeta/`; observe whether output names `tools/zeta` |
| D5 | a declared path that is not a directory is a finding naming the kit | a `[[kit]]` row whose path does not exist; observe whether output names that row's `name` |
| D6 | exemptions live in a file beside the registry, one path per line | read the tool's own exemption mechanism; observe whether it is a file next to `kits.toml` holding one path per line |
| D7 | a blank line and a `#` line in that file are ignored | add a blank line and a `# note` line to the exemption file of a clean exempted tree; observe the exit is unchanged |
| D8 | an exemption that no longer exempts anything is itself a finding | exempt a path that does not exist, and separately a path that is declared; observe a finding for each |
| D9 | a non-failing preview mode prints the same findings | find the tool's preview or report-only mode on a tree with findings; observe exit 0 and the same finding lines |
| D10 | the tree to check can be named, defaulting to the current directory | run the tool from outside the tree, naming it by the tool's own option; then from inside with no option |
| D11 | one line per finding, on stdout | a tree with two findings; observe exactly two finding lines on stdout and none of them only on stderr |
| D12 | the same tree gives the same bytes | run twice on a tree with three findings created in a different order; compare stdout bytes |
| D13 | only immediate subdirectories of `tools/` are kits | add `tools/a/b/` under a declared `tools/a/` and a plain file `tools/readme.txt`; observe no finding |
| D14 | an unparseable registry or a row missing a field is a misconfiguration, explained on stderr | a `kits.toml` that is not TOML, then a row with no `path`; observe the misconfiguration exit and a stderr message for each |
| D15 | a missing `kits.toml` is a misconfiguration | delete the registry; observe the misconfiguration exit, not a clean pass and not a finding exit |
| D16 | a named tree that is not a directory is a misconfiguration | name a file, then a nonexistent path, as the tree; observe the misconfiguration exit |
| D17 | a clean run prints at most a single summary line | the clean tree; observe at most one line of output |
| D18 | a declared row is matched by its path, never by its name | a row `name = "alpha"`, `path = "tools/a"` with `tools/a/` present; observe no finding |

D1 to D14 are the floor the spec's section 4 set; D15 to D18 are added from the full brief, which
the spec allows. No row was removed.

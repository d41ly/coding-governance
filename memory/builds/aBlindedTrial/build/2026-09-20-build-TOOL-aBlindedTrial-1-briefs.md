# The three briefs, verbatim — what every arm of the trial was given

**Serves:** journal TOOL-aBlindedTrial-1

Each brief below is the exact `brief.md` every cell received, with the example fixtures under
`fixtures/` beside it. The hidden suites, the probes and every arm read these and nothing else. The
headings are demoted one level so the three sit under one record.

---

## Task A — `declared.py`: a declared-population checker

Build `declared.py`, a Python 3 standard-library-only command-line checker, in this directory.

### What it is for

A tools directory holds "kits" as subdirectories. A registry file declares which kits exist. The
checker asserts that the two agree in BOTH directions: a kit directory nobody declared is a finding,
and a declaration naming a directory that does not exist is a finding. It is meant to run as a
merge-bar leg, so its exit codes and its output lines are contracts.

### Inputs

- `kits.toml` at the root of the tree being checked: a TOML file with an array of tables `[[kit]]`,
  each carrying `name` (string) and `path` (string, relative to the tree root, forward slashes).
- The tools directory: `tools/` under the tree root. Every immediate subdirectory of `tools/` is a
  kit.
- Optional `waivers.txt` beside `kits.toml`: one relative path per line; blank lines and lines
  starting with `#` are ignored. A waived path is an undeclared kit directory that is allowed to stay
  undeclared.

### Behaviour

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

### Constraints

- Python 3.11+, standard library only. One file. Runs on Windows and POSIX.
- `fixtures/` in this directory shows one clean tree and one tree with findings. They are examples,
  not the acceptance suite.

---

## Task B — `rows_merge.py`: a three-way merge driver for row-keyed markdown records

Build `rows_merge.py`, a Python 3 standard-library-only git merge driver, in this directory.

### What it is for

Several people append to the same backlog file from different machines. Git's line merge conflicts
on rows that were merely added next to each other. This driver merges by ROW KEY instead, so two
sides that touched different rows always merge clean, and only a real disagreement about one row
conflicts.

### The file format

A backlog is a markdown file. A ROW is a line of the form

    - <ID> · <STATUS> · <text>

where `<ID>` is `FAMILY-slug-N` (an uppercase family, an alphabetic slug, an integer N), `<STATUS>`
is one uppercase word, and the separator is ` · ` (space, U+00B7, space). Every other line is
NON-ROW content: headings, prose, blank lines. Rows may appear anywhere in the file.

### Invocation (git merge-driver convention)

    python rows_merge.py <base> <ours> <theirs>

Read the three files, write the merged result INTO `<ours>` (overwriting it), exit 0 on a clean
merge and 1 when any conflict remains. Git wires it as
`merge.rows.driver = python rows_merge.py %O %A %B`.

### Merge rules for rows, keyed by ID

- Added on one side only → kept.
- Added on both sides, identical → kept once. Added on both sides, different → conflict.
- Changed on one side only, relative to base → that side's version.
- Changed on both sides identically → kept once.
- Changed on both sides differently → conflict.
- Deleted on one side, untouched on the other → deleted.
- Deleted on one side, changed on the other → conflict.
- A conflict is written in git's own style so editors and `git diff` recognise it:

      <<<<<<< ours
      <the ours row, if any>
      =======
      <the theirs row, if any>
      >>>>>>> theirs

  A conflicting row that was deleted on one side has an empty side in the marker block.

### Non-row content

Merge it too: a change to non-row content on one side only is taken. Rows must stay in a sensible,
deterministic order — a reader must still be able to find a row where it was.

### Constraints

- Python 3.11+, standard library only. One file. Runs on Windows and POSIX; the output's line
  endings match the input's.
- `fixtures/` in this directory holds a few base/ours/theirs triples with the expected merge for the
  clean cases. They are examples, not the acceptance suite.

---

## Task C — `ledger_report.py`: a gate-ledger reporter with a liveness assertion

Build `ledger_report.py`, a Python 3 standard-library-only command-line reporter, in this directory.

### What it is for

A merge bar runs many gate legs and appends one row per leg per run to a ledger. Nobody reads the
ledger. This tool turns it into a per-leg report a session can read in one pass, and — the part that
matters most — it REFUSES to report a reassuring nothing: a leg that is declared but never runs, and
a ledger with nothing in it, are both failures rather than clean runs.

### Inputs

- `gate-ledger.tsv`: tab-separated, no header row. Columns: `run_id`, `timestamp` (ISO-8601 with an
  offset, e.g. `2026-09-18T14:03:22+03:00`), `leg` (a name), `seconds` (a decimal), `verdict` (one
  of `GREEN`, `RED`, `SKIPPED`). Rows are appended chronologically, but the file may have been merged
  from several machines, so do not assume they are in order.
- `gate-legs.json`: a JSON array of objects, each `{"name": "<leg>", "ceiling_s": <number>}`, and
  `ceiling_s` is optional. This is the DECLARED set of legs.

### Behaviour

    python ledger_report.py [--ledger PATH] [--manifest PATH] [--window N] [--since ISO]

- Defaults: `gate-ledger.tsv` and `gate-legs.json` in the current directory; `--window 5`.
- For every declared leg, in MANIFEST order, print one line to stdout:

      <leg>  runs=<n>  last=<verdict>  median_s=<x>  ceiling_s=<c|->  <status>

  where `median_s` is the median of `seconds` over that leg's most recent `--window` runs, and
  `<status>` is `OK`, `BREACH` (the median exceeds the ceiling), or `DEAD PROBE` (declared, but no
  row in the ledger after filtering).
- After the per-leg lines, print one `ORPHAN <leg> runs=<n>` line per leg present in the ledger but
  absent from the manifest.
- `--since ISO` keeps only ledger rows at or after that instant.
- Liveness: if the ledger has NO rows after filtering, print exactly `DEAD PROBE: ledger empty` and
  exit 1. A tool that reports a clean bar over an empty ledger is worse than no tool.
- Exit 0 when every declared leg is `OK` and there are no orphans. Exit 1 on any `BREACH`,
  `DEAD PROBE`, or `ORPHAN`. Exit 2 on misconfiguration: a missing or unparseable input, a manifest
  entry without a name, or a malformed ledger row.

### Constraints

- Python 3.11+, standard library only. One file. Deterministic output.
- `fixtures/` in this directory holds a sample ledger and manifest. They are examples, not the
  acceptance suite.

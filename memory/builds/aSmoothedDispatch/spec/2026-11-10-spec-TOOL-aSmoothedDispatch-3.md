# TOOL-aSmoothedDispatch-3 — `unattended.sh --help` prints the verb list and exits 0

**Status:** SPECCED · rev-2 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-brief.md) | research | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-1-token-fix.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-1-token-fix.md) | research | TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 |
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-3-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-3-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`unattended.sh --help` and `-h` print the verb list that refusal 14 already derives, a pointer to the
verb carrier and the usage text, then exit 0. Today both refuse with check 14 and exit 1, so an agent
asking for help spends a turn on a refusal (brief item 3).

## 2. Scope (IN)

- **S1** — A `--help|-h)` arm in the driver's argument loop prints one line naming the verbs through
  `verb_list`, one line naming `$MEMORY_ROOT/guides/UNATTENDED-VERBS.md`, then the output of `usage`,
  and exits 0. Observed by AC1, AC2 and AC3.
- **S2** — One header line documents `--help`, so `usage` renders it and check 26's flag join finds it.
  Observed by AC4.
- **S3** — Suite arms in `tools/unattended/unattended.test.sh` pass `--help` and `-h`, and the
  effective `FLOOR_ASSERTIONS` pin rises by exactly the assertions added. Observed by AC4.
- **S4** — A bare call keeps printing `usage` and exiting 2. Observed by AC5.

## 3. Non-goals (OUT)

- `--help` does not join `VERBS_INLINE`. It is not a verb: it takes no slug, touches no record and
  is not a run step. Joining the set would owe it an entry in `tools/unattended/VERBS.template.md`
  and an invocation in `tools/unattended/SKILL.template.md` through check 26's verb join, for no reader.
- No change to refusal 14, its message or its arm.
- No change to the run log. `--help` is journaled like every argument except `--version` and `--plan`,
  so the sentence in `memory/guides/UNATTENDED-VERBS.md` about that stays true.
- No per-verb help, such as `--dispatch --help` printing only that verb's line. `--help` anywhere in
  argv prints the whole text.
- No hand edit to `KIT_UNATTENDED_VERSION` or `tools/unattended/kit.toml`. The lander's `mint` moves it.
- No change to `load_driver_conf`. `--help` needs the conf exactly as `--version` does today.

### Edges

none

## 4. Design

### Where it sits

The argument loop is fenced by `# gov:argv-begin` and `# gov:argv-end`
(`tools/unattended/unattended.sh:15085`, `:15208`). `--version` exits inside it at `:15193`, after
`load_driver_conf` has run (`:924`), so `MEMORY_ROOT` is set (`:682`). The new arm sits beside
`--version` and above the catch-all `*)` arm at `:15199`, which is where `--help` falls to refusal 14
today:

```bash
    --help|-h)      echo "unattended: the verbs are $(verb_list); each verb's contract is $MEMORY_ROOT/guides/UNATTENDED-VERBS.md"
                    usage; RUNLOG_CLEAN=1; exit 0 ;;
```

`verb_list` (`:119`) renders `VERBS_SLUG` and `VERBS_INLINE`, the set refusal 14 prints at `:15205`,
so the list is derived and never typed. `usage` (`:137`) renders the header's invocation lines and the
`VERB_REQUIRES` rows. It is printed too because an agent asking for help wants argument shapes, and
the verb list alone would send it to an 800-line guide for them, which is the extra turn this build
removes. `usage` already falls back to the verb list when the header cannot be read (`:143`).

`RUNLOG_CLEAN=1;` immediately before `exit` is the shape the runlog-writer suite enumerates
(`tools/unattended/runlog-writer.test.sh:464`). The arm adds no `fail` call, so check-arms gains no
branch.

### The header line

Inserted after the `--version` line at `:36`, in that block's column layout:

```text
#   unattended.sh --help                                           # the verb list, the verb carrier's path and this text, then exit 0; -h is the same
```

Check 26's flag arm (`tools/unattended/check-unattended.sh:4924-4978`) reads every `--<name>` token in
the argv region and joins it to the header lines and to a non-comment line of the sibling suite, both
directions. With the arm, the header line and the suite arms, `--help` is on all three. `-h` is not a
`--<name>` token and is not graded.

### The suite arms

Beside the `--version` arms at `tools/unattended/unattended.test.sh:3949-3952`:

```bash
out=$(run --help); rc=$?
same "--help exits 0" "$rc" "0"
hit  "$out" "unattended: the verbs are --preflight, "
miss "$out" "the verbs are ;"
hit  "$out" "memory/guides/UNATTENDED-VERBS.md"
hit  "$out" "unattended.sh --help"
same "-h prints what --help prints" "$(run -h)" "$out"
```

That is six assertions, so the effective pin, the second `FLOOR_ASSERTIONS` assignment (`:19086`),
rises from 3256 by 6. Units 1, 2 and 4 of this build also move that pin, so the builder adds 6 to the
value it finds and does not write 3262 blind.

### Files touched (estimate)

`tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh`

### Alternatives rejected

- The verb list and the pointer alone, with no `usage`. Rejected because it leaves the argument
  shapes one more read away.
- `usage` alone. Rejected because the brief names the derived verb list and the pointer, and the
  header does not name the verb carrier.
- Joining `VERBS_INLINE`. Rejected in §3.

## 5. Production-readiness checklist

- security — N/A: the arm reads only the driver's own declarations and writes no record.
- perf / scale — N/A: one `sed` over the driver, which a bare call already runs.
- error / empty / loading states — an unreadable header prints `usage`'s own fallback line, and the
  first line still carries the list.
- observability — the run log records the `--help` call like any other argument.
- risks — the printed path is right only where the verb carrier is installed under `MEMORY_ROOT`,
  which is where `tools/unattended/adopt-unattended.sh:773` puts it.
- testing — the suite arms declared in §7, observed RED and GREEN by the main loop at the close, and
  the direct probes of §6.
- migration — none: an adopter gains a working `--help` at the next kit version.
- user docs — the header line is the driver's CLI documentation and `usage` renders it. No `help/`
  page covers the driver's CLI.

## 6. Acceptance criteria

Each probe runs from the repository root with `GOV_RUNLOG=0`, so it writes no run-log line.

- **AC1** — When `GOV_RUNLOG=0 bash tools/unattended/unattended.sh --help; echo "rc=$?"` runs, the
  first line opens `unattended: the verbs are --preflight, `, the same output carries
  `memory/guides/UNATTENDED-VERBS.md` and `usage:`, and the last line is `rc=0`.
  Red when: the arm is absent, as at `ae6735c1`, where the call prints
  `UNATTENDED check 14 FAILED — unknown argument` and `rc=1`.
- **AC2** — When `diff <(GOV_RUNLOG=0 bash tools/unattended/unattended.sh -h) <(GOV_RUNLOG=0 bash tools/unattended/unattended.sh --help)`
  runs, it prints nothing and exits 0.
  Red when: the arm's pattern omits `-h`, which then reaches refusal 14.
- **AC3** — When the verb list on `--help`'s first line, between `are ` and `; each`, is compared with
  the one `GOV_RUNLOG=0 bash tools/unattended/unattended.sh --frobnicate` prints between `are ` and
  `: --frobnicate`, the two strings are equal.
  Red when: the arm types its own list, and a verb added to `VERBS_SLUG` reaches one and not the other.
- **AC4** — When `grep -c '^#   unattended.sh --help ' tools/unattended/unattended.sh` runs it prints 1,
  `grep -v '^[[:space:]]*#' tools/unattended/unattended.test.sh | grep -c -- '--help'` prints at least 1,
  and the `usage:` block of AC1's output carries the `unattended.sh --help` line.
  Red when: the header line is missing, so check 26 refuses `--help` as a parsed flag no header
  documents, or the suite never passes it.
- **AC5** — When the command below runs, the output opens `usage:` and ends `rc=2`, as at `ae6735c1`.
  ```bash
  GOV_RUNLOG=0 bash tools/unattended/unattended.sh; echo "rc=$?"
  ```
  Red when: the arm changes the bare-call contract.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `tier2-review self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC4 · the six `--help` assertions, staged by deleting the `--help|-h)` arm, where the call reaches refusal 14 and exits 1 · `FLOOR_ASSERTIONS` at its second assignment, raised by 6

The close also runs `unattended kit gate`, whose check 26 reads the header line and the suite arms
together. The `tier2-review self-test` leg is owed because its guard names
`tools/unattended/unattended.sh`. This spec's author may run only `memory hygiene` and the lexicon,
so every other verdict is the main loop's at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.
- rev-2 · 2026-11-10 · AC5 · the bare-call command moved out of inline backticks into a fenced block
  inside the bullet, so the spec-tokens paths join stops grading its semicolon-suffixed driver path
  as untracked; meaning, command and expected output unchanged. Record
  `2026-11-10-prompt-TOOL-aSmoothedDispatch-3-1-spec-writer`.

## 10. Reuse audit

The seam is `verb_list` and `usage` in `tools/unattended/unattended.sh` (`:119`, `:137`), both reused
unchanged. `python tools/codebase-map/reuse_lookup.py "print the driver verb list and usage on a help
request"` ranked `usage` first, as a SEAM with fan-in 10. The new arm sits in the existing argument
loop beside `--version`, and no new function is minted. Recall returned TOOL-dDerivedDocket-41 and the
`cFinalBerth` F11 finding, both about the verb set drifting across carriers, which is why the list is
derived through `verb_list` and `--help` stays out of `VERBS_INLINE`. Neither hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does the unattended driver answer an unknown argument or a help request" --terms "unattended driver verb list refusal 14 unknown argument usage header verb carrier VERBS_SLUG help"`

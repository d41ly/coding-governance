# TOOL-aPairedSlots-7 — the common dir's shared files take a second concurrent writer safely

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base b6cd02bc · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md](../build/2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md) | journal | TOOL-aPairedSlots-5 TOOL-aPairedSlots-8 |
| [2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh](../build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh) | journal | TOOL-aPairedSlots-5 |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 |

<!-- /gen:spec-records -->

## 1. Goal

Four files in a repository's git common dir are written by every bar of every worktree: the run
log, the health log, the shared full green and the drift history. With two bars admitted at once
each of them meets a second writer for the first time. Each is made safe for it, by the change the
measurement says it needs and no more.

## 2. Scope (IN)

- **S1 — the run log line is written whole.** `write_runlog_verdict` in
  `tools/run-gates/run-gates.sh` appends its one `gates.log` line through `cat` rather than the
  `printf` builtin's redirection. Measured on node a: three concurrent writers of 2000-byte lines
  through `printf >>` tore 146 of 3200 lines, and of 12000-byte lines 308 of 900, while the same
  lines piped through `cat >>` tore none at 2000 or 12000 bytes. A run-log line grows with its
  failing legs' names and has reached 923 bytes. Observed by AC1.
- **S2 — the health log trim takes a lock and re-reads before replacing.** The trim in
  `add_health_event` runs only while it holds a `noclobber` lock file beside the log, created by
  a builtin redirection, so two bars never trim at once; and it compares the line count it trimmed
  from with the count just before the `mv`, re-trimming once if a sibling appended meanwhile. The
  append itself is unchanged: one short line through `>>`, measured whole for 4500 concurrent
  100-byte lines. Observed by AC2.
- **S3 — the shared full green is staged under a per-process name.** The copy to
  `gate-full-green.shared` goes through `gate-full-green.shared.tmp.$$`, so two bars stamping at
  once each `mv` a whole file and the last writer wins, as the prompt rules. Observed by AC3.
- **S4 — the drift history writes its header only into a file it created.** `write_drift_history`
  in `tools/drift-audit/drift_report.py` creates an absent history with exclusive-create mode and
  writes the header only when that create succeeded, then appends its rows in the one binary write
  it already makes. Measured on node a: 900 concurrent 27-row groups appended whole and contiguous.
  Two first writers could both see an empty file and both write a header. Observed by AC4.
- **S5 — the text.** Each site's comment states its second writer and the measurement.
  NOT OBSERVED — prose.

## 3. Non-goals (OUT)

- The worktree's own git dir, made per-bar by TOOL-aPairedSlots-5.
- Rotating or re-capping the health log.
- Any change to what a line in any of these files says.

### Edges

- **consumes-from** `TOOL-aPairedSlots-5` — the audit that names these four files.

## 4. Design

The measurement decided the shape of each fix. Short appends are already whole on this host, so the
health log append is left alone and only its trim, a copy-and-replace, is serialized. A run-log line
can pass the size where builtin `printf` splits its write, and one `cat` per bar is the cheapest
writer measured whole at every size tried. The shared green is a copy-and-replace whose only defect
is a fixed staging name. The drift history's appends are already one write each; only its
header-on-empty decision is racy, and exclusive create closes it.

The health log trim keeps a residual, stated at the site: an append that lands between the
re-read and the `mv`, a window of two builtins, is lost. Trims happen once per 250 events.

### Inventory

No function is minted. New paths: `health.log.trim` (the lock file) and
`gate-full-green.shared.tmp.<pid>` (the staging name).

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`

### Alternatives rejected

- **A lock around every append.** It costs two spawns per health event for a write the measurement
  shows is already whole.
- **Rotating the health log by rename.** It is lossless, but every reader of the log would have to
  read two files.

## 5. Production-readiness checklist

- security — N/A — the same files, the same writers.
- perf / scale — one `cat` spawn per bar for the run log; the health lock costs builtins only.
- error / empty / loading states — a trim that cannot take its lock skips the trim this event; the
  next event retries.
- observability — unchanged lines, whole.
- risks — the stated trim residual.
- testing — AC1 to AC4, each RED against the old writer.
- migration — none.
- user docs — N/A — internal files.

## 6. Acceptance criteria

- **AC1** — When three concurrent fixture runners each write 50 run-log lines padded past 4000
  bytes into one common dir, `gates.log` holds 150 whole lines, each parsing with `parse_line`.
  Red when: the line is written with `printf >>`, and lines tear.
  cost: about two minutes of spawns on node a.
- **AC2** — When two fixture bars trim one `health.log` at its cap while a third appends, no line
  appended before the trim began is absent afterwards except those the cap drops, and
  `health.log.trim` is gone.
  Red when: the trim runs unlocked and a sibling's line is lost.
- **AC3** — When two fixture runners stamp `gate-full-green.shared` at once, the file equals one of
  the two stamps byte for byte and no `gate-full-green.shared.tmp` file remains.
  Red when: the staging name is fixed and the file is torn or empty.
- **AC4** — When the drift-audit self-test's new arm starts two `write_drift_history` writers on an absent history, the
  file carries exactly one header line.
  Red when: the header is written on a size check, and two headers land.

## 7. Gates

`run-gates canary` · `drift-audit selftest`

New arm: tools/run-gates/run-gates.runlog.test.sh · covers AC1 AC2 AC3 · the writer replaced by printf, the trim unlocked, the staging name fixed · none
New arm: tools/drift-audit/selftest.py · covers AC4 · a header written on an empty-file check · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

The seams are the existing writers: `write_runlog_verdict`, `add_health_event` and the full-green
stamp in `tools/run-gates/run-gates.sh`, and `write_drift_history` in
`tools/drift-audit/drift_report.py`. `reuse_lookup.py` named no shared append-lock seam; the
`noclobber` claim follows the turnstile's own `mkdir` claim in spirit with builtins only. Recall
returned TOOL-aMendedFleet-48, the drift history's design, whose "interleave whole groups at worst"
the measurement confirmed.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`

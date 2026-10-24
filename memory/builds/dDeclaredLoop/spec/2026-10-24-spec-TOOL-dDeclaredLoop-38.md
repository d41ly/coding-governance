# TOOL-dDeclaredLoop-38 — the trailer CLI writes LF only, so a shell loop never keeps a CR on its last token

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 4 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-38-deviation-381.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-38-deviation-381.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
confirmed finding **id 18 at HIGH**, its item **H9**, alone in that item. `TOOL-dDeclaredLoop-23` §4
says the CLI's `tokens <revs>` "prints that function's bytes exactly", and its shell consumers read it
line by line. Python's `print` writes CRLF on win32: probed on node `d` on 2026-10-24,
`python -c "print('a b')" | od -c` shows `a b \r \n`. The pipeline it replaces ends in
`tr -c 'A-Za-z0-9\n-' ' '` (`tools/unattended/lib-unattended.sh:1153`), which turns that CR into a
space today. `tools/unattended/check-pass-order.sh:275-278` and
`tools/unattended/check-brief-recorded.sh:304-306` fill `_SUBJ` with `done < <(read_attribution_tokens
HEAD)`, which keeps the CR, so a unit named as the last token of a subject or `Pass:` trailer never
matches its ` $id ` pattern; the sha count still agrees, so those units grade unbuilt-in-range and the
legs exit 0. This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-23`.

## 2. Scope (IN)

- **S1** — Every stdout write of `commit_trailers.py`'s CLI goes through one writer that emits LF only:
  `main` calls `sys.stdout.reconfigure(newline="\n")` before its first write, in the canonical
  `tools/lib/commit_trailers.py` and so in every copy its `commit_trailers_py` parity row holds.
  Observed by AC1.
- **S2** — The shell wrapper `read_attribution_tokens` keeps one CR-stripping stage after the CLI, so a
  copy running under an interpreter that ignores the setting still yields LF-terminated tokens:
  `| tr -d '\r'`. Observed by AC2.
- **S3** — `TOOL-dDeclaredLoop-23` AC3's byte compare is made through files, never through `$(...)`,
  which strips trailing CRs and hides the defect: the probe writes each tree's output to a file under
  the run's scratch and compares them with `cmp`, and an `od -c` of the working tree's file shows no
  `\r`. This supersedes that criterion's comparison method, not its population. Observed by AC2.
- **S4** — The consumer probe the finding names: the CLI's output fed through `< <(...)` into the
  `_SUBJ` loop of `tools/unattended/check-pass-order.sh`, sourced in a scratch shell over a fixture
  whose commit names its unit as the final token of its `Pass:` trailer, matches that unit.
  Observed by AC3.

## 3. Non-goals (OUT)

- The reader, its views and the other consumers: `TOOL-dDeclaredLoop-23`'s.
- A lint over every Python CLI read by shell, the finding's left-shift. It is a class wider than this
  build's clauses; S1 and S4 gate this reader, and the class is recorded as a gotcha at the close.
- Line endings of a file a Python tool writes: `text eol` rules and the `encoding posture` leg own
  those, and this CLI writes no file.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-23` — `commit_trailers.py`'s CLI verbs `tokens` and `message` and `read_attribution_tokens`, whose output this unit makes LF-only
- **hands-off** `TOOL-dDeclaredLoop-58` — AC1's observation, a counted three-line output read before the CR check, which that unit re-specifies (the round-2 spec audit's id 51)

## 4. Design

### Evidence

- The probe above, and the same probe with `sys.stdout.reconfigure(newline="\n")`, which prints
  `a b \n`: both PINNED, measured 2026-10-24 on node `d`.
- `read_attribution_tokens` (`tools/unattended/lib-unattended.sh:1149-1154`) is the one shell function
  every `_SUBJ` cache reads; its last stage is the `tr` that absorbs a CR today.

### Why both S1 and S2

S1 fixes the producer, which is where the bytes are wrong. S2 is not a second fix of the same bytes: it
keeps the shell consumer's contract, LF-terminated lines of `[A-Za-z0-9-]` tokens, independent of the
interpreter the kit resolves, which is the property the replaced `tr` stage gave. It costs no fork,
because the pipeline already has a stage after the producer to replace.

### Files touched (estimate)

- `tools/lib/commit_trailers.py`
- `tools/memory-tree/commit_trailers.py`
- `tools/unattended/commit_trailers.py`
- `tools/loop/commit_trailers.py`
- `tools/runlog/model.py`
- `tools/unattended/lib-unattended.sh`

The copies change because the canonical block changes; the parity row holds them byte-identical.

### Alternatives rejected

- **Writing bytes to `sys.stdout.buffer`.** Equivalent output, but every write site must encode by
  hand, so a later `print` reintroduces the defect; one setting at entry covers every write.
- **Fixing only the shell side (S2 alone).** A Python consumer of the CLI, or a future shell reader
  without the stage, would read the CR again.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — the shell stage replaces a stage; no new spawn.
- error / empty / loading states — an empty range prints nothing, as before.
- observability — none changed.
- risks — a reader that relied on CRLF from this CLI: none exists, since the CLI is new in
  `TOOL-dDeclaredLoop-23`.
- testing — AC1 to AC3 as probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When the canonical copy's `python commit_trailers.py tokens HEAD~3..HEAD` runs on win32 over the
  `TOOL-dDeclaredLoop-23` AC1 fixture repository with its output redirected to a file, `od -c` of the
  file shows no `\r`.
  Red when: the CLI prints through a default win32 stdout, so each line ends `\r \n`.
  fixture: the AC1 repository `commit_trailers.py --fixture` builds under `%TEMP%`.
- **AC2** — When the probe writes `read_attribution_tokens HEAD` from base `ed497191` and from the
  working tree to two files and runs `cmp` on them, they are identical.
  Red when: the working tree's lines end in CR, which `cmp` sees and a `$(...)` compare would not.
- **AC3** — When a scratch shell sources `tools/unattended/lib-unattended.sh` and fills `_SUBJ` with
  `done < <(read_attribution_tokens HEAD)` over a fixture commit whose `Pass:` trailer ends with
  `TOOL-tFix-2`, `case "${_SUBJ[$sha]}" in *" TOOL-tFix-2 "*)` matches.
  Red when: the last token keeps a CR and the case pattern does not match.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `python resolver (behaviour + inline parity + idiom ban)` · `routed-commits selftest` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 · the CLI's output bytes over the fixture repository, staged by removing the reconfigure call in a scratch copy · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 18 (HIGH, item H9).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-58, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is the CLI `TOOL-dDeclaredLoop-23` mints and its one shell wrapper, `read_attribution_tokens`
(`tools/unattended/lib-unattended.sh:1149`); this unit changes their output bytes and adds nothing
beside them. `python tools/codebase-map/reuse_lookup.py "python CLI printing to stdout read by a shell
loop line endings"` ranked generic readers (`read`, `read_text`, `read_conf`) and `resolve_python`,
none of which sets an output line ending, so no existing seam fits the producer half.

Recall terms used: CRLF win32 print stdout reconfigure newline read_attribution_tokens _SUBJ tr pass-order brief-recorded

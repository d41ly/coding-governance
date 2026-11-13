# TOOL-dDeclaredLoop-38 — the trailer CLI writes LF only, so a shell loop never keeps a CR on its last token

**Status:** DEFERRED · rev-3 · 2026-11-13 · node d · Tier-2 · base ed497191 · streams tooling · order 4 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-38-deviation-381.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-38-deviation-381.md) | deviation | — |
| [2026-11-13-build-TOOL-dDeclaredLoop-38-deviation-382.md](../build/2026-11-13-build-TOOL-dDeclaredLoop-38-deviation-382.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-38-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-38-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-38-reground-brief.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-38-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
confirmed finding **id 18 at HIGH**, its item **H9**, alone in that item. Python's `print` writes CRLF
on win32, and a shell loop reading the trailer CLI through `< <(...)` keeps the CR on each line's last
token, so a unit named last never matches its ` $id ` pattern and grades unbuilt-in-range.
`TOOL-dDeclaredLoop-23` landed the CLI and closed the consumer half of the finding:
`tools/unattended/lib-unattended.sh#read_attribution_tokens` ends in `tr -d '\r'`. The producer half
is open at HEAD: `tools/lib/commit_trailers.py#main` writes through the default stdout, and the module
docstring of each copy names this unit as the owner of an LF-only CLI. This unit makes the CLI itself
write LF only. It repairs `TOOL-dDeclaredLoop-23`.

## 2. Scope (IN)

- **S1** — Every stdout write of the trailer CLI ends its lines in LF alone. `main`, inside the
  `commit_trailers_py` block, calls `sys.stdout.reconfigure(newline="\n")` as its first statement, in
  the canonical `tools/lib/commit_trailers.py` and so in the memory-tree kit's and the unattended
  kit's copy, which the block's parity row holds byte-identical. One call covers the verbs `tokens`,
  `message`, `--print-commits` and `--fixture`. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The reader, its views and its consumers: `TOOL-dDeclaredLoop-23`'s, landed.
- The consumer-side CR strips, which stay as they are: the `tr -d '\r'` stage of
  `tools/unattended/lib-unattended.sh#read_attribution_tokens` and the `trl=${trl%$'\r'}` line after
  the `message` call in `tools/unattended/unattended.sh`. Each keeps its consumer's contract under an
  interpreter that ignores the setting, and rev-2's S2 asked for the first, which HEAD holds.
- A byte compare of `read_attribution_tokens` between two trees, rev-2's S3: `TOOL-dDeclaredLoop-23`
  AC3 at its rev-3 already compares through files with `cmp`, and this unit moves no byte of the
  wrapper's output.
- A probe of the `_SUBJ` loops through the wrapper, rev-2's AC3: it holds at HEAD, so it cannot turn
  red on this unit's change. AC2 reads the CLI directly instead.
- The stdout encoding: `newline` is the one setting this unit passes.
- A lint over every Python CLI read by shell, the finding's left-shift. It is a class wider than this
  build's clauses; AC1 and the arm of §7 gate this reader, and the class is recorded as a gotcha at
  the close.
- Line endings of a file a Python tool writes: `text eol` rules own those, and this CLI writes no file.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-23` — `commit_trailers.py`'s CLI, its verbs and its fixture builder, whose output this unit makes LF-only
- **hands-off** `TOOL-dDeclaredLoop-58` — the count of output lines read before the CR check, in AC1 and in the arm of §7, which that unit specifies (the round-2 spec audit's id 51)

## 4. Design

### Evidence

Every probe below ran on node `d` at `32915e09` on 2026-11-13, and each figure is PINNED to that run.

- `python -c "print('a b')" | od -c` shows `a b \r \n`. With `sys.stdout.reconfigure(newline="\n")`
  first, a `print` and a `sys.stdout.write` both end in `\n` alone.
- `python tools/lib/commit_trailers.py tokens -1 HEAD | od -c` ends `\r \n`, and so does
  `--print-commits`: both write sites of `main`, `print` and `sys.stdout.write`, carry the defect.
- Over the repository `build_fixture` plants, `tokens HEAD` writes a CR on every line, and the
  `_SUBJ` loop statement fed that output directly does not match ` TOOL-tFix-2 `. Fed through
  `read_attribution_tokens` the same loop matches, and the wrapper's output holds no CR.
- `tokens HEAD~3..HEAD` over that repository prints nothing and exits 0, because `main` answers a
  range git cannot read that way. A CR check over that range passes on an empty file (§8 F2).
- `x=$(...)` of the CLI holds no CR in this node's bash, so a `$(...)` compare cannot see the defect.
- No file calls `main` in process: `tools/memory-tree/routed_commits.py` imports `derive_attribution`
  and `read_commits` alone, and every other consumer spawns the file.

### The change

`main` in `tools/lib/commit_trailers.py` gains one statement ahead of its argument read:
`sys.stdout.reconfigure(newline="\n")`. It sits in `main`, not under the `__main__` guard, because the
guard is outside the `commit_trailers_py` block and the parity row reads the block alone. Stderr is
not touched: no consumer reads it line by line. The module docstring of each of the files closes with
a `NOT here:` sentence naming an LF-only CLI as this unit's; that clause leaves the sentence in each,
since the docstring sits outside the block and no row carries it across.

The same idiom is live in `tools/govkit/shims.py`, whose entry passes `newline="\n"` to the same call.

### The arm

`tools/memory-tree/routed_commits.py#run_selftest` gains one arm. It plants the fixture with
`commit_trailers.build_fixture` under the selftest's scratch root, spawns the `commit_trailers.py`
beside the suite with `sys.executable` and the arguments `tokens HEAD`, the fixture as its working
directory, captures stdout as bytes and fails where they hold `b"\r"`. The spawned file finds the
trailer key table through `resolve_kit_dir` from its own directory, so it runs in place and needs no
copy.

What the arm does not check: on a node whose default newline is LF it cannot turn red, so it is live
on win32 nodes only, and its line says which it ran on. It reads the memory-tree copy; the parity row
is what carries the answer to the other files. It does not count lines: `TOOL-dDeclaredLoop-58`'s.

### What the change leaves alone

Each read at HEAD: `tools/unattended/lib-unattended.sh`, whose strip is built; no loop-kit
or runlog copy of the reader exists, the runlog re-point being `TOOL-dDeclaredLoop-56`'s; the
verdict-epoch gate's `DELEGATES` already lists both memory-tree files; the usage line of `main` and
the registry rows of `tools/playbook/namespaces.toml` and `tools/playbook/edges.toml` name no line
ending; `memory/map/generated/symbols.json` lists symbol names per file, and this change mints none;
no leg or guard is added, so the gate manifest and the kickoff manifest's stamp stay as they are;
and `memory/project/fork-ceilings.txt` holds no row naming the reader or the suite.

### Files touched (estimate)

- `tools/lib/commit_trailers.py`
- `tools/memory-tree/commit_trailers.py`
- `tools/unattended/commit_trailers.py`
- `tools/memory-tree/routed_commits.py`

### Alternatives rejected

- **Writing bytes to `sys.stdout.buffer`.** Equivalent output, but every write site must encode by
  hand, so a later `print` reintroduces the defect; one setting at entry covers every write.
- **The call under the `__main__` guard, as `tools/govkit/shims.py` places it.** The guard is outside
  the parity block, so a copy could lose the call and stay green.
- **Leaving the producer as it is, since the wrapper strips.** `--print-commits` and `message` reach
  their readers without the wrapper, and a later shell reader of `tokens` would read the CR again.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — no new spawn in any consumer; the arm adds one fixture and one spawn to the selftest.
- error / empty / loading states — an empty range prints nothing, as before.
- observability — none changed.
- risks — a reader that relies on CRLF from this CLI: none, since `read_attribution_tokens` and the
  `message` call both drop a CR, and `tools/playbook/edge_grammar.py#read_native_members` splits
  `--print-commits` with `splitlines`.
- testing — AC1 and AC2 as probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none: no page under `help/` states the CLI's line ending.

## 6. Acceptance criteria

- **AC1** — When `python commit_trailers.py tokens HEAD` and `python commit_trailers.py --print-commits`
  run on win32 from `tools/lib/`'s copy, inside the fixture repository, each with its output redirected
  to a file, `tr -cd '\r' < <file> | wc -c` prints `0` for both files.
  Red when: `main` writes through the default win32 stdout, so every line ends `\r \n`.
  fixture: the repository `python -c "import commit_trailers, sys; print(commit_trailers.build_fixture(sys.argv[1]))" <scratch dir>`
  plants when run in `tools/lib/`; the tree holds none, and `--fixture` deletes its own.
  figure: PINNED, measured 2026-11-13 at HEAD, where the `tokens` file holds a CR on each of its lines.
- **AC2** — When a scratch shell in that repository fills `_SUBJ` with the loop statement of
  `tools/unattended/check-pass-order.sh`, fed `done < <(python <canonical copy> tokens HEAD)` with no
  stage after the CLI, `case "${_SUBJ[$(git rev-parse HEAD)]}" in *" TOOL-tFix-2 "*)` matches.
  Red when: the last token keeps a CR and the pattern does not match, as at HEAD.

## 7. Gates

`routed-commits selftest` · `policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 · the CLI's stdout bytes over the planted fixture, staged on a win32 node by deleting the reconfigure call from the working tree's memory-tree copy for one run and restoring it · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which range does AC1 read, and the arm with it?** Rev-2 read `HEAD~3..HEAD` over the
  fixture. At HEAD that range prints nothing and exits 0, so AC1 passes on a CRLF build and the arm
  can never be seen red, which the round-2 spec audit's id 51 confirmed and `TOOL-dDeclaredLoop-58`
  S1 was promoted to repair at the order after this one. Options: (a) keep rev-2's range and let that
  unit correct it, so this unit closes on an arm nobody saw fail; (b) read `tokens HEAD` here and
  leave the line count, that unit's S2 and S3, where it is. (b) makes that unit's S1 already
  satisfied when it is re-grounded, and takes nothing else from it. Recommendation: (b). The body is
  written on (b).
  RESOLVED (agent, 2026-11-13, delegated): (b), rung 3: the criterion and the arm read a range that prints lines, so the arm can be seen red at this unit's close.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 18 (HIGH, item H9).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-58, written by the round-2 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-13 · §1 · S1 · §3 · §4 · §5 · AC1 AC2 · §7 · §8 F2 · §10 · re-grounded on `32915e09`
  by the brief `prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-38-reground-brief.md`. Satisfied by
  landed code and out of scope: rev-2's S2, the wrapper's strip; its S3, the file compare, which is
  TOOL-dDeclaredLoop-23 AC3; its S4 and AC3 through the wrapper. Moved by reading HEAD: the write set
  is the canonical, its two kit copies and the suite holding the arm, with no loop-kit copy, no
  runlog file and no library edit; AC1 plants its repository through `build_fixture` and reads
  `tokens HEAD` (F2); AC2 feeds the CLI to the loop directly; line citations became symbol citations.

## 10. Reuse audit

The seam is `tools/lib/commit_trailers.py#main`, the CLI `TOOL-dDeclaredLoop-23` minted, and the
idiom is the one `tools/govkit/shims.py` already passes at its entry; this unit adds one statement
there and one arm to `tools/memory-tree/routed_commits.py#run_selftest`, and nothing beside them.
`python tools/codebase-map/reuse_lookup.py "python CLI stdout newline reconfigure LF only carriage
return shell read loop"` ranked generic readers (`read_text`, `read`, `read_bytes`),
`resolve_python`, and `lf` of `tools/codebase-map/map_lib.py`, which normalises a text already read
and sets no stream's line ending, so no existing seam fits the producer beyond `main` itself.

Recall terms used: CRLF win32 print stdout reconfigure newline read_attribution_tokens _SUBJ tr build_fixture routed_commits

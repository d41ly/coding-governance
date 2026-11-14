**Serves:** research TOOL-aBriskDeclaration-1

# The dispatch declaration after aBatchedPacket: where the rest of the time goes

Measured on node `a` on 2026-11-14, on frozen clones, with the dDeclaredLoop run live on the node
throughout. Wall times therefore move with that run's load, by as much as a factor of two between
two runs of one command. The process counts do not move, so they are the figures to compare.

## 1. The apparatus

- `dd` is a clone of the live run's tip `bc42f13ca` (phase BUILDING, 99 units, 23 dispatch rows).
- `dm` is `dd` with origin/main `846d51d39` merged in, which is the tree the run holds once it
  merges main. Only `memory/DECISIONS.md` and the kickoff manifest conflicted, and the clone kept
  the run's side of both.
- `da` is a clone of `dm` with the prototype of this build's change in `tools/unattended/unattended.sh`.
- Each clone fetches from the real remote and pushes to a path that does not exist, so the claim
  read is the real one and no claim reaches the remote.
- The command is `bash tools/unattended/unattended.sh --dispatch dDeclaredLoop --pass
  TOOL-dDeclaredLoop-9 --writes tools/loop/loop_lib.py`, the order-7 unit the run dispatches next.
  It runs under `bash -x` with an `EPOCHREALTIME` prompt and `GIT_TRACE`. A trace line's cost is
  the gap to the next line. Git processes are counted from the trace file, and the other processes
  from the command words of the traced lines.

## 2. Where the time goes

| Stage | `dd` | `dm` |
|---|---|---|
| the whole verb | 387.7 s | 625.6 s |
| the spec-token checker, `run_bounded` | 186.6 s | 152.2 s |
| the order gate, its loop over the build's units | 90.8 s | about 230 s |
| the open-pass reader, `read_open_passes` | 80.5 s | about 172 s |
| the cache key, `derive_spec_token_key` | 9.8 s | 7.9 s |
| the chain gate, `check_chain_dispatch` | 6.5 s | under 10 s |
| git processes | 192 | 192 |
| other processes the trace names | 842 | 728 |

Both runs exited 0, printed the same lines and parked one row.

**The order gate.** `order_verb_of` reads one spec's status header through a command substitution
around `grep -m1`, then `printf | grep -oE | head -1 | grep -oE | head -1`, so each call costs about
seven processes and a fork. The gate calls it once for the dispatched unit and once for every other
unit of the build, so 99 calls and close to 700 processes in a 99-unit build. On `dm` its greps and
heads alone were 130.7 s of the 230 s. The cost grows with each unit the build adds.

**The open-pass reader.** It asks `check_pass_open` about every dispatch key in the run-state file,
18 at this tip, and every one read closed. Each call runs `pass_commit`, whose walk on the run's
branch is `read_attribution_tokens`: one `resolve_python` probe and one Python reader per key. That
reader is the run's own code, from TOOL-dDeclaredLoop-23, and main's lib walks with one `git log`.
On `dm` the Python half was about 45 s of the 172 s, `mktemp` and `rm` about 23 s, and git about
55 s.

**The checker.** It took 75 s alone on `dd` (PINNED 2026-11-14) and 152 to 187 s inside the verb,
under the run's load. The key that would skip it always misses on a unit's first dispatch, because
the brief and INPROGRESS commits move HEAD.

## 3. The candidates

| Candidate | Reading |
|---|---|
| **Read the order verb in the shell** | Taken. The header is the first `**Status:**` line, and both expressions are POSIX ERE, so `[[ =~ ]]` gives the same first match with no process. |
| **Start the checker before the open-pass reader, read it where it ran** | Taken. Neither reads the other, nothing between them writes the tree, and the driver already has the seam: `init_bounded` and `read_bounded`, which `--preflight` uses for its probes (TOOL-aBriskPreflight-4). |
| A batched `pass_commit` over every key | Not taken. The run's branch rewrote `pass_commit`'s walk, so a change there conflicts when the run merges main, and a second walk beside it is two answers to one question. |
| Ask a terminal unit's status before its openness | Not taken. Openness decides whether the `left out as terminal` note prints, so the note would change. |
| A recorded verdict of closed keys | Not taken. It is a cache whose wrong answer loosens condition 1. |
| A narrower checker, or a key without HEAD | Not taken. The checker's joins read history and the whole tree, and a narrower read is a refusal that can no longer happen. |

## 4. The prototype, measured

On `da`, against `dm`'s 625.6 s, 192 git processes and 728 others:

| | `dm`, before | `da`, after |
|---|---|---|
| the whole verb | 625.6 s | 203.2 s |
| git processes | 192 | 193 |
| other processes the trace names | 728 | 233 |
| waiting on the checker after the reader | 152.2 s | 43.8 s |

The stdout, the stderr lines other than the trace and the parked row matched by `diff`. The row
differs only in its UTC stamp. The extra git process is the checker's start moving ahead of the
reader.

The order verb reader was checked against the old one, function against function:

- every tracked spec, 2,991 files, under GNU grep 3.12 in WSL, with `LC_ALL` set to `C.UTF-8` and
  to `C`: 0 differences, 2,637 ordered;
- dDeclaredLoop's 99 specs under MSYS on node `a`: 0 differences;
- 22 planted headers under MSYS, unset, `C.UTF-8` and `C`, and under GNU grep in both locales: 0
  differences, 12 ordered and 4 malformed. The plants are a doubled space, no space, a trailing
  value, garbage after the value, a word value, CRLF with and without garbage, no header, no verb,
  two verbs, two headers, no final newline, tabs, a header not at column 0, an empty file, 0, -1,
  `reorder` before `order`, and leading zeros.

## 5. What remains, and whose it is

- The open-pass reader, about 80 to 170 s on this run. About half is the run's own per-key Python
  reader and its per-key `resolve_python` probe; that fix belongs to that run's branch.
- The checker, 75 s alone on an idle-ish node (PINNED 2026-11-14), which now overlaps the reader.
- `derive_spec_token_key`, 7 to 10 s, two `git status` walks in `gate-fingerprint.sh`.

## 6. What the change does not check

- A spec holding a NUL byte. `grep -m1` calls it a binary file and prints no header, so the old
  reader read no order; the shell reads the header line. No tracked spec holds one.
- A refusal from the generator pairing or condition 1 now waits for the checker to finish and
  discards its answer, as `--preflight` waits for an unread probe. Those refusals took the reader's
  time before and take the longer of the two now.

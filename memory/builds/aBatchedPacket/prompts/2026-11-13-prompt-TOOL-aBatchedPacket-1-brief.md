# Brief — aBatchedPacket: the packet check and re-render without a git process per spec revision

**Serves:** research TOOL-aBatchedPacket-1

## The prompt

> Make two slow steps of this repository's unattended chain builds fast, as its own build in coding-governance. Follow the charter: start with `/session-kickoff`, spec before code, and land only when the charter's landing mandate holds; otherwise stop at a pushed branch and say so.

> What done looks like: both steps drop from tens of minutes to at most a few minutes on node a for an unchanged chain, measured before and after on the same frozen clone and recorded; every verdict and refusal either step produces today is still produced, shown by the existing fixtures and plants (`packet.py --fixture` with its plants, the spec-token checker's own arms, the driver's dispatch arms) and by a byte comparison of the packet rendered the old way and the new way; and a cache, if you add one, is invalidated by the content it depends on and can never turn a red into a green. State what the new design does not check.

> Constraints. `packet.py`, `carries.py` and `deviations.py` are pinned instruments of the dClosedLoop chain [...] prefer a design that leaves their bytes alone if one meets the target. Do not touch `memory/builds/dDeclaredLoop/` or the branch `branch/unattended-declared-loop-d56bf0` [...] Do not run the full merge bar or the unattended kit's self-test suites while that run is live unless your close requires it.

The task came from the session that started this one, on the owner's request to analyse both steps and make them faster. It is quoted in part; the passages above are the ones this unit serves.

## The brief

### Goal
The packet instrument's `--check` and `--write` for a chain build finish in under a minute on node `a`, and the dispatch declaration's spec-token check no longer pays the instrument's history walk. The instruments keep their bytes, and every line either step prints is still the instrument's own.

### Items
1. A new script beside `tools/check-spec-tokens.py` is the front door for a chain build's packet. It takes the instrument's own `--write <slug>` and `--check <slug>`, loads the tracked packet instrument unchanged, and runs the instrument's own `main` with two reads answered in-process: the coverage report, which the instrument gets by running `carries.py --report <slug>` as a child, and the parent specs `schedule.py`'s `tree_state` reads with one `git show` each.
2. The coverage report is rendered by the carries instrument's own `design`, `join` and `report`, over each chain spec's working-tree text with an empty revision list. `report` reads no revision and no finding of `join`, so its bytes are the same; the analysis record states the reading line by line.
3. The parent specs are read through one `git cat-file --batch` process, decoded as `subprocess.run(text=True, encoding="utf-8")` decodes them.
4. The shortcuts are bound to content: the script carries the git blob id of each of the three instrument files whose internals it relies on (`packet.py`, `carries.py`, `schedule.py`), and compares each with the file's bytes before it loads anything. On any mismatch it says so on stderr and runs the instrument as it stands, as a child with the same arguments, so a re-pinned or stubbed instrument is graded the slow way and never by a shortcut read against other bytes.
5. A `--parity <slug>` mode renders the packet both ways in one process, the instrument's way first, and compares path and bytes. It is the on-demand proof and costs the slow path once.
6. `scan_live_packets` in `tools/check-spec-tokens.py` runs the front door where it ran the instrument, and runs the instrument directly when the front door is not beside the checker.
7. The front door's own suite: a mismatched blob falls back and says so; the fast path and the instrument print the same lines and exit status for `--check` on a fixture tree with a red packet and with a green one; `--parity` reds when the two renders differ. Each arm seen red.
8. Write one spec, `memory/builds/aBatchedPacket/spec/2026-11-13-spec-TOOL-aBatchedPacket-1.md`, Tier-2, status SPECCED, rev-1, node a, base `8db6f4bef`, streams tooling, order 1, in the shape `memory/TEMPLATE-SPEC.md` states, with `memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-3.md` as the worked example. Work only in this worktree.
9. The design rests on `memory/builds/aBatchedPacket/build/2026-11-13-build-TOOL-aBatchedPacket-1-analysis.md`. Verify what it says of the carries, packet and schedule instruments under `memory/builds/dClosedLoop/build/` by reading that code before relying on it, and report anything in it or in this brief that is wrong.
10. A working prototype of the front door sits outside the repository, in the session scratchpad under `proto/`, as the file `chain_packet.py`; the analysis record's measurements are of it. Read it, state the design in the spec's own words, and improve on it where the code shows a better seam. In the product script the three blob ids are constants. It is untracked, so name it in prose only.
11. Decide and state: the script's name and home beside the spec-token checker, and each function's name, through the lexicon's `--suggest`; whether the batch read reuses `tools/memory-tree/tree_lib.py#read_blobs_at` or needs its own reader, and why; and what a new shipped script under `tools/` owes (the codebase map, the symbols index, a kit descriptor, a `help/` page if it is a user-facing surface, a gate-manifest entry for its suite), split between the builder and the main loop.
12. The spec states what the design does not check, starting from the analysis record's section 5 with each item verified.
13. A choice that is not derivable is a fork in the spec's open questions with a recommendation the builder can take; no owner turn is available.
14. Before returning, stage the spec and clear `python tools/check-spec-tokens.py --spec` over it and `python tools/playbook/positional.py check`. Run no whole-tree hygiene, no merge bar and no self-test suite, and do not commit. Return the spec path, its status line, each criterion's id with one line, every fork with its recommendation, and the checker's final line.

### Acceptance
- On the frozen clone of `8db6f4bef`, the front door's `--check dDeclaredLoop` prints the lines and the exit status the instrument printed, and the packet `--write dDeclaredLoop` writes is byte-identical to the one the instrument wrote.
- Both finish in under 60 seconds there, against 845 seconds for the instrument's `--check` (PINNED 2026-11-13, node `a`).
- `packet.py --fixture` and each of its plants and controls exits as it does at the base.
- The spec-token checker's own suite arms for the packet join pass unchanged, a stub instrument included.
- The three instrument files' blobs at the branch tip are their blobs at the base.

### Gates
The spec-token checker's suite and the new suite, run directly. `check-arms` over the new suite. The lexicon and codebase-map legs a new shipped script owes. No full bar while the dDeclaredLoop run is live.

### Non-goals
- Any byte of `packet.py`, `carries.py`, `deviations.py`, `schedule.py` or another dClosedLoop instrument. The batched read inside `carries.py` is ask `TOOL-dGroundRules-112`, the owner's landing and re-pin.
- `carries.py --build <slug> --exit`, the Design-exit join, which reads every revision and stays as slow as it is.
- A recorded-verdict cache. The measured cost after the change leaves nothing for one to save.
- `memory/builds/dDeclaredLoop/` and the driver's `verb_dispatch`.
- `gen_build_index.py --asks`, 13 seconds of what remains.

### Limitations
- The spec's acceptance criteria name observations a pass makes directly: the suite the unit adds, probes over a fixture tree, a `git rev-parse` of the three instrument blobs. The two that need the frozen clone and a 14-minute instrument run (PINNED 2026-11-13) are the main loop's, and the criterion says so. The acceptance section cites no path the unit has not built yet.
- Every spec line stating a figure with a unit carries the word PINNED or a commit sha on that line.
- The checker's packet-join arms in `tools/check-spec-tokens.test.sh` plant a stub at the instrument's path, which the blob binding must send down the fallback.
- The driver `tools/unattended/unattended.sh` is being changed on `branch/sad-allen-74f7bd`; this unit does not edit it.
- A chain build's README and packet tell a builder to run `packet.py --write` and `--check`. Those texts are generated by pinned instruments and stay; the front door is a second way to get the same bytes.

### Reuse
- `tools/memory-tree/tree_lib.py#read_blobs_at`, the kit's one `cat-file --batch` reader, takes `(commit, path)` pairs and returns bytes. `tools/memory-tree/design_lib.py#read_spec_revisions` is the product's two-spawn history reader, which the checker's own carries join already uses.
- Ask `TOOL-dGroundRules-112` (`memory/builds/dGroundRules/BACKLOG.md:19`) names the same cost and files its cure inside the instrument.
- `tools/check-spec-tokens.py#scan_live_packets` is the one product caller of the instrument.

## Drawn from the session

> rc=1 wall=845.49 · 13901 `git show` 695.5s · 1543 `git log` 119.2s · `carries.py --report` 812.2s · `gen_build_index.py --asks` 13.5s
— agent, the traced `packet.py --check dDeclaredLoop` on the frozen clone of `8db6f4bef`, node a, 2026-11-13 (PINNED)

> rc=1 wall=16.79 · the same eight lines of output · 20 processes
— agent, the prototype front door over the same clone, 2026-11-13 (PINNED)

## Owner confirmation

not asked — the session was started by another session with the task above, which says the owner dislikes being asked during this work and to derive and record decisions instead

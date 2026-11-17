# TOOL-dDeclaredLoop-74 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-74

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-3 of the spec, over the working tree: the `failed-fetch`, `quiet-remote`, `offline-stale`,
`stale-remote` and `fresh-clone` plants of `position.py`, each run alone by `--fixture`, standing in for
the `loop position fixtures` leg; `python -c` probes of `check_fetch_head` and `derive_fetch_url`, and two
in-process patches of the reading run through `run_plant`, standing in for nothing a leg runs; the naming
lexicon's suggest verb for both minted names, standing in for `lexicon naming predicates`; the map
generator's write, standing in for `codebase-map coverage + freshness`; and `grep` probes. The section 5
sweep re-run at this pass's base held its design claims: `read_remote_claim` has its one caller, no reader
parses a `FETCH_HEAD` beside the engine, no `--explain` flag exists, the usage anchor of `help/loop.md` is
unchanged, the lexicon offender pin is 1215 PINNED, `SHARED_RECORDS` is not written, no shell file is
edited and no edited path is on the kickoff watch list; its stale figures are deviation 742.

Owed to the close: every leg section 7 names, and the `loop position fixtures` leg, whose budget row the
close's timed reading re-prices where it passes it. Owed RED-first: the `tools/loop/position.py` arm,
`failed-fetch` on its staged break beside `quiet-remote` and `offline-stale`.

**Evidences:** TOOL-dDeclaredLoop-74
- AC1 — `failed-fetch` — `python position.py --fixture --plant failed-fetch` printed `read — FETCH_HEAD · skipped — empty` right after the tracking ref's line ending `from reflog`, `next: none - stale-remote: ...` and `position: fixture · failed-fetch · held`, exit 0. With `check_fetch_head` patched in-process to keep every file, the mtime-only reading, the same plant read the ref `from FETCH_HEAD`, its claim `fresh`, and printed `MISSED`, exit 1.
- AC2 — `quiet-remote` — `--plant quiet-remote` printed the ref's line ending `from FETCH_HEAD` and `position: fixture · quiet-remote · held`, and `--plant offline-stale` the same ending and `position: fixture · offline-stale · held`, each exit 0 with no `skipped —` line; `stale-remote` and `fresh-clone` each still printed `held`.
- AC3 — `another url reads` — the `failed-fetch` run above printed `position: fixture · failed-fetch · another url reads no line for main of origin`. With the check patched in-process to compare a line's URL against itself, the plant printed `another url reads kept` and `MISSED a main line fetched from a second url read 'kept'`, exit 1.
- AC4 — `spelled otherwise` — `grep -c` printed 1 PINNED for `failed-fetch` and 1 PINNED for `skipped — ` over `help/loop.md`, and 1 PINNED for `spelled otherwise` over `tools/loop/position.py`.

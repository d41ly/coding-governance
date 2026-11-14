# Acceptance ledger — TOOL-aBatchedPacket-1

**Serves:** journal TOOL-aBatchedPacket-1

Built against spec rev-1 in the pass commit `d3ee4c149`. Every line below was observed by the main loop on node a, with the dDeclaredLoop run live on the node throughout, so each wall time is an upper reading. `<clone>` is a frozen clone of `8db6f4bef`. The instrument's own readings on that clone are in the analysis record's section 4. No bar ran.

**Evidences:** TOOL-aBatchedPacket-1
- AC1 — `python <door> --check dDeclaredLoop` — in `<clone>`: the instrument's eight lines by `diff` against its recorded output, exit 1, 23 processes, 26.4 s, against the instrument's 845.5 s and 15,465 processes. (PINNED, 2026-11-13)
- AC2 — `packet: wrote` — in `<clone>`: `packet: wrote` and exit 0 in 22.1 s with 17 processes; the packet equals the one the instrument wrote, 73,446 bytes, by `cmp`; the following check read `byte compare green`, exit 0. (PINNED, 2026-11-13)
- AC3 — `python <door> --parity dDeclaredLoop` — in `<clone>`: `chain-packet: parity dDeclaredLoop · identical · 73446 bytes`, exit 0, in 2,142 s, the instrument's walk once under load. (PINNED, 2026-11-14)
- AC4 — `chain-packet: shortcuts off` — the suite's CP1 and CP2 green; red with the blob comparison made to return no moved role.
- AC5 — `python <door> --check <slug>` — the suite's CP3, CP4 and CP6 green; CP4, CP5 and CP6 red with the report read leaving out each build's last spec.
- AC6 — `python <door> --parity <slug>` — the suite's CP5 and CP7 green; CP7 red with the caches left uncleared and the second render taken before the reads were installed.
- AC7 — `git diff --quiet 8db6f4bef HEAD -- memory/builds/dClosedLoop/build/` — exit 0 at `d46719074`.
- AC8 — `python tools/check-spec-tokens.py` — the checker suite's no-door arm green; red with the checker calling the door unconditionally. The suite's two other reds, both parity arms, are red at `8db6f4bef` too.
- AC9 — `grep -c 'chain-packet' memory/map/features/spec-tokens.md` — printed 7.
- AC10 — `phase: BUILDING` — on a frozen clone of the live run's tip `f75d11d47`, the built checker and door printed `1 live chain run(s) · 1 packet(s) checked` and the `[packet]` hit, every line equal to the base checker's by `diff`, exit 1, 49 processes, 97.7 s against 1,062.1 s and 15,509 processes. (PINNED, 2026-11-13)
- AC11 — `python <door> --fixture` — in `<clone>`: the unplanted fixture, `--plant pin`, the pin plant under each `--control`, and the run-live plant gave the instrument's stdout and exit byte for byte; the other fourteen plants gave the exits the instrument's docstring states, through the door only, as fork F3 decided.

The suite's first run took 236 s for seven arms. (PINNED, 2026-11-13)

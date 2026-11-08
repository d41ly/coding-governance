# Acceptance ledger — TOOL-dFairHearing-47

**Serves:** journal TOOL-dFairHearing-47

Built against spec rev-1 at the pass's parent `1dc7a7932`. Every line the spec cites was read in the tree at that parent, and each held: the commits since the spec's `22621f55a` moved none of the files it cites. Each criterion's red value below was read from the parent's blobs, and its green value from the built files. No suite, gate or bar ran in the pass, so the loops' behaviour under the two hook destinations legs and `unattended-build self-test`, and the verdicts of the shell hygiene, govkit and ratchet legs, are owed to the close, as the spec's Gates section says. The `python tools/lexicon/lexicon.py --check` count, the role's one gate, read 1211 verb offenders at the pass's start and 1211 after the edit. This unit declares no `New arm:` line, so no RED-first observation is owed.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-47
- AC1 — `tools/check-hook-destinations.sh` — the two count commands printed 2 and 2 at the parent and 0 and 0 after the edit, the two `done <` commands each printed 1, and `bash -n` exited 0 on both files. The built assignment and loop lines, lifted from the file and driven over a planted `FLAT`, landed `hook-kit/a.js` and `workflows/b.js` at their canonical kits, left a path no destination holds unlanded, and removed the scratch file on exit. Owed to the close: `hook destinations self-test` and `unattended-build self-test`.
- AC2 — `.governance/install.json` — the first command printed nothing at the parent and the three lines after the edit, and the second printed 1. `tomllib` read the row, and the partition's exact-path comparison holds for it. Owed to the close: `govkit selfcheck`.
- AC3 — `hook destinations self-test` — the command printed 0 at the parent and 3 after the edit, and each of the leg's guard entries resolves to a path in the tree.
- AC4 — `memory/project/unarmed-branches.txt` — the first command printed 0 at the parent and 1 after the edit, the second printed one line opening `271:`, and the third printed 5.
- AC5 — `memory/guides/SESSION-KICKOFF.md` — the probe printed 11 at the parent, and printed 1 over a dangling commit of the staged tree with the parent as its one parent, moving no ref. Both stamps take the parent's sha and `last-audit` a later datetime. The Orientation section was re-read and no sentence is stale, and all 34 paths the manifest cites resolve. Owed to the close: `kickoff-manifest ratchet`.

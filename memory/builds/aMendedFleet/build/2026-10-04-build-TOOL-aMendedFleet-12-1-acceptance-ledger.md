# TOOL-aMendedFleet-12 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-12

**Evidences:** TOOL-aMendedFleet-12
- AC1 — `python tools/memory-tree/gen_build_index.py --write` — on the live tree `memory/LIVE.md` opens with the anchor sentence (21 days, 2026-10-05, aMendedFleet), its header ends `| Last record | Activity |`, all 23 rows carry a date and an activity, 3 `active` rows precede 20 `dormant` ones with no interleave, and the aMendedFleet row reads `active`
- AC2 — `--selftest` — the arm over two fixture trees holding the same tracked bytes, committed with author and committer dates 2025-01-15 and 2026-01-15, reads `apart=True same=True`. RED on a staged break appending the fixture's `git log -1` date to the LIVE.md artifact
- AC3 — `--selftest` — the four-build fixture at 21 days renders aFile 2026-09-09 `active` (record filename, exactly 21 days), aSpec 2026-09-30 `active` (status header, the anchor), aAsk 2026-09-08 `dormant` (an ask's `filed`, 22 days) and aNone 2026-08-01 `dormant` (its `opened`), active first, and the sentence names 2026-09-30 and aSpec. RED on three staged breaks: the boundary as `>=`, the ask dates dropped, the filename dates dropped
- AC4 — `--selftest` — with the key blank the four-build render equals the pre-unit render, frozen in the arm as it shipped, byte for byte. RED on a staged break rendering the columns whatever the key says
- AC5 — `gen_build_index.py --check` — `LIVE_DORMANT_DAYS` set to `abc`, then `0`, in `.memory-tree.conf`: each exits 1 with a line naming the key, `memory/LIVE.md` keeps its md5; restored to 21, `--check` is clean
- AC6 — `awk '/^\|/ && !/^\|[-|: ]*$/ {n++} END{print n-1}' memory/LIVE.md` — prints 23, and `grep -c '](builds/' memory/LIVE.md` counts 23
- AC7 — `grep -n "LIVE_DORMANT_DAYS"` — hits in the kit README's generator row, the example conf (blank), this repo's conf (21) and the generator, whose docstring source line now reads "for the ROSTER, and for the date of a build's last record"

## Owed at the close

- `memory/map/generated/symbols.json` — regenerated in this commit by `gen_map.py --write`; the
  codebase-map coverage and freshness legs are the close's.
- The lexicon leg grades `derive_last_record`; `lexicon.py --suggest --as py.function` answered OK,
  and the leg itself is the close's.
- `build-index selftest` ran here as the direct check, green; the bar's other §7 legs are the close's.

# TOOL-aMendedFleet-13 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-13

**Evidences:** TOOL-aMendedFleet-13
- AC1 — `python tools/memory-tree/gen_build_index.py --write` with `LIVE_LANDED_UNCLOSED="1"` — the `memory/LIVE.md` header row ends `| Landed-unclosed |`, every row carries an integer, and the counts equal the `detail` rows of `drift_report.py --json` read in the same minute: aMendedFleet 2, aBatchedLintel 1, dNarrowedAnchor 1, zero elsewhere, at 4 of 121. With this spec CLOSED both read again: aMendedFleet 1, the report 3 of 120
- AC2 — `--selftest` — the arm hands `derive_landed_counts` three rows, a live build's tracked unit, a CLOSED build's unit, and the live unit's own id at a path the fixture never tracked, and reads `[('aDone', 0), ('aLive', 1)]`. RED on two staged breaks: the terminal clause dropped read aDone 1, and an id-only match read aLive 2
- AC3 — `gen_build_index.py --check` — `EVIDENCE_GLOBS` in `tools/drift-audit/drift_signals.py` overridden to one glob matching no tracked file: exit 1 with a line naming the EMPTY evidence population, no render, `memory/LIVE.md` keeps its md5; restored, `--check` is clean
- AC4 — `gen_build_index.py --check` — `LIVE_LANDED_UNCLOSED="yes"` in `.memory-tree.conf`: exit 1 naming the key and its two legal values, blank and 1
- AC5 — `--selftest` — with the key `1` and a resolver raising KeyError, a LookupError, `plan` refuses with `LIVE_LANDED_UNCLOSED=1 needs the drift-audit kit, which does not resolve` and returns no artifact. RED on a staged break returning None from the LookupError handler, which rendered the artifacts
- AC6 — `--selftest` — with the key blank, and again as a single space, and a resolver that raises when called, `LIVE.md` equals TOOL-aMendedFleet-12's frozen pre-unit render and its 21-day render, byte for byte. RED on a staged break resolving the kit before the blank test
- AC7 — `grep -n "LIVE_LANDED_UNCLOSED"` — hits in all five carriers; this repo's value is `1`, the example's blank, and the `kit.toml` hit is the `requires_if` row naming `drift-audit`, its key also in `conditional_keys` for `govkit selfcheck` check 7

## Owed at the close

- `memory/map/generated/symbols.json` — regenerated in this pass by `gen_map.py --write`; the
  codebase-map coverage and freshness legs are the close's.
- The lexicon leg grades `read_landed_unclosed` and `derive_landed_counts`; `lexicon.py --suggest
  --as py.function` answered OK for both, and the leg itself is the close's.
- `govkit selfcheck` grades the new `requires_if` row; not run here, the close's.
- `build-index selftest` ran here as the direct check, green; the bar's other section 7 legs are the
  close's.

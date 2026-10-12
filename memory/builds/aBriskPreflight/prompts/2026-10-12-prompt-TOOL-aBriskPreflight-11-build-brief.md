# Build brief — TOOL-aBriskPreflight-11: the ceilings instrument prices every fork at the worst host reading on record

**Serves:** research TOOL-aBriskPreflight-11

Build the unit its spec, `spec/2026-10-12-spec-TOOL-aBriskPreflight-11.md` at rev-2, describes. Its
§8 F2 is RESOLVED by the owner at the hand-off as option (i): the instrument's refusal at or above
`GATE_BOUND` grades the wiring subject only (S6, AC6). S1 to S6 are all in scope; S4 writes the
instrument's stdout into the driver's three constant lines byte for byte, and spec 7 takes a rev line
naming this unit, its AC8 narrowed to the wiring ceiling by the same ruling.

## The tree you start from

- The run is at VERIFYING after a hand-off, resumed. HEAD sits on a prepared landing merge
  (`4bb77a0db`, onto origin/main `37200355`); build on top of it, never reset it.
- The unattended kit's version was minted 1.101 at `7d98741e3`; your edit to the driver moves the kit
  after that mint. Do not bump it: the main loop re-mints once after this unit.
- The row files are `.log` records under `build/`; `log::dark` is declared in `.lexicon.conf`. Keep
  their names: spec 11's own §6 cites them by path.

## How to work in this tree

- **Declare before you write**, with `--dispatch`: the instrument, `tools/unattended/unattended.sh`,
  `tools/unattended/README.md`, spec 7, `memory/builds/aBriskPreflight/README.md`, `memory/LIVE.md`,
  `memory/ledger/2026-10.md`, `memory/map/generated/symbols.json`, and any record you add (an
  acceptance ledger: this is a Tier-2 unit, so hygiene check 23 wants one in unit 6's shape). Stage
  those AND `RUN.md`.
- Spec 7 is CLOSED: its change is a rev line in its own §9, with the section and AC it touches named.
- Lexicon `--suggest` before naming anything new; `gen_map.py --write` after; a records-only `.sh`
  carries its comment-marked `**Serves:**` line in its first 12 lines.
- No suite, no bar. AC1 and AC6 run the instrument and staged copies of it under the scratchpad.
- Never kill a process you did not start.

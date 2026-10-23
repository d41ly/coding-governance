**Serves:** research TOOL-dGroundRules-23

# Writer task — rejoin TOOL-dGroundRules-23's wrapped fork mark

TOOL-dGroundRules-23's §8 resolved mark at line 177 wraps: the line ends `widens: none ·` and `relaxes: none` sits on
line 178. The departures report (`deviations.py --report dGroundRules`) reads a mark per line, so it reads `widens:` as
`none ·`, which joins no record. Put `widens: none · relaxes: none` on one line, rewrapping the paragraph so no line
passes the template's width, and change nothing else in the mark's meaning.

- Bump the spec's rev with a §9 line saying the mark was rejoined onto one line for the departures report's reader.
- Write set: `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-23.md` alone. Keep its byte count
  under 48800.
- Do not commit; run no gate but memory hygiene.
- Return the new rev, the edited lines and the byte count.

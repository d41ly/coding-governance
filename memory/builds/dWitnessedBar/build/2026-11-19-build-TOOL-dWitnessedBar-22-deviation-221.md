# TOOL-dWitnessedBar-22 deviation 221 — a leg manifest that is not a list of rows is refused

**Serves:** deviation TOOL-dWitnessedBar-22

- **Departs from:** `TOOL-dWitnessedBar-22@rev-5 [S4]`
- **Hand-off:** spec-to-code
- **Before:** §4 "The edge read" names three refusal lines for `read_leg_edges`: a text that does not parse as JSON, a key that is not a list of strings, and a row carrying either key with no `tag`. It does not name a text that parses but whose top level is not a list.
- **After:** `read_leg_edges` refuses that text too, in the same `EdgeRefusal`, with the line `holds a JSON <type>, not the list of leg rows`.
- **Cause:** builder discovery
- **Reason:** a JSON object parses, and iterating it yields its keys, none a row, so the adapter would return no edge and the edges check would read the manifest's edges as absent rather than unread. Deny by default refuses it, as the runner already refuses a manifest that is not a list.
- **Evidence:** `read_leg_edges` in `tools/playbook/edge_grammar.py`; the pass's `python -c` probe over `{}` printed `REFUSED edges: gate-legs.json: 1 leg row(s) refused` with that line (the acceptance ledger's AC3 line).
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** PLAY-dClosedLoop-2

**Serves:** journal TOOL-dScriptedRepeat-1

# The seven kickoff forks and the owner rulings that closed them

Node `d`, 2026-08-20. Lifted VERBATIM out of the build README at the round-3 trim, where it was
first written. Nothing here is edited: the trim needed the bytes, and a ruling is not derivable
from the thing it ruled on, so the rows move rather than compress.

Round 4, MEDIUM 9 is why this file exists. The trim replaced the table with a sentence pointing at
"the kickoff record", and no such record existed — the rulings had been written into the README that
later deleted them. Four lines of that same document still cite forks 1, 5 and 6 by number, and
forks 8 through 11 immediately below them are spelled out in full, so the document defined four of
eleven and referenced three it had erased.

## The rulings

The owner answered all seven before any design work. Recorded here because they are older than the
spec set and every spec is measured against them.

| # | Fork | Ruling |
|---|---|---|
| 1 | Home and coupling | **Third mode PLUS an attended path.** `authorized-by: playbook` joins the closed set; a second entry point runs the same checklist discipline with an owner in the loop, no anchor and no push mandate. Two entry points, ONE playbook artifact and ONE gate. |
| 2 | "Refuses normal builds" | **Gate the paths, document the judgment.** The playbook declares OUTPUT PATHS and a machine check reds a playbook-mode diff touching anything outside them plus its own records; the class that gate cannot see — a code change landing inside a declared output path — is a stated CHECK. |
| 3 | N pieces vs. the spec set | **The playbook is the spec; pieces are passes.** One unit per playbook RUN, never one per piece. Each piece is a pass with its own commit and reground point. The DoD must count pieces against the requested N rather than counting units. |
| 4 | Template evidence base | **Corpus-derived plus external research.** Derive from the two reference playbooks, this repo's spec template, hygiene grammar and GATE/CHECK philosophy; challenge that shape against external checklist and instruction-design literature; then freeze it and mark it human-curated. |
| 5 | When is a piece done | **The playbook declares its own GATE legs.** A playbook is VALID only if every step is tagged `GATE <leg>` or `CHECK <why>` and every named leg is runnable; piece-done is its declared legs green. This forces the adopting repo to own a checker, and that cost is the point. |
| 6 | The improvement loop | **A separate register, surfaced at close.** A proposal is not a park: a park is what a run refused to decide and blocks the close, a proposal comes from work that succeeded and must not. Distinct verb, distinct region, distinct DoD treatment. |
| 7 | Producer knowledge | **Agnostic — the playbook carries it.** The kit knows paths, counts, steps, gates and status. How a piece is produced is playbook prose. The kit grows no dependency on any generator. |

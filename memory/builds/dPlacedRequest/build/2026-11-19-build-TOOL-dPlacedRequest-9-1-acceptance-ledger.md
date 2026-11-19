# TOOL-dPlacedRequest-9 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-9

The unit was built from its spec at rev-6 (PINNED) on base `5f874dfc6`. The playbook kit gains the
`pockets` verb, `tools/playbook/instruction_units.py#run_pockets`, reading the units the card's slot
composes through `tools/playbook/overlay.py#derive_slot_units` with the selector `reader.card`, which
`tools/playbook/readers.toml` now declares. The kickoff engine gains
`skills/session-kickoff/manifest-check.sh#derive_pockets_block` and `CARD_POCKETS_BOUND`, called by
`skills/session-kickoff/manifest-check.sh#write_card`,
`skills/session-kickoff/manifest-check.sh#add_card_body` and
`skills/session-kickoff/manifest-check.sh#print_rekeyed_card` before each one's cap check. The
kickoff-manifest descriptor gains the `[[upgrade]]` row `kickoff-manifest/facts-to-overlay`, its program
`tools/govkit/steps/kickoff_facts_to_overlay.py` with `cmd_up`, `cmd_down`, `cmd_witness` and the
fixture's sixteen plants (PINNED), each run by `tools/govkit/selftest.py#check_kickoff_facts_step`.
Gov's own manifest first had its two value-less bullets rewritten to cite the unattended Skill's path,
then the step's `up` moved every bullet of its section B into the overlay: 36 bullets (DERIVED), 15 of
them `block` units (DERIVED), none refused (DERIVED). The re-stamp came first, so the before-image
`.governance/steps/kickoff-manifest/facts-to-overlay.before.json` holds the committed manifest's hash.

No gate, suite or bar ran in this pass. The step's criteria were observed by its own CLI,
`python -I tools/govkit/steps/kickoff_facts_to_overlay.py --fixture --plant <case>`, one case at a time,
each building a throwaway repository under the node's short temp path; the card criteria by gov's
engine over those fixtures and over a scratch clone of this worktree.

**Evidences:** TOOL-dPlacedRequest-9
- AC1 — `repo.kickoff.f01` — the plant `up` printed `ok` for "the overlay at HEAD holds f01 to f03 at
  level 2 under reader.card, each text its bullet" and for the section holding the facts bullet alone;
  its summary line read `4 line(s) · 0 failed` (DERIVED).
- AC2 — `tag` — `grep -n -A1 '^tag = "reader.card"$' tools/playbook/readers.toml` printed the `tag`
  line, then the `why` line naming the orientation card.
- AC3 — `## pockets` — the plant `up` printed `ok` for the uncommitted write reading `- none declared`
  and for `--all` after the commit printing the heading and the bullets in tag order; the plant
  `pockets-level` printed `ok` for a level-3 card unit held at HEAD and absent from the section.
- AC4 — `--room 40` — the plant `pockets-cap` printed `ok` for each of its checks: the output within
  the room of 2048 bytes (PINNED), each unit line whole in tag order, `<k>` plus the lines shown equal
  to the 30 units (PINNED), `--all` printing every line, and `--room 40` printing nothing at exit 0.
- AC5 — `recent —` — the plant `card` printed `ok` for the section and its unit lines immediately
  above `recent —` and above the READY anchor; the plant `card-no-playbook` printed `ok` for one
  `pockets — skipped:` line above `recent —`, the card written. Over a scratch clone of this worktree
  with the overlay committed, `--card --write` wrote a card of 8074 bytes (DERIVED) whose section held
  24 fact lines and the closing line `- … (+12) — instruction_units.py pockets --all` (DERIVED), and
  `--card --check` named no fact line.
- AC6 — `witness` — the plant `refused` printed `ok` for `up` exiting 0 and naming the refused
  bullet's position alone, the overlay at HEAD holding the first and third units alone, the section
  holding the facts bullet then the refused one, the `witness` exiting 0 and `down` restoring the
  manifest byte for byte; the plants `template`, `no-answer` and `no-kit` each printed `ok` for every
  check, `git status --porcelain` printing nothing for the last two.
- AC7 — `down` — the plant `down` printed `ok` for the manifest restored byte for byte with no overlay
  and no image left, the witness failing before the up and after the down and holding between, and no
  policy mirror written.
- AC8 — `instructions_edit.py propose add --manifest overlay` — each `awk ... | grep -c` over the Step
  2b section of `skills/session-kickoff/SKILL.md` and the ratchet section of
  `skills/session-kickoff/MANIFEST-TEMPLATE.md` printed 1 (PINNED); the `awk` over gov's section B
  printed the facts bullet alone, naming `tools/playbook/instructions_edit.py`.
- AC9 — `appended —` — the plant `card-cap` printed `ok` for a written card holding every unit line,
  an append under a cap four unit lines below that card (DERIVED) exiting 0 with its `appended —` line,
  the line above `recent —` counting at least one unit left out, and the card within the cap.

The bug-class checklist over the pass commit named the refusal branches no arm reached; each gained
a fixture plant, observed `ok` by the same CLI, each writing nothing: `escape`, an answer leaving the
target, exit 1 (PINNED); `bad-deploy`, a descriptor that does not parse, exit 1 (PINNED); `not-utf8`,
exit 1 (PINNED); `duplicate`, an overlay already holding a fact's tag, the writer's exit 2 (PINNED);
and `pockets-refused`, a refused overlay read giving the verb's one line at exit 1 (PINNED) and a
malformed argv at exit 2 (PINNED). The card's bound gained its suite arm, a stub outliving
`CARD_POCKETS_BOUND=1` (PINNED), probed alone over a scratch repository, printing the
`pockets — skipped:` line that names the bound. The fixture's git runs with no global or system config.

Owed at the close, by the main loop: the `govkit selftest` leg's `check_kickoff_facts_step`, and the
`manifest-check self-test` leg's new pockets block and the arms that moved with it (`AGH8 AC7`,
`AGH8 AC8`, `K2 AC4`, the map-block stub), each new arm with the RED-first observation the spec's
`New arm:` declarations ask for.

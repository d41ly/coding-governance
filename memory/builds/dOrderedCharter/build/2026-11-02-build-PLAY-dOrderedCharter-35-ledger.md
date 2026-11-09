# PLAY-dOrderedCharter-35 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-35

Each line is a probe this pass ran at rev-9 of the spec, with the pass applied. No leg, suite or bar ran in the
pass: every plant ran through `tools/playbook/fixtures/row_kind.py --plant` over a throwaway repository, and the
new render selftest block was lifted from source and run alone by a scratch probe, every case green. Four plants
were also run with one function of `overlay_rows` stubbed to its broken form, and each went red. This record
cites no code line.

**Evidences:** PLAY-dOrderedCharter-35
- AC1 — `add` exited 0 with gov's three rows `unchanged` and `fixture.adopter.extra` composed with `origin` `repository`; `typed-origin` exited 1 naming `fixture.adopter.extra` and the typed `origin`.
- AC2 — `adopter-tag` exited 0 with the overlay row composed; `gov-adopter` exited 1 on a line naming `owned` and `fixture.adopter.x`; with `check_row_owners` stubbed to find nothing, `gov-adopter` exited 0.
- AC3 — `no-seat` exited 1 on a line naming `owned` and `fixture.extra`.
- AC4 — `amends` composed `fixture.alpha` with grants read and write, needs `fixture.gamma` alone and ceiling high, its origin and tag gov's; `amends-undeclared` exited 1 naming `colour`, `amends-scalar` exited 1 naming `ceiling`, `schema-shape` exited 1 naming the field `grants` and the shape `list`; with `set_row_patch` stubbed to apply `remove` as `add`, `fixture.beta` stayed in needs.
- AC5 — `supersedes` composed `fixture.gamma` with the overlay row's fields and origin `repository`, state `replaced`, gov's row gone, and `fixture.alpha`'s need of `fixture.gamma` naming a composed row.
- AC6 — `exclude --exclude fixture.beta`, the tag committed in the scratch policy file and read back through `read_excluded_tags` at `--rev HEAD`, left `fixture.beta` out with state `excluded`; `--exclude fixture.nowhere` exited 1 naming the tag.
- AC7 — `pin-reordered` exited 0 with no stale edge and `fixture.alpha` amended; `pin-no-at`, `pin-bad-hash` and `pin-unknown` each exited 1 naming the edge; with `derive_row_canon` stubbed to unsorted JSON, `pin-reordered` exited 1, its pin matching no revision.
- AC8 — `renamed` composed `fixture.alpha2` amended through the rename record, the edge's pin unchanged; `split` and `ended` each read both edges `orphaned`, held the amendment out, composed `fixture.adopter.gamma-own` alone and filed one order per orphan.
- AC9 — `semantic --stale order` applied the patch over gov's new row, state `stale`, one order; `--stale warn` applied it with one standard-error line, one journal line naming `fixture.adopter.alpha-tuned` and no order; `--stale refuse` exited 1 naming the stale edge; with the walk stubbed to read stale as standing, `warn` printed no stale line and journaled nothing.
- AC10 — `vanished-field --stale warn` held the patch, composed gov's row as shipped and named `ceiling`; `--stale order` held it the same and its order says the patch is held, naming `ceiling`.
- AC11 — `editorial`, a comma added to gov's ceiling under a record the classifier marked editorial, exited 0 with the pin standing, no stale edge and state `amended`.
- AC12 — the catalogue probe printed one row, `[]`, `dOrderedCharter`, `True`, `True`; `policy.py lists --write` drained `instructions.exclude` and `lists --check` exited 0; the grep found one line, in `tools/playbook/overlay.py#read_excluded_tags`.
- AC13 — `states` printed one state line per gov row, carrying `unchanged`, `amended`, `replaced`, `excluded`, `stale` and `orphaned` each once.
- AC14 — owed: its pathspec is unit 49's to correct and is observed at that pass; `help/overlay-rows.md` carries a stale-rows section naming `instructions.stale` and `help/README.md` links the page.

**Owed to the close.** The bar, the tags leg the brief asks green (the role hook refused `gov_tag.py check` in
the pass), and the RED-first observation of the `New arm:` line: the render selftest's block running
`row_kind.py` over every plant of the acceptance criteria.

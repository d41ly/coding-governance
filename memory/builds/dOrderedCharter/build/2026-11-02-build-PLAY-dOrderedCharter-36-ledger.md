# PLAY-dOrderedCharter-36 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-36

Each line is a probe this pass ran at rev-10 of the spec, with the pass applied. No leg, suite or bar ran in the
pass: every plant ran through `tools/playbook/fixtures/row_kind.py --plant` over a throwaway repository, and the
render selftest's row-kind block was lifted from source and run alone by a scratch probe, all 44 rows green (DERIVED at cb020dc12 with this pass applied). Three
row checks were also run stubbed to their broken form, and each guarded plant changed its answer. This record cites
no code line.

**Evidences:** PLAY-dOrderedCharter-36
- First probe — a scratch repository committing `exclude = ["practice.yagni"]` read `policy: check · .governance/policy.toml at <sha> is valid`, exit 0, and `get instructions.exclude --rev HEAD` printed `practice.yagni`; a member `-bad tag` read `member "-bad tag" is not admitted`. S4's policy arm was built on it.
- AC1 — `amends-fixed` exited 1 on one line naming `fixture.alpha`, the field `witness` and `parser=tools/playbook/fixtures/row_kind.py#render_rows`; with `check_rows` stubbed to find nothing it exited 0.
- AC2 — `widen-fixed` exited 1 naming the fixed row `fixture.epsilon` and `a widening of ceiling`; stubbed, it exited 0.
- AC3 — `supersedes-fixed` and `exclude-fixed` each exited 1 naming `fixture.epsilon` and `principle=principle.p16`.
- AC4 — `undeclared` exited 1 reading `note` fixed by its undeclared class; `typed-class` exited 1 naming the key `class` on `ceiling`.
- AC5 — `source-unresolved` exited 1 naming `principle=principle.nowhere`, which names no principle row; `both-declared` exited 1 naming `witness` as declaring both keys.
- AC6 — `exclude-needed --exclude fixture.beta` exited 1 naming `fixture.alpha` and its `needs` field; `exclude-actor` and `exclude-granted` exited 1 naming `fixture.adopter.actor` in `actor` and `fixture.adopter.granter` in `grants`; `exclude-policy --policy fixture.pick=fixture.beta` exited 1 naming `fixture.pick`; `exclude-instance` exited 1 naming `roles.harness.builder`, read through `read_tag_policy`; `exclude --exclude fixture.beta` exited 0 with `fixture.beta` excluded. Stubbed, `exclude-needed` and `exclude-instance` each exited 0.
- AC7 — `classify` printed five patch lines: `grants add widens`, `needs remove widens`, `ceiling low by default->mid widens`, `needs add narrows`, `ceiling low->high widens`; `scalar-off-list` exited 1 naming the value `extreme`. With `derive_patch_class` stubbed to read a remove as narrowing, `needs remove widens` was gone; stubbed to rank gov's off-order value, `ceiling low by default->mid widens` was gone.
- AC8 — `no-direction` exited 1 naming `ceiling` and its `widens []`.
- AC9 — `widenings` printed two widening lines, `fixture.alpha`'s `grants` add over gov `["read"]` and its `ceiling` set `high` over gov `"low by default"`.
- AC10 — `clean` exited 0 with `needs add narrows` and four counts, fixed 2, classify 1, exclude 2, policy 15, each above zero.
- AC11 — the first grep found nothing, exit 1; the second found 25 lines naming `fixture.adopter` tags (DERIVED at cb020dc12 with this pass applied).
- AC12 — owed: its pathspec is unit 49's to correct and is observed at that pass; `help/overlay-rows.md` gained the section on what a repository may not change and how a widening is reported, three lines of it naming `widens`.
- PLAY-dOrderedCharter-35's plants — every row of the render selftest block for that unit stayed green, the `exclude` plant with its one added patch.

**Owed to the close.** The bar, the tags leg, and the RED-first observation of the `New arm:` line: the render
selftest's block running `row_kind.py` over every plant of this unit's acceptance criteria and the clean plant.

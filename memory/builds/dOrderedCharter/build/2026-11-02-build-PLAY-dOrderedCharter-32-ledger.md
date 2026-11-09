# PLAY-dOrderedCharter-32 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-32

Each line is a probe this pass ran at rev-8 of the spec, with the pass applied. No leg, suite or bar ran in the
pass: every plant ran through `overlay.py --fixture --plant` over a throwaway repository, `overlay.py check` ran
over gov's tree, and the policy and tag reads were probed over scratch repositories. This record cites no code
line.

**Evidences:** PLAY-dOrderedCharter-32
- AC1 — `typed-origin` — with no overlay committed, `read_overlay` returned no unit and no key, and a template holding one unit slot rendered byte-identical to the units the slot's selector selects rendered with no overlay code; a committed overlay row typing `origin = "playbook"` made `overlay.py check` exit 1 naming the row and the `origin` field.
- AC2 — `foreign-tag` — the overlay unit `practice.local-rule` exited 1 naming it and the `repo` namespace; `repo-in-gov` — a fixture kit's row tagged `repo.shipped` exited 1 naming the row and the `repo.` tag.
- AC3 — `add-level-3` — the rendered slot read gov's principle unit, gov's two level-3 units, then the repository's level-3 unit, in that order; `add-level-1` exited 1 naming the unit and level 1.
- AC4 — `amends` — pinned with `derive_unit_pin` over gov's text, the composition held gov's open unit then the repository's, its state `amended`; `supersedes` held the repository's unit alone in gov's unit's place, its state `replaced`.
- AC5 — `exclude` — with no `[instructions]` table committed every gov unit composed, each `unchanged`; with the open unit committed under `instructions.exclude` and read at HEAD it was absent, its state `excluded`; the fixed-string grep for the read over the playbook kit found one line, the overlay module's `read_excluded_tags`.
- AC6 — `parsed-open` exited 1 naming the unit and its `parser=` source, and a unit declaring no class read fixed; `typed-fixed` exited 1 naming the typed class as derived; `fixed-by-unresolved`, `fixed-by-floor` and `fixed-by-empty` each exited 1 naming the entry; `overlay.py check` over gov's tree exited 0, printing itself unarmed, since gov tracks no manifest and no overlay yet.
- AC7 — `fixed-amend`, `fixed-supersede` and `fixed-exclude` each exited 1 naming `principle.p1` and `fixed by principle`.
- AC8 — `adopter-key` — `policy.py get adopter.release-train --rev HEAD` read `monthly`; `daily` and an undeclared `[adopter] other`, each the policy file's only revision, exited 2 naming the key; a `[[policy]]` row keyed `budgets.enforce` exited 2 naming the row; after an overlay-only commit `mirror --check` exited 1 naming `legacy_blobs` and passed after `mirror --write`; `guard.py --staged` refused the staged mirror beside a staged overlay change, naming the overlay as its input; `overlay.py check` printed the key with its tag `policy.adopter.release-train` on a line apart from the unit's. A scratch repository carrying copies of the playbook, memory-tree and policy kits answered `gov_tag.py show repo.release-train` with the unit's row, and `policy.adopter.release-train` with no row.
- AC9 — `gov-reads-adopter` — a fixture gov unit triggered on `policy.adopter.release-train.weekly` exited 1 naming the unit; a repository unit with the same trigger composed while the key read `weekly` and not while it read `monthly`.
- AC10 — `write-order` — `write_overlay_units` put two rows into an overlay holding a level-3 row and a `[[policy]]` row by level then tag, the policy row kept; a second write of a held tag raised exit 2 and left the bytes unchanged. A probe of the command's overlay `add` gave the same ordered text and refused a held tag with exit 2.
- AC11 — this pass's commit leaves `.governance/deploy.toml` out; the comment edit is named in the pass's hand-back for the owner's terminal.

**Owed to the close.** The bar, and the RED-first observation of each `New arm:` line: the render selftest's
arm running `overlay.py --fixture` over every plant, each staging its failing case, and `overlay.py check` over
gov's tree with a gov unit planted carrying a parser source and `class = "open"`. The policy mirror
`.governance/policy.json`, a guarded file, reads stale until the landing regenerates it, since its
`legacy_blobs` now records the overlay. The second half of AC11 observes the owner's edit.

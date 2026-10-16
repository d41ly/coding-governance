# Revision — dRedressedBar: TOOL-dRedressedBar-10, the builder's divergence (sibling-spec edits no builder may write)

**Serves:** research TOOL-dRedressedBar-10 TOOL-dRedressedBar-13 TOOL-dRedressedBar-17 TOOL-dRedressedBar-19

## The brief

### Goal
DIVERGENCE: the spec requires one commit that no single role can make. §2 S24, §4 "The sibling rev bumps" and its Files touched, and §6 AC19 put the eight sibling-spec corrections into this unit's own build-pass commit. Those are specs 1 and 3 to 9: S1-S3's revision line, S5, S8, S9, S14, S16 and S22's spec-9 half. AC19 then reads them at `<p10>~1..<p10>`. scratch-guard blocks that write. Under `.claude/roles.json` only gov-spec-writer may write spec files, and a gov-builder may change only the status and date cells of the spec it is routed to. So the one commit AC19 reads cannot be made by either role. The spec would have to say one of two things. Option one: the sibling corrections are a separate gov-spec-writer pass with its own commit (M6's "a review's fixes folded in"); this unit's build pass writes only `tools/govkit/entries/settings-merge.kit.toml`, `tools/govkit/matrix.py` and the acceptance ledger; and AC19, plus S24's "in this pass", reads the spec-writer's commit instead of `<p10>`. Option two: split the unit into a product unit and a spec-correction unit.

The builder's further findings, for the same revision: unit 20 shifted every `govkit.py` line after about 870 by +3 (`EPOCH_ROLES` now at :12938; §4's cites 1450-1456, 5913-5917, 6313-6324, 7740-7764 and 11104-11126 are each +3); spec 4's §5 migration line "once unit 7 bumps the two kits" is the same false fact S8 corrects but S8 names only three addresses; and S9's list "1 to 6, 8 and 9" omits unit 20, also ordered before unit 7.

### Items
1. **Take option one, and do the folding now, in this pass.** Apply every sibling-spec correction unit 10 owns to specs 1 and 3 to 9, each as a rev bump with its §9 line naming report id and unit 10. Include the spec-4 §5 migration line and S9's list with unit 20 added. CLOSED specs take the correction as a records fix with their status unchanged.
2. **Revise spec 10** to a new rev: S24 and §4 say the sibling corrections landed in this spec-writer pass, by its commit; §4's Files touched for the build pass lists only `tools/govkit/entries/settings-merge.kit.toml`, `tools/govkit/matrix.py` and the acceptance ledger; AC19 reads the spec-writer pass's commit, named as `<s10>`, not `<p10>`; the govkit.py line cites move by +3.
3. **Apply the same check to specs 13, 17 and 19.** For each S-item or AC that requires the builder's own commit to edit another spec, do the same: fold those sibling corrections now in this pass, and revise the unit so its build pass writes only product files and its AC reads this pass's commit. Name each moved item in the unit's §9 line. A unit with no such item is left alone, and the report says so.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades units 10, 13, 17 and 19 READY. No READY unit's build pass names a spec file other than its own in Files touched. `bash tools/memory-tree/check-memory-hygiene.sh --staged` over the staged specs prints no check 12 or 25 line for them.

### Gates
`memory hygiene` · `kit epoch`

### Non-goals
- No code: the product half of unit 10 stays for its builder.
- No status change to any spec.
- No merge to local main and no push without the owner's ask.

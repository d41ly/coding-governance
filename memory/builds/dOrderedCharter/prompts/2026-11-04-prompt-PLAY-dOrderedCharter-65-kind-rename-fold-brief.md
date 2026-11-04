**Serves:** research PLAY-dOrderedCharter-65

# Brief: the kind rename's outside writes — three dShippedRelease specs

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. Unit 65 renamed the kind tags `kind.kit`, `kind.layer` and `kind.practice` to `kind.tool-kit`,
`kind.product-layer` and `kind.charter-practice`, and the practice factory to `core.py new charter-practice`.
Its spec leaves the readers outside this build to the main loop. Three DEFERRED specs of dShippedRelease still spell
the old names: DEPL-dShippedRelease-10 (twelve hits), -15 (five) and -78 (two). A grep that keeps reading the old
spelling would pass vacuously after the rename.

## The brief

### Goal

Re-point every old kind spelling in those three specs to the new one, so each still describes the tree unit 65 left.

### Items

1. Edit only these scratch copies:
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold4/2026-10-30-spec-DEPL-dShippedRelease-10.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold4/2026-10-30-spec-DEPL-dShippedRelease-15.md`
   - `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold4/2026-10-30-spec-DEPL-dShippedRelease-78.md`
   The main loop moves them in.
2. Replace each old spelling with the new one: `kind.kit` becomes `kind.tool-kit`, `core.py new kit` becomes
   `core.py new tool-kit`, and likewise for layer and practice.
   - Fix each AC whose grep would now pass vacuously, so it greps the new spelling.
   - Re-read each hit in context. A hit that names a kit, a layer or a practice in plain prose, not as the kind tag or
     the factory, stays as it is.
3. Each spec bumps its **Status:** rev by one, dated 2026-11-04, keeping `DEFERRED`. Each history entry names the S
   or AC ids it touched, and cites this brief and unit 65 as the cause, an outside write recorded by dOrderedCharter.
4. The listed citations stay byte for byte. New text uses no section-sign form, no method-rule form, no hygiene
   check-number form and no `path:line`.

For the run:

- Writes stay in the three scratch copies.
- Do not commit and run no check.
- Return each spec's new rev and the hits you changed and kept.

### Acceptance

- No old kind spelling or old factory name is left in the three copies, other than plain prose.
- Each Status line is one rev higher, and each history entry names the ids it touched.

### Gates

The memory-hygiene hook and the spec-token check, at the main loop's commit.

### Non-goals

- No code.
- No other spec.
- No change of meaning beyond the rename.

### Limitations

The items above, "For the run".

### Reuse

Unit 65's spec and `tools/playbook/kinds.toml`.

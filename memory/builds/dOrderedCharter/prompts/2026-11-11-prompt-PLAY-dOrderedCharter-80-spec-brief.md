**Serves:** research PLAY-dOrderedCharter-80

# Brief: spec PLAY-dOrderedCharter-80 — the close bar's own product reds

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The close's bar over `daf84987f` failed eight legs. The main loop fixed its own record reds; a read-only
attribution (`memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-1-close-bar-attribution-researcher.md`)
traced the product reds to units 31, 78 and 55.

## The brief

### Goal

Write spec PLAY-dOrderedCharter-80, one fix unit at order 42 that clears every product red this build caused on its own bar, each
by its narrowest fix, the way PLAY-dOrderedCharter-77 cleared the previous close's.

### Items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold80/2026-11-11-spec-PLAY-dOrderedCharter-80.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md`; status line `DEFERRED · rev-1 · 2026-11-11 · node a ·
   Tier-2 · base <HEAD short sha> · streams playbook · order 42 · advances PLAY-dOrderedCharter-38`. Read PLAY-dOrderedCharter-77's
   spec as the shape of a close-fix unit.
2. **The reds and the fix each takes, as the attribution found them; confirm each at HEAD before you specify it:**
   - install-prefix: `tools/govkit/matrix.py` near line 848 spells the playbook kit directory as a literal; derive it from the
     `playbook-render` descriptor already in scope, as the `settings-merge` use near line 330 does.
   - dead-path carriers: `tools/govkit/registry.toml`'s two `[[retired]]` surfaces naming the deleted adopter must keep naming it
     (the step gate requires it); add two rows to `tools/dead-path-waivers.txt` naming them, with reasons.
   - govkit selfcheck (a): the `playbook render selftest` leg's guard pathspec for the root template falls into no declared class in
     check 7c of `tools/govkit/govkit.py`; add a derived class for root-level files a descriptor ships through a root-relative
     `[[files]]` include, derived as the root confs are.
   - govkit selfcheck (b): the `micro-format definitions` leg in `tools/govkit/entries/check-microformats.kit.toml` names a file only
     `playbook-render` ships; drop that argv element and have `tools/check-microformats.sh` find the template beside the playbook kit
     through an inline kit-dir resolver, gov's root as the fallback; its self-test and the matrix's argv-resolution arm follow.
   - kit epoch: `derive_epoch_state` in `tools/govkit/govkit.py` reads a fileless entry whose `version_from` is `none` as broken;
     return the skip verdict for it, keep `broken` otherwise, and never run `git log` with no paths. This also unblocks the lander's
     mint.
   - runbook parity: `tools/govkit/check_runbook_parity.py`'s `PROBLEM_PIN` moves 18 to 17 for the retired entry, with a
     re-measured note.
   - acceptance matrix, default and aged installs: `tools/govkit/matrix.py` shapes 6 and 7 write `deploy.toml` by hand; give both
     the placeholder-stub answers shape 5 derives, through one helper now used three times, and give shape 6 the default selection's
     `kits`.
   - acceptance matrix, scratch install: the render self-test (`tools/playbook/render_playbook.py --selftest`) reds four arms
     inside the matrix's shape-5 install, which the main loop's probe kept and re-ran. Each arm leans on a file gov's own tree has
     and an installed target does not:
     - `gov's template renders without drop_blocks cross-os` and `gov's template renders with drop_blocks cross-os` refuse because
       the document registry `tools/playbook/documents.toml` does not read in the fixture they build;
     - `the unattended start line renders once, with the attended /build line directly under it` refuses because the drive
       section finds no descriptor for the `unattended` kit at `{prefix}/unattended/kit.toml`;
     - `a v4.0 template naming a legacy placeholder: --check refuses it` exits 0, its `--check` reading the template beside the
       engine rather than the planted one.
     Specify the fix that makes each arm build what it reads in its own fixture, or ship what the arm reads with
     `playbook-render`, whichever the arm's intent and the reuse rule favour; never skip an arm by environment.
3. **Out of scope:** the policy check's five `review.*` reader findings (inherited from the merge base, dFairHearing's); gov's
   `.governance/install.json` receipt, which the lander's update rewrites.
4. The spec-token check grades a live spec's acceptance bullets word by word: no acceptance command whose words include an
   untracked path, no `path#symbol` in an acceptance bullet, no suite as the observation, each backticked span on one line, every
   tripped leg on the gates section's leg line. Cite code as `path#symbol` or a blob-pinned line. Every fork carries a resolution
   mark; every new fact is pinned on its own line outside backticks; every minted function passes
   `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Acceptance

- Spec 80 builds as written over HEAD, and each criterion observes one red leg's verdict line going green.

### Gates

None run on the repository: this is a scratch write. The main loop commits the spec and runs the spec-token check with it live.

### Non-goals

- No code. No edit outside the scratch copy. No fix outside this build's own reds.

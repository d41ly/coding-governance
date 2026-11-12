# dOrderedCharter — mid-build lint reading after units 18, 16, 61, 62 and 17

**Serves:** journal PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62

Read at the main loop at `75b579fb5`, against the same commands at the pinned base `8bec4cefd` in a detached worktree.

- `python tools/playbook/check_layers.py` exits 0: 39 allowed, 0 red, 0 contract reds.
- `python tools/lexicon/lexicon.py` reads OK.
- `sh_hygiene.py memory/project/substitution-fed-loops.txt` exits 0.
- `sh_hygiene.py --location-probes` exits 1 on one site, the same at base: inherited.
- `sh_hygiene.py --temp-names` exits 1 on 37 file rows, the same 37 at base: inherited.
- `sh_hygiene.py --spawn-idioms` exits 1 at base (422 file rows) and at HEAD (423). This run's own delta, each in a
  file already red at base: `skills/session-kickoff/manifest-check.test.sh` `path-subst` 8 → 9,
  `tools/unattended/check-unattended.test.sh` `path-subst` 10 → 11, `tools/playbook/adopt-playbook.sh` a new `var-pipe`
  site; `tools/check-wiring.test.sh` `pure-fn-subst` fell 10 → 9. Owed at the close: convert the three to the no-fork
  form, or declare them, in the closing fix batch.

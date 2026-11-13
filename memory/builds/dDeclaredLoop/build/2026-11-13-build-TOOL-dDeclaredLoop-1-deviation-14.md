# TOOL-dDeclaredLoop-1 deviation 14 — the new kit's registry rows and three respelt lines the spec's file estimate did not list

**Serves:** deviation TOOL-dDeclaredLoop-1

- **Departs from:** `TOOL-dDeclaredLoop-1@rev-5` [§4 Files touched]
- **Hand-off:** spec-to-code
- **Before:** `TOOL-dDeclaredLoop-1`'s spec at rev-5 estimates the files the pass touches, and S1 gives the loop descriptor an id, a layer, a version and an empty `requires`.
- **After:** the pass also writes a `loop` row in `tools/playbook-kit-waivers.txt`, a `loop definition` row in `tools/govkit/subject-pins.tsv`, a `[[usage]]` row in `tools/govkit/usage.toml` for each of the kit's commands, and the kickoff manifest's re-stamp in `memory/guides/SESSION-KICKOFF.md`; the loop descriptor carries `[adopt]`, `[check]`, an `[[outcome]]` and a `[[gate_leg]]` row, as every descriptor under `tools/` does; and one line each of `tools/playbook/README.md`, `tools/playbook/tag_index.py` and `tools/govkit/upgrade_steps.py` is respelt so it no longer spells the word `loop` as a path segment.
- **Cause:** builder discovery
- **Reason:** each row answers a join that reads the registry or the leg manifest: the playbook parity gate reds a registry kit the charter never names and no waiver excuses, and a charter loop section is a non-goal of this unit; the subject pins hold one row per leg of the manifest; the docs leg tests each command `help/loop.md` shows against a declared usage row; the manifest's `watch:` list names `tools/gate-legs.json`; and the deployer reads `[adopt]` and `[check]` from every entry. The three respelt lines were clean until a kit directory named `loop` existed: the install-prefix ban reads a kit's home before a file name, or as a quoted path segment, as a kit path, and its `--list` mode named exactly those lines once the kit landed.
- **Evidence:** `named_in_playbook` in `tools/check-playbook-parity.sh`, the header of `tools/govkit/subject-pins.tsv`, the header of `tools/govkit/usage.toml`, the `watch:` line of `memory/guides/SESSION-KICKOFF.md`, the output of `bash tools/check-install-prefix.sh --list` before and after the respelling, and the pass commit of `TOOL-dDeclaredLoop-1`.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** TOOL-dDeclaredLoop-1
- **Surface:** tools/playbook-kit-waivers.txt, tools/govkit/subject-pins.tsv, tools/govkit/usage.toml, the loop descriptor, and one line each of tools/playbook/README.md, tools/playbook/tag_index.py and tools/govkit/upgrade_steps.py

# TOOL-dWitnessedBar-12 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-12

This pass ran no merge bar, no self-test suite and no gate leg except the naming lexicon. Every
criterion was checked on node d on 2026-11-19 with a probe of the unit's own code: a `python -c`
call, the three new `gov_tag.py --fixture` plants, the two key-set arms and the gov canary's tag arm
cut out of their files and run alone, `owed_rows.py`'s probe over a scratch fixture repo under
`%TEMP%`, and govkit's emitter called in process over a scratch target. Still owed to the close: the
RED-first observation for each of the four `New arm:` lines in spec section 7, every leg that
section names, AC5's `python owed_rows.py --selftest`, and AC7's `govkit.py selfcheck`. The role
hook refused the last one in this pass.

**Evidences:** TOOL-dWitnessedBar-12
- AC1 — `tools/gate-legs.json` — a probe read the 198 rows (DERIVED) after the pass. Every row carries a
  `tag` matching `leg.<seg>.<seg>`, within `TAG_MAX_BYTES`, and there are 198 distinct values. Each
  returns None from `tag_index.derive_tag_fault` against the registry's 18 words, which now include
  `leg`. Each of the 70 descriptor-backed rows opens with its owner segment and equals its
  descriptor row's `tag`. The policy kit's leg reads `leg.policy-kit.policy-check`. The lexicon's
  `--tags` graded all 198 with 0 refused. The gov canary's G10 arm, run alone, was green over the
  real manifest. Over a copy with row 5's tag set to row 3's it was red, printing
  `legs 'micro-format definitions' and 'line length' share the tag leg.check-microformats.micro-format-definitions`.
  Over a copy with one row's tag removed it was red, naming `playbook parity`.
- AC2 — `grep -cE '^ns = "(leg|check|pack)"' namespaces.toml` printed 3 in `tools/playbook/`.
  `grep -cE '^\| .(leg|check|pack). \|' help/tags.md` printed 3 at the root. The registry holds 18
  `ns` rows, and the page now says "Eighteen".
- AC3 — `python gov_tag.py --fixture --plant leg-rows` exited 0. `where leg.gate-lint.shell-hygiene`
  resolved to `tools/gate-legs.json@1310a3e1:2`, the manifest row, and the plant printed
  `tags: plant leg-rows · where: rc=0, check: rc=0`. Its playbook-render selftest row is in the
  `run_plant_rows` heredoc of `tools/playbook/adopt-playbook.sh`. The duplicated-tag half is AC1's,
  on the gov canary.
- AC4 — `python gov_tag.py --fixture --plant pack-rows` exited 0 printing
  `members pack.ratchet pack.tags, check: rc=0` over a fixture manifest with `"pack": "tags"` twice
  and `"pack": "ratchet"` once. `--plant check-rows` exited 0. Its two kits each hold `[check]` and
  `[[numbered_check]]` with `id = "23"`, and it printed
  `members check.memory-tree.23 check.unattended.23, check: rc=0`. With the rows removed it printed
  `tags: unarmed check (0 not graded)` and `without [[numbered_check]]: 0 members, check: rc=0`. An
  in-process call of `extract_check` and `extract_command` over one descriptor holding `[check]`,
  `[[numbered_check]]` and `[[command]]` yielded `check.memory-tree.23` and
  `command.memory-tree.new`.
- AC5 — `LEG_KEYS` — arm 1a and `keyset_probe` were cut from `run-gates.test.sh` and run with the
  file's own `LEG_KEYS` line. Over a fixture row carrying `tag`, the arm left `fail=0` and the probe
  exited 0. With `tag` cut from `LEG_KEYS`, the arm set `fail=1` and the probe exited 1. The arm left
  `fail=0` over the real manifest. `grep -c '^KNOWN = ' run-gates.test.sh` and
  `grep -c 'KNOWN cop' owed_rows.py` each printed 0. `read_known_copies` returned the 16 keys of
  `LEG_KEYS`. Over a scratch fixture repo, `run_probe` exited 0 for a clean tree, exited 1 for a
  stray key with the owed row ending "`enforce` in LEG_KEYS, with its control pair", and exited 2
  naming the missing `LEG_KEYS="..."` line once the canary held none. The close owes
  `python owed_rows.py --selftest`.
- AC6 — `LEG_KEY_FLOORS["tag"]` — `write_gate_legs` was called in process over a scratch target
  whose runner read 1.50, one minor below the floor (1, 51). It wrote
  `{'name': 'fx leg', 'argv': ['true'], 'subject': 'repo'}` with no tag. At 1.51 it wrote the
  descriptor's `'tag': 'leg.fx.fx-leg'` beside the same keys. Neither run raised a problem.
- AC7 — `govkit.py selfcheck` — the role hook refused it as the leg "govkit selfcheck", so the close
  owes the observation. 7h compares `leg.get("tag")` against the manifest row's, presence included,
  and the failure line names the entry, the leg and both tags. The selftest's new run f stages
  `tag = "leg.push-main.drifted"` on `pre-push self-test` and asserts that line.

# PLAY-dOrderedCharter-4 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-4

Each line is a probe this pass ran at rev-5 of the spec, with the pass applied. No leg, suite or `--selftest`
ran in the pass: the playbook render arms were called alone through a scratch script importing
`tools/playbook/render_playbook.py#check_map_arms`, and the replay was run by hand over a scratch fixture
repository. The one plant of `instruction_units.py fixture` this pass changed, `map-held`, now expecting the
preset line last, was run alone and printed green. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-4
- AC1 — `check_map_arms` over a scratch target whose registry holds `AGENTS.md` at level 0 and `roles/a.md` at level 5, neither held: `run_map` exited 0 printing `[AGENTS.md · Level 0 · the instruction map: rebuild the hierarchy from it before acting]`, the eight level lines, `preset — none: presets join the policy reader at dKeptSession; a key's source: policy.py get <key> --explain`, then `[/AGENTS.md]`; the lines between the envelope pair equal the `- ` lines of the charter section `render` wrote from the same target, the preset line included. Over gov's own tree, `python tools/playbook/instruction_units.py map` exited 0 at 1005 bytes, the held line before the preset line.
- AC2 — six level-4 rows of long paths: the level-4 line ended `… (+<k>)` within 160 bytes; with nine held rows added the verb exited 2 printing one `instruction-map: <bytes> over MAP_CAP_BYTES` line. A registry with no `doc.charter` row and an absent registry each exited 2 with one `instruction-map:` line. Staged red: with the preset line filtered out of the verb's output, the two AC1 arms failed and the other four held.
- AC3 — `git grep -n -e "Level 0 ·" -e "def render_instruction_map" -- tools/playbook/` printed one definition of `render_instruction_map`; its two `Level 0 ·` hits are arms, an envelope plant and the AC1 arm, and none sits in `run_map`.
- AC4 — in a scratch repository whose one tracked `playbook/instruction_units.py` prints an envelope pair, `--card --replay --session p2` exited 0 printing those two lines, the stored card, then one `now —` line, and `cmp` found the card file unchanged.
- AC5 — with no module the first replay line read `map — skipped: no playbook instruction map resolves in this tree`, then the card and one `now —` line, exit 0; a stub printing `boom` and exiting 3 gave `map — skipped: boom`; a stub sleeping five seconds under `CARD_MAP_BOUND=1` gave `map — skipped: the map did not answer within 1s` in 2.3 seconds, and no `.map.` scratch file was left under the card directory.
- AC6 — `--card --write --session p2` over the same stub printed no line opening `map — ` or `[`.
- AC7 — `git diff --stat HEAD` over the two fragment files printed nothing.

**Owed to the close.** The bar; `bash tools/check-wiring.sh` naming one `card` line for AC7; `python tools/playbook/gov_tag.py check`; the instruction grammar and render gate over the re-rendered `AGENTS.md`; and the RED-first observation of both `New arm:` lines — the `map —` block of `skills/session-kickoff/manifest-check.test.sh` with its updated AC5 replay arm, staged by moving the map after the card, and `check_map_arms` in the playbook render selftest, staged by dropping the preset line. `AGENTS.md` now measures 23274 bytes against its 23161-byte size row, a warning under `budgets.enforce = "warn"`; a raise needs its decisions row first.

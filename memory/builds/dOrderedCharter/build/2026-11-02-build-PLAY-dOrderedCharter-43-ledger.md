# PLAY-dOrderedCharter-43 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-43

Each line is a probe this pass ran at rev-4 of the spec, with the pass applied. No leg, suite or `--selftest`
ran in the pass: the renderer and the adopter were run by hand over fixture repositories under the short temp
path. Gov's switch, the leg argv in `tools/gate-legs.json` and the second line of gov's `CLAUDE.md`, is not in
this pass: the spec's rollout lands it only once the main loop has recorded unit 8's live compaction fixture
green, and that has not been observed. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-43
- AC1 — `--render-scope entry-files --card` — over a fixture with aliases `claude gemini copilot`: exit 0, `CLAUDE.md` read by `od -c` as `@AGENTS.md`, a newline, `@.claude/orientation-card.md`, a newline; the new `.gemini/settings.json` held `"fileName": ["AGENTS.md", ".claude/orientation-card.md"]`; the output carried `card — not delivered: copilot has no native import` and the Codex line. Over a fixture whose `CLAUDE.md` was the one line `@AGENTS.md`, with no `--force`: exit 0 and the two lines. A foreign `CLAUDE.md` still refused without `--force`, exit 1; an existing settings file without the card got the merge-by-hand refusal naming the two-file array.
- AC2 — `--render-scope entry-files` without `--card` — `CLAUDE.md` read by `od -c` as `@AGENTS.md` and one newline, eleven bytes; the settings file held `"fileName": "AGENTS.md"` and the printed lines were the scope's own; a two-line pointer re-rendered without `--card` read as current.
- AC3 — `--check-render --card` — scoped over AC1's fixture: exit 0. Unscoped over a committed fixture holding a two-row renderers table, a legacy list naming both files and a stub parity gate, with `GOV_DEFAULT_BRANCH=main`: exit 0. With the second line of `CLAUDE.md` deleted, each exited 1 printing `CLAUDE.md lacks the card import line`; without `--card` the one-line pointer was green both ways. A settings file listing `AGENTS.md` alone red the scoped check under `--card`, naming `.gemini/settings.json`.
- AC4 — `git grep -n -e "orientation-card" -- tools/agent-instructions/` — printed nothing, exit 1. `adopt-agent-instructions.sh --aliases "claude gemini copilot" --card` wrote `CLAUDE.md`, the settings file and the copilot copy equal by `cmp` to the renderer's own `--card` render; its `--check --card` exited 0, then 1 naming `CLAUDE.md` once the card line was deleted, and 0 for the same file without the switch.
- AC5 — owed: the commit that lands gov's switch reads both legs' argv for `--card`, after unit 8's live fixture is recorded green here.
- AC6 — `find <fixtures> -name AGENTS.override.md` — after renders under each of `symlink`, `pointer` and `copy`, each with and without `--card`, over aliases `claude gemini copilot cursor windsurf`: printed nothing.
- AC7 — owed: gov's `CLAUDE.md` at the commit that lands the switch, and the scoped check with the switch over that tree.

**Owed to the close.** The bar; `python tools/playbook/gov_tag.py check`; AC5 and AC7 with gov's switch, after
unit 8's live fixture is green; and the RED-first observation of each `New arm:` line: the `--card` arms of
the renderer's scope cases in `tools/playbook/render_playbook.py#check_scope_arms`, staged by deleting the import line, and arm 13 of
`tools/agent-instructions/adopt-agent-instructions.test.sh`, staged by dropping the switch from the argv the
adopter execs. `AGENTS.md` measures 23279 bytes against its 23161-byte size row, unchanged by this pass.

**Serves:** journal TOOL-dTotalRecall-20
**Caused-by:** TOOL-dTotalRecall-20

# TOOL-dTotalRecall-20 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `f8156b855` from [2026-11-22-prompt-TOOL-dTotalRecall-20-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-20-build-brief.md), recorded whole; the pass commits are `f6bdef7b4` and `c18aaf8ff`.

## Why

TOOL-dTotalRecall-20 is built as its spec states. The pass commit is f6bdef7b4: it carries `Pass: TOOL-dTotalRecall-20`, sets the spec header to CLOSED, and includes RUN.md, the acceptance ledger, the regenerated symbols.json and the index generator's rewrites. A follow-up commit, c18aaf8ff (`Pass: none`), stops the new forward arm from picking up repository and remote settings from the calling environment. The bug-class checklist selected those environment classes on the pass commit.

## Summary

Built TOOL-dTotalRecall-20 in two commits: the pass commit f6bdef7b4 and a follow-up c18aaf8ff (`Pass: none`). The spec header now reads CLOSED · rev-5 · 2026-11-23. No gate, suite or bar ran.

**What was built**
- Three `[[upgrade]]` rows in tools/memory-tree/kit.toml.
- Three step programs:
  - tools/govkit/steps/memory_journal_alias.py
  - tools/govkit/steps/memory_front_matter.py
  - tools/govkit/steps/memory_retag.py
- tools/govkit/shims.py gains the `verb` kind:
  - It parses the `from-words` and `to-words` keys.
  - It renders a `run_shim_<slug>(argv)` block.
  - `--write` inserts or replaces the block; `--check` compares it, and refuses a block still present once its row is closed.
  - The py prelude is now held once for both templates. The existing py, module, sh and js renders are byte-identical to HEAD; I checked each against its HEAD render.
- tools/govkit/shims.toml has its two rows and a new header comment.
- tools/memory-tree/gen_build_index.py:
  - The two scaffold dispatch lines now call the rendered blocks above `main`.
  - New mode `--print-front-matter-findings` (`cmd_print_front_matter_findings`).
  - New arm `test_forwarded_new_spec`, registered in `cmd_selftest`.
- tools/playbook/gov_tag.py gains the `anchors <path>` verb (`print_heading_anchors`).
- tools/govkit/selftest.py gains `check_memory_tree_steps`.
- help/shims.md and help/upgrade-steps.md are updated.

**Write set:** I declared `help/shims.md`, `memory/LIVE.md`, `memory/backlog/TOOL.md` and `memory/builds/dTotalRecall/README.md` with `--dispatch`. Neither call was refused. The ledger is memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-20-1-acceptance-ledger.md.

**Checks that ran, each a probe of this pass's code and not a gate:**
- **AC1 to AC8:** each step program and the forward, run over fixture repositories under %TEMP%. These stand in for the `govkit selftest` and `build-index selftest` legs.
- **AC3:** `shims.py --check`, with one byte edited and then with the row closed: exit 1 both times; exit 0 once restored. This stands in for `govkit selfcheck` arm 11.
- **AC7:** `upgrade_steps.py list` prints the three rows as 28 to 30, in order. Each witness exits 0 against gov's own root; the journal step read 5,059 journal records there. This stands in for the `upgrade-walk` leg.
- **AC9:** the spec's three greps. This stands in for the `docs` leg.
- **Arm functions:** I called `check_memory_tree_steps` and `test_forwarded_new_spec` once each from `python -c` with a stub reporter. All 13 and all 3 checks were green, the forward arm again under `GOV_REMOTE=nosuch`.
- **Naming lexicon:** `--suggest` passed every new function name; `--measure` left `VERB_OFFENDER_PIN` at 1435.
- **Bug-class checklist:** ran over both commits. It led to the environment fix in c18aaf8ff.

**Owed to the close (main loop):**
- **New arm** tools/govkit/selftest.py (AC1, AC4 to AC8): needs its RED-first observation, staged by making the retag write under `derived`.
- **New arm** tools/govkit/govkit.py, selfcheck arm 11 (AC3): staged by changing one byte in a rendered block. No code edit was needed; the existing arm already grades `verb` rows.
- **New arm** tools/memory-tree/gen_build_index.py, `test_forwarded_new_spec` (AC2): staged by the forward dropping `--order`.
- **The spec's legs on the spec's gates section:** govkit selftest, govkit refusal join, govkit acceptance matrix, govkit selfcheck, recall floor arms, tier2-review self-test, build-index selftest, memory-hygiene self-test, policy fixtures, playbook render selftest, lexicon naming predicates, upgrade-walk, docs, kit epoch and memory hygiene.

**Choices the spec did not state, recorded as `Decided:` trailers on f6bdef7b4:**
- memory_front_matter.py and memory_retag.py import `run_index_mode` from memory_journal_alias.py, so the three steps share one way to run the index generator.
- A verb row's warning line and journal entry name each script path together with its words, so they say which flag moved.
- `down` reads the policy key like the other verbs, as S5 states. It therefore restores only while the key is `retag`.
- The steps page now says "Seven moves" instead of six.
- No kit version moves on the branch.

**Left untouched, for the owner to know:**
- A comment in tools/govkit/govkit.py beside selfcheck arm 11 still says gov ships no shim yet. That file is outside this unit's write set.
- `gov_tag.py anchors` has no fixture plant of its own. The retag arms in govkit selftest exercise it.

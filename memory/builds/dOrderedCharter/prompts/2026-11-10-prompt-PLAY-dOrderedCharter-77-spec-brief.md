**Serves:** research PLAY-dOrderedCharter-77

# Brief: spec 77 — the close bar's own product reds, in one unit

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. The close's full bar over `3c63fe888` failed sixteen legs; a read-only attribution
(`prompts/2026-11-10-prompt-PLAY-dOrderedCharter-1-bar-attribution-researcher.md`) found fifteen of them this build's own. The
main loop fixed the record-only ones at `de36424bf` and `51cd8b402`. This unit is the rest: every fix that writes under `tools/` or
`skills/`, batched as the build method batches minors, one unit naming them all.

## The brief

### Goal

Write spec 77, a Tier-2 unit whose pass leaves each of the legs below green over the tree, changing no behaviour a leg does not
demand.

### Items

1. **Where you write.** Write the spec at `memory/builds/dOrderedCharter/spec/2026-11-10-spec-PLAY-dOrderedCharter-77.md`; no builder
   is running. Header: `**Status:** DEFERRED · rev-1 · 2026-11-10 · node a · Tier-2 · base <HEAD's short sha> · streams playbook ·
   order 37 · advances PLAY-dOrderedCharter-38`, plus the `**Derived:**` binding line every promoted unit of this build carries. Edges
   `none`, its dependencies on CLOSED units named in prose: a consumes-from into a CLOSED spec reds the edge check.
2. **The fixes, each confirmed at HEAD before you spec it** (the attribution cites file:line at `3c63fe888`; lines may have moved):
   - shell hygiene: the fork idioms added on this branch in `skills/session-kickoff/manifest-check.test.sh`,
     `tools/agent-instructions/adopt-agent-instructions.test.sh` and `tools/check-template-size.test.sh` take their no-fork forms.
   - install-prefix: every kit path the branch spelled literally (the two test suites above, `tools/playbook/overlay.py`,
     `pins.py`, `practice_census.py`, `render_playbook.py`, `tools/roles/render_agents.py`) and the five `SKILL.template.md`
     envelope paths derive from the file's own location, `resolve_kit_dir` or a drained token; the gate takes no waiver.
   - harness arms: `tools/check-template-size.sh`'s check 8 branch 1 gets an arm stating its failure text.
   - dead-path carriers: the eight lines naming the harness's auto-memory index `MEMORY.md` get rows in `tools/dead-path-waivers.txt`.
   - remote literals: `tools/playbook/overlay.py`'s fixture assembles the remote name, as `check-remote-literals.sh` does.
   - govkit selfcheck: an `[[exempt]]` row in `tools/govkit/registry.toml` for `card-compaction.fixture.sh`, and
     `tools/govkit/entries/push-main.kit.toml`'s comment names no adopter now that the playbook kit ships the file.
   - govkit acceptance matrix: the three new selftest legs' expectations in `tools/govkit/matrix.py`; the policy kit's lookups the
     branch made hard, resolved under the fork rule (the playbook entry requires `policy` and the scratch install carries it, or the
     readers degrade as their older sibling does); and the `render_playbook.py --selftest` TOML decode error, found and fixed.
   - docs: `[[usage]]` rows in `tools/govkit/usage.toml` for the commands `help/charter.md` and `help/roles.md` show unrowed.
   - lexicon: rename `ask` in `skills/session-kickoff/card-compaction.fixture.sh` and `fold_text` and `strip_text` in
     `tools/playbook/pins.py` to declared verbs, each through `python tools/lexicon/lexicon.py --suggest`.
   - held legs budgeted: rows in `tools/run-gates/selftest-budgets.txt` for `core selftest`, `instruction units selftest`,
     `instruction edits selftest`, `tags positional selftest` and `tags bundle selftest`, from the main loop's measured walls, which it
     hands the builder.
   - tags ceiling: the leg's ceiling evidence, measured by the main loop alone over the tree at 210 s (DERIVED at de36424bf), against its 180 s (PINNED)
     ceiling, in the evidence file the ceilings derive from.
   - check 23 tokenizer: `tools/memory-tree/check-memory-hygiene.sh` extracts a criterion's backticked tokens one physical line at a
     time, so a span that wraps a line pairs the wrong backticks and no honest ledger token can match (PLAY-dOrderedCharter-13 AC5).
     Join a criterion bullet's lines before extracting, with an arm stating the case.
   - unit 76's unarmed refusal: `tools/govkit/docs_leg.py#check_unit_lines`' refused state gets an arm.
3. **Owed observations the pass records** in their own units' ledgers, each run as its criterion says: PLAY-dOrderedCharter-18 AC3,
   PLAY-dOrderedCharter-65 AC3 and PLAY-dOrderedCharter-72 AC6.
4. **The spec-token check grades a live spec's acceptance bullets word by word**: write no acceptance command whose words include a
   path that is not a tracked file, and keep each backticked span on one line.
5. Every section 8 fork carries a `RESOLVED` mark in the template's shape. Every function name it mints passes `--suggest`.

### Acceptance

- Spec 77 names, per leg, the criterion that shows the leg green after the pass, and builds as written over HEAD.

### Gates

Run `python tools/playbook/writing_practice.py check pinned-facts` and memory hygiene's fork check over the spec, and report each.

### Non-goals

- No code. No edit to any CLOSED spec.

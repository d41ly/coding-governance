# aDistilledCharter — acceptance ledger

**Serves:** journal TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-8

Observed on node `a` on 2026-10-09, over this build's branch. Every red proof was a staged break
observed red and then removed; none was left in the tree.

**Evidences:** TOOL-aDistilledCharter-1
- AC1 — `python tools/playbook/render_playbook.py --selftest` — the continuation-line arm passes, and fails with the grade replaced by a no-op
- AC2 — `ONE_LINE_MAX` — the over-length arm passes, and fails with the grade replaced by a no-op
- AC3 — `<!-- one-line -->` — the unclosed and nested arms pass, and fail with the grade replaced by a no-op
- AC4 — `{{ADOPTER_RULES}}` — the default and multi-line arms pass, and fail when the trailing-newline strip is undone
- AC5 — `bash tools/playbook/adopt-playbook.sh --selftest` — prints `render_playbook.selftest OK — 41 arm(s)`

**Evidences:** TOOL-aDistilledCharter-2
- AC1 — `python tools/playbook/render_playbook.py --selftest` — two checkouts and a reordered fleet render the same pairs; the arm fails with the fleet read unsorted and ungraded
- AC2 — `ab` — the repeated tag, repeated identity and two-letter tag arms each see a refusal, and fail with the fleet ungraded
- AC3 — `[nodes.q]` — the override moves one cell, and the unknown-tag and unknown-key arms refuse; they fail with the override reader stubbed
- AC4 — `--claim-node` — a scratch copy of the engine holding `fleet.toml` with a, b and d claimed `c`, refused the same identity in another case, and refused once `playbook.kit.toml` sat beside it
- AC5 — `drop_blocks = ["node-table"]` — renders with a `retired` note, and refuses with `RETIRED_BLOCKS` emptied
- AC6 — `## Node registry` — `--check` prints the note for a registry outside the region and not otherwise; the arm fails with the note's search disabled
- AC7 — `memory/archive/coding-governance-agents.template-v-3-5.md` — rendered with BASE's deploy answers under the rev-2 engine, writing the region and noting `legacy    template v3.5 … reseed`; the two v3-template arms against the shipped descriptor fail when the `TAG_A` row leaves it

**Evidences:** TOOL-aDistilledCharter-3
- AC1 — `bash tools/check-playbook-parity.sh` — prints `pairs in agreement`, naming no retired pair
- AC2 — `README.md` — appending `see the charter's §7` failed check 16 naming `README.md:118`; restored, the gate passed
- AC3 — `bash tools/check-playbook-parity.sh` — prints `825 line(s) carry a section sign` over the clean tree
- AC4 — `memory/guides/MERGE-BAR.md` — `gate-ledger.tsv` counts 1; a slice of the canary's G4/G5 block passed, and failed when the guide lost its ledger pointer

**Evidences:** TOOL-aDistilledCharter-4
- AC1 — `git grep` — over the S4 population the predicate printed two lines, both citing the spec template's own sections, which TOOL-aDistilledCharter-3 rev-2 excludes; no charter citation survived
- AC2 — `.claude/skills/lexicon/SKILL.md` — re-rendered from `.lexicon.conf`, and `adopt-lexicon.sh --check` reports the Skill in sync; the BUILD-METHOD dogfood pair agrees

**Evidences:** PLAY-aDistilledCharter-1
- AC1 — `render_playbook.py --target` — a scratch target selecting all 27 registry kits rendered with no block dropped, no `{{` surviving, and every one-line region passing the grade
- AC2 — `coding-governance-agents.template.md` — section 1 holds 33 handle bullets and no handle twice
- AC3 — `bash tools/check-microformats.sh` — 11 definitions graded, and the definition block is byte-identical to BASE's
- AC4 — `memory-tree` — a scratch target selecting only it rendered no other kit's tools or protocol line
- AC5 — `tools/gate-legs.json` — a resolver over the 115 ledger rows found 0 unresolved, and 2 when one handle was renamed
- AC6 — `tools/template-size-highwater.txt` — recorded 11455 at this unit and 11758 after TOOL-aDistilledCharter-7 restored four clauses; `bash tools/check-template-size.sh` is green; the archive is the 48597 bytes of BASE

**Evidences:** PLAY-aDistilledCharter-2
- AC1 — `memory/guides/REVIEW-PROTOCOL.md` — `## Tiers` at line 184 and `## Security boundaries` at line 198; each v3.5 §9 rule has a bullet
- AC2 — `git diff --exit-code memory/guides/REVIEW-PROTOCOL.md` — clean after the kit's parity render; the parity test reports 5 pairs in parity

**Evidences:** PLAY-aDistilledCharter-3
- AC1 — `memory/HYGIENE.md` — `## Ids` at line 168, one bullet per v3.5 §2 rule of lines 94 to 103
- AC2 — `git diff --exit-code memory/HYGIENE.md` — clean after the kit's dogfood render; 4 pairs agree

**Evidences:** PLAY-aDistilledCharter-4
- AC1 — `bash tools/playbook/adopt-playbook.sh --target . --check` — `render-playbook OK`
- AC2 — `bash skills/session-kickoff/manifest-check.sh --card --write` — a probe card's node cell reads `a · daily-agent @ COMPEETO-AGENT`
- AC3 — `bash tools/check-template-size.sh AGENTS.md` — 13151 of 16384 bytes at this unit, 13632 after TOOL-aDistilledCharter-7, both below the 32768 a Codex agent reads
- AC4 — `python tools/memory-tree/corpus_ids.py` — prints no `check 16 rule 3` line

**Evidences:** DEPL-aDistilledCharter-1
- AC1 — `WIRE-INTO-PROJECT.md` — every remaining section sign names the runbook's own sections or a frozen release note, and S4 is clean over it
- AC2 — `--claim-node` — the runbook names `adopter_rules` and the claim command

**Evidences:** TOOL-aDistilledCharter-5
- AC1 — `python tools/playbook/render_playbook.py --selftest` — two clones named apart both render `C:/p/app`, and a `primary_tree` override still wins; with the checkout directory restored as the source, three arms fail
- AC2 — `project_name` — with no answer the render refuses naming it

**Evidences:** TOOL-aDistilledCharter-6
- AC1 — `bash tools/check-playbook-parity.sh` — the three README pairs agree; a staged `≤7` in the README's lens bound reds `lens-array bound`
- AC2 — `const MAX_LENSES = 6` — the restored arm passes in the parity self-test

**Evidences:** TOOL-aDistilledCharter-7
- AC1 — `python tools/playbook/render_playbook.py --selftest` — 51 arms pass, the R3, R5, R7 and R8 arms among them; four staged breaks turned seven arms red
- AC2 — `GIT_DIR` — the selftest passes with `GIT_DIR` exported to this repository's git dir, and the R6 arm fails with the environment passed through
- AC3 — `the protocol template's §13` — the curly-apostrophe, non-breaking-space and trailing-form arms red and the protocol-template arm passes, in the parity self-test
- AC4 — `§1 Landing` — the root-install arm reds on a kit file citing it
- AC5 — `python3 tools/memory-tree/check-arms.py --emit-floors` — measures `13:11`, now the pin; `bash tools/check-playbook-parity.sh` passes with the `runlog` row drained
- AC6 — `min(8, nproc)` — a canary slice fails with it in `AGENTS.md` and passes on the tree
- AC7 — `coding-governance-agents.template.md` — the C5, C6, C8 and C10 clauses are present at 193, 189, 191, 178, 111 and 139 characters, each inside `ONE_LINE_MAX`
- AC8 — `grep -n 'runlog' AGENTS.md` — prints the tools line at line 94; `manifest-check.sh`'s retrofit step re-renders rather than pulling lines into the playbook

**Evidences:** PLAY-aDistilledCharter-5
- AC1 — `git diff --exit-code memory/TEMPLATE-SPEC.md` — clean after the dogfood render; `## Tiers` at line 322 and `## Security boundaries` at line 337
- AC2 — `memory/guides/REVIEW-PROTOCOL.md` — no `## Security boundaries` heading; one paragraph points at the spec template
- AC3 — `git diff 6473ae38 -- tools/govkit/registry.toml` — prints nothing
- AC4 — `render_playbook.py --target . --check` — green, and the ledger resolver finds 0 of 115 rows unresolved against the new home

**Evidences:** TOOL-aDistilledCharter-8
- AC1 — `python tools/playbook/render_playbook.py --selftest` — with `checkout_dir = "app/main"` every default row reads `C:/p/app/main`; the arm fails with `checkout_dir` ignored
- AC2 — `grep -n 'own charter' coding-governance-agents.template.md` — prints the claim note
- AC3 — `--check` — over a v3.5-marked fixture prints the reseed note; the arm fails with the note printing removed
- AC4 — `TEMPLATE_MAJOR = 3` — reds pair `template major` on the tree and in the parity self-test; a v4.0 fixture naming `{{TAG_A}}` is refused, and the arm fails with the refusal disabled

**Evidences:** KICK-aDistilledCharter-1
- AC1 — `awk` — zero continuation lines between §B's heading and the pointer map
- AC2 — `## Evictions` — 22 rows, one per §B bullet of BASE
- AC3 — `bash skills/session-kickoff/manifest-check.sh` — exits 0

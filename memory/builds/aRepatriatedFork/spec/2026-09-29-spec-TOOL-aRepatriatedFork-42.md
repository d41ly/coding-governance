# TOOL-aRepatriatedFork-42 — the memory-tree renders take every adopter path from the adopter's own declarations

**Status:** CLOSED · rev-3 · 2026-09-29 · node a · Tier-1 · base 012d9dd5 · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-29-build-TOOL-aRepatriatedFork-42-1-acceptance-ledger.md](../build/2026-09-29-build-TOOL-aRepatriatedFork-42-1-acceptance-ledger.md) | journal | — |
| [2026-09-29-review-TOOL-aRepatriatedFork-42-closing-diff-round1.md](../reviews/2026-09-29-review-TOOL-aRepatriatedFork-42-closing-diff-round1.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

The memory-tree kit renders four documents into an adopter's memory root. Their kit paths are
already derived, but five other kinds of path are spelled in gov's layout: the merge bar, the memory
root, the kickoff manifest and skill, the review and unattended protocols, and gov's spec-token
checker. At inCMS the render named `scripts/run-gates/run-gates.sh` as the merge bar, although its
bar is `scripts/gate.sh` and its `deploy.toml` already says so. It also named four paths inCMS does
not have, and inCMS raised `DEAD_PATH_PIN` from 2 to 6 to hold them. Owner ruling, 2026-09-29: every
adopter-specific path in these renders comes from the adopter's own declarations. The playbook
renderer's resolution supplies each answer, so there is one answer. A path to a gov-only artifact is
rendered conditionally. An undeclared answer is either a named refusal or a stated default, and never
gov's path.

## 2. Scope (IN)

- **S1** — `render_playbook.py` gains `--answers KEY...`. It prints, as JSON, the value the engine
  would use for each key. A key the playbook descriptor declares as a placeholder resolves as
  `render` resolves it, with the same precedence, probe and refusal. `kits` is the graded selection.
  Any other key is the `[answers]` value, then the top-level value, or null. `render` and the new
  verb share one deploy.toml reader and one `kits` grader. Observed by AC4.
- **S2** — `derive_kit_paths`, the canonical block the adopter script and the kit/dogfood parity
  test both carry, finds the playbook engine through the sibling-kit resolver that
  `TOOL-aRepatriatedFork-2` built. When the templates cite an answered placeholder and the tree
  declares `.governance/deploy.toml`, the block asks that engine once. It then prints one
  substitution line per placeholder. Observed by AC1 and AC2.
- **S3** — Seven placeholders replace the gov spellings. `{{GATE_RUNNER}}` comes from the engine.
  `{{MEMORY_ROOT}}` comes from the conf the render already sources, and the playbook's own
  `MEMORY_ROOT` probe reads the same key. `{{MANIFEST_PATH}}` and `{{KICKOFF_SKILL}}` render when
  `kickoff-manifest` is selected, from `manifest_path` and from `user_skills`. `{{REVIEW_PROTOCOL}}`
  renders when `review-harness` is selected, and `{{UNATTENDED_PROTOCOL}}` when `unattended` is, each
  at its kit's declared destination. `{{SPEC_TOKEN_CHECKER}}` renders only where `gov_source` is `.`,
  since the checker is a registry exemption that never ships. Observed by AC1.
- **S4** — Every placeholder carries a stated default phrase, which names no path. The default
  renders when the tree has no deploy.toml or no playbook engine, and when the owning kit is not
  selected. A selected kickoff-manifest with no `manifest_path` or no `user_skills` answer is a
  refusal naming the key. So is any refusal from the engine. Observed by AC2 and AC3.
- **S5** — The adopter script runs the block for a kit directory outside the repo as well. It passes
  the repo-relative kit path, so the resolver reads the target's receipt and never the shipping
  checkout's. A placeholder that survives the render is a refusal before any write. Observed by AC3.
- **S6** — Gov answers `manifest_path` and `user_skills` in its own `deploy.toml`. Gov's four live
  renders stay byte-identical except where gov's answer differs from the old literal. The merge-bar
  line names gov's derived command, the kickoff-skill line names gov's `user_skills`, and the two
  memory-root caveats go, since the root is rendered. The descriptor's `placeholders` lists name the new keys. memory-tree and
  playbook-render take a version bump in every carrier. Observed by AC5.
- **S7** — rev-3, review C1. Every line the derivation block prints is graded first: a value carrying
  a tab, a CR or a newline is a named refusal naming the placeholder, before any file is written.
  The charter admits a newline in a `[charter]` value, and a render line holds one line. Observed by
  AC6.
- **S8** — rev-3, review C2 and I1. The block reads the engine's `KIT_PLAYBOOK_RENDER_VERSION` before
  it spawns it. An engine below 1.11, the first whose `--answers` speaks the keys this block asks, or
  one whose version cannot be read, is treated as no engine: every placeholder states its phrase,
  and one stderr line names the engine, its version, the floor and `govkit update --kits
  playbook-render`. memory-tree's descriptor records the edge as a `requires_if` row, since govkit
  has no version floor and a plain `requires` refuses every default apply. `govkit update` prints
  the tail of a refused `[[regenerate]]` argv's stderr in its failure line. Observed by AC7, AC11.
- **S9** — rev-3, review C3 and I2. The block writes UTF-8 whatever the node's code page, and runs
  the engine with `PYTHONUTF8=1` and `PYTHONIOENCODING=utf-8`, decoding with `errors="replace"` and
  never reading an absent stream. Observed by AC8.
- **S10** — rev-3, review C4 and C6. `--answers` takes `kit.<entry>.<key>`: the `[kit.<entry>]`
  value over the `[answers]` value, as govkit's `target_context` builds the entry's tokens, or null.
  The block asks `manifest_path` and `user_skills` for the kickoff entry that way. Keys compare
  case-insensitively, as `[answers]` and `[charter]` already do. The memory root has one value: a
  declared answer, from `[charter]`, `[answers]` or `[kit.memory-tree]`, that differs from the
  conf's `MEMORY_ROOT` is a named refusal naming both. A govkit selftest arm pins the overlay
  against `target_context`. Observed by AC9.
- **S11** — rev-3, review C5, C7, I3 and I4. `{{UNATTENDED_PROTOCOL}}` without an answer states a
  neutral phrase. The spec-token sentence names no gate-leg path. `{{KICKOFF_SKILL}}` renders a
  repo-relative path only when git tracks it at the target; a `~`-rooted or absolute one renders as
  before. `{{REVIEW_PROTOCOL}}` and `{{UNATTENDED_PROTOCOL}}` render the path of their kit's
  `rendered` row in the target's receipt, the destination govkit actually wrote, or the phrase; the
  hand-typed copies of the descriptors' `to` go. Observed by AC10.

## 3. Non-goals (OUT)

- Install-prefix literals. The `{{TOOL_ROOT}}<kit>/<file>` citations the receipt resolves stay as
  they are. rev-3: the spec template's `{{TOOL_ROOT}}gate-legs.json` goes, because the sentence
  carrying it describes gov's checker, which reads gov's manifest and never the adopter's.
- Rolling two kits back together. govkit rolls back per kit by design, and no descriptor key couples
  two kits' rollbacks. S8 makes the rolled-back state render the phrases instead of refusing.
- A kit path whose kit the adopter did not select, such as the unattended driver. The receipt
  resolves these, and a kit the adopter lacks is the prefix drain's population.
- The `<MEMORY_ROOT>` prose token in the spec template. It names no path an adopter could miss.
- The charter template. The playbook renderer already fills it from these answers.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — the inCMS side. Once inCMS carries this kit it
  re-renders, drops the rows its dead-path registry holds for gov's paths, and lowers
  `DEAD_PATH_PIN`. rev-3: inCMS's receipt holds no rendered row for the review protocol, so its
  render states the phrase and that row drains with the others.
- **hands-off** `TOOL-aRepatriatedFork-26` — the install-prefix literals in these four templates.
  The two units split the same files. This unit owns the adopter-declared paths in the memory-tree
  renders, and `TOOL-aRepatriatedFork-26` owns the prefix literals. Neither waits on the other.

## 4. Design

### Evidence

At inCMS `71180c796` the rendered `guides/BUILD-METHOD.md` names `scripts/run-gates/run-gates.sh` as
the merge bar. The inCMS `deploy.toml` answers `gate_runner = "bash scripts/gate.sh"`. The playbook
renderer reads that answer, and the memory-tree renderer does not. The dead-path registry
`corpus-path-unresolved.txt` there holds four rows that cite gov: `scripts/check-spec-tokens.py`
twice, `memory/guides/REVIEW-PROTOCOL.md` twice, `memory/guides/SESSION-KICKOFF.md` once and
`skills/session-kickoff/SKILL.md` once. inCMS keeps its manifest at `.claude/SESSION-KICKOFF.md`, its
`manifest_path` answer. PINNED, read 2026-09-29.

### Path-token classification

Every path the four templates spell, read at `012d9dd5`. The annotation-style template spells none.

| Token | Template | Class | Source after this unit |
|---|---|---|---|
| `{{KIT_DIR}}/…` | all | a | the kit directory, derived |
| `{{TOOL_ROOT}}<kit>/<file>` | build method, spec template | a | the receipt row, then the probe |
| `{{TOOL_ROOT}}gate-legs.json` | spec template | a | the prefix |
| memory-root-relative forms such as `builds/*/spec/` | hygiene | a | relative, unchanged |
| `{{TOOL_ROOT}}run-gates/run-gates.sh` | build method | b | `GATE_RUNNER` |
| literal `memory/…` | build method, hygiene | b | `MEMORY_ROOT` |
| `memory/guides/SESSION-KICKOFF.md` | build method | b | `manifest_path` |
| `skills/session-kickoff/SKILL.md` | build method | b | `user_skills` |
| `memory/guides/REVIEW-PROTOCOL.md` | build method | b | rev-3: the review-harness kit's rendered receipt row |
| `memory/guides/UNATTENDED-PROTOCOL.md` | build method | b | rev-3: the unattended kit's rendered receipt row |
| `{{TOOL_ROOT}}check-spec-tokens.py` | spec template | c | `gov_source`, else the default |
| `{{TOOL_ROOT}}gate-legs.json` | spec template | c | rev-3: reworded, names no path |

### rev-3: the fold of the round-1 closing-diff review

The round-1 review of `012d9dd5..f02a3a56` found nine distinct defects, each reproduced red on the
`f02a3a56` bytes before any code moved, since no skeptic ran. They share one block and fall in four
groups. The input: a multi-line value cut the docs (C1) and a non-ASCII one broke them (C3, I2). The
engine: an older one could not answer and the render refused (C2, I1). The answers: govkit's
per-entry overlay and the memory root disagreed with the render's (C4, C6). The phrases and paths:
one phrase was false (C5), one sentence named the adopter's manifest for gov's checker (C7), one
path was never checked (I3), and two destinations were hand-typed copies (I4).

The protocol paths leave the `kits` test for the receipt. Selecting a kit is not the same as having
its rendered row, and the row's `path` is the destination govkit wrote. It is not a filesystem
test, so the render-order objection under Alternatives still holds. The match is the row's `kit`
and its `source` basename, the kit id being a membership string rather than a path.

Gov keeps no receipt, so gov's build method states the two protocol phrases after this fold. That
is the cost of reading the destination from the one record of it rather than restating it.

### Inventory

One new function in the playbook engine, `resolve_answers`, beside `resolve_placeholder_value`. Two
readers leave `render` for it to share, `read_deploy` and `read_kits`. The derivation block gains no
function.

### Files touched (estimate)

The four memory-tree templates, the adopter script, the kit/dogfood parity test, the canonical
render-doc block, the memory-tree descriptor, the playbook engine, the hygiene suite, gov's four
rendered docs, gov's deploy.toml, and the two kits' version carriers.

### Alternatives rejected

- Reading deploy.toml in the memory-tree block itself. That is a second reader of one answer, and it
  has no gate-runner probe, so gov's own bar would need a hand answer.
- A filesystem-existence test for the gov-only checker. `gov_source` already declares which tree is
  the shipping repo, and a render that depends on a file existing flips with render order.
- Fence blocks in the bash renderer. Every conditional here is one phrase inside a sentence, and a
  substitution line carries it through the renderer's existing loop.

## 6. Acceptance criteria

- **AC1** — In the hygiene suite, a fixture adopter at prefix `scripts` answers its gate runner as
  bash scripts/gate.sh, its `gov_source` as a sibling checkout, its `manifest_path` under `.claude/`,
  and its `user_skills`. It selects `kickoff-manifest` and neither `review-harness` nor
  `unattended`, and carries the playbook engine under its prefix. After `--render`, the build method
  names that gate runner, that manifest and the skill under `user_skills`. None of the four docs
  names gov's run-gates runner, `check-spec-tokens.py`, `REVIEW-PROTOCOL.md`,
  `UNATTENDED-PROTOCOL.md`, `memory/guides/SESSION-KICKOFF.md` or `skills/session-kickoff/`.
  Red when: any gov path reaches the fixture's docs.
- **AC2** — The same fixture without the playbook engine, rendered by `--render`, states every
  default phrase, and no placeholder survives.
  Red when: a default names a path, or a brace survives.
- **AC3** — With `kickoff-manifest` selected and no `manifest_path` answer, `--render` exits 1,
  names `manifest_path`, and leaves the four docs unchanged.
  Red when: the render guesses a manifest path or writes a partial set.
- **AC4** — The playbook selftest's new arm reads `--answers GATE_RUNNER kits manifest_path
  gov_source nope` over a fixture. The answered gate runner, the graded kit list, the
  answer, the top-level value and null each come back. A misspelled `kits` member is refused.
  Red when: the verb and `render` disagree on a value.
- **AC5** — On gov, `bash tools/memory-tree/adopt-memory-tree.sh --render` rewrites the four live
  docs, and their diff against `012d9dd5` touches only the lines S6 names. `bash tools/check-kit-versions.sh` exits 0, and
  `python tools/govkit/govkit.py epoch --base f8fdd873` reports no FAILED entry. The red-first
  control is the AC1 fixture rendered by the `012d9dd5` adopter, and its output names the gov paths.
  Red when: gov's render moves elsewhere, or a carrier keeps the old version.
- **AC6** — rev-3. In the hygiene suite, the AC1 fixture answering `[charter] gate_runner` over
  three lines makes `--render` exit non-zero, naming `{{GATE_RUNNER}}`, and leaves the four docs
  unchanged.
  Red when: the render exits 0, or any doc moves.
- **AC7** — rev-3. The AC1 fixture whose engine declares `KIT_PLAYBOOK_RENDER_VERSION` 1.10 renders
  with exit 0, states every phrase, and prints one stderr line naming 1.11 and `govkit update`.
  Red when: the render refuses, or an argparse usage error reaches the operator.
- **AC8** — rev-3. Under `PYTHONUTF8=0`, the AC1 fixture answering a gate runner that carries
  U+2192 renders valid UTF-8 that names it, and one whose `kits` names an unknown entry prints the
  engine's named refusal with no traceback.
  Red when: a doc is not UTF-8, or `Traceback` reaches the output.
- **AC9** — rev-3. The playbook selftest's arm reads `--answers` in both cases and through
  `kit.<entry>.<key>`, and the per-entry value wins. The govkit selftest's arm resolves the same
  qualified keys through the engine and through `target_context` over one fixture, and they agree.
  In the hygiene suite, a manifest answered only under `[kit.kickoff-manifest]` renders, and an
  `[answers] memory_root` differing from the conf is refused naming both.
  Red when: a casing or the overlay changes an answer, or two memory roots render.
- **AC10** — rev-3. In the hygiene suite, a receipt whose rendered rows put the review protocol at
  `docs/rp.md` makes the build method name `docs/rp.md`, and with no such row it states the phrase.
  An untracked repo-relative skill states the phrase. With no engine, the unattended phrase names no
  install state, and the spec template names no gate-leg path.
  Red when: a destination is not the receipt's, or a phrase asserts what the render did not check.
- **AC11** — rev-3. The govkit selftest's arm runs `update` over a kit whose `[[regenerate]]` argv
  prints a reason to stderr and exits with a code no outcome accepts, and the failure line carries
  that reason.
  Red when: the reason is absent from update's output.

## 7. Gates

`memory-hygiene self-test` · `kit/dogfood doc parity` · `playbook render selftest` · `playbook render wiring` · `python resolver (behaviour + inline parity + idiom ban)` · `kit placeholders (a declared token its adopter substitutes)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `build-method size` · `govkit selftest` · `govkit selfcheck` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)`

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · `a fixture adopter's render names its own declared paths` · `FLOOR_ASSERTIONS`

New arm: `tools/playbook/render_playbook.py` · `--answers agrees with render` · none

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · `a multi-line answer, an old engine, a non-UTF-8 node, the per-entry overlay, the memory root and the receipt's destinations` · `FLOOR_ASSERTIONS`

New arm: `tools/playbook/render_playbook.py` · `--answers is case-insensitive and applies the per-entry overlay` · none

New arm: `tools/govkit/selftest.py` · `--answers agrees with target_context, and a refused regenerate prints its reason` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-29 · initial draft, from the owner's ruling.
- rev-2 · 2026-09-29 · S1 · S2 · S3 · S4 · S5 · S6 · AC1 · AC2 · AC3 · AC4 · AC5 · built. The three
  new hygiene-suite arms red on the 012d9dd5 kit, and the new playbook arm reds on an ungraded
  `kits`. At an inCMS clone of 71180c796 the render names inCMS's own bar, manifest and skill, and
  `DEAD_PATH_PIN` measures 3 against 6.
- rev-3 · 2026-09-29 · S7 · S8 · S9 · S10 · S11 · §3 · §4 · §7 · AC6 · AC7 · AC8 · AC9 · AC10 ·
  AC11 · folds the round-1 closing-diff review, persisted as
  `2026-09-29-review-TOOL-aRepatriatedFork-42-closing-diff-round1.md`. No skeptic ran, so each of
  its nine distinct defects was reproduced red on the `f02a3a56` bytes before this revision. The
  derivation block refuses a multi-line value, treats an engine below 1.11 as absent, writes UTF-8,
  asks the kickoff answers through govkit's per-entry overlay, holds one memory root, and takes the
  protocol destinations from the receipt; `govkit update` prints a refused argv's reason.
  memory-tree and playbook-render bump again in every carrier.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve an adopter answer from deploy.toml for a rendered doc"`
ranked name-stem neighbours only, and it cannot see shell. The answer resolution this unit shares
was found by reading `render_playbook.py`: `resolve_placeholder_value` and the `kits` grading in
`render`. The sibling lookup is `resolve_kit_dir`, and the substitution loop is `render_doc`'s
existing `KIT_PATHS` pass. This unit adds no second copy of either.

Recall terms used: `render_doc derive_kit_paths KIT_PATHS GATE_RUNNER gate_runner deploy.toml answers
manifest_path user_skills resolve_kit_dir rendered docs TOOL_ROOT`.

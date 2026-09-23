# DEPL-aRepatriatedFork-1 — the charter renderer lets an answer win, and knows which file is its template

**Status:** CLOSED · rev-2 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams deployer+playbook · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-23-build-DEPL-aRepatriatedFork-1-1-acceptance-ledger.md](../build/2026-09-23-build-DEPL-aRepatriatedFork-1-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-DEPL-aRepatriatedFork-1-build-brief.md](../prompts/2026-09-23-prompt-DEPL-aRepatriatedFork-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/playbook/render_playbook.py` consults a `deploy.toml` answer for a `derived` placeholder only
when the probe returns nothing (`render_playbook.py:405-418`), so a probe that answers WRONGLY
cannot be corrected by the operator. Both adopters therefore fork gov's playbook descriptor to flip
three placeholders to `asked`, and gov's own charter prose cannot pass gov's own answer charset.
This unit makes an explicit answer outrank a probe, reclassifies the probes that answer from the
rendering node, separates the template's home from the charter's in the one place they collide, and
gives charter prose a value class that is never interpolated into an argv. The measured outcome is
that both adopters take gov's `playbook.kit.toml` verbatim.

## 2. Scope (IN)

- **S1** — ANSWER OVER PROBE. In `render()` a `derived` row whose key has a non-empty answer takes
  the answer whatever the probe returns. The note line prints both values:
  `answered  KEY = <answer>   (probe would derive <value>)`, and when they are equal it says the
  answer is redundant. A probe returning nothing with no answer still REFUSES, unchanged. Observed
  by AC1, AC2.
- **S2** — NODE-VARYING PROBES STOP BEING DERIVED. In `tools/govkit/entries/playbook.kit.toml`,
  `PROJECT_NAME`, `PRIMARY_TREE_A` and `WORKTREE_ROOT_A` become `asked`, carrying the reason
  `MACHINE_A` already gives at `playbook.kit.toml:125-127`. `TAG_A`, whose probe
  `derive_node_tag` returns the literal `'a'` at every node (`render_playbook.py:153-154`), becomes
  `defaulted` with default `a`, so the render prints `DEFAULTED` for it rather than `derived`. Gov's
  own `.governance/deploy.toml` gains the three answers its current charter already renders, so
  gov's `AGENTS.md` does not move. Observed by AC3, AC4, AC8.
- **S3** — THE TEMPLATE IS NEVER ITS OWN CHARTER. `render()` refuses when the resolved template path
  (`resolve_template_path`, `render_playbook.py:327-337`) and the charter path (`--charter`,
  default `AGENTS.md`, `render_playbook.py:546`) are the same file, naming both. Observed by AC5.
- **S4** — THE PLACEHOLDER HOLE STANDS DOWN IN RENDER MODE. A `[[hole]]` gains an optional
  `stands_down = { when_selected = ["<entry id>", ...], why = "..." }`. `cmd_check` and
  `exempt_leg` do not run the probe of a hole whose `when_selected` intersects the target's
  selection, and print `stood down — <entry> observes this`. The `playbook-placeholders` hole
  (`playbook.kit.toml:33-39`) declares `when_selected = ["playbook-render"]`, because in render mode
  `{playbook_path}` is the TEMPLATE, which always carries placeholders, and the render's own
  `--check` already reports a surviving one. In copy mode, with `playbook-render` unselected, the
  probe runs exactly as today. `selfcheck` refuses a `when_selected` member that is not a registry
  entry id. Observed by AC6, AC7.
- **S5** — A RENDER-ONLY VALUE CLASS. A `[charter]` table in `deploy.toml` holds values whose only
  consumer is `render_playbook.py`. `render()` reads a placeholder's value from `[charter]` first and
  `[answers]` second. `target_context` (`govkit.py:940-996`) never reads `[charter]`, so no value
  from it reaches a `ctx` token or an argv. A `[charter]` value is refused when it carries a control
  character other than a newline, the `{{` placeholder opener, or a `gov:playbook` region marker. A
  `[charter]` key that names no declared placeholder is refused, and so is one that names a token
  `needed_answers` (`govkit.py:9986-10017`) derives, because that key's value must reach an argv and
  belongs in `[answers]`. That join is made in TWO places, because the renderer ships without govkit:
  `render()` grades against the tokens of the one descriptor it reads (`read_argv_tokens`, the same
  walk `needed_answers` makes over one entry), and `govkit check` grades against `needed_answers` over
  the whole selection. Observed by AC9, AC10.
- **S6** — `KIT_PLAYBOOK_RENDER_VERSION` moves from `1.0` to `1.1` (`render_playbook.py:621`), because
  the shipped bytes change. `tools/playbook/README.md` and the render section of
  `WIRE-INTO-PROJECT.md` state the precedence, the two modes of `playbook_path` and the `[charter]`
  table. Observed by AC11.

## 3. Non-goals (OUT)

- Widening `ANSWER_VALUE_RE` (`govkit.py:907`). Its comment block at `govkit.py:860-905` explains
  why the prose class is sound only for a document-only consumer, and S5 builds that consumer's own
  table instead of loosening the shared one.
- Moving existing adopter answers into `[charter]`. That is an adopter edit each owner may make; it
  is not required for the fork to retire.
- The `gate_runner` probe's guessing ladder (`render_playbook.py:141-146`). It is the open row
  `TOOL-dPolishedVitrine-4`, and S1 already gives nc's answer precedence over it.
- `DEFAULT_BRANCH` reading `refs/remotes/origin/HEAD` (`render_playbook.py:110-117`). Node d's remote
  is not named `origin`, the probe falls back to `main`, and S1 lets an answer correct it where that
  fallback is wrong.
- nc's lexicon holes and its lexicon adopter exit, which `govkit check` also reports at nc. They are
  not the playbook's.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-13` — the `stands_down` table S4 creates, which that unit
  extends with an owned-engine predicate.

## 4. Design

### Data model

The three placeholder classes stay closed. What changes is the precedence inside `derived`:

| Class | Value source, in order | Refused when |
|---|---|---|
| `derived` | `[charter]`, then `[answers]`, then the probe | all three are empty |
| `asked` | `[charter]`, then `[answers]` | both are empty |
| `defaulted` | `[charter]`, then `[answers]`, then the declared default | the default is empty |

The hole table addition:

```toml
[[hole]]
id = "playbook-placeholders"
# ...unchanged fields...
stands_down = { when_selected = ["playbook-render"], why = "in render mode {playbook_path} is the template, and the render's own --check reports a surviving placeholder" }
```

### Inventory

- `resolve_placeholder_value(row, charter, answers, target)` — `py.function`, snake, verb `resolve`.
  It returns the value and its note line, and it is the one site the three classes share.
- `read_charter_table(cfg, rows, argv_tokens)` — `py.function`, snake, verb `read`. It grades every
  `[charter]` key and value.
- `read_argv_tokens(desc)` — `py.function`, snake, verb `read`. The engine-side half of S5's join.
- `resolve_stand_down(hole, selection)` — `py.function`, snake, verb `resolve`, in govkit. The one
  predicate `cmd_check` and `exempt_leg` share for S4.
- `[charter]` — a new `deploy.toml` table.
- `stands_down.when_selected` — a new optional `[[hole]]` key.

### Evidence, measured at a7c78ad2

The gov probes, run against each adopter by calling `render()` with gov's own descriptor:

| Key | inCMS derives | nc derives | Owner's answer |
|---|---|---|---|
| `PROJECT_NAME` | `main` | `vendor` | `inCMS` · `NicoCares` |
| `PRIMARY_TREE_A` | `C:/projects/incms/main` | `C:/projects/incms/main/.git/modules/vendor` | per node, see the registry |
| `WORKTREE_ROOT_A` | `.../main/.claude/worktrees` | `.../.git/modules/vendor/.claude/worktrees` | per node, see the registry |
| `MEMORY_DISCIPLINES` | probe empty, answer used | `package brand` | nc answers `package, brand`, silently ignored |
| `TAG_A` | `a` | `a` | the probe is a constant |

Every value in that table is PINNED, measured 2026-09-23 by the render call above.

The answer charset, measured the same day: 11 of the 15 string answers in gov's own
`.governance/deploy.toml` are refused by `ANSWER_VALUE_RE`, for an em dash, a middle dot, a
backtick, a semicolon, parentheses or angle brackets. Gov's renderer reads them only because govkit
never runs `target_context` over gov itself. The mandated commit trailer is the sharpest case:
inCMS's rendered charter spells it without its colon and angle brackets, because its answer could
not carry them.

The hole, measured the same day: `govkit check` prints
`hole 'playbook-placeholders' is UNDISCHARGED (probe exit 1)` at both adopters. Each installed
template holds 39 lines carrying `{{`, and each rendered `AGENTS.md` holds 0.

### Files touched (estimate)

`tools/playbook/render_playbook.py` · `tools/govkit/entries/playbook.kit.toml` ·
`tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `tools/playbook/README.md` ·
`WIRE-INTO-PROJECT.md` · `.governance/deploy.toml` · `AGENTS.md`

### Adopter deletions this unit enables

| Adopter | Deleted | Where |
|---|---|---|
| inCMS | `KIT_PLAYBOOK_KIT_DELTA` at three `why` strings and its header comment | the playbook descriptor, lines 72, 117-118, 134, 139 |
| inCMS | the `divergence` row for the playbook descriptor | `.governance/kits.json:327-331` |
| nc | carve-out 35/24 at three `why` strings | the playbook descriptor, lines 72, 131, 136 |
| nc | the carve-out's census line | the nc HYGIENE census that enumerates carve-outs |

Both then take gov's descriptor bytes, and both keep their existing answers, which S1 now honours.

### Migration

nc's next render changes `MEMORY_DISCIPLINES` from `package brand` to `package, brand`, because its
answer starts winning. That is the intended correction and moves nc's charter by one line. inCMS's
rendered region does not move: its forked descriptor already reads the three answers.

### Rollout

Dark landing does not fit a precedence change: a flag would leave two meanings of one answer
table live at once. The protection is AC2's pre-change measurement and AC3's byte-identical render
at gov itself. The first adopter render after the pull shows every overriding answer on a note line.

### Alternatives rejected

- Leaving the three probes `derived` and relying on S1 alone. The class would still lie about gov's
  own charter at any second node, which is exactly `MACHINE_A`'s stated hazard.
- Widening `ANSWER_VALUE_RE` for every answer. Rejected by that regex's own comment: several
  shipped probes interpolate answers into `bash -c`.
- Splitting `playbook_path` into two answer keys. Both adopters and `resolve_template_path` already
  agree on what the key means in render mode. The only incoherence was the hole, and S4 closes it
  without renaming a key two adopters have committed.

## 5. Production-readiness checklist

- security — S5 keeps prose off every argv by construction: `[charter]` never enters `ctx`, and a
  key that a descriptor token needs is refused there. The `{{` refusal stops a value re-entering
  substitution, and the marker refusal stops one splitting the region.
- perf / scale — one extra table read per render. No new subprocess.
- error / empty / loading states — an empty answer is still absent. A template that is its own
  charter refuses by name. A stood-down hole prints its reason instead of passing silently.
- observability — every overriding answer prints beside the value the probe would have used.
- risks — an adopter answer that was silently ignored starts winning. nc's discipline list is the
  one measured instance, and the note line surfaces every other one.
- testing — new `--selftest` arms in `render_playbook.py`, new `selfcheck` and `selftest` arms in govkit.
- migration — gov answers three keys itself. nc's charter moves by one line.
- user docs — `tools/playbook/README.md` and `WIRE-INTO-PROJECT.md`. Gov has no end-user `help/` tree.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --selftest` runs, a new arm whose
  fixture answers a `derived` key the probe also derives finds the answer in the body and the
  `answered` note naming the probe value.
  Red when: the body carries the probe value, which is today's behaviour at `render_playbook.py:405-419`.
- **AC2** — The AC1 arm is observed RED against `render_playbook.py` at a7c78ad2 before S1 lands,
  and the arm's name and failure line are recorded in the build journal.
  Red when: the arm passes against the unchanged engine, so it tests nothing.
- **AC3** — When the gov `playbook.kit.toml` bytes replace the inCMS fork in a scratch clone of the
  inCMS worktree, the clone's installed `adopt-playbook.sh --target . --check` exits 0 with no drift.
  Red when: the region differs from the committed `AGENTS.md`, or a placeholder survives.
  fixture: a `--shared` clone of the inCMS worktree; the tree holds none today.
- **AC4** — The AC3 observation holds at a scratch clone of the nc worktree, except for the one
  `MEMORY_DISCIPLINES` line the Migration sub-head names, which is the only drift reported.
  Red when: any other line drifts, or `PROJECT_NAME` renders `vendor`.
  fixture: a `--shared` clone of the nc worktree.
- **AC5** — When a `--selftest` fixture sets `playbook_path = "AGENTS.md"` and renders with the
  default charter, `render_playbook.py` exits 1 naming both paths and writes nothing.
  Red when: the render appends a region into its own template.
- **AC6** — When `python tools/govkit/govkit.py check --target <inCMS worktree>` runs, no line reports
  `playbook-placeholders` UNDISCHARGED, and one line reports it stood down naming `playbook-render`.
  Red when: the hole still probes the template in render mode.
  figure: the 39 placeholder lines are PINNED from 2026-09-23 and are not asserted.
- **AC7** — When a govkit `selftest` fixture selects `playbook` without `playbook-render` and its
  `{playbook_path}` file carries a `{{` line, `govkit check` still reports the hole UNDISCHARGED;
  `selfcheck` refuses a fixture descriptor whose `when_selected` names a non-entry.
  Red when: copy mode loses its only placeholder observer, or a typo in `when_selected` stands a
  hole down forever.
- **AC8** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs in gov after S2, it
  exits 0 and `AGENTS.md` is byte-identical to a7c78ad2.
  Red when: gov's own charter moves because its answers were not added.
- **AC9** — When a `--selftest` fixture puts `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`
  under `[charter]` as the trailer, the body carries it byte-exact, and the same value under
  `[answers]` is still refused by `govkit.py check` on a fixture target.
  Red when: the charter class admits nothing new, or the answers class starts admitting `<`.
- **AC10** — When a `[charter]` value carries `{{X}}`, a region marker, or a control byte, or a
  `[charter]` key names a token `needed_answers` returns, the render exits 1 naming the key.
  Red when: any of the four reaches the body or an argv.
- **AC11** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 with
  `KIT_PLAYBOOK_RENDER_VERSION = "1.1"` and its same-line marker `playbook-render@1.1`, and
  `grep -c '\[charter\]' tools/playbook/README.md` is at least 1.
  Red when: the engine moves without its version, the marker and the constant disagree, or the
  README omits the table.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `playbook placeholder catalogue` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: `tools/playbook/render_playbook.py` `--selftest` · a fixture answering a derived key its probe also derives, a template-is-charter fixture, and four hostile `[charter]` values · none
New arm: `tools/govkit/selftest.py` · a copy-mode and a render-mode fixture for the placeholder hole, plus a `when_selected` typo · none

## 8. Open questions

- **F1 — `TAG_A`: `defaulted` or `asked`?** `defaulted` keeps every current render byte-identical and
  prints that the value was not chosen. `asked` matches `MACHINE_A` and costs every adopter one more
  intake question. Recommendation: `defaulted`, because the registry row it fills is the rendering
  node's own and `a` is the fleet's first tag by construction.
  RESOLVED (owner, 2026-09-23): `defaulted`, as recommended.
- **F2 — should a redundant answer, equal to its probe, be a finding?** inCMS's `deploy.toml`
  comment calls such an answer a second copy of a value that has a home. Recommendation: a note
  line, never a failure. A finding would red an adopter for being explicit.
  RESOLVED (owner, 2026-09-23): a note line, never a failure, as recommended.
- **F3 — does `[charter]` also admit a `derived` override, or only `asked` and `defaulted` keys?**
  Recommendation: all three, per the Data model table. The class is about the consumer, not the key.
  RESOLVED (owner, 2026-09-23): all three classes, per the Data model table, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, grounded at a7c78ad2 with the render probes, the answer charset
  and the placeholder hole each measured against both adopters on 2026-09-23.
- rev-2 · 2026-09-23 · built. S5 moved: the `needed_answers` refusal is made by the renderer over its
  own descriptor's tokens and by `govkit check` over the whole selection, because the renderer ships
  without govkit and cannot call it. AC11 moved: `check-kit-versions.sh` does not assert this kit and
  prints nothing on success, so the version is observed by `govkit selfcheck`'s version cross-check,
  which reds on a marker that disagrees with the constant. Inventory gains `read_argv_tokens` and
  `resolve_stand_down`. `AGENTS.md` is not touched: AC8 holds with the three new answers alone.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an explicit deploy answer overrides a derived charter placeholder probe"`
returned only `derive_*` name-stem neighbours, such as `derive_scope` and `derive_lf`. No existing
seam fits: the render loop in `render()` is the seam, and it is not a mapped symbol. S1 edits that
loop in place. S4 extends `cmd_check`'s existing hole walk at `govkit.py:3926-3950` rather than
adding a second one.

Recall terms used: `render_playbook derived asked defaulted placeholder probe answers playbook_path
primary_tree worktree_root project_name override charter`. The top hit was `TOOL-dPolishedVitrine-4`,
the gate-runner ladder this unit leaves open.

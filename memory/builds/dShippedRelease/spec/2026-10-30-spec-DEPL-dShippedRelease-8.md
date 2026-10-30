# DEPL-dShippedRelease-8 — optional emitted CI: every `uses:` pinned by sha from one declaration gov's own workflow also uses, under least-privilege `permissions:`

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 27 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0418@0096c2c8 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md](../build/2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md) | research | DEPL-dShippedRelease-3 DEPL-dShippedRelease-6 DEPL-dShippedRelease-15 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-26 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

No CI job is emitted into adopters (`gap-deploy-03`), and `[gate_runner.ci]` is a validator with no
emitter (`tools/govkit/govkit.py:6001-6005`). Gov pins its own actions by full sha, but as literals in
one file (`.github/workflows/remote-ci.yml:27`, `:58`, `:118`). This unit lands one declaration of
those pins, an optional emitted workflow that reads it, and a leg over the emitted template and gov's
own workflow, so a tag-pinned `uses:` reds on either. It owns no node and reads none.

## 2. Scope (IN)

Build-run preconditions, specced and DEFERRED at base `f4597719`: TOOL-dWitnessedBar-11's
`leg_factory.py new`, which registers the legs, and TOOL-dSafePassage-12's `actions/setup-python` pin in
`.github/workflows/remote-ci.yml`, whose row S1 carries. `tools/integrations/` is created by
DEPL-dShippedRelease-15.

- **S1** — The declaration, `tools/integrations/ci/action-pins.toml`: one `[[action]]` row per action,
  with `name`, `sha` and `tag`, holding `actions/checkout`, `actions/upload-artifact` and
  `actions/setup-python`. `read_action_pins(path)` in `tools/integrations/ci/ci_emit.py` is its one
  reader, and it refuses a `sha` that is not 40 lowercase hex, an empty `tag` and a repeated `name`.
  Observed by AC8.
- **S2** — The template, `tools/integrations/ci/gov-bar.template.yml`: one workflow named `gov-bar` on a
  push to the default branch, with top-level `permissions:` of `contents: read`, and one job `bar` that
  checks out with `fetch-depth: 0` and `persist-credentials: false` and runs the repository's merge bar.
  A `uses:` line carries a token, `{{ACTION_CHECKOUT}}`, and never a ref. `{{DEFAULT_BRANCH}}` and
  `{{PREFIX}}` are the other two tokens. Observed by AC1 and AC6.
- **S3** — The emitter, `python ci_emit.py render --target <root>`. It reads `[gate_runner.ci]` from the
  target's `.governance/deploy.toml`. With no such table it prints `ci emit — not declared` and exits 0,
  which is what "optional" means here. With `system = "github-actions"` it writes
  `.github/workflows/gov-bar.yml`, each token filled from S1's rows as `<name>@<sha> # <tag>`, the first
  line a marker `# gov:ci-emit`. It refuses, exit 2, a destination that exists without the marker, so an
  adopter's own workflow is never overwritten. Observed by AC6.
- **S4** — The check, `python ci_emit.py check [--root <path>] [--workflow <file>]`, which renders each
  template with placeholder values and reads the render and each `--workflow` file by line, with no YAML
  library:
  - every `uses:` names `<name>@<40 hex> # <tag>`, equal to a row of S1;
  - a top-level `permissions:` block exists in a template, every value in any `permissions:` block is
    `read` or `none`, and `write-all` and `read-all` are refused;
  - every row of S1 is used by a template or a `--workflow` file, so a stale pin cannot sit unread.

  It prints one line per finding naming the file and line, then a count, and exits 1 on any finding.
  Observed by AC1, AC2, AC3, AC4, AC5 and AC7.
- **S5** — The legs, each made by `leg_factory.py new` as a `[[gate_leg]]` row of
  `tools/integrations/kit.toml`: `emitted ci pins`, running S4, whose `[gate_leg.gov]` value adds
  `--workflow .github/workflows/remote-ci.yml` because only gov's tree holds that file, and `emitted ci
  self-test`, running the module's in-file arms. Both render into `tools/gate-legs.json`. Observed by
  AC1.
- **S6** — The kit's rows. `tools/integrations/kit.toml`, which DEPL-dShippedRelease-15 creates with no
  adopter, gains a `[[files]]` row of role `rendered` whose `to` is `.github/workflows/gov-bar.yml` with
  the three placeholders, and `ci_emit.py render` as its `[adopt]` argv with a `[[regenerate]]` row. The comment at `tools/govkit/govkit.py:8491`, naming a unit as the
  future emitter, is corrected to name this module, and `UPDATE_ROLE["ci"]` stays `report`. NOT OBSERVED
  beyond AC6: a descriptor row and a comment.
- **S7** — Gov's workflow reads the declaration by parity. `.github/workflows/remote-ci.yml` keeps its
  literal `uses:` lines, and the header's sentences at `:15-16` and `:27` are amended to say the leg of
  S5 grades its `uses:` lines against `action-pins.toml`, and that nothing else but
  TOOL-dSafePassage-11's floor query grades the file. Observed by AC5 and AC9.
- **S8** — The docs. `help/emitted-ci.md`, with its row in `help/README.md`, states how to opt in, what
  the job runs, and how a pin moves: edit `action-pins.toml` and the workflow together. Observed by
  AC10.

## 3. Non-goals (OUT)

- The floor, `actions/setup-python` in the emitted job, and the Linux job: DEPL-dShippedRelease-26's.
- A scheduled job for receipt sync or the currency probe. Research named them, the clause does not, and
  the currency reader is DEPL-dShippedRelease-7's.
- Any CI system but GitHub Actions. The validator refuses the rest by name (`govkit.py:6003`).
- An adopter's own workflows. The leg reads the template and, on gov, gov's workflow, and nothing of
  the adopter's own. Importing them is DEPL-dShippedRelease-19's.
- Rendering `.github/workflows/remote-ci.yml` (§8 F1), and resolving a tag to its sha at gate time, which
  would be a network read in a leg. The leg checks agreement, and a tag whose sha moved upstream is
  caught by a person editing the row.
- Making a job a required check: a repository setting, the owner's.

### Edges

- **consumes-from** `DEPL-dShippedRelease-15` — `tools/integrations/kit.toml`, the kit this unit's files, rows and legs join; without it they have no descriptor
- **hands-off** `DEPL-dShippedRelease-26` — `action-pins.toml` and the template, into which that unit adds the floor, `actions/setup-python` and the Linux job
- **consumes-from** external — TOOL-dWitnessedBar-11's `leg_factory.py` and TOOL-dSafePassage-12's `actions/setup-python` pin; a build run with neither hand-edits the manifest row, as TOOL-dWellOiledMachine-20 S4 states, and records that it did

## 4. Design

### The declaration

```toml
# tools/integrations/ci/action-pins.toml
[[action]]
name = "actions/checkout"
sha = "d23441a48e516b6c34aea4fa41551a30e30af803"
tag = "v6.1.0"
```

The rows at base read `.github/workflows/remote-ci.yml:58` and `:137` (checkout) and `:118` and `:330`
(upload-artifact). PINNED at `f4597719`. The setup-python row takes the value
TOOL-dSafePassage-12 landed, re-read by the build pass.

### Why a line reader

The stdlib ships no YAML reader and M3's veto 2 refuses a dependency, the reason TOOL-dSafePassage-12 §8
F1 gives. Only two shapes are read, and both are indentation-stable: a `uses:` line, with an optional
`- `, and a `permissions:` key followed by deeper-indented `key: value` lines.

```python
USES = re.compile(r"^\s*(?:-\s+)?uses:\s*(?P<ref>\S+)(?:\s+#\s*(?P<tag>\S+))?\s*$")
```

A `uses:` of a local path, `./x`, has no `@` and is refused as well: an emitted template holds none and
gov's workflow holds none.

### The render

`render` substitutes three tokens and nothing else, so GitHub's own `${{ }}` passes untouched, and it
refuses any `{{[A-Z_]+}}` left in the result. `{{PREFIX}}` is the target's install prefix, from its
receipt. `{{DEFAULT_BRANCH}}` comes from the remote ladder, the `remote_ladder_py` inline block
(`tools/govkit/govkit.py:555-558`).

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `action-pins.toml`, `[[action]]` | declaration | `tools/integrations/ci/` |
| `ci_emit.py`, `render`, `check` | module and verbs | `tools/integrations/ci/` |
| `read_action_pins`, `render_template`, `check_emitted` | functions | `ci_emit.py` |
| `gov-bar.template.yml`, `.github/workflows/gov-bar.yml` | template and emitted file | the kit, and the adopter's tree |
| `# gov:ci-emit` | marker line | the emitted file |
| `emitted ci pins`, `emitted ci self-test` | gate legs | `tools/integrations/kit.toml` |

`lexicon.py --suggest <name> --as py.function` printed OK for the three functions on 2026-10-30. The
lexicon declares no `py.file` cell, so the module name asks nothing of it.

### Rollout

Dark for every adopter: nothing is emitted until one declares `[gate_runner.ci]`. Gov's bar gains the
leg at the landing. The comment change in `.github/workflows/remote-ci.yml` moves that file's blob.
Where `verdict.remote.pin` is set, the owner re-pins once, as for any edit to that file (§8 F1).

### Files touched (estimate)

- `tools/integrations/ci/action-pins.toml`
- `tools/integrations/ci/ci_emit.py`
- `tools/integrations/ci/gov-bar.template.yml`
- `tools/integrations/kit.toml`
- `tools/gate-legs.json`, rendered from the kit's `[[gate_leg]]` rows by `leg_factory.py --write`
- `.github/workflows/remote-ci.yml`
- `tools/govkit/govkit.py`
- `help/emitted-ci.md`
- `help/README.md`

### Alternatives rejected

- **Rendering gov's workflow through a `[[generated]]` row.** The test: `regen.py --write` runs in every
  landing, so a pin edit would move the blob `verdict.remote.pin` covers at a landing no one reviewed as
  a workflow change, and every gov-specific step of a 340-line file would have to become template text.
  A parity leg keeps the workflow human-edited and still reds a drift (§8 F1).
- **A `uses:` ban in an existing leg.** The test: `check-kit-placeholders.py` reads declarations, and no
  leg opens a template's render, so none sees the emitted text.
- **Shipping an already rendered workflow as an `engine` file.** It carries no default branch or prefix
  of the adopter's, and a row whose bytes differ per target is what `rendered` is for.

## 5. Production-readiness checklist

- security: emitted workflows run on the repository's token, so `contents: read` is the one grant and a
  `write` value reds the leg. Each action is pinned by sha, so a moved tag cannot change what an adopter
  runs. `render` writes one fixed path and refuses to overwrite a file it did not emit.
- perf / scale: the leg reads a few files, seconds at most, and runs no network.
- error / empty / loading states: a malformed row refuses naming it, an unresolved token refuses naming
  it, and no `[gate_runner.ci]` is one line and exit 0.
- observability: one line per finding, with file and line, and a count of templates, `uses:` lines and
  rows read, so an empty population cannot read green: zero `uses:` lines read is a finding.
- risks: a pin's tag comment is text, so a row's `tag` can lie about its `sha`. Nothing but the person
  editing the row checks that. An adopter who hand-edits the emitted file loses the edit at the next
  render, since it carries the marker.
- testing: the probes of §6 and the module's in-file arms (§7).
- migration: N/A — no adopter holds an emitted file, so nothing moves.
- user docs: `help/emitted-ci.md`, S8.

## 6. Acceptance criteria

- **AC1** — When `python ci_emit.py check --workflow .github/workflows/remote-ci.yml` runs on the tree,
  it exits 0 and prints a count of templates, `uses:` lines and rows, each above zero.
  Red when: any `uses:` differs from its row, or the count reads zero and the check still exits 0.
  figure: the counts are DERIVED at observation time.
- **AC2** — When `python ci_emit.py check --root <scratch copy>` runs with the template's checkout line
  planted as a literal `uses: actions/checkout@v6`, it exits 1 naming the file and line.
  Red when: a tag-pinned `uses:` passes, the clause's seen-red case.
  fixture: a scratch copy of the kit directory.
- **AC3** — When `python ci_emit.py check --root <scratch copy>` runs with a row's `tag` changed, so the
  rendered comment still matches but the workflow's does not, it exits 1. With a template `uses:`
  holding a 40-hex sha and no `#` comment it also exits 1.
  Red when: the sha alone is compared and the tag comment goes unread.
- **AC4** — When `python ci_emit.py check --root <scratch copy>` runs with `contents: write` planted in
  the template's `permissions:`, then with the top-level block deleted, then with `write-all`, each exits
  1 naming the file.
  Red when: a template holding no `permissions:` passes, so the job takes the repository's default token.
- **AC5** — When `python ci_emit.py check --workflow <scratch copy>` runs on a copy of gov's workflow with
  one `uses:` planted at another sha, it exits 1 naming that line.
  Red when: gov's workflow drifts from the one declaration with no leg seeing it.
- **AC6** — When `python ci_emit.py render --target <fixture>` runs with `[gate_runner.ci]` declared, the
  fixture gains `gov-bar.yml` whose first line is `# gov:ci-emit` and whose `uses:` lines
  equal the rows, and a second run changes no byte. With the table absent it prints `not declared` and
  writes nothing. With a marker-less file at that path it exits 2 and the file keeps its bytes.
  Red when: emission runs for an adopter that did not opt in, or overwrites the adopter's own workflow.
  fixture: a scratch repository under `%TEMP%`.
- **AC7** — When `python ci_emit.py check --root <scratch copy>` runs with a row no file uses added to
  `action-pins.toml`, it exits 1 naming the row.
  Red when: a stale pin sits in the declaration unread.
- **AC8** — When `python ci_emit.py check --root <scratch copy>` runs with a row's `sha` planted as 39 hex
  digits, then with a repeated `name`, each exits 2 naming the row.
  Red when: a malformed declaration reaches a render.
- **AC9** — When `grep -n 'action-pins.toml' .github/workflows/remote-ci.yml` runs, it prints the amended
  header, and `grep -c 'no permanent gate grades' .github/workflows/remote-ci.yml` prints `0`.
  Red when: the header still says no gate grades the file.
- **AC10** — When `grep -n 'emitted-ci.md' help/README.md` runs, it prints the page's row.
  Red when: an adopter has no page saying how to opt in.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/integrations/ci/ci_emit.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 · planted templates and a planted workflow copy: a tag-pinned `uses:`, a sha with no comment, a wider `permissions:` value, an unused row and a malformed row; the leg `emitted ci self-test` runs it · none
New arm: tools/integrations/ci/ci_emit.py · covers AC1 · the leg `emitted ci pins`, whose failing case is AC2's plant on the tree itself · none

What these do not check: that a pinned sha is the sha its tag names upstream, that the emitted job passes
on a real runner, or anything in a workflow file other than its `uses:` and `permissions:` lines.

## 8. Open questions

- **F1 — Does gov's workflow render from the declaration, or stay hand-edited under a parity leg (scout C
  F2)?** Options: (a) a `[[generated]]` render; (b) a parity leg over its `uses:` lines. Both read one
  declaration, the clause's bound. (a) moves the blob `verdict.remote.pin` covers inside a landing's regen
  and turns a 340-line gov-specific file into a template. (b) moves it only when a person edits the file.
  RESOLVED (agent, 2026-10-30, delegated): (b), rung 3, which meets the clause with the smaller write
  surface. It amends the file's header once, one blob move an owner re-pins where a pin is set.
  widens: none · relaxes: none
- **F2 — What does "optional" select on?** Options: (a) the existing `[gate_runner.ci]` table, whose
  validator already exists; (b) a new policy key, which the packet's key list does not hold and a new row
  would break the catalogue's rule. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the seam M5
  found. widens: none · relaxes: none
- **F3 — What does the emitted workflow run?** Options: (a) the bar on a default-branch push; (b) research's
  bar, scheduled receipt sync and currency probe. (b) reads currency, DEPL-dShippedRelease-7's, and the
  clause names neither job. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the least that closes
  `gap-deploy-03`. widens: none · relaxes: none
- **F4 — What happens to an adopter's own file at the destination?** Options: (a) refuse without the
  marker; (b) overwrite. (b) destroys adopter bytes (veto 3). RESOLVED (agent, 2026-10-30, delegated):
  (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft.

## 10. Reuse audit

The seams extended are the validator `[gate_runner.ci]` at `tools/govkit/govkit.py:6001-6005`, reused
as the opt-in, and `.github/workflows/remote-ci.yml` as gov's own instance, plus the `rendered` role of
`UNLANDED_REASON` (`tools/govkit/govkit.py:405`) for "written by this kit's own adopter".
`reuse_lookup.py "emit a CI workflow template with pinned action shas"` ranked `emit`, `load_workflows`
and `build_remote_ci_red_streak`, each a name-stem neighbour: none emits CI, and the map scans no
`.github/` file. Scout C's seam rows held at `f4597719`, and its disagreement 2 stands: research cites
the validator at `:5746` and it sits at `:6001`. `uses:` scanning exists nowhere: "no existing seam fits"
for the check itself, and `tools/memory-tree/routed_commits.py:248` is a message. The recall probe found
shape-audit M33 (`2026-10-18-review-PLAY-dClosedLoop-1-shape-audit-a.md:484`), whose fix this clause is.
Candidates rejected and their tests are under §4 "### Alternatives rejected".

Recall terms used: `python tools/memory-recall/query.py "how is emitted CI pinned by sha with least privilege permissions" --terms "emitted CI uses pinned sha tag comment permissions remote-ci workflow gate_runner ci-emit action pins"`

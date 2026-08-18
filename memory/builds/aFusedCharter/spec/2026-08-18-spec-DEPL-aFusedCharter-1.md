# DEPL-aFusedCharter-1 — the deploy path becomes a program, and the customize companion retires

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams deployer

## 1. Goal

Replace `parallel-coding-governance.customize.md` — prose instructing a human agent to fill 27
placeholders and hand-delete ten conditional blocks — with a renderer that derives what the target
repo can answer, refuses what it cannot, drops the blocks the target has no kit for, and writes the
result into the target's charter as a re-renderable region.

## 2. Scope (IN)

**S1 — Ship a `tools/playbook/` kit** holding `render_playbook.py` (the engine) and
`adopt-playbook.sh` (the adopter and its `--check` mode). This is the kit shape every other adopter
in this repo already has, and it is why the playbook entry's `why_no_adopter` reason retires with it.

**S2 — Declare every placeholder as data, in three classes.** The declaration is a `[[placeholder]]`
array in `tools/govkit/entries/playbook.kit.toml`, beside the entry it describes rather than in a
file of its own, because `needed_answers()` in `tools/govkit/govkit.py` already reads descriptors to
decide what `intake` must ask for. Each row carries a key, a class, and one line of guidance — the
useful residue of the retiring companion.

- `derived` — a named probe computes it from the target repo. The renderer RUNS the probe and prints
  what it derived, so a wrong derivation is visible rather than silent.
- `asked` — it must come from `deploy.toml`'s answers table. Absent is a refusal naming the key.
  Nothing is guessed; that rule is govkit's and this unit inherits it rather than restating it.
- `defaulted` — a declared default applies, and the render records in its summary that it defaulted.
  A default that is silently identical to an answer is how an operator ships a value they never
  chose.

**S3 — Teach `needed_answers()` the `asked` class.** Ten lines: the function scans a descriptor's
destinations, hole probes, gate-leg argv and adopter argv for lowercase brace tokens; it gains the
`[[placeholder]]` rows whose class is `asked`. It must also be SELECTION-AWARE for placeholders that
live only inside a conditional block: a row carries an optional gating kit id, and a row gated on an
unselected kit is not asked for. Without that, `intake` demands a design-token path from a target
that selected no design system.

**S4 — Drop conditional blocks by selection.** `PLAY-aFusedCharter-1` S8 fences each block with an
HTML comment naming the kit that justifies it. The renderer reads `deploy.toml`'s kit list and
deletes every fenced block whose kit is not in it, fences included. A fence naming a kit id that is
not a registry entry is a REFUSAL, not a skip — an unrecognised id would otherwise mean the block
always survives, which is the failure that reads as success.

**S5 — Write into a marker region, never over a file.** The render lands between
`<!-- gov:playbook -->` and its closing marker inside the target's charter. Absent charter: create
it holding only the region. Present charter with no region: append the region and leave every
authored byte alone. Present charter with a region: replace the region's contents and nothing else.
This is the same marker-region contract `tools/memory-tree/gen_build_index.py` already ships and
`tools/memory-tree/marker-contract.test.sh` already grades, and this unit uses that contract rather
than inventing a second one.

**S6 — `--check`, and a gate leg.** `adopt-playbook.sh --check` re-renders from the shipped template
and the target's own answers and byte-compares against the region in the charter, exiting non-zero
on a difference. It is wired as a gate leg exactly like `adopt-unattended.sh --check`,
`adopt-memory-recall.sh --check` and `adopt-drift-audit.sh --check`. It also asserts, as a SEPARATE
predicate with its own failure message, that no brace-shaped placeholder survived in the rendered
region — because template parity and placeholder completeness are two questions, and a conf
declaring nothing for a key renders a region that is perfectly in sync and still tells the agent to
invoke a placeholder's name.

**S7 — Close the `playbook-placeholders` hole.** The entry declares an authoring hole whose
discharge probe greps the deployed files for a surviving placeholder. With a renderer, the hole is
discharged by the adopter rather than by an operator, so the entry gains an `[adopt] argv`, loses
`why_no_adopter`, and the `[check] none` reason is replaced by the adopter's real argv.

**S8 — Retire `parallel-coding-governance.customize.md`, moving what a program cannot do.** Three
kinds of content survive and each has a destination. The per-placeholder guidance becomes the
`[[placeholder]]` rows' one-line `why`. The conditional-section rulings become the fences and their
kit ids. What remains is genuinely non-mechanical and moves to `WIRE-INTO-PROJECT.md`: the judgment
calls about which kits a project should adopt, the note that the memory tree is not droppable
because two sections are written against it, the re-pull procedure, and the warning that a dropped
block whose kit is absent leaves a rule nothing can make true. `TOOL-aFusedCharter-1` performs the
`git rm`.

## 3. Non-goals (OUT)

**No interactive prompting.** `intake` is non-interactive by design and refuses to invent an answer.
The renderer inherits that posture: it derives, it reads answers, or it refuses naming the key.

**No new govkit verb.** The renderer is a kit adopter, which `apply` already runs. Adding a verb
would put the playbook's deploy path outside the mechanism every other kit uses.

**No `apply`-side content substitution.** A `templated` role that substituted inside the deployer's
write path would put placeholder logic into the highest-risk code in this repo — the one guarded by
`tools/govkit/refusal_join.py` — for a property one kit needs. The adopter seam already exists.

**No change to which files the entry ships.** After `TOOL-aFusedCharter-1` the entry ships one file.
This unit changes what happens AFTER it lands.

**No render of this repo's own charter.** `PLAY-aFusedCharter-3` owns `AGENTS.md`. This unit builds
the renderer and proves it on a fixture target.

## 4. Design

### Data model

A placeholder row, as declared in the descriptor:

```toml
[[placeholder]]
key = "GATE_RUNNER"
class = "derived"
probe = "gate_runner"
why = "the one command that runs the whole local bar"
```

Classes and their contract: `derived` names a probe function in `render_playbook.py`; `asked`
carries no probe and no default; `defaulted` carries a `default` string. An optional `kit` field
gates the row on a selected kit. A row whose class is `derived` and whose probe returns nothing
falls through to REFUSAL, never to a default it did not declare — a probe that quietly returns the
empty string is how a charter ships with a blank where a branch name belongs.

### Inventory

The 27 placeholders surviving `PLAY-aFusedCharter-1`'s cuts, by class. Counts are stated nowhere in
the shipped files: `adopt-playbook.sh --check` derives every population figure, because a count
written in prose beside a table rots between edits and this repo has that defect on record twice.

| Class | Members |
|---|---|
| derived | project name · default branch · memory root, disciplines and id families from the memory-tree conf · the CI workflow file · the gate runner · the lexicon conf's presence · this node's tag, machine, primary tree and worktree root |
| asked | stream ownership · the doc routing table · the product preamble · the repo layout map · the command catalog · the product context home · gate commands · the commit trailer · the worktree script · the kind-factory map · shared primitives location · toolchain notes |
| defaulted | help dir · review dir · prose audit |

The fleet rows are the interesting case: the CURRENT node is derivable from hostname, username and
the repo root, and every OTHER node is not derivable at all. The renderer therefore derives one row
and asks whether more exist, rather than pretending a one-node registry is complete.

### Migration

`intake` refuses to overwrite an existing `deploy.toml`, so a target that already has one gains its
new answers by editing that file — deliberately, since it is the standing authorization for an
unattended re-run. The renderer must therefore report a MISSING answer key by name and stop, and its
message names the file to edit. A target with no descriptor is told to run `intake` first.

### Rollout

The renderer is proven against `tools/govkit/matrix.py`'s existing repo SHAPES before it is pointed
at anything real: an empty repo, a repo with no Python, a repo whose pre-commit refuses, and a repo
with an already-red gate leg. Each arm asserts a message or an on-disk effect and never an exit code
alone, per that harness's stated rule.

### Alternatives rejected

**Keep `customize.md` and add a script beside it.** Rejected: the catalogue and the program are two
answers to one question, and the catalogue is the copy that rots — this repo already gates that
arithmetic with `check-playbook-parity.sh` S3 precisely because it drifted.

**Put the placeholder table in its own TOML under `tools/playbook/`.** Rejected on the tie-break
that a seam already exists: `needed_answers()` reads descriptors, and a second declaration file
would mean `intake` and the renderer disagree about what a target must supply.

**Render over the whole charter rather than a region.** Rejected by the owner's resolution at
kickoff, and independently by the fact that a target's own project content has nowhere else to live.

### Files touched (estimate)

New: `tools/playbook/render_playbook.py`, `tools/playbook/adopt-playbook.sh`,
`tools/playbook/README.md`, `tools/playbook/kit.toml`, and a test.
Edited: `tools/govkit/entries/playbook.kit.toml`, `tools/govkit/govkit.py` (S3 only),
`tools/govkit/registry.toml`, `tools/gate-legs.json`, `WIRE-INTO-PROJECT.md`,
`memory/map/features/` (a dossier for the new kit).

## 5. Production-readiness checklist

- security — the renderer WRITES into a repository gov does not own. It writes one marker region and
  refuses every other path; the refusal set is what `tools/govkit/refusal_join.py` will need to see
  armed if the engine ever moves inside govkit, which `§3` forbids.
- perf / scale — N/A; one file, one pass.
- a11y — N/A.
- i18n — the template carries non-ASCII glyphs and the renderer must read and write bytes with an
  explicit encoding, never a platform default. The gate-lint kit exists because a platform default
  decoded an em dash into a parse error.
- error / empty / loading states — the three states in S5 (no charter, charter without a region,
  charter with one) are the empty and populated cases and each is an arm.
- observability — the render prints what it derived, what it defaulted, and which blocks it dropped.
  A silent render is indistinguishable from one that dropped everything.
- risks — writing into a foreign repo is the highest-consequence act in this build. Mitigated by the
  region contract, by refusing rather than guessing, and by proving against the four repo shapes
  before any real target.
- testing + left-shift gates — a kit test plus the `--check` leg from S6.
- migration / rollback — the region is delimited, so removing it restores the charter exactly.
- user docs — `WIRE-INTO-PROJECT.md` receives S8's residue and the kit ships a README.

## 6. Acceptance criteria

- **AC1** — When `bash tools/playbook/adopt-playbook.sh` runs against a fixture target holding a
  `deploy.toml` with every asked key, the target's charter gains a `gov:playbook` region and
  `grep -cE '\{\{[A-Z]' ` over that region returns `0`.
- **AC2** — When one asked key is removed from `deploy.toml`, the adopter exits non-zero and its
  message names that key and the file to edit; it writes no byte, verified by comparing the
  target's charter before and after.
- **AC3** — When a fixture target's `deploy.toml` kit list omits a kit, every block fenced for that
  kit is absent from the rendered region, its fences included, and every block for a selected kit is
  present — counted with `grep -c 'kit:'` over the region.
- **AC4** — When a fence names an id absent from `tools/govkit/registry.toml`, the renderer refuses
  and names the id — it does not leave the block in place.
- **AC5** — When the adopter runs twice, the second run leaves the charter byte-identical, and
  authored content outside the region is byte-identical after both — checked with `cmp`.
- **AC6** — When `bash tools/playbook/adopt-playbook.sh --check` runs after a deliberate one-byte
  edit inside the region, it exits non-zero naming the drift; after a one-byte edit OUTSIDE the
  region it exits 0.
- **AC7** — When the region is made to contain a surviving placeholder without otherwise drifting,
  `--check` still reds, with a message distinct from the parity one — the two predicates fail
  separately.
- **AC8** — When `python tools/govkit/govkit.py intake` runs for a selection excluding a
  conditional kit, it does not demand that kit's placeholder, and it does demand every ungated
  `asked` key — observable in the refusal message's key list.
- **AC9** — When `python tools/govkit/govkit.py selfcheck` and `python tools/govkit/selftest.py`
  run, both exit 0 with the playbook entry declaring an adopter and no `why_no_adopter`.
- **AC10** — When `python tools/govkit/matrix.py` runs, the renderer's arms pass against all four
  repo shapes, each asserting a message or an on-disk effect.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` ·
`install-prefix (shipped surface)` · `playbook parity` · `codebase-map coverage + freshness` ·
`kit version markers` · `testsuite counts` · `run-gates canary` · the new
`playbook render wiring` leg · the full bar. A new kit dir and a new leg together trip a growing set
of meta-gates, so the full bar is the instrument rather than this list.

## 8. Open questions

none — the forks below are RESOLVED.

- **F1 — where does the renderer live?** RESOLVED (agent, 2026-08-18, delegated by the build's
  stated order): a `tools/playbook/` kit with an adopter, on the tie-break that reuses an existing
  seam. Every other kit in this repo renders its own artifacts through its own adopter, and `apply`
  already runs one.
- **F2 — where is the placeholder declaration?** RESOLVED (agent, 2026-08-18, delegated): in the
  govkit descriptor, because `needed_answers()` already reads descriptors and a second file would
  let `intake` and the renderer disagree.
- **F3 — does the render-parity check need its own gate?** RESOLVED (agent, 2026-08-18, delegated):
  no. `--check` on the adopter is this repo's established wiring-leg idiom and three kits already
  use it. This removes a unit an earlier draft of the build carried.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft. F3's resolution folded the render-parity gate into this
  unit's `--check`, which is why the build roster carries seven units and not eight.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render a shipped template into a target repo from a conf"`
routes to the adopter-plus-check pattern shared by `tools/unattended/adopt-unattended.sh`,
`tools/memory-recall/adopt-memory-recall.sh` and `tools/drift-audit/adopt-drift-audit.sh`. All three
render a template against a conf and expose `--check` as a gate leg; this unit extends that pattern
to the playbook, which is the one shipped artifact that never had it. The second seam is
`tools/memory-tree/gen_build_index.py`'s marker-region contract, whose four live readers are already
graded by one case table — S5 uses it rather than writing a fifth reader.

Recall terms used: `playbook customize placeholder deploy render adopter intake answers descriptor
conditional block kit selection marker region refuse`. The binding prior records are
`TOOL-aSealedCaravan-1`, which built the registry and the hole model this unit discharges, and
`DEPL-aFerriedDossier-1` and `-3`, OPEN rows recording that a hand-forked repo has no update path
and that thirteen deployer defects were measured with line numbers — this unit must not claim to
close either, and its `--check` leg is the first mechanism that gives a playbook install any update
path at all.

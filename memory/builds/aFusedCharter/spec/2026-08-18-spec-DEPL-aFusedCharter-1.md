# DEPL-aFusedCharter-1 — the deploy path becomes a program, and the customize companion retires

**Status:** OPEN · rev-5 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams deployer

## 1. Goal

Replace `parallel-coding-governance.customize.md` — prose instructing a human agent to fill every
placeholder by hand and delete the conditional blocks their project has no kit for — with a renderer
that derives what the target repo can answer, refuses what it cannot, drops those blocks by
selection, and writes the result into the target's charter as a re-renderable region.

## 2. Scope (IN)

**S1 — Ship a `tools/playbook/` kit under a NEW registry entry id, `playbook-render`.** It holds
`render_playbook.py` (the engine) and `adopt-playbook.sh` (the adopter and its `--check` mode). This
is the kit shape every other adopter in this repo already has.

**The id must be new, and an earlier revision left that ambiguous.** `tools/govkit/registry.toml`
already declares an entry `playbook` — the root files this build renames — and `read_descriptors()`
keys its map by id with no duplicate predicate, so a second `playbook` entry would SILENTLY shadow
the first and the shadowed entry's claimed files would then red as unclaimed surface. The registry's
`[surface]` also globs `tools/*`, so `tools/playbook/` must be an entry or an exemption either way.
S7 below says which of the two entries gains an `[adopt] argv` and which keeps the hole, because
"the entry" was ambiguous across two entries.

**S1b — Couple the two entries, because a selection can otherwise take one without the other.**
`needed_answers()` iterates the SELECTION, and `derive_install_order` consults `requires` for
ordering while dropping a dependency that is outside the selection. The `[[placeholder]]` and
`[[block]]` arrays live on `playbook`, which is in `[selection] default`; the renderer lives on
`playbook-render`, which is new and unlisted. A default install would therefore have `intake` demand
every ungated `asked` key with no renderer to consume them — and `intake` refuses to overwrite the
`deploy.toml` it just wrote, so the operator cannot simply re-run it. The reverse selection installs
a renderer with no declarations to read. `playbook-render` declares `requires = ["playbook"]`, and
this spec states whether it joins `[selection] default`: it does, because a target taking the
playbook and not the thing that renders it receives a file full of placeholders.

**S1a — Name the leg's registry route, rather than leaving it to the build.** `govkit selfcheck`
fails a gate leg claimed by no descriptor and carried by no `[[exempt_leg]]`, and fails one that is
BOTH. The `playbook render wiring` leg and the kit's self-test are declared as `[[gate_leg]]` rows in
`playbook-render`'s own descriptor. `tools/playbook/` also joins the derived kit set that
`check-playbook-parity.sh` grades, so the playbook or `WIRE-INTO-PROJECT.md` must NAME it, or it
needs a row in `tools/playbook-kit-waivers.txt` — the same trap `PLAY-aFusedCharter-1` S6 hits for
the lexicon kit.

**S1c — Add the duplicate-id predicate `selfcheck` does not have.** S1 measured that a second entry
sharing an id would SILENTLY shadow the first, because `read_descriptors()` assigns into a dict with
no duplicate check and no arm greps for one. This unit adds two entries to that registry, so it is
the unit that should close the gap rather than rely on having avoided it: three lines in `selfcheck`
that fail on a repeated `[[entry]]` id, plus an arm in `tools/govkit/selftest.py` that observes the
failure. Without it, AC12's "no id is declared twice" asserts a check nothing performs — the
assertion-about-nothing shape this repo gates on.

**S2 — Declare every placeholder as data, in three classes.** The declaration is a `[[placeholder]]`
array in `tools/govkit/entries/playbook.kit.toml` — the `playbook` entry, not the new
`playbook-render` one, because the placeholders describe the ARTIFACT that entry ships and
`needed_answers()` in `tools/govkit/govkit.py` quantifies over every selected descriptor either way
and already reads them to decide what `intake` must ask for. Each row carries a key, a class, and one line of guidance — the
useful residue of the retiring companion.

- `derived` — a named probe computes it from the target repo. The renderer RUNS the probe and prints
  what it derived, so a wrong derivation is visible rather than silent.
- `asked` — it must come from `deploy.toml`'s answers table. Absent is a refusal naming the key.
  Nothing is guessed; that rule is govkit's and this unit inherits it rather than restating it.
- `defaulted` — a declared default applies, and the render records in its summary that it defaulted.
  A default that is silently identical to an answer is how an operator ships a value they never
  chose.

**S3 — Teach `needed_answers()` the `asked` class, and give the fence names a declaration site.**
The function scans a descriptor's destinations, hole probes, gate-leg argv and adopter argv for
lowercase brace tokens; it gains the `[[placeholder]]` rows whose class is `asked`. It must also be
SELECTION-AWARE for placeholders that live only inside a conditional block: a row carries an optional
gating kit id or block name, and a row gated on an unselected kit or a dropped block is not asked
for. Without that, `intake` demands a value for a section the target will not receive.

**The `when:` names need their own declaration, which an earlier revision never gave them.** A
`[[placeholder]]` row's optional field was the only carrier, and the surviving conditional sections
carry ZERO placeholder tokens between them — so there was no row to hang a name on, and S4's refusal
on an undeclared name would have fired on every fence. The `playbook` descriptor therefore gains a
`[[block]]` array, one row per fenceable block, each with a `name` and a `why`. That array is the
declared set S4 validates fences against, and it is what makes `drop_blocks` checkable: a member
naming no declared block refuses at `intake` rather than silently dropping nothing at render.

**S4 — Drop conditional blocks, over both fence namespaces, and NEITHER reads a boolean.**
`PLAY-aFusedCharter-1` S8 fences each block in one of two namespaces, because two of the
conditionals are keyed on a project property with no kit id to name.

- A `kit:` block drops when its id is absent from `deploy.toml`'s `kits` list.
- A `when:` block drops when its NAME is a member of `deploy.toml`'s `drop_blocks` list.

**`drop_blocks` is a list and not a set of booleans, and that is the whole point.** `cmd_intake`
writes every answer as `key = "value"`, so a key "answered false" arrives as the STRING `false`,
which is truthy under every natural reading, and the block survives — the failure that reads as
success, arriving through type coercion rather than through a name. Membership in a list has no such
reading: a name is present or it is not. Owner-resolved 2026-08-18 over two alternatives, dropping
the namespace entirely and building a full per-key declaration array.

Both namespaces refuse rather than skip. A `kit:` fence naming an id that is not a registry entry is
a REFUSAL; a `when:` fence naming a block the descriptor's declared block set does not carry is a
REFUSAL; and a `drop_blocks` MEMBER matching no fence in the rendered file is also a refusal, because
a list entry that drops nothing is either a typo or a block that has already gone.

**S5 — Write into a marker region, never over a file.** The render lands between
`<!-- gov:playbook -->` and its closing marker inside the target's charter. Absent charter: create
it holding only the region. Present charter with no region: append the region and leave every
authored byte alone. Present charter with a region: replace the region's contents and nothing else.
**The renderer carries its OWN reader, and an earlier revision claimed otherwise on two counts.**
`gen_build_index.py`'s region helper RAISES when no marker pair is present, so it serves neither the
absent-charter state nor the charter-without-a-region state — region CREATION lives in that script's
build-README slot walk, not in the helper. And `marker-contract.test.sh` slices four reader bodies BY
HAND against one case table; a fifth reader is invisible to it until it is added, and that test's own
header states the design is several implementations proven to agree rather than one shared
implementation, because a cross-kit edge is what it forbids. So this unit writes a fifth reader,
obeys the CONTRACT rather than reusing the code, and adds itself as a fifth column to that case
table — with an acceptance criterion on the reader count, so a sixth reader cannot land unnoticed.

**The fifth reader needs a loud SKIP, because the case table ships to adopters.**
`marker-contract.test.sh` is a `[[gate_leg]]` of the memory-tree kit, whose file rule includes
everything under it, so an adopter installing memory-tree receives that test. An adopter who has
memory-tree and NOT `tools/playbook/` would get a red leg for a kit they never took. That file
already handles its one existing cross-kit dependency with a loud skip that exits 0, and the playbook
reader takes the same treatment. The reader count is stated in three places in that file — its
header, its skip text and its pass line — so AC13 asserts all three rather than one, since an
adopter hitting the pre-existing skip would otherwise never run the new reader while AC13 read
green.

**S5a — The comparison normalises line endings before it compares.** Measured on this node,
`core.autocrlf` is `true` and `AGENTS.md` carries no `eol` attribute: its committed blob holds zero
carriage returns and its worktree copy holds 302, while the ruleset is pinned `eol: lf`. A render
from an LF source byte-compared against a CRLF charter mismatches on every line, on every node.
`TOOL-aFusedCharter-1` S4b adds the missing `.gitattributes` pins; this unit ALSO normalises before
comparing, because an adopter has not adopted gov's `.gitattributes` and a pin nobody applied
protects nobody.

**S6 — `--check`, and a gate leg.** `adopt-playbook.sh --check` re-renders from the shipped template
and the target's own answers and byte-compares against the region in the charter, exiting non-zero
on a difference. It is wired as a gate leg exactly like `adopt-unattended.sh --check`,
`adopt-memory-recall.sh --check` and `adopt-drift-audit.sh --check`. It also asserts, as a SEPARATE
predicate with its own failure message, that no brace-shaped placeholder survived in the rendered
region — because template parity and placeholder completeness are two questions, and a conf
declaring nothing for a key renders a region that is perfectly in sync and still tells the agent to
invoke a placeholder's name.

**S7 — RETIRE the `playbook-placeholders` hole rather than closing it, and say which entry changes
what.** The hole's discharge probe greps `{playbook_path}` — the UN-RENDERED template, which must
keep its placeholders permanently by design — so it can never come true, and an earlier revision's
"the hole is discharged by the adopter" was not reachable. Worse, the render now lands in the
target's CHARTER, which that entry has no file rule and no token for, so there is nothing for the
probe to point at either. The question the hole was asking is now owned by S6's `--check`, whose
second predicate is exactly *did a placeholder survive the render*. So the hole is deleted from the
`playbook` entry, and the `playbook` entry keeps its `seed` file rule and nothing else. The
`[adopt] argv` belongs to the NEW `playbook-render` entry, which is the one with an adopter.

**Three prose strings outlive the hole and each becomes false when it goes**, none of them reached by
any gate: the entry's `[check] none` reason and its `why_no_adopter`, both of which name the hole as
the thing that observes the placeholders, and `tools/check-placeholders.sh`'s own header, which
records that the render-side owner of the survival predicate "already exists and stays where it is"
and points at that hole. S6's `--check` is the new owner and all three are rewritten to say so.

**S7a — State what the new leg DOES on this repo's tree before unit 5 exists.** Every comparable
wiring leg runs unguarded against gov's own tree and expects a rendered artifact to be there. This
one has nothing to compare until `PLAY-aFusedCharter-3` writes `.governance/deploy.toml` and the
region — and this spec's Non-goals forbid rendering gov's charter here, while Migration says a target
with no descriptor is TOLD TO RUN INTAKE, which is a refusal and therefore a red leg. The leg
therefore exits 0 with an explicit `not adopted here yet` line when no descriptor exists, in the same
shape `tools/lexicon/lexicon.py` uses for an unadopted project, and flips to a real comparison the
moment unit 5 lands. AC11 covers both states, so the leg is never green for the reason that nothing
was measured.

**S8 — Retire `parallel-coding-governance.customize.md`, moving what a program cannot do.** Three
kinds of content survive and each has a destination. The per-placeholder guidance becomes the
`[[placeholder]]` rows' one-line `why`. The conditional-section rulings become the fences and their
kit ids. What remains is genuinely non-mechanical and moves to `WIRE-INTO-PROJECT.md`: the judgment
calls about which kits a project should adopt, the note that the memory tree is not droppable
because two sections are written against it, the re-pull procedure, and the warning that a dropped
block whose kit is absent leaves a rule nothing can make true. `TOOL-aFusedCharter-1` performs the
`git rm`, and it does so three passes before this unit runs — so this unit reads the companion at the
build's pinned BASE rather than from the worktree. Stating that here is not pedantry: an earlier
revision had each of the two specs deferring the deletion to the other, which reads as if the file
were still present when the harvest happens.

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
gates the row on a selected kit, and an optional `when` field gates it on a boolean answer, matching
the two fence namespaces `PLAY-aFusedCharter-1` S8 declares.

**Two spellings meet here and exactly one place folds them.** govkit's token regex matches lowercase
brace tokens, so `needed_answers()` returns and `deploy.toml`'s answers table stores LOWERCASE keys,
while a playbook placeholder is written in upper case. The declaration's `key` is written in the
placeholder's own upper-case spelling; the fold to the answers-table spelling happens once, in
`needed_answers()`, and the renderer folds the same way when it looks a value up. Naming the single
fold site is the whole point — two independent case conversions is how a key silently fails to
match. A row whose class is `derived` and whose probe returns nothing
falls through to REFUSAL, never to a default it did not declare — a probe that quietly returns the
empty string is how a charter ships with a blank where a branch name belongs.

### Inventory

The placeholders surviving `PLAY-aFusedCharter-1`'s cuts, by class. **No count appears here or in any
shipped file** — `adopt-playbook.sh --check` derives every population figure. A count written in
prose beside a table rots between edits, and this spec proved it: an earlier revision said 27 over a
table that enumerated 27 while the measured set was 28, because the table had silently dropped the
per-node variances row. The table below is the enumeration and the measurement is the authority.

| Class | Members |
|---|---|
| derived | project name · default branch · memory root, disciplines and id families from the memory-tree conf · the CI workflow file · the gate runner · the lexicon conf's presence · this node's tag, machine, primary tree and worktree root |
| asked | stream ownership · per-node variances · the doc routing table · the product preamble · the repo layout map · the command catalog · the product context home · gate commands · the commit trailer · the worktree script · the kind-factory map · shared primitives location · toolchain notes |
| defaulted | help dir · review dir · prose audit |

The fleet rows are the interesting case: the CURRENT node is derivable from hostname, username and
the repo root, and every OTHER node is not derivable at all — and the per-node variances column is
not derivable even for this node, since a credential quirk or a harness launch config is knowledge
the operator has and the tree does not. The renderer therefore derives one row, asks for its
variances, and asks whether more nodes exist, rather than pretending a one-node registry is complete.

The measurement itself is worth stating once, because two of this build's units depend on it: the
union of both current files is 38 distinct placeholders with exactly one shared between them, and
the two deleted sections account for ten. Convergence also dissolves the shared/disjoint problem
entirely — with one file there is no second carrier for a placeholder to be shared with, which is
why `TOOL-aFusedCharter-1` S3 can delete the catalogue-arithmetic arm rather than repoint it.

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
`tools/playbook/README.md`, `tools/playbook/kit.toml`, `tools/govkit/entries/playbook-render.kit.toml`,
and a test.
Edited: `tools/govkit/entries/playbook.kit.toml`, `tools/govkit/govkit.py` (S3, S1c),
`tools/govkit/selftest.py` (S1c's arm), `tools/govkit/registry.toml`, `tools/govkit/matrix.py`
(AC10's arms), `tools/memory-tree/marker-contract.test.sh` (the fifth reader and its skip),
`tools/check-placeholders.sh` (its header names the hole S7 deletes), `tools/gate-legs.json`,
`WIRE-INTO-PROJECT.md`, `memory/map/features/` (a dossier for the new kit).

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
  run, both exit 0 with `playbook-render` declaring the adopter and `playbook` keeping `argv = []`
  and a `why_no_adopter` restated to name `adopt-playbook.sh --check` rather than the hole S7
  deletes. An earlier revision of this criterion predated the two-entry split and required the
  opposite — a builder discharging it literally would have put an adopter on `playbook` and produced
  exactly the two-adopter state S1 exists to prevent.
- **AC10** — When `python tools/govkit/matrix.py` runs, the renderer's arms pass against all four
  repo shapes, each asserting a message or an on-disk effect.
- **AC11** — When the `playbook render wiring` leg runs on THIS repo before unit 5 lands, it exits 0
  printing an explicit not-adopted line; after unit 5 lands it performs a real comparison, verified by
  editing a byte inside the region and confirming it reds. A leg that is green in both states for the
  same reason is measuring nothing.
- **AC12** — When `python tools/govkit/govkit.py selfcheck` runs, the two entries are distinct:
  `playbook` carries a `seed` file rule and no hole, `playbook-render` carries the adopter and both
  `[[gate_leg]]` rows. The duplicate-id clause is observable because S1c ADDS that predicate —
  checked by declaring a second entry with a repeated id in a fixture and confirming `selfcheck`
  names it.
- **AC15** — When a selection names `playbook-render` alone, the resolver pulls in `playbook`; when
  it names `playbook` alone, `intake` does not demand answers for a renderer the target is not
  installing. Both directions are observed, because the coupling is what S1b adds.
- **AC16** — When `deploy.toml` carries a `drop_blocks` member naming no declared block, `intake`
  refuses naming it; when it names a declared block, that block and its fences are absent from the
  render and every other block is present.
- **AC13** — When `bash tools/memory-tree/marker-contract.test.sh` runs, its case table drives FIVE
  readers including this renderer's, and its stated reader count equals the number it drives.
- **AC14** — When a charter with CRLF line endings is compared against an LF render, `--check` exits
  0; it reds only on a real content difference. Checked with a fixture whose only difference is the
  line ending.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` ·
`install-prefix (shipped surface)` · `playbook parity` · `codebase-map coverage + freshness` ·
`kit version markers` · `testsuite counts` · `run-gates canary` · `drift-audit records` ·
`naming lexicon` · the new `playbook render wiring` leg · the full bar. A new kit dir and a new leg
together trip a growing set of meta-gates, so the full bar is the instrument rather than this list.

Two of those are here because the spec audit found them missing. `drift-audit records` is gateable
against a zero pin that this unit's new leg would trip if `TOOL-aFusedCharter-1` S10 had not already
retired the signal — it is listed so the dependency is visible rather than assumed. And
`naming lexicon` runs on any diff under `tools/`, with a Python parser coverage mode and a shrink-only
verb-offender pin, so `render_playbook.py`'s definitions must lead with a verb from the declared
table; `render`, `derive`, `read`, `check` and `resolve` are all already in it, so compliance is free
if the spec says so and expensive if it does not.

## 8. Open questions

none — all four forks below are RESOLVED.

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
- **F4 — does the target descriptor belong at `.governance/deploy.toml`, or at a repo-root
  `.playbook.conf` matching this tree's four other conf files?** Recommendation: keep
  `.governance/deploy.toml`. It is govkit's existing location, `intake` already writes it and refuses
  to overwrite it, and moving it would change a deployer contract for cosmetic consistency. The spec
  audit flagged that it was never compared against the root-conf convention, which is fair — the
  comparison is made here and comes out for the status quo. RESOLVED (owner, 2026-08-18): keep
  `.governance/deploy.toml`. The four root confs are tuning knobs an adopter edits; this file is a
  committed authorization artifact that `intake` writes once and refuses to overwrite, and every
  other deployer verb already reads it there. No scope change.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft. F3's resolution folded the render-parity gate into this
  unit's `--check`, which is why the build roster carries seven units and not eight.
- rev-5 · 2026-08-18 · folded the round-2 spec audit. `when:` fences become MEMBERSHIP in a
  `drop_blocks` list rather than booleans, because intake writes every answer as a quoted string and
  a false would have read as true; new S3 text gives the fence names a `[[block]]` declaration array
  they never had; new S1b couples the two registry entries so a selection cannot take one without
  the other; new S1c adds the duplicate-id predicate S1 measured missing and AC12 assumed; the fifth
  marker-contract reader gains a loud skip because that test ships to adopters; AC9 is rewritten
  after contradicting S7 and AC12 since rev-3; three stale reason strings are named; §10 stops
  claiming the reuse S5 refutes; and three ACs are added.
- rev-4 · 2026-08-18 · F4 resolved by the owner: the target descriptor stays at
  `.governance/deploy.toml`. No scope change; the fork is now marked rather than pending.
- rev-3 · 2026-08-18 · folded the M4 spec audit. The kit gets its own registry id because a second
  `playbook` entry would silently shadow the existing one; S7 RETIRES the placeholder hole rather
  than closing it, because its probe targets the un-rendered template and can never come true; S5's
  claim to reuse the marker-region implementation is corrected to reuse the CONTRACT and add a fifth
  reader to its case table; new S5a and S1a and S7a cover line-ending normalisation, the leg's
  registry route and the leg's behaviour before unit 5 exists; the two token spellings get one named
  fold site; and four ACs are added.
- rev-2 · 2026-08-18 · the Inventory stated a placeholder count of 27 over a table enumerating 27,
  and the measured set is 28 — the per-node variances row was missing from the table and from the
  count. The count is deleted rather than corrected, per the rule the same paragraph states, and
  the missing member is added to the asked class.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render a shipped template into a target repo from a conf"`
routes to the adopter-plus-check pattern shared by `tools/unattended/adopt-unattended.sh`,
`tools/memory-recall/adopt-memory-recall.sh` and `tools/drift-audit/adopt-drift-audit.sh`. All three
render a template against a conf and expose `--check` as a gate leg; this unit extends that pattern
to the playbook, which is the one shipped artifact that never had it. The second seam is
`tools/memory-tree/gen_build_index.py`'s marker-region CONTRACT, graded by one shared case table
across several independent reader implementations. S5 conforms to that contract and adds a fifth
reader plus a fifth column to the table — it does not reuse the existing implementation, which raises
where two of S5's three states need it to create. An earlier revision of this paragraph claimed the
reuse S5 refutes.

Recall terms used: `playbook customize placeholder deploy render adopter intake answers descriptor
conditional block kit selection marker region refuse`. The binding prior records are
`TOOL-aSealedCaravan-1`, which built the registry and the hole model this unit discharges, and
`DEPL-aFerriedDossier-1` and `-3`, OPEN rows recording that a hand-forked repo has no update path
and that thirteen deployer defects were measured with line numbers — this unit must not claim to
close either, and its `--check` leg is the first mechanism that gives a playbook install any update
path at all.

# TOOL-cMendedVintage-6 — the receipt-sync leg, and its row on gov's own bar

**Status:** CLOSED · rev-4 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-TOOL-cMendedVintage-6-acceptance-ledger.md](../build/2026-09-17-build-TOOL-cMendedVintage-6-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-17-prompt-TOOL-cMendedVintage-6-2-build-brief.md](../prompts/2026-09-17-prompt-TOOL-cMendedVintage-6-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter has no way, on their own bar, to learn that a file govkit installed has drifted from the
hash the receipt records for it. The only reader of `.governance/install.json` is `govkit check`,
which needs a gov checkout beside the target and is invoked automatically by nothing. This unit
ships one small checker into the run-gates kit and declares it as a gate leg, so the integrity half
of that verb runs on every adopter's merge bar with no gov checkout present.

## 2. Scope (IN)

- **S1** A new shipped file `tools/run-gates/check-receipt.py` reads
  `<repo>/.governance/install.json` and, for every row whose `role` is absent or `"engine"`, reds
  when the file is missing and reds when its sha256 differs from `row["sha256"]`. The repo root is
  DERIVED from the file's own location through git, never spelled, and one optional positional
  argument names a different tree — which is what makes a fixture observable from the command line.
  Observed by AC3, AC4 and AC7.
- **S2** With no receipt on disk the run prints a line whose head is the literal word `SKIP`, names
  the path it looked for, and exits 0. It is written as a skip and never as a pass. Observed by AC1.
- **S3** The run carries its own liveness: a receipt that parses but yields ZERO graded rows reds
  with a `DEAD PROBE` message rather than reporting a clean target. Observed by AC5.
- **S4** The same file carries four built-in fixture arms over receipts it writes into a temporary
  directory — a clean row, a drifted row, an absent file, and a receipt with no engine rows. They run
  on every invocation and under `--selftest` alone, so the leg grades the checker even in a tree that
  holds no receipt. Observed by AC2.
- **S5** `tools/run-gates/kit.toml` gains a `[[gate_leg]]` naming this file, with
  `subject = "repo"`. Observed by AC6.
- **S6** `tools/gate-legs.json` gains the matching row — same name, same subject, `chunk` and a
  declared `ceiling` — in the SAME commit as S5. Observed by AC6.
- **S7** `tools/govkit/subject-pins.tsv` is regenerated in that same commit by
  `python tools/govkit/govkit.py selfcheck --write`, because a new leg with no pin row is a refusal
  in its own right. Observed by AC6.

## 3. Non-goals (OUT)

- No descriptor half and no provenance half. `govkit check` resolves each row's `source` and
  `commit` against a gov checkout, and `gov_oid` against gov's own blobs; neither is reachable from
  inside a target. This leg is the INTEGRITY arm only, and its own header says so.
- No `seed` row is hashed. The role's contract is that the target owns the file after one copy, so
  hashing it would red every target that did what the role exists to permit. `govkit check` scopes
  the same way and the reason is written there.
- No use of `.governance/install.sums` and no `sha256sum -c`. The sidecar is written from EVERY row
  carrying `sha256`, seed rows included, so verifying it reds the population the previous bullet
  deliberately exempts.
- No `merged`, `attributes` or `forked` row is read. A merged row's `sha256` is the whole merged
  file and its real contract is the marked block, which needs the extractor and the marker table.
- No change to `govkit check`. The two readers answer different questions from the same file and
  this unit adds the one an adopter can run.
- No reporting of `evidence` states. That is the next unit.
- No emission of the new leg into an already-installed target. gov emits gate legs from descriptors
  on `apply`, so an adopter receives this row on their next `apply` run; making `update` emit legs is
  a separate unit of this build and this one does not depend on it.

### Edges

- **consumes-from** external — the run-gates descriptor's `[[files]] include = "**"` engine rule,
  which is what carries a new file in that directory to an adopter. Nothing in this build changes it,
  and without it the script ships to nobody.
- **hands-off** `TOOL-cMendedVintage-7` — the second loop over rows carrying
  `evidence: "unattributed"`. This unit builds the file, the roles scoping and the fixture harness
  that unit adds one arm to; it prints nothing about evidence.
- **hands-off** external — promoting any note this leg prints into a failure. Every verdict this unit
  ships is either a hash fact or a missing file.

## 4. Design

### Data model

The receipt is `.governance/install.json`, written by `govkit.py` at `:7827`, `:7862` and `:8342`.
The fields this unit reads, and nothing else:

| field | meaning here |
|---|---|
| `schema` | printed in the summary line so a false red on an old receipt is diagnosable |
| `files[].path` | target-relative path |
| `files[].role` | absent or `"engine"` selects the row; every other value is skipped |
| `files[].sha256` | the hash compared against the file's bytes |

`sha256` is the TARGET's own bytes at receipt-write time, and since `DEPL-dCarriedReceipt-13`'s D9
fold it is stamped from the WORKTREE rather than the index (`govkit.py:8132-8155`). That is the
population this checker reads, so the two agree by construction. A receipt written before that fold
stamped the index blob instead, which diverges from the worktree on any `core.autocrlf=true` clone;
§5 risks carries what that costs and why the summary line names the schema.

### The shape of the run

One file, one language, three steps. The fixture arms run first and unconditionally, then the
receipt is located, then it is graded or the skip is announced. There is no environment-dependent
branch in the fixture half: a leg whose only live behaviour is "no receipt here, nothing to do" is
the could-not-fail shape §7 refuses, and gov's own tree is permanently in exactly that state.

```
python tools/run-gates/check-receipt.py              # fixtures, then the receipt or the announced SKIP
python tools/run-gates/check-receipt.py --selftest   # the fixtures alone
python tools/run-gates/check-receipt.py <dir>        # grade that tree instead of the git root
```

The positional argument exists so a fixture tree is gradeable from a command line without being a
git repository. It is not a `--target` flag and takes no default beyond the derived root: a flag
that can be omitted and a positional that can be omitted are the same affordance, and the shorter
one needs no parser.

### Inventory

Minted by this unit, with the cell that grades each name. `.lexicon.conf` declares `py.function` at
`snake` over a closed verb table, and every name below was put to
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` before it was written.

| identifier | cell | what it is |
|---|---|---|
| `tools/run-gates/check-receipt.py` | — | the shipped file |
| `read_receipt` | `py.function` | parse the receipt, or return nothing when it is absent |
| `check_engine_rows` | `py.function` | the hash and existence loop; returns the findings |
| `check_fixtures` | `py.function` | the four built-in arms |
| `write_fixture` | `py.function` | one fixture tree on disk; added at build time, rev-4 |
| `receipt sync (installed files match the receipt)` | gate-leg name | the leg, in both declarations |

The leg name carries no digit-bearing parenthetical, which `govkit selfcheck`'s 7h arm refuses by
name because the emitter writes leg names into a target where a count nobody maintains is worse
than no name.

### The declarations, and why they are one commit

*Headed "the three declarations" through rev-3. Build-time measurement found a fourth and a fifth, so
the heading no longer states a count — the list below is the population, and the next unit to add a
leg will find it one short again, which is the whole shape of this bug class.*

`govkit selfcheck`'s 7h arm asserts the descriptor set and `tools/gate-legs.json` agree in BOTH
directions: a descriptor row naming a leg the manifest lacks reds, and a manifest leg no descriptor
claims reds. Its 7h2 arm then asserts every manifest leg has a `<name>\t<subject>\t<chunk>` row in
`tools/govkit/subject-pins.tsv`, and a NEW leg with no pin row reds by that fact. So the three files
move together or the bar is red on an incomplete landing. The brief this unit was written from named
two of the three; the pin file is the third and is not optional.

**There is a FOURTH, measured at build time and unnamed by any earlier revision of this section:
the file must be TRACKED.** `selfcheck` resolves every declared leg's argv against the paths the
descriptors actually write, and an untracked file is claimed by no rule — including by this kit's own
`[[files]] include = "**"`, whose pool is the tracked surface. Observed: with the descriptor row, the
manifest row and the file all in the worktree but the file unstaged, `selfcheck` reds with the leg's
argv naming a path that "NO rule in any descriptor writes, seeds, orders or produces", and states the
consequence — `apply` would withhold the leg and exit 1 at every target selecting this kit. So the
`git add` is not bookkeeping ahead of the commit, it is the fourth declaration, and a unit that
writes the other three and stages nothing sees a refusal whose text names neither the manifest nor
the pins.

**And a FIFTH: the leg NAME is an inventory key.** `tools/codebase-map/test_codebase_map.py` reds
with the new name UNCLAIMED until a feature dossier claims it — `memory/map/features/run-gates.md`
here — and the generated map artifacts regenerate in the same commit. §7 below named neither this leg
nor the kickoff-manifest ratchet, which fires too: `tools/gate-legs.json` is a watched file, so the
manifest owes a re-stamped `last-audit` even when no front-loaded claim moved. Both are the named
class `memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`, whose whole point is that the
set is discovered by RUNNING it and is never enumerable from memory — so this list records what fired
here and is not a promise to the next unit that adds a leg.

`subject = "repo"` because a failure of this leg means THIS repository's installed files no longer
match its own record — the criterion stated at the `subject` field declaration in
`tools/run-gates/run-gates.sh` is what a FAILURE means, not what is tested. `chunk = "declarations"`
for the same reading: the leg joins a declared population against the tracked surface, which is what
that chunk already holds. Neither value is held by the runner, so the leg runs on every default bar.

### Rollout

In gov's tree the leg is live from its first bar and always takes the announced-skip path for the
receipt half, because gov does not dogfood govkit and has no `.governance/`. The fixture half is
what gives it a verdict here. At an adopter the leg arrives with the run-gates kit files and reaches
their manifest on their next `apply`.

### Alternatives rejected

A `check-receipt.sh` wrapper, which is how the brief spelled it. The work is a JSON parse and a
sha256, so the shell would need the kit's inlined `resolve_python` block — a new copy for the
`python resolver (behaviour + inline parity + idiom ban)` leg to grade — plus a heredoc'd python
program inside it. And the fallback that spelling exists to buy is not real: `run-gates.sh` resolves
python at line 75 and exits 2 when it cannot, so no leg runs at all in the tree where the wrapper
would have had something to say. The runner rewrites `python` at argv position 0 to the resolved
launcher (`run-gates.sh:1369`) and `tools/process-monitor/kit.toml` already ships a `[[gate_leg]]`
in that form, so the python spelling needs nothing new.

Extending `govkit check` instead: it is the reader that cannot run at an adopter, which is the whole
defect.

A separate `check-receipt.test.sh` beside the script: a second file, a second leg, a second
descriptor row, a second pin row and a second ceiling, for four assertions that fit inside the file
they grade.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/run-gates/check-receipt.py` | new, roughly 60 lines including the fixture arms |
| `tools/run-gates/kit.toml` | one `[[gate_leg]]` block |
| `tools/gate-legs.json` | one row |
| `tools/govkit/subject-pins.tsv` | regenerated |
| `tools/run-gates/README.md` | one line naming the leg and what it does not check |

## 5. Production-readiness checklist

- security — the script reads two files and writes only into a temporary directory it creates for
  the fixture arms. It executes nothing from the receipt and interpolates no receipt value into a
  command.
- perf / scale — one sha256 per engine row. inCMS's receipt carries 95 rows; the declared ceiling of
  300 s is the chunk's standing value and leaves three orders of magnitude of headroom.
- error / empty / loading states — three of them are the design. An absent receipt is the announced
  SKIP (S2), a receipt with no engine rows is the `DEAD PROBE` red (S3), and a receipt that does not
  parse reds naming the parse error rather than being treated as absent.
- observability — one summary line per run naming the schema, the number of rows read and the number
  graded, both DERIVED. Every finding is its own line carrying the path.
- risks — the false-red population is ANY CLONE THAT IS NOT THE INSTALL MACHINE, for any
  receipt-covered path no claimed `[[lf_pin]]` covers. Finding 36 of
  `memory/builds/aSealedCaravan/reviews/2026-08-10-review-TOOL-aSealedCaravan-1-1.md` measured it:
  the receipt hashes WORKING-TREE bytes, so the hash is machine-local. The D9 fold did not remove
  that — it made two readers agree on a population and left the hash clone-dependent — so confining
  the risk to pre-D9 receipts, as this row previously did, named the wrong set. gov's
  `.gitattributes` is `* text=auto` with `eol=lf` pinned on `*.sh`, `gate-legs.json`,
  `*.fragment.json` and a handful of named files, so shipped `.py` and `.md` engine rows re-expand on
  any clone with `core.autocrlf=true`, and this leg is `subject = "repo"` and runs on every such
  clone. Not mitigated in code, and the two mitigations are refused for stated reasons rather than
  omitted: gating on schema makes the leg skip the trees most likely to have drifted, and hashing
  normalized content changes what the leg asserts from "these bytes" to "these bytes modulo an
  assumption". AC7 MEASURES the residue instead of asserting it away. Second risk: the leg is new on
  adopters' bars and any pre-existing drift surfaces as a red on their next pull. That is the leg
  working.
- testing — the four fixture arms (S4) are the permanent coverage and run on every invocation. AC3
  and AC4 observe the failing cases before the unit closes, which is §7's rule that a gate is not
  landed until its failing case has been seen.
- migration — none. No existing file's format changes and nothing reads a new field.
- user docs — one line in `tools/run-gates/README.md` naming the leg, and the script's own header
  stating what it does NOT check: no descriptor half, no provenance half, no seed row, no merged
  block.

## 6. Acceptance criteria

The new file is named here without backticks. `tools/check-spec-tokens.py` grades every backticked
path-shaped word in this section against `git ls-files`, and a unit's own deliverable is untracked
until it lands, so backticking it would red the `spec tokens (a spec's own names resolve)` leg for
the whole life of the spec. Each criterion carries a witness that exists.

- **AC1** — When check-receipt.py runs in this repo, which holds no `install.json` under
  `.governance/`, the output carries a line whose head is `SKIP` naming the path it looked for, and
  the exit status is 0.
  Red when: the absent receipt is treated as a clean target, so the run prints nothing about it and
  a target that lost its receipt is indistinguishable from one that verified.
- **AC2** — When check-receipt.py runs with `--selftest`, it prints one line per fixture arm and
  exits 0, and its output names four arms.
  Red when: the fixture half is absent or silent, leaving a leg whose only behaviour in gov's tree
  is a skip and therefore no reachable failing case.
  figure: DERIVED — the arm count is printed by the run, not asserted from this document.
- **AC3** — When a fixture tree is built under the run's own scratchpad whose `install.json` carries
  one engine row with its `sha256` altered by one character, and check-receipt.py is given that
  tree as its positional argument, it exits non-zero and its output names that row's `path`.
  Red when: the loop compares the row against itself, or skips rows whose `role` key is absent, so a
  drifted engine file passes.
  fixture: the tree does not exist today and the arm creates it; the same case is the second built-in
  fixture arm, so the observation is permanent after this unit as well as staged for it.
- **AC4** — When the same fixture tree has that engine row's file deleted, the run exits non-zero
  and its output names the `path` as missing rather than as a hash mismatch.
  Red when: the missing file is read as empty bytes and reported as drift, which names the wrong
  remedy.
- **AC5** — When a fixture `install.json` carries only `seed` and `merged` rows, the run exits
  non-zero and its output carries `DEAD PROBE`.
  Red when: zero graded rows reports as a clean target, which is the reading a broken receipt and a
  healthy one both produce.
- **AC6** — When `python tools/govkit/govkit.py selfcheck` runs after all three declarations move, it
  exits 0; when the `tools/gate-legs.json` row alone is present it names the leg as claimed by no
  descriptor, and when `tools/govkit/subject-pins.tsv` alone is stale it names the leg as having no
  pin row.
  Red when: only two of the three declarations move, which is the state the brief's own edit list
  would have produced.
- **AC7** — When the fixture tree from AC3 is re-cloned under the run's scratchpad with
  `core.autocrlf=true` and check-receipt.py is given that clone as its positional argument, the
  reported finding count is recorded in the run's output, and whatever that count is, the run's own
  summary line names the schema so the reading is available at the point of failure.
  Red when: the residue is asserted rather than measured, which is how §5's risk row came to name a
  population — pre-D9 receipts — that the fold had already stopped being the right one.
  figure: DERIVED — the finding count comes from the run, and this criterion deliberately pins no
  expected value, because the number is what the observation exists to establish.
  fixture: a second clone of the AC3 fixture with a different `core.autocrlf`; it does not exist
  today and the arm creates it.

## 7. Gates

`govkit selfcheck` · `leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `install-prefix (shipped surface)` · `line length` · `run-gates gov canary` · `dead-path carriers (deleted files still named)`

New arm: `tools/run-gates/check-receipt.py` · four built-in fixture receipts written to a temporary
directory, staged by `--selftest` and by every bare invocation · no assertion floor to move, because
this file is not in the population `tools/check-testsuite-counts.sh` reads.

## 8. Open questions

- **F1 — the shipped file's extension.** The brief spells the deliverable `check-receipt.sh` and the
build README's roster row 21 repeats that spelling. The work is a JSON parse and a sha256, so a
shell spelling needs a new inlined copy of `resolve_python` plus an embedded python program, and it
buys no fallback: the runner itself refuses to start without python. RESOLVED (agent, 2026-09-16,
delegated): `check-receipt.py`, on M3's rule — the option satisfying more acceptance criteria with
fewer follow-ups, past all three vetoes, since it adds no dependency, no install location and no
public surface, and reuses the runner's existing argv-0 resolution rather than a second mechanism.
The build README's roster row still says `.sh` and the build's closing README re-read owns fixing
that line; this spec is the record of why the two differ.

- **F2 — the chunk.** `wiring` groups the adopter `--check` legs and `declarations` groups the legs
that join a declared population against the tracked surface. RESOLVED (agent, 2026-09-16,
delegated): `declarations`. The receipt is a declaration and this leg is the join; `wiring` answers
whether a kit is installed, which this leg does not ask. The value is pinned in
`tools/govkit/subject-pins.tsv`, so a later move appears in a diff rather than silently taking the
leg off a bar.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · S1 · §5 · AC7 · folded spec-audit round 1 finding M3: §5 confined the
  false-red class to pre-D9 receipts, which is the wrong population — the receipt hashes worktree
  bytes, so every clone that is not the install machine is at risk. The row now names that population
  and cites finding 36 of the aSealedCaravan record, and AC7 measures the residue on a CRLF-expanded
  clone rather than asserting it away.
- rev-4 · 2026-09-17 · §4 · built and closed. THREE amendments, all from measurement at build time
  and none changing a design decision. Amended again the same day after the post-commit bug-class
  checklist: the subsection gains a FIFTH declaration (the leg name is a codebase-map inventory key,
  claimed in the run-gates dossier) plus the kickoff-manifest ratchet, and its heading no longer
  states a count, because a heading that counts a population this bug class grows is the other half
  an amendment leaves standing. (a) The three-declarations subsection gains a FOURTH, observed
  rather than predicted: `selfcheck` reds on a leg whose argv names an UNTRACKED path, because the
  `**` engine rule's pool is the tracked surface, so staging the file is itself a declaration. Every
  earlier revision, and the brief, named three. (b) The Inventory table gains `write_fixture`, a
  fixture-tree helper the four arms share; `--suggest` cleared it for `py.function` before it was
  written, as the table's own sentence requires. (c) §5's false-red row is CONFIRMED and, if
  anything, understated: AC7's clone was built with `core.autocrlf=false` and STILL came back
  CRLF, because `* text=auto` plus a native `core.eol` normalizes on checkout regardless — so the
  population really is every clone that is not the install machine, and not merely the ones that opt
  into `autocrlf`. No wording changed, because the row already names that population. One stale
  citation noted and not repaired here: §10 cites the integrity loop at `govkit.py:3074-3092` and it
  now sits near `:3511`; the file it names is right and the line numbers move with every commit,
  which is why the reuse audit is evidence of a reading rather than a live pointer.
- rev-3 · 2026-09-16 · §8 · SHAPE REPAIR, no decision changed. The fork items were written as bare `**F1 — …**` bold paragraphs; the classifier at `tools/unattended/unattended.sh:1797` counts an item only when the line opens `- `, `* ` or `### `, and with zero items it takes a branch that never consults the resolution mark and accepts only a `none` opening line. So a section carrying a conforming `RESOLVED (agent, …)` mark graded FORKED and the unit could not be dispatched. Ten sibling specs in this build use the `- ` bullet and all grade READY, so the house shape is the bullet and these two were the outliers. The reader errs toward FORKED, which is the safe direction, so this is a defect in the spec and not in the classifier. The resolution text, the chosen option and every criterion are byte-identical; the round-1 spec audit that reviewed this design still names this id and is not invalidated by a non-semantic reshape.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "verify installed files against the receipt hashes
recorded at adoption"` returned `map_from_receipt` and `hash_file`, both in `tools/govkit/census.py`,
as the closest existing readers of `.governance/install.json`. Neither is reusable here and the
reason is the unit's whole point: `tools/govkit/` is not a kit, ships to no target, and
`map_from_receipt` reads `source`, `oid` and `kit` for a provenance question rather than `sha256` for
an integrity one. The probe also reported `.sh` as an unscanned layer, so the shell side of the
run-gates kit is invisible to the map by construction. The seam this unit DOES extend is the
run-gates kit itself, by path: `tools/run-gates/kit.toml`'s `[[files]] include = "**"` engine rule
carries the new file, and `tools/run-gates/adopt-run-gates.sh:44-55` is the derivation pattern the
new file copies for its root resolution. Verified against source at writing time rather than taken
from the map: `govkit.py:3074-3092` is the integrity loop this checker mirrors, and `:8132-8155`
records that `sha256` is stamped from the worktree.

Recall terms used: `--terms "govkit receipt install.json install.sums engine row sha256 integrity
cmd_check adopter gate leg run-gates unattributed evidence"`, with the question "why does an adopter
have no way to detect that a govkit-installed file drifted from its receipt, and what gate leg could
report it". It returned `memory/builds/aTetheredConvoy/reviews/2026-08-16-review-DEPL-aTetheredConvoy-1-3.md`,
which records that `cmd_check` quantifies receipt to disk and never disk to receipt, and
`memory/builds/dCarriedReceipt/reviews/2026-08-26-review-DEPL-dCarriedReceipt-13-diff-review-round1.md`,
which is where the index-versus-worktree question for `sha256` was first asked.

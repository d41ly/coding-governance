# TOOL-dTieredTribunal-11 — the subject descriptor — one engine drives a spec audit too

**Status:** SPECCED · rev-5 · 2026-08-26 · node a · Tier-2 · base cd971285 · order 4 · streams tooling · ratified 2026-08-26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md) | spec-audit | TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` carries the trust accounting a review needs and can only be
pointed at a diff. This unit gives it one `args` field naming the review KIND, and makes six
things per-kind: the acquire sentence handed to the finder lenses, the lens catalogue, the
`context` default, the anchor predicate, the finding schema's address field, and the
`**Serves:**` kind token the synthesis prompt instructs. Same file, same name, same exit paths,
same counters. It is authorized by `TOOL-dTieredTribunal-7`, which grants P1 together with its M4
amendment, and it is this build's headline goal — the one the first run could not deliver because
the amendment was the owner's to grant.

The value is measured rather than asserted. A field a program emits reaches a review record 77–88%
of the time and a field a document asks a human to remember reaches it 5–27% of the time, and the
majority review kind in this corpus is the one the engine is currently forbidden to drive.

## 2. Scope (IN)

- **S1** — `args` gains `kind`, a string. It defaults to `diff-review`, so every caller in the tree
  today is unchanged, including the invocation block spelled at
  `memory/guides/BUILD-METHOD.md:222-227`, which passes no such field. Two values are legal,
  `diff-review` and `spec-audit`. Any other value is a thrown refusal naming what it got, in the
  shape the `repo` guard at `tools/workflows/tier2-review.js:53-60` already uses. A silent fallback
  to the diff kind would make a typo'd kind produce a confident review of the wrong shape, which is
  the defect class that guard exists for.
- **S2** — the lens catalogue at `tools/workflows/tier2-review.js:156-177` becomes two sibling
  top-level array literals and one selector line. `DIFF_LENSES` holds the four briefs that ship
  today, byte-unchanged. `SPEC_LENSES` holds the four M4 briefs COPIED from
  `tools/memory-tree/README.md:210-214`, not re-invented. The selector is a single marked ternary
  and its exact shape is fixed by §4, because the hook that grades it accepts one dialect.
- **S3** — the finding schema becomes two sibling schemas. `FINDING_SCHEMA` keeps its present shape
  at `:105-126`, requiring an integer `line`. `SPEC_FINDING_SCHEMA` requires a string `where` in
  `line`'s place, because an underspecification finding IS the absence of a line and a spec has no
  line worth citing. The address obligation stays machine-enforced on BOTH kinds. Making `line`
  merely optional on one shared schema would buy the spec kind an address by removing the diff
  kind's, and the charter requires a finder to emit a concrete address.
- **S4** — the display `ref` built at `:210` becomes kind-aware, so a spec finding reads its path
  followed by a section address rather than its path followed by `:undefined`. `ref` remains
  DISPLAY ONLY. The join key stays the orchestrator-assigned integer at `:211`, and this unit
  changes nothing about the join.
- **S5** — the anchor predicate at `:85-95` dispatches per kind. For `diff-review` it is unchanged.
  For `spec-audit` the anchor is a new `args` field, `subjects`, a non-empty array whose every
  entry carries a repo-relative `path` and a `blob`, and the blob is graded by the SAME
  `/^[0-9a-f]{7,40}$/` test the diff kind applies to `base`. One predicate, two populations. The
  refusal ladder is unchanged: refuse above round 1, warn at round 1.
- **S6** — the acquire sentence at `:182` becomes per-kind. The diff kind keeps its instruction to
  run `diffCmd`. The spec kind instructs the lens to run `git hash-object` on each subject path,
  compare the result against the pinned blob, report a mismatch as a blocker finding, and only then
  Read the file whole. The lens holds tools and a filesystem; the orchestrator holds neither. That
  comparison is what makes S5 a check that can FAIL rather than a string test any caller satisfies.
- **S7** — the `context` default at `:68` becomes per-kind. The diff kind keeps `the cumulative
  diff landing on main`. The spec kind gets a default naming the spec set as the subject. Neither
  default is load-bearing when a caller supplies `context`, and both are wrong if a kind inherits
  the other's.
- **S8** — the `**Serves:** diff-review` token hardcoded into the synthesis prompt at `:375`
  becomes the value of `kind`. Because S1 closes the legal set to two, and both are members of the
  closed record-kind vocabulary at `memory/HYGIENE.md:275-276`, the emitted token cannot leave that
  vocabulary without S1's refusal firing first.
- **S9** — the remaining diff-shaped prompt strings become per-kind. They are enumerated in §4's
  Inventory table, which is the authoritative list for this unit, and they are the round sentence
  at `:184`, the round-1 no-prior-findings sentence at `:192`, which reads `the whole diff` and must read the
  subject the kind names, the out-of-diff clause at `:194`, the finder's return-shape line at
  `:195`, the
  skeptic's read instruction at `:245`, the report instruction at `:345`, the range line at `:353`,
  the binding line's id clause at `:376`, and the pre-spawn log at `:103`.
- **S10** — no exit path is added, and no field is removed from any of the four returns. The exit
  paths are the all-lenses-dead return at `:215-219`, the nothing-raised return at `:227`, the
  everything-refuted return at `:315-324`, and the success return at `:419-458`, which is also the
  synthesis-death path. The prior-art price on a generalised engine is that its counters survive,
  and this unit meets it by not touching them.
- **S11** — `meta.version` moves from `1.3` to `1.4` at `:3`, and the same-line `gov:kit
  tier2-review@1.3` marker moves with it. `tools/workflows/kit.toml:6` derives the review-harness
  kit version from that field, and this unit changes the harness's `args` contract. In the same
  header edit, `:154`'s claim of a six-wide find wave is corrected to the width the code actually
  fans at, which closes `TOOL-aDeclaredBound-6` (`memory/backlog/TOOL.md:148`). That row's own
  citation is stale — it names line 128 and the text lives at `:154` — so the row is corrected as
  it is closed. A third live carrier is `tools/check-agent-cap-restatement.sh:34-36`, a merge-bar
  gate whose executable-files-are-out-of-scope bullet quotes that same sentence as a live example
  and records the row as filed; it is rewritten as a past observation closed by this unit. The
  bullet keeps its point and its widening argument, which rest on the remedy-string carrier named
  beneath the example rather than on the example. `memory/builds/dTieredTribunal/README.md:58`,
  which calls the row OPEN and untouched here, is amended in the same commit.
- **S12** — `memory/map/features/review-harnesses.md` is refreshed in the same commit. Its bullet
  at `:84`, which asserts that no harness takes a review-kind parameter, is falsified by this unit,
  and the dossier claims `tier2-review.js` at `:22`, so the refresh is this unit's rather than a
  sibling's. No inventory key is created or retired, so no claim edit and no regenerated artifact
  is owed.
- **S13** — a provenance comment naming this unit id sits on each edited site, matching the file's
  existing convention of citing the unit that earned a guard. The sites are the ones §4's Inventory
  table enumerates.

## 3. Non-goals (OUT)

- **Editing `memory/guides/BUILD-METHOD.md` or its template.** The M4 amendment is
  `TOOL-dTieredTribunal-12`, which runs at order 5 precisely so it describes what this unit shipped
  rather than what it promised. Two carriers hold that rule and both are that unit's.
- **Renaming the file.** Refused on record, on the ground that `AGENTS.md:557`, `README.md:89` and
  `WIRE-INTO-PROJECT.md` all name it. All three still do.
- **Editing `tools/hooks/agent-cap.js`.** That file is `TOOL-dTieredTribunal-13`, at order 2. This
  unit is a CONSUMER of the predicate that unit ships, and §8 carries the one fork where they meet.
- **A round axis or a reviewed-rev axis on the record.** That is P10 in the research record and is
  not in this build. The `blob` this unit pins is an input to the run, not a field on the record.
- **A lens declaration file, a convergence-loop driver, or folding the two drift-audit siblings
  in.** Those are P3, P4 and P7. Each is separately viable and none is authorized here.
- **A new gate leg.** All three shipped scanners already select this file.
  `tools/workflows/check-review-join.sh:43` takes every tracked `tools/**/*.js` with no marker
  filter. `tools/workflows/check-verifier-fanout.sh:49` and
  `tools/workflows/check-workflow-syntax.js:30` select on the `export const meta =` marker, which
  this file carries at `:1` and must keep. No new registration in `tools/gate-legs.json` or
  `tools/workflows/kit.toml` is owed.
- **Blurring the closing-review discrimination.** `tools/unattended/unattended.sh:2934` reads the
  binding line and requires a `diff-review` naming a commit in range, because a spec audit once
  satisfied an item named `closing-review-recorded`. An engine that can emit both tokens makes that
  discrimination stronger rather than weaker, and this unit adds nothing that lets a spec audit
  stand in.

## 4. Design

### Data model

`args` gains two fields and keeps every existing one.

| field | kind | required | shape |
|---|---|---|---|
| `kind` | both | no, defaults to `diff-review` | `diff-review` or `spec-audit`, else throws |
| `base` | `diff-review` | yes above round 1 | 7–40 hex, unchanged |
| `subjects` | `spec-audit` | yes above round 1 | non-empty array of path and blob pairs |

The anchor rule is one sentence with two populations: the field that pins what was reviewed must be
a content hash, and a caller who hands over a moving ref is refused above round 1 and warned at
round 1.

**Why the blob and not the spec's own header base.** A spec's status header carries a `base`, it is
7–40 hex, and it would satisfy any string test the orchestrator can run. It is also identical
across every revision of that spec, so it cannot distinguish rev-3 from rev-7 and would pass
forever on a spec nobody re-read. That is a check that cannot fail. A blob sha changes with every
fold, which is the property the check needs. And because a commit sha and a blob sha are both 40
hex, the orchestrator cannot tell a substituted one apart — which is why S6 puts the comparison in
the LENS, the only actor in this pipeline that can run `git hash-object` and read the file.

`git hash-object` is deliberate in place of `git rev-parse HEAD:<path>`. It hashes the working
tree, so it is defined for an uncommitted spec, which is the common case for a spec audit. Verified
on this tree: both spellings return `15bc14c7898b8b43829bfa70ac985f7ec2701710` for this build's
first spec, and only `git hash-object` survives that file being edited and not committed.

### The lens catalogue, and the one dialect that is allowed

`tools/hooks/agent-cap.js` reads the inline script at the `Workflow` tool call and denies an
`agent(` fanned over a receiver it cannot prove bounded. A map, object or registry of lens sets is
denied. What this unit ships is two sibling top-level array literals and one marked selector:

```js
const DIFF_LENSES = [ /* the four briefs shipped at :156-177, unchanged */ ]
const SPEC_LENSES = [ /* the four M4 briefs from tools/memory-tree/README.md:210-214 */ ]
const LENSES = kind === 'spec-audit' ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers
```

Each literal is under the hook's lens allowance, so each enters the bounded set on its own. The
marked ternary then inherits the bound, because a ternary between two bounded sources cannot grow
either of them. Measured rather than assumed: a fixture carrying exactly this shape, fed to
`tools/hooks/agent-cap.js` as a synthetic `Workflow` payload, returns rc=0.

The four spec briefs are COPIED from `tools/memory-tree/README.md:210-214` rather than written
fresh. That file is the M4 catalogue's home and the source is prose, so this unit creates a second
carrier of four sentences. The class is `TOOL-dUnstalledConvoy-16` and this unit does not close it:
closing it is P3, which makes the catalogue declared data with a parity leg. §7 records the gap as
standing rather than implying it away.

### The finding schema

| | `diff-review` | `spec-audit` |
|---|---|---|
| required | `file` `line` `severity` `claim` `impact` `fix` | `file` `where` `severity` `claim` `impact` `fix` |
| address type | integer | string, section-shaped |
| display `ref` | path and line | path and section |

Severity keeps the same four-token enum on both kinds, so the synthesis prompt's blocker and high
counts — the fields `TOOL-dTieredTribunal-1` made required and returned — mean the same thing
whatever the kind. That is what lets the returned blocker count reach the M4 convergence loop,
which is the loop the first run's unit could not reach.

### Inventory — every per-kind site, and every site deliberately left alone

| site | today | after |
|---|---|---|
| `:3` | `version: '1.3'` plus the same-line `gov:kit` marker | `1.4` on both tokens |
| `:5` | the description names no review kind | names the kind parameter |
| `:27-31` | the `args` doc comment | gains `kind` and `subjects` |
| `:68` | the `context` default | per-kind default |
| `:85-95` | base-must-be-a-sha | dispatches per kind, per the Data model above |
| `:103` | the pre-spawn log names the diff | names the diff or the subject set |
| `:105-126` | one finding schema | two sibling schemas |
| `:154` | the comment claims a six-wide find wave | corrected, closing `TOOL-aDeclaredBound-6` |
| `:156-177` | one lens catalogue | two sibling literals plus a marked selector |
| `:182` | the acquire sentence | per-kind, with S6's blob verification on the spec arm |
| `:184` | the round sentence names the diff | per-kind |
| `:192` | the round-1 no-prior-findings sentence names the whole diff | per-kind |
| `:194` | the address field list and the out-of-diff clause | per-kind on both halves |
| `:195` | the return-shape line names `file,line` | per-kind field list, matching the schema selected for the same kind |
| `:210` | `ref` is path and line | per-kind |
| `:245` | skeptics read the cited file, line and callers | per-kind |
| `:345` | the report instruction names a file and line | per-kind |
| `:353` | the range line | per-kind, naming the subject set and its blobs on the spec arm |
| `:375` | `**Serves:** diff-review` | the value of `kind` |
| `:376` | the id clause names every unit id in the diff | per-kind, naming the audited unit set on the spec arm |

Untouched on purpose: the `args` parse-and-validate guard at `:32-60`, the `priorFindings` split at
`:70-76`, the round inference at `:79`, the integer verdict join at `:265-285`, the batching line
at `:239`, every counter, every `note` arm, and all four returns.

`meta.phases` at `:6-10` stays STATIC. Whether the Workflow runtime reads `meta` before evaluating
the body is unestablished, so a phase list built from `args` would be an unmeasured claim. Both
catalogues carry four lenses, so the existing wording stays true for both kinds. If a later unit
gives one kind a different count, that wording is what has to move.

### Migration

`kind` defaults to `diff-review`, `subjects` is read only on the spec arm, and no return field
changes. So every existing caller keeps its exact behaviour, and the M8 invocation block at
`memory/guides/BUILD-METHOD.md:222-227` needs no edit — which is worth stating, because that file
is `TOOL-dTieredTribunal-12`'s and its byte budget is nearly spent.

### Rollout

Order 4 of this build. `TOOL-dTieredTribunal-13` lands first and its predicate must admit the
selector above; §8 carries that fork with a measured fallback. `TOOL-dTieredTribunal-12` lands
after, and until it does, `memory/guides/BUILD-METHOD.md:116` still forbids on a spec what the
engine can now do. That window is real and deliberate: the amendment describes shipped behaviour
instead of promised behaviour.

### Files touched (estimate)

`tools/workflows/tier2-review.js`, `memory/map/features/review-harnesses.md`, and
`tools/check-agent-cap-restatement.sh`, whose header example S11 re-points. The bookkeeping edits
are the backlog row closed by S11 under `memory/backlog/TOOL.md` and the Parked-decisions bullet at
`memory/builds/dTieredTribunal/README.md:58`.

### Alternatives rejected

- **One schema with `line` optional and `where` added.** Rejected. It buys the spec kind an address
  by removing the diff kind's machine-enforced one, and a finder that omits both leaves a skeptic
  nothing to verify.
- **A kind-to-lens-set registry.** Rejected because it does not run. A map or object of lens sets
  is denied at the tool call by `tools/hooks/agent-cap.js`, so this is a runtime constraint rather
  than a taste.
- **A second engine file, spec-shaped.** Rejected on record. It is instance #4 of a pipeline whose
  instances #2 and #3 already lost every hardening instance #1 learned, with the bar green over the
  loss.
- **Naming the spec anchor from the spec's own header base.** Rejected under the Data model above:
  it passes on every spec forever.
- **Making the harness itself verify the blob.** Rejected because it cannot. The script has no
  filesystem, stated three times in its own source at `:81`, `:98-100` and `:347`.

## 5. Production-readiness checklist

- security — no new write path and no new outbound request. The one new input, `subjects`, is
  interpolated into prompts, and it is refused unless every blob matches a hex predicate. The
  `path` half is NOT validated beyond being a string, which is stated rather than hidden: the
  harness cannot resolve a path, and the lens that reads it runs against the caller's own repo.
- perf / scale — the agent count is unchanged. Both catalogues carry four lenses, the verifier
  count is the same constant, and prompt growth is per-kind text that replaces existing text rather
  than adding to it.
- a11y — N/A. A workflow script has no user interface.
- i18n — N/A. Same reason.
- error / empty / loading states — an empty `subjects` on the spec arm is a refusal above round 1
  and a warning at round 1, matching the diff arm exactly. An unrecognised `kind` is a refusal at
  parse time, before any agent spawns.
- observability — this unit is what makes a spec audit's shape program-emitted. The kind token, the
  review-shape line and the subject anchor reach a spec-audit record by the same path they already
  reach a diff-review one. The liveness counters do NOT: they reach the CALLER on every exit path,
  which S10 preserves, and the synthesis prompt at `:346` interpolates finding counts only.
  `TOOL-dTieredTribunal-15`'s record is that disclosure.
- risks — one, and it is a cross-unit risk rather than a runtime one. This unit's selector sits on
  the branch of `tools/hooks/agent-cap.js` that `TOOL-dTieredTribunal-13` tightens, and a naive
  tightening denies it. It is measured in §8 rather than described, and the fallback is measured
  too.
- testing + left-shift gates — the three shipped scanners over this file stay green, and
  `check-verifier-fanout.sh` is the observation that the fan-out still passes the hook, because
  that gate delegates to the hook rather than re-implementing it. No new leg, per §3.
- migration / rollback — revert the files section 4 names. Nothing persists between runs and no artifact is
  generated.
- user docs — none. The harness is agent-facing. Its own header comment and the dossier refreshed
  by S12 are its documentation.

## 6. Acceptance criteria

- **AC1** — When `tools/workflows/tier2-review.js` is read, `kind` is sourced from `args` with a
  `diff-review` default, and a third value throws. Observation: a synthetic invocation carrying a
  `kind` of `audit` refuses with a message naming the value it got, and `grep -n "spec-audit"
  tools/workflows/tier2-review.js` returns hits where that grep exits 1 today.
- **AC2** — When the lens region is read, two sibling top-level array literals exist and one marked
  selector line assigns from them. Observation: `bash tools/workflows/check-verifier-fanout.sh`
  exits zero over the edited file, which is the hook's own verdict rather than a re-implementation
  of it.
- **AC3** — When the four spec briefs are compared against `tools/memory-tree/README.md:210-214`,
  each brief's content is the one that file states, and none names a lens the M4 catalogue does not
  hold.
- **AC4** — When the schema region is read, two schemas exist, the diff one requires `line` and the
  spec one requires `where`, and neither requires both. Observation: `grep -n "where"
  tools/workflows/tier2-review.js` returns a hit inside a `required` array and a hit inside a
  `properties` object. EVERY finder-prompt line naming the address field names the SAME field as the
  schema passed on that arm, not just the return-shape line: the unspaced list at `:195` and the
  spaced list inside `:194`'s emit sentence. Observation: `grep -c "file,line,severity"`, `grep -c
  "file,where,severity"`, `grep -c "file, line, severity"` and `grep -c "file, where, severity"` each
  return 1, where the two `where` counts are 0 today and the two `line` counts are already 1, and each
  arm spelling `where` is the arm passing `SPEC_FINDING_SCHEMA`.
- **AC5** — When the anchor block is read, the spec arm grades `subjects`, refuses an empty array,
  and applies the SAME hex expression the diff arm applies to `base`. Observation: `grep -c
  "0-9a-f]{7,40}" tools/workflows/tier2-review.js` shows the pattern spelled once rather than
  twice, so the two arms cannot drift apart.
- **AC6** — When the finder acquire sentence is read on the spec arm, it instructs the lens to run
  `git hash-object` per subject and to report a mismatch against the pinned blob as a finding,
  before it instructs the lens to `Read` anything.
- **AC7** — When the synthesis prompt is read, the binding-line instruction interpolates `kind`
  rather than spelling one token. Observation: `grep -n "Serves:\*\* diff-review"
  tools/workflows/tier2-review.js` returns no match, where it returns line 375 today.
- **AC8** — When each of the four returns is read, its field set is unchanged from the file at base
  `cd971285`. Observation: `git diff cd971285 -- tools/workflows/tier2-review.js` shows no line
  removed from inside a return block.
- **AC9** — When `grep -n 'dTieredTribunal-11' tools/workflows/tier2-review.js` runs, it returns a
  hit at each site §4's Inventory table lists as changed, and at no site the table lists as
  untouched.
- **AC10** — When `bash tools/check-kit-versions.sh` runs it exits zero, and `grep -n
  "tier2-review@1.4" tools/workflows/tier2-review.js` returns the single line 3 that also carries
  `version: '1.4'`. The leg is named because it runs and not because it grades the pair: its row
  for this file is a bare presence check, which is the open question at `TOOL-dTieredTribunal-6`,
  so this grep is the whole observation of the bump.
- **AC11** — When `git grep -n -- "6-wide"` runs over the whole tree, no hit is under `tools/` —
  today it returns `tools/workflows/tier2-review.js:154` and `tools/check-agent-cap-restatement.sh:35`
  — and every surviving hit outside `memory/builds/` and `memory/archive/` is the
  `TOOL-aDeclaredBound-6` row in `memory/backlog/TOOL.md`, which reads CLOSED with its stale line
  citation corrected. S11's fifth edit target gets its own observation, because that grep cannot see
  it: `grep -n 'TOOL-aDeclaredBound-6' memory/builds/dTieredTribunal/README.md` returns a
  Parked-decisions bullet naming the row as closed by `TOOL-dTieredTribunal-11`, where today it
  returns line 58 reading the row OPEN and untouched.
- **AC12** — When `memory/map/features/review-harnesses.md` is read, the bullet asserting that no
  harness takes a review-kind parameter is gone rather than negated beside its replacement.
  Observation: `grep -n "review-KIND parameter" memory/map/features/review-harnesses.md` returns no
  match, and the `codebase-map coverage + freshness` leg stays green.
- **AC13** — When `node tools/workflows/check-workflow-syntax.js` and `bash
  tools/workflows/check-review-join.sh` run over the tree, both exit zero.
- **AC14** — When the engine is run once for real against this build's own spec set with a `kind`
  of `spec-audit`, the record it writes opens with a `**Serves:**` line carrying that kind followed
  by unit ids, and `python tools/memory-tree/gen_build_index.py --check` classifies the record
  under that kind. This is the criterion that proves the unit rather than the diff: a kind token
  nothing ever emitted is a parameter, not a capability.
- **AC15** — S7's witness. When the harness is invoked with a `kind` of `spec-audit` and no
  `context`, the default it interpolates names the spec set and carries no `diff`. Observation:
  `grep -n "the cumulative diff landing on main" tools/workflows/tier2-review.js` returns a hit only
  on the diff arm of the per-kind expression at `:68`, where today that string is unconditional.
- **AC16** — S4's witness. When the display `ref` at `:210` is built for a spec-kind finding, it
  ends with that finding's own `where` value and contains no `:undefined`. Observation: a synthetic
  spec-kind finding carrying a `where` of `§2 S4` renders a `ref` whose tail is that string, where
  the shipped `${f.file}:${f.line}` renders `:undefined`.
- **AC17** — S9's witness. When `grep -nE 'diff|file:line|file, ?line, ?severity|\$\{base\}\.\.\.\$\{head\}'
  tools/workflows/tier2-review.js` runs, every hit inside a prompt string or inside the pre-spawn log
  string sits on a kind selection, on `diffCmd`, or on the `diff-review` kind token itself. Hits
  inside comments are outside the population. The alternation is wider than `diff` alone because
  FOUR S9 sites carry no `diff` token at all: `:245` and `:345` carry `file:line`, `:353` carries
  only the literal `${base}...${head}`, and `:195`'s return-shape list carries neither, so it is
  reached by the `file, ?line, ?severity` alternate alone. `:194`'s address list is reached by that
  same alternate. Verified per site with `sed -n '<n>p' … | grep -q diff` over all nine. Ran at HEAD, the widened grep
  returns every one of S9's nine sites. It reds there on at least two of them: the range line at
  `:353` spells `${base}...${head}` with no kind selection, and the pre-spawn log at `:103` names the
  diff unconditionally.

## 7. Gates

The named legs this unit must keep green are `workflow script syntax`, `review-join ban (no
ref-keyed join)`, `verifier fan-out`, `agent-cap restatement`, `kit version markers`, `codebase-map
coverage + freshness`, `memory hygiene`, `review-protocol parity (kit vs dogfood)`, `review-join
self-test`, `verifier fan-out self-test` and `agent-cap restatement self-test`.

No count of them is written here. `tools/gate-legs.json` owns the population, and a number typed
beside a manifest is wrong on the next commit.

`verifier fan-out` is the load-bearing one and deserves its own sentence. It does not implement the
cap rule; it feeds each workflow script to `tools/hooks/agent-cap.js` and reports what the hook
says. So it is simultaneously the gate this unit must pass and the instrument that answers §8's
fork, which is why AC2 names it instead of naming a grep over the selector line.

The named legs carrying `subject: kit` are `verifier fan-out self-test`, `review-join self-test` and
`agent-cap restatement self-test`, and all three are HELD by `tools/run-gates/run-gates.sh` unless
`GATE_SELFTESTS=1` is set. Their guards are not written here: `TOOL-dTieredTribunal-14` S12 moves two
of the three one order before this unit lands, so any guard sentence in this section is a claim about
a manifest this build is mid-way through editing. Read `tools/gate-legs.json`. What survives is the
part that does not move — a guarded leg arming is not the same as a leg running, so this unit's
Definition of Done needs the run that sets both that variable and `GATE_FULL=1`.

This unit adds no gate leg, per §3.

One gap is left OPEN rather than closed. S2 makes this file a SECOND carrier of the four M4 lens
briefs, whose first carrier is `tools/memory-tree/README.md:210-214`, and nothing joins the two.
That is the multi-carrier class tracked as `TOOL-dUnstalledConvoy-16`. Its fix is P3's declaration
plus a parity leg, which is a mechanism and not spec text, and folding a mechanism into this unit
would smuggle it past the round meant to price it. Any later report claiming this closed without a
parity pair is itself the defect.

## 8. Open questions

- **F1 — does `TOOL-dTieredTribunal-13`'s tightened predicate admit this unit's selector?**

The two units meet on one line. `TOOL-dTieredTribunal-13` tightens the marked-derivation branch of
`tools/hooks/agent-cap.js` to require every non-self reference bounded rather than merely one, and
this unit's `LENSES` line is a marked derivation whose condition is a scalar.

Measured rather than feared, at base `cd971285`. A fixture carrying this unit's exact selector
shape passes the hook at HEAD, rc=0. A copy of the hook with that branch's `refs.some` test
rewritten to the naive `refs.every` form denies the same fixture with rc=2 — and denies
`tools/workflows/drift-audit-state.js:224` too, which is the ONE shipped user of that branch and
which the sibling unit is required to keep passing. So the naive tightening is already ruled out by
the sibling's own constraint, and the question is only whether the shape it does ship treats a
scalar ternary condition as a reference it must bound.

**The fallback, also measured.** A shape that never uses the derivation branch at all passes both
the hook at HEAD and the naive-strict copy, rc=0 on each: keep the two sibling literals, drop the
`LENSES` assignment, hoist the finder prompt into a one-argument builder, and fan out at two call
sites selected by a ternary, each `.map` receiver being a bounded array literal directly. It costs
about six duplicated lines and removes the cross-unit dependency entirely.

**Recommendation: keep the marked ternary.** It is one line, it keeps one fan-out site, and it is
the dialect the hook's own comments describe as the sanctioned derivation. AC2 is the observation
that settles this once order 1 lands, and the fallback above is what this unit takes if it does not
— a build decision at that point, not a redesign.


**RESOLVED (agent, 2026-08-26, delegated): keep the marked ternary; the sibling unit binds its
admission.** This is a FACT-QUESTION and the probe already ran during spec authoring: the naive
tightening, `refs.some` rewritten to `refs.every`, denies BOTH this selector and
`tools/workflows/drift-audit-state.js`, which the owner's ruling at `TOOL-dTieredTribunal-8` says
must keep passing. So the naive form is refused by the sibling unit's own constraint rather than by
preference. `TOOL-dTieredTribunal-13` is order 2 and lands first, and its AC6 pins this exact
selector while its AC6b pins the shipped user, so the admission is an acceptance criterion of that
unit rather than an assumption of this one. The measured fallback shape stays recorded above and
unused; if 13's AC6 ever reds, this unit takes it without a redesign.
## 9. Revision log

- rev-1 · 2026-08-26 · initial draft. Every line citation re-derived against
  `tools/workflows/tier2-review.js` at base `cd971285`, which `git diff --stat cd971285 96f11c0e`
  confirms is byte-identical to HEAD for that file. The research record's citations were not
  copied.
- rev-2 · 2026-08-26 · spec-audit round 1 fold, closing findings 3, 9, 13, 15, 16, 25, 27, 29, 30,
  34 and 40. §4's Inventory and S9 gained the two omitted prompt sites `:195` and `:376`, and AC4
  gained the assertion that the finder's return-shape line names the same address field as the
  schema on that arm (29). S4, S7 and S9 gained one falsifiable observation each as AC15, AC16 and
  AC17, where §6 previously witnessed none of them (3). §5's observability bullet now says the
  liveness counters reach the caller and not the record, citing `TOOL-dTieredTribunal-15`, because
  the synthesis prompt at `:346` interpolates finding counts only (13). S11, §4's Files touched and
  AC11 gained the third live `6-wide` carrier `tools/check-agent-cap-restatement.sh:34-36` plus the
  build README's Parked-decisions bullet, and AC11 became a tree-wide grep (15, 25, 30). §7's
  `subject: kit` sentence lost its numeral and gained `agent-cap restatement self-test`, reconciled
  against `tools/gate-legs.json`, which reads all three of the named self-test legs as `subject: kit`
  with only the first two guarded (9, 16, 27, 34, 40). Every line citation re-derived against the
  tree at HEAD.
- rev-3 · 2026-08-26 · repaired two defects the rev-2 fold itself created, both caught by that
  fold's own adversarial verify stage before any code. `:192` — a finder-prompt sentence reading
  `the whole diff` — satisfies AC17's population and was absent from section 4's Inventory, which S9
  declares authoritative, so a builder implementing the Inventory exactly would have redded AC17.
  It is a genuine per-kind site. This sentence used to end "and the Inventory now carries it", which
  was false when it was written: rev-3 added the site to S9's prose and never touched the table.
  Corrected here rather than negated below it, and rev-4 is the revision that put the row in.
  Section 5's rollback bullet still
  said `two files` after section 4 grew to three; the numeral is deleted rather than corrected,
  because a count of a derived population does not belong in prose beside the section that owns it.
- rev-4 · 2026-08-26 · spec-audit round 2 fold, closing findings 1, 2, 5, 7, 8, 9, 10, 12, 13, 14, 18
  and 19 — five of the ten distinct defects that round grouped. §4's Inventory gained the `:192` row
  between `:184` and `:194`, and the table was read back and grepped before this line was written (1,
  5, 10, 14, 18); the rev-3 entry above, which certified that repair before it landed, is corrected in
  place. AC17's population widened from `grep -n "diff"` to a `grep -nE` alternation over `diff`,
  `file:line`, the address list and the literal `${base}...${head}`, because `:245`, `:345` and `:353`
  carry no `diff` token and the narrow grep never returned them, which also made the old `:353`
  failing-case sentence false; the widened grep was RUN at HEAD and its failing cases re-derived from
  what it actually returned (19, 2, 9). The `:194` Inventory row now names both of that line's
  diff-shaped halves, and AC4 widened from `:195` alone to every finder-prompt line naming the address
  field, with the two spaced counts added (7). AC11 gained the observation over
  `memory/builds/dTieredTribunal/README.md`, the fifth edit target S11 added and the one carrier its
  `6-wide` sweep cannot see (8, 13). §7's guard clause for the two self-test legs is DELETED rather
  than restated, because `TOOL-dTieredTribunal-14` S12 moves those guards at order 3 and this unit is
  order 4 (12). Every grep in this entry was run against the tree at HEAD, and every line citation
  re-derived there.
- rev-5 · 2026-08-26 · M3 fork sweep. F1 RESOLVED as a FACT-QUESTION whose probe already ran: the
  naive tightening denies both this selector and the one shipped user the owner's ruling protects, so
  `TOOL-dTieredTribunal-13`'s AC6 and AC6b bind the admission and this unit keeps the marked ternary.
  The measured fallback stays recorded and unused. Header gained `ratified 2026-08-26`.


## 10. Reuse audit

The seam is `tools/workflows/tier2-review.js` itself, and this unit extends it in place rather than
adding a sibling. `memory/map/features/review-harnesses.md:101-103` names that file as the reuse
affordance in exactly those terms — the reference implementation of the pipeline and of every trust
counter — and instructs an extender to carry a guard together with the comment naming the unit that
earned it, which is what S13 does. Two further seams are reused unchanged:
`tools/memory-tree/README.md` supplies the four M4 lens briefs, and `tools/hooks/agent-cap.js`
supplies the bound this unit's fan-out must satisfy.

`python tools/codebase-map/reuse_lookup.py "a review harness that drives finder lenses and batched
skeptics over a subject and writes one report"` returned a MISS on the harness, and the miss is
recorded as an answer. Its ranked candidates were name-stem matches on `write` and `report` across
`tools/memory-tree/` and `tools/drift-audit/`, plus the `agent-cap` and `review-harnesses`
affordance seams. It did not surface `tier2-review.js` as a symbol, because the corpus indexes
symbols and this file exports one `meta` object and defines two helpers. The dossier reached it and
the symbol index did not, which is the same shape as the exports-only gap recorded at
`TOOL-dClosedLexicon-12`.

`python tools/memory-recall/query.py "has anything decided whether one review engine may take a
review-kind parameter and drive a spec audit" --terms "review kind parameter spec-audit diff-review
tier2-review harness lens catalogue subject descriptor generalisation engine"` returned 36 hits.
The decisive ones are `TOOL-dTieredTribunal-7`, which authorizes this unit, and the research
record's own prior-art probe, which found four prose hits and no code anywhere taking a review-kind
parameter. Also returned and relevant: `TOOL-aLoosenedCeiling-6`, closed by the synthesis prompt
gaining a kind-bearing binding line, which is the exact string S8 parameterises; and
`TOOL-dHonouredPark-5`, which records a bespoke spec-audit fan-out whose four lenses each numbered
from `F1` and whose whole verify stage was discarded — the failure this unit's integer join makes
impossible for a spec audit for the first time. No record refuses the generalisation on merits.

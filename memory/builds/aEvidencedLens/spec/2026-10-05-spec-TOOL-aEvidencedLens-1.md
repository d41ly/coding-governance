# TOOL-aEvidencedLens-1 — the spec-audit lens catalogue: five lenses aimed at the measured classes, the harness its one source

**Status:** SPECCED · rev-1 · 2026-10-05 · node a · Tier-2 · base 028b5cac · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-0-run-mandate.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-0-run-mandate.md) | journal | — |
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md) | journal | TOOL-aEvidencedLens-2 TOOL-aEvidencedLens-3 TOOL-aEvidencedLens-4 TOOL-aEvidencedLens-5 TOOL-aEvidencedLens-6 TOOL-aEvidencedLens-7 TOOL-aEvidencedLens-8 TOOL-aEvidencedLens-9 TOOL-aEvidencedLens-10 TOOL-aEvidencedLens-11 |
| [2026-10-05-prompt-TOOL-aEvidencedLens-1-2-build-brief.md](../prompts/2026-10-05-prompt-TOOL-aEvidencedLens-1-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A spec audit runs four lenses whose briefs name none of the classes that most often escaped it:
fallout on the repo's own machinery, a criterion that cannot pass, degenerate inputs, and an
instance named where the class was meant. This unit replaces them with five lenses aimed at the
measured classes, reshapes prior art into a reuse-and-extend lens with a stricter bar, and makes the
harness the one source of the catalogue.

## 2. Scope (IN)

- **S1** — `SPEC_LENSES` in `tools/workflows/tier2-review.template.js` holds exactly five lenses, in
  this order: `coherence`, `grounding`, `reuse`, `blast-radius`, `failure-envelope`. Their briefs are
  the five texts under §4 "The catalogue". The four keys `underspecification`, `contradiction`,
  `unstated-assumption` and `prior-art` are retired. Observed by AC1, AC2 and AC3.
  - **Readers:** by name: `tools/workflows/tier2-review.test.sh` spells the four keys in `SPEC_KEYS`,
    `SPEC_ORDER`, a `buildLensFile` call and a `lensNotes` control; `tools/workflows/unattended-build.test.sh`
    spells `find:underspecification` in `MT20_SHAPE`; `tools/memory-tree/README.md` and
    `tools/memory-tree/BUILD-METHOD.template.md` list them, and unit 11 owns both. by value: the
    `lensNotes` validator compares a caller's keys against `LENS_KEYS`, which derives from this
    array; the checklist split assigns items round-robin over the running keys; finding ids are
    assigned in lens order, which the two self-tests' id-range fixtures count.
- **S2** — The `reuse` lens brief carries the probe recipe and the stricter bar: a reuse finding names
  the existing seam or record by path or id AND the spec text that duplicates or contradicts it. Its
  tools are named by bare filename and located with `git ls-files`, never by a kit path. Observed by
  AC2 and AC7.
- **S3** — `REVIEW_SHAPE` moves from `'lenses5-r1'` to `'lenses5-r2'`, once for this build (shared
  invariant 5). Observed by AC4.
- **S4** — No diff-kind prompt changes. The finder, skeptic and synthesis prompts of a diff review
  are byte-identical to the pass-start render once each run's own review key is masked. Observed by
  AC5.
- **S5** — The comment above `SPEC_LENSES` stops saying the catalogue is "COPIED from
  <prefix>/memory-tree/README.md" and says this array is the catalogue's one source. The meta `Find`
  detail names both kinds' lens counts. `tools/workflows/README.md` stops saying "A spec audit keeps
  its four lenses" and names the five. Observed by AC6.
- **S6** — The self-test arms that pin the four old keys, the spec-kind lens count or the id ranges a
  four-lens spec fan produced are re-keyed in `tools/workflows/tier2-review.test.sh` and
  `tools/workflows/unattended-build.test.sh`, and the first file's `FLOOR_ASSERTIONS` rises by the
  number of arms added. Observed by AC8.
- **S7** — The template and its render `tools/workflows/tier2-review.js` land in the same commit, the
  render regenerated, never hand-edited. Observed by AC9.

## 3. Non-goals (OUT)

- The probe policy, the `evidence` field and lifting "nothing outside the spec set" — unit 2.
- The spec skeptic's verdict test — unit 3. The round-N brief and the moved-blob grade — unit 4.
- Per-lens yield — unit 6.
- `tools/memory-tree/README.md`'s M4 catalogue and BUILD-METHOD M4's catalogue sentence. Both become
  pointers at `SPEC_LENSES`, and both are governance carriers unit 11 owns (shared invariant 11).
- `tools/hooks/agent-cap.js`. The receiver stays an array literal of five and the marked ternary
  stays as it is (shared invariant 6).
- Any kit version bump (shared invariant 7).
- A light lens subset for the spec kind. A spec audit still refuses `intensity: light`.

### Edges

- **hands-off** `TOOL-aEvidencedLens-2` — the probe policy the reuse and grounding lenses need to run
  commands legally; until it lands, the finding line still says "nothing outside the spec set".
- **hands-off** `TOOL-aEvidencedLens-11` — the memory-tree README M4 list and BUILD-METHOD M4's
  catalogue sentence become pointers at this unit's `SPEC_LENSES`.

## 4. Design

### Evidence

Read at HEAD of the run branch, whose `tools/` tree equals base `028b5cac`.

- `SPEC_LENSES` is template lines 459-482: four elements, under a comment saying the catalogue is
  COPIED from the memory-tree README (`TOOL-dTieredTribunal-11` S2).
- The receiver is `const LENSES = isSpec ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers` (line
  488). `LENS_KEYS` derives from it (line 505) and feeds the `lensNotes` refusal text.
- `REVIEW_SHAPE = 'lenses5-r1'` (line 609) joins `inputPrint`, which joins the review key. The key is
  interpolated into every finder prompt's DURABILITY line (line 784) and every skeptic's (line 915),
  on BOTH kinds. A literal byte-identity claim about diff prompts therefore cannot pass on a correct
  build: the shape bump moves the key inside them. S4 masks the key, which is the only change this
  unit makes to a diff prompt.
- The meta `Find` detail reads `'5 finder lenses (3 on a light run), one wave, ≤{{FANOUT_CAP}}
  concurrent'` and is true of the diff kind only.
- `tools/workflows/unattended-build.test.sh` RUNS the callee `tier2-review.js` over `MT_ARGS`, a
  spec audit (line 744), with a `find:` double of twelve findings per lens. The default shape
  asserts 48 raw over four lenses, and `MT20_SHAPE` asserts 46 raw from
  `{"find:underspecification":10,"find:":12}`. A fifth lens matched by `find:` adds twelve more and
  reds both.
- `tools/check-install-prefix.sh` rule 3 counts a kit segment followed by a file under any prefix,
  in templates and in `*.test.sh` alike. A brief or an arm spelling `codebase-map/reuse_lookup.py`
  reds that leg.

### The catalogue

The five briefs, as each `brief` string. "section N" is spelled in words, as the existing briefs do.

- **`coherence`** — "Coherence: does the spec set agree with itself, and can its acceptance decide
  anything? Report a section-2 item no section-6 criterion observes; a criterion whose observation
  cannot FAIL on today's tree, because it is already green before the unit is built; a criterion that
  cannot PASS on a correct build, because it demands what the design does not produce or a figure the
  build cannot reach; section 2 against section 3; section 4 Design against section 7 Gates; and,
  across the subjects and the sibling context, the four axes scope, interface, ordering and
  acceptance: a name, path or key spelled two ways, a unit depending on one ordered after it, two
  units claiming one file or one landing slot, and an overview acceptance no unit's criteria imply."
- **`grounding`** — "Grounding: is every claim sections 4 and 10 make about the world TRUE where the
  subjects stand? Check each claim about existing code, a tool's flags or output, a record, a count,
  a platform behaviour or a cost against the source, never against the spec. Hunt the traps this
  platform sets: MSYS argument and path rewriting, drive-letter and backslash paths, CRLF in a
  working copy and a text-mode read that drops a CR, and a stated wall-clock goal nobody timed. A
  claim marked UNVERIFIED is a finding only where the design rests on it."
- **`reuse`** — "Reuse: functionality is reused and extended, never rebuilt. Report a design that
  builds what already exists, such as a function, a checker, a gate leg, a driver verb or a record
  shape, instead of extending it; a section-10 seam that is cited but is not the one section 4
  extends, or that does not exist; and a question a decision record or an ask already decided,
  decided asks included. Probe before you claim: the codebase-map kit's reuse_lookup.py with a
  behaviour phrase, the memory-recall kit's query.py with a plain-English question and 8-14 --terms
  in this corpus's own jargon, and grep, because the lookup cannot see every layer and prints the
  ones it skipped. Locate each tool with git ls-files; where one is absent, say so in the finding and
  use grep. Read the asks through the memory-tree kit's gen_build_index.py --asks --json --all,
  falling back to the backlog shards when its mode field says shards. THE BAR: a reuse finding names
  the existing seam or record by path or id AND quotes the spec text that duplicates or contradicts
  it. That a related record exists is not a finding."
- **`blast-radius`** — "Blast radius: what does this change trip that the spec does not list? For
  every name, value or rule the spec renames, retires or changes, grep the name AND the value, and
  report each consumer, carrier, test arm or document the spec does not name. Join section 4's
  files-touched list against the gate-leg manifest (gate-legs.json, where the project keeps one) and
  report a guarded leg section 7 omits; report a declared size or time budget the change will cross;
  and report the repo's own machinery the spec forgets: version carriers, codebase-map keys, record
  and filename rules, a --dispatch write set, and a render an adopter regenerates."
- **`failure-envelope`** — "Failure envelope: what will the built thing meet that the spec never says
  it handles? Report the input classes the design is silent on (empty, malformed, multi-line,
  unterminated, huge, concurrent), signals, partial failure and a dead dependency; a security or
  write surface section 5 did not price; and a spec that names one INSTANCE where the class was
  meant, such as one file of two or one caller of three. A spec is built as a ceiling: in this kit's
  own trial (aBlindedTrial, report section 4.3), when a spec named the class for one input file and
  not the other, the builder handled exactly the file it named."

The order is fixed by the id layout the self-tests count: `coherence` takes the first slot, as
`underspecification` did, so a fixture keyed on the first lens keeps its ids.

### The comment and the meta line

- The comment above `SPEC_LENSES` names `TOOL-aEvidencedLens-1`, says this array IS the catalogue,
  and says the method and the memory-tree README point here rather than list names. The words
  "COPIED from" leave the file.
- The meta `Find` detail becomes `'5 finder lenses on either kind (3 on a light diff run), one wave,
  ≤{{FANOUT_CAP}} concurrent'`.

### Self-test re-keying

| File | What moves |
|---|---|
| `tools/workflows/tier2-review.test.sh` | `SPEC_KEYS` and `SPEC_ORDER` take the five keys; `buildLensFile('prior-art', …)` and `find:prior-art` become `reuse`; the `lensNotes` control becomes `{ reuse: 'n' }`; every arm counting spec-kind `find:` or `verify:` traces moves from 4 to 5 (lines 282, 435, 496, 498, 561 at HEAD); the two arms summing both kinds move too, `vp.length === 9` to 10 (line 702) and `scanRubricOk(rrs, 9)` to 11 (line 818); the comment at line 669 says five |
| `tools/workflows/tier2-review.test.sh` | one NEW `lensNotes` refusal row: the retired key on a spec audit, spelled `'prior-' + 'art'` so the file keeps no literal of it, as the retired diff key already is |
| `tools/workflows/unattended-build.test.sh` | the default shape's `lenses` becomes `{ "find:failure-envelope": 0, "find:": 12 }` (48 raw, ids 1-48 on the first four lenses as before); `MT20_SHAPE`'s becomes `{"find:coherence":10,"find:failure-envelope":0,"find:":12}` (46 raw, the same id layout); the comment at line 745 says so |

The doubles match the FIRST key a label starts with, in insertion order, so the specific keys sit
before `find:`. A fifth lens returning no finding keeps every measured id range, which is what the
replayed records' merges are keyed on.

### Inventory

Mints no function, constant or file. Five lens keys replace four inside one array. No codebase-map
inventory key moves: lens keys are not inventoried.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/README.md`

### Alternatives rejected

- **Naming the tools through `{{TOOL_ROOT}}`.** It needs `TOOL_ROOT` added to the harness's
  `placeholders` in `tools/workflows/kit.toml`. Two adopters install the memory-tree kit flat
  (`tools/workflows/check-protocol-parity.test.sh`, token comment), so a rendered nested path names a
  file they do not have. A bare filename located with `git ls-files` finds either layout and changes
  no declaration. See §8 F1.
- **A sixth lens.** The hook admits at most five elements on an array-literal receiver.
- **Keeping `prior-art` and adding `reuse`.** Prior art was the noisiest lens (precision 0.58, about
  60% of its confirmed output belonging to other lenses' classes, measured 2026-10-05, session study),
  and the decided-record half lives on inside `reuse` with a stricter bar.
- **Keeping the README as the source and copying it here.** That is the direction that drifted: the
  prior-art brief here already differs from the README's line. A pointer cannot drift.

## 5. Production-readiness checklist

- security — no new input surface. Lens briefs are constants; `lensNotes` keeps its refusal, over the
  new keys.
- perf / scale — one more lens agent per spec audit, five where there were four, inside the cap. Each
  spec finding adds one id to the skeptic batches, whose count stays bounded by the cap.
- error / empty / loading states — a lens returning no finding is already a live lens; the checklist
  split already handles fewer items than lenses.
- observability — the lens key is on every finding, in the ledger and in the appendix, as today.
- risks — until unit 2 lands, the reuse and grounding briefs ask for probes the finding line still
  forbids. The prior-art brief at HEAD has the same tension, and no unit lands alone.
- testing — the arms in §4 "Self-test re-keying"; the suites run once at VERIFYING, at the main loop.
- migration — a lens file written under `lenses5-r1` is never reused, because the shape moved.
- user docs — `tools/workflows/README.md` here; the method and the memory-tree README in unit 11.

## 6. Acceptance criteria

The stub run below is `tools/workflows/tier2-review.js` evaluated as an AsyncFunction with recording
`agent` doubles, the shape the kit's own self-test uses, copied into a scratch script and run with
`node`. It never runs the suite.

- **AC1** — When the stub run evaluates `tools/workflows/tier2-review.js` over spec-audit args, the
  trace holds exactly five `find:` labels, in the order `find:coherence`, `find:grounding`,
  `find:reuse`, `find:blast-radius`, `find:failure-envelope`, and five `verify:` batches for one
  finding per lens.
  Red when: `SPEC_LENSES` still holds the four retired keys and the trace holds four labels.
- **AC2** — When the same run's `find:` prompts are read, each carries its own brief on its `LENS:`
  line: `coherence` names both "cannot FAIL" and "cannot PASS", `grounding` names `MSYS` and `CRLF`,
  `reuse` names `reuse_lookup.py`, `query.py`, `--asks --json --all` and "THE BAR",
  `blast-radius` names `gate-legs.json` and "version carriers", and `failure-envelope` names
  "INSTANCE" and "section 4.3".
  Red when: a brief is the old text or omits the class it was written for.
- **AC3** — When the stub run is handed `lensNotes: { reuse: 'n' }` on a spec audit it proceeds, and
  when handed the retired `prior-art` key it throws before any agent, naming `lensNotes` and the five
  keys `coherence | grounding | reuse | blast-radius | failure-envelope`.
  Red when: the retired key is still accepted.
- **AC4** — When `grep -c "const REVIEW_SHAPE = 'lenses5-r2'" tools/workflows/tier2-review.template.js`
  runs it prints 1, and two stub runs of identical spec args, one over the pass-start render and one
  over the new render, return different `key` values.
  Red when: the literal still reads `lenses5-r1` and the keys are equal.
- **AC5** — When the stub run evaluates the pass-start render and the new render over the same diff
  args, once at round 1 with `checklist` and `specs` and once at round 2 with `priorFindings`, and
  each run's `result.key` is replaced by a fixed token in its prompts, every `find:`, `verify:` and
  `synth` prompt is byte-identical between the two renders.
  Red when: a diff lens brief, the diff finding line or a shared brief line changed.
  fixture: the pass-start render is `tools/workflows/tier2-review.js` as `git show` prints it at the
  sha the pass recorded before its first edit, saved to the scratchpad.
- **AC6** — When `grep -c "COPIED from" tools/workflows/tier2-review.template.js` runs it prints 0;
  `grep -c "keeps its four lenses" tools/workflows/README.md` prints 0 and `grep -c "failure-envelope"
  tools/workflows/README.md` prints 1 or more; and the meta `Find` detail contains "on either kind".
  Red when: the README still says four.
- **AC7** — When `bash tools/check-install-prefix.sh --offenders` runs, no key it prints names a
  file this unit touched.
  Red when: a staged break spells the reuse tool as a kit path in the `reuse` brief, which this
  checker counts under rule 3.
- **AC8** — When `grep -c -E "underspecification|unstated-assumption|'prior-art'" tools/workflows/tier2-review.test.sh tools/workflows/unattended-build.test.sh`
  runs it prints 0 for both files, and the stub run of the callee over `MT_ARGS` with the new
  `MT20_SHAPE` lens map returns `"raw":46` and over the new default map returns `"raw":48`.
  Red when: a fixture still keys a retired lens, or the fifth lens adds twelve findings to a measured
  shape.
  permission: the two suites themselves run once at VERIFYING, at the main loop, and not in this pass.
- **AC9** — When the template is rendered with `{{FANOUT_CAP}}` replaced by the value
  `bash tools/workflows/check-verifier-fanout.sh --print-cap` prints, the result equals
  `tools/workflows/tier2-review.js` byte for byte.
  Red when: the render was hand-edited or not regenerated.
  figure: the cap is DERIVED from the hook at observation time.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `install-prefix (shipped surface)` · `workflow script syntax` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · the retired spec key on a spec audit, refused by `lensNotes`, against the base render that accepts it · `FLOOR_ASSERTIONS` raised by one
New arm: tools/workflows/tier2-review.test.sh · five spec-kind `find:` labels in catalogue order, against the base render's four · `FLOOR_ASSERTIONS` raised by one

## 8. Open questions

- **F1 — How does the reuse brief name the tools it probes with?** (a) Bare filenames located with
  `git ls-files`, each "where present". (b) Kit paths through a new `{{TOOL_ROOT}}` token declared
  in `tools/workflows/kit.toml`. Option (b) renders a nested path two flat installs lack, and adds a
  declaration; (a) satisfies every criterion with neither. Recommend (a).
  RESOLVED (agent, 2026-10-05, delegated): (a), bare filenames located with `git ls-files`.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the template, its render and both self-tests at HEAD.

## 10. Reuse audit

The seam extended is `SPEC_LENSES` and its marked receiver in `tools/workflows/tier2-review.template.js`,
with `LENS_KEYS`, the `lensNotes` refusal and the checklist split reading it unchanged. The diff
kind's catalogue, `DIFF_LENSES`, is the precedent for the brief shape and for a lens set replaced
under one review-shape bump (`TOOL-aSightedSkeptic-5`). `python tools/codebase-map/reuse_lookup.py
"spec audit lens catalogue finder briefs"` returned no seam that holds a lens catalogue; its top hits
were name-stem matches such as `parse_spec_h1` and `checkSpecAuditDeclared`, and it printed
`unscanned layers: .sh`. Recall returned `TOOL-aSightedSkeptic-5`, the `TOOL-dTieredTribunal-7`
ruling that one engine drives a spec audit, and BUILD-METHOD M4's catalogue sentence. The
`TOOL-dTieredTribunal-11` S2 comment chose README-to-harness copying; this unit reverses the
direction, and §4 "Alternatives rejected" says why.

Recall terms used: spec-audit lens catalogue SPEC_LENSES prior-art underspecification contradiction unstated-assumption tier2-review finder brief REVIEW_SHAPE lensNotes

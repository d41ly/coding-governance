# TOOL-aRoutedQuill-1 — a Tier-1 spec is a micro-spec, and check 12 grades its sections by heading text

**Status:** CLOSED · rev-3 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 1 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aRoutedQuill-1-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aRoutedQuill-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md) | journal | KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7 |
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-build-brief.md) | journal | — |
| [2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md](../reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md) | diff-review | KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-5 TOOL-aRoutedQuill-7 |

<!-- /gen:spec-records -->

## 1. Goal

Check 12 grades a Tier-1 spec on its status header, its placeholders and the arms that run for both
tiers, so a SPECCED Tier-1 spec holding only a header and a revision log passes it today. The write
gate this build adds admits a Tier-1 unit at SPECCED on the strength of that grade, so the grade has
to mean something. This unit gives Tier-1 a micro-spec profile: eight required sections named by
heading text, each non-empty, graded by check 12 from a new dated cutoff, with a copyable skeleton
shorter than Tier-2's and a generator that writes it. Tier-2's canon does not change.

## 2. Scope (IN)

- **S1** — The Tier-1 bullet of `tools/memory-tree/SPEC-TEMPLATE.template.md` (section `Tier
  profiles, sub-specs, and where recurring content lives`) states the micro-spec profile: the eight
  required titles, the two optional ones, which owner phrase each answers, and that a spec dated
  before `SPEC_TIER1_CUTOFF` keeps the light profile. The file's opening paragraph and its
  headings-never-disappear rule say the same, and `memory/TEMPLATE-SPEC.md` is re-rendered from it.
  Text is §4 "The template text". Observed by AC7.
- **S2** — The same section carries a copyable Tier-1 skeleton fence, eight sections long, placed
  above the Tier-2 skeleton. Observed by AC6 and AC7.
- **S3** — Check 12 gains a Tier-1 arm in `tools/memory-tree/check-memory-hygiene.sh`, graded on
  a Tier-1 spec whose filename date is on or after `SPEC_TIER1_CUTOFF`: every `##` heading is a
  canonical title, the eight required titles are present, the titles present run in canonical
  order, and no section body is empty. It sits above the Tier-1 cut and reads one file, so it runs
  under `--staged` too. Mechanism is §4 "The check 12 arm". Observed by AC1, AC2, AC3 and AC4.
- **S4** — `SPEC_TIER1_CUTOFF` is a new date key with blank meaning off, on the terms its sibling
  cutoffs use. It is preset blank beside them in the engine, shipped blank in
  `tools/memory-tree/.memory-tree.conf.example`, declared in gov's `.memory-tree.conf` strictly
  ahead of every spec filename date, and announced by a zero-population notice beside its siblings'
  notices. Observed by AC5 and AC8.
- **S5** — `gen_build_index.py --new-spec <ID> --tier 1` writes the Tier-1 skeleton's eight
  headings, and `--tier 2` writes what it writes today. Observed by AC6.
- **S6** — Check 12's header comment in the engine and the check 12 entry of
  `tools/memory-tree/HYGIENE.template.md` state the Tier-1 arm; `memory/HYGIENE.md` is re-rendered
  from it. Observed by AC7.

## 3. Non-goals (OUT)

- Any change to the Tier-2 canon or to an arm that grades Tier-2 only: the section equality, the
  §8 F-item shape at any status, §3 Edges, the §5 readiness rows and the §10 evidence arm.
- Grading what a micro-spec says. The arm reads shape; a non-empty but hollow section passes, and so
  does a required section reading `N/A — <why>`.
- Grading ordinal values. A Tier-1 spec numbers its sections as it likes; plan_state, the scope join
  and `tools/check-spec-tokens.py` already find sections by text.
- Retrofitting a landed or grandfathered Tier-1 spec. The cutoff grades by filename date.
- The write gate, its BUILDABLE predicate, and what it admits for a Tier-1 spec the arm never graded:
  `TOOL-aRoutedQuill-2` (§8 F1 is the recommendation handed to it).
- The charter's Definition of Ready wording: `PLAY-aRoutedQuill-1`.
- The THIN predicate in `tools/unattended/unattended.sh`. A micro-spec that passes the arm already
  carries a non-empty Scope, Acceptance criteria and Gates, so it can never grade THIN.

### Edges

- **hands-off** `TOOL-aRoutedQuill-2` — a Tier-1 spec at SPECCED whose eight sections check 12
  graded at commit time, plus the facts in §4 "What check 12 grades, and when", which bound what the
  write gate may infer from SPECCED; what it admits for an ungraded Tier-1 spec is its decision.
- **hands-off** `PLAY-aRoutedQuill-1` — the micro-spec by name and the four owner phrases it
  answers, which the charter's Definition of Ready states and points at the spec template for.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- Check 12 is one awk program over the tracked spec population, `git ls-files` of the memory root
  (`tools/memory-tree/check-memory-hygiene.sh:276`). The cut `if (hdr ~ /Tier-1/) next` sits at
  `tools/memory-tree/check-memory-hygiene.sh:2008`. Above it, both tiers get the header,
  placeholder, streams, witness, failure-mode, scope-join, reader-inventory, rev high-water,
  base-resolve, rev-scope and terminal §8 arms. Below it sit the Tier-2-only arms, ending with the
  canon compare at `:2131` and the empty-body walk that prints at `:2150`.
- The rev high-water arm reds any spec, either tier, whose header rev is not logged under a
  `Revision log` heading (`:1823`). A terminal spec of either tier with no `Open questions` heading
  reds at `:1955`. So a Tier-1 spec already needs both sections, the second only once it closes.
- The canon titles reach the awk as `-v canon10` (`:1483`), built from `SPEC_CANON` (`:1441-1449`)
  plus the tenth heading.
- `plan_state` keys Scope, Acceptance criteria, Gates and Open questions by heading title
  (`tools/unattended/unattended.sh:3616-3645`, TOOL-dBriefedPass-1), and the scope-join arm does the
  same in check 12 (`:1694-1697`).
- `render_spec_skeleton` (`tools/memory-tree/gen_build_index.py:6326`) takes the FIRST fence whose
  next line opens with the skeleton's placeholder H1 as its start (`:6335-6336`) and the LAST fence
  line in the file as its end, then keys each section's body by its NUMBER (`:6345-6362`, `:6369`).
  A second skeleton fence above the Tier-2 one would be taken as the start and merge both heading
  lists, and a renumbered Tier-1 heading would receive the wrong body. So S2 needs S5.
- Observed on 2026-10-09: a SPECCED Tier-1 probe spec holding only its status header and a
  `## 1. Revision log` logging rev-1, staged in a throwaway clone at base, drew no check 12 finding
  from `check-memory-hygiene.sh --staged`. That is the Goal's claim, and AC1's fixture.
- Measured over `git ls-files` on 2026-10-09, PINNED: 270 Tier-1 specs are dated on or after
  `SPEC_FORMAT_CUTOFF`. All 270 carry Goal, Open questions and Revision log; 267 carry Scope (IN),
  Non-goals (OUT) and Acceptance criteria; 263 carry Gates; 251 carry Design; 249 carry all eight.
  One is live, `memory/builds/dLandedVerdict/spec/2026-08-19-spec-TOOL-dLandedVerdict-2.md` at
  INPROGRESS. The same walk re-derives the figures.
- The newest spec filename date over 42 local and remote refs on 2026-10-09 is 2026-10-09, PINNED.

### The micro-spec canon

| Title | Tier-1 | Owner phrase it answers (D3) |
|---|---|---|
| Goal | required | what to do |
| Scope (IN) | required | what to do, each item verifiable at done |
| Non-goals (OUT) | required | out of scope |
| Design | required | how to do it |
| Production-readiness checklist | optional | none: Tier-2's owner scope menu |
| Acceptance criteria | required | definition of done, and the observation half of how to verify |
| Gates | required | how to verify: the legs kept green and any new arm |
| Open questions | required | none: already demanded at close, and `none` costs one line |
| Revision log | required | none: the rev high-water arm already demands it on both tiers |
| Reuse audit | optional | none: the §10 evidence arm stays Tier-2 only |

### The check 12 arm

Population: a P record whose header carries `Tier-1`, with `t1cut` non-empty and the filename date
on or after it. The arm lives in the every-tier band, after the rev-scope arm and before the Tier-1
cut, guarded by `t1cut` alone so its population is never an intersection with a sibling key.

The canonical titles come from `canon10` by stripping each line's `## <n>. ` prefix, so the title
list keeps one spelling in the engine. The optional set is the two-title literal above.

One walk over `body[]` collects every `## ` line. A line not shaped `## <digits>. <title>`, or whose
title is not canonical, is NOT CANONICAL. Each canonical title takes its index in the ten. Titles
whose index does not strictly increase from the previous one are OUT OF ORDER, which also catches a
duplicate. Required titles never seen are MISSING. A section with no non-blank line before the next
`## ` is EMPTY, by the empty-body walk's own test. One finding line per spec names the cutoff and
every non-empty class with its titles. The arm emits no sentinel and joins nothing.

A zero-population notice joins its siblings near `:2463`, counted by date over the selection: it
over-counts by including Tier-2 specs, which is the safe direction the §10 notice already records.

### What check 12 grades, and when

The write gate reads a status the agent writes, so its admission at SPECCED is only as good as the
moment that status was last graded.

- At commit: `.githooks/pre-commit:126-133` runs `check-memory-hygiene.sh --staged` whenever a
  `memory/**` path is staged. Under `--staged` check 12's selection is the staged spec files
  (`in_scope`, `:503`), read from the WORKTREE, not from the staged blob (`:1427-1428`). This arm
  reads one file and holds no join, so it runs there.
- At the push boundary: the `memory hygiene` leg runs the engine in full mode over every tracked
  spec, and `.githooks/pre-push` runs the bar before a default-branch push.
- Not graded: an untracked spec, which is outside `git ls-files`; a spec edited after its last
  commit, until the next commit staging a `memory/**` path or the next bar; a commit made with
  `--no-verify`; and every Tier-1 spec dated before `SPEC_TIER1_CUTOFF`, or in a tree whose key is
  blank, which is every adopter until it arms the key.

### The template text

The Tier-1 bullet, replacing the light-profile bullet in the template's tier section:

```markdown
- **Tier-1** (micro-spec): a spec dated on or after `SPEC_TIER1_CUTOFF` carries eight `##`
  sections, found by heading TEXT, in canonical order, none empty: Goal, Scope (IN), Non-goals
  (OUT), Design, Acceptance criteria, Gates, Open questions, Revision log. Production-readiness
  checklist and Reuse audit are optional and sit at their canonical place when written; no other
  `##` title is legal, and numbering is free. Goal, Scope and Design say what and how, Acceptance
  criteria says when it is done, Non-goals says what is out of scope, and Acceptance criteria with
  Gates say how to verify it. A Tier-1 spec dated before the cutoff keeps the light profile: the
  status header and placeholder rules only. The skeleton is below.
```

The skeleton fence that follows it, with no fence nested inside. It is shown indented two spaces
so this spec's own heading readers skip it; the template carries it at column 0:

```markdown
  # <FAMILY-slug-seq> — <title>

  **Status:** OPEN · rev-1 · YYYY-MM-DD · node <tag> · Tier-1 · base <sha8> · streams <value>

  ## 1. Goal

  What changes and why, in one or two sentences.

  ## 2. Scope (IN)

  - **S1** — What this unit builds, verifiable at done. Observed by AC1.

  ## 3. Non-goals (OUT)

  What an eager builder might include but must not.

  ## 4. Design

  How it works, in a few sentences.

  ### Files touched (estimate)

  `<path>`

  ## 5. Acceptance criteria

  - **AC1** — When `<command>` runs, <the observable result>.
    Red when: <the break that turns it red>.

  ## 6. Gates

  `<leg>`

  ## 7. Open questions

  none

  ## 8. Revision log

  - rev-1 · YYYY-MM-DD · initial draft.
```

The opening paragraph's sentence on what check 12 enforces gains the Tier-1 clause, and the
headings-never-disappear rule reads as binding a profile's required set.

### The generator

`render_spec_skeleton` selects its fence by tier. For `--tier 1` it takes the skeleton fence whose
status line reads `Tier-1` and ends at that fence's own closing line. For `--tier 2` it takes the
LAST fence opening on the placeholder H1, which is today's skeleton, and keeps today's end rule.
Bodies are chosen by heading TITLE rather than number, each title receiving the body its Tier-2
number receives today, so Tier-1's `## 5. Acceptance criteria` gets the criterion slot and not the
readiness rows. Tier-2 output stays byte-identical. A template with no Tier-1 fence refuses
`--tier 1` by name rather than falling back to ten sections.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `SPEC_TIER1_CUTOFF` | conf key and engine preset | none: conf keys carry no naming cell |
| `t1cut` | awk `-v` variable | none: an awk variable is not a function definition |
| `SPEC_TITLE_NUMBERS` | python module constant in `gen_build_index.py` | `py.constant`, upper snake |

No function is minted; the generator's title-to-body map is the one constant above. If the builder extracts the arm into an awk function,
`python tools/lexicon/lexicon.py --suggest check_tier1_canon --as sh.function` answered OK; whether
the lexicon grades an awk function inside a shell string is UNVERIFIED.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` · `tools/memory-tree/check-memory-hygiene.test.sh` · `tools/memory-tree/SPEC-TEMPLATE.template.md` · `tools/memory-tree/HYGIENE.template.md` · `tools/memory-tree/.memory-tree.conf.example` · `tools/memory-tree/gen_build_index.py` · `memory/TEMPLATE-SPEC.md` · `memory/HYGIENE.md` · `.memory-tree.conf` · `memory/guides/SESSION-KICKOFF.md`

### Rollout

- Edit the two templates, then re-render `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md` with the
  dogfood parity script's `--render` mode; never hand-edit the renders.
- `SPEC_TIER1_CUTOFF` takes the relation `SPEC_HANDOFF_CUTOFF` records, RE-DERIVED at landing: the
  later of the newest spec filename date on any local or remote ref and the landing commit's day,
  plus one. The build-time derivation on 2026-10-09 gives 2026-10-10, DERIVED. This build's own
  Tier-1 unit, dated 2026-10-09, is therefore grandfathered and is written to the profile anyway.
- No kit version is bumped here. The memory-tree version moves once, after the build's last unit
  touching the memory-tree kit, and the lander mints it (`govkit.py mint`, called from
  `tools/push-main.sh:599`), which also moves every other carrier of that marker.
- The engine and `.memory-tree.conf` are on the kickoff manifest's `watch:` list, so the commit
  staging them re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md` with a delta line.
- Enforcement starts at landing, with no warn phase (D4). An adopter's example conf ships the key
  blank, so arming it there is that adopter's act; §8 F1 is how the write gate copes until it does.

### Alternatives rejected

- **Six required sections, without Open questions and Revision log.** The rev arm already reds a
  Tier-1 spec with no logged revision, and a terminal one with no Open questions; a six-section
  skeleton would be copied into specs that red at close.
- **An ordinal-keyed Tier-1 canon, `## 1.` to `## 8.` exactly.** Every reader that grades Tier-1
  finds sections by title, and TOOL-dBriefedPass-1 measured the ordinal read failing on Tier-1.
- **All ten sections on Tier-1.** D3 asks for an efficient Tier-1 spec, and the readiness checklist
  exists to become the Tier-2 owner scope menu.
- **Grading through the THIN predicate.** THIN is read by the unattended kit at dispatch and close;
  the write gate needs the grade check 12 makes at commit, on attended work too.
- **A conf-declared Tier-1 title list, rendered like `READINESS_ROWS`.** No adopter has asked to
  vary it, and it would add a placeholder, a render and a second channel for one fixed list.

## 5. Production-readiness checklist

- security — no new write path. The arm narrows what check 12 admits, and it is the content floor
  the write gate trusts, so a false pass here is a quiet route past that gate.
- perf / scale — one more loop over `body[]`, already in memory inside the single awk; no fork.
- error / empty / loading states — a blank key is off; an armed key grading nothing prints the
  notice; a Tier-1 spec with no `##` heading at all reds naming all eight titles.
- observability — the finding names the file, the cutoff, and each missing, misplaced, empty or
  non-canonical title.
- risks — a hollow section passes, as it does on Tier-2. The Tier-1 specs the arm never grades are
  §4 "What check 12 grades, and when" and §8 F1.
- testing — fixture arms in the hygiene self-test and in the generator's `--selftest`.
- migration — none: the cutoff grandfathers the landed corpus and adopters receive a blank key.
- user docs — `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md` are the user docs.

## 6. Acceptance criteria

- **AC1** — When `check-memory-hygiene.sh` runs over a fixture tree whose conf sets
  `SPEC_TIER1_CUTOFF` and which holds a SPECCED Tier-1 spec dated on it carrying only its status
  header and a `## 1. Revision log` logging rev-1, it names the spec and the seven missing titles.
  Red when: the spec passes, as the engine at base passes it.
- **AC2** — When that fixture spec carries the eight required sections numbered 1 to 8, with no
  readiness checklist and no reuse audit, check 12 reports nothing for it; and when the same body
  sits under a `Tier-2` header, `check-memory-hygiene.sh` still reports the canon difference.
  Red when: a renumbered micro-spec reds, or the Tier-2 canon admits the eight.
- **AC3** — When one required section of AC2's fixture is emptied, `check-memory-hygiene.sh` names
  it as empty; when `## 3. Non-goals (OUT)` and `## 4. Design` swap places it names the order; when a
  `## 9. Notes` heading is added it names the title as not canonical.
  Red when: any of the three passes.
- **AC4** — When a fixture repo stages only AC1's spec and `check-memory-hygiene.sh --staged` runs,
  it names the spec. This is the commit-time grade `TOOL-aRoutedQuill-2` relies on.
  Red when: the arm is held under `--staged`, or reads the staged selection as empty.
- **AC5** — When `SPEC_TIER1_CUTOFF` is blank, AC1's fixture passes; when the fixture spec's
  filename date precedes a declared cutoff, it passes; when the key is set and every tracked spec
  predates it, a full run prints a notice naming `SPEC_TIER1_CUTOFF`.
  Red when: a blank key grades, a grandfathered spec grades, or an armed run grading nothing is
  silent.
- **AC6** — When `gen_build_index.py --new-spec` runs with `--tier 1` in a fixture build, the file
  holds the eight required headings numbered 1 to 8, with the criterion slot under
  `## 5. Acceptance criteria`; with every `FILL_MARKER` slot filled, check 12 reports nothing for
  it; and `--tier 2` output is byte-identical to the base generator's.
  Red when: the Tier-1 skeleton carries readiness rows at §5, or the Tier-2 skeleton moves.
  fixture: the selftest's own template string at `tools/memory-tree/gen_build_index.py:6096`
  carries no Tier-1 fence today, and needs one.
- **AC7** — When `grep -n "SPEC_TIER1_CUTOFF" memory/TEMPLATE-SPEC.md memory/HYGIENE.md` runs, the
  Tier-1 bullet names the eight titles and the cutoff, the Tier-1 skeleton fence holds exactly those
  eight headings, and the check 12 entry names the arm.
  Red when: the template still says no section canon binds Tier-1 at any date.
- **AC8** — When `check-memory-hygiene.sh` runs over this tree with gov's declared
  `SPEC_TIER1_CUTOFF`, it adds no finding on any tracked spec.
  Red when: the declared value is not strictly past every spec filename date on every ref.
  cost: one full engine run, minutes on node a.
  figure: the date is DERIVED at landing by the relation in §4 "Rollout".

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `harness arms (fail branches armed or pinned)` · `kickoff-manifest ratchet` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 AC5 · a fixture tree with the key set, run against the base engine, which passes a header-and-revision-log Tier-1 spec · FLOOR_ASSERTIONS rises by the assertions added

New arm: tools/memory-tree/gen_build_index.py, its --selftest · covers AC6 · a template string carrying both fences, against the base generator, which merges them · none

## 8. Open questions

- **F1 — What does the write gate admit for a Tier-1 spec this arm never graded?** A Tier-1 spec
  dated before `SPEC_TIER1_CUTOFF`, or in a tree whose key is blank, reaches SPECCED with nothing
  checking its sections. Every Tier-1 spec dated before the landing is in that state, one of them
  live today at INPROGRESS, and so is every adopter until it arms the key. Options: (a) admit it
  at SPECCED as D6 reads, accepting a header-and-revision-log spec; (b) admit a Tier-1 spec at
  SPECCED only when the key is set and the spec's filename date is on or after it, and otherwise
  only at INPROGRESS, as a Tier-2 spec is admitted; (c) refuse it outright. Recommendation: (b). It keeps D6 for every spec the arm graded, costs one conf read and
  one string compare, and closes the grandfather window and the blank-key adopter together. The
  decision is `TOOL-aRoutedQuill-2`'s.
  RESOLVED (owner, 2026-10-09): (b). The ruling is recorded at `TOOL-aRoutedQuill-2` F4, where this fork was handed.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §8 · owner resolves F1 as (b), recorded at `TOOL-aRoutedQuill-2` F4.
- rev-3 · 2026-10-09 · build: §4 Inventory names `SPEC_TITLE_NUMBERS`, the generator's
  title-to-body map S5 needs. The S3 arm sits after the terminal §8 arm, still in the every-tier
  band above the Tier-1 cut. The AC1-AC5 arms run in a fixture tree of their own, as the F-item
  shape arms do, so no shared fixture moves. Status CLOSED.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade a Tier-1 spec's required sections by heading text
in the spec format check, and write a Tier-1 spec skeleton"` ranked only generic name tokens
(`read_text`, `check`, `write`), none of them a seam for this. The seams extended are named by
reading instead: check 12's single awk program in `tools/memory-tree/check-memory-hygiene.sh`, whose
every-tier band and title-keyed section reads this arm copies, and `render_spec_skeleton` in
`tools/memory-tree/gen_build_index.py`, which already reads its skeleton from the installed
template.

Recall terms used: `Tier-1 light profile section canon check 12 heading title ordinal THIN
plan_state empty-body cutoff skeleton new-spec` — which surfaced TOOL-dBriefedPass-1,
TOOL-aJoinedCanon-7, TOOL-cSettledDocket-3 and TOOL-aMendedFleet-20.

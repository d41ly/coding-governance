# TOOL-aJoinedCanon-1 — the revision log becomes a structured entry

**Status:** SPECCED · rev-2 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

A §9 revision entry must name what it moved — a section, a scope id or an acceptance id — so a
resumed session can re-read what a fold invalidated. Today the log records that a fold happened and
almost nothing about where, which is the mechanism behind the corpus's dominant defect class.

## 2. Scope (IN)

- **S1** — A `## REV_SCOPE_CUTOFF` section in `tools/memory-tree/SPEC-TEMPLATE.template.md` stating
  the entry grammar: a rev line is `- rev-<N> · <date> · <scope> · <what moved>`, where `<scope>` is
  one or more `§<n>`, `S<n>` or `AC<n>` tokens. It states that the gate reads SHAPE only, and that
  the token may sit anywhere in the entry including a wrapped continuation line.
- **S2** — The §9 skeleton example in the same file stops modelling the uninformative form. Both
  example lines move: `rev-1` keeps `initial draft`, and the `rev-2` example gains a scope field.
- **S3** — A check-12 arm: for a spec whose FILENAME date is at or after `REV_SCOPE_CUTOFF`, every
  §9 entry whose rev number is 2 or greater must carry at least one scope token. The arm is
  per-ENTRY with continuation lines folded in, and it runs on BOTH tiers.
- **S4** — The `REV_SCOPE_CUTOFF` key: preset blank in `check-memory-hygiene.sh` above the conf
  source, bound into the one batched awk as `-v`, guarded by an explicit non-empty test, and
  declared in `.memory-tree.conf` with the evidence for the date chosen.
- **S5** — A zero-population notice on the same footing as the §10 evidence arm's, so an arm that
  grades no spec in this corpus says so instead of printing a silent green.
- **S6** — Fixtures in `check-memory-hygiene.test.sh` covering the red, the pre-cutoff
  grandfather, the rev-1 exemption, the wrapped continuation, and the blank-cutoff off state. The
  red is OBSERVED before the arm lands.
- **S7** — The check-12 paragraph in `tools/memory-tree/HYGIENE.template.md` gains the arm, in the
  two sentences its sibling ratchets each get.
- **S8** — The landing bookkeeping this kit's own gates demand: `KIT_MEMORY_TREE_VERSION` bumped
  and the `gov:kit memory-tree@` marker moved in every carrier, both doc pairs re-rendered from
  their templates, and `memory/guides/SESSION-KICKOFF.md` re-stamped.

## 3. Non-goals (OUT)

- **Trimming, capping or summarising §9.** §9 is load-bearing in four places and this unit
  structures the entry rather than shortening it. Verified at writing time: `memory/HYGIENE.md:299`
  defines the acceptance ledger's `AMENDED` form as naming "the section 9 line that logs it";
  `memory/guides/BUILD-METHOD.md:207` (M7 step 4) has a regrounding session read the current
  sub-spec whole; `tools/drift-audit/drift_report.py:1281-1294` parses §9 entries as the evidence
  side of its build-README mechanism-drift signal; and the findings record's B2 closes by naming
  A5, A4 and B2 itself as resting on §9 lines as their evidence carrier.
- **The two arms `TOOL-dUnstalledConvoy-14` proposes** — that rev numbers in a log are unique and
  that they descend. Same section, same walk, different mechanism, and BUILD-METHOD M2 gives a unit
  one. The entry accumulator S3 builds is what that row needs, so it gets cheaper, not done.
- **Retrofitting the corpus.** No landed spec is edited. Measured below: under the ratified cutoff
  `2026-09-06`, zero landed specs change.
- **The fold procedure's re-read set.** That is `TOOL-aJoinedCanon-2`, and it is the half of B1 that
  edits `memory/guides/BUILD-METHOD.md`. This unit touches no method carrier.
- **Grading truth.** The arm asserts an entry NAMES a section, never that the fold actually touched
  it, exactly as the acceptance-witness arm grades a backticked token and not the thing it names.

## 4. Design

### Data model

The entry grammar, as the template will state it:

```
- rev-<N> · <YYYY-MM-DD> · <scope> · <what moved>
```

`<scope>` is a space- or comma-separated list of `§<n>`, `S<n>` and `AC<n>` tokens. The field sits
AFTER the date and never before it, and that ordering is a constraint rather than a preference:
`drift_report.py:1192` anchors on `^- rev-(\d+)\s*[·|-]\s*(\d{4}-\d{2}-\d{2})`, so a scope field
inserted ahead of the date would silently drop every entry out of that signal's population.

The gate grades presence, not position. That is the same call `SPEC_WITNESS_CUTOFF` recorded in
`.memory-tree.conf`, where four candidate predicates were measured and the loosest one was the only
one that did not punish good criteria. The template prescribes the field; the arm asks for a token.

### The arm

It rides the walk that already exists. `check-memory-hygiene.sh:1066-1078` opens §9 on
`/^## [0-9]+\. Revision log/`, closes on the next `## `, and scans `rev-[0-9]+` for the header-rev
high-water. That loop sits ABOVE the `if (hdr ~ /Tier-1/) next` cut at `:1173` — hoisted by
`TOOL-cSettledDocket-3` so both hoisted assertions grade every tier — so an arm added there is a
both-tiers arm for free, as `STREAMS_CUTOFF` and `SPEC_WITNESS_CUTOFF` are.

Three decisions inside it, each measured over the 476 tracked specs at `base 750ca0ca`:

**Per ENTRY, not per line.** The same scope-token predicate applied per LINE says 594 of 2,016 rev
lines name a token, 29.5% — which reproduces the findings record's 492 of 1,665 exactly. Applied
per ENTRY with continuation lines folded in, it says 1,013 of 1,682, 60.2%. The gap is entirely
wrapping: this corpus writes §9 at its ~100-column house width and puts the detail in the wrap. A
line-oriented arm would red half the corpus that already does the right thing, so the arm reuses
the acceptance-witness accumulator's shape at `:1020-1048` — a head line opens an entry, every
following non-blank line appends to it, and the entry is tested when the next head or the next
`## ` arrives.

**Head selector.** `/^([ \t]*(-|\*)[ \t]*)?(\*\*)?rev-[0-9]+/`, which is the witness arm's selector
with its label swapped. The optional-marker group is what makes an INDENTED continuation line fail
to open a new entry, which is the phantom-bullet defect that arm's own comment records. Measured:
1,683 rev heads in the corpus, 5 of them bolded, none using `*`, and 0 continuation lines that this
selector would misread as a head. Continuations are indented in 8,621 of 8,635 cases, so the arm
folds ANY non-blank line rather than requiring the two-space indent `drift_report.py:1293` requires
— the looser rule reaches 14 more lines and cannot misgrade.

**rev-1 is exempt.** A first draft moved the whole document, so a scope list on it names everything
and says nothing. Measured: rev-2+ entries are 1,194, of which 919 (77.0%) already carry a token;
rev-1 entries are 488, of which 94 (19.3%) do. Grading rev-1 would add 394 failing entries that no
author could usefully answer.

The token test, spelled to survive the awk dialect surface this file's header warns about twice:

```awk
p = index(E, "§")
hasScope = (p > 0 && substr(E, p + length("§"), 1) ~ /[0-9]/) || (E ~ /(^|[^A-Za-z0-9])(S|AC)[0-9]/)
```

The `§` half is `index()` plus `substr()` rather than a regex because the section sign is
multibyte, and `length("§")` is 2 on a byte-oriented awk and 1 on gawk in a UTF-8 locale. `substr`
counts in whatever unit `length` returned in the same interpreter, so the pair is consistent by
construction. Confirmed on node `a`: `awk 'BEGIN{print length("§")}'` prints 2, and the expression
above scores a `§4` line 1, a bare-prose line 0, and an `S2 and AC7` line 1. The ASCII half stays a
regex; it has no dialect surface and no interval expression.

The failure message names the file, the offending rev numbers, and the cutoff — the shape every
sibling arm's message takes, and the reason `check-arms.py`'s pin rows are readable.

### Migration

`REV_SCOPE_CUTOFF` is the sixth dated cutoff in this conf and takes the semantics of the four that
switch a rule on: blank means OFF, the awk guards it with an explicit `!= ""` test, and it does NOT
resolve forward the way `SPEC10_CUTOFF` must. It is preset above the conf source for the reason
`SPEC10_EVIDENCE_CUTOFF`'s comment records — this script runs `set -u` and `adopt-memory-tree.sh`
never back-fills a key into an existing conf, so an unpreset key aborts the gate in every adopter
tree whose conf predates it.

The date is `2026-09-06`, ratified by the owner at §8 F1 as one ruling over this whole build: every
cutoff it introduces sits strictly past the newest spec filename date on any branch. Re-derived at
the fold rather than carried over — across all 44 local and remote refs the newest spec filename
date is 2026-09-04, no spec dated 2026-09-05 exists on any ref or in any of the 15 live worktrees,
and today is 2026-09-05, so today is a date this fleet can still write into and 2026-09-06 is the
first one it cannot. `SPEC10_EVIDENCE_CUTOFF` is the precedent for that correction: measured
2026-08-31, it took 2026-09-01 because sibling branches held specs dated on the measuring day.

### Rollout

Under `REV_SCOPE_CUTOFF="2026-09-06"` the arm grades no spec in this corpus on day one, and the S6
fixtures are its entire coverage. That is the ratified cost rather than a tradeoff still being
weighed, and it is the state `STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF` and `SPEC10_EVIDENCE_CUTOFF`
each shipped in and each recorded. S5 is why it is not a silent green: the notice at `:1298-1305` already exists for the
§10 evidence arm, counts its population by DATE alone over `c12_sel`, and prints one line when the
count is zero. The new notice is that block with two strings changed.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | S1 section, ~14 lines; S2 skeleton, 2 lines |
| `memory/TEMPLATE-SPEC.md` | RENDERED from the above, never hand-edited |
| `tools/memory-tree/HYGIENE.template.md` | S7, 2 sentences in the check-12 entry |
| `memory/HYGIENE.md` | RENDERED |
| `tools/memory-tree/check-memory-hygiene.sh` | preset key, `-v` binding, the arm, the notice |
| `tools/memory-tree/check-memory-hygiene.test.sh` | fixtures 90-95 and their assertions |
| `.memory-tree.conf` | the key and its evidence block |
| `memory/guides/BUILD-METHOD.md` + template | version marker ONLY, no prose |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp |

Both doc pairs are byte-compared after a render substituting `{{KIT_DIR}}` and `{{TOOL_ROOT}}`, by
`kit-dogfood-parity.test.sh`, whose direction is TEMPLATE to LIVE. Editing a live copy by hand is
the red. `git grep -l 'memory-tree@2\.59'` names 7 carriers of the kit version today, six of them
line-1 doc markers and the seventh the constant and marker sharing `check-memory-hygiene.sh:20`.

### Alternatives rejected

- **A positional third field, gated.** Byte-grammar on prose, breaks on the wrap this corpus
  writes at, and inconsistent with every other check-12 arm, all of which grade presence.
- **A count cap on §9.** Directly refused by the findings record's skeptic and out of scope here.
- **Reusing `drift_report.py`'s entry reader.** It exists and it is the closest prior art, but it
  is Python and check 12 is one batched awk; a cross-language artifact for a six-line loop is the
  committed second copy §12 tells you not to build when the consumers cannot share one.
- **A `fail` branch per finding.** Check 12 reports through one `fail 12` and `check-arms.py` scans
  shell `fail` call sites only, so an awk branch is invisible to it. `cTracedPromise-2` deleted its
  own `ARMS_FLOORS` raise for exactly this reason; this unit does not raise the floor either.

## 5. Production-readiness checklist

- security: N/A — the arm reads tracked text already in scope and writes nothing.
- perf / scale: rides the existing §9 walk in the one batched awk, so it adds no pass over the
  corpus and no fork per spec. The `memory hygiene` leg's declared ceiling is 12,720 s and this
  cannot move it measurably.
- a11y: N/A — a shell gate with no user surface.
- i18n: N/A, except that the multibyte `§` is handled by `index`/`substr` rather than a regex.
- error / empty / loading states: the zero-population notice (S5) is the empty state, and it is
  loud by design.
- observability: the failure message names the file, the rev numbers and the cutoff.
- risks (concurrency, data-loss, rollback hazards): the only real hazard was a cutoff that reds
  in-flight branches on merge, and §8's ratified date retires it — `2026-09-06` sits past every spec
  filename date on every ref, so no branch reds on merge. Rollback is blanking one conf key.
- testing + left-shift gates: S6, with the red observed before landing per the build's own rule.
- migration / rollback: dated cutoff, blank means off, no corpus edit.
- user docs: the template and `HYGIENE.md` are where an author reads this; both are in scope.

## 6. Acceptance criteria

- **AC1** When fixture `2026-09-06-spec-tFixture-90.md` carries a rev-2 entry naming no section,
  scope id or acceptance id, `bash tools/memory-tree/check-memory-hygiene.sh` reds and its check-12
  output names that file and its rev number. The red is staged, confirmed and unstaged BEFORE the
  arm lands.
- **AC2** When the same entry gains a `§4` token, `tFixture-91.md` is silent.
- **AC3** When a fixture dated before `REV_SCOPE_CUTOFF` carries the identical unnamed entry,
  `tFixture-92.md` is silent and the grandfather holds.
- **AC4** When a post-cutoff fixture's only entry is `- rev-1 · <date> · initial draft.`,
  `tFixture-93.md` is silent.
- **AC5** When a post-cutoff entry's scope token sits on a wrapped continuation line rather than the
  head line, `tFixture-94.md` is silent — the accumulator folds it.
- **AC6** When `.memory-tree.conf` declares `REV_SCOPE_CUTOFF=""`, the blank-cutoff run in
  `check-memory-hygiene.test.sh` emits no `revision entries naming no` finding at all.
- **AC7** When `bash tools/memory-tree/check-memory-hygiene.sh` runs over this tree at the landing
  sha, it exits 0 — no landed spec is redded by the new arm.
- **AC8** When both halves of each doc pair have moved,
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0, and it exits 1 if only one half did.
- **AC9** When `KIT_MEMORY_TREE_VERSION` is bumped in the same range as the engine edit,
  `bash tools/memory-tree/check-verdict-epoch.sh` exits 0.
- **AC10** When the arm has landed, `python tools/memory-tree/check-arms.py --check` exits 0 with
  `ARMS_FLOORS` unchanged, because no shell `fail` call site was added.
- **AC11** When `memory/guides/SESSION-KICKOFF.md` has been re-stamped for the watched files this
  unit edits, `bash skills/session-kickoff/manifest-check.sh` exits 0.

## 7. Gates

The named legs from `tools/gate-legs.json` this unit must keep green: `memory hygiene`,
`kit/dogfood doc parity`, `verdict epoch (kit version dates the engine)`, `harness arms (fail
branches armed or pinned)`, and `kickoff-manifest ratchet`.

This is KIT work, so the DoD also owes the self-test chunk that the bar holds by default:
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, whose relevant leg is
`memory-hygiene self-test` (`subject: kit`, guard `tools/memory-tree/`).

No new gate leg is added. The arm lives inside check 12, which `tools/gate-legs.json` already
carries, so the manifest does not move.

## 8. Open questions

- **F1 · What date does `REV_SCOPE_CUTOFF` take?** This conf holds two live precedents pointing
  opposite ways, and the choice is a merge-bar knob rather than an implementation detail.
  - **Ahead of the fleet (2026-09-05).** The idiom `STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF` and
    `SPEC10_EVIDENCE_CUTOFF` each record: strictly ahead of every committed spec on every branch,
    so nothing landed and nothing in flight is retroactively red. Cost: the arm grades zero specs
    on day one and the fixtures are its whole coverage.
  - **This build's own date (2026-09-04).** `ACCEPTANCE_LEDGER_CUTOFF`'s precedent, taken so the
    check ships having been exercised on real units rather than on an empty set. Cost, measured
    across every local and remote ref: 2 of the 50 distinct spec versions dated on or after
    2026-09-04 carry a rev-2+ entry naming nothing, both on
    `branch/agent-orientation-tooling-research-5dad25`, and both would red that branch's bar on
    merge. It would also pull this build's own eleven specs into the population, so any fold during
    this build would owe a scope field.
  - **Recommendation: 2026-09-05.** The two in-flight specs belong to another run, and this repo's
    own rule is that a gate must not red honest content written before the rule existed. The
    dogfooding argument is weaker here than it was for the acceptance ledger, because that build
    could back-fill its OWN units and this one cannot back-fill another node's branch.
  - RESOLVED (owner, 2026-09-05): ahead of the fleet, ruled across the whole build at once — every
    cutoff this build introduces sits strictly past the newest spec filename date on any branch, so
    nothing landed and nothing in flight goes red. `REV_SCOPE_CUTOFF="2026-09-06"`. The date is
    RE-DERIVED and not the one the option above names: that bullet was written on 2026-09-04, when
    2026-09-05 was tomorrow, and today is 2026-09-05, so it is now the fleet's own working date
    rather than a date ahead of it. Measured at the fold across all 44 local and remote refs — newest
    spec filename date 2026-09-04, no spec dated 2026-09-05 on any ref or in any of the 15 live
    worktrees — 2026-09-06 is the first date this fleet can no longer write into.
    `SPEC10_EVIDENCE_CUTOFF` is the precedent for the same correction. The accepted cost is now a
    fact rather than a tradeoff: the arm grades zero specs on day one, and its S6 fixtures are its
    entire coverage.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8, §3, §4, §5, §6 · folded the owner's ruling on F1: the cutoff takes the
  ahead-of-the-fleet branch, re-derived to `2026-09-06` because 2026-09-05 is now the fleet's own
  working date. §4's Migration and Rollout, §3's retrofit non-goal and §5's risk row state the date
  and its zero-population cost as fact rather than as a pending choice, and AC1's fixture filename
  moved from 2026-09-05 to 2026-09-06 so the observed red is still reachable under the new cutoff.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade every bullet in a spec section and fold its
wrapped continuation lines into the entry before testing it"` returns no seam for this behaviour,
and the reason is a property of the index rather than of the tree: the lookup ranks Python and
shell SYMBOLS plus inventory keys, and the accumulator this unit extends is an unnamed awk block
inside a shell script, so it is unreachable by that instrument. Read directly, the seam is real and
is named in §4: the acceptance-witness accumulator at `check-memory-hygiene.sh:1020-1048` supplies
the head-selector and continuation-fold shape, and the §9 range walk at `:1066-1078` supplies the
section extraction, so the arm adds no new pass. A second, non-shareable prior art exists at
`tools/drift-audit/drift_report.py:1281-1294`, which folds §9 continuations in Python for the
mechanism-drift signal; it constrains this unit's grammar rather than being extended by it.

Recall terms used: `python tools/memory-recall/query.py "why does the spec revision log stay
unstructured and what dated cutoff would a new check 12 arm need" --terms "revision log rev line
dated cutoff check 12 grandfather corpus spec format ratchet awk arm continuation line"`. The hit
that changed this spec was `TOOL-dUnstalledConvoy-14`, the OPEN backlog row proposing two further
§9 arms, which §3 names as a non-goal this unit makes cheaper.

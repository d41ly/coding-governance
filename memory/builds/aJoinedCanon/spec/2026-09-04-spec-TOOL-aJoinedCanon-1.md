# TOOL-aJoinedCanon-1 — the revision log becomes a structured entry

**Status:** SPECCED · rev-6 · 2026-09-06 · node a · Tier-2 · base 750ca0ca · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md) | spec-audit | TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

A §9 revision entry must name what it moved — a section, a scope id or an acceptance id — so a
resumed session can re-read what a fold invalidated. Today the log records that a fold happened and
almost nothing about where, which is the mechanism behind the corpus's dominant defect class.

## 2. Scope (IN)

- **S1** — A `## REV_SCOPE_CUTOFF` section in `tools/memory-tree/SPEC-TEMPLATE.template.md` stating
  the entry grammar: a rev line is `- rev-<N> · <date> · <scope> · <what moved>`, where `<scope>` is
  one or more `§<n>`, `S<n>` or `AC<n>` tokens, separated by spaces, commas or the `·` this corpus
  already writes its status fields with. It states that the gate reads SHAPE only, and that the
  token may sit anywhere in the entry including a wrapped continuation line. Observed by AC14.
- **S2** — The §9 skeleton example in the same file stops modelling the uninformative form. Both
  example lines move: `rev-1` keeps `initial draft`, and the `rev-2` example gains a scope field.
  Observed by AC14.
- **S3** — A check-12 arm: for a spec whose FILENAME date is at or after `REV_SCOPE_CUTOFF`, every
  §9 entry whose rev number is 2 or greater must carry at least one scope token. The arm is
  per-ENTRY with continuation lines folded in, it runs on BOTH tiers, and `REV_SCOPE_CUTOFF` is its
  ONLY date guard — it does not nest inside another cutoff's block. Observed by AC1–AC5 for the
  behaviour and by AC15 for the independence.
- **S4** — The `REV_SCOPE_CUTOFF` key in all THREE of its carriers: preset blank in
  `check-memory-hygiene.sh` above the conf source, bound into the one batched awk as
  `-v revscopecut="$REV_SCOPE_CUTOFF"` and guarded by an explicit non-empty test; declared in
  `.memory-tree.conf` with the evidence for the date chosen; and shipped blank in
  `tools/memory-tree/.memory-tree.conf.example`. §4's Migration says why the third carrier is not
  bookkeeping, and §4's "The binding" says why the awk name is spelled out in full and where this
  unit claims it. Observed by AC13 for the shipped example ONLY; the preset and the `-v` binding
  are observed by AC1 and AC6, which are what make the arm fire under a valued key and fall silent
  under a blank one, and an unpreset key aborts the gate before any criterion runs at all; AC16
  observes that the name is this unit's alone on that invocation.
- **S5** — A zero-population notice on the same footing as the §10 evidence arm's, so an arm that
  grades no spec in this corpus says so instead of printing a silent green. Observed by AC12.
- **S6** — Fixtures in `check-memory-hygiene.test.sh` covering the red, the pre-cutoff
  grandfather, the rev-1 exemption, the wrapped continuation, and the blank-cutoff off state. The
  red is OBSERVED before the arm lands. They take `tFixture-90` upward, which is not a free-block
  claim measured against the file's high-water but the block the build README's number-space rule
  allocates to this unit by `order` — `80 + 10N`, N = 1 — so a sibling landing later cannot collide
  with it whatever the file looks like by then. This unit's whole claim is 90 through 95. Observed
  by AC1–AC6.
- **S7** — The check-12 paragraph in `tools/memory-tree/HYGIENE.template.md` gains the arm, in the
  two sentences its sibling ratchets each get. Observed by AC14.
- **S8** — The landing bookkeeping this kit's own gates demand: `KIT_MEMORY_TREE_VERSION` bumped
  and the `gov:kit memory-tree@` marker moved in every carrier, both doc pairs re-rendered from
  their templates, and `memory/guides/SESSION-KICKOFF.md` re-stamped. Observed by AC9 for the
  version bump, AC8 for the re-render, and AC11 for the re-stamp.

## 3. Non-goals (OUT)

- **Trimming, capping or summarising §9.** §9 is load-bearing in four places and this unit
  structures the entry rather than shortening it. Re-verified at this fold, and cited by source text
  rather than by line because three of these four files are in this build's shared write set:
  `memory/HYGIENE.md`'s acceptance-ledger skeleton defines the `AMENDED` form as the line
  `- AC2 — amended rev-<n> — the change, and the section 9 line that logs it`;
  `memory/guides/BUILD-METHOD.md` M7's step `4. The CURRENT sub-spec, whole` has a regrounding
  session read it; `_REVLOG_RE` and the entry loop beneath it in `tools/drift-audit/drift_report.py`
  parse §9 entries as the evidence side of its build-README mechanism-drift signal; and the findings
  record's B2 closes by naming A5, A4 and B2 itself as resting on §9 lines as their evidence
  carrier. Three of those four anchors were cited by line at rev-3 and two of the three numbers were
  wrong — `:1173` for a cut at 1172, `:299` for the ledger's OBSERVED form when `AMENDED` is the
  line below it, and `:207` labelled "M7 step 4" when 207 is step 3 — which is why none of them is a
  number any more.
- **The two arms `TOOL-dUnstalledConvoy-14` proposes** — that rev numbers in a log are unique and
  that they descend. Same section, same walk, different mechanism, and BUILD-METHOD M2 gives a unit
  one. The entry accumulator S3 builds is what that row needs, so it gets cheaper, not done.
  Round 3 supplied the reachability evidence that row was missing — a sibling spec's §9 with rev-4
  spliced into rev-2 and logged before rev-3, ungated because check 12 compares only the maximum
  `rev-[0-9]+` it sees — and the audit's left-shift proposes bolting the assertion onto this unit.
  It stays out, and this is the disposition rather than a deferral: that evidence belongs on
  `TOOL-dUnstalledConvoy-14`, the OPEN backlog row that already owns the proposal and now has a
  live instance to cite. Adding it here would make this unit two mechanisms in the round that has
  no further audit to catch the second one.
- **Retrofitting the corpus.** No landed spec is edited. Measured below: under the ratified cutoff
  `2026-09-07`, zero landed specs change.
- **The fold procedure's re-read set.** That is `TOOL-aJoinedCanon-2`, and it is the half of B1 that
  edits `memory/guides/BUILD-METHOD.md`. This unit writes no method PROSE — it touches that pair
  only for the kit-version marker, which §4's Files-touched table declares and which the parity test
  compares as one of its three pairs.
- **Grading truth.** The arm asserts an entry NAMES a section, never that the fold actually touched
  it, exactly as the acceptance-witness arm grades a backticked token and not the thing it names.

## 4. Design

### Data model

The entry grammar, as the template will state it:

```
- rev-<N> · <YYYY-MM-DD> · <scope> · <what moved>
```

`<scope>` is a list of `§<n>`, `S<n>` and `AC<n>` tokens separated by spaces, commas or the `·` this
corpus already uses between status fields — the arm reads presence, so the separator is house style
rather than grammar, and stating all three is what keeps this document legal under its own rule.
The field sits AFTER the date and never before it, and that ordering is a constraint rather than a
preference: `drift_report.py`'s `_REVLOG_RE` anchors on `^- rev-(\d+)\s*[·|-]\s*(\d{4}-\d{2}-\d{2})`,
so a scope field inserted ahead of the date would silently drop every entry out of that signal's
population.

The gate grades presence, not position. That is the same call `SPEC_WITNESS_CUTOFF` recorded in
`.memory-tree.conf`, where four candidate predicates were measured and the loosest one was the only
one that did not punish good criteria. The template prescribes the field; the arm asks for a token.

### The arm

It rides the walk that already exists: in `check-memory-hygiene.sh`, the loop opening on
`if (L ~ /^## [0-9]+\. Revision log/) in9 = 1`, closing on the next `## `, and scanning
`while (match(L, /rev-[0-9]+/))` for the header-rev high-water that ends in
`print f " (header rev-" hrev " not logged in the §9 Revision log)"`.

**Where it sits, stated as an exclusion.** That walk is ALREADY outside every cutoff guard — the
comment above it says so in the engine's own words, `these two run for EVERY TIER, so they sit ABOVE
the Tier-1 cut` — and this arm goes in it, at the same nesting depth, guarded by
`revscopecut != ""` and by nothing else. It does NOT go inside the `if (wcut != "" && fdate != "" && fdate >= wcut) {` block
that ends in `print f " (acceptance bullets naming no backticked witness…`. That is a live trap and
not a hypothetical one: this build's round-1 blocker and its round-2 blocker are both a new arm
nested in that guard, whose real population becomes the INTERSECTION of two cutoffs while its own
key reads as armed. Here the intersection would be invisible in this repo — `SPEC_WITNESS_CUTOFF` is
`2026-08-15` and `REV_SCOPE_CUTOFF` is `2026-09-07`, so every spec reaching the second passes the
first — and visible only in an adopter that arms one key and not the other, which is the case with
no local witness. AC15 is that witness. Being outside the `if (hdr ~ /Tier-1/) next` cut also makes
it a both-tiers arm for free, as `STREAMS_CUTOFF` and `SPEC_WITNESS_CUTOFF` are.

**The binding, and who owns the name.** The key rides in on `-v revscopecut="$REV_SCOPE_CUTOFF"`,
appended to the single check-12 invocation that today opens
`awk -F'\t' -v canon="$SPEC_CANON" -v canon10="$SPEC_CANON10" -v cut10="$SPEC10_CUTOFF" -v mroot="$M"`
and continues `-v discalt -v scut -v wcut -v fcut -v ecut`. Verified at HEAD: that is one `awk`
program, so every `-v` on it shares ONE variable namespace and a repeated name is last-wins for the
whole program, silently.

The name is spelled out rather than abbreviated, and that is the whole point of it. Round 3's
blocker was this unit and `TOOL-aJoinedCanon-4` both taking `mcut` on this invocation, for two
different cutoff keys — invisible locally, because in this repo both keys hold `2026-09-07`, and
invisible to both specs' criteria, because each blanks its own key and thereby blanks the shared
binding and turns BOTH arms off. The mechanism was not bad luck: several units of this build each
need a cutoff binding on this one invocation, the engine's live names there are `scut`, `wcut`,
`fcut`, `ecut` and `cut10`, and an `<initial>cut` space that small, with that many claimants,
collides by construction. The audit's Fix offered `rvcut`, which is free; this fold declines the
abbreviation and not the fix, because `rvcut` sits one letter from the `rcut` that same Fix records
as already spoken for, and so reproduces the shape that caused the blocker. `revscopecut` is
derived from `REV_SCOPE_CUTOFF` letter for letter and cannot be
confused with a sibling's. Confirmed on node `a`: zero hits for `revscopecut` anywhere in the tree,
and `awk -v revscopecut=…` binds and reads it.

**Claimed, so a sibling can see it.** This unit claims `revscopecut` on the check-12 awk for the
whole build, per the build README's one-owner-per-shared-engine-name rule. `TOOL-aJoinedCanon-3` §4
carries this build's namespace register — the paragraph whose opening words are "The binding is
named", cited by that text and not by line — and that paragraph is where the taken list lives, so
this spec states its OWN claim and does not restate the others: a copy of a four-name list beside
the register that owns it is the paraphrase class this repo refuses, and it would already be stale,
because `TOOL-aJoinedCanon-4` renamed its own binding in this same round. Round 3's proof that
nobody looked is that the register named unit 4 as the sole claimant of `mcut` while this unit,
three `order` steps EARLIER, was taking it too. AC16 is the observation, and it is mechanical
rather than a reading:
no name may be bound twice on that invocation. It costs one assertion in the self-test and it reds
at the commit that introduces a duplicate rather than in an adopter's tree, which is where the
collision was otherwise going to be found.

Three decisions inside it, each measured at `base 750ca0ca` over the 476 date-named specs there —
which is the population check 12's selector grades, and is the 479 files under `spec/` less the
three whose filenames carry no date.

**Per ENTRY, not per line.** The same scope-token predicate applied per LINE marks about 30% of §9's
lines, which is the rate the findings record measured at 29.5% (492 of 1,665) on a smaller corpus.
Applied per ENTRY with continuation lines folded in, it marks about 60%. The gap is entirely
wrapping: this corpus writes §9 at its ~100-column house width and puts the detail in the wrap. A
line-oriented arm would red half the corpus that already does the right thing, so the arm reuses the
shape of the acceptance-witness accumulator — the block whose head selector is
`/^([ \t]*(-|\*)[ \t]*)?(\*\*)?AC[0-9]+[a-z]?(\*\*)?([^A-Za-z0-9]|$)/` and whose fold is
`if (lab != "") acc = acc " " L` — where a head line opens an entry, every following non-blank line
appends to it, and the entry is tested when the next head or the next `## ` arrives. That block is
cited by its own source text and not by line because `TOOL-aJoinedCanon-4` unindents it out of the
`wcut` guard at `order` 4; this unit is `order` 1 and builds against the nested form, and the shape
it borrows survives that unindent either way.

The rates above are stated as rates on purpose. A Python transcription of the same predicate,
re-run at this fold over the same base, returns 1,028 of 1,682 entries and 934 of 1,194 rev-2+
entries where rev-3 recorded 1,013 and 919 — a spread of about 1.1 points that is a property of the
transcription, not of the corpus, since the arm's awk is the only authority and does not exist yet.
The load-bearing figure is the 2× gap between line and entry granularity, which both derivations
agree on; the exact counts are re-derived by the arm itself at build time.

**Head selector.** `/^([ \t]*(-|\*)[ \t]*)?(\*\*)?rev-[0-9]+/`, which is the witness arm's selector
with its label swapped. The optional-marker group is what makes an INDENTED continuation line fail
to open a new entry, which is the phantom-bullet defect that arm's own comment records. Measured at
base: 1,682 rev heads in the corpus — one per entry, which is what makes the head count and the
entry count the same number — a handful of them bolded, none using `*`, and 0 continuation lines
that this selector would misread as a head. Continuations are indented in 8,621 of 8,635 cases, so
the arm folds ANY non-blank line rather than requiring the two-space indent that
`drift_report.py`'s `elif revs and revs[-1][0] == sp and ln.startswith("  ")` guard requires — the
looser rule reaches 14 more lines and cannot misgrade.

**rev-1 is exempt.** A first draft moved the whole document, so a scope list on it names everything
and says nothing. Measured at base: rev-2+ entries are 1,194, of which roughly 78% already carry a
token; rev-1 entries are 488, of which 94 do. Grading rev-1 would add 394 failing entries that no
author could usefully answer, and that subtraction is exact because both of its terms are counts of
entries rather than of matches.

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

`REV_SCOPE_CUTOFF` is another dated cutoff in this conf and takes the semantics of the ones that
switch a rule on: blank means OFF, the awk guards it with an explicit `!= ""` test, and it does NOT
resolve forward the way `SPEC10_CUTOFF` must. It is preset above the conf source for the reason
`SPEC10_EVIDENCE_CUTOFF`'s comment records — this script runs `set -u` and `adopt-memory-tree.sh`
never back-fills a key into an existing conf, so an unpreset key aborts the gate in every adopter
tree whose conf predates it.

The third carrier, `tools/memory-tree/.memory-tree.conf.example`, follows from the same adopter
argument and is not bookkeeping. The parity arm in `check-memory-hygiene.test.sh` derives every
`*_CUTOFF` preset out of the comment-stripped engine, unions it with the `${NAME:-}` read form,
exempts two keys by name, and reds naming any remainder the shipped example does not declare —
because an adopter cannot discover a key that never reaches it. Every engine preset is declared
there today, and that arm's own comment records this hole swallowing `FORK_MARK_CUTOFF` and
`REVIEW_VERDICT_CUTOFF` once already. Omitting the line would red `memory-hygiene self-test` — a leg
§7 already owes — on this unit's own landing commit, for a reason with nothing to do with the arm
being built.

The date is `2026-09-07`, ratified by the owner at §8 F1 as one ruling over this whole build: every
cutoff it introduces sits strictly past the newest spec filename date on any branch. Re-derived at
the fold rather than carried over — across all 44 local and remote refs the newest spec filename
date is 2026-09-04, no spec dated 2026-09-05 exists on any ref or in any of the 15 live worktrees,
and today is 2026-09-05, so today is a date this fleet can still write into and 2026-09-07 is the
first one it cannot. `SPEC10_EVIDENCE_CUTOFF` is the precedent for that correction: measured
2026-08-31, it took 2026-09-01 because sibling branches held specs dated on the measuring day.

**Re-derived again at BUILD time, which is what "re-derived rather than carried over" obliges.** The
paragraph above measured on 2026-09-05 and is left standing as the record of that measurement. Today
is 2026-09-06: specs dated 2026-09-05 now exist on `main` and on eight other live branches, so the
newest spec filename date on any ref has moved a day, and today is again a date this fleet can still
write into — two unattended runs are live in it. Applying the ratified rule to today's measurement
gives `2026-09-07`, and that is the value every carrier below carries. The date moved because the
rule is a relation to the fleet's working day and not a constant; a value carried over from the fold
would have armed the arm against a sibling branch landing a spec today.

### Rollout

Under `REV_SCOPE_CUTOFF="2026-09-07"` the arm grades no spec in this corpus on day one, and the S6
fixtures are its entire coverage. That is the ratified cost rather than a tradeoff still being
weighed, and it is the state `STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF` and `SPEC10_EVIDENCE_CUTOFF`
each shipped in and each recorded. S5 is why it is not a silent green: the notice already exists for
the §10 evidence arm, as the block opening
`if [ "$STAGED" = 0 ] && [ -n "$SPEC10_EVIDENCE_CUTOFF" ]; then` and ending in the echo beginning
`memory-hygiene: the §10 reuse-evidence arm graded NO spec`. It counts its population by DATE alone
over `c12_sel` and prints one line when the count is zero. The new notice is that block with two
strings changed.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | S1 section, ~14 lines; S2 skeleton, 2 lines |
| `memory/TEMPLATE-SPEC.md` | RENDERED from the above, never hand-edited |
| `tools/memory-tree/HYGIENE.template.md` | S7, 2 sentences in the check-12 entry |
| `memory/HYGIENE.md` | RENDERED |
| `tools/memory-tree/check-memory-hygiene.sh` | preset key, the `-v revscopecut=` binding, the arm, the notice |
| `tools/memory-tree/check-memory-hygiene.test.sh` | fixtures 90-95, their assertions, and AC16's duplicate-binding assertion |
| `.memory-tree.conf` | the key and its evidence block |
| `tools/memory-tree/.memory-tree.conf.example` | the same key, blank |
| `tools/memory-tree/BUILD-METHOD.template.md` | version marker ONLY, no prose |
| `memory/guides/BUILD-METHOD.md` | RENDERED from the above; marker only |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp |

Every doc pair is byte-compared after a render substituting `{{KIT_DIR}}` and `{{TOOL_ROOT}}`, by
`kit-dogfood-parity.test.sh`, whose direction is TEMPLATE to LIVE and whose `PAIRS` list carries
three of them — `HYGIENE.md`, `TEMPLATE-SPEC.md` and `guides/BUILD-METHOD.md` — so the version-marker
row in the table above is a pair edit like the other two. Editing a live copy by hand is the red.

The kit-version carrier set is DERIVED at build time by
`git grep -l 'memory-tree@<the version being replaced>' -- ':!memory/builds'`, and no count of it is
written here. Two reasons, both learned: build records quoting the old version string match that
grep without being carriers, so the unscoped form already returns one more hit than rev-3 claimed;
and the marker's own line in the engine, `KIT_MEMORY_TREE_VERSION=2.59   # gov:kit memory-tree@2.59`,
is a carrier twice over — the constant and the marker share it — which is the thing a count hides
and the reason `check-verdict-epoch.sh`'s remediation message under-names its own remedy.

**Baseline for AC14, measured at this fold, before any of these files move.** In
`memory/TEMPLATE-SPEC.md`: `grep -cF '<scope>'` is 0 and `grep -cF 'REV_SCOPE_CUTOFF'` is 0, while
`grep -cF 'rev-<N>'` is already 2 (the status-header field and the bump rule), which is why AC14
greps for the scope field and not for the rev token. The §9 skeleton's second line today is the
`rev-2` example whose reason reads `folded review wf_<id> corrections.` and whose trailing HTML
comment marks it as the example shape; it carries no `§`. In `memory/HYGIENE.md`:
`grep -cF 'REV_SCOPE_CUTOFF'` is 0. Every one of those is a count AC14 requires to have RISEN, which
is what makes it a content check rather than a sameness check. That skeleton line cannot be quoted
whole in this spec, because check 12 reds any spec body containing the date placeholder it carries —
a small, real constraint on how a spec discusses the template it edits.

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
  corpus and no fork per spec. `tools/gate-legs.json` owns the `memory hygiene` leg's ceiling and
  declared 12,720 s at this fold; a walk that adds no pass cannot move it measurably.
- a11y: N/A — a shell gate with no user surface.
- i18n: N/A, except that the multibyte `§` is handled by `index`/`substr` rather than a regex.
- error / empty / loading states: the zero-population notice (S5) is the empty state, and it is
  loud by design.
- observability: the failure message names the file, the rev numbers and the cutoff.
- risks (concurrency, data-loss, rollback hazards): the only real hazard was a cutoff that reds
  in-flight branches on merge, and §8's ratified date retires it — `2026-09-07` sits past every spec
  filename date on every ref, so no branch reds on merge. Rollback is blanking one conf key.
- testing + left-shift gates: S6, with the red observed before landing per the build's own rule.
  AC15 is the second observed red and it costs no fixture — it rides the self-test's existing
  blank-`SPEC_WITNESS_CUTOFF` run over the same fixture tree. AC16 is the third and also costs no
  fixture: it reads the engine's own awk invocation, and its red is staged by duplicating one `-v`
  name. AC9's two reds are the fourth and fifth.
- migration / rollback: dated cutoff, blank means off, no corpus edit.
- user docs: the template and `HYGIENE.md` are where an author reads this; both are in scope, and
  AC14 grades what they SAY rather than only that both halves of each pair moved together. No gate
  leg greps template prose, so AC14 is a documented manual check and §7 records it as one.

## 6. Acceptance criteria

- **AC1** When fixture `2026-09-07-spec-tFixture-90.md` carries a rev-2 entry naming no section,
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
  sha, it exits 0. Read honestly: under `REV_SCOPE_CUTOFF="2026-09-07"` the arm grades no spec, so
  this criterion CANNOT go red for the reason "a landed spec was redded by the new arm" — no such
  spec exists to red. What it does observe is that the engine edit broke nothing ELSE in check 12,
  which is a real failure mode and the one the `-v` binding and the awk dialect surface actually
  threaten. The corpus-truth half is AC12's lowered run, not this line.
- **AC8** When both halves of each doc pair have moved,
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0, and it exits 1 if only one half did.
  This is a SAMENESS check and nothing more: it compares a render of the template against the live
  copy and has no opinion about what either says. AC14 is the criterion that reads the content.
- **AC9** When `KIT_MEMORY_TREE_VERSION` is bumped in the same range as the engine edit AND every
  `gov:kit memory-tree@` carrier has moved with it, `bash tools/memory-tree/check-verdict-epoch.sh`
  and `bash tools/check-kit-versions.sh` both exit 0. Two legs, two failure modes, two reds staged
  and observed SEPARATELY, because neither leg catches the other's: revert the constant alone and
  `verdict epoch` reds, since its rule is topological and the bump must be at or after the commit
  that last moved a behaviour-bearing line; move one carrier and leave the rest and `kit version
  markers` reds, since `tools/check-kit-versions.sh` enumerates
  `git ls-files 'tools/memory-tree/*.template.md'` and reds any member whose marker disagrees with
  the constant — while `verdict epoch` stays green throughout, an advanced constant with a stale
  marker satisfying it exactly. S8 demands the carrier sweep and §4 warns the carrier set is easy
  to undercount, so the leg that grades the sweep is named here rather than assumed. Confirmed on
  node `a` that `tools/check-kit-versions.sh` is tracked and exits 0 at this fold's tree.
- **AC10** When the arm has landed, `python tools/memory-tree/check-arms.py --check` exits 0 with
  `ARMS_FLOORS` unchanged, because no shell `fail` call site was added.
- **AC11** When `memory/guides/SESSION-KICKOFF.md` has been re-stamped for the watched files this
  unit edits, `bash skills/session-kickoff/manifest-check.sh` exits 0.
- **AC12** When no tracked spec's filename date reaches `REV_SCOPE_CUTOFF`, a full
  `bash tools/memory-tree/check-memory-hygiene.sh` run prints the zero-population line naming
  `REV_SCOPE_CUTOFF` on stdout, and still exits 0 — the notice is stdout, not a verdict, so AC7
  holds beside it. The run must not be `--staged`: the §10 evidence notice this one copies is inside
  an `[ "$STAGED" = 0 ]` block and a staged run would report the absence of a notice that was never
  reachable. When the cutoff is temporarily lowered to `2026-01-01`, a date the whole corpus
  reaches, the line is absent AND the run names untagged rev-2+ entries in the LOW HUNDREDS — the
  fold's own re-derivation predicts about 260 of 1,194 — rather than zero, which would mean the arm
  never fired, or thousands, which would mean it is grading per line. That lowered run is this arm's
  only observation against real specs and the reason the lowering happens at all rather than being a
  formality. The lowering is reverted before the commit.
- **AC13** When `grep -qE '^REV_SCOPE_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` succeeds
  and `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0, the key has reached the shipped
  example. Deleting that one line and re-running the self-test reds naming `REV_SCOPE_CUTOFF`, which
  is the failing case observed before the landing commit.
- **AC14** When the render has run, the AUTHOR-FACING text exists and says the thing, measured
  against the baseline §4's Files-touched records: `grep -cF '<scope>' memory/TEMPLATE-SPEC.md` and
  `grep -cF 'REV_SCOPE_CUTOFF' memory/TEMPLATE-SPEC.md` each rise from 0 to at least 1;
  `grep -cF 'REV_SCOPE_CUTOFF' memory/HYGIENE.md` rises from 0 to at least 1; and the §9 skeleton's
  `rev-2` example line in `memory/TEMPLATE-SPEC.md` contains a `§`, where today it does not. Red
  when: S1, S2 or S7 ships as a heading with no body, or as a body that never names the key — every
  one of which passes AC8, because AC8 compares two files to each other and neither of them to the
  grammar this unit exists to publish. This is a manual check by construction (§7 records the
  exemption), and its failing case is observed by running the four greps BEFORE the render, where
  all four return 0.
- **AC15** When `SPEC_WITNESS_CUTOFF` is blank and `REV_SCOPE_CUTOFF` is valued, the self-test's
  existing disabled-when-blank run — the one already asserting `no backticked witness` does not fire
  — ALSO shows the rev-scope finding still firing on `tFixture-90`. Red when: the arm is nested
  inside the `wcut` guard, in which case blanking the unrelated key silently disarms this one while
  its own key still reads as armed. No new fixture: the run and the fixture tree both exist, and
  this is one assertion added beside the three already there.
- **AC16** When `check-memory-hygiene.test.sh` extracts the check-12 awk invocation from
  `check-memory-hygiene.sh` — the line carrying the literal `bad12_raw=$(printf`, cited by that
  text because sibling units edit this engine at a lower `order` — and runs
  `grep -o -- ' -v [a-z0-9]*=' | sort | uniq -d` over it, the output is EMPTY: no name is bound
  twice on the one invocation that all five of this build's cutoff arms share. Red when: two units
  bind the same `-v` name, which is round 3's blocker and is last-wins for the whole awk program,
  so one arm answers to the other's key while its own conf key reads as armed. The red is staged
  and observed before landing by duplicating one existing `-v` name in a scratch copy. Confirmed on
  node `a` at this fold: the predicate over the real line prints nothing, and the same line with
  ` -v wcut=` duplicated prints ` -v wcut=`, so the check both passes on the tree and can actually
  fire. **Liveness:** if the locator matches no line, or more than one, the assertion REFUSES and
  says so rather than reporting zero duplicates — the `-v` list is one physical line today, and a
  later unit wrapping it would otherwise turn this into a check that passes because it looked at
  nothing. Read honestly about its reach: at this unit's own landing only `revscopecut` is new, so
  the criterion cannot go red for a real collision until a later `order` lands a second binding on
  this invocation — and whichever name that turns out to be is the register's business, not this
  criterion's, because the predicate reads the invocation and names nothing. Its value is that
  it reds at THAT commit rather than in an adopter's tree, and the staged duplicate is what proves
  it will.

## 7. Gates

The named legs from `tools/gate-legs.json` this unit must keep green: `memory hygiene`,
`kit/dogfood doc parity`, `verdict epoch (kit version dates the engine)`, `kit version markers`,
`harness arms (fail branches armed or pinned)`, `spec tokens (a spec's own names resolve)`, and
`kickoff-manifest ratchet`.

`spec tokens (a spec's own names resolve)` is here because this section just became a longer list
of leg names, and that leg is `subject: repo` with no guard — it runs on every bar and grades the
backticked names in this document, so a leg name typed wrong in the line above reds this unit's own
landing commit. Found by sweeping H3's class rather than by a finding of its own.

`kit version markers` is `bash tools/check-kit-versions.sh`, unguarded, and it is the OTHER half of
S8's version obligation: the constant and every `gov:kit memory-tree@` carrier move together. It was
missing from this list while S8 demanded the marker moved in every carrier and §4 spent a paragraph
on how easily that set is undercounted — `verdict epoch` cannot cover the gap, because an advanced
constant with a stale marker satisfies the epoch rule exactly. The leg's population is whatever
`git ls-files 'tools/memory-tree/*.template.md'` returns at build time, no count of it is written
here, and every member of it appears in §4's Files-touched table — which is what makes this leg
owed rather than incidental. Observed by AC9, which now runs both scripts and names the two staged
reds separately.

This is KIT work, so the DoD also owes the self-test chunk that the bar holds by default:
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, whose relevant leg is
`memory-hygiene self-test` (`subject: kit`, guard `tools/memory-tree/`). That leg is also the home
of the example-conf parity arm §4's Migration describes, so it is the leg AC13 observes as well as
the one carrying S6's fixtures.

No new gate leg is added. The arm lives inside check 12, which `tools/gate-legs.json` already
carries, so the manifest does not move.

**One deliberate gate exemption, with its compensating check named beside it** (charter §7). AC14
reads the author-facing prose in `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md`, and no leg on
this bar greps either file for content: `kit/dogfood doc parity` compares each pair to itself and
`memory hygiene` grades specs, not the template that describes them. Gating "the template explains
the rule" would mean pinning template prose in a test, which is the paraphrase-beside-its-source
shape this repo refuses. So AC14 stays a manual check, run at the fold and again at the landing, and
its four greps are written out in full so that running it takes no judgement.

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
    nothing landed and nothing in flight goes red. `REV_SCOPE_CUTOFF="2026-09-07"`. The date is
    RE-DERIVED and not the one the option above names: that bullet was written on 2026-09-04, when
    2026-09-05 was tomorrow, and today is 2026-09-05, so it is now the fleet's own working date
    rather than a date ahead of it. Measured at the fold across all 44 local and remote refs — newest
    spec filename date 2026-09-04, no spec dated 2026-09-05 on any ref or in any of the 15 live
    worktrees — 2026-09-06 was the first date this fleet could no longer write into.
    `SPEC10_EVIDENCE_CUTOFF` is the precedent for the same correction. The accepted cost is now a
    fact rather than a tradeoff: the arm grades zero specs on day one, and its S6 fixtures are its
    entire coverage. The RULE is what the owner ratified and the DATE is derived from it, so the
    derivation was re-run at build time on 2026-09-06 and returned `2026-09-07` — §4's Migration
    carries that measurement, and every carrier in this build takes the same value.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8, §3, §4, §5, §6 · folded the owner's ruling on F1: the cutoff takes the
  ahead-of-the-fleet branch, re-derived to `2026-09-06` because 2026-09-05 is now the fleet's own
  working date. §4's Migration and Rollout, §3's retrofit non-goal and §5's risk row state the date
  and its zero-population cost as fact rather than as a pending choice, and AC1's fixture filename
  moved from 2026-09-05 to 2026-09-06 so the observed red is still reachable under the new cutoff.
- rev-3 · 2026-09-05 · §2 · §4 · §6 · §7 · folded spec-audit round 1, findings H1, H3 and H7. H3:
  S4, §4's Migration and the Files-touched table add `tools/memory-tree/.memory-tree.conf.example`
  as the key's third carrier, and new AC13 observes it plus the deletion red. H7: new AC12 observes
  S5's zero-population notice, which had no criterion at all, and pins that it is a stdout line on a
  run that still exits 0 and is unreachable under `--staged`. H1: S6 states the `tFixture-90`-upward
  block as the build README's `80 + 10N` allocation rather than a free-block claim measured against
  the file's high-water. §7 gains the clause naming `memory-hygiene self-test` as the parity arm's
  home. §4's Migration also stops calling this the "sixth" dated cutoff in the conf — the count was
  wrong and nothing derives it.
- rev-4 · 2026-09-05 · §2 S1 S2 S3 S4 S6 S7 S8 · §3 · §4 · §5 · §6 AC7 AC8 AC12 AC14 AC15 · §7 · §10 ·
  folded spec-audit round 2, named findings H3 and M1, plus the class sweep the build README's
  close-over-the-CLASS rule requires. H3: every scope item now names its observer, and new AC14
  grades what the author-facing text SAYS — four greps against a baseline §4 records before the
  render — where AC8, now restated as the sameness check it always was, only ever compared two files
  to each other. M1: the three wrong anchors are gone, and with them every other line pin in this
  document; §3, §4 and §10 cite `check-memory-hygiene.sh`, `drift_report.py`, `HYGIENE.md` and
  `BUILD-METHOD.md` by source text, since round 1 ruled `:1173` should have been `:1172` and the fold
  corrected only the sibling. Swept classes that HIT: B1's nested-guard shape — §4 now states the
  arm's placement as an exclusion and AC15 witnesses it on a blank `SPEC_WITNESS_CUTOFF`; M7's
  could-not-fail criterion — AC7 says what it cannot prove and AC12's lowered run carries the
  corpus evidence; M10's false `Observed by` — S4's tag covered one of three carriers; M3 and L1's
  stale population count — the seven kit-version carriers became a derivation; M8's
  false-of-its-own-file prescription — S1's grammar admits the `·` separator this file's own §9 uses;
  L2's off-by-N — the `drift_report.py` pin named the append line, not the indent guard the sentence
  beside it quoted, so it too became a source-text citation. This document now holds no line pin at
  all, which is the only form of the build README's rule 6 that cannot rot. Also
  corrected without a finding: 1,683 rev heads was 1,682, "476 tracked specs" now says which
  population it counts, and three entry-level percentages became rates because a re-derivation at
  this fold disagreed with them by about a point.
- rev-5 · 2026-09-05 · §2 S4 · §3 · §4 · §5 · §6 AC9 AC16 · §7 · folded spec-audit round 3, the
  TERMINATING fold: findings B1 and H3, both disposed here, nothing parked. B1, the blocker and
  half this unit's: the awk binding for `REV_SCOPE_CUTOFF` is named `revscopecut`, spelled from the
  key rather than abbreviated, and the single `mcut` this document carried is gone. S4 and §4's
  Files-touched row name the binding; §4 gains "The binding, and who owns the name", which states
  the claim for `TOOL-aJoinedCanon-3`'s register to carry, records that the audit's `rvcut` was
  declined for sitting one letter from an already-taken `rcut`, and verifies at HEAD that the
  check-12 `-v` list is one awk program with one namespace. New AC16 is the observation the round
  said neither spec had: no name bound twice on that invocation, with a liveness refusal if the
  locator matches no line, a staged red run at this fold, and an honest note that it cannot red for
  a real collision until `order` 4. H3: §7 gains `kit version markers` with the reason it is not
  covered by `verdict epoch`, and AC9 now runs `check-kit-versions.sh` beside
  `check-verdict-epoch.sh` with the two staged reds named separately. Swept for H3's class — a leg
  that reds on this landing and §7 does not name — and it HIT once more: `spec tokens (a spec's own
  names resolve)` is unguarded, grades this document's own backticked names, and was absent. Swept
  for B1's class, a shared engine resource taken without a register, and it did not hit again: this
  unit adds no shell function, and its fixture block is already allocated by the build README.
  Also corrected without a finding: the fix text says "both `mcut` occurrences" and this document
  held one; `TOOL-aJoinedCanon-4` independently renamed its own binding to `fmcut` in this round,
  so the collision is closed from both ends; the Files-touched table now names
  `tools/memory-tree/BUILD-METHOD.template.md` by path, which §7's claim about that leg's
  population needed; and two derived counts written while drafting this fold were caught and
  replaced by the derivation, which is the rule this document keeps re-breaking. §3's
  `TOOL-dUnstalledConvoy-14` non-goal records that round 3's H1 gave that backlog row its missing
  reachability evidence, and states that the evidence goes to the row rather than into this unit.
- rev-6 · 2026-09-06 · §4 · §6 AC1 AC7 AC12 · §8 · re-derived the ratified date at BUILD time,
  which §4's Migration obliges: specs dated 2026-09-05 now sit on `main` and eight other live
  branches, and today is 2026-09-06 with two unattended runs live in it, so the rule the owner
  ratified returns `REV_SCOPE_CUTOFF="2026-09-07"`. §4's Migration carries the new measurement
  beside the fold's, the §8 mark records that the rule was ratified and the date derived from it,
  and AC1's fixture filename moved to 2026-09-07 so the observed red stays reachable. The fold's
  own measurement sentences are left standing as the record of what was measured then.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade every bullet in a spec section and fold its
wrapped continuation lines into the entry before testing it"` returns no seam for this behaviour,
and the reason is a property of the index rather than of the tree: the lookup ranks Python and
shell SYMBOLS plus inventory keys, and the accumulator this unit extends is an unnamed awk block
inside a shell script, so it is unreachable by that instrument. Read directly, the seam is real and
is named in §4, and cited there and here by source text rather than by line because three sibling
units edit this engine before this one builds: the acceptance-witness accumulator in
`check-memory-hygiene.sh` — the block whose fold is `if (lab != "") acc = acc " " L` — supplies the
head-selector and continuation-fold shape, and the §9 range walk opening on
`if (L ~ /^## [0-9]+\. Revision log/) in9 = 1` supplies the section extraction, so the arm adds no
new pass. A second, non-shareable prior art is `_REVLOG_RE` and the loop under it in
`tools/drift-audit/drift_report.py`, which folds §9 continuations in Python for the mechanism-drift
signal; it constrains this unit's grammar rather than being extended by it.

Recall terms used: `python tools/memory-recall/query.py "why does the spec revision log stay
unstructured and what dated cutoff would a new check 12 arm need" --terms "revision log rev line
dated cutoff check 12 grandfather corpus spec format ratchet awk arm continuation line"`. The hit
that changed this spec was `TOOL-dUnstalledConvoy-14`, the OPEN backlog row proposing two further
§9 arms, which §3 names as a non-goal this unit makes cheaper.

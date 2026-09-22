**Serves:** spec-audit TOOL-aProvenReuse-1 TOOL-aProvenReuse-2

# aProvenReuse — round 2 spec audit: the FOLD, not the design

Round 2 · 2026-08-31 · node a · fold commit `a3c23955`, pre-fold `11e6d8bb` · adjudicated by one
synthesis pass over the round-2 finder/skeptic corpus, with every source claim re-verified against
the tree at HEAD `a3c23955` before it was written down.

**Subjects, pinned at the blob each was read at.** ROUND 2.
`memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-1.md@36bf2507bac4a4e45de10c79cc223c62f34cd7b8` ·
`memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-2.md@065d78a3741dd08fe25de155f62f9267ddd6551e` ·
`memory/builds/aProvenReuse/README.md@e52299c8b1caf078da5e646ea9f5bd26d679a420`

## Verdict: BLOCKED

Four blockers, five highs, six mediums — fifteen distinct defects, every one of them created or
left standing BY THE FOLD rather than by the original design. Round 1 asked for eight repairs and
got eight edits; four of them fixed the sentence they were pointed at and left the other half of the
same fact standing somewhere else in the same file. That is this repo's own
`amendment-leaves-its-other-half-standing` class, and the fold reproduced it on its own flagship
fix: unit 1 now states its single most load-bearing value, the evidence cutoff, twice and
differently, with the RATIFIED half carrying the value round 1 rejected.

Neither spec is buildable as it stands. Two of the four blockers would ship a broken artifact (a
hygiene gate that aborts in every adopter tree; a Definition-of-Done item that reports UNMET on
every conforming Windows run — the *same* false verdict the fold was commissioned to remove), and
two would ship a green acceptance criterion over an unfixed defect.

## Review shape

**39 raw · 27 confirmed · 12 refuted · 0 unverified · precision 0.69.** The 27 confirmed reports
consolidate to **15 distinct defects**: four clusters were reported independently by three to five
finders each (the §8 Q2 residue, the deleted shell-side preset, AC8's grep, and the corpus figures).
Consolidation is recorded per finding so the round-3 fold can attribute each edit.

Precision rose from round 1's 0.49 to 0.69 on a smaller, denser surface — expected, and consistent
with the charter's rule that a hardened target earns fewer agents, not more.

## Claims the fold asserts about existing code — VERIFIED, and TRUE

These were the three highest-risk assertions in the fold text. All three hold; recorded so a
round-3 reader does not re-spend the tokens.

- **Unit 2 S4, the LOG side of the join.** `tools/memory-recall/query.py:242-243` puts the log at
  `common_git_dir(repo)/recall/queries.jsonl`; the live file carries
  `"worktree": "C:\\projects\\coding-governance\\..."` — two backslash BYTES per separator, exactly
  as S4 states. The row filter's space is real too: `query.py` writes `"type": "query"` through
  `json.dumps` while `recall-opened.js:186` writes `"type":"opened"` through `JSON.stringify` (59
  such rows in the live log), so the two spellings cannot collide. The prefix hazard is real: 18
  rows for the primary tree, 100-plus for linked worktrees under it.
- **Unit 2 S6a, the protocol table and check 16 arm E.** `check-unattended.sh:1512-1537` joins
  `DOD_CORE` to the protocol's Definition-of-Done table in BOTH directions (`ed1`/`ed2`) and then
  word-compares the count sentence above it (`cw` → `cn` against `ndod`); its word table already
  carries `eleven`. `PROTOCOL.template.md:313` and its render both read `Ten kit-owned core items.`
  The leg is `unattended kit gate`, guard `[]` in `tools/gate-legs.json`, so it runs on every bar.
  S6a's "omitted, S1 reds the merge bar twice" is exactly right.
- **Unit 1 S1 / §5, the `STREAMS_CUTOFF` guard shape at `:846`.** `check-memory-hygiene.sh:846`
  reads `if (scut != "" && fdate != "" && fdate >= scut)`. The citation, the line number and the
  shape are all correct, and the three siblings (`scut`, `wcut`, `fcut`) do use it in that block.
- **Unit 2 S6's carrier measurement.** `grep -c reuse-first` returns 0 for
  `tools/unattended/PROTOCOL.template.md` and 0 for `memory/guides/UNATTENDED-PROTOCOL.md`, 3 for
  each SKILL carrier. The fold's correction of round 1's "two templates and two renders" model is
  sound.

## Findings

| # | Sev | Subject | Address | Defect |
|---|---|---|---|---|
| F1 | BLOCKER | spec 1 | §8 Q2 | ratified resolution still pins `2026-08-31`, the value the fold rejected |
| F2 | BLOCKER | spec 1 | §2 S1 + §4 Inventory | the shell-side `SPEC10_EVIDENCE_CUTOFF=""` was deleted from scope; the gate ABORTS under `set -u` in every existing adopter |
| F3 | BLOCKER | spec 2 | §6 AC8 | the fold's grep returns 7 hits today, 5 unrelated; unsatisfiable by a correct S6 |
| F4 | BLOCKER | spec 2 | §2 S4 | the compare was made EXACT and the other operand — this run's tree — is still unnamed; `pwd` reproduces the round-1 false verdict |
| F5 | HIGH | spec 2 | §6 AC8 vs §2 S6 | case-sensitive pattern is blind to S6's second required occurrence |
| F6 | HIGH | spec 2 | §2 S9, §6 | fold-added scope item with no declaration form and no criterion, against a validating schema |
| F7 | HIGH | spec 1 | §2 S5a | fold-added scope item, conditional on nothing that decides it, with no Inventory row and no criterion |
| F8 | HIGH | spec 1 | §6 AC5 | pins `188`, orders re-derivation in the same bullet, and mislabels the other population |
| F9 | HIGH | spec 2 | §2 S7, §6 AC4 | the mandated byte-copy fixture cannot match in the harness the suite actually builds |
| F10 | MEDIUM | spec 1 + README | §3 N3, "Expected improvements" | both still size the ungraded population at 253-that-fails-the-predicate |
| F11 | MEDIUM | README | problem statement vs build rule 5 | 346 in one bullet, 348 in the bullet added to stop that confusion |
| F12 | MEDIUM | spec 1 | §4 Design, placement paragraph | names an awk block gated on `want == canon10`; no such block exists |
| F13 | MEDIUM | spec 2 | §4 Migration | reads `None` while S5 raises a floor every existing adopter declares in their own conf |
| F14 | MEDIUM | README | `roster:units` | flipped to SPECCED while both spec headers and the generated table below say OPEN |
| F15 | MEDIUM | spec 2 | §2 S6 | retires two sentences and leaves the prose the same edit invalidates |

---

### F1 — BLOCKER · `spec/2026-08-31-spec-TOOL-aProvenReuse-1.md` §8 Q2 (against §2 S1a, §4 Migration, §4 Alternatives, §5, AC4, AC5a, README)

*Consolidates round-2 findings 2, 9, 18, 30 — four independent finders.*

**Defect.** The fold moved the evidence cutoff to `2026-09-01` in S1a, §4 Migration, §4
Alternatives, §5 Error states, AC4, AC5a and the build README, and left §8 Q2 reading
**`RESOLVED (agent, 2026-08-31, delegated): this build's date, 2026-08-31. The two are the same
day, and pinning the later of two identical values buys nothing.`** `git show a3c23955` confirms
the fold touched every other carrier and never touched Q2.

**Why it is a blocker and not a typo.** §8 is the fork-resolution record, the header stamps
`ratified 2026-08-31`, and `memory/TEMPLATE-SPEC.md:118-124` defines that pointer as the mark added
once §8's forks are resolved — so the ratification now vouches for the answer §4 Alternatives
records as *"Setting the cutoff to this build's date. Rejected at round 1 (finding 21)."* A builder
who reads §8 for the settled decision pins `2026-08-31` and reds `memory hygiene` on `main` for the
21 Tier-2 specs S1a measured across three live sibling branches — the exact blocker the fold was
commissioned to close, and the build README's own "neither unit may red a landed spec" broken by the
unit that wrote the rule. Q2's supporting sentence is also now false on its face: `2026-09-01` and
`2026-08-31` are not the same day.

**Fix.** Rewrite Q2's resolution to `2026-09-01`, replace its reason with S1a's cross-branch
enumeration, and keep the `UNITS_REGION_CUTOFF` citation only as the argument for not deferring to
the landing date. Q2's *question* also needs re-scoping — with the value now ahead of both dates,
"this build's date or the landing date" is no longer the fork that was decided. Alternatively mark
Q2 SUPERSEDED and point it at S1a. Do not leave a RESOLVED question the rest of the document
contradicts.

**Left-shift.** This is the general class, and it is cheaply gateable at fold time rather than at
review time. Add `tools/memory-tree/fold-residue.sh <pre-fold-blob> <file>`: diff the pre-fold blob
against the file, and for every literal the fold REMOVED, grep the post-fold file for it — any
surviving hit is printed with its line and must be accounted for. Run it as a step of BUILD-METHOD's
fold, and it catches F1, F8, F10, F11 and F15 in one pass. It is a dozen lines and it fails on this
very commit today.

### F2 — BLOCKER · `spec/2026-08-31-spec-TOOL-aProvenReuse-1.md` §2 S1 and §4 Inventory (row `tools/memory-tree/check-memory-hygiene.sh`)

*Consolidates round-2 findings 3, 10, 19, 29 — four independent finders.*

**Defect.** Round-1 finding 26 asked the fold to drop the FORWARD resolution and the
`_SPEC10E_SHIPPED` capture. The fold dropped the shell-side declaration as well: the Inventory row
went from rev-1's ``S1 shipped default + `-v ecut=` `` to ``S1 the `-v ecut=` binding``, and
rewritten S1 names only `.memory-tree.conf` and the `.example` as declaration sites. Nothing in
rev-2 now requires `SPEC10_EVIDENCE_CUTOFF=""` to exist in the checker.

**Verified consequence.** `check-memory-hygiene.sh:19` is `set -u`. Every sibling optional cutoff is
declared `=""` ABOVE the conditional conf source — `SPEC_FORMAT_CUTOFF` :31, `STREAMS_CUTOFF` :32,
`SPEC_WITNESS_CUTOFF` :33, `FORK_MARK_CUTOFF` :34, `REVIEW_VERDICT_CUTOFF` :35 — with
`[ -f "$ROOT/.memory-tree.conf" ] && . "$ROOT/.memory-tree.conf"` at :62 and the awk bindings at
:798. Built from the rev-2 Inventory, `-v ecut="$SPEC10_EVIDENCE_CUTOFF"` expands an UNSET variable
under `set -u` and the gate aborts — in every tree whose conf predates the key, which is every
existing adopter, because `adopt-memory-tree.sh:47-50` copies the `.example` only when no conf
exists and never back-fills one. The `memory hygiene` leg does not red; it fails to RUN, for a
reason unrelated to hygiene. S1's own headline promise, *"an adopter who ships it blank means off"*,
is delivered by the preset the fold deleted, not by the `.example` — blank is unreachable in a conf
that never declares the key. The defect is invisible in this repo, because S1 adds the key to this
repo's own conf, so the builder's green run proves nothing about the population that breaks.

**Fix.** Restore the obligation to BOTH S1 and the Inventory row: `SPEC10_EVIDENCE_CUTOFF=""`
declared beside its five siblings at `:31-35`, above the conf source, with the conf value
overriding it.

**Left-shift.** A real regression gate exists for this and covers all six cutoffs at once: add an
arm to `tools/memory-tree/check-memory-hygiene.test.sh` that runs the checker against a fixture tree
whose `.memory-tree.conf` declares NO cutoff key at all and asserts exit 0 with no output. That arm
fails today if any preset is ever deleted, and it is the only observation that distinguishes
"blank means off" from "unbound means abort". Add the matching AC to §6.

### F3 — BLOCKER · `spec/2026-08-31-spec-TOOL-aProvenReuse-2.md` §6 AC8

*Consolidates round-2 findings 1, 12, 22, 31 — four independent finders.*

**Defect.** The fold replaced rev-1's vague "no tracked file still asserts…" with a concrete
observation: ``grep -rn "is SILENT" tools/unattended/ .claude/skills/unattended/`` returns nothing.
Run verbatim at HEAD it returns **7 hits**, and 5 are unrelated comment prose in files S6 does not
touch:

```
tools/unattended/adopt-unattended.test.sh:19    "a missed one is SILENT rather than red"
tools/unattended/check-unattended.sh:437        "Equal-and-zero is a young tree and is SILENT"
tools/unattended/check-unattended.test.sh:14    "a missed one is SILENT rather than red"
tools/unattended/check-unattended.test.sh:1221  "Arm B is SILENT without the carrier"
tools/unattended/check-unattended.test.sh:1365  "the join is SILENT"
```

**Impact.** AC8 is the only observable for S6, and it reds forever: a builder who executes S6
perfectly still cannot make it pass. The two available responses are both wrong — delete five
checker/test comments that have nothing to do with this unit, or declare AC8 met against a non-empty
grep, which is an unobserved scope item wearing a criterion. The fold scoped the grep to the kit
directory to protect this build's own README from round-1 finding 4, and aimed it at a directory
that carries the phrase for five other reasons.

**Fix.** Scope the observation to the two carriers S6 actually owns and match the SENTENCES, not the
two words. Note that a naive case-insensitive widening is also wrong: `SKILL.template.md:668` and
`SKILL.md:668` legitimately read *"neither way of getting it wrong is silent"*, so `grep -i
"is silent"` over the two carriers cannot return nothing either. Pin the sentences:

```
grep -n -e 'Waiving it is SILENT' -e 'is silent and is recommended against' \
  tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md
```

returns nothing, and `grep -c reuse-first` returns 1 in each carrier (the directive-table row at
:85, which stays). Naming the surviving hit stops a green-by-deletion pass. Keep the
`memory/builds/` exclusion rationale — it is correct and it is why the grep was scoped at all.

**Left-shift.** The charter already carries the rule this criterion broke, in §7: *run a candidate
gate predicate over the real tree before wiring it, and print hits AND near-misses.* Extend it to
acceptance criteria in `memory/TEMPLATE-SPEC.md`'s §6 writing rules: an AC whose witness is a
command asserting an EMPTY result records the count observed at authoring time beside it. A
criterion that has never been run against the tree is an assertion about nothing, and both halves of
this defect would have been visible in one execution.

### F4 — BLOCKER · `spec/2026-08-31-spec-TOOL-aProvenReuse-2.md` §2 S4 (third bullet, "The compare is EXACT")

*Consolidates round-2 findings 20, 33.*

**Defect.** S4 now pins the LOG side of the join to the byte — `grep -o '"worktree": "[^"]*"'`,
strip, `tr '\134' '/'`, `tr -s '/'`, `grep -xF` — and never names the expression that supplies the
OTHER operand of that exact compare. Round-1 finding 5's confirmed fix required exactly that half:
*"apply the same normalization to the shell root, naming which expression supplies it."* The fold
took finding 5's doubled-backslash half and its byte-copy-fixture half and dropped its shell-root
half. Finding 5 is also the only confirmed unit-2 finding missing from rev-2's §9 revision log,
which is how the omission survived a self-review.

**Reproduced on this worktree, against the live log.** S4's own pipeline:

- compared against `git rev-parse --show-toplevel` → `C:/projects/coding-governance/.claude/worktrees/unattended-kit-gaps-a3b869` → **3 matches**
- compared against `pwd` → `/c/projects/coding-governance/.claude/worktrees/unattended-kit-gaps-a3b869` → **0 matches**

Zero is the `zero` outcome: UNMET, "go run a probe", on a tree holding three real query rows. That
is the precise false verdict the other three S4 bullets were folded in to prevent, on the same
platform, in the same comparison. Making the compare EXACT removed the slack that would have hidden
a near-miss, so this fold made the unnamed operand MORE load-bearing than rev-1 left it. Both idioms
are already live inside the target file: `unattended.sh:274` sets `ROOT` with
`GIT rev-parse --show-toplevel` (the correct form) while `unattended.sh:2214` uses
`cd "$(...)" && pwd` for a path comparison (the `/c/` form). Nothing in the spec binds the builder to
the first.

**Fix.** Add a fourth S4 bullet: the compared value is the driver's existing `ROOT`
(`unattended.sh:274`), never `$PWD` or `pwd`, and it takes the SAME fold-then-squeeze before the
compare so both sides are normalized by one rule. Name the failure mode being closed, as the other
three bullets do.

**Left-shift.** An S7 arm, which is a gate and not a note: a fixture whose row carries the MSYS
`/c/...` spelling of the scratch root and asserts it is NOT counted, beside the `met` arm. The wrong
operand then fails a test instead of failing a run on one operator's machine.

### F5 — HIGH · `spec/2026-08-31-spec-TOOL-aProvenReuse-2.md` §6 AC8 against §2 S6

*Consolidates round-2 findings 32 and the second half of 1, 12, 22. Independent of F3: fixing the
directory scope leaves this standing, and fixing this leaves F3 standing.*

**Defect.** AC8's pattern is case-SENSITIVE, so it matches only the first of the two occurrences S6
retires. The second, at `SKILL.template.md:157` and `.claude/skills/unattended/SKILL.md:157`, reads
*"`reuse-first` is silent and is recommended against"* — lowercase, and invisible to `"is SILENT"`.

**Impact.** The criterion is narrower than the scope item it observes: it cannot distinguish a fold
that retired both sentences from one that retired only line 113. Round-1 finding 27 recorded this
exact scenario as the reason AC8 needed restating; the fold corrected S6's carrier set and left
AC8's pattern where it was. The "AC8 goes green over half a fix" outcome is blocked today only by
F3's five unrelated hits — remove those and the under-observation is live.

**Fix.** Fold into F3's replacement: both sentences, both carriers, counts pinned at 2 before and 0
after, with the surviving `reuse-first` count stated as 1 per carrier.

**Left-shift.** Same as F3 — an AC that asserts an empty result records its authoring-time count.

### F6 — HIGH · `spec/2026-08-31-spec-TOOL-aProvenReuse-2.md` §2 S9 (and §6, which carries no criterion for it)

*Consolidates round-2 findings 4, 35.*

**Defect.** S9 is fold-added and says `tools/unattended/kit.toml` "declares the memory-recall edge"
without naming a field or a value, against a schema that validates the only candidate form.

**Verified.** `tools/unattended/kit.toml` ships `requires = ["memory-tree"]` and nothing else, so
S9's premise is correct. The registry knows exactly two edge forms: `requires` (which N6 vetoes) and
`requires_if`, whose one live instance is `tools/memory-tree/kit.toml:8`. `tools/govkit/govkit.py`
check 7 (`:1114-1128`) fails any `requires_if` naming a non-registry kit, and fails any
`when_any_key_set` key absent from the declaring entry's OWN config key lists
(`required_keys_gate` / `required_keys_render` / `optional_keys` / `conditional_keys`). Unit 2's
coupling is unconditional — S1 puts `reuse-probed` in `DOD_CORE` outright and no `.unattended.conf`
key gates it — so no legitimate condition key exists to hang a `requires_if` on. Meanwhile
`govkit selfcheck` is guard-less in `tools/gate-legs.json` and runs on every bar, and no criterion
in AC1–AC9 observes the edge at all (AC8 runs `check-kit-versions.sh`, a version check; §7 does not
name `govkit selfcheck`). So S9 can be skipped with the whole bar green, or attempted and refused by
a schema the spec never mentions.

**Fix.** State the field and its value in S9 — either a `requires_if` whose condition key
`.unattended.conf` actually declares, or an explicit decision that the edge is a `why`-style comment
because check 7 has no evaluator for an unconditional soft edge. Add an AC that the
`govkit selfcheck` leg exits 0 with the edge declared.

**Left-shift.** Give that AC a negative control: it reds with `memory-recall` misspelled. That
proves the declaration is READ rather than merely present, and it is the same
skip-that-announces-itself discipline the fold already applied to S2's `kit absent` outcome via
AC3a.

### F7 — HIGH · `spec/2026-08-31-spec-TOOL-aProvenReuse-1.md` §2 S5a

*Round-2 finding 5.*

**Defect.** S5a is fold-added, conditional on a question nothing decides — *"…**if** M5's wording
needs to name the new requirement"* — and neither §8 Q1 nor Q2 decides it. It has no §4 Inventory
row for either `tools/memory-tree/BUILD-METHOD.template.md` or `memory/guides/BUILD-METHOD.md`, and
no §6 criterion: AC8 observes only the rendered `memory/TEMPLATE-SPEC.md`.

**Verified.** Both files exist and are a real parity pair —
`tools/memory-tree/kit-dogfood-parity.test.sh:53` pairs
`$M/guides/BUILD-METHOD.md:$KITREL/BUILD-METHOD.template.md`, and the `kit/dogfood doc parity` leg's
guard in `tools/memory-tree/kit.toml` already names `{memory_root}/guides/BUILD-METHOD.md`. So the
builder who TAKES S5a is caught by a gate if they hand-edit the render. What no gate catches is the
other direction: nothing in the spec's own check set distinguishes "S5a done" from "S5a skipped",
and skipped leaves M5 describing an obligation whose new machine form it does not name.

**Mitigating fact, recorded so the fix is not over-scoped.** S8's watched-file list is incomplete
(it names only `check-memory-hygiene.sh` and `.memory-tree.conf`), but the manifest itself already
watches `memory/guides/BUILD-METHOD.md` — it is the tenth `watch:` entry and also a `verify-paths:`
entry at `memory/guides/SESSION-KICKOFF.md:6-7`. So `kickoff-manifest ratchet` C5 would red on an
un-restamped edit. That is a late signal, not a silent hole.

**Fix.** Decide it: add the question to §8 with a resolution, or drop S5a. If kept, add both
BUILD-METHOD rows to the Inventory, extend S8's prose to name the guide, and extend AC8 to assert
the rendered `memory/guides/BUILD-METHOD.md` names the new requirement.

**Left-shift.** A template-spec writing rule and a check-12 arm: a §2 scope item whose text contains
a conditional (`if`, `where needed`, `if it turns out`) must cite the §8 question that resolves it.
Conditional scope with no resolver is unobservable by construction, and this is the second one this
build has shipped.

### F8 — HIGH · `spec/2026-08-31-spec-TOOL-aProvenReuse-1.md` §6 AC5

*Round-2 finding 7.*

**Defect.** Two defects in one criterion. It pins **188** and, in the same bullet, orders
*"Re-derive both numbers at build time rather than copying either"* — so it states no single
observation that can pass or fail. And its gloss of the other figure is wrong: it calls 253 *"the
all-tiers §10-bearing population"*. 253 is the all-tiers FAILURE count; the §10-bearing population
is 348, which is the number the same fold put into the README's new bullet.

**Independently derived at HEAD**, with a stdlib approximation of check 12's selector (tracked files
under `memory/` whose basename matches `YYYY-MM-DD-spec-`, filename date ≥ `2026-08-04`, containing
a `## 10.` heading; Tier read from the `**Status:**` line; arms matched case-insensitively as
substrings over the §10 body): **348** §10-bearing · **264** Tier-2 · **254** failing either arm
across all tiers · **189** failing within Tier-2. Every figure lands within one of the documents'
own, which is precisely the point — a second derivation does not reproduce the pin, because the
population moves with every post-`2026-08-04` Tier-2 spec authored on any branch, this build's own
two included.

AC5 is the sole liveness assertion for AC4, which reds nothing by construction, so its ambiguity is
load-bearing rather than cosmetic.

**Fix.** State the observation first and the measurement as evidence: *"reds and names the count
re-derived at build time over the Tier-2 post-`2026-08-04` specs failing either arm — 188 when
measured 2026-08-31, against 264 in that population."* Correct the gloss: 253 is the ALL-TIERS
failure count over 348 §10-bearing specs.

**Left-shift.** The charter's §7 rule — *no count of a derived population is written in prose* —
applied to acceptance criteria: an AC naming a corpus count names the DERIVATION COMMAND beside it,
and the number is an annotation with a date. Then the criterion is falsifiable and the number cannot
rot into a wrong bar.

### F9 — HIGH · `spec/2026-08-31-spec-TOOL-aProvenReuse-2.md` §2 S7 and §6 AC4

*Round-2 finding 21.*

**Defect.** S7 and AC4 both require the `met` arm's fixture row to be *"a byte copy of a real
`query` row out of a live `queries.jsonl`, escapes included, never one hand-authored from this
spec."* `tools/unattended/unattended.test.sh` builds ONE scratch repo — `TMP=$(mktemp -d)` at :57,
`cd "$TMP"` at :83, and its own header declares *"ONE scratch repo, reset between arms"* — so the
driver's `ROOT` inside every arm is that temp tree, never
`C:\projects\coding-governance\.claude\worktrees\…`.

**Impact.** A byte-copied row's `worktree` value can never equal the scratch tree's root under
S4's exact compare, so the `met` arm cannot report MET: S7's fixture rule and AC4's assertion cannot
both hold in the harness the suite actually builds. The arm the fold added to certify the corrected
join certifies nothing, and on a POSIX adopter the copied row carries no backslashes at all, so the
escaping path goes unexercised too. AC4's *"Measured now, this tree's live log holds 3 such rows, so
the arm has a real subject"* is true of the LIVE tree and irrelevant to the FIXTURE; the two are
conflated.

**Fix.** Restate the rule as what it needs to be: the fixture reproduces a real row's ESCAPING —
doubled backslashes, `"type": "query"` with the space, field order — with the `worktree` value set
to the scratch tree's own path escaped the same way. Then assert the arm reports MET with a count of
1.

**Left-shift.** Pair it with F4's negative fixture: one row carrying a foreign absolute Windows path
that must NOT be counted, and one carrying the `/c/...` spelling of the scratch root that must NOT
be counted. Three fixtures, and the escaping, the exactness and the operand are each observed by a
test that can fail.

### F10 — MEDIUM · `spec/2026-08-31-spec-TOOL-aProvenReuse-1.md` §3 N3 and `README.md` "Expected improvements"

*Round-2 findings 23, 36 (part).*

**Defect.** The fold corrected AC5's population confusion and added a README rule explaining it, and
left both PROSE statements of the wrong figure standing. N3 still reads *"repairing the 253 landed
specs that would fail the predicate"*; the README's Expected improvements still reads *"The 253
specs that would fail the predicate today are grandfathered."* `check-memory-hygiene.sh:1014` runs
`if (hdr ~ /Tier-1/) next` immediately before the Tier-2 body assertions, so the predicate reaches
only Tier-2 specs — 65 of the 253 are files it never reaches. The README now contradicts itself
inside one document: line 41's "253 specs that would fail the predicate" against line 87's "the
predicate only ever reaches the 264 Tier-2 specs … and 188 of those fail".

**Impact.** N3 sizes the deliberately-ungraded population at 253 when the correct figure is ~188,
and N3 is the non-goal a builder reads to decide whether a migration is owed. Round 1 confirmed this
confusion twice, findings 1 and 25, and its skeptic named the README half explicitly; the fold
closed the AC5 instance and not the class — which is the charter's own "gate the CLASS, not the
instance", broken in prose.

**Fix.** N3: *"repairing the 188 landed Tier-2 specs the predicate would red — 253 fail across both
tiers, but 65 of those are Tier-1 files check 12 never reaches."* Make the identical edit in the
README bullet.

**Left-shift.** F1's `fold-residue.sh` catches this mechanically: `253` was removed from AC5 and
survives in two other places in the same fold.

### F11 — MEDIUM · `README.md` problem statement against build-level rule 5

*Round-2 findings 16, 36 (part).*

**Defect.** The fold's new rule 5 states the all-tiers post-`SPEC10_CUTOFF` §10-bearing population
as **348**; the untouched problem statement four paragraphs above states the same population as
**346**, and its 54% / 51% / 27% figures are computed against 346. Derived at HEAD: 348. The bullet
added to stop two populations being confused introduced a second denominator for one of them.

**Discounted sub-claim, recorded for honesty.** The percentages do not visibly break — 188/348,
176/348 and 93/348 still round to 54%, 51% and 27%. The contradiction is the finding; the
arithmetic is not.

**Fix.** Re-derive the problem-statement bullet against the tree rule 5 was measured on, or drop the
raw counts from prose and leave the derivation to the specs, per the charter's rule against prose
counts of derived populations.

**Left-shift.** Same as F8: a build README that must carry corpus figures carries the command that
produces them, and the numbers are dated annotations. `fold-residue.sh` catches the specific
residue.

### F12 — MEDIUM · `spec/2026-08-31-spec-TOOL-aProvenReuse-1.md` §4 Design, the placement paragraph after the Inventory table (against §2 S1)

*Round-2 finding 13.*

**Defect.** §4 says the assertion sits *"inside the block the awk already gates on `want ==
canon10`"* and justifies the placement by reusing `want`, *"so the two cannot drift into disagreeing
about which specs are ten-section specs."* No such block exists. `want` is assigned at
`check-memory-hygiene.sh:1019` and appears only in the `wantn` ternary at :1020 and the
`got != want` test at :1021; the empty-body test at :1027-1038 that the assertion is told to follow
runs for EVERY Tier-2 spec whatever canon was chosen.

**Impact.** The fold rewrote S1's guard as the date-only conjunction `ecut != "" && fdate != "" &&
fdate >= ecut` and left this paragraph asserting a canon-gated enclosing block, so the two sections
now specify different scoping predicates for one assertion, and the stated justification rests on a
structure the source does not have.

**Fix.** Rewrite the paragraph to what is true: the assertion is added after the empty-body loop
inside the Tier-2 region beginning at `if (hdr ~ /Tier-1/) next` (`:1014`), and its own guard is
spelled explicitly — `want == canon10 && ecut != "" && fdate != "" && fdate >= ecut` if the canon
term is wanted, because no enclosing canon block exists to inherit it from.

**Left-shift.** A gate this repo can afford and does not have: a check that every `path:line` or
`path` citation inside a spec's §4 resolves — the file exists, and where a line is cited, the line
exists. It is the same idiom as `check-method-carriers.sh` ("every pointer declared"), one document
class over, and it would have caught a design paragraph describing code that is not there.

### F13 — MEDIUM · `spec/2026-08-31-spec-TOOL-aProvenReuse-2.md` §4 Migration

*Round-2 finding 14.*

**Defect.** §4 Migration reads `None`, while S5 raises the DoD half of `CORE_FLOOR` from 10 to 11.

**Verified.** `check-unattended.sh:430-431` reds when the declared floor sits below the kit's own
core count; `CORE_FLOOR` is REQUIRED from the project's own `.unattended.conf` (fail 1 at :387-388
when undeclared); and `adopt-unattended.sh:114-115` requires a pre-existing conf and never rewrites
it. Both `.unattended.conf` and `tools/unattended/.unattended.conf.example` read `12:10` today. So
an existing adopter who copy-installs an 11-item `DOD_CORE` keeps `12:10` and reds check 3 with *"the
declared Definition-of-Done floor sits below the kit's own core count"* until they hand-edit a conf
key nothing told them about. The `.example` S5 edits reaches only NEW adopters.

**Impact.** The fold added S9, N6 and the `kit absent` outcome specifically to keep this item
meetable for adopters, and then left Migration asserting there is nothing for an adopter to do.

**Fix.** Replace `None` with the adopter step — taking this kit version requires bumping the second
`CORE_FLOOR` field to 11 in the project's own `.unattended.conf` — and say so where an adopter reads
it, in `tools/unattended/README.md`'s update notes. Keep the existing `zero`-outcome sentence for
the run-level migration; the two are different migrations and both are owed.

**Left-shift.** An AC with a fixture tree whose conf still carries `12:10`, asserting
`check-unattended.sh` reds AND that the message names `CORE_FLOOR`. That turns the adopter's
discovery path into an observation the build makes on their behalf, and it is the liveness half AC6
already half-states.

### F14 — MEDIUM · `README.md` `roster:units` (against both spec headers and the `gen:build-units` table eight lines below)

*Round-2 finding 15.*

**Defect.** The fold flipped both authored roster rows from OPEN to SPECCED and re-rendered the
generated region in the SAME commit — and the regenerated table still says OPEN, because it derives
from the spec headers, which the fold did not touch. Both spec files still read `**Status:** OPEN`.
`memory/TEMPLATE-SPEC.md:61` makes these distinct members of one vocabulary (`OPEN` drafting ·
`SPECCED` complete, awaiting owner scope approval), so this is a contradiction, not two notations.

**Impact.** The authored roster is what a resuming agent reads first, and it disagrees with the
derived table beside it and with the source both are derived from. No leg catches it:
`gen_build_index.py` renders the generated region from spec headers, and the authored pair's only
surviving reader is the driver's `roster_ids` (`unattended.sh:1671`), which uses it for unit IDs.
The documented fleet query `git grep -lE '^\*\*Status:\*\* (SPECCED|INPROGRESS)'` finds neither
spec.

**Fix.** Pick one side and land it in one commit: either move both spec headers to `SPECCED` and
re-run `python tools/memory-tree/gen_build_index.py`, or revert the roster cells to OPEN.

**Left-shift.** The best gate in this report, because it is nearly free: `gen_build_index.py`
already parses both the authored `roster:units` region and every spec header. Add an arm to its
`--check-format` leg (already on the bar as "build README slot contract") that reds when an authored
roster status disagrees with the derived status for the same id. One comparison, on data the script
holds in memory already.

### F15 — MEDIUM · `spec/2026-08-31-spec-TOOL-aProvenReuse-2.md` §2 S6 (and S6a, and §6 AC8)

*Round-2 finding 37.*

**Defect.** S6 retires exactly two sentences and leaves standing the prose in the same paragraphs
that the same edit invalidates. `SKILL.template.md:114-115` continues *"A waived run's spec §10 must
NAME the waiver, or the skip leaves no trace at all"* — whose trailing clause is falsified by this
unit's own S2 `waived` outcome, where `DOD_OUT` names the waiver and its recorded reason. And the
count prose round-1 finding 27's fix explicitly listed — line 111's *"Two rows carry a consequence
worth knowing before you waive them"* and line 157's *"for the two handles that have a
consequence"* — appears in neither S6, S6a, nor any AC. Line 157's list holds `reuse-first` and
`land-once-done`; deleting the `reuse-first` clause leaves an introduction counting two over a list
of one.

**Impact.** After a conforming S6 the Skill still tells a waiving agent the skip leaves no trace,
which is the belief this unit exists to retire. Nothing catches it: AC8 greps only `is SILENT`, and
the `unattended skill wiring` leg compares the template to its render, so both carriers stay wrong
in identical bytes and the leg is green.

**Fix.** Extend S6 to the sentence that follows — *"A waived run's spec §10 must NAME the waiver"*
keeps its first clause and loses *"or the skip leaves no trace at all"*, replaced by what the
`reuse-probed` line now reports — and name both count phrases as edits S6 owns.

**Left-shift.** This repo already has the exact idiom, and it is proven: `check-unattended.sh` check
16 arm E word-compares the protocol's *"Ten kit-owned core items."* against the driver's set,
because *"the rows were right and only the prose was wrong"* is how the last count sentence went
stale in both copies while its leg stayed green. Add the same join for the Skill's waiver-consequence
list: the spelled-out count in the introduction against the number of handles the list names.

## Left-shift summary

Five of the fifteen fixes are gates this repo can afford, and three of them are joins it already
runs somewhere else:

- **`tools/memory-tree/fold-residue.sh <pre-fold-blob> <file>`** — every literal a fold REMOVED must
  not survive elsewhere in the file. Catches F1, F8, F10, F11 and F15's count phrases. It fails on
  commit `a3c23955` today, which is the only proof a new gate is worth having.
- **A no-cutoff-conf arm in `check-memory-hygiene.test.sh`** — the checker exits 0 with a conf
  declaring no cutoff key at all. Covers F2 and all six cutoffs, forever.
- **An authored-vs-derived status arm in `gen_build_index.py --check-format`** — F14, on data the
  script already holds.
- **The SKILL waiver-consequence count join in `check-unattended.sh`** — F15, an exact copy of check
  16 arm E's proven shape.
- **A `path:line` citation resolver over spec §4** — F12, the same idiom as
  `check-method-carriers.sh`.

Two are writing rules for `memory/TEMPLATE-SPEC.md` rather than gates, because the class is
judgement and not syntax:

- An acceptance criterion whose witness asserts an EMPTY result records the count observed at
  authoring time (F3, F5) — the §7 "run the predicate over the real tree first" rule, extended from
  gate predicates to acceptance criteria, which is where this fold broke it twice.
- A §2 scope item containing a conditional cites the §8 question that resolves it (F7).

## What this review did NOT check

- The DESIGN. Round 1 owns it; this pass graded the fold text against the tree and against the
  round-1 findings it claims to close. A defect in rev-1 that rev-2 left untouched and round 1 did
  not raise is not in scope here and would still be live.
- Whether the two arms unit 1 demands are the RIGHT two facts. Unchanged from rev-1, and unit 1's
  own §7 already declares it out of reach of any predicate.
- Execution. No gate was run end to end: every claim above was verified by reading source and by
  running the specific greps, derivations and pipelines quoted with their output. The corpus figures
  in F8 come from a stdlib approximation of check 12's selector, stated inline, not from the checker
  itself — they are within one of every figure the documents carry, which is enough to establish
  that the pin is not reproducible and not enough to replace the checker's own count.

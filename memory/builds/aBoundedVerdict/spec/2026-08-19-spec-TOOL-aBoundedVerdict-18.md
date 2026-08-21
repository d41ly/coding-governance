# TOOL-aBoundedVerdict-18 — the two checks that cannot fail get subjects

**Status:** CLOSED · rev-5 · 2026-08-21 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

Two close-path checks are green because nothing they could catch is reachable: the
`landed-via-lander` Definition-of-Done item is two conf-non-empty tests plus a grep the merge bar has
already run inside the same close, and the gate leg's check 8 exempts terminal records wholesale, so
its emptiness branch has no reachable subject over a corpus that is terminal almost everywhere — while
exempt records carry exactly the bytes it exists to refuse. Give each one a subject, or say in the
source why it has none. Every population figure in this spec is a command, not a numeral: the
run-state corpus is `git ls-files 'memory/builds/*/RUN*.md'` plus each record's `phase:` line, and it
moves with every run.

## 2. Scope (IN)

- **S1** — **`landed-via-lander` gains a REAL observation: the lander writes a marker and `--landed`
  reads it.** Resolved by the owner at F2 against this spec's own recommendation, which was to narrow
  the claim instead. Today the item asserts that `LANDER` and `BYPASS_BAN` are non-empty and that the
  run-state file does not contain the flag — three facts, of which the third is leg check 11's job and
  the first two are that the conf parsed, so it cannot fail for anything the run did. After S1 it can.
- **S1a** — the marker is a DECLARATION, not a convention: a new `.unattended.conf` key names the path
  the lander writes and the driver reads. Undeclared, the item degrades to S2's narrower claim rather
  than refusing — an adopter who has not adapted their lander must not be wedged by a key they have
  never heard of, and this is the one place in the unit where a missing declaration is allowed to mean
  "not asked" instead of "unmet".
- **S1b** — the marker carries the run's own identity, not just its existence. A bare touched file is
  satisfied by any previous landing, which is the pass-by-finding-anything shape this repo has already
  paid for twice; it names the slug and the witness sha `--landed` is about to record, and `--landed`
  compares them rather than testing presence.
- **S1c** — the ADOPTER path carries the change, because S1 changes what `LANDER` means for everyone
  who has one: `adopt-unattended.sh` seeds the key, the conf example documents what a compliant lander
  must write, and `tools/push-main.sh` — this repo's own declared lander — writes it, so the dogfood
  is the first adopter rather than an exception to the rule.
- **S2** — the redundant grep is DELETED regardless of S1, because it duplicates leg check 11 inside
  the same close. Where the marker key is undeclared, the item's remaining claim is stated honestly in
  the protocol's Asserts cell: an item that says less beats one that implies a check it does not run.
- **S3** — leg check 8's terminal exemption is SCOPED to the emptiness branch, not kept wholesale.
  Today it clears `rd` for any terminal phase, which skips the malformed-generated-markers refusal as
  well as the emptiness one; backlog row `TOOL-cSettledDocket-11` (OPEN, `memory/backlog/TOOL.md`)
  prescribes exactly that scoping, and F1 resolves with the row rather than around it. After S3 the
  marker-shape refusal runs on every record including terminal ones, and the emptiness refusal keeps
  its exemption plus S5's note. The row is SATISFIED by this unit, not by this spec: its status edit
  rides the landing commit and is the orchestrator's bookkeeping.
  Measured: unexempting the marker-shape branch reds nothing today — every tracked record has a
  well-formed marker pair. Re-derive both populations at build time from the command in §1; no figure
  for either is written in this spec, because the corpus moves with every run.
- **S4** — whichever way S3 resolves, the check gains a RED fixture in
  `check-unattended.test.sh`. A check whose only evidence is a corpus that cannot trigger it is the
  `fixture-passes-by-finding-nothing` class, and this unit's whole subject is that class.
- **S5** — a one-line note in each check's source recording that its vacuity was measured and on what
  date, so a later reader can tell a deliberately narrow check from an accidentally empty one.

## 3. Non-goals (OUT)

- No new Definition-of-Done item, and no removal of one. `landed-via-lander` keeps its name and its
  slot; what changes is what it observes or what it claims.
- Not leg check 11, which owns the bypass-flag ban over the run-state file and does it correctly. S1's
  redundancy is on the driver side.
- Not a general vacuity sweep of the leg's other checks. The audit examined four; the rest are
  named as uncovered in its own coverage section and a sweep is a separate unit if the owner wants one.
- Not the `landed-via-lander` item's TRUST properties. Whether a run could lie about having used the
  lander is protocol section nine's subject and unchanged here.
- No change to the CORE DoD floor or to any checker assignment.

## 4. Design

### `landed-via-lander`, as it stands

```
[ -n "$LANDER" ] && [ -n "$BYPASS_BAN" ] && ! grep -qF -- "$BYPASS_BAN" "$rel"
```

Term 1 and term 2 fail only if the conf declared nothing, which the leg's required-key loop already
refuses. Term 3 is a grep the leg runs over the same file in the same close. So the item cannot fail
for any reason attributable to the run, which is what makes it vacuous — not that it is wrong, but
that it is answering a question two other checks already answered.

What it is NAMED for is observable at `--landed`: that verb knows the push happened, and it is the only
place the driver sees the landing at all. **The owner resolved F2 toward making it observable** — the
lander writes a marker, `--landed` reads it — which is the option this spec priced highest and
recommended against, on the ground that it changes what `LANDER` means for every adopter. That cost is
real and is accepted; S1a and S1c are where it is paid, and the degradation path in S1a is what keeps
an unadapted adopter working rather than wedged.

Why the marker must carry identity (S1b): a presence test is satisfied by the marker a PREVIOUS landing
left, so the item would pass on a run that never called the lander at all. The same degeneration the
driver's own comments record in `check_authorization`, where an empty base turned a provenance test into
a read of the git index. Presence is not provenance.

### Check 8, as it stands

The check refuses a run-state file carrying a copied unit list — the staleness the main redesign removed
by making the unit list derived. It has TWO refusals, not one, and both hang off the same variable:

```
rd=${f%/RUN.md}/README.md
case " $PHASES_TERMINAL " in *" $ph "*) rd="" ;; esac
if [ -n "$rd" ] && [ -f "$rd" ]; then   # malformed markers, then emptiness
```

Clearing `rd` on a terminal phase disables the malformed-generated-markers refusal as well as the
emptiness one. That over-wide scoping is what backlog row `TOOL-cSettledDocket-11` records against
`cBriefedPilot-36`, and it is the half the vacuity argument never reached: retired bytes are a reason to
tolerate a stale COPY, never a reason to stop reading whether the region's markers parse at all. A
record whose markers are malformed cannot be read by anything, terminal or not.

So the two refusals resolve differently, which is what F1 now says:

- the EMPTINESS refusal keeps its exemption — retired bytes are history that must not be rewritten, and
  a check firing on frozen records produces a red nobody can clear. Its correctness stays
  indistinguishable from its emptiness until S4's fixture and S5's note make it legible;
- the MARKER-SHAPE refusal loses it, per the row. Measured: unexempting it reds nothing today, because
  every tracked record has a well-formed marker pair, so this is a scope repair with no migration
  attached.

### Inventory

| Concern | Today | After |
|---|---|---|
| `landed-via-lander`'s failure modes | none attributable to the run | the lander's marker, matched on slug + witness |
| a landing that skipped `$LANDER` | indistinguishable from one that used it | the item is unmet |
| a marker left by a PREVIOUS landing | would satisfy a presence test | refused: the witness does not match |
| an adopter whose lander writes nothing | — | the key is undeclared, the item degrades to its narrow claim |
| its redundant grep | duplicates leg check 11 | deleted |
| check 8's emptiness refusal | exempt on every terminal record, so unreachable over this corpus | exemption kept, with a dated note saying it was measured |
| check 8's marker-shape refusal | exempted by the same cleared `rd`, for no stated reason | runs on every record, terminal included (`TOOL-cSettledDocket-11`) |
| check 8's evidence | a corpus that cannot trigger it | a red fixture per branch |
| why either check is narrow | unrecorded | a dated note in source |

### Migration

None, and F1's re-resolution is what removes it. The EMPTINESS exemption stays, so the terminal records
carrying copied unit lists stay exempt and are not touched — a terminal record is a record, and
rewriting one to satisfy a check written later is what the freeze exists to prevent. The MARKER-SHAPE
refusal loses its exemption and reds nothing today, so it needs no waiver either. Re-run the §1 command
before building: if the corpus has since acquired a record with a malformed marker pair, the fix is a
shrink-only entry in the `*.txt` waiver registry pattern beside the other gate lists (§10), never a
rewrite of the record and never a re-widening of the exemption.

### Rollout

S5 and S4 first: they are additive, they cost nothing, and they make the current state legible before
it changes. Then S3's scoping, which is a two-line edit plus its fixture arm. S1/S2 last, because they
are the ones that touch a shipped contract and the adopter path.

### Files touched (estimate)

The leg and the driver: `tools/unattended/unattended.sh` (the item's arm) ·
`tools/unattended/check-unattended.sh` (check 8) · `tools/unattended/check-unattended.test.sh` (S4's
fixture) · `tools/unattended/unattended.test.sh`.

The declaration and the adopter path S1a and S1c put in scope, none of which were listed through rev-3
even though AC4b and AC4c grade them: `.unattended.conf` (this repo's own declaration of the marker
key) · `tools/unattended/.unattended.conf.example` (the key and the compliant-lander contract) ·
`tools/unattended/adopt-unattended.sh` (seeding the key — today this script only READS the conf, so
seeding is new code, not a template edit) · `tools/push-main.sh` (this repo's declared lander, which
must write the marker).

`.unattended.conf` is on the kickoff manifest's `watch:` list, so `memory/guides/SESSION-KICKOFF.md` is
touched too: the manifest is re-stamped in the SAME commit that edits the conf, with the delta line in
that commit's message. The watch list is in that file's manifest-audit block.

The protocol pair, if S2 fires: `memory/guides/UNATTENDED-PROTOCOL.md` and
`tools/unattended/PROTOCOL.template.md` (the Asserts cell, byte-compared by leg check 10).

The kit version bump is not one carrier. `tools/check-kit-versions.sh` forces five files and seven
sites: `KIT_UNATTENDED_VERSION=` and its same-line `gov:kit` marker in both
`tools/unattended/unattended.sh` and `tools/unattended/check-unattended.sh`, the `gov:kit` marker in
`tools/unattended/PROTOCOL.template.md` and in `tools/unattended/SKILL.template.md`, and the re-render
`.claude/skills/unattended/SKILL.md`, which `check-wiring.sh` compares against the tracked template.

### Alternatives rejected

- **Delete `landed-via-lander` outright.** Rejected: the CORE DoD set is shrink-only by a declared
  floor, so deleting a member is a reason-free override of everything keyed on it.
- **Have the driver parse the lander's own output to prove it ran.** Rejected: it couples the kit to a
  project-declared command's output format, which is the one thing `LANDER` exists to keep opaque. The
  marker is the same information through a declared interface rather than a scraped one.
- **A presence-only marker.** Rejected at S1b: satisfied by a previous landing's marker, so it would
  read as provenance while proving nothing — weaker than the vacuous item it replaces, because vacuity
  at least does not mislead.
- **Narrowing the claim (this spec's own recommendation through rev-1).** Refused by the owner. Kept as
  the DEGRADATION path in S1a for an adopter with no declared marker, which is the one place its
  reasoning still applies.
- **Leave check 8 as it is and accept the vacuity.** Rejected on this repo's own rule: a check that
  cannot fail is recorded as such or fixed, never left to read as coverage. S5 is the minimum acceptable
  outcome and it is still a change.
- **Repair the terminal records carrying copied unit lists so check 8's emptiness branch has clean
  subjects.** Refused: a terminal record is a record, and rewriting one to satisfy a check written
  later is the opposite of what the freeze is for.
- **Keep the terminal exemption wholesale, as rev-3 resolved it.** Rejected at F1 against
  `TOOL-cSettledDocket-11`: the exemption clears one variable and disables two refusals, and the
  frozen-history argument reaches only the emptiness one. Nothing about a retired record makes its
  generated markers unreadable-by-design.

## 5. Production-readiness checklist

- **security** — S1b is the security-relevant line. A presence-only marker is a pass-by-finding-anything
  check and would be WEAKER than the vacuous item it replaces, because it would look like provenance.
  The witness comparison is what makes it a check; arm the stale-marker case explicitly. Note also what
  this still does not buy: a run with shell access can write the marker itself, so the item remains an
  attestation the run could forge, exactly as protocol section nine already says of everything the run
  writes. It stops an HONEST bypass, not a deliberate one, and the spec must not claim more.
- **perf / scale** — S1's deletion removes one grep per close.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — the empty case IS the subject of this unit.
- **observability** — S5's dated notes are the observability deliverable: they let a reader distinguish
  a narrow check from an empty one without re-measuring.
- **risks** — low. The one real risk left after F1 is S3's scoping being implemented by removing the
  exemption outright, which would red the exempt terminal records carrying copied unit lists and tempt
  a repair. Migration forbids the repair explicitly, and AC1a's control arm is what proves the
  emptiness exemption is still in force after the edit.
- **testing + left-shift gates** — S4 is the left-shift and it is the point of the unit.
- **migration / rollback** — none; see Migration, which F1's scoped resolution empties.
- **user docs** — the protocol's Asserts cell, only if S2 fires. The conf example is the OTHER doc S1c
  moves, and it is a shipped contract rather than a note: it is where an adopter reads what a compliant
  lander must write.

## 6. Acceptance criteria

- **AC1** — When leg check 8 runs against a fixture holding a NON-terminal run-state record carrying a
  copied unit list, it reds naming the file; the red fixture in
  `tools/unattended/check-unattended.test.sh` that does not exist today.
- **AC1a** — When leg check 8 runs against a fixture holding a TERMINAL record whose `run:generated`
  markers are malformed, it reds naming the file — the branch S3 unexempts, which passes today for the
  wrong reason. Its control arm: the same terminal record with a well-formed EMPTY-or-populated region
  stays clean, so the emptiness exemption is proven still in force rather than removed by accident.
- **AC2** — When `bash tools/unattended/check-unattended.sh` runs against the real tree it is clean, and
  `tools/unattended/check-unattended.sh` carries a dated note recording that check 8's emptiness-branch
  subject population over this corpus was MEASURED, naming the command that measures it rather than the
  figure it returned.
- **AC3** — When the `landed-via-lander` case body in `tools/unattended/unattended.sh` is extracted by
  line range and compared against its pre-change body as the control, the after-body no longer contains
  `grep -qF -- "$BYPASS_BAN" "$rel"` and the before-body does. A whole-file `grep -c 'BYPASS_BAN'` is
  NOT the assertion: the token appears across several unrelated call sites, so a count delta of one
  identifies nothing and any unrelated edit forges it.
- **AC4** — When a fixture run lands through a lander that writes the declared marker naming the slug
  and witness, `landed-via-lander` is MET; when the same run lands via a bare `git push` and no marker
  is written, the item is UNMET — the two arms that make the item able to fail for something the run
  did, which it cannot today.
- **AC4a** — When the marker exists but names a DIFFERENT witness (the stale-marker case, seeded by
  copying a prior run's marker into place), `landed-via-lander` is UNMET — the arm in
  `tools/unattended/unattended.test.sh` that proves S1b, and the one a presence-only implementation
  passes and must not.
- **AC4b** — When the marker key is UNDECLARED in `.unattended.conf`, the item reports its narrowed
  claim and does not refuse, and the Asserts cell in both halves of the protocol pair says what it then
  asserts; `bash tools/unattended/check-unattended.sh` is clean over the pair.
- **AC4c** — When `bash tools/unattended/adopt-unattended.sh --check` runs after S1c, it is clean, and
  `tools/push-main.sh` writes the marker — observed by landing a fixture through this repo's own
  declared lander rather than through a stub.
- **AC5** — When either check's source is read, it carries the S5 note, and
  `python tools/memory-tree/check-arms.py` is clean with any changed `ARMS_FLOORS` entry updated.
- **AC6** — When the tracked run-state records are enumerated by §1's command after this unit,
  `git diff` over `memory/builds/*/RUN*.md` is empty for every one of them — the arm that proves
  Migration's prohibition held and that no record was repaired to satisfy a check.

## 7. Gates

`tools/unattended/check-unattended.sh` + `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`tools/unattended/adopt-unattended.test.sh` (S1c's seeding is new code in that script) ·
`tools/push-main.test.sh` (the lander now writes the marker) ·
`bash skills/session-kickoff/manifest-check.sh` (`.unattended.conf` is watched) ·
`python tools/memory-tree/check-arms.py` · `tools/check-testsuite-counts.sh` ·
`tools/check-kit-versions.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — does check 8's terminal exemption stay or go, and for WHICH of its two refusals?** The
  exemption clears one variable and disables two refusals: malformed generated markers, then a
  non-empty region. Backlog row `TOOL-cSettledDocket-11` (OPEN, `memory/backlog/TOOL.md`) prescribes
  scoping it to emptiness alone, naming the over-wide scoping `cBriefedPilot-36` shipped; rev-3
  resolved "stays" wholesale without citing the row, and closed it by silence. The row is right on the
  half rev-3's grounds never reached: frozen history is a reason to tolerate a stale COPY, never a
  reason to stop reading whether the markers parse. **Recommendation: SCOPED — the exemption stays for
  the emptiness refusal and goes for the marker-shape one**, plus S4's fixture and S5's note.
  Grounds, both halves: a check firing on the copied bytes in superseded terminal records produces a red
  nobody can clear, which is worse than the defect it catches; and unexempting the marker-shape refusal
  reds nothing today, so the repair is free. Re-run §1's command before building rather than trusting
  that last clause.
  RESOLVED (agent, 2026-08-20, delegated): scoped to emptiness. Mechanism-only fork, it makes the spec
  agree with an OPEN backlog row instead of overriding one by silence, and neither branch changes a
  public surface.

- **F2 — can `--landed` observe that the push went through `$LANDER`, and is it worth a mechanism?**
  Options: parse the lander's output (rejected in §4 as coupling); have the lander write a marker the
  driver reads; or accept S2 and let the item claim less. This spec recommended the narrowing.
  RESOLVED (owner, 2026-08-19): **the lander writes a marker.** The cost the owner accepted, stated
  plainly: every adopter with a lander must adapt it, and this unit moves from Tier 1 to Tier 2 because
  it now changes a shipped contract rather than a local predicate. Three things follow and are in
  scope — the key is a declaration (S1a), the marker carries identity rather than existence (S1b), and
  the adopter path plus this repo's own lander carry the change (S1c). What it does not buy is stated
  in §5: a run with shell access can write the marker itself.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's mediums 7 and 31, kept as one
  unit because both are the same class — a check green for want of a reachable subject — and the fix for
  both is a fixture plus an honest statement rather than new logic. Tier 1: no contract another kit
  reads is changed, and the one item that might narrow its claim does so in a documented cell. F1
  resolved under the delegated fork rule; F2 raised to the owner because one of its options changes what
  a project-declared value means.

- rev-2 · 2026-08-19 · **F2 resolved by the owner against this spec's recommendation: the lander writes
  a marker.** The unit moves Tier 1 -> Tier 2, because it now changes what `LANDER` means for every
  adopter rather than fixing a local predicate. S1 is rewritten from "gains an observation" to the
  mechanism; S1a makes the marker a declared conf key whose absence DEGRADES to the old narrow claim
  rather than wedging an unadapted adopter; S1b makes the marker carry slug and witness, because a
  presence test is satisfied by a previous landing's marker and would read as provenance while proving
  nothing — weaker than the vacuity it replaces; S1c puts the change on the adopter path and on
  `tools/push-main.sh`, so the dogfood is the first adopter. S2 keeps the grep deletion, which was
  never conditional on F2. AC4 splits into four. §5 states what the marker still does not buy: a run
  with shell access can write it, so this stops an honest bypass and not a deliberate one.

- rev-3 · 2026-08-20 · M3 fork sweep, before any code. No fork moved: F1 and F2 were both already
  RESOLVED in place, F2 by the owner. What was missing is the machine-legal `none` first line in §8 —
  and its absence is not cosmetic, because the hygiene gate grades a terminal spec on that line OR on
  every bullet carrying the mark on the bullet's OWN line, and this spec's marks sit on continuation
  lines. Without this the unit could not have gone terminal despite having no open question at all.

- rev-4 · 2026-08-20 · the spec-audit fold, `2026-08-20-review-TOOL-aBoundedVerdict-1.md`, verdict
  BLOCKED. Five findings.
  **B8** (blocker): S1a declares a new `.unattended.conf` key and S1c puts the adopter path in scope,
  and AC4b/AC4c grade exactly those — while Files touched named NONE of the four paths that carry them.
  A unit cannot be graded on files it does not admit it edits. Added `.unattended.conf`,
  `tools/unattended/.unattended.conf.example`, `tools/unattended/adopt-unattended.sh` (noting that this
  script only READS the conf today, so seeding is new code rather than a template edit) and
  `tools/push-main.sh`, plus `memory/guides/SESSION-KICKOFF.md`, because `.unattended.conf` is on the
  kickoff manifest's `watch:` list and the manifest re-stamps in the same commit. §7 gains
  `tools/unattended/adopt-unattended.test.sh`, `tools/push-main.test.sh` and the manifest check. The
  same edit removes "the kit version constant" as a single carrier: `tools/check-kit-versions.sh`
  forces five files across seven sites and they are now enumerated.
  **H21** (high): F1 resolved the terminal exemption as "stays" wholesale without citing OPEN backlog
  row `TOOL-cSettledDocket-11`, which prescribes the opposite and names the over-wide scoping
  `cBriefedPilot-36` shipped. The row is right about the half rev-3's grounds never reached — the
  exemption clears ONE variable and disables TWO refusals, and the frozen-history argument covers only
  the emptiness one. Nothing about a superseded record makes its `run:generated` markers
  unreadable-by-design. F1 is re-resolved SCOPED: the exemption stays for the emptiness refusal, goes
  for the marker-shape one. Measured: unexempting it reds nothing, so Migration drops from a
  shrink-only waiver registry to none, and §5's risk becomes the implementation over-shooting into
  removing the exemption outright. S3, the design section, the inventory and the alternatives all
  carry the split now; the row's own status edit is the landing commit's bookkeeping and is NOT this
  spec's to make.
  **M11** (medium): the README roster gives this unit Tier 1 and this header says Tier-2. The header is
  right — F2 moved it in rev-2 because the unit now changes what `LANDER` means for every adopter — so
  Tier-2 is KEPT and the roster's Tier cell is the orchestrator's fix, not this file's.
  **M12** (medium): AC3 asserted on a whole-file `grep -c 'BYPASS_BAN'`, which counts several unrelated
  call sites, so a delta of one identifies nothing and any unrelated edit forges it. Re-written to
  extract the `landed-via-lander` case body by line range and assert the token's absence there, with
  the pre-change body as the control.
  **M13** (medium): same missing `memory/guides/SESSION-KICKOFF.md` entry as B8's last item, folded once
  in Files touched with the re-stamp note.
  Also, under the fold's no-stale-numeral rule: every population figure for the run-state corpus is
  gone (the "seven tracked records", the "zero subjects", the "three records" and their 1280/3082/4032
  byte sizes) and replaced by the command in §1, because that corpus moves with every run — and the
  "other seventeen leg checks" in §3 became "the leg's other checks" for the same reason. AC1a is new:
  it arms the marker-shape branch S3 unexempts, with a control arm proving the emptiness exemption
  survived the edit.

- rev-5 · 2026-08-21 · **built, and the check this unit exists to give a subject had a FOURTH silent-skip mechanism.** The
  promotion clause tested whether the subject appeared anywhere in the generated units region; per
  S5 the subject is the build slug or a spec path, and both are substrings of every row already.
  Measured against the real region: slug, spec path and unit id were all silent, and only a
  fabricated id fired it. It grades a unit-id DELTA against the roster at the run's pinned BASE now,
  matched as a whole id, which is what a promotion actually leaves behind.

  `landed-via-lander` is the other subjectless check, and its honest predicate turned out to be
  narrower than the row claimed: the bypass grep duplicated leg check 11 inside the same close, so
  it is gone and the protocol row says what remains. The real observation is `--landed`'s marker
  check, which is EQUALITY against the pushed commit rather than ancestry - a rule that reached no
  agent-facing carrier until this fold put it in the Skill and beside the verb's own row.

## 10. Reuse audit

Two seams, both existing. Leg check 11 already owns the bypass-flag ban over the run-state file, which is
why S1's deletion is a deletion and not a move — the predicate has a home and this item was a second
copy of it. And the shrink-only `*.txt` waiver registry pattern beside the other gate lists is what
Migration reaches for if the corpus has acquired a malformed-marker record by build time; naming it
means no new registry mechanism is invented for a contingency that is empty today.

`checker_of` and the CORE floor are read, not changed: the floor is why deleting the item was rejected
rather than considered.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict adversarial
diff fold unattended close build-complete DoD stall halt`.

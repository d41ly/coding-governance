# TOOL-aBoundedVerdict-18 — the two checks that cannot fail get subjects

**Status:** SPECCED · rev-1 · 2026-08-19 · node c · Tier-1 · base 098bebd9 · streams tooling

## 1. Goal

Two close-path checks are green because nothing they could catch is reachable: the
`landed-via-lander` Definition-of-Done item is two conf-non-empty tests plus a grep the merge bar has
already run inside the same close, and the gate leg's check 8 exempts terminal records and every
tracked record is terminal, so it has zero subjects while three of them carry exactly the bytes it
exists to refuse. Give each one a subject, or say in the source why it has none.

## 2. Scope (IN)

- **S1** — `landed-via-lander` gains an observation only the driver can make. Today it asserts that
  `LANDER` and `BYPASS_BAN` are non-empty and that the run-state file does not contain the flag —
  three facts, of which the third is leg check 11's job and the first two are that the conf parsed.
  The item is named for whether the landing WENT THROUGH the lander, and that is observable at
  `--landed` and nowhere else.
- **S2** — if no such observation is available without a mechanism this build does not want, the item's
  scope is stated honestly in the protocol's Asserts cell and the redundant grep is DELETED rather than
  left to imply a check. An item that says less is better than one that implies more; the deletion is
  the acceptable outcome and the spec says so up front.
- **S3** — leg check 8's terminal exemption either goes, or gains a comment stating why retired bytes
  are exempt. Measured: all seven tracked run-state records are terminal, so the check has zero
  subjects, while three of them carry 1280, 3082 and 4032 bytes of the copied unit list the check
  exists to refuse.
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
- Not a general vacuity sweep of the other seventeen leg checks. The audit examined four; the rest are
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
place the driver sees the landing at all. Whether it can observe that the push went through `$LANDER`
rather than through a bare `git push` is the open question, and S2 exists because the honest answer may
be no.

### Check 8, as it stands

The check refuses a run-state file carrying a copied unit list — the staleness the main redesign removed
by making the unit list derived. It exempts `LANDED` and `ABORTED` records. Every tracked record is one
or the other. So the check has no subjects at all, and three of the exempt records carry the exact bytes
it refuses, in quantity.

Two readings, and they lead to different fixes:

- the exemption is CORRECT and retired bytes are history that must not be rewritten — in which case the
  check is fine and needs S5's note plus S4's fixture, because its correctness is currently indistinguishable
  from its emptiness;
- or the exemption was a convenience that let the corpus pass — in which case it goes, and three records
  need either repair or a waiver.

S3 forces the choice rather than leaving it implicit, and F1 is where it is made.

### Inventory

| Concern | Today | After |
|---|---|---|
| `landed-via-lander`'s failure modes | none attributable to the run | one real observation, or an honest narrower claim |
| its redundant grep | duplicates leg check 11 | deleted |
| leg check 8's subjects | zero, corpus-wide | non-zero, or a stated reason for zero |
| check 8's evidence | a corpus that cannot trigger it | a red fixture |
| why either check is narrow | unrecorded | a dated note in source |

### Migration

Depends on F1. If check 8's exemption goes, three tracked terminal records carry bytes it refuses, and
they must NOT be rewritten — a terminal record is a record. So the migration is a waiver registry entry
naming those three, shrink-only, which is how this repo already handles a measured pre-existing
population. If the exemption stays, there is no migration.

### Rollout

S5 and S4 first: they are additive, they cost nothing, and they make the current state legible before
it changes. Then S3's decision and its consequence. S1/S2 last, because the answer to whether
`--landed` can observe the lander decides which of the two it is.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the item's arm) · `tools/unattended/check-unattended.sh` (check 8) ·
`tools/unattended/check-unattended.test.sh` (S4's fixture) ·
`tools/unattended/unattended.test.sh` · possibly a waiver registry beside the other `*.txt` lists ·
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (the Asserts cell,
if S2 fires) · the kit version constant.

### Alternatives rejected

- **Delete `landed-via-lander` outright.** Rejected: the CORE DoD set is shrink-only by a declared
  floor, so deleting a member is a reason-free override of everything keyed on it.
- **Have the driver parse the lander's own output to prove it ran.** Rejected: it couples the kit to a
  project-declared command's output format, which is the one thing `LANDER` exists to keep opaque.
- **Leave check 8 as it is and accept the vacuity.** Rejected on this repo's own rule: a check that
  cannot fail is recorded as such or fixed, never left to read as coverage. S5 is the minimum acceptable
  outcome and it is still a change.
- **Repair the three terminal records so check 8 has clean subjects.** Refused: a terminal record is a
  record, and rewriting one to satisfy a check written later is the opposite of what the freeze is for.

## 5. Production-readiness checklist

- **security** — N/A as a surface. One note: S2's honest narrowing must not read as a strengthening. If
  the item ends up claiming less, the protocol cell says less.
- **perf / scale** — S1's deletion removes one grep per close.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — the empty case IS the subject of this unit.
- **observability** — S5's dated notes are the observability deliverable: they let a reader distinguish
  a narrow check from an empty one without re-measuring.
- **risks** — low. The one real risk is S3 resolving toward removing the exemption and the three
  affected records being repaired rather than waived, which Migration forbids explicitly.
- **testing + left-shift gates** — S4 is the left-shift and it is the point of the unit.
- **migration / rollback** — see Migration; conditional on F1.
- **user docs** — the protocol's Asserts cell, only if S2 fires.

## 6. Acceptance criteria

- **AC1** — When leg check 8 runs against a fixture holding a NON-terminal run-state record carrying a
  copied unit list, it reds naming the file; the red fixture in
  `tools/unattended/check-unattended.test.sh` that does not exist today.
- **AC2** — When `bash tools/unattended/check-unattended.sh` runs against the real tree it is clean, and
  `tools/unattended/check-unattended.sh` carries a dated note saying its check-8 subject count over this
  corpus was measured at zero.
- **AC3** — When `grep -c 'BYPASS_BAN' tools/unattended/unattended.sh` is compared before and after, the
  `landed-via-lander` arm no longer greps the run-state file for the flag — the redundancy S1 removes.
- **AC4** — When `landed-via-lander` is driven with `LANDER` declared and the run-state file clean, it is
  met; when the item's claim is narrowed by S2, the Asserts cell in both halves of the protocol pair
  says what it now asserts and `bash tools/unattended/check-unattended.sh` is clean over the pair.
- **AC5** — When either check's source is read, it carries the S5 note, and
  `python tools/memory-tree/check-arms.py` is clean with any changed `ARMS_FLOORS` entry updated.
- **AC6** — When the three terminal records carrying copied unit lists are inspected after this unit,
  `git diff` over `memory/builds/*/RUN.md` is empty for them — the arm that proves Migration's
  prohibition held.

## 7. Gates

`tools/unattended/check-unattended.sh` + `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`python tools/memory-tree/check-arms.py` · `tools/check-testsuite-counts.sh` ·
`tools/check-kit-versions.sh` · `bash tools/run-gates.sh`.

## 8. Open questions

- **F1 — does check 8's terminal exemption stay or go?** Measured: it has zero subjects, and three
  exempt records carry the bytes it refuses. Staying means the check is correct and merely
  unexercised, which S4 and S5 make legible. Going means three records need a shrink-only waiver,
  because repairing them is forbidden. **Recommendation: it STAYS, with S4's fixture and S5's note.**
  Grounds: the bytes in question are in terminal records the redesign has already superseded, and a
  check that fires on frozen history produces a red nobody can clear — which is a worse defect than the
  one it would catch.
  RESOLVED (agent, 2026-08-19, delegated): stays. Mechanism-only fork, and the alternative creates an
  unclearable red on frozen records.

- **F2 — OWNER, not delegated. Can `--landed` observe that the push went through `$LANDER`, and is it
  worth a mechanism?** Options: parse the lander's output (rejected in §4 as coupling); have the lander
  write a marker the driver reads (a change to a project-declared contract, so an owner call); or accept
  S2 and let the item claim less. The options differ in what gets built and one of them changes what
  `LANDER` means for every adopter, so §3's fork rule sends it up.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's mediums 7 and 31, kept as one
  unit because both are the same class — a check green for want of a reachable subject — and the fix for
  both is a fixture plus an honest statement rather than new logic. Tier 1: no contract another kit
  reads is changed, and the one item that might narrow its claim does so in a documented cell. F1
  resolved under the delegated fork rule; F2 raised to the owner because one of its options changes what
  a project-declared value means.

## 10. Reuse audit

Two seams, both existing. Leg check 11 already owns the bypass-flag ban over the run-state file, which is
why S1's deletion is a deletion and not a move — the predicate has a home and this item was a second
copy of it. And the shrink-only `*.txt` waiver registry pattern beside the other gate lists is what
Migration would use if F1 had gone the other way; naming it means no new registry mechanism is invented.

`checker_of` and the CORE floor are read, not changed: the floor is why deleting the item was rejected
rather than considered.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict adversarial
diff fold unattended close build-complete DoD stall halt`.

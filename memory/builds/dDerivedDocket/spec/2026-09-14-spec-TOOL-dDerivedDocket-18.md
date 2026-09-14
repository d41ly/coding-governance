# TOOL-dDerivedDocket-18 — leg second opinions over the ask mandate

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

Unit 16 makes the driver pin an ask mandate at preflight and unit 17 grades it at close, but both
answers are written into a run-state file by the run being graded. Give the unattended leg its own
reading of each mandate fact, re-derived from inputs the run cannot move, so that a forged,
mistaken or stale fact reds the bar instead of certifying itself. This is the pattern check 19
already applies to `authorized-by:`, `playbook:` and `pieces:`
(`tools/unattended/check-unattended.sh:1387-1418`), extended to the four facts the ask path adds.

## 2. Scope (IN)

- **S1** The `asks:` fact against the build README. The leg re-parses the `asks:` front-matter line
  from the README blob at the recorded BASE, the blob check 19 already reads, and requires it
  byte-equal to the recorded fact. For a non-terminal record it also requires the README at HEAD to
  carry the same bytes, which is property P6 seen from the leg. Observed by AC1 and AC2.
- **S2** P5 re-derived. For every mandated id the leg requires the ask row `- <id> · filed ` in the
  home build's `BACKLOG.md` at the recorded `m-base:`, and it checks `m-base:` itself against the
  pinned `anchor-sha:`, never against `base:` (fix F4). Observed by AC3 and AC4.
- **S3** The folder-wide anchor ban. For a record carrying an `asks:` fact, no tracked file under
  that build's folder may carry a line that anchors an id whose slug is not this build's, judged by
  the memory-recall kit's own `anchor_at`, never by a copy of its shapes. Observed by AC5 and AC6.
- **S4** The freeze is present. Every record whose phase is LANDED and that carries an `asks:` fact
  carries an `asks-at-landing:` fact naming every mandated id. Observed by AC7.
- **S5** One authorization path (owner ruling D12-a). A record carrying an `asks:` fact must record
  mode `slug`, and no record may carry one while the conf's `ASKS_CMD` is blank. Observed by AC8.
- **S6** Every arm is vacuous without an `asks:` fact and says so on one line, with the count of
  mandated records it examined. Observed by AC9.
- **S7** Every new `fail` branch gets an arm in `tools/unattended/check-unattended.test.sh`, and
  `ARMS_FLOORS` moves in the same commit. Observed by AC10.

## 3. Non-goals (OUT)

- Pinning any fact. The driver's preflight pins `asks:`, `asks-ready:` and `m-base:` (unit 16) and
  `--landed` writes `asks-at-landing:` (unit 17). This unit only reads.
- Re-deriving READY or any ask status. That is the fold's (unit 6), printed by unit 15's
  `--asks --tsv`, and a second implementation of status would be a second answer to one question.
- Check 13's claimant rule across the whole corpus is the memory-tree engine's, refined by D12-g in
  unit 15. S3 is narrower: it covers the run's own folder for every foreign id, legacy ones included,
  which is where the 27 hazard ids came from (DR §19.1 K9).
- Moving the freeze to `--close` (unit 22) changes which phases S4 grades. Unit 22 extends S4 to a
  derived-LANDED record in the same commit that moves the freeze; this unit grades recorded LANDED.
- The real-tree staged RED of S3 on a typed resolution table is unit 35's.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-16` — the pinned `asks:`, `m-base:` and `anchor-sha:`
  facts, `ASKS_CMD`, and the ask-row line matcher the driver's P5 uses. Without them S1, S2 and S5
  have nothing to compare.
- **consumes-from** `TOOL-dDerivedDocket-17` — the `asks-at-landing:` fact S4 requires on a landed
  record.
- **hands-off** `TOOL-dDerivedDocket-35` — the real-tree staged RED of S3, a typed resolution table
  in a mandated run's folder, after gov sets `ASKS_CMD`.

## 4. Design

### Which inputs each arm trusts

| Arm | Reads | Never reads |
|---|---|---|
| S1 | the README blob at the recorded BASE, and at HEAD for a live record | the driver's own parse |
| S2 | the pinned `anchor-sha:`; the commit that first recorded `m-base:`; the home `BACKLOG.md` blob at `m-base:` | `base:`, and any working-tree file |
| S3 | tracked files under the run's build folder; the recall kit's `anchor_at` | a local list of anchor shapes |
| S4 | the record's own facts | the witness, which may have moved since landing |
| S5 | the record's `mode:` and the conf's `ASKS_CMD` | anything the Skill printed |

### S2, the m-base re-derivation

`m-base:` is merge-base(`anchor-sha:`, HEAD at preflight), both frozen commits, so equality is safe
here in a way it is not for check 9. Check 9 had to move to ancestry because a merge-base computed
NOW moves after landing (`tools/unattended/check-unattended.sh:1202-1208`); a merge-base of two
frozen commits never moves. HEAD at preflight is the first parent of the earliest commit whose copy
of the record carries the `m-base:` line, because preflight refuses a dirty tree and stages the
record, so the next commit carries it.

Where that commit cannot be found, as in a rotated record whose path changed, or a shallow clone,
the arm falls back to two ancestry tests: `m-base:` is an ancestor of `anchor-sha:` and of the
record's HEAD. It announces the weaker reading by name, so a green row is never read as the
equality test. The ask-row match itself is the SAME line matcher the driver's P5 calls, shared
through the kit library: the second opinion's independence lies in its inputs, never in a second
grammar, which would be a second implementation and not a second opinion.

### S3, the anchor ban

The extractor is reached through the declared `RECALL_CLI`, whose directory holds the recall kit's
extractor. That keeps the kit file from naming a sibling kit by literal, which the install-prefix
gate bans. A blank `RECALL_CLI`, or an extractor that does not import, SKIPS S3 with a line saying
which, never a pass. The arm runs one interpreter per folder, feeding every line of every tracked
file under it, and collects `(file, line, id)` for each anchor whose slug is not the folder's.

Why a foreign slug and not "an id whose ask row is filed elsewhere": both a foreign ask id and a
foreign unit id anchored in this folder make this build a second claimant under check 13, and the
narrower predicate would need the witness, which S3 deliberately does not read.

### Fail codes

S1, S2 and S5 are declaration second opinions and report under check 19, beside the arms they
extend. S4 is a terminal-record fact and reports under check 15. S3 is a new class and takes a new
leg code, allocated at build time as the next integer above the leg's highest, because other units
of this build allocate leg codes concurrently.

### Rollout

Dark by construction. No record carries an `asks:` fact until a run is pointed at asks after unit
35 arms gov, so every arm announces vacuity on every bar until then. The fixtures carry the
coverage in the meantime.

### Inventory

No new fact, conf key or verb. One leg code for S3, number allocated at build time. Any new shell
function is named through `python tools/lexicon/lexicon.py --suggest <identifier> --as <cell>`.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/lib-unattended.sh`, only if unit 16's matcher is not already there ·
`.memory-tree.conf` for `ARMS_FLOORS` · `memory/map/features/unattended.md`.

### Alternatives rejected

- **A subset arm over the prompt record's IDLIST (fix F2 as first adopted).** Owner ruling D12-a
  makes every ask-driven run start from an owner-landed README, and an ids invocation writes nothing,
  so no run-written IDLIST exists to compare. F2's check becomes S1 plus S5; see §8 F1.
- **Reading anchors with a local regex copy.** Two copies of one grammar disagree silently, which is
  derive critique F13's own finding against the view's selftest (DR §5.3).
- **Ancestry-only for `m-base:`.** It passes a pin moved to any older common commit. Kept only as
  the announced fallback.

## 5. Production-readiness checklist

- security — every arm reads committed blobs or the record; the anchor extractor runs over tracked
  text and executes nothing it reads.
- perf / scale — per mandated record, two `git show` calls for S1, one per mandated id for S2, and
  one interpreter per folder for S3. Zero mandated records today, so the leg's cost does not move.
- error / empty / loading states — no `asks:` fact is announced vacuity; an unreadable blob or an
  unresolvable `m-base:` is a named refusal; a missing extractor is a named skip.
- observability — one line per arm per mandated record, and one summary count line per run.
- risks — S2's equality depends on preflight staging the record before any other commit, which
  unit 16's preflight inherits from today's; the fallback covers the cases where it cannot be shown.
- testing — one fixture per arm in `tools/unattended/check-unattended.test.sh`, each observed RED;
  the unattended suites run once at the unit's end (D12-h).
- migration — none; every existing record is vacuous.
- user docs — none beyond the leg's own header comments, which state what each arm does NOT check.

## 6. Acceptance criteria

- **AC1** — When a fixture record's `asks:` fact differs by one id from the README line at its
  recorded BASE, `bash tools/unattended/check-unattended.sh` reds check 19 naming both values.
  Red when: the arm compares the fact against the driver's parse, or against the README at HEAD
  only, so a README edited after BASE agrees with a forged fact.
- **AC2** — When a live fixture record's README at HEAD carries an `asks:` line that differs from the
  one at BASE, check 19 reds; the same README on a LANDED record does not red.
  Red when: the HEAD half grades terminal records, so a later edit to a landed build's README reds
  the bar forever.
- **AC3** — When a mandated id has no ask row in its home `BACKLOG.md` at the fixture's `m-base:`,
  check 19 reds naming the id and the blob it read.
  Red when: the arm reads the working tree, so a row filed after the run started satisfies it.
- **AC4** — When a fixture's recorded `m-base:` is replaced by an older ancestor of `anchor-sha:`,
  check 19 reds; when the introducing commit cannot be found, the arm prints that it fell back to
  ancestry.
  Red when: the arm derives the merge-base from `base:`, or the fallback runs silently.
- **AC5** — When a mandated fixture run's folder carries a table row whose first cell is a
  backticked foreign id, the new S3 check reds naming the file and line; a link-wrapped first cell
  does not red.
  Red when: the arm uses a local shape list that misses the backticked first cell `anchor_at`
  admits.
- **AC6** — When `RECALL_CLI` is blank in the fixture conf, the S3 arm prints a skip line naming the
  key and the leg exits on its other arms' verdicts alone.
  Red when: a blank key reads as zero anchors found.
- **AC7** — When a LANDED fixture record carrying an `asks:` fact has no `asks-at-landing:` fact,
  check 15 reds; with the fact present it passes.
  Red when: the arm grades only records with no `asks:` fact, the population where it cannot fire.
- **AC8** — When a fixture record carries an `asks:` fact with mode `prompt`, or carries one while
  `ASKS_CMD` is blank, check 19 reds.
  Red when: either combination passes, so a run-authored mandate carries a pinned ask set.
- **AC9** — When the leg runs over today's tree, it prints one line stating that no record pins an
  `asks:` fact, with the count 0.
  Red when: the leg prints nothing, so vacuity reads as a pass.
- **AC10** — When `bash tools/unattended/run-unattended-gates.sh --selftests` runs once at the end
  of the unit, every arm this unit added passes and each was observed RED with its fix unstaged;
  the run shows no NEW failure against unit 1's baseline.
  Red when: an arm is wired without its failing case ever being seen.
  cost: one run of the unattended suites, the unit's single sanctioned suite run (D12-h).

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/check-unattended.test.sh` · one fixture record per arm S1 to S5 carrying the break, plus a vacuous fixture · `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`

## 8. Open questions

- **F1 — what does fix F2's IDLIST arm check once D12-a drops the ids start?** F2 was adopted
  against E2, where the run wrote a prompt record holding the IDLIST. Under D12-a an ids invocation
  prints the recipe and writes nothing, the owner lands the scaffolded README, and the run starts as
  E1. The only record of the list is then the README's `asks:` line, which S1 already
  second-opinions. A provenance stamp written by the scaffold was considered and rejected: it would
  widen unit 15's output and create a second carrier of one list. RESOLVED (agent, 2026-09-14,
  delegated): F2's arm reduces to S1 plus S5.
- **F2 — may the leg reach the recall kit's extractor at all?** It must not name the kit by literal.
  RESOLVED (agent, 2026-09-14, delegated): through the declared `RECALL_CLI`, with a blank key an
  announced skip, which is the kit's existing adoption idiom for that key.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR §19.8 U13, fixes F2 and F4, and ruling D12-a. Adds one
  edge the brief's table does not carry: hands-off unit 35, which DR §19.8 U15 names as staging the
  leg's RED on a typed resolution table. The IDLIST arm of fix F2 is reduced under D12-a (§8 F1).

## 10. Reuse audit

The seam is check 19 in `tools/unattended/check-unattended.sh`, which already re-parses front
matter from the README blob at the recorded BASE and compares it against recorded facts; S1 and S5
are two more keys through that same blob and `awk`. The anchor judgement reuses
`tools/memory-recall/extract.py`'s `anchor_at` rather than a copy. `reuse_lookup.py "second opinion
leg re-derives a run fact against the build README at BASE"` returns only generic python helpers,
because the lookup reports `.sh` as an unscanned layer and so cannot see the leg; the `unattended`
dossier's shared seams name no second re-derivation mechanism, and none is built. Where DR and the
source disagree: DR places check 19 at `:1395-1418`, and at BASE the membership and agreement arms
start at `tools/unattended/check-unattended.sh:1387`; nothing else moved.

Recall terms used: `second-opinion check-19 recorded-BASE authorization-mode playbook anchor-ban
resolution-table foreign-id landed-anchor units-at-landing leg-arm skip-announce`

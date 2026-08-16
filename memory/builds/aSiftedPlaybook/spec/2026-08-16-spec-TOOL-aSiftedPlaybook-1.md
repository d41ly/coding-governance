# TOOL-aSiftedPlaybook-1 — the template ceiling moves to 48 KiB, as a recorded rule reversal

**Status:** SPECCED · rev-6 · 2026-08-16 · node a · Tier-2 · base 91ef1b05 · streams tooling · ratified 2026-08-16

## 1. Goal

Raise the enforced template ceiling from 32768 to 49152 bytes on owner order, and move every
carrier that states the old limit or the never-raise rule, so the repo does not keep instructing
agents to obey a rule it no longer enforces. Record the reversal as a decision that names the prior
records which relied on the old ceiling, because at least three of them cited it as binding.

## 2. Scope (IN)

- **S1 — the constant, and ONLY the innermost default.** `tools/check-template-size.sh:19` now reads
  `MAX_BYTES=${2:-${MAX_BYTES:-32768}}`. **Only the `32768` moves to `49152`**; the positional and
  environment layers are untouched, and the trailing rule comment at `:19-20` is rewritten.

  **This gate has a SECOND consumer and the raise must not reach it.** `tools/gate-legs.json` carries
  `kickoff engine size <=18KiB`, which runs
  `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md 18432` — the positional exists
  precisely because a leg cannot set an environment variable. That consumer passes its own limit, so
  it is insulated by construction: raising the default cannot move it. Verified rather than assumed,
  because the alternative reading — that the default is the ceiling for everything riding the
  script — would have silently raised the kickoff engine's cap from 18 KiB to 48 KiB.
- **S2 — the gate's own prose.** Same file: the header rule statement at `:2-5` ("never inflating
  the template"), the usage echo `MAX_BYTES=32768` at `:8`, and the FAILURE MESSAGE at `:31-32`
  ("Do NOT raise the limit"). The failure message is the string an agent reads at the exact moment
  it is over budget, so it is the highest-value line in the file to get right — and it is now shared
  by two consumers, so its wording must stay true for the kickoff engine at 18 KiB as well as the
  playbook at 48.
- **S3 — the charter.** `AGENTS.md:16-17` (the most emphatic never-raise carrier — the sentence
  SPANS the line break, "…trim or externalize, never" / "raise the limit)", so an edit scoped to
  `:16` alone orphans the rest), `:97` (the gate-suite leg bullet, which now also names the kickoff
  engine riding the same script — that clause stays true and must survive the edit), `:197` (the
  Conventions restatement), and `:7` (which calls `baseline.toml` shrink-only — see S6). Note `:97`
  spells `≤32 KiB` with a unicode `≤` while the leg itself spells `<=32KiB`, so a grep for the leg
  name alone misses it.
- **S4 — the adopter-facing README.** `README.md:12` (the ceiling claim) **and `README.md:33`**,
  which still reads "a 19-check hygiene gate" against the true 20. `PLAY-aSiftedPlaybook-1` §3 routes
  that carrier here because this unit already edits the file; it is received here rather than merely
  pointed at, which is the defect that shape produced once already.
- **S5 — the kickoff manifest trap, at its NEW path.** The manifest moved to
  `memory/guides/SESSION-KICKOFF.md` (commit `24f3991`, `KICK-cKeyedLaunchpad-2`); the old
  `memory/guides/SESSION-KICKOFF.md` no longer exists. The trap is now three lines at `:121-123`:
  "The template is under a STRICT 32 KiB gate. Never raise it; externalize into … Read the current
  margin FROM `bash tools/check-template-size.sh`, never from prose."

  **The edit is much smaller than it was.** The measured-figure-plus-funding-policy paragraph this
  unit was scoped to delete is already gone — main trimmed it and replaced it with the
  read-the-margin-from-the-gate instruction, which is CORRECT and stays. What remains is the ceiling
  sentence and the never-raise clause, plus a line naming the ratchet from S8.
- **S6 — the decision record, covering BOTH reversals.** A new `memory/DECISIONS.md` row minting the
  ceiling reversal and naming the four records that relied on the old ceiling —
  `PLAY-aCandidStub-1` §3, `TOOL-aGuardedTally-1`, `PLAY-aPrunedCeremony-1` RD7, and the
  `aCandidStub` review's refuted id 19. Append-only: nothing prior is edited.

  **This build reverses TWO rules, not one.** F1's in-place `baseline.toml` key swap is the second:
  `memory/map/baseline.toml:3-4`, `AGENTS.md:7` and `compute_coverage`'s docstring all still assert
  the file only shrinks and that additions are reserved for the initial backfill. That exception is
  recorded in the same row and annotated in the `baseline.toml` header in place, dated. Precedent:
  `tools/drift-audit/drift_signals.py` states an exclusion from a shrink-only promise deliberately
  and in writing rather than by omission. A reversal recorded only in a spec's §8 is a reversal
  nobody downstream can find.
- **S7 — the gate-leg label and its inventory key** (F1, resolved). `tools/gate-legs.json:17`
  becomes `template size <=48KiB`, and `memory/map/baseline.toml:35` is edited IN PLACE to the new
  key. `memory/map/generated/{MAP.md,inventories.json}` are regenerated with
  `python tools/codebase-map/gen_map.py --write`, never hand-edited. No dossier is minted by this
  unit.
- **S8 — the growth warning, as a HIGH-WATER RATCHET** (F2 + B2, resolved). Not a fixed threshold.
  The gate records the template's size in a tracked file, `tools/template-size-highwater.txt`, and
  prints a `TEMPLATE-SIZE WARN` line — still exiting 0 — whenever the measured size EXCEEDS the
  recorded value. Raising the recorded value is a deliberate act visible in the diff, via a
  `--bump` mode that rewrites the file and says by how much.

  **Why not a constant.** Measured: this build lands the template near 34963 bytes, 71% of 49152.
  Every conventional fraction is silent through the whole build and several KiB beyond it (80% =
  39321, 90% = 44236), while any constant low enough to price these edits sits at or below 32768 and
  fires on every run forever — the permanently-red decoration `tools/drift-audit/drift_signals.py:113`
  names as an anti-pattern. A ratchet has neither failure mode: it is silent until something grows,
  and it prices EVERY growth, which is the forcing function the 32 KiB ceiling was actually
  providing and the one F2 set out to replace.

  **The record is KEYED BY MEASURED FILE**, one `<path>	<bytes>` row per subject. This gate has two
  consumers (S1), and a single un-keyed number cannot serve both: `skills/session-kickoff/SKILL.md`
  is 18215 bytes against a template of 32682, so under a template-sized high-water the kickoff leg
  could never warn, and a `--bump` on that leg's argv would rewrite the record to ~18215 — after
  which the template leg prints WARN on every run forever.

  **The record's PATH resolves like `MAX_BYTES` does** — a third positional, then an environment
  variable, then the tracked default — because a gate leg cannot set an environment variable and
  `TOOL-aSiftedPlaybook-2`'s arms must point the gate at a scratch copy without writing the tracked
  one. `--bump` writes to the same resolved path.

  **Absent or malformed record.** An absent file means no ratchet plus one explicit line saying so —
  never a silent pass, and never a `set -u` explosion on an empty operand at the numeric comparison.
  Non-numeric content is a named failure. Both are armed in `TOOL-aSiftedPlaybook-2` S2.

  **Seeding is NOT this unit's act** (B3). This is unit 1 of 7 and the template is not edited until
  units 4-6, so a value seeded here is either the pre-build 32682 — which makes every run from
  `PLAY-aSiftedPlaybook-2` onward print WARN forever, the permanently-red shape this section exists
  to avoid — or a forecast, which carries a number out of a spec paragraph. This unit seeds at the
  size it measures when it lands and **states that units 5 and 6 are expected to fire the warn**;
  `PLAY-aSiftedPlaybook-3`, the last template-touching unit, owns the closing `--bump`.
- **S9 — the backlog row the raise falsifies.** `memory/backlog/PLAY.md:7` reads
  "`PLAY-aCandidStub-2` · OPEN · the template is effectively FULL at v2.5 and the §11
  externalization spent the cheap slack". The owner kept that row OPEN but re-justified it on
  readability, so its stated rationale is now false. Rewrite it to the readability justification.
  Not cosmetic: this spec's own §1 argues that a constant changed under records that cite it leaves
  them "reading as current guidance", and leaving this row would be that exact failure inside the
  unit whose purpose is to prevent it.

## 3. Non-goals (OUT)

- **Changing the externalization POSTURE.** The ceiling moves; the preference for putting
  activity-scoped prose in a companion does not. The rewritten rule keeps that preference and
  changes only its absoluteness. Stated because an agent reading "the limit went up" could
  reasonably infer the discipline was withdrawn, and it was not.
- **The gate's missing self-test.** `TOOL-aSiftedPlaybook-2`. Discovered while specing this unit and
  deliberately split: this unit changes a number, that one changes what the bar proves.
- **Historical records.** ~45 hits under `memory/builds/**` are past measurements in landed specs,
  reviews and build logs. `memory/DECISIONS.md` is append-only and `memory/archive/**` is frozen.
  None is edited.
- **Spending the new headroom.** `PLAY-aSiftedPlaybook-3` spends it; **its §4 cost table owns the
  figure** and this spec deliberately does not restate it. An earlier draft here said 1593 bytes,
  which was that unit's pre-`gate-lint` total — the second-copy defect this build exists to close,
  committed by the unit that justifies the raise.

## 4. Design

### Inventory

Tracked lines outside historical records, across the files below plus the append-only
`memory/DECISIONS.md` — the table is the inventory and the count is stated once here rather than
being maintained in two places. Verified negatives are as
load-bearing as the hits: the three `parallel-coding-governance*.md` files, `WIRE-INTO-PROJECT.md`,
every kit `*.template.md` and every rendered `.claude/skills/**` state the limit **nowhere**, so the
raise touches no shipped adopter artifact.

| File | Lines | Class |
|---|---|---|
| `tools/check-template-size.sh` | 19 | the constant — innermost default of `${2:-${MAX_BYTES:-32768}}` only |
| `tools/check-template-size.sh` | 2-5, 8, 31-32 | rule statements + usage echo |
| `AGENTS.md` | 16-17, 97, 197, 7 | rule statements (`:97` also names the second consumer; `:7` the baseline claim) |
| `README.md` | 12 | rule statement |
| `memory/guides/SESSION-KICKOFF.md` | 121-123 | rule statement — the file MOVED (`24f3991`) |
| `tools/template-size-highwater.txt` | new | S8's ratchet record, keyed by measured file |
| `tools/govkit/registry.toml` | + row | S8's new depth-1 path must be DECLARED or `govkit selfcheck` reds — see below |
| `tools/gate-legs.json` | 17 | the leg label — see F1 |
| `memory/map/baseline.toml` | 35 | the label as an inventory key — see F1 |
| `memory/map/generated/inventories.json` | 46 | generated mirror of the key |
| `memory/map/generated/MAP.md` | 53 | generated mirror of the key |
| `memory/DECISIONS.md` | append | S6's reversal row — append-only, nothing edited |
| `memory/backlog/PLAY.md` | 7 | S9 — the `PLAY-aCandidStub-2` row whose rationale this unit falsifies |

### The blast radius, measured rather than assumed

The charter's documented trap says "Adding ONE gate leg trips FOUR gates at once". That is true for
an ADDED leg and false here, in both directions:

- **A bytes-only change trips exactly ONE gate** — the kickoff-manifest ratchet, because
  `tools/check-template-size.sh` is a watched pathspec at `memory/guides/SESSION-KICKOFF.md:6`, forcing a
  `last-audit` re-stamp with a delta line.
- **Renaming the leg label trips TWO MORE** — codebase-map coverage (the old key reds as
  `stale_baseline` AND the new key reds as `unclaimed`, both at once) and codebase-map freshness
  (`inventories.json` and `MAP.md` are byte-compared against a fresh render).
- **It does NOT trip the drift-audit charter signal.** That probe matches a leg's ARGV SCRIPT PATH,
  not its display name (`tools/drift-audit/drift_signals.py:86-92`). Worth stating explicitly
  because the trap's "four gates" framing would have predicted otherwise and sent the build looking
  for a red that cannot occur.

**With F1 resolved to the in-place swap, this unit trips THREE gates**: the manifest ratchet, plus
codebase-map coverage and freshness. The coverage leg reds in both directions if the swap is done
by halves — the old key as `stale_baseline`, the new one as `unclaimed` — so `tools/gate-legs.json`
and `memory/map/baseline.toml` move in the same commit, and the generated artifacts are re-rendered
rather than edited. S8's WARN touches no gate but changes the size leg's stdout, which is why
`TOOL-aSiftedPlaybook-2` arms it.

### Migration

None. `MAX_BYTES` remains env-overridable, and no adopter reads the constant — the gate ships only
in this repo. A project that copied the gate keeps its own number.

### Rollout

S1-S5 land in one commit, because a tree where the constant and its prose disagree is worse than
either state. S6's decision row lands with them. The manifest re-stamp rides the same commit per the
ratchet's own rule.

### Alternatives rejected

- **Raise to 48 KiB by deleting the gate.** Rejected: the owner ordered a new ceiling, not the
  absence of one, and an unbounded operating ruleset has no failure mode anyone would notice until
  it is far too large to fix cheaply.
- **Keep 32768 and externalize §14 to fund the fixes** (the audit's original sequencing). Rejected:
  the owner has ordered otherwise. Recorded here because it remains the alternative that preserves
  the forcing function, and F2 exists precisely because the raise removes it.
- **Make the ceiling a `.memory-tree.conf`-style declared pin.** Rejected as out of scope, but
  **recorded as a backlog row rather than deferred to a unit that declines it** — an earlier draft
  sent it to `TOOL-aSiftedPlaybook-3`, whose §2 has no ceiling pin and whose §3 forecloses growth.
  The prior art is live and directly on point: `.memory-tree.conf:43-50` declares
  `READ_PATH_CEILING` for the charter's mandatory read path and records each of its three raises
  with the reason beside it — "a session's mandatory reading is a budget, and two binding docs
  growing at once spends from it visibly". That is this repo's established answer to exactly this
  problem, and S8's ratchet is a weaker cousin of it. Worth a real comparison in a later unit.

## 5. Production-readiness checklist

- security — N/A. No write path or surface.
- perf / scale — N/A.
- a11y / i18n — N/A.
- error / empty / loading states — the gate's failure message is rewritten; S2 treats it as the
  primary output, not an afterthought.
- observability — the gate prints its measured byte count and percentage on every run; unchanged.
- risks — **the real risk is silent discipline loss.** At 86 bytes free every template edit was
  priced by the gate. At 16470 free nothing prices one until the headroom is spent. This is not a
  hypothetical: three prior units cite the ceiling as the reason they externalized rather than
  inlined. F2 is where that risk is resolved, and it is unresolved.
- testing + left-shift gates — this unit changes a gate that **has never had its failing case
  observed** (no test file, no `fail()` helper, outside `check-arms.py`'s population). Paying that
  debt is `TOOL-aSiftedPlaybook-2` and it is sequenced immediately after this unit, not "later".
- migration / rollback — revert the commit; the constant is one line and the prose is prose.
- user docs — `README.md:12` is the adopter-facing statement and is in scope as S4.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-template-size.sh` runs, it reports a limit of 49152 and exits 0.
- **AC2** — When a file of 49153 bytes is passed to the gate, it exits 1; when one of 49152 is
  passed, it exits 0. This observes the new boundary rather than asserting the constant, and is the
  minimum honest proof that the number took effect. (The durable version of this check is
  `TOOL-aSiftedPlaybook-2`; AC2 is its one-shot ancestor and must be run by hand here.)
- **AC3** — When
  `git grep -nE '32768|32 ?KiB|never raise the limit|[Dd]o NOT raise|raise the limit|inflating' -- ':!memory/'`
  runs, every surviving hit is either the gate's own history comment or absent entirely.
  **The last three alternatives are load-bearing**: `tools/check-template-size.sh:4` says "never
  inflating the template" and `:25` says "Do NOT raise the limit", and neither matches the original
  three-token pattern. Without them S2 could be skipped in its entirety and every AC would still
  pass, shipping a gate that tells an over-budget agent not to raise a limit the owner just raised.
- **AC3b** — When `bash tools/check-template-size.sh <over-limit-file>` is run, the emitted failure
  message is read and contains no instruction not to raise the limit. AC3 observes the ABSENCE of
  old strings; this observes the PRESENCE of the correct one, and S2 calls that message the
  highest-value line in the file.
- **AC4** — When `bash skills/session-kickoff/manifest-check.sh` runs, it exits 0, and
  `memory/guides/SESSION-KICKOFF.md`'s `last-audit` carries a stamp newer than BASE with a delta line in
  the commit message.
- **AC5** — When `python tools/codebase-map/test_codebase_map.py` runs, coverage reports neither an
  `unclaimed` key nor a `stale_baseline` entry for the size leg, and the freshness byte-compare is
  green against a fresh `gen_map.py --write` render.
- **AC7** — With `tools/template-size-highwater.txt` holding a value H and `MAX_BYTES` at 49152:
  a file of H bytes exits 0 and prints **no** warn line; a file of H+1 bytes **exits 0 AND prints
  the warn line** naming H, H+1 and the delta; a file of 49153 bytes still exits 1. The middle case
  is what proves the ratchet is advisory rather than a second ceiling, and it is the case a
  hand-written check omits. `--bump` rewrites the file to the measured size and reports the delta.
- **AC9** — When `bash tools/check-template-size.sh` runs immediately after THIS unit lands, it
  prints no warn line, because S8 seeds the record at the size measured then. It is EXPECTED to warn
  during units 5 and 6; `PLAY-aSiftedPlaybook-3`'s closing `--bump` is what returns the tree to
  quiet, and that unit owns the observation. A ratchet that ships already firing is
  the permanently-red shape S8 exists to avoid.
- **AC8** — When `grep -n 'template size' tools/gate-legs.json memory/map/baseline.toml` runs, both
  spell `<=48KiB` and neither still spells `<=32KiB`.
- **AC6** — When `memory/DECISIONS.md` is read, a new row records **both** reversals — the ceiling
  and the `baseline.toml` exception — and names all four records whose premise the ceiling change
  falsifies: `PLAY-aCandidStub-1`, `TOOL-aGuardedTally-1`, `PLAY-aPrunedCeremony-1` RD7, and the
  `aCandidStub` review's refuted id 19. No prior row has been edited. §10's recall result and this
  list are the same four; a mismatch between them was how RD7 nearly went unrecorded.
- **AC6b** — When `memory/map/baseline.toml`'s header is read, it carries the dated exception for
  the in-place swap, so the file's own shrink-only claim is qualified where a reader meets it.
- **AC10** — When `memory/backlog/PLAY.md:7` is read, the `PLAY-aCandidStub-2` row is still OPEN and
  its justification names per-session readability, with no claim that the template is full.
- **AC12** — When `python tools/govkit/govkit.py selfcheck` runs, it is green with
  `tools/template-size-highwater.txt` declared. A new depth-1 path under `tools/` reds this leg by
  design, and three units in this build create one.
- **AC11** — When `python tools/drift-audit/drift_report.py --check` runs after S3's edits,
  `handkept_inventories_disagreeing_with_source` still reports 0 at pin 0. **The dangerous edit is
  the `AGENTS.md` gate-suite rewrite, not the leg rename**: `_charter_mentions_every_leg`
  (`tools/drift-audit/drift_signals.py:104-136`, the argv-path match at `:132-136`) credits a leg
  only when one of its argv paths appears verbatim in that section. **At least one surviving line
  must still spell `tools/check-template-size.sh` after S3's edits** — not `:97` specifically, since
  the merge added `:98` spelling it too for the kickoff-engine leg. §4's blast-radius analysis clears
  the RENAME and says nothing about this.

## 7. Gates

- `bash tools/check-template-size.sh` — the subject.
- `bash skills/session-kickoff/manifest-check.sh` — `tools/check-template-size.sh` is a watched
  pathspec; the re-stamp is mandatory, not optional.
- `python tools/codebase-map/test_codebase_map.py` — F1 resolved to a rename, so this is mandatory,
  not conditional. Coverage AND freshness.
- `python tools/drift-audit/drift_report.py --check` — expected unaffected by the rename per §4; run it to
  confirm that rather than trust the analysis. Also guards the landmine below.
- `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gotchas.py --for-diff`.
- `python tools/govkit/govkit.py selfcheck` — **mandatory, and new since the merge.**
  `tools/govkit/registry.toml` asserts a depth-1 `tools/*` surface and fails on any tracked path
  that is "neither an entry member nor an exemption". S8 creates one such path, so the declaration
  lands in the same commit. An `[[exempt]]` row is the right shape: `tools/check-template-size.sh`
  is already exempt and exemptions are per-path.
- `bash tools/run-gates.sh` at the push boundary.

**A live landmine for this unit specifically.** `memory/guides/SESSION-KICKOFF.md` is named BY FILE
PATH in the drift signal's `PRODUCT_GLOBS`
and `non_terminal_specs_cited_by_product_source` sits AT its pin of 2 with tolerance 0. S5 rewrites
that manifest's trap; if that rewrite names this spec's id while its status
is non-terminal, the `drift-audit records` leg goes red. The paragraph being replaced documents
having been bitten by exactly this. Reference the change without an id, or land the citation after
the spec closes.

## 8. Open questions

none — the forks below are RESOLVED (owner, 2026-08-16).

- **F1 — what happens to the gate-leg label `template size <=32KiB`?**
  **RESOLVED (owner, 2026-08-16): option 2 — rename to `template size <=48KiB` and edit
  `memory/map/baseline.toml:35` in place.** Built as S7.

  One consequence to carry rather than re-argue. `baseline.toml`'s header, the coverage gate's
  docstring and `AGENTS.md` each state the file is shrink-only and that additions are reserved for
  the initial backfill; an in-place key swap is a delete plus an add through that file. Nothing
  enforces the rule, which is why the option is available at all. Two follow-ons:
  `TOOL-aSiftedPlaybook-2` must now mint `memory/map/features/playbook.md` itself, since this unit
  no longer does and a genuinely NEW leg key is an addition rather than a rename; and
  `TOOL-aSiftedPlaybook-3` keeps the unenforced convention as an explicit non-goal, because a gate
  written to enforce it would red this resolution on the day it landed. The map still has no
  playbook dossier after this unit.

  The original options, kept for the record:

  1. **Leave it.** Zero gate work. The leg then advertises 32KiB while the gate enforces 49152 —
     the same rot class this whole build exists to close, in the build that closes it.
  2. **Rename to `template size <=48KiB` and edit `memory/map/baseline.toml:35` in place.**
     Mechanically GREEN — proved by simulation on the real tree: `compute_coverage` has no
     grew-check, so a swapped key returns `clean=True`. But `baseline.toml`'s own header, the
     coverage gate's docstring and `AGENTS.md` all state the file is shrink-only and that additions
     are reserved for the initial backfill. Four written statements, zero enforcement.
  3. **Rename to a NUMBERLESS label (`template size gate`), claim the new key in a new dossier
     `memory/map/features/playbook.md`, delete the baseline line, regenerate.**

  (Agent recommendation at the time was option 3, on the ground that it followed the documented
  policy and would have closed the missing-playbook-dossier gap. Not taken; recorded so the reasoning
  is not lost if the convention is ever gated.)

- **F2 — what replaces the forcing function the ceiling was providing?**
  **RESOLVED (owner, 2026-08-16): (b) and (c) together** — a soft WARN threshold in the gate, built
  as S8, AND `PLAY-aCandidStub-2` stays OPEN, re-justified on readability rather than bytes.

  Two follow-ons. The WARN changes the gate's OUTPUT contract, so
  `TOOL-aSiftedPlaybook-2` gains an arm for it — a file above the soft threshold and below
  `MAX_BYTES` must exit 0 **and** print the warn line, which is the only combination that proves
  the threshold is advisory rather than a second blocker. And at landing, the
  `PLAY-aCandidStub-2` backlog row needs its rationale rewritten: it currently reads "the template
  is effectively FULL at v2.5", which this unit falsifies, so leaving the row untouched would keep
  it open for a reason that no longer exists.

## 9. Revision log

- rev-6 · 2026-08-16 · folded round-3 blockers B2/B3 and highs H1/H3/H6/H8/H9 plus M3.
  **B3**: AC9 quantified over a state unit 1 cannot reach — the template is not edited until units
  4-6 — so S8 now seeds at ITS landed size, says units 5 and 6 are expected to warn, and hands the
  closing `--bump` to `PLAY-aSiftedPlaybook-3`. **H1**: the record is keyed by measured file, because
  one number cannot serve two consumers 14 KB apart. **H3/M3**: the record's path resolves like
  `MAX_BYTES`, and absent/malformed is a stated contract rather than a `set -u` explosion.
  **B2**: `govkit selfcheck` arrived with the merge and reds on any undeclared depth-1 `tools/` path;
  S8 creates one. **H8**: AC11's two citations were both wrong and its uniqueness premise false —
  the merge added a second carrier at `AGENTS.md:98`. **H6**: `README.md:33` is now RECEIVED by S4.
- rev-5 · 2026-08-16 · folded round-2 mediums and lows. **S9 added** for the
  `memory/backlog/PLAY.md:7` rewrite, which the README and §8 both called a "landing task" belonging
  to no scope item — the failure mode this unit's own §1 names. **AC11 added**: the edit that can
  move the zero-tolerance charter signal is `AGENTS.md:97`, not the leg rename, and §4's blast-radius
  analysis had cleared only the rename. The declared-conf-pin alternative now points at
  `.memory-tree.conf`'s `READ_PATH_CEILING` as live prior art and becomes a backlog row instead of
  being deferred to `TOOL-aSiftedPlaybook-3`, which declines it. Corrected "seven files" to eight
  plus the append-only log.
- rev-4 · 2026-08-16 · cleared blocker B2 and five findings from the round-2 audit
  `wf_98677a7a-009`. **S8 is now a HIGH-WATER RATCHET, not a threshold constant** (owner, 2026-08-16):
  the audit measured that every conventional fraction is silent through this whole build while
  anything tight enough to price it fires forever, so no constant works and the mechanism changed.
  AC7 rewritten against the ratchet, AC9 added so it ships quiet. AC3 gained the three alternatives
  that let S2 be skipped entirely with every AC green ("Do NOT raise", "inflating"), plus AC3b
  observing the rewritten message rather than only the absence of the old one. §4's
  `SESSION-KICKOFF` row still carried the pre-rev-2 range and contradicted S5 — the boundary falls
  MID-LINE-107 and is now spelled by sentence in both places. S3 extended to `AGENTS.md:16-17`
  (the sentence spans the break) and `:7`. S6 and AC6 now record BOTH reversals and all four
  falsified records; the `baseline.toml` exception was recorded nowhere but a spec's §8.
  Dropped the restated 1593-byte figure in favour of a pointer.
- rev-3 · 2026-08-16 · owner resolved both forks. F1 → the in-place `baseline.toml` swap (option 2),
  added as S7; the map gains no playbook dossier here, so `TOOL-aSiftedPlaybook-2` mints it and
  `TOOL-aSiftedPlaybook-3` keeps the unenforced shrink-only convention as a non-goal. F2 → the WARN
  threshold AND keeping `PLAY-aCandidStub-2` open, added as S8 with AC7 and a landing task to
  rewrite that backlog row's now-false rationale. Blast radius restated at THREE gates, since the
  rename is now happening.
- rev-2 · 2026-08-16 · folded the spec audit `wf_4ed62ebb-cef`. S5's line range stopped mid-paragraph
  at `:107` and would have taken the drift-signal warning at `:107-109` with it — the warning that
  stops this unit redding the bar. Added `memory/DECISIONS.md` to the §4 Inventory, which S6 always
  required. Corrected the "smallest dossier" citation (`codebase-map.md` at 76 lines, not
  `install-prefix.md` at 77) and the `drift_report.py` gate spelling to `--check`.
- rev-1 · 2026-08-16 · initial draft. Carrier inventory and blast radius measured by a five-lens
  discovery pass (`wf_4e13d9e7-550`), not estimated; the "four gates" trap was tested and found to
  over-predict for a rename, and `baseline.toml`'s shrink-only rule was tested and found unenforced.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "template size ceiling gate enforcement"` returns the
`template size <=32KiB` gate-legs inventory key and `check-install-prefix.sh` via the install-prefix
affordance seam. **The seam this unit wires through is `tools/gate-legs.json`** — the single source
the runner, the codebase-map inventory extractor and the drift-audit charter probe all read, which
is why F1 is a fork at all rather than a rename.

For F1 option 3 the extended seam is `memory/map/features/*.md`: a new dossier follows the pinned
heading contract in `tools/codebase-map/map_lib.py:58` (`## Constraints & why`, `## Shared seams`,
`## Gaps`) plus the graced `## Reuse affordance`, modelled on
`memory/map/features/codebase-map.md` (76 lines, the smallest of the seven).

**Prior art the recall query did NOT surface, and should have.** `.memory-tree.conf:43-50`'s
`READ_PATH_CEILING` is a declared byte budget over a mandatory read path, with each raise justified
in the conf beside the number. It is structurally the same problem this unit solves and the same
problem S8's ratchet approaches from the other side. No §10 recall terms in this build would have
found it, because it lives in a conf file rather than a decision record — a real gap in what the
retrieval corpus covers, and worth its own follow-up.

Recall terms used, recorded per M5: `template size gate byte ceiling externalize companion
domain-rules headroom strict limit raise refuse stub`. The query returned the records this
unit's §2 S6 must name — `PLAY-aCandidStub-1` §3 ("Raising the 32 KiB template gate. The limit is
not the variable"), `TOOL-aGuardedTally-1` (a §-stub parked unlandable, writing "the gate is right
to refuse"), and `PLAY-aPrunedCeremony-1` RD7 ("template edits are byte-neutral in-place rewords or
externalize — the load-bearing constraint"). All three remain accurate as of their dates; the
reversal changes their premise, not their correctness, and S6 must say so in those terms.

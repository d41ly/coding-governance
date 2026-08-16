# TOOL-aSiftedPlaybook-1 — the template ceiling moves to 48 KiB, as a recorded rule reversal

**Status:** SPECCED · rev-3 · 2026-08-16 · node a · Tier-2 · base 91ef1b05 · streams tooling · ratified 2026-08-16

## 1. Goal

Raise the enforced template ceiling from 32768 to 49152 bytes on owner order, and move every
carrier that states the old limit or the never-raise rule, so the repo does not keep instructing
agents to obey a rule it no longer enforces. Record the reversal as a decision that names the prior
records which relied on the old ceiling, because at least three of them cited it as binding.

## 2. Scope (IN)

- **S1 — the constant.** `tools/check-template-size.sh:14`: `MAX_BYTES=${MAX_BYTES:-32768}` becomes
  `49152`, and the trailing `never raise to fit new prose` comment is rewritten. This line is both
  the constant and a rule statement.
- **S2 — the gate's own prose.** Same file: the header rule statement at `:2-5` ("never inflating
  the template"), the usage echo `MAX_BYTES=32768` at `:8`, and the FAILURE MESSAGE at `:25-26`
  ("Do NOT raise the limit"). The failure message is the string an agent reads at the exact moment
  it is over budget, so it is the highest-value line in the file to get right.
- **S3 — the charter.** `AGENTS.md:16` (the most emphatic never-raise carrier), `:97` (the gate-suite
  leg bullet), `:178` (the Conventions restatement). Note `:97` spells `≤32 KiB` with a unicode `≤`
  while the leg itself spells `<=32KiB`, so a grep for the leg name alone misses it.
- **S4 — the adopter-facing README.** `README.md:12`.
- **S5 — the kickoff manifest trap.** `.claude/SESSION-KICKOFF.md:99` (the rule) and `:100-106`
  (the measured 32682/32768/86-free figure plus the scarcity-funding policy the raise makes
  obsolete). The paragraph actually runs to `:109`, and **`:107-109` SURVIVES the rewrite**: it is
  the parenthetical explaining why the trap paraphrases rather than citing a non-terminal spec id,
  which is still true and still load-bearing — see §7's landmine. Scoping the edit to `:99-109`
  without saying that would delete the warning that keeps this very unit from redding the bar.
  This is the largest single edit and the one an agent reads at every kickoff.
- **S6 — the decision record.** A new `memory/DECISIONS.md` row minting the reversal and naming the
  records that relied on the old ceiling. Append-only: nothing prior is edited.
- **S7 — the gate-leg label and its inventory key** (F1, resolved). `tools/gate-legs.json:17`
  becomes `template size <=48KiB`, and `memory/map/baseline.toml:35` is edited IN PLACE to the new
  key. `memory/map/generated/{MAP.md,inventories.json}` are regenerated with
  `python tools/codebase-map/gen_map.py --write`, never hand-edited. No dossier is minted by this
  unit.
- **S8 — the soft ceiling warning** (F2, resolved). The gate prints a `TEMPLATE-SIZE WARN` line above
  a soft threshold while still exiting 0, so growth stays visible before it becomes urgent. Roughly
  six lines. The threshold is a second named constant beside `MAX_BYTES`, env-overridable on the
  same pattern, and the warn line names both the measured size and the soft threshold.

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
- **Spending the new headroom.** `PLAY-aSiftedPlaybook-3` spends 1593 bytes of it and is a separate
  unit with its own review.

## 4. Design

### Inventory

Twelve tracked lines outside historical records, in seven files. Verified negatives are as
load-bearing as the hits: the three `parallel-coding-governance*.md` files, `WIRE-INTO-PROJECT.md`,
every kit `*.template.md` and every rendered `.claude/skills/**` state the limit **nowhere**, so the
raise touches no shipped adopter artifact.

| File | Lines | Class |
|---|---|---|
| `tools/check-template-size.sh` | 14 | the constant |
| `tools/check-template-size.sh` | 2-5, 8, 25-26 | rule statements + usage echo |
| `AGENTS.md` | 16, 97, 178 | rule statements |
| `README.md` | 12 | rule statement |
| `.claude/SESSION-KICKOFF.md` | 99 | rule statement |
| `.claude/SESSION-KICKOFF.md` | 100-107 | measured figure + funding policy |
| `tools/gate-legs.json` | 17 | the leg label — see F1 |
| `memory/map/baseline.toml` | 35 | the label as an inventory key — see F1 |
| `memory/map/generated/inventories.json` | 46 | generated mirror of the key |
| `memory/map/generated/MAP.md` | 53 | generated mirror of the key |
| `memory/DECISIONS.md` | append | S6's reversal row — append-only, nothing edited |

### The blast radius, measured rather than assumed

The charter's documented trap says "Adding ONE gate leg trips FOUR gates at once". That is true for
an ADDED leg and false here, in both directions:

- **A bytes-only change trips exactly ONE gate** — the kickoff-manifest ratchet, because
  `tools/check-template-size.sh` is a watched pathspec at `.claude/SESSION-KICKOFF.md:6`, forcing a
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
- **Make the ceiling a `.memory-tree.conf`-style declared pin.** Rejected as out of scope: it is a
  real improvement and it is `TOOL-aSiftedPlaybook-3`'s territory, not a number change's.

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
- **AC3** — When `git grep -nE '32768|32 ?KiB|never raise the limit' -- ':!memory/'` runs, every
  surviving hit is either the gate's own history comment or absent entirely; no hit asserts a live
  rule.
- **AC4** — When `bash skills/session-kickoff/manifest-check.sh` runs, it exits 0, and
  `.claude/SESSION-KICKOFF.md`'s `last-audit` carries a stamp newer than BASE with a delta line in
  the commit message.
- **AC5** — When `python tools/codebase-map/test_codebase_map.py` runs, coverage reports neither an
  `unclaimed` key nor a `stale_baseline` entry for the size leg, and the freshness byte-compare is
  green against a fresh `gen_map.py --write` render.
- **AC7** — When a file between the soft threshold and `MAX_BYTES` is passed to the gate, it **exits
  0 and prints the warn line**; below the threshold it exits 0 and prints no warn line; above
  `MAX_BYTES` it still exits 1. The middle case is the one that proves the threshold is advisory
  rather than a second ceiling, and it is the case a hand-written check omits.
- **AC8** — When `grep -n 'template size' tools/gate-legs.json memory/map/baseline.toml` runs, both
  spell `<=48KiB` and neither still spells `<=32KiB`.
- **AC6** — When `memory/DECISIONS.md` is read, a new row records the reversal, names
  `PLAY-aCandidStub-1`, `TOOL-aGuardedTally-1` and the `aCandidStub` review's refuted id 19 as
  records whose premise this changes, and no prior row has been edited.

## 7. Gates

- `bash tools/check-template-size.sh` — the subject.
- `bash skills/session-kickoff/manifest-check.sh` — `tools/check-template-size.sh` is a watched
  pathspec; the re-stamp is mandatory, not optional.
- `python tools/codebase-map/test_codebase_map.py` — F1 resolved to a rename, so this is mandatory,
  not conditional. Coverage AND freshness.
- `python tools/drift-audit/drift_report.py --check` — expected unaffected by the rename per §4; run it to
  confirm that rather than trust the analysis. Also guards the landmine below.
- `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gotchas.py --for-diff`.
- `bash tools/run-gates.sh` at the push boundary.

**A live landmine for this unit specifically.** `.claude/` is in the drift signal's `PRODUCT_GLOBS`
and `non_terminal_specs_cited_by_product_source` sits AT its pin of 2 with tolerance 0. S5 rewrites
a paragraph in `.claude/SESSION-KICKOFF.md`; if that rewrite names this spec's id while its status
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

Recall terms used, recorded per M5: `template size gate byte ceiling externalize companion
domain-rules headroom strict limit raise refuse stub`. The query returned the three records this
unit's §2 S6 must name — `PLAY-aCandidStub-1` §3 ("Raising the 32 KiB template gate. The limit is
not the variable"), `TOOL-aGuardedTally-1` (a §-stub parked unlandable, writing "the gate is right
to refuse"), and `PLAY-aPrunedCeremony-1` RD7 ("template edits are byte-neutral in-place rewords or
externalize — the load-bearing constraint"). All three remain accurate as of their dates; the
reversal changes their premise, not their correctness, and S6 must say so in those terms.

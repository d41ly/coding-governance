# PLAY-aFusedCharter-3 — AGENTS.md becomes a rendered region plus authored slots, and stops re-narrating its own gate manifest

**Status:** CLOSED · rev-4 · 2026-08-19 · node a · Tier-2 · base 497d25d0 · streams playbook

## 1. Goal

Restructure this repo's charter so the ruleset half is a rendered region joined to its source by a
re-render check, and the project half is authored slots around it — then pay for the region by
cutting the 26 222-byte gate-suite section, which re-narrates a manifest the charter itself says to
read from the manifest.

## 2. Scope (IN)

**S1 — Render this repo's own charter, over the FULL kit selection.** Write `.governance/deploy.toml`
for this repo, run `bash tools/playbook/adopt-playbook.sh`, and land the resulting `gov:playbook`
region in `AGENTS.md`. The descriptor names every kit this repo actually carries, not
`[selection] default` — that default is five entries against gov's thirteen tracked kit dirs, so a
default intake would drop the unattended, drift-audit, lexicon and agent-cap blocks out of gov's own
charter while gov's bar goes on enforcing exactly those rules. It also writes an EMPTY `drop_blocks`,
because both fenceable project-property blocks apply here: this fleet is multi-OS and the security
section's surface exists. This is the dogfood: the first real target of `DEPL-aFusedCharter-1` is this repo, and a
defect the fixture missed surfaces here rather than in somebody else's tree.

**S2 — Restructure the authored half into slots around the region.** What survives above the region:
the one-paragraph identity of the repo, what it ships, the layout, and the node registry. What
survives below it: the conventions section and the gate-suite remnant from S3. Authored content
never enters the region and the region never grows an authored line, because the next render would
silently delete it.

**S3 — Cut the gate-suite section against the admission test.** The section is 79 per cent of the
file and states, about its own subject, that a reader should read the split from the manifest and
not from the section. What survives is what a session cannot get anywhere else:

- the runner and its three invocations — concurrent, serial, and guard-ignoring;
- the guard rule and where it is declared, without restating any guard;
- the facts about how the bar behaves: bounded pool width, longest-first scheduling from a timing
  cache, manifest-order reporting, per-leg logs on disk and the durable failure file;
- the push-boundary authority — the pre-push hook, the branch guard, the SessionStart self-heal;
- the two BINDING protocol pointers, review fan-out and unattended runs, which are rules and not leg
  descriptions;
- one line stating that the leg list is `tools/gate-legs.json` and each leg's rationale is its own
  script header, with the map dossiers as the third carrier.

What goes: the per-leg bullets. There are 46 top-level bullets covering 70 legs — a bullet
legitimately groups several legs, which is why the drift probe over this section matches on script
paths rather than counting bullets, and why an earlier revision's "seventy per-leg paragraphs"
described a structure the section does not have. Each bullet's content already has an owner: the
manifest owns membership, the script header owns the why, and `memory/map/features/` owns the
machinery.

**S4 — The charter-completeness signal is already retired by the time this unit runs, and that is
deliberate.** `_charter_mentions_every_leg` asserts that the gate-suite section cites every leg's
argv script path; it measures `0 of 70` against a pin of `0` and is gateable, so S3 would red it on
seventy legs at once. The retirement is `TOOL-aFusedCharter-1` S10's, not this unit's, because three
units BEFORE this one add a gate leg and each would red the same zero-pin signal with no unit owning
the fix — the spec audit's third blocker. This unit therefore inherits a retired signal and asserts
that inheritance rather than performing it, which AC4 covers.

An earlier revision of this scope item performed the retirement here AND got the mechanism wrong in
three ways, all corrected in `TOOL-aFusedCharter-1` S10 and recorded here so the correction is not
lost with the move. The probe is one row in a `HANDKEPT` list, so the edit is a row DELETION plus a
SIGNAL name added to `DECLARED_EMPTY` — not "declaring a probe's population empty". That renders as
*empty by declaration*, which is the right reading; `NOT ASKED` is a different engine flag that makes
the signal non-gateable, and the engine's own comment records rejecting that route for this case
deliberately, so the earlier text contradicted its own acceptance criterion. And
`tools/drift-audit/selftest.py` carries NO arms for this probe — its fixture already writes an empty
`HANDKEPT` and already uses this signal's name as the literal its `DECLARED_EMPTY` arms exercise — so
"its arms retire with it" named work that does not exist.

**S5 — Amend the gates rule the cut depends on.** The output-discipline rule currently says a green
gate line enumerates every expected leg. After S3 the charter no longer holds that list, so the rule
must say where the list comes from: the manifest, read at emission time. This is the same rule
`PLAY-aFusedCharter-1` S10 adopts into `§6` in its general form, applied here to the one place a
session actually needs it. The amendment lands in the converged ruleset and reaches `AGENTS.md`
through the render, so it is written once.

**S6 — Adopt the ruleset's tone and its micro-formats, which is what the render delivers.** The
charter today carries no voice section, no output discipline, no session-execution hygiene and no
micro-formats; a session reading only `AGENTS.md` gets none of them. After S1 all four arrive inside
the region. This scope item is the acceptance of that, not separate work: it is named because it is
half the reason the owner opened the session, and a spec that leaves it implicit cannot be checked.

**S6a — `.governance/deploy.toml` needs a line-ending pin, and a place in the deployer's surface.**
It is a new committed file this unit creates, and `TOOL-aFusedCharter-1` S4b adds its `eol=lf` row —
without one, `core.autocrlf` decides its bytes per node and the render's answers differ across the
fleet for no reason anybody can see. This unit verifies the pin took effect with `git check-attr`
rather than assuming the row was written.

**S8 — Declare a byte ceiling for the charter, over the WHOLE file, AND wire the leg that enforces
it.** The owner resolved this at the second fork round, so it is scope rather than a recommendation.
One row in `tools/template-size-limits.txt`, keyed on `AGENTS.md`, in that file's existing grammar,
with the justification beside the number the way every other row there carries its history. It is
seeded at the LANDED measurement plus headroom rather than at a figure predicted here — this spec
projects roughly 56 KB and a projection is not a measurement.

**A declared row on its own is inert, and an earlier revision shipped exactly that.** The size gate
takes its subject from a positional argument and consults the declaration FOR THAT SUBJECT ONLY, so a
row nothing invokes the gate with is never read. There are three size legs on the bar today and none
names the charter — the kickoff engine got its own leg with its own positional for precisely this
reason. S8 therefore adds a fourth leg row invoking the gate with `AGENTS.md`, unguarded, and takes
the registry route a new leg needs: the gate's script is a registry exemption rather than an entry
file, so the leg is an `[[exempt_leg]]` row with its reason. Without this the ceiling is measured
twice by hand at AC8 and AC9 and never again.

**Why the whole file and not the authored half.** The alternative was to measure `AGENTS.md` minus
the rendered region, so the region stayed priced by the ruleset's own 48 KiB gate and this ceiling
priced only what gov adds. It was rejected: the number that matters is what a session actually reads
every turn, and that is the whole file. The apparent double-counting is the honest reading rather
than a flaw — if the ruleset grows five kilobytes, gov's charter really did become five kilobytes
more expensive to read, and a ceiling that hid that would be pricing the wrong thing.

**The headroom's consumer is smaller than an earlier revision priced it.** That revision budgeted a
wrap across eight lines — but all eight of this file's over-length lines sit INSIDE the gate-suite
section S3 deletes, so after this unit the charter's long lines are whatever the rendered region
brings, and those are wrapped in the RULESET rather than here. The headroom is sized against the
region's contribution, and `TOOL-aFusedCharter-3` re-measures against the declared ceiling rather
than assuming it still fits.

**S7 — Re-stamp the kickoff manifest.** `memory/guides/SESSION-KICKOFF.md` names `AGENTS.md` in
`verify-paths` and states the charter is authoritative. Its `§B` claims are re-verified against the
restructured file and `last-audit` re-stamped with a delta line in this unit's commit message.

## 3. Non-goals (OUT)

**No rule is deleted for brevity.** S3 deletes narration and duplication. Every rule the gate-suite
section carries that exists nowhere else survives, and the six bullets above are the enumeration of
those — a rule discovered during the build that is not on that list extends it rather than being
dropped.

**No renderer work.** `DEPL-aFusedCharter-1` owns the engine, the adopter and `--check`. This unit is
its first target.

**No SECOND measurement mode.** The ceiling S8 declares is over the whole file. Measuring the
authored half alone — the file minus the rendered region — was the fork's other option and was not
taken, so no region-aware measurement is built here.

**No rewrite of the node registry.** Four rows, all still true. The registry stays authored, above
the region, because it is per-repo data the ruleset asks for rather than ruleset text.

**No change to `.memory-tree.conf`'s charter key.** `AGENTS.md` stays the charter and stays the
target of every check keyed on it.

## 4. Design

### Inventory

Measured at BASE.

Sizes are CHARACTERS, and the column says so because an earlier revision headed it "Bytes" while
holding character counts — the file's byte total is 33 413 against 33 146 characters, and nothing was
mis-measured, only mislabelled. The distinction matters downstream: `check-template-size.sh` enforces
bytes.

| Part | Characters | After |
|---|---|---|
| preamble | 933 | authored, kept |
| what ships here | 2 399 | authored, kept |
| layout | 942 | authored, kept |
| node registry | 1 297 | authored, kept |
| the gate suite | 26 222 | cut to the six survivors in S3 |
| conventions | 1 353 | authored, kept |
| the rendered region | — | the converged ruleset, filled for this repo |

The honest arithmetic: the file grows. It carries roughly seven kilobytes of authored content plus
the gate-suite remnant plus the region, against 33 146 today. Convergence costs read-path bytes here
precisely because this charter never carried the ruleset — it pointed at it, and a pointer is what
let the two drift. The trade is that the rules are now loaded rather than optionally read, and that
they cannot diverge from their source without a leg saying so.

### Migration

S1 through S3 land in one commit: a tree with the region added and the gate-suite section still
present would carry two answers about the bar, and a tree with the section cut and no region would
carry neither. S4 lands nothing — the retirement it used to perform is `TOOL-aFusedCharter-1` S10's
and happens four passes earlier, which is what unblocks the three units between.

### Alternatives rejected

**Keep the gate-suite section and accept the size.** Rejected by the owner at kickoff. It is also
the section whose own first paragraph tells the reader not to read it for that answer.

**Move the seventy paragraphs to a new reference document.** Rejected: that is the companion shape
this whole build is retiring, and the content already has three owners.

**Weaken the drift signal to a warning.** Rejected in S4's terms. A signal that still asks a question
nobody can answer is the permanently-red decoration the kit refuses; declaring the population empty
is the honest act and the file already has a precedent for it.

### Files touched (estimate)

`AGENTS.md`, `.governance/deploy.toml` (new, committed — it is the standing authorization),
`tools/template-size-limits.txt` and `tools/gate-legs.json` (S8's row and its leg),
`tools/govkit/registry.toml` (S8's `[[exempt_leg]]`), `memory/guides/SESSION-KICKOFF.md`, and the
converged ruleset for S5. **Neither drift-audit file is touched here** — an earlier revision listed
both, and after S4's move one belongs to `TOOL-aFusedCharter-1` and the other is not edited by
anybody.

## 5. Production-readiness checklist

- security — `.governance/deploy.toml` is committed and holds answers about this repo's layout and
  fleet. It carries no credential and must not: the renderer's asked keys are paths, names and
  tables.
- perf / scale — the per-session read cost is the whole subject; the Inventory states it plainly
  rather than burying it.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — `bash tools/playbook/adopt-playbook.sh --check` is the standing observation that
  the region still matches its source.
- risks — the region and the authored slots can be confused by a future editor, which is what the
  markers and the check exist to prevent. The sharp edge used to be S4's retirement landing in the
  same commit that would red the signal; that moved to `TOOL-aFusedCharter-1` S10, and the
  commit-message visibility obligation moved with it rather than being dropped.
- testing + left-shift gates — the render-parity leg arrives with `DEPL-aFusedCharter-1`; this unit
  is what makes it non-vacuous, because before S1 there is no region for it to compare.
- migration / rollback — one commit, revertable; the region is delimited.
- user docs — `README.md` describes the repo and is unaffected.

## 6. Acceptance criteria

- **AC1** — When `bash tools/playbook/adopt-playbook.sh --check` runs, it exits 0 against the landed
  `AGENTS.md`, which is only meaningful because the region is present — verified by deleting one
  byte inside the region and confirming it reds.
- **AC2** — When `grep -c 'gov:playbook' AGENTS.md` runs it returns `2`, and every authored heading
  sits outside the marker pair.
- **AC3** — When the charter is read, its voice, output-discipline, session-hygiene and
  micro-format rules are present — `grep -c 'BUILD — ' AGENTS.md` returns at least `1`, proving S6
  arrived through the render rather than by hand.
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs after this unit's cut, it
  exits 0 and the signal renders with the literal `empty by declaration` rather than as zero
  offenders. `python tools/drift-audit/selftest.py` exits 0 UNCHANGED — it carries no arms for this
  probe, and an earlier revision that expected to remove some named work that is not there.
- **AC5** — When the surviving gate-suite remnant is read, each of S3's six survivors is present and
  no per-leg paragraph is — `grep -c 'check-verdict-epoch' AGENTS.md` returns `0` while
  `grep -c 'gate-legs.json' AGENTS.md` returns at least `1`.
- **AC6** — When `GATE_FULL=1 bash tools/run-gates.sh` runs, every leg is green, including
  `memory hygiene`, whose check 16 rules read the charter.
- **AC7** — When the commit lands, `memory/guides/SESSION-KICKOFF.md` carries a re-stamped
  `last-audit` and the commit message carries the `manifest-audit` delta line.
- **AC8** — When `bash tools/check-template-size.sh AGENTS.md` runs, it exits 0 and resolves its
  limit FROM `tools/template-size-limits.txt` — observable through the ratchet line, which names the
  key when it is unresolved and does not when it resolves. The printed limit alone cannot serve as
  the observable unless the declared value differs from the gate's `49152` default.
- **AC10** — When `bash tools/run-gates.sh` runs, a leg invokes the size gate with `AGENTS.md` as its
  subject and is green; removing the declared row makes THAT leg print its unresolved-key line. A
  declaration with no leg reading it is measured twice by hand and never again.
- **AC9** — When the declared row is temporarily lowered below the landed size,
  `bash tools/check-template-size.sh AGENTS.md` reds naming the overage. A ceiling whose failing
  case has never been observed is an assertion about nothing, so this is checked before the row is
  committed at its real value.

## 7. Gates

`memory hygiene` · `drift-audit records` · `drift-audit selftest` · `drift-audit wiring` ·
`kickoff-manifest ratchet` · `playbook render wiring` · `template size <=48KiB` (S8 adds a third
subject to its declaration) · `template size gate selftest` · the full bar.

## 8. Open questions

none — the fork below is RESOLVED.

- **F1 — should `AGENTS.md` get a declared byte ceiling, and over what?** RESOLVED (owner,
  2026-08-18): yes, over the WHOLE file, seeded at the landed measurement plus headroom. This is now
  S8 rather than a recommendation, and the rejected option — a ceiling over the authored half only,
  which would have needed a region-aware measurement mode the size gate does not have — is recorded
  in `§3` as a Non-goal so a later reader does not re-open it as an oversight. The ceiling is still
  not set by this spec: S8 seeds it from the landed measurement, because a ceiling written from a
  projection prices a file nobody measured.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft. S4 was added after measuring that the charter-completeness
  drift signal sits at a drained pin of zero and would red on seventy legs the moment S3 lands.
- rev-4 · 2026-08-18 · folded the round-2 spec audit. S8 now wires the leg that reads the ceiling —
  a declared row alone is inert, because the size gate consults the declaration only for the subject
  it is invoked with and no leg named the charter. S1 states the kit selection, which `[selection]
  default` would have got wrong by eight kits, and an empty `drop_blocks`. The headroom is repriced
  against the population S3 actually leaves. Migration, risks and Files touched are cleaned after
  S4's retirement moved out, including two drift-audit paths this unit does not touch.
- rev-3 · 2026-08-18 · F1 resolved by the owner: the charter gets a whole-file byte ceiling. That
  flips a Non-goal into new scope S8, adds two acceptance criteria including the failing-case
  observation, records the rejected authored-half option as a Non-goal in its place, and names
  `TOOL-aFusedCharter-3`'s wrapping as the headroom's one known consumer. This unit was classified
  FORKED until now and is READY with it.
- rev-2 · 2026-08-18 · folded the M4 spec audit. S4's retirement MOVES to `TOOL-aFusedCharter-1` S10,
  because three earlier units add a gate leg and would each red the same zero-pin signal; its three
  wrong mechanism facts are corrected and recorded here rather than lost with the move. New S6a pins
  the new committed descriptor's line endings, the Inventory column is relabelled to characters, and
  the "seventy per-leg paragraphs" figure is corrected to 46 bullets over 70 legs.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a generated region inside an authored document"` routes
to `tools/memory-tree/gen_build_index.py` and the marker-region contract graded by
`tools/memory-tree/marker-contract.test.sh`, whose case table already drives four live readers. This
unit consumes that contract through `DEPL-aFusedCharter-1`'s renderer and adds no reader of its own.
The second seam is `tools/drift-audit/drift_signals.py`'s declared-empty population, which
`ledger_rows_contradicting_git` established when a retired record left a signal with nothing to
grade — S4 is the second instance of that pattern rather than a new mechanism.

Recall terms used: `charter AGENTS gate suite enumerate leg manifest drift signal handkept inventory
rendered region marker admission narration read path`. The binding prior records are
`TOOL-cSightedPlumb-1`, which built the drift-audit kit and seeded this signal, and the upstream
inCMS charter-restructure unit, which applied the same admission test to a 60 893-byte charter and
measured the result at 43 928 — the precedent for both the method and the expectation that a cut of
this size is achievable without deleting a rule.

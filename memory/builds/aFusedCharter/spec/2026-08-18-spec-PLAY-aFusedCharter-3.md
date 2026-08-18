# PLAY-aFusedCharter-3 — AGENTS.md becomes a rendered region plus authored slots, and stops re-narrating its own gate manifest

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams playbook

## 1. Goal

Restructure this repo's charter so the ruleset half is a rendered region joined to its source by a
re-render check, and the project half is authored slots around it — then pay for the region by
cutting the 26 222-byte gate-suite section, which re-narrates a manifest the charter itself says to
read from the manifest.

## 2. Scope (IN)

**S1 — Render this repo's own charter.** Write `.governance/deploy.toml` for this repo with its own
answers, run `bash tools/playbook/adopt-playbook.sh`, and land the resulting `gov:playbook` region in
`AGENTS.md`. This is the dogfood: the first real target of `DEPL-aFusedCharter-1` is this repo, and a
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

What goes: the seventy per-leg paragraphs. Each one's content already has an owner — the manifest
owns membership, the script header owns the why, and `memory/map/features/` owns the machinery.

**S4 — Retire the charter-completeness drift signal, by declaring its population empty.**
`_charter_mentions_every_leg` in `tools/drift-audit/drift_signals.py` asserts that the gate-suite
section cites every leg's argv script path. Its pin is `0` and it is green today, so S3 reds it on
seventy legs at once. The signal is not weakened and its pin is not raised: its POPULATION is
declared empty, the way `ledger_rows_contradicting_git` already is in the same file and for the same
reason — the record it graded no longer exists. The comment records that the charter stopped making
the claim, so there is nothing left to disagree with the source. Per the kit's liveness rule the
declaration must read as NOT ASKED rather than as a clean zero, since a signal quietly reporting
zero over an empty population is the reassuring-nothing shape drift-audit exists to refuse.
`tools/drift-audit/selftest.py`'s arms for that signal retire with it.

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

**No byte ceiling for `AGENTS.md`.** Recommended and raised as a fork; setting one is an owner
decision and this unit does not take it.

**No rewrite of the node registry.** Four rows, all still true. The registry stays authored, above
the region, because it is per-repo data the ruleset asks for rather than ruleset text.

**No change to `.memory-tree.conf`'s charter key.** `AGENTS.md` stays the charter and stays the
target of every check keyed on it.

## 4. Design

### Inventory

Measured at BASE.

| Part | Bytes | After |
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
carry neither. S4 lands in the same commit, because the signal reds between the two states.

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
`tools/drift-audit/drift_signals.py`, `tools/drift-audit/selftest.py`,
`memory/guides/SESSION-KICKOFF.md`, and the converged ruleset for S5.

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
  markers and the check exist to prevent. S4 is the sharp edge: retiring a green signal in the same
  commit that would red it must be visible in the commit message, not just in the diff.
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
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs it exits 0, and the
  charter-completeness signal reports its population as declared-empty rather than as zero
  offenders; `python tools/drift-audit/selftest.py` exits 0 with that signal's arms removed.
- **AC5** — When the surviving gate-suite remnant is read, each of S3's six survivors is present and
  no per-leg paragraph is — `grep -c 'check-verdict-epoch' AGENTS.md` returns `0` while
  `grep -c 'gate-legs.json' AGENTS.md` returns at least `1`.
- **AC6** — When `GATE_FULL=1 bash tools/run-gates.sh` runs, every leg is green, including
  `memory hygiene`, whose check 16 rules read the charter.
- **AC7** — When the commit lands, `memory/guides/SESSION-KICKOFF.md` carries a re-stamped
  `last-audit` and the commit message carries the `manifest-audit` delta line.

## 7. Gates

`memory hygiene` · `drift-audit records` · `drift-audit selftest` · `drift-audit wiring` ·
`kickoff-manifest ratchet` · `playbook render wiring` · `template size <=48KiB` · the full bar.

## 8. Open questions

- **F1 — should `AGENTS.md` get a declared byte ceiling in `tools/template-size-limits.txt`?**
  Recommendation: yes, seeded at the landed measurement plus the headroom that file's own comments
  argue for, so the charter gets the same forcing function the ruleset has. It is an owner decision
  by that gate's stated rule — a ceiling is never set by the unit that would be measured against it
  — and this unit does not take it. Building without a ceiling is safe; the file simply stays
  unpriced, which is where it is today.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft. S4 was added after measuring that the charter-completeness
  drift signal sits at a drained pin of zero and would red on seventy legs the moment S3 lands.

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

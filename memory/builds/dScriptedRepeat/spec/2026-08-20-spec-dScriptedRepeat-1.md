# TOOL-dScriptedRepeat-1 — the mode vocabulary, published and joined

**Status:** SPECCED · rev-2 · 2026-08-20 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-20

## 1. Goal

Publish the authorization-mode set as a driver constant, add the third member, add the matching third
value to the directive SCOPE set, and give the merge-bar leg the membership branch it does not have —
so a misspelled mode is refused rather than silently agreed with in two places.

## 2. Scope (IN)

- **S1.** Add `AUTH_MODES` to `tools/unattended/unattended.sh` beside `PHASES_CORE`, `DOD_CORE` and
  `DIRECTIVES_CORE`, holding the closed set of authorization modes. It joins the constants `core_of`
  already reads, and is today the only mode vocabulary spelled as a `case` arm rather than a named set.
- **S2.** Rewrite the closed-set refusal at `unattended.sh:794-797` to test membership of `AUTH_MODES`
  rather than enumerate two values inline. The refusal message keeps its shape and DERIVES the legal
  set from the constant, so adding a member cannot leave the message stale.
- **S3.** Add the third member. The default for an absent `authorized-by:` key stays `slug`,
  unchanged, because every build folder written before the key existed is one.
- **S4.** Extend the directive SCOPE closed set with the third value, and extend `check_waiver_scope`
  at `unattended.sh:661-662` so a third-mode-scoped handle waived on a run of another mode is refused
  the way the existing scoped case already is.
- **S5.** Add a MEMBERSHIP branch to check 19 of `tools/unattended/check-unattended.sh`. Today that
  check compares the mode recorded in the run-state file against the mode in the README blob at BASE
  and has no opinion about whether either is a LEGAL value, so a README and a record that carry the
  same misspelling agree and pass. The leg reads `AUTH_MODES` through the existing `core_of` parse it
  already uses for the phase, DoD and directive sets, never a second copy.
- **S6.** Extend the leg's scope-cell handling at `check-unattended.sh:709` and its refusal at `:714`,
  both of which hardcode the two-value scope set today.
- **S7.** Arms in `unattended.test.sh` and `check-unattended.test.sh` for: the new member accepted; an
  illegal member refused with the derived message; a third-mode-scoped waiver on another mode's run
  refused; check 19's membership branch redding on a misspelling that is IDENTICAL on both sides.
  Each arm carries the branch's entire literal signature.

## 3. Non-goals (OUT)

- No change to `check_authorization`, `resolve_base`, `observe_anchor` or leg check 13. The precedent
  build measured that a mode is a RECORD rather than a verdict and that no authorization code moves.
  That finding is reused, not re-derived, and the reproduction is in its build folder.
- No project channel for the mode set. `AUTH_MODES` is kit-owned exactly as the other vocabularies
  are, with no `MODES_EXTRA`. A project-declarable mode is a discipline nobody wrote.
- No shrink-only floor for `AUTH_MODES`. The sets beside it carry one because a project may EXTEND
  them and a deleted core member would be a silent override; nothing extends this set, so a floor
  here would pin a constant only this kit edits.
- The mode's SPELLING is not settled by this spec. See §8 F1.

## 4. Design

### Data model

`AUTH_MODES` is a space-separated string, matching the three sets beside it, so `core_of` parses it
with no new reader. Members carry no second field: unlike a DoD item there is no checker to name, and
unlike a directive there is no method section to point at.

The SCOPE set is NOT a separate constant. It is derived as `all` plus every member of `AUTH_MODES`,
because a scope is exactly "every run" or "a run in mode M". Deriving it is what stops the two sets
disagreeing, which is precisely the drift a second constant would introduce.

### Inventory

| Seam | Where it is today | Change |
|---|---|---|
| the closed-set refusal | `unattended.sh:794-797` | membership test; message derived from the constant |
| the waiver scope refusal | `unattended.sh:661-662` | reads the derived scope set |
| `scope_of`'s default | `unattended.sh:123-132` | unchanged — an absent third field still means `all` |
| leg scope-cell handling | `check-unattended.sh:709` | reads the derived scope set |
| leg scope refusal text | `check-unattended.sh:714` | message derived |
| check 19 | `check-unattended.sh` | gains a membership branch it does not have |

### Alternatives rejected

**A `case` arm listing three values.** This is the shape today, and it is what makes a new mode cost
several edits in two files with nothing joining them. The consequence is already live: check 19 agrees
with a misspelling because it compares two values without asking whether either is legal — the
`assertion-between-two-derived-values` class this repo tracks by name.

**A `MODES_FLOOR` pin.** Rejected above, and worth stating rather than omitting: a pin whose subject
nothing extends is a guard sharing a variable with the thing it guards.

## 5. Production-readiness checklist

- security — the mode is a byte in a file the run can write. Protocol §9's reduction applies
  unchanged and this unit neither widens nor narrows it. Publishing the set makes a MISSPELLING
  refused, which is an integrity property and not an authorization one. Saying otherwise would
  overclaim exactly what §9 forbids overclaiming.
- perf / scale — N/A. One membership test per verb invocation.
- a11y — N/A, a shell driver with no user surface.
- i18n — N/A, an ASCII closed set.
- error / empty / loading states — an EMPTY `AUTH_MODES` must REFUSE rather than accept everything.
  Protocol §8's rule that an empty declaration is a refusal applies, and S5's branch is written so a
  vacuous set reds rather than passes.
- observability — the recorded `mode:` line in Run facts is unchanged; the leg's new branch names the
  illegal value in its refusal so a reader is not sent to diff two identical strings.
- risks — the scope set is DERIVED from `AUTH_MODES`, so a member added for authorization silently
  becomes a legal directive scope. That is intended, and it is stated here so a later reader does not
  read it as an accident.
- testing + left-shift gates — S7. Every arm's failing case is staged and observed RED before the arm
  lands, per the charter's rule that a gate seen only to pass is an assertion about nothing. AC4 names
  the one case that PASSES today.
- migration / rollback — additive. An existing tree has no third mode and every existing record parses
  unchanged. Reverting is deleting one member.
- user docs — the mode set is described in `memory/guides/UNATTENDED-PROTOCOL.md` §1. That sentence
  becomes a POINTER at the constant rather than a second copy of it, per §10 of that same document's
  own rule about naming a set twice.

## 6. Acceptance criteria

- **AC1** — When `AUTH_MODES` lands, the closed set is spelled exactly ONCE in the kit: a grep for the
  inline two-value alternation over `unattended.sh` and `check-unattended.sh` returns zero hits.
- **AC2** — When a build README at BASE declares the third mode, `bash tools/unattended/unattended.sh --preflight`
  records it in Run facts and does not refuse.
- **AC3** — When a build README declares a value outside the set, `--preflight` refuses and the
  message NAMES every legal value, derived from `AUTH_MODES` rather than typed.
- **AC4** — When a run-state file and its README blob BOTH record the same illegal value, check 19 of
  `bash tools/unattended/check-unattended.sh` REDS. Staged and observed RED before the branch lands;
  this case PASSES today, which is why the arm is worth writing.
- **AC5** — When `--waive` names a third-mode-scoped handle on a run of a different mode,
  `unattended.sh` refuses, and the pre-existing scoped case still refuses unchanged.
- **AC6** — When `AUTH_MODES` is emptied in a scratch copy, `bash tools/unattended/check-unattended.sh`
  REDS rather than accepting every value. Observed in a scratch tree, never asserted.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/unattended.test.sh` ·
`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/cross-component.test.sh` ·
`bash tools/run-gates/run-gates.sh`. No new leg: the membership branch is a CHECK inside an existing
leg, which the research measured as far cheaper than a new leg and which trips none of the meta-gates
that key on `tools/gate-legs.json`. Adding an arm costs `ARMS_FLOORS` and one arm per `fail` call site.

## 8. Open questions

- **F1 — the mode's SPELLING.** `playbook` collides with three live things: the `DISCIPLINES` enum at
  `.memory-tree.conf:11`, the `PLAY` family at `:15`, and the charter-renderer kit at `tools/playbook/`
  with its own parity gate and map dossier. None is a MACHINE collision — the mode set and the
  discipline enum are never compared — but a reader grepping the word gets four unrelated subjects, and
  the mode value is user-facing and permanent. Candidates: `recipe`, `runbook`, `serial`, `script`.
  Recommendation: `recipe`. It is unused anywhere in the tree, both reference artifacts call themselves
  a recipe in their own prose, and it does not suggest the charter renderer. **Owner decision.**
- **F2 — whether `AUTH_MODES` is also joined to the rendered Skill's own list**, the way the directive
  registry is joined to its Skill table in both directions. Recommendation: yes, but authored in unit
  10 where the Skill is written, not here. Deferred rather than open.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft. Decomposed from the research pass. S5 and the derived scope set
  come from the contradiction hunt's ranked decision 9, which two lenses reached independently and
  which no kickoff fork covered.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F21 dropped two prose counts of a derived population
  that contradicted each other inside this spec - in the unit whose whole subject is not spelling a set
  twice. Two audit passes produced two different corrected censuses, which is itself the argument for
  writing no number at all.

## 10. Reuse audit

The seam is the driver's existing vocabulary shape: three constants read through one `core_of` parse
that the leg already shares. This unit adds a member of that established pattern rather than a new
mechanism, which is why it needs no new reader, no new conf key and no new leg. `scope_of` at
`unattended.sh:123-132` is reused unchanged — its shortest-prefix/longest-prefix pair already yields
`all` for a two-field entry, and that property is exactly what lets the scope set grow without
touching a single existing directive row. Recall terms used: unattended driver closed vocabulary
constant core parse leg join membership refusal mode scope directive registry shrink floor waiver.

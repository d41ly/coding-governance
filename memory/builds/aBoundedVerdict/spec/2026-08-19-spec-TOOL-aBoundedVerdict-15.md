# TOOL-aBoundedVerdict-15 — every close-path write is staged, guarded, and reachable by a verb

**Status:** CLOSED · rev-3 · 2026-08-19 · node c · Tier-1 · base 098bebd9 · streams tooling

## 1. Goal

Two of the driver's five phase writers do not stage what they wrote — `--close` and `--phase` — so
`--landed` then refuses on the dirt `--close` created and blames the tree; the two agent-attested
Definition-of-Done items have no writer at all, so the documented sole exit from a wedged run is reachable only by
hand-editing the file the kit calls generated; and the override park is the one park caller with no
bypass-flag guard, so a truthful reason permanently reds the bar on a record no verb rewrites. Close
the three.

## 2. Scope (IN)

- **S1** — `verb_close` calls `stage_or_fail` after its phase write, and so does `verb_phase`. Today
  `--close` writes `LANDING` and the override park rows and stages neither, and `--phase` writes an
  arbitrary phase and stages nothing. **Measured at rev-2**: `set_fact "$rel" phase` has five call
  sites (`:1023`, `:1069`, `:1133`, `:1288`, `:1442`); `stage_or_fail` has four (`:1080`, `:1136`,
  `:1303`, `:1598`) and `:1598` is inside `verb_park`, which writes no phase. So **three of five
  stage** — rev-1's "the only phase writer that does not" was wrong, and S4's source rule would have
  reddened on `verb_phase` on the very diff that landed it.
- **S2** — an `--attest <slug> --item <item>` verb writes an agent-attested Definition-of-Done key
  through `set_fact` and stages it, refusing any item whose checker is not `agent`. It writes the
  RECORD KEY, so the `parked-decisions-surfaced` / `parked-surfaced:` mismatch cannot be reproduced by
  an operator following the verb.
- **S3** — the override park's item and reason pass the same bypass-flag refusal `--abort`, `--waive`
  and `--park` already apply, and it fires in `verb_close`'s validation loop BEFORE anything is
  written — the loop that already validates every override pair before acting on any of them.
- **S4** — a source-level arm: every `park()` call site is preceded by the bypass guard, and every
  phase write is followed by `stage_or_fail`. Both are one-line rules over a single file, and both are
  the class that returned here because the fix was made at one call site and not made a rule. The
  rule lands AFTER S1 has fixed BOTH omissions — rev-1 assumed one violator, and a meta-gate written
  against a two-violator tree reds on its own diff.

## 3. Non-goals (OUT)

- Not what a blocked close SAYS. `TOOL-aBoundedVerdict-12` owns the message channel; this unit owns
  what the close path WRITES. S2 touches a message only where the verb's existence removes the need
  for one.
- Not the DoD set, the checker assignment of any item, or which items are overridable. `--attest`
  writes an existing key for an existing item and invents nothing.
- Not the attestation's TRUTH. A verb that records "I reaped the keepalive" is still an attestation —
  the protocol's section nine already says what an agent-attested item can and cannot buy, and this
  unit does not claim to change it. What it removes is the hand-edit, not the trust assumption.
- Not `--landed`'s clean-tree requirement. That check is correct and this unit stops giving it a
  false subject.
- No new phase, no new terminal, and no change to `refuse_if_terminal`.

## 4. Design

### Why the missing stage is a wedge and not an untidiness

The gate leg's entire per-run population is `git ls-files`, which reads the INDEX — which is why
`--preflight` stages the run-state file rather than leaving it untracked, and the driver's own comment
says so. So an unstaged `LANDING` phase is invisible to every leg check. Worse, `--landed`'s
`check_clean` then refuses because the tree is dirty, and the dirt is `--close`'s own write: a verb
refusing on the previous verb's uncommitted output, with a message that blames the operator's tree.

Three phase writers of five stage. That ratio is S4's whole justification: the rule exists, it is
followed three times out of five, and nothing enforces it. Rev-1 said four-of-five and named one
omission; the audit measured two, and a meta-gate written to the wrong ratio reds on itself.

### Why the two agent keys need a verb

`keepalive-reaped` and `parked-surfaced` are read at two sites and written at none. `--abort` REQUIRES
both before it will record a terminal, because an abort orphans the same job and leaves the same
decisions unseen — so the documented sole exit from a wedged run is gated on two keys no verb writes.
An agent following the protocol must hand-edit a file whose grammar the driver owns and whose region
the leg byte-compares.

The `parked-decisions-surfaced` → `parked-surfaced:` mismatch makes it worse: the item name is not the
key, `--abort` carries the mapping and `--close` does not, so an operator obeying the close-path
refusal writes a key nothing reads. A verb removes the class rather than documenting it — the operator
never spells a key.

### Inventory

| Concern | Today | After |
|---|---|---|
| `--close`'s phase write | unstaged, invisible to every leg | staged, as three other writers do |
| `--close`'s override park rows | unstaged | staged with the phase |
| `--landed` after `--close` | refuses on `--close`'s dirt, blaming the tree | proceeds |
| the two agent-attested keys | no writer; hand-edit required | `--attest`, which writes the record key |
| the override park's reason | no bypass guard; a truthful reason reds the bar forever | refused before anything is written |
| the guard and stage rules | followed 3-of-4 and 3-of-5 | asserted at source |
| `--phase`'s write | unstaged, and unnoticed until this audit | staged |

### Migration

None. No key changes name, no record is rewritten, and a run that already hand-wrote an attestation
key is unaffected — `--attest` writes the same line the hand-edit would have.

### Rollout

S1 first and alone if need be: it is one line and it unblocks the `--close` → `--landed` sequence.
S3 next, because until it lands a truthful override reason is a permanent red. Then S2, then S4 —
S4 last for the reason a meta-gate is always last: written before its subject is clean, it reds on the
diff that fixes it.

### Files touched (estimate)

`tools/unattended/unattended.sh` (one `stage_or_fail`, one verb, one guard moved into the validation
loop) · `tools/unattended/unattended.test.sh` (arms per branch, plus S4's source arms) ·
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (the verb table
gains `--attest`) · `tools/unattended/SKILL.template.md` and the rendered Skill (the close and abort
sections stop implying a hand-edit) · `.memory-tree.conf` (`ARMS_FLOORS`) · the kit version constant.

### Alternatives rejected

- **Have `--close` commit rather than stage.** Rejected on the driver's own recorded reason: a driver
  that makes commits has to decide about hooks, and the one flag it would reach for is the flag this
  kit bans.
- **Widen the two readers to accept either spelling of the parked key.** Rejected: it makes both
  spellings correct forever and leaves the hand-edit in place. `TOOL-aBoundedVerdict-12` S5 fixes the
  MESSAGE for anyone who still hand-edits; this unit removes the reason to.
- **Let `--attest` write any DoD key.** Refused: writing a machine-checked key by hand is exactly the
  self-certification the kit exists to prevent, so the verb refuses a non-`agent` checker.
- **Make the attestation a flag on `--close` (`--attest-keepalive`).** Rejected: `--abort` needs the
  same two keys and does not go through `--close`, so the flag would have to exist on both verbs.
- **Fix only the missing stage.** Rejected: the unstaged write and the unwritable keys are both
  "`--close` leaves the record in a state no verb can advance", and splitting them means the wedge
  survives at half strength.

## 5. Production-readiness checklist

- **security** — S2 is the one to read. `--attest` must refuse a machine-checked item, and the refusal
  must be on the item's declared CHECKER rather than on a hardcoded pair of names, so a project that
  declares its own agent-attested extra item gets the verb and a project that renames a machine item
  gets the refusal.
- **perf / scale** — N/A.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — `--attest` on a slug with no run-state file, on a terminal
  record, on an undeclared item, and on a machine-checked item are four distinct refusals.
- **observability** — S1's effect is observable only as `--landed` no longer refusing, so the arm must
  assert the SEQUENCE `--close` then `--landed`, not each verb alone. That is the arm that fails today.
- **risks** — low. Two hazards. S4's source rule written as a whole-file grep reds on the comment
  documenting its own fix (`memory/gotchas/absence-assertion-over-whole-file-text.md`). And S4 landing
  before S1 has fixed BOTH omissions reds on `verb_phase` — the ordering point rev-1 missed by
  believing there was one violator.
- **testing + left-shift gates** — S4 is the left-shift, and the sequence arm in the observability line
  is what proves S1.
- **migration / rollback** — none; revert is per-scope-item.
- **user docs** — the protocol verb table and the Skill's close and abort sections.

## 6. Acceptance criteria

- **AC1** — When `--close` succeeds and `--landed` is invoked immediately after with no intervening
  `git add`, `--landed` does not refuse on a dirty tree — the sequence arm in
  `tools/unattended/unattended.test.sh`, which fails against the shipped driver.
- **AC2** — When `--close` succeeds, `git diff --cached --name-only` names the run-state file.
- **AC3** — When `bash tools/unattended/unattended.sh --attest <slug> --item keepalive-reaped` runs, the
  run-state file gains `keepalive-reaped: yes` and it is staged; when the item is
  `parked-decisions-surfaced`, the line written is spelled `parked-surfaced:`.
- **AC4** — When `--attest` names a machine-checked item such as `gates-green`, it refuses naming the
  item's checker, and the run-state file is byte-unchanged.
- **AC5** — When `--close --override <item> --reason` is given a reason containing the declared
  `BYPASS_BAN` flag, it refuses BEFORE writing anything: the run-state file is byte-unchanged and the
  phase is not `LANDING`.
- **AC6** — When `--abort` is run after `--attest` has written both agent keys, it proceeds; the arm
  that proves the documented exit is reachable without a hand-edit.
- **AC7** — When S4's source arms run, they red against a fixture copy of the driver with the
  `stage_or_fail` removed from `verb_close`, a second with it removed from `verb_phase`, and a third
  with a `park()` call site stripped of its guard — THREE red fixtures, because a source rule with no
  red fixture passes by finding nothing and rev-1's single fixture was built on a one-violator
  assumption.
- **AC7a** — When `--phase` writes a phase, `git diff --cached --name-only` names the run-state file;
  the second staging arm, which rev-1 did not have because it did not know `verb_phase` omitted it.

## 7. Gates

`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.sh` +
`check-unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` (the rendered Skill
moves) · `python tools/memory-tree/check-arms.py` · `tools/check-testsuite-counts.sh` ·
`tools/check-kit-versions.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — is the verb `--attest <slug> --item <item>`, or `--attest <slug> <item>`?** The driver's
  existing verbs take a slug positionally and everything else as a named flag, and `--item` is already
  parsed for `--park`. **Recommendation: `--item`,** reusing the parsed flag rather than adding a
  second positional convention to one verb.
  RESOLVED (agent, 2026-08-19, delegated): `--item`. Mechanism-only, and it reuses an existing parse.

- **F2 — does `--attest` take a VALUE, or always write `yes`?** `TOOL-aBoundedVerdict-5` S6 wants the
  parked-surfaced key's value to carry a COUNT so the close can verify it against the record. If that
  unit lands, the value is not always `yes`. **Recommendation: accept an optional `--value`, defaulting
  to `yes`,** so unit 5 needs no second verb and this unit does not pre-empt its design.
  RESOLVED (agent, 2026-08-19, delegated): an OPTIONAL value, defaulting to `yes`. Built as
  `--value`, so the countable-attestation unit needs no second verb; the current predicate already
  tolerates trailing text after yes-or-true, so the default path is byte-unchanged.

- **F3 — should S4's stage rule cover every `set_fact` call, or only phase writes?** Every `set_fact`
  is the stronger rule and would catch a future fact writer that forgets. Some `set_fact` calls are
  legitimately followed by more writes before a single stage. **Recommendation: phase writes only,**
  keyed on the `phase` key, because the broader rule has known-good exceptions and a rule with
  exceptions is a rule nobody trusts.
  RESOLVED (agent, 2026-08-19, delegated): phase writes only, plus DECLARED exemptions. Covering
  every `set_fact` was tried and produced false positives on CORRECT code - `verb_landed` batches
  three writes before one stage - so the rule is function-scoped, and the one genuine cross-function
  case (`verb_preflight`'s guard lives in `check_waivers`) is named as an exemption in both the rule
  and its red fixture rather than silently tolerated.

## 9. Revision log

- rev-3 · 2026-08-19 · F2 and F3 RESOLVED in place: an optional `--value` defaulting to `yes`, and a phase-write-scoped stage rule with the one cross-function case declared rather than silently tolerated. §8 gains its machine-read first line; status INPROGRESS -> CLOSED at the landing.
- rev-2 · 2026-08-19 · folded the M4 spec audit. **The premise was wrong by one**: `--close` is not
  the only phase writer that skips staging — `verb_phase` skips it too, so three of five stage rather
  than four. Corrected at every site rev-1 spelled it (§1, S1, §4, §5) and, more importantly, in S4
  and AC7: the source rule would have reddened on `verb_phase` on the diff that landed it, and AC7's
  single red fixture was built on a one-violator assumption. AC7a is new and observes the second
  staging fix. The bypass-guard fraction rev-1 gave was correct and is unchanged: three of four park
  callers carry it, the `--close` override at `:1435` being the exception.
- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's highs 11 and mediums 13 and
  20, consolidated as one mechanism — what the close path writes and whether a verb can reach it —
  because all three leave the record in a state no verb can advance. Tier 1: three local changes and
  one verb, none of which changes a contract another kit reads. F1 resolved under the delegated fork
  rule; F2 and F3 carry recommendations and are left open because F2's answer belongs to another unit's
  design and F3's is a judgement about rule strength the builder should re-read at build time.

## 10. Reuse audit

Three existing seams, and naming them is what makes this Tier 1 rather than Tier 2:

- `stage_or_fail` — the staging helper four phase writers already call. S1 adds a fifth caller.
- `set_fact` — the fact writer `--attest` routes through, so the verb adds no write path.
- the bypass-flag refusal in `verb_park` (`unattended.sh:1578`-region) and its twins in `--abort` and
  `--waive` — S3 adds a fourth caller of a guard that exists in triplicate. That it exists three times
  and not four is the defect.

`checker_of` is the fourth: S2's refusal reads an item's declared checker through it rather than
matching item names, which is what makes the verb correct for a project that declares its own extra
agent-attested item.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict
adversarial diff fold unattended close build-complete DoD stall halt`.

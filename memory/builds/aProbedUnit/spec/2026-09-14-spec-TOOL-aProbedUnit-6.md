# TOOL-aProbedUnit-6 — `REVIEW_ROUNDS` bounds a spec-audit subject; the `BOUNDED` exit

**Status:** SPECCED · rev-1 · 2026-09-14 · node a · Tier-2 · base 1b000d1a · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-7 |

<!-- /gen:spec-records -->

## 1. Goal

`review_state` in `tools/unattended/unattended.sh` re-arms the loop at round 1 whenever the
blocker count is above zero, so every spec audit that confirms one blocker costs a second lens
fan. The owner ruled on 2026-09-14 that a SPEC subject takes one round by default and that the
closing DIFF review keeps its convergence loop. This unit gives the driver a conf key
`REVIEW_ROUNDS`, a fifth state `BOUNDED` that is terminal, a default disposition at every terminal
exit, and lands the vocabulary in every carrier that spells the state set.

## 2. Scope (IN)

- **S1** — A conf key `REVIEW_ROUNDS`, preset beside `GATE_BOUND=""` before the conf is sourced,
  validated after `RUNAWAY_CEILING` is defined as a positive integer not above that ceiling,
  defaulting to 1 with the default ANNOUNCED on stderr the way `GATE_BOUND`'s is, and REFUSED with
  exit 2 when malformed, zero, or above the ceiling. Observed by AC1 and AC2.
- **S2** — `review_state` takes an optional third argument, the bound, defaulting to
  `RUNAWAY_CEILING`, and returns `BOUNDED` when `n+1 >= bound` after the three existing tests and
  before `CONVERGING`. With the default bound the function is byte-for-byte today's behaviour,
  because `CEILING` fires at equality first. Observed by AC3.
- **S3** — `verb_review` passes `REVIEW_ROUNDS` as the bound when the subject is NOT the build
  slug and `RUNAWAY_CEILING` when it is; `BOUNDED` joins the terminal grep, the `note` case and
  the echo case with its own sentence; `--disposition` at a terminal exit becomes OPTIONAL and
  DEFAULTS to `promote`, the `fail 37` branch that required it is DELETED, and an explicit
  `--disposition` on a non-terminal round stays refused. Observed by AC4, AC5 and AC6.
- **S4** — `--close`'s `diff-reviewed` term admits `BOUNDED` in its terminal case, for vocabulary
  parity, with the header saying it is unreachable for the slug subject. Observed by AC7.
- **S5** — `tools/unattended/check-unattended.sh` check 2: `BOUNDED` joins the `term` regex and
  the `needs` regex, so a `BOUNDED` exit owes a disposition and a promote owes an id exactly as
  `NON-CONVERGENT` does. Observed by AC8.
- **S6** — `tools/workflows/unattended-build.template.js` and its render: `REVIEW_TOKENS` gains
  `BOUNDED` and the recorder prompt names five tokens; the harness suite's terminal loop gains
  `BOUNDED`. Observed by AC9.
- **S7** — The prose carriers land in the same commit: `VERBS.template.md`'s `--review` bullet,
  `SKILL.template.md`'s "Record each review round" section, `PROTOCOL.template.md` section 8's
  key table and its `closing-review-recorded` row, `kit.toml`'s `optional_keys`,
  `.unattended.conf` and `.unattended.conf.example` with the reason beside the key, then
  `bash tools/unattended/adopt-unattended.sh` re-renders. Observed by AC10.
- **S8** — `tools/memory-tree/BUILD-METHOD.template.md` M4's convergence sentence becomes the
  round-bound rule, byte-neutral or better, leaving the disposal sentence to unit 7; the render
  is re-made and the kickoff manifest's `last-audit` is re-stamped in the same commit. Observed by
  AC11.
- **S9** — `tools/unattended/unattended.test.sh`: `mkconf` gains a sixth positional
  `REVIEW_ROUNDS` defaulting to the ceiling so every existing sequence arm holds unchanged, the
  new arms section 6 names land beside the review-loop arms, the deleted refusal's arm is
  rewritten to assert the default is written, and the floors rise by the arms added. Observed by
  AC12.

## 3. Non-goals (OUT)

- **Disposal by severity is unit 7's.** The harness's `DISPOSAL` stage, its `confirmed === 0`
  skip, its `promoted`/`folded` counts, M4's disposal sentence, and the Skill's `NON-CONVERGENT`
  bullet's severity wording are not touched here. This unit makes `BOUNDED` flow into that stage
  the way `NON-CONVERGENT` does today and nothing more.
- **The closing diff review is unchanged in behaviour.** Its subject is the build slug, its bound
  is the ceiling, and no round it records can read `BOUNDED`. `TOOL-aProvenReuse-3`'s question,
  what a promoted SPEC blocker is, is answered by unit 7's ruling and that backlog row is unit 7's
  to close.
- **`RUNAWAY_CEILING` stays a file constant** at `tools/unattended/unattended.sh:464`, for the
  reason its header gives. `REVIEW_ROUNDS` is a conf key because a tracked conf leaves a diff
  behind, which is the property that header wants.
- **`fold` stays legal at a terminal exit** when spelled explicitly; only the REQUIREMENT goes.
  The closed set `REVIEW_DISPOSITIONS` and its two refusals are unchanged.
- **No new verb, no new `fail` branch.** The malformed-key refusal is an `echo` and `exit 2` at
  conf-read time, exactly as `GATE_BOUND`'s at `:305` to `:311`, so `harness arms` gains nothing to
  arm; the driver's branch floor in `ARMS_FLOORS` is 104 against 194 measured on 2026-09-14, so
  deleting one branch moves no floor.
- **No kit version bump inside this unit.** Unattended `1.21` to `1.22` and memory-tree `2.75` to
  `2.76` are the closing pass's, once each, across every carrier the build README names.
- **Not parallel with unit 3 or unit 7.** Unit 3 edits `unattended.sh`, `kit.toml`'s
  `optional_keys`, `PROTOCOL.template.md` section 8, `.unattended.conf` and `SKILL.template.md`;
  unit 7 edits the same M4 paragraph and the same harness template. The write sets intersect, so
  the passes are sequential, in roster order.

### Edges

- **hands-off** `TOOL-aProbedUnit-7` — the disposal sentence in M4 and the harness's disposal
  stage. This unit writes the round-bound sentence beside it and the `BOUNDED` token into
  `REVIEW_TOKENS`; unit 7 decides what happens to the blockers a `BOUNDED` exit leaves standing.
- **consumes-from** external — the owner's ruling of 2026-09-14 in the run mandate's owner-turn
  table: one round for SPECS ONLY, the diff review keeps its loop. Without it the bound would be
  a run's own choice, which M3 forbids.
- **hands-off** external — the two kit version bumps at the closing pass.

## 4. Design

### The key

`GATE_BOUND` is preset at `tools/unattended/unattended.sh:292`, the conf is sourced at `:294`, and
the value is defaulted, validated and announced at `:305` to `:312`. `REVIEW_ROUNDS=""` joins the
preset line. Its validation block sits directly after `RUNAWAY_CEILING="8"` at `:464`, because
the upper bound IS that constant and a comparison written above its definition reads an empty
string:

```bash
case "${REVIEW_ROUNDS:-}" in
  "") REVIEW_ROUNDS=1
      echo "unattended: NOTE - this project declares no REVIEW_ROUNDS, so a spec-audit subject exits BOUNDED after the kit default of ${REVIEW_ROUNDS} round(s). Declare one in $CONF to change it." >&2 ;;
  *[!0-9]*|0)
      echo "unattended: REFUSING - REVIEW_ROUNDS is declared as '$REVIEW_ROUNDS', which is not a positive integer of rounds. A bound that cannot be parsed is a bound nobody set, and 0 would end every loop before its first round." >&2
      exit 2 ;;
esac
[ "$REVIEW_ROUNDS" -le "$RUNAWAY_CEILING" ] || { echo "unattended: REFUSING - REVIEW_ROUNDS is $REVIEW_ROUNDS, above the runaway ceiling of $RUNAWAY_CEILING, so the ceiling would fire first and the declared bound could never be reached." >&2; exit 2; }
```

The kit default is the literal `1` in that block rather than a `REVIEW_ROUNDS_DEFAULT` constant,
because one reader exists and a constant read once is a second spelling of one fact.

### The predicate

`review_state` at `:3974` becomes:

```bash
review_state() { # prior-counts (space separated) · this count · [bound, default the ceiling] -> the state
  local prev="" n=0 c bound="${3:-$RUNAWAY_CEILING}"
  for c in $1; do prev=$c; n=$((n+1)); done
  if [ "$2" = 0 ]; then printf 'CONVERGED\n'; return 0; fi
  if [ "$n" -gt 0 ] && [ "$2" -ge "$prev" ]; then printf 'NON-CONVERGENT\n'; return 0; fi
  if [ "$((n + 1))" -ge "$RUNAWAY_CEILING" ]; then printf 'CEILING\n'; return 0; fi
  if [ "$((n + 1))" -ge "$bound" ]; then printf 'BOUNDED\n'; return 0; fi
  printf 'CONVERGING\n'
}
```

Order is the whole design. `CONVERGED` and `NON-CONVERGENT` stay ahead because a clean round and
a flat round are facts about THIS round and outrank any bound. `CEILING` stays ahead of `BOUNDED`
so that a bound equal to the ceiling yields the ceiling's own loud exit, which is what makes the
default third argument today's behaviour verbatim. A bound of 1 makes the first round of a subject
terminal unless it is clean; a bound of 2 lets a strictly smaller second round end the loop rather
than re-arm it. The sliced arms in the suite call this with two arguments and hold unchanged.

### The verb

`verb_review` at `:4030` computes `state=$(review_state "$prior" "$blockers")` at `:4099`. It
passes the bound instead:

```bash
bound=$RUNAWAY_CEILING; [ "$subj" = "$slug" ] || bound=$REVIEW_ROUNDS
state=$(review_state "$prior" "$blockers" "$bound")
```

The subject test is the same equality `review_last_reason` makes and the `--close` term at
`:3527` relies on: the closing loop's subject IS the slug, the harness records a spec audit as
`<slug>-spec-set` at `tools/workflows/unattended-build.template.js:625`, and `TOOL-dHonouredPark-8`
records why the two must not share a subject. Four more edits in the verb:

- The terminal grep at `:4095` gains `BOUNDED` in its alternation, so a bounded subject refuses a
  further round with the existing `fail 37` message, which already says a later blocker is
  DISPOSED and never re-rounded.
- The state gate at `:4104` to `:4116`: the first case becomes `NON-CONVERGENT|CEILING|BOUNDED)`
  with body `[ -n "$disposition" ] || disposition=promote`; the `fail 37 "--review exits $state
  and requires --disposition ..."` branch at `:4107` is deleted. The `*)` case keeps its refusal
  of an explicit disposition on a non-terminal round. The default is `promote` because the
  severity rule the owner set makes `promote` the demanded value whenever a blocker stands, a
  standing blocker is the only way a non-`CONVERGED` exit is reached, and the gotcha
  `one-value-field-records-a-mixed-outcome` already rules that a one-value field records the
  value that demands something. `review_exit_note`'s `*)` arm stays unreachable and keeps saying so.
- The `note` case at `:4117` gains `BOUNDED) note=" · BOUNDED" ;;`, so the row reads
  `verdict <v> · blockers <n> · BOUNDED · disposition <d>` in the grammar check 2 already parses.
- The echo case at `:4127` gains its own sentence: the declared round bound of `$REVIEW_ROUNDS`
  is reached, the loop STOPS here, and every standing blocker is disposed by severity, followed by
  `review_exit_note "$disposition"`. The `four states` comment above `review_state` at `:3971`
  becomes five.

### The readers

`--close`'s `diff-reviewed` term at `:3533` reads `*CONVERGED*|*NON-CONVERGENT*|*CEILING*)`; it
gains `*BOUNDED*`, and its header paragraph says the token cannot occur on the slug subject
because that subject's bound is the ceiling, so the case is parity and not a reachable branch.
Check 2 in `tools/unattended/check-unattended.sh` at `:512` and `:513` reads
`rs ~ /CONVERGED|NON-CONVERGENT|CEILING/` into `term` and `rs ~ /NON-CONVERGENT|CEILING/` into
`needs`; both gain `BOUNDED`. The `needs` half is the one with teeth: a graded record whose
`BOUNDED` row carries no disposition is the NO-disposition refusal, and one carrying `promote`
demands a new non-`WONTDO` unit id since the run's BASE, which is the obligation unit 7's stage
discharges. The `term` half cannot be observed through a driver-written record, because the
driver writes `BOUNDED` only on a strictly smaller count and the stalled-loop clause needs a flat
one; it lands for parity and section 6 says how it is observed.

### The harness and its carriers

`REVIEW_TOKENS` at `tools/workflows/unattended-build.template.js:647` gains `'BOUNDED'`, and the
recorder prompt at `:628` to `:629` names five tokens. Nothing else in the template moves: the
`verdict === 'CONVERGING'` hand-back at `:674` and the `verdict === 'CONVERGED'` skip at `:725`
both let `BOUNDED` fall through to the disposal stage exactly as `NON-CONVERGENT` does. The
render `tools/workflows/unattended-build.js` is re-made by the parity leg's `--render` mode, and
the harness suite's loop at `tools/workflows/unattended-build.test.sh:138` becomes
`for v in CONVERGED NON-CONVERGENT CEILING BOUNDED`.

`VERBS.template.md:102` to `:112` describes four states and says `--disposition` is REQUIRED at a
terminal exit; it names five, says the exit RECORDS a disposition that defaults to `promote` and
may be spelled `fold`, and keeps every refusal it lists except the terminal-without-disposition
one. `SKILL.template.md:615` to `:648`: the section's opening paragraph, which argues that a
round cap only moves the stall earlier, gains the reconciling sentence that a SPEC subject's
bound ends in a disposition rather than a stall; "one of four states" at `:630` becomes five; a
`BOUNDED` bullet joins the list; and the "Record which you took" sentence at `:642` says the
default. `PROTOCOL.template.md:452`'s table gains a `REVIEW_ROUNDS` row beside `GATE_BOUND`, and
the `closing-review-recorded` row at `:334` stops counting "three declared exits" and says "a
declared exit", because the driver owns that count. `kit.toml:92`'s `optional_keys` gains the key.
`.unattended.conf:32`'s `GATE_BOUND` block gains a `REVIEW_ROUNDS="1"` block beneath it carrying
the ruling, and `tools/unattended/.unattended.conf.example:33` gains the same, because check 22
joins the protocol table, the example and the project conf in both directions and reds any one
of the three missing a key the others carry.

### The method

`tools/memory-tree/BUILD-METHOD.template.md:140` opens M4's convergence paragraph with two
sentences this unit replaces, measured at 287 bytes on 2026-09-14:

> **A BLOCKED verdict has a disposition, and until now it had none.** The loop is bounded by
> CONVERGENCE, not a round count: a round re-arms only if its confirmed-blocker count is STRICTLY
> SMALLER than the one before — not merely "changed", which a 2, 1, 2 oscillation satisfies forever.

The replacement, measured at 274 bytes, so 13 bytes under:

> **A BLOCKED verdict has a disposition.** A SPEC subject takes `REVIEW_ROUNDS` rounds (protocol
> §8) and exits BOUNDED; the DIFF review converges: a round re-arms only on a count STRICTLY
> SMALLER than the round before, never merely "changed", which 2, 1, 2 satisfies forever.

The disposal sentence that follows is unit 7's and is not touched. "protocol §8" is a pointer
and not a restatement, which is M1's rule for this file. The render `memory/guides/BUILD-METHOD.md`
is re-made by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, and because that
file is one the kickoff manifest WATCHES, `memory/guides/SESSION-KICKOFF.md`'s `last-audit` is
re-stamped in the same commit with a delta line in the commit message.

### The suite

`mkconf` at `tools/unattended/unattended.test.sh:108` writes `GATE_BOUND="${4-3600}"`; it gains
`REVIEW_ROUNDS="${6-8}"`, the ceiling, so every existing review arm keeps its sequence. The new
arms sit beside the review-loop arms at `:4530` to `:4646`:

- sliced `review_state` arms: `review_state '' 3 1` is `BOUNDED`; `review_state '3' 2 2` is
  `BOUNDED`; `review_state '' 3 8` is `CONVERGING`; `review_state '9 8 7 6 5 4 3' 2 8` is still
  `CEILING`; `review_state '' 0 1` is `CONVERGED`; `review_state '2' 2 1` is `NON-CONVERGENT`.
- verb arms under a conf written with the sixth positional at 1: a spec subject's first round with
  3 blockers prints `BOUNDED · disposition promote` and the row carries the same; a second round
  on that subject hits the terminal refusal; the slug subject's first round with 3 blockers prints
  `CONVERGING`; an explicit `--disposition fold` on a bounded round writes `fold`.
- the rewritten arm at `:4634`: `run --review tRun --subject D1 --verdict BLOCKED --blockers 3`
  after a first round of 3 prints `NON-CONVERGENT · disposition promote`, where it asserted the
  deleted refusal.
- the `NOCONF` conf at `:5206`, which declares no `GATE_BOUND`, also declares no `REVIEW_ROUNDS`,
  so the arm at `:5219` gains a second `hit` on the new NOTE; a conf declaring `REVIEW_ROUNDS="9"`
  hits the above-ceiling refusal and one declaring `0` hits the not-positive refusal.

### Inventory

| Identifier | Kind | Cell | Note |
|---|---|---|---|
| `REVIEW_ROUNDS` | conf key | none graded | joins `GATE_BOUND`'s preset, table row and example |
| `BOUNDED` | review state token | none | joins the closed set in every carrier section 3 lists |
| `bound` | local in `verb_review` | none | shell locals are not graded |

No new function or verb, so the lexicon and check 26 populations are unchanged.

### Files touched (estimate)

- the driver and its suite: `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`
- the leg and its suite: `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`
- the kit's prose templates: `tools/unattended/VERBS.template.md`, `tools/unattended/SKILL.template.md`,
  `tools/unattended/PROTOCOL.template.md`, with their renders under `memory/guides/` and
  `.claude/skills/unattended/`
- the declarations: `tools/unattended/kit.toml`, `tools/unattended/.unattended.conf.example`,
  `.unattended.conf`
- the harness: `tools/workflows/unattended-build.template.js`, its render
  `tools/workflows/unattended-build.js`, and `tools/workflows/unattended-build.test.sh`
- the method: `tools/memory-tree/BUILD-METHOD.template.md`, its render `memory/guides/BUILD-METHOD.md`,
  and the watched-file re-stamp in `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **A file constant instead of a conf key.** `RUNAWAY_CEILING`'s header argues against an
  environment override because it leaves no diff; a tracked conf key leaves one, and the owner
  named the key.
- **Keep `--disposition` required and have the harness's recorder pass `promote`.** The recorder
  prompt at `:624` runs the verb without the flag, so today a terminal exit fails there with
  `fail 37` and the agent returns stderr; a default in the driver fixes the harness and every
  hand-run alike, where a prompt edit fixes one caller.
- **Make `BOUNDED` re-arm nothing but not be terminal.** A state that is neither terminal nor
  re-arming is the abandoned loop `diff-reviewed`'s second term was built to refuse.

## 5. Production-readiness checklist

- security — a conf key read where `GATE_BOUND` is, validated before use; the leg's conf import
  allow-list does not need it, because no leg reads the bound.
- perf / scale — the change is one integer comparison per recorded round and, at the harness, one
  fewer lens fan per spec audit that confirms a blocker, which is the point.
- error / empty / loading states — absent key defaults and announces; malformed, zero or
  above-ceiling refuses at start-up before any verb runs; an empty prior sequence at a bound of 1
  is the common `BOUNDED` case and is arm one.
- observability — the `BOUNDED` echo names the bound in force; the NOTE names the default; the
  row grammar is unchanged so `--status` and check 2 read it as they read the other exits.
- risks — a hand-edited record pairing `BOUNDED` with a flat count is not caught by the
  stalled-loop clause once `term` admits it, which is the same latitude `NON-CONVERGENT` has
  today and is stated in section 4; the M4 edit and the manifest re-stamp are two carriers that
  must land in one commit.
- testing — section 6: six sliced arms, five verb arms, three conf arms, one check-2 fixture pair,
  one harness loop member, and the byte measurement.
- migration — N/A. Landed run-state records carry no `BOUNDED` row and nothing rewrites them; a
  record written by the new driver parses under the old check 2 as a round with no exit token,
  which is why the two ship in one commit.
- user docs — the Skill, VERBS and protocol renders are the user docs and are S7.

## 6. Acceptance criteria

The driver suite `tools/unattended/unattended.test.sh` and the leg suite
`tools/unattended/check-unattended.test.sh` are on no bar leg, by the 2026-08-23 ruling their
`kit.toml` records, and `TOOL-aHoistedPass-38` records the leg suite red in both shards for causes
that predate this build. So no criterion below reads a suite's exit status; each reads the arm's
own line. The pass observes each criterion by the single command it names, and the suites whole
are the closing pass's compensating run.

- **AC1** — When `bash tools/unattended/unattended.sh --status <slug>` runs in a fixture tree whose
  conf declares no `REVIEW_ROUNDS`, its stderr carries `declares no REVIEW_ROUNDS, so a spec-audit
  subject exits BOUNDED after the kit default of 1 round`.
  Red when: the default is silent, or the key is read before the conf is sourced so a declared
  value is overwritten by the default.
- **AC2** — When the same verb runs with `REVIEW_ROUNDS="9"` declared, the driver exits 2 naming
  the runaway ceiling of 8; with `REVIEW_ROUNDS="0"` it exits 2 naming a positive integer of
  rounds.
  Red when: a value above the ceiling is accepted, which makes the bound unreachable, or zero is
  accepted, which ends every loop before it starts.
- **AC3** — When `review_state` is sliced out of the driver by the suite's `slice_fn` and called,
  `review_state '' 3 1` prints `BOUNDED`, `review_state '3' 2 2` prints `BOUNDED`,
  `review_state '' 3 8` prints `CONVERGING`, `review_state '' 3` with no third argument prints
  `CONVERGING`, `review_state '2' 2 1` prints `NON-CONVERGENT`, and
  `review_state '9 8 7 6 5 4 3' 2 8` prints `CEILING`.
  Red when: `BOUNDED` is tested before `NON-CONVERGENT` or `CEILING`, so a flat count or a ceiling
  hit reads as bounded; or the default third argument is not the ceiling, so the two-argument
  arms move.
- **AC4** — When a fixture run under a conf written with `REVIEW_ROUNDS` at 1 records
  `--review tRun --subject B1 --verdict BLOCKED --blockers 3` with no `--disposition`, the verb
  prints `BOUNDED · disposition promote` and the run-state file gains one row whose reason is
  `verdict BLOCKED · blockers 3 · BOUNDED · disposition promote`; a second round on `B1` is refused
  with the existing terminal-round message.
  Red when: the base driver is used, which prints `CONVERGING` and arms the loop; or the default
  is announced and not written, so the row carries no disposition and check 2 refuses it.
- **AC5** — When the same fixture records `--review tRun --subject tRun --verdict BLOCKED
  --blockers 3`, the verb prints `CONVERGING`, because the slug subject's bound is the ceiling.
  Red when: the bound is applied to every subject and the closing diff review ends at round 1.
- **AC6** — When a fixture under the ceiling-bound conf records two rounds of 3 blockers on `D1`
  with no `--disposition`, the second prints `NON-CONVERGENT · disposition promote` and the row
  carries it, where at base the second round is refused with `and requires --disposition`; an
  explicit `--disposition promote` on the first round is still refused with `not a terminal exit`.
  Red when: the deleted refusal still fires, or the non-terminal refusal went with it.
- **AC7** — When `grep -n 'CONVERGED\*|\*NON-CONVERGENT\*|\*CEILING\*|\*BOUNDED\*' tools/unattended/unattended.sh`
  runs at the landed tip, it prints one line inside the `diff-reviewed` term, and the comment
  block above it says the token is unreachable there.
  Red when: the case was left at three tokens, or it was widened without saying why a fourth
  token that cannot occur is listed.
- **AC8** — When `bash tools/unattended/check-unattended.sh` runs over a fixture record under
  a graded `DISPOSITION_CUTOFF` whose only review row is `blockers 2 · BOUNDED` with no
  disposition, it prints the `record NO disposition` refusal for check 2; the same row with
  `· disposition promote` and one new unit id in the README's units region prints no `check 2`
  line. At base the first fixture prints nothing, which is the red-first observation. The `term`
  membership is observed by `grep -c 'CONVERGED|NON-CONVERGENT|CEILING|BOUNDED'` over the leg
  printing 1, and the spec states why no driver-written record can discriminate it.
  Red when: `needs` was left at two tokens, so a bounded promote owes nothing and the exit is
  green-by-absence.
  fixture: the leg suite's `mkdisp` and `dispconf` helpers at `tools/unattended/check-unattended.test.sh:826`
  to `:851` are the shape; `DISPOSITION_CUTOFF` is the one key the fixture conf arms.
- **AC9** — When `node tools/workflows/check-workflow-syntax.js` runs at the landed tip it exits 0,
  `grep -c "'BOUNDED'" tools/workflows/unattended-build.template.js` and the same over the render
  each print 1, and the harness suite's terminal loop, run with the test double returning
  `BOUNDED` and zero blockers, prints `BOUNDED: hands out a roster`.
  Red when: the token is in one of template and render only, which the parity leg reds; or the
  double's `BOUNDED` falls into the "not one of" throw.
- **AC10** — When `bash tools/unattended/adopt-unattended.sh --check` runs at the landed tip it
  exits 0, `grep -c 'REVIEW_ROUNDS' tools/unattended/PROTOCOL.template.md tools/unattended/kit.toml
  .unattended.conf tools/unattended/.unattended.conf.example` prints 1 or more for each, and
  `grep -c 'BOUNDED' tools/unattended/VERBS.template.md tools/unattended/SKILL.template.md` prints
  1 or more for each. `bash tools/unattended/check-unattended.sh` prints no `check 22` line.
  Red when: a render is stale; or a carrier is missing the key, which check 22 reports as
  undocumented, documented-but-in-no-example, or set-by-this-project-and-undocumented.
- **AC11** — When `wc -c memory/guides/BUILD-METHOD.md` runs at the landed tip it prints a
  number at or below the figure at base, `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md`
  exits 0, `bash tools/memory-tree/kit-dogfood-parity.test.sh` prints no `FAIL` line for the
  method pair, and `bash skills/session-kickoff/manifest-check.sh` exits 0 on the commit that
  moved the render.
  Red when: the swap added bytes; or the render was not re-made; or the manifest's `last-audit`
  was not re-stamped for a watched file.
  figure: the base byte count is DERIVED by the same `wc -c` at base, 26743 measured 2026-09-14;
  the 287-to-274 sentence delta in section 4 is PINNED from that measurement.
- **AC12** — When `bash tools/unattended/unattended.test.sh --shard 2/2` runs at the landed tip,
  it prints no `FAIL` line naming any arm section 4's suite paragraph adds, no `FAIL executed`
  line, and `FLOOR_ASSERTIONS` at `tools/unattended/unattended.test.sh:5434` and `FLOOR_SHARD_2`
  at `:5461` stand exactly the added arms' executed assertions above their base values of 706 and
  510; at base, the same shard prints `FAIL` for every added arm.
  Red when: an added arm is stranded past a floor exit, so the floors did not move; or an existing
  sequence arm moved because `mkconf`'s default bound is not the ceiling.
  cost: minutes; the shard is on no bar leg and is `--close`'s compensating run via
  `bash tools/unattended/run-unattended-gates.sh` on a frozen clone.
  figure: the added-arm count is DERIVED from the suite's floor-breach line with the floor
  over-pinned, the method `TOOL-aRatifiedRulings-2` AC6 records; the floors are then PINNED.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `kit/dogfood doc parity` · `build-method size` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

These are the legs `--close` runs, not what the pass runs: the pass verifies with the one command
each criterion in section 6 names and nothing else. From `tools/gate-legs.json` at base:
`unattended kit gate` is chunk `declarations`, unguarded, and carries check 2 and check 22;
`unattended skill wiring` is chunk `wiring`, unguarded, and is AC10's render check; `harness arms`
is chunk `declarations`, unguarded, and holds because one branch leaves and none arrives;
`review-protocol parity` is chunk `declarations`, unguarded, and byte-compares the harness
template against its render; `workflow script syntax` is chunk `wiring`; `kit/dogfood doc parity`
is chunk `declarations`, guarded on the method render among others, and compares
`BUILD-METHOD.template.md` with `memory/guides/BUILD-METHOD.md`; `build-method size` is chunk
`product`, unguarded, and is AC11's cap. `memory hygiene` and `spec tokens` grade this file. The
three self-test suites section 6 names are on no leg and are the close's compensating run.

New arm: `tools/unattended/unattended.test.sh` · every verb arm against the driver at base, which
prints `CONVERGING` where `BOUNDED` is expected and refuses the terminal round that now defaults ·
`FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the arms' executed assertions.
New arm: `tools/unattended/check-unattended.test.sh` · the `BOUNDED`-without-disposition fixture
against the leg at base, which prints nothing · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by two.
New arm: `tools/workflows/unattended-build.test.sh` · the loop member `BOUNDED` against the render
at base, which throws on an unknown token · none.

## 8. Open questions

none

Three choices were made without a fork and each is a consequence rather than a preference: the
default disposition is `promote` because the owner's severity rule and the recorded gotcha both
demand the value that owes something; the bound is a conf key because the owner named it and the
ceiling's own header rejects only an environment override; and `review_state`'s third argument
defaults to the ceiling because any other default changes a two-argument call, and the one
caller always passes it.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "bound the number of review rounds a spec-audit subject may take before the loop exits"`,
run 2026-09-14 at this worktree, reported `scan coverage: 71 files scanned | 0 parse skips |
unscanned layers: .sh` and ranked `boundedParallel`, `run_bounded` and the `.unattended.conf`
affordance seam; every file this unit's mechanism lives in is `.sh`, so the map probe is blind to
the subject and the seam was found by reading the source. It exists: `review_state` at
`tools/unattended/unattended.sh:3974` is the predicate and takes the bound as one more argument;
`verb_review` at `:4030` already holds `subj` and `slug` and makes the equality the bound keys on;
the `GATE_BOUND` block at `:305` to `:312` is the conf-read shape the key copies verbatim; check
2's awk at `tools/unattended/check-unattended.sh:512` to `:513` is the reader whose two regexes
gain a token. The recall query returned `TOOL-dCarriedReceipt-1`, which records that
`review_state` reads only the rows a run can see; `TOOL-dHonouredPark-8`, which records why a spec
audit and the closing review must not share a subject; `TOOL-aBoundedVerdict-1`'s convergence
predicate, the origin of the four states; `TOOL-dFoldedVerdict-1`'s build record, which pins the
refusal this unit deletes; `TOOL-aProvenReuse-3`, the open row that asked what a promoted spec
blocker is; and `TOOL-aLeakedHandle-6`, the ruling that a converged subject is disposed and never
re-rounded, which the terminal grep's `BOUNDED` member extends. Where a hit was stale:
`TOOL-aBoundedVerdict-1` says a first round always re-arms when blockers are above zero, and the
Skill's opening paragraph says a round cap only moves the stall earlier; both are superseded by
the 2026-09-14 ruling for SPEC subjects, and the Skill paragraph is rewritten so the two answers
agree.

Recall terms used: `review round convergence CONVERGING NON-CONVERGENT disposition fold promote blockers ceiling spec-audit tier2 bound one round`

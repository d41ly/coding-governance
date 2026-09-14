# TOOL-aProbedUnit-6 — `REVIEW_ROUNDS` bounds a spec-audit subject; the `BOUNDED` exit

**Status:** CLOSED · rev-6 · 2026-09-14 · node a · Tier-2 · base 1b000d1a · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-aProbedUnit-6-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aProbedUnit-6-1-acceptance-ledger.md) | journal | — |
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-7 |
| [2026-09-14-prompt-TOOL-aProbedUnit-6-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-6-1-build-brief.md) | journal | — |
| [2026-09-14-review-TOOL-aProbedUnit-1-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-diff-review-round1.md) | diff-review | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round2.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-7 |

<!-- /gen:spec-records -->

## 1. Goal

`review_state` in `tools/unattended/unattended.sh` re-arms the loop at round 1 whenever the
blocker count is above zero, so every spec audit that confirms one blocker costs a second lens
fan. The owner ruled on 2026-09-14 that a SPEC subject takes one round by default and that the
closing DIFF review keeps its convergence loop. This unit gives the driver a conf key
`REVIEW_ROUNDS`, a fifth state `BOUNDED` that is terminal and owes a `--disposition` exactly as the
other two terminal exits do, and lands the vocabulary in every carrier that spells the state set.

## 2. Scope (IN)

- **S1** — A conf key `REVIEW_ROUNDS`, preset beside `GATE_BOUND=""` before the conf is sourced and
  read through `read_bound_key`, the defaulted-validated-announced reader `TOOL-aProbedUnit-3`
  hoists out of the `GATE_BOUND` block and lands first: default 1, the default ANNOUNCED on stderr,
  malformed or zero REFUSED with exit 2. One line of this unit's own, after `RUNAWAY_CEILING` is
  defined, refuses a value AT OR ABOVE that ceiling — `-lt`, because `review_state` tests the
  ceiling first, so a bound equal to it is exactly the value the sentence refuses (rev-6; rev-5's
  `-le` accepted it). The default is the constant `REVIEW_ROUNDS_DEFAULT=1` beside the other two,
  interpolated into the NOTE (rev-6). Observed by AC1 and AC2.
- **S2** — `review_state` takes an optional third argument, the bound, defaulting to
  `RUNAWAY_CEILING`, and returns `BOUNDED` when `n+1 >= bound` after the three existing tests and
  before `CONVERGING`. With the default bound the function is byte-for-byte today's behaviour,
  because `CEILING` fires at equality first. Observed by AC3.
- **S3** — `verb_review` passes `REVIEW_ROUNDS` as the bound when the subject is NOT the build
  slug and `RUNAWAY_CEILING` when it is; `BOUNDED` joins the terminal grep, the state gate's
  terminal case, the `note` case and the echo case with its own sentence. `--disposition` stays
  REQUIRED at every blocker-bearing exit (`NON-CONVERGENT`, `CEILING`, `BOUNDED`) and REFUSED on
  a `CONVERGING` round, by the 2026-09-01 owner ruling section 8 cites; a `BOUNDED` exit without
  one is the `fail 37` refusal naming the state. Rev-6 (closing review cluster C): at those three
  exits `fold` is REFUSED by its own `fail 37`, because `review_state` returns `CONVERGED` for
  count 0 so each of them stands on a blocker the severity rule promotes; at `CONVERGED` a
  disposition is ACCEPTED and never required, written into the row, so the highs disposed at zero
  blockers are recordable. Observed by AC4, AC5 and AC6 as re-targeted.
- **S4** — `--close`'s `diff-reviewed` term admits `BOUNDED` in its terminal case, for vocabulary
  parity, with the header saying it is unreachable for the slug subject. Observed by AC7.
- **S5** — `tools/unattended/check-unattended.sh` check 2: `BOUNDED` joins the `term` regex and
  the `needs` regex, so a `BOUNDED` exit owes a disposition and a promote owes an id exactly as
  `NON-CONVERGENT` does. Observed by AC8.
- **S6** — `tools/workflows/unattended-build.template.js` and its render: `REVIEW_TOKENS` gains
  `BOUNDED`; the recorder prompt names five tokens and tells the recorder to run the verb once
  without `--disposition` and, when the driver refuses naming `--disposition`, once more with
  `--disposition promote`; the harness suite's terminal loop gains `BOUNDED`. Observed by AC9.
- **S7** — The prose carriers land in the same commit: `VERBS.template.md`'s `--review` bullet,
  `SKILL.template.md`'s "Record each review round" section, `PROTOCOL.template.md` section 8's
  key table and its `closing-review-recorded` row, `kit.toml`'s `optional_keys`,
  `.unattended.conf` and `.unattended.conf.example` with the reason beside the key, then
  `bash tools/unattended/adopt-unattended.sh` re-renders. Observed by AC10.
- **S8** — `tools/memory-tree/BUILD-METHOD.template.md` M4's convergence sentence becomes the
  round-bound rule, byte-neutral or better, leaving the disposal sentence to unit 7; the render
  is re-made and the kickoff manifest's `last-audit` is re-stamped in the same commit. Observed by
  AC11.
- **S9** — `tools/unattended/unattended.test.sh`: `mkconf` gains a SEVENTH positional,
  `REVIEW_ROUNDS="${7-7}"`, defaulting to one below the ceiling (rev-6; rev-5's `8` is refused at
  startup now) so every existing sequence arm holds unchanged — the sixth is `TOOL-aProbedUnit-3`'s, `UNIT_STALL_BOUND="${6-1800}"`, landed ahead
  of this pass; the new arms section 6 names land beside the review-loop arms, the
  requires-disposition arm at `:4634` stands in this pass, and the floors rise by the arms added.
  Observed by AC12.

## 3. Non-goals (OUT)

- **Disposal by severity is unit 7's.** The harness's `DISPOSAL` stage, its `confirmed === 0`
  skip, its `promoted`/`folded` counts, M4's disposal sentence, and the Skill's `NON-CONVERGENT`
  bullet's severity wording are not touched here. This unit makes `BOUNDED` flow into that stage
  the way `NON-CONVERGENT` does today and nothing more.
- **The closing diff review is unchanged in behaviour.** Its subject is the build slug, its bound
  is the ceiling, and no round it records can read `BOUNDED`. `TOOL-aProvenReuse-3`'s question,
  what a promoted SPEC blocker is, is answered by unit 7's ruling; the row's status flip is the
  CLOSING pass's, as spec 7's Edge says, because `memory/backlog` is a `SHARED_RECORDS` member and
  no dispatched pass may declare it.
- **`RUNAWAY_CEILING` stays a file constant** at `tools/unattended/unattended.sh:464`, for the
  reason its header gives. `REVIEW_ROUNDS` is a conf key because a tracked conf leaves a diff
  behind, which is the property that header wants.
- **`--disposition` stays REQUIRED at a terminal exit and both values stay legal.** The `fail 37`
  branch at `:4107` keeps its requirement and gains `BOUNDED` in the case it guards; the closed
  set `REVIEW_DISPOSITIONS` and its two refusals are unchanged. The driver writes no default:
  section 8 records the fork and the 2026-09-01 ruling that settles it.
- **No new verb, no new `fail` branch, no new function.** The key's reader is `read_bound_key`,
  which `TOOL-aProbedUnit-3` lands ahead of this unit; it is an `echo` and `exit 2` at conf-read
  time with no `fail N` branch, exactly as the `GATE_BOUND` block at `:305` to `:311` it was
  hoisted from, so `harness arms` gains nothing to arm, and the above-ceiling line this unit adds
  is the same shape. No branch leaves either, so the driver's branch floor in `ARMS_FLOORS`, 104
  against 194 measured on 2026-09-14, does not move.
- **No kit version bump inside this unit.** Unattended `1.21` to `1.22` and memory-tree `2.75` to
  `2.76` are the closing pass's, once each, across every carrier the build README names.
- **Not parallel with unit 3 or unit 7.** Unit 3 edits `unattended.sh`, `kit.toml`'s
  `optional_keys`, `PROTOCOL.template.md` section 8, `.unattended.conf` and `SKILL.template.md`;
  unit 7 edits the same M4 paragraph and the same harness template. The write sets intersect, so
  the passes are sequential, in roster order.

### Edges

- **hands-off** `TOOL-aProbedUnit-7` — the disposal sentence in M4, the harness's disposal
  stage, the disposal clause of the terminal-round `fail 37` message at
  `tools/unattended/unattended.sh:4096`, which still says `fold or promote`, the `admits BOTH`
  clause of the requires-disposition `fail 37` at `:4107` with its comment at `:4101` to
  `:4103`, and `review_exit_note`'s two sentences at `:4025` to `:4026`, which open `every
  blocker still standing`. This unit writes the round-bound sentence beside M4's, the `BOUNDED`
  token into `REVIEW_TOKENS`, into the grep above the `:4096` message and into the case that
  guards the `:4107` one, and leaves every one of those messages' own words to unit 7, which
  rewrites every carrier of the disposal rule in one commit.
- **consumes-from** `TOOL-aProbedUnit-3` — `read_bound_key <NAME> <DEFAULT> <UNIT> <NOTE>`, the reader
  that unit hoists out of the `GATE_BOUND` block for `UNIT_STALL_BOUND` and that this unit's key
  routes through. The decision spec 3 delegated here is taken: the three keys share one reader,
  and the one arm the others lack, the above-ceiling refusal, is one line after the call.
- **consumes-from** external — the owner's ruling of 2026-09-14 in the run mandate's owner-turn
  table: one round for SPECS ONLY, the diff review keeps its loop. Without it the bound would be
  a run's own choice, which M3 forbids.
- **hands-off** external — the two kit version bumps at the closing pass.

## 4. Design

### The key

`GATE_BOUND` is preset at `tools/unattended/unattended.sh:292`, the conf is sourced at `:294`, and
at base the value is defaulted, validated and announced by the inline `case` at `:305` to `:312`.
`TOOL-aProbedUnit-3`, order 3, hoists that `case` into `read_bound_key <NAME> <DEFAULT> <UNIT> <NOTE>` —
blank takes the default and prints the NOTE on stderr, `*[!0-9]*|0` prints `REFUSING - <NAME> is
declared as '<value>', which is not a positive integer` and exits 2, an integer stands — and
routes `GATE_BOUND` and `UNIT_STALL_BOUND` through it. This is the third key, and it is a CALL,
not a third copy. `REVIEW_ROUNDS=""` joins the preset line at `:292`. The call sits directly after
`RUNAWAY_CEILING="8"` at `:464`, because the one arm the other two keys lack, the upper bound, IS
that constant and a comparison written above its definition reads an empty string:

```bash
read_bound_key REVIEW_ROUNDS "$REVIEW_ROUNDS_DEFAULT" rounds "a spec-audit subject exits BOUNDED after the kit default of ${REVIEW_ROUNDS_DEFAULT} round(s)"
[ "$REVIEW_ROUNDS" -lt "$RUNAWAY_CEILING" ] || { echo "unattended: REFUSING - REVIEW_ROUNDS is $REVIEW_ROUNDS, at or above the runaway ceiling of $RUNAWAY_CEILING, so the ceiling would fire first and the declared bound could never be reached." >&2; exit 2; }
```

The exact NOTE and REFUSING sentences the reader composes are spec 3's; this unit owns the NOTE
clause it passes and the at-or-above-ceiling line, and section 6 asserts only those. Rev-6: the
kit default is `REVIEW_ROUNDS_DEFAULT=1`, a constant beside `GATE_BOUND_DEFAULT` and
`UNIT_STALL_BOUND_DEFAULT`, interpolated into the NOTE exactly as its siblings are. Rev-5 argued
for a literal `1` in the call "because one reader exists"; the closing review (cluster I) found
the digit typed TWICE — the argument and the prose NOTE — so raising the argument left the
sentence saying 1 and the arm green, which is the two-spellings fault the argument claimed to
avoid. The comparison is `-lt` (cluster H): `review_state` tests the ceiling before the bound, so
a bound EQUAL to the ceiling can never surface as `BOUNDED`, which is the condition the refusal
sentence names. If the reader is not in the tree
when this pass opens — unit 3 parked or re-ordered — the pass STOPS and says so rather than
writing the inline copy back: the delegated decision was taken once, in spec 3's fold of the
round-1 audit's cluster F and here, and a third copy is the thing it decided against.

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
  further round with the existing `fail 37` message at `:4096`, which already says a later blocker
  is DISPOSED and never re-rounded. That message's `fold or promote` clause is unit 7's to
  rewrite to the severity rule, with the three suite arms that quote it; this unit changes the
  grep and not the words.
- The state gate at `:4104` to `:4116`: the first case becomes `NON-CONVERGENT|CEILING|BOUNDED)`
  and KEEPS its body, the `fail 37 "--review exits $state and requires --disposition ..."` at
  `:4107`, so a `BOUNDED` exit without a disposition is refused with a message naming `BOUNDED`.
  That message's `because the method admits BOTH fold and promote at the exit` clause, and the
  `M4 admits BOTH` comment above the gate at `:4101` to `:4103`, are unit 7's to reword to the
  severity rule, with the arm at `:4634` that quotes the clause; this unit widens the case and
  keeps the body's bytes.
  The `*)` case keeps its refusal of an explicit disposition on a non-terminal round. Rev-6
  (cluster C): the blocker-bearing case gains a second `fail 37` refusing `fold`, the
  requires-disposition sentence names `promote` and the standing count, and `CONVERGED)` is its
  own case accepting an optional disposition — the echo then carries `· disposition <d>` and
  `review_exit_note`; check 2 counts a `CONVERGED · disposition promote` row into `nneed` and reds
  `fold` beside a non-zero blocker count. Nothing here
  writes a default: the 2026-09-01 owner ruling in `memory/builds/dFoldedVerdict/README.md`,
  "a forced value is a constant, and a constant is not evidence for the clause that reads it — so
  the field stays evidence at every exit", is the reason `fail 37` exists, and a driver-written
  `promote` is exactly the constant it refused. `review_exit_note`'s `*)` arm stays unreachable
  and keeps saying so.
- The `note` case at `:4117` gains `BOUNDED) note=" · BOUNDED" ;;`, so the row reads
  `verdict <v> · blockers <n> · BOUNDED · disposition <d>` in the grammar check 2 already parses.
- The echo case at `:4127` gains its own sentence: the declared round bound of `$REVIEW_ROUNDS`
  is reached, the loop STOPS here, and every CONFIRMED finding is DISPOSED BY SEVERITY (rev-6,
  cluster G; rev-5 said "every standing blocker", the pre-severity-rule half left standing),
  followed by `review_exit_note "$disposition"`. The `four states` comment above `review_state` at `:3971`
  becomes five.
- Two comment blocks carry the withdrawn-cap ruling — `TOOL-aBoundedVerdict-1`, "the loop's
  engine was M4's missing BLOCKED disposition, not a missing count" — in the driver's own words
  and are rewritten, because after this pass `review_state` exits `BOUNDED` on a count
  for spec subjects and a paragraph above it saying a count is the wrong variable is the
  two-answers class the README's rule four names. `WHY A PREDICATE AND NOT A COUNT` at `:3966`
  to `:3969`, directly above `review_state`, says "a round cap does not give a loop an exit; it
  moves the stall earlier" and ends by restating the disposal rule; the `RUNAWAY_CEILING` header
  at `:457` to `:458` says the loop is "bounded by a CONVERGENCE PREDICATE, not by a count". Both
  become the one statement: a SPEC subject is bounded by `REVIEW_ROUNDS` and exits in a
  disposition, the DIFF review by convergence, and the ceiling backstops both. The rewritten
  `:3966` block carries no disposal words — the rule lives in M4 and the Skill, unit 7's carriers,
  and a comment paraphrasing it is the copy that rots — so `blocker still standing` at `:3969`
  goes with the rewrite and `moves the stall earlier` prints zero times in the driver at the tip.
  No parity or method-carriers leg reads comment prose, which is why AC7 greps for it.

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
recorder prompt at `:621` to `:631` names five tokens. That prompt runs the verb with no
`--disposition`, because the recorder cannot know before the driver answers whether this round is
terminal — the state is a property of the SEQUENCE, which only the driver sees — and an explicit
disposition on a non-terminal round is refused. Today a terminal exit therefore fails there with
`fail 37` and the agent returns stderr. The prompt gains one instruction: if the command REFUSES
naming `--disposition`, run the same command again with `--disposition promote` appended and
return THAT run's token and exit code. `promote` is the value the severity rule demands at every
exit the refusal can be reached from: `NON-CONVERGENT`, `CEILING` and `BOUNDED` are reached only
with blockers standing, and the owner's rule promotes every blocker. The value is the CALLER's,
derived from the count it holds, which is what the 2026-09-01 ruling asks of the field. Nothing
else in the template moves: the `verdict === 'CONVERGING'` hand-back at `:674` and the
`verdict === 'CONVERGED'` skip at `:725` both let `BOUNDED` fall through to the disposal stage
exactly as `NON-CONVERGENT` does. The render `tools/workflows/unattended-build.js` is re-made by
the parity leg's `--render` mode, and the harness suite's loop at
`tools/workflows/unattended-build.test.sh:138` becomes
`for v in CONVERGED NON-CONVERGENT CEILING BOUNDED`.

`VERBS.template.md:102` to `:112` describes four states and says `--disposition` is REQUIRED at a
terminal exit; it names five, `BOUNDED` among the terminal ones, and keeps every refusal it lists,
the terminal-without-disposition one included. `SKILL.template.md:615` to `:648`: the section's
opening paragraph, which argues that a round cap only moves the stall earlier, gains the
reconciling sentence that a SPEC subject's bound ends in a disposition rather than a stall; "one
of four states" at `:630` becomes five, so that phrase prints ZERO times at the tip; and a
`BOUNDED` bullet joins the list, opening `**BOUNDED** — the declared round bound`, a phrase the
file does not carry at base. The "Record which you took" sentence at `:642` stands as written,
since the requirement it states stands. `PROTOCOL.template.md:452`'s table gains a `REVIEW_ROUNDS` row beside `GATE_BOUND`, and
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

The whole-file figure is NOT this unit's to pin. The render measured 26743 bytes at base
`1b000d1a`, and unit 1, order 1, lands its own edit on the same file before this pass opens, so a
criterion holding the tip at or below 26743 reds against a correct build of both specs. What this
unit can assert is its own delta: the render at this pass's commit is exactly 13 bytes smaller
than the render at the pass's parent commit, read with
`git show HEAD~1:memory/guides/BUILD-METHOD.md | wc -c` against `wc -c` at HEAD. The cap itself,
27648, is the `build-method size` leg's, and it holds because the file never crossed 26941, the
recorded high-water, and this pass only lowers it.

### The suite

`mkconf` at `tools/unattended/unattended.test.sh:108` writes `GATE_BOUND="${4-3600}"` from five
positionals at base; `TOOL-aProbedUnit-3`, order 3, takes the SIXTH for
`UNIT_STALL_BOUND="${6-1800}"`, so this unit takes the SEVENTH, `REVIEW_ROUNDS="${7-7}"`, one
below the ceiling (rev-6), and every existing review arm keeps its sequence. The new arms sit beside the
review-loop arms at `:4530` to `:4646`:

- sliced `review_state` arms: `review_state '' 3 1` is `BOUNDED`; `review_state '3' 2 2` is
  `BOUNDED`; `review_state '' 3 8` is `CONVERGING`; `review_state '9 8 7 6 5 4 3' 2 8` is still
  `CEILING`; `review_state '' 0 1` is `CONVERGED`; `review_state '2' 2 1` is `NON-CONVERGENT`.
- verb arms under a conf written with the seventh positional at 1: a spec subject's first round with
  3 blockers and no `--disposition` is refused with `--review exits BOUNDED and requires
  --disposition` and writes no row; the same round with `--disposition promote` prints
  `BOUNDED · disposition promote` and the row carries the same; a second round on that subject
  hits the terminal refusal; the slug subject's first round with 3 blockers prints `CONVERGING`,
  and with `--disposition promote` is refused as `not a terminal exit`; an explicit
  `--disposition fold` on a bounded round writes `fold`.
- the arm at `:4634`, which asserts the requires-disposition refusal on a `NON-CONVERGENT`
  second round, stands in THIS pass: the refusal it observes stands, and this unit changes the
  case that guards it and not the message. It MOVES in unit 7's pass, because the literal it
  quotes — `because the method admits BOTH fold and promote at the exit` — is the `:4107`
  clause spec 7 S7 rewrites to the severity rule; rev-3 said it stands unchanged across the
  build, and that was wrong.
- the `NOCONF` conf at `:5206`, which declares no `GATE_BOUND`, also declares no `REVIEW_ROUNDS`,
  so the arm at `:5219` gains a further `hit` on the new NOTE, beside the one unit 3 adds there
  for `UNIT_STALL_BOUND`; a conf declaring `REVIEW_ROUNDS="9"` hits the above-ceiling refusal
  and one declaring `0` hits the reader's not-positive refusal naming `REVIEW_ROUNDS`.

**How one arm is run alone**, because the README's rule three forbids the suite whole inside a
pass. The suite's preamble, `sed -n '1,/^# ---- REGION ONE/p' unattended.test.sh`, lines 1 to
445, sourced in a shell whose working directory is `tools/unattended` so `HERE` and `SCRIPT`
resolve, defines `hit`, `miss` and `same` at `:69` to `:71`, `reset_tree` and `run` at `:355`
and `:357`, `bcsetup` at `:410` and `bcopen` at `:428`, builds the fixture repository under its
own `mktemp -d` and runs the prologue arms only, which are seconds. It does NOT define
`slice_fn`: that helper's only definition is at `:3930`, inside region two, so the form sources
it too, before use — `eval "$(sed -n '/^slice_fn()/,/^}/p' tools/unattended/unattended.test.sh)"`
— or `slice_fn review_state` is `command not found` and the sliced arms grade nothing. `bcsetup`
then builds the epoch the review-loop arms open with `bcopen`, which is what shard 2 itself does
at `:1679`; `slice_fn review_state` is the sliced arms' one precondition. Each arm is then its
own `same` or `hit` line, and a `same` or `hit` prints only on FAIL, so a silent line is the
observation.

### Inventory

| Identifier | Kind | Cell | Note |
|---|---|---|---|
| `REVIEW_ROUNDS` | conf key | none graded | joins `GATE_BOUND`'s preset, table row and example |
| `BOUNDED` | review state token | none | joins the closed set in every carrier section 3 lists |
| `bound` | local in `verb_review` | none | shell locals are not graded |

No new function or verb, so the lexicon and check 26 populations are unchanged.

### Files touched (estimate)

- the driver and its suite: `tools/unattended/unattended.sh` — the preset and the key's call,
  `review_state`, `verb_review`, the `diff-reviewed` term, and the two comment blocks at `:457`
  to `:458` and `:3966` to `:3969`; `tools/unattended/unattended.test.sh` — `mkconf`'s seventh
  positional, the new arms, the `NOCONF` hit, the two floors
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
- **Default `--disposition` to `promote` in the driver at every terminal exit.** Rev-1 took this,
  because a default fixes the harness and every hand-run alike where a prompt edit fixes one
  caller. It reverses the 2026-09-01 owner ruling without a fork (section 8), and check 2's
  clause 3 would then read a driver-written constant, which is the false evidence that ruling
  named. The recorder is the one caller that reaches the refusal unattended, and it holds the
  count the rule decides on; so the prompt is fixed and the driver keeps refusing.
- **Have the recorder pass `--disposition promote` on every call.** Refused on every non-terminal
  round by the `*)` case at `:4110`, and the recorder cannot tell a terminal round from the count
  it holds; hence the two-step form, refusal first, then the flag.
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
- testing — section 6: the sliced arms, the verb arms and the conf arms it lists, each run alone
  by the form section 4's suite paragraph gives; one check-2 fixture pair; one harness loop
  member; and the parent-commit byte delta. The suites whole and every leg are the close's.
- migration — N/A. Landed run-state records carry no `BOUNDED` row and nothing rewrites them; a
  record written by the new driver parses under the old check 2 as a round with no exit token,
  which is why the two ship in one commit.
- user docs — the Skill, VERBS and protocol renders are the user docs and are S7.

## 6. Acceptance criteria

The driver suite `tools/unattended/unattended.test.sh` and the leg suite
`tools/unattended/check-unattended.test.sh` are on no bar leg, by the 2026-08-23 ruling their
`kit.toml` records, and `TOOL-aHoistedPass-38` records the leg suite red in both shards for causes
that predate this build. So no criterion below reads a suite's exit status; each reads the arm's
own line. The pass observes each criterion by the grep or the single arm it names, run by the
form section 4's suite paragraph gives; every leg and every suite whole is the close's, and a
ledger row for that half reads `observed at --close`, per the build README's rules.

- **AC1** — When `bash tools/unattended/unattended.sh --status <slug>` runs in a fixture tree whose
  conf declares no `REVIEW_ROUNDS`, its stderr carries `REVIEW_ROUNDS` and `so a spec-audit
  subject exits BOUNDED after the kit default of 1 round` on one line.
  Red when: the default is silent, or the key is read before the conf is sourced so a declared
  value is overwritten by the default.
  fixture: the reader is `read_bound_key`, landed by `TOOL-aProbedUnit-3` ahead of this pass; the
  words around the NOTE clause are that reader's, and this criterion asserts only the clause this
  unit passes.
- **AC2** — When the same verb runs with `REVIEW_ROUNDS="9"` declared, the driver exits 2 and its
  stderr carries `above the runaway ceiling of 8`; with `REVIEW_ROUNDS="0"` it exits 2 and its
  stderr carries `REFUSING - REVIEW_ROUNDS` and `not a positive integer` on one line.
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
  prints `--review exits BOUNDED and requires --disposition` and the fixture's run-state file
  holds no `review · item B1` row, the suite's own "a refused round wrote nothing" shape; the
  same command with
  `--disposition promote` prints `BOUNDED · disposition promote` and the run-state file gains
  one row whose reason is `verdict BLOCKED · blockers 3 · BOUNDED · disposition promote`; a
  further round on `B1` is refused with the existing terminal-round message.
  Red when: the base driver is used, which prints `CONVERGING` for the first command and refuses
  the second as `not a terminal exit`; or the requirement was dropped, so the first command
  writes a row with no disposition, which check 2 refuses.
- **AC5** — When the same fixture records `--review tRun --subject tRun --verdict BLOCKED
  --blockers 3`, the verb prints `CONVERGING`, because the slug subject's bound is the ceiling;
  with `--disposition promote` appended it is refused with `not a terminal exit`.
  Red when: the bound is applied to every subject and the closing diff review ends at round 1,
  or the non-terminal refusal went.
- **AC6** — When the AC4 fixture records `--review tRun --subject B2 --verdict BLOCKED --blockers 3
  --disposition fold`, the verb prints `BOUNDED · disposition fold` and the row carries it.
  Red when: `fold` is refused at a `BOUNDED` exit, which would be the forced value the
  2026-09-01 ruling refused, spelled as a refusal instead of a default.
- **AC7** — When `grep -n 'CONVERGED\*|\*NON-CONVERGENT\*|\*CEILING\*|\*BOUNDED\*' tools/unattended/unattended.sh`
  runs at the landed tip, it prints one line inside the `diff-reviewed` term, and the comment
  block above it says the token is unreachable there; and
  `grep -c 'moves the stall earlier' tools/unattended/unattended.sh` prints `0`, where at base
  it prints `1`, at `:3968`.
  Red when: the case was left at three tokens, or it was widened without saying why a fourth
  token that cannot occur is listed; or the driver's own comment prose still says a round cap
  moves the stall earlier above a predicate that now exits `BOUNDED` on one, which no parity leg
  can see because none reads a comment.
- **AC8** — When `bash tools/unattended/check-unattended.sh` is run by hand as one arm of the
  leg suite, over a fixture record under a graded `DISPOSITION_CUTOFF` whose only review row is
  `blockers 2 · BOUNDED` with no disposition, it prints the `record NO disposition` refusal for
  check 2; the same row with
  `· disposition promote` and one new unit id in the README's units region prints no `check 2`
  line. At base the first fixture prints nothing, which is the red-first observation. The `term`
  membership is observed by `grep -c 'CONVERGED|NON-CONVERGENT|CEILING|BOUNDED'` over the leg
  printing 1, and the spec states why no driver-written record can discriminate it.
  Red when: `needs` was left at two tokens, so a bounded promote owes nothing and the exit is
  green-by-absence.
  fixture: the leg suite's `mkdisp` and `dispconf` helpers at `tools/unattended/check-unattended.test.sh:826`
  to `:851` are the shape; `DISPOSITION_CUTOFF` is the one key the fixture conf arms.
- **AC9** — When `grep -c "'BOUNDED'" tools/workflows/unattended-build.template.js` and the same
  over the render run at the landed tip, each prints 1; `grep -c -- '--disposition promote'`
  over both prints 1 each, where at base it prints 0; and the harness suite's terminal loop
  member, run alone with the test double returning `BOUNDED` and zero blockers by the preamble
  form spec 7 AC1 gives, prints `BOUNDED: hands out a roster`. The `workflow script syntax` and
  `review-protocol parity` legs over the pair are observed at `--close`.
  Red when: the token is in one of template and render only, which the parity leg reds; or the
  double's `BOUNDED` falls into the "not one of" throw; or the recorder prompt still runs the
  verb once and returns stderr at a terminal exit.
- **AC10** — When `grep -c 'REVIEW_ROUNDS'` runs at the landed tip over
  `tools/unattended/PROTOCOL.template.md`, `tools/unattended/kit.toml`, `.unattended.conf` and
  `tools/unattended/.unattended.conf.example`, it prints 1 or more for each;
  `grep -c 'BOUNDED' tools/unattended/VERBS.template.md` prints 1 or more, where
  at base it prints 0; `grep -c 'declared round bound' tools/unattended/SKILL.template.md` prints
  1, where at base it prints 0; and `grep -c 'one of four states' tools/unattended/SKILL.template.md`
  prints 0, where at base it prints 1. The `unattended skill wiring` leg, which is
  `bash tools/unattended/adopt-unattended.sh --check`, and check 22 of the `unattended kit gate`
  leg are observed at `--close`.
  Red when: a render is stale; or a carrier is missing the key, which check 22 reports as
  undocumented, documented-but-in-no-example, or set-by-this-project-and-undocumented; or the
  Skill still describes four states, which `grep -c 'BOUNDED'` alone cannot see because the file
  carries that word once at base, at `:694`, about the bar.
- **AC11** — When `wc -c memory/guides/BUILD-METHOD.md` runs at this pass's commit and again
  over the same path as `git show` reads it from the pass's parent commit, the first prints
  exactly 13 less than the second, and `grep -c 'exits BOUNDED' tools/memory-tree/BUILD-METHOD.template.md`
  and the same over the render each print 1, where at base each prints 0. The `build-method size`,
  `kit/dogfood doc parity` and `kickoff-manifest ratchet` legs are observed at `--close`.
  Red when: the swap added bytes or moved more than the one sentence; or the render was not
  re-made; or the manifest's `last-audit` was not re-stamped for a watched file, which the
  ratchet leg names at the close.
  figure: the 287-to-274 sentence delta in section 4 is PINNED from a 2026-09-14 measurement at
  base `1b000d1a`; the parent-commit figure is DERIVED at observation, because unit 1 edits the
  same file ahead of this pass and its delta is its own.
- **AC12** — When each arm section 4's suite paragraph adds is run alone by the form that
  paragraph gives — the preamble sourced, `slice_fn`'s definition sourced from `:3930`,
  `bcsetup`, `slice_fn review_state`, then the arm's own `same` or `hit` line — every line is
  silent against the landed driver, and against the driver at base every verb arm whose
  expectation carries `BOUNDED` or the new NOTE or refusal text prints `FAIL`, the sliced
  `BOUNDED` arms print `FAIL` with `CONVERGING` in the got-column, and the existing two-argument
  sliced arms at `tools/unattended/unattended.test.sh:4546` to `:4557` stay silent against both.
  Three verb arms hold against BOTH drivers by construction and are not reds at base: AC5's two
  slug-subject arms, because the closing review is unchanged in behaviour and that is what they
  assert; and the further-round refusal on the bounded subject, because the base driver reaches
  the same terminal refusal through a `NON-CONVERGENT` second round. The four sliced order arms
  (`NON-CONVERGENT`, `CONVERGED`, `CEILING`, and the ceiling-equal `CONVERGING`) are order
  controls and hold against both by the same token. `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` at HEAD each stand exactly
  this pass's added assertion count above the values the pass's PARENT commit carries, read with
  `git show 'HEAD~1:tools/unattended/unattended.test.sh' | grep '^FLOOR_'`, which prints four
  lines: the pins are the LAST `FLOOR_ASSERTIONS` — the first, at `:5403`, is annotated
  `SHADOWED` and a bump there does nothing — and `FLOOR_SHARD_2`.
  Red when: an added arm reads `CONVERGING` where `BOUNDED` is expected; or an existing
  sequence arm moved because `mkconf`'s default bound is not the ceiling; or a floor did not
  move; or a floor was set to the build base plus this pass's count, which LOWERS a shrink-only
  floor below the value unit 3 landed and hides a stranded block again, the failure the pin's
  own header at `:5422` exists to catch.
  figure: the added assertion count is DERIVED as the number of `hit`, `same` and `miss` lines
  this pass's diff adds to the suite, which is the count each such line adds to `n`; the
  parent-commit floors are DERIVED at observation, on AC11's pattern, because
  `TOOL-aProbedUnit-3`, order 3, raises both constants by its own arms before this pass opens
  and its AC9 says so. The 706 at `:5434` and 510 at `:5461` are base-of-build figures PINNED
  from a 2026-09-14 measurement at `1b000d1a`; spec 3 moves them first and they are never the
  oracle here. Whether the pinned `FLOOR_ASSERTIONS` is met by the executed count is the
  close's: `bash tools/unattended/run-unattended-gates.sh` runs the suite UNSHARDED on a frozen
  clone and a `FAIL executed` line there is the red. NO scheduled run grades `FLOOR_SHARD_2`,
  because that compensating run is unsharded by its own help text; the pin rises so a future
  `--shard 2/2` run is not under-pinned, and this line is the skip announcing itself.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `kit/dogfood doc parity` · `build-method size` · `kickoff-manifest ratchet` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

These are the legs `--close` runs, not what the pass runs: the pass verifies with the grep or
the single arm each criterion in section 6 names and nothing else, and the leg half of AC9, AC10
and AC11 is ledgered `observed at --close`. From `tools/gate-legs.json` at base:
`unattended kit gate` is chunk `declarations`, unguarded, and carries check 2 and check 22;
`unattended skill wiring` is chunk `wiring`, unguarded, and is AC10's render check; `harness arms`
is chunk `declarations`, unguarded, and holds because no branch leaves and none arrives;
`review-protocol parity` is chunk `declarations`, unguarded, and byte-compares the harness
template against its render; `workflow script syntax` is chunk `wiring`; `kit/dogfood doc parity`
is chunk `declarations`, guarded on the method render among others, and compares
`BUILD-METHOD.template.md` with `memory/guides/BUILD-METHOD.md`; `build-method size` is chunk
`product`, unguarded, and is the cap AC11 leaves to it; `kickoff-manifest ratchet` is chunk
`records`, unguarded, and is what reds a moved `memory/guides/BUILD-METHOD.md` or
`.unattended.conf` — both on the manifest's watch line, both edited here — without the
same-commit `last-audit` re-stamp. `memory hygiene` and `spec tokens` grade this file. The three
self-test suites section 6 names are on no leg and are the close's compensating run.

New arm: `tools/unattended/unattended.test.sh` · the verb arms whose expectation carries `BOUNDED`
against the driver at base, which prints `CONVERGING` where `BOUNDED` is expected and refuses the
explicit disposition as non-terminal; AC5's slug-subject arms hold against both by design (AC12) ·
`FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the arms' executed assertions.
New arm: `tools/unattended/check-unattended.test.sh` · the `BOUNDED`-without-disposition fixture
against the leg at base, which prints nothing · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by two.
New arm: `tools/workflows/unattended-build.test.sh` · the loop member `BOUNDED` against the render
at base, which throws on an unknown token · none.

## 8. Open questions

- **F1 — may the driver write a disposition the run did not state?** Rev-1 defaulted
  `--disposition` to `promote` at every terminal exit and deleted the `fail 37` that required
  it, calling that a consequence of the severity rule rather than a choice. The round-1 audit's
  cluster E found it reverses a recorded owner ruling: `memory/builds/dFoldedVerdict/README.md`,
  build-level rules, 2026-09-01 — "a forced value is a constant, and a constant is not evidence
  for the clause that reads it — so the field stays evidence at every exit" — with the same
  reasoning in `TOOL-dFoldedVerdict-1` section 4. Option A, raise it as a fork for the owner
  with that ruling quoted, and park. Option B, keep the flag REQUIRED at every terminal exit and
  fix the one caller that reaches the refusal unattended: the harness recorder runs the verb
  once, and on a refusal naming `--disposition` runs it again with `--disposition promote`,
  because every exit that refusal is reached from stands with blockers and the owner's severity
  rule promotes every blocker. RESOLVED (agent, 2026-09-14, delegated): B. The 2026-09-14 owner
  turn covers severity and the round count, not the field's optionality, so the 2026-09-01
  ruling stands and B needs no owner; the value the recorder passes is the CALLER's, read from
  the count it holds, which is what that ruling asks of the field. Veto 2 is not tripped: the
  driver's surface narrows back to what it is at base.
- **F2 — the bound reader, delegated here by spec 3.** Spec 3 named `UNIT_STALL_BOUND` as
  instance two of the `GATE_BOUND` conf-read shape and handed the instance-two extraction call
  to this unit; rev-1 wrote a third inline copy and took no call. RESOLVED (agent, 2026-09-14,
  delegated): extract. Spec 3's fold of the same audit hoists `read_bound_key <NAME> <DEFAULT>
  <UNIT> <NOTE>` and routes its own key and `GATE_BOUND` through it; this unit's key is a third CALL.
  Legal without a floor move because the block is `echo` and `exit 2` with no `fail N` branch,
  so `harness arms` sees nothing leave or arrive. The one arm the others lack, the ceiling
  comparison, stays one line after the call rather than a parameter of the reader, because a
  parameter one of three callers uses is the reader growing a case for one key.

Two choices were made without a fork and each is a consequence rather than a preference: the
bound is a conf key because the owner named it and the ceiling's own header rejects only an
environment override; and `review_state`'s third argument defaults to the ceiling because any
other default changes a two-argument call, and the one caller always passes it.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft.
- rev-2 · 2026-09-14 · folded the round-1 spec audit: clusters B (ids 21, 8 — AC12 per-arm, AC9 to AC11 leg halves at `--close`), D (id 18 — AC11 against the parent commit), E (id 48 — `--disposition` stays required, the recorder retries with `promote`, F1), F (ids 23, 51 — `read_bound_key`, F2), H (id 7 — AC10's Skill oracles), O (id 31 — the ratchet leg), P (id 33 — the backlog flip is the close's).
- rev-3 · 2026-09-14 · §3 · §4 · §8 F2 · the helper signature aligned to spec 3's four positionals, `read_bound_key <NAME> <DEFAULT> <UNIT> <NOTE>` — the `<UNIT>` word is what makes the refusal sentence true for a key that counts rounds rather than seconds; the `<NOTE>` no longer repeats the "Declare one" clause the helper prints itself (sub-spec interface agreement, M2).
- rev-5 · 2026-09-14 · AC12 · the base-red clause narrowed from "every verb arm" to the arms whose expectation moved: measured at the pass, 12 of the 19 added arms red against a frozen copy of the base kit and 7 hold against both — AC5's two slug-subject arms and the further-round refusal by design, the four sliced order arms as controls — so "every verb arm prints FAIL" was a sentence the spec's own AC5 contradicted (build pass, TOOL-aProbedUnit-6).
- rev-6 · 2026-09-14 · S1 S3 S9 · §4 (the reader block, the state gate, the echo) · §The suite · folded the closing diff review round 1: cluster C (ids 20, 4 — the state gate refuses `fold` at `NON-CONVERGENT|CEILING|BOUNDED` with its own `fail 37` naming the severity rule, the requires-disposition sentence names `promote`, `CONVERGED` accepts an optional disposition written into the row; `review_exit_note`'s header and fold sentence say where fold is reachable; id 12 — check 2 counts `CONVERGED · disposition promote` into `nneed` and reds `fold` beside a non-zero blocker count), cluster G driver half (id 8 — the BOUNDED echo says every CONFIRMED finding is DISPOSED BY SEVERITY), cluster H (ids 7, 16 — `-lt`, `mkconf`'s seventh default 7, an arm refusing `REVIEW_ROUNDS=8` at exit 2), cluster I (id 23 — `REVIEW_ROUNDS_DEFAULT=1` beside the other two constants and interpolated into the NOTE; the NOTE arm reads the constant out of the driver and a `grep -cE '^read_bound_key [A-Z_]+ [0-9]'` arm pins literal-digit defaults at 0). The B2/D2 fold-at-exit arms and the `F1 (fork)` fixture re-targeted at the refusal; every new arm observed red against a frozen copy of the base kit and green at the tip, one block at a time with the preamble sourced. Floors: driver suite +17 of the fold's +19, leg suite +4.
- rev-4 · 2026-09-14 · §3 · §4 · S9 · AC7 · AC12 · §10 · folded the round-2 spec audit: clusters A (ids 1, 10 — AC12's floors measured against the pass's parent commit on AC11's pattern, 706 and 510 kept as base-of-build figures spec 3 moves first), F (id 27 — the run-alone form sources `slice_fn` from `:3930`, which the preamble does not define), H (id 33 — the `WHY A PREDICATE AND NOT A COUNT` block at `:3966` to `:3969` and the `RUNAWAY_CEILING` header at `:457` to `:458` join the verb edits and Files touched; AC7's `moves the stall earlier` grep, 0 at the tip and 1 at base), K (id 15 — `mkconf`'s SEVENTH positional, `REVIEW_ROUNDS="${7-8}"`, unit 3 holding the sixth); and cluster G's correction (id 28, spec 7's) that the `:4634` arm stands in this pass and moves in unit 7's, where rev-3 said it stands unchanged.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "bound the number of review rounds a spec-audit subject may take before the loop exits"`,
run 2026-09-14 at this worktree, reported `scan coverage: 71 files scanned | 0 parse skips |
unscanned layers: .sh` and ranked `boundedParallel`, `run_bounded` and the `.unattended.conf`
affordance seam; every file this unit's mechanism lives in is `.sh`, so the map probe is blind to
the subject and the seam was found by reading the source. It exists: `review_state` at
`tools/unattended/unattended.sh:3974` is the predicate and takes the bound as one more argument;
`verb_review` at `:4030` already holds `subj` and `slug` and makes the equality the bound keys on;
the `GATE_BOUND` block at `:305` to `:312` is the conf-read shape, which `TOOL-aProbedUnit-3`
hoists into `read_bound_key` ahead of this unit and this key calls rather than copies; check
2's awk at `tools/unattended/check-unattended.sh:512` to `:513` is the reader whose two regexes
gain a token. The recall query returned `TOOL-dCarriedReceipt-1`, which records that
`review_state` reads only the rows a run can see; `TOOL-dHonouredPark-8`, which records why a spec
audit and the closing review must not share a subject; `TOOL-aBoundedVerdict-1`'s convergence
predicate, the origin of the four states; `TOOL-dFoldedVerdict-1`'s build record, which pins the
refusal this unit KEEPS and whose 2026-09-01 owner ruling section 8 F1 cites as the reason no
driver default is written; `TOOL-aProvenReuse-3`, the open row that asked what a promoted spec
blocker is; and `TOOL-aLeakedHandle-6`, the ruling that a converged subject is disposed and never
re-rounded, which the terminal grep's `BOUNDED` member extends and whose check-37 sentence unit 7
rewrites to the severity rule. Where a hit was stale:
`TOOL-aBoundedVerdict-1` says a first round always re-arms when blockers are above zero, and the
Skill's opening paragraph says a round cap only moves the stall earlier; both are superseded by
the 2026-09-14 ruling for SPEC subjects, and the Skill paragraph is rewritten so the two answers
agree. The driver carries the same sentence twice in comment prose, at
`tools/unattended/unattended.sh:3968` and, as "not by a count", at `:457` to `:458`; section 4
rewrites both, because a comment is the one carrier no parity leg reads.

Recall terms used: `review round convergence CONVERGING NON-CONVERGENT disposition fold promote blockers ceiling spec-audit tier2 bound one round`

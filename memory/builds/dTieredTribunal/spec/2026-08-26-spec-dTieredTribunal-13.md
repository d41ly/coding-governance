# TOOL-dTieredTribunal-13 — the marked-derivation branch requires every reference bounded

**Status:** SPECCED · rev-2 · 2026-08-26 · node a · Tier-2 · base cd971285 · order 2 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js:200` accepts a `gov:fixed-verifiers`-marked assignment as soon as ONE
non-self identifier anywhere in its right-hand side is already known bounded. A ternary whose other
arm is caller-supplied therefore passes unread, and an args-supplied array of any length reaches
`agent()` once per element under a marker whose shape was never checked against it. That is the same
defeat the `<expr> || <int>` binder was deleted for, one branch over: a caller-settable value wearing
a constant's clothes. Require every value branch of a marked line to qualify on its own. The owner
authorized this unit and sequenced it AHEAD of the ref-keyed-join port into the same file
(`TOOL-dTieredTribunal-8`), so that port is not built on an open hole.

Two things this spec establishes by measurement rather than by reading the research record. The hole
reproduces at the pinned base, and so does a second instance of it in the sibling branch the research
did not name — a marked ternary whose FIRST arm is a bounded split and whose second is caller-supplied
also passes. One predicate closes both, and section 4 carries the run.

## 2. Scope (IN)

- **S1** — the marked branch judges EVERY top-level value branch of the assignment, not the first one
  that happens to match. `tools/hooks/agent-cap.js:181-202` is replaced as one block: the
  `chunk`/`splitInto` accept at `:184-187` and the derivation accept at `:196-200` become one
  per-branch qualifier applied to each branch, and the marked assignment is admitted only when every
  branch qualifies. Today those two are sequential accepts, either of which can return on a single
  arm.
- **S2** — a new helper splits an expression into its top-level value branches. It is named
  `parseBranches`, which `python tools/lexicon/lexicon.py --suggest parseBranches` accepts against the
  declared verb table. It is depth-aware over `()`, `[]` and `{}`, skips `?.` and `??`, recurses into
  nested ternaries, drops a ternary CONDITION because a condition is not a value, and returns a single
  null branch for a `?` whose `:` it cannot find. A null branch never qualifies, which keeps an
  expression this walk cannot delimit on the deny side.
- **S3** — the qualifying forms are a CLOSED list, and each is judged on the branch text alone:
  a bounded split (`chunk(<x>, Math.ceil(<x>.length / <K>))` or `splitInto(<x>, <K>)` whose `<K>`
  resolves through `boundedK`); an array LITERAL whose top-level element count is at or under
  `MAX_LENSES`, counted with the existing `topLevelArgs` splitter so a trailing comma is not an
  element; or a bare identifier already in `ok`, alone or followed by a `.filter(` or `.slice(` chain
  that cannot grow it. The whole-RHS `grows` test at `:197` is kept and still vetoes the assignment.
- **S4** — a marked assignment that FAILS records why, keyed by the name it binds, and the fan-out
  deny at `:313` prefers that reason over the generic one. Today the refusal a caller sees is
  `agent() fanned over LENSES, which this file does not show to be bounded`, emitted at the fan-out
  line while the author is looking at a marked assignment two lines above. The replacement names the
  marker and the branch that did not qualify. This is the convention `why()` at `:458-467` already
  applies to every unresolvable `K` — one explanation per refusal, naming the FORM, because an
  operator who cannot tell which spelling was refused fixes it by guessing.
- **S5** — `tools/hooks/agent-cap.test.sh` gains four arms, three DENY and one ALLOW, and each DENY
  arm is the failing case observed before the predicate is trusted. They are the caller-supplied
  ternary arm, the caller-rooted `.filter` whose predicate merely mentions a bounded name, the
  bounded-split ternary whose other arm is caller-supplied, and the two-sibling-literal ternary that
  must keep passing. The existing arm at `:195-198` covers the shipped derivation and stays byte
  identical.
- **S6** — `.claude/hooks/agent-cap.js` is updated in the SAME commit. It is the copy
  `.claude/settings.json` actually invokes for the `Workflow|Agent` matcher, so a fix landing only in
  `tools/hooks/agent-cap.js` is inert in this repo. Nothing on a default bar catches that: the only
  check comparing the two is the parity arm inside `agent-cap.test.sh`, whose leg carries
  `subject: kit` and is held unless `GATE_SELFTESTS=1`.
- **S7** — the hooks kit version moves from `1.6` to `1.7` at all FOUR carriers, which is more than
  the gate binds. They are the constant and its same-line `gov:kit agent-cap@1.6` marker at
  `tools/hooks/agent-cap.js:52`, the same pair in the wired copy, and the sibling marker at
  `tools/hooks/scratch-guard.js:41` with its own wired copy, which names the hooks kit entry rather
  than its own version. `tools/check-kit-versions.sh:46-49` reconciles the pair in
  `tools/hooks/agent-cap.js` and nothing else, so three of the four sites are moved by reading. The
  bump is owed because `tools/hooks/kit.toml` takes the entry's `version_from` from that constant, and
  an adopter holding 1.6 cannot otherwise tell that the grammar their scripts must satisfy has moved.
- **S8** — the grammar gains its third receiver in prose at `tools/hooks/README.md:24-26`, which
  gains a bullet. The derivation branch has been undocumented since it shipped, which the 2026-08-08
  review recorded as part of the same finding. The parallel bullet in
  `memory/guides/REVIEW-PROTOCOL.md` is a governance carrier this run holds no grant to edit, and it
  is fork F3 in section 8 rather than scope. The new bullet states no bound as a digit beside a noun,
  because `tools/check-agent-cap-restatement.sh` scans that README and it is not under a frozen
  prefix.
- **S9** — `memory/map/features/agent-cap.md` has its prose refreshed in the same commit as the code.
  Its paragraph on the retired `<expr> || <int>` binder is where this belongs: the two are one class,
  and the dossier currently describes the marked receivers without naming the derivation branch at
  all. Its Gaps section at `:132` gains and loses no bullet, because this unit closes rather than
  discloses.

## 3. Non-goals (OUT)

- **The ref-keyed-join port into this same file.** It is authorized by `TOOL-dTieredTribunal-8` and
  is a later unit of this build. The whole point of the owner's sequencing is that it does not land
  on top of the hole this unit closes.
- **`TOOL-aCandidStub-1`, the empty-literal bypass.** The hook blesses an identifier bound from an
  empty array literal and never re-examines it, so a later `push` grows it past hook and gate alike.
  That is the array-LITERAL branch and a re-examination question, not the marked branch and not a
  per-branch question. The row stays OPEN and this unit neither closes it nor makes it worse: an
  empty literal is admitted as a qualifying branch here exactly as it is admitted today, which is
  what keeps `tools/workflows/drift-audit-code.js:285` passing.
- **`TOOL-aNumeralWarden-2`, the enclosing-opener walk.** Two nested wrappers or enough distance
  between the `.map` and the `agent(` call defeat it. That is the fan-out detector, a different
  mechanism, and this unit changes nothing about which calls it looks at.
- **`TOOL-dFramedEntrypoint-1`, the two documents that read as an exemption from the raw-primitive
  ban.** This unit edits one of those two documents and must not fold that row's fix into the same
  bullet. The row is about the array-literal allowance being described as if it exempted a raw
  primitive; a fold would smuggle a second correction past the round that prices it.
- **A new gate leg.** The hook's own self-test already rides the bar as `agent-cap self-test`, and
  the failing cases this unit owes are arms in it. Nothing here needs a leg that does not exist.
- **The doc-completeness gate arm the 2026-08-08 review proposed** — every branch in `scan` that can
  add to `ok` must be named in the protocol. It is a real mechanism and it is a fork in section 8,
  not scope.
- **Rules 1, 3 and 4 of the hook.** The raw-primitive ban, the three places a bound is written, and
  the direct-`Agent` slot budget are untouched. `CAP`, `MAX_VERIFIERS` and `MAX_LENSES` keep their
  values; this unit changes what a marked line must SPELL, never what any number is.

## 4. Design

### Inventory

The marked branch at the pinned base has two sequential accepts and one shared veto. Every row was
read from `tools/hooks/agent-cap.js` at `cd971285`.

| Line | What it does today | After this unit |
|---|---|---|
| `:181` | opens the branch for any line carrying `FIXED_MARK` | unchanged |
| `:182-183` | matches a bounded split anywhere in the line | becomes one qualifying form, judged per branch |
| `:184-187` | accepts and RETURNS on that single match | deleted; no single arm can accept |
| `:188-195` | the comment justifying a non-growing derivation | kept, extended to state the per-branch rule |
| `:196` | takes the right-hand side of the assignment | unchanged |
| `:197` | `grows` vetoes `concat`, `push`, a spread and four more | unchanged, still a whole-RHS veto |
| `:198` | `shrinks` requires a `filter`, a `slice` or a ternary | subsumed by the per-branch qualifier |
| `:199-200` | accepts when SOME non-self identifier is in `ok` | replaced by every-branch qualification |

### The two holes, and the one predicate that closes both

Each row below was run against the hook at the pinned base and against a patched candidate, by
feeding a synthetic `{tool_name:'Workflow', tool_input:{script}}` payload on stdin and reading the
exit code. `rc=0` is ALLOWED and `rc=2` is DENIED.

| Fixture | At base | Tightened |
|---|---|---|
| a marked ternary whose second arm is `args.customLenses` | `rc=0` | `rc=2` |
| a marked `a.lenses.filter((x) => ALL.includes(x))`, bounded name in the predicate only | `rc=0` | `rc=2` |
| a marked `all.length ? chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) : args.batches` | `rc=0` | `rc=2` |
| the shipped `tools/workflows/drift-audit-state.js:224` shape | `rc=0` | `rc=0` |
| a marked ternary between two sibling literals of four elements each | `rc=0` | `rc=0` |

The third row is the finding this spec adds to the research record. The research named the derivation
branch alone, and the `chunk`/`splitInto` branch at `:182-187` has the identical weakness: it matches
its regex anywhere in the line and returns, so a ternary's other arm is never looked at. Fixing only
the branch the research named would have shipped the same defeat one accept above the one being
repaired, in a unit whose whole subject is that one qualifying reference is not enough.

The predicate, stated as the shape a builder implements rather than as final bytes:

```js
// inside the FIXED_MARK branch, replacing both accepts
const rhs = l.slice(l.indexOf('=') + 1)
const grows = /* unchanged whole-RHS veto */
const branches = parseBranches(rhs)          // top-level value branches; condition dropped
const okBranch = (b) =>
     b !== null
  && (   boundedSplit(b)                     // chunk(x, Math.ceil(x.length / K)) | splitInto(x, K)
      || literalAtOrUnder(b, MAX_LENSES)     // counted with topLevelArgs
      || boundedIdentifier(b))               // a name in `ok`, alone or .filter(/.slice( chained
if (!grows && branches.length && branches.every(okBranch)) ok.add(name)
```

`branches.length` is load-bearing and is not decoration. `Array.prototype.every` is TRUE over an
empty array, so a walk that returned nothing would admit the assignment — the vacuous-predicate shape
this repo gates against, inside the guard being hardened.

### The candidate run over the real tree, with near-misses

The charter requires a candidate predicate run over the real tree before it is wired, printing hits
AND near-misses. It was, at the pinned base.

Ten tracked `.js` files exist. Each was fed to the base hook and to the candidate: `HEAD=rc` against
`CAND=rc`, with zero differences. Two of the ten deny under both, and they are the two copies of
`agent-cap.js` itself, which spell a `batches.map((g) => () => agent(…))` fan-out inside their own
remediation TEMPLATE LITERALS and so trip rule 2 at `L796` and `L816` — the file's own declared
fail-closed ceiling, unrelated to this change. Unit 14's alternatives-rejected entry names the same
cause; the block-comment case is rule 1 and a separate gap in the dossier.

The near-misses are the marked lines themselves, because a file with no marked line cannot be moved
by this predicate whatever it contains. Four marked lines ship in this repo's harnesses, and the
tightened predicate must be judged against each rather than against the file count:

| Marked line | Branches | Verdict |
|---|---|---|
| `tools/workflows/tier2-review.js:239` | one, a bounded split | qualifies |
| `tools/workflows/drift-audit-code.js:285` | two, a bounded split and `[]` | both qualify |
| `tools/workflows/drift-audit-state.js:297` | two, the same pair | both qualify |
| `tools/workflows/drift-audit-state.js:224` | two, a `.filter` on `ALL_LENSES` and `ALL_LENSES` | both qualify |

The two `:285` and `:297` rows are why the empty-array-literal form stays a qualifying branch. Making
the literal form stricter here would red two shipped harnesses for a defect neither has, and the
re-examination question those files raise belongs to `TOOL-aCandidStub-1`.

`bash tools/hooks/agent-cap.test.sh` was also run against the candidate. It reported zero failures,
with the two-copy parity arm skipping because the candidate was exercised outside the tree. At the
pinned base the same suite reports zero failures with that arm running.

### Migration

Nothing an adopter passes as `args` changes, and no return shape moves. What changes is which SCRIPTS
the hook admits, and that is the intended break: a script relying on the loose form is denied at the
tool call from the moment the wired copy moves. No such script ships here, and the run above is the
evidence rather than an assertion.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` and `.claude/hooks/agent-cap.js` — the predicate, the helper, the deny
  reason and the version pair. The two files stay byte identical.
- `tools/hooks/agent-cap.test.sh` — the four new arms.
- `tools/hooks/scratch-guard.js` and `.claude/hooks/scratch-guard.js` — the sibling kit marker only.
- `tools/hooks/README.md` — the third receiver.
- `memory/map/features/agent-cap.md` — the dossier prose the code change touches.

No regeneration of `memory/map/generated/` is owed. The dossier's `[claims]` block is untouched
because this unit adds no gate leg, no kit, no workflow script and no new file of any claimed kind,
and the generated artifacts carry claims rather than prose.

### Alternatives rejected

- **Requiring every IDENTIFIER in the right-hand side to be bounded.** This is the literal reading of
  the research proposal and it denies the one shipped user immediately: the right-hand side of
  `drift-audit-state.js:224` mentions `a`, `lenses`, `length`, `filter`, `includes`, `slug` and the
  arrow parameter, none of which is or should be a bounded array. The rule has to be about value
  BRANCHES, not about mentions, and that distinction is the whole design.
- **Leaving the `chunk`/`splitInto` accept alone.** Rejected on the measurement above. Its
  single-arm weakness is the same defect and it is live at the pinned base.
- **A blacklist of caller-rooted spellings, such as banning `args.` on a marked line.** Rejected for
  the reason the file already records for the arity rule: a blacklist bans a spelling and not the
  defect, and the same text is legitimate wherever the value is not the fan-out receiver.
- **Denying at the marked ASSIGNMENT rather than at the fan-out.** Rejected. A marked assignment that
  never reaches an `agent()` call harms nobody, and denying it would red files this hook has no
  business grading. S4 keeps the deny where the fan-out is and moves the EXPLANATION back to the
  assignment, which is the half that was missing.

## 5. Production-readiness checklist

- security — this unit IS the security work. The hook is an enforcement boundary and the defect is a
  caller-supplied value reaching a bounded position; the fix is to stop trusting a claim whose shape
  was never checked against the branch that carried it.
- perf / scale — the branch walk is linear in the length of one assignment line and runs only on
  lines carrying the marker, of which this tree has four. No new file read and no new process.
- a11y — N/A. A hook with no user interface.
- i18n — N/A. Same reason.
- error / empty / loading states — the empty case is the one that matters and it is handled
  explicitly: an empty branch list denies rather than passing vacuously, and a ternary whose `:` is
  not found yields a null branch that never qualifies.
- observability — the deny message. S4 exists because a refusal an author cannot satisfy is the
  failure mode the hooks kit descriptor names for this exact file.
- risks — the real risk is a false REFUSAL of a legitimate script, since the hook denies at a tool
  call and a denied caller is blocked. It is bounded by the sweep in section 4 and by the ALLOW arms
  in S5, and the residual is a shape nobody in this tree writes. The opposite risk, a false pass,
  is what the unit removes.
- testing + left-shift gates — the class is `a guard that accepts on one qualifying reference and
  never examines the rest`, and it is left-shifted into the hook's own self-test across BOTH branches
  rather than into the branch the research named. No `memory/gotchas/` record is owed, because a
  gate covers the class; that is the charter's own order of preference.
- migration / rollback — revert every file named under Files touched together. The
  two `agent-cap.js` copies must never be reverted singly.
- user docs — S8 is the doc work, and `tools/hooks/README.md` is agent-facing. No `help/` page exists
  for a hook and none is owed.

## 6. Acceptance criteria

- **AC1** — When a `Workflow` payload whose script is a `gov:fixed-verifiers`-marked ternary with a
  caller-supplied second arm is piped to `node tools/hooks/agent-cap.js`, it exits 2. At the pinned
  base the identical payload exits 0, which was run rather than assumed.
- **AC2** — When the same is done with a marked `a.lenses.filter((x) => ALL.includes(x))`, whose only
  bounded name appears inside the predicate, `node tools/hooks/agent-cap.js` exits 2.
- **AC3** — When the same is done with a marked
  `all.length ? chunk(all, Math.ceil(all.length / MAX_VERIFIERS)) : args.batches`, it exits 2. This
  is the branch the research did not name, and a build that satisfies AC1 and AC2 while leaving this
  at exit 0 has fixed one of two identical accepts.
- **AC4** — When `bash tools/workflows/check-verifier-fanout.sh` runs with no arguments, it exits 0.
  That leg feeds every committed workflow script to this hook, so it is the observation that
  `tools/workflows/drift-audit-state.js:224` and the three other marked lines still pass.
- **AC5** — When `bash tools/hooks/agent-cap.test.sh` runs, it prints no line beginning `FAIL`, exits
  0, and its trailing count line reports strictly more passing arms than the 64 it reports at the
  pinned base. Four arms are added by S5 and none is removed.
- **AC6** — When the EXACT selector `TOOL-dTieredTribunal-11` ships —
  `const LENSES = kind === 'spec-audit' ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers`, a marked
  ternary between two IDENTIFIERS each bound from a top-level array literal at or under
  `MAX_LENSES` — is piped to `node tools/hooks/agent-cap.js`, it exits 0. The fixture is that shape
  and not two inline literals, because the two are different inputs to the predicate under test and
  only one of them is the shape this build actually ships. A tightening that denied it would break
  the unit it exists to unblock.
- **AC6b** — When `tools/workflows/drift-audit-state.js` is piped to the same hook, it exits 0. That
  file's `ALL_LENSES.filter((L) => a.lenses.includes(L.slug)) // gov:fixed-verifiers` is the ONE
  shipped user of this branch, and a filter over a bounded array can only shrink it. Measured during
  spec authoring: the naive tightening, `refs.some` rewritten to `refs.every`, DENIES both this file
  and AC6's selector, so the naive form is already refuted and §4 must not reach for it.
- **AC7** — When the payload from AC1 is run and stderr is read, the refusal names the
  `gov:fixed-verifiers` marker and the branch that did not qualify. A refusal reading only
  `which this file does not show to be bounded` fails this criterion, because it points at the
  fan-out line while the author's error is on the marked assignment.
- **AC8** — When `diff .claude/hooks/agent-cap.js tools/hooks/agent-cap.js` runs, it reports no
  difference. Without this the wired copy the `Workflow|Agent` matcher actually invokes still carries
  the old predicate and the unit ships inert.
- **AC9** — When `bash tools/check-kit-versions.sh` runs it exits 0, and
  `grep -rn 'agent-cap@1\.6' tools/hooks/ .claude/hooks/` returns no hits. The second half is the one
  that binds: the gate reconciles only the pair inside `tools/hooks/agent-cap.js`, so three of the
  four carriers are observable only by grep.
- **AC11** — When `bash tools/check-agent-cap-restatement.sh` runs after S8, it exits 0. The edited
  `tools/hooks/README.md` is live markdown outside the frozen prefixes, so a new bullet stating a
  bound as a digit beside a noun reds this leg.
- **AC12** — When `memory/map/features/agent-cap.md` is read at HEAD, its prose names the marked
  derivation and the per-branch rule, and `git diff cd971285 -- memory/map/features/agent-cap.md`
  shows no added and no removed line between the `## Gaps` heading and the `## Reuse affordance`
  heading. A dossier that gained a gap describing this hole fails the second half, because the hole
  is closed rather than disclosed.
- **AC13** — When every tracked `.js` file is fed to the rebuilt `tools/hooks/agent-cap.js` and to the
  copy at the pinned base, using `git ls-files '*.js'` for the population, every file returns the same
  exit code from both. This is the charter's run-it-over-the-real-tree rule made observable, and it is
  the criterion that fails if the predicate reds an innocent file.

## 7. Gates

This unit adds no gate leg. Every name below was read from `tools/gate-legs.json` rather than typed
from memory, and the list covers the legs whose subject this unit touches — it is not the run's full
leg set, so a builder reads the manifest for what will execute.

TWO independent things decide whether a leg runs. A `guard` scopes a leg to a diff. A `subject` of
`kit` makes the runner HOLD the leg unless `GATE_SELFTESTS=1`, whatever its guard says. A Definition
of Done for this unit therefore needs the run that sets both `GATE_SELFTESTS=1` and `GATE_FULL=1`,
and that is not optional here: `agent-cap self-test` is the leg that grades this unit's own subject
and it is one of the held ones.

Carrying no guard and `subject: repo`, so they run on every bar and this unit must not red any:
`verifier fan-out`, `review-join ban (no ref-keyed join)`, `agent-cap restatement`,
`kit version markers`, `codebase-map coverage + freshness` and `memory hygiene`.

Armed by this diff and `subject: repo`, so it runs: `lexicon naming predicates`, guarded on `tools/`
and `.claude/` among others, which is why S2 names the helper against the declared verb table.
`review-protocol parity (kit vs dogfood)` is NOT armed — its guard is
`memory/guides/REVIEW-PROTOCOL.md`, `tools/lib/` and `tools/workflows/`, and this unit touches none of
them once the protocol bullet becomes fork F3 — but the `GATE_FULL=1` run this unit's Definition of
Done needs bypasses that guard, so the leg must stay GREEN with neither carrier touched.

Armed by this diff and HELD by `subject: kit`: `agent-cap self-test`, guarded on `tools/hooks/` and
`tools/lib/`, which holds every arm in S5 and the two-copy parity arm S6 depends on; and
`check-wiring self-test`, guarded on `.claude/`, `tools/` and `tools/lib/`, armed only because the
wired copy moves.

## 8. Open questions

- **F1 — should the protocol gain a gate arm asserting that every branch of `scan` which can add to
  `ok` is named in the receiver list?** The 2026-08-08 review proposed exactly this as the left-shift
  for the finding this unit closes, at
  `memory/builds/aDrainedSluice/reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md:308-311`, and
  its ground was that an unnamed allow-path is an unreviewed one — which is what let the derivation
  branch stay undocumented for eighteen days while its shape check was missing. Options seen: build
  it here, on the argument that S8 makes the assertion true today and a gate is what keeps it true;
  or leave it, on the argument that a new gate owes its failing case observed and a predicate over
  `scan`'s branch structure is a mechanism of its own, not a fold. Recommendation: leave it, and let
  whoever takes it mint the row, because this build's own precedent
  (`TOOL-dTieredTribunal-6`) is that a gate arm found during a spec round is a unit rather than a
  fold. This is a fork the owner can close either way without changing anything else in this spec.
- **F2 — does the version bump belong to this unit at all?** `tools/check-kit-versions.sh` asserts
  internal CONSISTENCY only, so a behavioural change carrying NO bump leaves every carrier equal and
  the leg green; only a PARTIAL bump reds. Options seen: bump, on the ground that
  `tools/hooks/kit.toml` takes `version_from` from that constant and an adopter has no other signal
  that the grammar moved; or skip, on the ground that nothing forces it and the sibling markers are
  ungated hand work. Recommendation: bump, as S7 specifies. The precedent is
  `TOOL-aNumeralWarden-1` S10, which moved the same pair for a change to the same file.
- **F3 — should `memory/guides/REVIEW-PROTOCOL.md` gain the third receiver too?** Its predicate lists
  two receivers at `:113-116` and then says `Everything else is denied` at `:118`, which is false
  while the derivation branch goes unnamed — the same defect S8 closes in the kit README. This run
  holds no grant to fix it. That document declares itself BINDING at `:1`,
  `memory/guides/BUILD-METHOD.md:84` makes a change to a governance carrier an owner turn the
  delegation does not reach, and this build's README at `:46` puts `REVIEW-PROTOCOL.md` in scope as a
  PROPOSAL and not as an edit; the first run parked its own headline proposal on that same rule, at
  `RUN.LANDED.3584b586.md:29`. Neither ruling this run holds — `TOOL-dTieredTribunal-7` and
  `TOOL-dTieredTribunal-8` — names either protocol carrier. Options seen: ruled IN, in which case the
  bullet is authored in `tools/workflows/REVIEW-PROTOCOL.template.md` and rendered down, because
  `tools/workflows/check-protocol-parity.test.sh:45` runs `render "$SHIP" > "$LIVE"` while that
  file's `:6` header claims the opposite direction, so a bullet typed into the live guide is
  destroyed by the leg's own printed remedy; or left parked, and the `Everything else is denied`
  sentence stays false until someone with the grant takes it. NO recommendation is offered, because a
  run cannot ratify its own authorization. If it is ruled in, S8 cites the ruling by id the way unit
  12 cites `TOOL-dTieredTribunal-7` at `memory/DECISIONS.md:107`.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft. Every line citation re-derived against `tools/hooks/agent-cap.js`
  and its siblings at the pinned base; the two holes, the shipped-shape allow and the whole-tree sweep
  were run rather than quoted from the research record.
- rev-2 · 2026-08-26 · spec-audit round 1 folded. Findings 23, 31 and 37: S9 and AC12 drop the
  three-gaps count — `memory/map/features/agent-cap.md` holds six Gaps bullets at both the pinned base
  and HEAD — and AC12 becomes a diff observation over the `## Gaps` span. Finding 35: §4's self-denial
  row now names rule 2 over the two copies' own remediation template literals, reproduced at `L796`
  and `L816`, which is what unit 14 already says. Finding 28, the blocker, takes the PARK arm: S8
  keeps only the `tools/hooks/README.md` bullet, the `REVIEW-PROTOCOL.md` and
  `REVIEW-PROTOCOL.template.md` half moves to fork F3 with its veto-2 ground, both carriers leave §4
  Files touched and the Migration trap paragraphs that existed only for them, AC10 is dropped while
  the remaining criteria keep their labels so the audit's citations still resolve, and §7 restates
  `review-protocol parity (kit vs dogfood)` as must-stay-green-untouched. The OWNER arm of 28 is not
  folded and is not this run's to resolve.

## 10. Reuse audit

The seam is `tools/hooks/agent-cap.js` itself, and the two reuse affordances its dossier declares are
the ones this unit extends. `memory/map/features/agent-cap.md:151-160` names
`agent-cap.topLevelArgs` — reuse it whenever source text must be split into positional items and the
count matters, never by re-deriving a comma count — and `agent-cap.boundedK` — reuse it to resolve a
token to an integer bound, extending it by adding a CALL SITE and never a second resolver. S3 does
exactly both: the literal form counts with `topLevelArgs` and the split form resolves through
`boundedK`. The one genuinely new function is the branch walk, and it has no existing seam: the
file's closest relative is `joinCall` at `:414-426`, which joins forward until parens balance and
answers a different question.

The prior art is stronger than a seam. The record is
`memory/builds/aDrainedSluice/reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md:292-311`, which
raised this defect on 2026-08-08 and prescribed the fix: restrict the branch to non-growing member
calls on a bounded receiver, `.filter(`, `.slice(`, or a ternary whose BOTH ARMS are in `ok`. Half of
that landed — the `grows` and `shrinks` tests at `:197-198` close the `.concat` case the review
measured — and the both-arms half did not, which is the residue this unit removes. Its second
left-shift, the doc arm, is F1.

`python tools/codebase-map/reuse_lookup.py "a PreToolUse hook predicate that proves a fan-out receiver
is bounded before an agent call"` returned `boundedK` and `guardAgentSpawn` and `joinCall` from this
file, `boundedParallel` in `tools/workflows/tier2-review.js` as a fan-in seam, and the
`agent-cap.topLevelArgs` affordance. It named no candidate outside the file being edited, which is
the answer: there is no second implementation of this predicate to route through.

`python tools/memory-recall/query.py "why does agent-cap refuse a caller-settable bound wearing a
constant's clothes" --terms "agent-cap marked derivation fixed-verifiers bounded receiver ternary
filter caller-supplied fallback binder lens array literal"` returned 37 hits. The load-bearing ones
are the 2026-08-08 review above, which no probe in the research record surfaced, and
`TOOL-aNumeralWarden-1`, which records the `<expr> || <int>` binder deletion this unit's ground
argument rests on. `TOOL-aCandidStub-1` and `TOOL-dFramedEntrypoint-1` also returned, and section 3
records why neither is closed here.

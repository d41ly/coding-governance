# TOOL-dTieredTribunal-13 — the marked-derivation branch requires every reference bounded

**Status:** CLOSED · rev-7 · 2026-08-26 · node a · Tier-2 · base cd971285 · order 2 · streams tooling · ratified 2026-08-26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-build-TOOL-dTieredTribunal-11-acceptance-ledger.md](../build/2026-08-26-build-TOOL-dTieredTribunal-11-acceptance-ledger.md) | journal | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-14 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-closing-diff-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-closing-diff-round2.md) | diff-review | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-closing-diff.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-closing-diff.md) | diff-review | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-post-acceptance-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-post-acceptance-round1.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |

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
- **S5** — `tools/hooks/agent-cap.test.sh` gains SIX arms, five DENY and one ALLOW, and each DENY
  arm is a failing case that has been SEEN rather than assumed. Three of the five are the holes: the
  caller-supplied ternary arm, the caller-rooted `.filter` whose predicate merely mentions a bounded
  name, and the bounded-split ternary whose other arm is caller-supplied. The other two are the
  guards inside the new predicate, which had no arm at all — a marked line whose right-hand side
  yields NO branch, and a marked ternary whose `:` is not on the line. Those two are what stop the
  tightening from vacuously admitting the exact shapes it was written to deny, and a guard nobody
  has watched fail is an assertion about nothing. The ALLOW is the two-sibling-literal ternary that
  must keep passing. The existing arm at `:195-198` covers the shipped derivation and stays byte
  identical. Section 4 records what each guard arm was measured to do at the pinned base, because
  the two are NOT both red there and an arm that is already green is trusted for a different reason.
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
- **S8** — the `tools/hooks/README.md:24-26` bullet is REWRITTEN, and the third receiver is
  documented in a bullet added after it. The rewrite is not optional and appending alone is refused.
  That bullet today reads that the batching assignment "carries a `gov:fixed-verifiers` marker and
  must spell `chunk(x, Math.ceil(x.length / K))` or `splitInto(x, K)`" — an absolute the derivation
  receiver contradicts and this unit widens further. Appending a third bullet beneath it leaves two
  adjacent sentences in the kit's own grammar document disagreeing about what a marked line may
  spell, with nothing on the bar able to tell an adopter which one is live, and that is the
  append-a-negation-beside-the-text-it-contradicts class recorded at
  `memory/gotchas/fold-text-is-unreviewed-surface.md`. The replacement says that every top-level
  value branch of the marked assignment must qualify on its own, and names the three qualifying
  forms of S3 rather than two spellings. The added bullet documents the marked-derivation receiver,
  undocumented since it shipped, which the 2026-08-08 review recorded as part of the same finding.
  Neither bullet states a bound as a digit beside a noun, because
  `tools/check-agent-cap-restatement.sh` scans this README and it is not under a frozen prefix. The
  array-LITERAL sentence at `:31` stays byte identical: that is `TOOL-dFramedEntrypoint-1`'s
  sentence and section 3 keeps it out of this unit. The parallel bullet in
  `memory/guides/REVIEW-PROTOCOL.md` is a governance carrier this run holds no grant to edit, and it
  is fork F3 in section 8 rather than scope.
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
  ban.** This unit edits one of those two documents and must not fold that row's fix into its own
  edit. The row is about the array-literal allowance being described as if it exempted a raw
  primitive; a fold would smuggle a second correction past the round that prices it. The carrier is
  the standalone sentence at `tools/hooks/README.md:31`, a different sentence from the `:24-26`
  bullet S8 rewrites, and it stays byte identical.
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
this repo gates against, inside the guard being hardened. The null branch is the same argument for
the ternary the walk cannot delimit.

Both guards were RUN at the pinned base, by the same method as the table above, because a guard
whose failing case nobody has watched is an assertion about nothing. The two payloads are the two
new S5 arms and the two new criteria AC14 and AC15.

| Guard fixture | At base | Required after | Reds if the guard is dropped |
|---|---|---|---|
| a marked line whose right-hand side is only the trailing marker comment, the assignment continuing on the next line | `rc=2`, on the generic `agent() fanned over LENSES, which this file does not show to be bounded` | `rc=2`, on S4's marked-branch reason | drop `branches.length &&` and `[].every` is true, so the name is admitted and the arm reads `rc=0` |
| a marked ternary whose `:` sits on the NEXT line | `rc=0` | `rc=2` | return the first arm instead of a null branch and its `.filter` qualifies, so the arm reads `rc=0` |

The first arm is GREEN at base, and it is said plainly rather than left to be misread as a verified
row: its failing case is the guard's ABSENCE, not the base hook, and the half of AC14 that fails
today is the deny REASON, which at base is the generic fan-out line quoted above. The second arm is
red at base and red again against a walk that swallows an unclosed ternary, so it is armed twice.

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
- `tools/hooks/agent-cap.test.sh` — the six new arms.
- `tools/hooks/scratch-guard.js` and `.claude/hooks/scratch-guard.js` — the sibling kit marker only.
- `tools/hooks/README.md` — the rewritten `:24-26` bullet and the third receiver added after it.
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
  not found yields a null branch that never qualifies. Both are S5 arms and both are graded, by AC14
  and AC15, so neither guard ships never having been seen to fail.
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
  pinned base. Six arms are added by S5 and none is removed. The 64 was re-run at fold time:
  `---- 64 passed, 0 failed ----`, rc=0, zero `FAIL` lines.
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
- **AC11** — Three observations over `tools/hooks/README.md`, one absence and two presence. First,
  `bash tools/check-agent-cap-restatement.sh` exits 0 after S8. That README is live markdown outside
  the gate's frozen `memory/(builds|archive|gotchas|backlog)/` prefixes, so a bullet stating a bound
  as a digit beside a noun reds this leg. That half is TRUE at the pinned base and stays true if the
  README is never touched — it is kept as the no-digit-beside-a-noun check it already is, and the
  two halves below are what carries the presence assertion AC10 took with it when the park dropped
  it. Second, `grep -c 'gov:fixed-verifiers' tools/hooks/README.md` returns 2, one higher than the 1
  it returns at `cd971285`, where the single hit is `tools/hooks/README.md:25`; the added hit is the
  new bullet naming the marked-derivation receiver. Third, `grep -c 'must spell'
  tools/hooks/README.md` returns 0, where it returns 1 today at that same `:25` — the `:24-26`
  bullet was rewritten rather than appended beside, and its replacement names the three qualifying
  forms of S3 and the every-branch rule instead of two admissible spellings. The two greps interlock:
  deleting the old bullet outright satisfies the third and reds the second. A build that ships the
  predicate and never touches the README passes the first half and fails the other two, which is the
  point of adding them.
- **AC12b** *(ADDED at rev-6 by the post-acceptance spec audit)* — The array-LITERAL branch is
  graded for its OVERSIZE case, not only its accepted one. When the hook is handed a marked assignment
  whose literal holds more than `MAX_LENSES` elements it DENIES, and the same holds unmarked. Measured
  at this rev against `tools/hooks/agent-cap.js`: a marked literal of 5 returns 0, of 6 returns 2, of
  12 returns 2, and an unmarked literal of 9 returns 2. The arm at `tools/hooks/agent-cap.test.sh:170`
  already pins the marked-oversize case; this criterion is what makes the unit GRADE it. The audit
  filed this as a fail-open re-opening the cap — it is not, the code refuses correctly, and the defect
  was that nothing in this spec said so. A branch whose accepted case is graded and whose refused case
  is not is a criterion that cannot fail.
- **AC12** *(AMENDED at rev-5, round 2 — the second half was written to catch THIS unit disclosing
  its own hole instead of closing it, and it fired instead on a SIBLING unit legitimately adding its
  own gap to the same span)* — When `memory/map/features/agent-cap.md` is read at HEAD, its prose
  names the marked derivation and the per-branch rule, and no line added between the `## Gaps`
  heading and the `## Reuse affordance` heading describes the marked-derivation hole THIS unit
  closes. `TOOL-dTieredTribunal-14`'s join-rule bullet lands in that span and is not this unit's to
  suppress. A dossier that gained a gap describing this unit's own hole still fails, because the
  hole is closed rather than disclosed — which is the property the criterion was always for, and
  span-level byte equality was only ever a proxy for it.
- **AC13** — When every tracked `.js` file is fed to the rebuilt `tools/hooks/agent-cap.js` and to the
  copy at the pinned base, using `git ls-files '*.js'` for the population, every file returns the same
  exit code from both. This is the charter's run-it-over-the-real-tree rule made observable, and it is
  the criterion that fails if the predicate reds an innocent file.
- **AC14** — When a `Workflow` payload whose marked assignment carries nothing after the `=` but the
  `gov:fixed-verifiers` comment, its right-hand side continuing on the NEXT line, is piped to
  `node tools/hooks/agent-cap.js`, it exits 2 AND its stderr names the marker and reports that the
  marked line yielded no qualifying branch. The exit code is already 2 at the pinned base, which was
  run rather than assumed; what fails today is the reason, which reads only
  `agent() fanned over LENSES, which this file does not show to be bounded`. The exit half is not
  decoration either: it is the arm that reds against a candidate with `branches.length &&` removed,
  where `[].every` admits the assignment and the payload exits 0. This is `branches.length`'s
  failing case, seen rather than argued.
- **AC15** — When a `Workflow` payload whose marked ternary has its `:` on the NEXT line — the first
  arm a `.filter` over a bounded literal, the second `args.customLenses` — is piped to
  `node tools/hooks/agent-cap.js`, it exits 2. The identical payload exits 0 at the pinned base,
  which was run rather than assumed. This is S2's null-branch rule made observable: a walk that
  returned the first arm instead of a single null branch admits the line on a `.filter` that
  qualifies, and reds this criterion.

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
  **RESOLVED (agent, 2026-08-26, delegated): leave it, and record it as a follow-up.** A new gate
  arm is a MECHANISM, and folding a mechanism into a unit that is not about it is the shape round 1
  of this build's audit refused when it parked the protocol edit. M8's left-shift obligation is
  discharged for this build by `TOOL-dTieredTribunal-15`'s record, so nothing is left uncovered by
  taking the cheaper arm. Under M3 the option that adds the arm trips no veto but leaves the same
  follow-ups open at strictly higher cost, so it is not the more feature-rich survivor.

- **F2 — does the version bump belong to this unit at all?** `tools/check-kit-versions.sh` asserts
  internal CONSISTENCY only, so a behavioural change carrying NO bump leaves every carrier equal and
  the leg green; only a PARTIAL bump reds. Options seen: bump, on the ground that
  `tools/hooks/kit.toml` takes `version_from` from that constant and an adopter has no other signal
  that the grammar moved; or skip, on the ground that nothing forces it and the sibling markers are
  ungated hand work. Recommendation: bump, as S7 specifies. The precedent is
  `TOOL-aNumeralWarden-1` S10, which moved the same pair for a change to the same file.
  **RESOLVED (agent, 2026-08-26, delegated): bump, exactly as S7 specifies.** `tools/hooks/kit.toml`
  takes its `version_from` from that constant, so the constant IS the kit's version and an adopter
  has no other signal that the grammar moved. The precedent is `TOOL-aNumeralWarden-1` S10, which
  moved the same pair for a change to the same file. The skip arm rests on the gate not forcing it,
  which is true and is not a reason: `check-kit-versions.sh` grades consistency, not movement, and a
  version that never moves is consistent and useless.

- **F3 — RESOLVED (owner, 2026-08-27, `TOOL-dTieredTribunal-25`): ruled IN.** The bullet is authored
  in `tools/workflows/REVIEW-PROTOCOL.template.md` and rendered down with
  `check-protocol-parity.test.sh --render`, which is the direction that file's own `:6` header gets
  backwards; the parity leg is green on the rendered pair. The `Everything else is denied` sentence
  is no longer false. Original question and options below, unedited.
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
- rev-3 · 2026-08-26 · spec-audit round 2 folded — findings 6, 16 and 20, this spec's three. Every
  claim below was made by editing the body first and reading the edited body back, never by writing
  the intent down. Finding 6: AC11 was unfailable after the park. Re-run at fold time,
  `bash tools/check-agent-cap-restatement.sh` exits 0 at the pinned base and stays 0 whether or not
  S8's bullet is ever written, so AC11 now carries two presence halves over the carrier that stayed
  in scope. `grep -c 'gov:fixed-verifiers' tools/hooks/README.md` counts 1 at `cd971285` and 1 at
  HEAD, at `:25` both times, and the criterion requires 2; `grep -c 'must spell'` counts 1 at both
  and the criterion requires 0. Fork F3 stays PARKED — this is bookkeeping the park owes, not an
  unpark, and a run cannot ratify its own authorization. Finding 16: S8 now REWRITES the `:24-26`
  bullet, whose `must spell` absolute contradicts what this unit ships, rather than appending a
  third bullet beside it, §4's Files touched names the rewrite, and §3's `TOOL-dFramedEntrypoint-1`
  non-goal now names `:31` as the sentence that stays byte identical. Finding 20: the two
  vacuous-predicate guards shipped unarmed, since deleting `branches.length &&` left every S5 arm
  and every criterion passing. S5 becomes SIX arms, five DENY and one ALLOW; §4 gains the two guard
  fixtures RUN at the pinned base against the shipped hook — `rc=2` on the generic refusal for the
  empty-branch line, `rc=0` for the ternary whose `:` sits on the next line; §6 gains AC14 and AC15;
  AC5 reads six arms added and its 64 was re-run at fold time as `---- 64 passed, 0 failed ----`;
  §4's Files touched row for the self-test reads six. One thing is stated rather than hidden,
  because a green row misread as a verified one is the whole class: the empty-branch arm is already
  GREEN at base, so AC14's fails-today half is the deny REASON and its exit-code half is what reds
  against a candidate with the guard removed.
- rev-6 · 2026-08-26 · post-acceptance spec audit. AC12b ADDED so the array-LITERAL branch grades its
  OVERSIZE case and not only its accepted one — the code refuses correctly, measured, and nothing in
  this spec said so, which is a criterion that cannot fail. AC12 amended at rev-5 stands. F1's
  follow-up now names `TOOL-dTieredTribunal-23`, because the audit found it promising a record that
  no backlog row carried.
- rev-4 · 2026-08-26 · M3 fork sweep. F1 RESOLVED to leave the gate arm and record it as a follow-up:
  a new arm is a mechanism, and M8's left-shift is already discharged by `TOOL-dTieredTribunal-15`.
  F2 RESOLVED to bump, as S7 specifies, because `tools/hooks/kit.toml` takes `version_from` from that
  constant. F3 stays PARKED for the owner under M3 veto 2 and is untouched. Header gained `ratified`.


- rev-5 · 2026-08-26 · **AC11 REPAIRED and AC12 AMENDED, both disclosed.** The acceptance pass found
  AC11's `gov:fixed-verifiers` count at 1 where the criterion demands 2: the marked-derivation bullet
  this unit added to `tools/hooks/README.md` documented the marker without ever spelling it, which is
  the one thing a bullet about a marker must do. Spelled now, together with the consuming-chain rule
  round 2 added. AC12's second half was a byte-equality proxy over the dossier's `## Gaps` span; it
  fired on `TOOL-dTieredTribunal-14` adding its OWN gap there, which is not this unit's to suppress,
  so the criterion now grades the property it was always for.

- rev-7 · 2026-08-27 · **F3 RESOLVED by the owner, ruled IN — `TOOL-dTieredTribunal-25`.** The unit
  shipped with `memory/guides/REVIEW-PROTOCOL.md` listing two receivers above a sentence reading
  `Everything else is denied`, which the marked derivation this unit tightened had made false. The
  run held no grant to fix it and said so rather than editing a binding carrier under a delegation
  that does not reach one. Authorized now, the bullet was authored in
  `tools/workflows/REVIEW-PROTOCOL.template.md` and rendered down — the direction that file's own
  `:6` header states backwards, and the trap the fork flagged in advance — and the parity leg is
  green on the rendered pair.

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

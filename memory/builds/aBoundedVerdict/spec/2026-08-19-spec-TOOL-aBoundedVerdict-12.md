# TOOL-aBoundedVerdict-12 — a blocked close names its cause, not just the item it blocked on

**Status:** SPECCED · rev-2 · 2026-08-19 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

`--close` refuses with the NAME of the unmet Definition-of-Done item and, in six of eight cases,
nothing else — while the diagnosis it needs has already been computed and thrown away by a redirect
or an unset variable. Make every close-path refusal reach the operator, because an unattended run
that cannot read the cause either stalls or reaches for the one override the kit exists to refuse.

## 2. Scope (IN)

- **S1** — drop the output-discarding redirect from `verb_close`'s `observe_anchor` prologue
  (`:1387`). Its eight named refusals (checks 22-25 and 27-30) are the only statement of why the
  anchor could not be observed, and the item they block — `authorization-reachable` — is the one item
  `fail 21` forbids overriding. Use the `|| true` form `--landed` and `--preflight` already use.
- **S2** — drop the redirect from the `authorization-reachable` arm (`:1457`). A redirection on an
  `&&` list binds only to its last simple command, so it silences `check_authorization`'s six
  refusals while `trusted_base`'s continue to print — the silenced half being exactly the
  operator-repairable one.
- **S3** — `build-complete`'s four surviving terms report which term failed. `DOD_OUT=""` sits above
  an AND chain whose four conjuncts already compute their values in substitutions that are discarded;
  evaluate them sequentially so each sets `DOD_OUT` from the value it already has.
- **S4** — `closing-review-recorded` sets `DOD_OUT` naming which of its four failure modes fired: no
  record, an UNTRACKED record, no matching sha, or no pinned base. The untracked case is the likeliest
  and the least guessable, because the arm reads `--cached`.
- **S5** — the close path's agent-item refusal names the RECORD KEY, not only the item.
  `parked-decisions-surfaced` is read from a line spelled `parked-surfaced:`, so an operator obeying
  the refusal writes a key nothing reads. `--abort` already carries the mapping and the sentence; this
  is that fix at the call site its author did not grep for.
- **S6** — a meta-gate over `dod_met`'s arm bodies, and **rev-2 rewrites its predicate because rev-1's
  was vacuous.** A literal `return 1` appears in exactly TWO arms (`gates-green` at `:1464`/`:1466`
  and `build-complete` at `:1497`) — and those are the two arms that already set `DOD_OUT`. Six arms
  fail by falling off the end of the case arm with a false test, so "no arm reaches a `return 1`
  without setting `DOD_OUT`" is satisfied by every arm today: the
  `fixture-passes-by-finding-nothing` class this very spec warns about, in this very spec. The rule
  is therefore on the arm's FAILING EXIT however it is spelled, and it requires a NON-EMPTY message —
  `gates-green` clears `DOD_OUT` to the empty string on success, so a non-empty test is what
  distinguishes "reported" from "cleared". The `*)` project-item arm at `:1533` is a ninth arm and is
  a THIRD declared exemption alongside the two agent-attested ones, because the kit knows nothing
  about a project item's failure mode.
- **S6a** — the target is stated honestly: S1-S5 give a message to `gates-green`, `build-complete`,
  `closing-review-recorded` and the two agent items. `records-current`, `landed-via-lander` and
  `authorization-reachable` are NOT in this unit's scope — `authorization-reachable`'s cause is
  printed by S2 rather than carried in `DOD_OUT`, and the other two are
  `TOOL-aBoundedVerdict-18`'s. So S6's rule is scoped to the arms this unit gives messages to, and
  rev-1's "0 of 8, plus 2 exemptions" was unreachable inside this unit's own scope.
- **S7** — one progress line before the prologue, so a close that is about to spend a network
  round-trip has printed something first.

## 3. Non-goals (OUT)

- Not the transport bound itself. That `observe_anchor` can block indefinitely is
  `TOOL-aBoundedVerdict-13`; this unit makes the failure legible, that one makes it terminate. They
  are separable and both are needed: an unbounded wait that prints its cause is still a hang.
- Not the ORDERING fix (evaluating `refuse_if_terminal` before the network call). Also
  `TOOL-aBoundedVerdict-13`, which owns everything about when the round-trip happens.
- Not the satisfiability of any item. `build-complete`'s terms keep their semantics exactly;
  `TOOL-aBoundedVerdict-11` owns the region they read, and the closing-review
  join is its own roster unit, unminted until its spec defines it. This unit changes only what a
  failing term SAYS.
- No new DoD item, no new phase, no change to the override grammar or to which items are overridable.
- Not a general logging framework, a verbosity flag, or a structured output mode. The refusals exist;
  they are being un-swallowed.

## 4. Design

### Data model

`DOD_OUT` is the existing single-slot channel: set by a `dod_met` arm, printed indented under the
`fail 13` headline, filtered so the gate bar's roll-call does not bury the one line that matters, then
cleared. Nothing about that contract changes. What changes is that six more arms use it and two
redirects stop erasing what precedes it.

The filter is already `grep -vE '^(GATE (ok|skip) )'` — anything that is not an ok/skip line
survives. So a refusal reaching stdout from `fail` is carried by the existing machinery with no new
plumbing, which is why this unit is deletions and assignments rather than a mechanism.

### Why the redirects are two defects and not one

`:1387` suppresses a whole function's output. `:1457` suppresses one command inside an `&&` list and
therefore silences a SUBSET, which is worse: the failure presents as intermittent, because whether
the operator sees a cause depends on which of two functions refused. The audit reproduced both — a
fixture with a dangling remote HEAD printed only the bare item name as shipped and
`check 28 FAILED — the remote answered but advertised no HEAD symref` with the redirect removed; a
fixture whose pinned BASE predates the build folder printed `check 6 FAILED — no build README at the
pinned BASE` the same way.

`trusted_base`'s own header comment records that it was rebuilt to return through a global
specifically because a captured refusal made `--close` print only the downstream symptom. The very
next call in the chain re-introduced it. That is the whole argument for S6: the fix was made once,
correctly, and did not become a rule.

### Inventory

| Concern | Today | After |
|---|---|---|
| `observe_anchor`'s 8 refusals under `--close` | discarded | printed |
| `check_authorization`'s 6 refusals under `--close` | discarded | printed |
| `trusted_base`'s refusals under `--close` | printed | unchanged |
| `build-complete` failing | one identical sentence for four causes | the failing term names itself |
| `closing-review-recorded` failing | no output at all | the failing mode names itself |
| an unmet agent item | names the item, which is not the key | names the key, as `--abort` does |
| arms that return 1 with no `DOD_OUT` | 6 of 8 | 0, plus 2 declared exemptions |
| a close before its first check | silent | one progress line |

### Migration

None on disk. No record format changes, no conf key moves, and no existing run-state file is read or
written differently. The observable change is stdout, which nothing joins on — with one exception
worth stating: `unattended.test.sh` asserts on `--close`'s output with `hit`, so arms that assert the
ABSENCE of text may newly see the un-swallowed refusals. That is a test-side fix, not a migration.

### Rollout

S1 and S2 are two deletions and land first — they are the largest legibility gain per byte in the
unit. S3, S4 and S5 are independent assignments. S6 lands last, because a meta-gate written before
its subject is clean reds on the very diff that fixes it, and this repo has a recorded instance of
that ordering costing a session.

### Files touched (estimate)

`tools/unattended/unattended.sh` (two redirects deleted, four arms gain assignments, one refusal gains
its key mapping, one progress line) · `tools/unattended/unattended.test.sh` (an arm per new message,
plus S6's source-level assertion and any existing arm that asserted on the swallowed silence) ·
`tools/unattended/check-arms` floor in `.memory-tree.conf` if any new `fail` call site is added —
none is expected, because every message here rides `DOD_OUT` or an existing `fail` · the kit version
constant.

### Alternatives rejected

- **A verbosity flag.** Rejected: the default is the only mode an unattended run gets, and a flag
  makes the silent path the one nobody passes.
- **Print `$GATE_CMD`-style captured output for every arm.** Rejected: `gates-green` needs capture
  because the bar is verbose and the filter exists for it; the other arms have short refusals that
  belong on stdout unmediated. Adding capture where none is needed re-creates the defect.
- **Route the agent-item message through a generic key-mapping table.** Rejected on cost: there are
  exactly two agent items and `--abort` already spells the mapping. A table for two entries is the
  abstraction this repo's own rules refuse.
- **Fix only the blocker (S1) and file the rest.** Rejected because S2 is the defect that makes the
  behaviour look intermittent, and an intermittent diagnosis is worse than a consistently absent one.
- **Make `authorization-reachable` overridable so a wedged run has a forward move.** Refused: an
  override on the authorization check IS the authorization check. The forward move is the printed
  cause, which is this unit.

## 5. Production-readiness checklist

- **security** — un-suppressing `observe_anchor` prints refusal text that names remote refs, URLs and
  the `GOV_DEFAULT_BRANCH` value. None is a secret and all of it is already in the record or the
  config; no credential material is reachable by these code paths. Worth one look during review, not
  a redaction.
- **perf / scale** — N/A. Deletions and string assignments.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — this unit IS the error-state work. The empty case that matters:
  an arm that sets `DOD_OUT` to the empty string must print nothing rather than a blank indent block,
  which the existing `[ -n "${DOD_OUT:-}" ]` guard already handles and S6 must not break.
- **observability** — the whole unit. The measure is that each of the eight `dod_met` arms has a
  distinguishable failure output, which AC7 asserts by count.
- **risks** — low. The one real hazard is an existing test arm that passes BECAUSE output was
  swallowed; S6's source-level assertion is what stops a future redirect re-introducing the class.
  Rollback is reverting the deletions.
- **testing + left-shift gates** — S6 is the left-shift, and it is a source-level assertion rather
  than a behavioural one for the reason `check-arms.py` exists: a behavioural arm proves one path,
  a source rule covers the arms nobody wrote a fixture for.
- **migration / rollback** — none on disk; see Migration.
- **user docs** — none. No document states that a blocked close is silent, so nothing needs
  correcting. The protocol's DoD table describes what each item ASSERTS, not what it prints.

## 6. Acceptance criteria

- **AC1** — When `--close` runs against a fixture whose remote advertises no HEAD symref, its output
  contains `check 28` before the `authorization-reachable` line; against the shipped driver it
  contains only the item name.
- **AC2** — When `--close` runs against a fixture whose pinned BASE predates the build folder, its
  output contains `check 6` and the `<sha>:<path>` it could not resolve.
- **AC3** — When `--close` runs against a fixture failing each of `build-complete`'s four surviving
  terms in turn, the four runs print four DIFFERENT sentences, asserted as four distinct arms in
  `tools/unattended/unattended.test.sh`.
- **AC4** — When `--close` runs against a fixture whose review record exists but is UNTRACKED, the
  output says the record is not in the index and names `git add`.
- **AC5** — When `--close` blocks on `parked-decisions-surfaced`, its message contains
  `parked-surfaced` — the key an operator must actually write.
- **AC6** — When `grep -c 'DOD_OUT=' tools/unattended/unattended.sh` is compared before and after,
  the count rises by at least four, and every arm in S6's scoped population reaches its failing exit
  with a NON-EMPTY `DOD_OUT` — asserted at source level by S6's arm. Rev-2: the arm must red against
  a fixture in which one in-scope arm falls off the end of its case with no assignment, because
  rev-1's predicate was satisfied by the shipped driver and the criterion claiming otherwise was
  false.
- **AC7** — When the eight `dod_met` arms are each driven to failure, eight distinguishable outputs
  result: six naming a cause and two naming an absent attestation and its key.
- **AC8** — When `--close` is invoked, a line is printed before any network call, observed by
  running it against an unreachable remote under `timeout 5` and seeing non-empty stdout.
- **AC9** — When `bash tools/unattended/unattended.test.sh` runs, it prints an executed assertion
  count in the agreed shape and that count is at or above its floor in
  `tools/testsuite-count-waivers.txt` or the floor registry that leg reads.

## 7. Gates

`bash tools/run-gates/run-gates.sh` whole, and specifically: `unattended driver selftest`
(`tools/unattended/unattended.test.sh`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`) + `check-unattended.test.sh` · `harness arms`
(`tools/memory-tree/check-arms.py`) · `testsuite counts`
(`tools/check-testsuite-counts.sh`) · `kit version markers` · `absence-assertion` discipline: S6's
source rule must not be a whole-file grep for a redirect string, or it reds on the comment that
documents its own fix — `memory/gotchas/absence-assertion-over-whole-file-text.md`.

## 8. Open questions

- **F1 — is S6 a new leg, a new check inside the hygiene gate, or an arm in the driver's own test
  suite?** A new leg costs a `gate-legs.json` entry, a `[[gate_leg]]` row in `kit.toml`, a
  codebase-map dossier claim and the map's coverage assert. A hygiene check costs `ARMS_FLOORS` and an
  arm per `fail` call site. An arm inside `unattended.test.sh` costs nothing new and is where the
  subject already lives. **Recommendation: an arm in `unattended.test.sh`.** The rule is about ONE
  file's arm bodies, and the suite that owns that file already runs on the bar.
  RESOLVED (agent, 2026-08-19, delegated): an arm in `unattended.test.sh`. Mechanism-only fork, and
  the alternatives cost gate surface for a rule scoped to a single file.

- **F2 — does S6 assert over `dod_met`'s arm bodies by parsing the `case` block, or by requiring a
  literal `DOD_OUT=` within N lines of each arm label?** Parsing is precise and brittle to
  reformatting; proximity is crude and cannot see an assignment made in a helper. **Recommendation:
  parse the `case` block between its `case`/`esac`, keyed on arm labels, and fail CLOSED if the block
  cannot be located** — a locator that silently finds nothing is
  `memory/gotchas/fixture-passes-by-finding-nothing.md`.

- **F3 — should the progress line in S7 be unconditional, or suppressed when stdout is not a
  terminal?** Unconditional is simpler and adds one line to every close, including the test suite's
  many `hit` assertions. Suppressing on a non-tty makes the tests silent and the humans informed, and
  makes the observable in AC8 untestable without a pty. **Recommendation: unconditional.** AC8 is the
  reason; a progress line an unattended run cannot observe is not a progress line.

## 9. Revision log

- rev-2 · 2026-08-19 · folded the M4 spec audit. **S6's predicate was vacuous and is rewritten.** A
  literal `return 1` appears in only two `dod_met` arms and both already set `DOD_OUT`; the other six
  fail by falling off the end of their case arm, so rev-1's rule was satisfied by every arm on the
  shipped driver and AC6's "fails against the shipped driver" was false. The rule now keys on the
  arm's FAILING EXIT however spelled and requires a NON-EMPTY message, because `gates-green` clears
  the variable on success. S6a is new and states the scope honestly: three arms rev-1's "0 of 8"
  target implied are not in this unit's reach, two of them being another unit's. The `*)` project-item
  arm becomes a third declared exemption. This is the class this spec warns about, found inside this
  spec.
- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's blocker 15·9·28 and highs
  4·10·16, 5, 3 and low 26, consolidated because they are one mechanism — the close path's message
  channel — and the audit's own verdict names them that way. F1 and F2 resolved under the delegated
  fork rule; F3 resolved on AC8's testability.

## 10. Reuse audit

The seam is `DOD_OUT` and its single print site in `verb_close` — the channel
`TOOL-aBranchedMandate-12` built when it stopped discarding `$GATE_CMD`'s output, and
`TOOL-aBranchedMandate-13` extended when it made the roster region report itself by name. Both are
CLOSED and both are cited by the driver's own comments at the sites this unit touches. This unit adds
no channel; it widens the population that uses the existing one, which is why §4 has no Data model
change to describe.

The `fail`-to-stdout convention (`unattended.sh:76`) is the second seam, and it is what makes S1 and
S2 pure deletions: the refusals already write where the operator reads, and only a redirect stood
between them.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict
adversarial diff fold unattended close build-complete DoD stall halt`. No symbol-level seam was
returned for refusal plumbing, which is recorded here as the probe's answer rather than retried with
softer words.

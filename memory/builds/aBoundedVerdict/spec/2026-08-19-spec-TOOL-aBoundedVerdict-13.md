# TOOL-aBoundedVerdict-13 — every remote observation is bounded, and pays its cost last

**Status:** SPECCED · rev-6 · 2026-08-20 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

Nothing in the unattended kit bounds a remote round-trip, and `--close` opens with one — so a
partitioned network turns the close into an indefinite silent wait, and the same calls inside the
gate leg turn a `git push` into a hung push rather than a red one. Bound every remote observation,
and stop paying for one before the free refusals that would have blocked the close anyway.

**The tracked incident is backlog row `TOOL-aBoundedVerdict-10`** (OPEN): the `unattended driver
selftest` leg hung inside its first `--preflight` with zero output and wedged the whole bar. That row
names TWO fixes — a per-leg deadline in `run-gates.sh`, and a timeout on the driver's anchor call —
and **this unit delivers only the second**, so the row does not close when this unit lands (§3).

## 2. Scope (IN)

- **S1** — a single bounded-observation helper in `unattended.sh` wraps every `ls-remote`. Both call
  sites go through it: `observe_anchor`'s HEAD advertisement (`:240`) and `branch_tip_quiet`'s
  per-branch tip (`:298`, reached twice under `ANCHOR_SCOPE="published"` — once from `resolve_base`
  and once from `trusted_base`'s alternate).
- **S1a** — **the helper captures through a FILE, never a command substitution**, and this is the
  difference between a bound and a decoration rather than a style note. `out=$(timeout N cmd)` reads
  until EOF, and EOF arrives only when the last inherited write end closes, so a surviving descendant
  holds the pipe while `timeout` reports 124 on schedule. MEASURED on node `c` before the helper was
  written: `out=$(timeout 1 bash -c 'sleep 6 & exit 0')` returned after **6 s** against a declared
  **1 s** bound, and the same command redirected to a file returned in **0 s**. `timeout -k` follows,
  for the child that ignores SIGTERM. Added at rev-5, from the recall probe this build's own method
  requires before a pass: the gate runner hit the identical defect, its fix landed hours earlier at
  `tools/run-gates/run-gates.sh`, and this helper follows that shape instead of re-deriving it. Had
  the probe not run, this unit would have shipped a wall-clock bound that buys zero seconds — which is
  the exact class it exists to remove, one level up.
- **S1b** — the helper cannot call `GIT()`, because `timeout` needs an external command and `GIT` is a
  shell function. So the dereference pins move into NAMED constants that `GIT()` and the helper both
  expand. Spelling them twice was the alternative and it is the two-answers class: a pin added to one
  copy and not the other is silent, and the whole point of `GIT()` is that no read escapes the pins.
- **S2** — the bound is belt and braces, because no single mechanism covers every transport: an outer
  wall-clock cap, plus `http.lowSpeedLimit`/`http.lowSpeedTime` for the HTTP transports and
  `ssh -o ConnectTimeout` for the ssh ones. A wall-clock cap alone kills a slow-but-working clone; a
  transport option alone does not bound a server that accepts and then stalls.
- **S3** — the credential path is closed, not merely un-prompted. `GIT_TERMINAL_PROMPT=0` bounds
  git's OWN prompt and not a configured helper; this node carries `credential.helper=manager` with
  `credential.interactive` and `guiPrompt` unset, so a GUI prompt is reachable and would block with
  nothing on stdout. Set `credential.interactive=never` (or an askpass that refuses) at every call
  site.
- **S4** — the same three bounds apply in `check-unattended.sh`, at its TWO call sites — the
  `ADV_HEAD` symref advertisement (`:228`) and the `ADV_TIPS` heads listing (`:230`), both inside the
  leg's one-advertisement-per-run block — where an unbounded call is strictly worse: the leg runs
  inside `$GATE_CMD`, which runs inside `.githooks/pre-push`, so a stall hangs the push instead of
  reddening it. **`:211-212` is NOT a third call site**: it is the `GIT_TERMINAL_PROMPT=0` rationale
  COMMENT that S5 corrects. Rev-3 listed it beside the two calls, which sent a builder hunting for a
  site that does not exist; it is named here as the comment it is.
- **S5** — the leg's comment claiming `GIT_TERMINAL_PROMPT=0` makes a credential prompt *refuse
  rather than hang* is corrected to what it does.
- **S6** — `refuse_if_terminal` moves ABOVE the `observe_anchor` prologue in `verb_close`, so a close
  against an already-terminal record refuses for free. The prologue's own refusals are explicitly
  non-fatal to `--close`, so nothing depends on it running first.
- **S7** — a transport failure stops being reported as a semantic answer. `branch_tip_quiet`'s
  `|| return 2` collapses git's 128 (could not connect) into 2 (answered, no matching ref), so a
  network fault tells the operator to push a branch that is already pushed. `observe_anchor:241`
  splits the same pair correctly; this is that split applied one function over.
- **S8** — a timeout is a NAMED refusal carrying the endpoint, the elapsed bound and the fact that it
  is a timeout rather than an answer, so an unattended run's record says what happened.

## 3. Non-goals (OUT)

- Not retries, backoff, or a circuit breaker. A bounded refusal an operator or a resumed run can read
  is the deliverable; retrying a partition is a policy this unit does not have the evidence to set.
- Not an offline mode, and no caching of an advertisement. The anchor is deliberately OBSERVED from
  the remote on every read — that is the property `TOOL-aBranchedMandate-3` bought and two reproduced
  bypasses paid for. A cache is a local ref by another name.
- Not the legibility of the refusals themselves. That every one of these messages is currently
  discarded by a redirect is the sibling unit's scope; this unit makes them terminate. Both are
  needed and neither substitutes: an unbounded wait that prints its cause is still a hang, and a
  bounded one that prints nothing is still unreadable.
- No change to which anchors exist, to `ANCHOR_SCOPE`'s value set, or to the number of round-trips a
  close makes — except S6, which changes only WHEN the first one happens.
- **Not `run-gates.sh`'s per-leg deadline.** That is the OTHER half of `TOOL-aBoundedVerdict-10`, and
  the row keeps it: it stays OPEN after this unit lands, amended to say the anchor-timeout half is
  done and the deadline half is not. A bound on one leg's slowest call is not a bound on a leg, and a
  leg with no deadline can still wedge the bar from any other call.
- **This unit does not claim to fix the traced 240s hang, and the measurement says it will not.**
  Backlog row `TOOL-aPromptedMandate-9` measured the driver's precondition chain on node `a` and
  found the `ls-remote` answering in seconds while `check-wiring.sh --check` dominated the chain,
  I/O-bound — read the figures in that row, not here. So §4's grounds for a generous cap survive
  (no advertisement in this fleet is slow), but the corollary is stated plainly: bounding the
  observation makes a PARTITION terminate, and leaves the slow-preflight problem to that row.
- Not the rest of the bar's runtime. That the full bar is slow, and slower on a polluted `TMPDIR`, is
  environmental and separately recorded.

## 4. Design

### Data model

No data. One helper, and a bound expressed in seconds as a file constant with the same argument the
review protocol's cap uses: a bound that can be raised from the environment leaves no diff behind.
The constant is generous — the honest failure this guards is a partition, not a slow server — and it
is stated in the refusal so the number is discoverable without reading source.

### What was measured

`grep -rnE 'timeout|lowSpeed|ConnectTimeout|GIT_HTTP|GIT_SSH' tools/unattended/` returns nothing
outside the test files, and `git ls-remote` has no `--timeout`. Against a blackhole IP in a scratch
repo, `observe_anchor`'s call ran until an external `timeout 8` killed it, with no output. Two
corrections the audit made against its own first framing, kept here because they bound the fix:
`--close` opens with ONE round-trip, not two — the `ls-remote --get-url` at `:231` is offline by
design and measured 0s against the same unreachable URL — and `observe_anchor` is the third statement
of `verb_close`, not the first.

### Why three bounds and not one

Each covers a different failure, and the audit's own reproduction only exercised the first:

| failure | wall-clock cap | lowSpeed / ConnectTimeout | credential.interactive=never |
|---|---|---|---|
| packets blackholed | bounds it | `ConnectTimeout` bounds ssh; HTTP connect may not | — |
| server accepts, then stalls mid-transfer | bounds it, bluntly | `lowSpeedTime` bounds it precisely | — |
| helper opens a GUI prompt | bounds it only if the cap kills the child | — | prevents it |
| slow but working clone | **false positive if the cap is tight** | tolerates it | — |

The last row is why the cap is not the only mechanism and why it is generous: a tight cap converts a
working slow link into a refused close, which is a new stall wearing the fix's clothes.

### Inventory

| Concern | Today | After |
|---|---|---|
| `ls-remote` NETWORK call sites | 2 in the driver — `observe_anchor`'s HEAD advertisement and `branch_tip_quiet`'s branch tip — and 2 in the leg, the `ADV_HEAD` symref and the `ADV_TIPS` heads listing; none bounded | every one bounded through one helper |
| `ls-remote --get-url` | 1 in the driver, OFFLINE by design, measured 0s against an unreachable URL | unchanged, and excluded from the bound by name rather than by accident |
| a partition under `--close` | indefinite silent wait | named refusal naming endpoint and bound |
| a partition under `pre-push` | the push hangs | the leg reds |
| a credential helper prompt | reachable, blocks | prevented |
| `--close` on a terminal record | pays a round-trip first | refuses for free |
| transport failure vs "no such ref" | collapsed to one status | split, as `observe_anchor` already does |
| the leg's comment about `GIT_TERMINAL_PROMPT=0` | states a bound it does not provide | states what it does |

**Two more `ls-remote` hits are PROSE, not sites.** A grep over the pair also returns the driver's
`resolve_base` note about an adopter paying no extra `ls-remote`, and the leg's
`GIT_TERMINAL_PROMPT=0` rationale that S5 corrects. Neither is a call. Both are why AC5 is written
over `grep -n` and excludes comment lines by name — a count over the file text cannot tell a call
from a sentence about one.

### Migration

None on disk. One behavioural change worth stating plainly: a close that today would hang forever
will now refuse. That is the point, and it means a run previously wedged in a silent wait becomes a
run with a readable terminal outcome — which the abort verb can then record.

### Rollout

S6 and S7 first: both are local, need no new constant, and S6 removes the cost from the commonest
wasted call. Then S1-S3 in the driver, then S4-S5 in the leg, then S8's message. The leg last on
purpose: it runs inside the pre-push hook, so a defect there is discovered at the worst moment.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the helper, the constant, two call sites, the ordering move, the
status split) · `tools/unattended/unattended.test.sh` (arms per refusal, and the ordering arm) ·
`tools/unattended/check-unattended.sh` (TWO call sites and one comment — the third `ls-remote`
reference in that file is the comment) + `check-unattended.test.sh` ·
`.memory-tree.conf` (`ARMS_FLOORS`, for the new `fail` call sites) ·
`memory/guides/SESSION-KICKOFF.md` — the kickoff manifest is re-stamped in the SAME commit, because
`.memory-tree.conf` is on its `watch:` list and an unstamped edit reds the ratchet both staged and
committed ·
**the kit version bump, which is not one carrier** — `tools/unattended/unattended.sh` and
`tools/unattended/check-unattended.sh` each move `KIT_UNATTENDED_VERSION=` AND the `gov:kit` marker
on the same line, `tools/unattended/PROTOCOL.template.md` and `tools/unattended/SKILL.template.md`
each move their `gov:kit` marker, and `.claude/skills/unattended/SKILL.md` is re-rendered because
`check-wiring.sh` compares it to the tracked template; `tools/check-kit-versions.sh` forces all of
them ·
`memory/map/features/unattended.md` (the dossier claims the bound) ·
`memory/backlog/TOOL.md` — section 3's non-goal commits to amending `TOOL-aBoundedVerdict-10` on
landing, to say the anchor-timeout half is done and the per-leg-deadline half is not, so the file that
carries that row is declared here rather than edited by a commitment nothing lists. Three sibling
units in this build declare the same carrier for the same reason.

### Alternatives rejected

- **An external `timeout` in the callers rather than a helper.** Rejected: the leg and the driver
  would each spell the bound, which is the two-answers class this build is full of, and the rendered
  Skill would need a third spelling.
- **`GIT_HTTP_LOW_SPEED_*` environment variables instead of `-c http.lowSpeed*`.** Equivalent effect;
  rejected because `observe_anchor` refuses to run when git config arrives through the environment
  (check 22), and adding an environment mechanism to a function built to distrust the environment
  invites exactly the confusion that check exists to prevent.
- **Cache the advertisement for the duration of a run.** Rejected in §3: the observation's value is
  that it is not local.
- **Bound only the driver, not the leg.** Rejected on S4's reason — the leg's calls are the ones that
  hang a push.
- **Make the bound a conf key.** Rejected on the review protocol's argument for a file constant, and
  because an adopter who needs a different bound has a slow remote, which is the false-positive case
  the generous default already covers.

## 5. Production-readiness checklist

- **security** — the credential change is the one to read carefully. `credential.interactive=never`
  must not be set so broadly that it disables credentials for the LANDING push, which is a different
  process and must still authenticate; scope it to the observation calls with `-c`, never to the
  repo's config.
- **perf / scale** — improves the failing case, unchanged on the happy path. S6 removes one round-trip
  from every close against a terminal record.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — S8 is the error state. The empty case: a timeout must not be
  reported as "the remote answered and advertised nothing", which is precisely S7's defect one
  function over.
- **observability** — S8, plus the sibling unit's progress line. The bound is stated in the refusal
  so the number is discoverable without source.
- **risks** — the false-positive on a slow link, mitigated by a generous cap plus precise transport
  options. Concurrency: none. Data loss: none; every call is a read.
- **testing + left-shift gates** — TWO fixture mechanisms, because one does not reach both arms. The
  timeout arms use an unroutable address, which is hermetic and needs no network. The FALSE-POSITIVE
  arm (AC8) cannot: an unroutable address transfers nothing, so it can never present a slow-but-
  working transfer. That arm drives the helper against a stub that sleeps under the bound and then
  succeeds — wall clock only, no network, no git transport. The left-shift is a source-level rule
  that no `ls-remote` may appear outside the helper, in both the driver and the leg, armed in
  `tools/unattended/unattended.test.sh` per §8 F2 — and it must be written to survive the COMMENTS
  that document it (`memory/gotchas/absence-assertion-over-whole-file-text.md`), which is what AC5
  spells out.
- **migration / rollback** — none; revert is the helper's removal.
- **user docs** — the map dossier, and the leg's corrected comment. The protocol describes WHAT is
  observed, not with what bound, so it needs no change.

## 6. Acceptance criteria

- **AC1** — When `--close` runs against a fixture whose remote endpoint REFUSES the connection, it
  exits non-zero promptly with the named refusal, and an outer `timeout` above the bound does not
  fire. **What this fixture does not reach, stated so a green arm is never misread as coverage of the
  wall clock:** a refused connection returns without the bound being consulted, so this arm proves the
  refusal PATH and not the deadline. The deadline is graded instead by AC1a's mechanism arm and by
  AC3's elapsed assertion, and no arm drives a blackholed endpoint for the full bound — that would add
  the declared bound to the wall clock of the slowest leg on the bar, in a suite whose historical
  failure mode is exactly a leg that takes too long. The trade is recorded rather than taken quietly.
- **AC1a** — **the mechanism arm, and it is the one that makes the bound credible.** On the node
  running the suite, `timeout -k 2s 1` around a process that leaves a background descendant is
  measured twice: captured through a command substitution, and redirected to a FILE. The file form
  must complete inside a small multiple of the declared 1 s; the substitution form is measured and
  REPORTED rather than asserted, because it is a property of the platform and not of this kit. If the
  file form does not bound the clock on this node, the helper's bound is inert here and the arm says
  so — a bound nobody has watched fire is an assertion about nothing.
- **AC2** — When the same fixture is driven through `bash tools/unattended/check-unattended.sh`, the
  leg reds within the bound rather than hanging.
- **AC3** — When `--close` is invoked on a record whose phase is `LANDED`, no `ls-remote` runs —
  observed by pointing the remote at an unroutable address and seeing the terminal refusal return
  immediately.
- **AC4** — When the remote is reachable but advertises no matching branch ref, `branch_tip_quiet`
  returns its "no such ref" status; when the remote is unreachable, it returns a DIFFERENT status and
  the caller's message does not tell the operator to push. Two arms in
  `tools/unattended/unattended.test.sh`.
- **AC5** — When `grep -n 'ls-remote' tools/unattended/unattended.sh
  tools/unattended/check-unattended.sh` is taken, EVERY hit's LINE is a member of a sanctioned set
  written into the arm: a line whose `ls-remote` is an argument to the bounded helper, the offline
  `--get-url` line, or a COMMENT line, matched as such by its leading `#` and excluded deliberately
  rather than by luck. Any other
  hit fails the arm. The arm lives in `tools/unattended/unattended.test.sh` (§8 F2) and implements
  §5's testing + left-shift item. **`grep -c` cannot express this criterion** — it prints one number
  per file, a number that already includes the two prose hits, so no value of it distinguishes a call
  site from a sentence. That is the class at
  `memory/gotchas/absence-assertion-over-whole-file-text.md`, and rev-3's AC5 was an instance of it.
- **AC6** — When a credential helper would prompt, it does not: `credential.interactive=never` is
  observable in the helper's own invocation, passed with `-c` so it is scoped to that call and cannot
  reach the landing push. Asserted at source level in the same arm that reads the other three options
  no runtime fixture can reach — `http.lowSpeedLimit`, `http.lowSpeedTime` and
  `ssh -o ConnectTimeout` — each of which appears in the invocation and whose runtime effect is
  untested for the reason AC8 records. Source-level is the honest home for all four: a fixture that
  could exercise them would need a server that authenticates, stalls mid-transfer, and speaks ssh.
- **AC7** — When `tools/unattended/check-unattended.sh` is read, its comment about
  `GIT_TERMINAL_PROMPT=0` states that the variable bounds git's own prompt and not a configured
  helper.
- **AC8** — When the bounded helper is driven against a STUB THAT SLEEPS AND THEN SUCCEEDS — a fake
  `git` ahead of the real one on `PATH` that sleeps a fixed interval below the wall-clock bound on
  `ls-remote` and forwards every other subcommand to the real binary, then exits 0 with a well-formed
  advertisement on stdout — the helper returns the stub's answer and
  `--close` still succeeds; the bound does not fire. Wall clock only: no network, no git transport, no
  remote. This is the false-positive arm, the only one proving the cap is not merely tight enough to
  pass AC1, and it lives in `tools/unattended/unattended.test.sh`. **The `http.lowSpeedLimit` /
  `lowSpeedTime` arm is NOT COVERED, deliberately.** Exercising it needs a remote that accepts a
  connection and then transfers below the threshold for longer than `lowSpeedTime`, and neither
  fixture can produce that: an unroutable address transfers nothing at all, and the sleeping stub
  never reaches git's transport layer. Those two options are therefore asserted by INSPECTION only —
  they appear in the helper's invocation, where AC5's arm reads them — and their runtime effect is
  untested. Written here so a green AC8 is never misread as coverage of §4's "server accepts, then
  stalls" row.

## 7. Gates

`bash tools/run-gates/run-gates.sh` whole, and specifically: `unattended driver selftest` ·
`unattended kit gate` + `check-unattended.test.sh` · `harness arms`
(`tools/memory-tree/check-arms.py`, one arm per new `fail`) · `testsuite counts` ·
`pre-push self-test` (`.githooks/pre-push.test.sh`, because S4 changes what happens inside the hook's
gate run) · `codebase-map coverage + freshness` (the dossier claims the bound) ·
`kit version markers` · `skills/session-kickoff/manifest-check.sh` (the `.memory-tree.conf` edit is
on the manifest's watch list, so the re-stamp rides in the same commit).

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — what is the wall-clock bound, in seconds?** It must exceed a cold ssh handshake to a busy
  host and a large advertisement on a slow link, and it must be short enough that an unattended run
  fails within a keepalive interval rather than between two of them — that interval is declared as ten
  minutes. **Recommendation: 60s per call, with the two transport options doing the precise work.**
  Grounds: three calls at 60s is bounded well inside one keepalive tick, and no measured
  advertisement in this fleet has taken more than single-digit seconds.
  RESOLVED (agent, 2026-08-19, delegated): 60s. Mechanism-only, and the bound is stated in the
  refusal so it is discoverable and revisable without archaeology.

- **F2 — does the source-level rule live in the driver's test suite or in the kit gate?** The rule
  spans TWO files, one of which is the gate itself, so a gate asserting it about its own source is the
  self-reference this repo already handles elsewhere with an exclusion. **Recommendation: the driver's
  test suite**, which already reads both files' source for other arms and is not a subject of its own
  assertion.
  RESOLVED (agent, 2026-08-20, delegated): the DRIVER'S TEST SUITE. Mechanism-only, and the
  alternative is the self-reference the bullet names: a gate asserting a source-level rule about its
  own source needs an exclusion, and an exclusion is only as wide as the control it defers to. The
  suite already reads both files for other arms and is not a subject of its own assertion.

- **F3 — should the bound apply to the LANDING push as well?** Out of scope as written: the push is
  `$LANDER`, a project declaration this kit does not wrap, and bounding someone else's lander is a
  change to what the mandate delegates. Raised because a hung push is the same stall one command later.
  RESOLVED (owner, 2026-08-19): **yes, in a FOLLOW-UP UNIT, not here.** `TOOL-aBoundedVerdict-21`
  carries it. This unit keeps its scope — the observations — because widening it to wrap a
  project-declared command would change a contract every adopter reads, inside a unit reviewed for
  something else. The cost the owner accepted: the hung-push stall survives until that unit lands, and
  this spec says so rather than implying the bound is complete.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's blocker 14·29·6 and its
  mediums 19, 12 and 18, consolidated as one mechanism — the bound on a remote observation — with the
  ordering and status-collapse points kept as separately verifiable scope items because each is
  independently fixable. F1 and F2 resolved under the delegated fork rule; F3 raised to the owner
  because it changes what the mandate delegates.

- rev-2 · 2026-08-19 · F3 resolved by the owner: the landing push IS bounded, but by
  `TOOL-aBoundedVerdict-21` rather than here, so this unit's scope is unchanged. Recorded with the cost
  the owner accepted — the hung-push stall survives until that unit lands — because a spec that bounds
  "every remote observation" and leaves the push unbounded must not read as if it bounded everything.

- rev-3 · 2026-08-20 · M3 fork sweep, before any code. F2 RESOLVED as recommended — the rule is
  armed in the driver's test suite, not in the kit gate, because a gate asserting it about its own
  source would need an exclusion. §8's first non-blank line is now the machine-legal `none` form.

- rev-4 · 2026-08-20 · folded the second M4 spec audit
  (`reviews/2026-08-20-review-TOOL-aBoundedVerdict-1.md`): H9, H10, H11, H12, M13, L2.
  **H9 — the inventory sent a builder after a call site that does not exist.** It said "3 in the leg";
  `check-unattended.sh` has exactly TWO `ls-remote` calls, at the declared base and at HEAD, and the
  third reference S4 listed (`:211-212`) is the `GIT_TERMINAL_PROMPT=0` rationale COMMENT — which is
  S5's own subject, so the spec was counting its comment fix as a call site. The inventory row now
  breaks the population down by NAME rather than by count — `observe_anchor` and `branch_tip_quiet`
  in the driver, `ADV_HEAD` and `ADV_TIPS` in the leg — with the offline `--get-url` on its own row,
  and a paragraph names the two PROSE hits so a grep result reads correctly. Every other line
  reference in S1, S4 and §4 resolves exactly at base `098bebd9` and was deliberately NOT renumbered.
  **H10 — AC5 could not fail for the right reason.** It was written over `grep -cE`, which prints one
  count per file; a count cannot express a LOCATION property, and the counts already included the two
  comment hits, so no value of them distinguished a call from a sentence about one. That is the class
  at `memory/gotchas/absence-assertion-over-whole-file-text.md` — flagged in §5 and ignored by the
  criterion two sections later. AC5 is now over `grep -n`, with the sanctioned set (helper body,
  `--get-url` line, comment lines matched by a leading `#`) written into the arm and the comment
  exclusion made explicit instead of incidental.
  **H11 — the false-positive arm had no mechanism that could exercise it.** AC8 is the only criterion
  proving the cap is not merely tight enough to pass AC1, and the sole declared fixture was an
  unroutable address, which transfers NOTHING and so can never present a rate below
  `http.lowSpeedLimit`. AC8 now names the real mechanism — a stub ahead of `git` on `PATH` that
  sleeps under the bound on `ls-remote`, forwards everything else, and succeeds; wall clock only, no
  network — and RECORDS THE SKIP: the `lowSpeedLimit`/`lowSpeedTime` arm is not covered, because
  neither fixture reaches git's transport layer, so those options are asserted by inspection only.
  §5's testing item carries the same two-mechanism split. A skip that announces itself, rather than a
  green row that reads as coverage of §4's "accepts, then stalls" failure.
  **H12 — the unit half-closed an OPEN backlog row and cited it nowhere.** `TOOL-aBoundedVerdict-10`
  names two fixes and this unit delivers one, so the row read as closed on landing. §1 now cites it
  and says which half lands; §3 gains a non-goal putting `run-gates.sh`'s per-leg deadline out of
  scope, with that same row keeping it. §3 also weighs `TOOL-aPromptedMandate-9`'s measurement, which
  found the `ls-remote` answering in seconds while `check-wiring.sh --check` dominated the
  precondition chain: §4's grounds for a generous cap survive it, but the corollary is now stated —
  this unit makes a PARTITION terminate and does not fix the traced slow preflight. The figures stay
  in that row rather than being copied here.
  **M13 (build decision D6)** — `.memory-tree.conf` is on the kickoff manifest's `watch:` list and
  `memory/guides/SESSION-KICKOFF.md` was missing from Files touched, so the ratchet would red the
  commit staged and committed alike; it is added with the same-commit re-stamp note, and §7 gains the
  ratchet leg. While there, **build decision D7**: "the kit version constant" was one phrase standing
  for five files and seven sites, and is now enumerated, because a builder cannot move a carrier the
  spec does not name.
  **L2** — AC5 attributed its source-level rule to "S5's checklist item"; S5 is the comment
  correction. The rule is §5's testing + left-shift item, and the arm's home is
  `tools/unattended/unattended.test.sh` per F2's resolution, which the criterion had not carried.
  Both are now written where they belong.

- rev-5 · 2026-08-20 · **written DURING the build, from what the M5 recall probe found.** The probe
  returned a blocker this spec could not have known: a sibling build measured, hours earlier, that
  `out=$(timeout N cmd)` does not bound the wall clock — the command substitution reads until EOF and
  a surviving descendant holds the pipe — and its fix had already landed in the gate runner. This
  spec's S1 said "an outer wall-clock cap" and nothing about capture, so the obvious implementation
  was the broken one. Reproduced on node `c` before designing on it: 6 s against a declared 1 s bound
  through a substitution, 0 s through a file. **S1a and S1b are new**, S1b because the helper cannot
  call the driver's own `GIT()` wrapper through `timeout` and the dereference pins therefore needed a
  single home rather than a second spelling. **AC1 is narrowed and AC1a is new:** the refusing-endpoint
  fixture proves the refusal path and never consults the deadline, so claiming it covered the bound
  would have been the green-by-absence class this build is full of gates against; the deadline is
  graded by a mechanism arm plus AC3's elapsed assertion, and the decision NOT to spend the full bound
  in the bar's slowest leg is recorded rather than taken quietly. **AC6 widened** to the three options
  no fixture can reach, each asserted by inspection and each stated as runtime-untested. AC5's
  sanctioned set now describes a line where `ls-remote` is an ARGUMENT to the helper, which is what the
  implementation produced.

- rev-6 · 2026-08-20 · **built, and four things the building corrected.** (1) The kit version is SIX
  carriers, not the five this spec's Files-touched list inherited from the fold brief: the installed
  `memory/guides/UNATTENDED-PROTOCOL.md` carries the `gov:kit` marker too, forced by the unattended
  leg's check 10 rather than by `check-kit-versions.sh`, which is why a list derived from the latter
  missed it. Observed by bumping five and watching check 10 red. The list now lives once, in the build
  README's cross-unit rules. (2) The timeout refusal was first written as a shared
  `remote_timeout_note` helper and `fail 27 "$(...)"`. That branch CANNOT BE ARMED —
  `check-arms.py` signs a branch with the LITERAL source text of its `fail` call, so the signature
  became the opening characters of a command substitution — which is the same class as the recorded
  positional trap. The sentence is inlined with only interpolations trailing, and the helper is gone;
  it had one caller, so the indirection bought nothing and cost the arm. (3) `ARMS_FLOORS` for the
  driver moves 81:78 to 91:88, from `--report` rather than from arithmetic, and the two new refusals
  are ARMED rather than pinned: the registry's contract is that a pin means no fixture CAN reach a
  branch, and "chose not to" is a different fact wearing the same row. A dead `TMPDIR` reaches the
  scratch-file guard; a stub `git` exiting 124 — the status `timeout` itself returns — reaches the
  timeout refusal without spending the declared bound. (4) Inserting a `fail 27` branch RENUMBERED the
  pinned row for an unrelated branch from ordinal 2 to 4, which surfaced as a stale-signature
  complaint that reads like a rewording; the registry now records why the ordinal moved.
  **One measurement for whoever runs this leg next:** the driver selftest did not complete inside
  1200 s on node `c` while another session held the box, and produced no output at all inside 900 s
  on a later attempt. Four cores, seven live `bash`/`git` processes, a second worktree active. That is
  the recorded contention behaviour, not a hang — the leg's own tracked incident is a genuine hang and
  the two are indistinguishable from a wall clock alone, which is why the arms print progress markers.

## 10. Reuse audit

The seam is `GIT()`, the driver's own git wrapper, which every call in this unit already routes
through and which exists so the object-substitution lever stays inert. The bounded helper wraps `GIT`
rather than replacing it, so nothing this unit adds can bypass that property.

The second seam is `observe_anchor:241`'s existing split between a transport failure and a semantic
answer — S7 is not new logic, it is that logic applied at the one call site whose author wrote `||
return 2` instead. Naming it here is what makes S7 a two-line change rather than a design.

No `reuse_lookup.py` pass returned a bounded-subprocess seam; the SET-level recall pass for this
build is recorded in the sibling specs with its terms, and the answer for this unit's question was
that nothing in the tree bounds a subprocess — which is the probe's answer and is what §4's
measurement confirmed independently.

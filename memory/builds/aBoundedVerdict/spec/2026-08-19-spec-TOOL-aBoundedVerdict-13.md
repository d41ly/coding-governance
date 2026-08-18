# TOOL-aBoundedVerdict-13 — every remote observation is bounded, and pays its cost last

**Status:** SPECCED · rev-1 · 2026-08-19 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

Nothing in the unattended kit bounds a remote round-trip, and `--close` opens with one — so a
partitioned network turns the close into an indefinite silent wait, and the same calls inside the
gate leg turn a `git push` into a hung push rather than a red one. Bound every remote observation,
and stop paying for one before the free refusals that would have blocked the close anyway.

## 2. Scope (IN)

- **S1** — a single bounded-observation helper in `unattended.sh` wraps every `ls-remote`. Both call
  sites go through it: `observe_anchor`'s HEAD advertisement (`:240`) and `branch_tip_quiet`'s
  per-branch tip (`:298`, reached twice under `ANCHOR_SCOPE="published"` — once from `resolve_base`
  and once from `trusted_base`'s alternate).
- **S2** — the bound is belt and braces, because no single mechanism covers every transport: an outer
  wall-clock cap, plus `http.lowSpeedLimit`/`http.lowSpeedTime` for the HTTP transports and
  `ssh -o ConnectTimeout` for the ssh ones. A wall-clock cap alone kills a slow-but-working clone; a
  transport option alone does not bound a server that accepts and then stalls.
- **S3** — the credential path is closed, not merely un-prompted. `GIT_TERMINAL_PROMPT=0` bounds
  git's OWN prompt and not a configured helper; this node carries `credential.helper=manager` with
  `credential.interactive` and `guiPrompt` unset, so a GUI prompt is reachable and would block with
  nothing on stdout. Set `credential.interactive=never` (or an askpass that refuses) at every call
  site.
- **S4** — the same three bounds apply in `check-unattended.sh` (`:211-212`, `:228`, `:230`), where an
  unbounded call is strictly worse: the leg runs inside `$GATE_CMD`, which runs inside
  `.githooks/pre-push`, so a stall hangs the push instead of reddening it.
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
| `ls-remote` call sites | 2 in the driver, 3 in the leg, none bounded | all bounded through one helper |
| a partition under `--close` | indefinite silent wait | named refusal naming endpoint and bound |
| a partition under `pre-push` | the push hangs | the leg reds |
| a credential helper prompt | reachable, blocks | prevented |
| `--close` on a terminal record | pays a round-trip first | refuses for free |
| transport failure vs "no such ref" | collapsed to one status | split, as `observe_anchor` already does |
| the leg's comment about `GIT_TERMINAL_PROMPT=0` | states a bound it does not provide | states what it does |

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
`tools/unattended/check-unattended.sh` (three call sites, one comment) + `check-unattended.test.sh` ·
`.memory-tree.conf` (`ARMS_FLOORS`, for the new `fail` call sites) · the kit version constant ·
`memory/map/features/unattended.md` (the dossier claims the bound).

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
- **testing + left-shift gates** — the fixture is a blackhole IP or an unroutable host, which is
  hermetic and needs no network. The left-shift is a source-level rule that no `ls-remote` may appear
  outside the helper, in both the driver and the leg — and it must be written to survive the comment
  that documents it (`memory/gotchas/absence-assertion-over-whole-file-text.md`).
- **migration / rollback** — none; revert is the helper's removal.
- **user docs** — the map dossier, and the leg's corrected comment. The protocol describes WHAT is
  observed, not with what bound, so it needs no change.

## 6. Acceptance criteria

- **AC1** — When `--close` runs against a fixture whose remote URL is an unroutable address, it exits
  non-zero within the declared bound and its output names the endpoint and the bound; measured with an
  outer `timeout` set above the bound, which does not fire.
- **AC2** — When the same fixture is driven through `bash tools/unattended/check-unattended.sh`, the
  leg reds within the bound rather than hanging.
- **AC3** — When `--close` is invoked on a record whose phase is `LANDED`, no `ls-remote` runs —
  observed by pointing the remote at an unroutable address and seeing the terminal refusal return
  immediately.
- **AC4** — When the remote is reachable but advertises no matching branch ref, `branch_tip_quiet`
  returns its "no such ref" status; when the remote is unreachable, it returns a DIFFERENT status and
  the caller's message does not tell the operator to push. Two arms in
  `tools/unattended/unattended.test.sh`.
- **AC5** — When `grep -cE 'ls-remote' tools/unattended/unattended.sh tools/unattended/check-unattended.sh`
  is taken, every hit is inside the bounded helper or is the offline `--get-url` call, asserted by the
  source-level arm S5's checklist item names.
- **AC6** — When a credential helper would prompt, it does not: asserted by driving a fixture whose
  remote requires auth with `credential.interactive` observable as `never` in the invocation, via
  `git -c credential.interactive=never`.
- **AC7** — When `tools/unattended/check-unattended.sh` is read, its comment about
  `GIT_TERMINAL_PROMPT=0` states that the variable bounds git's own prompt and not a configured
  helper.
- **AC8** — When a slow-but-working remote is simulated below the `http.lowSpeedLimit` threshold's
  tolerance, `--close` still succeeds — the false-positive arm in
  `tools/unattended/unattended.test.sh`, and the one that proves the cap is not merely tight enough to
  pass AC1.

## 7. Gates

`bash tools/run-gates.sh` whole, and specifically: `unattended driver selftest` ·
`unattended kit gate` + `check-unattended.test.sh` · `harness arms`
(`tools/memory-tree/check-arms.py`, one arm per new `fail`) · `testsuite counts` ·
`pre-push self-test` (`.githooks/pre-push.test.sh`, because S4 changes what happens inside the hook's
gate run) · `codebase-map coverage + freshness` (the dossier claims the bound) ·
`kit version markers`.

## 8. Open questions

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

- **F3 — OWNER. Should the bound apply to the LANDING push as well?** Out of scope as written: the
  push is `$LANDER`, a project declaration this kit does not wrap, and bounding someone else's lander
  is a change to what the mandate delegates. Raised because a hung push is the same stall one command
  later, and the answer decides whether a follow-up unit exists.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's blocker 14·29·6 and its
  mediums 19, 12 and 18, consolidated as one mechanism — the bound on a remote observation — with the
  ordering and status-collapse points kept as separately verifiable scope items because each is
  independently fixable. F1 and F2 resolved under the delegated fork rule; F3 raised to the owner
  because it changes what the mandate delegates.

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

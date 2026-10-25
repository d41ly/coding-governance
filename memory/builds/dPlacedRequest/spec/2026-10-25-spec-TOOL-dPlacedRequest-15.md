# TOOL-dPlacedRequest-15 — the fenced effect push: the lander's push carries the holder's lease beat atomically

**Status:** DEFERRED · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 9 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0133@231564d8 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-15-deviation-151.md](../build/2026-10-25-build-TOOL-dPlacedRequest-15-deviation-151.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

Close the check-then-act gap in fencing (gap-conc-12). Every effect push a lease holder makes, which
at `c63aabbb` is the lander's push of the default branch, carries the holder's new lease beat in one
`git push --atomic` under `--force-with-lease=<lease ref>:<tip read>`. A holder replaced between its
read of the lease and its push then lands nothing, with the branch left unchanged, and a re-push of an
unchanged lease ref, which the remote never checks, never counts as the fence (P40; research-cloud-
headless P2(b) and P2(c′)).

## 2. Scope (IN)

- **S1** — The remote's support is proven first: the build run's first observation is an `--atomic`
  push of two scratch refs to the real remote, one under a stale `--force-with-lease`, which must
  reject both. Observed by AC1.
- **S2** — The fence read: `unattended.sh --lease fence build <slug>`, a new act of
  TOOL-dPlacedRequest-1's `--lease` verb, reads the build lease `refs/gov/leases/<slug>/build` once,
  bounded, decides whether this session holds it by that verb's `lease` mode (the record's fleet tag
  and session equal this node's and this harness's), and prints exactly one line. Held: it builds a
  beat with `build_gov_commit <tip read> <message>`, the record copied with a fresh `beat-utc`,
  `renews: no` and the `witness` unchanged, so it carries no new witness and renews nothing (clause
  0135), pushes nothing, and prints `fence — <lease ref> <tip> <beat>`. `RUN_CLAIMS` off, or no lease
  ref on the remote: `fence — none · <why>`, exit 0. Held by another, terminal, or unreadable: the
  verb's refusal line `lease refused — <cause> · <tail> · <holder>`, exit 1, the cause one word of I9.
  Observed by AC2, AC5.
- **S3** — The fenced push: `tools/push-main.sh`, under `--land --slug <slug>` and under the attended
  landing given `--slug <slug>`, runs the fence read once per attempt before it clears the hook's
  verdict files. On a fence line it refuses unless the beat differs from the tip and the beat's first
  parent is the tip, then pushes
  `git push --atomic "--force-with-lease=<lease ref>:<tip>" <remote> <branch refspec> <beat>:<lease ref>`
  in place of today's single-ref push (`tools/push-main.sh:978`, `:1128`). On `none` it pushes as
  today; on `refused` it exits 1 and pushes nothing. Observed by AC2, AC3, AC4, AC5.
- **S4** — The fenced failure: when a fenced push fails and the existing classifier
  `derive_push_failure` (`tools/push-main.sh:262`) reads `unchanged`, the lander reads the lease ref
  once with `git ls-remote`: moved from the tip read is `fenced`, the lease lost and nothing landed;
  unmoved is `unfenced`, the remote refused the atomic push, nothing landed. Both exit 1, each line
  naming its remedy. `race` keeps its re-prepare, and the next attempt reads the lease again.
  Observed by AC2, AC6.
- **S5** — The landed beat joins the feed: `tools/push-main.sh` carries TOOL-dPlacedRequest-13's
  `gov_feed_sh` block inline, byte-identical, and the function that makes the fenced push calls
  `add_feed_event <lease ref> <beat>` once the push lands, so the feed holds the lander's lease write
  and `scan_feed_writers`, which reds a function pushing with `--force-with-lease` that calls neither
  `add_feed_event` nor `write_gov_ref`, passes it. Observed by AC4.
- **S6** — The attended landing takes `--slug`: `tools/push-main.sh` no longer refuses `--slug` without
  a flag (`:95`), and holds its value to the build-folder grammar the flags already use (`:99-106`);
  with it, the attended landing fences on that build's lease, and without it the landing names no
  build, covers no lease and pushes as today. Observed by AC7.
- **S7** — The documentation: the lander's header comment, the verbs guide's `fence` act row and
  its Land section, which under `primary` reads `LANDER --slug <slug>`. Observed by AC8.

## 3. Non-goals (OUT)

- Effect pushes that do not exist at `c63aabbb`: the driver pushes no build branch (`git grep -n
  "GIT push" tools/unattended/unattended.sh` finds nothing; its claim writes push through
  `observe_remote`), and the commit queue is
  dWellOiledMachine's. Each joins this fence when it lands, through the `fence` act.
- The release with `landed` and the mailbox's `landed` message in the same atomic push (P5): the
  release is TOOL-dPlacedRequest-16's write and the mailbox dKeptSession's.
- The lease grammar, the record, the `lease` mode and the epoch: TOOL-dPlacedRequest-1's. The parented
  commit and the lander lock's retirement: TOOL-dPlacedRequest-11's. Which beat renews:
  TOOL-dPlacedRequest-17's.
- The pre-push hook. It reads every pushed ref and gates once on the default branch's line
  (`.githooks/pre-push:606-617`), so the lease line rides an unchanged hook.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-11` — `build_gov_commit`, which builds the beat parented on the tip read, and the retirement of the lander's claim-push lock, after which a lease write from the lander's own git dir is safe; `write_gov_ref`'s porcelain reading is not reused, because the lander never reads its push's output and reads the lease's state after a failed push with `ls-remote`; without it the beat would be a parentless commit and the lander would still wait on the lock
- **consumes-from** `TOOL-dPlacedRequest-1` — the build lease `refs/gov/leases/<slug>/build`, its record, the `--lease` verb and its `lease` mode, which the fence act decides with; without it there is no lease to fence on
- **consumes-from** `TOOL-dPlacedRequest-13` — the change feed `gov-feed.log`, the `gov_feed_sh` block and `add_feed_event`, which the landed beat joins; without it the lander would be a `refs/gov/*` writer the feed's census reds
- **hands-off** `TOOL-dPlacedRequest-29` — the fence act, the fenced push and its failure table, which that unit gives a same-holder `refenced` class
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **consumes-from** `TOOL-dPlacedRequest-36` — the rule that a carrier of `gov_feed_sh` carries `health_log_sh` beside it, which `tools/push-main.sh` follows when this unit inlines the block
- **consumes-from** `TOOL-dPlacedRequest-37` — `NODE_LOCK_BOUND`, the block's own lock deadline, which the lander's copy carries so it takes the lock under `set -u` with no driver name
- **hands-off** `TOOL-dPlacedRequest-40` — `--lease fence`, which that unit exempts from the id-less refusal so the `fence — none` path keeps exit 0

## 4. Design

### Evidence

- The lander's two effect pushes are single-ref and unfenced: `git push "$remote" "HEAD:refs/heads/$def"`
  under `--land` (`tools/push-main.sh:978`) and `git push "$remote" "$def"` on the attended path
  (`:1128`); `git grep -- --atomic` finds no product use, only a comment
  (`tools/branch-reconcile/branch_reconcile.py:1099`).
- A failed push is classified by the hook's verdict, then a reachability probe, then ancestry, never
  by the push's words (`derive_push_failure`, `:262-292`); its output is shown and never read (S2 of
  the lander's header).
- The research probes: a holder that re-reads its lease and pushes normally lands its stale write
  (P2(a)); one `--atomic` push of the branch and a lease beat under the tip seen is rejected with the
  branch unchanged (P2(b)); re-pushing the lease ref unchanged sends no command for it, so nothing is
  checked (P2(c′)) (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-cloud-headless.md:35-37`).
- Whether the remote, GitHub, accepts `--atomic` is unconfirmed: the record cites a 2015 blog post and
  a 2019 list report only (`:45`). Git's client fails the whole push when the server does not
  advertise the capability, and a server sets `receive.advertiseAtomic false` to stop advertising it.
- The lander finds sibling kits with `resolve_kit_dir "$py" <kit> <file> "$self_dir"` (`:445`, `:735`),
  `self_dir` read at `:116`; it finds the driver the same way, with `resolve_kit_dir "$py" unattended
  unattended.sh "$self_dir"`, and with no driver beside it the fence reads `none`.
- The attended landing refuses `--slug` without a flag (`:95-98`).

### The fence read

```
--lease fence build <slug>   -> one line, exit 0 or 1
  RUN_CLAIMS off             -> fence — none · leases are off
  one bounded read of refs/gov/leases/<slug>/build
  read failed                -> lease refused — offline · <tail> · <why>       exit 1
  no ref                     -> fence — none · no lease on the remote
  lease mode not mine        -> lease refused — <cause> · <tail> · <holder>    exit 1
  mine                       -> beat = build_gov_commit <tip> <record, beat-utc now,
                                renews: no, witness unchanged>
                             -> fence — refs/gov/leases/<slug>/build <tip> <beat>
```

The read is the holder check and the compare-and-swap's expected value in one: nothing re-reads the
tip between them. A take-over after the read is caught by the remote, which compares the lease ref
with `<tip>` inside the atomic push, after the hook's bar has run.

### The fenced push

| Landing | Today | Fenced |
|---|---|---|
| `--land --slug <s>` | `git push <remote> HEAD:refs/heads/<def>` | `git push --atomic --force-with-lease=<lease>:<tip> <remote> HEAD:refs/heads/<def> <beat>:<lease>` |
| attended, `--slug <s>` | `git push <remote> <def>` | `git push --atomic --force-with-lease=<lease>:<tip> <remote> refs/heads/<def>:refs/heads/<def> <beat>:<lease>` |
| attended, no `--slug` | as today | as today: the landing names no build and covers no lease |

`check_fence_beat <tip> <beat>` runs before the push: `<beat>` differs from `<tip>` and
`git rev-parse <beat>^` is `<tip>`. A beat equal to the tip is the unchanged re-push P2(c′) shows is
never checked, so it is refused before anything is pushed. The lease is named only in
`--force-with-lease`, so the default branch keeps its fast-forward rule.

### The fenced failure

| `derive_push_failure` | Lease tip after | Class | Line and exit |
|---|---|---|---|
| `refused`, `unreachable` | not read | as today | as today, exit 1 |
| `race` | not read | as today | re-prepare; the next attempt fences again |
| `unchanged` | moved from `<tip>` | `fenced` | the lease was taken after the read; nothing landed; end the run with `--abort <slug> --code claim-lost`; exit 1 |
| `unchanged` | `<tip>` | `unfenced` | the remote refused the atomic push; nothing landed; leases stay off on a remote without atomic pushes; exit 1 |

`unfenced` is the fail-closed fallback: a remote that refuses `--atomic` never lands a fenced
landing, and the line names the switch as the way back to unfenced landings. The bar has already run
by then, because git runs the pre-push hook before it sends.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `fence` | an act of the `--lease` verb, kind `build` only | `tools/unattended/unattended.sh` |
| `write_fence_beat` | function | `tools/unattended/unattended.sh` |
| `check_fence_beat`, `read_fence_line` | functions | `tools/push-main.sh` |
| the `gov_feed_sh` block | inline copy, graded by TOOL-dPlacedRequest-13's parity row | `tools/push-main.sh` |
| `fenced`, `unfenced` | failure classes | `tools/push-main.sh` |
| `--slug` on the attended landing | argument | `tools/push-main.sh` |

### Files touched (estimate)

- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Re-read the lease's epoch, then push** (the design as first worded, layer-runtime:411-420). P2(a)
  lands the stale write.
- **Push the beat and the branch in two pushes.** A failure between them leaves one without the
  other, which is the check-then-act this unit removes.
- **Build the beat in the lander.** The record's format is the driver's; a second writer of it in
  `push-main.sh` would be a copy.
- **Fall back to an unfenced push when the remote refuses `--atomic`.** That reopens gap-conc-12
  silently on exactly the remote the fence cannot protect.

## 5. Production-readiness checklist

- security — the lander gains a second ref in its one push, the lease, written only by
  compare-and-swap on a tip the holder check read; nothing pushes without the hook, and the bypass ban
  is unchanged.
- perf / scale — one driver call, one bounded lease read and one local commit per attempt, one
  `ls-remote` on a failed fenced push, and one feed append after a landing.
- error / empty / loading states — no unattended kit beside the lander, the switch off and no lease
  ref each read `none` and land as today; an unreadable lease refuses, so an outage never lands an
  unfenced effect under a lease.
- observability — the fence line is printed before the push; `fenced` and `unfenced` name the lease,
  the tip read and the tip found.
- risks — a remote that refuses `--atomic` turns every leased landing into `unfenced` after a full
  bar; AC1 is ordered first so the build run learns it before any other pass relies on the fence.
- testing — AC1 against the real remote, AC2 to AC7 on fixtures, and the arms in §7.
- migration — none: with leases off every landing pushes exactly as before.
- user docs — the lander's header and the verbs guide's Land section; no page under `help/` describes
  the lander.

## 6. Acceptance criteria

The fixture for AC2 to AC7 is a bare remote and two clones under `%TEMP%` with short names, the lease
switch on, each clone's `.githooks/pre-push` a stub that writes the allow record `check_push_allow`
reads (`<pushed sha><TAB><run id>` in the git dir's `pre-push-allow`) and exits 0. The unattended
kit's own suites are waived for this build's landing (README rule 8), so each driver probe below is
the observation.

- **AC1** — When the build run pushes two scratch refs `refs/gov/probe/atomic/<session8>/a` and `/b`
  to `origin` with `git push --atomic --porcelain`, `/b` under a `--force-with-lease` naming a stale
  sha, the porcelain lines reject both, `/b` with `(stale info)` and `/a` with `(atomic push failed)`;
  the same push under the right sha writes both; and a delete push then removes both.
  Red when: the remote prints that it does not support `--atomic`, or `/a` is written while `/b` is
  rejected.
  permission: writes and deletes two scratch refs under `refs/gov/probe/` on the real remote, with
  the build run's push credential; this spec run did not run it.
  fixture: the real remote; a `--force-with-lease` against a bare remote proves nothing about it.
- **AC2** — When clone A holds lease `fx` and its stub hook, while the lander's push waits on it,
  has clone B take the lease over, `push-main.sh --land --slug fx` exits 1 naming `fenced`, the bare
  remote's default branch is unchanged and its lease tip is B's.
  Red when: the default branch moves; the planted case is a holder whose lease is taken over after it
  read the tip and before it pushes.
- **AC3** — When the fence line is planted with a beat equal to its tip, beside a default branch
  carrying a stale effect, the lander's `check_fence_beat` refuses before pushing, exit 1, and
  `git ls-remote` over the bare remote prints the default branch and the lease tip unchanged.
  Red when: the lander pushes; the planted case is a holder that re-pushes its unchanged lease ref
  beside a stale effect.
- **AC4** — When clone A holds lease `fx` and `push-main.sh --land --slug fx` lands, the bare remote's
  default branch is the pushed sha, the lease tip is the beat, `git rev-parse <beat>^` is the tip
  read, the beat's record reads `renews: no`, and clone A's `gov-feed.log` holds one event for the
  lease ref at the beat; `scan_feed_writers` over `push-main.sh` prints nothing.
  Red when: the lease tip does not move with the landing, the feed misses the event, or a planted
  copy of the pushing function without its `add_feed_event` call is printed by the census.
- **AC5** — When `RUN_CLAIMS` is off, or no lease ref exists, `unattended.sh --lease fence build fx`
  prints one `fence — none` line, and the lander lands with a single-ref push; against a lease clone B
  holds, it prints `lease refused — live-holder` and exits 1.
  Red when: a landing holding no lease is refused, or pushes a lease ref.
- **AC6** — When the bare remote sets `receive.advertiseAtomic false` and clone A lands under its
  lease, the lander exits 1 naming `unfenced`, and the remote's default branch and lease tip are
  both unchanged.
  Red when: the landing falls back to an unfenced push; the planted case is the fail-closed fallback.
- **AC7** — When `push-main.sh --slug fx` runs with no flag in clone A's primary tree holding lease
  `fx`, it fences as AC4 does; with no argument it prints no fence line and lands as before.
  Red when: `--slug` without a flag is refused, or the attended landing pushes a lease ref with no
  slug.
- **AC8** — When `grep -n "lease fence" tools/unattended/VERBS.template.md` and
  `grep -n "LANDER --slug" tools/unattended/VERBS.template.md` run, each finds its line.
  Red when: either is missing.

## 7. Gates

`push-main self-test` · `unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates`

New arm: tools/push-main.test.sh · covers AC2 AC3 AC4 AC5 AC6 AC7 · a take-over planted inside the stub hook, an unchanged-lease fence line, a fenced landing, no lease, a remote with `receive.advertiseAtomic false` and the attended `--slug`, staged against the base lander, which pushes one ref · the suite's assertion count raised by the arms added
New arm: tools/unattended/unattended.test.sh · covers AC5 · the `fence` act over the switch off, no lease, a held lease and a foreign one, staged against the base driver, which has no such act · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **FACT-QUESTION · F1 — Does the real remote accept `--atomic` and fence it?** Probe: AC1, two
  scratch refs pushed atomically under a stale lease, then the right one. Decided by the porcelain
  lines: both rejected, then both written. Liveness: the same probe prints the client's "does not
  support" refusal or a split outcome, each a negative. The brief places the observation in the build
  run, before any other pass relies on the fence; this spec specs the fail-closed fallback (S4,
  AC6) for the negative, so no option waits on it. RESOLVED (agent, 2026-10-25, delegated): fence
  with `--atomic`, observed first by AC1, failing closed as `unfenced` on a remote that refuses it.
  widens: none · relaxes: none
- **F2 — How does the lander learn which lease to fence?** (a) From the slug: `--land --slug` has it,
  and the attended landing gains an optional `--slug`; (b) by searching the remote for any lease this
  session holds; (c) `--land` only. (c) leaves every `primary` landing unfenced; (b) guesses when a
  session holds two leases and reads every lease on every landing. Rung 3 under the grant: the clause
  names every effect push, so the lander's argument surface is its change. RESOLVED (agent,
  2026-10-25, delegated): (a). grants: PLAY-dClosedLoop-3 `--slug` on the attended landing ·
  widens: none · relaxes: none
- **F3 — Where is the beat built?** (a) In the driver, the `--lease fence` act, which owns the record
  and the `lease` mode, the lander only pushing; (b) in the lander, rewriting the record's lines. (b) is a second
  writer of the record format. Rung 3. RESOLVED (agent, 2026-10-25, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: AC3 names its witnesses, `check_fence_beat` and
  `git ls-remote`; §7's leg line gains `recall floor` and `recall floor arms`.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-29,
  hands-off TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.
- rev-4 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirrors
  consumes-from TOOL-dPlacedRequest-36, consumes-from TOOL-dPlacedRequest-37, hands-off
  TOOL-dPlacedRequest-40.

## 10. Reuse audit

The seams extended are the lander's two effect pushes (`tools/push-main.sh:978`, `:1128`) and its
failure classifier `derive_push_failure` (`:262`), which keeps its order of evidence and gains a lease
read only on `unchanged`; the sibling-kit lookup `resolve_kit_dir` the lander already uses (`:445`,
`:735`); in the driver, TOOL-dPlacedRequest-1's `lease` mode and TOOL-dPlacedRequest-11's
`build_gov_commit` (today's `commit-tree` at `tools/unattended/unattended.sh:2419`, parentless); and
TOOL-dPlacedRequest-13's `gov_feed_sh` block, carried inline as every writer kit carries it. The probe
`python tools/codebase-map/reuse_lookup.py "push the default branch and a lease beat in one atomic push
fenced by force-with-lease"` ranked `resolveLease`, `check_lease_only_diff` and the claim-push lock
functions, none an atomic or multi-ref push. Scout A's row cited the pushes at `:978` and `:1128` and
`--atomic` only in a comment at `branch_reconcile.py:1099`; all three agreed with source at
`c63aabbb`. Its note that the pass push is the driver's but no driver push of a build branch exists
also agreed.

Recall terms used: `python tools/memory-recall/query.py "how does the lander fence its push against a
lost lease" --terms "lander push-main atomic force-with-lease lease beat fence stale holder take-over
epoch"`

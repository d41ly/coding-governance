# TOOL-aGraftedHelix-31 — `--settle` writes the run claim, and a terminal-phase writer that writes no claim reds

**Status:** CLOSED · rev-1 · 2026-10-05 · node a · Tier-2 · base 018b5675 · streams tooling · order 15 · ratified 2026-10-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-31-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-31-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-aGraftedHelix-29-1-spec-brief.md](../prompts/2026-10-05-prompt-TOOL-aGraftedHelix-29-1-spec-brief.md) | journal | TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-32 |

<!-- /gen:spec-records -->

## 1. Goal

`--settle` came in with the first reconciling merge and never writes the run claim, so a hand-off
its owner landed stays `held` on the remote for good, and the slug's next run is refused at check
107 by a claim nobody will release. This unit gives `run_settle` the status write that `--hold`,
`--landed` and `--abort` already carry. It also adds a kit-gate check that reds any function in the kit's
shell that writes a terminal phase and no claim, so the next terminal writer reds until it writes
the claim or names why not. The source is the closing review's H3, finding id 21.

## 2. Scope (IN)

- **S1** — After `run_settle`'s `stage_or_fail`, and before its `settled` lines, the status-write
  block `verb_abort` carries: where `RUN_CLAIMS` is `on`, `read_claims soft`, then
  `check_claim_writable "$slug" status <record keepalive> <record session> <record keepalive> "$rel"`,
  then `write_claim "$slug" <status> <record keepalive> soft "$rel"`. The status is `landed` on the
  `handed` branch and `aborted` on the `lease-dead` branch. Announced, and never failing the verb,
  exactly as the siblings' writes are. Observed by AC1, AC2, AC4 and AC5.
- **S2** — The `legacy` branch, and the already-settled exit, write no claim (§8 F1). Observed by
  AC3.
- **S3** — The status-write sentence of the stops template's section 7 names `--settle` with its two
  statuses and the branch that writes none. `memory/guides/UNATTENDED-STOPS.md` is re-adopted from
  it. Observed by AC8.
- **S4** — A new numbered check in `tools/unattended/check-unattended.sh`, the next free number at
  the pass's parent, 51 at `018b5675`. Over the kit's tracked shell files that are not self-tests,
  it reds a function that writes a terminal phase and never calls `write_claim`, unless the declared
  list `TERMINAL_CLAIM_EXEMPT_FNS` names it. It reds a list entry that names no such function. It
  reds when its scan finds no terminal writer at all. It prints one REPORT line of counts. Observed
  by AC6 and AC7.
- **S5** — Arms for S4 in the kit gate's own self-test: a staged terminal writer with no claim
  write, the same writer on the list, a stale list entry, the liveness break, and a control over the
  shipped driver and list. Observed by AC7.
- **S6** — Arms for S1 and S2 in the driver's self-test, inside the `--settle` block's own scratch
  repository: the handed branch through `--claims`, the lease-dead branch, the legacy branch, a
  foreign live claim, and the switch off. Observed by AC1 to AC5.
- **S7** — Every `fail` branch S4 adds is armed by a positive assertion naming its text, so the
  arms leg pins none. Observed by AC10.
- **S8** — The unattended kit version, bumped once after the last move, in every carrier
  `tools/check-kit-versions.sh` enumerates. Observed by AC9.

## 3. Non-goals (OUT)

- No change to `read_claims`, `check_claim_writable`, `write_claim`, the claim write table, the
  claim's status vocabulary or `CLAIM_MODES`. The settle's write takes the `status` column as the
  other status writes do.
- No fix to `read_claims soft` letting check 24 fail a verb after its record writes. That is the
  closing review's M6, batched into TOOL-aGraftedHelix-32, and it is fixed in the shared reader, so
  `--settle` inherits the fix with the other four writers.
- No helper shared by the five status-write blocks (§4, Alternatives rejected).
- No claim write in any `--settle` refusal, and none at the already-settled exit (§3 Edges, §8 F1).
- No grading of `HELD`, of the `abandoned` fact, or of a phase write whose value is a variable, by
  the new check. §4 names each with its reason.
- No content edit to the protocol or verbs templates, and none to the stops template beyond the
  section 7 sentence and its version marker line (§8 F3).
- No gotcha class record: the check S4 adds is the class's gate. No dossier edit: no inventory key is
  minted (§4, Inventory). The stops dossier's stale claim-check numbers are the review's L4, also in
  the minors batch.

### Edges

- **consumes-from** external — `--settle` and its three branches, merged in from dUnstuckLanding as
  TOOL-dUnstuckLanding-14, and the claim write table with its `status` column, which this build's
  first unit shipped. This unit builds neither, and every criterion here runs them as they stand at
  `018b5675`.
- **hands-off** external — a settle whose status write does not complete leaves a hand-off's claim
  `held`, and a `held` claim never ages to `stale`, so no verb takes it over: the next `--preflight`
  of the slug is refused at check 107, and the already-settled exit writes nothing on a re-run. Its
  siblings leave a `live` claim that ages and is taken. A retry path is a mechanism of its own (M2),
  so this run's orchestrator adopts it as a unit or parks it.

## 4. Design

### The defect, measured

At `018b5675`, `run_settle` runs from line 5917 to 6028 of `tools/unattended/unattended.sh`. Its
`handed` branch writes `phase LANDED` at line 6010 with three facts, its `legacy` branch writes
`work-landed-at`, and its `lease-dead` branch writes `work-landed-at` and `abandoned`. It stages the
record at line 6020 and returns, and no line of it calls the claim functions. The review cites the
range as `:5917-6045`, which runs into `verb_preflight`; the function closes at 6028.

A hand-off's claim was last written by `run_hold` at 5786 to 5789, as `held`, under the record's
keepalive and session. `read_claims` maps `held` to verdict `held` at any age, and the `--preflight`
column reads a foreign `held` claim as check 107. So a settled hand-off blocks its slug.

The three sibling blocks are identical but for the status: `verb_landed` at 5095 to 5098 and 5345 to
5348, `verb_abort` at 5486 to 5489, and `run_hold` at 5786 to 5789. Each runs after its verb's last
`stage_or_fail`, so check 48 sees no fact written after the last stage.

### The status write

S1 copies that block. `_sk` is the record's `keepalive`, read once, and a new local holds the status
the branch selects, empty on `legacy`. `run_settle`'s `local` line gains both names. Handed the
record's keepalive and session, `check_claim_writable` reads the hand-off's `held` claim as `mine`,
because `run_hold` wrote it from those facts, and it does so whatever session runs the settle. The
`status` column then writes. A claim another session holds `live` or `held` is announced and left,
an `unknown` one too, and the settle still exits 0 with its record staged.

On the `lease-dead` branch the claim is the dead holder's `live` one, `mine` by the same rule, and it
is written `aborted`. Left `live` it would age to `stale` and be announced at every other slug's
`--preflight` until the slug's next run took it over.

`write_claim` copies `session`, `host` and `lease-utc` from the record, so the settle writes the run's
identity and never the settler's. No fact is written after the stage, so check 48 stays silent on
`run_settle`.

### The stops template

Section 7's sentence becomes, with only the `--settle` clause new:

> The status writes are `--hold` (`held`), `--landed` (`landed`), `--abort` (`aborted`), `--settle`
> (`landed` over a landed hand-off, `aborted` over an abandoned working record, and none over a
> legacy `ABORTED` one) and the landing re-bind (`live`, its new keepalive), each after its own
> staging and never failing its verb.

The kit's adopter re-renders `memory/guides/UNATTENDED-STOPS.md`, and `adopt-unattended.sh --check`
compares the two.

### The class gate — the check, its predicate and what it does not check

The check sits after check 50, inside the block `--only 28` skips. Its header uses the
`# ---- check <n> - ` spelling the `--only 28` announcer reads, and states what it does not check.

**Population.** `_c48_files`, the array check 48 builds from `GIT ls-files -- "$KITREL"`, is
reused, never listed twice. A `*.test.sh` entry is skipped: a self-test stages terminal writes inside
`sed` scripts and fixture copies, and none of them is a writer of this kit.

**Framing.** Check 48's own: a function opens on a column-0 `name() {` line and closes on the next
column-0 `}`, or on its opening line when that ends in `}`. Full-line comments are skipped.

**Predicate.** A terminal write is a `set_fact` call whose first argument is a plain shell variable,
quoted or not, whose second word is `phase`, and whose third is a literal member of
`PHASES_TERMINAL`. The set is the one the leg already reads from the driver through `core_of`, never
restated. A claim write is a `write_claim` call on a non-comment line of the same function. A hit is
a function holding at least one terminal write and no claim write, whose name the list does not hold.

**The list.** `TERMINAL_CLAIM_EXEMPT_FNS`, declared beside the check as `PHASE_RECORDED_FNS` is beside
check 39, so a fixture can move it. It ships EMPTY. An entry carries its reason on a comment line
above the declaration. An entry naming anything other than a function the predicate would hit reds,
whether it is a ghost, a function with no terminal write, or one that now writes the claim: a stale
row widens the very set it was written to narrow.

**Liveness.** The awk prints its counts last. A run whose counts are missing, or whose scan finds no
terminal writer, FAILS rather than reports. The driver certainly holds `--abort`'s terminal write,
so a scan that finds none no longer matches how the driver spells the write, and grading it would
pass by finding nothing.

**Messages.** One `fail` for the findings, each finding on its own indented line as check 39 prints
them, its head saying a function writes a terminal phase and no run claim. One `fail` for liveness,
its head saying the scan found no function writing a terminal phase. The REPORT line reads
`check <n> graded <f> function(s) in <m> shell file(s) of this kit, <t> writing a terminal phase,
<e> exempt`.

**What it does NOT check**, written into its header:

- A PATH. It grades a function, so a function that writes the claim on one branch and a terminal on
  another passes. `run_settle`'s two writing branches are observed by the driver arms, AC1 and AC2.
- `HELD`. It is not terminal, and which phases a claim status mirrors is declared nowhere the leg
  could read it. Its one writer, `run_hold`, is observed writing `held` by unit 1's status-write arm.
- The `abandoned` fact, a terminal for rotation only. Its one writer is `run_settle`, which the
  predicate reaches through its `LANDED` write.
- A phase written as a variable, `verb_phase`'s `$want` and `run_takeover`'s `$hf`. `verb_phase`
  refuses a terminal at check 19, and check 40 grades the producers it may not reach.
- That the claim's status matches the phase, that the write is guarded by `RUN_CLAIMS`, or that it
  follows the stage.
- `verb_preflight`'s terminal write is to a scratch copy of the record being retired. It passes
  because that function writes the new run's `live` claim, which replaces the retired run's.

### The predicate, run over the real tree

Run at HEAD `9024901c`, whose `tools/` bytes equal `018b5675`'s, on 2026-10-05, node `a`, PINNED.
Ten tracked shell files of the kit are not self-tests, holding 358 functions. Four write a terminal
phase:

| function | terminal write | claim write | verdict |
|---|---|---|---|
| `verb_landed` | `LANDED` | yes, both landing modes | pass |
| `verb_abort` | `ABORTED` | yes | pass |
| `verb_preflight` | `LANDED`, on the rotation's scratch copy | yes, the new run's `live` | pass, named above |
| `run_settle` | `LANDED` | none | HIT, the H3 instance |

Near-misses, phase writes the predicate does not grade: `run_hold` (`HELD`), `verb_close`
(`LANDING`), `verb_preflight` (`RUNNING`), `verb_phase` (`$want`) and `run_takeover` (`$hf`). Across
the thirteen self-tests, literal `phase: LANDED` and `phase: ABORTED` lines are `sed` edits of fixture
records, with no `set_fact`. With the self-tests included the count was 760 functions and the same four
writers, so the exclusion changes no verdict today.

### Inventory

| identifier | where | cell |
|---|---|---|
| `TERMINAL_CLAIM_EXEMPT_FNS` | `tools/unattended/check-unattended.sh` | a shell constant, no lexicon cell |
| check `<n>`, 51 at `018b5675` | `tools/unattended/check-unattended.sh` | n/a |
| a local for the branch's claim status | `run_settle` | a shell local, no lexicon cell |
| arms | both self-tests | n/a |

No function, conf key, leg, file or gotcha is minted, so no map key moves. An awk helper the check
defines leads with a table verb, asked first with
`python tools/lexicon/lexicon.py --suggest <name> --as sh.function`, as shared invariant 8 says.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/README.md`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/SKILL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `.claude/skills/unattended/SKILL.md`

The version bump also moves the marker on every other carrier `tools/check-kit-versions.sh`
enumerates. Only `unattended.sh`, `check-unattended.sh`, the two self-tests and the stops template
with its render move beyond that line.

### Rollout

1. Write the check and its five arms. Run the check over the real tree against the driver at the
   pass's parent and observe it red naming `run_settle`, the live instance (AC6). Run the arms as a
   slice and observe each red and green as AC7 states.
2. Write the five driver arms, and observe AC1's and AC2's red halves against the unfixed driver:
   the claim stays `held`, and `live`.
3. Add the status write to `run_settle`. Re-run both slices and the check over the real tree.
4. Edit the stops template's sentence, then re-adopt the rendered guides and the Skill.
5. Bump the unattended version once, last, in every carrier, and re-adopt again.
6. Dispatch the pass declaring every path it writes, then commit through the hook.

### Alternatives rejected

Candidates for the left-shift, each tested against the real tree by the predicate run above.

- **A driver-suite arm that drives every terminal verb and reads the claim.** It grades the verbs it
  names, so a terminal writer added later is never driven and cannot red. That is the instance, not
  the class. The predicate run shows the case: `run_settle` arrived by a merge, and a typed verb list
  written before that merge would not have named it.
- **Writing the claim inside `set_fact` when the key is `phase` and the value terminal.** The
  predicate's own hit list rejects it: `verb_preflight` writes `LANDED` to a scratch copy before the
  rotation's refusals, and a hook there would publish a status for the slug before the verb decided
  anything. `set_fact` also runs before the stage, where every status write is ordered after it.
- **A gotcha class record only.** A gate fits the class (charter §7, left-shift: a gate where one
  fits), and the check costs one awk pass.

For the fix, one candidate was rejected: **a helper shared by the five status-write blocks.** It
moves four landed call sites for a one-site defect, a second mechanism in one unit (M2). It would
also hide `write_claim` behind a name the check would then have to know, where today the predicate
is one token.

## 5. Production-readiness checklist

- security — The claim write already exists on four verbs and takes the same table, CAS and identity
  rules here. It writes only a claim the table admits under the `status` column: a foreign `live`,
  `held` or `unknown` claim is announced and never overwritten. The check reads source only.
- perf / scale — One `read_claims` fetch and at most one push per settle, both bounded by
  `REMOTE_BOUND`. The settle already reads the advertised tip, so the remote is answering. The check
  is one awk pass over ten files, 24 416 lines at `018b5675`, PINNED.
- error / empty / loading states — The switch off writes nothing. A claim the remote does not answer
  for is one `claims not read` line. A write that does not complete is one `claim not written` line.
  Neither fails the settle. The `legacy` branch writes nothing.
- observability — The two announcement lines `write_claim` and `read_claims soft` already print. The
  check's REPORT line of counts.
- risks — A status write that does not complete on the handed branch leaves the claim `held`, which
  never ages, and re-running the settle does not retry it. That is the hands-off edge in §3.
- testing — Five driver arms and five kit-gate arms, each observed red on a staged break before the
  fix or with the check removed. The check is observed red over the real tree against the unfixed
  driver.
- migration — None, PINNED 2026-10-05. `origin/main` at `290d0d2d` carries `run_settle` and no
  `write_claim`, and the remote holds exactly one claim, `refs/gov/runs/aGraftedHelix`, so no settled
  hand-off holds a `held` claim anywhere.
- user docs — The stops guide's section 7 sentence (S3). The verbs entry already points at the stops
  guide for the contract (§8 F3).

## 6. Acceptance criteria

- **AC1** — When the new handed arm runs as a slice of the driver's self-test, meaning its prologue,
  the `--settle` block's fixture with `RUN_CLAIMS="on"` committed in its conf, and the arm, in a
  temp script inside the kit dir: `--handoff tRun` leaves the claim's `status` reading `held`; the
  owner lands the hand-off on the fixture's origin; `--settle tRun`, run under
  `CLAUDE_CODE_SESSION_ID=owner-session`, exits 0 and stages the record at `phase: LANDED`; the
  claim's `status` then reads `landed`, its `keepalive` and `session` are the record's, and
  `--claims` prints the slug with verdict `terminal`. Run against the driver at the pass's parent,
  the claim reads `held` after the settle.
  Red when: the claim reads `held` after the settle, or it names the settler's session.
  fixture: the block's own scratch repository and bare origin; claims are read with
  `git --git-dir=<origin> log -1 --format=%B refs/gov/runs/tRun`.
- **AC2** — When the lease-dead arm runs in the same slice, over the working record `tAwork` leased
  under keepalive `k1`, session `absent`, a `lease-utc` and commit date in 2000 and no live pid, with
  a `live` claim seeded under that keepalive and session and a beat older than the stale bound:
  `--settle tAwork` writes `abandoned`, and the claim's `status` reads `aborted`. Against the driver
  at the pass's parent it reads `live`.
  Red when: the claim stays `live` after the record reads abandoned.
- **AC3** — When the legacy arm runs in the same slice, with a claim seeded for the `ABORTED` record
  `tAkept`, which predates the fixture's `HANDOFF_CUTOFF`: `--settle tAkept` writes `work-landed-at`,
  and `git --git-dir=<origin> rev-parse refs/gov/runs/tAkept` prints the sha it printed before.
  Red when: the settle moved the legacy record's claim (§8 F1).
- **AC4** — When a fresh `live` claim under another session and keepalive is seeded on `tRun` before
  the handed settle: `--settle tRun` exits 0, stages the record at `phase: LANDED`, and prints
  `unattended: claim not written — tRun is held live by session`; the claim ref is unmoved.
  Red when: the settle overwrote the foreign claim, or exited non-zero over it.
- **AC5** — When the handed settle runs in the block's fixture with its conf declaring no
  `RUN_CLAIMS`: `git --git-dir=<origin> for-each-ref refs/gov` prints nothing after the settle.
  Red when: the status write runs outside its `RUN_CLAIMS` guard and creates a claim.
- **AC6** — When `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh --skip 28` runs
  over the real tree with the new check added and `tools/unattended/unattended.sh` at the pass's
  parent, it prints the check's findings failure naming `run_settle()`. At the build commit it
  prints no line of either of the check's failures, no check 48 line naming `run_settle`, and the
  check's REPORT line counts four functions writing a terminal phase and 0 exempt.
  Red when: the unfixed driver passes, or the fixed one still reds.
  figure: PINNED at four writers and ten files, measured at `9024901c` on 2026-10-05.
  cost: 11.7 s for `--skip 28` on node `d` on 2026-08-23, the figure the leg's header records and
  PINNED there; the leg has grown since, and its last bar reading on node `a` was 886 s for the
  whole leg, PINNED from `<git-dir>/gate-ledger.tsv` on 2026-10-05.
- **AC7** — When the kit gate's five new arms run as a slice of its self-test, each over a fixture
  copy of the driver and the leg: a scratch function writing `phase ABORTED` with no `write_claim`
  reds the findings failure naming it; the same function named on `TERMINAL_CLAIM_EXEMPT_FNS` is
  silent; a list entry naming `ghostfn` reds naming `ghostfn()`; every terminal write spelled with a
  quoted `"phase"` key reds the liveness failure; and the shipped driver with the shipped list prints
  neither failure. With the check's block deleted from a staged copy of the leg, the three red arms
  fail.
  Red when: an arm passes against the deleted check, or the control reds.
- **AC8** — When `grep -n -- '--settle' memory/guides/UNATTENDED-STOPS.md` runs at the build commit,
  section 7's status-write sentence names `--settle` with `landed` and `aborted`.
  `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  `git diff <the pass's parent sha> -- tools/unattended/STOPS.template.md` moves line 1 and that
  sentence and nothing else.
  Red when: the render disagrees with the template, or another sentence of the template moved.
- **AC9** — When `bash tools/check-kit-versions.sh` runs at the build commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` reads `clean` for the
  unattended kit. `git diff <the pass's parent sha> -- tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md`
  changes line 1 of each and nothing else.
  Red when: a carrier keeps the old version, or a protocol or verbs sentence moved.
- **AC10** — When `python tools/memory-tree/check-arms.py --check` runs at the build commit it exits
  0, and `grep -c 'check-unattended.sh' tools/unattended/unarmed-branches.txt` prints the count it
  printed at the pass's parent.
  Red when: a new `fail` branch of the check is unarmed, or pinned rather than armed.

## 7. Gates

`unattended kit gate` · `pass-order history` · `brief-recorded` · `unattended skill wiring` · `unattended protocol size` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `check-wiring self-test` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the handed, lease-dead, legacy, foreign-claim and switch-off settles over the `--settle` block's fixture; stage the driver at the pass's parent · the suite's floor rises by the arms' assertion count

New arm: tools/unattended/check-unattended.test.sh · a terminal writer with no claim write, the same on the list, a stale entry, the liveness break and the control; stage the check's block deleted · the suite's floor rises by the arms' assertion count

The unattended suites are not on the bar (`tools/unattended/README.md`), and `check-wiring self-test`
is a held kit leg the re-adopted Skill's guard trips. A pass runs both sets of arms as slices and
AC6's check over the real tree directly, and the main loop runs the suites once at VERIFYING.

## 8. Open questions

- **F1 — Does `--settle`'s `legacy` branch write the claim?**
  Option A writes nothing. Option B writes `aborted` through the `status` column. The record was
  already `ABORTED` and `--abort` wrote its claim then; the settle adds one fact and no phase. B
  rewrites an `aborted` claim to itself, or CREATES one for a run that ended before claims existed,
  since the column's `none` row creates. B's one gain is repairing an `--abort` whose own write did
  not complete, and that claim already ages to `stale` and is taken. A needs no code and keeps the
  write paired with the phase it mirrors.
  RESOLVED (agent, 2026-10-05, delegated): A. AC3 observes the claim unmoved.
- **F2 — Where does the class gate live: the kit gate leg, or an arm of the driver's self-test?**
  The brief and the review say "a class gate in the unattended suite". Option A is a numbered check
  in `tools/unattended/check-unattended.sh`, the `unattended kit gate` leg, which runs on every bar
  with no guard, its arms in the leg's own self-test, beside checks 39, 40 and 48, which already grade
  the driver's source this way. Option B is an arm of the driver's self-test, which is off the bar
  and runs on demand, so a new terminal writer reds only when somebody runs it. Option C is both, one
  predicate in two places, two answers to one question. A reds at the push boundary, which is the
  left-shift's whole purpose, and its arms do sit in a suite of the kit. No veto trips: no new leg,
  dependency or surface.
  RESOLVED (agent, 2026-10-05, delegated): A, with AC6 and AC7 as the observations.
- **F3 — Which governance-carrier lines may this unit move?**
  Shared invariant 10 reserves edits to the protocol, verbs and stops templates. This unit's brief
  names the stops template's section 7 list. Option A moves that sentence and the version marker on
  line 1 of each template, the marker being a derived carrier of the version that unit 27's F3
  ratified the same way. Option B also adds a claim sentence to the verbs template's `--settle` entry,
  for parity with `--hold`, `--landed` and `--abort`. That entry states nothing false without it,
  since it points at the stops guide for the contract, and veto 2 kept TOOL-dAlignedCarrier-7 from
  the same template for the same reason. B trips veto 2; A does not.
  RESOLVED (agent, 2026-10-05, delegated): A, with AC8's and AC9's diffs as the observations.

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the unit's section of the 2026-10-05 spec brief, the
  closing review's H3 with its Fix and Left-shift lines, and the shared brief's invariants. Grounded
  against `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh` and
  `tools/unattended/STOPS.template.md` at `018b5675`. The predicate run and the main-branch probe
  were taken on node `a` the same day.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "assert every function that writes a terminal phase also writes the remote run claim"`
ranked Python name-stem matches only, `run` and `write` first, and printed `unscanned layers: .sh`,
so the shell layer was grepped by hand. Three seams fit, all in this kit, and this unit extends each.
Check 48 in `tools/unattended/check-unattended.sh` is a per-function scanner over the kit's tracked
shell files with a counts-or-announce liveness, and S4 reuses its population array `_c48_files` and
its framing. Check 39 in the same file joins a declared allow-list, `PHASE_RECORDED_FNS`, both ways,
and the exemption list copies that shape. The status-write block in `verb_abort`, `verb_landed` and
`run_hold` is the one S1 copies. Recall agreed with the source on every point but two. The stops
dossier still names the claim refusals 89 and 90, which the closing review's L4 records. Spec 1's S9
lists only three status writers, because `--settle` arrived after it. The review's `:5917-6045` range
for `run_settle` overruns the function, which closes at 6028.

Recall terms used: settle claim status write terminal held landed aborted handoff run_settle write_claim RUN_CLAIMS check 107

The question passed with them: "why does a settled hand-off keep its run claim held, and which verbs
write the claim status at a terminal".

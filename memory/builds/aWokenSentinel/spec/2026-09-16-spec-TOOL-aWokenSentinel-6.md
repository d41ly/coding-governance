# TOOL-aWokenSentinel-6 — the contract: protocol section 5, the Skill, the README, the conf prose and the dossier, with the cron job demoted to the idle-wake

**Status:** CLOSED · rev-4 · 2026-09-21 · node a · Tier-2 · base 5f9648d6 · streams tooling · order 15 · ratified 2026-09-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md](../build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md) | research | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 |
| [2026-09-16-build-TOOL-aWokenSentinel-6-1-acceptance-ledger.md](../build/2026-09-16-build-TOOL-aWokenSentinel-6-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-7 |
| [2026-09-16-prompt-TOOL-aWokenSentinel-6-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-6-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-7 |

<!-- /gen:spec-records -->

## 1. Goal

The protocol's section 5 calls the cron job "the keepalive", splits the obligation between two
actors, and the Skill's `## Resume` says the record cannot be corrected in place — three sentences
units 1 to 5 make false. This unit rewrites every prose carrier of the old shape in one commit so the
contract names the failure-domain rule, the three actors and the mechanisms outside the session,
and stops calling the idle-wake a keepalive, before a reader meets the new mechanisms with the old
words beside them.

## 2. Scope (IN)

- **S1** — `tools/unattended/PROTOCOL.template.md` section 5 rewritten and re-rendered to
  `memory/guides/UNATTENDED-PROTOCOL.md` in the same commit. Its opening sentence is the
  failure-domain rule; it names the IDLE-WAKE (the cron job, scheduled first and reaped last, with
  its verified limits), the KEEPALIVE (the stop-guard, the stall-recorder and the resume tick), the
  three actors, and the absent-owner default with the CONTINUE payload rule, each stated once.
  The file stays under `GUIDE_CAP_BYTES`. Observed by AC1, AC5 and AC7.
- **S2** — `tools/unattended/SKILL.template.md` and its render `.claude/skills/unattended/SKILL.md`:
  the keepalive section becomes the idle-wake section, keeps `--audit` as the tick's prompt and
  adds the absent-owner instruction; `## Resume` replaces "cannot be corrected in place" with
  `--resume <slug> --keepalive-id <id>`; one short new section names the two hooks and the tick
  and points at the kit README's registration line; `## Reap` and `## If it cannot finish` say
  idle-wake where they mean the job. Observed by AC2 and AC5.
- **S3** — `tools/unattended/README.md`: the sidecar layout — `<git-dir>/unattended/`, its three
  kinds `stop`, `stall` and `resume`, and the launcher and `.out` files — written beside unit 5's
  registration section, which this unit does not rewrite. Observed by AC3.
- **S4** — `tools/unattended/VERBS.template.md` and its render `memory/guides/UNATTENDED-VERBS.md`:
  the `--audit` and `--abort` entries say idle-wake where they say keepalive. Observed by AC4 and
  AC5.
- **S5** — `.unattended.conf` and `tools/unattended/.unattended.conf.example`: the `KEEPALIVE_*`
  comments say the job they name is the idle-wake, and each of the four knobs `STOP_GUARD_BLOCKS`,
  `RESUME_STALE_BOUND`, `RESUME_ATTEMPTS` and `RESUME_TURNS` carries a one-line rationale in both
  files. The KEY lines are never this unit's: `RESUME_STALE_BOUND` is unit 2's, `RESUME_ATTEMPTS`
  and `RESUME_TURNS` are unit 5's, `STOP_GUARD_BLOCKS` is `TOOL-aWokenSentinel-10`'s, each with
  its rationale; this unit adds a rationale only where one of them left none, and expects to find
  none absent. A touch of `.unattended.conf` re-stamps `last-audit` in
  `memory/guides/SESSION-KICKOFF.md` in the same commit. Observed by AC6.
- **S6** — `memory/map/features/unattended.md`: the scheduler paragraph rewritten for the hooks
  and the tick, within `DOSSIER_CAP_BYTES`; no claim changes, so no generated map artifact moves.
  The closing "unenforceable by construction" bullet is NOT this unit's: unit 7 rewrites it for the
  `--landed` check it builds, one order later, so one paragraph has one writer and unit 7's
  `prints 0` criterion is 1 at its own base. Observed by AC7.
- **S7** — The sweep: every tracked non-record carrier is grepped for `keepalive` and for
  `cannot be corrected`, and each hit is either rewritten here, or listed in section 3 with the
  reason it stays true or stays out of reach. Observed by AC2 and AC8.

## 3. Non-goals (OUT)

- **No machine-named thing is renamed.** The fact key `keepalive:`, the DoD item
  `keepalive-reaped`, the option `--keepalive-id`, the conf keys `KEEPALIVE_CREATE`,
  `KEEPALIVE_DELETE` and `KEEPALIVE_INTERVAL`, and the kit.toml hole `keepalive-tool-names` keep
  their names: each is a public surface with readers in the driver, the gate, the adopter and
  every landed record, and renaming one is M3's second veto. Section 5 says so in one sentence
  and uses "idle-wake" everywhere prose can.
- **No driver, hook or tick text.** The driver's `fail 51` sentence "a keepalive still auditing
  it" at `tools/unattended/unattended.sh:3010` is a literal an arm asserts and names the job by its
  fact key, which stays true; the stop-guard's block reason and the tick's CONTINUE payload are
  units 3 and 5's code. This unit is prose.
- **No governance carrier.** `memory/guides/BUILD-METHOD.md` M10 reads "the keepalive is yours on
  both ends … Both halves: protocol §5", and after this unit that noun names the idle-wake. It is
  rendered from `tools/memory-tree/BUILD-METHOD.template.md`, is on the kickoff manifest's `watch:`
  line, and is a governance carrier the mandate's delegation does not reach (M3, veto 2). Its
  pointer stays correct; the noun is left for the owner, as a backlog row the close mints. The same
  reasoning keeps `AGENTS.md:147`, `coding-governance-agents.template.md:75` and
  `memory/guides/SESSION-KICKOFF.md:83` untouched: "the keepalive split by actor" and "the
  keepalive precedes orienting" name the topic section 5 still is, and each stays true.
- **Carriers grepped and left, because they stay true.** `skills/session-kickoff/SKILL.md:248`
  names the DoD item; `tools/memory-tree/README.md:233` names section 5's topic;
  `tools/workflows/unattended-build.template.js:66` names what the harness does not cover;
  `tools/push-main.sh:59` is a TCP keepalive; `tools/unattended/kit.toml`'s hole names conf keys;
  the driver's comments name the fact. None says the cron job wakes a stalled run.
- **Carriers that landed after this spec's base, grepped and left.** `tools/unattended/stop-guard.js`,
  `run-lease.js`, `resume-tick.sh`, `check-unattended.sh`, `adopt-unattended.sh`, the five suites
  `unattended.test.sh`, `check-unattended.test.sh`, `adopt-unattended.test.sh`,
  `resume-tick.test.sh` and `cross-component.test.sh`, `tools/workflows/unattended-build.js` and
  `unattended-build.test.sh`, `tools/memory-tree/check-memory-hygiene.sh` and
  `memory/project/readme-contract.txt`: each names
  the fact key, the option, a `KEEPALIVE_*` key, a literal an arm asserts, or the slug
  `aPrimedKeepalive`. Code carriers are units 3 to 5's and 20's; a rename is section 3's first
  bullet. The stop-guard's `landing-unstamped` text says "recorded keepalive id", the fact key.
- **No charter change.** The charter template's `Unattended runs` block points at the protocol and
  does not change.
- **No kit version bump** — the closing pass's, once.
- **No suite runs inside the pass.** The kit gate's parity checks 10 and 22 are observed by `cmp`
  and `awk` over the pairs they compare, and `adopt-unattended.sh --check` compares the five
  installed artifacts in seconds; `check-unattended.sh` itself carries a 16040 s ceiling in the
  leg manifest and runs at the close.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-1` — `--resume <slug> --keepalive-id <id>`, which
  `## Resume` now names; without it the replaced sentence would be replaced by a false one.
- **consumes-from** `TOOL-aWokenSentinel-2` — `--liveness` as the predicate section 5 names for
  every reader, and `RESUME_STALE_BOUND` with its section 8 row.
- **consumes-from** `TOOL-aWokenSentinel-3` — `stop-guard.js`, its sidecar kind `stop` and
  `STOP_GUARD_BLOCKS`; the stop-guard's block reason is the absent-owner instruction the Skill
  quotes.
- **consumes-from** `TOOL-aWokenSentinel-4` — `stall-recorder.js` and the sidecar kind `stall`.
- **consumes-from** `TOOL-aWokenSentinel-5` — `resume-tick.sh`, the README's registration
  section, the sidecar kind `resume` with its launcher and `.out` files, `RESUME_ATTEMPTS` and
  `RESUME_TURNS` with their section 8 rows.
- **consumes-from** `TOOL-aWokenSentinel-10` — the `STOP_GUARD_BLOCKS` line with its rationale in
  both conf files and its section 8 row; without it AC6 finds the key nowhere to locate.
- **hands-off** `TOOL-aWokenSentinel-7` — the sentence in section 5 that `keepalive-reaped` is
  checked at `--landed` against the harness's own listing; this unit writes the actors, unit 7
  writes the check, and section 5 names the check by the verb only. And the dossier's closing
  bullet, "The keepalive half is unenforceable by construction", which unit 7 rewrites and this
  unit leaves byte-identical.
- **hands-off** external — the M10 noun in `tools/memory-tree/BUILD-METHOD.template.md`, a backlog
  row the close mints for the owner.

## 4. Design

### Section 5 of the protocol (S1)

Heading: `## 5. The idle-wake and the keepalive — three actors`. The body, in order, each item one
short paragraph or one bullet, and none restating a unit's mechanism beyond its name and its
trigger:

1. The rule. A mechanism counts as a keepalive only where it does not share the stalled session's
   process, event loop or account — a guard that shares a variable with the thing it guards is not
   a guard. The cron job shares all three, which is why it is demoted rather than fixed.
2. The IDLE-WAKE. The scheduled job the agent creates as the run's first act and reaps last, on
   every start path, unchanged from today; recorded under the `keepalive` fact and attested as
   `keepalive-reaped`, names that stay because a fact key, a DoD item and an option have readers.
   Its limits carry a verified stamp: it fires only while the session is idle (documented,
   2026-09-13), and is owner-reported on 2026-09-13, unmeasured, to stay silent while a background
   task is pending. Its prompt is `--audit`.
3. The KEEPALIVE: what wakes a run from outside its own turn — the stop-guard at every turn end,
   the stall-recorder at every error end, the resume tick from the OS scheduler. One sentence each
   with its trigger and its sidecar kind under `<git-dir>/unattended/`; registration of the tick is
   the owner's, one line per OS in the kit README, and `--check` reports it as INFO.
4. The actors. The AGENT schedules and reaps the idle-wake and, on resume, runs
   `--resume <slug> --keepalive-id <id>` so the lease is re-recorded. The DRIVER records the lease
   (`session:` and `pid:`), grades liveness (`--liveness`), and checks the reap at `--landed`
   against the harness's own listing. The HOOKS and the TICK refuse, record and resume.
5. The absent-owner default, stated once. A session bound to a non-terminal run does not end its
   turn by asking: it runs `--plan` and builds the next READY unit, or aborts with a code. A resumed
   session never parks a question the protocol lets it decide: it takes the option that makes no
   measured observable worse and records why. The CONTINUE payload the tick sends is this rule and
   nothing more; its text lives in the tick.
6. RESUME. Reap the recorded id first, read the result back, schedule the replacement, record it
   with `--resume --keepalive-id`. "Cannot be corrected in place" is gone; the ordering sentence
   stays.

What LEAVES: the two paragraphs recounting that this section said the job dies with the process
"for four kit versions" — `TOOL-aPromptedMandate-11` is cited once in item 2 and git keeps the
narration, the same move `.lexicon.conf` records for its own history. Measured at base: section 5 is
3404 bytes over 44 lines and the file is 60324 of 61440 bytes; units 1, 2, 3 and 5 each add
section 8 rows or a section 2 sentence before this unit, so the byte budget for the rewrite is
DERIVED at build time as `61440 - wc -c` of the template with section 5 cut out, and the pass
trims item text before it trims a carrier: a section 5 that does not fit is shorter, never absent.

The section 8 key table is not this unit's: each knob's row lands with the unit that reads the
key, because check 22 joins the example to the table and a row without its key is the same defect
as a key without its row.

### The Skill (S2)

`## Before any path — schedule the keepalive NOW` becomes `## Before any path — schedule the
idle-wake NOW`. The first paragraph keeps `{{KEEPALIVE_CREATE}}`, `{{KEEPALIVE_INTERVAL}}` and
"keep the id it returns"; "What the tick runs" keeps `--audit` and its `STALLED` remedy and gains
the absent-owner instruction at its end: on a `STALLED` verdict act, and never end the turn by
asking — the owner is absent, and a session bound to a non-terminal run has a stop-guard that will
refuse the stop and say so. The "why it is here" and "if the run never starts" paragraphs are kept
with the noun changed.

A new `## What wakes a stalled run` section, placed directly after it and before `## Which path`,
of at most twelve lines: the stop-guard refuses a turn end while the run is non-terminal, up to
`STOP_GUARD_BLOCKS` times; the stall-recorder writes an API-error end to the `stall` sidecar; the
resume tick, registered by the owner on the OS scheduler, resumes a `STALE` run from another
process; `--liveness <slug>` is the one predicate all three read and the one to run by hand; the
registration line is in the kit README and is not restated here. It names neither `--preflight`
nor `/session-kickoff`, so check 18's ordering does not move.

`## Resume`: the paragraph beginning "The record cannot be corrected in place" is replaced by:
after the reap and the re-schedule, run `bash {{KIT_DIR}}/unattended.sh --resume <slug>
--keepalive-id <id>` with the new id, which re-records `keepalive`, `session` and `pid`, prints
what it replaced and stages the file; the close attestation then covers one job. `## Reap` and
`## If it cannot finish` say "the idle-wake" and name `keepalive-reaped` as the item.

The directive table and the routing section are untouched; checks 24 and the directive join read
them.

### README, VERBS, conf, dossier (S3 to S6)

README: a `## The sidecar` section after unit 5's registration section: `<git-dir>/unattended/` is
the worktree's git dir, never the common dir, because a run lives in one worktree; `stop.<slug>.log`
(one JSON line per stop, unit 3), `stall.<slug>.log` (one line per API-error end, unit 4),
`resume.<slug>.log` with `resume.<slug>.<utc>.sh` and `.out` beside it (unit 5); append-only, never
tracked, read by `--liveness`, `--status`, `--landed` and the tick. No kit path is spelled.

VERBS: `--audit`'s "the keepalive runs it" becomes "the idle-wake runs it"; `--abort`'s "while the
keepalive is still orphaned" becomes "while the idle-wake is still orphaned". Both renders are
re-made by `adopt-unattended.sh`, which copies the verb carrier and the protocol and renders the
Skill and the fixture in one run.

Conf: the `KEEPALIVE_CREATE`/`KEEPALIVE_DELETE` comment gains "the job is the idle-wake; the
keepalive is the hooks and the tick, protocol section 5"; the `KEEPALIVE_INTERVAL` comment says
idle-wake. For the four knobs the pass reads both files and adds a one-line rationale only above a
key that carries none, so a knob unit 2, 5 or 10 documented is not touched twice — and each of
those units declares its key WITH a rationale, so the read is expected to add nothing. Whether
`.unattended.conf` is touched at all is decided by that read and by the `KEEPALIVE_*` comment
edit; when it is, the manifest re-stamp rides in the same commit, and when it is not, the stamp is
not touched.

Dossier: the paragraph beginning "Nothing in a script can reach the scheduler" is rewritten to
name the idle-wake, the three keepalive actors and `--liveness` as the shared predicate. The
closing bullet "The keepalive half is unenforceable by construction" is left byte-identical: unit
7 rewrites it for the check it builds, and two ratified records prescribing two texts for one
paragraph was audit finding M1. Measured at base: 20387 of `DOSSIER_CAP_BYTES` 20480,
ninety-three bytes of headroom, so the rewrite replaces its paragraph at no more than the
original's byte length plus that headroom, and leaves unit 7 headroom it states in its own §4;
the `[claims]` block does not change.

### The sweep (S7)

Before the commit: `git grep -il keepalive -- ':!memory/builds' ':!memory/archive' ':!memory/ledger'
':!memory/LIVE.md' ':!memory/DECISIONS.md' ':!memory/backlog'` and
`git grep -l 'cannot be corrected'` over the same exclusions. Measured at base 2026-09-16: 30 files
carry the first, 2 the second. Every file in the first list is either edited by this unit or named
in section 3 with its reason; the second list is empty after the edit.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `## 5. The idle-wake and the keepalive — three actors` | protocol heading | no cell |
| `## What wakes a stalled run` | Skill heading | no cell |
| `## The sidecar` | README heading | no cell |
| "idle-wake" | the noun for the cron job, prose only | no cell |

No function, key, verb or file is minted.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md` | section 5 rewritten; re-rendered |
| `tools/unattended/SKILL.template.md`, `.claude/skills/unattended/SKILL.md` | three sections edited, one added; re-rendered |
| `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md` | two words; re-rendered |
| `tools/unattended/README.md` | the sidecar section |
| `.unattended.conf`, `tools/unattended/.unattended.conf.example` | comments; rationale where absent |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp, only when the conf moved |
| `memory/map/features/unattended.md` | two paragraphs |

### Alternatives rejected

- Renaming the fact key, the DoD item and the conf keys to match the new noun — section 3.
- Restating the CONTINUE payload and the block reason in the protocol verbatim — three copies of
  one sentence; the protocol states the RULE and the two code carriers state it as text.
- Editing M10 of the build method — section 3.

## 5. Production-readiness checklist

- security — N/A; prose in tracked documents and their renders.
- perf / scale — N/A; one adopter render.
- error / empty / loading states — a section 5 that does not fit the guide cap is shortened, never
  dropped; a dossier rewrite that does not fit its cap is shortened.
- observability — the sweep's two greps are recorded in the commit message with their counts.
- risks — a carrier named in section 3 as "stays true" is a judgment; the sweep lists them so a
  reviewer can disagree with one line each. Every render is byte-compared to its template at the
  close by check 10 and by `--check` now, so a template edited without its render cannot land.
- testing — section 6; greps over the templates and renders, `cmp` over the pairs, `wc -c` against
  the two caps.
- migration — N/A; no record shape changes.
- user docs — this unit IS the user docs of units 1 to 5.

## 6. Acceptance criteria

Each criterion is a grep, a `cmp` or a `wc -c` over a tracked file, seconds; none runs a suite.
The base for the "0 at base" figures is this unit's own pass base, read by `git show <base>:<path>`.

- **AC1** — When `grep -c 'does not share the stalled session'` runs over
  `tools/unattended/PROTOCOL.template.md` and over `memory/guides/UNATTENDED-PROTOCOL.md`, each
  prints 1 and prints 0 at base; `grep -c '^## 5[.] The idle-wake and the keepalive'` prints 1 in
  both; the section 5 region cut by `awk '/^## 5[.] /{f=1;next} f&&/^## /{f=0} f'` carries
  `stop-guard`, `stall-recorder`, `resume-tick`, `--liveness` and `--resume` each at least once,
  `never ends its turn by asking` exactly once (item 5, the one-copy rule every pointer targets),
  `AGENT` and `DRIVER` each at least once (item 4, the actors), each of those three 0 at base, and
  `for four kit versions` zero times.
  Red when: the opening sentence is absent, which means the rule was paraphrased instead of stated;
  a mechanism name is missing, which means an actor was left out; the one-copy rule is absent,
  which leaves the Skill, the stop-guard reason and the tick payload pointing at nothing; or the
  narration survived.
- **AC2** — When `grep -c 'cannot be corrected in place'` runs over `tools/unattended/SKILL.template.md`
  and `.claude/skills/unattended/SKILL.md`, each prints 0 and prints 1 at base; the `## Resume`
  region cut by `awk '/^## Resume/{f=1;next} f&&/^## /{f=0} f'` carries `--resume <slug> --keepalive-id`
  at least once and prints 0 at base; `grep -c '^## What wakes a stalled run'` prints 1 in both files and
  0 at base; `grep -c 'schedule the idle-wake NOW'` prints 1 in both; the `## What wakes a
  stalled run` region, cut by `awk '/^## What wakes a stalled run/{f=1;next} f&&/^## /{f=0} f'`,
  carries `stop-guard`, `stall-recorder`, `resume-tick` and `--liveness` each at least once and
  names neither `--preflight` nor `/session-kickoff`; the `## Reap` region cut the same way
  carries `idle-wake` at least once and 0 at base; and the `## Before any path` region, cut the
  same way, carries `never end the turn by asking` once and 0 at base, the absent-owner sentence
  §4 places at the end of "What the tick runs".
  Red when: the sentence survives in either file, which is the two-answers class; the new section
  names `/session-kickoff`, which moves check 18's first-mention order; the new section's content
  names no mechanism, which is a heading over nothing; or the Reap prose still calls the job the
  keepalive.
- **AC3** — When `grep -c '^## The sidecar' tools/unattended/README.md` runs, it prints 1 and 0 at
  base, and the region below it carries `stop.<slug>.log`, `stall.<slug>.log` and
  `resume.<slug>.log`; `grep -c 'gov-resume-tick' tools/unattended/README.md` is unchanged from
  base, because unit 5's registration section is not rewritten.
  Red when: a kind is missing; or the registration count moved, which means this unit rewrote a
  sibling's section.
- **AC4** — When `grep -c 'the keepalive runs it' tools/unattended/VERBS.template.md` runs, it prints
  0 and prints 1 at base, and `grep -c 'the idle-wake runs it'` prints 1 in the template and in
  `memory/guides/UNATTENDED-VERBS.md`.
  Red when: the template moved and the render did not, which check 10 reds at the close and `cmp`
  sees now.
- **AC5** — When `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md`
  and `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` run, both exit 0,
  and `bash tools/unattended/adopt-unattended.sh --check` exits 0 printing its `in sync` line.
  Red when: any pair drifted, which means a template was edited and the adopter was not re-run.
- **AC6** — When each of `STOP_GUARD_BLOCKS`, `RESUME_STALE_BOUND`, `RESUME_ATTEMPTS` and
  `RESUME_TURNS` is located in `.unattended.conf` and in `tools/unattended/.unattended.conf.example`,
  the line immediately above each key starts with `#`; `grep -c 'idle-wake'` over each file prints
  at least 1 and 0 at base; `grep -c '^STOP_GUARD_BLOCKS='` over each file is unchanged from this
  unit's base, because that line is unit 10's and this unit adds no key; and `git show --stat HEAD`
  lists `memory/guides/SESSION-KICKOFF.md` whenever it lists `.unattended.conf`.
  Red when: a knob carries no rationale line, which means a reader configuring from the file gets a
  bare number; or the conf moved without the stamp, which `kickoff-manifest ratchet` reds at the
  close.
- **AC7** — When `wc -c memory/map/features/unattended.md` runs, it prints at most the
  `DOSSIER_CAP_BYTES` value in `.memory-tree.conf`; `wc -c memory/guides/UNATTENDED-PROTOCOL.md`
  prints at most 61440; `grep -c 'resume tick' memory/map/features/unattended.md` prints at least
  1 and 0 at base; `grep -c 'unenforceable by construction' memory/map/features/unattended.md`
  is unchanged from this unit's base, the closing bullet being unit 7's; and
  `python tools/codebase-map/gen_map.py --check` exits 0, because no claim moved.
  Red when: either file grew past its cap, which `memory hygiene` reds at the close; or the dossier
  was left untouched; or the map check reds, which means a claim moved and a regen is owed.
  figure: both caps are DERIVED at observation, 20480 from `.memory-tree.conf` and 61440 from the
  hygiene gate's default; 20387 and 60324 are the base sizes, PINNED as read on 2026-09-16.
- **AC8** — When the two sweep greps of section 4 run at the tip, `cannot be corrected` matches
  no file, and every file matching `keepalive` is either in the commit's `--stat` or named in
  section 3 of this spec; the commit message carries both counts.
  Red when: a carrier matches, is not in the commit, and is not in section 3 — the
  one-carrier-fixed class `TOOL-dUnstalledConvoy-16` records.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `memory hygiene` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)`

These run once at `--close`. The pass runs none of them: it verifies with the greps, `cmp` and
`wc -c` invocations section 6 names, and `bash tools/unattended/adopt-unattended.sh --check`.
Under `unattended kit gate`, checks 10, 18, 22 and 24 are the joins this unit's files reach.

New arm: none — this unit adds no gate arm; its carriers are graded by the existing parity and
cap checks.

## 8. Open questions

- **F1 — rename the machine names to match the noun, or leave them.** (a) Rename `keepalive:`,
  `keepalive-reaped`, `--keepalive-id` and the three `KEEPALIVE_*` keys to `idle-wake` forms, with
  every reader. (b) Rename nothing machine-named; say once in section 5 that the fact, the item and
  the keys keep their names, and use "idle-wake" in prose. (a) is a public-surface change across
  the driver, the gate, the adopter, every landed record and every adopter's conf.
  Recommendation: (b).
  RESOLVED (agent, 2026-09-16, delegated): (b). (a) is M3's second veto — a change to a public
  surface — and a vetoed option is not the mandate's to take; (b) fails no criterion and leaves one
  sentence of naming debt where a reader meets it.
- **F2 — where the absent-owner instruction lives.** (a) Verbatim in the protocol, the Skill, the
  stop-guard's reason and the tick's payload. (b) The RULE once in section 5; the Skill quotes the
  two verbs and points at it; the two code carriers keep their strings because a hook and a
  scheduler cannot read a guide. Recommendation: (b).
  RESOLVED (agent, 2026-09-16, delegated): (b); (a) is four copies of one sentence with no gate
  over their agreement, the class this unit exists to remove.

## 9. Revision log

- rev-4 · 2026-09-21 · §3 · AC2 · at the build pass: the sweep at the pass base c8aaeb90 found 35
  `keepalive` carriers against the 30 measured at the spec base: the kit README (S3's, edited here)
  and four code and test files units 3 and 5 landed after 2026-09-16, and §3 also lacked a line
  for the test, harness and registry carriers it had folded into "the driver's comments"; §3 now
  names every unedited carrier with the reason it stays. AC2 said the absent-owner sentence sits
  in the region's LAST paragraph while §4 puts it at the end of "What the tick runs", which is not
  last; AC2 now grades the region, and §4 is the placement. AC2's `## Resume` needle was
  `--keepalive-id` with "0 at base", but the paragraph it replaces names that option ("accepted by
  `--preflight` alone"), so it read 1 at both bases; the needle is now the invocation
  `--resume <slug> --keepalive-id`, 0 at base and 1 at the tip. Section 5 was rewritten to 2473 bytes against a derived budget of 2477, which
  brought the render to 61436 under the 61440 cap, so unit 10's curation-debt row for the render
  hid nothing and was drained in the same commit (the registry's stale-row guard reds a row that
  waives a passing file). Status CLOSED.
- rev-3 · 2026-09-20 · §3 · folded at the M4 disposal of spec-audit round 2: the `hands-off` on
  unit 7 gains its reciprocal in spec 7's rev-3 (a check-12 line the round-2 record's M2 paragraph
  reports as seen), and spec 13's rev-2 drops the `hands-off` it declared on this unit for the conf
  comment sentence spec 5 writes (M2, raw 22), so this unit's edge set is unchanged in bytes.
  Order 12 → 15 for the insertions of units 20, 16 and 18.
- rev-2 · 2026-09-20 · S5 · S6 · §3 · §4 · AC1 · AC2 · AC6 · AC7 · folded spec-audit round 1: M1
  (raw 2, 25, 28, 37, 49) — units 6 and 7 both rewrote the dossier's closing bullet, so S6 and §4
  leave it to unit 7 and AC7 asserts it unchanged; M6 (raw 9) — the one-copy absent-owner rule had
  no needle, so AC1 greps item 5 and item 4; M7 (raw 24) — no unit wrote the root conf's
  `STOP_GUARD_BLOCKS` line, so S5, §4 and AC6 name unit 10 as its writer and the edge consumes it;
  L8 (raw 17) — three of S2's Skill edits had no criterion, so AC2 cuts the new section and the
  Reap section and greps them. Order 6 → 12.
- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "state the keepalive obligation by actor in the protocol
and the skill so the two renders agree"` returned only `render_*` symbols from the map, lexicon
and process-monitor kits — no seam, as expected for a prose unit. The seams are the carriers
themselves, cited by line: section 5 at `tools/unattended/PROTOCOL.template.md:370`, the Skill's
keepalive section at `tools/unattended/SKILL.template.md:19` and its `## Resume` at `:714`, the
VERBS entries at `tools/unattended/VERBS.template.md:75` and `:137`, the dossier paragraph at
`memory/map/features/unattended.md:91` and its closing bullet at `:270`, and the adopter that
re-renders all of them. The memory-recall hits `TOOL-aPrimedKeepalive-8` and
`TOOL-aPromptedMandate-11` are the two prior corrections of this same section — the resumed job
is presumed alive, and the attestation is uncheckable — and both are kept as citations in the
rewrite; `TOOL-dUnstalledConvoy-16` is the class the sweep in section 4 guards against. One
disagreement with the brief, settled by measurement: it asks `map_diff.py` to report the dossier
fresh, and that tool attributes a range and reports no freshness; the freshness observation is
`gen_map.py --check`, the byte-compare the map gate itself runs.

Recall terms used: `protocol section 5 keepalive agent obligation actor split driver records reaps resume presumed alive Skill render parity two answers one question`

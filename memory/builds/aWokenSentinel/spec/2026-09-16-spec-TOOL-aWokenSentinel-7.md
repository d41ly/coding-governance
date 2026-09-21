# TOOL-aWokenSentinel-7 — `keepalive-reaped` becomes CHECKED: `--landed` reads the harness's own cron listing

**Status:** CLOSED · rev-6 · 2026-09-21 · node a · Tier-2 · base 5f9648d6 · streams tooling · order 17 · ratified 2026-09-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-aWokenSentinel-7-1-acceptance-ledger.md](../build/2026-09-16-build-TOOL-aWokenSentinel-7-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 |
| [2026-09-16-prompt-TOOL-aWokenSentinel-7-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-7-1-build-brief.md) | journal | — |
| [2026-09-21-prompt-TOOL-aWokenSentinel-5-2-fold-brief.md](../prompts/2026-09-21-prompt-TOOL-aWokenSentinel-5-2-fold-brief.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-12 |
| [2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |

<!-- /gen:spec-records -->

## 1. Goal

`--landed` reads the last stop the stop-guard recorded for the run and refuses when the harness's
own `session_crons` listing still names the recorded `keepalive` id, so the one Definition-of-Done
item nothing could contradict becomes a check against evidence the agent did not write. It closes
`TOOL-aPromptedMandate-11`, open since 2026-08-18, where a run attested the reap twice while
`CronList` showed both jobs firing.

## 2. Scope (IN)

- **S1** — `verb_landed` reads the newest line of the stop sidecar for the slug and, when that line
  was recorded in phase `LANDING` and its `session_crons` value contains the record's `keepalive`
  id, refuses through a new `fail` branch naming the id and the utc the harness listed it at.
  Observed by AC1.
- **S2** — When the sidecar exists but its newest line was recorded in any phase other than
  `LANDING`, `verb_landed` refuses through a second new `fail` branch: the stop-guard records this
  session and no stop after the close exists to check the reap against, so the check could run and
  did not. The refusal names the remedy, which is to end the turn once and re-run the verb — and
  the continuation that remedy promises is `TOOL-aWokenSentinel-8`'s `landing-unstamped` row,
  landed at order 6, which BLOCKS a bound session at `FINISHED-UNSTAMPED` and tells it to re-run
  `--landed`; at base the stop-guard's table ALLOWED that stop and the remedy ended the run
  (audit B1). Observed by AC2 and AC14.
- **S3** — When the newest line was recorded in `LANDING` and does not name the id, `verb_landed`
  proceeds to the anchor observation and prints one `checked` line naming the id and the utc; when
  no sidecar exists, or the record names no `keepalive` id, or (rev-6) the lease names no session,
  it proceeds and prints one `unchecked` line saying why. A pass is never silent. Observed by AC3
  and AC4.
- **S11** — (rev-6) BEFORE the sidecar read, `verb_landed` compares `CLAUDE_CODE_SESSION_ID` with
  the record's `session:` fact: a mismatch, or no id in the environment, refuses through a third
  `fail` branch naming both and `--resume <slug> --keepalive-id <id>` as the step that binds this
  session, never END THE TURN — the stop-guard binds by the lease and records nothing for any
  other session. Observed by AC15.
- **S12** — (rev-6) A newest line whose `utc` is older than the record's `lease-utc` (unit 1) is
  the pre-close case, whatever its phase: a LANDING line the dead incarnation wrote does not pass
  for the one that replaced the lease. Observed by AC16.
- **S4** — RETIRED at rev-2. The recorded keepalive id and what the newest stop-guard line says
  about it is `TOOL-aWokenSentinel-9`'s FIELD on `verb_status`'s existing line, omitted when
  unrecorded; this unit prints no second line and edits `verb_status` not at all, because a second
  stdout line reds the suite's whole-output reader at `unattended.test.sh:1874` and the driver
  header's one-line promise (audit H1). NOT OBSERVED — moved; AC5 observes that this unit leaves
  the line alone.
- **S5** — `dod_met`'s `keepalive-reaped` arm sets `DOD_OUT` on the met path so `--close` announces
  that the attestation is checked at `--landed`, through the existing met-with-something-to-say
  print rather than a new one. Observed by AC6.
- **S6** — Every carrier that calls the item unobservable by a script is corrected in the same
  commit: the protocol's DoD table row, the Skill's close paragraph and its landed section, the
  VERBS entry for `--landed` (the `--status` entry is unit 9's), and the map dossier's closing
  bullet on the keepalive half, which unit 6 leaves byte-identical for this unit; each template
  edit re-renders its output in that commit. The build README's roster row for this unit, written
  at `--rescope` after base and so outside the git-grep-at-base sweep, said `--close` where the
  check is at `--landed`; it was corrected at the audit's disposal on 2026-09-20 and is listed here
  so the sweep's scope names it. Observed by AC7 and AC8.
- **S7** — The backlog row `TOOL-aPromptedMandate-11` moves to `CLOSED` in this unit's commit,
  citing the mechanism. Observed by AC9.
- **S8** — Both new `fail` branches and the two pass shapes get arms in the driver's suite, beside
  the existing `--landed` success arm, each observed red on a staged break before the branch is
  wired, and the suite's floors move by the arms' executed assertions; plus ONE continuation arm
  that drives the documented landing order end to end — the S2 refusal on the `--landed` fixture,
  one `Stop` payload for the fixture's bound session through the real `stop-guard.js` beside the
  real driver, the `landing-unstamped` block, the sidecar line in `LANDING`, and `--landed` re-run
  to `LANDED` with no second turn — so the B1 wedge is a red arm rather than a paragraph. Observed
  by AC10, AC11 and AC14.
- **S9** — This verb reads the sidecar root through `resolve_sidecar_dir`, unit 2's one derivation,
  and spells no `rev-parse --git-dir` of its own; the rule that the driver holds ONE derivation is
  `TOOL-aWokenSentinel-11`'s kit-gate check, landed at order 3, which binds every unit and not
  this pass alone. Observed by AC12.
- **S10** — The match rule for the id inside `session_crons` is verified against a REAL stop-guard
  line where one exists at build time, because the listing's shape is unmeasured and a substring
  rule that never matches the real spelling is a check that cannot fail. Observed by AC13.

## 3. Non-goals (OUT)

- No check at `--abort`. It writes the terminal phase in the same turn as the reap, and no later
  verb of the run exists to read a post-abort stop line. The stop-guard sees that stop and could
  compare the listing on a terminal verdict; that is a change to unit 3's predicate and a follow-up
  under `### Edges`, not this unit.
- No change to the stop-guard's predicate, its continuation reason, or the sidecar's grammar. This
  unit is a READER of unit 3's line and writes nothing under the git dir. The one row that makes
  this unit's remedy true — a bound session at `FINISHED-UNSTAMPED` is blocked and told to run
  `--landed` — is unit 8's, already landed; this unit asserts it in AC14 and does not build it.
- No `--status` edit. The listing field is unit 9's.
- No gate leg reads the sidecar. It is untracked and per-worktree, so a leg in a fresh clone could
  only report DEAD PROBE — the same reason `reuse-probed` is not a leg, protocol section 6.
- No parsing of the `session_crons` value beyond a substring test for the recorded id. Its shape
  is unmeasured (research §6 records presence, not form); the id match is the whole question this
  unit asks, and S10 verifies the rule against a real line before the unit closes. **UNVERIFIED at
  the build** (AC13 deferred: no worktree of this repo held a stop sidecar and this run carries no
  `session:` fact); the first bound landing observes it, and a `0` there amends the rule.
- No new conf knob, no kit version bump (the closing pass's, once), no kickoff-manifest stamp (the
  driver is not a watched path; `.unattended.conf` is not touched).
- No change to `--liveness` (unit 2) or to the CONTINUE payload (unit 5).
- The sentence "no script can reach the store" in protocol section 5, `.unattended.conf` and
  BUILD-METHOD M10 stays true for the WRITE half — no script schedules or reaps — and is not this
  unit's to edit; unit 6 owns section 5, and M10 is a governance carrier. This unit corrects only
  the carriers that say the DoD ITEM cannot be checked, enumerated in §4.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-3` — the stop sidecar `<git-dir>/unattended/stop.<slug>.log`
  and its line grammar: one compact JSON object per line carrying the keys `utc`, `phase` and
  `session_crons`, with `session_crons` the LAST key so a cut from that key to end-of-line is the
  verbatim listing. Without the file every landing reads `unchecked`; without those three key
  spellings the reader matches nothing and refuses every landing as pre-close.
- **consumes-from** `TOOL-aWokenSentinel-2` — the driver's derivation of the sidecar root, which
  that unit introduces to read `stall.<slug>.log`. This verb calls it; S9 forbids a second one.
- **consumes-from** `TOOL-aWokenSentinel-8` — the stop-guard's `landing-unstamped` row: a bound
  session at `FINISHED-UNSTAMPED` is BLOCKED, the listing is recorded in phase `LANDING`, and the
  session is told to re-run `--landed`. Without it every wired landing that follows the documented
  order ends its turn on the S2 remedy and is never continued — the six-records wedge B1 names.
- **consumes-from** `TOOL-aWokenSentinel-6` — section 5's actor sentence, which names this
  unit's check by the verb only and is left for this unit to make true, and the dossier's closing
  bullet unit 6 leaves byte-identical for this unit to rewrite.
- **consumes-from** `TOOL-aWokenSentinel-11` — the kit-gate check that the driver holds one
  `rev-parse --git-dir`; S9's read through the function is what keeps it green.
- **hands-off** `TOOL-aWokenSentinel-9` — the keepalive listing as a field on `--status`'s one
  line, its `none` arm in field form (audit L6), and the `--status` VERBS entry.
- **consumes-from** `TOOL-aWokenSentinel-1` — the `session:` fact that binds a session to the run.
- **consumes-from** `TOOL-aWokenSentinel-17` — `check_status_one_line`, the suite's one-line
  reader over the verb's stdout, which AC5 asserts through; without it AC5's count would be a
  third whole-line reader over merged stderr in the shape that unit retires.
  The stop-guard writes a line only for a bound session, so a record preflighted before unit 1
  landed never gains a sidecar and every landing of it reads `unchecked`, announced.
- **hands-off** external — a listing check inside the stop-guard on a TERMINAL verdict, which would
  cover `--abort` and a close-and-land done in one turn; a backlog row, not a unit here.
- **hands-off** external — measuring the `session_crons` value's shape under a real harness where
  no bound run exists at build time; S10 states the deferral rule.

## 4. Design

### The read, in `verb_landed`

The check sits after the phase gate (check 31) and `check_clean`, and BEFORE `observe_anchor`
(`tools/unattended/unattended.sh:2354` opens the verb at base 5f9648d6; the lines move). It is a
local file read against a remote round-trip, which is the ordering rule the verb's own
lander-marker comment states; and a refusal here leaves the record at `LANDING`, repairable by the
remedy the refusal names, because the terminal writes sit last.

One helper, `read_stop_listing` (cell `sh.function`, verb `read`, confirmed by `--suggest`), takes
the slug and prints three fields or nothing: the newest line's `utc`, its `phase`, and its
`session_crons` value. It resolves the sidecar root through unit 2's derivation, takes `tail -n 1`
of `stop.<slug>.log` with the CR stripped, and reads each field by KEY, never by position:
`"utc":"…"` and `"phase":"…"` through `grep -o` on the quoted key, and the listing as everything
after the literal `"session_crons":` — the cut that needs unit 3 to write that key last. A missing
file prints nothing and returns 1; an empty file is the same. A line whose `phase` cannot be read
prints `(unreadable)` as the phase, so the caller treats it as pre-close and the refusal shows what
it saw rather than passing a line it could not parse.

The verb then decides, in this order, with `kid=$(fact "$rel" keepalive)`:

| state | outcome |
|---|---|
| `kid` empty | proceed; print `unattended: keepalive-reaped: attested, unchecked — the record names no keepalive id` |
| `session` fact empty or `absent` (rev-6) | proceed; print `unattended: keepalive-reaped: attested, unchecked — the lease names no session (the harness exposed none), so the stop-guard never bound this run and recorded no stop of it` |
| `CLAUDE_CODE_SESSION_ID` is not the `session` fact (rev-6) | refuse, `fail 55` |
| no sidecar, or empty | proceed; print `unattended: keepalive-reaped: attested, unchecked — no stop-guard record for this run (the hook is not wired, or the session was never bound)` |
| newest line's `utc` older than `lease-utc` (rev-6) | the phase reads `<phase>, older than the lease taken at <lease-utc>` and takes the row below |
| newest line's phase is not `LANDING` | refuse, second new `fail` number |
| newest line's listing contains `kid` (`grep -qF`) | refuse, first new `fail` number |
| newest line's listing does not contain `kid` | proceed; print `unattended: keepalive-reaped: checked — <kid> absent from the harness listing at <utc>` |

Why the line's own `phase` field decides "after the close" and not a clock: the record carries no
timestamp for a phase change, so a clock comparison would mean reading the LANDING commit's
committer date and parsing the line's ISO utc with `date -d` — a second clock with its own failure
mode. `--close` is the sole writer of `LANDING` — S9 of `TOOL-cFinalBerth-1`
(`memory/builds/cFinalBerth/spec/2026-08-13-spec-cFinalBerth-1.md`, the driver's branch comment
at `unattended.sh:2312` is that S9), with the staging fix `TOOL-aBoundedVerdict-15` cites at
`:2324` — and `--landed` is the sole writer of `LANDED`, so a stop recorded in `LANDING` is by
construction a stop between the two, and the field is already on the line.

The two refusal texts, literal head first so `check-arms.py` can arm them, `<…>` interpolated:

- `the keepalive attestation is contradicted by the harness's own listing: the stop-guard recorded
  the cron store after the close and it still names the recorded keepalive id, so the job was not
  reaped — reap it, END THE TURN so the stop-guard records the listing again, then re-run --landed:
  <kid> listed at <utc>`
- `the stop-guard records this session and no stop after the close exists to check the reap
  against, so the attestation could be checked and was not — END THE TURN once (the stop-guard
  records the listing and continues you), then re-run --landed; if no record appears afterwards
  the hook is unwired and adopt-unattended.sh --check says so: newest stop-guard record <utc> in
  phase <phase>`

The `fail` numbers are the next two free in the driver at build time, read with
`grep -oE 'fail [0-9]+' tools/unattended/unattended.sh | sort -k2 -n | tail -1`; the high-water is 51
at base 5f9648d6 and units 1 to 5 take numbers before this one runs, so no number is pinned here.
Taken at the build, high-water 52: **53** for the listed id and **54** for the pre-close line. The
rev-6 fold took **55** for the unbound session, derived the same way at high-water 54:
`the stop-guard binds by the lease and this session is not the one the record names, so no stop of
this session is ever recorded and ending the turn cannot help — run --resume <slug> --keepalive-id
<the idle-wake id you schedule now> so the lease names this session and the stop-guard records it,
then re-run --landed: lease session <sid>, this session <id|unset>`.

Why the second refusal exists rather than the brief's `unchecked` pass: the Skill never mandates a
turn boundary between `--close` and `--landed`, and the ordinary landing runs attest, close, commit,
lander and `--landed` in ONE turn. Under a pass-on-older-line rule the check would fire only when a
turn happened to end between the two, which is by accident, and `TOOL-aPromptedMandate-11` would
not honestly close. Requiring the post-close line costs one stop-guard block per landing — and
that block is `TOOL-aWokenSentinel-8`'s `landing-unstamped` row, not an assumption about unit 3:
after the lander the witness is on `origin/<default>`, `--liveness` reads `FINISHED-UNSTAMPED`
(spec 2 S3), and at base spec 3's table ALLOWED that stop, so the turn ended and nothing continued
the session (audit B1, raw 18, 29, 43). Unit 8 makes the row a bounded BLOCK whose reason names
`--landed`; the stop-guard records the listing, continues the session, and the re-run reads the
post-close line. The refusal fires only where the sidecar already exists, so an adopter without
the hook, or a session never bound, is never wedged; a reap the harness never reflects ends in
`blocks-exhausted`, announced, after `STOP_GUARD_BLOCKS` blocks. The fork and its M3 derivation
are §8; AC14 is the arm.

What it does NOT check, said in the verb's header comment: whether the job named by `keepalive`
was ever the run's job, whether a job under another id is still firing, or anything about a stop
the hook did not record. It reads one line the harness populated and compares one id. What it DOES
check from rev-6, because the header used to claim the opposite: that the session running the verb
is the leased one (the header said "a session never bound … is never wedged", and it was, on a
false "the hook is unwired" diagnosis — closing review ids 7 and 11), and that the newest line is
younger than the lease (id 15). A record with no `lease-utc` takes the newest line whoever wrote it.

### `--status` and `--close`

`verb_status` is not edited by this unit. The listing reaches the operator as
`TOOL-aWokenSentinel-9`'s field on the existing status line — ` · keepalive <kid> <present|absent>
in the harness listing at <utc>`, omitted when nothing is recorded — built from this unit's
`read_stop_listing` and the same `grep -qF`, one order later. A second stdout line was this unit's
rev-1 shape and reds the suite's `:1874` whole-output reader on every fixture (audit H1).

`dod_met`'s `keepalive-reaped` arm (`tools/unattended/unattended.sh:3909` at base) keeps its
predicate and gains one line on the met path: `DOD_OUT="keepalive-reaped: attested; checked at
--landed against the stop-guard's last harness listing"`. `verb_close` already prints
`unattended: $DOD_OUT` for a met item with something to say, so the row reaches the operator
through the existing branch and no new print is added.

### The carriers

Derived by `git grep -l keepalive-reaped` over the live tree at base, plus the dossier sentence
found by `git grep -i 'unenforceable by construction'`:

| carrier | edit | render, same commit |
|---|---|---|
| `tools/unattended/PROTOCOL.template.md` DoD table, the `keepalive-reaped` row | `agent-attested` stays; the description gains: checked at `--landed` against the stop-guard's newest listing, refused when the id is still listed, announced `unchecked` where no record exists | `memory/guides/UNATTENDED-PROTOCOL.md` |
| `tools/unattended/SKILL.template.md`, the close paragraph "Two of them are yours to attest, because no script can observe them" | one of them is READ BACK: the stop-guard records the harness's listing at every stop and `--landed` refuses when your id is still in it; the landed section gains the end-the-turn remedy | `.claude/skills/unattended/SKILL.md` |
| `tools/unattended/VERBS.template.md`, the `--landed` entry | the listing check and its two refusals; the `--status` entry is unit 9's | `memory/guides/UNATTENDED-VERBS.md` |
| `memory/map/features/unattended.md`, "The keepalive half is unenforceable by construction" | the reap is checked at `--landed` where the stop-guard is wired; the schedule half stays agent-only. Unit 6 leaves this bullet byte-identical (its S6 at rev-2), so this unit is its one writer and the sentence is present at this unit's own base | none, the dossier is authored; `python tools/codebase-map/gen_map.py --check` is the freshness observation — `map_diff.py` attributes a range and reports no freshness |
| `memory/builds/aWokenSentinel/README.md`, roster row 7 | said CHECKED at `--close`; corrected to `--landed` at the audit's disposal, 2026-09-20, outside the pass | none |
| `memory/backlog/TOOL.md`, `TOOL-aPromptedMandate-11` | `OPEN` → `CLOSED`, with the mechanism named | none |

The render command is `bash tools/unattended/adopt-unattended.sh`; the parity legs byte-compare
template and render, which is why the render is in the commit and not a follow-up.

### The fixture

The suite's `--landed` success arm (region two, `git push -q -f origin HEAD:main` then
`git checkout -q -B main HEAD`) is the base fixture, because a refusal is attributable only on a
fixture that would otherwise land. One trap the arms must handle: `reset_tree` runs `git clean -qfd`,
which never reaches the git dir, so a stop log written by one arm survives into the next. Every new
arm starts with `rm -f` of the sidecar file and the last one removes it, so the existing `--landed`
arms downstream keep reading `unchecked`. The stop lines are written by `printf`, one compact JSON
object each, with `session_crons` last, for example
`{"utc":"2026-09-16T12:00:00Z","phase":"LANDING","session_crons":[{"id":"k1"}]}` — the shape is
this unit's fixture and not a claim about the harness, which S10 covers.

The continuation arm (S8, AC14) writes no stop line by hand. On the `--landed` fixture with a
pre-close line present it runs `--landed`, reads the S2 refusal, then feeds one `Stop` payload —
`session_id` equal to the fixture record's `session:` fact, which is the prologue's
`fixture-session` from unit 1, `cwd` the fixture root — to the REAL `stop-guard.js` under
`tools/unattended/` with the real driver beside it, so the hook binds, spawns `--liveness tRun`,
reads `FINISHED-UNSTAMPED` (the fixture's witness is on the fixture `origin/main`), takes unit 8's
row, and writes the `LANDING` line itself with the payload's `session_crons`; the arm then re-runs
`--landed` and reads `phase LANDED`. It is the one arm in the suite that runs the hook, and it
needs `node`, which every registered node has for `gate-guard.js`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `read_stop_listing` | shell function in the driver | `sh.function`, verb `read`, snake — `--suggest` says OK |
| two `fail <n>` numbers | refusal branches | derived at build time, next free above the high-water |

No conf key, no verb, no file under the kit dir.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.sh` | `read_stop_listing`; `verb_landed` check and two refusals; `dod_met` `DOD_OUT` |
| `tools/unattended/unattended.test.sh` | the arms of AC1 to AC4, AC6, AC10 and AC14; floors of AC11 |
| `tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` | DoD row |
| `tools/unattended/SKILL.template.md` · `.claude/skills/unattended/SKILL.md` | close paragraph, landed section |
| `tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md` | the `--landed` entry |
| `memory/map/features/unattended.md` | one paragraph |
| `memory/backlog/TOOL.md` | one row's status |

### Alternatives rejected

- **Record the delete's return beside the id** (the round-2 spec audit of `aPrimedKeepalive`, its
  remedy for this row). Still the agent reporting its own act with more words; the harness's
  `session_crons` is the first evidence the agent did not write.
- **Check at `--close`.** The stop that records the post-reap listing ends the turn `--close` runs
  in, so the listing does not exist yet — the brief's own reason for `--landed`.
- **Check inside the stop-guard on a terminal verdict.** Covers more, including `--abort` and a
  one-turn landing, but it is unit 3's predicate and a terminal stop has nobody left to act on a
  refusal; a follow-up, named under `### Edges`.
- **A clock comparison** for "after the close": needs `date -d`, a second clock and a commit
  lookup; the line's own `phase` is the same fact for free.
- **Parse the JSON with the resolved python.** `--landed` needs no python today and an adopter's
  landing would start needing one for a three-key read of a line this kit's own hook wrote.
- **Refuse on a pre-close line only when the sidecar is non-empty** was considered as a softer
  form of S2 and is what S2 is: the file's presence proves the hook is wired and the session was
  bound, so the refusal never wedges a run that could not have produced the line.

## 5. Production-readiness checklist

- security: the sidecar sits under the git dir and is written by a hook the adopter wired. A
  forged line naming the id makes the check STRICTER; a forged line omitting it fakes a pass at
  the same trust level as today's attestation, since the agent that would forge it could attest
  falsely already. No new write surface; the driver never writes the sidecar.
- perf / scale: one `tail -n 1` and three `grep` calls per `--landed` and per `--status`; nothing
  measurable.
- error / empty / loading states: no file, empty file, and no `keepalive` fact each print an
  announced `unchecked`; an unreadable phase refuses through S2 and shows `(unreadable)`; a refusal
  writes nothing, which the arms assert with `sum` before and after.
- observability: every outcome prints one line naming the id, the utc and the phase it read; the
  two refusals name the remedy and the `--check` that reports an unwired hook.
- risks: the real `session_crons` spelling of an id is unmeasured, so the substring rule could miss
  — S10 and AC13; a hook unwired mid-run wedges `--landed` at S2 until re-wired, and the refusal
  names `adopt-unattended.sh --check`; an adopter without the stop-guard reads `unchecked` forever,
  announced on every landing.
- testing: the arms of §7, each observed red on a staged break; floors move by executed
  assertions, AC11.
- migration: none. An older record without `keepalive`, or one preflighted before unit 1, reads
  `unchecked` with the reason; no conf key is added; no existing arm changes its assertion.
- user docs: the Skill, the protocol, the VERBS file and the dossier, §4's carrier table; the kit
  README does not name the item and is untouched.

## 6. Acceptance criteria

The driver's suite is on no bar leg (the 2026-08-23 ruling in the kit descriptor) and the build's
own rule keeps it out of the pass, so each criterion is observed by running the driver over the
suite's fixture in a scratch clone the way its arm does; the arms exist so `harness arms (fail
branches armed or pinned)` counts them at the close. The fixture is the suite's `tRun` build at its
`--landed` success shape: `reset_tree`, `run --preflight tRun --keepalive-id k1`, phase set to
`LANDING`, `fixture`, the push to the fixture origin and `git checkout -q -B main HEAD`, then a stop
log written by `printf` under the fixture's git dir as §4 shows, removed with `rm -f` before and
after.

- **AC1** — When the newest stop line reads phase `LANDING` and its `session_crons` contains `k1`,
  stamped at or after the record's `lease-utc` (rev-6; a stamp older than the lease is AC16's
  refusal), `run --landed tRun` prints a line beginning `the keepalive attestation is contradicted
  by the harness's own listing` and ending `k1 listed at <that stamp>`, the phase stays `LANDING`,
  and `sum` is unchanged.
  Red when: the verb reaches `phase LANDED`, which means the read was skipped or the listing cut
  missed the key; or the refusal names no id or no utc.
  fixture: the suite's own scratch repo and a hand-written stop line; no live fixture in this tree.
- **AC2** — When the newest stop line reads phase `BUILDING` on the same fixture, `run --landed
  tRun` prints a line beginning `the stop-guard records this session and no stop after the close
  exists to check the reap against` and ending `in phase BUILDING`, and `sum` is unchanged; when
  the newest line carries no `phase` key at all, the same refusal ends `in phase (unreadable)`.
  Red when: the verb lands, which means an older line was read as post-close; or the unreadable
  line passes, which means a line the reader cannot parse was treated as evidence.
- **AC3** — When the newest stop line reads phase `LANDING` and its `session_crons` is `[]`,
  stamped at or after `lease-utc` (rev-6), `run --landed tRun` prints `keepalive-reaped: checked
  — k1 absent from the harness listing at <that stamp>` and then `phase LANDED`, and the record's
  `landed-anchor` reads `remote`.
  Red when: no `checked` line prints while the phase still moves, which is the silent pass this
  unit forbids; or the check refuses on an empty listing.
- **AC4** — When no stop log exists for the slug, `run --landed tRun` prints `keepalive-reaped:
  attested, unchecked — no stop-guard record for this run` and then `phase LANDED`; when the log
  is absent and the record's `keepalive` line is deleted with `sed -i '/^keepalive: /d'`, it prints
  `keepalive-reaped: attested, unchecked — the record names no keepalive id` and lands.
  Red when: the verb refuses on a missing file, which would wedge every adopter without the hook;
  or lands with no `unchecked` line.
- **AC5** — When `check_status_one_line tRun` runs on the three fixtures of AC1, AC3 and AC4, its
  `same` passes with `1` — the helper unit 17 lands one order before this unit, which counts the
  verb's stdout alone and drops the stderr NOTEs a conf declaring no bound makes the driver print —
  and the line it prints is byte-identical to what the driver at this unit's base prints on the
  same fixture, compared with `cmp` over the two outputs.
  Red when: a second line prints, which reds the `:1874` whole-output reader on every fixture; or
  the line changed, which is this unit editing a verb unit 9 owns; or the count is taken over
  `run`'s merged output with `wc -l`, which is a test of the fixture's conf and not of the verb
  (spec 17 §4) and reads an empty output as one line.
- **AC6** — When `run --close tRun` runs on the suite's close-success fixture with
  `keepalive-reaped: yes` attested, its output carries `unattended: keepalive-reaped: attested;
  checked at --landed against the stop-guard's last harness listing` and still ends `close OK`.
  Red when: the line is absent, which means `DOD_OUT` was set on the unmet path or not at all; or
  the close blocks, which means the predicate moved.
- **AC7** — When the pass finishes, `grep -c 'checked at --landed' tools/unattended/PROTOCOL.template.md`
  and the same grep over `memory/guides/UNATTENDED-PROTOCOL.md` both print 1;
  `grep -c 'no script can observe them' tools/unattended/SKILL.template.md` and over
  `.claude/skills/unattended/SKILL.md` both print 0; `grep -c 'harness listing'
  tools/unattended/VERBS.template.md` and over `memory/guides/UNATTENDED-VERBS.md` print the same
  non-zero count; `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: a template count and its render's count differ, which is the parity defect the same
  commit exists to prevent; or the refuted sentence survives in either Skill file.
- **AC8** — When the pass finishes, `grep -c 'unenforceable by construction'
  memory/map/features/unattended.md` prints 0 and prints 1 at this unit's own base, because unit
  6 leaves the bullet to this unit; `grep -c 'checked at' memory/map/features/unattended.md`
  prints at least 1 and 0 at this unit's base; `wc -c memory/map/features/unattended.md` prints at
  most the `DOSSIER_CAP_BYTES` value in `.memory-tree.conf`; and
  `python tools/codebase-map/gen_map.py --check` exits 0.
  Red when: the sentence survives; the positive needle is absent, which is the bullet deleted
  rather than rewritten; the dossier grew past its cap; or the map check reds, which means a claim
  moved. A `prints 0` that already held at this unit's base would be a criterion that cannot fail,
  which is why the base value is stated as 1 and derived from unit 6's rev-2 S6.
  figure: the cap is DERIVED at observation from `.memory-tree.conf`; 1 at base is DERIVED from
  spec 6 S6 at rev-2 and checked by `git show <base>:memory/map/features/unattended.md`.
- **AC9** — When the pass finishes, `grep -c 'TOOL-aPromptedMandate-11 · CLOSED' memory/backlog/TOOL.md`
  prints 1 and `grep -c 'TOOL-aPromptedMandate-11 · OPEN'` over the same file prints 0.
  Red when: the row is still `OPEN`, or a second row was added instead of the one being moved.
- **AC10** — When each of the two refusal literals is staged OUT of `tools/unattended/unattended.sh`
  by commenting its `fail` line, the arm that names it goes red in the scratch clone, and goes green
  with the line restored; `python tools/memory-tree/check-arms.py --report`, filtered to the driver,
  lists both new branches as armed.
  Red when: an arm stays green with its branch commented out, which is an arm about nothing; or the
  report lists a new branch as unarmed.
  fixture: the scratch clone the pass builds under a short `%TEMP%` path, never this worktree.
- **AC11** — When the arms are in place, `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` in the driver's
  suite each rise by the arms' executed assertion count, and `FLOOR_SHARD_1` does not move; the
  count is DERIVED at the close from the suite's own summary.
  Red when: a floor is left where it was, which lets a later deletion of these arms pass silently.
  figure: DERIVED at the close; the floors sit at `unattended.test.sh:5721` and
  `unattended.test.sh:5765` at base 5f9648d6 and move.
  permission: the executed count is the suite's, which the close runs and the pass does not; the
  pass counts its `hit`, `miss` and `same` calls and the ledger row says `count confirmed at
  --close`.
- **AC12** — When the pass finishes, `grep -c 'rev-parse --git-dir' tools/unattended/unattended.sh`
  is unchanged from this unit's own order base, and `grep -c 'resolve_sidecar_dir' tools/unattended/unattended.sh`
  is one higher than at that base — this verb's call.
  Red when: the first count moved, which means this unit spelled a second sidecar-root derivation
  and unit 11's kit-gate check reds at the close; or the second did not, which means the verb reads
  the sidecar some other way.
  figure: DERIVED at observation against this unit's order base; the count-is-one rule itself is
  unit 11's check and not pinned here.
- **AC13** — When a stop-guard line exists for a BOUND run in any worktree of this repo at build
  time — this run's own `stop.aWokenSentinel.log` if the run re-bound its session after unit 1,
  else none — `grep -c` of that run's recorded `keepalive` id over the newest line prints 1 while
  the job is scheduled, confirming the harness spells the id as the `keepalive` fact does.
  Red when: it prints 0 while the job is listed by the harness, which means the substring rule
  misses the real spelling and §4's match rule is amended before the unit closes.
  fixture: none is guaranteed in this tree — this run was preflighted before unit 1 landed and
  carries no `session:` fact. Where no bound run exists, the ledger row reads `deferred: no bound
  run at build time`, the assumption stays marked UNVERIFIED in §4, and the first bound landing
  observes it.
- **AC14** — When, on the `--landed` fixture with a stop line in phase `BUILDING` present,
  `run --landed tRun` prints the S2 refusal, then one `Stop` payload with `session_id`
  `fixture-session` and `cwd` the fixture root is fed to `node stop-guard.js` from
  `tools/unattended/` with the real driver beside it, the hook prints one JSON object with
  `decision` `block` and a `reason` carrying `landing-unstamped`'s text — `finished and
  unstamped` and `--landed` — the sidecar's newest line has `phase` `LANDING` and `session_crons`
  deep-equal to the payload's, and a second `run --landed tRun` prints `keepalive-reaped: checked`
  and `phase LANDED`. Observed RED first against a hook copy with unit 8's row reverted to allow,
  where the record stays at `LANDING`.
  Red when: the hook allows the stop, which is the wedge B1 names, manufactured by this unit's
  remedy; the second `--landed` still refuses on a pre-close line, which means the hook wrote no
  `LANDING` line or wrote it with another phase; or the hook does not bind, which means the
  fixture's `session:` fact and the payload's `session_id` disagree.
  fixture: the suite's `--landed` success fixture with the prologue's `fixture-session` lease from
  unit 1 and the fixture `origin`; `node` on `PATH`, as `gate-guard.js` already requires.
  cost: one driver spawn from inside the hook, seconds.
- **AC15** — When the `--landed` fixture holds a pre-close `BUILDING` stop line and the verb runs
  with `CLAUDE_CODE_SESSION_ID=some-other-session`, it exits 1 printing a line beginning `the
  stop-guard binds by the lease and this session is not the one the record names` and ending
  `lease session fixture-session, this session some-other-session`, with no `END THE TURN` and
  `sum` unchanged; with the variable unset the same refusal ends `this session unset`; and with
  the record's `session:` rewritten to `absent` the verb prints `keepalive-reaped: attested,
  unchecked — the lease names no session (the harness exposed none)` and lands.
  Red when: the unbound session reaches check 54 and END THE TURN, which is the loop a takeover
  session sat in; or an `absent` lease is refused, which wedges every harness exposing no id.
- **AC16** — When the `--landed` fixture holds a LANDING `[]` stop line stamped now, the lease is
  replaced one second later by `--resume tRun --keepalive-id k2` and committed, `run --landed
  tRun` refuses through check 54 with `newest stop-guard record <that stamp> in phase LANDING,
  older than the lease taken at <lease-utc>`, no `phase LANDED`, `sum` unchanged.
  Red when: the line passes as `checked` and the record lands, which is the dead incarnation's
  witness graded for the new one.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `hook destinations (every declared hook path ships)`

These are what `--close` runs, once, on the whole bar. The pass runs none of them: it verifies with
the driver invocations §6 names over a scratch clone, the greps of AC7 to AC9 and AC12, and
`check-arms.py --report` filtered to the driver, which is the meta-gate's report mode and not its
leg. Under `unattended kit gate`, the protocol-render parity check is the join this unit moves;
under `unattended skill wiring`, the Skill render.

New arm: `tools/unattended/unattended.test.sh` · the two new refusals, each observed by the fixture
of AC1 and AC2 with its `fail` line commented out before the arm is trusted, plus the `checked`,
`unchecked` and no-id passes of AC3 and AC4, the one-line `--status` assertion of AC5 through
`check_status_one_line`, the
`--close` row of AC6, and the continuation arm of AC14 through the real hook with unit 8's row
reverted as its break · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the executed count, AC11;
`FLOOR_SHARD_1` does not move.

## 8. Open questions

- **A pre-close newest line: pass as `unchecked`, or refuse until a post-close line exists?** The
  brief says pass and print `unchecked`. Options: (B1) pass, the brief's shape — the check fires
  only when a turn happens to end between `--close` and `--landed`, which the Skill never mandates,
  so the ordinary one-turn landing is never checked and the backlog row does not honestly close;
  (B2) refuse when the sidecar exists and its newest line predates the close, naming the remedy —
  every wired, bound landing is checked, at the cost of one stop-guard block per landing, and a
  run with no sidecar is never wedged. M3: B2 satisfies more of the unit's stated goal and leaves
  fewer follow-ups; veto 1, no acceptance criterion or non-goal is violated; veto 2, no new
  dependency, surface or governance-carrier change beyond the carrier edits both options make;
  veto 3, no widened write surface, the driver reads only. Recommendation B2.
  RESOLVED (agent, 2026-09-16, delegated): B2, as S2 and AC2 state; the run-state file names the
  mandate (`mode: prompt`, `authorized-by: prompt`) and M3 delegates the forks the build's specs
  state. The spec audit may refute the derivation; the record of it is here.
  AMENDED at rev-2 (agent, 2026-09-20, delegated): the audit did not refute B2, it refuted B2's
  PREMISE — that the stop-guard refuses a `LANDING` record's stop — which was asserted here and
  contradicted by spec 3's `FINISHED-UNSTAMPED → allow` row (B1, raw 18, 29, 43). B2 stands;
  the premise is now `TOOL-aWokenSentinel-8`'s row, consumed by this unit and asserted by AC14.

## 9. Revision log

- rev-6 · 2026-09-21 · S3 · S11 · S12 · §4 · AC1 · AC3 · AC15 · AC16 · folded the closing diff review round 1
  (`reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md`), ids 7, 11 and 15: fail 54's remedy
  assumed the running session was the leased one, so an unbound takeover session looped on END
  THE TURN with a false "hook is unwired" diagnosis (7 and 11, one defect) — `fail 55` refuses it
  first with `--resume --keepalive-id` as the step; and `read_stop_listing` took the newest line
  whoever wrote it, so a dead incarnation's LANDING line passed check 53 against the id the new
  lease replaced (15) — a line older than `lease-utc` is the pre-close case. The header sentence
  that claimed an unbound session is never wedged is corrected; the NOT CHECKED list names what is
  now checked. Class `witness-graded-against-a-fact-written-after-it`. Status unchanged, CLOSED.
- rev-5 · 2026-09-21 · §4 · §3 · status · the build pass: the two `fail` numbers taken (53, 54); the
  `session_crons` match rule marked UNVERIFIED with AC13's deferral, since no bound run existed at
  build time. Two carrier edits diverged from §4's table for BYTE CAPS the table did not price: the
  protocol render sat at 61436 B against `GUIDE_CAP_BYTES` 61440, so the DoD row's +150 B is paid
  for by dropping the attestation-verb paragraph's history sentence ("Before it existed the keys
  had no writer …", −184 B; git holds it), 61402 B after; the dossier sat at 20473 B against
  `DOSSIER_CAP_BYTES` 20480, so the bullet is 247 B for 241, 20479 after. The dispatch was
  declared without `memory/LIVE.md` and `memory/ledger`, which check 49 reserves to unit 16's never-
  written rows, as every sibling since unit 16 did. CLOSED.
- rev-4 · 2026-09-20 · §3 · AC5 · §7 · folded spec-audit round 3 M6 (raw 23, 41): AC5 counted
  `run --status` output with `wc -l` over merged stderr, a third whole-line reader one order before
  the unit that retires that shape, so it now asserts through `check_status_one_line` with a
  `consumes-from` on unit 17 and §7's arm line names the helper. Order 16 → 17, swapped with unit
  17 so the helper exists when the arm is written.
- rev-3 · 2026-09-20 · §3 · folded at the M4 disposal of spec-audit round 2: one check-12 line
  the round-2 record's M2 paragraph reports as seen on the full hygiene run at 12513c25 — spec 6
  declares `hands-off` this unit and this unit declared no `consumes-from` back, so the edge is
  declared with what this unit takes. The `--landed` check-34 predicate this unit's verb sits
  beside is `TOOL-aWokenSentinel-16`'s at order 7, sequenced before this unit; AC14's fixture is
  the fast-forward shape and is unmoved by it. Order 13 → 16 for the insertions of units 20, 16
  and 18.
- rev-2 · 2026-09-20 · S2 · S4 · S6 · S8 · S9 · §3 · §4 · AC5 · AC8 · AC12 · AC14 · §7 · §8 · §10
  · folded spec-audit round 1: M1 (raw 2, 25, 28, 37, 49) — AC8 could not fail and two units
  wrote one dossier bullet, so unit 6 leaves the bullet to this unit, AC8 states the base value as
  1 with a positive needle and `gen_map.py --check` as the freshness observation; L6 (raw 15) —
  the `none` arm of the listing grammar is unit 9's in field form, routed by the S4 retirement;
  L10 (raw 50) — the LANDING-is-close-only rule is cited to `TOOL-cFinalBerth-1` S9; L11 (raw 52)
  — `RUN.md:30`; L12 (raw 53) — the roster row corrected to `--landed` and listed as an S6
  carrier. Sibling agreement for the promoted units: the S2 remedy's continuation is unit 8's row,
  consumed and asserted by the new AC14 (B1); S4 is retired to unit 9's field and AC5 asserts one
  line (H1); S9 and AC12 defer the one-derivation rule to unit 11's check (H3). Order 7 → 13.
- rev-1 · 2026-09-16 · initial draft, authored by the harness's SPEC stage from the unit-7 brief.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read back the harness cron listing at landing to check the keepalive reap attestation"`
returned no seam for the behaviour and reported `unscanned layers: .sh`, so the driver is invisible
to it and that result alone decides nothing. The seam was found by reading the driver: `verb_landed`'s
refusal ladder (`tools/unattended/unattended.sh:2354` at base), `verb_status`'s single `printf`
(`tools/unattended/unattended.sh:2890`), and `dod_met`'s `keepalive-reaped` arm
(`tools/unattended/unattended.sh:3909`) — this unit extends all three and mints one helper. The
sidecar root is unit 2's derivation, cited rather than re-spelled (S9). The recall probe's top hit
is the backlog row itself; its fourth hit is the `aPrimedKeepalive` round-2 spec audit whose
remedy — record the delete's return beside the id — is rejected in §4 because it is still the
agent's own report. The recall hit at `memory/builds/aPromptedMandate/RUN.md:30` — the CORRECTION
row, `:24` being the `## Parked` heading — is the measurement: two jobs attested dead, both listed
firing. Where the probes and the sibling specs disagreed with this spec's rev-1: spec 2 S3 grades a
`LANDING` record whose witness is on the local remote-tracking ref as `finished-unstamped`, and
spec 3's ratified table allowed that stop, so the premise rev-1 §4 rested on was not in any
sibling and is now unit 8's row. Otherwise nothing the probes returned disagreed with source; the
driver line numbers above were re-found at base 5f9648d6 and the brief's `:3909` for the grep was
exact.

Recall terms used: `keepalive-reaped attestable not checkable CronList firing forever attestation read-back list verb landed status`

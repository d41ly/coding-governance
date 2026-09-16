# TOOL-aWokenSentinel-7 — `keepalive-reaped` becomes CHECKED: `--landed` reads the harness's own cron listing

**Status:** SPECCED · rev-1 · 2026-09-16 · node a · Tier-2 · base 5f9648d6 · streams tooling · order 7 · ratified 2026-09-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 |

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
  did not. The refusal names the remedy, which is to end the turn once and re-run the verb.
  Observed by AC2.
- **S3** — When the newest line was recorded in `LANDING` and does not name the id, `verb_landed`
  proceeds to the anchor observation and prints one `checked` line naming the id and the utc; when
  no sidecar exists, or the record names no `keepalive` id, it proceeds and prints one `unchecked`
  line saying why. A pass is never silent. Observed by AC3 and AC4.
- **S4** — `verb_status` prints one more line after its status line: the recorded keepalive id and
  what the newest stop-guard line says about it — `present`, `absent`, or `unrecorded` when no
  line exists. Observed by AC5.
- **S5** — `dod_met`'s `keepalive-reaped` arm sets `DOD_OUT` on the met path so `--close` announces
  that the attestation is checked at `--landed`, through the existing met-with-something-to-say
  print rather than a new one. Observed by AC6.
- **S6** — Every carrier that calls the item unobservable by a script is corrected in the same
  commit: the protocol's DoD table row, the Skill's close paragraph and its landed section, the
  VERBS entries for `--landed` and `--status`, and the map dossier's paragraph on the keepalive
  half; each template edit re-renders its output in that commit. Observed by AC7 and AC8.
- **S7** — The backlog row `TOOL-aPromptedMandate-11` moves to `CLOSED` in this unit's commit,
  citing the mechanism. Observed by AC9.
- **S8** — Both new `fail` branches and the two pass shapes get arms in the driver's suite, beside
  the existing `--landed` success arm, each observed red on a staged break before the branch is
  wired, and the suite's floors move by the arms' executed assertions. Observed by AC10 and AC11.
- **S9** — The driver holds ONE derivation of the sidecar root after this unit lands: this verb
  calls the derivation unit 2 introduced, and where unit 2 left it inline this unit extracts it at
  instance #2 rather than spelling a second `rev-parse --git-dir`. Observed by AC12.
- **S10** — The match rule for the id inside `session_crons` is verified against a REAL stop-guard
  line where one exists at build time, because the listing's shape is unmeasured and a substring
  rule that never matches the real spelling is a check that cannot fail. Observed by AC13.

## 3. Non-goals (OUT)

- No check at `--abort`. It writes the terminal phase in the same turn as the reap, and no later
  verb of the run exists to read a post-abort stop line. The stop-guard sees that stop and could
  compare the listing on a terminal verdict; that is a change to unit 3's predicate and a follow-up
  under `### Edges`, not this unit.
- No change to the stop-guard's predicate, its continuation reason, or the sidecar's grammar. This
  unit is a READER of unit 3's line and writes nothing under the git dir.
- No gate leg reads the sidecar. It is untracked and per-worktree, so a leg in a fresh clone could
  only report DEAD PROBE — the same reason `reuse-probed` is not a leg, protocol section 6.
- No parsing of the `session_crons` value beyond a substring test for the recorded id. Its shape
  is unmeasured (research §6 records presence, not form); the id match is the whole question this
  unit asks, and S10 verifies the rule against a real line before the unit closes.
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
- **consumes-from** `TOOL-aWokenSentinel-1` — the `session:` fact that binds a session to the run.
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
| no sidecar, or empty | proceed; print `unattended: keepalive-reaped: attested, unchecked — no stop-guard record for this run (the hook is not wired, or the session was never bound)` |
| newest line's phase is not `LANDING` | refuse, second new `fail` number |
| newest line's listing contains `kid` (`grep -qF`) | refuse, first new `fail` number |
| newest line's listing does not contain `kid` | proceed; print `unattended: keepalive-reaped: checked — <kid> absent from the harness listing at <utc>` |

Why the line's own `phase` field decides "after the close" and not a clock: the record carries no
timestamp for a phase change, so a clock comparison would mean reading the LANDING commit's
committer date and parsing the line's ISO utc with `date -d` — a second clock with its own failure
mode. `--close` is the sole writer of `LANDING` (S9 of `TOOL-aBoundedVerdict-15`, armed in the
suite), and `--landed` is the sole writer of `LANDED`, so a stop recorded in `LANDING` is by
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

Why the second refusal exists rather than the brief's `unchecked` pass: the Skill never mandates a
turn boundary between `--close` and `--landed`, and the ordinary landing runs attest, close, commit,
lander and `--landed` in ONE turn. Under a pass-on-older-line rule the check would fire only when a
turn happened to end between the two, which is by accident, and `TOOL-aPromptedMandate-11` would
not honestly close. Requiring the post-close line costs one stop-guard block per landing — the
stop-guard refuses a `LANDING` record's stop, records the listing, continues the session — and
only where the sidecar already exists, so an adopter without the hook, or a session never bound,
is never wedged. The fork and its M3 derivation are §8.

What it does NOT check, said in the verb's header comment: whether the job named by `keepalive`
was ever the run's job, whether a job under another id is still firing, or anything about a stop
the hook did not record. It reads one line the harness populated and compares one id.

### `--status` and `--close`

`verb_status` prints, immediately after its `unattended: <slug> · phase …` line and before the
witness refusal, exactly one line:

```
keepalive: <kid|none> · last harness listing <utc|none>: present|absent|unrecorded
```

`present` and `absent` come from the same `read_stop_listing` call and the same `grep -qF`;
`unrecorded` when the helper prints nothing. `--status` reads the newest line whatever its phase,
because it reports, it does not judge.

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
| `tools/unattended/VERBS.template.md`, the `--landed` and `--status` entries | the listing check and its two refusals; the one-line addition to `--status` | `memory/guides/UNATTENDED-VERBS.md` |
| `memory/map/features/unattended.md`, "The keepalive half is unenforceable by construction" | the reap is checked at `--landed` where the stop-guard is wired; the schedule half stays agent-only | none, the dossier is authored; `map_diff.py` reports it fresh |
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

### Inventory

| identifier | kind | cell |
|---|---|---|
| `read_stop_listing` | shell function in the driver | `sh.function`, verb `read`, snake — `--suggest` says OK |
| two `fail <n>` numbers | refusal branches | derived at build time, next free above the high-water |
| `keepalive:` status line | printed line | no cell; grammar above |

No conf key, no verb, no file under the kit dir.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.sh` | `read_stop_listing`; `verb_landed` check and two refusals; `verb_status` line; `dod_met` `DOD_OUT` |
| `tools/unattended/unattended.test.sh` | the arms of AC1 to AC6, AC10; floors of AC11 |
| `tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` | DoD row |
| `tools/unattended/SKILL.template.md` · `.claude/skills/unattended/SKILL.md` | close paragraph, landed section |
| `tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md` | two entries |
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
  `run --landed tRun` prints a line beginning `the keepalive attestation is contradicted by the
  harness's own listing` and ending `k1 listed at 2026-09-16T12:00:00Z`, the phase stays
  `LANDING`, and `sum` is unchanged.
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
  `run --landed tRun` prints `keepalive-reaped: checked — k1 absent from the harness listing at
  2026-09-16T12:00:00Z` and then `phase LANDED`, and the record's `landed-anchor` reads `remote`.
  Red when: no `checked` line prints while the phase still moves, which is the silent pass this
  unit forbids; or the check refuses on an empty listing.
- **AC4** — When no stop log exists for the slug, `run --landed tRun` prints `keepalive-reaped:
  attested, unchecked — no stop-guard record for this run` and then `phase LANDED`; when the log
  is absent and the record's `keepalive` line is deleted with `sed -i '/^keepalive: /d'`, it prints
  `keepalive-reaped: attested, unchecked — the record names no keepalive id` and lands.
  Red when: the verb refuses on a missing file, which would wedge every adopter without the hook;
  or lands with no `unchecked` line.
- **AC5** — When `run --status tRun` runs on the three fixtures of AC1, AC3 and AC4, its second
  line is respectively `keepalive: k1 · last harness listing 2026-09-16T12:00:00Z: present`,
  `keepalive: k1 · last harness listing 2026-09-16T12:00:00Z: absent` and `keepalive: k1 · last
  harness listing none: unrecorded`; the first line is byte-identical to what it printed before
  this unit.
  Red when: the line is missing on any of the three, or `present` and `absent` swap, or the first
  line changed.
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
  memory/map/features/unattended.md` prints 0 and `python tools/codebase-map/map_diff.py` reports
  the `unattended` dossier fresh.
  Red when: the sentence survives, or the dossier is reported stale.
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
  prints 1.
  Red when: it prints 2 or more, which means this unit spelled a second sidecar-root derivation
  beside unit 2's instead of calling it, or found unit 2's inline and copied it rather than
  extracting it.
  figure: DERIVED at observation; the count is 0 at base 5f9648d6 and unit 2 makes it non-zero.
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

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `hook destinations (every declared hook path ships)`

These are what `--close` runs, once, on the whole bar. The pass runs none of them: it verifies with
the driver invocations §6 names over a scratch clone, the greps of AC7 to AC9 and AC12, and
`check-arms.py --report` filtered to the driver, which is the meta-gate's report mode and not its
leg. Under `unattended kit gate`, the protocol-render parity check is the join this unit moves;
under `unattended skill wiring`, the Skill render.

New arm: `tools/unattended/unattended.test.sh` · the two new refusals, each observed by the fixture
of AC1 and AC2 with its `fail` line commented out before the arm is trusted, plus the `checked`,
`unchecked` and no-id passes of AC3 and AC4, the three `--status` shapes of AC5 and the `--close`
row of AC6 · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the executed count, AC11;
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

## 9. Revision log

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
agent's own report. The recall hit at `memory/builds/aPromptedMandate/RUN.md:24` is the
measurement: two jobs attested dead, both listed firing. Nothing the probes returned disagreed with
source; the driver line numbers above were re-found at base 5f9648d6 and the brief's `:3909` for
the grep was exact.

Recall terms used: `keepalive-reaped attestable not checkable CronList firing forever attestation read-back list verb landed status`

# KICK-dKeptSession-35 — every dependency notice posted per dependent and per Design exit, so each one lands as its own message

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 25 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-build-KICK-dKeptSession-35-deviation-351.md](../build/2026-10-26-build-KICK-dKeptSession-35-deviation-351.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 4 at HIGH**, report item **H3**. Id 54 is the same defect at BLOCKER, item B2,
promoted as `KICK-dKeptSession-31`. Fixing one item fixes the other; unit 31 puts the recipient and
the content key into the id, and this unit makes the notices pass what tells two of them apart.

`KICK-dKeptSession-7` S4 posts every `changed` with the fixed subject `interfaces <slug>` and no
`--item` or `--pass`, and S5 posts every `landed` the same way. With the six-field id the second
dependent's `confirmed` collides at the first Design exit, and every later `changed` collides with the
first; the dependent never receives the new key and its Build items stay held until the parent lands.
AC7 uses one dependent and two moves, so it sees neither. This unit gives each notice its Design-exit
ordinal, keeps every refusal visible, and observes two dependents over three exits. It repairs
`KICK-dKeptSession-7` and builds one step after it (order 25).

## 2. Scope (IN)

- **S1** — id 4. The pass. `write_dependency_notices` in `tools/loop/loop_transition.py` passes
  `--pass <n>` on every `confirmed` and `changed`, `<n>` the Design-exit ordinal: the count of this
  build's transitions from `designing` to `building` that `read_transitions(build, repo)` returns,
  this one included. A parent that leaves Design twice with the same interface text therefore posts
  two messages, and its dependents read the newer. Observed by AC1.
- **S2** — id 4. The landing. `verb_landed`'s per-dependent `landed` passes `--pass <sha8>`, the
  landed sha's first eight hex, so a re-landing after a revert is a new message. Observed by AC2.
- **S3** — id 4. A refused notice is visible. Where a post exits non-zero, the caller prints
  `notice — not posted <kind> to build:<dependent> · rc <n> · <the post's first line>`, one line per
  refused post; the transition and the landing still succeed, as `KICK-dKeptSession-7` §5 states.
  Observed by AC3.
- **S4** — id 4. `KICK-dKeptSession-7` AC7 is superseded by name by AC1, which observes two
  dependents over three Design exits; that unit's acceptance ledger answers AC7 with AC1's output.
  Observed by AC1.

## 3. Non-goals (OUT)

- The id's fields: `KICK-dKeptSession-31`, the B2 half.
- Acknowledging a notice once its dependent consumes it: id 55, item H9, `KICK-dKeptSession-42`.
- The left-shift arm, N notices with distinct recipient and key pairs: `KICK-dKeptSession-31` AC2.

### Edges

- **consumes-from** `KICK-dKeptSession-7` — `write_dependency_notices` and `verb_landed`'s `landed` notice, whose posts this unit gives a pass and a visible refusal line (id 4)
- **consumes-from** `KICK-dKeptSession-31` — the eight-field `derive_message_id`, without which two dependents at one exit still share one id whatever pass is given

## 4. Design

### Evidence

- `KICK-dKeptSession-7` S4 and §4 "The notices" spell the three notices with subject
  `interfaces <slug>` or `landing <slug>` and no item or pass; its AC7 has one dependent and two
  moves (spec-7 lines 63-74, 135-139 and 223-229).
- `KICK-dKeptSession-22` S2's id takes `pass` as a field, absent written `none`.
- `read_transitions(build, repo)` returns a build's transitions in order (TOOL-dDeclaredLoop-3 S7),
  the reader `KICK-dKeptSession-5` S10 already uses for its disposal.

### The posts, two dependents over three exits

```
exit 1  confirmed · to build:dA · pass 1      confirmed · to build:dB · pass 1
exit 2  changed   · to build:dA · pass 2      changed   · to build:dB · pass 2
exit 3  changed   · to build:dA · pass 3      changed   · to build:dB · pass 3
```

### Inventory

No identifier is minted; `notice — not posted` is a line of the existing callers.

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: S1 and S3 in `write_dependency_notices`
- `tools/loop/selftest.py`: the two-dependent, three-exit case
- `tools/unattended/unattended.sh`: S2 and S3 in `verb_landed`
- `tools/unattended/unattended.test.sh`: the landed arm extended

### Alternatives rejected

- **The recipient in the subject.** `KICK-dKeptSession-31` puts it in the id, where every caller
  gets it once.
- **The content key alone telling exits apart.** An A to B to A interface change returns to an
  earlier key, which would collide with the first notice.

## 5. Production-readiness checklist

- security — none beyond `KICK-dKeptSession-7`'s: the posts pass through unit 5's post path.
- perf / scale — one `read_transitions` per Design exit.
- error / empty / loading states — an unreadable transition log gives no ordinal; the post is then
  refused by S3's line rather than posted with a guessed pass.
- observability — every refused notice prints its own line.
- risks — none new.
- testing — the cases of §6 and the arms in §7.
- migration — none.
- user docs — `help/loop.md`'s notices paragraph (`KICK-dKeptSession-7` S7) gains the pass.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-7` AC7's: a scratch repository with two builds' READMEs naming one
parent, a bare origin under `%TEMP%` and `RUN_CLAIMS=on`.

- **AC1** — When `python loop_transition.py record` moves the parent out of Design three times with
  two dependent READMEs, `--mail read dA` and `--mail read dB` each list one `confirmed` and two
  `changed`, six posts in all, every one printed `mail — posted`.
  Red when: a post prints `mail — duplicate`, as a copy dropping `--pass` shows on the A to B to A
  case.
- **AC2** — When `bash tools/unattended/unattended.sh --landed <parent>` succeeds twice on two
  landed shas, each dependent holds two `landed` messages.
  Red when: the second landing's notice is refused as a duplicate.
- **AC3** — When the post is planted to exit 1, `loop_transition.py record` still exits 0 and prints
  `notice — not posted confirmed to build:dA · rc 1`.
  Red when: the refusal is silent, or it fails the transition.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC1 AC3 · two dependents over three Design exits and a post planted to exit 1, staged red by a copy dropping `--pass` · none
New arm: tools/unattended/unattended.test.sh · covers AC2 · two landings to one dependent · `FLOOR_ASSERTIONS` and its shard floor rise by the arm's count, counted off the diff

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H3 (id 4).

## 10. Reuse audit

The seams extended are `KICK-dKeptSession-7`'s `write_dependency_notices` and `verb_landed`'s notice
(`tools/unattended/unattended.sh:6316` for the verb), with `read_transitions` for the ordinal.
`python tools/codebase-map/reuse_lookup.py "a dependency gate switched by policy and parent
reachability"`, unit 7's probe, ranked `load_policy` and gate readers by name stem; the loop kit is
not at this base, so no existing seam in the tree fits and unit 7's spec is the seam.

Recall terms used: `python tools/memory-recall/query.py "how does a parent post each dependent its
interface notices" --terms "confirmed changed landed notice dependent pass Design exit ordinal
duplicate derive_message_id write_dependency_notices"`

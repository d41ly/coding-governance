# KICK-dKeptSession-52 — the per-exit pass observed on a repeated interface, so dropping `--pass` prints a duplicate

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-52-deviation-521.md](../build/2026-10-26-build-KICK-dKeptSession-52-deviation-521.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 3 at HIGH**, report item **H5**, which no other id shares.

`KICK-dKeptSession-35` S1 gives every `confirmed` and `changed` notice `--pass <n>`, the Design-exit
ordinal, and its AC1 says a copy dropping `--pass` reds "on the A to B to A case". It cannot.
`KICK-dKeptSession-31` S1 derives the id from eight fields, `kind` and `content-key` among them, and
over interface texts A, B, A the posts to one dependent are (`confirmed`, A), (`changed`, B) and
(`changed`, A): exits 1 and 3 differ in kind, and exits 2 and 3 in key, so without `--pass` no two
share an id and the arm stays green with S1 removed. AC1 pins no interface texts, and unit 35 §4's
Alternatives line ("an A to B to A interface change ... would collide with the first notice") is
false for the same reason. This unit pins the case that only the pass separates and names the red
it prints. It repairs `KICK-dKeptSession-35` and builds one step after it (order 26).

## 2. Scope (IN)

- **S1** — id 3. The discriminating case. A loop selftest case `notices-repeat-key` in
  `tools/loop/selftest.py` moves the parent out of Design three times with the interface texts A, B
  and B, and two dependent READMEs, so exits 2 and 3 publish two `changed` notices with one content
  key to each dependent. Observed by AC1.
- **S2** — id 3. The staged red named. The case's staged break is a copy of `loop_transition.py`
  whose `write_dependency_notices` passes no `--pass`; on it, exit 3 prints `mail — duplicate` for
  each dependent, and the build records that line in unit 35's acceptance ledger before the fix
  lands. Observed by AC2.
- **S3** — id 3. The sibling text superseded by name. `KICK-dKeptSession-35` AC1's "Red when"
  clause and §4's Alternatives line read: the pass separates a `changed` from a later `changed`
  with the same key, a changed-to-changed key repeat, while kind and key already separate the A, B,
  A posts. Answered in unit 35's acceptance ledger. Observed by AC1.

## 3. Non-goals (OUT)

- The pass itself and the refusal line: `KICK-dKeptSession-35`, unchanged.
- The id's fields: `KICK-dKeptSession-31`.
- The report's left-shift entry, that every staged break in a spec names the red line it prints.
  No clause of this build names that checklist; S2 is the instance here.

### Edges

- **consumes-from** `KICK-dKeptSession-35` — `write_dependency_notices`' `--pass <n>` and AC1's three-exit fixture, which this unit pins to a key the pass alone separates (id 3)
- **hands-off** `KICK-dKeptSession-62` — the `notices-repeat-key` arm, whose leg the batch's S1 records (id 2)

## 4. Design

### Evidence

- `KICK-dKeptSession-31` S1: `derive_message_id <build> <item> <pass> <kind> <subject> <answers> <to>
  <content-key>`, each absent field `none`.
- `KICK-dKeptSession-7` S4: the first post to a dependent is `confirmed`, every later one `changed`,
  each carrying its `--interface` key, so a key repeated at a later exit is the only collision the
  kind leaves.

### The posts to one dependent, interface texts A, B, B

```
exit 1  confirmed · key(A) · pass 1
exit 2  changed   · key(B) · pass 2
exit 3  changed   · key(B) · pass 3      without --pass: id equals exit 2's -> mail — duplicate
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `notices-repeat-key` | selftest case | `tools/loop/selftest.py` |

### Migration

None.

### Files touched (estimate)

- `tools/loop/selftest.py`: S1's case

### Alternatives rejected

- **Four exits A, B, A, B.** It also collides at exit 4, but needs a fourth exit and reads no more
  than A, B, B does.
- **Keeping A, B, A and asserting six posts.** Six posts land with or without the pass, so the case
  cannot fail on the scope item it claims.

## 5. Production-readiness checklist

- security — none: a selftest case.
- perf / scale — one more three-exit case in the loop suite.
- error / empty / loading states — none new.
- observability — S2's recorded red.
- risks — none.
- testing — the criteria of §6 and the arm in §7.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-35`'s: a scratch repository with two builds' READMEs naming one
parent, a bare origin under `%TEMP%` and `RUN_CLAIMS=on`.

- **AC1** — When the `notices-repeat-key` case runs `python loop_transition.py record` three times
  with the interface texts A, B and B, `--mail read dA` and `--mail read dB` each list one
  `confirmed` and two `changed`, every post printing `mail — posted`.
  Red when: a post prints `mail — duplicate`.
- **AC2** — When the same case runs against the copy whose `write_dependency_notices` passes no
  `--pass`, exit 3 prints `mail — duplicate` for each dependent, and unit 35's acceptance ledger
  holds that line.
  Red when: the copy stays green, so the case does not decide S1 of unit 35.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC1 AC2 · three Design exits with interface texts A, B, B to two dependents, staged red by a copy dropping `--pass` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H5 (id 3).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-35`'s three-exit fixture and its staged copy, now pinned to
interface texts; no case runner is minted. `python tools/codebase-map/reuse_lookup.py "a dependency
gate switched by policy and parent reachability"`, unit 7's probe, ranked `load_policy` and gate
readers by name stem; the loop kit is not at this base, so no existing seam in the tree fits and
unit 35's spec is the seam.

Recall terms used: `python tools/memory-recall/query.py "which staged break makes the per-exit
pass decide a notice id" --terms "pass Design exit ordinal changed confirmed content-key duplicate
staged break fixture write_dependency_notices"`

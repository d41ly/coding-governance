# TOOL-dBoundRoles-59 — unit 53's read check folds each `reads` entry through `roles_lib.parse_read_key`, so the tag spelling unit 14 writes passes and the read-key grammar keeps one owner

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 23 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 |
| [2026-10-26-build-TOOL-dBoundRoles-59-round4-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-59-round4-fix-return.md) | research | TOOL-dBoundRoles-60 |
| [2026-10-26-prompt-TOOL-dBoundRoles-59-round4-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-59-round4-fix-brief.md) | research | TOOL-dBoundRoles-60 |
| [2026-10-26-review-TOOL-dBoundRoles-59-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-59-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 52 to 58
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md`) confirmed
finding **id 21 at HIGH**, report item **H1**. No other id shares the item. Id 22 reports the same
stale-parse class on spec 58 AC5 at MEDIUM, item M9, and id 23 the stale citation on spec 52 at LOW,
item L7; both are `TOOL-dBoundRoles-60`'s.

`TOOL-dBoundRoles-53` S1 has `assert_role_reads` read a role's `reads` through `roles_lib.load_roles` and
copy the parse `tools/roles/handoff.py:1025` makes at base: split on commas, strip, drop a trailing `?`.
`TOOL-dBoundRoles-14` S4 (order 1) makes `roles_lib.parse_read_key` the one read-key parser, and its S7
rewrites every gov role's `reads:` line to the tag spelling. At order 22 the copy yields
`field.input.question`, so `assert_role_reads gov-orienter input:question` fails on a correct tree, 53
AC1 passes for the wrong reason, and 58 S2 inherits the failure on every render of 47's case.

This unit makes the read check fold each entry through `parse_read_key` and restates unit 53's spec for
it. It repairs `TOOL-dBoundRoles-53` and builds one step after it (order 23).

## 2. Scope (IN)

- **S1** — The fold. `assert_role_reads <role> <key>...` in `tools/roles/adopt-roles.test.sh` reads the
  role's `reads` value through the installed kit's `roles_lib.load_roles`, splits it on commas as
  `check_roles.py` R3 and `render_handoff` do, and passes each entry to `roles_lib.parse_read_key`. It
  compares the native keys that function returns with the keys the case passes, ignoring the optional
  flag, and fails naming the role and the first key it does not find. Every key is checked,
  `input:prompt` included, as 53 S1 states. Observed by AC1 and AC2.
- **S2** — Both spellings pass. A role line in the tag spelling (`field.input.question,
  field.input.prompt?`) and one in the native spelling (`input:question, input:prompt?`) satisfy the
  same call, because `parse_read_key` accepts both (14 S4, 14 AC5). Observed by AC2.
- **S3** — One parse in the suite. No line of `tools/roles/adopt-roles.test.sh` strips a `?` from a
  `reads` entry or compares a raw entry with a key; the helper's Python slice names `parse_read_key`.
  Observed by AC3.
- **S4** — Unit 53's spec follows the helper. The pass bumps `TOOL-dBoundRoles-53`'s spec before it edits
  the helper (BUILD-METHOD M2, READY): S1 and its Readers clause cite `parse_read_key` and unit 14 S4 in
  place of `handoff.py:1025`, §4 Evidence and §10 likewise, and a §9 line names this unit and S1. Unit
  53's ledger answers AC1 and AC2 `amended rev-<n>`, naming that revision. Where unit 53's pass already
  folded through `parse_read_key` and recorded the deviation, this pass records that, edits no code, and
  still makes the bump. Observed by AC4.

## 3. Non-goals (OUT)

- Lifting the comma split into a `roles_lib` list parser shared by R3, `render_handoff` and the
  render's read check at `handoff.py:1025`. The grammar that moved is the entry's, which
  `parse_read_key` owns; those readers sit in files units 14 and 20 edit (§4 "Alternatives rejected").
- The report's left-shift grep gate over every split of a `reads` value. No clause of this build names
  it; S3 and AC3 are this suite's regression.
- 58 AC5's raw-prefix read and 52's stale citation: `TOOL-dBoundRoles-60`'s, for ids 22 and 23.
- The case's role and its exit check: units 52 and 53, read here.

### Edges

- **consumes-from** `TOOL-dBoundRoles-53` — `assert_role_reads`, its S1 Readers clause, §4 Evidence and §10, which S1 re-points and S4 restates (id 21)
- **consumes-from** `TOOL-dBoundRoles-14` — `parse_read_key` and the tag-spelled `reads:` lines of S7, which S1 folds each entry through (id 21)
- **hands-off** `TOOL-dBoundRoles-58` — the folded `assert_role_reads`, which 58 S2 and AC2 call on every render of 47's case (id 21)
- **hands-off** `TOOL-dBoundRoles-60` — the folded helper, under which unit 60's item for id 2 stages 53 AC3's refusal-only break with a passing control render (ids 2 and 21)
- **hands-off** `TOOL-dBoundRoles-61` — the folded `assert_role_reads` and its slice, which unit 61 fails on any non-zero exit, and S1, §4, §5 and §6, which its pass restates (id 19 of the round-1 audit of units 59 and 60)
- **hands-off** `TOOL-dBoundRoles-63` — S1, S4, §4 and AC4, which unit 63 restates: the exit status read, 53's OBSERVED answers, every spelling of the retired citation, 53's §10 seam and the ledger in the write set (ids 7, 9, 11, 14, 17 and 18 of the round-1 audit of units 59 and 60)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/roles/handoff.py:1025` builds the render's read set as
  `{x.strip().rstrip("?") for x in keys.get("reads","").split(",")}` inside `main`, and `:1026-1028`
  call `ap.error` for an unread input other than `prompt`.
- `tools/roles/roles_lib.py:330-336` `load_roles` returns each role file's raw front-matter keys; it
  folds nothing.
- `tools/roles/check_roles.py:198` and `tools/roles/handoff.py:337` split `reads` on commas the same way.
- `tools/roles/agents/gov-orienter.agent.md:8` reads `input:question, input:prompt?` at base.
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md` S4 adds
  `parse_read_key(entry)`, returning the native key and its optional flag, and S7 tag-spells the ten
  lines. 14 AC6 renders `--input spec=` on a migrated line and expects the base `task-sha=`, so the read
  check at `:1025` folds through `parse_read_key` from order 1 on as well.
- `tools/roles/adopt-roles.test.sh:60` resolves `$PY` by running each candidate, and `:81` holds
  `FLOOR_ASSERTIONS=50` with a `+n for arm k (unit)` comment per raise above it.

### The slice

```bash
"$PY" -B -c 'import sys
sys.path.insert(0, sys.argv[1])
import roles_lib
keys = roles_lib.load_roles(sys.argv[1])[sys.argv[2]]["keys"]
have = {roles_lib.parse_read_key(e.strip())[0] for e in keys.get("reads", "").split(",") if e.strip()}
print(next((k for k in sys.argv[3:] if k not in have), ""))' "$FX/$FXK" "$role" "$@"
```

An empty line means every key is read; a printed key fails the case through `check_arm`, naming the role
and that key. The slice is the design's shape; the pass fits it to the helper's argument handling.

### Inventory

Minted: none. `assert_role_reads` keeps its name and its call sites.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 23, after unit 53 at order 22. `TOOL-dBoundRoles-20` holds order 23 and its
Files touched names the same suite, so the two passes' declared write sets intersect and `--dispatch`
refuses the second while the first is open (`tools/unattended/unattended.sh:13421`, M6 condition 1).

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`
- the spec of TOOL-dBoundRoles-53, a rev bump (S4), named here for the dispatch write set

### Alternatives rejected

- **A `parse_reads(value)` list parser in `roles_lib`, every reader re-pointed.** It moves three product
  readers in files units 14 and 20 own at nearby orders, for a comma grammar that has not changed.
- **Compare the tag spelling in the test.** It hard-codes 14 S7's spelling in a second place, and a native
  line, which `parse_read_key` still accepts, would fail.

## 5. Production-readiness checklist

- security — no new write path; the case can no longer pass or fail on a spelling the render accepts.
- perf / scale — one `"$PY" -B -c` read of the roster per call, as 53 S1 already makes.
- error / empty / loading states — an empty `reads` value yields no key, so S1 fails naming the first key.
- observability — each failure names the role and the native key.
- risks — a later change to `parse_read_key`'s return shape reds the case at S1, loudly.
- testing — AC1 to AC4 by staged copies of the helper, scratch role lines and grep; the arm of §7 at the
  close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the roles adopter fixture, whose installed `gov-orienter.agent.md` holds the line unit
  14 leaves (`reads: field.input.question, field.input.prompt?`), calls
  `assert_role_reads gov-orienter input:question input:prompt`, the call passes; with the helper staged
  back to the raw split that strips a trailing `?`, the same call fails naming `input:question`.
  Red when: the helper compares raw entries, so a tag-spelled line refuses a key the role reads.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC2** — When the fixture's `gov-orienter.agent.md` is rewritten to the native line
  `reads: input:question, input:prompt?`, the same call passes; with `field.input.prompt?` left out of the
  tag-spelled line, it fails naming `input:prompt`.
  Red when: one spelling is refused, or a handed key the role does not read passes.
- **AC3** — When `grep -n 'parse_read_key' tools/roles/adopt-roles.test.sh` runs, it names the helper's
  slice, and `grep -nF 'rstrip("?")' tools/roles/adopt-roles.test.sh` prints nothing.
  Red when: the suite keeps a second parse of a `reads` entry.
- **AC4** — When `grep -n 'parse_read_key' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-53.md`
  runs, it prints S1's Readers clause and a §4 Evidence line, `grep -n 'handoff.py:1025-1026'` over the
  same file prints nothing, and its §9 carries a line naming `TOOL-dBoundRoles-59` and S1.
  Red when: unit 53's spec still assigns the read-key grammar to a copy.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · the folded read check over both spellings, staged by restoring the raw split, which refuses the tag-spelled line · `FLOOR_ASSERTIONS` raised by the floored assertions the case adds, with a `+n` comment naming this unit

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 53 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 52 to 58, id 21
  (HIGH, item H1), on the report's fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-61 and TOOL-dBoundRoles-63, the HIGH promotion and the minors batch of the round-1 audit of units 59 and 60; nothing else moved.

## 10. Reuse audit

The seam is `TOOL-dBoundRoles-14`'s `roles_lib.parse_read_key`, the one read-key parser, which the
helper calls rather than copying, inside unit 53's `assert_role_reads` and the suite's `check_arm`
(`tools/roles/adopt-roles.test.sh:83`).
`python tools/codebase-map/reuse_lookup.py "fold a tag-spelled role reads entry back to its native read key"`
ranked `read`, `read_text`, `key` and `read_conf_key`, none a read-key parser, because
`parse_read_key` is minted at unit 14's pass and absent at base; the recall query below found it in
14 S4. No existing seam fits beyond that function and the helper it serves.

Recall terms used: `python tools/memory-recall/query.py "which function owns parsing a role reads entry after the tag spelling" --terms "parse_read_key reads field tag spelling native key roles_lib assert_role_reads load_roles handoff"`

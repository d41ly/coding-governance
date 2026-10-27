# TOOL-dWellOiledMachine-98 — one ordering probe, defined once in spec 95: an amendment is an ancestor of the amended unit's build commit, never the first subject a log prints

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 67 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-98-deviation-981.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-98-deviation-981.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-98-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-4 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md`),
finding 1, item H1, at HIGH. Item H1 also carries findings 11, 19 and 29 (closed by
TOOL-dWellOiledMachine-99, -100 and -101 on spec 95), 12, 20 and 30 (-102, -103 and -104 on spec 96)
and 13, 21 and 31 (-105, -106 and -107 on spec 97). Finding 1 is the class: one probe,
`git log --reverse --format=%s <BASE>..HEAD | grep -E "<ids>" | head -1`, is copied into 95 AC2, 96
AC5 and 97 AC15, and in every copy the first matching subject is an older spec-set commit (089c397aa
or e446e9582), so it can never print the amendment. This unit defines the replacement once, as a
shell function in spec 95's §6 that the other two specs load, so the three criteria read one
ordering predicate: the amending unit's first commit touching the amended spec is a strict ancestor
of the built unit's build commit.

## 2. Scope (IN)

- **S1** — The predicate, defined once. Spec 95 takes a rev bump, its §9 line naming this unit and
  finding 1 of the round-4 promotions audit, whose §6 preamble gains the sentence "The ordering probe
  of this build is `check_amended_before_built`, defined below and loaded by
  `eval "$(sed -n '/^check_amended_before_built() {/,/^}/p' memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md)"` from the repository
  root, that code span on one line;
  `LIB` may name the checkout's `tools/unattended/lib-unattended.sh` when the caller's working
  directory is elsewhere." followed by §4's fenced function, verbatim. Observed by AC1, AC3.
- **S2** — No second copy. Specs 96 and 97 spell no definition of the function and no subject-order
  probe; their criteria load spec 95's (TOOL-dWellOiledMachine-103 and -106 rewrite those criteria).
  Observed by AC1, AC2.
- **S3** — The route. S1's rev bump is made by the build run's main loop at BUILD-METHOD M2's
  cross-read, before its first code pass, in a spec pass whose commit touches spec 95 and whose
  subject names this unit and neither TOOL-dWellOiledMachine-90 nor TOOL-dWellOiledMachine-93, the
  route TOOL-dWellOiledMachine-95 §8 F1 takes. At this unit's own pass, at order 67, nothing is
  written: the pass runs AC1 to AC4 and records them. Observed by AC4.

## 3. Non-goals (OUT)

- Rewriting 95 AC2, 96 AC5 or 97 AC15 to call the predicate: findings 19, 20 and 21, units 100, 103
  and 106.
- The staged red cases: findings 29, 30 and 31, units 101, 104 and 107.
- The S-item text naming what "before the pass" means: findings 11, 12 and 13, units 99, 102 and 105.
- No kit function: the predicate is a probe in spec text, not code in `tools/unattended/` (§8 F1).
- No lint over git-log criteria in specs: the report's left-shift line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-95` — its §6 preamble, which gains the predicate before unit 95's pass runs AC2
- **hands-off** `TOOL-dWellOiledMachine-99` — the predicate whose ancestry relation 95 S3 names as its meaning of before unit 90's pass
- **hands-off** `TOOL-dWellOiledMachine-100` — the predicate 95 AC2 calls for specs 90 and 93
- **hands-off** `TOOL-dWellOiledMachine-101` — the predicate 95's staged red case runs on a fixture repository
- **hands-off** `TOOL-dWellOiledMachine-102` — the predicate whose ancestry relation 96 S4 names
- **hands-off** `TOOL-dWellOiledMachine-103` — the predicate 96 AC5 loads from spec 95 and calls for spec 93
- **hands-off** `TOOL-dWellOiledMachine-104` — the predicate 96's staged red case runs on a fixture repository
- **hands-off** `TOOL-dWellOiledMachine-105` — the predicate whose ancestry relation 97 S24 names
- **hands-off** `TOOL-dWellOiledMachine-106` — the predicate 97 AC15 loads from spec 95 and calls for specs 91 to 94
- **hands-off** `TOOL-dWellOiledMachine-107` — the predicate 97's staged red case runs on a fixture repository
- **hands-off** `TOOL-dWellOiledMachine-108` — the predicate the batch's ordering criteria call for its own rev bumps
- **hands-off** `TOOL-dWellOiledMachine-109` — the predicate 109's ordering check calls for its rev bump of spec 108 (round-5 promotions audit, finding 27)
- **hands-off** `TOOL-dWellOiledMachine-110` — the predicate 110's ordering check calls for its rev bump of spec 108 (round-5 promotions audit, finding 4)
- **hands-off** `TOOL-dWellOiledMachine-111` — the predicate 108 AC21's rewritten loop and 111's ordering check call (round-5 promotions audit, finding 5)
- **hands-off** `TOOL-dWellOiledMachine-112` — the predicate 112's fixture loads from spec 95 and runs (round-5 promotions audit, finding 29)
- **hands-off** `TOOL-dWellOiledMachine-113` — the predicate 113's ordering check calls for its rev bump of spec 103 (round-5 promotions audit, finding 20)
- **hands-off** `TOOL-dWellOiledMachine-114` — the predicate 114's ordering check calls for its rev bump of spec 106 (round-5 promotions audit, finding 21)
- **hands-off** `TOOL-dWellOiledMachine-115` — §4's predicate, §4 Evidence and §5's perf line, which gain the `_SUBJ` cache, trailer-aware attribution and bullet-label citations before this unit's amendment of spec 95 lands (round-5 promotions audit, findings 14, 15 and 17)

## 4. Design

### The predicate

```bash
check_amended_before_built() {  # amended unit, amending unit, built unit: 0 when ordered
  local d=memory/builds/dWellOiledMachine floor a p
  floor=$(git log --diff-filter=A --format=%H -- "$d/spec/*-TOOL-dWellOiledMachine-$2.md" | tail -1)
  [ -n "$floor" ] || return 1
  a=$(git log --reverse --format='%H %s' "$floor..HEAD" -- "$d/spec/*-TOOL-dWellOiledMachine-$1.md" \
    | grep -E "(^|[^A-Za-z0-9-])TOOL-dWellOiledMachine-$2([^A-Za-z0-9-]|$)" | head -1 | cut -d' ' -f1)
  p=$(. "${LIB:-tools/unattended/lib-unattended.sh}" && build_commit "$floor..HEAD" \
    "TOOL-dWellOiledMachine-$3" "$d" "$(read_conf_value .unattended.conf GENERATED_INDEXES)" \
    "$(read_conf_value .unattended.conf SHARED_RECORDS)")
  [ -n "$a" ] && [ -n "$p" ] && [ "$a" != "$p" ] && git merge-base --is-ancestor "$a" "$p"
}
```

- **floor** is the commit that added the amending unit's own spec. Every commit at or before it is
  outside the window, so an older spec-set commit naming the same ids, 089c397aa or e446e9582, is
  never read. For TOOL-dWellOiledMachine-95, -96 and -97 it is 0d8692025, the commit the report
  names, derived rather than typed.
- **A**, the amendment, is the first commit after the floor that touches the amended spec and names
  the amending unit as a whole token of its subject. Whole-token, so `TOOL-dWellOiledMachine-960` and
  a record name such as `TOOL-dWellOiledMachine-98-spec-audit` do not match
  (`memory/gotchas/id-matched-as-a-substring`).
- **P**, the built unit's build commit, is `build_commit`'s answer
  (`tools/unattended/lib-unattended.sh:1186`): the first commit naming the unit, by `Pass:` trailer or
  subject, that touches a path outside the build's folder and the declared indexes and shared
  records. It is the pass-order history leg's own definition.
- **Verdict**: A and P both exist, differ, and A is an ancestor of P. Every empty population is a
  refusal, so no amendment, no build, or no amending spec reads red.

### What it does not check

- What the amendment says. Each spec's text criteria observe that.
- The kits' `[[generated]]` rows, which `resolve_generated_indexes` adds to the conf's
  `GENERATED_INDEXES` (`tools/unattended/lib-unattended.sh:838`); it is not called, because it
  creates bare temp files. A commit naming the built unit that touches only such an index is read as
  its build, which moves P earlier. On this run's linear branch that can only turn a true verdict
  false, never the reverse, and the backlog row TOOL-aRepatriatedFork-48 is the same direction.
- A later commit naming the amending unit that touches the amended spec before the M2 spec pass. S3
  and the routes of units 99, 102 and 105 make the M2 spec pass the first such commit.

### Evidence

- 95 AC2 (`spec-95.md:136-140`), 96 AC5 (`spec-96.md:179-181`) and 97 AC15 (`spec-97.md:295-297`)
  each take the first subject matching an id set over `<BASE>..HEAD`.
- The function above, loaded from a scratch file and run 2026-10-27 on this tree, exits 1 for
  `90 95 90`, `93 96 93`, `91 97 91` and `94 97 94`: its floor is 0d8692025 each time, and neither an
  amendment nor a build commit exists yet.
- On scratch fixture repositories under `%TEMP%` it exits 0 for an amendment before the pass, and 1
  for an amendment after it, for a pass with no amendment, for an amendment with no pass, and for an
  amendment whose subject names `TOOL-dWellOiledMachine-950`.
- `build_commit` takes a range, the unit id, the build folder, the generated indexes and the shared
  records (`tools/unattended/lib-unattended.sh:1186`), and `read_conf_value` reads a conf key without
  sourcing the conf (`:780`); `.unattended.conf:417-418` declares both keys.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_amended_before_built` | shell function in spec 95's §6, never in code | `sh.function`, `check`, OK |

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-95.md` (S1's rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 95's rev cell moves)

### Alternatives rejected

- **A content anchor, `git log -S <string>`.** `fixture-session` is in spec 91 since e446e9582, so
  the anchor finds the old commit and reads green whatever the order (finding 31's skeptic).
- **The first subject after `<BASE>`.** The finding itself.
- **A copy per spec.** Three copies of one predicate is the defect finding 1 names.

## 5. Production-readiness checklist

- security — N/A — no write path, secret or surface; the probe reads history.
- perf / scale — two `git log` walks and one `build_commit` walk per call, over the run's range.
- error / empty / loading states — an absent floor, amendment or build commit returns 1.
- observability — the verdict is the exit status; AC3 shows the empty populations read red.
- risks — a later commit naming this unit touching spec 95 first would be read as the amendment; S3
  makes the M2 spec pass that commit.
- testing — AC1 to AC4.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`.
Each command runs from the repository root, after the predicate is loaded by
`eval "$(sed -n '/^check_amended_before_built() {/,/^}/p' <spec 95>)"`.

- **AC1** — When `grep -c '^check_amended_before_built() {'` runs over `<spec 95>`, it prints 1, and
  over `<spec 96>` and `<spec 97>` each prints 0; and `type check_amended_before_built` after the load
  prints a function.
  Red when: the predicate is missing from spec 95, or a copy is spelled in spec 96 or 97.
- **AC2** — When `grep -c -- '--format=%s <BASE>..HEAD |'` runs over `<spec 95>`, `<spec 96>` and
  `<spec 97>`, each prints 0.
  Red when: a criterion still orders by the first subject a log prints.
- **AC3** — When `check_amended_before_built 90 95 999` and `check_amended_before_built 90 999 90`
  run, each exits 1.
  Red when: a built unit with no build commit, or an amending unit with no spec, reads as ordered.
- **AC4** — When `check_amended_before_built 95 98 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 95 lands after unit 90's build commit, so unit 95's pass
  ran the old AC2.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: the predicate is a probe in spec text, and each criterion above runs it.

## 8. Open questions

- **F1 — Where does the one predicate live?** (a) a fenced function in spec 95's §6, loaded by the
  other specs; (b) a function in `tools/unattended/lib-unattended.sh`; (c) one copy in each spec.
  (c) is the copy finding 1 names. (b) adds a public function to a copy-installed kit, with its kit
  version, self-test and documentation, for a probe three spec criteria run: a new public surface,
  which BUILD-METHOD M3 veto 2 reserves to the owner. (a) spells it once, reuses `build_commit` as it
  stands, and needs no code. RESOLVED (agent, 2026-10-27, delegated): (a). widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-4 promotions, finding
  1 (H1).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-5
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-109, TOOL-dWellOiledMachine-110, TOOL-dWellOiledMachine-111, TOOL-dWellOiledMachine-112, TOOL-dWellOiledMachine-113, TOOL-dWellOiledMachine-114, TOOL-dWellOiledMachine-115.

## 10. Reuse audit

The seam reused is `build_commit` (`tools/unattended/lib-unattended.sh:1186`), the pass-order history
leg's one definition of the commit that built a unit, called through `read_conf_value` (`:780`) as it
stands. The probe `python tools/codebase-map/reuse_lookup.py "check that a spec amendment commit
landed before the unit's build commit"` ranked `build_commit` sixth, beside name-stem hits (`check`,
`before`, `build`) that are not this predicate; the recall query below ranked the round-4 report's
fix first among this build's records, TOOL-dTotalRecall-67 AC2's `merge-base --is-ancestor` between
pass commits, and TOOL-aRepatriatedFork-48, `build_commit`'s known early read, which §4 records.

Recall terms used: `python tools/memory-recall/query.py "how do we check that an amendment of a spec
landed before the amended unit built" --terms "amendment ordering ancestor build commit pass order
merge-base is-ancestor first pass spec revision"`

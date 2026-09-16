# Acceptance ledger — TOOL-aReplayedCard-4, the manifest traps eviction

**Serves:** journal TOOL-aReplayedCard-4

Every figure here was DERIVED by the pass at its base tree (`5a551aa5`, the branch tip the unit was
dispatched from) and re-measured at the staged landing tree; none is copied from the brief or the
design record. Where a figure the brief stated could not be reproduced, this record says so rather
than repeating it.

## The population, derived

Probe: `ANCHOR_RE` from `tools/memory-tree/gotchas.py` over every `- ` bullet of the manifest's
`### Environment traps worth front-loading` section at base, with continuation lines joined;
resolution by that module's `selectable` over `git ls-files`, because that is the predicate
check 19 and `--for-paths` apply.

- bullets in the section at base: 45, in 13033 bytes of section
- bullets carrying at least one anchor token: **22** — agrees with the brief and the design record
- of those, resolving to at least one tracked path under `selectable`: **19**
- of those, carrying an anchor byte-equal to a tracked path: **9**. The brief said 14 under a
  criterion it did not state; this pass could not reproduce that count and records its own two.
- the three `selectable` cannot resolve: the both-sides-rotated bullet (placeholders `<FAMILY>`),
  the `scratch-guard` bullet (`~/.claude` only), the new-gotcha-record bullet (`memory/gotchas/`,
  which `selectable` excludes by construction)

## Bullet → record, all twenty-two

The join is by CLASS (spec S1 at rev-2). Head of each bullet as it stood at base.

| # | bullet head | disposition | record |
|---|---|---|---|
| 1 | `tools/install-prefix-waivers.txt` is keyed `<path>:<line>` | DELETED — the catalogue already states it | `line-keyed-registry-reds-on-a-file-that-grew.md` (already named in the evicted sentence) |
| 5 | Two branches can BOTH rotate the backlog shard | NEW, shared with 38 | `row-driver-emits-a-plausible-file-with-rows-missing.md` |
| 11 | Editing the shipped `manifest-check.sh` | NEW | `shipped-checker-edit-is-an-adopter-contract-change.md` |
| 12 | The hooks kit ships TWO PreToolUse guards (`agent-cap`) | FOLDED | `concurrency-is-not-a-budget.md`, new closing section |
| 13 | `scratch-guard` is the second hook | FOLDED (S2: no tracked anchor; the tracked file it is about is `tools/hooks/scratch-guard.js`, which that record already anchors) | `allowlist-narrower-than-the-root-it-guards.md`, new closing section |
| 15 | A conf value interpolated into a REGEX | NEW | `conf-value-interpolated-into-a-regex.md` |
| 18 | Editing `.claude/settings.json` takes effect MID-SESSION | NEW | `settings-edit-takes-effect-mid-session.md` |
| 20 | `node --check <file>` is NOT a syntax gate | NEW | `node-check-is-not-a-syntax-gate.md` |
| 22 | `gen_build_index.py --check-format` grades TWO populations | NEW | `check-format-grades-two-populations.md` |
| 24 | Check 8's population is the backlog shards ALONE | NEW | `waiver-row-that-hides-nothing-reds.md` |
| 28 | A new tool at the REPO ROOT | STAYS in the manifest (S2) — its trigger is a path outside the tool root, which no anchor can express, and its only anchor is the bare tool root, which selects every kit file: the over-selection `TOOL-aWeighedCompass-14` measured | none |
| 29 | Adding ONE gate leg trips a SET of meta-gates | NEW, shared with 43 | `a-new-leg-trips-a-growing-set-of-meta-gates.md` |
| 32 | CRLF in a worktree is NOT limited to what a gate byte-compares | NEW, shared with 39 | `worktree-crlf-outside-the-gated-population.md` |
| 33 | A NEW record under `memory/gotchas/` needs `--write` and a claim | STAYS in the manifest (S2) — its subject is the one path `selectable` excludes by construction, so no record could be selected by the change it warns about | none |
| 35 | An arm must contain the branch's ENTIRE literal signature | FOLDED, shared with 36 | `arm-literal-strands-on-message-edit.md`, new closing section |
| 36 | A positional in a gate's `fail` message CANNOT be armed | FOLDED, shared with 35 | `arm-literal-strands-on-message-edit.md`, same section |
| 37 | Hygiene checks 13-15 ALONE are pin-gated | NEW | `pin-gated-checks-arm-nothing-without-a-pin.md` |
| 38 | `merge-rows.py` takes `%O %A %B` | NEW, shared with 5 | `row-driver-emits-a-plausible-file-with-rows-missing.md` |
| 39 | A HARNESS-CREATED WORKTREE carries CRLF | NEW, shared with 32 | `worktree-crlf-outside-the-gated-population.md` |
| 42 | Every NEW file under a build's record folders needs a `Serves:` line | NEW | `record-without-serves-or-with-a-round-counter.md` |
| 43 | A new CHECK inside the hygiene gate is far cheaper than a new LEG | NEW, shared with 29 | `a-new-leg-trips-a-growing-set-of-meta-gates.md` |
| 44 | The hygiene engine PRE-SETS its conf keys | NEW | `sourced-conf-blank-overrides-the-default.md` |

Totals: 12 new records; 3 existing records extended by 4 bullets; 1 bullet deleted as already
stated; 2 bullets kept; **20 bullets left the manifest**. Every new record is `kind: class`, none
is `universal`; the catalogue went from 49 to 61 records and stays at 5 universal against a budget
of 5.

## The manifest, measured

- `wc -c memory/guides/SESSION-KICKOFF.md`: 25597 at base, **20967** staged — 4630 bytes freed
- the twenty evicted bullets: 5553 bytes; the evicted-to-the-catalogue sentence gained 923 bytes
  naming the fifteen records they landed in; 5553 − 923 = 4630, so the whole difference is
  accounted for and the dated-corrections section is byte-identical
- the traps section: 13033 bytes at base, 8403 staged
- stamps: `last-audit` and `last-body-change` both at `c4f0230860daf81e2988f247ab29eea73a931dba`,
  the merge-base with `origin/main`, which is the rule for a branch; every remaining bullet is under
  check 11's 400 bytes, and the freed bytes are left free for `KICK-aReplayedCard-1`

**Evidences:** TOOL-aReplayedCard-4

- AC1 — `tools/memory-tree/gotchas.py` — `--for-paths` over one anchor of each of the fifteen
  records a bullet landed in (twelve new, three extended) printed all fifteen on the checklist, at
  the staged landing tree: `30 class(es) selected by an anchor + 5 universal`.
- AC2 — `gotchas.py --check` — exit 0 at the staged tree over 61 records, so checks 17, 18 and 19
  pass every new record; every one carries a `DECLARES_RE` phrase and no new record's anchors reach
  only append-only paths (`memory/archive/` appears once, beside `memory/backlog/` and the driver).
- AC3 — amended rev-2 — the byte bound is net of the bytes the evicted sentence gains, which S3
  itself requires; rev-1's "at least the bytes of the evicted bullets" was unreachable by
  construction. Observed under the amended form: `bash skills/session-kickoff/manifest-check.sh`
  exit 0, plain and `--staged`, and `wc -c` 20967 against 25597, a shrink of 4630 = 5553 − 923.
- AC4 — `codebase-map coverage + freshness` — `python tools/codebase-map/test_codebase_map.py`
  exit 0 after the twelve claims were added across seven dossiers and
  `gen_map.py --write` re-rendered `memory/map/generated/`; every new key is claimed.
- AC5 — amended rev-2 — the backlog flip is not this pass's write: `memory/backlog` is a
  `SHARED_RECORDS` member in `.unattended.conf` and `unattended.sh --dispatch` refuses a declaration
  overlapping one, so `memory/backlog/TOOL.md` rows `TOOL-aWeighedCompass-14` and
  `TOOL-aWeighedCompass-15` are the
  orchestrator's to flip in a records commit after this unit lands, with a note naming this unit.
  The facts that close them are in the manifest at base already: the pointer map's tooling row
  names the kit dirs a unit touches rather than the tool root, and the probe block names
  `tools/memory-recall/query.py`.

# Pre-code review, part 1 of 2 — the engine and safety units, DEPL-dCarriedReceipt-1..8

**Serves:** spec-audit DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8

**Reviewed:** all 19 specs of the build in one pass; this record carries the findings against units
1–8. Units 9–15 are part 2, `2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md`, and the
adopter units are reviewed in `d41ly/incms` under `memory/builds/dPinnedVintage/reviews/`. The
split is a rendering constraint, not an editorial one — see DEPL-dCarriedReceipt-16 in the backlog.
**Base:** `9ddcc5c9` (coding-governance, clean) · adopter trees inCMS `2bba21572`, NicoCares `d941b35`
**Harness:** 5 authors over disjoint unit sets against one fixed architecture contract, then 1
convergence auditor, then 5 default-refute lenses (buildability · acceptance · safety · scope ·
evidence), then a fold that re-verified the disputed quantities itself. 12 agents, all returned.

## Verdict: BLOCKED

Seven blockers across the build, each with a named edit. Four of them land in this half. The graph is
acyclic and every unit is individually buildable once they are fixed; this is a small number of
load-bearing holes, not a rewrite.

---

## The convergence question, answered

**No — the 19 specs do not yet describe one build.** The *vocabulary* converges, and that is the
build's strongest property: `gov_oid`, `oid`, `carry`, `verbatim`/`eol`/`relocate` and `forked` are
used identically in all 19 documents with **no synonym anywhere**, and both `-7` and `-8` reject a
stored `locally_modified` boolean by name. What does not converge is three of the architecture's own
ratified sentences — one owned by nobody, one contradicted across two specs, one double-owned. The
first and third are part 2's; the second is below as B2.

## Blockers in this half

**B2 — `-7`/`-8`: `gov_oid` is stored in one spec and recomputed in the other.** `-7` S3 makes it a
stored field read by the OURS axis; `-8`'s migration line says it is recomputed from
`blob_at(root, commit, source)` rather than trusted from the file. `cmd_update`'s preamble at
`:2940-2955` validates only that `--to` and `base_commit` resolve; there is **no** per-row check that
`gov_oid == blob_at(root, row["commit"], row["source"])`. `install.json` is a committed file and
`-11` rewrites `path`/`source`/`commit`/`gov_oid` together on a rename, so a text merge can pair
`commit` from one side with `gov_oid` from the other. A stale `gov_oid` that happens to equal the
target's live index blob reads the delta predicate FALSE and opens the raw-write arm on a row
carrying a local edit — `-8`'s own failure, reached from the other end. **Edit:** decide the field's
nature once in `-7` and make `-8` match; if stored, add the per-row integrity refusal beside the
existing unresolvable-commit refusal at `:2946`, give it a `refusal_join.py` arm, and add an AC that
hand-edits one `gov_oid` and observes the refusal.

**B5 — `-7` AC5 cannot be observed on the fixture it names.** `tools/memory-tree/kit.toml` declares
five `[[lf_pin]]` blocks → one `role:"attributes"` row each at `:1420-1424` →
`UPDATE_ROLE["attributes"] = "refuse"` at `:2864` → `r.fail` + `continue` at `:3009-3012` →
`if r.problems:` at `:3115` returns at `:3123`, **before** `receipt["schema"] = RECEIPT_SCHEMA` at
`:3125`. `install.json` can never read `"schema": 3` on that fixture until `-2` lands. §3's
land-alone defence rests on a `check-wiring` fixture (0 pins) that no AC touches. **Edit:** move
every AC onto the `check-wiring` fixture, or add `-2` to §3's dependency line and drop the
land-alone claim. Do not leave a land-alone claim resting on a fixture the ACs abandoned.

**B6 — `-4` AC2's calibration is unreachable by the command it names.** `resolve_selection`
(`:410-429`) branches on `all` / `kits` / `default_kits(reg)` and **never reads `deploy['kits']`**, so
`plan --target <NC>` with no `--kits` resolves the registry default set and prints 69 write rows, not
143. The full run also reconciles the four numbers circulating across `-4`, `-13`, ABL-2 and ARCH-1:
**181 plan rows → 143 writes → 136 role engine → 142 unique destinations**, i.e. exactly one
destination collision, which is ABL-2's "1 not installed at all" masked by a destination-keyed join.
**Edit:** name the full command in AC2, or make `--coverage` derive its selection from
`deploy['kits']`; state whether the report counts 143 rows or 142 destinations; and put the four-way
join into `-4` §4 so the other three specs stop disagreeing.

**B7 — `-4` AC3 and `-6` AC6 both assert a pre-`-1` world the landing order has already left.** In
inCMS, `.githooks/pre-push` IS tracked and `pre-push.test.sh` is not, and no root-level `pre-push` is
tracked. `push-main.kit.toml:19-24` declares both under `root_relative = true`, `to = "{relpath}"`.
After `-1` lands, `pre-push` resolves to a path inCMS holds: the gap count is **54, not 55**, and
neither row sits at the target root. `-6` AC6 has the mirror defect — its second inCMS hit is
`push-main.kit.toml:63`'s leg argv naming `.githooks/pre-push.test.sh`, which stops being a hit under
`-6` S3's own union predicate the moment `-1` lands, and `-6` §4 already says so. Both specs order
themselves after `-1` and then assert the before.

## The ranked remainder touching these units

`--to` is accepted on existence alone: `:2940-2944` validates it with `rev-parse --verify` and nothing
compares it to the receipt's `gov_commit`, so `update --to <older sha>` raw-writes every clean row
backwards and rewinds `receipt["gov_commit"]` at `:3126`. Two refusals belong in `-12` (descendant of
the receipt's commit; reachable from some ref), each with a `refusal_join.py` arm. Separately,
`RECEIPT_SCHEMA`'s own convention is that any unit adding a per-row field bumps it — `-7` bumps 2→3
for its two fields, then `-9` and `-13` each add one and both declare "Migration: None" with no bump.

## What is sound in this half — do not re-litigate

`-8`'s destruction sequence, verified end to end in source: `:3098` stamps `_sha(merged)` → the next
run's `classify_row` compares `_sha(ours)` at `:2889` and reads `o_state == "equal"` →
`VERDICT_GRID[("equal","differs")] = "stale"` at `:2845` → `dp.write_bytes(c["theirs"])` at `:3071`.
`-4`'s NicoCares calibration (143 write rows, gap 0) reproduces exactly. `-3`'s RED-first observation
— the literal at `:3206` overriding `--answer prefix=` — is real. `-6`'s underlying gov defect is
real: `push-main.kit.toml:63` names a leg argv no target tracks, a genuine silenced leg shipped to
every adopter. `-12`'s subject holds: `cmd_update`'s preamble at `:2930-2967` checks the target is not
gov, that a receipt exists, that both commits resolve and that every claimed kit is still a registry
entry — and nothing about index state, `MERGE_HEAD`, dirty paths or concurrency.

## What remains unverified in this half

`-6`'s element-versus-leg counts (the structural half is confirmed — `kickoff-manifest.kit.toml:60`'s
third argv element is a `/`-carrying leg subject — but the full predicate was not re-run over both
trees). `-8`'s fixture run and `-12`'s `MERGE_HEAD`-in-a-linked-worktree claim: both
mechanism-verified in source, neither fixture rebuilt. `-7`'s stated "four patterns across twelve
entries" does not hold — measured, it is 22 patterns across 11 of 25 registry entries — though its
conclusion (only 1 of 24 memory-tree engine rows falls under a pin) survives.

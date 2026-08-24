# Pre-code review, part 2 of 2 — the reach and adopt units, DEPL-dCarriedReceipt-9..15

**Serves:** spec-audit DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-10 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15

**Reviewed:** part 1 is `2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md` and carries the
convergence verdict, the harness description and the findings against units 1–8. This record carries
units 9–15. The split is a rendering constraint, not an editorial one — see DEPL-dCarriedReceipt-16.
**Base:** `9ddcc5c9` (coding-governance, clean)

## Verdict: BLOCKED

Three blockers land in this half, and two of them are the architecture sentences that nobody owns.

---

## Blockers

**B1 — `-9`: the rung→verdict contract is never stated, and the spec's three statements imply three
different write behaviours.** Found independently by four lenses. `VERDICT_GRID:2843-2853` maps
`("equal","differs") → "stale"`; the raw arm is `if v == "stale" or v == "missing":` at `:3069` with
`dp.write_bytes(c["theirs"])` at `:3071`. So if a proven rung moves `o_state` to `equal`, a stale
`relocate` row takes gov's **un-relocated** bytes, sets `oid == gov_oid`, and reports a clean write at
exit 0 — re-manufacturing the exact divergence this build exists to end.

**Resolution taken.** A proven rung sets `carry` for reporting and does **not** change `o_state`; the
verdict comes from the unchanged grid, and S6 applies the rung to `base` and `theirs` before
`three_way`. That still delivers the architecture's intent automatically: when `ours == rung(base)`,
`git merge-file` applies cleanly and emits `rung(theirs)` with zero conflicts and no operator turn. It
costs the ratified sentence only its literal word "write", needs no write-time transform so `-9` §3's
cut-line stands unedited, and it is the only reading that is safe when a rung is stale. The
architecture's third consequence becomes *"differ by a proven rung → automatic reconciliation to the
carried bytes, through the three-way"*. A rung row whose gov copy did not move classifies
`("differs","equal") = "patched"`, which is a **lie** for a relocate row — print it as
`carried (relocate)`, sourced from `carry`.

**B1b — the `missing` cell defeats both candidate fixes, and no lens named it.** `classify_row`
returns `o_state = "absent"` at `:2887-2888`; `VERDICT_GRID[("absent","equal")]` and
`[("absent","differs")]` are both `"missing"`; and `missing` is the *same* raw-write arm at
`:3069-3071`. A rung-carrying row the target deleted is restored with gov's **un-carried** bytes under
either fix, because there are no `ours` bytes to prove a rung against. **Edit:** the `missing` restore
arm derives `relocate` from the row's own `(dirname(source), dirname(path))` pair — which needs no
bytes and is exactly `-9` S3's derivation — and writes the carried form. Add an AC over a deleted
`relocate` row.

**B3 — role `forked` is defined twice, incompatibly, and `adopt` never binds a role to its
descriptor.** `-10` S5 makes `direction` and `record` **required** keys and its S4 printer reads
`direction` off every forked row; `-13` S7 and AC6 write forked rows with no `commit`, no `gov_oid`
and neither key. Worse: `how = UPDATE_ROLE.get(role)` at `:2974` keys on the **receipt's** role, and
`-13` has no scope item saying a destination whose RULE declares `forked` is recorded `forked`
regardless of the attribution walk. A fork has a common ancestor by construction, so `-13` S3's walk
attributes it at the pre-fork vintage, S4 matches `verbatim` there, and the row adopts as `engine`
with the raw-write arm **open** — `oid == gov_oid` on an exact coincidental match, so `-13` §5's "the
arm stays closed" does not apply. Payload verified: gov's `tools/memory-recall/extract.py` does
`import recall_conf` at `:55` and `CONF = recall_conf.resolve()` at `:57`, and inCMS's
`scripts/recall/` carries no `recall_conf`. **Edit:** the row's `role` comes from the rule
`resolve_entry` returned, never from the attribution outcome; an attribution failure gets its own
`evidence: "unattributed"` state so `forked` never carries two meanings; `-10`'s printer tolerates an
absent `direction` and the missing-key refusal is scoped to DESCRIPTORS.

## The ranked remainder

**`-14` wedges a target whose kit check was already red.** §4 rejects a baseline run, S4 runs the
check only after the write, S5 rolls back on any red, and S6's `r.fail` reaches `:3115` so
`gov_commit` never advances. An adopter with an unrelated local red reverts every correct write on
every run, forever. **Edit:** baseline the TOUCHED kits only — the population S4 already bounds — and
report red-before-and-red-after as pre-existing rather than rolling back.

**`-14` × `-11`: renamed rows are written, never verified, and cannot be rolled back.** `-14` S2
snapshots paths in `changed`/`deleted` and S4's touched-kit predicate uses the same two lists; `-11`
S4's `renamed` rows appear in neither, and a merged renamed row lands at a NEW path whose pre-write
snapshot is `absent` under the old key. `-14` F3's "does not conflict with `-11`" is false.

**`-11`: a renamed row's four-way rewrite has no stated byte outcome.** If `commit` advances,
`gov_oid` is gov's blob at the new path while `oid` is the old content, so `oid != gov_oid` for a row
nobody edited: `-8` closes the raw-write arm, the three-way runs with `base == theirs`, `merge-file`
returns ours, and the file freezes at pre-rename content forever while printing `patched` — the
engine's word for an adopter edit that never happened. If `commit` stays, `gov_oid` cannot resolve.
Neither outcome is stated and neither has an AC.

**`-15` §4's inventory reproduces under no predicate.** Six populations were measured (97/656,
86/594, 109/752, and three test-excluded variants); none is the spec's 93/534, and the backlog row's
"59 files" reproduces at no population either. §3 cuts scope on "not converting all 534 lines" and S4
sizes the ratchet on it. **Edit:** publish the exact predicate beside the table and derive both the
inventory and AC1 from the same code path that writes the ratchet file — the artifact is the
assertion. Relatedly, `-15` AC5 demands a count its own scope cannot reach: `lexicon.py` carries 7
`tools/<kit>/` literals, S5 touches four, and three are prose quoting a path as the subject of a
measured glob bug. After a correct S5 the count is 3 and AC5 reds.

## What is sound in this half — do not re-litigate

`-9`'s declared population: inCMS's `.governance/kits.json` carries exactly **92** file rows across
**14** kits with **16** `divergence` records. `-10`'s landmine payload, cited above. `-13`'s `intake`
facts — the existing-descriptor refusal at `:3186-3191`, the absolute `gov_source` at `:3204`, the
literal `prefix = "tools"` at `:3206`. And `-11`'s and `-12`'s shared flag test — *a scope flag
enables a narrower class of action, defaults OFF, and overrides no refusal* — which is a good rule,
correctly applied in both; the review asks only that `-13` be held to it too.

## What remains unverified in this half

`-9`'s rung yields (verbatim 21 / eol 6 / relocate 5 / none 20 over 52 resolvable rows) and its
disputed "27 green by identity, 17 flipped by a blanket rewrite" — the reviewer reproduced the 92-row
denominator but could reach 27/17 under none of eight populations, so treat that sentence as unsourced
until `-9` names its population. `-13`'s `evidence` semantics and the adopt walk's per-row yields.
`-9`'s `alpha` needle-map construction beyond its stated `(dirname(source), dirname(path))`
derivation. And whether the fixes interact: B1's resolution, B2's operand ruling and B3's role binding
all touch `classify_row`'s inputs, and were assessed individually rather than as a composed diff.

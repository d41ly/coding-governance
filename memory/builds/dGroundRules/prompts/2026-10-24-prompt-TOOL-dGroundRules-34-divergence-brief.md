**Serves:** research TOOL-dGroundRules-34

# Divergence brief — TOOL-dGroundRules-34, a batch the built branch overtook

## The prompt

> Its builder probed TOOL-dGroundRules-34 rev-6 at HEAD eb67e2cc8 and handed it back as a DIVERGENCE before writing anything. (1) S19 says `budgets-census-join` reads `unadopted` because unit 29's copy rule never applied, but `tools/policy/check_policy.py` copies the registry into that case's repository, so it reads `source`. (2) AC18 quotes `RED as planted`, which only the planted-seed loop prints; `budgets-census-join` reports through `print_checks` as `<scenario> · red naming it · …`. (3) S5/AC5 are already built: unit 30 (93e4b4d31) removed the `KIT_AGENT_CAP_VERSION` arm and the count already prints 0. (4) S21 is already built with a stricter rule: `derive_census_tree` rejects any `..` segment in the raw prefix, where S21's `posixpath.normpath` would accept `a/../b`. (5) AC26's grep prints 21 where `ORDER_ROWS | wc -l` prints 19, because it matches this spec's own probe text and unit 52's prose; unit 43's ORDERS spelling, filtered to status lines, is the working form. (6) S22's argv passes no `prefix` answer, so `intake` writes `prefix = "tools"` where unit 24 S4 requires the kit's tool-root name. (7) S30 is mostly built: `check-protocol-parity.test.sh` already quotes the first line after the FAILED header with its indent stripped. (8) `render_order` sits at `gen_build_index.py:1748`, not :1716, and the sibling-kit sentence at `map_lib.py:1504`, not :1505. Also, S20 replaces unit 31's AC4 staged `policy.py` without saying whether `adopt-policy.test.sh` arm 3b, which still arms the `exit 1` branch, stays.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S19 states that `budgets-census-join` reads `source` (the registry copy unit 29 put there stays), and restates whatever S19 still needs on that reading; AC18 quotes the line `print_checks` prints, `red naming it`.
2. S5 and AC5 are restated as already built by TOOL-dGroundRules-30, with the observation that confirms it; §4's per-file row for `check-protocol-parity.test.sh` drops S5.
3. S21 keeps HEAD's stricter rule (any `..` segment refused); loosening it to `posixpath.normpath` is refused, and S21 is restated as already built.
4. AC26 uses TOOL-dGroundRules-43's ORDERS spelling, filtered to status lines, so its count matches `ORDER_ROWS`.
5. S22 passes `--answer prefix=<tool root name>` to `intake`, so unit 24 S4 stays true.
6. S30 is restated against what `check-protocol-parity.test.sh` already does; only what remains is specified.
7. S20 states that `adopt-policy.test.sh` arm 3b stays, arming the `exit 1` branch.
8. Re-cite `render_order` and the sibling-kit sentence by symbol.
9. Leave AC11, AC12, AC15, AC16, AC32 and AC36 untouched; later units restate them.
10. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. The spec must stay at or under 48600 bytes measured with `wc -c` including its records region, which grows by about 300 bytes when this handoff is recorded: keep it at or under 48300, trimming prose outside §2 and §6 to pay for every byte added; every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); `wc -c` prints at most 48300; every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's per-finding statuses at eb67e2cc8 stand: S1, S4, S7-S10, S13, S23, S27-S29, S31, S33, S34, S36, S37 buildable; S17, S18, S35 already true.

### Reuse
TOOL-dGroundRules-43's ORDERS spelling for item 4.

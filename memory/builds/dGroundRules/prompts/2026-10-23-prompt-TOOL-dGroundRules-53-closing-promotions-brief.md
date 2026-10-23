**Serves:** research TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64

# Spec brief — dGroundRules, the closing review's promotions and the respelling repair

You author specs and write no product code. This is the build's SPEC RUN, closing under the owner's round-6 audit
cap (`2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md`): every unit is deferred and built by the build run,
and these specs close unaudited under a recorded `specs-audited` override. Read, in this order:

1. The closing review, `memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md`,
   whole: its HIGH, MEDIUM and LOW items, their Fix and Left-shift paragraphs, and the appendix entry of each finding id
   your units carry. Where the finder's fix was judged UNSOUND, the skeptic's corrected fix is the one to spec.
2. The original brief, `2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md`, for the shared interfaces, and
   `memory/TEMPLATE-SPEC.md`.
3. Each spec your unit repairs, whole.

## Every spec

- Path `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-<n>.md`; H1 `# TOOL-dGroundRules-<n> — <title>`.
- Status header `OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order <k>`, with
  `<k>` from 17 to 98 placing the unit after every unit it repairs; leave `closes` and `advances` out.
- `**Derived:** PLAY-dClosedLoop-2` on its own line after the status header.
- A `**consumes-from**` edge to each unit it repairs, and the reciprocal `**hands-off**` line added to that unit's
  spec as a rev bump with its §9 line, exactly as the audit disposals did.
- §6 criteria a pass can observe without a gate; a new suite arm on a `New arm:` line in §7.
- Before you return, run `python tools/check-spec-tokens.py` and leave no hit naming a spec you wrote or touched.
- Do not commit.

## The respelling defect behind H1, H2, M1 and unit 64

The main loop cleared spec-tokens path hits by respelling every flagged word in every spec's §6 to its basename.
Some flagged words were not witness paths but FIXTURE LITERALS a criterion runs verbatim: a sourced library, a
pair table's operands, a fixture tree's paths, a `rev:path` argument. Respelled, those criteria cannot pass. A
repair restores each literal's original meaning in a form the paths join does not grade, and never by basename: put
the literal in §4 (Design), which the join does not read, or in a form the join excludes (a glob, a `path:line`
citation, a token carrying a space), and have the §6 criterion run that literal by reference. Check each
restoration against `git log -p` of the spec where a committed revision still holds the original.

## The units

- **TOOL-dGroundRules-53 to -57** — item H1, one unit per raw finding: ids 5, 9, 12, 14 and 19 in that order.
  Each repairs the unit-44 defect its finding names.
- **TOOL-dGroundRules-58 to -60** — item H2, ids 4, 13 and 20 in that order: unit 45's PAIRS_TABLE and the
  criteria of units 40, 43 and 52 that route through it.
- **TOOL-dGroundRules-61** — item H3, id 1: rule 7 reads every settings layer the harness applies, in its precedence.
- **TOOL-dGroundRules-62** — item H4, id 8: one answer for `resolve` on an unset `budgets.<cap>` across units 9 and 21.
- **TOOL-dGroundRules-63** — the minors batch: M1 (ids 6, 15, 21), M2's left-shift gate (id 22; the packet
  re-render itself is the main loop's close step) and L1 (ids 7, 11, 18, 23), one scope item each.
- **TOOL-dGroundRules-64** — the adopted discovery: every stripped literal below that H1, H2 and M1 do not already
  cover, one scope item per spec. The inventory is machine-built from the main loop's flagged list, so verify each
  line; a line naming several originals is ambiguous and is resolved from the spec's own context or its history.

## The respelling inventory

- `21` line 424: `policy.toml` was `.governance/policy.toml`
- `25` line 424: `policy.toml` was `.governance/policy.toml`
- `29` line 147: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `29` line 148: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `29` line 151: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `32` line 355: `a.py"]` was `["tools/a.py"]`
- `32` line 355: `ab.py"]` was `["tools/ab.py"]`
- `32` line 355: `x.py"]` was `["tools/policy/x.py"]`
- `33` line 171: `selftest.py` was `{prefix}/govkit/selftest.py`
- `33` line 172: `selftest.py` was `{prefix}/govkit/selftest.py`
- `33` line 176: `selftest.py` was `{prefix}/govkit/selftest.py`
- `34` line 486: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `34` line 490: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `34` line 499: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `34` line 504: `x.py"]` was `["tools/policy/x.py"]`
- `34` line 504: `x.py"])` was `["tools/policy/x.py"])`
- `34` line 505: `a.py"]` was `["tools/a.py"]`
- `34` line 505: `ab.py"]` was `["tools/ab.py"]`
- `34` line 505: `ab.py"])` was `["tools/policy/ab.py"])`
- `34` line 505: `a.py"],` was `check_writes_intersect(["tools/policy/a.py"],`
- `34` line 509: `ab.py;` was `tools/policy/ab.py;`
- `34` line 509: `x.py;` was `tools/policy/x.py;`
- `34` line 509: `lib-unattended.sh;` was `tools/unattended/lib-unattended.sh;`
- `34` line 522: `policy.toml` was `.governance/policy.toml`
- `34` line 538: `selftest.py` was `{prefix}/govkit/selftest.py`
- `34` line 571: `f4d31452a:README.md` was `f4d31452a:memory/builds/dGroundRules/README.md`
- `39` line 129: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `39` line 140: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `39` line 142: `registry.toml` was `a/b/c/govkit/registry.toml` or `a/govkit/registry.toml` or `b/govkit/registry.toml` or `vendor/gov/govkit/registry.toml`
- `40` line 129: `x.py;` was `tools/policy/x.py;`
- `40` line 129: `lib-unattended.sh;` was `tools/unattended/lib-unattended.sh;`
- `40` line 130: `ab.py;` was `tools/policy/ab.py;`
- `43` line 231: `f4d31452a:README.md` was `f4d31452a:memory/builds/dGroundRules/README.md`
- `44` line 129: `ab.py;` was `tools/policy/ab.py;`
- `44` line 129: `lib-unattended.sh;` was `tools/unattended/lib-unattended.sh;`
- `45` line 124: `lib-unattended.sh;` was `tools/unattended/lib-unattended.sh;`
- `5` line 333: `policy.toml` was `.governance/policy.toml`
- `5` line 333: `HEAD:policy.toml` was `HEAD:.governance/policy.toml`

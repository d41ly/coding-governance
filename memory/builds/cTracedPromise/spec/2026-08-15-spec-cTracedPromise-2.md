# TOOL-cTracedPromise-2 — an acceptance criterion has to name something a machine can find

**Status:** OPEN · rev-3 · 2026-08-15 · node c · Tier-2 · base 37c05e1b · streams tooling

## 1. Goal

Make `## 6. Acceptance criteria` name concrete artifacts by rule rather than by habit: once a spec's
filename date reaches a new `SPEC_WITNESS_CUTOFF`, every acceptance bullet in it must carry at least
one backticked token. A forward ratchet, so no landed spec is retroactively red.

## 2. Scope (IN)

- **S1** — `SPEC_WITNESS_CUTOFF` declared in `tools/memory-tree/check-memory-hygiene.sh` beside
  `STREAMS_CUTOFF`, blank-defaulting to off, read from `.memory-tree.conf` by the same loader. It is
  DOUBLY gated: the branch sits inside check 12, whose outer guard is `[ -n "$SPEC_FORMAT_CUTOFF" ]`,
  so a repo with no spec-format ratchet gets no witness ratchet either — the same as the streams one.
- **S2** — a new branch in check 12's awk body. For a spec whose filename date is on or after the
  cutoff, walk the acceptance section and report every AC bullet containing no backtick pair. The
  head selector is `^[ \t]*(\-|\*)?[ \t]*(\*\*)?AC[0-9]+[a-z]?(\*\*)?[ \t]*([-.):]|—|–)?[ \t]` —
  list marker OPTIONAL, bold OPTIONAL, trailing punctuation OPTIONAL.
- **S3** — the rule applies on BOTH tiers, like the streams ratchet and unlike the section canon.
  Measured with the S2 selector, Tier-1 specs contribute 55 acceptance bullets, so this is a real
  claim; under a bold-requiring selector they contributed 18 and every Tier-1 spec in the tree
  matched zero, which would have made the claim decorative.
- **S4** — `SPEC_WITNESS_CUTOFF="2026-08-15"` in `.memory-tree.conf`, with the measurement and the
  reason in a comment.
- **S5** — the acceptance-section body of `tools/memory-tree/SPEC-TEMPLATE.template.md` states the
  rule, and the rendered `memory/TEMPLATE-SPEC.md` carries it identically.
- **S6** — three fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`: a post-cutoff spec
  with a witnessless AC reds and the message names the bullet; the same spec with a backticked token
  passes; a PRE-cutoff spec with the identical witnessless AC passes. The grandfathered fixture's
  filename date must sit strictly inside `[SPEC_FORMAT_CUTOFF, SPEC_WITNESS_CUTOFF)` — outside that
  window it would pass for the wrong reason, which is a fixture that proves nothing.
- **S7** — a fourth fixture: an UNBOLDED acceptance label (`- AC1. When …`) is judged, not skipped.
  This is the arm for S2's widened selector, and without it the widening is untested.
- **S8** — `KIT_MEMORY_TREE_VERSION` bumped, because a non-comment line of
  `tools/memory-tree/check-memory-hygiene.sh` moves and `tools/memory-tree/check-verdict-epoch.sh`
  gates exactly that. The bump moves SEVEN marker sites, not one — see the Inventory.
- **S9** — the five adopter-facing sites the `STREAMS_CUTOFF` precedent touches and an earlier
  revision of this spec missed: `tools/memory-tree/.memory-tree.conf.example`, the closing arming
  step in `tools/memory-tree/adopt-memory-tree.sh`, item 12 of
  `tools/memory-tree/HYGIENE.template.md`, `optional_keys` in `tools/memory-tree/kit.toml`, and
  `WIRE-INTO-PROJECT.md`.

## 3. Non-goals (OUT)

- **Checking that the witness EXISTS.** The gate reads shape: it asserts an AC names something in
  backticks, never that the named file, flag or test is real or that the build satisfied it. Stated
  the way `tools/memory-tree/check-method-carriers.sh` states its own structural bound, because a
  gate believed to check more than it does is worse than one nobody trusts.
- **Retrofitting the corpus.** Measured with the S2 selector: 181 of 774 acceptance bullets across
  the tracked corpus carry no backtick. Every one is grandfathered by filename date.
- **A check-arms-visible arm.** `tools/memory-tree/check-arms.py` scans the gate's SHELL source for
  `fail <n> "` call sites; an awk-internal `print` is not one. So this branch adds NO countable
  branch, `ARMS_FLOORS` does NOT move, and the meta-gate cannot reach this rule. **S6 and S7 are the
  only things that prove the branch can fire.** An earlier revision planned to raise the floor, which
  would have made the harness meta-gate permanently red.
- **A phrasing rule.** An earlier design required each bullet to open `**AC<n>** — When …`. Measured,
  it flagged 247 of 597 bullets on formatting variance — the corpus legitimately writes both
  `**AC1** — When` and `AC1. When`. It punished good criteria for punctuation and is dropped.
- **The strongest per-bullet predicate.** A witness-SHAPED token (path, extension, callable) flagged
  218 of 597 with false positives on `.map` and a `.txt` registry. A per-section anchor rule flagged
  2 specs of 75 — too weak to ratchet. The bare backtick is the middle that survived measurement.
- **A new gate leg or a new check.** The rule is a branch inside check 12, so the count stays at 20
  and `tools/gate-legs.json` is untouched.

## 4. Design

### Data model

No new data. One cutoff string threaded from `.memory-tree.conf` into check 12's awk invocation as
`-v wcut=`, joining `scut` and `cut10` which are threaded the same way.

### Inventory

| Item | Where | Change |
|---|---|---|
| `SPEC_WITNESS_CUTOFF` default | `tools/memory-tree/check-memory-hygiene.sh` | new, blank = off |
| `-v wcut=` and the scan | `tools/memory-tree/check-memory-hygiene.sh` | new awk branch inside check 12 |
| `KIT_MEMORY_TREE_VERSION` + its `gov:kit` marker | `tools/memory-tree/check-memory-hygiene.sh` | bumped |
| `gov:kit memory-tree@` markers | `HYGIENE.template.md`, `SPEC-TEMPLATE.template.md`, `BUILD-METHOD.template.md` and the three renders `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md` | moved together by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` |
| `SPEC_WITNESS_CUTOFF` | `.memory-tree.conf` | new key |
| `SPEC_WITNESS_CUTOFF=""` | `tools/memory-tree/.memory-tree.conf.example` | new key, shipped blank |
| arming step | `tools/memory-tree/adopt-memory-tree.sh` | beside the streams step |
| item 12 sentence | `tools/memory-tree/HYGIENE.template.md` | mirrors the streams sentence |
| `optional_keys` | `tools/memory-tree/kit.toml` | add the key |
| the conf key list | `WIRE-INTO-PROJECT.md` | add the key + its arming step |
| rule text | `tools/memory-tree/SPEC-TEMPLATE.template.md` + `memory/TEMPLATE-SPEC.md` | states the rule |
| four fixtures | `tools/memory-tree/check-memory-hygiene.test.sh` | red, green, grandfathered, unbolded |

`ARMS_FLOORS` is deliberately ABSENT from this table — see §3.

### Where the branch sits

Above the `if (hdr ~ /Tier-1/) next` early exit, beside the streams ratchet, because S3 puts it on
both tiers. The `fdate` it needs is already computed there for exactly that reason.

The scan walks `body[i]` from the acceptance heading to the next `## ` heading. A bullet's
continuation lines are indented, so the scan accumulates until the next head or the section end and a
backtick on a continuation counts toward its own bullet.

### What the message says

The `fail 12` heading names `SPEC_FORMAT_CUTOFF`, which is the wrong cutoff for this violation, so
the branch's own printed line names `SPEC_WITNESS_CUTOFF` and the offending bullet labels — following
the streams line at the same place, which spells out its own cutoff for the same reason. The wording
is held by a literal `hit '<text>'` assertion in `tools/memory-tree/check-memory-hygiene.test.sh`,
not by `tools/memory-tree/check-arms.py`, which never sees it.

### Alternatives rejected

- **A bold-requiring head selector.** It was the first draft and it is a hole, not a simplification:
  measured, it missed 159 of 774 acceptance bullets and saw ZERO bullets in 19 specs — including all
  seven specs of this node's own preceding build, which write `- AC1. When …`. Opting out of the rule
  would have been two asterisks, and `tools/memory-tree/SPEC-TEMPLATE.template.md` never asked for
  bold in the first place.
- **A cutoff earlier than today.** At `2026-08-14` the rule reds 7 bullets across 2 specs that landed
  under no such rule (6 in `cSteadyMetronome-1`, 1 in `cTracedPromise-1`), counted with continuations
  accumulated; head-lines-only gives 9. An earlier revision of this spec said 4, which reproduces
  under no counting rule at all.

## 5. Production-readiness checklist

- security — N/A. A read-only text scan inside an existing gate.
- perf / scale — one extra pass over the acceptance section per spec, inside an awk already reading
  the body.
- a11y — N/A. Gate output on a terminal.
- i18n — N/A. Backticks and ASCII labels only.
- error / empty / loading states — a blank `SPEC_WITNESS_CUTOFF` or a blank `SPEC_FORMAT_CUTOFF`
  disables the branch; a spec with no acceptance section or no AC bullets is silent, not red.
- observability — the message names the cutoff and each offending bullet label.
- risks — the shape-not-truth bound is §3 and is repeated in `memory/TEMPLATE-SPEC.md`, where an
  author reads it while writing the criteria. The meta-gate blind spot is §3 and is why S7 exists.
- testing + left-shift gates — four fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`.
  That harness is the ONLY arm: `tools/memory-tree/check-arms.py` cannot see an awk-internal branch.
- migration / rollback — blank the cutoff in `.memory-tree.conf`. No state, no data migration.
- user docs — the acceptance-section body of `memory/TEMPLATE-SPEC.md` and item 12 of
  `memory/HYGIENE.md`.

## 6. Acceptance criteria

- **AC1** — When a spec dated on or after the cutoff carries an AC bullet with no backtick,
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 and its output names that bullet's label
  and `SPEC_WITNESS_CUTOFF`.
- **AC2** — When that same bullet gains a backticked token, `bash tools/memory-tree/check-memory-hygiene.sh`
  exits 0, with no other fixture change.
- **AC3** — When the identical witnessless bullet sits in a spec dated `2026-08-02` — inside
  `[SPEC_FORMAT_CUTOFF, SPEC_WITNESS_CUTOFF)` in the harness's scratch tree —
  `bash tools/memory-tree/check-memory-hygiene.sh` is silent about it.
- **AC4** — When the offending label is UNBOLDED, as `- AC1. When …`, it is still reported; the
  fixture in `tools/memory-tree/check-memory-hygiene.test.sh` proves the widened selector.
- **AC5** — When `SPEC_WITNESS_CUTOFF` is blank, the branch is inert and the AC1 fixture passes; the
  same holds when `SPEC_FORMAT_CUTOFF` is blank, since check 12's outer guard already gates it.
- **AC6** — When `python tools/memory-tree/check-arms.py` runs it exits 0 with `ARMS_FLOORS`
  UNCHANGED at `tools/memory-tree/check-memory-hygiene.sh:14:14`, because the new branch is not a
  `fail` call site and raising the floor would red the meta-gate.
- **AC7** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs, it exits 0, so the engine
  change and the `KIT_MEMORY_TREE_VERSION` bump landed together.
- **AC8** — When `bash tools/check-kit-versions.sh` runs it exits 0: all seven memory-tree marker
  sites equal the bumped constant.
- **AC9** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, it exits 0: the rendered
  `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md` still equal the shipped templates.
- **AC10** — When the gate runs over `memory/builds/cTracedPromise/spec/2026-08-15-spec-cTracedPromise-2.md`,
  it passes. This spec is dated on the cutoff, so it is the rule's first live subject; two of its own
  bullets failed the rule on the first draft and were fixed, not waived.
- **AC11** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, every arm passes; when
  the new branch is deleted from the engine, that harness reds.

## 7. Gates

`memory hygiene (20 checks)` · `harness meta-gate (check-arms)` · `verdict epoch` ·
`kit/dogfood doc parity` · `method carriers` · `kit version markers` ·
`codebase-map coverage + freshness`, and the full bar at the push boundary.

## 8. Open questions

- **F1 — both tiers, or Tier-2 only?** RESOLVED (agent, 2026-08-15, delegated): both. Measured, the
  widened selector makes Tier-1 a real population of 55 bullets rather than the 18 a bold-requiring
  selector saw, so the claim is now testable rather than decorative.
- **F2 — is a bare backtick pair enough?** It admits `` `it` ``. RESOLVED (agent, 2026-08-15,
  delegated): yes, and §3 says so. Every stronger predicate measured worse on this corpus, and a gate
  whose false positives teach authors to work around it is worse than a weak one they respect.
- **F3 — should the cutoff be today or later?** RESOLVED (agent, 2026-08-15, delegated): today,
  `2026-08-15`. It is strictly ahead of every spec committed before it and EQUAL to this spec's own
  date, which is what makes this spec the rule's first live subject instead of leaving the population
  empty.

## 9. Revision log

- rev-1 · 2026-08-15 · initial draft, written against the three predicates measured over 597 AC
  bullets and the 43 specs that would have been retrofitted.
- rev-2 · 2026-08-15 · AC2 and AC9 rewritten: running the proposed predicate over this spec found
  both of them witnessless. The rule caught its own author, which is the first evidence it discriminates
  at all.
- rev-3 · 2026-08-15 · folded the M4 audit (`wf_f6c630a6-cf1`): 14 confirmed findings of 20 raised,
  one a blocker. The `ARMS_FLOORS` raise is deleted — `check-arms.py` scans shell `fail` call sites
  and cannot see an awk branch, so the raise would have made the meta-gate permanently red and the
  fixtures are the only arm. The head selector is widened off bold, which was a 159-bullet blind spot
  and a two-asterisk opt-out; S7 arms the widening; S3's Tier-1 claim becomes true as a result. Five
  adopter sites and six extra version-marker sites are added to the Inventory, the double gate on
  `SPEC_FORMAT_CUTOFF` is stated, the grandfathered fixture gains a date window, the printed line
  names its own cutoff, and the mis-measured "4 bullets" becomes 7.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "spec acceptance criteria gate"` and a read of
`tools/memory-tree/check-memory-hygiene.sh` put the seam inside check 12's existing awk body, beside
the `STREAMS_CUTOFF` ratchet: it already computes `fdate`, already receives its cutoff through `-v`,
already walks `body[i]`, and already runs on both tiers. No new file, no new selector population, no
new walk. A separate gate script was rejected for the same reason the streams ratchet is not one — it
would re-derive the spec population check 12 already holds. The `STREAMS_CUTOFF` rollout is also the
reuse target for S9: its twelve sites are the checklist this unit follows rather than rediscovers.

**Serves:** spec-audit DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11

# Spec audit, round 1 — the eleven inCMS-triage units of dGaugedVintage

**Round:** 1 · **Node:** d · **Streams:** deployer · **Base:** `d65da7ab` · **Date:** 2026-09-01 ·
**Graded:** the specs, never the code. The subject surface is `tools/govkit/govkit.py`,
`tools/check-kit-versions.sh` and `tools/check-install-prefix.sh`, read at this base only to decide
whether each spec's factual claims about this tree are true. Nine units are on the full ten-section
canon; `DEPL-dGaugedVintage-2` and `DEPL-dGaugedVintage-6` use the Tier-1 light profile
`memory/TEMPLATE-SPEC.md` permits, and were graded on the sections they actually carry. The evidence
base each unit was measured against is
[the triage](../build/2026-09-01-build-dGaugedVintage-1-incms-dossier-triage.md).

**Reviewed at these blobs:** `memory/builds/dGaugedVintage/spec/2026-09-01-spec-DEPL-dGaugedVintage-8.md@e391538b330d` · `…-3.md@5d3ddffacdf6` · `…-4.md@029ba864cc1b` · `…-5.md@bc4faea7595f` · `…-1.md@14a452de8f6b` · `…-9.md@b46943f72db1` · `…-10.md@0bfaffd27660` · `…-11.md@6613717b5e0b` · `…-7.md@b026a209eca7` · `…-6.md@68f8cafbb14f` · `…-2.md@04922e7a1eac` — all eleven re-derived with `git hash-object` at this base and matching.

## Verdict: BLOCKED

Four units cannot be built as written. Two of them rest on a mechanism that does not exist in the
code they name (`-9`, `-10`); one derives its assertion population from a set that structurally
cannot reach three of the eight sites its own table enumerates (`-4`); and one recommends, as an open
fork, the exact thing a ratified record already refused, citing nothing (`-3`). Nine further findings
are high, six medium, one low. `DEPL-dGaugedVintage-2` drew no finding at all.

The dominant class is not weak reasoning. The mechanisms are mostly right and the cut-lines mostly
real. It is that **eleven specs measured this tree by hand and seven got a measurement wrong**, each
time in the paragraph the spec itself nominates as load-bearing. That is the defect this build exists
to stop propagating, one level up.

## Review shape

raw 73 · confirmed 33 · refuted 40 · unverified 0 · precision 0.45

Precision sits below the charter's ~0.5 floor (§8), driven by five lenses over eleven documents that
share one subject: the same four measurement errors were re-reported by up to four lenses each. The
33 confirmed findings collapse to **20 distinct defects** after merging duplicate reports; the body
below is that merged set, and each entry names the raw ids it absorbed. Nothing was dropped in the
merge — a merged entry carries the strongest address and the union of the evidence.

| Unit | Blocker | High | Medium | Low |
|---|---|---|---|---|
| `DEPL-dGaugedVintage-1` | — | 1 | — | — |
| `DEPL-dGaugedVintage-2` | — | — | — | — |
| `DEPL-dGaugedVintage-3` | 1 | 2 | 2 | — |
| `DEPL-dGaugedVintage-4` | 1 | 1 | — | — |
| `DEPL-dGaugedVintage-5` | — | 1 | 2 | — |
| `DEPL-dGaugedVintage-6` | — | — | 1 | — |
| `DEPL-dGaugedVintage-7` | — | 1 | — | — |
| `DEPL-dGaugedVintage-8` | — | — | — | 1 (shared) |
| `DEPL-dGaugedVintage-9` | 1 | 1 | — | 1 (shared) |
| `DEPL-dGaugedVintage-10` | 1 | — | — | — |
| `DEPL-dGaugedVintage-11` | — | 2 | 1 | — |

---

## Blockers

### B1 — `-9`: the `version` field the whole unit reads is never refreshed by `update`

**Address:** `memory/builds/dGaugedVintage/spec/2026-09-01-spec-DEPL-dGaugedVintage-9.md` §4 Data
model, §3 non-goals, §2 S1. Raw id 58.

§3 says "The field is present and populated; only the reader is missing." That is false for every row
`update --write` has moved. Reproduced at this base: `_cmd_update` spans
`tools/govkit/govkit.py:5169-6317` and the string `version` does not occur anywhere inside it; its
three mutating branches refresh `row["sha256"]` and `row["commit"]` only. Every `"version":` write is
in `apply` (`:3964`, `:4032`, `:4056`, `:4093`) or `adopt` (`:6411`, `:6418`, `:6462`, `:6571`,
`:6599`), and `entry_version` is called at `:3995` and `:6403` and nowhere else.

This is not new. `memory/builds/aTetheredConvoy/reviews/2026-08-16-review-DEPL-aTetheredConvoy-1-3.md`
F6 reproduced it by bumping `KIT_CHECK_WIRING_VERSION` from 1.0 to 9.9 and running `update --write`:
the target's file on disk read 9.9 while the receipt row still read 1.0, against the NEW commit and
the NEW sha256. Nothing in `memory/DECISIONS.md` resolves it. So §4's claim that a row's `version` is
"what gov was at when this row landed" holds only for rows `apply` wrote, and the delta report `-9`
proposes prints a false "behind" for exactly the population an adopter runs it against — a maintained
target. AC1 and AC2 pass on a fixture while the field lies in the field.

**Fix.** Add an S4, or a §3 dependency on the unit that owns it, refreshing `row["version"]` in both
of `_cmd_update`'s mutating branches — recomputed alongside the hash and resolved through
`blob_at(root, to_commit, …)`, because `--to` can differ from `HEAD`. Cite aTetheredConvoy round-3 F6
in §4. Add an AC observing that a row `update --write` has refreshed reports level, not behind.

**Left-shift gate.** A `govkit` selftest arm that bumps a kit's version constant, runs `update
--write` over a fixture target, and asserts the receipt row's `version`, `sha256` and `commit` all
moved together. Staged RED first, which costs nothing here: it fails at this base today.

### B2 — `-4`: the derivation basis reaches five of the eight marker sites the spec enumerates

**Address:** `…-spec-DEPL-dGaugedVintage-4.md` §2 S1 and S3, against §6 AC1 and AC4. Raw id 39.

S1 derives each kit's marker population "from the entry's own resolved file set". For `drift-audit`
that set cannot contain `tools/workflows/drift-audit-code.js` or `-state.js`: the descriptor declares
`home = "tools/drift-audit"` with `include = "**"` (`tools/drift-audit/kit.toml:4`, `:10`), while
`tools/workflows/kit.toml` — entry id `review-harness` — claims those two files through its own `**`.
Both nonetheless carry `// gov:kit drift-audit@1.8` at `:15`. So S2's second direction — *a file
carrying a marker for an entry that does not claim it reds* — reds two correctly-valued markers that
§4's own table lists as drift-audit sites asserted today, while AC1 requires the leg to exit 0. Both
statements cannot hold.

One originally-reported site does **not** belong to this finding, recorded so it is not re-found:
`drift_signals.py` is `project-owned` (`tools/drift-audit/kit.toml:14-15`), but `resolve_entry` keeps
the project-owned row in `survivors` (`tools/govkit/govkit.py:304-306`), and this repo's own
precedent reads survivors — the file appears in `tools/install-prefix-carried.txt`. AC4 can name all
five stale `@1.4` files.

**Fix.** §4 must name WHICH resolution it means — `resolve_entry`'s `writes`, its `unlanded`, or
`entry_members` (`tools/govkit/govkit.py:356`), which claims non-landable and carved sources too —
and must state that cross-entry markers exist in this tree. Then either widen the basis to
`entry_members` plus a declared cross-entry allowance keyed to the recorded `TOOL-aScouredKit-26`
gap, or narrow §4's table and AC1/AC4 to the sites the chosen basis actually reaches.

**Left-shift gate.** A `govkit selfcheck` arm asserting that every versioned `gov:kit <id>@<n>` token
under `tools/` and `skills/` sits in a file some entry's declared basis resolves — with the basis
NAMED in the arm's own header, per §7's rule that a gate states what it does not check.

### B3 — `-10`: a commits-behind distance is not computable under the unit's own constraints

**Address:** `…-spec-DEPL-dGaugedVintage-10.md` §2 S1 and S2, against §3 bullet 1, §5 perf, and §6
AC2, AC3 and AC5. Raw ids 40, 18.

§2 requires reachability AND "how far behind" the measurer is; AC2 names a distance, AC3 refuses past
a bound, AC5 reports "the true distance without fetching". §3 forbids fetching and §5 budgets one
`git ls-remote`-shaped call. An advertisement returns a sha, not objects. On the stale clone this
unit exists to catch, `git rev-list --count <to_commit>..<remote_head>` dies with a bad-object error
and `git merge-base --is-ancestor` has no remote history to walk. The two design claims are mutually
exclusive: either the remote head is already local, in which case the `origin/main` comparison §4
rejects outright would also work, or it is not, and only equal/not-equal is obtainable. The unit's
motivating case is the second.

The precedent §10 leans on says the same thing and the spec never notices: `check-unattended.sh:655`
and `unattended.sh:747` are `ls-remote --symref --exit-code HEAD`, an identity observation that
computes no distance. It supports the binary form alone.

The sharpest consequence is in the fixtures. AC3 and AC5's fixtures keep the objects locally, because
rewinding a ref does not delete them, so those criteria go green where the feature already works and
never touch the stale clone the unit exists for.

**Fix.** Either reduce S1/S2 and AC2/AC3/AC5 to the answerable question — is `to_commit` equal to the
remote's advertised head, yes or no — and delete the declared staleness bound; or add a §2 item
permitting an object fetch scoped to the remote head
(`git fetch --no-write-fetch-head <remote> <head-sha>`), reverse the §3 non-goal that forbids it, and
price it in §5.

**Left-shift gate.** No predicate over spec text catches this, so it becomes a §10 recurring-class
entry: **an AC naming a derived quantity must name the command that derives it, and that command is
run against the FAILING fixture, not only the passing one.** The build's own "staged RED before it
lands" rule is the mechanical half; this is the half it does not cover.

### B4 — `-3` §8 F1 recommends what `DEPL-dCarriedReceipt-10` already ratified against

**Address:** `…-spec-DEPL-dGaugedVintage-3.md` §8 F1 and §2 S3. Raw id 59.

F1 recommends seeding a `forked` file on first install, "because the role already exists and carries
the right ownership semantics", and cites nothing.
`memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-10.md:74-76` reads, verbatim:
"**Not** teaching `apply` to install a forked file at first install either. A fork's whole claim is
that gov's bytes are wrong for the target, and that claim does not weaken because the target's copy
is absent." The same ruling is carried in code at `tools/govkit/govkit.py:247-252`, whose comment says
gov's bytes are wrong there "whether or not the target's own copy is absent".

`-3` §3 cites `DEPL-dCarriedReceipt-10` only for the ALREADY-HOLDS case, so a reader takes F1 as
genuinely open. Under §6's supersede-with-a-new-id rule, building F1's recommendation reverses a
ratified decision by silence.

**Fix.** Cite `DEPL-dCarriedReceipt-10` §3 and `tools/govkit/govkit.py:247-252` inside F1. Restate F1
as "reopen a ratified non-goal, or take the refusal branch", and move the seed option under §3 as an
explicitly-superseded alternative unless the owner ratifies the reversal with a new id.

**Left-shift gate.** A hygiene rule in the same family as check 18 ("a class declares its
resolution"): **every §8 fork carries a `prior:` line naming the record that last ruled on the
question, or the words "no prior ruling found" after a `memory-recall` query.** Presence is gateable
even though truth is not, and the absent line is what let this through twice in one build (see L1).

---

## High

### H1 — `-9`: `entry_version` returns a source line, so no ordering claim has a basis

**Address:** `…-spec-DEPL-dGaugedVintage-9.md` §4 Data model, against §6 AC1 and AC2. Raw id 46.

`entry_version` (`tools/govkit/govkit.py:333-353`) returns the whole matched SOURCE LINE via
`return ln.strip()` at `:352` — for example `KIT_CODEBASE_MAP_VERSION = "1.3"` — or one of the
sentinels `"(none declared)"` (`:341`) and `"(unresolvable)"` (`:345`, `:348`, `:353`). Never a
version value. Three consequences the spec does not carry:

1. AC1's "a version older than gov's" is an ORDERING claim over two source lines. It has no basis.
2. A cosmetic re-spelling of the constant's line reports a false delta where the version did not move.
3. Ten entries declare `version_from = { none … }` and therefore store the literal `"(none
   declared)"`, which string-compares equal to gov's and reports LEVEL under AC2 — indistinguishable
   from a real match. S3 covers only an ABSENT key, and §3's non-goal "Changing the receipt schema.
   The field is present and populated" forecloses the repair.

§4's citation `:333-347` also stops five lines short of the return it describes.

**Fix.** §4 states that the stored field is a source line. Then either declare the comparison
equality-only and delete "older" from AC1 and §1, or specify a parse from the line to a comparable
version with its stated failure mode. Extend S3 and §5's error states to treat `"(none declared)"`
and `"(unresolvable)"` as outcomes distinct from LEVEL. Correct the range to `:333-353`.

**Left-shift gate.** A selftest arm asserting that a receipt row storing `"(none declared)"` reports
`undeclared`, not `level` — the failing case observed RED first.

### H2 — `-11`: S2 is already shipped and already gated, so AC2 is green at base

**Address:** `…-spec-DEPL-dGaugedVintage-11.md` §2 S2, §4 Rollout and Alternatives rejected, §6 AC2.
Raw ids 41, 60.

The dropped set is already reported by name, in both verbs. `tools/govkit/govkit.py:5349-5353` prints
`govkit update — carry map DROPPED the ambiguous gov directory '<gd>': this receipt puts it at
<dests>…`; `:6431-6434` prints the same fact in `adopt` with its destination count. Both run before
the first row is classified, on the read-only path. `tools/govkit/selftest.py:3682` and `:4034` assert
it, the latter against the literal string.

This was resolved and built.
`memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-9.md` §8 F1 reads "RESOLVED
(agent, 2026-08-24, delegated): drop and report by name", its S7 landed the printer, and
`derive_carry_map`'s own docstring records the ruling at `tools/govkit/govkit.py:4807-4810`.

So AC2 passes today with no change — an acceptance criterion satisfied by an unrelated existing
green, which is the shape this build was convened to catch. §4's rejected alternative also mis-states
the gap: the RUNG is silent, the DROP is announced. §5's "S2 IS the observability half, and it lands
first for that reason" prices shipped work.

**Fix.** Narrow S2 to the one genuinely new behaviour — AC3's explicit zero-count line when `dropped`
is empty — and cite `:5349-5353` and `:6431-6434` in §4's Inventory as the existing report. Delete
AC2, or restate it as a regression check that the existing report survives S1. Re-price §4 Rollout so
S1 is the whole unit, and amend §3's `DEPL-dCarriedReceipt-9` non-goal to name §8 F1 as the
ratification S1 reopens rather than only "the rung and its re-proof-each-run discipline".

**Left-shift gate.** Generalize this build's own rule into the spec template: **every AC asserting new
behaviour is observed RED at the spec's declared base before the unit lands, and §6 records the
observation token.** `-3` AC4 already does this by hand; nothing requires it.

### H3 — `-11` §8 F1 keys off a seam `derive_carry_map` is ratified not to use

**Address:** `…-spec-DEPL-dGaugedVintage-11.md` §8 F1 and §6 AC4. Raw id 61.

F1 recommends keying on the `[[files]]` rule index "since `resolve_dests` already knows it", and AC4
observes "the pair `resolve_dests` returns on the S3 fixture". `derive_carry_map`'s docstring at
`tools/govkit/govkit.py:4791-4797` forbids exactly that, as a decision rather than an oversight: the
map is "NOT re-resolved from the descriptors" because `resolve_dests` and `rule_relpath` "answer for
the descriptor as it reads TODAY, while this map must answer for what the target actually installed,
possibly at a different gov commit and a different `prefix`".

The receipt makes it worse. A receipt row carries no rule index — row construction at `:6462` writes
path, role, kit, version and source, and `rule` exists on PLAN rows at `:275`. In `cmd_update`, whose
pairs come from the receipt, F1's key is obtainable only by re-resolving the descriptor, which is the
forbidden reuse. §3 claims the unit does not reopen `DEPL-dCarriedReceipt-9`'s discipline; the
recommendation does, and the spec never acknowledges the conflict.

**Fix.** Rewrite F1 to key off the receipt's own `(source, path)` pair — the sequence
`derive_carry_map` already receives — quote `:4791-4797` as the constraint, and restate AC4 as an
assertion over the pairs the caller feeds `derive_carry_map`, never over `resolve_dests`.

**Left-shift gate.** A `govkit` selftest arm: `derive_carry_map` called with pairs that disagree with
the descriptors as they read today must still return the target's installed map. It fails the moment
someone reintroduces descriptor re-resolution.

### H4 — `-1`: the include split is 10-vs-5, not 14-vs-1, and `hooks` is not a registry id

**Address:** `…-spec-DEPL-dGaugedVintage-1.md` §4 Inventory, sentence 2. Raw ids 5, 25, 56, 62 — four
independent lenses.

§4 says "Fourteen do so via an `include = \"**\"` rule; `hooks` names `agent-cap.js` explicitly", and
flags the sentence itself as load-bearing: "This is stated plainly because it changes how the unit
must be verified." Counted at this base, fifteen entries declare a `version_from` file. **Ten** reach
it through a `**` rule — codebase-map, drift-audit, lexicon, memory-recall, memory-tree,
playbook-render, pytest-parallel-guardrails, run-gates, unattended, review-harness. **Five** name it
in an explicit include list: `tools/govkit/entries/check-wiring.kit.toml:11`,
`kickoff-manifest.kit.toml:11`, `playbook.kit.toml:23`, `settings-merge.kit.toml:11`, and
`tools/hooks/kit.toml:12`. The registry's id at `tools/govkit/registry.toml:97` is `agent-cap`;
`hooks` is the directory, not an entry id.

The error runs the wrong way for the unit's own argument. The hand-written-include population is what
a future narrowing can break, and it is five times larger than stated, so the arm has MORE forward
value, not less. AC4 already stages its break into `check-wiring`, one of the five the inventory
denies exists.

**Fix.** Restate as ten via `**` and five explicit, name the five by entry id, rename `hooks` to
`agent-cap`, and say plainly that the five explicit-include entries are the live risk surface — which
is also why `check-wiring` is the AC4 fixture. No other section needs to move.

**Left-shift gate.** Make the count derived rather than typed: a `--measure`-style flag on
`tools/check-kit-versions.sh` printing the `**`-vs-explicit split, plus a spec convention that a
population count in §4 cites the command that produced it. That kills the class corpus-wide.

### H5 — `-3` points the builder at `LANDABLE_ROLES:236`, a shadowed dead literal

**Address:** `…-spec-DEPL-dGaugedVintage-3.md` §4 Inventory row 3 and §10 Reuse audit. Raw ids 14,
50, 63.

`LANDABLE_ROLES` is bound twice at module level: the hand-written `("engine", "seed")` at
`tools/govkit/govkit.py:236` and the derived
`tuple(k for k, v in ROLE_KINDS.items() if v == "write")` at `:1776`, which shadows it. `ROLE_KINDS`
itself is at `:1749`. Every read sits inside a function body, so all of them resolve to the `:1776`
binding and `:236` is dead. §10 pairs the two names against `:236` and `:1776`, so it points
`LANDABLE_ROLES` at the dead literal and mislabels the derived line as `ROLE_KINDS`; §4 row 3 cites
`:236` too.

§3's non-goal calls adding `forked` to `LANDABLE_ROLES` "the one-line change". At the effective site
that edit is `ROLE_KINDS["forked"] = "write"` at `:1749`. So the cut-line and the reuse audit both
describe a binding no code reads, and a builder who "fixes" it there ships a change with no behaviour
and a green bar.

The hazard is already recorded twice.
`memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-10.md:104-111` calls it out
verbatim "so the builder does not 'fix' S1 by editing the wrong line", and
`tools/govkit/govkit.py:2797-2801` says the same. `-3` cites neither and walks into it.

**Fix.** Repoint §10 at `ROLE_KINDS` (`:1749`) with `LANDABLE_ROLES` derived at `:1776`; restate §4's
row as "`ROLE_KINDS[\"forked\"] == \"forked\"`, so `LANDABLE_ROLES` excludes it (`:1749`, `:1776`)";
re-word §3's non-goal to name the `ROLE_KINDS` edit; and add a one-line note citing
`DEPL-dCarriedReceipt-10` §4 that `:236` is a shadowed duplicate and must not be the edit site.

**Left-shift gate.** A structural check over `tools/govkit/govkit.py` refusing a second module-level
binding of an already-bound module-level name. It deletes the trap rather than documenting it for a
third time, and its failing case is observable at this base today.

### H6 — `-7`: the acceptance fixture cannot match the arm the unit changes

**Address:** `…-spec-DEPL-dGaugedVintage-7.md` §1 Goal and §2 S1, against §6 AC1. Raw id 45.

`tools/check-install-prefix.sh` has two arms with two regexes. `RE` at `:63` matches the ROOT-prefix
form `<kit>/<file>.<ext>`, uses `grep -HnE`, and is waived per `<path>:<line>`. `re_ship` at `:201`
binds a literal `tools/` prefix, uses `grep -cHE`, and feeds the shrink-only ratchet. §4's Inventory
pins the change to `re_ship` and `tools/install-prefix-carried.txt` — arm 2 — while §1, S1 and AC1 all
say "root-prefix", which by the script's own vocabulary is arm 1's spelling and cannot match
`re_ship` at all.

AC1 prescribes a fixture of "two root-prefix literals … on one line", a string arm 2's regex never
matches, so the observation never exercises the changed code. AC1's "where today it counts one" does
not disambiguate either: `grep` prints a matching line once regardless of how many literals sit on it,
and the script's own comment at `:197-198` says so — "The count is hit LINES per path: a line carrying
two literals counts once." That sentence is equally true of arm 1, whose `<path>:<line>` waivers carry
the identical second-literal hole S1 leaves untouched.

**Fix.** §1 and §4 name the two arms separately and say the ratchet counts SHIPPING-prefix
(`tools/<kit>/…`) literals. AC1's fixture becomes two `tools/<kit>/<file>.<ext>` literals on one line.
Either extend S1 to arm 1's waiver granularity, or add a §3 non-goal deferring the identical class in
arm 1 and naming the unit that owns it.

**Left-shift gate.** A self-test fixture for `check-install-prefix.sh` carrying two shipping-prefix
literals on one physical line and asserting a count of two. RED at this base, which is the change.

### H7 — `-4` S2's reverse direction declares no population, and the real one is 35 files

**Address:** `…-spec-DEPL-dGaugedVintage-4.md` §2 S2, second direction. Raw id 48.

"A file carrying a marker for an entry that does not claim it reds" names no population. Run over the
tracked tree, `git grep -lE 'gov:kit [a-z0-9-]+@[0-9]'` outside `tools/` and `skills/` returns 35
files: `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `.claude/skills/lexicon/SKILL.md`,
`.claude/skills/unattended/SKILL.md`, three files under `memory/guides/`, the hook scripts under
`.claude/hooks/`, and roughly 28 build and review records. Rendered destinations carry
`role = "rendered"`, whose `ROLE_KINDS` value is a side-effect, so they sit in `unlanded` and in no
entry's resolved write set; the historical records sit in no entry at all. The arm reds on every one
of them, and not one is a wrong claim.

§5 prices only direction one — "one grep per entry over that entry's resolved file set" — so direction
two's cost and blast radius are unpriced, and §8 F2 addresses only the single `*.test.sh` instance
while the rendered-artifact class is larger and unmentioned.

**Fix.** Declare the reverse direction's population in S2 explicitly — the union of every entry's
resolved set, or the tracked surface minus rendered destinations and `memory/builds/**` — and carry it
into §4's Design. Add an AC observing that a rendered artifact carrying its own kit's marker does NOT
red, so the exclusion is gated rather than assumed.

**Left-shift gate.** The charter already holds the rule (§7: run a candidate gate predicate over the
real tree before wiring it, printing hits AND near-misses). Make it a spec-template requirement: a
scope item proposing a corpus-wide predicate carries its measured hit count at the declared base.

### H8 — `-5`: the affected population is five entries, not four

**Address:** `…-spec-DEPL-dGaugedVintage-5.md` §2 S1 and §4 Inventory, the four-row carrier table.
Raw id 2.

`tools/workflows/kit.toml:6` declares
`version_from = { file = "tier2-review.js", pattern = "version: " }` under entry id `review-harness`,
and the only marker in that file is `gov:kit tier2-review@1.4` at `tools/workflows/tier2-review.js:3`
— an id no registry entry uses. An id-scoped read (`gov:kit review-harness@`, which is what S1 defines
and what §1's deployer-grep framing requires) returns nothing for it. An id-agnostic read would
instead pass `review-harness` on `drift-audit-code.js`'s `gov:kit drift-audit@1.8`, which is precisely
the mis-claim `DEPL-dGaugedVintage-4` S2's second direction exists to red.

S2 is derived over every entry declaring a version constant, while S1 repairs four. The fifth entry
appears in no scope item, no §4 carrier row, no non-goal and no AC, and `why_two_ids` at
`tools/workflows/kit.toml:8` is free prose, not a marker-id declaration. Arming S2 reds a leg the spec
says lands green.

**Fix.** Either add a `review-harness` row to §4's carrier table and to S1, or add a non-goal naming
it and the follow-up that owns it. If the two-ids arrangement is deliberate, state it as a third case
in S2 with its own AC.

**Left-shift gate.** A `govkit selfcheck` arm: for every entry declaring a `version_from` file, that
file carries a `gov:kit <entry-id>@` token. Two entries fail it at this base — `review-harness` and
`playbook` (see M6) — which is what makes it a gate rather than an assertion about nothing.

### H9 — `-3` S3 has no acceptance criterion, and F1's own recommendation falsifies AC1

**Address:** `…-spec-DEPL-dGaugedVintage-3.md` §2 S3, against §6 AC1. Raw id 3.

§6 carries AC1 (S2's INCOMPLETE report), AC2 (the non-goal's no-overwrite property), AC3 (S1's
no-noise path) and AC4 (S4's gate RED). None grades S3. Worse, the two are in direct conflict: AC1
requires that on a scratch target holding no memory-recall files the entry be reported INCOMPLETE
naming `query.py` and `extract.py`, while F1's recommendation — seed on first install, since `seed` is
already landable — makes those files land, so the entry is complete and AC1 becomes unobservable.
§3's non-goal forbids only adding `forked` to `LANDABLE_ROLES`; it does not forbid re-roling those
rules to `seed`, so the fork's recommended arm is live. The acceptance matrix silently pre-commits to
the refusal arm of an explicitly unresolved fork. B4 is why that is the right arm — but it should be
committed to by citation, not by omission.

**Fix.** Split AC1 into the two branches F1 selects between and mark them mutually exclusive; or make
S2's INCOMPLETE report conditional on S3 resolving to "refuse" and add an AC for the seed branch:
"When S3 resolves to seed, `apply` over a fresh scratch target lands `query.py` and `extract.py` once
and a second run rewrites neither, observed by `git hash-object` before and after."

**Left-shift gate.** A memory-tree hygiene check over `builds/*/spec/*.md`: **every `S<n>` in §2 is
named by at least one criterion in §6.** Purely structural, cheap, and it catches the orphaned scope
item without pretending to grade the criterion's truth.

---

## Medium

### M1 — `-11` §4 Data model: every line citation is wrong

**Address:** `…-spec-DEPL-dGaugedVintage-11.md` §4 Data model. Raw ids 4, 27, 55.

Verified at `d65da7ab` and at `HEAD`; `git diff --stat d65da7ab HEAD -- tools/` is empty, so this is
not base drift. `derive_carry_map` spans `tools/govkit/govkit.py:4779-4842`, not `:4779-4844`. The
per-row dirname lift runs `:4826-4834`, not `:4833-4839` — `:4833` is a `continue` guard. The quoted
`dropped = [(gd, sorted(ds)) for gd, ds in sorted(lifted.items()) if len(ds) > 1]` sits at `:4835`;
`:4840` is `needles[gd] = td`, inside the needle-population loop. The quoted text is verbatim correct,
which is what makes the offset easy to miss: an implementer following §4 lands on the wrong mechanism,
and a reviewer checking `:4840` reads a different statement. §10's claim that the unit "modifies an
existing private seam" rests on the same mis-located reading, and the triage record carries the same
number.

**Fix.** `:4835` for the drop, `:4826-4834` for the lift, `:4779-4842` for the function. Add the
sibling `pairs_out` comprehension at `:4836-4837`, which discards the same fan-out keys and is a
second consumer S1 must change. Correct the triage record's `-11` bullet in the same commit.

**Left-shift gate.** A hygiene check over the spec corpus: a `path:line` citation adjacent to a
backticked quotation must find that quotation's bytes at that line. Narrow, mechanical, and it retires
the citation-drift class this build produced four times.

### M2 — `-6` §3 non-goal 2 excludes waiver rows that do not exist

**Address:** `…-spec-DEPL-dGaugedVintage-6.md` §3, second non-goal. Raw ids 12, 29, 53, 72 — four
lenses.

The non-goal excludes "the root-prefix waiver rows in `tools/install-prefix-waivers.txt` that name
this README". That file holds twelve rows, naming `.githooks/pre-commit`, `tools/check-wiring.sh`
(five), `tools/codebase-map/*` (three) and `tools/memory-tree/*` (three). None names
`tools/drift-audit/README.md`, and none could: the README's `cp -r` line spells no root-prefix FILE,
so arm 1 never reaches it.

A cut-line over an empty set is not a cut-line, and it displaces the real constraint. The thing S1
must not raise is the shrink-only carried-ledger row for this README, counted at 3 in
`tools/install-prefix-carried.txt:24` — a different registry with different semantics. AC2 names it
correctly; §3 never mentions it. Given the waiver file's own header — "A row whose spelling is gone
reds as stale" — a builder hunting the named rows would read their absence as someone else's deletion.

**Fix.** Replace the bullet with the measured fact: this README carries no waiver row, its constraint
is the carried-ledger count of 3, the repair may lower that count and must not raise it, and
re-measuring the ledger is `DEPL-dGaugedVintage-7`'s work.

**Left-shift gate.** M1's citation check, widened one notch: a spec sentence naming a registry file
plus a row selector is graded by grepping that file for the selector. It would have fired here on
`grep -n drift tools/install-prefix-waivers.txt` returning nothing.

### M3 — `-3` §3 non-goal 3 names an empty set, and the real population is one

**Address:** `…-spec-DEPL-dGaugedVintage-3.md` §3, third non-goal. Raw id 49.

"Auditing the other two kits with `forked` rules" carves out a set that does not exist:
`git grep 'role = "forked"' -- '*.toml'` returns exactly one hit, `tools/memory-recall/kit.toml:79`.
The consequence matters more than the phantom. S1's descriptor-derived detection and S4's gate would
run over a population of exactly ONE entry, and a gate whose predicate has one live instance certifies
nothing about the class it claims to fix. This repo already keeps a gotcha about that shape.

**Fix.** Replace the non-goal with the measured fact — one `forked` rule ships today — carry the count
as a measured row in §4's Inventory, and add to S4 a synthetic second-entry fixture so the gate
exercises the CLASS rather than the single instance.

**Left-shift gate.** Charter §7 already says to gate the class, not the instance. Make it a
spec-review item: a scope item introducing a gate declares its live-instance count at the base, and a
count of one requires a synthetic second fixture.

### M4 — `-3` §10 concludes "no existing seam fits" over two seams that already exist

**Address:** `…-spec-DEPL-dGaugedVintage-3.md` §10 Reuse audit. Raw id 51.

`resolve_entry` (`tools/govkit/govkit.py:282`) already returns `unlanded` rows carrying rule index,
source, destination and role, and `UNLANDED_REASON` (`:242-252`) already holds the per-role sentence
naming who produces the file instead — including "rendered: written by this kit's own adopter".
`_cmd_apply` calls both, `resolve_entry` at `:3992` and `UNLANDED_REASON` at `:4045`, and `_cmd_adopt`
calls the same pair.

So S1's detection — "every file that would carry its executable behaviour is withheld by a
non-landable role, derived from the descriptor" — is a filter over a role-annotated list both verbs
already build, and S2's report already has its reason strings written. §10's "No existing seam fits
the DETECTION", and its evidence that the reuse query returned "only generic writers — `write`,
`write_text`, `tracked_files` — none of which knows about roles", are both false, so the unit is
priced as new derivation work.

**Fix.** Rewrite §10 to name `resolve_entry`'s `unlanded` return and `UNLANDED_REASON` as the seam this
unit filters and reports over, and re-price S1/S2 accordingly. Keep the `reuse_lookup.py` evidence
line, but note it ranked writers because the query asked about landing bytes rather than about the
resolver's return.

**Left-shift gate.** Not a gate but a §10 method note: **a reuse query returning only generic
primitives is evidence the query was wrong, not that the seam is absent.** Re-query against the
resolver's RETURN before concluding absence.

### M5 — `-5`: codebase-map does emit a versioned marker, into its generated artifacts

**Address:** `…-spec-DEPL-dGaugedVintage-5.md` §1 Goal and §4 Inventory row 2, with §6 AC5. Raw id 52.

`codebase-map@{KIT_CODEBASE_MAP_VERSION}` is written by `tools/codebase-map/map_lib.py:1393`, `:1421`
and `:1462` into `memory/map/generated/inventories.json`, `symbols.json` and `MAP.md`; all three read
`codebase-map@1.3` in this tree today. `WIRE-INTO-PROJECT.md:770` documents the mirror and its
freshness gate, and `tools/codebase-map/selftest.py:512` and `:580` assert it. The comment at
`map_lib.py:46-47` that §4 quotes half of continues "…mirrored into the generated artifacts as
`codebase-map@<v>` so the deployer can grep the installed version".

So §1's "for these four that read returns nothing" is false for codebase-map, and §4's "none
versioned" omits the mechanism the bare token is explicitly a pointer TO. As written, S1 adds a second
hand-maintained spelling of a fact that is already generated and freshness-gated — the
one-fact-one-place rule the rest of this build applies.

**Fix.** Add the generated-artifact carrier to §4's table for codebase-map, and either move that entry
under the exemption S3 defines for playbook's separate convention or state in §4 why a `gov:kit`
marker must exist alongside the generated one. AC5 then observes the generated marker rather than
proposing an `@` on the pointer comment.

**Left-shift gate.** Covered by H8's `selfcheck` arm if it accepts a declared alternative carrier. The
declaration is what makes the exemption auditable rather than remembered.

### M6 — `-5` S3 asks for a declaration that already exists and is never read

**Address:** `…-spec-DEPL-dGaugedVintage-5.md` §2 S3. Raw id 70.

`tools/govkit/entries/playbook.kit.toml:6` already reads
`version_from = { file = "coding-governance-agents.template.md", pattern = "governance-template: v", kind = "marker" }`.
The `kind` key IS the exemption S3 asks for. Nothing consumes it: every `version_from` reader in
`tools/govkit/govkit.py` (`:339`, `:1049-1071`, `:1089-1093`, `:3454`) touches only `file`, `pattern`
and `none`. The `kind` reads at `:364` and `:1608` are the descriptor's top-level `kind = "flat"`, a
different key.

Written as "add a declaration", the unit adds a second key beside a live-but-unread one. Written as
"consume the declaration", it is a smaller change with a stated failing case. No non-goal covers this,
and the spec nowhere says the key exists.

**Fix.** Restate S3 as "consume the existing `version_from.kind = \"marker\"` declaration at
`tools/govkit/entries/playbook.kit.toml:6`", note in §4 that the key is declared and dead today, and
add an AC that a descriptor omitting `kind` is NOT exempted.

**Left-shift gate.** A `selfcheck` arm asserting every declared descriptor key is read by some code
path — the declared-population discipline §7 already applies to kits, applied to the descriptor
schema.

---

## Low

### L1 — `-8` §8 F2 and `-9` §8 F1 steer the same fork on a citation with nothing behind it

**Address:** `…-spec-DEPL-dGaugedVintage-8.md` §8 F2 and `…-spec-DEPL-dGaugedVintage-9.md` §8 F1. Raw
ids 36, 37.

`-8` F2 justifies "a phase of `update`, no new verb" with "`DEPL-dGaugedVintage-2` shows this repo
already struggles to keep verbs discoverable". `-9` F1 justifies "a flag on `update`" with
"`DEPL-dGaugedVintage-2` shows a new verb is a discoverability cost this repo has already paid once".
Read in full, `-2` is a backlog status sweep reconciling row status against spec status headers for
the `DEPL-dCarriedReceipt` units and `DEPL-aFerriedDossier-1`. Its title, S1 through S3, non-goals,
AC1 through AC4 and F1 contain no verb, no CLI surface and no discoverability claim of any kind.

Two specs steer one fork on the same empty citation, so an owner cross-checking either finds nothing.
Low because both recommendations are defensible on their own merits; the defect is the evidence, not
the conclusion.

**Fix.** Cite real evidence for the verb-discoverability cost, or drop the clause. If the intended
reference is this build's own finding that a five-lens manual audit ran where a verb should have
answered, cite that instead.

**Left-shift gate.** B4's `prior:` line, plus its corollary: **a §8 fork citing an id states in one
clause what that record says.** A citation that cannot be paraphrased has not been read.

---

## What this audit did not check

- **The code.** Every govkit line number, regex, marker and registry row cited above was read at this
  base to grade a spec's claim about it. No judgement is offered on whether the subject code is
  correct, only on whether the specs describe it truthfully.
- **Whether the eleven defects are worth fixing.** The triage's selection is taken as given.
- **`-2`'s fifteen status flips.** The build README parks them for the owner, and grading them would
  be making the judgement calls the build declined to make.
- **`DEPL-dGaugedVintage-8` beyond L1.** Its mechanism, criteria and cut-lines survived the pass; the
  fork citation is the only confirmed finding against it.
- **Anything the skeptic refuted.** Forty raw findings were refuted and are not recorded here. The
  0.45 precision is the honest cost of five lenses over eleven documents with one shared subject.

## The left-shift set, ranked by what it would have caught

| Gate | Would have caught | Where it lives |
|---|---|---|
| Spec citation check: a `path:line` beside a backticked quote must find those bytes at that line | M1, M2, part of H5 | memory-tree hygiene, over `builds/*/spec/*.md` |
| Every `S<n>` in §2 is named by at least one §6 criterion | H9 | memory-tree hygiene, structural |
| Every AC asserting new behaviour is observed RED at the declared base, with the token recorded | H2, and the AC-already-green class generally | spec template plus a §6 convention |
| `govkit selfcheck`: every `version_from`-declaring entry carries a `gov:kit <entry-id>@` token | H8, M5, M6 | `tools/govkit/govkit.py` |
| `govkit selfcheck`: every versioned marker under `tools/` and `skills/` resolves under some entry's declared basis | B2, H7 | `tools/govkit/govkit.py` |
| `govkit` selftest: `update --write` moves `version` with `sha256` and `commit` | B1 | `tools/govkit/selftest.py` |
| `govkit` selftest: `derive_carry_map` answers from its pairs, not from today's descriptors | H3 | `tools/govkit/selftest.py` |
| Structural refusal of a second module-level binding of an already-bound name | H5 | a run-gates leg over `tools/govkit/govkit.py` |
| `check-install-prefix.sh` fixture: two shipping-prefix literals on one line count two | H6 | that script's own self-test |
| §8 forks carry a `prior:` line, or "no prior ruling found" | B4, L1 | memory-tree hygiene, presence-only |
| Documented check, ungateable: an AC naming a derived quantity names the command that derives it, run against the FAILING fixture | B3 | the §10 recurring-bug-class checklist |

# TOOL-aMouldedFolio-1 — enforceable templates and generated documents: census, routes, recommendation

*2026-08-11 · node a · Tier 2 design pass, stage 1 (research) · base `af6de23` · stream tooling.*

*Research record for: can every load-bearing authored document be put under an ENFORCEABLE
template, and how much of each can move from authored to GENERATED? Scope covers this repo's
`memory/` tree, the root product docs, the shipped playbook template and its two companions, the
backfill of existing content, and migration for already-landed adopters.*

*Status: RECOMMENDATION — pre-build. No template, renderer or gate leg was written. The owner
ratifies the route in §8 before any spec is authored.*

---

## 0 · Method and how much to trust this

13 agents: 5 source-verification census lanes → 3 cross-cutting analysis lanes → 5 adversarial
verifiers. Every lane was instructed that a prose claim in a document is not evidence, and that
only source is. Claims were joined on orchestrator-assigned integer ids, never on echoed strings.

| | |
|---|---|
| Doc rows surveyed | 66 |
| Load-bearing claims judged | 109 |
| **Confirmed** (independently reproduced by a skeptic) | **92** |
| **Refuted** | **17** |
| Unverified / conflicting / spurious | 0 / 0 / 0 |
| Lanes or verifier batches that died | 0 |

The 17 refutations are in §9. They are not noise: they corrected a misattributed file, a false
enforcement obligation, three "this is the only kit that…" over-generalizations, and a garbled
count that a route would otherwise have inherited. **Anything in this record that a skeptic did not
reach is marked as such.** Five findings I reproduced personally at the terminal are marked ⊕.

---

## 1 · The finding that reframes the ask

The brief assumed the problem is *missing templates*. It is not. This repo runs the
template→render→byte-parity mechanism **five** times already (four claimed in `AGENTS.md`, plus
`adopt-drift-audit.sh`, which the census initially missed and a skeptic caught). The mechanism
works. It is also **green over documents that are false**, because it grades *sameness*, not
*truth*.

**Exhibit A — the shipped rule-set states a measured falsehood, under a green gate.** ⊕

```
memory/HYGIENE.md:218              ] byte-identical
tools/memory-tree/HYGIENE.template.md:218  ]
    "The pin is EMPTY today — 30 of 30 branches across both gates are armed"
```

Measured: `.memory-tree.conf:64` `ARMS_FLOORS` names **four** gates totalling **16+14+31+33 = 94**
branches. `kit-dogfood-parity.test.sh` → **exit 0**. The "pin is empty" half is still true; the
count and "both gates" rotted when the unattended kit added two gates. Every adopter installs this
sentence as their own committed rule set.

**Exhibit B — the generator launders an authored error into a machine-verified artifact.** ⊕

`memory/builds/aUnmannedHelm/README.md` declares `ids: TOOL-aUnmannedHelm-1`. That build has **7
spec files** and the backlog carries **11 rows** (`TOOL-aUnmannedHelm-1..-10`).

| Step | Site | Behaviour |
|---|---|---|
| declared | README front matter | `ids: TOOL-aUnmannedHelm-1` |
| validated? | `gen_build_index.py:76` | in `REQUIRED_KEYS` — **presence only**, never parsed |
| contrast | `gen_build_index.py:246` | `roster` **is** validated: split on `+`, checked against `FAMILIES` |
| rendered | `gen_build_index.py:269` | `fm['ids']` interpolated **verbatim** |
| result | the generated region | `**Build status:** CLOSED · **7 unit(s)** · … · **ids TOOL-aUnmannedHelm-1**` |
| propagated | `memory/ledger/2026-08.md:19` | same wrong value |
| copied again | `check-unattended.sh` check 8 | `RUN.md` byte-verified against that slice |

One generated sentence says *7 units* (derived, correct) and *1 id* (copied, wrong). I checked
whether anything else catches it: hygiene check 14 covers ids **cited but never defined** — this is
the opposite direction and has no check. `gen_build_index.py --check` → `clean (28 artifact(s))`.
Full hygiene suite → **exit 0**.

**The lesson both exhibits teach.** A parity gate proves two files agree. A freshness gate proves an
artifact matches a fresh render. **Neither proves a sentence is true**, and a generated region
inherits the truthfulness of its inputs. So the axis that matters is not templated-vs-untemplated;
it is **AUTHORED vs DERIVED, per section**, plus *is the derivation's input itself validated*.

Every stale claim found across five lanes sits in an authored sentence. Three of them sit inside
green parity pairs.

---

## 2 · The census

66 rows surveyed. Collapsed to the classes that matter:

| Class | n | Authored | Template | Generated | Shape gate | Verdict |
|---|---:|---|---|---|---|---|
| `HYGIENE.md` | 1 | full | ✅ | — | parity | **generate the check catalog + arms counts** |
| `TEMPLATE-SPEC.md` | 1 | full | ✅ | — | parity | **generate the skeleton + status grammar** |
| `guides/*.md` | 2 | full | ✅ | — | parity ×2 | keep; fix pair-4 (see §9) |
| `memory/README.md` | 1 | full | ✗ scaffold-once | — | **none** | template root-files only (§6) |
| build `README.md` — front matter | 25 | full | ✗ | — | presence | **template + validate — free** |
| build `README.md` — gen region | 25 | none | — | ✅ | check 9 | already correct; widen it |
| build `README.md` — prose | 25 | full | ✗ | — | **none** | **leave authored** (§3) |
| `DECISIONS.md` + `backlog/*.md` | 5 | full | ✗ | — | id shape only | **validator, 0 rows migrated** |
| `gotchas/<class>.md` | 12 | full | front matter only | — | checks 18/19 | presence canon: 1 file |
| `gotchas/INDEX.md` | 1 | none | — | ✅ | check 17 | already correct |
| `LIVE.md`, `ledger/*.md` | 3 | none | — | ✅ | check 9 | already correct |
| `map/features/*.md` | 5 | full | ✗ | — | key presence | 0-file backfill; generate counts |
| `map/generated/*` | 3 | none | — | ✅ | freshness | already correct |
| `AGENTS.md` | 1 | full | ✗ | — | shrink-only pin | **generate 2 enumerations** |
| `README.md`, `WIRE-INTO-PROJECT.md` | 2 | full | ✗ | — | **none** | pin, don't template |
| playbook template + 2 companions | 3 | full | ✗ | — | byte cap only | **no** (§7) |
| `MANIFEST-TEMPLATE.md` + ratchet | 2 | full | ✅ | — | ratchet | different shape — keep |

**Documents with no shape gate at all: 19 of 66.** The largest are `WIRE-INTO-PROJECT.md` (45 KB),
`parallel-coding-governance.domain-rules.md` (24 KB), and the entire authored body of all 25 build
READMEs.

---

## 3 · The build README — the priority case

**Measured across all 25** (⊕ mine, at the terminal):

- **Front matter is already a perfect contract.** `slug` `node` `opened` `streams` `roster` `ids`
  in **25/25**, plus `status:` on **6/25** (the sanctioned escape hatch when no spec carries a
  status header). Nothing needs migrating. It simply is not written down, and only `roster` is
  validated for content.
- **`ids:` is not "two readings" — it is two semantics across four separator spellings**: `..`
  ranges (`TOOL-aDrainedSluice-1..-9`), `/` (`-1/-2`), `·` between families (`aPrunedCeremony`),
  and plain space (`aSealedCaravan`). Reading A is "every id this build minted"; reading B is "the
  ids that are units of this build". Nothing chooses.
- **The prose has no shape to template.** `## Start here` in **3/25**. `**State.**` in **3/25**.
  Only **3/25** name a next action. **17/25 carry no `##` heading at all.** Body length runs 7→137
  lines and is bimodal: 13 of 25 are 7–12-line stubs, the live builds carry 40–137.
- **25/25 carry a well-formed `gen:build-index` marker pair.**

**Conclusion, and it cuts against the brief's instinct.** The build README splits into three parts
with three different answers, and only the middle one is a template problem:

1. **Front matter → template and validate.** Cost is near zero because the corpus already conforms.
   This is where the `ids:` defect lives and it is the single highest-value fix in the build.
2. **Mechanical prose → generate away.** Two blocks are restatements of machine-known facts: the
   `Node · opened · streams` line (15/25) and the `Records live under …` paragraph (13/25). Widen
   `render_region` and hygiene check 9 grades them for free.
3. **Narrative → leave authored and ungated.** A prose template would describe 8 files and invent a
   rule for 17. **Do not write it.** The entrypoint quality problem is real but it is an
   authoring-discipline problem, not a schema problem, and a template that 17 of 25 files violate
   on day one is decorative.

**The unattended coupling.** `check-unattended.sh` check 8 compares `RUN.md`'s generated region
against the README slice it copies. That coupling is sound *as a copy check* and it is exactly what
propagated Exhibit B's wrong `ids` into the run-state file. **Fixing `ids:` validation fixes the
RUN.md agreement automatically** — the two documents already agree; they agree on something false.

---

## 4 · Four enforcement shapes are already on the bar

The most useful thing the census produced. The route must pick per document, not pick one:

| Shape | Instrument | Catches | Cannot catch | Live examples |
|---|---|---|---|---|
| **Byte-parity** | render template → `diff` | live copy edited away from template | a false sentence in **both** | HYGIENE, TEMPLATE-SPEC, REVIEW-PROTOCOL, 2 Skills |
| **Freshness** | regenerate → byte-compare | artifact stale vs its source | a wrong **input** to the render | check 9, check 17, map/generated |
| **Ratchet** | re-attest + watch-pathspec | a watched input moved with no re-audit | anything unwatched | `manifest-check.sh` |
| **Shrink-only pin** | measured predicate vs pinned count | **omission**, drains one at a time | falsehood *inside* what it counts | `drift_report.py`, `ORPHAN_ID_PIN` |

Two consequences the route must carry:

- **Parity and freshness are truth-blind.** Both exhibits in §1 are their blind spot. Where content
  is derivable, *generate it* — that converts a truth question into a freshness question, which
  these gates do answer.
- **The pin is the right instrument for per-repo prose.** `AGENTS.md` is gated today only by
  `drift_report.py`'s `_charter_mentions_every_leg` — 7 unmentioned of 47 legs, pin 7, tolerance 0.
  It tolerates arbitrary prose and drains one bullet at a time. It gates **omission only**: two of
  `AGENTS.md`'s five stale claims sit *above* the section the probe parses.

---

## 5 · Grandfather vs backfill

This repo's no-backfill mechanism is date cutoffs plus five shrink-only registries. The analysis
found four things that constrain its use, all measured:

1. **A date cutoff is TOTAL EXEMPTION, not relaxation.** A pre-cutoff spec is dropped from check
   12's selection entirely — no status header, no skeleton scan, no canon, no empty-body check.
2. **`check 12`'s canon is EXACT EQUALITY, so a grandfathered file is FORBIDDEN to conform early.**
   Adding `## 10. Reuse audit` to a pre-`SPEC10_CUTOFF` spec **reds the gate**. That is why 0 of 11
   grandfathered specs carry §10: voluntary drain is mechanically impossible.
3. **The soft shape is the only one that has ever drained.** `streams` is validated-when-present,
   required-only-after the cutoff — and **15 of 33** pre-cutoff specs adopted it with zero gate
   pressure, against **0 of 11** for §10.
4. **`pop_guard` — the repo's own anti-vacuity guard — is blind to date vacuity.** It measures the
   population *before* the date filter, so a cutoff that governs zero files reports nothing.

**Only 2 of 8 doc classes carry a date key at all.** For gotchas, backlog, DECISIONS, dossiers,
guides and root docs, a cutoff would first require inventing and backfilling a date field — the
same file count as the migration it was meant to avoid. **The cheap option does not exist for them.**

Per class:

| Class | Verdict | Migration cost |
|---|---|---|
| Build READMEs | **GENERATE-AWAY.** Grandfathering is unacceptable | 25 files rewritten by `--write`, **0 authoring acts** |
| Backlog + DECISIONS | **Ship validator, no migration** | **0 rows** — 136/136 already key under `merge-rows.py` |
| Dossiers | Backfill at presence strength | **0 files** (1 if ordering is pinned) |
| Gotcha records | Backfill, presence canon | **1 file** (7 at exact-and-ordered) |
| Specs §10 | Backfill and retire the cutoff | 11 files + 1 engine edit + version bump |
| Root docs | Generate enumerations, pin the rest | 1 file, ~7 line edits |
| Guides | Nothing to phase in | 0 |

**Why grandfathering build READMEs is not on the table.** A cutoff would key on `opened:` — an
authored field, shape-checked, never cross-checked against git. The newest build opened 2026-08-10,
so a cutoff set today exempts **25 of 25**, including all 10 that `LIVE.md` links and that
`unattended.sh --preflight` reads on entry. And any author extends the exemption by typing an older
date.

**One caveat the analysis raised against itself, and it is right:** "generate-away costs 0 authoring
acts" holds only where the marker pair already exists. `apply_region` **raises** on a README with no
marker and no mode inserts one. Today's 25/25 is the result of that cost already having been paid.

---

## 6 · Adopters — the picture is not what the mention counts suggest

**inCMS is not an adopter.** `aLeasedGauntlet` spec:64 — *"inCMS did not adopt the kit"*; it keeps a
parallel `scripts/` copy and is the **upstream source**. ⊕ Of its 189 mentions, 109 are
provenance-shaped. Its migration cost for any change here is **zero**.

| | swydee | nicocares | inCMS |
|---|---|---|---|
| Status | the one real adopter | manifest-layer only | upstream, not an adopter |
| Recorded state | memory-tree **kit 1.4**, pre-flatten, 3 ledger rows, 0 build READMEs with front matter | manifest frozen at v1.0; **no kit-version record** | unmanaged prototype manifest, exits 0 by design |
| Cost of a doc-template change | **19 files / +6927/−301** behind at HEAD, 10 bumps in 7 days; already specced and BLOCKED | **UNKNOWABLE from this repo** — that is the finding | 0 |

**Delivery is broken, and that is what makes the change safe rather than any design property.**

- Delivery is a hand-run `cp -r`. There is exactly one push channel — the kickoff-skill junction —
  and it carries no kit. So `skills/session-kickoff/SKILL.md` edits are live on every machine
  instantly, while `manifest-check.sh` *in the same directory* reaches nobody until a human copies.
- **No version negotiation exists.** The only in-adopter version signal compares their manifest to
  their own checker copy. `check-kit-versions.sh` sits at `tools/` root, outside every kit dir, so
  `cp -r tools/<kit>` never delivers it. Nothing in an adopter can answer "is my copy stale".
- **Re-adopting memory-tree is a no-op.** `adopt-memory-tree.sh:49-52` exits 0 on any tree carrying
  the marker, without re-rendering and without reading the marker's version. So "re-adopt to get the
  new shape" is **false for the one kit that owns both existing doc pairs**.
- **The runbook never wires the parity gate.** `grep -c kit-dogfood-parity WIRE-INTO-PROJECT.md` →
  **0**. The flagship enforceable-template mechanism is enforced in this repo only. A fifth pair
  costs existing adopters nothing *because it is not on their bar* — the route must not claim it
  "enforces" anything cross-repo.

**Three consequences for the route:**

1. **Prototype where migration cost is provably zero.** `gate-lint`, `pytest-parallel-guardrails`
   and `unattended` — 17 tracked files — have no runbook `§`-step. The unattended kit additionally
   **cannot pass its own check 10 in any adopter**, because nothing installs
   `guides/UNATTENDED-PROTOCOL.md`. Fixing that is one `cp` and converts an unpassable gate into a
   working pair at zero adopter cost.
2. **Stamp the kit version into the render and byte-compare it.** That is codebase-map's move and it
   is the only mechanism here that turns a stale adopter copy into a red gate on their next run.
3. **No upgrade path is tested anywhere on the 47-leg bar.** Both "adopter e2e" legs build fresh
   throwaway repos; none installs kit N, upgrades, and asserts green. **Every migration cost in §5
   is therefore currently unfalsifiable**, including mine.

---

## 7 · Route A vs Route B vs Route C

**Route B — one declarative doc-contract engine — should not be built as stated.** Three sourced
reasons:

1. **Kit independence forbids it.** `check-protocol-parity.test.sh:8-12` already refused exactly
   this consolidation, in writing, because a shared gate hardcodes one kit's paths into another's
   shipped surface. The engine would have to be a new kit every kit depends on (an edge none of the
   11 have), or gov-internal and therefore shipped to nobody, or inline-duplicated and byte-gated —
   which is Route B's own copy problem one level down.
2. **"One leg validating all of them" is `two-answers-to-one-question`** — a class this repo refused
   **by name** on the bar. Route B would have to *replace* legs, not add one. That converts it from
   an addition into a migration.
3. **A schema expressive enough for the live shapes is a program, not a declaration.** The governed
   docs are validated today by at least a dozen distinct predicates, several of them literals inside
   the engines that own them.

**Route C is already the winning mode and deserves the name.** *Generate-only, no template* runs
today over `LIVE.md`, both ledger shards, `gotchas/INDEX.md`, `map/generated/*` and the region in
25 of 25 build READMEs — and **no census lane found drift in that class.** Meanwhile every stale
claim found sits in an authored sentence, three inside green parity pairs.

**So: Route A for the few documents that are genuinely per-repo prose, Route C wherever the content
is derivable, and Route B's renderer half only.** Concretely — unify the marker-region primitive
without adopting a schema. That primitive exists **four times** (`gen_build_index.py:285`;
`gotchas.py:253`, a **dead** twin nothing calls; `unattended.sh:75/:86`; `check-unattended.sh:119`)
and the two live ones **measurably disagree in both directions**: trailing text after a marker — awk
accepts, Python refuses; an indented marker — awk exits 3, Python accepts and silently rewrites it
to column 0. `unattended.sh:70-74` records that the transcription dropped an order check and
**deleted authored data**.

---

## 8 · Recommended route — for ratification

Ordered so each step's cost is paid by the step before it. **Steps 1–3 need no new gate leg**, which
matters: adding one carries six obligations (a `gate-legs.json` entry, a dossier claim, a `MAP.md`
regen, a kickoff re-stamp, an `AGENTS.md` bullet against a pin at tolerance 0, and — for a bare
`*.sh` with `fail()` — a sibling test).

| # | Unit | What it does | Cost | New legs |
|---|---|---|---|---|
| **1** | **Validate `ids:`, and widen the generated region** | Parse `ids:` against one ratified grammar; make the README's mechanical prose derived | 1 generator edit; 25 READMEs rewritten by `--write`; **0 authoring acts** | **0** (check 9 already grades it) |
| **2** | **Generate `HYGIENE.md`'s check catalog + arms counts** | `check-arms.py` already parses the exact keyspace; kills Exhibit A and the stalest prose in the shipped surface | 1 renderer; 1 template edit; branch-1 inside an existing pair | **0** |
| **3** | **Generate `TEMPLATE-SPEC.md`'s skeleton** | Canon is already a literal at `check-memory-hygiene.sh:482-496`; kills the nine/ten contradiction | same shape as 2 | **0** |
| **4** | **Row-grammar validator for backlog + DECISIONS** | Reuse `merge-rows.py`'s parser; ship with an empty registry and a 0 pin | **0 rows migrated** (136/136 conform); repairs the duplicate-id defect | 0–1 |
| **5** | **Unify the marker-region primitive** | Parametrize the Python markers, delete the dead twin, settle one well-formedness contract | 4 impls → 1–2; re-validate 25 READMEs + INDEX + 2 fixture sets | 0 |
| **6** | **Generate `AGENTS.md`'s gate-suite + kit roster** | From `gate-legs.json` and `git ls-files 'tools/*/*'`; drives the drift pin toward 0 | 1 file, 2 regions, 1 renderer; repairs 5 stale claims | 0 |
| **7** | **Adopter reachability** (optional, and the honest one) | Install `UNATTENDED-PROTOCOL.md`; stamp kit version into renders; add an *upgrade-path* e2e leg | 1 `cp`; 1 marker; 1 leg | 1 |

**Explicitly NOT recommended:** a build-README prose template (§3); a cutoff for any class lacking a
date key (§5); Route B's schema half (§7); and **any templating of the playbook template or its
companions** — see below.

**The playbook template stays as it is.** It sits at **32620/32768 — 148 bytes free** ⊕ under a
strict gate. `.customize.md` is already a deploy-time placeholder catalog, but its substitution is
**prose an agent is trusted to follow**, enforced by nothing. Adding a render step would spend bytes
the file does not have, and a generated region inside a byte-capped file makes the cap
non-deterministic. If the owner wants movement here, the funded move is the one already identified:
externalize the §-stub parentheticals into `.domain-rules.md`. That is a byte-budget decision, not a
drift decision, and it does not belong in this build.

---

## 9 · Defects found in passing

Confirmed, each with a witness, none fixed by this pass:

| # | Defect | Site |
|---|---|---|
| 1 | Shipped rule set states a measured falsehood under a green parity gate | `HYGIENE.md:218` == template:218 ⊕ |
| 2 | `ids:` unvalidated, laundered into a generated artifact and copied into `RUN.md` | `gen_build_index.py:76,269` ⊕ |
| 3 | **Append-only `DECISIONS.md` carries duplicate ids** — `TOOL-aUnmannedHelm-5` and `-6` twice each, different content, full bar green | `DECISIONS.md:22/26, 23/27` ⊕ |
| 4 | `TEMPLATE-SPEC.md` says both "ten canonical sections" and "nine-section canon"; shipped to adopters | `:6-7` vs `:16` |
| 5 | Parity gate's own usage header inverts its direction — `--render` rewrites the LIVE copy; running the fix the gate prints destroys a hand edit | `check-protocol-parity.test.sh:6` vs `:45` |
| 6 | `gotchas.py`'s `apply_region` is dead code — no caller anywhere | `gotchas.py:253` |
| 7 | Two render implementations differ: `tr -d "\r"` vs `sed 's/\r$//'` — a mid-line CR renders differently in an adopter than in the gate grading it | `adopt-memory-tree.sh:64` vs `kit-dogfood-parity.test.sh:58` |
| 8 | `memory/map/README.md` spells 5 root-install kit paths that resolve to nothing; both watchdogs structurally blind | `:4,5,16,22,34` |
| 9 | `AGENTS.md` — 5 stale claims incl. "two dossiers" (5) and "engine at kit 2.2" (2.4), the latter inside the clause saying not to trust that line | `:6-7, :76` ⊕ |
| 10 | Kickoff manifest's leg arithmetic garbled: "7 of 40 … leg 41" should read 40 of 47, leg 48 | `.claude/SESSION-KICKOFF.md:165` |
| 11 | `memory/README.md`'s scaffold emits 5 fewer directories than this repo's tree has — adopters get an incomplete index | `adopt-memory-tree.sh:74-83` |
| 12 | Unattended kit's check 10 is unpassable in any adopter — nothing installs the protocol's live half | `check-unattended.sh:241-242` |
| 13 | Two runbook pre-commit snippets are silent no-ops at the prefix the runbook itself prescribes | `WIRE:136-138, :366` |

**The 17 refutations that changed this record.** Worth reading before citing anything: the four-gate
paragraph is in the *kickoff manifest*, not `AGENTS.md`; a missing `ARMS_FLOORS` row is **silently
skipped**, not enforced; **no** parity leg ships all four arms (the census claimed every one did);
`codebase-map` is **not** the only self-announcing kit (memory-tree is too); `inCMS` is not an
adopter; and "the runbook carries fourteen false claims" is a garbled restatement inside a
gate-green build README — the defensible version is 14 confirmed defects in the *memory-recall
adoption surface*, from a review at precision 0.82.

---

## 10 · Open questions — owner calls, not research gaps

1. **Which `ids:` semantics is canon** — every id the build minted, or only its units? Reading A
   survives `aSealedCaravan`; reading B survives `aUnmannedHelm`. Unit 1 cannot start without this,
   and it also decides whether the range spellings (`..`, `/`, `·`) stay legal or normalize to one.
2. **Does unit 1 repair the 25 existing `ids:` values, or only validate new ones?** Validation-only
   reds the bar immediately on at least `aUnmannedHelm` and `aBatchedTribunal`. Repair is ~5 files
   of judgment, and the judgment is the answer to question 1.
3. **Is adopter reachability (step 7) in this build or its own?** It is the only step that adds a
   gate leg, the only one that touches `WIRE-INTO-PROJECT.md`, and the only one whose value is
   unmeasurable until an upgrade-path test exists.

**What this record does not know.** nicocares's install state is unknowable from this repo. No
migration cost stated here is falsifiable until an upgrade-path leg exists. And the prose-quality
problem in build READMEs — 22 of 25 not naming a next action — is real, named here, and
deliberately left without a mechanism, because the only honest mechanism is authoring discipline.

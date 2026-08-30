# wave2 — lens: is the machine-verified layer still true?

**Serves:** research TOOL-aScouredKit-1

## Verdict: CLEAN WITH FIXES

Subject: `memory/map/` (the codebase map), its generator `tools/codebase-map/gen_map.py`, its ratchet
`tools/codebase-map/test_codebase_map.py`, the inventory declarations in
`tools/codebase-map/map_extractors.py`, and the charter sentences that route sessions to them.
Reviewed at HEAD `66c4891c` on `branch/kit-adversarial-review-15ed31`, merge-base `14e21399`.

## 1. What the ratchet actually proves

Run at HEAD, all five assertions green:

```
$ python tools/codebase-map/test_codebase_map.py
ok   test_every_inventory_key_is_claimed_or_baselined
ok   test_dossier_prose_headings_pinned
ok   test_dossier_affordance_present_or_graced
ok   test_path_derived_keys_are_posix
ok   test_generated_artifacts_are_fresh
```

Read from `tools/codebase-map/test_codebase_map.py:79-147`, the gate proves exactly four things:

1. every key returned by an extractor is claimed by some dossier, by `FOUNDATION.md`, or is on the
   `baseline.toml` backfill — and no claim names a key that no longer exists (`:79`);
2. every dossier carries the pinned headings and a `## Reuse affordance` section (`:93`, `:102`);
3. no derived key carries a backslash (`:122`);
4. `generated/inventories.json`, `generated/MAP.md` and `generated/symbols.json` byte-match a fresh
   render (`:128`).

It proves **nothing about the prose**. Not one assertion reads a `## Constraints & why`,
`## Shared seams` or `## Gaps` sentence. It also does not care WHICH dossier claims a key: any
dossier may claim any key, and `memory/map/README.md:28` says overlap is legal. Those two holes are
where every finding below lives.

## 2. The grace lists — healthy, with one unwired drain

`memory/map/baseline.toml` holds 43 keys of the 181 the extractors enumerate (23.8%). It is
genuinely shrinking — measured by replaying its own history:

```
9eff763d 68 → 5f28bd0f 62 → a4caea91 61 → 9d41abb1 57 → 22f3e12c 54 → 5d2c32fe 50 → 3b5f9b11 43
```

The gate ratchets it in both directions (`cov.lazy_baseline` reds a baselined key that a dossier now
claims, `cov.stale_baseline` reds a row whose key is gone), so it cannot rot into permanence by
neglect. Its one documented exception (`baseline.toml:6-11`, the `template size <=32KiB` →
`<=48KiB` rename) is recorded honestly, including the admission that nothing enforces the rule.

`memory/map/affordance-exempt.toml` is `exempt = []` — nothing parked. But its own header (`:4`) and
`memory/map/README.md:11` both describe the drain as automatic: "a touch drops entries (map_diff
attribution)". It is not automatic. The only code that drops entries is
`tools/codebase-map/map_diff.py:76 _drop_affordance_exempt`, reachable only through the opt-in flag
`--drop-affordance-exempt` (`map_diff.py:218`). Grepping the whole tree for that flag outside
`map_diff.py` itself returns nothing — no gate leg, no hook, no adopter, no runbook step. In gov the
cost is zero because the list is empty; in an adopting repo the list is *seeded at adoption*
(`gen_map.py:162`) and there is no caller to drain it. That is the lens's canonical shape: a shrink
mechanism whose un-gracing command is invoked by nothing is permanent.

## 3. False sentences in the machine-verified layer

I checked every numeric prose claim across the 18 dossiers. Four are false at HEAD.

### 3.1 `memory/map/features/codebase-map.md:61-64` — both numbers wrong, in the paragraph that warns about it

> "- **Two feature dossiers so far.** 69 inventory keys still sit in `baseline.toml`, so coverage is
> ratcheted but not yet described. […] Read the live counts from `reuse_lookup.py`'s corpus header,
> never from this line — it is prose and this gap is exactly where prose rots."

Measured through the kit's own loader:

```
$ python -c "... m.load_map_tree(ext.inventory_ids()) ..."
BASELINE TOTAL 43
DOSSIERS 18
INV TOTAL 181
```

Two → eighteen. Sixty-nine → forty-three. The file's last commit is `be0ee6a7` (2026-08-16); the map
has grown nine-fold since and the dossier describing the map has not been opened once. The
self-aware disclaimer does not save it: the sentence is still read before the disclaimer, and its
pointer is wrong too (§3.5).

### 3.2 `memory/map/features/memory-tree-hygiene.md:1` vs `:31` — the file disagrees with itself, and both halves are wrong

Line 1 (the H1): "the **21-check** gate over the memory tree".
Line 31 (the body): "One shell engine over the tracked contents of `<MEMORY_ROOT>/`, **22 checks**".

The engine implements 23. `tools/memory-tree/check-memory-hygiene.sh:1120` heads its last block
`# ---- 23: every acceptance criterion of a CLOSED Tier-2 unit is EVIDENCED or AMENDED`, `:1167` and
`:1288` both emit `memory-hygiene: check 23 …`, and `:1122` states outright that "Every fail arm
below says 23".

`TOOL-aScouredKit-22` (`memory/backlog/TOOL.md:282`) already tracks `memory/HYGIENE.md` and
`HYGIENE.template.md` stopping at 22 — this dossier is a **third carrier** that row does not name,
and it is the only one of the three that contradicts itself inside one file.

### 3.3 `memory/map/features/install-prefix.md:107` — "Eleven rows today", and the registry it counts broke its own ratchet

> "- **The waiver registry is shrink-only but not zero.** Eleven rows today, in two classes […]"

`tools/install-prefix-waivers.txt` carries 12 non-comment rows (lines 9-20):
`grep -cvE '^\s*(#|$)' tools/install-prefix-waivers.txt` → `12`.

The second half is worse. The registry's own header (`tools/install-prefix-waivers.txt:2`) says
"SHRINK-ONLY: the count may fall, never rise", and `tools/check-install-prefix.sh:27-28` restates it
("the count may fall, never rise, so a new spelling cannot be waived away quietly"), and
`tools/playbook-kit-waivers.txt:12` restates it a third time ("which is shrink-only and can only
lose rows"). The count rose. At `5c83c180` (2026-08-20) the diff adds
`tools/check-wiring.sh:162  dual-spelling probe: scratch-guard fragment, both layouts` and takes the
file 11 → 12. Nothing enforces the count: `--write-ratchet` in that gate governs
`tools/install-prefix-carried.txt`, a different artifact, and no reader of
`install-prefix-waivers.txt` anywhere in the tree compares its row count to anything.

### 3.4 `memory/map/features/unattended.md:98` — "eleven named directives", the driver ships sixteen

> "**A run is bound by eleven named directives, and each is a POINTER.**"

`tools/unattended/unattended.sh:446` declares `DIRECTIVES_CORE` with sixteen `handle:carrier`
members (`minimal-prose sub-specced forks-resolved specs-reviewed reuse-first
parallel-when-disjoint passes-committed diff-reviewed land-once-done conflicts-reconciled
wrap-up-derived researched solution-tested pieces-recorded playbook-followed
discoveries-adopted`). `.unattended.conf:81` pins `DIRECTIVES_FLOOR="16"`, and
`tools/unattended/check-unattended.sh:1443-1444` reds if that floor sits below the driver's own core
count — so 16 is machine-asserted, and the dossier's 11 is machine-contradicted one directory over.
Replaying the driver, the set has been 16 since at least `8e2c7d90` (2026-08-27); the dossier's last
edit is `c2f1ab25` (2026-08-25).

### 3.5 `AGENTS.md:9` — the command the charter names for the live counts does not print them, and errors as spelled

> "Both counts move as dossiers land, so neither is spelled here — `python
> tools/codebase-map/reuse_lookup.py` prints the live pair."

Two independent failures.

As spelled it does not run. `reuse_lookup.py:394` declares `parser.add_argument("query",
nargs="+")`, so:

```
$ python tools/codebase-map/reuse_lookup.py
usage: reuse_lookup.py [-h] query [query ...]
reuse_lookup.py: error: the following arguments are required: query
```

Given a query it still does not print the advertised pair. The corpus header is:

```
# corpus: 588 symbols | 177 inventory keys | 19 affordance seams | 18 dossiers
```

"18 dossiers" is right. The other half of the charter's "pair" is "the keys not yet claimed by one",
which is 43 — and 177 is neither that nor even the true inventory total. 177 is the count after
deduplication across inventories; the inventories hold 181 keys, with `drift-audit`, `lexicon`,
`memory-recall` and `unattended` each appearing in both `kits` and `rendered-skills`. So a session
following the charter either gets a usage error, or gets a number four times the one it was told to
read. This is the only place either count is supposed to be obtainable.

`memory/map/features/codebase-map.md:63-64` points at the same header for the same purpose, so the
bad pointer has two carriers.

## 4. Nothing refreshes dossier prose, and the build that just landed proves it

`AGENTS.md` §1 Definition of Done: "Codebase map adopted (§5)? New inventory keys claimed in the map
tree (machine-enforced); **dossier prose refreshed on touch**; claim edits regen the generated
artifacts in the same commit." The parenthetical is doing all the work — the key half is
machine-enforced, the prose half is not enforced by anything, and it is the half that decides
whether the layer is true.

The aScouredKit build (16 commits, `14e21399..66c4891c`) changed 59 files. Its own map digest:

```
$ python tools/codebase-map/map_diff.py 14e21399..HEAD
# map-diff … — 59 files, mapped 13/59 (22%)
## govkit — 6 file(s)
## install-prefix — 1 file(s)
## playbook-mode — 1 file(s)
## review-harnesses — 2 file(s)
## unattended — 4 file(s)
```

Five dossiers own files the build changed. `git diff --name-only 14e21399..HEAD -- memory/map/`
returns **zero**. Not one dossier was opened. The map's ratchet was green throughout, because no
inventory key moved.

The consequence is not hypothetical. Two of the four false sentences in §3 sit in dossiers on that
list (`install-prefix.md`, `unattended.md`). And `memory/map/features/govkit.md:115-117` opens its
Gaps with "Named rather than assumed, because a deployer that is quiet about its own holes is the
thing this unit exists to replace" — while this same build measured and filed
`TOOL-aScouredKit-24` (`memory/backlog/TOOL.md:284`): eleven of govkit's 25 registry entries are
never passed to `apply` by any gate, and the `deployability.test.sh` that `DEPL-aTetheredConvoy-3`'s
CLOSED AC7 requires has never existed. A dossier that declares its holes are named, with a measured
hole from the current build absent from it, is the disclosure claim failing rather than the
disclosure being incomplete.

## 5. Coverage holes the premise cannot see

### 5.1 Ten shipped deployables are in no inventory at all

`tools/codebase-map/map_extractors.py:39-52 _tool_kits()` enumerates "Every kit directory directly
under tools/" — directories only. That yields the 15 keys in the `kits` inventory. But
`tools/govkit/registry.toml` declares **25** deployable entries, ten of which are single files or
non-`tools/<id>` homes: `check-line-length`, `check-microformats`, `check-placeholders`,
`check-testsuite-counts`, `check-wiring`, `push-main`, `check-kit-versions`,
`check-agent-cap-restatement`, `check-install-prefix`, `settings-merge` (registry lines 40, 44, 92,
122, 127, 132, 137, 142, 147, 117). There are 33 tracked files sitting loose directly under
`tools/`; none is a key in any inventory. Adding an eleventh single-file gate under `tools/` adds
nothing the ratchet can fail on.

Meanwhile `memory/map/generated/MAP.md:5` advertises itself as "Every machine-enumerable moving
part, annotated with its claimant". A session using MAP.md to answer "what is this repo made of"
gets 15 kits and misses ten shipped gates. Note the asymmetry: govkit's own surface predicate
(`memory/map/features/govkit.md:56-62`) DOES span depth-1 loose files in both directions. The
deployer's ratchet is strictly stronger than the map's, and the charter routes sessions to the map.

### 5.2 Six kits, including `drift-audit`, have no dossier

`kits` keys still on the baseline: `agent-instructions`, `drift-audit`, `gate-lint`, `lib`,
`pytest-parallel-guardrails`, `workflows` (`memory/map/baseline.toml:36-43`). The conspicuous one is
`drift-audit`: five of its keys are baselined (the kit, the rendered skill, and gate legs
`drift-audit records`, `drift-audit selftest`, `drift-audit wiring`) and it has no dossier at all,
while `AGENTS.md` names `python tools/drift-audit/drift_report.py` as the first thing to run when
the build feels like it is drifting — the exact question that commissioned this review. It was also
the most-touched kit in the build that just landed (7 files). The feature the drift question routes
through is invisible to the layer sessions are told to trust.

### 5.3 The kickoff engine's key is owned by the wrong dossier

The `skill-engines` inventory has two keys. `memory/map/generated/MAP.md:142` renders
`session-kickoff | unattended`. `memory/map/features/unattended.md:15` claims
`skill-engines = ["session-kickoff"]`; `memory/map/features/session-kickoff.md:15` claims
`skill-engines = []`. So the dossier NAMED for the kickoff engine owns none of the engine keys, and
a session resolving ownership through the map is routed into 16 KB about unattended runs. The gate
cannot see this — any dossier may claim any key, and it did not check redundancy or fit. This is not
the legal multi-claim overlap the README sanctions; it is a sole claim in the wrong file.

## 6. Interrogating the Tier-0 baselines

Re-ran at HEAD to confirm the handover numbers; identical. Three of the rows deserve comment.

**`dangling_pointers_in_own_ledger -1 / 0 DEAD PROBE` — permanently dead, and its message
misdirects.** `tools/drift-audit/drift_report.py:1380` sets
`self.ledger_dir = root / self.memory_root / "project" / "in-flight"`, and `:595` reads
`ctx.ledger_dir / f"{tag}.md"`. That directory was deleted when the per-node session ledger retired;
`tools/drift-audit/drift_signals.py:103-105` says so in as many words for the SIBLING signal
(`ledger_rows_contradicting_git`), which was added to `DECLARED_EMPTY`. This one was not. It will
print DEAD PROBE forever, and its detail reads `{"note": "no ledger file for node a"}` — which sends
an operator looking for a file that is not supposed to exist, rather than telling them the feature
retired. The probe is honest about being dead (good), but nothing in the tree explains why, and it
is not a signal any more.

**`handkept_inventories_disagreeing_with_source 0 / 0 EMPTY BY DECLARATION` — honest, but its pin
comment is false.** `drift_signals.py:158` sets `HANDKEPT: list[dict] = []`, retired deliberately
with the reasoning at `:147-157`. That is clean. But `PINS` still carries
`"handkept_inventories_disagreeing_with_source": 0` with the comment (`drift_signals.py:196-199`):
"DRAINED to 0: all seven were SELF-TESTS whose parent gate was cited but whose own script path was
not; **the charter now names them in one bullet, so every leg on the bar is spelled there**." The
charter does no such thing at HEAD — `AGENTS.md` now reads "**The leg list is `tools/gate-legs.json`.
Read it there and nowhere else.**" and explains that the enumerating section was deleted. The
retirement note 40 lines above says the same. Two answers to one question, inside one file.

**`shrink_only_lists_not_shrinking 2 / 5` — the population is a hand-kept declaration and it misses
more than half the tree's shrink-only lists, including the one that broke.** `SHRINK_ONLY`
(`drift_signals.py:78-88`) names five files, all under `memory/project/`. Grepping the tree for a
self-declared shrink-only rule finds at least twelve data files carrying one, of which these are NOT
watched:

- `tools/install-prefix-waivers.txt:2` — and it grew 11 → 12 at `5c83c180` (§3.3)
- `memory/project/testsuite-count-waivers.txt:2` — in the very directory the declaration's own
  comment cites as the population
- `tools/dead-path-waivers.txt:27`
- `tools/agent-cap-restatement-waivers.txt:2`
- `tools/lexicon/lexicon-verb-waivers.txt:2`, `lexicon-suffix-waivers.txt:4`,
  `lexicon-layer-waivers.txt:4`
- `memory/map/baseline.toml:3`, `memory/map/affordance-exempt.toml:3`

The signal's `of` is derived from the table and printed honestly; the table itself is the hand-kept
half, and its own comment (`drift_signals.py:66-71`) records that it has already been wrong twice
about its own scope. The one list that demonstrably broke its promise is outside it.

**`readme_mechanism_drift 24 / 79`** — a number about that class is also mis-stated in prose:
`memory/project/readme-contract.txt:13-14` says "This repo's own drift audit reports **three of
five** such lists out of tolerance today, which is the evidence for making this one an equality."
The live report says two of five. Written at `94b6195f` (2026-08-25) and not re-derived since; it is
a count of a derived population written in prose, which `AGENTS.md` §7 bans by name.

## 7. What I could not refute

- `memory/map/features/run-gates.md:63` — "Seven of the 86 legs name a network verb in their own
  script". The 86 is correct (`tools/gate-legs.json` holds 86 legs). The seven is a stamped
  measurement (2026-08-20) against an unstated predicate; my own predicates returned 4 and 25
  depending on the regex, which refutes nothing. Left alone.
- `memory/map/features/agent-cap.md:112` cites `MAX_LENSES = 6` while `tools/hooks/agent-cap.js:119`
  holds 5 — but the sentence is narrating the historical off-by-one, not the current value. Not a
  finding.
- `memory/map/features/build-readme-surface.md:64` — "Eleven build READMEs carry the pair" quotes a
  reproduction command with its grep pattern elided, so I could not re-derive it. Left alone.
- `map_extractors._read_lexicon_verbs()` (`:139-166`) has a bare `except Exception: return []`,
  which the file's own header law (`:14-15`) forbids ("Fail CLOSED… an extractor that quietly
  returns [] is a permanent coverage hole"). It is nevertheless safe here: an empty verb inventory
  turns all 23 claims in `lexicon.md` into stale claims and reds the coverage assert. The comment at
  `:130-134` already says exactly this. Not a finding.

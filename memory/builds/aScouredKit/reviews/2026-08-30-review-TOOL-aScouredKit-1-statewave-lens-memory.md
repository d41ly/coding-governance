# wave 2 — is the memory tree still true, and is it affordable?

**Serves:** research TOOL-aScouredKit-1 TOOL-aScouredKit-2

## Verdict: BLOCKED

*Node `a`, 2026-08-30, at `66c4891c`. Lens: the memory tree's own truth — spec statuses against git,
memory documents against the code at HEAD, retired mechanisms still instructed, and what a DoR
session is actually told to read. Every finding below names both sides: what a record says, and what
is true, each with its own path:line or command output.*

---

## The headline

**Fourteen of the eighteen non-terminal specs in this tree describe work that has already
landed on `main` and is an ancestor of HEAD.** As a consequence, **six of the sixteen rows in
`memory/LIVE.md`** — the GENERATED work-state index that `AGENTS.md` §5 says status is DERIVED
from, and that §1's Definition of Ready sends every session to read — name builds that are
finished.

The tree's answer to "what is in flight?" is wrong for 38% of its own rows. That is the reported
symptom, mechanically.

---

## Finding 1 — 14 of 18 non-terminal specs contradict git (BLOCKER)

Population: every `**Status:**` header under `memory/builds/*/spec/**` whose token is in
`{OPEN, SPECCED, BLOCKED, INPROGRESS}` — the same set `tools/drift-audit/drift_report.py:438` uses.
Eighteen specs. Five more carry no status header at all (pre-cutoff grandfathers) and are excluded,
as is `WONTDO`, which is terminal.

Method per spec: `git log --all --grep=<id>`, then `git merge-base --is-ancestor <sha> HEAD` on every
commit found, then an artifact check in the tree at HEAD, then a cross-read of
`memory/backlog/<FAMILY>.md`, `memory/DECISIONS.md` and `memory/map/features/`.

### The fourteen, with both sides

| # | Spec (header status) | Record says | Reality at HEAD |
|---|---|---|---|
| 1 | `memory/builds/aPacedTurnstile/spec/2026-08-20-spec-TOOL-aPacedTurnstile-14.md:3` — SPECCED | `memory/backlog/TOOL.md:171` — `TOOL-aPacedTurnstile-14 · CLOSED · … CLOSED by TOOL-dHonouredPark-1`; `memory/map/features/build-readme-surface.md:146` "is closed by"; `memory/builds/dHonouredPark/build/2026-08-25-build-TOOL-dHonouredPark-1-acceptance.md:64` "OBSERVED … `TOOL-aPacedTurnstile-14 · CLOSED`" | S1/S5 shipped at `tools/unattended/unattended.sh:1671-1686` (`roster_ids` captures `region` and returns 3, comment cites `TOOL-dHonouredPark-1 S5`); S8's roster pair is live at `memory/builds/aPacedTurnstile/README.md:263,276` |
| 2-9 | `memory/builds/aMendedLedger/spec/2026-08-09-spec-aMendedLedger-1.md:3` and the seven unit specs under `memory/builds/aMendedLedger/spec/units/` — all SPECCED | build README `memory/builds/aMendedLedger/README.md` renders **Build status: SPECCED**, 8 units | every unit has a landed build commit, all ancestors of HEAD: `dc5ae995` (U1), `f3c48dee` (U2+U4), `3e25a56f` (U3), `a08c2f3d` (U5), `9369123e` (U6), `bde0de8c` (U7), `390a87e7` (U8), `e6fb7047` (U9), merged as `289daf72` "merge: aMendedLedger — finish the memory rework, adopt the map, key the corpus". Artifacts present: `tools/memory-tree/merge-rows.py`, `.gitattributes:51-59` wiring it, `memory/archive/ledger/` holding the retired shards |
| 10 | `memory/builds/aTetheredScratch/spec/2026-08-20-spec-TOOL-aTetheredScratch-1.md:3` — INPROGRESS | `memory/DECISIONS.md:86` records the ratified decision; review verdict `CLEAN WITH FIXES` at `memory/builds/aTetheredScratch/reviews/2026-08-20-review-TOOL-aTetheredScratch-1-2.md:1` | the guard shipped: `tools/hooks/scratch-guard.js`, `tools/hooks/scratch-guard.fragment.json`, `tools/hooks/scratch-guard.test.sh`, and it is wired at `.claude/hooks/scratch-guard.js`. Commit `67973f6e`, ancestor of HEAD |
| 11 | `memory/builds/aTetheredScratch/spec/2026-08-20-spec-TOOL-aTetheredScratch-2.md:3` — INPROGRESS | `memory/DECISIONS.md:87` — the retarget was "specced, audited and REFUSED on measurement", the defect fixed instead; `memory/backlog/TOOL.md:115` — `TOOL-aBranchedMandate-6 · CLOSED · … built as TOOL-aTet…` | the fix shipped: `tools/memory-recall/selftest.py:150-163` clears the read-only bit and retries. Commit `5c83c180`, ancestor of HEAD |
| 12 | `memory/builds/dNarrowedAnchor/spec/2026-08-24-spec-TOOL-dNarrowedAnchor-1.md:3` — INPROGRESS | `memory/DECISIONS.md:92` records the ratified per-mode anchor | `SECOND_ANCHOR_MODES` is live at `tools/unattended/check-unattended.sh:211-213` and `:1012`; merged at `baa2857e`, kit vintage bumped at `29d86ba4`/`81afc545` |
| 13 | `memory/builds/aBatchedLintel/spec/2026-08-03-spec-aBatchedLintel-1.md:3` — INPROGRESS | — | `tools/memory-tree/check-memory-hygiene.sh:773-774` says in its own comment "ONE awk over the whole population, replacing ~13 forks PER SPEC … `TOOL-aBatchedLintel-1` ports `PERF-aSlothfulCapstan-1`"; `memory/builds/aThawedCorpus/reviews/2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md:252` calls it one of "two prior hand-fixes" |
| 14 | `memory/builds/bConvergentLodestar/spec/2026-07-22-spec-bConvergentLodestar-1.md:3` — SPECCED | — | S1's `## Reuse affordance` sections are live in every dossier under `memory/map/features/`; the SYMBOL recall tier is read at `tools/codebase-map/reuse_lookup.py:5-6,72-75`; `--converge` exists at `tools/codebase-map/map_diff.py:4,17`. Commits `3af46f66`, `449ce976`, `2d9cc962`, `e54cbb49` — all ancestors of HEAD |

### The four that are honestly non-terminal (control group)

Reported so the finding is not "everything is stale", which would be as useless as "some are".

- `memory/builds/aQuarriedLantern/spec/2026-08-03-spec-aQuarriedLantern-1.md:3` — the header itself
  says `U1-U3 built, closing review folded; NOT CLOSED — §8 Q6 is deliberately open`. Class (b): old
  but true, and it says why.
- `memory/builds/aDeclaredBound/spec/2026-08-18-spec-TOOL-aDeclaredBound-4.md:3` — OPEN. Its S1
  ships a repo-root `.agent-cap.conf`; `git ls-files | grep agent-cap` returns no such file. True.
- `memory/builds/aGradedDoorway/spec/2026-08-29-spec-TOOL-aGradedDoorway-7.md:3` — INPROGRESS, and
  `memory/backlog/TOOL.md:267` agrees. Active build.
- `memory/builds/dScriptedRepeat/spec/2026-08-20-spec-dScriptedRepeat-8.md:3` — SPECCED. Its S1
  output-scope refusal does not exist: `grep -rn 'output-scope\|output_scope' tools/` returns
  nothing, and `tools/unattended/check-unattended.sh` has no diff-vs-output-glob predicate. True.

### The reader-facing consequence

`memory/LIVE.md` at HEAD holds 16 rows. Six of them are live ONLY because of the specs above:

```
aBatchedLintel      INPROGRESS   sole non-terminal spec = TOOL-aBatchedLintel-1  (landed)
aMendedLedger       SPECCED      all 8 non-terminal specs                        (landed)
aPacedTurnstile     SPECCED      7 units CLOSED, -14 SPECCED                     (landed)
aTetheredScratch    INPROGRESS   both units                                       (landed)
bConvergentLodestar SPECCED      sole unit                                        (landed)
dNarrowedAnchor     INPROGRESS   sole unit                                        (landed)
```

Verified by enumerating every spec header per build; `aPacedTurnstile`'s other seven are CLOSED, so
unit 14 alone holds that build on the index.

### Why no gate sees this

`tools/drift-audit/drift_report.py:441-483` is the signal for exactly this class, and at HEAD it
reports **2 of 18**. Its oracle is "the spec's own id is cited by tracked PRODUCT source"
(`ctx.product_globs`, line 429 comment: "Product source only — keying a record's truth on another
record is circular"). That is a deliberately narrow oracle and it works: it caught
`TOOL-aBatchedLintel-1` and `TOOL-dNarrowedAnchor-1`, the only two whose ids a source file happens
to spell. It cannot see the other twelve, because a landed unit whose id never reached a code
comment is indistinguishable from one that never landed.

So the signal is not broken — it is **precise and 14% sensitive**, and the pin of 2 makes it read
`ok`. A green row on this signal has been carrying a 78% miss rate.

The measurement itself is cheap and needs no new oracle: a CLOSED backlog row naming the id, or a
merge commit that is an ancestor of HEAD, resolves twelve of the fourteen in one pass. The circularity
argument in that comment is right about records-grading-records in general and is worth relaxing for
the specific case of `backlog row CLOSED` + `commit ancestor of HEAD`, which are two independent
witnesses, only one of which is a record.

---

## Finding 2 — `AGENTS.md` sends every Tier-2 review to a directory that has never existed (HIGH)

`AGENTS.md:318`:

> Persist each Tier-2 run as an in-repo artifact folder (`memory/reviews/`)

`memory/reviews/` does not exist and has never been tracked:

```
$ ls memory/reviews          -> No such file or directory
$ git ls-files memory/reviews -> (empty)
```

The real convention is `memory/builds/<slug>/reviews/`, stated at `memory/HYGIENE.md:33` and again
at `:126` (a build folder holds only `README.md RUN.md prompts/ spec/ build/ reviews/`), and
practised by all 111 review records in the corpus — including this one.

This is not a template placeholder left unfilled: `coding-governance-agents.template.md:250` carries
`{{REVIEW_DIR}}`, and the render that filled it landed at `e1919b28` (2026-08-18,
"AGENTS.md becomes a rendered region plus authored slots"). It has been wrong for twelve days in the
one document every session loads.

**Why nothing catches it.** Hygiene check 15 (dead repo-path citations) scans the *memory tree*
corpus; `AGENTS.md` sits at the repo root and is outside its population — `corpus_ids.py --report`
prints `dead path cites : 0`. Check 16's read-path derivation
(`tools/memory-tree/corpus_ids.py:395-421`) admits a candidate only `if cand in tracked`, so an
untracked citation is silently dropped: it lands in neither `members` nor `absent`, and rule 4
never sees it. The charter is the only document in the tree with no path-resolution gate at all.

---

## Finding 3 — the charter and the decision index point at a second tier that does not exist (HIGH)

`AGENTS.md:223`:

> Logs are two-tier for token scoping: a one-line-per-decision index pointing at per-decision detail
> files; open details only for the areas you touch.

`memory/DECISIONS.md:6`:

> One line per decision, APPEND-ONLY, every family in one file. Detail in `decisions/`.

`memory/decisions/` does not exist:

```
$ git ls-files 'memory/decisions*'   -> (empty)
```

`memory/DECISIONS.md` is a single flat 25,374 B file. There is no second tier. A session following
§6's session-start reading order — "ALWAYS load the master decision index first, then the stream
logs for the area touched" — is being told to open a tier that is not there, and will either
conclude the tree is broken or fall back to reading whatever it can find.

`memory/HYGIENE.md` compounds it: line 26 draws `decisions/` into the structure diagram, and lines
50, 118 and 121 carve it out of checks 2 and 3. Those carve-outs select an empty population, which
`memory/HYGIENE.md:44` itself forbids —

> **A check never selects an empty population.** A path selector that matches nothing prints
> nothing, and nothing is what a passing check prints.

— so the file breaks its own rule 5 three times over a directory it also documents.

*Not class (c).* This is not an append-only record superseded by a later id, and not an archive
path. It is a present-tense instruction in the currently-loaded charter and in the live header of
the live decision index.

---

## Finding 4 — `memory/HYGIENE.md` says `project/` holds six registries; it holds nine (HIGH)

`memory/HYGIENE.md:29`:

> `├── project/               the gate's own waiver registries (*.txt, six of them) and nothing else`

`memory/HYGIENE.md:94`:

> Six plain lists in `memory/project/` — **the whole of what that directory holds** — read as
> exact-key set membership …

`memory/HYGIENE.md:112`:

> All six are scaffolded by `adopt-memory-tree.sh`.

Reality:

```
$ git ls-files memory/project/ | wc -l
9
```

| registry | scaffolded by `adopt-memory-tree.sh` | read by `check-memory-hygiene.sh` | named in HYGIENE's six |
|---|---|---|---|
| `corpus-path-unresolved.txt` | yes | yes | yes |
| `curation-debt.txt` | yes | yes | yes |
| `id-orphan-waiver.txt` | yes | yes | yes |
| `legacy-files.txt` | yes | yes | yes |
| `method-carriers.txt` | yes | yes | yes |
| `unarmed-branches.txt` | yes | yes | yes |
| `readme-contract.txt` | **yes** | yes | **no** |
| `testsuite-count-waivers.txt` | no | yes | **no** |
| `trace-waiver.txt` | no | yes | **no** |

So all three numbers are wrong: nine exist, seven are scaffolded, nine are read.
`readme-contract.txt` is a memory-tree registry, scaffolded by the kit's own adopter, and the file
that documents the kit does not know it exists.

The gate itself carries the same stale count in a comment while its code admits nine —
`tools/memory-tree/check-memory-hygiene.sh:296`:

> `# machinery it used to also hold … is retired, and the F:*.md catch-all goes with it: a directory
> defined as six named files cannot also admit any .md anyone drops in.`

…directly above the `case` at lines 308-315, which admits nine names.

**This ships.** `tools/memory-tree/HYGIENE.template.md:29,94,112` carries the identical text, and
`tools/memory-tree/kit-dogfood-parity.test.sh` byte-compares the pair, so the parity leg is green
over a shared falsehood. Every adopter of memory-tree receives a rule set that mis-describes the
directory it is the rule set for.

*Distinct from `TOOL-aScouredKit-22`*, which is about the numbered CHECK catalog stopping at 22.
This is the `project/` structure section, a different part of the file and a different claim.

---

## Finding 5 — `AGENTS.md` §5 delegates the hygiene check count to a carrier that stopped stating it (MEDIUM)

`AGENTS.md:206` (the "point at the source, do not restate the number" idiom, applied):

> a **hygiene gate** whose check count is stated by the kit README and the gate-leg name and is
> deliberately not restated here

The kit README does state it — `tools/memory-tree/README.md:18`, "the gate — 23 checks". The
gate-leg name does not:

```json
{"name": "memory hygiene", "argv": ["bash", "tools/memory-tree/check-memory-hygiene.sh"], ...}
```

It used to. `git show 47f4ba2e -- tools/gate-legs.json` shows the rename on 2026-08-17:

```
-    "name": "memory hygiene (20 checks)",
+    "name": "memory hygiene",
```

The charter names two carriers for a fact that now lives in one, and the count the deleted carrier
held (20) was already three behind. A session that follows the charter to the leg name finds
nothing and has to go looking. Low blast radius, but this is precisely the rule the charter states
about itself at §6 — "A value stated in prose beside the source that OWNS it rots between changes …
it is the one most often broken by the document that states it" — and it broke thirteen days ago.

---

## Finding 6 — check 16 rule 3 asks the index set *before* the waiver filter (MEDIUM)

`memory/HYGIENE.md:206` states rule 3 as:

> every member is byte-capped by check 6 or listed in `READ_PATH_WAIVER`, because a charter citation
> nothing watches is a read budget nobody watches

The implementation asks the wrong question. `tools/memory-tree/corpus_ids.py:477`:

```python
capped = {l for l in ask_shell("--print-index-set", root).split("\n") if l.strip()}
```

`--print-index-set` (`tools/memory-tree/check-memory-hygiene.sh:441`) prints the raw `$INDEX_SET`.
Check 6 does **not** measure that set — line 447 filters it first:

```sh
sel6=$(printf '%s\n' "$INDEX_SET" | while IFS= read -r f; do in_debt "$f" && continue; ...
```

Observed:

```
$ bash tools/memory-tree/check-memory-hygiene.sh --print-index-set | grep -E 'backlog/TOOL|aBoundedVerdict/README'
memory/backlog/TOOL.md
memory/builds/aBoundedVerdict/README.md
```

Both of those are in `memory/project/curation-debt.txt` and check 6 skips them entirely. A
charter-cited file on the debt registry therefore satisfies rule 3 while nothing measures it — the
guard reads a variable the exemption does not touch.

Latent today: no current read-path member is on the debt registry. Not hypothetical, though —
`memory/DECISIONS.md` is both a read-path member and an index, and the way `memory/backlog/TOOL.md`
got onto that registry (a merge-induced overflow, per the registry's own header) applies to
`DECISIONS.md` identically. The fix is a `--print-index-set` that honours `in_debt`, or a second
print mode for the measured set.

---

## Finding 7 — the DoR read mandate is roughly 413 KB and nothing bounds the largest part (HIGH)

What `AGENTS.md` §1's Definition of Ready actually tells a session to read before touching code:

> Locate: read your stream's decision log + backlog (§6) and the derived work-state index (§5)

Measured at HEAD:

| what | bytes |
|---|---|
| `AGENTS.md` (auto-loaded, before the DoR even starts) | 64,066 |
| check 16's derived read path, 6 files (`corpus_ids.py --report`) | 150,777 |
| `memory/backlog/TOOL.md` — the tooling stream's backlog | 198,088 |
| **total for a tooling-stream DoR** | **≈ 412,931** |

That is on the order of 100k tokens of mandatory reading before the first line of code, on the
stream that owns 20 of the 23 open builds. A mandate at that size is not followed; it is skimmed,
and skimming a governance document is the failure mode the document exists to prevent.

The structural half is worse than the number. `memory/backlog/TOOL.md` is bound by **nothing**:

- **check 6** (byte cap, 61,440 for its class) — skipped, `memory/project/curation-debt.txt` lists it.
- **check 7** (entry budget) — skipped, same registry, same row.
- **check 8** (status vocabulary) — skipped, same row. The registry's own text admits this row "is
  currently hiding one real status-token fault as well as the width".
- **check 16** (read-path accounting) — never sees it. `read_set`
  (`tools/memory-tree/corpus_ids.py:395-421`) derives members from literal `memory/…` tokens in the
  charter, and the charter spells the backlog only as `memory/backlog/<FAMILY>.md`
  (`AGENTS.md:69`), a placeholder that resolves to no tracked file. The six-file read path
  `corpus_ids.py --report` prints does not include it.

So the single largest document the DoR mandates is exempt from every size gate the tree has, and
it is 3.2× the cap for its class:

```
$ awk 'BEGIN{n=0} /^- [A-Z]+-[A-Za-z]+-[0-9]+ · /{n++} END{print n}' memory/backlog/TOOL.md
284
```

284 rows, 196,204 B of rows, against `INDEX_CAP_BYTES="61440"` — a value `.memory-tree.conf`
derives as "250 rows at the measured 247.6 B/row".

**The retirement argument does not survive this.** `.memory-tree.conf` retires `READ_PATH_CEILING`
on the grounds that "check 6 already caps every member by class, so the summed budget was a second
bound over an already-bounded population", and `tools/memory-tree/corpus_ids.py:433-437` repeats it.
That premise is true of the six files check 16 happens to derive and false of the document a DoR
session spends the most tokens on. The retirement was sound for its measured population; the
population is the part that is wrong.

Related but distinct from `TOOL-aScouredKit-23` (`WIRE-INTO-PROJECT.md` and the unattended SKILL
have no declared ceiling): that row is about two files outside `MEMORY_ROOT` with no row anywhere.
This one is about a file inside `MEMORY_ROOT` that HAS a cap and is waived past it, on a registry
whose own header says the waiver "now describes a drain nobody has performed rather than one that
cannot be".

---

## Finding 8 — `aScouredKit`'s own README contradicts three of its own specs (HIGH)

Graded as asked, and it does not hold up.

`memory/builds/aScouredKit/README.md:51`:

> **Ids `-10` and `-16` through `-34` are NOT units and carry no spec.** They are the findings this
> run reported rather than built, each a row in `memory/backlog/TOOL.md` with its own measurement.

Three of the twenty ids that sentence covers do carry a spec, and each is a unit:

```
memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-30.md   CLOSED rev-1  Tier-1
memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-31.md   CLOSED rev-2  Tier-1
memory/builds/aScouredKit/spec/2026-08-30-spec-TOOL-aScouredKit-32.md   CLOSED rev-1  Tier-1
```

And none of the three has a backlog row — `grep -n 'TOOL-aScouredKit-3[0-2] ·' memory/backlog/TOOL.md`
returns nothing, while `-10`, `-16`…`-29`, `-33`, `-34` all have one. So the sentence is wrong in
both directions for exactly those three: they are units, and they are not rows.

The build's own sibling record already says so —
`memory/builds/aScouredKit/reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md:46`:

> `-30`, `-31` and `-32` are PROMOTED units. The closing review's blocker counts ran 4 → 3 → 4 …
> Every blocker still standing became a unit, specced at its tier and built

Two records in one build folder, written the same day, giving opposite answers to "is `-30` a unit?".

The **authored roster** carries the same error and it is the one a machine reads. The
`<!-- roster:units -->` region at `memory/builds/aScouredKit/README.md:61-80` lists **14 rows**,
ending at `TOOL-aScouredKit-15`. The generated region at `:87-105` lists **17 specs**, including
`-30`, `-31`, `-32`. The rendered build-index line at `:83` says "17 unit(s)".

Nothing catches it, and the reason is structural: `missing_units` in
`tools/unattended/unattended.sh` reports roster ids with no spec — the one-way difference. A spec
with no roster row is invisible to `--plan`, to `build-complete` term 3, and to the DoD this run
declared met. The authored plan can silently under-report the build forever.

**What this means for the commissioning question.** The orchestrator's heuristic was that these
records are honest. On the evidence they are honest about the code and wrong about themselves: the
backlog rows I sampled reproduce exactly (below), the spec-audit's stated limits are honest and
self-critical, and the acceptance ledger's commands re-run — but the README's authored prose
describes a fourteen-unit build that shipped seventeen units.

### The sampled backlog rows do reproduce

Two rows checked byte-for-byte against the tree, both exact:

- `TOOL-aScouredKit-22` (`memory/backlog/TOOL.md:282`) claims `grep -n "23"` over
  `memory/HYGIENE.md` "returns zero hits" and the catalog "STOPS AT ITEM 22".
  `grep -c '23' memory/HYGIENE.md` → `0`; the last catalog item is `memory/HYGIENE.md:252`,
  `22. **review verdict vocabulary**`. Exact.
- `TOOL-aScouredKit-23` (`:283`) claims `WIRE-INTO-PROJECT.md` at 59833 B / 816 lines and
  `.claude/skills/unattended/SKILL.md` at 48767 B / 731 lines.
  `wc -c -l` → `816 59833` and `731 48767`. Exact to the byte.

### The spec-audit's stated limits are honest

`…-1-spec-audit.md:32-43` says it ran no multi-agent audit (correct — `AGENTS.md:311` forbids one at
Tier 1, and 15 of the 17 units are Tier 1), no sub-spec cross-read (correct — no unit has sub-specs),
and that it caught none of the defects the closing review did. That last one is a real
self-indictment and is stated rather than implied. No finding.

### The acceptance ledger's evidence re-runs

`memory/builds/aScouredKit/reviews/2026-08-30-review-TOOL-aScouredKit-11-acceptance-ledger.md`
names four commands and two arms. Re-run at HEAD:

- `python tools/govkit/selftest.py` → **exit 0**, `govkit-selftest: all arms held`, and
  `grep -c '^ok '` on the run's output returns **1001**. The ledger's "1001 arms held" reproduces
  exactly at HEAD. AC1 and AC4 for `-11` and AC4 for `-13` hold.
- `python tools/govkit/govkit.py selfcheck` → **exit 0**, five summary lines including
  "surface 58 tracked path(s) · 25 entr(y|ies) · 17 exemption(s) · 0 unclaimed". AC5 holds.
- The named arms exist: `AC-withheld` (6 occurrences in `tools/govkit/selftest.py`), `AC-ordered`
  (`tools/govkit/selftest.py:1135,1140`), and the AC1 arm for `-13` at
  `tools/govkit/selftest.py:2124` — spelled `a target's own \`kits\` list is honoured by a
  no---kits plan`, which the ledger renders without the backticks. Cosmetic, not a defect.
- Its "What this ledger does not claim" section correctly states that the gate grades shape and
  coverage, not truth, and flags its one AMENDED criterion as load-bearing. That is the honest form.

No finding against the ledger.

---

## Interrogating the handed-over baselines

- **`dangling_pointers_in_own_ledger -1/0 DEAD PROBE`** — correct and correctly reported. Detail:
  `{"note": "no ledger file for node a"}`. The authored per-node session ledger was retired by
  `TOOL-aMendedLedger-3` (U2) and its shards frozen under `memory/archive/ledger/`. The liveness
  assertion is doing exactly its job: the probe says it cannot move rather than reporting 0.
- **`ledger_rows_contradicting_git 0/0 EMPTY BY DECLARATION`** — same retired artifact, same honest
  reporting. Not blind, just retired.
  **But note what that means together:** two of eleven drift signals are permanently dark because
  their subject was retired, and the question they answered — "does a work-state record contradict
  git?" — was not re-pointed at the artifact that replaced it. The replacement is the spec status
  header, and Finding 1 is the answer nobody is computing.
- **`handkept_inventories_disagreeing_with_source 0/0 EMPTY BY DECLARATION`** — this repo declares
  no hand-kept inventory. Honest.
- **`closed_specs_with_no_product_commit 1/287`** — the one offender is
  `memory/builds/aMooredAnchor/spec/2026-08-11-spec-aMooredAnchor-1.md`, and its CLOSED status is
  **true**: S1's replace-ref refusal is live at `tools/unattended/check-unattended.sh:491` and the
  grafts check at `:494-496`. Untraceable by commit-subject convention, not unbuilt. The pin is
  honest.
- **`shrink_only_lists_not_shrinking 2/5`** — the two are `curation-debt.txt` (seed 0 → 4 rows) and
  `memory/project/trace-waiver.txt` (seed 5 → 7 rows). Both genuinely grew, both carry per-row
  reasons, and `trace-waiver.txt`'s own header says "SHRINK-ONLY". Report-only, so a shrink-only
  list has grown twice with nothing gating it. Real but minor next to the above.
- **`non_terminal_specs_cited_by_product_source 2/18 ok at pin 2`** — see Finding 1. This is the
  reassuring-green row, and it is reassuring because its oracle is 14% sensitive, not because the
  tree is clean.

## What was checked and found clean

Said so a green line is not mistaken for an unrun one.

- `python tools/memory-tree/gen_build_index.py --check` → `build-index: clean (447 artifact(s))`.
  The generated indexes match a fresh render; the falsehood in Finding 1 is in the *inputs*, which
  is why the renderer is happy.
- `python tools/memory-tree/corpus_ids.py --report` → `ids defined 716 · ids cited 716 ·
  orphan ids 0 · build collisions 0 · dead path cites 0`. Inside the memory tree, citations resolve.
- `python tools/govkit/govkit.py selfcheck` → exit 0.
- Every commit sha named in this report was tested with `git merge-base --is-ancestor <sha> HEAD`.
- `python tools/govkit/selftest.py` → exit 0, 1001 `ok` arms, `all arms held`.
- **Not run:** `bash tools/run-gates/run-gates.sh`. The full bar has a 26-minute floor and this
  audit changed no code, so the merge bar was not this lens's question. Stated rather than omitted.

## Ordering, if only some of this gets fixed

1. Finding 1 — it is the reported symptom, and eight of the fourteen are one build's headers.
2. Findings 2 and 3 — the always-loaded charter pointing at two directories that do not exist.
3. Finding 4 — a shipped kit document mis-describing its own directory, byte-compared into every
   adopter.
4. Finding 8 — one build's README, one edit, but it is the record the next session reads first.
5. Findings 6 and 7 — the two gates that are looking at the wrong population.
6. Finding 5 — one sentence.

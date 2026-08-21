# Design brief — the floor-bound bar: sharding, dispatch, and the invisible queue

**Serves:** research TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4
**Commissions:** TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4

**Node `a` · 2026-08-21 · worktree `.claude/worktrees/unattended-ascanned-throttle-18a592` · BASE `36d0ad3` · nothing written, nothing committed.**

Everything below was re-verified against source in this worktree. Where a skeptic refuted a brief, the refutation is applied. Where I re-established a refuted claim myself, the sentence says so and names what I read or ran.

---

## 0 · What binds all four units

**The bar is floor-bound.** Three of four reconstructed bars have one leg exceeding leg-seconds ÷ width (`memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md:80-84`). No width change, no extra worker and no faster sibling leg moves span. Only the floor moves span.

**Two pins move under almost every unit here, and neither brief that named one named both.**

| Pin | File:line | Who moves it |
|---|---|---|
| `last-audit` stamp | `memory/guides/SESSION-KICKOFF.md:5` | every unit that edits `tools/gate-legs.json` or `tools/run-gates/run-gates.sh` |
| the charter's measured pair, machine-graded in both directions | `AGENTS.md:498` + `tools/run-gates/run-gates.gov.test.sh:210-215` | every unit that moves wall clock or leg-seconds |

I verified the first myself: `memory/guides/SESSION-KICKOFF.md:6` lists both `tools/run-gates/run-gates.sh` and `tools/gate-legs.json` in `watch:`, and `AGENTS.md` in `verify-paths:`. The `kickoff-manifest ratchet` leg (`tools/gate-legs.json:1-9`) carries **no** `guard` key, so it runs on every bar including a scoped one, and its check 5 fires in both directions — `skills/session-kickoff/manifest-check.sh:305` on committed watched changes with no re-stamp, and `:417` on staged ones. A landing that edits the manifest and skips the re-stamp reds the bar.

The second is a matched negative/positive pair I read in full at `tools/run-gates/run-gates.gov.test.sh:210-215`: the negative half greps the charter for the retired `335s|~?95s`, the positive half requires the literals `873 s` **and** `4018 s`. **The charter figure must move exactly once**, in the last of the span-moving landings, with a fresh measurement — not three times in three commits, each reddening the one after it.

**A fresh measurement I took in this worktree, 2026-08-21, node `a`,** which corrects a rationale in the ledger brief and adds a risk to both sharding units:

```
common dir = C:/projects/coding-governance/.git
  gate-timings.tsv   73 rows · 69 of the 88 manifest names known · 4 orphans
  gate-ledger.tsv    90 rows · 88 of the 88 manifest names known · 2 orphans
this worktree's $gd  = C:/projects/coding-governance/.git/worktrees/unattended-ascanned-throttle-18a592
```

Two consequences. The legacy file is at **78.4 %** coverage, not "almost nothing" — the honest argument for a coverage count is that it separates 78 % from 100 %. And the **common dir already holds a fully warm ledger**, which is what makes the rename risk below real rather than theoretical.

**The rename risk, re-derived from source because the shard-driver brief had it backwards.** `tools/run-gates/run-gates.sh:637` is `order = sorted(range(len(data)), key=lambda i: -durs.get(data[i]["name"], 0.0))`, and the runner's own comment at `:618` states the consequence: *"A leg the cache does not know scores 0 and sorts last."* An unknown name keys `0.0`; every known leg keys a negative. So on a **warm** ledger a renamed leg dispatches **dead last** — not in manifest order. On a floor-bound bar, dispatching a floor shard last is the worst schedule available. Manifest order is what you get only on a fully **cold** ledger, where every key is equal and the stable sort preserves input order.

---

## Unit A — `shard-driver`

Split `unattended driver selftest` (`tools/unattended/unattended.test.sh`, 2244 lines, 398 executed assertions measured) into two bar legs. **One file, no physical split.**

### The one mechanism

`--shard i/n` parsed as a flag, two guarded contiguous regions, two manifest rows on the same script, per-shard floors.

1. **Parse above `TMP=$(mktemp -d)`** (`tools/unattended/unattended.test.sh:14`), so a refusal costs ~50 ms and creates nothing. Parse the flag, do **not** position-read it: the manifest stores argv as a list and the runner execs `"${argv[@]}"` (`tools/run-gates/run-gates.sh:786`), so the script receives `$1=--shard` and `$2=1/2`. Declare `SHARD_ARITY=2` as a script constant.
2. `in_shard()` → true when unsharded or when the index matches.
3. Wrap the arm body in `if in_shard 1; then … fi` / `if in_shard 2; then … fi`. **No reindentation** — four inserted lines. This is load-bearing for the arms gate: `check-arms.py`'s `armed_signatures` scans lines and skips comments, so an unindented `if` wrapper leaves every arm signature byte-identical.
4. **Hoist SIX definitions** into the prologue at `:176` (the brief said "exactly five" and listed six): `roster()` `:275`, `units()` `:287`, plus `bcsetup()` (the body of `:696-703`, ending `BCP=$(git rev-parse HEAD)` at `:703`), `bcrestore()` (the single line `:881`), and `bcreset()`/`bcopen()` `:704-706`. Region 1 calls `bcsetup` where `:696` sits and `bcrestore` where `:881` sits, so the unsharded run is behaviourally identical. Region 2 opens with `bcsetup; bcrestore`.
5. **Mode-selected floor — the step the original brief omitted, and without it every shard leg reds on every bar, forever.** `tools/unattended/unattended.test.sh:2242` is `[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent…"; st=1; }` — I read the line. Under the un-corrected diff, `--shard 1/2` executes 196 against a floor of 338. Replace with `FLOOR=$FLOOR_ASSERTIONS`, overridden to `$FLOOR_SHARD_1`/`$FLOOR_SHARD_2` by `in_shard`, compared once at `:2242` with the shard name in the failure text.
6. **Manifest:** two rows, same script, `["bash","tools/unattended/unattended.test.sh","--shard","1/2"]` and `"2/2"`, both carrying `"guard": ["tools/lib/","tools/unattended/"]` (`tools/gate-legs.json:606-609`, verified: this leg's guard is **two** entries, unlike its sibling's three) and `"chunk": "selftests"`.

**Leg naming, and it is not cosmetic.** `tools/govkit/govkit.py:879` refuses `re.search(r"\([^)]*\d[^)]*\)", nm)` on any descriptor-claimed name, so `(1 of 2)` is illegal. **Recommendation: keep shard 1's name as the existing `unattended driver selftest` and name shard 2 `unattended driver selftest shard B`.** This is the cheap mitigation for the warm-ledger sort: shard 1 inherits the existing 659.9 s ledger row and still dispatches first, and only shard 2 (~248 s standalone) takes the sorts-last penalty, which a ~766 s throughput-bound bar absorbs. It also halves the map/descriptor churn — one key arrives instead of one arriving and one departing. The cost is an asymmetric name pair; say so in the manifest comment.

### Why not the alternatives

- **Physical file split — refuted by a gate, and I verified the arithmetic.** `tools/memory-tree/check-arms.py:132` is `pairs.append((rel, rel[:-3] + ".test.sh"))` — one gate, exactly one sibling test — and `.memory-tree.conf:178` pins `tools/unattended/unattended.sh:81:78`. Live `check-arms.py --report` reports 88 branches / 85 armed. Split at the seam, 38 branches go unarmed and the armed floor of 78 breaks. `.memory-tree.conf:178` is the pin that **decides** the mechanism.
- **Per-arm hash assignment** — the file has fixture epochs that must run contiguously; a hash breaks them, and it touches 130 blocks instead of 4 lines.
- **Make the arms cheaper** — changes the subject under test rather than the harness, and does not deterministically move the floor.

### The seam — verified, not argued

**Line 1255**, the `# ---- S6, the phase PRODUCER` block header. Region 1 = 179–1254, region 2 = 1255–2244. I confirmed `:1254` is blank and `:1255` opens a fresh `# ----` block, and that `:1253` ends on an assertion.

The file is stateful but has an **invariant**, not a chain: branch `unit` at `$UNIT0`, local `main` and `origin/main` at `$BASE`, one remote, clean tree, `.unattended.conf` from `mkconf` — exactly what the prologue `:143-176` leaves and what `reset_tree` `:169` re-establishes. Every permanent mutation is closed: the roster excursion `:296-396` (restores at `:353`, `:367`, `:388`, `:396`), the anchor-refusal block `:442-520` (each swap paired with its undo), the degenerate-base block `:532-572` (closed at `:572`), the build-complete epoch `:696-703` (closed at `:881`), `--landed` `:1802` (closed at `:1820`), and `ANCHOR_SCOPE` `:2007-2069` (never pushes main).

The real constraint is **name** state, not tree state. A mechanical cross-seam scan found exactly one hidden dependency — `$BCP`, reached through `bcopen` at `:1591`, `:1598`, `:1610`, `:1619`, `:1628`, `:1636` — plus `roster` at `:1380` and `units` at `:1396`. `slice()` `:600`, `crbc`/`cropen`/`crbase` `:890-1038`, `wcw` `:1155`, `$ALIEN` `:555` all live and die in region 1; `mkspec` `:1313`, `dodarm` `:1720`, `scope` `:2001` live and die in region 2.

**Measured** (built in the scratchpad, nothing written to the repo): whole file `PASS (398 assertions)` exit 0; shard 1 `PASS (196)` in 242 s standalone; shard 2 `PASS (206)` in 145 s standalone; prologue alone 2.37 s; prologue + hoists 4.19 s. `196 + 206 = 398 + 4`, the 4 being the prologue `mutate` arms at `:112`, `:122`, `:124`, `:129` that both shards pay. Duplication cost ≈ **4.2 s** of leg-seconds, which refines the report's ~2.75 s per-split estimate upward for this split.

**The 63/37 split is fine.** With both selftests sharded the bar is throughput-bound at ~766 s (report §4 R2), so any shard under that leaves span identical. A better seam near `:1041` is unmeasured; land the verified one and write the seam line into the script as a named constant with the measured pair beside it.

### Gate pins this unit moves

| Pin | File:line | What happens |
|---|---|---|
| `FLOOR_ASSERTIONS=338` | `tools/unattended/unattended.test.sh:2241` | stays as the unsharded floor; gains `FLOOR_SHARD_1=196`, `FLOOR_SHARD_2=206`, and the identity `SHARD_1 + SHARD_2 = FLOOR_ASSERTIONS + 4` checked every run |
| `last-audit` | `memory/guides/SESSION-KICKOFF.md:5` | `tools/gate-legs.json` is a `watch:` path; unguarded ratchet leg reds without a re-stamp + `manifest-audit:` delta line |
| codebase-map claim, **both directions** | `memory/map/features/unattended.md:11` | new key claimed AND (if shard 1 is renamed) the retired key removed — `tools/codebase-map/test_codebase_map.py:79` reds on `stale_claims` as well as on unclaimed |
| generated artifacts | `memory/map/generated/inventories.json:85-86`, `memory/map/generated/MAP.md:92-93` | regenerate in the **same commit** or `test_codebase_map.py:128` reds on freshness |
| descriptor↔manifest join, both directions | `tools/unattended/kit.toml:97-100` | a second `[[gate_leg]]`, or `tools/govkit/govkit.py:902` fails "claimed by no descriptor" |
| leg-name grammar | `tools/govkit/govkit.py:879` | no digit inside a parenthetical |
| `chunk` ∈ six declared names | `tools/run-gates/run-gates.gov.test.sh:238-247` | `SIX = {"records","product","wiring","declarations","selftests","e2e"}`, unconditional over the manifest |
| manifest key set | `tools/run-gates/run-gates.test.sh:96` | `KNOWN = {name, argv, guard, impure, chunk}` — the shard index rides in `argv`, never a new key |
| charter figure + its gate arms | `AGENTS.md:498` + `tools/run-gates/run-gates.gov.test.sh:210-215` | wall down, leg-sum up by ~4.2 s; move sentence and both arm halves together |
| gov canary floor | `tools/run-gates/run-gates.gov.test.sh:70` | `FLOOR_ASSERTIONS=12` raised for the new cover/reverse arms |
| kit version, **eight spellings across six files** | `tools/unattended/unattended.sh:33`, `tools/unattended/check-unattended.sh:18`, their same-line `gov:kit unattended@1.7` markers, both `tools/unattended/*.template.md` markers, plus the rendered carriers `.claude/skills/unattended/SKILL.md:5` and `memory/guides/UNATTENDED-PROTOCOL.md:1` | paired by `tools/check-kit-versions.sh:123-151`; `adopt-unattended.sh:185` asserts the rendered pair in sync, so a bump needs a re-render |
| pre-push cost | `.githooks/pre-push:151-161` | touching the manifest invalidates the recorded green from both directions; next default-branch push owes a full `GATE_FULL` bar |
| **UNMOVED, and named because it decides the mechanism** | `.memory-tree.conf:178` `tools/unattended/unattended.sh:81:78` | untouched by `--shard`; broken by a physical split |
| **UNMOVED** | `memory/project/testsuite-count-waivers.txt` | `tools/check-testsuite-counts.sh:36` dedupes argv paths with `sort -u`, so two legs on one file are one member |
| **flagged, not folded in** | `memory/map/features/run-gates.md:62` | "Seven of the 86 legs" — I derived the live count as 88 (`grep -c '"name"' tools/gate-legs.json`). A prose count of a derived population, already wrong. Delete it and point at the source; that is a dossier edit with its own owner |

### Observed RED before believed

Five staged breaks, each confirmed RED and unstaged. Four are unobservable until the new gov-canary arms exist, which is why those arms are part of this unit.

1. **A lost shard.** Delete the `--shard 2/2` row from `tools/gate-legs.json`. Today the bar goes green having run half the suite and nothing notices. The new complete-cover arm in `tools/run-gates/run-gates.gov.test.sh` must RED naming the missing index. Sibling break: set **both** rows to `2/2` — the arm must RED on the missing `1/2`, not merely on the duplicate.
2. **The silent-ignore shape, live today.** The script parses no argv at all, so `--shard 1/2` on two rows would be ignored and both legs would run the full 398-assertion suite: bar green, wall unchanged, leg-seconds **doubled**. Stage exactly that and the reverse-direction arm must RED — a script declaring no `SHARD_ARITY` may not be called with `--shard`, and one that declares it must be.
3. **The empty shard.** Break `in_shard` so region 2 never executes under `--shard 2/2`; the leg prints `PASS (4 assertions)`. `FLOOR_SHARD_2=206` must RED with the executed count in the message. Symmetrically for shard 1.
4. **The argument refusals**, each firing before `mktemp -d`: `--shard 3/2`, `--shard 1/3`, `--shard 0/2`, `--shard banana`, and a bare `--shard` with no value. Each exits non-zero, prints its own refusal text, and leaves no temp dir.
5. **The hoist regression.** Move the `bcsetup`/`bcrestore` calls off `:696`/`:881` by a few blocks and confirm the unsharded run changes. The evidence must be an **output diff**, not the assertion count — a count cannot see an arm that passed for the wrong reason.

**Control, already observed:** `--shard 1/2` exits 0 at 196/242 s, `--shard 2/2` exits 0 at 206/145 s, unsharded exits 0 at 398, and 196 + 206 − 4 = 398 exactly.

### Acceptance criteria

- **AC1** — no-argument run exits 0 and prints `PASS (398 assertions)`, byte-identical output to the pre-change run.
- **AC2** — `--shard 1/2` exits 0 with n ≥ 196; `--shard 2/2` exits 0 with n ≥ 206. The identity `FLOOR_SHARD_1 + FLOOR_SHARD_2 = FLOOR_ASSERTIONS + 4` is asserted in every mode. *This is a tripwire over three authored constants, not a measurement* — it catches an editor who moves one of three, and nothing more.
- **AC3** — each sharded run prints, above the PASS line, which region it ran and that the other region was **not** exercised by this leg.
- **AC4** — the header states what a sharded run does not check: neither shard alone is the suite; a new region-2 arm depending on region-1 state passes unsharded and reds only under `--shard 2/2`; the fixture epochs are why the split is contiguous.
- **AC5** — `bash tools/check-testsuite-counts.sh` green with no new waiver row: the emitting line still matches the anchored shape at `tools/check-testsuite-counts.sh:52`, `^FLOOR_ASSERTIONS=[0-9]+$` at `:56` still resolves non-zero (`:55` bans a zero floor), and a literal `$FLOOR_ASSERTIONS` read survives for `:60`.
- **AC6** — `python tools/memory-tree/check-arms.py --check` green, still 85 of 88 branches armed for `tools/unattended/unattended.sh`, `.memory-tree.conf:178` untouched, no new row in `memory/project/unarmed-branches.txt`.
- **AC7** — the five staged breaks each RED with a message naming the defect, and each greens on unstage.
- **AC8** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` green; both shard legs report under chunk `selftests` with distinct per-leg logs under `<git-dir>/gate-logs/` (the runner sanitises names to `[A-Za-z0-9._-]` at `tools/run-gates/run-gates.sh:103`, so two names differing only by a slash would collide — one more reason the names differ in a letter).
- **AC9** — codebase-map coverage + freshness green, both directions, generated artifacts regenerated in the same commit.
- **AC10** — `python tools/govkit/govkit.py selfcheck` green: descriptor rows match the manifest, no digit-bearing parenthetical.
- **AC11** — span re-measured from the run records on the **second** bar after the change, and the `AGENTS.md:498` pair plus both `run-gates.gov.test.sh:210-215` halves moved in the same commit.
- **AC12** *(restated as an observation, not a future conditional)* — the in-pool durations for both shard legs are read from the run record and each is below the ~766 s throughput bound.
- **AC13** *(new — the one observation the set was missing)* — in both modes, `git rev-parse "$BCP^{tree}"` is identical between the unsharded run and `--shard 2/2`, failing with both values named. The **tree**, never the commit, whose parent and message differ by construction. This is the only check that distinguishes a shard that *reproduced* the epoch from one that merely survived it: region 1's `bcsetup` runs after ~500 lines of arms and after a forced `git checkout -qf main` that leaves untracked files standing, which `:701`'s `git add -A` sweeps into the fixture commit — and `.unattended.conf` is exactly such a file.
- **AC14** *(new)* — run `--shard 2/2` and the unsharded suite with per-arm output captured; diff the region-2 slice; identical bytes, or the seam moved something.

### Risks

- **The warm/cold ledger split — two cases, not one.** Cold ledger (a fresh worktree; 24 of 26 when measured): every key is 0.0, the stable sort yields manifest order, the shards land around index 55 of 89 — the null-result reading. **Warm ledger** (the primary tree, and every worktree once Unit C lands): a new name is the *only* leg keying 0.0, so `run-gates.sh:637` sorts it **last** and the floor shards start after ~87 others. That is a measurable **regression**, not a null. Mitigation: the asymmetric naming above; failing that, one slow bar per worktree while the ledger self-heals.
- **Worthless shipped alone.** Sharding the driver alone buys 38.9 s (3.7 %) — the gate selftest becomes the new floor. Must land with Unit B; AC11's measurement is only meaningful once both are in.
- **The hoist is behaviour-preserving only if the calls sit at exactly `:696` and `:881`.** A call a few blocks off silently changes what every arm from `:710` to `:874` sees, and those arms would still PASS. AC1/AC13/AC14 are the mitigations; the assertion count is not one.
- **A new failure mode the file did not have:** a future region-2 arm depending on region-1 state passes the unsharded run a developer habitually types and reds only on the bar. The AC4 header text is the only mitigation; there is no gate for it.
- Both shard legs run concurrently; each builds its own `mktemp -d` scratch repo (`:14`) and bare origin (`:143`), so they share nothing.
- Adopters receive a second leg the day they take the kit; `govkit.py:2420-2432` resolves tokens across the whole argv list, so the extra elements travel.

---

## Unit B — `shard-gate`

Split `unattended gate selftest` (`tools/unattended/check-unattended.test.sh`, 1204 lines) the same way. **Adopts Unit A's contract verbatim** — same flag, same parser, same refusal, same floor treatment. It does not re-invent them.

### The one mechanism

Identical to Unit A. What differs is the seam, the hoists and the floors, which is why this is a second spec rather than a second paragraph.

The physical-split refutation is the same gate and I re-verified it: `check-arms.py:132` maps one gate to one sibling, and `.memory-tree.conf:178` pins `tools/unattended/check-unattended.sh:78:78`.

**Argument parsing — the defect that would have made every shard leg exit 2 on every bar.** The original brief specified manifest `["--shard","1/2"]` and a reader of `SHARD="${1:-}"`. The runner execs `"${argv[@]}"` (`run-gates.sh:786`), so `$1` is `--shard`. Under the brief's own dispatcher that is "anything else", and both legs refuse forever. Parse the flag: `SHARD=""; [ "${1:-}" = --shard ] && { SHARD="${2:-}"; shift 2; }`, with a bare `--shard` (empty `$2`) taking the same refusal branch as an unrecognised value.

**"Its arms are genuinely independent" is FALSE at arm granularity** — the report's seam guidance is half true, and a builder who trusts it cuts in the wrong place. Arms chain inside blocks: `:256-265` (the control at `:265` edits a file created by the `:259` commit), `:345-388` (five arms ride one commit at `:359`, restoring with `git checkout -q -- skills/session-kickoff/SKILL.md` at `:369`/`:375`/`:382`), `:408-427`, `:434-460`, `:722-810` (`WP` at `:754`, `wreset` at `:755`, restore only at `:810`), `:941-1000`, `:1012-1043`.

What **is** independent is the `reset_tree`-led block. **Do not write a count of them into the spec** — the original brief said "~30" and I derived 112 lines beginning `reset_tree` in that file. Derive it in the checker if a number is needed; the design rule is "one boundary, at a block edge".

`reset_tree` (`:118-124`) does `git reset -q --hard "$PRISTINE"`, `git clean -qfd`, then a batched `update-ref --stdin --no-deref` deleting `refs/remotes/` and `refs/replace/` and repointing `refs/remotes/origin/main` at `ANCHOR0`. It does **not** restore the ORIGIN bare repo's refs, any `refs/heads/` ref including local `main`, the checked-out branch, the remote URL, or `info/grafts`.

### The seam

**The boundary is a MEASUREMENT, not a guess, and the one concrete candidate in the source briefs was off by one.** Check 14 spans `:576-587`; its last line is the `miss "$(run)" "also carries a grafts file"` control at `:587`, with `rm -f "$gf"` at `:586`. I read those lines. Cutting "after `:586`" separates an arm from its control — the exact defect the design's own risk list forbids. **Candidate boundaries: after `:587`** (end of check 14) **and after `:574`** (end of the lifecycle block, and the edge that keeps the un-restored `main`/origin state entirely inside shard one). Time both standalone, then confirm in-pool, and record the rejected timing.

Do not pick by arm count. `$(run` splits 66/64 at line 596, but `git ` tokens split 89 before line 576 against 41 from it — the first half owns the pushes, the merges and four `anchor_break`/`anchor_restore` cycles at `:484-527`. The bar's floor is the **larger** shard, so imbalance eats the win directly.

**Manifest guard:** both rows carry the existing three-entry array byte-identically — `["memory/guides/UNATTENDED-PROTOCOL.md","tools/lib/","tools/unattended/"]` (`tools/gate-legs.json:593-597`). Note this differs from the driver's two-entry guard at `:606-609`, which I verified: **the identical-guard rule is within a sibling pair, not across the two units.** Divergent guards inside a pair would let a diff run one half and skip the other while the summary reads green.

### Gate pins this unit moves

All of Unit A's rows, at this leg's own coordinates — `tools/gate-legs.json:588-599`, `tools/unattended/kit.toml:92-95`, `memory/map/features/unattended.md:11` (a second key swap), `memory/map/generated/inventories.json:86`, `memory/map/generated/MAP.md:93` — plus:

| Pin | File:line | Note |
|---|---|---|
| `FLOOR_ASSERTIONS=200` | `tools/unattended/check-unattended.test.sh:1201-1202` | per-part floors + sum assertion evaluated in every invocation |
| **the sibling's floor** | `tools/unattended/unattended.test.sh:2241` | identical treatment, same landing, absent from the original brief |
| the charter arm pair | `tools/run-gates/run-gates.gov.test.sh:210-215` | moves with `AGENTS.md:498` — **this is why the original AC12 was unsatisfiable**: `GATE_FULL=1` cannot be green while the charter figures move and the arm still greps for `873 s`/`4018 s` |
| prose count of a derived population | `tools/gate-legs.json:584` | the `impure` note reads "the only leg of the 86" against a manifest of 88. Re-derive or drop |
| backlog row | `memory/backlog/TOOL.md:123` | `TOOL-aPacedTurnstile-8`, the row this pair discharges |
| **UNMOVED** | `tools/drift-audit/drift_signals.py:155` | `HANDKEPT` is empty precisely so units adding legs do not red `drift-audit records` |
| **UNMOVED** | `memory/map/baseline.toml` | carries no unattended key; the shrink-only ratchet is untouched |
| **UNMOVED** | `tools/govkit/matrix.py:48,56-65` | `SCRATCH_EXPECT` is scoped to `SCRATCH_KITS`, which excludes unattended |

### Observed RED before believed

1. **The dispatcher's refusal.** `--shard 3/2`, `--shard two`, bare `--shard`. Each exits 2 quoting the argument. **Observe RED against the current file first**: today argv is ignored, so the pre-change run exits 0 after a full 635 s suite — the silent-full-run failure demonstrated rather than argued.
2. **The sum pin.** Set the two floors to sum to 199. All three invocations must red naming the sum.
3. **A stranded part.** Delete one block from part two; `--shard 2/2` reds on its own floor with the existing "arms are UNREACHABLE rather than absent" text. This is `TOOL-cBriefedPilot-23`'s defect re-proved at half granularity.
4. **Divergent guards.** Give the two rows different `guard` arrays, touch only `memory/guides/UNATTENDED-PROTOCOL.md`, run the bar. One shard runs, the other prints the guarded-skip row, and the bar is green having tested half the leg. Revert.
5. **The descriptor claim.** Remove one shard leg from `tools/unattended/kit.toml`; `govkit selfcheck` reds at `govkit.py:901-903`.
6. **The leg name.** Name a leg `unattended gate selftest (1/2)`; `govkit selfcheck` reds at `govkit.py:879`.

### Acceptance criteria

- **AC1** — each shard exits 0 and prints `PASS (<n> assertions)`. *(Satisfiable only with the corrected flag parsing.)*
- **AC2** *(replaced — the original arithmetic could not see the risk it looked like it covered)* — each shard's per-arm PASS/FAIL **vector** equals the corresponding slice of the unsharded run at the same commit. The naive `n1 + n2 == n` holds **structurally**: `hit`/`miss`/`same` (`:16-18`) and `mutate` (`:134`) increment unconditionally when reached, the two source-level bumps at `:632` and `:640` are unconditional, and the only loop is a fixed three-iteration `for ph in LANDING LANDED VERIFYING` at `:424-427`. So the count equality passes even if the leaked `refs/heads/ahead` (`:556`) makes a shard-two arm pass for a different reason. Additionally observe both shards at a commit where a known arm is deliberately broken, so the equality is exercised red as well as green.
- **AC3** — the unsharded invocation still exits 0 above `FLOOR_ASSERTIONS`.
- **AC4** — `--shard 3/2`, `--shard two`, bare `--shard`: exit 2, refusal names the argument, suite does not run.
- **AC5** — the per-part floors sum to at least `FLOOR_ASSERTIONS`, asserted in every invocation; setting the sum to 199 reds all three.
- **AC6** — byte-identical `guard` arrays **within this pair**, both `"chunk": "selftests"`; a diff touching only `memory/guides/UNATTENDED-PROTOCOL.md` runs both or skips both.
- **AC7** — `max(shard one, shard two)` standalone is at most 55 % of the unsharded standalone wall; both candidate boundary timings recorded, including the rejected one.
- **AC8** — `check-arms.py --check` green with `.memory-tree.conf:178` unchanged.
- **AC9** — `check-testsuite-counts.sh` green, no new waiver row.
- **AC10** — `govkit selfcheck` green, retired name absent from the manifest.
- **AC11** — codebase-map coverage + freshness green, both directions, same commit.
- **AC12** *(now satisfiable)* — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` green, with the charter sentence and both gov-canary arm halves moved in the same commit; run record shows both shard legs as separate rows with separate input keys (`run-gates.sh:701` folds argv into the input key).
- **AC13** — the suite header states that a green shard leg is evidence about its own part only, and where the whole-suite claim lives.
- **AC14** — the sibling ships in the same landing, or the win is 3.7 % instead of 27.6 %.
- **AC15** *(new — nothing in the original set observed the objective)* — over N `GATE_FULL` bars at the same profile row and width, the mean span reconstructed from `<git-dir>/gate-run/<id>/*.leg` is at least X s below the recorded pre-change mean, with both means and N quoted in the build record. The report's §1 method makes this free: every bar already writes per-leg start/end in nanoseconds.

### Risks

Everything in Unit A's list, plus:

- **State leaks forward across any boundary.** `:556` pushes `refs/heads/ahead` to the origin and nothing deletes it — `check-unattended.sh:243-245`'s `is_published()` reads `$ADV_TIPS` from `ls-remote --heads` (`:233`), so from `:556` onward every `run()` sees an extra advertised tip a fresh prologue would not. `:564-574` leaves local `main` and origin `main` at a merge commit until `:810`. **Settle this by RUNNING both shards, never by reasoning about it.**
- **Two controls lose their meaning without failing.** `:710-712` ("the tree is still clean after nine mutations") is a control only if the nine mutations ran in the same process; split away, it degrades into a duplicate of the opening control at `:140-142`. Same shape at `:283` and `:1019`.
- **The sibling's boundary is not free** — an omission from every source brief. `tools/unattended/unattended.test.sh` establishes three sequential anchors by real fixture work (`UNIT0=` `:163`, `RPRISTINE=` `:301`, `BCP=` `:703`) with four reset helpers keyed to them. A prologue-plus-part-two shard of that file is legal only at those lines or with the anchor-building blocks replayed. Unit A's hoist strategy is what discharges this; the report's ~2.75 s/split price does not cover it.
- **Wrapping ~570-line bodies in functions without reindenting is deliberately ugly** and will invite a later reindent producing an unreviewable diff. Say why at each brace, in the file.
- Sharding splits work; it does not remove it. After both siblings shard the bar is throughput-bound at ~766 s and a third shard buys exactly zero.

---

## Unit C — `ledger-common-dir`

The dispatch hint reads a repository-wide store; the reuse **key** stays per-worktree.

### The one mechanism

Split the one file by its two jobs, at the line that already fused them.

1. **READ — the hint.** `tools/run-gates/run-gates.sh:158` is `TIMINGS="$LEDGER"`, with its own comment at `:156-157` already naming the two jobs. Replace with an ordered candidate list, de-duplicated by resolved path: `$gd/gate-ledger.tsv`, `<common>/gate-ledger.tsv`, `$gd/gate-timings.tsv`, `<common>/gate-timings.tsv`. Merge **first-wins per leg name**, so coverage is strictly ≥ either single source.
2. **READ — the reuse key.** `$LEDGER` at `:155` stays exactly `$gd/gate-ledger.tsv`; the reuse loop at `:750-766` opens it and nothing else, forever.
3. **PARSER.** `:629` already takes the cache as `sys.argv[2]`; widen to `argv[2:]` with `durs.setdefault`. Change the blanket `except: durs = {}` at `:635-636` to a **per-file** try, so a corrupt low-precedence file cannot blank a good high-precedence one.
4. **WRITE.** `:970-994` unchanged — the keyed per-worktree ledger still goes to `$gd`, because `profile_bar.py:284,294` reads `rev-parse --git-dir` + `gate-ledger.tsv` and refuses when that file did not move. After `:994`, when `<common>` resolves **and differs from `$gd`**, publish a duration-only projection (fields 1–2, field 4 forced to `-`) to `<common>/gate-ledger.tsv`, applying the **same `awk` carry-forward as `:991`** and the same atomic `mv -f`. Field 4 forced to `-` is defence in depth: `:761` requires a key that is non-empty and not `-`.
5. **SAY IT — with the corrections that keep it from breaking two gates.**
   - `PROF_LINE` at `:374` gains one tail field naming the hint source, keeping its position **ahead of** the turnstile wait at `:475-518` so it is not hidden behind a queue.
   - **The vocabulary needs four tokens minimum**, not three: the candidate list creates *per-worktree only* (today's primary tree), *common only* (every cold worktree after this lands), *both*, and *legacy*, plus `NONE`. A three-token vocabulary cannot name two of the states it creates.
   - **Coverage `<k>/<total>` goes on its own second output row, never appended to the dispatch header line.** `:653` assigns manifest line 1 to `ORDER` and `:900` does `disp=($ORDER)`; a non-numeric token there becomes `k` at `:930` and `${names[$k]}` at `:931` resolves an unset name to index 0 — leg 0 dispatched twice, one leg reporting `(no result)` = FAIL at `:840`. **That is a verdict change**, which the runner's own comment at `:617` says a hint may never cause.
   - **The new stdout line must be filtered by name in the width-equivalence arm.** `tools/run-gates/run-gates.test.sh:236-248` compares full stdout across a width-1 and a width-4 run of the same scratch, filtering only `^gate profile: `. The scratch's ledger is **not** cleared between runs (only `fx/ts` is, at `:230`), so run 1 emits a cold coverage figure and run 2 a warm one, and the canary fails with a diff. Extend the filter to `^gate (profile|dispatch): ` **and** add the companion presence check that the arm's own comment at `:238-241` demands — a filter with no presence check makes any regression in the filtered line invisible.
   - Header keys `dispatch_source` and `dispatch_known` join `dispatch` at `:735-736`.
6. **Path flavour — one resolution, one spelling.** Do **not** introduce `--path-format=absolute` here. The runner's own idiom is `cd "$(git rev-parse --git-common-dir)" && pwd` (`:392`), `$gd` at `:92` is the **relative** `.git` in the primary tree, and `:75-78` states the rule verbatim: *"Never compare path strings across flavours."* Resolve `<common>` once at `:154` through that chain, have the turnstile at `:391-392` read the variable instead of re-resolving, and normalise `$gd` through the same chain before any dedupe or equality test.
7. **HEADERS.** State what is not checked: the hint can never change a verdict; the coverage count says how many manifest names the hint knew, not whether those durations are current; the shared file's key column is read by nothing.

**Seam:** `run-gates.sh:158`, whose own comment already argues the split. Secondary seams already parameterised: the cache argument at `:629`, and the common-dir resolution at `:391-392`.

### Gate pins this unit moves

| Pin | File:line |
|---|---|
| `last-audit` — `tools/run-gates/run-gates.sh` is a `watch:` path and `AGENTS.md` a `verify-paths:` entry | `memory/guides/SESSION-KICKOFF.md:5-6` |
| `FLOOR_ASSERTIONS=102` — candidate resolution, legacy fallback, per-file corrupt-cache isolation, the coverage line, the property arm | `tools/run-gates/run-gates.test.sh:45` |
| `FLOOR_ASSERTIONS=51` — the never-reuse-from-common arm plus its control | `tools/run-gates/run-gates.evidence.test.sh:26` |
| `FLOOR_ASSERTIONS=28` — arm 10's population line widened | `tools/run-gates/run-gates.turnstile.test.sh:26` |
| `FLOOR_ASSERTIONS=12` — the charter arm pair | `tools/run-gates/run-gates.gov.test.sh:70` |
| **the runner may not spell a leg's argv path** | `tools/run-gates/run-gates.test.sh:157-171` — greps `run-gates.sh` for every leg argv path and reds on a hit. State the `profile_bar` coupling by naming the tool, not `tools/run-gates/profile_bar.test.sh` |
| four literal-string pins the `AGENTS.md` edit must **preserve** | `tools/run-gates/run-gates.gov.test.sh:210-215` (`873 s`/`4018 s`) and `:219-225` (`min(8, nproc)` negative, `tools/run-gates/gate-profiles.txt` positive) |
| the charter sentence naming the dead `gate-timings.tsv` as the live cache | `AGENTS.md:496` — already wrong (`TOOL-aMeteredTurnstile-4`); this unit makes it wrong in a new way |
| dossier prose that becomes false | `memory/map/features/run-gates.md:47-53` ("One store") |
| ungated prose | `tools/run-gates/README.md:82` — `check-dead-paths.sh` derives needles from deleted **tracked** basenames and a git-dir path was never tracked, so nothing gates it. §7 says the gov canary is where a confirmed finding of this class belongs |
| backlog | `memory/backlog/TOOL.md:147` closed; `:12` (`TOOL-aMeteredTurnstile-3`) refined, not closed |
| ledger row orphaning | `<git-dir>/gate-ledger.tsv` — rows keyed on leg name at `:983`, read at `:637` |
| **UNMOVED, and named because a reader will assume it moves** | `tools/run-gates/profile_bar.test.sh:21` `FLOOR_ASSERTIONS=33` — the per-worktree keyed write is preserved precisely so `profile_bar.py` needs no edit |
| **UNMOVED** | `memory/project/unarmed-branches.txt` — `run-gates.sh` defines no `fail() {` helper, so `check-arms.py`'s population (HELPER_RE at `:56`) excludes it, and `.memory-tree.conf:178` carries no run-gates row. The runner's header should say so, because a reader will assume otherwise |
| **UNMOVED** | leg count stays 88 (derived, not typed); no manifest-population pin moves |
| context, so nobody re-derives it | `memory/backlog/TOOL.md` is 60,156 B against `INDEX_CAP_BYTES="61440"` (`.memory-tree.conf:147`); the debt row at `memory/project/curation-debt.txt:23` silences checks 6, 7 **and** 8 on that file |

### Observed RED before believed

**A. The headline.** No existing harness builds the fixture this unit is about — a **linked worktree of a scratch repo**. Build it: scratch repo with two legs of known unequal duration; one bar in the primary (populates `<common>`); `git worktree add` a linked worktree of that scratch; first bar there. Read `$RUNDIR/header`'s `dispatch` key. At HEAD it is manifest order; after the change it is longest-first. Assert **both** directions so a runner that stopped emitting the key cannot pass.

**B. The probe that cannot move.** Same fixture, every candidate removed. Assert stdout carries `0/<n>` with `<n>` derived from `${#names[@]}` at emission, the PROF_LINE tail carries `NONE`, and the header carries `dispatch_source\tNONE`. Stage the break by having the resolver report the source it **looked for** rather than the one it **found** — the arm must red on a hint file that exists but covers zero manifest names.

**C. The soundness control.** Plant a green keyed row for leg X in `<common>` only, in a linked worktree with `GATE_REUSE=1`. Assert `GATE ok X` and **not** `GATE reuse X` — carrying its control on the **same run**: a leg Y whose keyed row is in the per-worktree ledger must print `GATE reuse Y`. That is the shape the existing arms already use at `run-gates.evidence.test.sh:474-478` and `:493-499`. Stage the break by pointing `$LEDGER` at the common path.

**D. The carry-forward.** Delete the `awk` merge from the projection write; confirm a guard-scoped run **blanks** a skipped leg's row in `<common>`; unstage. Without this arm, criterion 6 below has no observed red.

### Acceptance criteria

1. A first-ever bar in a linked worktree of a scratch repo whose primary has run once writes a `dispatch` header key that is not manifest order and whose leading index is the longest leg. **Durable negative direction:** *the same fixture with every candidate file removed writes manifest order.* (The original "the same fixture at HEAD writes manifest order" stops being true the moment the change lands — keep it as the pre-landing RED observation only.)
2. With only `<common>/gate-timings.tsv` present and no ledger anywhere, `dispatch` is not manifest order and the source token names `legacy` — the nine worktrees the report measured recover their hint without running a bar. **The coverage count is load-bearing because it separates 78.4 % from 100 %**, which I measured on this node today, not because the legacy file knows "almost nothing".
3. With no candidate present: `0/<n>` on stdout with `<n>` derived at emission, `NONE` in the PROF_LINE tail and in `dispatch_source`.
4. A green keyed row present only in `<common>`, `GATE_REUSE=1`, yields `GATE ok` and never `GATE reuse`, with the same-run control proving a per-worktree row does yield `GATE reuse`.
5. *(corrected — the original was vacuous)* `$gd/gate-ledger.tsv` keeps HEAD's exact 5-field shape, and **`python tools/run-gates/profile_bar.py --width N` — not `--report` — run from inside a linked worktree of a scratch repo does not print `did not move`.** `profile_bar.py:297-298` returns `print_last(record_path)` before `before_mtime` is taken at `:325` and before the refusal at `:373-377`, so `--report` cannot exercise that refusal in any tree.
6. A guard-scoped run in a linked worktree does not remove a skipped leg's row from `<common>` — read before and after — **with the staged-break RED of observation D.**
7. In the primary tree exactly **one** ledger file is written, it still carries real keys, and no self-merge occurs — asserted by **content plus "exactly one file exists"**, not by inode (unreliable on MSYS) and not by absence of an error.
8. Every leg driving a nested runner resolves a git common dir different from the real repo's, asserted over a **manifest-derived population** that selects every such leg, not the one leg `turnstile.test.sh:263-269` currently selects.
9. Stdout of a warm-hint run, filtered of `gate profile:` and `gate dispatch:`, is byte-identical to the same tree with every hint removed — the existing control at `run-gates.evidence.test.sh:485-489` extended.
10. *(corrected — assert the property, not the spelling)* No leg's scratch repo shares the real repo's git common dir. The original "ban `git worktree add` in leg scripts" would red the very arms this unit adds, and `tools/memory-recall/recall-opened.test.sh:100` already uses that spelling legitimately. Extend the dynamic probe at `turnstile.test.sh:275-280` over the widened population from criterion 8, using the git-identity idiom at `run-gates.test.sh:559-562` rather than path-string comparison.
11. **The win, observed in both directions** *(new — nothing in the original set measured it)*: a cold linked worktree's floor leg moves from a late dispatch rank to rank 1 with the ledger present, and back to manifest order with it removed.

### Risks

- **Time-to-first-signal is the top risk and it is measured.** Report §4 R1: 669.1 s to first verdict on a warm ledger against 5.1 s cold — a **131×** swing decided solely by ledger warmth. Today 24 of 26 worktrees were *accidentally* protected by having no hint; this unit removes that protection everywhere at once. **Hard sequencing constraint: land with the reserved-short-leg-slot unit (`TOOL-aMeteredTurnstile-5`) or a real 16 % win reads as a regression to the person who filed the complaint.** The new coverage line explains the silence; it does not remove it.
- **The projection's carry-forward.** Omit the `:991` merge and a guard-scoped run in a linked worktree blanks the shared hint for every leg its guards skipped — the defect the comment at `:985-989` records, reintroduced one file over, now degrading every *other* worktree.
- **The primary tree's `$gd` IS `<common>`.** Every dedupe and equality test must handle it or the primary merges its ledger with itself and strips its own keys.
- **A present-but-stale hint** would print a reassuring source token; the coverage count is what discharges it.
- **Sharing spreads a bad hint** repository-wide where today the damage is confined. Bounded: durations are advisory (`:616-618`, `:636`) and cost wall clock only.
- **The turnstile is not a lock** — three documented escapes: `GATE_TURNSTILE=0` (`:390`), the fail-open at `:487-493` ("running UNQUEUED alongside whatever holds the beacon", message at `:491`), and an empty `TS_COMMON` (`:391-393`). The atomic `mv -f` must be preserved on the projection; the residual is a lost update costing dispatch quality only.
- **The nested-run proof leans on an arm whose population line is near-vacuous.** `turnstile.test.sh:263-269` selects legs whose argv contains `run-gates.sh`, which on the live manifest matches exactly **one** (`run-gates wiring`, via `adopt-run-gates.sh`), while at least six legs actually drive a nested runner. The property arm at `:275-280` still executes on its own probe repo, so the proof stands; the population line does not, and this design depends on it. **Fold the fix in** — it is a defect in an arm this unit's proof rests on.

---

## Unit D — `queue-key`

Record the turnstile queue wait: two header keys, one summary line, zero new stdout bytes. **Buys 0 s of span, and is the only way to see the largest component of the complaint** (report §4 R3). A lander queueing behind one peer experiences ~31–35 min where every span in the report reads ~16 (report §3.4).

### The one mechanism

Build the wait once, after the turnstile resolves, and emit it at three sites the way `PROF_LINE` already is.

1. **At `run-gates.sh:518`**, resolve a closed four-word state from variables already in scope (`TS_COMMON` `:391-392`, `TS_HELD` `:389`/`:470`, `TS_WAITED` `:389`/`:486`): `held` when `TS_HELD=1`; `expired` when `TS_COMMON` is non-empty and `TS_HELD=0` (the fail-open at `:487-493`); `unresolved` when the turnstile was on but `TS_COMMON` came back empty at `:392`; `off` when `GATE_TURNSTILE=0` (`:390`). Value = `TS_WAITED` for `held`/`expired`; a literal `-` for `off`/`unresolved`, this file's own idiom for an unmeasurable value (`:682-683`: *"an unmeasurable input is NOT a reusable one: the key is a dash"*). The `echo "gate queue: waited ${TS_WAITED}s"` format string is **unchanged**.
2. **Two header keys**, inserted after the `worktree` printf at `:732` and before the dispatch comment at `:733-735` — deliberately **outside** the run-envelope block at `:722-730`:
   ```
   printf 'queued\t%s\n'      "$QUEUED"
   printf 'queued_from\t%s\n' "$QUEUED_FROM"
   ```
   The pairing is the header's own grammar: `base`/`base_from` (`:714-715`), `full`/`full_from` (`:720-721`), `profile_row`/`profile_from` (`:727`/`:730`).
   **The real justification for the second key is a TWO-way ambiguity, not three.** With `-` emitted for `off` and `unresolved`, `queued 0` can only mean held-and-uncontended (an `expired` run requires n ≥ `TS_MAXWAIT`, which is `TS_TTL * 4` at `:410` and therefore ≥ 4). `queued_from` earns its place by carrying the **held/expired** split a bare integer cannot, and by separating `off` from `unresolved`. Say that, not the three-way story.
   **Placement outside the envelope is prose hygiene, not a pin.** I read `run-gates.evidence.test.sh:411-419`: the four-key arm selects by name via `awk -F'\t' '$1=="profile_row"'` and friends, so keys placed inside the block would leave the arm green and only its comment lying. Keep them outside so the comment stays true.
3. **The header is the right file** — the wait is final at `:518`, long before dispatch, and the header survives a crash while the verdict does not.
4. **`schema\t1` at `:710` does not bump.** I grepped: `run-gates.sh:710` is the only occurrence in `tools/run-gates/` and `.githooks/`. The predicate that would read it lives only in a spec table (`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-7.md:263`); what shipped at `.githooks/pre-push:104-135` reads `gate-full-green` with its own key set. Every real reader selects **by key name**, so an additive key breaks none — §12's forward-compatible-data rule. A bump could not be armed anyway: nothing observes the field, so its failing case cannot be staged.
5. **`gate-last-summary.txt`, always, as its own line** — after `PROF_LINE` at `:1066` (green), `:1069` (red), `:1075` (the RED-only durable copy). One string built once at `:518` and emitted, exactly as `PROF_LINE` is built once at `:374` and emitted at `:375`/`:1066`/`:1069`/`:1075`. A conditional line makes an absent line mean two things.
6. **One fidelity fix, in scope because otherwise the recorded number is wrong.** `TS_WAITED` is last refreshed at `:486`; the acquire arm `break`s at `:483` without refreshing, and `ts_try_reap && continue` at `:485` skips the refresh entirely. Add `TS_WAITED=$(( $(ts_now) - ts_start ))` immediately before the `break` at `:483`, inside the `[ -n "$TS_COMMON" ]` block where `ts_start` (`:459`) is in scope. **"Byte-identical stdout" is true of the FORMAT only** — this deliberately changes the VALUE on contended runs, which is the point.

**Seam:** `PROF_LINE`, `run-gates.sh:374-375`. One run-envelope fact three audiences need, built once as a string and emitted at several sites so the copies cannot drift. `QUEUE_SUMMARY` is the same shape built at `:518` instead of `:374`, for the one reason `PROF_LINE` cannot absorb the wait: it is echoed at `:375`, **before** the turnstile block at `:389-518`, and folding the wait in would delay the profile line by the entire queue wait. Second seam, for the keys: the header's value/`_from` pairing — a fourth instance of a pattern with three.

**Reuse probe:** `python tools/codebase-map/reuse_lookup.py` ranked 30 candidates, all python/js/dossier, and **declared its own blindness**: *"recall partial: layers bash have no symbol extractor — a matching seam THERE would not appear above."* Every file this unit touches is bash. The refusal is the useful output; both seams above come from the hand check it demands. That is a probe that cannot move saying so.

**What this does NOT do**, stated because a gate's header must say so: it does not fix the stdout line's own zero-ambiguity — `gate queue: waited 0s` still prints when `GATE_TURNSTILE=0`. The bytes are pinned by two consumers (`profile_bar.py:342`'s `$`-anchored regex and `run-gates.turnstile.test.sh:306`), so moving them is a separate unit. It also does not teach `profile_bar.py` to read the header: that tool launches the runner itself (`:330`) and already sees every wait it can be in a position to see. The header is for the runs it never brackets.

### Gate pins this unit moves

| Pin | File:line | Note |
|---|---|---|
| `FLOOR_ASSERTIONS=28` | `tools/run-gates/run-gates.turnstile.test.sh:26` | four new arms; the compare at `:341` is `-ge` so it will not red, but leaving it strands them |
| `last-audit` | `memory/guides/SESSION-KICKOFF.md:5` | `tools/run-gates/run-gates.sh` is a `watch:` path |
| backlog row | `memory/backlog/TOOL.md:148` | states "the run-record header has 19 keys" — I counted 19 printfs at `:710-736`. **Close the row rather than restating the number** |
| **the byte cap this closure sits under** | `.memory-tree.conf:147` `INDEX_CAP_BYTES="61440"` vs `memory/backlog/TOOL.md` at 60,156 B — **1,284 B of headroom** | closing the row must shrink it; the remedy for an overflow is an archive rotation, not an edit. `memory/project/curation-debt.txt:23` silences checks 6, 7 and 8 on that file today |
| dossier prose | `memory/map/features/run-gates.md:36-48` | this dossier owns `tools/run-gates/` and claims the `run-gates turnstile` leg the arms land on |
| README clause | `tools/run-gates/README.md:57-62` | "so a wrapper can tell waiting from working" is now half the story. Explicitly do **not** add a key list at `:75-82` |
| dated measurement — **do not rewrite** | report `:214-243`, `:424-432` | record the change in `memory/DECISIONS.md` instead |
| **CHECKED, unmoved** | `memory/map/generated/inventories.json` (88 gate-legs), `memory/map/baseline.toml` | no leg is added; the arms go into suites the manifest already runs. Putting them in a new leg would move both plus the coverage gate |
| **CHECKED, unmoved** | `memory/project/unarmed-branches.txt` | `run-gates.sh` defines no `fail() {` |
| **CHECKED, unmoved** | `memory/project/testsuite-count-waivers.txt` | neither run-gates suite is listed; both already print the shape and pin a floor |
| **CHECKED, unmoved** | `tools/run-gates/run-gates.turnstile.test.sh:306`, `tools/run-gates/profile_bar.py:342` | byte pins on the stdout line — **if either needs editing, the design was violated** |
| **CHECKED, unmoved** | `tools/run-gates/kit.toml [gate_runner_seed]`, `tools/line-length-limits.txt`, the four `gate-last-summary.txt` consumers, `profile_bar.py`'s `"queued"` JSON key | no new stdout line, no new line-count pin |
| **CHECKED, unmoved** | `.memory-tree.conf:178` ARMS_FLOORS | `run-gates.sh` is absent from it and stays absent |

### Observed RED before believed

Four arms, four states. Three cost zero seconds because they read a run record an existing fixture already produces and throws away.

**A — the number MOVES under contention.** After `rm -rf "$B8"; wait "$w8"` at `turnstile.test.sh:195`. That fixture plants a live-pid beacon (`:180-181`), launches a real runner (`:183`), polls until it announces a position, then releases. Assert `queued` > 0 and `queued_from = held`. Stage the break: delete the two printfs → RED. **Second break, the one that matters:** keep the printfs, revert the `:483` fidelity fix, set `GATE_TURNSTILE_TICK` high enough that the stale value reads 0 — the arm must red on the **understatement**, not merely on the absence. Do not pin a tick-exact number: this harness documents its timing bites at `:283-292`. Grade `> 0` and `<= <elapsed the harness itself observed>`.

**B — `expired` is not `held`. THIS FIXTURE MUST BE BUILT; the R9 piggyback does not reach the branch, and I traced it.** `turnstile.test.sh:199-210` sets `GATE_TURNSTILE_TTL=1 GATE_TURNSTILE_TICK=1` with a **static** planted heartbeat. Every `gate-profiles.txt` row declares `timeout=0` (`:46`, `:54`, `:61`), so `PROF_TIMEOUT=0`, `TS_TTL=${GATE_TURNSTILE_TTL:-1800}` = 1 (`:405`) and `TS_MAXWAIT = TS_TTL * 4` = 4 (`:410`). `ts_try_reap` at `:485` fires on heartbeat age > TTL at t≈2 s, long before `TS_WAITED` reaches 4 — the run **reaps** and ends `held`. The suite's own arm admits it by accepting either outcome (`grep -q 'WAIT EXPIRED\|stalled holder'` at `:205`), and its comment at `:202-203` claims "TTL 600" while the code beside it sets 1. **Reaching `expired` needs a heartbeat REFRESHER**: a background loop rewriting `$B/heartbeat` every 1 s at `GATE_TURNSTILE_TTL=2 GATE_TURNSTILE_TICK=1` keeps age ≤ 1 while `TS_MAXWAIT=8` burns. **Cost ≈ 9 s on a 232.5 s leg. Budget it.** Stage the break: make the state resolution read `TS_COMMON` alone and ignore `TS_HELD` — the run then reports `held` while having run UNQUEUED alongside the planted beacon.

**C — uncontended zero is a real zero.** In the R12 `qline` block at `:302-313`: `queued = 0`, `queued_from = held`, and the header's `queued` agrees with the stdout line's `waited Ns` on the same run. That cross-check is the cheapest guard against the two emissions drifting, and the reason to feed them from one variable.

**D — a disabled turnstile writes a DASH.** One extra invocation in the R12 repo with `GATE_TURNSTILE=0`: `queued = -`, `queued_from = off`. Stage the break: make the `off` branch emit `0` → RED naming the class. This is the dead-probe arm and the whole justification for the second key; if it is cut, cut the key with it and say plainly in the header comment that the zero is ambiguous.

**Control for the whole set:** `turnstile.test.sh:306` and the profiler arms at `:315-336` still pass unmodified.

**Before any of this:** run `bash tools/check-wiring.sh --fix` in the worktree (a fresh worktree smudges unpinned paths to CRLF and reds the bar for unrelated reasons), then verify staged bytes with `git diff --cached | cat -A` — `.sh` is LF-pinned and `git show` misleads on Windows.

### Acceptance criteria

1. A contended run's header carries `queued\t<n>` with n > 0 and `queued_from\theld`.
2. An uncontended run carries `queued\t0` and `queued_from\theld`, and that 0 equals the stdout number on the same run.
3. A `GATE_TURNSTILE=0` run carries `queued\t-` and `queued_from\toff`. A grep for `^queued\t0$` on that run returns nothing.
4. A run that burned the bounded wait carries `queued_from\texpired` with n > 0 — **observed on the purpose-built heartbeat-refresher fixture.** If that fixture is cut, this criterion is cut with it and `expired` is listed in the header's own "does NOT check" section as an unarmed arm. Do not keep an acceptance bullet no fixture can reach.
5. *(restated by CONTENT, because the `:483` insertion shifts every line below it)* `git diff -U0` contains **no hunk touching the `gate queue: waited ${TS_WAITED}s` echo**, `turnstile.test.sh:306` passes unmodified, and `profile_bar.py:342`'s regex is untouched.
6. *(same restatement)* `git diff -U0` contains **no hunk touching the `printf 'schema\t1\n'` line**.
7. The four-key envelope arm at `run-gates.evidence.test.sh:408-428` passes unmodified across both `capable` and `minimal` rows.
8. `gate-last-summary.txt` carries the queue line on green **and** red runs, and `gate-last-failure.txt` carries it too.
9. The wait recorded does not understate by a full tick, with the `:483` refresh in place.
10. `bash tools/run-gates/run-gates.turnstile.test.sh` prints PASS at or above a raised floor; `bash tools/check-testsuite-counts.sh` exits 0 silently.
11. *(restated as arithmetic, not "within noise")* `GATE_FULL=1 bash tools/run-gates/run-gates.sh` is GREEN and span movement is **zero by construction**: the turnstile leg at 232.5 s plus ~10 s stays far below the floor leg at 812–926 s, and the bar is floor-bound.
12. Every one of the four arms observed RED against a staged break, with the RED text naming a literal slice of that arm's own failure message.

### Risks

- **The strongest temptation is to append the state word to the stdout line.** It breaks `profile_bar.py:342` (`$`-anchored) and `turnstile.test.sh:306`, reddening the leg whose whole job is to measure this. The state lives in the header and the summary.
- **Shipping the key without the `:483` fix** records a number that is quietly wrong and gives it durable authority — worse than today, where nobody can cite it.
- **Putting the arms in `run-gates.evidence.test.sh`** inherits `TOOL-aScannedThrottle-7` (`memory/backlog/TOOL.md:153`): `:225` gives a nested `GATE_FULL` bar `timeout -s KILL 5` to write its header against a measured 2136 ms in a two-file scratch repo. New fixtures there buy a flake in the leg that grades the run record.
- The turnstile harness is timing-sensitive by nature (`:283-292`). Grade values as ranges the harness itself observed.
- `schema` is a version field with no reader. Leaving it is honest for this unit but latent: the next person to add a key gets the same non-answer.

---

# UNIT DECOMPOSITION

**Five specs.** Four mechanisms plus one pre-existing dependency that is not a spec here.

| # | Spec | The one mechanism | Depends on |
|---|---|---|---|
| **S1** | `spec-queue-key` | Build the wait string once at `run-gates.sh:518`; emit it as two paired header keys and one summary line, the way `PROF_LINE` already is | nothing |
| **S2** | `spec-shard-driver` | `--shard i/n` flag + two guarded contiguous regions + six hoists + mode-selected floor, on `tools/unattended/unattended.test.sh`. **Defines the shard contract** (parse, refuse, floor selection, cover arm) | nothing; must co-land with S3 |
| **S3** | `spec-shard-gate` | The **same** contract, adopted verbatim, on `tools/unattended/check-unattended.test.sh` with its own measured boundary and hoists | S2 (contract), co-lands with it |
| **S4** | `spec-ledger-common-dir` | Split `TIMINGS` from `LEDGER` at `run-gates.sh:158`: hint reads a candidate list including the common dir, reuse key stays per-worktree, write projects duration-only to `<common>` | S2+S3 landed (they change the floor S4 schedules around); **externally gated on `TOOL-aMeteredTurnstile-5`** |
| **—** | `TOOL-aMeteredTurnstile-5` (reserved short-leg slot) | not written here; an existing backlog row | must land with or before S4 |

**Why S2 and S3 are two specs and not one.** The mechanism is one shape, but each file carries its own seam, its own hoist set, its own floors, its own fixture-epoch hazards and its own failing cases. One spec holding two independent seams is two specs wearing one heading. They are nonetheless **one landing** — the report's R2 is explicit that the driver alone buys 3.7 % because the gate selftest becomes the new floor.

**Why S2 goes first.** Its seam is **measured** — both halves built and run, 196 and 206 assertions, exit 0 — while S3's boundary is a live open question with two candidates. The contract belongs in the spec that has already exercised it.

**Dependency order: S1 → (S2 + S3, one landing) → S4.**

- **S1 first** because it is independent, buys 0 s, costs ~0 s, and gives the later units a way to *see* the queue component that the span measurements exclude.
- **S2+S3 next** because they move the floor, which is the only thing that moves span on a floor-bound bar, and because S4's dispatch work is scheduling around a floor that is about to change.
- **S4 last**, and gated: it makes every worktree's ledger warm, which is exactly the condition under which a renamed shard leg sorts last. Landing S4 before S2/S3 makes the shard rename penalty worse, not better.

**The charter figure (`AGENTS.md:498` + `run-gates.gov.test.sh:210-215`) moves exactly once, in the last span-moving landing, with a fresh measurement.** Three commits each moving it is three commits each reddening the next.

**Every one of S1–S4 owes a `last-audit` re-stamp at `memory/guides/SESSION-KICKOFF.md:5` with a `manifest-audit:` delta line**, because each edits a `watch:` path.

---

# OPEN QUESTIONS

Only those whose answer changes what gets built.

### Answerable from the source — answered here

1. **Does the shard flag ride in `argv` or a new manifest key?** **`argv`.** `tools/run-gates/run-gates.test.sh:96` pins `KNOWN = {name, argv, guard, impure, chunk}`, and argv length ≥ 2 is separately required at `:71-74`. A new key moves a pin for nothing.
2. **Can a physical file split be made to work?** **No, without changing the arms meta-gate's contract.** `check-arms.py:132` maps one gate to one sibling and `.memory-tree.conf:178` pins armed floors of 78 for both `unattended.sh` and `check-unattended.sh`. Rewriting the sibling relation is a change to `memory/HYGIENE.md:272-277` prose and to the harness, far outside any of these units.
3. **Does `schema\t1` bump?** **No.** Nothing reads it (grep over `tools/run-gates/` and `.githooks/` returns the writer alone), every real reader selects by key name, and a bump could not be armed. File a backlog row: implement the predicate or delete the field.
4. **Where do the shard-argument refusals live?** **Gov-only, in `tools/run-gates/run-gates.gov.test.sh`**, for this unit. The manifest **cover** arm must be gov-only because an adopter's manifest is emitted, not authored. Shipping the four argument refusals in `tools/unattended/cross-component.test.sh` is a named follow-up, so the unit does not grow a second subject.
5. **Does `expired` need its own fixture?** **Yes.** Traced above: R9's static heartbeat reaps at t≈2 s against `TS_MAXWAIT=4`. ~9 s on a 232.5 s leg. Budget it, or drop the criterion and name the unarmed arm in the header.
6. **Which reads the hint first — per-worktree or common?** **Per-worktree, first-wins**, because the merged result is strictly ≥ either single source in coverage. The report's wording ("common dir with a per-worktree fallback") is a different rule and changes what the source token can honestly say. Record the choice explicitly; do not leave two rules in the corpus.
7. **Is `turnstile.test.sh:263-269`'s population fix in scope for S4?** **Yes.** It is a defect in an arm S4's nested-run proof leans on — one leg selected where six qualify. Fixing it elsewhere leaves S4 resting on an arm it knows is near-vacuous.
8. **Does `memory/map/features/run-gates.md:62`'s "Seven of the 86 legs" get corrected?** It is a prose count of a derived population, already wrong (live count 88, derived). **The repo's own rule says delete it and point at the source.** It is a dossier edit with its own owner — flag it, do not fold it into a sharding spec.

### Scope forks for the owner

1. **The shard-1 name: keep `unattended driver selftest`, or rename both symmetrically?** Keeping it inherits the existing warm ledger row and halves the map/descriptor churn, at the cost of an asymmetric pair (`unattended driver selftest` / `unattended driver selftest shard B`). Renaming both is tidier and takes the sorts-last penalty on both shards on every warm tree. My recommendation is keep-and-append; the owner may prefer symmetry.
2. **Bump `KIT_UNATTENDED_VERSION` 1.7 → 1.8?** Nothing gates a bump on a content change — `tools/check-kit-versions.sh:123-151` only enforces internal consistency. But the descriptor's declared leg set is an adopter-visible contract and it changes. **Eight spellings across six files plus a re-render.** My read is bump.
3. **Does `TOOL-aPacedTurnstile-8` split into two ids?** They must land together to buy anything (one id); they are two files with two floors and two boundaries (two ids). Owner's call; it decides whether S2 and S3 share a backlog row.
4. **Does the legacy `gate-timings.tsv` read fallback expire?** A permanent fallback keeps a dead filename alive forever; a one-shot migrate-then-delete needs a write to the git dir on the READ path, which S4 otherwise avoids entirely. At 78.4 % coverage the fallback is worth something today and worth nothing once every worktree has run a bar.
5. **The `input_key` hole — act now or file it?** `input_key` hashes `HEAD^{tree}`, never HEAD's commit sha, so legs whose verdict reads git **history** (`kickoff-manifest ratchet`, `verdict epoch`, `drift-audit records`) can differ at an equal key. Two worktrees cut from the same `origin/main` with the same tree and different shas share a key. **The hole exists today inside one worktree; S4 does not create it, it raises the hit-rate from rare to routine.** Widening the key invalidates every cached key at once, so it is its own unit.
6. **Does S4 wait for `TOOL-aMeteredTurnstile-5`, or ship with the 131× time-to-first-signal regression documented?** This is the one sequencing decision that is genuinely the owner's, because the complaint that started the build is about *perceived* latency and S4 makes perceived latency dramatically worse while making real span 16 % better.
7. **Does S3's boundary go after `:574` or after `:587`?** Must be measured, and both timings recorded including the rejected one. `:574` keeps the un-restored `main`/origin state entirely inside shard one, which is the safer property; `:587` is the more balanced candidate. The measurement decides, but the owner should know the safety argument favours `:574`.
8. **A stray fact worth one minute before S3's builder trusts the file:** the comment at `check-unattended.test.sh:167-169` claims `reset_tree`'s `git clean -qfd` removes the copied kit, so the arm re-copies it. The kit was copied at `:24` and committed at `:88`, so it is **tracked** and `clean` cannot touch it — the re-copy reads as a no-op and the comment as wrong. Confirm in a scratch repo before any other `reset_tree` claim in that file is trusted.

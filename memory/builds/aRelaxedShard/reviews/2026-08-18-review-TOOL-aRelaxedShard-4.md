## Verdict: BLOCKED

**Serves:** spec-audit TOOL-aRelaxedShard-4

*Review shape: raw 47, confirmed 37, refuted 10, unverified 0, precision 0.79, lenses 3/3, verify
batches 5. Round 1 of the M4 spec audit over `spec/2026-08-18-spec-TOOL-aRelaxedShard-4.md` at rev-2,
read against this worktree at HEAD `600500ac`. Every figure the spec states was re-derived from the
repo by an independent method before being accepted or rejected; the census population, the area
table and the byte arithmetic reproduce, the terminal/live split and the three sibling-family counts
do not. The 37 confirmed findings collapse to **19 distinct defects** — two blockers, nine highs,
seven mediums, one low. F1 is answered by the owner (build it) and is not re-litigated anywhere below.*

Two blockers. The first is a seam that cannot execute the thing S3 is scoped to build; the second is a
`wc -l` output presented as a row count, twice, load-bearing both times. Neither is fatal to the unit's
argument — the mint-versus-closure gap survives every re-derivation I ran, so §3's two rejections stand
— but S1's deliverable is *the measurement of record*, and four of its figures do not reproduce. A spec
whose product is a number cannot ship with four wrong ones.

---

## Blockers

### B1 — `drift_signals.py` cannot host a signal, and the file that must change is named nowhere

*Lenses: measurement, mechanism, consistency — converged 3/3.*
*§2 S3 · §4 Files touched · §10.*

S3 places the drain signal in `tools/drift-audit/drift_signals.py`. That file is the project layer and
holds declarations only. Every signal implementation lives in the shipped engine `drift_report.py`, and
the executed set is a hardcoded module-level list there:

- `drift_report.py:697` — `SIGNALS = [signal_ledger, signal_spec_status, signal_shrink_only,
  signal_handkept, signal_dangling_pointers, signal_closed_specs_untraceable,
  signal_lexicon_verbs_unused, signal_lexicon_ratified_stale]`, consumed at `:794` as
  `out = [s(ctx) for s in SIGNALS]`.
- `load_project_layer` (`:105`) imports `drift_signals` and validates exactly four attributes —
  `PRODUCT_GLOBS`, `SHRINK_ONLY`, `HANDKEPT`, `PINS`. There is no registration hook of any kind.
- `drift_signals.py`'s only executable code is one `HANDKEPT` probe, `_charter_mentions_every_leg`
  (`:104`), which reads `tools/gate-legs.json` and the charter.

A builder following §2 and §4 literally adds a function nothing calls, and the leg stays green because
no signal was added. The one genuine extension point is the wrong shape: `signal_handkept`
(`drift_report.py:392-424`) folds every probe into ONE scalar `gap = sum(max(0, actual - claims))`
scored against ONE pin, `handkept_inventories_disagreeing_with_source` (0 today) — which is exactly the
aggregation §5's observability bullet forbids ("A total lets one shard's growth hide inside another's
drain"). So the honest change is an edit to the shipped ENGINE — the surface every adopter receives —
and §4's files-touched table names only `drift_signals.py` and `selftest.py`, while §10 doubles down:
"S3 is one more signal in that file, not a new tool."

**Fold.** §2 S3, §4's files-touched table and §10 all name `tools/drift-audit/drift_report.py` as the
file that gains the signal, with `drift_signals.py` named only for the pin declaration. Delete "S3 is
one more signal in that file, not a new tool" from §10 and replace it with what is true: the signal is
a new implementation in the kit ENGINE, the pin is a project-layer declaration, and the two are
different files with different adopter consequences. Add a §5 line acknowledging that S3 changes shipped
kit code (see M4 for what that means for adopters on their first run).

### B2 — "`PLAY`, `KICK` and `DEPL` hold 9, 4 and 11 rows" is `wc -l` mislabelled as a row count

*Lenses: measurement, mechanism, consistency — converged 3/3.*
*§3 Non-goals (last bullet) · §8 F3.*

Measured rows are **6, 1 and 6**. `wc -l memory/backlog/{PLAY,KICK,DEPL}.md` prints exactly 9, 4, 11 —
the 3-line header, plus DEPL.md's two blank lines, counted as rows:

```
grep -cE '^- PLAY-' → 6      wc -l PLAY.md → 9   (3 header + 6)
grep -cE '^- KICK-' → 1      wc -l KICK.md → 4   (3 header + 1)
grep -cE '^- DEPL-' → 6      wc -l DEPL.md → 11  (3 header + 6 + 2 blanks)
```

The figures correspond to no state this repo has ever been in. Walking every commit that touched each
shard, the maxima are PLAY 6, KICK 1, DEPL 6 — and `main` also reads 6/1/6. There are no PLAY/KICK/DEPL
archives (`memory/archive/` holds only `TOOL.*` and `DECISIONS.*`), so no rotation hides earlier rows.
No alternative reading gets there either: distinct ids per family across the whole tracked memory tree
are 16/8/16, and `DECISIONS.md` holds 1/0/0.

Load-bearing twice. §3 concludes the three families "have no growth problem", and F3 sizes "one pin per
shard, three of them generous" off nothing else — KICK is off by 4x against a shard holding one row. It
also fails the spec's own predicate: AC1 specifies a ROW count, so §4's basis and the acceptance
criterion are computed by different methods, and §3's TOOL figure of 82 IS a row count (`wc -l` on that
file is 87), so one spec counts two shards two ways. Worst, a line count on a backlog shard is the one
measure that drifts on ROTATION — TOOL.md's header has grown from 3 lines to 5 across three rotations,
so a pin seeded this way gets slacker every time a shard rotates. Row-versus-line is the exact axis
`TOOL-aRelaxedShard-1` just retired from check 6.

**Fold.** §3's last bullet and F3 both read 6, 1 and 6, measured by the same
`grep -cE '^- <FAMILY>-'` predicate AC1 names, with the command stated once in §4 (see H4). Re-derive
F3's "three of them generous" against the corrected counts, and say in §3 that the three sibling shards
are measured by rows, not lines.

---

## High

### H1 — 91 terminal / 79 live does not reproduce; the split is 89/81, and AC1 contradicts §4

*Lenses: measurement, mechanism, consistency — converged 3/3.*
*§4 measurement table · §6 AC1 · §8 F2.*

Over the stated population — `memory/backlog/TOOL.md` plus `archive/TOOL.2026-08-14.md`,
`.2026-08-17.md`, `.2026-08-17b.md` — I measure 187 rows and **170 distinct ids, which reproduces
exactly** (17 ids duplicated across the two 08-17 archives, identical statuses in every case). The
statuses over those 170: CLOSED 88, WONTDO 1, OPEN 67, INPROGRESS 7, SPECCED 6, DEFERRED 1.

`memory/HYGIENE.md:70-71` defines terminal for a backlog row — "BACKLOG rotation carries forward every
non-CLOSED/non-WONTDO row" — so terminal is **89** and live is **81**. Counting DEFERRED as terminal
gives 90/80; counting only CLOSED gives 88/82; BLOCKED has zero rows. **No reading of the seven-token
vocabulary reaches 91/79.** The derived rates move with it: closure is 9.9/day not 10.1, and net live
growth is **+9.0 rows/day, not +8.8** — the corrected rate is worse.

The spec contradicts itself on this: AC1's own oracle is
`grep -cE '^- TOOL-' memory/backlog/TOOL.md` (= 82) less its terminal rows (= 1 CLOSED) = **81**,
against §4's "still live: 79". No archived id is also live, so the two should be identical. The byte
rate and the runway survive by coincidence — 9.0 × the true 247.6 B/row = 2,228 B/day against the
stated 2,233, and 40,500 / 2,228 = 18.2 days. What does not survive is F2's pin: 141 is 79 + 7 × 8.8,
seeded from the wrong population. On the reproducible base it is 81 + 7 × 9.0 = **~144**. §7 lists
`pin-copied-from-another-corpus` as a class to watch; this is that class inside one repo.

**Fold.** §4's table: terminal 89, live 81, closure 9.9/day, net +9.0 rows/day. State the terminal set
explicitly as CLOSED or WONTDO and cite `HYGIENE.md`'s rotation rule as its owner, so the DEFERRED and
WONTDO ambiguity is closed rather than left to the reader (this is also the fix H3 needs). Re-derive
F2's pin from 81 and +9.0. Add one clause to AC1 naming the expected value at this base, so the
criterion and the table can never disagree silently again.

### H2 — S2's green arm cannot fail, and AC3 cannot tell apart the two states F4 turns on

*Lenses: mechanism, consistency — converged 2/3.*
*§2 S2 · §6 AC3 · §10.*

`corpus_ids.py:191-193` builds the corpus as every tracked path under `MEMORY_ROOT`
(`corpus = [p for p in tracked if p.startswith(m + "/")]`) with no `archive/` exclusion — the string
"archive" appears nowhere in the file. Definitions come from path-agnostic anchors, and a backlog row
`- <id> · STATUS · …` both DEFINES its id (anchor) and CITES it (id regex) on the same line. Check 14
is `set(w["cites"]) - set(w["defs"])` (`:368`). So moving a row between two tracked files under
`memory/` cannot change either set: **the orphan verdict is invariant under rotation by construction.**
`corpus_ids.py` already records this in its own fixture comment at `:566-568` — "`- <id> ·` IS an
anchor, so a backlog row DEFINES its id rather than orphaning it. The first cut of this fixture used a
backlog row, produced no orphan at all."

I confirmed it empirically on the live corpus: **83 ids are defined ONLY inside `memory/archive/`, and
zero of them are orphans.** Today's orphan count is 0.

AC3 therefore promises something observation cannot deliver — "F4 is settled by observation rather than
by reading `corpus_ids.py`" — because the observation cannot come out any other way. It pins neither
trackedness nor an external citation, and it specifies "a sibling fixture" rather than the same one, so
the red arm does not inherit the green arm's shape. That is the `fixture-passes-by-finding-nothing`
class §7 names, and naming a can-fail sibling does not cure it: a sibling proves the DETECTOR fires, not
that rotation is safe. See the dedicated section below for the reachable failing case.

**Fold.** Rewrite S2 and AC3 on the axis that actually decides the question: CORPUS MEMBERSHIP. The
green arm rotates to a TRACKED archive under `memory/` and asserts zero orphans; the red arm rotates the
SAME rows to a destination outside the corpus (an unstaged archive file, or a path outside
`MEMORY_ROOT`) over the same fixture, and asserts one orphan per moved id. Say in S2 that the reading of
`corpus_ids.py` IS decisive for the tracked case and that the fixture is a REGRESSION PIN against a
future `archive/` exclusion — not an open empirical question. Then state what `cSteadyMetronome`
actually hit, because its recorded mechanism ("`archive/` is not scanned for definitions",
`README.md:80`) is false against source and was false when written.

### H3 — §10's reuse claim is wrong in three checkable ways, and §5 claims a read that does not exist

*Lenses: measurement, mechanism, consistency — converged 3/3.*
*§10 Reuse audit · §5 perf / scale.*

`memory/TEMPLATE-SPEC.md:65` requires every claim about existing code to be verified against source at
writing time. Four are not:

1. **"the status vocabulary it counts against is `.memory-tree.conf`'s"** — the conf declares no status
   vocabulary at all. Reading it end to end: `MEMORY_ROOT`, `DISCIPLINES`, `FAMILIES`,
   `TOMBSTONE_ROOTS`, four cutoffs, `CHARTER`, the pins/ceilings/budgets, `DEAD_PATH_EXCLUDE`,
   `READ_PATH_WAIVER`, `RECALL_*`. No status tokens.
2. **"read the way `row_grammar.py` reads it"** — `row_grammar.py` contains zero status tokens and reads
   exactly three conf keys: `FAMILIES` (`:105`), `MEMORY_ROOT` (`:154`), `ROW_DUPLICATE_PIN` (`:195`).
   The read described does not exist.
3. **"`drift_signals.py` … already walks the memory tree, and already reports per-item detail under
   `--json`"** — true of `drift_report.py`, false of the named file (see B1).
4. **§5: "One pass over the backlog shards, which drift-audit already reads"** — nothing under
   `tools/drift-audit/` opens `memory/backlog/`. The kit's only memory-tree reads are
   `{memory_root}/builds/*/spec/**/*.md` (`drift_report.py:314`, `:524`) and
   `{memory_root}/project/in-flight/*.md` (`:714`); the sole "backlog" hit in the kit is a prose comment
   at `drift_signals.py:211`.

The consequence of (1) and (2) is real, not cosmetic: S3's promise that "the terminal-status set is not
spelled a second time" is unachievable as described. The only authoritative statement of the rule for a
backlog row is `HYGIENE.md` prose. The machine spellings that exist disagree with each other —
`check-memory-hygiene.sh:531-532` is a 7-token alternation with no terminal split;
`drift_report.py:305` is `NON_TERMINAL = frozenset({"OPEN","SPECCED","BLOCKED","INPROGRESS"})`
(DEFERRED absent, so DEFERRED reads as terminal); `drift_report.py:474` is
`TERMINAL = frozenset({"CLOSED"})`
(WONTDO absent); `gen_build_index.py:90` is `TERMINAL = ("CLOSED","WONTDO")`. Adopting
`NON_TERMINAL` silently moves the tooling live count by one row — there is exactly one DEFERRED row
today — a design decision the spec never makes. And reaching into `row_grammar.py` is ruled out in
writing by `drift_report.load_conf`'s own docstring: importing across kit directories "would make
drift-audit un-adoptable without codebase-map".

**Fold.** Rewrite §10's second sentence: the terminal set for a backlog row is owned by
`HYGIENE.md`'s rotation rule, S3 spells it once in `drift_report.py` as CLOSED-or-WONTDO, and it
deliberately does NOT reuse the engine's existing `NON_TERMINAL`, which classifies DEFERRED as terminal
— state that as a choice with the one-row consequence named. Correct §5's perf bullet to say drift-audit
gains a read it does not have today (four small file reads, still seconds). Attribute the `--json`
detail and the memory-tree walk to `drift_report.py`.

### H4 — S1 has no criterion, no carrier and no committed derivation, and is demonstrably not
discharged

*Lenses: measurement, mechanism, consistency — converged 3/3.*
*§2 S1 · §4 · §6.*

AC1 grades S3, AC2 grades S4, AC3 grades S2, AC4 grades S5, AC5 grades the bar plus F4's resolution.
**Nothing grades S1.** §4's files-touched table's `forced by` column reads S3, S4, S2, S5, S2 — S1
appears nowhere. `TEMPLATE-SPEC.md:108` requires "Every item is verifiable at DoD."

S1's own promise is the unverifiable half: "committed so a later session can re-run the derivation
instead of re-inventing it." What is committed is figures in prose — no command, no script, no
definition of "terminal", no rule for what counts as an active day, no statement of how the census was
taken. The demonstration is this audit: working from §4 alone I reproduced 170 distinct ids and every
area-table cell exactly, and could not reproduce 91/79, 9/4/11, 253.7 or "three of the 170". Three
independent re-derivations in this review produced **three different daily series** because the
day-boundary rule is unstated. And the rate S1 exists to stabilise has now been published at four
values in this tree: 8.1 (`.memory-tree.conf:101`), 6.7 and 8.8 (§4), 9.0 (re-derived here).

There is also a window mismatch. §4 says "the nine active days the corpus covers", but
`git log --follow -- memory/backlog/TOOL.md` reaches back through `memory/tooling/BACKLOG.md` to
2026-07-12 across **13** commit-active days, and at the last commit of 08-08 the shard already held 17
rows (all terminal, live 0). Dividing an all-time 170-id census by 9 days counts pre-window minting as
in-window. Applying the census method over the shard's own 13 active days gives 13.1 minted, 6.8 closed,
net **+6.2/day** and a ~26-day runway — approximately the ~24 days rev-2 said it was replacing. The NET
survives independent check (the live-row series supports +9.0), but the two COMPONENT rates do not, and
the spec commits nothing that lets a later session tell which window it meant.

**Fold.** Add AC0 (or extend AC1) witnessing S1: one committed command block in §4 that reproduces the
census — the four-file population, the row predicate, the terminal set, and the window with its
endpoints named as dates — plus a files-touched row for whatever carries it. State plainly that the
census window is 2026-08-08 through 2026-08-17 and that it is NOT the shard's whole history, and give
the 13-active-day figure as the third method with its +6.2, since it is the one a later session's
`git log --follow` will produce first.

### H5 — the area table measures whether an author spelled a directory name, not whether rows
cluster

*Lens: measurement.*
*§4 "Why sharding below FAMILY is rejected".*

The table reproduces byte-exactly — unattended 9, memory-tree 4, drift-audit 4, run-gates 3, playbook 3,
memory-recall 3, lexicon 2, hooks 2, govkit 2, codebase-map 1, 53 matching none — which confirms the
method is faithfully reported, and confirms what it is: a substring grep for ten kit DIRECTORY names. It
misses every row that names a file, a check or an engine instead. Printing all 53 unmatched rows settles
it. Adding tracked basenames from `git ls-files` mechanically drops the catch-all from 53 to the low
40s; attributing by how the rows actually talk moves it much further:

- hygiene `check 10`/`check 21`, `corpus_ids.py`, `check-arms.py`, `gen_build_index.py`,
  `READ_PATH_CEILING` → memory-tree. The seven `aTetheredRecord` rows are check-21 work; so are
  `cTracedPromise-4/-6`, `cSettledDocket-9/-10/-11`, `aBoundedVerdict-9`, `aRelaxedShard-2/-3`.
- `--plan`, `--preflight`, `park()`, `RUN.md`, the DoD items, `DIRECTIVES_EXTRA_TABLE`, "leg check
  17/18" → unattended. That is ~10 `cBriefedPilot` rows plus `aStandingWrit-7/-9`,
  `aBranchedMandate-3`, `cSettledDocket-8/-14`.
- `closed_specs_with_no_product_commit`, `TRACE_CUTOFF`, `DEAD PROBE` → drift-audit; `agent-cap` →
  hooks.

Under that attribution the catch-all falls to roughly one row in eight and the largest cluster rises
past 30%, which inverts the stated basis. For reference the shard also partitions cleanly by build slug
(cBriefedPilot 12, cSettledDocket 10, aStandingWrit 7, aTimedTurnstile 7, aTetheredRecord 7).

The rejection of sharding still stands on its OTHER leg — closure trails minting, so a sub-shard
relocates the growth — and that leg is untouched by every correction in this review. What does not stand
is §4's closing sentence: "The measurement lives in this spec so the option cannot be re-proposed
without new data." As measured, the data would support re-proposing it.

**Fold.** Keep the rejection; move its weight onto the closure-trails-minting leg, which is the one that
holds. Say what the grep measures (a kit directory name spelled in the row text) and that a topic-aware
attribution collapses the catch-all substantially, so the 65% figure is a floor on clusterability, not a
measure of it. Delete or soften "cannot be re-proposed without new data" — as written it forecloses a
re-proposal the spec's own method cannot support. A non-goal declared "measurement-rejected, not
deferred" on a grep artifact is a worse record than no measurement.

### H6 — the runway is a point estimate over a series that is not a slope, and the window's edges
are not the main risk

*Lens: measurement (window half converged with mechanism).*
*§4 measurement table (runway) · §8 F1.*

Live non-terminal rows at each day's last commit, measured over the shard's history:

```
07-12   0    08-08   0    08-11  33    08-14  52    08-16  62
07-15   1    08-09   1    08-13  34    08-15  44    08-17  81
07-16   2    08-10  20
```

Daily net inside the census window runs **+1, +19, +13, +1, +18, −8, +18, +19** around a mean of +9.0
— values differing by a factor of two either side, and one negative. The byte series is worse than the
row series because rotation subtracts: TOOL.md's day-close bytes run 3,336 → 9,271 → 17,477 → 20,434 →
**12,817** (rotation) → 14,836 → 17,910 → 20,940, with single-day steps up to +8,206 B, which is 20% of
today's remaining 40,500 B of headroom. Growth arrives in merge STEPS, not as a slope: minting is pooled
across four nodes, and other nodes' rows enter THIS tree at a merge while carrying back-dated author
dates, so a mean over author-dated days smooths away the arrival pattern that actually breaches the cap.
Pooling is correct — all four nodes write the same shard — so this is a stationarity problem, not a
double count.

§4 hedges the wrong thing. It says "the window is approximate at its edges"; the edges are worth about
two days (dropping 08-08, the day the shard was created with 17 already-terminal rows and 0 live, moves
the rate to ~10 and the runway to ~16). The variance is worth considerably more, and F1's whole case for
waiting is "18 days is still real". That figure needs a range and a statement that the breach lands on a
merge day.

**Fold.** §4's runway row becomes a range with its method named — the mean, the observed daily spread,
and the fact that the byte series steps at merges rather than sloping. One clause in F1 saying the
breach arrives on a merge day, so "18 days" is not 18 days of warning.

### H7 — F2's pin becomes a merge-blocking refusal in about a week on an unguarded leg, and §5's
mandatory movement rule is in no scope item

*Lens: mechanism.*
*§8 F2 · §5 risks · §3.*

Today's live TOOL count is 81, so F2's 141 is 60 rows of headroom — **6.8 days** at the spec's own
+8.8/day, 6.7 at the corrected +9.0. The leg is unguarded: `tools/gate-legs.json`'s
`{"name": "drift-audit records", "argv": ["python","tools/drift-audit/drift_report.py","--check"]}`
carries no `guard` key (`kit.toml` says `guard = []`), and `run-gates.sh` skips only legs WITH a guard.
`drift_report.py:502-503` states the consequence in its own words: the records leg "carries an empty
guard, so it runs on every branch-scoped bar." So about a week after landing, every merge and every push
on every node reds until someone raises the pin or closes 60 rows — which is §4's own rejected
alternative, "a hard cap on live rows that REFUSES a new row", delayed by seven days.

§5 declares the remedy mandatory — "The pin needs headroom and a stated movement rule, or S3 becomes the
refusal §4's alternatives already rejected" — and no S-item, AC or fork delivers the movement-rule half.
S1-S5 and AC1-AC5 cover the signal, its arms, the rotation fixture, the HYGIENE paragraph and the bar;
F2 answers only location and value. The spec names the failure and builds half the mitigation.

**Fold.** Either add the movement rule to S3's scope as a deliverable (what justifies a raise, where the
`<old> -> <new>` marker goes, who may write it) with an AC witnessing it, or resolve F2 toward the
non-gateable shape in H8 so the schedule question does not arise. Note in §5 that
`drift-audit records` is UNGUARDED, so a red pin blocks diff-scoped runs too, not just the push
boundary.

### H8 — a forecast pin inverts the convention the PINS block declares, and the in-file idiom for a
legitimately-growing population is never considered

*Lenses: mechanism, consistency — converged 2/3.*
*§4 "What the lever is" · §8 F2 · §8 F3 · §5 observability.*

`drift_signals.py:147-149`: "PINS — seeded at MEASURED values, never guessed. Lower each as its
population drains; raising one needs the same justification any other ratchet raise does." Every live
pin's comment records what was measured and the residual it tolerates (2, 0, 1, 3, 0). F2's 141 is not a
measured population value — it is today's count plus a one-week forecast — over a quantity §4 itself
proves grows monotonically. That is a ratchet whose only reachable move is the weakening one, which is
what the convention forbids without justification.

The engine already has the right idiom and the spec does not consider it: `signal_shrink_only` is
`"gateable": False` with the comment "Report, never gate: a list can legitimately sit still for a week"
(`drift_report.py:373-384`). Non-gateable also escapes the DEAD-gateable red at `:838`. That is the
choice which reconciles §4's monotonic-growth finding with §5's freeze risk and H7's schedule.

On F3's shape: a per-shard pin IS buildable, but not inside `PINS`. `PINS` is `dict[str, int]` keyed by
SIGNAL name and `drift_report.py:796` resolves exactly one pin per signal
(`s["pin"] = ctx.pins.get(s["signal"], s["tolerance"])`). A separate per-shard dict works and is
ratchetable — I ran `_scalar_at` against a `{"TOOL": 141, "PLAY": 12}` literal and it returned
`(141, 1)` and `(12, 2)`, because the guard matches a dict ENTRY by its own key — but that requires one
explicit `RATCHETS` row per shard, and §4's files-touched table prices none of it. Separately, §5 and F3
both cite `ARMS_FLOORS` as the precedent for per-shard splitting, and the `RATCHETS` header excludes
exactly that shape by name: "SCALARS ONLY… The compound floors — `ARMS_FLOORS` and `CORE_FLOOR`, both
`<name>` plus two numbers — are NOT covered here." The precedent cited is the shape the guard refuses.

**Fold.** Add a third option to F2: ship the signal `gateable: False` (report, never gate) until the
measurement has produced a quarter of data, with the shrink-only pin arriving in a later unit. Recommend
between it and a headroom pin on stated grounds. If F3 keeps a per-shard pin, name the declaration it
lives in (not `PINS`), add its per-shard `RATCHETS` rows to §4's files-touched table, and replace the
`ARMS_FLOORS` citation with an accurate one — `ARMS_FLOORS` is the compound shape the ratchet guard
explicitly does not cover.

### H9 — two live carriers still state the rate and runway this unit supersedes, and one is the
ratified fork's own justification

*Lenses: measurement, consistency — converged 2/3.*
*§3 Non-goals (`ROW_DOC_CAP_BYTES`) · §4 · §5 user docs.*

`.memory-tree.conf:100-102` states, in the present tense, directly above `ROW_DOC_CAP_BYTES="61440"`:
"Runway at the measured net growth of 8.1 live rows/day (~2,057 B): about 21 days" and "no byte cap
compatible with a readable file buys a quarter at 17.3 ids a day." §4 attributes "17.3 and 10.6 for a
net of +6.7" to that same diff scan — and 17.3 − 10.6 = 6.7 while 17.3 − 8.1 = 9.2, so the conf's net
and the spec's net cannot both be that method's output. Unit 1's §8 prices its three candidates "at
2,057 bytes per day", so 8.1 is the rate the ratified fork rests on.

That comment is the declaration's own rationale, and the conf is listed in `RECALL_EXTRA_SOURCES`
(`:144`) with each key chunked together with the comment block above it — so it is an INDEXED answer
surface for exactly the question S1 makes this unit's deliverable, and a later recall query for the
backlog growth rate returns the superseded figure. §3 makes re-opening the KEY a non-goal, which is
correct and is not what this asks; §5 limits user docs to S5. So the conf keeps saying 8.1 and 21 days
permanently. §4's own stated principle is that the weaker method is "named rather than dropped" — here
it is left un-named in the one carrier a later session reads first.

The build README has the same defect in one file: `README.md:88` reads "about 18 days at the census
rate" while `:109` still reads "About 21 days of runway". The immediately preceding commit (`600500a`,
"two stale runway figures the rev-2 fold missed") was fixing this class and missed this pair.

**Fold.** Add a files-touched row and one clause to S5 (or a sixth scope item): amend
`.memory-tree.conf`'s `ROW_DOC_CAP_BYTES` comment to name the census rate and point at this spec's §4 as
the owner, marking 8.1/2,057/21 days as superseded rather than deleting it. Fix `README.md:109` in the
same commit. §7 lists `two-answers-to-one-question` for these paths.

---

## Medium

### M1 — the area table sums to 86 over the 82 rows it says it measures

*Lenses: measurement, mechanism, consistency — converged 3/3. §4.*

9+4+4+3+3+3+2+2+2+1 = 33 kit hits, +53 no-kit = 86. Measured: 29 rows match at least one name and 4 of
those match more than one, which is exactly the 33 − 29 = 4 excess. §4 introduces the table as "Measured
over all 82 rows, by which kit or area each row names" with a `rows` column, which reads as a partition,
and the sharding argument presupposes each row lands in one shard. The derived percentages are computed
off the right denominator (53/82 = 64.6% → "65%", 9/82 = 11.0% → "11%"), so nothing downstream is
arithmetically wrong — but a re-deriving session hits an 86-vs-82 mismatch with nothing explaining it,
in the one section written so the option "cannot be re-proposed without new data".

**Fold.** One clause under the table: it is a per-area tally, not a partition; 4 rows name two areas, so
29 of 82 rows name any, and the column sums to 86.

### M2 — 253.7 B/row is unit 1's figure over a different population, presented as this census's own

*Lenses: measurement, mechanism, consistency — converged 3/3. §4 measurement table.*

253.7 is verbatim `.memory-tree.conf`'s `ROW_DOC_CAP_BYTES` comment — "the tooling backlog shard's live
rows are 18,519 B over 73 rows = 253.7 B/row by `wc -c`" — a 73-row population measured for
`TOOL-aRelaxedShard-1`. Today: `grep -E '^- TOOL-' memory/backlog/TOOL.md | wc -c` = 20,307 over 82 rows
= **247.6 B/row** (whole-file-over-rows is 20,940/82 = 255.4). Under neither method is it 253.7, yet it
sits under a column headed "measured (census)". It is load-bearing: 8.8 × 253.7 = 2,233 reproduces the
spec's B/day exactly, and 40,500 / 2,233 = 18.1 reproduces the runway. rev-2's stated purpose was
re-deriving the load-bearing figures by a second method, and this one — which converts the row rate into
the byte rate and hence the runway — was not re-derived. The error nearly cancels against the +8.8 →
+9.0 correction (2,228 vs 2,233), which is luck, not method.

**Fold.** 247.6 B/row over the 82 live-shard rows, with the predicate named. State the whole-file
figure (255.4) separately if the runway uses it, and say which one the B/day figure multiplies.

### M3 — the declared base sha does not resolve

*Lenses: measurement, consistency — converged 2/3. Status header.*

`git rev-parse 86eefd8f` → "fatal: ambiguous argument … unknown revision or path not in the working
tree". The intended commit is `86eefd8e97cd28d703b1fc233a3c0830447485a0` ("TOOL-aRelaxedShard-1: trim
two trap bullets under check 11's 400-byte cap") — the eighth character is `e`, not `f`. The object
database is shared across worktrees, so no other checkout resolves it either. Check 12's header grammar
(`check-memory-hygiene.sh:699`) validates only eight hex characters of SHAPE, and `TEMPLATE-SPEC.md:46`
asks only for "8+ hex chars", so nothing on the bar catches it. It matters more than usual because S1
commits the measurement "so a later session can re-run the derivation" and every §4 figure is stated as
of that base: the ground cannot be checked out. rev-1's log already documents WHY a branch tip is used
rather than a default-branch sha, so only the value is wrong.

**Fold.** `base 86eefd8e` in the status header. Nothing else changes.

### M4 — "migration / rollback: None" is wrong for the population the kit ships to

*Lens: measurement. §5 migration / rollback.*

`drift_report.py:796` is `s["pin"] = ctx.pins.get(s["signal"], s["tolerance"])`, every signal's
tolerance is 0, and `--check` reds on `value > pin` (`:837`). `drift_signals.template.py:106-110` ships
`PINS` with all three example entries commented out, so a template-derived adopter has an empty dict and
inherits pin 0 for any signal they have not seeded. Since the signal must live in the shipped engine
(B1), an adopter with one open backlog row reds on their first `--check`; with no backlog shard at all
they red the other way, as DEAD (`:845`). The kit already solved the analogous problem and says so in
writing — `DECLARED_EMPTY`'s comment: "without it a fresh adopter reds on their first run for doing
exactly what the template told them to." §5 currently asserts there is nothing to migrate. F2 does not
cover this: it reasons that a gov-local pin is fine because "this is a drift REPORT about gov's own
records", which is the choice that PRODUCES the adopter red rather than a resolution of it.

**Fold.** §5's migration bullet states the adopter consequence and its remedy — a template default, an
entry in the shipped `PINS` block, or shipping the signal non-gateable until seeded (which H8 also
argues for). Add the chosen remedy to S3's scope.

### M5 — S4's "both arms" understates the work: the shared base fixture has no backlog shard

*Lens: consistency. §2 S4 · §4 Files touched · §6 AC2.*

`selftest.py`'s `make_repo` creates the spec dir, `memory/project/in-flight`, `src`, `conf` and
`drift-audit` — **no `memory/backlog/` anywhere** — and writes `.memory-tree.conf` as exactly
`MEMORY_ROOT=memory\n` with no `FAMILIES`. Its fixture project layer writes `PINS = {}`, spelled that
way on purpose because the pin-semantics arm rewrites the literal (`:242-244`, rewritten at `:521`), and
`DECLARED_EMPTY = {'handkept_inventories_disagreeing_with_source'}` only. A gateable per-shard signal in
that tree finds no shards, so `live` is False, so `--check` reds it as DEAD unless it is added to
`DECLARED_EMPTY` — which §7's own `vacuous-selector-empty-population` class says is not the honest
escape. The base fixture's comment states the constraint directly (`:202-204`): "The base fixture must be
CLEAN for every signal, or the `--check` pin-semantics arms below inherit a second over-pin signal and
stop asserting what their names say." The concrete casualty is the arm at `:522-525`, which asserts
`rc == 0` for "`--check` greens once the pin is seeded at the measured value". So this is fixture surgery
on a shared base that every other signal's arms run through, and AC2 is graded through it.

**Fold.** S4 says the shared `make_repo` fixture gains a backlog shard (and whatever declaration the
signal's selector needs), and §4's files-touched row for `selftest.py` prices that rather than "both
arms". One clause in AC2 noting the existing `--check` arms must stay green through the change.

### M6 — S5 restates a sentence already in the carrier it edits, and adds a second definition of
the terminal set

*Lens: mechanism. §2 S5.*

`memory/HYGIENE.md:69-72` and `tools/memory-tree/HYGIENE.template.md:71`, both inside "Index budgets,
caps, rotation", already read: "BACKLOG rotation carries forward every non-CLOSED/non-WONTDO row.
Rotated archives stay inside `memory/` so the all-time id collision grep still covers them." That is
S5's first clause in substance plus the fact S2 exists to confirm. Only the floor framing — "a shard's
floor is its live set, so the bound that matters is the live-row count" — is new. The second-definition
half is the material one: HYGIENE.md's own status vocabulary holds seven tokens including DEFERRED, so
"non-terminal" and "non-CLOSED/non-WONTDO" select different sets, and that difference is exactly the row
by which my census differs from a DEFERRED-counting one. S3 counts "live non-terminal rows" and AC1 says
"less its terminal rows" without naming the set, so the ambiguity is load-bearing for the signal, not
just the prose. §7 lists `two-answers-to-one-question` as a class this unit must avoid.

**Fold.** S5 is scoped to the floor framing ONLY, appended to the existing rotation bullet rather than
written beside it, and it uses that bullet's own wording (CLOSED or WONTDO) rather than a second phrase.
Nothing in S5 re-defines the terminal set.

### M7 — two gated carriers of the signal set are unnamed, and one of them is already stale

*Lens: consistency. §4 Files touched · §7 Gates.*

`tools/drift-audit/SKILL.template.md:29` carries a hand-kept `| Signal | Asks |` table, mirrored into
`.claude/skills/drift-audit/SKILL.md:29`, and the UNGUARDED leg `drift-audit wiring`
(`bash tools/drift-audit/adopt-drift-audit.sh --check`) renders to a temp file and diffs, so — in the
adopter script's own words — "a hand-edited Skill reds instead of silently outliving the kit it came
from." §7's gate list does not include that leg, and §4's files-touched table names neither carrier. The
table is already stale in the same way: `SIGNALS` holds eight signals, the table lists six (both lexicon
signals missing), and the surrounding prose still says "the five implementations are the kit's". So the
only human-readable enumeration of drift-audit's signals is a gated carrier whose truth S3 changes,
named in neither §4 nor §7.

**Fold.** Add `tools/drift-audit/SKILL.template.md` and the rendered `.claude/skills/drift-audit/SKILL.md`
to §4's files-touched table, and `drift-audit wiring` to §7. Fixing the two missing lexicon rows while
there is a one-line courtesy, not a scope expansion.

---

## Low

### L1 — "Three of the 170 are this build's own rows" — there are two

*Lenses: measurement, consistency — converged 2/3. §4 measurement table (footnote).*

`grep -nE '^- TOOL-aRelaxedShard' memory/backlog/TOOL.md` returns exactly two rows, `-2` and `-3`, and
no `aRelaxedShard` row exists in any of the three archives. Unit 1 filed no row of its own — the build
README records that it closes `TOOL-cSettledDocket-16` "rather than landing a duplicate beside it" — and
`-4` has none either; the README's generated region says so ("Ids no record names:
TOOL-aRelaxedShard-4"). The generous reading fails too: this build's commits add three row lines
relative to the merge-base, but the third is `TOOL-cSettledDocket-16`, which existed as OPEN at
merge-base and was minted by another build. Immaterial to the rate, and it is the fourth §4 figure that
does not reproduce, which is itself the signal about how the section was measured.

**Fold.** "Two of the 170 are this build's own rows."

---

## Refuted

Ten of the 47 raw findings did not survive verification and are recorded here so the fold does not
chase them. Three claimed the two §5 production-readiness bullets are jointly unsatisfiable, that a
per-shard pin is not expressible as one signal, and that a drained shard would red the bar as DEAD —
all three misread `live` as a row count. `live` is a field the signal computes for itself, and the
closest precedent keys it on structure rather than contents: `signal_shrink_only`'s
`live = any(r["seed"] is not None for r in rows)`. A `live` keyed on shard-file PRESENCE satisfies §5's
two clauses exactly as written, with per-shard values in `detail`.

The most instructive refutation is the claim that the ratchet guard cannot read a per-shard pin, so a
"shrink-only pin" would be shrink-only in name only. I tested it: `_scalar_at` against a
`{"TOOL": 141, "PLAY": 12}` literal returns `(141, 1)` and `(12, 2)`, because its second pattern matches
a quoted dict KEY. The `RATCHETS` header's "SCALARS ONLY" excludes the compound `<name>`-plus-two-numbers
STRING floors of the `ARMS_FLOORS` kind, not a dict of scalar lines. What survives from that cluster is
narrower and sits in H8: the pin cannot live in `PINS` (one scalar per signal name), each shard needs its
own `RATCHETS` row, and the `ARMS_FLOORS` citation is the wrong precedent.

Also refuted: that the kickoff-manifest ratchet is listed on a speculation no scope item acts on (§7's
clause is explicitly conditional — "a file that MAY join its `watch:` list" — and the leg runs whatever
§7 says); that S2's fixture is redundant because the answer is already established (arguing that is
arguing S2 should not be built, which F1 settled, and the reading-versus-fixture point is already stated
in S2 and §10); that the spec settles the wrong question by framing F4 as archive-exclusion
(`cSteadyMetronome`'s recorded wording IS mechanism-specific, so answering it as recorded answers what
was asked — the surviving half of that objection is H2's discriminating axis); that the 18-day runway is
a floor figure passed off as time-to-red (terminal rows accumulate at ~10/day, so the rotation triggered
at a gross-rate breach reclaims ~21 KB, not one row — 18 days correctly dates when rotation stops being
able to pay, which is the quantity the decision turns on); that S2's stated rationale names a purpose §3
declares out of scope (§3's bullet already states the same coupling from the other side); and that the
figures are branch-local while `main`'s shard is red — `main:memory/backlog/TOOL.md` IS listed in
`main:memory/project/curation-debt.txt`, and check 6 does `in_debt "$f" && continue`, so it is waived,
not red.

## Unverified

None. Every raw finding reached a verdict.

---

## Does S2 have a failing case?

**As scoped in S2 and AC3, no — the green arm cannot fail. As re-scoped along the axis the source
actually turns on, yes, and the failing case is reachable and worth pinning.**

The green arm is green by construction, not by observation. `corpus_ids.py` builds its corpus as every
tracked path under `MEMORY_ROOT` with no `archive/` exclusion, definitions come from path-agnostic
anchors, and a backlog row both defines and cites its own id on the same line. Check 14 is
`cites − defs`. Moving that line between two tracked files under `memory/` changes neither set. I
verified this on the live corpus rather than by reading: **83 ids are defined only inside
`memory/archive/`, and not one of them is an orphan; today's orphan count is 0.** The file's own fixture
comment records the same thing from the other direction — the first cut of the check-14 fixture used a
backlog row and "produced no orphan at all". So a fixture that rotates rows to a tracked archive and
asserts zero orphans reports 0 by arithmetic, whatever the walk does, and would stay green if someone
later added an `archive/` exclusion in a way that only bit untracked destinations. That is the
`fixture-passes-by-finding-nothing` class §7 names, and AC3's specified "sibling fixture" — a separate
fixture, so not the same rows — proves the DETECTOR fires, not that rotation is safe.

The reachable failing case is CORPUS MEMBERSHIP, and it is the one reading under which
`cSteadyMetronome`'s report is reproducible. `corpus_ids.py` enumerates `git ls-files`, so an archive
file that exists but is not staged contributes no definitions while the live shard's copy is already
gone — and the citations survive, because the moved ids are cited from outside the archive. I measured
that too: of the 23 rows in `TOOL.2026-08-17b.md`, **all 23 are cited from at least one non-archive
file**, so every one of them would become an orphan in that state. That is exactly "moving 34 terminal
rows orphaned every id they defined."

So the fixture is worth building, but not as scoped. Both arms must run over the SAME rows and vary only
the destination's corpus membership: tracked archive under `memory/` → zero orphans; unstaged archive (or
a destination outside `MEMORY_ROOT`) → one orphan per moved id. That pair discriminates, it settles what
`cSteadyMetronome` actually hit, and it pins the real footgun — which is a mid-rotation session, not a
rotation. As written, AC3 ships a permanently-green arm certifying rotation while testing nothing about
it, and records F4 as "settled by observation" on an observation that could not have come out otherwise.

## Is the design clean enough to build?

No — one more round is warranted, and it is a short one. The unit's central argument survived every
re-derivation I ran: closure trails minting, the live set grows monotonically, and neither a sub-shard
nor a spill tier changes that. Both §3 rejections stand. But S1's deliverable IS the measurement, and
four of its figures do not reproduce (91/79, 9/4/11, 253.7, "three of the 170"), while the seam S3 names
cannot execute a signal and the fixture S2 specifies cannot fail. Those are not things building tests —
B1 sends a builder to edit the wrong file, B2 seeds three pins off numbers the repo has never held, and
H2 ships a vacuous arm that looks like evidence. The fold is mostly arithmetic and three re-pointed
sentences; once §4's figures reproduce, §2 and §4 name `drift_report.py`, AC3 varies corpus membership,
and F2 answers the gateable question, building becomes the stricter test and round 3 should not be
needed.

## What the fold must not do

- **Do not re-open F1.** The owner answered: build it. Nothing above argues the unit should not exist,
  and the fold must not turn H6's variance point or H7's schedule point into a case for deferring.
- **Do not weaken §3's two rejections.** The closure-trails-minting leg survives every correction here,
  including the corrected +9.0 rate, which makes the case stronger rather than weaker. H5 asks for the
  area table's method to be stated honestly and for one over-reaching sentence to go — not for sharding
  to be reconsidered.
- **Do not fix the numbers by re-measuring a third way and quoting the new figures in prose.** That is
  how the rate reached four published values. H4's fold is a committed command with its population,
  predicate, terminal set and window endpoints named, so the next session re-runs it instead of
  re-inventing it.
- **Do not resolve B1 by using the `HANDKEPT` probe hook.** It folds every probe into one scalar against
  one shared pin, which is the aggregation §5 forbids and would file backlog growth under "an inventory
  disagreeing with its source".
- **Do not add `DECLARED_EMPTY` to make M5's fixture problem go away.** §7's own
  `vacuous-selector-empty-population` class says a shard glob matching nothing must report, not pass.
  The fixture gains a backlog shard.
- **Do not fold the spill tier back in.** It is a §3 non-goal and H2's re-scoped S2 does not unblock it;
  it stays a later unit with its own spec.
- **Do not delete the diff-scan method from §4.** Naming the method to distrust is right and §4 says why.
  H4 asks for the 13-active-day third method to join it, not for either to be dropped.

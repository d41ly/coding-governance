# Wave-2 drift audit — records vs state

**Serves:** research TOOL-aScouredKit-1

## Verdict: CLEAN WITH FIXES

**Build:** aScouredKit · **Date:** 2026-08-30 · **Node:** a · **Tree:** `.claude/worktrees/kit-adversarial-review-15ed31`, ships at HEAD
**Shape:** 5 finder lenses → 5 skeptic batches → this synthesis
**Commissioning question:** are the records stale, and why does the project's state feel uncertain?

---

## 1. Verdict

**The generated half of the records is trustworthy. The authored half is not.**

Everything a program renders re-derives correctly: 447 generated artifacts re-render
byte-identically, all 24 `LANDED` witnesses are ancestors of `main`, `adopt-playbook --check` is
green over the rendered charter region, all 20 load-bearing charter paths resolve, and the map's
`baseline.toml` is genuinely shrinking (68 → 43 unclaimed keys). Nothing a machine writes here is
lying to you.

Everything a human typed is a coin flip. Forty-four of forty-seven raw findings survived skeptical
verification, and the overwhelming majority are sentences somebody wrote beside a source that then
moved.

**The single worst instance is finding 15:** fourteen of the eighteen non-terminal spec headers in
the tree say `SPECCED` about work that is already merged into HEAD. Because `memory/LIVE.md` is
rendered from those headers, six of its sixteen rows name builds that are finished. That file is the
tree's only *derived* answer to "what is in flight", the Definition of Ready sends every session to
it, and it is wrong about 38% of its rows. Anchor: all eight aMendedLedger unit headers still read
`SPECCED`
(`memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-2-u1-journal-relocation.md:3`)
while `dc5ae995`, `f3c48dee`, `3e25a56f`, `a08c2f3d`, `9369123e`, `bde0de8c`, `390a87e7`, `e6fb7047`
and merge `289daf72` are all ancestors of HEAD.

Runner-up, and the more damning one for the *mechanism*: `memory/builds/aScouredKit/README.md:51`
asserts that ids -30, -31 and -32 "are NOT units and carry no spec". All three have tracked CLOSED
specs, none has the backlog row the sentence promises, the generated region thirty lines below the
claim lists all three, and `git log -L51,55` shows the sentence was added by `bfa90c33` — the *last*
records commit of the run, *after* `86148e20` promoted those three ids to units. It was false the
moment it was typed. The full bar was green over it.

---

## 2. THE STATE ANSWER

Plainly: **the work is further along than the records say, and roughly a fifth of the finished work
is not visible from anywhere but one disk.**

### How many build records contradict git

**Eight builds carry at least one record that contradicts git at HEAD.**

| Build | The contradiction | Finding |
|---|---|---|
| aBatchedLintel | spec headers `SPECCED`, work merged | 15 |
| aMendedLedger | 8 unit headers `SPECCED`, 9 shas ancestors of HEAD | 15 |
| aPacedTurnstile | spec `SPECCED` while `memory/backlog/TOOL.md:171` says CLOSED | 15 |
| aTetheredScratch | spec headers `SPECCED`, work merged | 15 |
| bConvergentLodestar | spec headers `SPECCED`, work merged | 15 |
| dNarrowedAnchor | spec headers `SPECCED`, work merged | 15 |
| aThawedCorpus | `RUN.md:15` phase `LANDING`; witness `2416de50` landed 2026-08-27, ledger says CLOSED | 38 |
| aScouredKit | `README.md:51` denies three of its own CLOSED units; `RUN.md:14` witness `3eaf38d0` predates three of its unit specs | 20/34/40, 39 |

That is 14 individual spec files plus 2 RUN.md records plus 1 build README. Downstream: 6 of 16 rows
in `memory/LIVE.md` name finished builds.

### What is built but unlanded

**21 commits of finished or in-flight work sit on two branches that exist on node a's disk and
nowhere else.** Neither is on `origin`.

- `branch/paired-lexer-followup-9c31a2` — 6 commits ahead of `main`, 0 behind. The aPairedLexer
  build: 5 ids, 4 specs, 2 reviews, and a 148-insertion / 75-deletion change to
  `tools/hooks/agent-cap.js` fixing a reproduced fail-open in the only mechanical control against an
  unbounded agent burst. `grep -rl aPairedLexer memory/` at HEAD returns nothing but this audit's own
  scratch file. **Correction to the raw finding:** all four specs read `SPECCED` and there is no
  `RUN.md`, so this is an in-flight build on its own feature branch, which is the *designed* state
  under §3 — not a stranded finished one. The exposure is single-copy storage, not lost records.
- `branch/acollapsedscan-followups` — 15 commits of closed aCollapsedScan work, including the leg
  that halved the bar from 3162 s to 1605 s. `memory/builds/aCollapsedScan/README.md:66` reads
  `CLOSED · 1 unit(s)` at HEAD and `CLOSED · 5 unit(s)` on the branch. Both say CLOSED.
- Its worktree, `unattended-check-plan-27c557`, **has been frozen mid-merge since 2026-08-27
  04:53**: `MERGE_HEAD` = `f5dff6ae`, 71 paths staged, zero unmerged, never committed. That base is
  now 163 commits behind `main` (**not** the 204 the raw finding claimed), so the resolution is
  against the wrong tree and will have to be redone.

### What is structurally UNKNOWABLE from this clone

This is the honest reason the state feels uncertain, and no amount of record-fixing removes it.

1. **Nodes b, c and d are invisible.** The registry declares a four-node fleet. This clone sees
   `origin` plus node a's local refs. Unpushed branches, dirty worktrees and frozen merges on the
   other three machines are not observable from here at all — and node a alone turned out to be
   hiding 21 commits and an abandoned merge.
2. **`memory/LIVE.md` cannot answer the question it is asked.** It is generated per-tree from merged
   build front matter, so by construction it can never list an unmerged build. A session that asks
   the derived index "what is in flight" gets "what is in flight *and already merged*", which is a
   different question with the same wording.
3. **The two Tier-0 signals that would ask exactly these questions are dark.**
   `tools/drift-audit/drift_report.py:1380` resolves `ledger_dir` to `memory/project/in-flight`, a
   directory retired with the per-node session ledger. `signal_ledger` (:377) prints `empty by
   declaration` — correctly, it is in `DECLARED_EMPTY` at `drift_signals.py:97-104` with the
   retirement reason. `signal_dangling_pointers` (:586) is **not** in that list, so it prints `DEAD
   PROBE -1` on every run, forever. Meanwhile 27 `memory/builds/*/RUN.md` records carry
   phase/witness/branch-ref and **no signal reads any of them.**
4. **The one signal that could have caught §2's headline is ~14% sensitive.** The lens reports signal
   3 scoring 2 of 18 against a re-derived 14 of 18, because its oracle requires the unit id to be
   cited by tracked *product source*; a landed build nobody greps for scores nothing. *(The 14%
   figure is the lens's characterization; the 2/18-vs-14/18 gap was re-derived by the skeptic.)*

---

## 3. Confirmed findings, severity-ordered

Fifteen findings survived verification with their claim and severity intact. Every one was
re-derived by a skeptic who ran the check independently.

| id | sev | file:line | claim |
|---|---|---|---|
| 15 | blocker | `memory/builds/aMendedLedger/spec/units/2026-08-09-spec-aMendedLedger-2-u1-journal-relocation.md:3` | 14 of 18 non-terminal spec headers say SPECCED about work merged into HEAD; 6 of 16 LIVE.md rows name finished builds |
| 27 | high | `AGENTS.md:94` | Six live bullets cite §4/§13/§17, deleted at v3.0 (:94, :99, :100, :231, :321, :390); two are in §0's TL;DR; all six also ship in `coding-governance-agents.template.md:18,23,24,161,253,328` |
| 34 | high | `memory/builds/aScouredKit/README.md:51` | "-16 through -34 are NOT units and carry no spec" is false in both directions for -30/-31/-32; added by `bfa90c33` *after* `86148e20` promoted them |
| 20 | high | `memory/builds/aScouredKit/README.md:51` | same defect, reached independently: three CLOSED specs, zero backlog rows, authored roster 14 rows vs generated 17 |
| 26 | high | `AGENTS.md:318` | §8 sends Tier-2 artifacts to `memory/reviews/`, which has never existed; `AGENTS.md:52` in the same file says the opposite; cause is `REVIEW_DIR` `class="defaulted"` at `tools/govkit/entries/playbook.kit.toml:219-221`, unanswered in `.governance/deploy.toml` |
| 18 | high | `memory/HYGIENE.md:94` | "Six plain lists in `memory/project/` — the whole of what that directory holds"; `git ls-files` returns 9, scaffolding writes 7, the consuming allowlist names 9. Repeated at :29 and :112, byte-identical in `tools/memory-tree/HYGIENE.template.md`, byte-compared green by `kit-dogfood-parity.test.sh:53` — a shared falsehood shipped to every adopter |
| 1 | high | `AGENTS.md:9` | The charter's only named route to the dossier/unclaimed-key pair exits 2 as spelled (`reuse_lookup.py:394`); given a query it prints `177 inventory keys` where a reader expects the 43 unclaimed, against a true total of 181. Repeated at `memory/map/features/codebase-map.md:63` |
| 45 | medium | `tools/memory-tree/check-memory-hygiene.sh:674` | Under `--staged`, checks 21 (:674), 13-16 (:1073), 17-19 (:1088) and 20 (:1098) are held silently; only check 23 (:1166) announces. A staged run prints one line and exits 0. The file's own comment at :1151 names this as the class it refuses |
| 14 | medium | `memory/map/features/govkit.md:115` | `map_diff 14e21399..HEAD` attributes 13/59 files to five dossiers; `git diff --name-only 14e21399..HEAD -- memory/map/` returns zero. §1's "dossier prose refreshed on touch" is unenforced and the run closed claiming every DoD item met |
| 11 | medium | `tools/drift-audit/drift_signals.py:78` | `SHRINK_ONLY` declares 5 files, all under `memory/project/`; at least 9 more tracked data files declare the rule in their own headers, including `tools/install-prefix-waivers.txt:2`, the only one that has demonstrably broken its promise (11→12 rows at `e08040b6`). Report prints `2 of 5` with no coverage caveat |
| 28 | medium | `AGENTS.md:208` | §5 delegates the hygiene check count to "the kit README and the gate-leg name"; `tools/gate-legs.json:984` is `{"name": "memory hygiene"}` with no count. The surviving carriers disagree: kit README says 23, `README.md:33` — the repo front door — says 21. Source settles it at 23 |
| 8 | medium | `memory/map/features/unattended.md:15` | claims `skill-engines = ["session-kickoff"]` while `session-kickoff.md:15` claims `[]`; `MAP.md:142` renders `session-kickoff \| unattended`, so the dossier named for the kickoff engine owns none of its keys, with no prose anywhere justifying the claim |
| 47 | low | `memory/project/curation-debt.txt:40` | "with the registry emptied it reds on line 34"; measured by draining the row, check 8 reds on `memory/backlog/TOOL.md:57`. Line 34 today passes. ~23 rows prepended since the note was written |
| 13 | low | `memory/project/readme-contract.txt:13` | "reports three of five such lists out of tolerance today"; live report says 2 of 5 |
| 12 | low | `tools/drift-audit/drift_signals.py:198` | PINS comment says the charter "names them in one bullet, so every leg on the bar is spelled there"; the charter says "Read it there and nowhere else", and the retirement is recorded forty lines up at :147-157 |

Three of these — 20, 34 and 40 (below) — are the same defect at the same `file:line`, found
independently by three lenses. See the contradictions appendix.

---

## 4. Partial findings, with corrected severity

Twenty-nine findings had their facts hold and their severity or impact reasoning fail. Every one was
corrected by the skeptic that verified it; none was corrected by this synthesis. **Original → final**
is shown for each.

### Corrected to high (1)

| id | sev | file:line | claim, and what the correction did |
|---|---|---|---|
| 40 | blocker → **high** | `memory/builds/aScouredKit/README.md:51` | Fact identical to 34 and 20. Downgraded because nothing gates on the sentence and the generated region contradicting it is on the same screen — and because it is a third count of one defect |

### Corrected to medium (13)

| id | sev | file:line | claim, and what the correction did |
|---|---|---|---|
| 23 | blocker → **medium** | `AGENTS.md:223` | §6 sends every session at start to a two-tier `decisions/` tree with zero of 945 tracked memory files; `memory/DECISIONS.md:5` repeats it. `AGENTS.md:68` states the real flat topology, so one file holds two. Downgraded: nothing parses it, cost is one failed directory listing |
| 33 | blocker → **medium** | `memory/backlog/TOOL.md:14` | The frozen merge, verified. Downgraded: staleness is 163 commits not 204, the 15 commits are committed and not at risk, and the cited row never claimed to be a run-state record |
| 16 | high → **medium** | `AGENTS.md:318` | Same defect as 26. Downgraded because it is already reported twice in this build's own committed records, and because `check-memory-hygiene.sh:282` would red anyone who actually obeyed the directive |
| 19 | high → **medium** | `memory/backlog/TOOL.md:1` | The DoR read mandate is ~413 KB; this 198,088 B shard is 3.22× `INDEX_CAP_BYTES` and exempt from checks 6, 7 and 8 via `curation-debt.txt`. Downgraded: the row count is already on the drift report and the exemption already documents its own blast radius. What survives is new and narrow — `corpus_ids.py:410-418` drops the charter's `memory/backlog/<FAMILY>.md` placeholder without a note, so the largest DoR document is in no graded population |
| 35 | high → **medium** | `memory/builds/aScouredKit/README.md:61` | `--plan aScouredKit` prints 17 unit rows then `roster: … 14 id(s)`. Downgraded: `--plan` lists all 17 with statuses and derives `next:` from tracked specs, so it does not under-report units — the count line and the stale authored region are wrong, which is id 34's defect again |
| 36 | high → **medium** | `memory/builds/aCollapsedScan/README.md:66` | `CLOSED · 1 unit(s)` at HEAD vs `CLOSED · 5 unit(s)` on the branch. Downgraded: ledger row is :14 not :12, and `memory/backlog/TOOL.md:14-15` does name the branch — the merged record is incomplete, not false |
| 41 | high → **medium** | `tools/unattended/check-unattended.sh:1802` | Nothing compares a README's authored `roster:units` region to its generated `gen:build-units` region; check 21 grades only marker well-formedness, `--check-format` grades headings and slot bytes. Downgraded: authorization, presence and terminality all read the *generated* region, so the consequence is a false record not a bad landing verdict — and only the generated-minus-roster direction is gateable, since a roster naming planned-but-unspecced units is by design |
| 42 | high → **medium** | `skills/session-kickoff/manifest-check.sh:294` | Reproduced: rewriting `memory/guides/SESSION-KICKOFF.md:6` to `watch: README.md` leaves the ratchet at exit 0 with zero output. The only floor is `${#WATCH[@]} -gt 0` at :231 — the check's population is declared by the file it audits. Downgraded: the template half of AGENTS.md *is* watched, so a rule change does trip C5; only the repo-authored preamble is dark, and the disarm is a visible edit to a tracked governance line |
| 43 | high → **medium** | `tools/memory-tree/check-memory-hygiene.sh:1170` | Check 23's population filter (:1248-1249) requires `CLOSED` and `Tier-2`, both authored by the graded run. Two edits buy a unit out of the acceptance ledger *and* out of §8. Downgraded: the check demonstrably reds (the finder's own experiment), its header discloses this at :1129-1132, and no unit is named as actually mis-tiered |
| 2 | high → **medium** | `memory/map/features/codebase-map.md:61` | "Two feature dossiers so far. 69 inventory keys still sit in `baseline.toml`" against a measured 18 and 43; last touched `be0ee6a7`, 2026-08-16. Downgraded: the next sentence self-disclaims the numbers, and the pointer it redirects to is finding 1 |
| 3 | high → **medium** | `memory/map/features/memory-tree-hygiene.md:1` | H1 says "the 21-check gate", :31 says "22 checks", the engine implements 23. Both halves wrong, and this third carrier is named in no backlog row. Downgraded: stale prose in a dossier, primary carriers already tracked by TOOL-aScouredKit-22 |
| 4 | high → **medium** | `memory/map/features/install-prefix.md:107` | "Eleven rows today" against 12 (`tools/install-prefix-waivers.txt:9-20`); the shrink-only promise is stated in three carriers, was broken at `5c83c180`, and nothing compares the count to anything. Downgraded: every row is stale-checked, so the exposure is a slowly widening blind spot not a live hole |
| 5 | high → **medium** | `memory/map/features/unattended.md:98` | "bound by eleven named directives" against `DIRECTIVES_CORE`'s 16 (`unattended.sh:446`), machine-pinned at `.unattended.conf:81` and asserted at `check-unattended.sh:1443-1444`. It was not even true when written. Downgraded: authoritative value is machine-pinned one directory over and nothing reads the dossier |

### Corrected to low (15)

| id | sev | file:line | one line |
|---|---|---|---|
| 24 | blocker → **low** | `AGENTS.md:9` | Same pointer as finding 1; "never counts" is false — with a query it prints 18 dossiers. Under-specified, not pointing at nothing |
| 32 | blocker → **low** | `memory/LIVE.md:7` | aPairedLexer local-only. All 4 specs `SPECCED`, no `RUN.md`, so an in-flight build on its branch is the designed state; diff is 148/75 not "+223 lines" |
| 17 | high → **low** | `memory/DECISIONS.md:6` | Same `decisions/` defect as 23; the HYGIENE.md carve-outs are legitimate kit forward-declarations, not dead selectors |
| 25 | high → **low** | `AGENTS.md:155` | §2's registry renders one row for a four-node fleet and tells a new node to claim `b`. But `AGENTS.md:58-66` carries a full a/b/c/d table ninety lines earlier, and b, c and d each added their row there. A duplicate to reconcile, not a collision trap |
| 6 | medium → **low** | `memory/map/generated/MAP.md:5` | "Every machine-enumerable moving part" enumerates kit directories only; 33 loose tracked files under `tools/`. But all ten named registry entries already contribute inventory keys via `gate-legs.json`, so the stated impact is refuted |
| 9 | medium → **low** | `memory/map/README.md:11` | The grace drain is written passively but gated behind `--drop-affordance-exempt`; "invoked by nothing" is refuted — `WIRE-INTO-PROJECT.md:319` makes it an adopter DoD step |
| 10 | medium → **low** | `tools/drift-audit/drift_report.py:1380` | `signal_dangling_pointers` prints `DEAD PROBE` forever; its sibling is in `DECLARED_EMPTY` and it is not. The liveness assertion is working as designed; the cost is one permanently dead row |
| 21 | medium → **low** | `tools/memory-tree/corpus_ids.py:477` | Rule 3's `capped` set reads raw `INDEX_SET` (`:441`) while check 6 filters `in_debt` first (`:447`) — a guard reading a variable the exemption does not touch. Zero live instances; the finder concedes latent |
| 22 | medium → **low** | `AGENTS.md:206` | Finding 28 refiled under another lens, with the wrong line number (:208 is the sentence) |
| 29 | medium → **low** | `AGENTS.md:193` | §5 mandates `help/` pages and §1's DoD gates on them; no `help/` has ever existed, `HELP_DIR` defaulted and unanswered. Same root cause as 26, but nothing in the tree is *false* — an unsatisfied rule is weaker than a lie |
| 30 | medium → **low** | `AGENTS.md:25` | "What ships here" names 13 of `registry.toml`'s 25 entries, omitting `run-gates` and `lexicon`. Undercoverage in an orientation blurb, nothing false, no consumer derives from it |
| 31 | medium → **low** | `AGENTS.md:538` | "no staleness-drift class here" — the repo's own `core.hooksPath` is the relative `.githooks`, which git resolves per worktree exactly as claimed; the absolute override in 4 of 7 worktrees is environment-injected and the checkouts are byte-identical |
| 37 | medium → **low** | `tools/drift-audit/drift_report.py:1380` | Duplicate of 10 from another lens; the "quietly darkened signal" premise is refuted by `drift_signals.py:97-104`, which names the retirement and keeps the path for adopters |
| 38 | medium → **low** | `memory/builds/aThawedCorpus/RUN.md:15` | `LANDING` over landed work — one instance of a documented class, already specced as TOOL-dUnstalledConvoy-38, with the driver accommodating it at `unattended.sh:1217-1247` |
| 39 | medium → **low** | `memory/builds/aScouredKit/RUN.md:14` | `verb_close` (`:2797`) writes `LANDING` and never stamps `witness`, so the witness predates three of the build's own unit specs. Real and un-backlogged, but 8 commits behind not 9, and `UNATTENDED-PROTOCOL.md:286-290` requires only presence at non-terminal phases |

---

## 5. Unverified findings

**Zero.** All 47 raw findings received a verdict from a skeptic that re-derived the claim
independently.

**This is positive evidence, not an absence of checking, and here is why that assertion is
defensible:** the run integrity line reports 5 of 5 lenses returned with 0 died, and 5 of 5 skeptic
batches returned with 0 died. No lens output was lost, so no finding sat unadjudicated for want of a
verifier, and no zero in this report is the artifact of a dead agent. Had any lens died, this section
would read differently and every count below would be a floor rather than a total.

The one caveat, stated plainly: zero unverified means every finding *got* a verdict. It does not mean
every verdict is right. Section 10 lists four places where two skeptics reached different verdicts on
the same fact.

---

## 6. Refuted findings

| id | file:line | why it fell |
|---|---|---|
| 7 | `memory/map/baseline.toml:38` | `drift-audit` sitting in `baseline.toml` undossiered is the file's *designed* state — its own header says so — and the DoR dossier trigger fires on design passes, while every aScouredKit unit touching that kit is Tier-1. A tracked gap restated as a finding |
| 44 | `tools/memory-tree/check-memory-hygiene.sh:1128` | "Zero checks adjudicate whether a record's assertion is true" is false: check 9 (:607) runs `gen_build_index.py --check`, re-deriving every build's status, roster and unit table from the specs and redding on disagreement. The residual — authored prose is not semantically graded — is the declared definition of a structural gate, stated by name in the headers the finding cites |
| 46 | `memory/builds/aScouredKit/README.md:55` | The claim is wrong at its own cited source: `build-complete` *does* read the authored roster — `unattended.sh:3117` calls `missing_units`, which resolves `want` from `roster_ids` (`:1785-1802`), and the function's comment at :1789-1793 names that caller explicitly. The proposed rewording would replace a true sentence with a false one. The finding's conclusion is right by a different mechanism, which is finding 41's territory |

---

## 7. Gate integrity

### Can the record-policing gates actually fail? Yes — six were TESTED by constructing failing input.

**TESTED (a break was staged and the red observed, or a disarm was staged and the green observed):**

| gate / check | what was staged | observed |
|---|---|---|
| hygiene check 23 | deleted aScouredKit-13's AC4 evidence line | **RED** |
| hygiene check 23 | flipped that spec's header `Tier-2` → `Tier-1`, re-rendered | **exit 0**, gap intact — the buy-out |
| hygiene check 8 | drained `memory/backlog/TOOL.md` from `curation-debt.txt` | **RED** at `memory/backlog/TOOL.md:57` |
| hygiene check 6 | same drain | **RED**, 198088 B > 61440 B |
| hygiene check 7 | same drain | **RED** on 193 rows |
| hygiene `--staged` mode | ran it unmodified | exit 0, **one line of output** for 23 checks |
| `manifest-check.sh` C5 | rewrote `SESSION-KICKOFF.md:6` to `watch: README.md` | **exit 0, zero output** — the check disarms itself |

All staged breaks were restored (`git checkout --`).

**ASSUMED (reported by a lens, not re-derived by a skeptic):** the "six checks across three gates"
total, and `check-arms` holding 23 of 23 hygiene fail-branches armed with 3 reasoned pins. Treat both
as the lens's count.

### SHAPE versus TRUTH

The lens classified all 23 numbered hygiene checks as 12 SHAPE (spelling, placement, size, grammar)
and 9 TRUTH-but-referential (does this id/path/render resolve), concluding zero adjudicate truth.
**The skeptic refuted that conclusion, and the refutation is the important part of this section:**

- **Something does adjudicate truth — for the generated half.** Check 9 (`:607`) runs
  `gen_build_index.py --check`, which re-derives every build's status, roster and unit table from the
  specs and reds when the committed record disagrees. Check 23 joins a spec's numbered acceptance
  criteria to ledger records in other files. Those are live re-derivations graded against records,
  not shape checks.
- **Nothing adjudicates the authored half, by design, and every relevant header says so.**
  `gen_build_index.py:10-15` and `check-memory-hygiene.sh:1128-1132` both state in terms that they
  grade position and canon, never what a slot *says*; :1129-1132 adds that a green row "is not
  evidence the unit was built correctly".
- **The gap between the two halves is where every finding in §3 lives.** A document may assert
  anything about the tree and stay green provided every id and path it names resolves.

The live proof, at HEAD, on the newest record in the tree: `memory/builds/aScouredKit/README.md:51`
states three closed units carry no spec while their specs sit in the same folder and the generated
region thirty lines below lists all three — and the full bar was green over it. Nothing compares the
authored `roster:units` region to the generated `gen:build-units` region (finding 41), and the one
join that exists runs in a single direction: `missing_units` ends at `unattended.sh:1802` with
`comm -23`, so a roster id with no spec is a finding and a spec with no roster row is invisible.

### One gate's guard shares a variable with the thing it guards

`manifest-check.sh` check 5 — the only staleness check in the kickoff ratchet — reads its watch
population from the file it audits, with a floor of one surviving pathspec (`:231`). That is the
charter's own named anti-pattern, live in a merge-bar leg. `ARMS_FLOORS` at
`check-unattended.sh:384` is the existing prior art for the fix.

---

## 8. Cross-cutting themes — the mechanism, not the instances

Six mechanisms produce every finding above. None of them is carelessness; all of them are structural.

**1. A number typed beside the source that owns it.** Findings 2, 3, 4, 5, 13, 18, 28, 30 and 47 are
one defect: a derived count written into prose. `AGENTS.md` §7 bans this by name — "NO count of a
derived population is written in prose" — and `AGENTS.md` itself, `memory/HYGIENE.md`,
`README.md:33`, five map dossiers and two waiver registries all break it. The rule is correct and
unenforced; nothing in the tree compares a prose cardinality to anything.

**2. Unanswered `defaulted` placeholders ship conventions nobody chose.** `REVIEW_DIR` and
`HELP_DIR` are `class="defaulted"` in `tools/govkit/entries/playbook.kit.toml` and unanswered in
`.governance/deploy.toml`, so the charter ships two directory conventions naming directories that
have never existed, one of them contradicting the same file's own preamble. The descriptor's comment
two lines above the block warns about exactly this: a default silently identical to an answer is how
an operator ships a value they never chose.

**3. Deletion without repointing.** §4, §13 and §17 were dropped at v3.0 and six citations to them
survive, two in the TL;DR, all six shipped to adopters. The per-node session ledger retired and one
of its two drift signals was declared dead while the other still prints `DEAD PROBE`. The two-tier
`decisions/` tree went flat and two documents still route sessions to it. The charter's
gate-enumerating section was deleted and a pin comment forty lines from the retirement note still
says it enumerates.

**4. Every join runs in one direction.** `missing_units` is `comm -23`. The map's coverage ratchet
grades key claims and never dossier prose, so five dossiers' sources moved in one 16-commit build
with zero dossier edits and the map stayed green. `corpus_ids.py:410-418` keeps only candidates
already tracked, so the charter's `<FAMILY>` placeholder is dropped without a note and the largest
DoR-mandated document is in no graded population. `SHRINK_ONLY` is a hand-kept table of five over a
tree with at least fourteen declared shrink-only lists, and prints `2 of 5` with no coverage caveat.

**5. The authored record is written last, after the facts moved.** `README.md:51` was added by the
final records commit of the run, after the commit that falsified it. `verb_close` writes `LANDING`
and never re-stamps the witness. Fourteen spec headers were never reopened after their work landed.
The pattern is not "records rot slowly" — it is "records are written at the end of a run by a session
that is finishing, and nothing re-reads them against the tree afterwards".

**6. And the run then certifies itself.** `6dfd08d0` closed aScouredKit as "every declared DoD item
met" over a build README that denies three of its own units, a roster three rows short, a stale
witness, and five dossiers whose sources it changed. Every one of those is a DoD item in §1. None is
machine-checked. The DoD is a checklist a run grades itself against, in the same way check 23's
`Tier-2` token is authored by the run being graded.

**Net:** the project's state feels uncertain because the *derived* layer is honest and narrow, the
*authored* layer is broad and unpoliced, and the two sit in the same files thirty lines apart with no
visual distinction. A reader cannot tell by looking which half they are reading.

---

## 9. Do this next

Cheapest and highest-value first. Each names the file to touch.

1. **`memory/builds/aScouredKit/README.md`** — narrow line 51 to "-10, -16 through -29, -33, -34",
   and add -30/-31/-32 as roster rows 15-17 in the `roster:units` region (:61-80). Two edits. Kills
   findings 20, 34, 40 and the count half of 35, and removes the newest false record in the tree.
2. **`.governance/deploy.toml`** — answer `review_dir = "memory/builds/<slug>/reviews/"`; answer
   `help_dir` with the per-kit README convention gov actually uses or fence the bullet. Re-render.
   Two lines. Kills 26 and 29, and removes a self-contradiction from the always-loaded charter.
3. **`coding-governance-agents.template.md`** (:18, :23, :24, :161, :253, :328) **and `AGENTS.md`**
   (:94, :99, :100, :231, :321, :390) — repoint §17 → §16, drop or restore §4 and §13. Six
   citations, two in the TL;DR, currently shipping to every adopter. Then add a leg asserting every
   cited `§N` has a matching `^## §N` heading in both files.
4. **The 14 stale spec headers** across aBatchedLintel, aMendedLedger, aPacedTurnstile,
   aTetheredScratch, bConvergentLodestar and dNarrowedAnchor — flip to `CLOSED` and re-render. This
   is the largest single truth win in the audit: it corrects 6 of 16 `memory/LIVE.md` rows. Then
   widen the oracle at `tools/drift-audit/drift_report.py:441` so a CLOSED backlog row naming the id,
   or a merge commit that is an ancestor of HEAD, resolves the claim — that alone resolves 12 of the
   14 without a product-source citation.
5. **`memory/HYGIENE.md`** (:29, :94, :112) **and `tools/memory-tree/HYGIENE.template.md`** — six →
   nine, fix the enumeration, and correct the sibling comments at
   `tools/memory-tree/adopt-memory-tree.sh:126` and
   `tools/memory-tree/check-memory-hygiene.sh:296`, plus `memory/README.md:26`. The pair is
   byte-compared, so they move together or the parity leg reds.
6. **`README.md:33`** — delete "21-check" and point at the kit README. **`AGENTS.md:208`** and the
   template — drop "and the gate-leg name". One carrier, one fact.
7. **Push both local-only branches to `origin`** (`branch/paired-lexer-followup-9c31a2`,
   `branch/acollapsedscan-followups`) so 21 commits stop being single-copy, and **decide the frozen
   merge** in the `unattended-check-plan-27c557` worktree — commit it or `git merge --abort`. Its
   base is 163 commits stale, so the resolution is dead either way.
8. **`tools/memory-tree/check-memory-hygiene.sh`** — copy the HELD `printf` from :1166 to the four
   silent blocks at :674, :1073, :1088 and :1098. Four lines, and the pre-commit leg stops claiming
   coverage it does not have.
9. **`tools/drift-audit/drift_signals.py`** — add `dangling_pointers_in_own_ledger` to
   `DECLARED_EMPTY` with the retirement reason (:97-104 is the model); delete the stale PINS comment
   at :198; derive `SHRINK_ONLY` (:78) from the in-file marker instead of declaring five.
10. **`tools/unattended/unattended.sh:1785`** — add the `comm -13` direction to `missing_units`, or
    have it refuse when roster and generated ids disagree. Guard the exemption case: a roster naming
    planned-but-unspecced units is by design, so only generated-minus-roster is safely gateable.
11. **`skills/session-kickoff/manifest-check.sh:231`** — add a `WATCH_FLOOR` graded like
    `ARMS_FLOORS` (`tools/unattended/check-unattended.sh:384`): a minimum count or a required subset
    naming the gate manifest and the charter.
12. **The map dossiers** — `codebase-map.md:61`, `memory-tree-hygiene.md:1` and `:31`,
    `install-prefix.md:107`, `unattended.md:98`: delete the cardinality, cite the source. Move the
    `skill-engines` claim from `unattended.md:15` to `session-kickoff.md:15`. Add
    `memory-tree-hygiene.md` to TOOL-aScouredKit-22's carrier list.
13. **`tools/codebase-map/reuse_lookup.py`** — add a `--counts` mode printing dossiers and baseline
    keys, or delete the pointer sentence at `AGENTS.md:9` and `memory/map/features/codebase-map.md:63`.
    Do not replace it with two numbers in prose.
14. **`memory/project/curation-debt.txt:40`** — state the hidden fault by row id, not by line number.
15. **Left-shift the mechanism**, once the instances are cleared: a leg comparing each build README's
    authored roster region to its generated units region, and a leg redding a dossier whose
    `[paths]` moved in the push range while the dossier did not (`map_diff` already computes the
    attribution). Those two close themes 4 and 5 for good.

---

## 10. Contradictions appendix

Four facts received two different adjudications. The orchestrator reported **0 duplicates** and **0
contradictory verdicts demoted to unverified**; both figures are inconsistent with the skeptic prose,
which names the duplication explicitly in at least two places. Reported as measured, and flagged.

| the fact | adjudication A | adjudication B | resolution taken here |
|---|---|---|---|
| `AGENTS.md:9` — the `reuse_lookup.py` pointer | **1: confirmed, high.** Errors as spelled; prints 177 where a reader expects 43 | **24: partial, blocker → low.** "Never counts" is false; it prints 18 dossiers, so it is under-specified not empty | Both skeptics agree on the *behaviour*; they disagree on what a broken pointer in the charter's opening costs. Carried at high in §3 and low in §4, unmerged, because the disagreement is the finding |
| `AGENTS.md:318` — `memory/reviews/` | **26: confirmed, high.** Self-contradiction with `AGENTS.md:52`, root cause in an unanswered defaulted placeholder | **16: partial, high → medium.** Already twice on this build's own record, and the hygiene gate would red anyone obeying it | Same defect, opposite verdict classes. The fix is identical either way and is item 2 in §9 |
| `memory/DECISIONS.md` / `AGENTS.md:223` — the `decisions/` tree | **23: partial, blocker → medium** | **17: partial, high → low** | Two skeptics, one fact, two final severities three steps apart. Neither re-derivation is wrong; they priced the same failed directory listing differently |
| `memory/builds/aScouredKit/README.md:51` | **20 and 34: confirmed, high** | **40: partial, blocker → high** — whose skeptic writes that it "duplicates id 34 exactly … and should be merged into it rather than counted twice" | Three independent lenses found it. Counted three times in the raw 47; counted once in the state answer |
| `AGENTS.md` hygiene-count delegation | **28: confirmed, medium** (cites :208) | **22: partial, medium → low** (cites :206) — whose skeptic writes "this is finding 28 filed a second time under a different lens" and that the line number is wrong | 28 is the surviving copy; it carries the actionable half (`README.md:33` states a false 21) |

The pattern in this table matters more than any row: **five of the fifteen confirmed findings are
duplicate reports of three underlying defects.** The independent-lens design found the same rot from
three angles, which is corroboration — but the raw count of 47 overstates the distinct defect count,
and the orchestrator's dedup did not catch it.

---

## 11. Run integrity and counts

Stated as measured. **This run is complete: every integrity figure below is zero where it must be.**

- **Lenses:** 5 of 5 returned, **0 died.**
- **Skeptic batches:** 5 of 5 returned, **0 died.**
- **Spurious verdicts discarded:** 0. **Duplicates detected:** 0. **Contradictory verdicts demoted to
  unverified:** 0. **Severity corrections applied:** 29.
- Because no lens died, the finding set is not truncated and the zero in §5 is evidence rather than
  an artifact.

**Counts, all five, unrounded:**

| | count |
|---|---|
| raw findings | 47 |
| confirmed | 15 |
| partial | 29 |
| refuted | 3 |
| unverified | 0 |

15 + 29 + 3 + 0 = 47. Every partial received exactly one severity correction (29 partials, 29
corrections).

**Precision: 0.83, and this is an orchestrator heuristic that was NOT re-derived by this synthesis.**
It is `confirmed / (confirmed + refuted)` = 15 / 18 = 0.833, which excludes all 29 partials from both
numerator and denominator. Counting a partial as a confirmed-with-corrected-severity — which is what
every one of them is — gives 44 / 47 = **0.94**. The charter's §8 threshold of ~0.5 is cleared on
either reading, so no scope tightening is indicated. The two figures are reported side by side rather
than picked between, because the choice of denominator is the whole difference.

**Two integrity caveats of my own, since the orchestrator's zeros are its own measurement:**

1. The **0 duplicates** figure is contradicted by the data it summarizes. Findings 20, 34 and 40 are
   one defect; 1 and 24 are one; 16 and 26 are one; 17 and 23 are one; 22 and 28 are one; 10 and 37
   are one. That is six clusters covering thirteen findings. Two skeptics say so in their own prose.
   The distinct-defect count is therefore closer to **41 than 47**, and the confirmed set contains
   **12 distinct defects, not 15.**
2. Severity distribution after correction — 1 blocker, 7 high, 18 medium, 21 low, 3 refuted — is
   heavily reshaped by the skeptic stage. Twenty-nine of forty-seven findings arrived over-priced.
   That is the finder lenses running hot, not the tree being worse or better than it looks; the
   *facts* held in 44 of 47 cases.

---

*Scope: this audit read records against the tree at HEAD in one worktree on node a. It cannot see
nodes b, c or d, and §2's unknowables apply to every conclusion in it.*

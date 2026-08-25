# TOOL-aMendedLedger-6 — U6: doc truth, the template edit, the residual sweep and the adopter note

**Status:** SPECCED · rev-2 · 2026-08-09 · node a · Tier-2 · base 663ca427 · streams tooling+playbook

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md](../../build/2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md) | journal | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md](../../reviews/2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md](../../reviews/2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md](../../reviews/2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md](../../reviews/2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |

<!-- /gen:spec-records -->

## 1. Goal

Land the master's S6 and S6b. After U1/U2/U4 drain the session ledger out of `memory/project/` and
U3 stops the kit scaffolding and admitting it, every governing doc in both layers — this repo's own
and the adopter-facing product — must describe the tree that now exists, and the product-level
retirement must reach an adopter as a written migration instead of a silent break on their next
hygiene run.

## 2. Scope (IN)

- **S1** `parallel-coding-governance.template.md`: delete `:86-88` and rewrite `:31`, `:68`, `:101`,
  `:102`, `:211` exactly as the master's §4 template table specifies. `:101`'s surviving clause is
  the point of the change — a shared mutable index every session edits is still forbidden; the
  answer is now a GENERATED build index plus U5's row-keyed merge driver for the two indexes that
  must stay authored, not sharding by node.
- **S2** The two template lines master AC10b's own grep still hits after S1 and the master's table
  does not name: `:99` (`in-flight state` in the memory-content list) and `:209` (`greps the journal
  first`). AC10b requires the template's hit count to reach **0**, so both must be reworded.
- **S3** The residual `ledger` sweep the AC10b grep pattern cannot see, because `in-?flight|journal`
  does not match a bare `ledger`. After S1 the word survives at `:33`, `:43`, `:49`, `:67`, `:74`,
  the `## §3` heading at `:76`, and `:181` — each one a pointer into a §3 rule S1 deletes. Repoint
  or drop each; a mandate whose target no longer exists is the `two-answers-to-one-question` class
  this build exists to close.
- **S4** `parallel-coding-governance.template.md:106`: the memory-tree bullet claims a tree "by
  discipline" (false since the 1.5 flatten), `project/` machinery (this build drains it) and a
  "12-check hygiene gate" (the kit catalogues 19). Re-true all three; the check-count fix is
  byte-neutral.
- **S5** `WIRE-INTO-PROJECT.md`: correct the six `in-?flight|journal` claims at `:119`, `:140`,
  `:256`, `:389`, `:403` and `:447`, which state the sharded ledger as a live deliverable of the
  memory-tree kit — AND the four bare-`ledger` claims that pattern cannot see, which are live in the
  same way: `:10` ("streams, sharded ledger, gates, reviews, memory, output discipline" — a contents
  inventory falsified the moment S1 deletes template `:86-88`), `:97` ("the ledger and the decision
  logs share one id scheme"), `:255` (the "**ID + ledger protocol**" sentence) and `:373` ("surface
  the playbook + gate + ledger protocol"). Counted so the sites do not double-book: `:255-256` is
  ONE sentence with the already-listed `:256` and is one edit; `:140` is already listed above and
  also sits inside the `:139-142` paragraph S6 replaces wholesale, so S6 owns `:139`, `:140` and
  `:142`; `:134` (`memory/ledger/*.md text eol=lf`) names the GENERATED month shard and stays. That
  is the whole measured population — `grep -n "ledger" WIRE-INTO-PROJECT.md` → `:10 :97 :119 :134
  :139 :142 :255 :256 :373 :403`.
- **S6** `WIRE-INTO-PROJECT.md`: the S6b migration section — the sharded authored ledger is RETIRED
  at **playbook v2.4 / memory-tree kit 1.8**. Two products, two version lines: S11 bumps the
  playbook, U3 bumps the kit, and naming only the kit version mis-attributes a ruleset change to the
  tooling. An adopter carrying a ledger moves its shards to `<MEMORY_ROOT>/archive/ledger/` and takes
  work state from `gen_build_index.py`, which requires build README front matter.
- **S7** The two docs that contradict the BINDING review protocol: `README.md:45` (`cap-6`
  helpers), `README.md:58` (`~7–9 agents, never >6 concurrent`), and `WIRE-INTO-PROJECT.md:354`
  (`≤6-concurrent rule`) and `:355` (`~7–9 agents, ≤6 concurrent`). The corrected text cites its own
  LAYER's copy of the rule, never the other's: `README.md` is this repo's doc and cites
  `memory/guides/REVIEW-PROTOCOL.md`; `WIRE-INTO-PROJECT.md` is the ADOPTER runbook and cites the
  shipped `tools/workflows/REVIEW-PROTOCOL.template.md`, telling the adopter to install it at
  `<MEMORY_ROOT>/guides/REVIEW-PROTOCOL.md` — the path `check-protocol-parity.test.sh:32-33` treats
  as LIVE (`LIVE="$M/guides/REVIEW-PROTOCOL.md"` / `SHIP="$KITREL/REVIEW-PROTOCOL.template.md"`).
- **S8** `AGENTS.md`: the `memory/` layout bullet, the ID paragraph, and the gate-suite hygiene
  bullet at `:62` — which gains the RUNNING kit version without disturbing the `1.5` token already
  there, because that token names the flatten, not the engine. See §4 Migration.
- **S9** `.claude/SESSION-KICKOFF.md` §B: the ledger pointer row in `### ID + ledger protocol`, the
  template byte-budget trap at `:94-96` whose number this commit falsifies, plus this unit's own
  `last-audit` re-stamp in the same commit.
- **S10** `memory/README.md`, `tools/memory-tree/README.md`, `README.md:32`.
- **S11** `parallel-coding-governance.template.md` version bump, because S1 deletes a MANDATE from a
  shipped ruleset. `:3-6` and the `<!-- governance-template: v2.3 -->` marker at `:8` go to **v2.4**;
  the v2.3 sentence ("v2.3 tightens prose + externalizes the deploy scaffolding and those six
  sections — no rule changed from v2.2", 111 B) is REPLACED — not appended to — by a retirement +
  re-pull sentence in the literal v2.1 shape
  (`memory/archive/parallel-coding-governance.template-v-2-1.md:9`: "the in-flight ledger is now
  sharded per node … re-pull §3 + §5 and the `memory-tree` kit's ledger handling"), reading
  **"v2.4 (2026-08-09): §3's sharded per-node session ledger is RETIRED — work state now comes from
  the generated build index; re-pull §3, §5 and the `memory-tree` kit's handling."** The wording is
  constrained twice over: it must carry no `in-flight` and no `journal` token, or AC1's zero is
  unreachable in the very commit that claims it, and its one bare `ledger` hit is DESCRIPTIVE, so
  AC2 lists it as a surviving hit that instructs nothing. The PRE-edit file is copied to
  `memory/archive/parallel-coding-governance.template-v-2-3.md` in the same commit, matching the
  v-2-0/v-2-1/v-2-2 snapshots already there. Nothing reds if S11 is skipped —
  `tools/check-kit-versions.sh` carries no governance-template entry (its only marker pair is
  memory-tree's, `:31`) — so the miss is silent, the adopter S6b exists to protect gets no re-pull
  signal, and the banner keeps asserting "no rule changed from v2.2", which S1 makes false.

## 3. Non-goals (OUT)

- **`memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`.** They are U3's, coupled by the
  kit/dogfood parity pair, which forces every `memory/HYGIENE.md` edit into the shipped template in
  the same commit via `--render`. AC10a's baseline of 6 hits on each is U3's to drain, not U6's.
  U6 must not touch either file.
- **The kickoff-skill product layer.** `skills/session-kickoff/MANIFEST-TEMPLATE.md:83`, `:141` and
  `skills/session-kickoff/SKILL.md:16`, `:80`, `:113`, `:157-158` still describe an id + ledger
  protocol for adopters. The master's §4 Files touched does not list them, and they are a `kickoff`
  stream product change, not `tooling+playbook`. See §8 F2.
- **`tools/workflows/tier2-review.js:128`.** Its comment reads "ONE ≤6-wide wave" while the file's
  own `boundedParallel(thunks, cap = 5)` at `:15` is correct. Same stale-cap class as S7, but it is
  a workflow script under `check-workflow-syntax.js` and `check-review-join.sh`, and the master's §4
  does not list it. Spin it off.
- **Raising `MAX_BYTES` in `tools/check-template-size.sh`.** The gate's own header forbids it and
  master AC10c requires the count to FALL. S11 is the one ADDING edit in this unit and it funds
  itself out of S1's −954 B; it does not buy space by moving the ceiling.
- **`parallel-coding-governance.customize.md` and `.domain-rules.md`.** Verified: the customize
  companion has zero `ledger|in-flight|journal` hits, and the domain-rules companion's two hits
  (`:45`, `:47`) are database and async-request "in-flight", unrelated to the session ledger.
- **Re-homing the five `*.txt` registries in `memory/project/`.** Master §4 Alternatives rejected.
- **The `check-memory-hygiene.sh:346` `ex7` rewrite.** It was a master Non-goal at rev-2 pending F6;
  at master rev-4 F6 is RESOLVED and the fix is IN, in **U3** (master §3 `:47-48`, §8 F6 `:390-394`).
  It is not U6's, and §7 coupling 1 holds because of it: U6 still changes no line of that script.

## 4. Design

### Inventory

Every claim below is measured at `f9cf666` in this worktree.

| file | measured state | why it is wrong after this build |
|---|---|---|
| template `:86-88` | 954 B over three lines | mandates the sharded per-node ledger, its row shape, and the `{in-flight \| merged:<sha>}` vocabulary |
| template `:31 :68 :101 :102 :211` | 119 · 272 · 251 · 108 · 177 B | read/scan/index/status/wrap-up steps that route through the ledger |
| template `:99 :209` | 220 · 300 B | the only other lines master AC10b's grep still hits |
| template `:33 :43 :49 :67 :74 :76 :181` | 113 · — · 215 · 223 · — · heading · — B | bare `ledger` pointers into the §3 rule `:86-88` defines |
| template `:106` | 420 B | "by discipline" · "`project/` machinery" · "12-check hygiene gate" |
| template `:3-6` and `:8` | `v2.3` banner (415 B over the four lines; the v2.3 sentence is 111 B) + `<!-- governance-template: v2.3 -->` | the banner says "no rule changed from v2.2"; S1 deletes a §3 mandate, so it is false the moment U6 lands |
| `WIRE-INTO-PROJECT.md` `in-?flight\|journal` | 6 hits: `:119 :140 :256 :389 :403 :447` | states the sharded ledger as a live scaffold deliverable and a verification step |
| `WIRE-INTO-PROJECT.md` bare `ledger` | 10 hits: `:10 :97 :119 :134 :139 :142 :255 :256 :373 :403` | four of them (`:10 :97 :255 :373`) are live adopter instructions master AC10b's pattern is blind to; `:134` is the generated month shard and is correct |
| `README.md:45 :58` | `cap-6` · `~7–9 agents, never >6 concurrent` | `tools/hooks/agent-cap.js:38` is `Number(process.env.AGENT_CAP) \|\| 5` |
| `WIRE-INTO-PROJECT.md:354 :355` | `≤6-concurrent rule` · `≤6 concurrent` | same; `:352` on the adjacent line already says `cap-5`, so the file contradicts itself |
| `README.md:32`, `tools/memory-tree/README.md:5 :18` | "12-check hygiene gate" | the kit catalogues 19 checks |
| `AGENTS.md:40-43` | names `project/`, omits the rest | the real `memory/` root is `DECISIONS.md HYGIENE.md LIVE.md README.md TEMPLATE-SPEC.md archive backlog builds gotchas guides ledger map project` |
| `AGENTS.md:62` | "19 checks, kit 1.5 flat tree" | the `1.5` is CORRECT and names the flatten; what is missing is the running engine version, `KIT_MEMORY_TREE_VERSION` at `check-memory-hygiene.sh:13` (`1.7`, moved to `1.8` by U3) |
| `memory/README.md:23` | `MEMORY.md, IN-FLIGHT.md (pointer) + in-flight/<tag>.md, journal/, notes` | none of those survive U1/U2; `gotchas/ guides/ map/` are missing from the Directories list |
| `.claude/SESSION-KICKOFF.md:76-77` | `Ledger: memory/project/in-flight/<tag>.md` | the path is gone after U2 |
| `.claude/SESSION-KICKOFF.md:94-96` | "It now sits at 32746/32768 (**22 bytes free**, measured 2026-08-09)" plus the funding advice built on it | AC3 makes the reported count FALL, so this trap goes stale in the same commit that falsifies it |

The review-protocol truth, verified at source: `memory/guides/REVIEW-PROTOCOL.md:7` "The hard cap —
≤5 verify-stage agents TOTAL", `:62` "Concurrency — ≤5 agents at once, always", `:70` "It moved 6 → 5
here on that basis". `tools/workflows/tier2-review.js` spends `LENSES.length + batches.length + 1`
agents (`:341`) with four lenses (`:130-152`) and `MAX_VERIFIERS = 5` (`:202`), so its real budget is
6–10 agents total, of which at most 5 are verify-stage and at most 5 run at once. This repo's own
manifest already states it correctly at `.claude/SESSION-KICKOFF.md:102-106`; `README.md` and
`WIRE-INTO-PROJECT.md` are the two drifted copies. Measured, and it changes what S7 is:
`grep -rn 'REVIEW-PROTOCOL' WIRE-INTO-PROJECT.md README.md` returns **nothing** today, so S7 does not
correct a citation — it CREATES one in each file, and each must be the citation its own reader can
resolve.

### Migration

**The template byte budget.** The gate reports `32746 / 32768` with **22 free**
(`bash tools/check-template-size.sh`). The measured deltas:

| edit | bytes |
|---|---|
| S1 delete `:86-88` | −954 |
| S1 rewrite `:31 :68 :101 :102 :211` (master's estimates) | ≈ −310 |
| S2 `:99 :209` | ≈ 0, both are substitutions of one term |
| S3 seven residual sites | negative; every one drops a clause or a heading word |
| S4 `:106` | free-floating; funded by the above |
| S11 banner `:3-6` + marker `:8` | the ONLY adding edit: `v2.3` → `v2.4` in the marker is byte-neutral, and the 111 B v2.3 sentence is replaced by a v2.4 sentence of ≈ 175 B, so ≈ **+64** — funded many times over by the deletion, but it must land AFTER it |

Master AC10c binds the outcome, not the arithmetic: the reported count after U6 must be **lower than
32 746**. Land the deletion first and measure after each edit — the gate is one command and the
margin before the deletion is 22 bytes.

**The read-path trap in `AGENTS.md`.** `AGENTS.md` is `CHARTER` in `.memory-tree.conf`, so hygiene
check 16 derives a read set from its own text: `read_set` (`corpus_ids.py:277-305`) collects every
backticked, md-linked or bare token that starts with `memory/` and resolves to a tracked FILE; check
16 itself sums those bytes against `READ_PATH_CEILING` at `corpus_ids.py:392-397` — NOT inside
`read_set` — and — rule 3, `corpus_ids.py:401-404` — fails any member that is not in check 6's index
set and not in `READ_PATH_WAIVER` (currently empty).

- Measured now: 3 members, 29 624 B, ceiling 37 060 — 7 436 B of headroom.
- The index set (`bash tools/memory-tree/check-memory-hygiene.sh --print-index-set`) contains
  `memory/README.md`, `memory/LIVE.md`, `memory/DECISIONS.md`, `memory/ledger/*.md`, the backlog
  shards, `memory/map/*` and `memory/guides/REVIEW-PROTOCOL.md`. It does **not** contain
  `memory/HYGIENE.md` (17 281 B) or `memory/TEMPLATE-SPEC.md` (8 795 B).
- Therefore: a prefixed `` `memory/HYGIENE.md` `` or `` `memory/TEMPLATE-SPEC.md` `` in `AGENTS.md`
  fires check 16 rule 3 immediately. The existing layout bullet already dodges this by naming its
  entries TREE-RELATIVE (`` `DECISIONS.md` ``, `` `backlog/<FAMILY>.md` ``), which the `memory/`
  prefix test rejects. **S8 keeps that convention**: the enlarged layout bullet names `HYGIENE.md`,
  `TEMPLATE-SPEC.md`, `LIVE.md`, `ledger/<month>.md`, `gotchas/`, `guides/`, `map/`, `archive/` and
  `project/` tree-relative, at zero read-path cost. A directory citation is also safe — resolution
  requires a tracked file — which is why `` `memory/archive/` `` in the same bullet costs nothing
  today.
- S8's ID-paragraph rewrite MAY cite `` `memory/LIVE.md` `` with the prefix: it is in the index set
  and adds 1 436 B, landing the read path at 31 060 of 37 060.

**The kit-version claim in `AGENTS.md:62`.** The line reads, verbatim:

    - `memory/` hygiene (19 checks, kit 1.5 flat tree) — `tools/memory-tree/check-memory-hygiene.sh`; checks 9, 13-16 and 17-19 delegate to `gen_build_index.py`, `corpus_ids.py` and `gotchas.py`

Measured, and it reverses rev-1's premise: the `1.5` is **not** a stale running-version token. It
names the kit release that FLATTENED the tree, and it agrees with five in-repo sites this unit does
not touch — `check-memory-hygiene.sh:17` ("Since 1.5 the tree is FLAT"), `:112` ("the 1.5 flatten
changed the segment count…"), `:206` and `:243` ("FLAT (1.5)"), and `adopt-memory-tree.sh:12`
("(kit 1.5). The tree is flat."). Substituting `1.8` for it would assert the flatten happened at 1.8
— false — and would manufacture exactly the `two-answers-to-one-question` divergence §7 names as this
unit's live exposure. So S8 does not substitute; it states both facts in one line, verbatim:

    - `memory/` hygiene (19 checks, flat tree since kit 1.5; engine at kit 1.8) — `tools/memory-tree/check-memory-hygiene.sh`; checks 9, 13-16 and 17-19 delegate to `gen_build_index.py`, `corpus_ids.py` and `gotchas.py`

Read the `1.8` from `KIT_MEMORY_TREE_VERSION` at `tools/memory-tree/check-memory-hygiene.sh:13` at
build time — U3 runs before U6 in the master's §4 Rollout and moves it 1.7 → 1.8 — never from recall.
Do **not** remove the argv path `tools/memory-tree/check-memory-hygiene.sh` from that bullet: the
drift signal `handkept_inventories_disagreeing_with_source` matches gate legs on their argv script
path (`tools/drift-audit/drift_signals.py:64-103`, `:129-137`) and is pinned shrink-only at 7 of 38.
**Ownership:** `AGENTS.md:62` is edited exactly ONCE. U3's sub-spec also claimed it, on the premise
this paragraph refutes; if U3 lands the corrected line first, U6 verifies it against AC11 and edits
nothing.

**`memory/README.md` is inside check 15's present-tense corpus.** `corpus_ids.py:198-201` restricts
that corpus to `memory/{DECISIONS,README,HYGIENE,TEMPLATE-SPEC,LIVE}.md` plus `backlog/ ledger/
project/ guides/` — that is the `present = re.compile(...)` block; `:281-292` is `read_set`'s
docstring tail and the `READ_PATH_PREFIX` comment and belongs to check 16, not here. `DEAD_PATH_PIN="0"`
means one new unresolving rooted citation reds the leg.
`AGENTS.md`, `README.md`, `WIRE-INTO-PROJECT.md` and `.claude/SESSION-KICKOFF.md` are all OUTSIDE
that corpus. So S10's `memory/README.md` edit is the only one where every backticked path and every
md-link target must resolve at commit time; `gotchas/`, `guides/`, `map/` and `archive/` all exist.
Keep each line ≤ 300 chars — the file is in the index set and check 7 applies.

**The archive snapshot S11 adds.** `memory/archive/parallel-coding-governance.template-v-2-3.md` is a
new tracked file inside the memory tree, so its gate exposure was checked rather than assumed:
`archive/` is exempt from check 1 (prompt placement, `check-memory-hygiene.sh:156`) and check 2 (link
integrity, `:163`), opaque to check 3's structure lint (`:212`), outside check 6's index set, and
outside check 10's rotated-name pattern `^memory/archive/[^/]+\.[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$`
(`:430`), which `…template-v-2-3.md` does not match. It is outside check 15's corpus regex above, and
it defines no ids — measured, the template carries zero `(PLAY|KICK|TOOL|DEPL)-<slug>-<seq>` tokens,
same as the v-2-2 snapshot. The three snapshots already tracked are the standing precedent.

**The S6b migration section.** Its home is `WIRE-INTO-PROJECT.md` §3 (the memory-tree adoption
section), directly replacing the ledger-rule paragraph at `:139-142`. It must state, in this order:

1. the sharded authored ledger (`project/IN-FLIGHT.md` + `project/in-flight/<tag>.md`) is RETIRED at
   playbook v2.4 / memory-tree kit 1.8; the scaffolder no longer writes it and hygiene check 3 no
   longer admits it;
2. an adopter carrying one relocates — never deletes — the shards to `<MEMORY_ROOT>/archive/ledger/`,
   byte-identically, because the shards are the only carrier of worktree names, review ids and
   session narrative;
3. work state now comes from `gen_build_index.py`, which needs each build's `README.md` front matter:
   `slug node opened streams roster ids` are REQUIRED (`gen_build_index.py:56`) and `status:` is
   required only when no spec under that build carries a `**Status:**` header
   (`gen_build_index.py:185-193`), while `status:` alongside a spec header is a hard error
   (`:194-199`);
4. the prerequisite list, because for a real adopter this is not a one-liner. Measured on the one
   adopter found on this node (`swydee`): kit 1.4, a pre-flatten tree, three live rows, no
   `LIVE.md`, no `ledger/`, and zero build READMEs carrying front matter. Migrating that repo is its
   own unit in its own repo.

This section is the ONLY place in either product doc where the words `in-flight` or `journal` may
survive, per master AC10b, and every surviving use must describe the ledger as retired and name the
migration.

### Rollout

U6 is one commit. It is the third of the three units that stage a watched pathspec, and the last of
the doc units, so it runs after U3 has moved the kit version and after U2 has created
`memory/archive/ledger/`.

| step | why in this order |
|---|---|
| 1. `cp parallel-coding-governance.template.md memory/archive/parallel-coding-governance.template-v-2-3.md` | the snapshot must be the PRE-edit bytes; taken later it archives the wrong version |
| 2. template `:86-88` deletion, then measure | frees the kilobyte every later edit spends against a 22-byte margin |
| 3. template `:31 :68 :101 :102 :211 :99 :209 :106` + the S3 sweep, measuring after each | AC10c is a falling count, not a green gate |
| 4. template `:3-6` + `:8` → v2.4 (S11), then measure | the only ADDING edit — land it after the deletion has funded it, and word it clear of `in-?flight\|journal` so AC1 still reaches 0 |
| 5. `WIRE-INTO-PROJECT.md` — the six `in-?flight` hits, the four bare-`ledger` hits, the S6b section replacing `:139-142`, `:354-355` | the adopter-facing layer |
| 6. `AGENTS.md`, `README.md`, `memory/README.md`, `tools/memory-tree/README.md` | this repo's own layer |
| 7. re-run `bash tools/check-template-size.sh` and rewrite `.claude/SESSION-KICKOFF.md:94-96`'s byte number and its `measured <date>` FROM THAT OUTPUT, not from recall | the trap states 32746 / 22 free; step 2 falsifies it, and a trap quoting a budget the gate no longer reports is this unit's own gotcha class, self-inflicted |
| 8. `.claude/SESSION-KICKOFF.md` §B row, THEN re-verify §B against the tree, THEN re-stamp `last-audit` | the stamp must be the last edit in the commit and must be taken from `date` |

### Files touched (estimate)

`parallel-coding-governance.template.md` (1 deletion of 3 lines, 15 line rewrites, plus the `:3-6`
banner and the `:8` marker), `WIRE-INTO-PROJECT.md` (6 `in-?flight` corrections, 4 bare-`ledger`
corrections, 2 cap corrections, 1 new section replacing `:139-142`), `AGENTS.md` (`:40-43`,
`:54-57`, `:62`), `README.md` (`:32`, `:45`, `:58`), `memory/README.md` (`:17-23`),
`tools/memory-tree/README.md` (`:5`, `:18`), `.claude/SESSION-KICKOFF.md` (`:5`, `:73-78`, `:94-96`,
and `:85-88` if U3 or U5 has not already pruned that dated correction — its prune condition, "a
second audit has stamped from `date` cleanly", holds by U6). **One new file:**
`memory/archive/parallel-coding-governance.template-v-2-3.md`, a byte copy of the pre-edit template.
No code.

### Alternatives rejected

- **Naming `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md` prefixed in `AGENTS.md` and waiving
  them via `READ_PATH_WAIVER`.** Rejected: it spends 26 KB of a 7 436 B headroom and buys the space
  by disabling the rule that watches it, on a file that `.memory-tree.conf` deliberately ships with
  an empty waiver. The tree-relative convention already in that bullet gives the same reader the
  same information for free.
- **Leaving the bare-`ledger` sites (S3, and S5's four) to a follow-up because master AC10b's grep
  cannot see them.** Rejected: template `:33`, `:43`, `:49`, `:67`, `:74`, `:76` and `:181` would
  keep instructing a session to write a ledger row into a §3 that no longer defines one, and
  `WIRE-INTO-PROJECT.md:10`, `:97`, `:255` and `:373` would keep selling an adopter a protocol the
  kit no longer ships. A shipped ruleset with a mandate pointing at a deleted rule is worse than the
  state before the build.
- **Shipping the retirement inside an unchanged v2.3 (no S11).** Rejected: nothing reds, which is the
  whole problem. `tools/check-kit-versions.sh` has no governance-template entry, so an adopter
  diffing §-body by version would see "no rule changed from v2.2" over a deleted §3 mandate and take
  no re-pull. S6b's upgrade note has no version to point at without it.
- **Substituting `1.8` for the `1.5` token in `AGENTS.md:62`.** Rejected on measurement: `1.5` names
  the flatten and agrees with five untouched in-repo sites. See §4 Migration.
- **Citing `memory/guides/REVIEW-PROTOCOL.md` from `WIRE-INTO-PROJECT.md` (S7).** Rejected: that path
  is under THIS repo's `MEMORY_ROOT`, and an adopter chooses where their memory tree and kits live.
  The adopter-facing artifact is `tools/workflows/REVIEW-PROTOCOL.template.md`, which
  `check-protocol-parity.test.sh` renders into `<MEMORY_ROOT>/guides/REVIEW-PROTOCOL.md`. Nothing
  would red — `WIRE-INTO-PROJECT.md` is outside check 15's corpus — which is precisely the failure
  class S5 and S7 exist to close.
- **Retiring the ledger in `skills/session-kickoff/` in this commit.** Rejected: cross-stream, and
  the master's §4 does not list those files. See §8 F2.

## 5. Production-readiness checklist

- security — N/A. Documentation only; no auth, egress or input-handling surface changes.
- perf / scale — N/A. No executable path changes. The template shrinks, which shortens every
  session's mandatory read.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing product strings.
- error / empty / loading states — N/A. No runtime states; the only "empty" is the AC10b grep
  reaching zero hits on the template, asserted directly.
- observability — `bash tools/check-template-size.sh` prints the byte count on every run, and the
  AC10a/AC10b greps are the instrument for the rest. Both are recorded in the commit message.
- risks — no data-loss surface. The live risk is a FALSE correction: a doc claim rewritten from
  recall rather than re-derived from its source. Every claim in this unit names the file and line it
  was read from, and the kit version is read at build time rather than typed. Rollback is
  `git revert`.
- testing + left-shift gates — no new gate leg. The existing legs that can catch this unit's
  failures are `template size <=32KiB`, `memory hygiene (19 checks)`, `kickoff-manifest ratchet` and
  `drift-audit records`; each is named in §7 with what it catches here.
- migration / rollback — no adopter data moves. The adopter-facing behaviour change is the
  retirement the owner ratified at master §8 F2 and F5, and S6 IS its migration note; S11 is the
  version line that makes the note findable by an adopter diffing per §-body.
- user docs — this unit is the user docs. `WIRE-INTO-PROJECT.md` is the adopter-facing surface and
  `parallel-coding-governance.template.md` is the shipped ruleset.

## 6. Acceptance criteria

- **AC1** When `grep -rniE "in-?flight|journal" parallel-coding-governance.template.md` is run after
  U6, it returns **0** hits (master AC10b). Baseline at `f9cf666` is 8, at lines 31, 68, 86, 87, 99,
  101, 209, 211. S11's new banner sentence is written to carry neither token, so it does not put the
  count back above 0.
- **AC2** When `grep -n "ledger" parallel-coding-governance.template.md` is run after U6, every
  surviving hit is listed in the commit message with its reason, and none of them instructs a
  session to read, write or prune a ledger row. Baseline at `f9cf666` is **13** hits, measured
  `grep -c`, at lines 31, 33, 43, 49, 67, 68, 74, 76, 86, 101, 102, 181, 211. The arithmetic S3
  rests on needs all 13: 5 S1 rewrites + line 86 + the 7 S3 sites. Exactly one hit is EXPECTED to be
  new — S11's v2.4 banner, which describes the retirement and instructs nothing.
- **AC3** When `bash tools/check-template-size.sh` is run after U6 it exits 0 and the reported byte
  count is **lower than 32 746** (master AC10c). And the byte number quoted in
  `.claude/SESSION-KICKOFF.md:94-96` equals that reported count, with its `measured <date>`
  parenthetical rewritten from the same run — a trap stating a budget the gate no longer reports is
  the `two-answers-to-one-question` class this unit exists to close.
- **AC4** When `grep -rniE "in-?flight|journal" WIRE-INTO-PROJECT.md` is run after U6, every hit is
  inside the S6b migration section, describes the ledger as RETIRED, and names the migration
  destination `<MEMORY_ROOT>/archive/ledger/` (master AC10b). Baseline 6, at lines 119, 140, 256,
  389, 403, 447.
- **AC4b** When `grep -n "ledger" WIRE-INTO-PROJECT.md` is run after U6, no surviving hit instructs
  an adopter to scaffold, write or read a sharded ledger row, and every surviving hit is either
  inside the S6b migration section or the generated `memory/ledger/` path at `:134`. Baseline 10, at
  lines 10, 97, 119, 134, 139, 142, 255, 256, 373, 403 — this is the wider pattern AC4 is blind to,
  and it is what grades S5's four extra sites.
- **AC5** When `WIRE-INTO-PROJECT.md` §3 is read after U6, it states the three front-matter facts a
  migrating adopter needs — the six REQUIRED keys, when `status:` is required, and that `status:`
  beside a spec header is an error — each matching `tools/memory-tree/gen_build_index.py:56` and
  `:185-199`.
- **AC6** When `grep -rniE "cap-6|>6 concurrent|≤6 concurrent|6-concurrent" README.md
  WIRE-INTO-PROJECT.md` is run after U6, it returns 0 hits, and both files instead state the cap as
  5, each citing the copy of the rule ITS OWN reader can resolve: `README.md` cites
  `memory/guides/REVIEW-PROTOCOL.md`; `WIRE-INTO-PROJECT.md` cites
  `tools/workflows/REVIEW-PROTOCOL.template.md` and instructs the adopter to install it at
  `<MEMORY_ROOT>/guides/REVIEW-PROTOCOL.md` — the LIVE path of
  `tools/workflows/check-protocol-parity.test.sh:32-33`. `grep -rn 'REVIEW-PROTOCOL'
  WIRE-INTO-PROJECT.md README.md` returns nothing at baseline, so this AC grades citations being
  CREATED; `grep -n 'memory/guides/REVIEW-PROTOCOL' WIRE-INTO-PROJECT.md` must stay at 0 hits.
- **AC7** When `README.md:58` and `WIRE-INTO-PROJECT.md:355` are read after U6, the agent budget they
  quote for `tools/workflows/tier2-review.js` matches that file's own arithmetic — four finder
  lenses plus at most five batched verifiers plus one synthesis pass, at most five verify-stage
  agents TOTAL and at most five concurrent.
- **AC8** When `grep -rniE "in-?flight|journal" AGENTS.md .claude/SESSION-KICKOFF.md README.md
  memory/README.md tools/memory-tree/README.md` is run after U6, it returns 0 hits, and the commit
  message records the per-file baseline it started from: 0 · 1 · 0 · 1 · 0 (master AC10a). A
  zero-hit result on a file whose baseline was already 0 is not evidence of work and is not claimed
  as such. The path list deliberately excludes `memory/archive/`, where S11's v-2-3 snapshot
  preserves the retired text on purpose, exactly as the v-2-0/-1/-2 snapshots already do.
- **AC9** When `AGENTS.md`'s `memory/` layout bullet is read after U6, it names every entry
  `git ls-files memory | cut -d/ -f2 | sort -u` returns — `DECISIONS.md HYGIENE.md LIVE.md README.md
  TEMPLATE-SPEC.md archive backlog builds gotchas guides ledger map project` — and names them
  tree-relative, so `python tools/memory-tree/corpus_ids.py --check` reports no check 16 rule 3
  finding.
- **AC10** When `python tools/memory-tree/corpus_ids.py --measure` is run after U6, the measured
  read-path total is at or under `READ_PATH_CEILING` (37 060) with no member outside the index set.
  Baseline 29 624 B over 3 members.
- **AC11** When `sed -n 62p AGENTS.md` is read after U6 it contains `kit 1.8` — the value of
  `KIT_MEMORY_TREE_VERSION` at `tools/memory-tree/check-memory-hygiene.sh:13` after U3 — AND still
  contains `flat tree since kit 1.5`, AND still cites the argv path
  `tools/memory-tree/check-memory-hygiene.sh`. Independently, `grep -rn "FLAT (1\.5)"
  tools/memory-tree/` still returns **3** hits (`check-memory-hygiene.sh:206`, `:243`, `:429`), and
  `grep -n "kit 1\.5" tools/memory-tree/adopt-memory-tree.sh` still returns `:12` — the flatten
  token is not what moved.
- **AC12** When `python tools/drift-audit/drift_report.py --check` is run after U6 it exits 0 and
  `handkept_inventories_disagreeing_with_source` reads at or under its pin of 7.
- **AC13** When `grep -rniE "12[- ]check" README.md tools/memory-tree/README.md
  parallel-coding-governance.template.md` is run after U6, it returns 0 hits, and each rewritten
  claim states 19 — the count `memory/HYGIENE.md`'s catalog carries (12 in the shell gate, 13-16 in
  `corpus_ids.py`, 17-19 in `gotchas.py`).
- **AC14** When `bash skills/session-kickoff/manifest-check.sh --staged` is run on U6's staged
  commit it exits 0 with no FAILED line: the commit stages the watched
  `parallel-coding-governance.template.md` and carries its own `last-audit` re-stamp in the same
  commit (C5s).
- **AC15** When `.claude/SESSION-KICKOFF.md`'s `last-audit` datetime is compared to the node clock at
  commit time, it was produced by `date -Iseconds` and not hand-written — the failure the file's own
  dated correction at `:85-88` records. If that correction is still present, U6 prunes it, since its
  stated prune condition has held.
- **AC16** When `bash tools/run-gates.sh` is run on U6's commit, all 38 legs are green (master AC11).
- **AC17** When `grep -n 'governance-template:' parallel-coding-governance.template.md` is run after
  U6 it reads `v2.4`, the `:3-6` banner names v2.4 with the retirement + re-pull sentence and no
  longer says "no rule changed from v2.2", and
  `git ls-files --error-unmatch memory/archive/parallel-coding-governance.template-v-2-3.md` exits 0
  with that file byte-identical to `parallel-coding-governance.template.md` at `HEAD~1`.

## 7. Gates

Every leg of `bash tools/run-gates.sh` (38 at `f9cf666`) must stay green. The ones this unit can
actually break, with what each catches here:

- `template size <=32KiB` — `tools/check-template-size.sh`. The only gate on S1-S4 and S11, and it is
  one-sided: it passes at 32 767 bytes. AC3 is what makes the count FALL, so run the command and
  read the number rather than trusting the exit code. S11 is the one edit that ADDS, so measure
  after it specifically.
- `memory hygiene (19 checks)` — `tools/memory-tree/check-memory-hygiene.sh`. Check 2 (link
  integrity) and check 7 (entry budget ≤ 300 chars) on `memory/README.md`; check 15 (dead repo-path
  citations, `DEAD_PATH_PIN="0"`) on the same file; check 16 (read-path accounting) on `AGENTS.md`.
  S11's archive snapshot is inside the memory tree but outside every one of those populations — the
  per-check evidence is in §4 Migration.
- `kickoff-manifest ratchet` — `skills/session-kickoff/manifest-check.sh`. C5/C5s on the staged
  template, C4 on the three `verify-paths` anchors (`AGENTS.md`,
  `parallel-coding-governance.template.md`, `README.md` — U6 edits all three, so the §B
  re-verification behind the stamp is real work, not a formality).
- `drift-audit records` — `python tools/drift-audit/drift_report.py --check`, for the `AGENTS.md`
  gate-suite edit.
- `codebase-map coverage + freshness` — U6 claims no new inventory key and edits no dossier, so this
  leg should be untouched; if it moves, an edit went somewhere it was not scoped to go.

Three couplings the master states in its §7, honoured here:

1. **U6 changes no non-comment line of `tools/memory-tree/check-memory-hygiene.sh`**, so the
   `KIT_MEMORY_TREE_VERSION`-in-the-same-diff coupling (three sites plus a `--render`) does not bind
   this unit. U6 only READS that constant, for AC11. The `ex7` rewrite at `:346` that master rev-4
   moved out of Non-goals is U3's, not U6's. If an edit here ever reaches that script, the coupling
   binds immediately.
2. **The kickoff manifest watches seven pathspecs** —
   `tools/memory-tree/check-memory-hygiene.sh`, `tools/check-template-size.sh`, `tools/run-gates.sh`,
   `tools/gate-legs.json`, `skills/session-kickoff/manifest-check.sh`, `.memory-tree.conf`,
   `parallel-coding-governance.template.md`. U6 stages the last of those, so U6's commit carries its
   own `last-audit` re-stamp, stamped from `date -Iseconds` @ the full sha
   (`HEAD` on the default branch, else `git merge-base origin/main HEAD`).
3. **U6 adds no gate leg**, so no `AGENTS.md` gate-suite bullet is owed and
   `handkept_inventories_disagreeing_with_source` must not move off 7. The inverse is the live risk:
   S8 must not delete an argv script path from that section.

A fourth coupling, this unit's own: **no file under `tools/`, `skills/`, `.claude/`, the playbook
template or `WIRE-INTO-PROJECT.md` may cite this build's spec id.** `tools` is `PRODUCT_GLOBS[0]`
(`tools/drift-audit/drift_signals.py:20-28`) and `signal_spec_status` flags every non-terminal spec
whose H1 id `git grep`s inside those globs, against a pin already at its value. U6 edits five of
those paths, so every doc line it writes cites this build by SLUG (`aMendedLedger U6`), never by id.

Run `python tools/memory-tree/gotchas.py --for-diff 663ca427..HEAD` before the review, not after.
The class this unit is most exposed to is `two-answers-to-one-question` (`universal: true`): a doc
that restates a number owned by source.

## 8. Open questions

- **F1 — master AC10b's grep is narrower than the change it grades.** `in-?flight|journal` cannot
  match a bare `ledger`, and after the master's table lands, seven template sites (`:33`, `:43`,
  `:49`, `:67`, `:74`, the `## §3` heading at `:76`, `:181`) plus four `WIRE-INTO-PROJECT.md` sites
  (`:10`, `:97`, `:255`, `:373`) still point at a §3 rule that no longer exists.
  **RESOLVED (build, 2026-08-09): treat AC10b's zero as a floor, not a ceiling** — S3 sweeps the
  template sites, S5 sweeps the runbook sites, and AC2 and AC4b grade both on the wider bare-`ledger`
  pattern. No owner answer is needed to proceed; the master's AC10b is reported as under-scoped
  rather than silently reinterpreted.
- **F2 — does the kickoff-skill product layer retire the ledger too?** `MANIFEST-TEMPLATE.md:83`,
  `:141` and `SKILL.md:16`, `:80`, `:113`, `:157-158` still describe an id + ledger protocol to
  adopters. Both mentions in `SKILL.md:157-158` are conditional ("only if the manifest defines an
  id/ledger protocol"), so nothing there breaks on its own, and the master's §4 Files touched does
  not list either file. **RESOLVED (build, 2026-08-09): its own `KICK` unit** — it is a
  `kickoff`-stream product change with its own per-machine junction install path, and folding it
  into a `tooling+playbook` unit would make one commit answer two product questions. OUT here (§3).

All six of the MASTER's forks (F1-F6) are `RESOLVED` at master rev-4, so no step of this unit waits
on an answer from either level.

## 9. Revision log

- rev-1 · 2026-08-09 · initial draft of U6, written to master `TOOL-aMendedLedger-1` rev-3 (ratified
  2026-08-09, forks F2 and F5 resolved as retire-everywhere). Every line number, byte count and
  baseline in §4 and §6 was measured in this worktree at `f9cf666`, not recalled. Two findings the
  master's §4 table does not carry are folded in as S2 and S3: the template lines `:99` and `:209`
  that master AC10b's own grep still hits, and the seven bare-`ledger` sites that grep cannot see.
  The `AGENTS.md` read-path trap (check 16 rule 3 against a non-index-set member) is pinned in §4
  Migration because the obvious way to write S8 fires it.
- rev-2 · 2026-08-09 · folded the adversarial sub-spec review (X1 + D6-1…D6-6), re-based on master
  rev-4 where all six forks now read RESOLVED. **X1:** the H1 was `TOOL-aMendedLedger-1 U6 — …`,
  which `gen_build_index.py:54`'s `H1_RE` cannot parse (the id must be followed immediately by ` — `)
  and which put six specs on one id — the shape `drift_report.py:228-231` records as over-flagging
  107/126 upstream. It now reads `TOOL-aMendedLedger-6 — U6: …`, per-file seq, unit label after the
  dash. **D6-1:** §4 Migration cited `corpus_ids.py:281-292` for check 15's present-tense corpus;
  opened, those lines are `read_set`'s docstring tail and the `READ_PATH_PREFIX` comment, which are
  check 16's. Repointed to `:198-201` (the `present = re.compile(...)` block), and the read-path
  paragraph now separates `read_set` (`:277-305`, re-measured — rev-1 said `:277-303`) from the byte
  sum against `READ_PATH_CEILING`, which happens in check 16 at `:392-397`. **D6-2:** AC2's baseline
  said 12 hits while listing 13 numbers; `grep -c "ledger" parallel-coding-governance.template.md` is
  **13**, and 13 is the count S3's arithmetic needs. **D6-3:** new **S11** — the unit deleted a
  mandate from a shipped ruleset inside an unchanged v2.3 whose banner says "no rule changed from
  v2.2". `:3-6` and the `:8` marker go to v2.4 in the v2.1 banner shape, the pre-edit file is
  snapshotted to `memory/archive/parallel-coding-governance.template-v-2-3.md`, S6b now says
  "playbook v2.4 / memory-tree kit 1.8" (two products, two version lines), AC17 grades it, and the
  banner is constrained to carry no `in-flight`/`journal` token so AC1 still reaches 0. Nothing reds
  without S11: `tools/check-kit-versions.sh` has no governance-template entry. **D6-4:** AC6 told
  `WIRE-INTO-PROJECT.md` to cite `memory/guides/REVIEW-PROTOCOL.md`, a path under THIS repo's
  MEMORY_ROOT that no adopter has; AC6 and S7 now split by layer, the runbook citing
  `tools/workflows/REVIEW-PROTOCOL.template.md` and the install path
  `check-protocol-parity.test.sh:32-33` treats as LIVE. The review's own pointer for that pair
  (`:14-16`) was off — measured, `LIVE=`/`SHIP=` are at `:32-33`, and `:14-16` is the substitution
  comment. **D6-5:** `.claude/SESSION-KICKOFF.md:94-96` states "32746/32768 (**22 bytes free**)" and
  the funding advice built on it; AC3 falsifies that number in this same commit, so the line joins S9
  and §4 Files touched, Rollout gains step 7 (re-measure, then rewrite from the gate's output), and
  AC3 asserts the two agree. **D6-6:** S5 covered only the six `in-?flight|journal` hits in the
  runbook; the four live bare-`ledger` claims at `:10`, `:97`, `:255` and `:373` survived both S5 and
  AC4. S5 now carries them with the double-booking spelled out (`:255-256` is one sentence; `:139`,
  `:140`, `:142` belong to S6's replacement; `:134` is the generated path and stays), and **AC4b**
  grades the wider pattern. Beyond the review: rev-1 called `AGENTS.md:62`'s `kit 1.5` a stale
  version token and directed substituting `1.8`. Measured, `1.5` names the FLATTEN and agrees with
  five untouched sites (`check-memory-hygiene.sh:17`, `:112`, `:206`, `:243`,
  `adopt-memory-tree.sh:12`), so substituting it would assert a false history and manufacture this
  unit's own gotcha class; S8 now states both facts in one verbatim line, AC11 asserts both plus the
  3 surviving `FLAT (1.5)` hits, and §4 Alternatives records the reversal. §7 gained a fourth
  coupling forbidding this build's spec id in any `PRODUCT_GLOBS[0]` path U6 edits, and §3 gained the
  `ex7` note now that master rev-4 moved that rewrite out of Non-goals and into U3.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "documentation claim re-derived from its single source
instead of restated"`, run with `CODEBASE_MAP_ROOT` exported (the map is installed at the
non-canonical `tools/` prefix — `memory/map/features/codebase-map.md` §Gaps), returns `claims`
(`tools/codebase-map/selftest.py`, fan-in 4, SEAM) and `derive_status`
(`tools/memory-tree/gen_build_index.py`, fan-in 0). Neither is a seam this unit can wire code
through, because this unit ships no code.

The reuse decision is therefore about SOURCES, not functions: no claim in this unit is authored
twice. Each corrected doc line is re-derived at build time from the one place that owns the fact —
`KIT_MEMORY_TREE_VERSION` in `tools/memory-tree/check-memory-hygiene.sh:13` for the engine version
and the kit's own comments (`:17`, `:112`, `:206`, `:243`) for the flatten version, `CAP` in
`tools/hooks/agent-cap.js:38` and `memory/guides/REVIEW-PROTOCOL.md` for the agent cap (with
`tools/workflows/REVIEW-PROTOCOL.template.md` as the adopter-layer copy of that same source),
`REQUIRED_KEYS` in `tools/memory-tree/gen_build_index.py:56` for the front-matter contract,
`memory/HYGIENE.md`'s catalog for the check count, `bash tools/check-template-size.sh`'s own output
for the byte budget quoted in `.claude/SESSION-KICKOFF.md:94-96`, and `git ls-files memory` for the
layout bullet. Where a doc cannot avoid restating a number, it cites the file that owns it, so the
next reader can tell which copy is the source. That is the `two-answers-to-one-question` class
handled by construction rather than by a gate, which is the only handling available for prose.

Two caveats, stated rather than hidden: the map's corpus does not index Markdown prose, so no
lookup over it could have found the doc-layer duplication this unit removes; and 69 of 71 inventory
keys are still baselined, so the map ratchets coverage without yet describing the system. Both are
recorded in `memory/map/features/codebase-map.md` §Gaps.

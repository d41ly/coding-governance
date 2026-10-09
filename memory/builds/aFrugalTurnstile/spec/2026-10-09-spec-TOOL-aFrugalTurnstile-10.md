# TOOL-aFrugalTurnstile-10 — the unattended protocol's landing rule states the scoped-then-full path

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's prompt asks for the protocol text of part E in terms: a landing that takes the scoped
bar, a full bar after the merge whose red binds the next landing through a recorded state, and what
an adopter declares. At base `memory/guides/UNATTENDED-PROTOCOL.md` §6 says the in-place close
grades the prepared merge under `GATE_FULL=1`, and §4 defines `gates-green` as the full bar having
run on the landed tip; both become false the moment a project declares a post-merge bar. This unit
implements design D12 for the protocol: one paragraph in §6, two clause edits that keep §4 and §8
true, the kit's shipped copy kept byte-identical, and the protocol's pinned size row moved by the
measured growth, in the open.

## 2. Scope (IN)

- **S1 — the §6 paragraph.** A new paragraph, the text in §4 "The text", sits in §6 immediately
  before the paragraph opening "`landed-via-lander` is the machine-checked DoD item". It states,
  in this order: where `GATE_POST_MERGE` is declared and what `local` and `ci` mean; that the close
  runs the bar the boundary decides, through the pre-push hook's `--decide`; that its green is
  recorded so the landing push is `covered`; that the full bar runs on the landed sha and its red
  binds through `refs/gov/bar-red` until a full green descends from it; and that relaxing a
  project's own stricter rule is that project's change. Observed by AC2.
- **S2 — §6's in-place sentence stays true.** "`--close` grading THAT merge under `GATE_FULL=1` and
  committing on it," gains the clause "or under the boundary's decision where a post-merge bar is
  declared,". Observed by AC2.
- **S3 — §4's `gates-green` row stays true.** Its Asserts cell gains, after "ran on the tip being
  landed", the clause "— under a declared post-merge bar (§6), the bar the push boundary decides for
  it, which a recorded green covering that tip meets —". The item name and the checker cell are
  unchanged, so check 16's item-name join reads the same set. Observed by AC3.
- **S4 — §8's `GATE_POLICY_FILE` row names the key it now carries.** Its Meaning cell reads "the file
  `INHERITED_RED`, its age bound and `GATE_POST_MERGE` are read from, …". No §8 row is added:
  `GATE_POST_MERGE` lives in the gate-env file, not in `.unattended.conf`, and check 22 joins the
  table's first cell against the kit's example conf. Observed by AC3 and AC6.
- **S5 — the shipped copy is the same bytes.** Every edit is made identically in
  `tools/unattended/PROTOCOL.template.md`, which check 10 of `check-unattended.sh` compares with the
  installed copy. Observed by AC1.
- **S6 — the pinned size row moves by the measured growth, and says why.** The
  `memory/guides/UNATTENDED-PROTOCOL.md` row in `tools/template-size-limits.txt` is set to the
  CR-stripped byte size of the edited file, still with no headroom, and its comment block gains one
  line naming this unit and the owner's prompt as the reason (§8 F1). Observed by AC4 and AC5.

## 3. Non-goals (OUT)

- The mechanism itself: the record, the `covered` decision, `--decide`, `post-merge.sh`, the binding
  ref and the close's decision are the build's code units.
- Gov's own `GATE_POST_MERGE` declaration in `.githooks/gate-env.sh`, decided at the close once the
  code exists, and the key's comment in that file.
- `UNATTENDED-STOPS.md` §10, whose "Why the order is forced" paragraph says the boundary reuses the
  close's full-green stamp. It stays true for an undeclared project, and the closing review re-reads
  it against the code.
- §13 of the protocol. Its exits are the kickoff engine's interactive stops and none of them is a
  landing; it is read and left as it is.
- The kit-version bump of the unattended kit, which happens once after the last unit.

### Edges

- **consumes-from** external — the mechanism the text describes exists only once this build's code
  units for design D2 to D11 are built, at later orders. No criterion here rests on them: each is
  textual. The closing review reads the paragraph against the built code, as M8 asks of every
  sentence naming a shipped mechanism.

## 4. Design

### Evidence

Read at base `bef97330`.

- `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` prints
  `65692 / 65692 bytes (0 under, 100.0%)`. The row's comment says the figure is PINNED at the
  committed render with deliberately no headroom (owner, 2026-09-23, `TOOL-aRepatriatedFork-11` S6
  §8 F3), so that "the next byte of growth is a line in THIS file's diff".
- `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` exits 0. The kit
  renders it with `placeholders = []` (`tools/unattended/kit.toml`), so it is a straight copy.
- `check-unattended.sh` check 22 reads only the first cell of each §8 row (`awk -F'|' 'NF>2 {print
  $2}'`), so a backticked key in a Meaning cell is not a declared key. Check 16 joins §4's item names
  and leaves the checker column unjoined.
- `TOOL-dDerivedDocket-73` (an ask, partly superseded) recorded the same class: the `gates-green` row
  went stale when the inherited-red policy changed what a close may land.
- The policy file the driver reads `INHERITED_RED` from is `GATE_POLICY_FILE`, blank meaning the
  pre-push hook's own file; design D11 reads `GATE_POST_MERGE` with that same reader.

### The text

The new §6 paragraph, verbatim, hard-wrapped at the file's width:

```markdown
**A declared post-merge bar lets a landing take the scoped bar.** `GATE_POST_MERGE` is declared
at R in the file `INHERITED_RED` is read from: `local` has the lander start the post-merge bar on
this node, and `ci` leaves it to remote CI. Under either, `--close` asks the pre-push hook's
`--decide` for the prepared merge and runs that bar: full, scoped to the base it names, or none
where a recorded green already covers the tree. Its green is recorded, so the landing push is
`covered` and runs nothing. The full bar then runs on the landed sha, and its red is BINDING:
published as `refs/gov/bar-red`, it forces FULL on every later landing that descends from it until
a full green descends from it too. A project whose own rules demand a full bar per landing relaxes
them itself.
```

The paragraph, S2's clause, S3's clause and S4's three words measure 1007 bytes together (PINNED,
measured 2026-10-09 by applying the four edits to a scratch copy of the base file). This design's
ceiling on the unit's growth is 1100 bytes.

### What this unit's gate does not check

N/A — this unit adds no gate. The two legs it moves compare the two copies to each other and the
file to its row; the protocol's own header already says a parity leg is a copy check, not a truth
check.

### Files touched (estimate)

- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/PROTOCOL.template.md`
- `tools/template-size-limits.txt`

### Rollout

The protocol ships to every adopter of the unattended kit as a copy. An adopter whose declared
`GUIDE_CAP_BYTES` sits below the new size learns so from its own hygiene gate's announcement, which
is the route the size row's comment names; gov's own cap is 98304.

### Alternatives rejected

- **Moving the mechanism into `UNATTENDED-STOPS.md`, which carries no size row, and pointing at it
  from §6.** The prompt names the protocol's landing rule, the pointer itself still grows the pinned
  file, and a landing rule split across two documents is the copy that rots. `TOOL-dFoldedVerdict-5`
  moved section 7 out because a whole section had outgrown the cap, which is not this case.
- **Paying for the growth by trimming other protocol text.** It rewords binding rules this unit has
  no mandate over, to keep a figure whose own comment says growth is decided where it can be seen.

## 5. Production-readiness checklist

- security — N/A — prose in two tracked copies and one size row; no write path.
- perf / scale — every unattended run reads about 1 KB more of the protocol.
- error / empty / loading states — N/A — no runtime behaviour.
- observability — `unattended protocol size` prints the new figure; check 10 reds on any drift
  between the copies.
- risks — the text names mechanisms built by later units; if one of them parks, the paragraph is
  false until the close's review reconciles it, which M8 owes.
- testing — direct greps, `cmp`, and the size checker run directly.
- migration — N/A — no stored state.
- user docs — the protocol is the document.

## 6. Acceptance criteria

No refusal is added, so nothing here is observed RED on a staged break; each `Red when:` names the
break the named command reports.

- **AC1** — When `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md`
  runs, it exits 0. Red when: one copy carries an edit the other lacks.
- **AC2** — When `awk '/^## 6\. Landing/,/^## 7\. /' memory/guides/UNATTENDED-PROTOCOL.md` is piped to
  `grep -F` once per token, each of `GATE_POST_MERGE`, `--decide`, `covered`, `refs/gov/bar-red`,
  `relaxes` and `under the boundary's decision` hits. Red when: a fact S1 or S2 states is missing from §6.
- **AC3** — When `grep -n '^| .gates-green. |' memory/guides/UNATTENDED-PROTOCOL.md` runs, its one row
  carries `post-merge bar`, and `grep -n '^| .GATE_POLICY_FILE. |'` over the same file shows a row
  carrying `GATE_POST_MERGE`. Red when: §4 or §8 still describes only the full bar's world.
- **AC4** — When `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` runs, it exits
  0 at `0 under`, and the figure it prints exceeds 65692 by at most 1100.
  Red when: the leg reds, headroom was added to the row, or the growth passed the design's ceiling.
  figure: 65692 is PINNED at base; 1100 is PINNED as this design's ceiling; the new size is DERIVED.
- **AC5** — When `grep -n 'TOOL-aFrugalTurnstile-10' tools/template-size-limits.txt` runs, it hits a
  comment line directly above the protocol row. Red when: the row moved with no reason beside it.
- **AC6** — When `grep -c '^| .GATE_POST_MERGE. |' memory/guides/UNATTENDED-PROTOCOL.md` runs, it
  prints 0. Red when: a §8 row was added for a key no `.unattended.conf` declares, which check 22
  would refuse against the kit's example conf.

## 7. Gates

`unattended protocol size` · `unattended kit gate` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` · `kit-placeholders self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The twelve legs after the recall pair are owed by the broad `tools/` guard the two `tools/` paths
trip, named as the build's brief asks. All run once, at the close.

## 8. Open questions

- **F1 — how does the protocol, pinned at its size with no headroom, take about 1 KB of text?**
  Options: (a) the text in §6 and the row moved to the measured size in the same commit, with a
  comment line naming the reason; (b) the mechanism in `UNATTENDED-STOPS.md` and a pointer in §6,
  the row still moving by the pointer's bytes; (c) the same bytes trimmed from other protocol text.
  (c) rewords binding rules outside the mandate. (b) still moves the row and splits one landing
  rule across two documents, against the prompt naming the protocol's landing rule. (a) satisfies
  every criterion; the row is a gate declaration, not one of the governance carriers M11 lists, and
  its comment names a diff line as the route for growth. No option trips an M3 veto, and the
  protocol text itself is the mandate (design D12). RESOLVED (agent, 2026-10-09, delegated): (a),
  with no headroom added.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the build's spec brief and design D12, with the text
  measured against the base file.

## 10. Reuse audit

The seams are the protocol's own §6, §4 row and §8 row, the kit's copy rule (`placeholders = []`,
check 10) and the existing size row with its comment block. No code is added.
`python tools/codebase-map/reuse_lookup.py "state in the unattended protocol's landing rule that a
scoped landing is safe when a post-merge full bar's red binds"` returned name-stem matches only
(`merge`, `scope`, `read_landing_commit`), so no existing seam fits beyond the sections named.
Recall named this build's prompt, brief and design; `TOOL-dDerivedDocket-73`, the earlier stale
`gates-green` row; and `TOOL-aMendedFleet-117`, an open ask that the protocol and charter landing
text describe a remote ruleset, which this unit leaves to that ask. Where the brief and the tree
disagree: the brief points at "its §13 exits" for the landing rule, and §13 holds the kickoff
engine's interactive exits, none of them a landing.

Recall terms used: `python tools/memory-recall/query.py "which records govern the landing rule
text in the unattended protocol, the charter section 1 Landing and the runbook's gate-env
declarations" --terms "landing rule push boundary scoped bar full bar post-merge binding red
gate-env declaration INHERITED_RED GATE_DOC_PATHS charter Landing protocol size"`

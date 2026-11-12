# TOOL-aNimbleMend-11 — the documents: a help page per mechanism, and the build method and the unattended protocol saying where the pass legs run and what the lane admits

**Status:** SPECCED · rev-3 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-11-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-11-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Ten units build two mechanisms and none of them writes the page a user reads or the sentence a
run is bound by. This unit writes one help page per mechanism, anchors both policy keys for the
docs leg, and changes the build method and the unattended protocol in their templates, so a run
that reads either guide learns that pass legs run after a unit pass's commit and that a red leg
may be fixed with no spec.

## 2. Scope (IN)

- **S1** — A new page, `help/pass-legs.md`, with the sections of §4, "The pass-leg page". It
  anchors `policy:pass.fast-legs` and each `script:` row its commands need. Observed by AC1, AC2
  and AC3.
- **S2** — A new page, `help/red-fix-lane.md`, with the sections of §4, "The lane page". It
  anchors `policy:bar.inline-red-fixes` and each `script:` row its commands need. Observed by AC1,
  AC2 and AC4.
- **S3** — `tools/govkit/usage.toml` gains one `[[usage]]` row per script the two pages show that
  holds none, and the existing `build_records.py#new` row gains the four flags the `red-fix` door
  takes. `help/charter.md`, which anchors that row, takes its new fingerprint. Observed by AC2.
- **S4** — `help/README.md` gains one index line per new page, and the consumer list at the head
  of `help/policy.md` gains both keys, each beside its consumer and linked to its page. Observed
  by AC5.
- **S5** — `help/reference/policy.md` is re-rendered by
  `python tools/playbook/render_playbook.py --reference`, so each key's section there reads
  `Documented on` its page. Observed by AC6.
- **S6** — The build method's M6 paragraph on gates changes by the two replacements of §4, "The
  build method", in `tools/memory-tree/BUILD-METHOD.template.md` and in its render,
  `memory/guides/BUILD-METHOD.md`. The render stays inside its 30720-byte budget. Observed by AC7.
- **S7** — The protocol's section 12 gains the paragraph of §4, "The protocol", in
  `tools/unattended/PROTOCOL.template.md` and in its render,
  `memory/guides/UNATTENDED-PROTOCOL.md`, which stay byte-identical to each other. Observed by AC8.
- **S8** — The protocol's row in `tools/template-size-limits.txt` is raised to the render's
  measured bytes, argued above the row in the `RAISED <old> -> <new>` shape. Observed by AC9.
- **S9** — One row in `memory/DECISIONS.md` records that raise. The main loop writes it in a
  `Pass: none` records commit ahead of this unit's pass commit, and the builder writes nothing to
  that file. Observed by AC9.

## 3. Non-goals (OUT)

- Any change to what a mechanism does. Every sentence here describes what units 1 to 10 built, read
  from the tree at the pass.
- The kit READMEs and the hygiene guide. Each building unit states its own mechanism there:
  `tools/run-gates/README.md`, `tools/hooks/README.md`, `tools/policy/README.md`,
  `tools/memory-tree/README.md` and `memory/HYGIENE.md` through its template.
- `tools/unattended/VERBS.template.md` and `tools/roles/SKILL.template.md`. The sentence that tells
  a main loop to act on a unit harness return is the run point's own.
- `tools/unattended/SKILL.template.md`, `tools/unattended/STOPS.template.md` and
  `tools/workflows/REVIEW-PROTOCOL.template.md`. None states that a pass is gate-free or that a
  product write needs a spec, by `git grep` at 97e0841d, so none moves.
- The charter. `[spec]` in `AGENTS.md` is rendered from the practice catalogue, and F1 asks whether
  it changes.
- The build method's own budget. M1's figure and its row are the owner's to move
  (`tools/template-size-limits.txt@48a2868a:128-135`), so S6 fits inside them.
- The M6 sentence that grants the main loop the plain bar. It keeps its rule; one clause of it is
  shortened (§4).
- A row in `memory/project/docs-undocumented.txt`. That list only shrinks, and both keys are
  anchored in the landing that adds them.
- The kit version markers, which the lander's `mint` moves once, after the last unit.

### Edges

- **consumes-from** `TOOL-aNimbleMend-1` — the two keys, their values and defaults, and the ask
  contract's outcomes. Without them neither page has a key to anchor and S4 has nothing to list.
- **consumes-from** `TOOL-aNimbleMend-2` — the pass-leg field, the rule that derives it and the
  write verb, which the pass-leg page names. Without them the page cannot say how a list is made.
- **consumes-from** `TOOL-aNimbleMend-7` — the unit harness return that tells the main loop to run
  the pass legs, which S6 and S7 point at. Without it both guides would name a run point nothing
  performs.
- **consumes-from** `TOOL-aNimbleMend-8` — what opens the lane, what the commit owes and what the
  lane does not check, which the lane page states.
- **consumes-from** external — the rest of the built tree the pages describe: the adapter and its
  run record under `tools/run-gates/`, the budget verbs, the scoped rows of the leg manifest, the
  role-gate row in the hooks kit, the `red-fix` record door with its join, and the limits verb of
  the commit grader. A page section whose subject is not in the tree at the pass is not written,
  and the builder returns the gap.
- **hands-off** external — the main loop writes S9's row before the pass, and runs the legs of §7
  at the close.

## 4. Design

### Evidence

Read at 97e0841d and re-read at 91ca33f2, which adds only records.

| Fact | Where |
|---|---|
| The render of the method measures 30659 bytes CR-stripped against a row of 30720 (PINNED, 2026-11-12). | `memory/guides/BUILD-METHOD.md`, `tools/template-size-limits.txt` |
| The method's row reserves its next movement: "Spent, it is the owner's again." | `tools/template-size-limits.txt@48a2868a:128-135` |
| M3 puts M1's own budget outside a run's delegation. | `memory/guides/BUILD-METHOD.md`, section M3 |
| The protocol's render measures 67360 bytes against a row of 67361, and its block's rule is no headroom (PINNED, 2026-11-12). | `tools/template-size-limits.txt@48a2868a:138-162` |
| A run may raise a measured-file row on four terms. | `tools/template-size-limits.txt@48a2868a:16-28` |
| The protocol template and its render are the same bytes: the pair holds no placeholder. | `diff` of the two files, empty at 97e0841d |
| M6 lines 199 to 207 of the method's template hold no placeholder, so the template's edit and the render's are the same text. | `diff` of template and render, which differs on other lines only |
| No suite pins the M6 phrases this unit moves. | `git grep -F` for `returns that need to the main loop` and `never in a child` over `tools/`, `skills/` and `.githooks/` finds the template alone |
| A file outside the memory root that spells the method's file name owes a row of the carriers list. | `memory/project/method-carriers.txt`, whose rows 38, 39 and 44 are help pages |
| A policy key anchored on a topic page renders on the reference page as `Documented on` that page. | `help/reference/policy.md@924a4b33:78-88` |
| A page command whose script has no row is the docs leg's `UNROWED`, and a placeholder in a runnable block is `RUN`. | `help/docs-leg.md`, "What it reds" |
| `script:tools/memory-tree/build_records.py#new` is anchored by `help/charter.md` at fingerprint `f857b30a` (PINNED, `docs_leg.py --fingerprints`, 2026-11-12). | `tools/govkit/usage.toml@fa34ce95:129-133` |
| A role agent's hook refuses the bare docs leg and admits its `--list` and `--fingerprints` verbs. | observed 2026-11-12 from this writer's session |

### The pass-leg page

`help/pass-legs.md`, in the shape of `help/docs-leg.md`: a bold `**What it is.**` opening, then
`##` sections. Every name, figure and output line is copied from the built tree at the pass.

| Section | States | Read from |
|---|---|---|
| What it is | after each unit pass's commit the main loop runs the declared fast legs over that pass's diff; the bar still runs once, at the close | the unit harness return and the adapter |
| How to run it | the adapter's command with its base argument, its exit code, the run record's path and keys | `tools/run-gates/pass-legs.sh`, `tools/run-gates/README.md` |
| What it prints | the two finding lines, the note line and the empty-list line, each quoted | the adapter |
| How the list is declared | the manifest field, the rule in one sentence, the report, write, apply and check verbs, and the evidence file | `tools/run-gates/pass_legs.py`, `tools/run-gates/README.md` |
| The budget | the budget, the limit and the cap as `pass_legs.py --figures` prints them, the budget verb's findings, and the bar leg that carries the gate | `tools/run-gates/pass_legs.py` |
| The scoped legs | each row of the manifest carrying a scope key, with the leg it is a form of | `tools/gate-legs.json` |
| Who runs it | the main loop only; a role agent's call is refused, and by which row | `tools/hooks/README.md` |
| The switch | the key's anchor line, then a two-row table of `on` and `off`; what a repository with no policy kit does | `tools/policy/README.md`, "A default-on switch" |
| What a run costs the bar's records | the failure record, the green stamp, the ledger rows | `tools/run-gates/README.md` |
| What it does not check | the adapter's and the budget gate's stated limits | the kit README |

The page states no second copy of a figure: where the tree prints the budget or the cap, the page
shows the command that prints it and the value it printed at the pass.

### The lane page

`help/red-fix-lane.md`, same shape.

| Section | States | Read from |
|---|---|---|
| What it is | a leg recorded red may be fixed with no spec, and its typed record follows; every other product write still needs its specced unit | `tools/hooks/README.md` |
| What opens the lane | a red row of the gate ledger, from a bar or a pass-leg run; which writers it admits; that it closes when the leg next runs green | `tools/hooks/scratch-guard.js`, its lane step |
| What the commit owes | the `Red-fix:` trailer, one leg name per line, beside `Pass: none`; what the grader does with a value that names no leg | `tools/memory-tree/routed_commits.py` docstring |
| The limits | each limit and its bound, and the verb that grades one commit | `tools/memory-tree/routed_commits.py`, `tools/memory-tree/README.md` |
| The record | the door's command and fields, that the record is the next commit, the join's command, its summary line and its hygiene check number | `memory/HYGIENE.md`, "Red-fix records" |
| The switch | the key's anchor line, then a two-row table of `on` and `off`, with what `off` does to a lane commit already in history | the grader's docstring |
| What it does not check | the lane's, the limits' and the join's stated limits, one list | the three sources above |

### Anchors, rows and blocks

- Each key is anchored once, on its page's switch section, as `help/docs-leg.md@48fe45d9:88-90`
  anchors `help.enforce`: `<!-- usage: policy:<key> <fingerprint> -->` at the end of the sentence
  that names the key. The fingerprint is the one `python tools/govkit/docs_leg.py --fingerprints`
  prints for the id.
- A script a page shows gets a `[[usage]]` row of shape `verb` in `tools/govkit/usage.toml`, in the
  form of the `build_records.py#new` row, and its anchor on the page that shows it. The rows are
  whichever of these the pages show: the adapter, `pass_legs.py`, the `join` verb of
  `build_records.py` and `routed_commits.py`. A flag that takes a value is spelled with a trailing
  `=`. A script already rowed keeps its row.
- The `build_records.py#new` row's `flags` gain the door's four new flags, read from the door's own
  argument parse. Its fingerprint then moves, so the anchor in `help/charter.md` takes the new one.
- Every fenced `bash`, `sh` or `console` block on the two pages carries a `<!-- run: no — <reason> -->`
  line above its fence. Each runs a kit by its path in gov's checkout, or carries a placeholder,
  which are the two reasons `help/docs-leg.md` gives.
- Neither page spells the build method's file name. It names the guide as "the build method", so
  no row of `memory/project/method-carriers.txt` is owed.
- Relative links only, each to a tracked path: the docs leg checks them offline.

### The build method

Two replacements in M6's paragraph that opens `**A pass runs no merge bar`, applied identically to
the template and the render.

The first replaces this text:

```text
An agent pass verifies with a fixture or a probe of its own code,
and a pass that needs a gate or suite verdict returns that need to the main loop rather than running
one; a new arm's RED-first observation is the main loop's, at the close (M8). The
```

with this:

```text
An agent pass verifies with a fixture or a probe of its own code
and returns any need for a gate or suite verdict to the main loop; a new arm's RED-first observation
is the main loop's, at the close (M8). After a unit pass's commit the main loop runs the pass legs,
and a red leg may be fixed inline: protocol §12. The
```

The second shortens one clause and drops no rule, because the same sentence already says the MAIN
LOOP judges the bar necessary:

```text
plain bar with no flag is the scoped form — at the main loop, never in a child. A pass whose check
```

becomes

```text
plain bar with no flag is the scoped form, never in a child. A pass whose check
```

The paragraph's opening sentence stands as written: a pass still runs no gate, because the pass
legs run after the pass's commit, at the main loop. M6's closed set of pass kinds stands too. An
inline fix is a commit the main loop or a product-writing role makes between passes, and the
method points at the protocol for it, as M1 requires of anything a carrier states.

**The bytes.** With both replacements the render measures 30709 bytes CR-stripped and 367 lines
(PINNED, 2026-11-12, both replacements applied in memory to the render at 91ca33f2). The first
alone measures 30730, which is over the row, so the two land together.

### The protocol

One paragraph, appended to section 12 after the paragraph that opens
`**A build pass owes a recorded BRIEF**`, in the template and in the render:

```text
**Two switches act BETWEEN passes, each a policy key that defaults on.** Under `pass.fast-legs` the
unit harness's return carries a `nextAction`, and the MAIN LOOP runs it before the next dispatch:
the declared pass legs over that pass's diff. A role agent's pass stays gate-free. Under
`bar.inline-red-fixes` a leg the gate ledger records red, the bar's or a pass leg's, may be fixed
with NO spec: the commit names the leg in a `Red-fix:` trailer beside `Pass: none`, the fix's typed
record is the next commit, and the commit grader holds the fix to its limits. Every other product
write keeps the route above; either key `off` restores it for that mechanism.
```

Each backticked name is checked against the built tree at the pass, and a name a sibling's
revision moved is written as built. The paragraph names no verb of the driver, so the Skill's verb
list owes nothing.

**The row.** The render sits one byte under its row, so the paragraph takes it past. The four
terms hold as they held for TOOL-dFoldedAudit-1 and PLAY-dOrderedCharter-3: this unit's change
takes the render past the row; the row's block reserves nothing to the owner and states no
headroom, so the new value is the measured render exactly; the movement is argued above the row;
and S9's row lands before the raise. The comment line added above the row:

```text
# RAISED 67361 -> <measured>, 2026-11-12, by TOOL-aNimbleMend-11: section 12's paragraph on the two
# switches that act between passes, which the owner's prompt asks the protocol to state. The render
# measures <measured> CR-stripped, and the row is that figure because this block's rule is no
# headroom. A run's raise, on the four terms above (memory/DECISIONS.md, TOOL-aNimbleMend-11).
```

`<measured>` is DERIVED at the pass by `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c`.

S9's row, in the shape of the row for PLAY-dOrderedCharter-3 at `memory/DECISIONS.md@f565cb8a:13`:
the unit id, that section 12's paragraph raises the protocol's no-headroom size row to its
render's measured bytes, `agent, 2026-11-12, under TOOL-aOrientedCast-23's four raise terms`, and
`Detail builds/aNimbleMend/`. `memory/DECISIONS.md` is a shared record
(`.unattended.conf@dca9e08e:417`), which is why the main loop writes it and no pass commit does.

### Rendering

The builder applies each edit to the template and to the render. For the method the edited lines
hold no placeholder, and for the protocol the pair holds none, so the render of each edited
template is the edited file. Where the pass's hook admits them,
`kit-dogfood-parity.test.sh --render` and the unattended adopter write the same bytes; the close's
parity legs are what grade it.

### What it does not check

- That a page's prose is true. The docs leg grades anchors, commands and links, and AC3 and AC4
  grade that named facts are present.
- The pages' fenced commands by running them. Each is marked `run: no`.
- The protocol paragraph against the unattended kit gate. The close's bar runs without that leg,
  by the owner's rule of 2026-11-11, so its joins over the protocol next run at a later bar.
- An adopter's render of the method. Its length is set by that install's own paths, and no gate of
  an adopter holds it to gov's row.

### Inventory

| Minted | Where | Graded by |
|---|---|---|
| page `help/pass-legs.md` | `help/` | the `docs` leg; the lexicon declares no cell for a markdown file |
| page `help/red-fix-lane.md` | `help/` | the same |
| `[[usage]]` rows for the scripts the pages show | `tools/govkit/usage.toml` | the `docs` leg's `UNROWED`, `ORPHAN` and `RESTATED` findings |

No function, key, flag or leg is minted.

### Migration

None. The pages are new, and both guides are re-rendered in an adopter by its next update.

### Rollout

No switch. The documents describe mechanisms that are on by default.

### Files touched (estimate)

- `help/pass-legs.md`
- `help/red-fix-lane.md`
- `help/README.md`
- `help/policy.md`
- `help/charter.md`
- `help/reference/policy.md`
- `tools/govkit/usage.toml`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/template-size-limits.txt`

### Alternatives rejected

- **Raising the method's budget.** Its row's block reserves the next movement to the owner and M3
  puts M1's budget outside a run's delegation, so no run may make it. The two replacements fit
  with 11 bytes to spare.
- **Stating both mechanisms in full in the method.** M1 forbids a rule stated both there and in a
  carrier it points at, and the bytes are not there. The method points, the protocol states.
- **A new protocol section 14.** Section 12 is the section about what happens between passes, and
  a new numbered section would move the method's pointer for no reader's gain.
- **Trimming the protocol to fund its paragraph.** Each of the last four movements of that row paid
  with the ceiling on the four terms, and a trim would cut a rule nobody asked to cut.
- **One page for both mechanisms.** The owner's prompt asks for a page each, and each key is
  anchored on exactly one page.
- **Listing both keys in the undocumented list.** That list only shrinks, so a new member must be
  documented in its landing.

## 5. Production-readiness checklist

- security — No write path, hook or input boundary. The lane page states what the lane does not
  check, so a reader does not take the lane for a proof that a fix was needed.
- perf / scale — The method grows 50 bytes and the protocol about 700, each read whole by a run at
  its own boundary.
- error / empty / loading states — A page section whose subject the tree does not hold at the pass
  is left out and returned as a gap, never written from this spec's reading of a sibling.
- observability — `docs_leg.py --list` names each key's page, and the size row's comment records
  its movement.
- risks — A sibling's fork resolved against its recommendation moves a name or a rule these
  documents state; the builder reads the built tree, and AC3, AC4 and AC8 grade names it holds.
  TOOL-aNimbleMend-6's F1, resolved to deny the plain bar, would also need M6's scoped-bar sentence
  changed, which is a revision of this spec before code.
- testing — AC1 to AC9 are greps and the docs leg's listing verbs. The close's `docs`,
  `help reference pages` and two size legs grade the whole.
- migration — None (§4, "Migration").
- user docs — This unit is the user docs: S1, S2, S4 and S5.

## 6. Acceptance criteria

`<help>` is the `help` directory at the repository root. The two pages are spelled through it
below because neither is tracked before this unit builds.

- **AC1** — When `python tools/govkit/docs_leg.py --list` runs, the row for
  `policy:pass.fast-legs` ends with `<help>/pass-legs.md` and a line number, the row for
  `policy:bar.inline-red-fixes` ends with `<help>/red-fix-lane.md` and a line number, and
  `python tools/govkit/docs_leg.py --list --undocumented` prints neither id.
  Red when: a key is anchored on no page, on the other page, or on two.
- **AC2** — When `python tools/govkit/docs_leg.py --fingerprints` runs, every row whose page column
  names `<help>/pass-legs.md`, `<help>/red-fix-lane.md` or `help/charter.md` carries a fingerprint that
  `grep -c "<id> <fingerprint> -->"` finds once on that page, and
  `grep -c "run: no" <help>/pass-legs.md <help>/red-fix-lane.md` prints for each page at least the
  number of fences that page opens as `bash`, `sh` or `console`.
  Red when: a page shows a command whose script has no row, an anchor holds a stale fingerprint,
  the door's new flags moved the `build_records.py#new` row and `help/charter.md` kept the old
  anchor, or a block that cannot run is unmarked.
  figure: every count is DERIVED from the pages and the verb's output at the pass.
- **AC3** — When `grep -c` runs over `<help>/pass-legs.md` for each of `pass-legs.sh --base`,
  `gate-pass-legs.txt`, `pass-legs: FINDING`, `pass_leg`, `pass_legs.py --write`,
  `pass_legs.py --budget` and `## What it does not check`, each prints at least 1, and
  `grep -c "BUILD-METHOD" <help>/pass-legs.md` prints 0.
  Red when: the page omits how to run the list, how it is declared, its budget gate or its limits,
  or spells the method's file name and so owes a carriers row.
  fixture: the seven tokens are the names units 2, 3 and 5 specify; a name the built tree spells
  otherwise is grepped as built, and the ledger says so.
- **AC4** — When `grep -c` runs over `<help>/red-fix-lane.md` for each of `Red-fix:`, `Pass: none`,
  `gate-ledger.tsv`, `new red-fix`, `join red-fix`, `--red-fix-limits` and
  `## What it does not check`, each prints at least 1, and `grep -c "BUILD-METHOD"` over it
  prints 0.
  Red when: the page omits what opens the lane, what the commit owes, the record, the limits or
  what the lane does not check.
  fixture: as AC3, for the names units 8, 9 and 10 specify.
- **AC5** — When `grep -c -e "pass-legs.md" -e "red-fix-lane.md" help/README.md` runs it prints 2,
  and `grep -c -e "pass.fast-legs" -e "bar.inline-red-fixes" help/policy.md` prints at least 2,
  each match on a line above the sentence opening `Every other key has no consumer yet`.
  Red when: a page is not indexed, or the policy page still counts a key among those with no
  consumer.
- **AC6** — When `grep -A1 -F "pass.fast-legs" help/reference/policy.md` and
  `grep -A1 -F "bar.inline-red-fixes" help/reference/policy.md` run, the line under each key's
  heading reads
  `Documented on` followed by a link to S1's page, its text the page's path from the repository
  root and its target that page one folder up, and the same for S2's page.
  Red when: the reference page was not re-rendered after the anchors landed, so it still carries
  the key's own summary and anchor, which the docs leg reads as anchored twice.
- **AC7** — When `tr -d '\r' < memory/guides/BUILD-METHOD.md | wc -c` runs it prints at most 30720,
  and `grep -c "runs the pass legs" memory/guides/BUILD-METHOD.md tools/memory-tree/BUILD-METHOD.template.md`
  prints 1 for each file, as does `grep -c "fixed inline: protocol §12"`, and
  `grep -c "never in a child"` over both still prints 1 for each.
  Red when: the sentence landed in one file only, the first replacement landed without the second
  and the render reads 30730, or the scoped-bar rule was cut rather than shortened.
  figure: 30709 is PINNED, both replacements applied in memory to the render at 91ca33f2 on
  2026-11-12; 30720 is the row.
- **AC8** — When `cmp memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/PROTOCOL.template.md`
  runs it prints nothing and exits 0, and `grep -c` over the render prints 1 for each of
  `Two switches act BETWEEN passes`, `pass.fast-legs`, `bar.inline-red-fixes` and `nextAction`,
  with the first match on a line between the headings `## 12.` and `## 13.`.
  Red when: the render was edited and the template was not, or the paragraph landed outside
  section 12, where the method's pointer does not find it.
- **AC9** — When `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c` runs, the figure it
  prints equals the second field of the row `grep -P '^memory/guides/UNATTENDED-PROTOCOL\.md\t' tools/template-size-limits.txt`
  prints, `grep -c "RAISED 67361 -> " tools/template-size-limits.txt` prints 1 on a line naming
  this unit, and `git log --format=%H -1 -S"TOOL-aNimbleMend-11" -- memory/DECISIONS.md` names an
  ancestor of the commit that moved the row.
  Red when: the row keeps headroom, the movement is not argued in place, or the raise landed with
  no decision row before it.
  figure: the row's new value is DERIVED at the pass; 67361 is PINNED at 97e0841d.
  permission: the decision row is the main loop's write, in a `Pass: none` commit before the pass.

## 7. Gates

`docs` · `help reference pages` · `help page commands` · `policy fixtures` · `build-method size` · `unattended protocol size` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once, after the last unit. `docs` and `help reference pages` grade the
pages, the anchors and the re-render, and `help page commands` reads the `run: no` marks.
`policy fixtures` guards `help/policy.md` and is in the held tier. The two
size legs grade S6 and S8, under `budgets.enforce`, which reads `warn` in this repository, so a
breach there prints and does not refuse: AC7 and AC9 are the checks that hold the figures. The
unattended kit gate also reads the protocol, and the close runs without it. The kit epoch and
version legs expect the lander's `mint`.

No arm is added or moved. The docs leg's own plants already stage a stale anchor, an unrowed
command and an unmarked block.

## 8. Open questions

- **F1 — Does the charter's `[spec]` line change?** It reads "every product-code unit commits its
  spec first". An inline fix is product code with no spec, and the charter is the level every
  other document yields to.
  - **A, leave the charter.** A lane fix is no unit, so the line holds as written. The protocol's
    new paragraph is where a run reads the exception, and the owner's prompt, recorded under this
    build's `prompts/`, is the owner's own word for it. No governance carrier beyond the two the
    prompt names is touched.
  - **B, amend the practice.** The `[spec]` practice in the practice catalogue gains a clause
    naming the lane, and the charter is re-rendered. Every reader meets the exception at level 0.
    It changes a governance carrier the prompt did not name, which the build method's veto 2 makes
    an owner turn, and the charter's size row was set to its measured bytes with no headroom.
  - Recommendation: A. B is the owner's to order, and the wrap-up is where it is offered.
  RESOLVED (agent, 2026-11-12, delegated): A, leave the charter. B changes a governance carrier the prompt did not name, which is an owner turn; it is offered at the wrap-up.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · AC6 names the two help pages by their scope items, since a path the unit has not built yet is an untracked citation to the spec-token check.
- rev-3 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

This unit extends seams that exist and adds no mechanism. `python tools/codebase-map/reuse_lookup.py
"a help page documents a policy key and a guide template is edited where it is rendered from"`
returned name-stem neighbours only, `read_policy_value`, `derive_template_rel` and `read_renderers`
among them, and none is a writer of a help page or a guide, so the seams were read from source.
The page seam is the docs leg's anchor and `[[usage]]` row, as `help/spec-audit.md` and
`help/measure-legs.md` use them for three keys and two scripts. The reference page is rendered by
`tools/playbook/render_playbook.py`, which already prints `Documented on` for a key a topic page
anchors. The method is edited in `tools/memory-tree/BUILD-METHOD.template.md` and the protocol in
`tools/unattended/PROTOCOL.template.md`, the two sources the kit descriptors render from
(`tools/memory-tree/kit.toml@fdae4a71:77-79`, `tools/unattended/kit.toml@326d74c4:78-80`). The size
row is raised on the four terms `tools/template-size-limits.txt` states. Recall returned
TOOL-dFoldedAudit-18, the help page for three policy keys and two verbs, which is the shape S1 and
S2 follow; TOOL-dSafePassage-13, the docs leg; and TOOL-dCountedConsumers-1, which owns the
consumer list S4 extends and records that a second anchor for a key is the leg's `TWICE` finding.
A `git grep` for the method's template under the build records found TOOL-dFoldedAudit-1, which
edited both guides in their templates and raised the protocol's row on those terms with a decision
row written by the main loop: the precedent S6 to S9 follow. For a second route to any of these,
no existing seam fits and none is built.

Where the records and the source disagreed: the owner's prompt says both guides "state that no
gate runs in a pass and that every product change is specced". The method states the first in M6
and the second as M2's hard floor for a unit; the protocol states neither in those words, and its
section 12 is where the pass order and the dispatch refusal are stated, so the paragraph lands
there.

Recall terms used: `python tools/memory-recall/query.py "how was the build method or the unattended
protocol edited in its template and its size row raised, and how does a help page anchor a policy
key" --terms "BUILD-METHOD template render PROTOCOL template size row raise four terms help page
anchor usage fingerprint docs leg policy key"`

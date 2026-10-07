# TOOL-aGraftedHelix-47 — check-arms.py discovers a refusal that is not a fail call, and every one it finds is armed or waived with a printed reason

**Status:** CLOSED · rev-3 · 2026-10-07 · node a · Tier-2 · base e1f4d8c0 · streams tooling · order 28 · closes TOOL-aDeferredBar-8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-47-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-47-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md](../build/2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md) | journal | TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 TOOL-aGraftedHelix-33 TOOL-aGraftedHelix-34 TOOL-aGraftedHelix-35 TOOL-aGraftedHelix-36 TOOL-aGraftedHelix-37 TOOL-aGraftedHelix-38 TOOL-aGraftedHelix-39 TOOL-aGraftedHelix-40 TOOL-aGraftedHelix-41 TOOL-aGraftedHelix-45 TOOL-aGraftedHelix-46 |
| [2026-10-07-prompt-TOOL-aGraftedHelix-45-1-spec-brief.md](../prompts/2026-10-07-prompt-TOOL-aGraftedHelix-45-1-spec-brief.md) | journal | TOOL-aGraftedHelix-45 TOOL-aGraftedHelix-46 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/check-arms.py` grades a refusal only when its script defines `fail() {` and calls
`fail <n> "`. Every other refusal is invisible to it. That covers an adopter's `--check` that prints
a reason and exits 1, and a gate's delegated dispatch block that prints a module's capture and sets
`status=1`. This unit adds a second discovery signature for those refusals, behind a conf switch.
It lands with every site it finds either armed by a positive assertion or waived in the pin with a
reason the gate prints. It closes the open ask `TOOL-aDeferredBar-8`, and the wider version the owner
adopted on 2026-10-07, check 24's block included.

## 2. Scope (IN)

- **S1** — Signature 2. With `ARMS_REFUSALS="graded"` in `.memory-tree.conf`, `check-arms.py`
  discovers a REFUSAL SITE by the rules of §4 "The site and its reason". It reads every tracked
  `*.sh` that is not `*.test.sh` and does not sit under the memory root (§8 F1). A script holding a
  site is a gate beside the helper-defined ones, and its sibling test is `<stem>.test.sh` as today.
  A site is `reasoned` when a literal message is read for it. Its signature comes from that message
  through the existing `message_of` and `signature`. A site is `delegated` when its block prints
  only interpolations, or when its exit is conditioned on a command. Its signature is then the text
  of an `# arm-signature:` marker in its block (§8 F2). A line whose block prints nothing is
  `unreasoned` and is not a site. Observed by AC1, AC2 and AC3.
- **S2** — Keys, pins and reasons. A site is keyed by its gate, its kind and its occurrence. The kind
  is `exit` for an `exit 1` and `status` for a `status=1` assignment. The occurrence counts the sites
  of that gate and kind sharing its signature, so an inserted refusal does not re-key the rows below
  it. A pin row of either kind carries a fifth tab-separated field, its reason. `--check` refuses a
  row of that kind whose reason is empty or `REASON-OWED`, and prints one `waived` line per such row
  on every run. `--emit-pin` writes `REASON-OWED` into that field. With the switch off, rows of these
  kinds are not read, and the OFF line counts them. A script found only by signature 2 that has no
  sibling test is not an error while every one of its sites is pinned. Observed by AC1 and AC5.
- **S3** — Announcements. With the switch on, `--check` prints one census line on every run, naming
  sites, scripts, armed, waived and unreasoned counts. With it off, `--check` prints one OFF line
  naming the key and the number of sites it is not grading. `--report` prints every signature-2 site
  with its kind, its class, the line its reason or marker was read from, and its state. It also
  prints one `UNREASONED <path>:<line>` row per near-miss. Observed by AC1 and AC3.
- **S4** — The red, before any arm. With the switch on in the working tree, and before S5 and S6 add
  any arm or pin, `--check` exits 1 and names check 24's `status=1` site in
  `tools/memory-tree/check-memory-hygiene.sh`. Observed by AC2.
- **S5** — Check 24's block is armed. Its block carries the marker
  `# arm-signature: and this tree does not honour it`, text `row_grammar.py --check-rotation` prints
  on its `cut` refusal. The hygiene suite gains a check 24 engine arm in the shape of the check 28
  arm `TOOL-aGraftedHelix-13` added. A scratch repository declaring `ROTATION_MODE="cut"` commits a
  clean archive on `main`, and a branch adds an archive id that the live index also holds. The
  branch run reds the engine with output carrying the marker text, and `--offenders` keys `check 24`
  alone. Per §8 F4's recommendation the block also prints its capture on a green run, as blocks 20,
  27 and 28 do, and the arm asserts the clean run prints `rotation-mode: clean (`. The suite's
  assertion floor rises by the block's executed count. Observed by AC4.
- **S6** — Every other site is armed or waived, by the rule of §4 "Arming and waiving". A site is
  armed where its sibling suite already has an arm that drives that refusal. For a reasoned site,
  that arm's assertion is made to carry the site's whole signature. For a delegated site, the block
  gains a marker naming text the arm already asserts. The UNWIRED refusal of
  `tools/unattended/adopt-unattended.sh`, the instance `TOOL-aDeferredBar-8` was filed for, is armed
  this way. Every remaining site is pinned in `memory/project/unarmed-branches.txt` with its reason.
  An arm is lengthened only in a suite inside this unit's dispatched write set, the memory-tree and
  unattended kits' (rev-2). A driving arm in another kit's suite is waived with a reason naming that
  arm's line, because lengthening it moves that kit's shipped bytes and version. Observed by AC5
  and AC6.
- **S7** — Configuration. `.memory-tree.conf` declares `ARMS_REFUSALS="graded"` with a comment naming
  this unit. Its `ARMS_FLOORS` line is re-emitted by `--emit-floors`, so every discovered gate is
  floored. `tools/memory-tree/.memory-tree.conf.example` ships the key blank, and
  `tools/memory-tree/kit.toml` lists it in `optional_keys`. Any value other than blank or `graded`
  is refused by name. Observed by AC7 and AC8.
- **S8** — Documentation. The module docstring of `check-arms.py` states signature 2, the marker, the
  reason field, the switch, and what it does NOT check (§4 "Gaps it leaves"). The pin file's header
  documents the fifth field and names `ARMS_REFUSALS` as the switch under which rows carrying it are
  read. `tools/memory-tree/README.md` updates its `check-arms.py` row and gains
  an "Upgrading to" section naming the key and the `--emit-pin` step. §8 F3 resolved (c) under
  delegation (rev-3), so the meta-gate paragraph of `tools/memory-tree/HYGIENE.template.md` is NOT
  rewritten: the template and `memory/HYGIENE.md` move by the version marker alone. Observed by AC9.
- **S9** — The class record `memory/gotchas/a-grep-for-a-word-is-a-presence-probe.md` names the gate.
  Its "Documented check, no machine gate" paragraph is rewritten to say the delegated dispatch block
  is graded by `python tools/memory-tree/check-arms.py --check` under `ARMS_REFUSALS`. Observed by
  AC10.
- **S10** — The memory-tree kit's version moves once, after the unit's last edit to a shipped file,
  in every carrier `tools/check-kit-versions.sh` pairs. So does any other kit whose shipped script
  gained a marker under S6. The map's generated artifacts are re-rendered for the functions S1 adds.
  Observed by AC11.

## 3. Non-goals (OUT)

- **Python refusals.** Signature 2 keeps signature 1's `*.sh` population. A Python raise belongs to
  the open ask `TOOL-aSurfacedLexicon-21`.
- **Exit codes other than 1, and `return 1`.** An `exit 2` in this tree is a usage or precondition
  refusal taken before any verdict, and the ask names exits of 1.
- **Hooks without a `.sh` suffix.** `.githooks/pre-push` and its siblings stay outside, as they are
  outside signature 1.
- **Unreasoned exits.** A site whose block prints nothing cannot be armed by text. It is counted and
  listed, never graded. Making each one print a reason is a follow-up.
- **Arming every waived site.** S6 arms where an arm already drives the refusal, and S5 writes the one
  new fixture. New fixtures for the rest, and sibling suites for the seven test-less scripts of §4,
  drain the pin later.
- **Signature 1's keying.** Fail rows stay keyed by ordinal; `TOOL-aDeferredBar-13` owns that. Signature
  2 keys by signature from its first row.
- **The other delegated blocks' green prints.** Blocks 13-16, 17-19, 20, 26, 27 and 28 already print
  their capture on a green run. Only check 24's block swallows it (§8 F4).
- **A marker's truthfulness.** Nothing checks that a callee prints its marker text. An arm asserting
  that text over a callee that never prints it fails when its suite runs.
- **No new leg.** Signature 2 lives in the `harness arms` leg it extends, the cheaper unit the class
  record `a-new-leg-trips-a-growing-set-of-meta-gates` names.
- **Whole suites are not run here.** The owner runs the kit suites by hand from the merged tree
  (ruling of 2026-10-06). A pass runs slices and `--selftest`.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-13` — the check 28 engine arm and its fixture shape, which S5
  copies for check 24 and S6 reads as the arm a check 28 marker names.
- **consumes-from** `TOOL-aGraftedHelix-14` — the check 27 engine arm, which S6 reads as the arm a
  check 27 marker names.
- **hands-off** external — Python refusal sites, to the open ask `TOOL-aSurfacedLexicon-21`.
- **hands-off** external — the waived set, which drains as later units arm its rows; the pin is
  shrink-only.
- **hands-off** external — the whole hygiene suite's run over S5's arm, which is the owner's manual
  run from the merged tree.

## 4. Design

### The population (§8 F1)

Signature 1 is unchanged. A script that defines `fail() {` and calls `fail <n> "` is discovered as
today, and its fail branches are keyed and pinned as today. Signature 2 adds a second kind of
branch, and a second way to be a gate. It reads every tracked `*.sh` that is not `*.test.sh` and does
not sit under `MEMORY_ROOT`. The memory root is excluded because a build record can hold a repro
script, which is a frozen record and not a gate; the tree holds one today. A script signature 1
already discovers gains its signature-2 sites as further branches of the same gate.

### The site and its reason

Each line of a population script is read in this order.

1. **Candidate.** The line's quoted spans are blanked and its trailing comment is cut. It is a
   candidate when what is left carries `exit 1` as a word, or assigns `status=1`. A comment line, a
   line inside a here-document body, the `fail() {` definition and a line carrying a `fail <n> "`
   call are never candidates. The last rule keeps a line signature 1 owns from becoming a second
   branch.
2. **Reason.** The first rule that applies decides.
   - (a) A print before the exit on the same line, `echo` or `printf` followed by a double-quoted
     literal. Its message, cut at the first unescaped closing quote by `message_of`, gives the
     signature by `signature`. A signature under the existing 12-character floor makes the site
     `delegated` instead of raising.
   - (b) A print on the same line carrying no literal, such as `printf '%s\n' "$rotm"; status=1`.
     The site is `delegated`.
   - (c) An exit conditioned on a command: `<command> || exit 1`, or `|| { …; exit 1; }`, whose left
     side is not a `[`, `[[` or `test` condition. The site is `delegated`, because the callee prints
     the reason.
   - (d) Otherwise the BLOCK is walked upward. The walk reads lines at the site's indentation or
     deeper, skips comments and the closing-quote line of a multi-line `printf` format, and stops at
     the first blank or shallower line. The topmost print in that span decides, as in (a) or (b).
   - (e) No print found: `unreasoned`, which is not a site.
3. **Marker.** A delegated site's arm signature is the text of the nearest `# arm-signature: <text>`
   comment inside its walked block, trimmed, at least 12 characters. With none, the site cannot be
   armed and its pin key is its own source line, whitespace-squeezed. A marker on a reasoned site is
   refused by name, because a declared signature beside a derived one is two answers to one
   question. A marker that no delegated site reads is refused by name too, so a marker cannot outlive
   its site silently.

| Site at `e1f4d8c0` | Rule | Class | Signature |
|---|---|---|---|
| `adopt-unattended.sh`, the SKILL template refusal | (a) | reasoned | `unattended: SKILL.template.md is missing from the kit at` |
| `adopt-unattended.sh`, the UNWIRED refusal's lone `exit 1` | (d) | reasoned | `hook is UNWIRED —`, from the topmost echo of its block |
| `check-memory-hygiene.sh`, check 24's `printf … "$rotm"; status=1` | (b) | delegated | its marker, from S5 |
| `check-memory-hygiene.sh`, check 26's `[ "$_tarc" -ne 0 ] && status=1` | (d) | delegated | none until marked |
| `adopt-lexicon.sh`, `write_skill \|\| exit 1` | (c) | delegated | none until marked |

The UNWIRED row is why the ask's own instance reads unarmed today. `message_of` stops at the quote
inside `${SJ#"$ROOT"/}`, so the signature is `hook is UNWIRED —`. The arm in its sibling suite
asserts `gate-guard hook is UNWIRED`, which does not contain it. S6 makes the assertion carry it.

### Keys, the pin and the reason field

A signature-2 branch is keyed `(gate, kind, occurrence)`, and its pin row has five fields:

```
gate<TAB>kind<TAB>occurrence<TAB>signature<TAB>reason
```

`kind` is `exit` or `status`. `occurrence` is 1 unless two sites of one gate and kind share a
signature. A numbered fail row keeps its four fields, and a row of kind `exit` or `status` must carry
five. The reason is the LAST field, so an empty one shifts nothing, and it is refused by name rather
than read as absent (class `empty-field-collapses-unless-it-is-last`). Every existing pin rule holds
for the new rows: shrink-only, a pinned site that is armed reds, a row naming no live site reds, and a
site pinned in two files is refused. Signature-2 rows go in the central file
`memory/project/unarmed-branches.txt`, which gov ships to nobody.

`--check` prints, per waived row, one line in this shape:

```
check-arms: waived <gate>:<line> <kind> — <reason>
```

### The switch and what prints

`ARMS_REFUSALS` is read from `.memory-tree.conf`. Blank or absent is OFF, `graded` is ON, and any
other value is refused by name. Discovery scans in both states, because the OFF line's count is that
state's liveness assertion: a skip announces how much it skipped.

```
check-arms: refusal signature — <S> site(s) in <G> script(s): <A> armed, <W> waived; <U> unreasoned line(s) not graded
check-arms: refusal signature OFF — ARMS_REFUSALS is not `graded`, so <S> refusal site(s) outside fail() go ungraded and <R> pin row(s) of kind exit or status were not read
```

### Why it ships dark

`check-arms.py` ships to every memory-tree adopter as `engine`. Switched on everywhere, an adopter's
next upgrade would red `harness arms` on every reasoned exit in their own scripts. That is the
adopter contract change the class record `shipped-checker-edit-is-an-adopter-contract-change`
describes, and its remedy is a conf key. Charter §1 lands Tier-2 behaviour default-OFF as well. Gov
turns the switch on in the same unit, so its own tree is graded from the landing commit.

### The census at the base

PINNED: measured on node `a`, 2026-10-07, at `e1f4d8c0`, by a read-only probe in the session
scratchpad. It implements rules 1 and 2 above without the here-document and quoted-span refinements
of rule 1. AC3 re-derives every figure with `--report`.

| Measure | Count |
|---|---|
| candidate lines | 173 |
| reasoned sites | 116 |
| delegated sites | 39 |
| unreasoned lines, not sites | 18 |
| scripts holding a site | 25 |
| of those, with no sibling test | 7 |
| reasoned sites armed today under the arm rule | 0 |

The seven scripts with no sibling test are `tools/check-kit-versions.sh`,
`tools/drift-audit/adopt-drift-audit.sh`, `tools/lexicon/adopt-lexicon.sh`, `tools/lib/render-doc.sh`,
`tools/memory-recall/adopt-memory-recall.sh`, `tools/memory-tree/adopt-memory-tree.sh` and
`tools/runlog/adopt-runlog.sh`. The hygiene engine holds nine sites. Seven are delegated blocks:
checks 13-16, 17-19, 20, 24, 26, 27 and 28. Two are reasoned: the empty `READINESS_ROWS` refusal and
the empty-population report. `check-arms.py --check` ran in 1.4 s at the base, against a leg ceiling
of 300 s.

### Two association rules, measured

Two rules for reading a site's reason were run over the same tree. Rule S walked a block only for a
standalone `exit 1` or `status=1` line. Rule W, the one above, walks every site with no print on its
own line. What would make each lose was written down first. S loses if it leaves a delegated block
the owner named undiscovered. W loses if its walk attaches a site to a message that is not its
reason.

- **Rule S found 110 sites and lost.** It left four of the hygiene engine's seven delegated blocks
  undiscovered: checks 13-16, 17-19, 20 and 26. It also missed six `rm -f …; exit 1` refusals in
  `tools/unattended/adopt-unattended.sh`.
- **Rule W without rule (c) made six walks longer than 12 lines.** Three of those were
  `<command> || exit 1` sites whose reason is their callee's, and one of them took an unrelated
  message from 26 lines above. Rule (c) classes those as delegated without a walk. Three long walks
  remain, one each in `tools/push-main.sh`, `tools/lib/lib-selftest.sh` and
  `tools/run-gates/run-gates.sh`.

`--report`'s reason-line column is the defence against a false association: the builder and a
reviewer read which line each reasoned site took its signature from.

### Refinements measured at the build (rev-2)

Rules 1 to 3 above hold. The build refines how each is read, and every refinement was measured over
the real tree at `4fc54f77`, after units 45 and 46 landed.

- **Quoted spans carry across lines.** The reader tracks single, double and `$'…'` quotes, a command
  substitution inside double quotes, comments and here-document bodies across the whole file. A line
  that opens inside a quote belongs to the statement above it, so check 20's `' "$rowg"; status=1`
  takes its statement's print and indentation. A script that ends inside a quote or a here-document
  by this reading is refused by name, because reading the rest as clean would hide its sites.
- **Rule (a) takes the LAST print before the exit in its statement**, not the first: the first is
  often the data a pipe tests, as in `echo "$x" | grep -q y || { echo "…"; exit 1; }`. Its first
  argument may be double-quoted, single-quoted, `$'…'` or bare. In a printf format a conversion
  counts as an interpolation, a positional or special parameter such as `$0` counts as one in any
  print, and `\"`, a backslash-escaped backtick and `\\` are read as the characters the shell prints.
- **Rule (c) reads its left side from the raw line.** A command whose words are all quoted is blank
  once quotes are masked, so `"$PY" "$KIT_DIR/scaffold_lexicon.py" "$CONF" || exit 1` fell through
  to the walk and took an unrelated message.
- **Rule (d)'s walk also stops at another site**, and it prefers the topmost print at the
  statement's OWN indentation over one nested deeper in an earlier compound. Measured against the
  rev-1 walk: six associations moved and every one moved to its own message. Examples are
  `tools/push-main.sh` line 763, which took line 718's message across a whole loop and now takes
  line 762's, and `tools/memory-recall/adopt-memory-recall.sh` line 175, which took line 163's and
  now takes 172's DRIFTED line. Two walks stay long. The `tools/run-gates/run-gates.sh` wall
  refusal reads its block's capture print and is delegated. The `tools/lib/lib-selftest.sh` probe
  exit reads an `echo "----"` and is delegated. Both are pinned by source line.
- **A marker belongs to the first site below it**, with no other site between them.
- **`--emit-pin` writes refusal rows only under `graded`**, because under OFF they would not be read.

The census at the build, re-derived by `--check` and `--report`: 158 sites in 26 scripts, 118
reasoned and 40 delegated, and 10 unreasoned lines. The sites are within 2 per cent of the PINNED
census. The unreasoned lines are 44 per cent under it, because a here-document body and a quote
continuation are no longer candidates. The walk refinements moved one site from reasoned to
delegated and left the unreasoned count where it was. The acceptance ledger records both totals.

### Arming and waiving

S6 applies one rule per site, in the order `--report` lists them.

- **Arm** when an arm in the sibling suite already drives the refusal path. For a reasoned site, that
  arm's assertion is made to carry the whole signature `--report` prints, never a prefix (class
  `arm-literal-strands-on-message-edit`). For a delegated site, the block gains a marker naming text
  the arm already asserts and the callee prints on its refusal path.
- **Waive** every other site: pin it with a reason saying why no arm reaches it. Two reasons cover
  most rows: no sibling suite exists for the script, or no arm in it stages that refusal's
  precondition. A reason names the precondition when it is the second.
- S5's check 24 arm is the one new fixture. The waived count is DERIVED at the build and recorded in
  the acceptance ledger, and the floors follow it.

The check 24 fixture's archive must satisfy checks 9 and 10, or `--offenders` keys them too and the
arm's "check 24 alone" assertion reds. The suite's rotation block of `TOOL-aRelaxedShard-4` already
builds a rotated archive those checks accept; S5 takes its shape.

### Selftest arms

AC1 reads these labels from `check-arms.py --selftest`. Each builds its own fixture with the switch
set as the label says.

1. `S1: a script with no fail() helper is discovered by a reasoned exit 1`
2. `S1: a multi-line block's reason is its topmost print`
3. `S1: a capture-print status=1 is a delegated site signed by its marker`
4. `S1: a command-conditioned exit 1 is delegated, not reasoned`
5. `S1: an exit 1 whose block prints nothing is counted unreasoned, not a site`
6. `S1: exit 1 inside quotes, a comment or a here-document body is not a site`
7. `S1: a *.test.sh and a script under the memory root are not discovered`
8. `S1: a line carrying a fail call is signature 1's alone`
9. `S1: a marker on a reasoned site is refused`
10. `S1: a marker no delegated site reads is refused`
11. `S2: a waived row prints its reason`
12. `S2: an exit row with an empty reason is refused, and so is REASON-OWED`
13. `S2: a refusal inserted above a pinned site does not re-key its row`
14. `S2: a test-less script passes with every site pinned, and one unpinned site names the missing test`
15. `S3: the switch off grades no site, reads no exit row, and prints the OFF line`
16. `S7: a switch value other than blank or graded is refused by name`

### Inventory

| Identifier | Where | Kind |
|---|---|---|
| `ARMS_REFUSALS` | `.memory-tree.conf` and the kit's example conf | conf key; no declared naming cell grades one |
| `scan_refusal_sites` | `check-arms.py` | function, cell `py.function` |
| `derive_refusal_reason` | `check-arms.py` | function, cell `py.function` |
| `read_arm_marker` | `check-arms.py` | function, cell `py.function` |
| `scan_shell_lines`, `extract_print_message`, `check_refusal_switch`, `check_refusal_sites` | `check-arms.py` | functions, cell `py.function`, rev-2 |
| `run_rot24_gate` | the hygiene suite | shell function, the check 24 fixture's runner, rev-2 |
| `# arm-signature: ` | a comment in a gate's block | marker grammar |
| `exit`, `status` | pin column 2 | pin row kinds |
| `REASON-OWED` | pin column 5 | the placeholder `--emit-pin` writes and `--check` refuses |
| the census, OFF and `waived` lines | `--check` stdout | output shapes |

`lexicon.py --suggest` returned `scan` over `find` for the first function and accepted the other two.
Any further helper is named through `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
No leg, gate file or gotcha record is minted. The three functions enter the map's symbol tier.

### Files touched (estimate)

- `tools/memory-tree/check-arms.py`
- `memory/project/unarmed-branches.txt`
- `tools/memory-tree/check-memory-hygiene.sh`, check 24's block and any delegated block S6 marks
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/unattended/adopt-unattended.test.sh`, the UNWIRED assertion
- the other sibling suites whose existing arms S6 lengthens, each named in the acceptance ledger:
  rev-2 adds `tools/memory-tree/check-verdict-epoch.test.sh` and
  `tools/unattended/check-pass-order.test.sh`
- every carrier `adopt-memory-tree.sh --render` re-renders at the bumped version, rev-2:
  `memory/TEMPLATE-SPEC.md` and two guides beside `memory/HYGIENE.md`
- `.memory-tree.conf`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/README.md`
- `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md`, the version marker only, because
  §8 F3 resolved (c)
- `memory/gotchas/a-grep-for-a-word-is-a-presence-probe.md`, and `memory/gotchas/INDEX.md` if the
  generator moves it
- `memory/map/generated/symbols.json`, and whatever else `gen_map.py --write` moves beside it
- every version carrier `tools/check-kit-versions.sh` pairs for the memory-tree kit, and for any kit
  whose shipped script gained a marker

### Rollout

One pass, in this order, each step verified by its own criteria before the next.

1. S1 to S3 in `check-arms.py`, with the selftest arms, then AC1.
2. The switch set to `graded` in the working tree, then AC2, before any arm or pin exists.
3. S5, then AC4.
4. S6, arms first and pins after, then AC5, AC6 and AC3.
5. S7's floors, re-emitted once no arm or pin moves again, then AC7 and AC8.
6. S8 and S9, then AC9 and AC10.
7. S10 last, then AC11.

Unit `TOOL-aGraftedHelix-45` (order 26) edits shipped shell before this unit builds. The census is
therefore taken after it lands, and a site it adds is discovered here like any other.

### Gaps it leaves, stated

- A reason is prose. Nothing checks that it is true.
- A marker's text is trusted until the suite holding its arm runs.
- The waived set is large: the census puts it near 130 rows. It is DERIVED at the build.
- Python refusals and hooks without a `.sh` suffix stay outside the population.
- Unreasoned exits are listed and never graded.
- A false association by the walk reads as a reasoned site with the wrong signature. It can only be
  armed by asserting that wrong text, and the reason-line column is the only defence.
- The walk reads indentation, so a block indented against its own nesting can end early or late.

### Alternatives rejected

- **Rule S** for the reason walk, measured above.
- **Ordinal keys for signature-2 rows**, as signature 1 uses. Every inserted refusal would re-key the
  rows below it across a waived set of about 130, the class `TOOL-aDeferredBar-13` records.
- **Sidecar pin files beside each shipped script.** Eight kit directories would each gain a shipped
  file their descriptor must claim, a new public surface (M3 veto 2). Their rows would also reach
  adopters who run the switch off.
- **A whole-script waiver row.** A refusal added to that script later would be waived silently,
  widening the surface the row was written to narrow.
- **The reason as a comment above its row**, the sidecar's convention today. A comment is not data,
  so the gate cannot print it.
- **Signature 2 on in every tree at the next kit version**, with no switch, for the reason "Why it
  ships dark" gives.

## 5. Production-readiness checklist

- security — No write path and no new input. The gate reads tracked shell and the pin as today. A
  marker or a reason is author text the gate prints, and nothing executes it.
- perf / scale — One more pass over the tracked shell the gate already reads, and up to 25 more
  sibling suites read as text. `--check` took 1.4 s at the base (PINNED, node `a`), and the leg's
  ceiling is 300 s.
- error / empty / loading states — With the switch on and no site found, the census line prints
  zeros rather than nothing. A missing sibling test stays a named failure unless every site is
  pinned. A malformed row names its file and line.
- observability — The census line on every run, the OFF line when off, one `waived` line per waived
  row, and `--report`'s reason-line column and `UNREASONED` rows. The leg's log grows by one line per
  waived row.
- risks — The pin grows from zero rows to the waived count, every row with a reason. `memory/HYGIENE.md`
  says its working state is empty, and with F3 resolved (c) it keeps saying so until the owner takes
  the rewrite; the pin's own header and `--report` state the live population. The switch keeps every
  adopter's verdict where it was.
- testing — The `--selftest` arms of §4 (AC1), the red observed before any arm (AC2), and check 24's
  engine arm on a staged break (AC4).
- migration — None for data. An adopter reads the README's upgrade section; the example conf ships the
  key blank.
- user docs — The docstring, the pin header, and the kit README row and its upgrade section. The
  HYGIENE carrier is the owner's turn, F3. No `help/` page, because the kit is internal.

## 6. Acceptance criteria

A slice is the hygiene suite's prologue plus the block a criterion names, run from the session
scratchpad under a name that is not a suite name, with `HERE` pinned to the kit dir under test. A
staged break edits a scratch copy of the kit dir, or a scratch clone under a short directory in
%TEMP%, and never a tracked file.

- **AC1** — When `python tools/memory-tree/check-arms.py --selftest` runs at the pass commit, it exits
  0 and prints `arm ok` for every label §4 "Selftest arms" lists, and no `arm FAIL`.
  Red when: in a scratch clone, `scan_refusal_sites` is edited to return no site; the discovery arms
  then print `arm FAIL` and the exit is 1.
  fixture: the selftest builds its own git fixtures under %TEMP%.
- **AC2** — When `python tools/memory-tree/check-arms.py --check` runs over the working tree after S1
  to S3, with `ARMS_REFUSALS="graded"` and before S5 and S6 add any arm or pin, it exits 1. One line
  names `tools/memory-tree/check-memory-hygiene.sh` at check 24's `status=1` line as a `status` site
  with no positive assertion.
  Red when: rule (b) classes a print carrying no literal as unreasoned, so check 24's block is no site
  and no line names it.
- **AC3** — When `python tools/memory-tree/check-arms.py --report` runs at the pass commit, it prints
  one row per signature-2 site with its kind, class, reason line and state, and one `UNREASONED` row
  per near-miss. Its site total equals the total in the census line `--check` prints, and both are
  recorded in the acceptance ledger beside §4's census.
  Red when: the report omits the `UNREASONED` rows, so the lines the predicate skips go unannounced.
  figure: the totals are DERIVED at observation. §4's 155 sites and 18 unreasoned lines are PINNED at
  `e1f4d8c0`, and a gap over ten per cent is explained in the ledger.
- **AC4** — When a slice runs the hygiene suite's new check 24 block over the pass's kit dir, it
  prints that block's `ok` lines and no `FAIL` line. Its branch run exits non-zero with output
  carrying `and this tree does not honour it`, and `--offenders` keys `check 24` alone. Its clean run
  exits 0 and prints `rotation-mode: clean (`. `python tools/memory-tree/check-arms.py --report` then
  reads check 24's site ARMED by the hygiene suite.
  Red when: the slice runs over a scratch kit copy whose check 24 block has `status=1` deleted, and
  the branch-run arm prints `FAIL`. Over a copy whose block prints nothing on a green run, the
  clean-run arm prints `FAIL`.
  cost: one scratch repository and three engine runs, as the check 28 slice of `TOOL-aGraftedHelix-13`.
- **AC5** — When `python tools/memory-tree/check-arms.py --check` runs at the pass commit, it exits 0.
  It prints the census line, with armed plus waived equal to the site total, and one `waived` line
  per waived row, each carrying a reason. `grep -c REASON-OWED memory/project/unarmed-branches.txt`
  prints 0.
  Red when: a scratch clone's pin file has one `exit` row's reason field emptied, and `--check` there
  exits 1 naming that row.
- **AC6** — When `python tools/memory-tree/check-arms.py --report` runs at the pass commit, the UNWIRED
  refusal of `tools/unattended/adopt-unattended.sh` reads ARMED by its sibling suite, at the
  signature `hook is UNWIRED —`.
  Red when: the sibling suite's assertion quotes only `gate-guard hook is UNWIRED`, as at the parent,
  which arms nothing under signature 2.
- **AC7** — When `grep -c '^ARMS_REFUSALS="graded"' .memory-tree.conf` runs it prints 1, and
  `grep -c '^ARMS_REFUSALS=""' tools/memory-tree/.memory-tree.conf.example` prints 1.
  `grep -c ARMS_REFUSALS tools/memory-tree/kit.toml` prints at least 1, and
  `python tools/govkit/govkit.py selfcheck` exits 0.
  Red when: the example conf ships the key set, and an adopter's next upgrade grades signature 2
  unasked.
- **AC8** — When `python tools/memory-tree/check-arms.py --emit-floors` runs at the pass commit, its
  stdout is byte-equal to the line `grep '^ARMS_FLOORS=' .memory-tree.conf` prints.
  Red when: a script signature 2 discovers has no floor token, as every one of them lacks at the
  parent.
- **AC9** — When `bash tools/memory-tree/adopt-memory-tree.sh --render` runs at the pass commit,
  `git status --porcelain memory/HYGIENE.md` prints nothing. `grep -c ARMS_REFUSALS` prints at least 1
  over `tools/memory-tree/README.md`, over `tools/memory-tree/check-arms.py` and over
  `memory/project/unarmed-branches.txt`.
  Red when: the template moved and the carrier was not re-rendered, which the porcelain line shows.
- **AC10** — When `python tools/memory-tree/gotchas.py --check` runs at the pass commit, it exits 0, and
  `grep -c 'check-arms.py --check' memory/gotchas/a-grep-for-a-word-is-a-presence-probe.md` prints at
  least 1.
  Red when: the record keeps its "no machine gate" paragraph beside a gate that grades its class, the
  class `two-answers-to-one-question`.
- **AC11** — When `python tools/govkit/govkit.py epoch --base <the parent>` runs at the pass commit,
  its memory-tree line reads clean at the bumped version. `bash tools/check-kit-versions.sh` and
  `python tools/codebase-map/gen_map.py --check` each exit 0.
  Red when: a shipped file moved and its kit's version did not, or the map's symbols were not
  re-rendered for the new functions.
  figure: the version is DERIVED from the parent at observation.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `check-arms selftest` · `memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `govkit selfcheck` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `gotchas selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-arms.py, its --selftest · covers AC1 · each label builds its own fixture, and the staged break empties scan_refusal_sites in a scratch clone · none, the selftest carries no floor
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC4 · a scratch kit copy whose check 24 block has status=1 deleted, and one whose block prints nothing on green · the suite's assertion floor rises by the block's executed count
New arm: tools/unattended/adopt-unattended.test.sh · covers AC6 · the UNWIRED arm's assertion carries the derived signature, observed through check-arms rather than by a staged break · none, the suite carries no floor (TOOL-aDeferredBar-9)

The bar and the whole suites run once, after the last unit is terminal. A pass runs every criterion
above directly.

## 8. Open questions

- **F1 — Which scripts does signature 2 read?**
  (a) Every tracked `*.sh` that is not `*.test.sh` and not under the memory root. That is the class:
  155 sites in 25 scripts by §4's census. (b) The kit adopters, by their `adopt-*.sh` names, plus the
  non-`fail` sites of the scripts signature 1 already discovers: 115 sites by the same probe. The
  bar-leg checkers that exit 1, such as `tools/check-dead-paths.sh` and
  `tools/check-hook-destinations.sh`, stay outside. (c) The scripts `tools/gate-legs.json` runs as
  legs. A memory-tree kit file would then read the run-gates kit's manifest by name, which the
  charter's kit-literal ban refuses, and an adopter with no such manifest gets nothing.
  Option (b) gates an instance family, which charter §7's "gate the CLASS" names as the defect. Option
  (c) trips §12's ban. Option (a) costs the largest waived set, every row with a reason, and one
  printed line per row on every run of the leg.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-07, delegated): (a). Option (c) fails the `install-prefix` gate through
  §12's kit-literal ban, M3's first veto. Option (b) survives the vetoes and grades fewer sites, so
  the most feature-rich survivor is (a).
- **F2 — How is a delegated site armed?**
  (a) An `# arm-signature:` marker in its block declares the text its callee prints on refusal, and
  an arm asserting that text arms it. (b) Each delegated refusal is routed through a literal of the
  script's own: in a `fail()` gate, a `fail <n> "<literal>"` after the capture print, which makes it
  a signature-1 branch; in an adopter, an `echo "<literal>"` before its `exit 1`. (c) A delegated site
  is never armable and is always waived.
  Option (b) changes what the hygiene engine prints and keys under `--offenders` for seven checks,
  which the `memory hygiene` leg's signature compares across a push. It also adds a second refusal
  line to every delegated red. Option (c) contradicts the owner's ruling that check 24's block is
  armed. Option (a) adds one comment grammar, and trusts its text until the suite runs.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-07, delegated): (a). Option (c) fails S5, which arms check 24's block,
  M3's first veto. Option (b) survives but changes seven checks' printed and keyed output, so (a) is
  the survivor with the fewest follow-ups.
- **F3 — May this unit edit the governance carrier `memory/HYGIENE.md`?** Its meta-gate paragraph
  states signature 1 as THE population, which the switch makes false. It also says the pin's
  working state is empty. (a) Rewrite the paragraph in `tools/memory-tree/HYGIENE.template.md` to
  point at the module docstring for the population, keep only the pin's rules there, and re-render.
  (b) Add a paragraph stating signature 2 beside signature 1's. (c) Leave it, so the carrier and the
  docstring disagree.
  M3's veto 2 makes any carrier edit the owner's. Option (b) states a predicate the module owns a
  second time (`two-answers-to-one-question`), and option (c) ships that class.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-07, delegated): (c). Options (a) and (b) change a governance carrier,
  which M3's second veto reserves to the owner, and no `may:` grant in the build README names it.
  Option (c) is the one survivor. The carrier's sentence stays TRUE for signature 1, which is all it
  states; it is incomplete, not wrong, and its claim that the pin is empty was already false before
  this unit. The rewrite of (a) is the owner's turn, and the return of this pass names it.
- **F4 — Does check 24's block print its capture on a green run?** It does not today.
  `row_grammar.py --check-rotation` prints its `ROTATION_MODE` UNDECLARED and `snapshot`
  announcements at exit 0, and the block never shows them. Blocks 20, 27 and 28 print theirs.
  (a) Print it as they do, and arm the clean run under S5. (b) Arm the red path only, and leave the
  swallow.
  Option (a) adds one line to every adopter's `memory hygiene` output, which is an adopter-visible
  change; where the key is unset, that line is the UNDECLARED announcement. Option (b) leaves a skip
  that looks like a pass in the block this unit arms (`swallowed-delegate-reads-as-clean`).
  Recommendation: (a).
  RESOLVED (agent, 2026-10-07, delegated): (a). Neither option trips a veto: one more output line is
  no new public surface. Option (a) satisfies S5's clean-run arm, which (b) leaves unwritten, so it
  is the more feature-rich survivor.

## 9. Revision log

- rev-1 · 2026-10-07 · initial draft from the unit 45 to 47 spec brief, grounded at `e1f4d8c0` on node
  `a`, with §4's census and the two association rules measured by a read-only probe over the tree.
- rev-2 · 2026-10-07 · the build's refinements of rules 1 to 3, each measured over the tree at
  `4fc54f77`, in §4's new subsection; S6 lengthens arms only inside the dispatched write set and
  waives a driving arm elsewhere with its line named; the census re-derived at the build; Files
  touched gains the two lengthened suites and the re-rendered carriers. No acceptance criterion moved.
- rev-3 · 2026-10-07 · §8's four forks resolved under delegation: F1, F2 and F4 take (a); F3 takes
  (c), because (a) and (b) edit a governance carrier, so S8 drops the HYGIENE paragraph rewrite and
  §5 says the carrier is the owner's turn. No acceptance criterion moved.

## 10. Reuse audit

The map probe was `python tools/codebase-map/reuse_lookup.py "discover a shell refusal that exits 1
with a printed reason and grade it for an armed sibling test"`. It scanned every present layer and
reported `unscanned layers: none`. It ranked `discover` in `tools/memory-tree/check-arms.py` as the
seam, and this unit extends it, with `message_of`, `signature`, `armed_signatures`, `parse_pin` and
`parse_floors` beside it. Each was verified against source at `e1f4d8c0`. Its other hits were
name-stem neighbours. `parse_shell_defs` in the lexicon kit reads function definitions, not refusal
sites, and `refusal` in the recall kit reads a conf. No existing seam pairs an `exit 1` with its
printed reason, so that walk is S1's new code. The engine-arm shape S5 copies is the check 28 block
of `TOOL-aGraftedHelix-13` in the hygiene suite, with its `run_cont28_gate` helper.

Recall surfaced the ask `TOOL-aDeferredBar-8` and the build README's parked decision. It surfaced the
abandoned run's decline, refused then as a MEDIUM that a fold may not promote, and now owner-adopted.
`TOOL-aTimedTurnstile-7` and `TOOL-aSurfacedLexicon-21` name the Python population, which §3 keeps
out. `TOOL-aDeferredBar-13` names ordinal keying, which S2 avoids for its own rows. `TOOL-cGradedDebt-3`
names a hygiene floor trailing its population, which AC8's equality closes for every gate.
`TOOL-aFoldedQuarry-7` made fail branches mechanical. None records a ruling against a second
signature.

Recall terms used: `python tools/memory-recall/query.py "how does check-arms discover gates and what was decided about refusals that exit without a fail helper" --terms "check-arms discovery signature fail-helper unarmed-branches ARMS_FLOORS delegated dispatch status=1 adopter refusal armed sibling pin"`

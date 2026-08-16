# Review — aSiftedPlaybook, round 6 (M8 closing review)

## Verdict: BLOCKED

*Synthesis pass over the cumulative `0f0a121..HEAD` diff (36 files, +1726/-142), HEAD `262d07e`.
Five lenses -> batched skeptics -> this pass; **5/5 lenses live, 0 dead, 0 dead skeptic batches,
0 spurious / duplicate / conflicting verdicts, 0 unverified findings.** **28 raw judged — 21
confirmed, 7 refuted, 0 unverified.** The 21 confirmed collapse to **17 findings** after merging
four duplicate pairs (two lenses filed the playbook-parity temp-file vacuity, two the `customize.md`
placeholder-total contradiction, two the `{{DEFAULT_BRANCH}}` sense count, two the map dossier's
receiver count). **Every finding below was re-executed by this pass against the working tree or an
isolated clone at HEAD before it entered the table** — nothing here is inherited on a lens's word.
Two impact claims were corrected rather than accepted; both corrections are recorded in Coverage.*

*The bar is green: `GATE_FULL=1 bash tools/run-gates.sh` -> **58/58 legs passed**, and
`bash tools/check-wiring.sh --check` reports six of six ok. **Not one finding below reds a leg.**
That is the point of most of them: the recurring shape in this round is a gate or an arm that is
green because it is not looking, in a build whose whole subject is that shape.*

**One blocker.** `B1` ships a false claim about a shipped product in the product's own operating
ruleset plus three more carriers, and the acceptance criterion written to prevent exactly it
(`PLAY-3` AC3) was not performed for that kit.

| id | sev | file:line | finding | fix |
|---|---|---|---|---|
| B1 | blocker | `parallel-coding-governance.template.md:150` | **The new §7 `gate-lint/` bullet describes a kit that does not exist.** It tells every adopter the kit "catches the failure a green suite cannot — a gate whose selector matches the empty set, or that asserts between two values the same code derives, and therefore passes while checking nothing." The kit is one 193-line file, `ps-hygiene.py`, whose functions are `_code · _close_brace · _scopes · case_collisions · missing_bom · scan · _selftest · main`; `grep -rniE 'selector\|derive\|empty set\|vacuous' tools/gate-lint/` returns **nothing**. Its own README states its two classes — case-only PowerShell identifier collisions and BOM-less non-ASCII CP1252 mis-decode — and says outright that a repo with no `.ps1` "gets `0 files clean`, which is honest but proves nothing". I ran it: `python tools/gate-lint/ps-hygiene.py .` -> `ps-hygiene: OK — 0 .ps1 file(s) clean`, rc=0. The same fabrication is in three more carriers: `AGENTS.md:167-169` ("It lints the GATES, catching…"), `README.md:46-48`, and the drop-condition at `parallel-coding-governance.customize.md:87` ("drop if the project has no gates of its own to lint" — the true condition is "no PowerShell"). Each sentence's preceding clause ("project-agnostic, drop-in, two lines to adopt and no gate legs of its own") IS copied verbatim from the README, so a reader gets no cue that the referent switches. The two classes named are gotcha DOCUMENTS (`memory/gotchas/vacuous-selector-empty-population.md`, `assertion-between-two-derived-values.md`), not code. `spec-PLAY-aSiftedPlaybook-3.md:228-232` (AC3) required "each new bullet … read against its kit's own README … Checked per kit, by reading the README" and names `tools/gate-lint/README.md` explicitly; the other three kits' bullets do check out. `check-playbook-parity.sh` cannot see it — S1 asserts only that the kit is NAMED, and its header disclaims description fidelity. | Rewrite all four carriers to state what `ps-hygiene.py` does — two PowerShell source-hygiene classes — and carry over the README's own caveat that a `.ps1`-free repo gets a result that proves nothing. Change `customize.md:87` to "drop if the project ships no PowerShell". If vacuous-selector / derived-value linting is wanted, that is a new scope item, not a description. |
| H1 | high | `tools/check-playbook-parity.sh:121` | **The whole S2 value-parity stage silently no-ops and the gate then prints an affirmative "pairs in agreement" and exits 0.** The pair loop's results leave the subshell through an unchecked temp file at `${TMPDIR:-/tmp}/pp.$$`; `done > "$PPTMP" 2>/dev/null` (:121) and `done < "$PPTMP"` (:125) both fail to stderr without touching `status`, and the OK line at :160 asserts pair agreement on `status -eq 0` alone. Reproduced in a clone at HEAD with a real drift injected (`MAX_LENSES = 5` -> `6` in `tools/hooks/agent-cap.js`): normal `TMPDIR` -> `PLAYBOOK-PARITY check 7 FAILED — … Pair lens-array bound … the playbook states 5 where tools/hooks/agent-cap.js owns 6`, rc=1; `TMPDIR=/definitely/not/here` -> two redirect errors on :121 and :125 then `playbook-parity OK — 12 kit(s) documented or waived · pairs in agreement · catalogue arithmetic holds`, rc=0. Same drift, same gate, opposite verdict, and the green one makes a positive claim about the section that never executed. All three declared anti-vacuity arms live INSIDE the discarded subshell, so none can see it; `run-gates.sh` classifies on exit code, so the leg reports GATE ok. No arm in `check-playbook-parity.test.sh` perturbs the side channel — every arm mutates fixture CONTENT. S2 is the stage the file's own header calls the reason the gate exists. | Delete the side channel: `pairfails=$(printf '%s\n' "$PAIRS" \| while …; done)`, or read the pairs from a here-doc so the loop runs in the current shell and can call `fail 7` directly. If the file is kept it must be `mktemp` with a hard `exit 2` on failure, a `trap … EXIT`, and a reader that never falls through to the OK line. Add an arm that runs the gate with an unwritable `TMPDIR` over a drifted fixture and asserts it does NOT exit 0. |
| H2 | high | `tools/check-template-size.test.sh:72` | **No arm anywhere pins the 48 KiB ceiling this build was convened to raise.** A1/A2/A4 derive both the fixture size and the expectation from the gate's own OK line (`LIMIT=$(bash "$GATE" \| sed …)`), so each boundary arm is relative to whatever the default happens to be. Proved in an isolated clone at HEAD, mutating only `MAX_BYTES=${2:-${MAX_BYTES:-49152}}`: raised to `131072` -> `harness    shipped limit read from the gate: 131072`, every arm ok, `PASS`; lowered to `40000` -> `PASS`. Both directions, zero arms red, full bar green. Nothing else pins it: tracked `git grep 49152` returns only `check-template-size.sh:11/:44` and the harness's own positionals; `check-playbook-parity.sh`'s PAIRS holds two rows (lens-array bound, agent-cap hook matcher) and neither is this; `gate-legs.json:17` is a leg NAME with no check; `AGENTS.md`, `README.md:12`, `memory/guides/SESSION-KICKOFF.md:121` and the template's v2.8 header state 48 KiB in ungated prose. The harness header at :18-21 claims the opposite outcome verbatim, and `TOOL-2` rev-2 records that sentence as the defect it fixed. | Add one arm on the discipline A12 already uses: read the OK line's limit and compare it to a hand-written literal `49152`, failing by name when it moves. Better, add a PAIRS row binding the gate's default to the figure `AGENTS.md` states, which puts all six prose carriers under the parity gate built in this same build. |
| H3 | high | `parallel-coding-governance.customize.md:15` | **The shipped placeholder catalogue contradicts itself five lines apart, and the gate built in this build to stop exactly that is anchored past it.** `:15` reads "14 of the **36** placeholders sit unfilled in the companion"; `:20` reads "**37** in total: 24 in the template and 14 in the companion"; `:24` reads "the union is what the 37 counts". Measured at HEAD: template unique 24, companion unique 14, union 37, intersection exactly `{{MEMORY_ROOT}}` — so 36 is simply wrong. `WIRE-INTO-PROJECT.md:99` states it correctly ("the companion carries 14 of the 37 placeholders"), so the two shipped deploy documents disagree, and the OPEN backlog row that named both — `memory/backlog/PLAY.md:8`, `PLAY-aSealedCaravan-1` — is only half-dischargeable. The move was ASSIGNED and missed: `spec-PLAY-aSiftedPlaybook-2.md` §4 row 4 routes "the `36` moves here" while PLAY-4 S4 moved only the `13`->`14`. `tools/check-playbook-parity.sh:138` extracts the total with `sed -n 's/^\([0-9]\+\) in total.*/\1/p'` — anchored at column 0, so it reads only `:20`; the gate prints `catalogue arithmetic holds (24 + 14 over 37 unique)` rc=0 over the stale 36. Its own comment at :130 says it "would have caught 23 + 14 = 37 against a stated 36" — the surviving instance is that literal sentence. | Change `:15` to "14 of the 37 placeholders". Then close the hole: add an S3 extraction that quantifies over EVERY placeholder-total figure in `customize.md`, not just the `^N in total` line (e.g. `s/.*of the \([0-9]\+\) placeholders.*/\1/p`), compare it to `$u_n`, and add an arm that reds when the two totals disagree. |
| H4 | high | `tools/memory-tree/README.md:6` | **PLAY-1 deleted the hardcoded hygiene check count from the template and pointed every adopter at a file that holds the wrong value and disagrees with itself.** Template `:110` now reads "a **hygiene gate** whose check count is stated by the kit README and the gate-leg name and is deliberately not restated here". That kit README says **19** at `:6` ("a 19-check hygiene gate that keeps it that way") and **20** at `:18` ("the gate — 20 checks (1-12 in the shell, 13-16 delegated to `corpus_ids.py`, 17-19 to `gotchas.py`, 20 to `row_grammar.py`)"). Three independent carriers agree the live value is 20: `tools/gate-legs.json:3`, `AGENTS.md:94`, and root `README.md:33` — which THIS build moved 19->20. `git diff --stat 0f0a121..HEAD -- tools/memory-tree/` is **empty**: the file the template now delegates to was never touched. Nothing gates it — the memory-tree kit/dogfood parity leg covers `HYGIENE.template.md` and `SPEC-TEMPLATE.template.md`, not the README, and S2's PAIRS has no row for the count. Every adopter of the kit receives this README as its front page. | Change `:6` to "a 20-check hygiene gate". Add an S2 PAIRS row extracting the count from the kit README against the count in the `gate-legs.json` leg name — the template names both as the owners, so the pair has a source on each side. |
| H5 | high | `memory/archive/parallel-coding-governance.template-v-2-7.md:3` | **The archived "v2.7" snapshot is not v2.7 — it carries v2.8 content under a v2.7 header and a v2.7 marker.** `git hash-object` of the archive is `39c35b2b`, which matches the template blob at exactly one revision: `ac3d091` (PLAY-2). Diffing the BASE blob (`git show 0f0a121:…`, 32682 B) against the archive (33670 B) gives 13 hunks / 36 changed lines, and every one is a PLAY-1 or PLAY-2 change — `{{DEFAULT_BRANCH}}` substituted throughout, the two-halves agent-cap rule, the `Workflow\|Agent` matcher, "build plan"->"build folder", the deleted 19-check. Those are the exact items the live template's own v2.8 changelog at `:6-9` claims as v2.8 changes. AC7's precedent is the opposite of what it assumed: the v-2-5 archive (`83a3967`) is NOT `c702dda^`'s blob (`b6eff82`), because two commits put v2.6 content into the still-v2.5-marked template in between; the v-2-6 case (`240bafda` = `5ed9b4b^`) is the single case where both readings coincide, and it is the one AC7 cited. No convention resolves it — `README.md:12` calls these "Historical `…-v-N-N.md` snapshots" with no rule about which blob. | Replace the file with `git show 0f0a121:parallel-coding-governance.template.md`, the last blob that shipped under the v2.7 label, and correct PLAY-3 AC7 to name that blob ("the last commit whose marker read v2.7 before any v2.8-content edit"), noting that the v-2-6 precedent it cites is degenerate. |
| M1 | medium | `tools/check-template-size.sh:36` | **The `--bump` flag-stripping loop re-splits argv unconditionally, and it is a regression this diff introduced.** `ARGS="$ARGS $a"` (:33) then unquoted `set -- $ARGS` (:36) runs on EVERY invocation, not just `--bump` ones: it word-splits any positional containing whitespace, glob-expands `*`/`?`/`[`, and drops an empty positional, sliding every later argument one slot left. Measured against `main` and HEAD on the same argv: `main` prints `template-size OK — f.md: 100 / 200 bytes` rc=0 for a subject under `dir with space`; HEAD prints `TEMPLATE-SIZE check 1 FAILED — the file to measure does not exist: /tmp/tmp.XXXX/dir` rc=2. Also reproduced: an empty subject slides the LIMIT into the subject slot (`does not exist: 999999`); `'*.md'` expands so the limit lands in the record slot (`line 59: [: b.md: integer expected`, then `line 116: … arithmetic syntax error`, rc=1). The file's own comment at :27-29 names this class as the thing the flag design exists to prevent. Not hit by today's callers — `gate-legs.json` passes `skills/session-kickoff/SKILL.md 18432` and the harness uses space-free scratch paths — and the gate is govkit-exempt (registry `:150`: "Prescribed for copy nowhere in the runbook"), so no adopter receives it; the defect is the regression, not the blast radius. | Use an array: `ARGS=(); for a in "$@"; do if [ "$a" = --bump ]; then BUMP=1; else ARGS+=("$a"); fi; done; set -- ${ARGS+"${ARGS[@]}"}`. Add an arm passing a subject under a directory whose name contains a space. |
| M2 | medium | `tools/check-template-size.sh:101` | **On the `--bump` path a non-numeric recorded value reaches `$((bytes - recorded))` and dies with a `set -u` unbound-variable error**, contradicting the file's own contract in two places. Measured on fresh records: read path -> `TEMPLATE-SIZE check 3 FAILED — the high-water record holds a non-numeric value for … : 'not-a-number'` rc=3; `--bump` path -> `tools/check-template-size.sh: line 101: not: unbound variable` rc=1. The numeric guard at :109 that produces the documented exit-3 named failure sits in the `elif` chain the `--bump` branch at :90 skips whole. The header at :15 promises "Exit 3 = the high-water record exists but this subject's row is not a number", the ratchet comment at :72-73 promises "a NAMED failure, never a `set -u` explosion at the numeric comparison below", and `spec-TOOL-1:117-118` says the same. The operator gets a raw bash error and exit 1 — indistinguishable from over-budget — on the one verb the build method runs at wrap-up. Arm A11 exercises only the read path, so the bar never enters this branch. | Validate `$recorded` right after it is read at :87, above the `if [ "$BUMP" = 1 ]` dispatch, so both paths share the guard. Add an A11b arm running `--bump` over a non-numeric row and asserting the same named message and exit 3. |
| M3 | medium | `tools/check-template-size.sh:99` | **The `--bump` write sequence checks none of its four steps and reports success when every one of them fails.** Measured: `bash tools/check-template-size.sh "$T/f.md" 200 "$T/nodir/hw.txt" --bump` emits `line 95: … No such file or directory`, `line 97: … No such file or directory`, `sort: cannot read: …`, `mv: cannot stat: …` and then still prints `TEMPLATE-SIZE BUMP — …/f.md high-water recorded at 100 (no prior row).` and `template-size OK`, **rc=0**; `ls "$T/nodir"` confirms nothing exists, and the next read run prints `no high-water record …; growth is unpriced.` The success echo at :100-103 is unconditional. Both the exit code and the success line assert an effect that did not occur, in a repo whose stated discipline is to gate on the EFFECT and never the exit code. The failure is fully invisible under the `--bump >/dev/null 2>&1` form the harness itself uses at :108/:117/:130/:133/:157. `$tmp` (`${HIGHWATER}.tmp.$$`) has no trap, so a partial failure leaks it beside the record. | Guard the sequence and route failure through `fail()` with a new check number, and add `trap 'rm -f "$tmp"' EXIT`. Add an arm pointing `--bump` at an unwritable record path, asserting it does NOT print `TEMPLATE-SIZE BUMP` and does not exit 0. |
| M4 | medium | `tools/check-playbook-parity.test.sh:48` | **No arm pins the anchored path-segment matcher — the property the gate's own header calls "the vacuous-selector shape this gate exists to prevent, committed by the gate itself".** Loosening `named_in_playbook` (`check-playbook-parity.sh:72`) from `grep -qE "tools/$1/\|\`$1/\`"` to a bare `grep -qF "$1"` leaves all sixteen arms green: `PASS — check-playbook-parity.test.sh: every arm held`. The fixture cannot exhibit it — its only waived kit is `hooks` and the four-line trio it writes never contains the string "hooks", so anchored and substring agree on every fixture kit. On the real tree the same mutation reds, but ONLY through check 6 (`a waiver row names a kit the playbook DOES document … hooks` / `… lib`) — i.e. purely by accident of the present waiver population, whose own header says the registry must be able to gain and lose rows. Retire either row and a substring matcher would certify every kit as documented with no arm objecting. | Give the fixture a kit whose name occurs as a bare substring but never as a path segment — the real corpus already demonstrates it with `lib` inside "deliberately"/"stdlib". Add `tools/lib/x.sh`, put "deliberately" in the fixture template, waive `lib`, and add an arm that loosens the matcher and expects a red. |
| M5 | medium | `tools/check-template-size.test.sh:144` | **A10 asserts `TEMPLATE-SIZE no-ratchet`, a prefix SHARED by the two ratchet branches at `check-template-size.sh:106` (record absent) and `:108` (record present, subject has no row)**, so it does not distinguish the branch it names — violating the harness's own first discipline at :16-17. Proved by two independent mutations in a clone: deleting the whole `elif [ ! -f "$HIGHWATER" ]` branch -> `PASS — every arm held`; rewording its message while keeping the prefix -> `PASS`. Control on the same run (`-gt` -> `-ge` at :112) DOES red (`arm FAIL A7 at the recorded high-water: no warn`), so the harness bites elsewhere and the weakness is specific to A10. Deleting the branch also silently mislabels the state: the survivor then reports "`$key` has no row in `$HIGHWATER`" for a record file that does not exist. `check-arms.py` cannot backstop it — both branches are `echo`s, not `fail()`s. | Assert the distinguishing text — `"no high-water record at"` — and give the sibling branch (`:108`) its own arm asserting `"has no row in"`. An existing record whose subject row was deleted is the likelier way the ratchet goes quiet, and today it has no arm at all. |
| M6 | medium | `README.md:46` | **The two charter-level kit inventories disagree with the live `tools/` population and with each other, and the gate this build shipped is scoped away from both files.** Live population (`git ls-files -- 'tools/*/*' \| awk -F/ 'NF>2 {print $2}' \| sort -u`) is 12 kits. Root `README.md`'s Contents list gained exactly one entry this build (`gate-lint`), leaving it looking complete while a whole-file `grep -c` returns **0** for `drift-audit`, `memory-recall`, `unattended` and `govkit`. `AGENTS.md`'s "What ships here -> `tools/`" bullet at `:24-41` is missing `gate-lint` and `govkit`; its only `gate-lint` mention sits far below at `:167` in the gate-suite list. `govkit` — the deployer that decides what installs into a target — is named in neither ships-here inventory. `PLAY-3` AC8 ("both carry a `gate-lint` entry in their shipped-kit lists") is satisfied by that gate-suite line rather than the ships-here list, which is how the omission survived. `check-playbook-parity.sh:72` quantifies over `$TEMPLATE $CUSTOMIZE $DOMAIN` only, so a kit can be absent from both charter files forever with the leg green. | Add `drift-audit/`, `memory-recall/`, `unattended/` and `govkit/` to `README.md`'s Contents, and `gate-lint/` and `govkit/` to `AGENTS.md:24-41`. Then widen S1's file set to include `AGENTS.md` and `README.md` (or add a second arm over them with its own waiver column). |
| M7 | medium | `parallel-coding-governance.customize.md:34` | **The `{{DEFAULT_BRANCH}}` catalogue entry states "It carries 17 senses in the template"; measured at HEAD it is 18** (`grep -o … \| wc -l` = 18, `grep -c` = 15 lines). Per-commit: `ac3d091` (PLAY-2) occ=17 — matching the sentence as written; `d3bd21b` (PLAY-3) occ=18; HEAD 18. The 18th is template `:8`, inside the v2.8 changelog clause PLAY-3 S8 added ("the default branch becomes `{{DEFAULT_BRANCH}}` throughout") — a real substitution site, added by a commit that also edited `customize.md` without re-deriving the figure. Neither PLAY-3 nor PLAY-4 mentions the placeholder at all (`PLAY-4:45` explicitly disclaims ownership). Consequence beyond the prose: **PLAY-2 AC1 no longer reproduces at HEAD** — it pins `wc -l` = 17 and `grep -c` = 14 — so a future re-verification of a landed unit reds against a correct tree. Nothing gates it; S2's PAIRS has no row for the count. | Change to 18 and update PLAY-2 AC1's two figures to 18/15, or de-number it on the policy this build applied in TOOL-1 §4, PLAY-3 §4 and TOOL-3 rev-11 ("It appears throughout the template, including two §16 micro-formats"). Better: add an S2 pair extracting the stated number against `grep -o … \| wc -l`. |
| L1 | low | `AGENTS.md:99` | **The new charter bullet claims "Every branch red-proved by mutation" for `tools/check-template-size.test.sh`; two gate branches are red-proved by no arm at all.** Proved in a clone by replacing `check-template-size.sh:103` (the `--bump` no-prior-row message) and `:108` (the "has no row in" message) each with `:` — the harness printed every arm ok and `PASS`, exit 0. The unit itself says the opposite in its own words: `spec-TOOL-2` AC8 — "A3 and A5 still carry no mutation criterion, which is a deliberate limit rather than an oversight." A reader takes the charter claim as a standing property and skips re-proving a branch after a refactor. Ungated: drift-audit's handkept signal only checks that each leg's argv path is cited in the section. *(One correction to the filing lens: A3 and A5 ARE mutation-sensitive — the exempted arms are not the uncovered ones. The uncovered branches are `:103` and `:108`.)* | Match the bullet to what shipped: a red proof per arm, with the ratchet and degenerate-record mutation criteria recorded in AC8 rather than automated, and A3/A5 carrying none. Consider dropping the spelled "twelve" on the same de-numbering policy — the harness prints fifteen `arm ok` lines. |
| L2 | low | `tools/check-template-size.test.sh:112` | **The ratchet arms assert the marker substring, not the numeric content their spec rows require.** `TOOL-2` S2's A6 row reads "exit 0 **and** the warn line, naming `H`, the size and the delta" and A8's reads "the delta reported"; the landed arms match on `TEMPLATE-SIZE WARN` and `TEMPLATE-SIZE BUMP` alone. Proved by mutation in a clone: rewriting the warn line to `TEMPLATE-SIZE WARN — the file grew past its recorded high-water. Advisory only.` and the bump line to `TEMPLATE-SIZE BUMP — re-recorded.` still gives `arm ok A6 …`, `arm ok A8 --bump re-records and names the delta`, `PASS`. An arm whose own label says "names the delta" asserts nothing about the delta, and the ratchet's whole diagnostic payload is unguarded. `TOOL-1` AC7 makes the numbers the point of the warn; the harness header at :16-17 states "Every arm asserts the SPECIFIC MESSAGE or the SPECIFIC BYTES". | Assert the numbers the arm already sets up: `1000 -> 1001 (+1)` for A6, `high-water 1000 -> 1001 (1 bytes)` for A8. Both are literals, so neither re-derives the value from the gate. |
| L3 | low | `tools/check-playbook-parity.sh:67` | **The header's measured justification for the anchored matcher is already stale.** It states a substring search "scores the kit `lib` seven times across the trio, six inside \"deliberate\"/\"deliberately\" and one inside `stdlib`". Measured at HEAD: `grep -oF lib` over the trio returns **9**, classified `4 deliberately + 3 deliberate + 1 Stdlib + 1 stdlib` = seven and **two**. Not an occurrence-vs-line ambiguity (`grep -c` also returns 9). The matcher's rationale survives the correction, but this is a stated measured figure contradicted by its own source, inside the gate written to catch that class — and the next reader who checks it and finds it wrong has no way to tell whether the rationale is wrong too. | State the shape without the count ("a substring search scores `lib` inside \"deliberately\" and `stdlib`"), or move the number into the fixture proposed in M4 so an arm derives it. |
| L4 | low | `memory/map/features/playbook.md:75` | **The dossier's shared-seams entry says the feature contributes "three such paths" to `tools/govkit/registry.toml`; its own `[paths].globs` at `:21-28` lists six, and all six carry exact-path `[[exempt]]` rows** (registry `:150/:154/:158/:162/:166/:170`). Provenance: `git show 346f0c8:…` had three globs and the prose "three"; `git diff 346f0c8..bff1e7b` shows TOOL-3 adding three more globs and two gate-leg claims with **zero** prose change. Ungated in both directions — `python tools/codebase-map/test_codebase_map.py` passes (it pins headings and `[claims]` keys, not the sentence) and `python tools/govkit/govkit.py selfcheck` exits 0. The unit's own spec named this class: `spec-TOOL-3:122`, "a spelled receiver count went stale in the very commit that added a receiver". *(Filed twice, by two lenses; merged here.)* | Drop the number: "every path in this dossier's `[paths]` block needs its own row" — the same rule this build applied to the build README's `B*` table. |

## Left-shift

For each finding, the regression gate that should have caught it — or, where no gate can, the
`memory/gotchas/` class it belongs to.

- **B1** — no gate; `PLAY-3` **AC3** is the control and it was not executed for this kit. The
  durable left-shift is mechanical: extend `check-playbook-parity.sh` S1 from "the kit is NAMED" to
  a per-kit assertion that each distinctive noun phrase in the §7 bullet occurs in that kit's
  README. Class: `two-answers-to-one-question` — two descriptions of one kit, in the direction where
  the wrong one is the shipped one.
- **H1** — `tools/check-playbook-parity.test.sh`: a side-channel arm (broken `TMPDIR` + drifted
  fixture -> must not exit 0). Class: `vacuous-selector-empty-population`, in its purest form — the
  population is empty because the stage never ran, and the OK line asserts over it anyway.
- **H2** — `tools/check-template-size.test.sh`: a literal-pin arm on the OK line's limit, or a
  `check-playbook-parity.sh` PAIRS row binding the default to the figure `AGENTS.md` states. Class:
  `assertion-between-two-derived-values` — both sides of every boundary arm come from the gate.
- **H3** — `tools/check-playbook-parity.sh` S3, widened off the `^N in total` anchor to every
  placeholder-total figure in the file, plus an arm. Class: `two-answers-to-one-question`.
- **H4** — a `check-playbook-parity.sh` S2 PAIRS row (kit README count vs `gate-legs.json` leg
  name); the template now names both as the owners. Class: `two-answers-to-one-question`.
- **H5** — no gate exists and one is cheap: assert that each `memory/archive/…-v-N-N.md` snapshot's
  marker equals the marker in the template blob it hashes to. Class:
  `pin-copied-from-another-corpus` (a label taken from the wrong revision of the same corpus).
- **M1** — `tools/check-template-size.test.sh`: an arm with a subject path containing a space.
  No gotcha class covers argv re-splitting; the file's own :27-29 comment is the standing warning.
- **M2** — `tools/check-template-size.test.sh` A11b (`--bump` over a non-numeric row).
  Class: `fixture-passes-by-finding-nothing` — A11 is real and covers half the state space.
- **M3** — `tools/check-template-size.test.sh`: an unwritable-record `--bump` arm asserting the
  EFFECT, not the exit code. Class: `fixture-passes-by-finding-nothing`.
- **M4** — `tools/check-playbook-parity.test.sh`: a fixture kit whose name is a bare substring but
  never a path segment. Class: `vacuous-selector-empty-population`.
- **M5** — `tools/check-template-size.test.sh`: A10 re-pointed at `"no high-water record at"`, plus
  a new arm for `"has no row in"`. Class: `absence-assertion-over-whole-file-text` (a substring
  shared by two branches is an assertion over neither).
- **M6** — `tools/check-playbook-parity.sh` S1 widened to `AGENTS.md` and `README.md`. Class:
  `vacuous-selector-empty-population` — the quantifier excludes the files the claim is about.
- **M7** — a `check-playbook-parity.sh` S2 PAIRS row for the sense count. Class:
  `two-answers-to-one-question`.
- **L1** — `tools/drift-audit/drift_signals.py`: the handkept signal checks that a leg's argv path
  is cited, never that the sentence beside it is true; the honest left-shift is to de-claim rather
  than to gate. Class: `two-answers-to-one-question`.
- **L2** — `tools/check-template-size.test.sh`: assert the literals. Class:
  `fixture-passes-by-finding-nothing`.
- **L3** — the M4 fixture, once it exists, derives this number. Class:
  `two-answers-to-one-question`.
- **L4** — `tools/codebase-map/test_codebase_map.py` reads `[claims]` and headings, not prose; the
  fix is to de-number rather than to gate the sentence. Class: `two-answers-to-one-question`.

## Checked and clean

- **The full bar.** `GATE_FULL=1 bash tools/run-gates.sh` -> **gates GREEN — 58/58 legs passed**,
  run on a quiescent tree at `262d07e`. `bash tools/check-wiring.sh --check` -> six of six ok
  (hooks, agent-cap, recall, merge driver, eol, kickoff engine). No finding below reds a leg.
- **The size gate against the raised ceiling.** `bash tools/check-template-size.sh` ->
  `template-size OK — parallel-coding-governance.template.md: 36529 / 49152 bytes (12623 under,
  74.3%)`, no warn — PLAY-3's closing `--bump` did return the ratchet to quiet, and the tracked
  record holds both subjects (`36529`, `18215`) keyed repo-relative as specified.
- **The parity gate's other stages.** S1 and S3 both bite on the real tree: the deliberate matcher
  loosening reds through check 6, and the S3 arithmetic reproduces exactly (`24 + 14 over 37
  unique`) against an independent measurement of the placeholder sets.
- **The other three new §7 kit bullets.** `drift-audit`, `pytest-parallel-guardrails` and
  `agent-instructions` each check out against their own READMEs — B1 is specific to `gate-lint`,
  not a systematic failure of S1-S4.
- **The govkit registry.** All five new `[[exempt]]` rows this build added resolve to real tracked
  paths; `python tools/govkit/govkit.py selfcheck` exits 0 with `0 unclaimed`.
- **Round-5 fold.** Nothing from round 5's five findings resurfaced; the specs' revision logs and
  the run-state generated region are consistent with the commits that produced them.
- **Two lens claims refuted on measurement rather than inherited** — see Coverage.

## Coverage

I received the five lenses as a merged judged set without per-lens attribution, so these bullets
describe the five review surfaces the finding population covers, not five named agents. All five
were live; no batch was dead.

- **Size-gate mechanics** (`tools/check-template-size.sh`) — filed 5, confirmed 3 (M1, M2, M3),
  refuted 2. Re-executed all five myself. The two refutations hold: the tri-grammar `MAX_BYTES`
  parse (`0100` -> `156.2%` rc=0) is byte-identical on `main` and needs an input no caller supplies;
  and the WARN's bar invisibility is answered by `.githooks/pre-commit:47-51`, which runs the gate
  unredirected whenever the template is staged.
- **Parity-gate mechanics and vacuity** (`tools/check-playbook-parity.sh`) — filed 5, confirmed 3
  (H1 twice, merged; L3), refuted 2. Both refutations hold on scope grounds recorded in
  `spec-TOOL-3` §3 (the two-row PAIRS seed is an explicit non-goal) and on the derivation the code
  itself documents at :44-45.
- **Arm and self-test coverage** — filed 6, confirmed 5 (H2, M4, M5, L1, L2), refuted 1. Every one
  proved by mutation in an isolated clone at HEAD, with a control mutation on the same run to show
  the harness bites elsewhere. The refuted one (the "twelve arms" count) is defensible: the harness
  numbers A1-A12 and prints A5a/A5b and A8/A8b as halves.
- **Shipped playbook and companion prose fidelity** — filed 6, confirmed 4 (B1, H3 twice merged,
  M7 twice merged), refuted 2. The v2.8 marker-parity refutation holds: both markers read v2.8 at
  HEAD and `customize.md:101-103` documents human inspection at re-pull as the mechanism.
- **Records, inventories and the archive** — filed 6, confirmed 4 (H4, H5, M6, L4 twice merged),
  refuted 2. The `gate-legs.json` label refutation holds — the rename was owner-resolved as F1 in
  `spec-TOOL-1:371-400`, and two of the four cited carriers are generated and byte-compared.

**Two impact claims corrected rather than inherited.** (1) **H5** was filed on the premise that the
documented re-pull procedure diffs an adopter's copy against the archive; it does not —
`WIRE-INTO-PROJECT.md:569-575` and `customize.md:103-107` both diff against the *current* template
and call the snapshots "version history". H5 stays high because the file is an affirmatively wrong
record under a version label, but it does not silently cost an adopter 11 hunks, and it is not a
blocker. (2) **M1** was filed as breaking "a shipped kit" for adopters; `tools/govkit/registry.toml:150`
exempts the gate from deployment with the reason "Prescribed for copy nowhere in the runbook", so
the adopter exposure is nil and the finding stands purely as a regression against `main`.

**Limits of this report.** No lens was dead and no skeptic batch was dead, so no area went
unreviewed for harness reasons. There are **zero unverified findings** — every confirmed item was
re-executed by this pass, and nothing was carried on a lens's or a skeptic's word alone. What this
review does NOT cover: the diff was read as a cumulative `0f0a121..HEAD`, so a defect introduced and
then reverted within the build is invisible to it; the seven spec documents were audited in rounds
1-5 and re-read here only where a finding cited them; and the mutation testing was bounded to the
two new gates and their harnesses — the other 54 legs were exercised only by running them green,
which is a liveness check, not a red proof.

**Disposition: this may NOT merge and push as it stands.** One blocker (B1) ships a false claim
about a shipped kit in the product's own operating ruleset and three further carriers, and it is
adopter-facing in every one of them; it must be corrected before landing. The five highs should
land with it: H1, H2 and H4 are each one small edit to a gate or an arm, H3 completes a move the
build itself assigned and left half-done, and H5 is a single `git show` redirect plus an AC
correction. The seven mediums and four lows are ordinary follow-ups and none of them blocks —
but M1 is a regression against `main` and is cheap, so it belongs in the same fold. After B1 and
the five highs are folded, re-run the full bar and this becomes CLEAN WITH FIXES.


## Fold — applied 2026-08-16, after the review

Every one of the seventeen was folded; none was waived. Recorded here because the report above is
the last record a later session reads, and a BLOCKED verdict with no fold note reads as unlanded.

- **B1** the fabricated `gate-lint` description replaced with what `ps-hygiene.py` actually scans
  (case-only identifier collisions; BOM-less non-ASCII decoded as CP1252), in all four carriers —
  template §7, `AGENTS.md`, root `README.md`, the customize drop row. `PLAY-aSiftedPlaybook-3`
  gains **AC3b**, which requires each kit bullet to be checked against that kit's own README by
  reading it: AC3 was satisfiable by a bullet merely existing, which is how a description inferred
  from a kit's NAME shipped into four files.
- **H1** the parity gate's S2 stage now checks both ends of its subshell crossing and emits a
  completion SENTINEL, so lost results red instead of reading as "no pair disagreed".
- **H2** `A0` pins the shipped 49152 ceiling to a literal — the only arm that does, deliberately.
  Red-proved: mutating the default to 131072 reds it and nothing else.
- **H3** `customize.md:15` 36 → 37, so the catalogue no longer contradicts itself five lines apart.
- **H4** `tools/memory-tree/README.md:6` 19 → 20. Delegating the count to a carrier without reading
  it turned a known follow-up into a defect this build created.
- **H5** the archive re-cut from the BASE blob (the finished v2.7), and `PLAY-3` AC7 re-worded. The
  `5ed9b4b` precedent was re-measured: that bump was marker-only and LAST in its build, so its
  parent was the finished v2.6. `<bump>^` was a proxy for "the finished content of the version you
  are leaving", and the proxy fails whenever the bump is not last — which round 4 did not check.
- **M1/M2/M3** the argv re-split rebuilt through `"$@"`; the non-numeric contract enforced before
  the bump branch; the write sequence checked at every step with the directory tested before any
  open, so an unwritable target is `check 4` rather than four shell errors and a false BUMP.
- **M4** an arm naming a kit only inside an unrelated word; red-proved by loosening the matcher.
- **M5** `A10`/`A10b` split onto the clause unique to each branch.
- **M6** root `README.md` completed against the live twelve-kit population (five were missing).
- **M7** the `{{DEFAULT_BRANCH}}` sense count de-numbered — it read 17 and PLAY-3 made it 18.
- **L1** the charter's "every branch red-proved" claim replaced by a pointer at `ARMS_FLOORS`.
- **L2** the ratchet arms assert the numbers their spec rows require, not the marker substring.
- **L3** the parity header's `lib` measurement de-numbered (7 → 9 between drafting and landing).
- **L4** the dossier's path count replaced by its own globs list.

**Three of these — H3, H4 and M7 — are the same defect as B1 in miniature**: a value delegated or
restated without reading what it was delegated to. That is the class this build exists to close, and
it produced four fresh instances of it while closing eleven. The gate this build ships would have
caught H3 alone; the rest are why `AC3b` is worded as a reading obligation rather than a grep.

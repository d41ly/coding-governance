**Serves:** diff-review TOOL-aBlindedTrial-7 TOOL-aBlindedTrial-8 KICK-aBlindedTrial-1

# Closing diff review, round 3 — aBlindedTrial units 7, 8 and KICK-1: the fold of round 2's twelve findings

Node `a` · 2026-09-21 · Tier-2 · on `branch/spec-audit-followups` · adversarial fan through `tier2-review.js` (4 finder lenses → 4 skeptic batches → this synthesis). Round 2's record is `2026-09-21-review-TOOL-aBlindedTrial-7-8-kick1-closing-diff-round2.md` in this folder (R1–R12); round 1's is the `…-round1.md` beside it. Every confirmed finding below was re-read at source and, where it names behaviour, re-executed in this synthesis before it was adjudicated: the checker over six fixture repos (four carrying the LIVE manifest) and in `--list` mode over the live corpus, a `tools/./`-admitting mutant of the checker against the shipped R8 fixture and the whole checker suite, the driver's line-1549 idiom sliced byte-for-byte under `set -u` against twelve blob shapes beside the startup source and the hook's regex, and the driver's `specs-audited` block (94 arms) run through the real driver at HEAD and through a one-character-patched copy. Nothing was taken from a skeptic's word alone.

**Reviewed range:** `315201b0cf4c5654afc03c556f286018d1f72593...HEAD` — **ROUND 3**. HEAD is `312213ec8ad9`, one commit, 21 files, +507/−120: the fold of round 2. The base is round 2's HEAD and resolves (`git cat-file -t` → commit).

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing. Round 2's twelve items are closed at source, and the PRIORITY question has a measured answer: on a fixture carrying the LIVE `tools/gate-legs.json` (111 legs) with a spec dated at the 2026-09-22 cutoff whose sub-head reads exactly `No file under `tools/` is touched.`, the checker exits **0 with zero hits**, its guards line reads `0 declared path(s) examined in 1 live spec(s)`, and `--list` prints one row, `tools/ — a one-segment root declares nothing, not joined`. Round 2's 36-hit sentence (the same negation plus a declared `memory/builds/tOne/build/note.md`) now yields the 2 `memory/` hits the floor owes for the declared file and none for `tools/`. A genuine two-segment directory still trips: `tools/hooks/` under the sub-head owes all five `tools/hooks/` legs, and `tools/run-gates/` owes `run-selftests self-test` through the symmetric arm. `--list` over the live corpus at HEAD prints 159 `NEAR [guards]` rows (190 in round 2), the 34 `<- tools/` rows gone and four root rows in their place, exactly the four U8's rev-3 line records. `check-spec-tokens.test.sh` is 66/66, `kickoff-manifest ratchet` is green at HEAD (round 2's R5 closed), and the engine sits at 18428/18432.

What this round finds is one fix that opened a narrow fail-open path in the direction three refusal codes exist to close: round 2's R6 sentinel, glued to the BASE conf blob with ONE newline, lets a blob whose last line is the key assignment ending in a backslash continuation turn that assignment into a temp-env prefix of the sentinel `printf`, whose argument was already expanded from the blanked variable. The driver then reads a declared project default as ABSENT and prints `preflight OK`. Reproduced through the real driver, not only the sliced idiom. One MEDIUM. Six LOWs: the DoD grader's not-gradable sentence now misattributes a refused conf read to the README and the anchor; the engine's reflow split the second `## open` spelling across two lines; the R8 arm's `tools/./` claim is asserted by prose alone; the checker's new docstring types two manifest-derived figures undated (and one of them is the token count wearing the sentence's name); the header's "residual, stated" states one direction of a two-direction cut; U7's estimate omits the BUILD-METHOD carriers its own S5 names. Every fix is a character, a rewrap, an arm or a sentence; the units are INPROGRESS, so they fold before the close.

Why not BLOCKED: nothing reds at HEAD, no leg the specs name is red, and the MEDIUM's trigger is a stray trailing backslash on the key line when it is the conf's last statement — a typo class, not a shipped conf (both shipped confs are pure assignments) — with a one-character fix verified on every shape the suite covers.

## Review shape

Raw **11** · confirmed **8** · refuted **3** · unverified **0** · precision **0.73**.

Precision is above the 0.5 floor §8 sets. The eight confirmed collapse to **7 items**: ids 1 and 5 are the same defect with the same byte-for-byte repro from two lenses, merged by hand in this synthesis at write time; the pipeline discarded no duplicates. The three refuted did not reach this synthesis as text, only as the count, so they are not re-adjudicated here.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 1 MEDIUM · 6 LOW** (7 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 2 MEDIUM · 6 LOW** (8 findings; ids 1 and 5 take the MEDIUM of R1 and every other id keeps the LOW its finder gave).

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **4/4** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so a zero in this report is evidence of absence and not of a hole. The one duplicate pair was judged by hand in this synthesis, as stated above.

What this synthesis ran, per the lens instruction. Six fixture repos, cutoff `2026-09-22` staged and uncommitted so the relation rule announces rather than refuses: **A** the LIVE manifest with round 2's 36-hit sentence → exit 1, 2 hits, both `recall floor* <- memory/builds/tOne/build/note.md`; **A2** the LIVE manifest with `No file under `tools/` is touched.` alone → exit 0, 0 hits, one root NEAR row; **B** `tools/run-gates/` declared → exit 1, `run-selftests self-test <- tools/run-gates/`; **C** `tools/hooks/` declared → exit 1, five hits; **D** `.githooks/` declared → exit 0, 0 hits, one root NEAR row; **E** `./` · `../` · `tools/./` · `tools/x/thing.sh` on a Gates-carrying spec against a bare `tools/` guard under the floor → `1 declared path(s) examined`. A mutant checker refusing only a LEADING `''`/`.`/`..` segment (admits `tools/./`) against the shipped R8 fixture → `--list` output byte-identical to HEAD's, and against the whole suite → every arm that runs on a copied checker passes (the two `parity` arms fail on an out-of-tree copy whether or not it is mutated, measured both ways). `python tools/check-spec-tokens.py --list` over the live corpus at HEAD → 159 `NEAR [guards]` rows, 0 `<- tools/ `, 4 root rows. `extract_files_touched` walked over every spec → roots `tools/` 14, `memory/` 6, five others once each; the exact sentence `No file under `tools/` is touched` occurs 4 times in spec files. `derive_guarded_legs` on the live manifest → broad `tools/lib/` 30 · `tools/` 11 · `tools/memory-tree/` 9 · `tools/run-gates/` 6; one-segment JOINED guards `.githooks/` 5 · `.claude/` 2 · `memory/` 2. The line-1549 idiom sliced byte-for-byte under `set -u` (bash 5.3.9) against twelve blob shapes beside the round-1 idiom, the two-newline fix and `bash -uc '. conf'`; `git show` captured through `$(…)` verified by `od` to leave the blob ending in the backslash. `readSpecAuditDefault`'s regex driven in node against the backslash line → `null`. The driver's `specs-audited` block (`unattended.test.sh:5565-5897`, byte-identical to the fold session's slice harness) plus one probe arm, run through the REAL driver at HEAD → 94 arms, only the probe RED (`spec-audit — not owed (opt-in)` and `preflight OK`), and through a copy patched with the one-character fix → **PASS (114 assertions)**, the probe reading the date. `bash tools/check-spec-tokens.test.sh` — **66 assertions, exit 0**. `bash skills/session-kickoff/manifest-check.sh` — rc 0. `bash tools/check-template-size.sh skills/session-kickoff/SKILL.md` — 18428/18432, advisory high-water warn only. `gotchas.py --for-diff 315201b0..HEAD` — 31 classes by anchor + 5 universal. The bar and the driver suite whole were not run, as instructed. All suite output went to files and was grepped, never read through `tail`.

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| R1 | MED | 1, 5 | `tools/unattended/unattended.sh:1549` | The in-eval sentinel's single-newline glue turns a BASE conf whose LAST line is `SPEC_AUDIT_DEFAULT="<date>" \` into a temp-env prefix of the sentinel `printf`; the read returns `OK ` and the driver reads a declared project default as ABSENT — `not owed (opt-in)`, `preflight OK`. Round 1 refused this blob (fail 55); the fold regressed it to fail-open. |
| R2 | LOW | 7 | `tools/unattended/unattended.sh:3927`, `:3922-3925` | With `DERIVED=1` now after both halves, fail 54/55 land on the not-gradable branch whose sentence and comment name the README and the anchor as the cause; the R2 arm at `unattended.test.sh:5791` pins the misattributing bytes. |
| R3 | LOW | 6 | `skills/session-kickoff/SKILL.md:208-209` | The Step 5 reflow splits `spec audit: not declared (owner)` across two lines; the second of the three `## open` spellings no longer exists on one line (`grep -c` 1 at the base, 0 at HEAD). |
| R4 | LOW | 10 | `tools/check-spec-tokens.py:62`, `:268`, `:552` | "The residual, stated" names one direction only; a one-segment root that is ITSELF a joined guard (`.githooks/` 5 legs, `.claude/` 2, `memory/` 2) declared wholesale declares nothing, and the NEAR row names the skip without the remedy. |
| R5 | LOW | 8 | `tools/check-spec-tokens.test.sh:519-521`, `:531` | The R8 arm's label and comment claim `tools/./` declares nothing, but a mutant admitting it is byte-identical on that fixture and passes the whole suite; the refusal is load-bearing on a Gates-carrying spec under a bare `tools/` guard. |
| R6 | LOW | 11 | `…spec-TOOL-aBlindedTrial-7.md:80-86`, `:142` | U7's `### Files touched (estimate)` omits the two BUILD-METHOD carriers its S5 names and this fold edited again; its §7 omits `kit/dogfood doc parity`, the one leg guarding `memory/guides/BUILD-METHOD.md`. |
| R7 | LOW | 9 | `tools/check-spec-tokens.py:231-232`; `tools/check-spec-tokens.test.sh:490-491` | The new docstring types "fourteen times" and "34 legs on the live manifest" undated and in present tense, one commit after round 2's R9 removed the header's count for exactly this; "fourteen" is the root-TOKEN count, and the sentence occurs 4 times. |

### R1 — MEDIUM · a trailing line continuation on the key line reads a declared default as absent (ids 1, 5)

`tools/unattended/unattended.sh:1548-1549`:

```sh
_sad=$( SPEC_AUDIT_DEFAULT=""; exec 3>&1
        eval "$_cf"$'\n''printf "OK %s" "${SPEC_AUDIT_DEFAULT:-}" >&3' >/dev/null 2>&1 )
```

`_cf` is `$(GIT show "$base:.unattended.conf")`, and command substitution strips the trailing newline, so a blob whose last line is `SPEC_AUDIT_DEFAULT="2026-09-21" \` ends in the backslash (`od`-verified). Glued with one `\n`, the shell sees `SPEC_AUDIT_DEFAULT="2026-09-21" printf "OK %s" "${SPEC_AUDIT_DEFAULT:-}" >&3` — a temporary-environment prefix on the sentinel, whose argument was expanded BEFORE the prefix took effect, from the variable the subshell blanked. The sentinel prints `OK `, the `"OK "*` arm accepts it, the `""` arm at `:1556` falls through, `AUTH_SPEC_AUDIT` stays blank, `AUTH_SPEC_AUDIT_DERIVED=1` is set at `:1565`, and the run proceeds as if the conf declared nothing.

Measured, the idiom sliced byte-for-byte under `set -u` (bash 5.3.9):

| blob's last lines | HEAD idiom | round-1 idiom | `bash -uc '. conf'` | two-newline glue |
|---|---|---|---|---|
| `SPEC_AUDIT_DEFAULT="2026-09-21"` | `OK 2026-09-21` | `OK 2026-09-21` | `2026-09-21` | `OK 2026-09-21` |
| `SPEC_AUDIT_DEFAULT="2026-09-21" \` | **`OK `** | no sentinel (fail 55) | `2026-09-21` | `OK 2026-09-21` |
| `SPEC_AUDIT_DEFAULT=""` then `…="2026-09-21" \` | **`OK `** | no sentinel | `2026-09-21` | `OK 2026-09-21` |
| `…="2026-09-21"` then `OTHER="x" \` | `OK 2026-09-21` | no sentinel | `2026-09-21` | `OK 2026-09-21` |
| trailing `false` · trailing `[ -n "${OPT:-}" ] && Y=1` · trailing comment, no NL | the date | (R6's cases) | the date | the date |
| `return 0` · `exit 0` · unbound · syntax error | no sentinel | no sentinel | — | no sentinel |

The hook's `readSpecAuditDefault` (`agent-cap.js:1778`) returns `null` for the backslash line (`(?:\s+#.*)?\s*$` does not admit ` \`), so three readers give three answers: the startup source sees the date, the hook sees no assignment, and the binding BASE read sees a declared-empty default. Then through the real driver: the `specs-audited` block with one probe arm (a `mkconf` with a blank default, then `SPEC_AUDIT_DEFAULT="2026-09-21" \` appended as the last line, committed on the fixture's `main` and merged into the run branch) prints `unattended: spec-audit — not owed (opt-in)` and `preflight OK`; at `--close` the grader would print `specs-audited — not owed … declares no SPEC_AUDIT_DEFAULT` (the `:3936` branch, reached because `DERIVED=1` was set). Nothing downstream catches it: the hook is consulted only on an audit call, and no audit is called. This is the silent read-as-absent opt-out fail 52, 54 and 55 were written to refuse, reached through the one path they did not cover, and it is a regression: the round-1 `eval && printf` idiom hit EOF inside the continuation and printed no sentinel. The comment at `:1528-1530` promises a typo never falls back to the default; here one does. Class: `two-readers-of-one-config-one-re-derived`.

Why MEDIUM: fail-open in the guarded direction, reproduced end to end, in a fold one round old. Why not HIGH: the trigger is a trailing `\` on the key line when that line is the conf's last statement — a typo class, unreachable on either shipped conf (both are pure assignments), and the last-wins override shape that would most plausibly produce it (`…="2026-09-22" \` appended after an existing date) reads the EARLIER date rather than absent, a wrong answer but not an opt-out.

**Fix.** Glue with TWO newlines so a trailing continuation consumes the first and the sentinel starts its own line:

```sh
        eval "$_cf"$'\n\n''printf "OK %s" "${SPEC_AUDIT_DEFAULT:-}" >&3' >/dev/null 2>&1 )
```

Verified on every shape in the table (the backslash blobs → the date; the four dying shapes → no sentinel; the R6 shapes unchanged) and through the driver: a copy of `unattended.sh` patched with that one character passes the whole `specs-audited` block, 114 assertions, with the probe reading `opted in by project default SPEC_AUDIT_DEFAULT: 2026-09-21`. Extend the comment at `:1543-1545` ("The `$'\n'` matters …") to say the second newline is for a blob ending in a line continuation, which would otherwise swallow the sentinel into a temp-env prefix.

**Left-shift.** One arm beside the R6 arm at `unattended.test.sh:5891`, with its OWN conf rather than `init_sa_base_ending_early`: `bcreset; git checkout -qf main; mkconf true true "" 3600 "" 1800 7 ""` (a BLANK default), then `printf '%s\n' 'SPEC_AUDIT_DEFAULT="2026-09-21" \' >> .unattended.conf`, commit, push, merge into `unit`; `run --preflight` → `hit 'opted in by project default SPEC_AUDIT_DEFAULT: 2026-09-21'`, `miss 'not owed (opt-in)'`; restore `main` to `$_sa_main0` and `bcreset`. Observed RED on HEAD and GREEN on the patched copy in this synthesis. Note that id 5's proposed shape, `init_sa_base_ending_early 'SPEC_AUDIT_DEFAULT="2026-09-21" \' 0`, does NOT red on HEAD: that helper's `mkconf` already writes the date, and the sentinel's argument expands from it (measured: `OK 2026-09-21`). The blank-default shape is the one that observes the break.

### R2 — LOW · the not-gradable branch names a cause that did not happen (id 7)

`unattended.sh:1480-1565`: `authorization-reachable` reads the README blob, parses its front matter and sets `AUTH_SPEC_AUDIT` from the README key BEFORE consulting the conf; fail 54 (`:1558`) and fail 55 (`:1552`) `return 1` from the conf half, and after the fold `AUTH_SPEC_AUDIT_DERIVED=1` sits after both halves (`:1565`), so those returns leave it blank — the R2 fix, working. But the branch they now land on, `:3926-3928`, says `specs-audited — not gradable: the README at BASE was not derived in this shell (authorization-reachable is unmet above)`, and its comment at `:3922-3925` says `this branch says the anchor is the cause`. Under fail 55 the README half completed and the conf blob was refused, three lines up in the same output. The fold's own arm at `unattended.test.sh:5789-5791` is exactly this fixture (a conf that dies with `return 0` at the merge-base) and `hit`s both the fail-55 line and the README sentence, so the misattribution is pinned as correct. Verdict right, attribution wrong. Class: `amendment-leaves-its-other-half-standing`.

**Fix.** Generalise the sentence and the comment to the three causes: `specs-audited — not gradable: the spec-audit source at BASE was not derived in this shell (authorization-reachable is unmet above: an unreachable anchor, a missing README, or a refused spec-audit:/SPEC_AUDIT_DEFAULT read), so whether this build opted in is unknown here`; update the `hit` at `:5658` and `:5791` to the new bytes.

**Left-shift.** The two existing arms, on the new bytes.

### R3 — LOW · the second `## open` spelling is split across two lines (id 6)

`skills/session-kickoff/SKILL.md:208-209` at HEAD:

```
Step 3's answer, or what answered for it: `spec audit: declared <date>`, `spec audit: not declared
(owner)` or `spec audit: project default <date>`) —
```

`grep -c 'not declared (owner)' skills/session-kickoff/SKILL.md` is 1 at `315201b0` and 0 at HEAD. KICK-1's AC3 names its evidence as a grep that finds the three spellings, round 2's R10 left-shift rests on it, and the file is the one the `reflowed-prompt-string-reads-as-a-deleted-stop` / `ledger-token-wrapped-across-a-line-joins-nothing` classes were catalogued for. Held at LOW because AC3's actual command is `grep -n 'spec audit:'`, which still hits both lines, no machine reader greps the full spelling, and nothing reds; the record's evidence is weaker than it reads, not wrong.

**Fix.** Move the break before the token, byte-neutral (a newline and a space swap places): line 208 ends `…`spec audit: declared <date>`,` and line 209 reads ``spec audit: not declared (owner)` or `spec audit: project default <date>`) —`. The engine is 18428/18432, so nothing else moves. Re-run AC3's grep and `check-template-size.sh skills/session-kickoff/SKILL.md`.

**Left-shift.** `kickoff engine size <=18KiB` holds the cap; AC3's grep, with the three literal spellings, is the documented check.

### R4 — LOW · the residual is stated in one direction (id 10)

Header `:60-62` and the `check_dir_shaped` docstring `:266-269` both say "The residual, stated: a two-segment directory named in prose is still read as declared." The same cut has a second side: a one-segment directory that is ITSELF a joined guard, declared wholesale under the sub-head, now declares nothing. On the live manifest `derive_guarded_legs` keeps `.githooks/` (5 legs), `.claude/` (2) and `memory/` (2) in the join — only `tools/` (11) is broad among the one-segment guards. Measured on fixture D (LIVE manifest, `Edited: `.githooks/`.` under the sub-head, spec dated 2026-09-23): exit 0, zero hits, and the one row `.githooks/ — a one-segment root declares nothing, not joined`, which names the skip and not the remedy. An author who means the hooks directory gets a green join and five un-owed names. The corpus today has no such declaration on a live post-cutoff spec (aQuarriedLantern-1 `:547` declares `memory/` indexes, TREE files, ledger` as a genuine write-set row and `--list` shows it as that NEAR row with the two `memory/` recall legs un-owed, but it predates the cutoff), so this is the header's completeness under the §7 rule that a gate states what it does not check, not a live red. It is the other half of the `a-view-fix-trades-one-blindness-for-another` cut round 2's R1 made.

**Fix.** Header and docstring: "…and a one-segment directory that is itself a joined guard, `.githooks/`, must be declared by its files or by a two-segment child." NEAR text at `:552`: `a one-segment root declares nothing, not joined — name the files or a directory of two or more segments`. Update the R1 arm's expected substring at `check-spec-tokens.test.sh:498`.

**Left-shift.** The R1 `--list` arm, on the new text; nothing machine-shaped sees the sense.

### R5 — LOW · the `tools/./` refusal is asserted by prose (id 8)

`check-spec-tokens.test.sh:519-521` and the label at `:531` say `./`, `../` and `tools/./` are not declared paths. The fixture is a no-Gates spec declaring `tools/x/thing.sh` · `./` · `../` · `tools/./` against guard `tools/x/`. A mutant whose `derive_dir_segments` refuses only a LEADING `''`/`.`/`..` segment — so `./` and `../` are still refused and `tools/./` is admitted — produces `--list` output byte-identical to HEAD's on that fixture (one NEAR row, `0 declared path(s) examined`) and passes every arm of the suite that runs on a copied checker. Cause: a no-Gates spec adds a NEAR row only for a declared path that trips a joined guard (`:560-561`), and `check_guard_trips('tools/./', 'tools/x/')` is false. The refusal IS load-bearing elsewhere: on fixture E (a Gates-carrying spec, bare `tools/` guard carried by one leg) HEAD reports `1 declared path(s) examined` and the mutant reports `2` plus a hit `bare leg <- tools/./`, because `'tools/.'.startswith('tools/')`. So the `./` and `../` halves are observed (a lost refusal makes them one-segment roots and a second NEAR row) and the `tools/./` half is not. Class: `fixture-passes-by-finding-nothing`.

**Fix.** Assert the dot refusal where it is visible: add `./` · `../` · `tools/./` to the breadth arm's one-leg bare-`tools/` fixture (`:467-469`) and assert `1 declared path(s) examined` with exit 0; or drop `tools/./` from the label and comment.

**Left-shift.** That arm; RED first against the mutant shape above.

### R6 — LOW · U7's estimate omits the BUILD-METHOD carriers (id 11)

`…spec-TOOL-aBlindedTrial-7.md`: S5 (`:44-47`) names `BUILD-METHOD.template.md` and its render as scope (rev-2, R5); the `### Files touched (estimate)` block (`:80-86`) lists neither; the §7 leg line (`:142`) omits `kit/dogfood doc parity`, and that leg is the ONLY one whose guard carries `memory/guides/BUILD-METHOD.md` (`tools/gate-legs.json`, an exact-file guard). `git log` shows this build edited both files in `315201b0` and again in `312213ec` (R12's M4 heading). The rev-2 log line touched S5 only. The guards join reads the estimate as written, so the omission is invisible to it by construction, and the leg is named only through U8's `memory/TEMPLATE-SPEC.md` path. The spec is dated 2026-09-21 against a cutoff of 2026-09-22, so nothing reds; the record is inconsistent with itself (S5 versus estimate versus §7) in the unit whose sibling's product is this join. Classes: `hand-named-gate-list-green-while-the-bar-reds`, `amendment-leaves-its-other-half-standing`.

**Fix.** Add the two carriers to U7's estimate and `kit/dogfood doc parity` to its §7 leg line, with a rev-3 line naming §4 and §7; `--list` then shows the spec's NEAR row for that leg gone.

**Left-shift.** Records; `spec tokens` and hygiene hold the shape.

### R7 — LOW · a fresh derived count, typed where the last one was removed (id 9)

`git show 312213ec -- tools/check-spec-tokens.py` shows one commit both removing the header's "several legs guard bare `tools/` and thirty guard `tools/lib/`" (round 2, R9) and adding, at `:231-232`, "the corpus writes "No file under `tools/` is touched" fourteen times, and reading that as declaring the whole root owed 34 legs on the live manifest" — undated, present tense, keyed to "the live manifest" rather than a sha, while the file's sanctioned form is the dated `Measured on the manifest at 144cd1fb` beside `BROAD_LEG_FLOOR` (`:140-144`) and its header still says "no count of it lives in prose". Measured at HEAD: the exact sentence occurs **4** times in spec files (11 across `memory/builds/` counting the review records that quote it); **14** is the count of one-segment `tools/` TOKENS `extract_files_touched` returns over every spec, which round 2's R1 reported as prose of several shapes. The docstring's figure is the token count wearing the sentence's name, wrong on the commit that typed it, and `check-spec-tokens.test.sh:490-491` types the "34" a second time. Class: `two-answers-to-one-question`, R9's class one commit later.

**Fix.** Date it or drop it: `(round 2, R1, measured at 315201b0: a one-segment `tools/` token appeared 14 times over every spec, every one prose, and reading it as declared owed 34 legs)`, or `(round 2, R1: the corpus's most common negation sentence, which read as declaring the whole root)` and let the review record carry the figures. Same treatment for the test comment.

**Left-shift.** The report line carries the derived figure; prose stops carrying one.

## Observed, not a finding

Stated so the next reader does not re-derive it.

- A two-segment declared prefix that is itself BROAD still trips the legs UNDER it: fixture B declares `tools/run-gates/` (6 legs, excluded) and owes `run-selftests self-test`, whose guard sits under that prefix. That is round 1's R3 symmetric arm doing what it was asked, and the printed excluded set is what to decide any change from. Not adjudicated.
- A blob whose last line is a NON-key assignment with a trailing backslash (`OTHER="x" \`) reads the date on HEAD, because the sentinel's argument expands from the key set above it. R1's trigger is specifically the key line.
- The root NEAR rows are emitted for pre-cutoff specs too, with no `predates` suffix; they name a skip, not a demand, so the omission is consistent with what the row says.

## By design — not re-reported

Stated in the brief and confirmed unchanged at source; none of these is a finding.

- The hook reads the WORKTREE conf and the driver reads BASE — `agent-cap.js:1832-1834`; the BASE read binds.
- A bare `spec-audit:` line falls to the conf at the hook and is refused (fail 52) by the driver.
- Broad guards excluded by the leg-count floor — `BROAD_LEG_FLOOR = 5`, the excluded set printed with counts on every run.
- One hit per missing leg, not per (leg, path) — `:572-575`.
- No per-build opt-out under a project default — U7 §3.
- No version marker on the kickoff engine — KICK-1 §3.
- The `;`-joined conf line reads as no assignment at the hook and denies.

## Closed from round 2, observed

R1 (root → NEAR, zero hits on the live sentence, fixtures A/A2), R2 (`DERIVED=1` after both halves, the fold's `--close` arm green through the real driver), R3/R4/R9/R10/R11/R12 (the carriers read at HEAD), R5 (`manifest-check.sh` rc 0 at HEAD), R6 (the in-eval sentinel, the trailing-`false` arm green), R7 (`set(...)` at `:296`, the duplicated-entry arm green), R8 (dot tokens refused, `0 declared path(s) examined in 0 live spec(s)`, the NEAR row named).

## Checklist classes run

`gotchas.py --for-diff 315201b0..HEAD` selected 31 classes by anchor + 5 universal. Produced a confirmed finding: `two-readers-of-one-config-one-re-derived` (R1), `amendment-leaves-its-other-half-standing` (R2, R6), `reflowed-prompt-string-reads-as-a-deleted-stop` and `ledger-token-wrapped-across-a-line-joins-nothing` (R3), `fixture-passes-by-finding-nothing` (R5), `hand-named-gate-list-green-while-the-bar-reds` (R6), `two-answers-to-one-question` (R7). R4 is the unstated half of round 2's `a-view-fix-trades-one-blindness-for-another`. Run and clean on this range: `containment-tested-one-way` (fixtures B and C trip both directions), `heredoc-escape-reaches-the-regex` (no conf value enters a pattern), `two-guards-one-question-two-answers` (the hook and the driver disagree on R1's blob, but the driver's own answer is the finding, filed once).

## Left-shift summary

| # | Gate or documented check |
|---|---|
| R1 | `unattended.test.sh`: a blank-default `mkconf` plus `SPEC_AUDIT_DEFAULT="2026-09-21" \` as the conf's last line → `opted in by project default …`; RED on HEAD, GREEN on the `$'\n\n'` glue (both observed). |
| R2 | The two existing `not gradable` arms, on the generalised sentence. |
| R3 | `kickoff engine size <=18KiB`; AC3's grep with the three literal spellings. |
| R4 | The R1 `--list` arm's expected substring, on the text that carries the remedy. |
| R5 | `check-spec-tokens.test.sh`: dot tokens on the one-leg bare-`tools/` fixture → `1 declared path(s) examined`, exit 0. |
| R6 | Records; `spec tokens` holds the shape. |
| R7 | The report line carries the figure; prose stops. |

State at synthesis: `branch/spec-audit-followups` at `312213ec8ad9` · base `315201b0cf4c` · `check-spec-tokens.test.sh` 66/66 · `manifest-check.sh` rc 0 · `check-template-size.sh` SKILL.md 18428/18432 · driver `specs-audited` block 94 arms green at HEAD plus one probe RED · bar not run · driver suite whole not run.

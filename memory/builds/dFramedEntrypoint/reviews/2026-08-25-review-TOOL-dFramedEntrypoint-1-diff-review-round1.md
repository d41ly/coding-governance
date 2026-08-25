**Serves:** diff-review TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8

# Diff review round 1 — the cumulative diff landing on main

**Reviewed range: `470bb09ba977030f5c651c55e813bc6e5bd53b03...HEAD` (HEAD = `beb5fce43e2680983f01732975ae005b004eb980`). ROUND 1.**

*Node d, 2026-08-25. Adversarial finder fan over the built code, then skeptics prompted to REFUTE each finding, then this synthesis. Ten commits, 363 files, +5339/-2236; the review's weight sits on `tools/memory-tree/gen_build_index.py` (+1204 lines changed) and `tools/memory-tree/adopt-memory-tree.sh`.*

## Verdict: BLOCKED

### Review shape

Raw 25 · confirmed 24 · refuted 1 · unverified 0 · precision 0.96.

Surviving by severity: **3 BLOCKER · 6 HIGH · 10 MEDIUM · 5 LOW**.

One of the three blockers is **already fixed at HEAD** and is recorded below for the left-shift it still owes, not for work. **Two blockers remain open**, and both of them fail GREEN — that is the through-line of this round and the reason the verdict is BLOCKED rather than CLEAN WITH FIXES.

The 24 confirmed findings collapse to **15 distinct defects**; several finder lenses reached the same code from different directions. Each defect below names every finding id that reached it, so nothing is lost in the merge. Every one of these was reproduced, not reasoned about.

### Caveat on symbol names and line numbers

Every `file:line` below was re-resolved against the committed HEAD `beb5fce4`, not against the working tree. **A concurrent session is mid-rename in this worktree** and has staged a verb-table conformance pass over `tools/memory-tree/gen_build_index.py` — `_read_slot_table` → `read_slot_table`, `_assert_slot_table` → `check_slot_table`, `slot_sizes` → `measure_slot_sizes`, with `memory/map/generated/symbols.json` regenerated to match. That work is uncommitted and outside the reviewed range, so this record uses the names as they exist at HEAD. A reader checking the working tree will find the new spellings; the defects are the same code either way, and none of them is fixed by the rename.

### The shape of what was found

Four of the fifteen defects are the same failure mode wearing different clothes, and it is this repo's own named class: **a check that cannot fail.** A ceiling file whose values were blanked in a landed commit while the leg stayed green. A heading canon that one duplicated line switches off entirely, still printing `slot contract clean`. A test-arm label left standing over the retirement note that replaced its assertion. An exemption pointing at a documented manual check that was never written. The diff introduced the enforcement and the ways around it in the same pass.

---

## BLOCKERS

### D1 — the adopter blanks the governance checkout's own ceilings, and the bar stays green

**Findings: 20 (blocker) · 7 (high) · 14 (high) · 2 (high). Severity taken from the highest member. OPEN, and the damage has LANDED.**

`tools/memory-tree/adopt-memory-tree.sh:143`

```sh
awk -F'\t' 'BEGIN{OFS="\t"} /^## /{ print $1, ""; next } { print }' \
  "$HERE/build-readme-slot-limits.txt" > "$HERE/.slot-limits.tmp" \
  && mv "$HERE/.slot-limits.tmp" "$HERE/build-readme-slot-limits.txt"
```

This is the only write in the entire script that lands outside `$ROOT`. Lines 40, 79, 80, 83 and 250 all read from `$HERE` and write under `$ROOT`, which is the invariant the script's own comment states verbatim: every asset is read from `$HERE` and every file is written under `$ROOT`. This block reads the kit's source file and writes back over it.

The flow that triggers it is not exotic — the same script's header explicitly blesses and keeps alive the run-the-shipped-adopter-from-the-governance-checkout-against-a-fresh-repo flow. In that flow `$HERE` is gov's own `tools/memory-tree/`, so scaffolding somebody else's repo strips gov's ceilings. The early already-scaffolded exit means the strip only ever runs when `$ROOT` is some other tree, so the destructive case is the only case. The target repo never receives the stripped file at all.

It already happened. `tools/memory-tree/check-memory-hygiene.test.sh:1168` runs the adopter from a temp repo with `$HERE` pointing at the real kit directory, so the kit's own self-test strips the tracked declaration on every run. Commit `beb5fce4` then committed the blanked file: its stat carries `tools/memory-tree/build-readme-slot-limits.txt | 10 +++---`, its message enumerates four deliberate fixes and never mentions this one, and its trailer reads `Gates: ... slot contract ... all GREEN`.

Verified at HEAD in this worktree, working tree clean:

```
$ grep -n '^## ' tools/memory-tree/build-readme-slot-limits.txt
27:## The problem this build exists to solve<TAB>
28:## Expected improvements<TAB>
...five rows, five empty values...

$ python tools/memory-tree/gen_build_index.py --check-format
build-index: NOTE 5 canonical slot(s) ship UNARMED — no declared ceiling: ...
build-index: slot contract clean (62 build README(s); heading canon BOUND on 1)
rc=0
```

The declared ceilings 900/500/500/1800/1800 are gone from committed code. `TOOL-dFramedEntrypoint-2`'s hard half currently enforces nothing.

**Why nothing reds.** A row with no value is the legal ANNOUNCED-UNARMED state, so `_assert_slot_table` does not raise, the rows survive so no row-count refusal fires, and `kit.toml`'s `slot-budget-ceilings` discharge probe carries `blocks_gate = false`. This is failure by construction, not by accident: every guard around the file was designed to tolerate exactly the state the bug produces.

**Fix.** Never write under `$HERE`. Write the stripped copy to the target at `$ROOT/$KIT_REL/build-readme-slot-limits.txt` and leave the kit source read-only like every other asset the script consumes. When `$HERE` sits outside `$ROOT` — the `KIT_REL` fallback branch already detects this — skip the in-place rewrite entirely and print the strip instruction for the operator to run after the `cp -r`. Separately and before landing, **restore the five ceiling values**; they are blank in committed code right now.

**Left-shift gate.** Two legs, because one covers the mechanism and the other covers the outcome:

1. An adopter invariant arm: run `adopt-memory-tree.sh --scaffold` from a scratch repo against a throwaway copy of the kit, then assert the KIT COPY is byte-identical to its pre-run state. This catches any future write under `$HERE`, not just this one. It is three lines and would have caught this on the commit that introduced it.
2. Flip `slot-budget-ceilings`'s discharge probe to `blocks_gate = true` in gov's own `kit.toml`, so an unarmed ceiling in THIS repo reds. The hole exists so that adopters may ship unarmed; gov measured its corpus and has no such excuse. As it stands, the announced-unarmed state is indistinguishable from a deliberate configuration in the one tree where it is neither.

---

### D2 — one duplicated heading switches the entire heading canon off, silently and green

**Finding: 6. OPEN.**

`tools/memory-tree/gen_build_index.py:1183`

`_canon_violations` returns an empty list when a canonical heading appears twice, and the caller reads an empty list as clean. The `if got != want:` branch fires, but none of its three sub-checks can match a duplicate:

- `outside the canon` cannot fire — the duplicate IS in `want`.
- `missing` cannot fire — all five canonical headings are present.
- out-of-order cannot fire — `[g for g in got if g in want].index(h)` returns the FIRST occurrence, which still sits at its correct index.

So `out` stays empty and the branch `return`s **before** the body loop that grades empty bodies and bullet lists. One appended line disables trigger 3 completely.

Reproduced against the one BOUND README, `memory/builds/dFramedEntrypoint/README.md`:

| input | `_canon_violations` returns |
|---|---|
| mandatory description emptied | `[(12, 'canonical slot has an empty body and may not: ## The problem this build exists to solve')]` |
| second `## Parked decisions` appended | `[]` |
| both together | `[]` |

`--check-format` still prints `slot contract clean`. The selftest has arms for out-of-order, missing, empty-body and bullets — and none for a duplicate, which is why it shipped.

**Fix.** Detect repeats explicitly before the ordering loop:

```python
for h in {x for x in got if got.count(x) > 1}:
    out.append((seen_index[h], f'canonical slot appears more than once: {h}'))
```

And never let the `got != want` branch return an empty list — fall through to a generic `(title + 1, 'heading sequence does not match the canon')` when nothing more specific fired. A branch that has decided something is wrong and then reports nothing is the bug, independent of which specific case exposed it.

**Left-shift gate.** A selftest arm that duplicates the LAST canonical heading over a fixture whose description body is ALSO empty, asserting the empty-body violation still fires. Duplicating a heading over a clean fixture would pass today by accident — the arm has to prove the body checks still run, not merely that something was reported. Generalise it as a two-line invariant test: for every fixture the suite already breaks, break it AND duplicate a heading, and assert the original violation survives.

---

### D3 — the unterminated grep that killed the adopter mid-scaffold

**Finding: 1. CLOSED at HEAD by `beb5fce4` — recorded for the left-shift it still owes.**

`tools/memory-tree/adopt-memory-tree.sh:167` (at `94b6195f`)

Under `set -eu`, the `readme-contract.txt` seeding assigned `_rc=$(... | grep -E "^$M/builds/[^/]+/README\.md$")`, and on a fresh scaffold that grep matched nothing, so the assignment exited 1 and killed the adopter. Since `$M/builds/` had just been created empty, the only path reaching that line was one where the grep could not match — 100% of adoptions failed.

Reproduced against the sha it cites: extracting `94b6195f`'s script into a clean scratch repo and running `--scaffold` exits 1 after writing 11 files, leaves `memory/project/readme-contract.txt` holding its comment header with no `exempt-pin:` line, and never writes `method-carriers.txt`, `builds/`, `backlog/`, `guides/SESSION-KICKOFF.md` or `LIVE.md`. The half-tree is then permanent: `memory/HYGIENE.md` had already been written carrying the `gov:kit memory-tree@` marker, so the idempotence guard makes every re-run print `memory/ already scaffolded by memory-tree — nothing to do` and exit 0.

A concurrent session fixed it in `beb5fce4`, whose message calls it out by name and bisects it across `470bb09b`/`4ab1f121`/`94b6195f`. Current lines 158-159 terminate every probe with `|| true`, and the same scratch run against the current script completes with exit 0 and `exempt-pin: 0`.

**No fix owed.** The debt is the gate.

**Left-shift gate.** No arm in this build exercised the adopter at all, which is how a scaffolder that could not scaffold reached three commits. Add an end-to-end acceptance arm: run `adopt-memory-tree.sh --scaffold` in a fresh scratch repo and assert **exit 0 AND the full expected file set**, not merely exit 0 — the failing run wrote 11 real files before dying, so an exit-code-only arm is weaker than it looks. Pair it with the D1 arm above; both drive the same entrypoint and neither exists.

---

## HIGH

### D4 — `--bump` duplicates every high-water row on every run

**Findings: 12 (high) · 21 (high) · 3 (medium). OPEN.**

`tools/memory-tree/gen_build_index.py:1574`

```python
keep = [l for l in read_text(p).split("\n") if not l.strip() or l.lstrip().startswith("#")]
```

Every canonical slot row starts with `## `, so all five data rows satisfy `startswith("#")`, survive the keep filter, and are then re-appended. Reproduced on the live tree: `build-readme-slot-highwater.txt` goes 5 rows → 10 → 15, with each slot present N times after N invocations.

This is the exact trap `_read_slot_table`'s own docstring, ten lines earlier, documents as a bug this repo already paid for once: **a comment is a line with no tab, never a line starting with `#`.** The reader was fixed; the writer one function away reproduces it inverted.

`_read_slot_table` is last-wins so values still resolve correctly today, and `_assert_slot_table` only checks heading presence and membership — so nothing catches the accumulation. The damage is not cosmetic: when a high-water is LOWERED, the superseded higher row sits ABOVE the live one, and the file stops being a readable record of anything. Any future first-wins or duplicate-detecting reader gets the stale ceiling. The file is LF-pinned and tracked, so it grows five rows per invocation forever.

`--bump` is the only documented writer of this file and has **zero selftest arms** anywhere — nor do `do_report` or `do_survey`.

**Fix.** Reuse the reader's own predicate in the writer: `keep = [l for l in ... if not l.strip() or "\t" not in l]`.

**Left-shift gate.** An arm that calls `do_bump` **twice** over a fixture and asserts the file is byte-identical after the second run. Idempotence is the right assertion rather than a row count, because it also catches ordering churn and trailing-blank drift. Given that all three of `do_bump`/`do_report`/`do_survey` are untested, the honest gate is a smoke arm per verb — the module's verb table should not have entries nothing ever calls.

### D5 — a live refusal lost its only test arm, and the label stayed

**Finding: 13. OPEN.**

`tools/memory-tree/gen_build_index.py:1687`

The `# AC2 — an unpaired marker is a NAMED error` heading now sits directly over a retirement note that justifies retiring the **sentence-removal** arms and never mentions AC2 at all. The assertion it labelled is gone. `git show e3f006c9^:tools/memory-tree/gen_build_index.py` shows the arm as it was: a `nomark` fixture built via `_fixture(t3, marker=False)` asserting the refusal text `expected exactly one '<!-- gen:build-index -->' marker pair, found 1 open and 0 close`.

Corroborated by a dead parameter — `_fixture`'s `marker=True` keyword now has no caller anywhere passing `False`. `grep -n "unpaired marker\|nomark\|expected exactly one"` returns only the raise site and the orphaned comment.

The refusal itself is still live at line 907, and `plan()`'s own comment calls it the only thing standing between a build README and a hand-authored status block, citing a **measured control** where deleting four marker lines left `--check`, `--check-format` and the whole hygiene gate green. That guard now has no coverage while its heading reads as coverage — this repo's own could-not-fail class, at the test layer.

**Fix.** Restore the arm: rebuild the `nomark` fixture via `_fixture(t3, marker=False)` and assert `plan(t3, conf3)` raises with the exact refusal text. Move the retirement note BELOW the restored arm so the AC2 label sits over its own assertion again.

**Left-shift gate.** Beyond restoring this arm: a structural check that every `# ACn —` label in the selftest is followed by at least one `arm(` or `raises(` call before the next `# ACn` label. A label with no assertion under it is mechanically detectable, and this diff proves it is worth detecting.

---

## MEDIUM

### D6 — the high-water file ships gov's measurements to adopters, unstripped and undeclared

**Findings: 10 · 15 · 23. OPEN.**

`tools/memory-tree/build-readme-slot-highwater.txt:19`

`kit.toml:16-18` declares the file `role = "seed"`, and `LANDABLE_ROLES = ("engine", "seed")` in `tools/govkit/govkit.py:230` puts seed rows in the write set — so it lands in an adopter verbatim. `grep -c highwater adopt-memory-tree.sh` returns 0: unlike its twin, it is never stripped, and unlike its twin it has no declared `kit.toml` hole.

Adopters therefore inherit 693/435/397/720/480 measured against **gov's** build READMEs. This is precisely the failure the sibling `slot-budget-ceilings` hole exists to prevent, in the ceilings file's own words: a pin measured against this corpus and shipped into a tree that never measured it is either vacuous or permanently red. The asymmetry is undocumented anywhere. With the ceilings stripped and these not, the adopter's only armed number is the one nobody argued was portable.

The file's header also contradicts its contents: it says it is EMPTY of rows today because the declared population is empty, while `grep -c '^## '` returns 5. The rows landed in `0d06b045`; the prose describing them did not move.

**Fix.** Strip the high-water rows in the adopter alongside the ceilings — same awk, same rows-survive rule — or drop the file from the `[[files]]` seed rules so adopters start with no baseline and earn one from their first `--bump`. An absent high-water is already declared legal by the file's own header. Either way, correct the header to describe the rows the file actually carries.

**Left-shift gate.** Extend the adopter invariant arm from D1: after a scaffold, assert that **no** file the adopter ships carries a gov-corpus measurement. Concretely, assert every `^## .*\t[0-9]` row is absent from the adopter's tree. That is one predicate covering both declaration files and any third one that appears later, rather than a rule per file.

### D7 — 61 of 62 build READMEs lost their final newline, and the loss is a stable fixed point

**Finding: 8. OPEN.**

`tools/memory-tree/gen_build_index.py:1336`

When a dead region is the LAST block in the file, `while end < len(lines) and not lines[end].strip()` consumes the final empty element produced by the trailing newline. Reproduced directly: `remove_dead_regions("# T\n\nbody\n\n<!-- gen:build-docs -->\nx\n<!-- /gen:build-docs -->\n")` returns `'# T\n\nbody'`.

Corpus effect measured at HEAD: **61 of 62** `memory/builds/*/README.md` end without `0x0a`; the same files at the merge-base end `0a`. `DEAD_REGIONS` holds the single `build-docs` pair, which sat last in those files.

It will never self-heal. `plan()` renders the same newline-less text, so `--check` reports clean, and no hygiene leg inspects final newlines. Any consumer using `while IFS= read -r` over one of these files silently drops the last line.

**Fix.** Restore the terminator after the `DEAD_REGIONS` loop — `if not readme_text.endswith("\n"): readme_text += "\n"` — or stop `end` advancing onto the final element with `while end < len(lines) - 1 and ...`. Re-run `--write` so all 61 files regain the byte.

**Left-shift gate.** A hygiene-leg assertion that every tracked text file under `memory/` ends in `\n`. This is a POSIX invariant, it is one line of shell, it covers every generator rather than this one, and the fact that a 61-file regression landed green says the check is overdue. Add a selftest arm too, asserting a README whose dead region is the last block still ends in `\n`.

### D8 — trailing whitespace on a heading passes the canon and vanishes from the budget

**Finding: 9. OPEN.**

`tools/memory-tree/gen_build_index.py:1042`

`slot_sizes` matches canonical headings by exact line equality (`lines[i] in heads`), while `_canon_violations` records them after `l.rstrip()`. One trailing space therefore passes the canon and is invisible to the byte budget.

Measured on the bound README with one trailing space added to `## Expected improvements`: `slot_violations(..., canon=True)` returns `[]`, `slot_sizes` drops the slot entirely, and its 435 bytes are billed to the PRECEDING slot, which goes 693 B → 1157 B. Against a 900 B description ceiling that reds the wrong slot; where the neighbour has headroom, the whitespaced slot's ceiling goes unenforced with nothing reported at all. `--report` also omits the row, so the margin table is short.

No gate strips or rejects trailing whitespace on a heading, so a routine authoring slip reaches this.

**Fix.** Normalise both sides identically — compare `lines[i].rstrip()` against `heads` in `slot_sizes`, keeping `i` for the slice bounds.

**Left-shift gate.** A selftest arm feeding a trailing-space heading to both functions and asserting **they agree on the slot set**. Agreement between the two readers is the real invariant; asserting either one in isolation would have missed this. Where two functions parse one grammar, the gate belongs on their agreement, not on their outputs.

### D9 — `remove_dead_regions` is fence-blind and does not validate its pair count

**Finding: 4. OPEN — mechanism proven, reachability latent.**

`tools/memory-tree/gen_build_index.py:1333`

The function takes `_marker_index`'s FIRST hit for open and FIRST for close, deletes everything between them plus all adjoining blank lines, and does so with no pair-count validation and no fence awareness — in a function whose subject is an **authored** file.

Proven with a fixture: called on a README body whose `Parked decisions` slot quotes the retired marker pair at column 0 inside a fenced block, everything between the two quoted marker lines is deleted, leaving an empty broken fence and orphaned prose.

The asymmetry is the finding. `apply_region` at line 906 refuses outright on `len(opens) != 1 or len(closes) != 1` over exactly this class of ambiguity, on the same file. The deleter that now runs BEFORE it takes the first index of each and deletes. The retired `strip_records_sentence` was made fence-aware after this repo shipped a cut that rewrote a fenced quote, and its docstring says a scanner that ignores fences is wrong by construction — that lesson did not transfer to its replacement.

Honest caveats that hold this at medium: zero build READMEs mention the marker today, `--check` reports the loss as drift before `--write` eats it, and the deletion shows in `git diff`. The reason it is a defect anyway is that the deleter is **permanent** while its legitimate target no longer exists in any README — every input it can ever fire on from here is a false positive.

**Fix.** Reuse the existing `unfenced_lines()` helper to skip fenced marker lines, and RAISE `Problem` rather than delete when the count of opens or closes is not exactly one — the same contract `apply_region` already enforces one function away.

**Left-shift gate.** An arm asserting `remove_dead_regions` leaves a fenced marker quote byte-identical, plus an arm asserting it refuses on a doubled pair. The general rule worth writing into the module: any scanner over an authored file skips fences, and any scanner that deletes validates its pair count first.

### D10 — the contract registry does not check its own two row kinds against each other

**Finding: 16. OPEN.**

`tools/memory-tree/gen_build_index.py:1118`

`read_contract_rows` builds `exempt` as a dict and `bound` as a set with no cross-check, so two malformed states pass every assertion including the equality pin. Reproduced by driving the real functions against scratch copies of the tracked registry:

- A path declared BOTH bound and exempt passes with the pin raised by one. `named = bound | set(exempt)` dedupes, so FORWARD and REVERSE both see it, and `do_check_format` then grades — via `canon=rel in bound` and `budget_findings` — a file the registry declares exempt.
- A duplicated exempt row passes with the pin unchanged. `exempt[path] = why` overwrites, so the duplicate is literally uncountable by the pin.

The file's own header declares the two row kinds mutually exclusive and sells `exempt-pin` as the equality that stops the shrink-only list from silently stopping its shrink. Neither claim is enforced. The contradiction resolves in the fail-safe direction — the file is still graded, and duplicates do not widen the exempt set — which is why this is a medium and not a high, but it is an unenforced invariant in a declared population this very diff introduces.

**Fix.** In `read_contract_rows`, refuse a path already present in the other collection, and refuse a repeat of a path already seen in either — each with its row number. Both are three lines and make the pin an honest count.

**Left-shift gate.** Two selftest arms over a scratch registry, one per malformed state, asserting a NAMED refusal rather than a rc. The broader rule: wherever a declaration file defines two row kinds, the parser asserts they are disjoint — the pin cannot do it, because the pin counts what the parser already collapsed.

### D11 — a deliberate gate exemption names a documented check that does not exist

**Finding: 24. OPEN.**

`tools/memory-tree/gen_build_index.py:13`, repeated at `:1209` and `:1489`

All three sites assert that the description's immutability is a DOCUMENTED check in `memory/HYGIENE.md`. It is not there. Grepping that file for `immutab|first authored|description block|README|check-format|build-index` returns nothing on the subject — its only `description` hit is about gotchas front matter, and its README hits are the entry and byte caps and the build-index drift check, none of which grade whether a build README's description is the one first authored. `git diff main -- memory/HYGIENE.md` is a single line: the kit-version bump 2.30 → 2.36.

This is §7's *an exemption is not coverage* rule, failed in the direction that reads as covered. A reader who follows the pointer finds nothing and cannot distinguish a missing check from a wrong filename.

**Fix.** Write the check into `memory/HYGIENE.md` and mirror it into `tools/memory-tree/HYGIENE.template.md` — stating what an author must verify by hand about a description slot and why it is ungateable. Otherwise delete all three claims and say plainly that immutability is unchecked. Both are acceptable; the current state is not.

**Left-shift gate.** A cheap, general leg: every in-repo prose reference of the form *a DOCUMENTED check in `<file>`* resolves to a matching anchor in that file. This is a grep-shaped check over a small population and it catches the whole class of exemptions that point at nothing — which is the class §7 already names and this repo keeps re-entering.

### D12 — the advisory prints `under its None B ceiling`

**Findings: 22 (medium) · 18 (low). OPEN, and reachable in gov today.**

`tools/memory-tree/gen_build_index.py:1067`

The `elif hw is not None and size > hw` branch is entered whenever the hard branch is false, which includes `cap is None`, and the message interpolates `cap` unconditionally. Reproduced verbatim against a scratch copy of the bound README with one slot grown 400 B:

```
slot `## Expected improvements` is 839 B, past its recorded high-water of 435 B and under its None B ceiling
```

Both findings' caveat that this is adopter-only is already stale. D1's damage blanked all five ceilings in **this** tree while the high-water file still carries 693/435/397/720/480, and `--report` on the real tree prints all five slots as ceiling UNARMED with sizes exactly equal to their high-waters. A single byte of growth in the one bound README emits the nonsense line here, today. In adopters it is the permanent normal state.

The advisory asserts a bound that does not exist, in the one output a reader is meant to act on before a breach.

**Fix.** Branch the tail on `cap is None`: emit `past its recorded high-water of {hw} B; no ceiling is declared for this slot` when unarmed, and keep the current wording only when `cap` is an integer.

**Left-shift gate.** An arm driving `budget_findings` with `cap=None, hw=<int>, size>hw` and asserting `None` does not appear in the emitted string. Generalise it to the module's other f-string emitters: no operator-facing message may contain the literal `None`. That is one assertion over all of them and it is worth more than the single arm.

---

## LOW

### D13 — two hand-run verbs traceback where the gate leg gives a named refusal

**Findings: 5 · 19. OPEN.**

`tools/memory-tree/gen_build_index.py:1558` (`do_report`) and `:1571` (`do_bump`)

Both call `read_contract_registry` without `assert_contract_registry`, unlike `do_check_format` at `:1495`. Reproduced by appending one bare row naming a nonexistent build README: `--report` and `--bump` both die with an uncaught `FileNotFoundError` out of `read_text`, while `--check-format` on the identical tree prints the registry's own refusal naming the bad row. `main()` catches only `Problem`, so nothing converts it.

`do_survey` survives by accident — it iterates tracked files and uses `bound` only as a tag.

One tree, two entry points, two qualities of message, and the traceback lands on exactly the verbs an author runs between edits — including right after deleting a build folder, which is when the stale row exists. It also violates the module's own selftest AC4: an absent README is a named error on BOTH modes, never a traceback. Severity is low because the failure is loud and the merge-bar leg still refuses correctly.

**Fix.** Call `assert_contract_registry(root, conf, tracked)` at the top of both verbs, deriving `tracked` the way `do_check_format` does. Both already need the git listing.

**Left-shift gate.** An arm per verb over a registry with a dead bound row, asserting a `Problem` rather than an `OSError`. Better as one parametrised arm across every verb that reads the registry, so a verb added later is covered by construction — the reason `do_survey` is fine today is luck, not design.

### D14 — a dead `docs` key computed for 62 builds on every run

**Finding: 17. OPEN.**

`tools/memory-tree/gen_build_index.py:689`

`collect()` still builds the `docs` key for the document-inventory region, whose only consumer `render_docs` was deleted in this diff. `grep -n '"docs"'` returns exactly one hit, the producer; `grep -rn 'def render_docs' tools/` returns none. The value is a per-build comprehension over the whole tracked list times `RECORD_KINDS`, computed on every `--check`, `--write`, `--check-format` and `--selftest` for all 62 builds, and read by nothing.

Its comment still names the removed region and its retired filename-grammar rationale, so the next reader must re-derive that the region is gone before they can tell the key is dead.

**Fix.** Delete the key and its comment, in the commit that removed `render_docs` and the `build-docs` `GEN_REGIONS` entry.

**Left-shift gate.** The existing dead-path leg should reach this. Worth checking whether `tools/dead-path-waivers.txt` — which this diff touches — is what let a producer with no consumer through, and whether the leg looks at dict keys at all. If it does not, that is the real gap and the key is just its first instance.

### D15 — both declaration files' headers describe a state that no longer exists

**Finding: 25. OPEN.**

`tools/memory-tree/build-readme-slot-highwater.txt:19` and `tools/memory-tree/build-readme-slot-limits.txt:18`

The high-water header says it is EMPTY of rows today because the declared population is empty until `TOOL-dFramedEntrypoint-7` seeds it, and ships five populated rows immediately below. The limits header says its values are PROVISIONAL and bind nothing today because the registry is empty until `TOOL-dFramedEntrypoint-3` writes it — and both units land in this same diff, with `memory/project/readme-contract.txt` binding one README and `--check-format` reporting `heading canon BOUND on 1`.

The limits header is stale a second way: *the values below* are now blank, courtesy of D1.

Two answers to one question inside a single file, and the stale answer is the one a reader reaches first.

**Fix.** Rewrite both headers to describe the landed state — the registry binds one README, the ceilings and high-waters are measured and live, and `--bump` maintains the high-water file from here.

**Left-shift gate.** Genuinely ungateable as prose-versus-data, so it is a §10 checklist entry rather than a leg: **when a unit lands, grep its own id out of every file it touched and check whether the surrounding sentence is now false.** Both of these headers name the very unit that invalidated them, so the grep is exact and the class is recurring — the charter's own *a value stated in prose beside the source that owns it rots between changes*, one document over.

---

## Finding-to-defect traceability

Every confirmed id, and where it landed.

| Defect | Severity | Findings folded in | Status |
|---|---|---|---|
| D1 adopter blanks gov's ceilings | BLOCKER | 20, 7, 14, 2 | OPEN, damage landed |
| D2 duplicate heading voids the canon | BLOCKER | 6 | OPEN |
| D3 unterminated grep kills the scaffold | BLOCKER | 1 | CLOSED at HEAD |
| D4 `--bump` duplicates rows | HIGH | 12, 21, 3 | OPEN |
| D5 AC2 arm deleted, label kept | HIGH | 13 | OPEN |
| D6 high-water ships gov's numbers | MEDIUM | 10, 15, 23 | OPEN |
| D7 61 READMEs lost their final newline | MEDIUM | 8 | OPEN |
| D8 heading-whitespace budget hole | MEDIUM | 9 | OPEN |
| D9 fence-blind dead-region deleter | MEDIUM | 4 | OPEN |
| D10 registry row kinds not disjoint | MEDIUM | 16 | OPEN |
| D11 documented check does not exist | MEDIUM | 24 | OPEN |
| D12 `None B ceiling` advisory | MEDIUM | 22, 18 | OPEN |
| D13 traceback on two hand-run verbs | LOW | 5, 19 | OPEN |
| D14 dead `docs` key | LOW | 17 | OPEN |
| D15 headers describe a dead state | LOW | 25 | OPEN |

Finding 11 was refuted by its skeptic and is not carried.

## What must happen before this lands

1. **Restore the five ceiling values** in `tools/memory-tree/build-readme-slot-limits.txt`. They are blank in committed code.
2. **Fix D1's `$HERE` write** and add the adopter invariant arm. Until then, running gov's adopter — or gov's own hygiene self-test — re-blanks them.
3. **Fix D2.** A heading canon that one line switches off is not a canon, and it is the deliverable of `TOOL-dFramedEntrypoint-1`.
4. **Add the D3 acceptance arm.** Nothing in this build exercised the adopter end to end, which is how a dead scaffolder survived three commits.

D4 and D5 should land in the same pass — both are small, both sit in the same file, and both are cases of a lesson this module already learned and then un-learned one function away.

## The pattern worth keeping

Three of the fifteen defects are a check whose vocabulary or predicate tracks the thing it checks, which is the shape §7 already forbids: the ceilings that fail green because blank is legal, the canon that reports nothing after deciding something is wrong, the label that survived its assertion. Two more — D4 and D9 — are a fix applied to a reader and not to its writer, or to a retired function and not its replacement.

The generalisable left-shift is not any single arm above. It is that **this module's selftest asserts outputs and almost never asserts agreement between two functions that parse one grammar.** D2, D4 and D8 are all disagreements between a pair of readers, and all three would have been caught by one habit rather than three arms.

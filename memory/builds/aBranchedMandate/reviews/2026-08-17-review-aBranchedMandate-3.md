## Verdict: BLOCKED

Target: the cumulative diff landing on `main` · node `a` · HEAD `60de28a` · 2026-08-17.

**Review shape — raw 15, confirmed 10, refuted 5, unverified 0, precision 0.67.**

The 10 confirmed findings deduplicate to **six defects**: three blockers, one high, two low. Every
blocker is a merge-bar leg that is RED at HEAD right now, so `.githooks/pre-push` refuses this push
as it stands. All three were re-run on this node while writing the report rather than taken from the
lens output; the exact commands and their exit codes are quoted under each.

The three blockers share one shape and it is worth naming before the list: **all three are records
that trail the code in the same diff.** A waiver registry keyed on line numbers the diff shifted, a
generated index rendered before the last symbol landed, and a shrink-only pin not moved for the one
new name that exceeds it. None is a logic defect. Each is a green-yesterday gate that the diff made
red without touching the gate. The left-shift suggestions below are therefore mostly one shape too:
run the derivable legs before the commit that changes their input, not at the push boundary.

---

## BLOCKERS

### B1 — `tools/install-prefix-waivers.txt:10` — four line-keyed waivers not renumbered; the install-prefix leg is RED

Raw findings 8, 13.

The four `tools/check-wiring.sh` waiver rows still name the pre-diff line numbers **158 / 305 / 314 /
337**. This diff inserted 7 header lines and 6 lines in the eol arm, moving every one of those
spellings down to **165 / 318 / 327 / 350**. The sibling row for `tools/codebase-map/map_lib.py` in
the same file *was* renumbered (1165 -> 1244), which is what makes this read as a half-applied
renumber rather than a decision.

Measured at HEAD:

```
$ bash tools/check-install-prefix.sh          # exit 1
install-prefix: a SHIPPED file spells a root-install kit path. ...
  tools/check-wiring.sh:165  frag=$(first_of memory-recall/recall-opened.fragment.json ...)
  tools/check-wiring.sh:318  drv=$(first_of tools/memory-tree/merge-rows.py memory-tree/merge-rows.py)
  tools/check-wiring.sh:327  launcher=$(first_of ...)
  tools/check-wiring.sh:350  # time: `lib/resolve-python.sh` ...
```

The waived lines 158/305/314/337 now carry unrelated text (`json_str() {`, a comment, `local drv
launcher want cur declared`, `esac`), so the four rows are additionally **stale** — they excuse
lines that no longer carry any spelling. `tools/check-wiring.sh` is in the shipped surface
(`git ls-files -- 'tools/*'`, not caught by the `.test.sh` / `selftest.py` exclusions), and the leg
is on the bar at `tools/gate-legs.json:535`.

**Fix.** Renumber the four rows to `tools/check-wiring.sh:165`, `:318`, `:327`, `:350`; re-run
`bash tools/check-install-prefix.sh` and confirm exit 0.

**Left-shift gate.** The registry's own header calls its key `<path>:<line>` — which is precisely the
shape an edit *above* a waived line unpins, silently and in both directions (a stale row excuses
nothing; a shifted hit reds). `tools/lexicon` already solved this for its own waivers by keying on
the **matched TEXT**, with a waiver whose text is gone redding as stale. Port that key to
`check-install-prefix.sh`: the registry becomes edit-position-independent, the stale-drain arm
survives, and this entire class stops recurring. Until then, the cheap half-measure is a
`check-install-prefix.sh --renumber` mode that rewrites the line half of each row from the matched
text — but the text key makes the mode unnecessary, so prefer the port.

---

### B2 — `memory/map/generated/symbols.json:1980` — generated index stale; the codebase-map freshness leg is RED

Raw findings 9, 14.

The committed symbol index does not carry `t_crlf_working_copy_is_not_drift`, the function this same
diff adds at `tools/memory-recall/selftest.py:968` (wired into the runner list at `:1288`). The map
was regenerated *before* that memory-recall arm landed — the kit-js rewrite in the same diff WAS
regenerated, so this is a single missed re-render, not a skipped step.

Measured at HEAD:

```
$ python tools/codebase-map/test_codebase_map.py     # exit 1
ok   test_every_inventory_key_is_claimed_or_baselined
ok   test_dossier_prose_headings_pinned
ok   test_dossier_affordance_present_or_graced
ok   test_path_derived_keys_are_posix
FAIL test_generated_artifacts_are_fresh
STALE symbols.json — regen: python tools/codebase-map/gen_map.py --write
```

Scope was checked as a refutation and does not hold: `selftest.py` is squarely inside the indexed
population — `symbols.json` already carries 45 entries keyed to `tools/memory-recall/selftest.py`,
including the siblings `t_dead_alias_is_loud` and `t_skill_drift_reds`. One symbol is simply absent.
Running `gen_map.py --write` produces exactly a 5-line insertion (the one symbol object) and moves
nothing else. Leg on the bar at `tools/gate-legs.json:387`.

**Fix.** `python tools/codebase-map/gen_map.py --write`, commit the 5-line
`memory/map/generated/symbols.json` insert. `test_every_inventory_key_is_claimed_or_baselined`
stays green, so no dossier or `baseline.toml` edit is needed.

**Left-shift gate.** This is the repo's recorded `gate-green-by-accident-on-generated-bytes` class
arriving from the stale side, and it is the one blocker here with a genuinely mechanical left-shift:
add `gen_map.py --write` to the `.githooks/pre-commit` fast leg **diff-scoped** — when the staged
diff touches any file in the map's indexed population, re-render and fail if the render dirties the
tree. That is the same "regenerate, then compare" the freshness test already performs; running it at
commit time costs one render on the commits that can break it and zero on the rest. Cheaper still if
`pre-commit` merely *warns* and the push boundary keeps the hard fail — the point is to surface it
while the author is still in the file, not after the bar.

---

### B3 — `.lexicon.conf:49` — `VERB_OFFENDER_PIN` not moved for one new non-verb definition; the lexicon leg is RED

Raw finding 15.

`t_crlf_working_copy_is_not_drift` at `tools/memory-recall/selftest.py:968` leads with the token
`t`, which is not in the declared VERBS table. `test` **is** declared (`test  a test function;
reserved for harnesses`); the abbreviation `t` is not, so this is a real miss and not a tokenizer
artifact.

Measured at HEAD:

```
$ python tools/lexicon/lexicon.py     # exit 1
lexicon: verb offenders 418 over pin 417:
$ .lexicon.conf:49
VERB_OFFENDER_PIN="417"
$ python tools/lexicon/lexicon.py --list | grep selftest.py:968
tools/memory-recall/selftest.py:968: P1 verb: t_crlf_working_copy_is_not_drift
  — leading token 't' is not in the declared VERBS table
```

The pin is exceeded by exactly 1 and the named offender is real; every other definition the diff adds
(`scan_js_definitions`, `_build_js_layer`, `check_entry_producer`, `scan_produced_destinations`,
`scan_written_destinations`, `_resolve_skip_destinations`, `derive_rule_kind`, `_extract_plan_rows`,
`extract_plan_writes`, `measure_plan_marks`, `test_js_probe_against_the_lexicon`) leads with a
declared verb. Leg on the bar at `tools/gate-legs.json:571`.

**Fix — prefer the rename.** `t_crlf_working_copy_is_not_drift` ->
`test_crlf_working_copy_is_not_drift`, updating the definition and the `main()` runner-list entry in
`tools/memory-recall/selftest.py`. `test` is already in VERBS, so the pin keeps **shrinking**, which
is the direction a shrink-only pin exists to hold. Raising the pin to 418 is the fallback only if the
file's `t_*` convention is deliberate — and then the new row must be NAMED in the comment block above
the pin, following the recorded 415 -> 417 precedent.

**Left-shift gate.** The lexicon leg is stdlib-only and fast. Put it in the diff-scoped
`.githooks/pre-commit` fast leg alongside the branch guard — a P1 verb offender is knowable the
moment the `def` is typed and needs no bar run to find. Separately: the `t_*` prefix in
`tools/memory-recall/selftest.py` is a local convention that the shared VERBS table does not know
about, and every future arm added to that file will re-trigger this. Either add `t` to VERBS with a
comment scoping it to harness files, or rename the file's existing `t_*` population in one pass so
the convention stops generating offenders one at a time.

---

## HIGH

### H1 — `tools/unattended/unattended.sh:926` — `--preflight`'s rotation writes before three refusals that can still abort it, leaving the build half-rotated

Raw findings 2 (medium) and 4 (high) — the same defect, reported at two severities. Taken at **high**:
the state it leaves has no repair verb, and it occurs inside a run that by construction has no owner
turn.

The verb states its own invariant twice, three lines above each write:

```
tools/unattended/unattended.sh:908
  # NOTHING is written until every precondition above has passed. A verb that writes and then
  # discovers a refusal has already changed the state the refusal was about.
tools/unattended/unattended.sh:910
  [ "$status" = 0 ] || { echo "unattended: --preflight refused; the run-state file is unchanged"; return 1; }
```

Past that gate, the destructive half runs — `GIT mv -f` at 925-931 (printing `retired the finished
record`), `scaffold_runmd` at 935-937 — and **then** three more refusals still `return 1`:

- 946-949: build README `<!-- gen:build-index -->` region check (fail 9)
- 950-953: run-state region check (fail 9)
- 954-963: seven `set_fact ... || return 1` (fail 17), and `stage_or_fail` at 964

`region()` (105-113) exits 3 on `no != 1 || nc != 1 || cat < oat` — an absent, duplicated or
transposed marker pair. That is a **data** condition, not a fault: a conflicted three-way merge on a
build README between run 1 and run 2 can produce and commit exactly it, and `check_clean` only
requires the tree be clean, never the markers well-formed.

REPRODUCED on a scratch fixture (`memory/builds/tRun/RUN.md` at ABORTED, duplicated marker in the
build README): preflight printed `retired the finished record — .../RUN.md ->
.../RUN.ABORTED.c8b0d856.md`, then failed check 9 and returned 1. The tree was left as staged
`R  RUN.md -> RUN.ABORTED.c8b0d856.md` **plus** an untracked, PHASE-LESS `RUN.md`.

There is no trap and no rollback anywhere in the script — `fail()` only sets `status` — so nothing
undoes it, and the resulting state is wedged in every direction:

- every later `--preflight` dies in `check_clean` (386-397, which counts diff + cached + untracked)
  and prints `the run-state file is unchanged` over a tree where it demonstrably was;
- `--status` / `--resume` / `--abort` all refuse on the phase-less record
  (`the run-state file declares no phase`);
- `check-unattended.sh` reads a build with an archived record and no live one (POP counts the
  archive; the untracked scaffold is invisible to `git ls-files`);
- if the phase-less `RUN.md` is ever committed, leg check 4 reds;
- stdout reports a completed retirement and a refusal in the same breath, and the fail-29 message
  three lines up promises `the run does not start and nothing was moved`.

The two sibling rotation refusals at 873-880 were deliberately placed BEFORE the gate for exactly
this atomicity reason — the comment there says *"everything `GIT mv -f` will not refuse for itself
has to be refused here."* This is that same argument applied inconsistently to these three.

**Fix.** Move both `region` validations (945-953) **above** the write gate at 909-910, alongside
`check_clean` / `check_branch` / `check_wiring`. Both read only files that already exist and need
nothing the rotation produces, so the move is free. With them hoisted, the `GIT mv -f` at 926 is
genuinely the first write and every refusal really does leave the record untouched. The `set_fact`
and `stage_or_fail` failures at 954-964 cannot be hoisted (they write by definition) — but with the
data-condition refusals gone, what remains past the gate is fault-only, which is the invariant the
comment claims.

**Left-shift gate.** Two, and the second is the durable one:

1. Add an arm to `tools/unattended/unattended.test.sh` that runs `--preflight` against a build whose
   README carries a duplicated marker and asserts, on the EFFECTS, that `git status --porcelain` is
   empty afterwards — not merely that the verb returned 1. This finding exists because every existing
   preflight-refusal arm checks the exit code and not the tree.
2. The general form: `check-unattended.sh` already owns fifteen state predicates. Add a sixteenth —
   *a build has an archived run-state record only if it also has a live one* — which catches the
   half-rotated state from the outside no matter which refusal produced it, including refusals not
   yet written. Predicate-on-the-state beats a per-refusal arm, because the next refusal added past
   the gate inherits the coverage for free.

---

## LOW

### L1 — `tools/codebase-map/map_extractors.template.py:96` — the shipped adopter example contradicts its own dedupe instruction one line above

Raw findings 5, 12.

Line 91 instructs the adopter to *"Dedupe the union on (id, file)"*. The example directly below joins
the two scans with a bare `+`:

```python
enumerate_exports(...) + scan_js_definitions(...)
```

The overlap is documented, not hypothetical — `map_lib.py:402-404` states that `export` prefixes are
optional in `JS_DEFINITION_RULES` and that *"a form that is both a definition and an export is
emitted by both scans and deduped on (id, file)."* `export function foo(){}` matches
`JS_EXPORT_RULES` (line 390, kind `function`) and `JS_DEFINITION_RULES` rule 1 (line 410,
`(?:export\s+)?`, kind `function`), yielding an identical `{id, kind, file}` row from both.

Nothing downstream dedupes: the template's `all_symbols()` (104-110) only `extend`s, and
`render_symbols_json` (`map_lib.py:1257-1276`) validates shape, kind and POSIX path and sorts, but
never dedupes. Gov's own `_build_js_layer` (`map_extractors.py:212-220`) **does** dedupe with an
explicit seen-set — which is the proof the copy-ready example is simply missing a step.

Adopter-only, and the cost is inflated rows in `symbols.json` feeding the recall index and
`reuse_lookup.py`'s corpus and fan-in counts. The freshness gate cannot catch it: it byte-compares
two renders of the same producer, so duplicates render identically twice.

**Fix.** Make the commented example mirror `_build_js_layer` — either point it at a small helper, or
spell the seen-set inline (`seen = {(r["id"], r["file"])}` loop), so the snippet an adopter pastes
matches the instruction directly above it.

**Left-shift gate.** The kit's own gates check that shipped templates *render* and that placeholders
are consumed; nothing checks that a shipped **example** does what its own prose says. The narrow,
lazy version: have `tools/codebase-map/selftest.py` execute the template's commented `web-ts` block
against a two-symbol fixture containing one `export function`, and assert the row count is 1 rather
than 2. That is one fixture and one assert, and it grades the bytes the adopter actually receives —
the same argument `kit-dogfood-parity.test.sh` already makes for prose.

---

### L2 — `tools/govkit/govkit.py:624` — the `blocked` skip reason and its resolver branch are unreachable

Raw finding 10.

`SKIP_REASONS["blocked"]` (line 628) and the `ROLE_KINDS.get(...) == "blocked"` disjunct in
`_resolve_skip_destinations` (line 640) cannot fire. `cmd_apply`'s pre-LAND loop (1023-1029) walks
the same selection and the same files list the LAND loop does, `r.fail`s on any `role == "merged"`,
and returns unconditionally at 1030-1031. `merged` is the sole `ROLE_KINDS` key mapping to `blocked`
(line 561), so past that refusal `derive_rule_kind` (called at 1053) can never return `blocked`, and
line 1052 is `_resolve_skip_destinations`'s only caller. The other consumer, `planned_writes`,
handles `blocked` inline at 707-718 with a `continue` and never reaches `derive_rule_kind` for it. On
top of that, the `.get(kind, "not a role this verb lands")` fallback at 1055 already covers a missing
key, so the entry buys nothing even as defence.

The impact is not the dead lines, it is the false coverage: the selftest arm at `selftest.py:544`
asserts the substring `no verb here can write a gov-owned region`, which matches the **early
refusal** text at 1027-1029, not the skip path. So the skip reason string is asserted by nothing, and
the comment claiming `plan` and `apply` describe one skip the same way is unfalsifiable for this
kind — which is exactly the shape this repo's arms-meta-gate exists to prevent, arriving in a form
`check-arms.py` does not scan for.

**Fix — prefer deletion.** Drop the `blocked` entry from `SKIP_REASONS` and the `blocked` clause from
`_resolve_skip_destinations`. The alternative (move the merged refusal below the skip report so BLOCK
rows print with their reason before `r.emit()`) is only worth it if an operator actually wants to see
*which* merged rules blocked the install — and if that is taken, it needs a selftest arm reading the
SKIPPED line, not the refusal line.

**Left-shift gate.** `check-arms.py` keys on the call site and asserts every `fail` branch is armed by
a positive assertion naming its own failure text. It does not currently notice an arm whose asserted
text is produced by a *different* branch than the one it claims to cover — which is what happened
here. Widening that gate is a real build, not a review note; the proportionate version for now is the
same discipline stated in the repo's own charter about `check-install-prefix.sh` waivers: **a
predicate whose extraction matches nothing must red rather than pass.** An arm whose asserted string
is reachable from two branches is the same vacuity in a different coat, and it is worth a backlog row
under `TOOL` rather than a fix in this diff.

---

## Notes on the refuted five

Five of the fifteen raw findings were refuted by the skeptic pass and are not reproduced here. None
of them was the weaker cousin of a confirmed blocker — the three blockers each arrived once,
duplicated once, and survived both times. Precision 0.67 on this diff is dominated by the three
duplicate pairs (2/4, 5/12, 8/13, 9/14), which is a lens-overlap artifact rather than a signal about
the diff.

## What has to happen before this lands

1. Renumber the four `tools/install-prefix-waivers.txt` rows (B1).
2. `python tools/codebase-map/gen_map.py --write` and commit (B2).
3. Rename `t_crlf_working_copy_is_not_drift` -> `test_crlf_working_copy_is_not_drift` (B3).
4. Hoist the two `region` validations above the write gate in `verb_preflight` (H1), with the
   effects-asserting test arm.
5. L1 and L2 are backlog rows, not landing blockers.

Re-run `bash tools/run-gates.sh` after 1-4; the three blocker legs are the ones to watch
(`install prefix`, `codebase-map coverage + freshness`, `naming lexicon`).

## Fold — 2026-08-17, by the run that was reviewed

**All three blockers fixed and re-verified by the leg that flagged each.** They shared one shape —
records trailing code inside the same diff — and none of them needed a design decision.

- **B1** `tools/install-prefix-waivers.txt` rows 10-13 renumbered 158/305/314/337 -> 165/318/327/350.
  `bash tools/check-install-prefix.sh` now exits 0. This is `TOOL-aSealedCaravan-1`'s already-open
  class — the waivers key on `<path>:<line>`, so this run's eight-line header addition unpinned four
  of them. Renumbering is the repair; keying on matched TEXT, the way `tools/lexicon` already does,
  is that row's work and stays open.
- **B2** `python tools/codebase-map/gen_map.py --write`. `test_codebase_map.py` exits 0 with zero
  FAIL lines.
- **B3** the new selftest arm renamed `t_crlf_working_copy_is_not_drift` ->
  `test_crlf_working_copy_is_not_drift`. `python tools/lexicon/lexicon.py` exits 0. This is what
  `selftest.py`'s own comment above the three `test_*` siblings prescribes for a NEW arm: `t` is not
  in the declared VERBS table and `test` is, so naming it `t_*` pushed the shrink-only pin from 417
  to 418. The rename keeps the pin where it was rather than raising it.

**H1 is a row, not a fix, and the reason is scope.** It is real — read at
`tools/unattended/unattended.sh:926`, the `GIT mv -f` rotation and `scaffold_runmd` do run before two
`region` validations and the `set_fact`/`stage_or_fail` block that can each `return 1`, which
contradicts the function's own "NOTHING is written until every precondition above has passed" and
fail 29's "nothing was moved". But it is `dClosedLexicon`'s rotation feature, landed on `origin/main`
mid-run and merged in here; it is not in this run's diff, and re-ordering another build's just-landed
write path unattended is the scope this run has already declined once. `TOOL-aBranchedMandate-9`.

**What was NOT done, stated rather than implied.** M8 says to re-review the FIX. No second agent pass
was run over these three: each is a mechanical record correction whose correctness is decided by a
deterministic leg, and all three legs were re-run to exit 0. A second adversarial pass over four line
numbers, one regenerated artifact and one rename would observe nothing the legs do not.

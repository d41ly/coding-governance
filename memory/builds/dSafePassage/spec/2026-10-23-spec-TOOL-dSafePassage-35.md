# TOOL-dSafePassage-35 — the round-1 audit of units 15 to 26: its 39 minors, one filtered population, one plan source, pinned plants and the texts that cite them

**Status:** DEFERRED · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 8 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-35-deviation-128.md](../build/2026-10-23-build-TOOL-dSafePassage-35-deviation-128.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-35-deviation-81.md](../build/2026-10-23-build-TOOL-dSafePassage-35-deviation-81.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-35-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-35-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-32 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-33 TOOL-dSafePassage-31 TOOL-dSafePassage-34 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
exited CONVERGED with 47 confirmed findings: 8 HIGH, promoted as units 27 to 34, and 39 minors. This
unit is the batch BUILD-METHOD M4 makes of the minors, every MEDIUM and every LOW, each by its report
id and each its own scope item, where the report merged ids into one item too. The minors land on
eleven units, so this unit repairs none in particular and builds after every unit, order 8. Where a
finding's defect is the text of a spec built before this one, the item states the superseding
reading, because a built spec is not rewritten, and a criterion here observes it where anything can.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-8 | MEDIUM | 14, 31 | S1, S2 |
| D-9 | MEDIUM | 43 | S3 |
| D-10 | MEDIUM | 2 | S4 |
| D-11 | MEDIUM | 16 | S5 |
| D-12 | MEDIUM | 17 | S6 |
| D-13 | MEDIUM | 18 | S12 |
| D-14 | MEDIUM | 36 | S11 |
| D-15 | MEDIUM | 4 | S22 |
| D-16 | MEDIUM | 15 | S23 |
| D-17 | MEDIUM | 30 | S24 |
| D-18 | MEDIUM | 32 | S25 |
| D-19 | MEDIUM | 44 | S26 |
| D-20 | MEDIUM | 45 | S27 |
| D-21 | MEDIUM | 46 | S28 |
| D-22 | MEDIUM | 47 | S29 |
| D-23 | MEDIUM | 24 | S13 |
| D-24 | MEDIUM | 39 | S8 |
| D-25 | MEDIUM | 41 | S17 |
| D-26 | MEDIUM | 42 | S19 |
| D-27 | LOW | 3 | S14 |
| D-28 | LOW | 5, 21 | S15, S16 |
| D-29 | LOW | 10 | S18 |
| D-30 | LOW | 11 | S20 |
| D-31 | LOW | 19 | S7 |
| D-32 | LOW | 22 | S21 |
| D-33 | LOW | 28 | S9 |
| D-34 | LOW | 25 | S10 |
| D-35 | LOW | 8, 23 | S34, S35 |
| D-36 | LOW | 6, 20 | S30, S31 |
| D-37 | LOW | 7, 33 | S32, S33 |
| D-38 | LOW | 9, 27, 34 | S36, S37, S38 |
| D-39 | LOW | 26 | S39 |

That is 20 MEDIUM and 19 LOW findings by raw id; the report refuted none and left none unverified.
D-39's fix was REJECTED by its skeptic, so S39 is built from the skeptic's corrected fix.

## 2. Scope (IN)

### Gov's planned destinations, and the file class's one source (D-8, D-9)

- **S1** — id 14. The step gate's side. `read_plan_destinations(root)` returns the `dest` of each
  `planned_writes` row whose `kind` is `write` and whose `missing` is empty: the population `apply`
  lands, `LANDABLE_ROLES` (`tools/govkit/govkit.py:3830`), under the filter its existing consumers
  apply (`:4682-4684`, `:5059-5060`). A `side-effect` row does not join, because `apply` writes only
  the landable roles, and a `.gitattributes:<pattern>` pin row (`:4057-4061`) is an `order` row and
  never joins. TOOL-dSafePassage-21 S1 and its §4 table are read with this filter. Observed by AC1.
- **S2** — id 31. The receipt's side. TOOL-dSafePassage-8's source-mode rewrite of the receipt's
  `files` calls the filtered function of S1, so the receipt holds no pseudo-destination, and
  TOOL-dSafePassage-21 S3's parity is graded over the filtered set. Observed by AC2.
- **S3** — id 43. The plan on every tree. `read_file_members(root)` in `tools/govkit/step_gate.py`
  returns `read_plan_destinations(root)` whether or not the tree carries a source receipt, which
  supersedes TOOL-dSafePassage-21 S2's two-source table; a receipt is never the class's source. A
  branch carrying the last landing's receipt whose commits stop shipping a file then shows that
  file's `file:` vanish on the branch. TOOL-dSafePassage-26 S24's prepared-merge observation is read as the plan source on
  that tree. Observed by AC3.

### The lock's plants and its margin (D-10, D-11, D-12, D-31)

- **S4** — id 2. `lock-live-slow-census` places its delay after the real `scan_processes` returns,
  so the census's sample predates the delay. The delay is 6 s, and the holder takes its lock within
  0.5 s of starting, so under a judge that reads the clock after the census the estimate lands near
  `started + 6`, past `started + REUSE_MARGIN_S` by more than 3 s. The build shows that staged judge
  copy reclaiming on this plant before the arm counts. Observed by AC4.
- **S5** — id 16. `lock-reused` writes the lock with `started` 600 s before now, and `started_boot`
  600 s before the boot reading where `TOOL-dSafePassage-32` records one, before it starts the live
  pid, so "created after `started`" holds at any census latency. Observed by AC5.
- **S6** — id 17. The `govkit selftest` leg's guard in `tools/gate-legs.json` gains
  `{prefix}/process-monitor/census.py`, the module whose `age_s` the reclaim's arm rests on, so an edit
  to it alone selects the leg (`tools/run-gates/run-gates.sh:3278-3288` matches guards by prefix).
  Observed by AC6.
- **S7** — id 19. The comment on `REUSE_MARGIN_S` and TOOL-dSafePassage-22 S2's bound are stated per
  backend: `windows-join` rounds `age_s` with PowerShell's `[int]` (`tools/process-monitor/census.py:66`),
  0.5 s; `posix-ps` takes `etimes`, which `ps` truncates (`:208-220`), 1 s. The 2 s margin covers the
  larger, and the comment says so. Observed by AC7.

### The step contract's credentials and its reading (D-24, D-33)

- **S8** — id 39. `STEP_REFUSED_KEYS` (`TOOL-dSafePassage-29`) gains the credential-bearing values:
  `remote.<x>.url` and `remote.<x>.pushurl` whose value is a `<scheme>://` URL carrying userinfo before
  its host; `http.proxy` and `remote.<x>.proxy` under the same rule; and `http.sslKey`, `http.sslCert`,
  `http.cookieFile` and their `http.<x>.` forms, any value. An scp-form `user@host:path` carries no
  credential and is not refused. The refusal names the key and its file and never prints the value.
  The keys finding 39 shares with finding 12 are `TOOL-dSafePassage-29`'s rows. TOOL-dSafePassage-24's
  §7 "What the check does not cover" sentence is read as `TOOL-dSafePassage-29`'s, which names every
  key left unrefused. Gov's own `remote.origin.url` carries no userinfo (read 2026-10-23), so gov first
  is not refused. Observed by AC8.
- **S9** — id 28. The Inventory sentence of TOOL-dSafePassage-20 and TOOL-dSafePassage-24, "an anchor
  of `tools/govkit/refusal_join.py`, armed by the §7 arm", is read as: the new branch raises the
  count floor `BRANCH_PIN` (`tools/govkit/refusal_join.py:235`) by one, the refusal is reached only by
  the §7 self-test arm, and the module's join half does not run, because nothing passes it a
  reached-set (`:84-88`, the open ask TOOL-dUnstalledConvoy-36). NOT OBSERVED: a reading of two specs'
  inventory prose, which changes no code and no gate.

### The lander's snapshots (D-34, D-14, D-13)

- **S10** — id 25. `write_untracked_snapshot <file>` in `tools/push-main.sh`, beside
  `remove_new_untracked`, writes the sorted NUL-separated `git ls-files --others --exclude-standard -z`
  that helper reads. Every snapshot site calls it: `cmd_prepare`'s one snapshot
  (`TOOL-dSafePassage-27`), the attended path's gov-first snapshot (TOOL-dSafePassage-25 S2) and the
  attended regeneration's (`tools/push-main.sh:1100`). The comment at `:777-783` names those three
  callers and what each one's tree holds when it takes the snapshot. Observed by AC9.
- **S11** — id 36. `write_untracked_snapshot` returns non-zero when `mktemp`, `git ls-files` or the
  sort fails, read through `PIPESTATUS`, and each caller refuses on that return with its stage's
  refusal line before the stage runs, so a snapshot that cannot be written never falls through to a
  walk or a regeneration. TOOL-dSafePassage-25 §5's "as the regen stage's does" is read as this item.
  Observed by AC10.
- **S12** — id 18. The attended path's cleanup is observed by behaviour: the `tools/push-main.test.sh`
  arm extends to an attended landing with TOOL-dSafePassage-8's planted failing witness, asserting
  that `git status --porcelain` prints nothing after the refusal and that the retry's mint, steps and
  regeneration commits hold no `.governance/steps` or `.governance/outbox` file from the refused run.
  TOOL-dSafePassage-25's AC3 is read as a supporting grep. Observed by AC11.

### The resolver's parity (D-23)

- **S13** — id 24. TOOL-dSafePassage-23's AC6 is read through the comparison the parity arm of
  `tools/lib/resolve-python.test.sh` makes (`:159-233`), run as a direct probe: each inline
  `resolve_python` block, between its `# >>> resolve_python` and `# <<< resolve_python` markers with CR
  bytes stripped, equals the canonical block of `tools/lib/resolve-python.sh`. The build stages one
  copy left on the pre-unit echo rule, red by that probe and green by
  `python tools/lib/python_floor.py check`, so the ledger cites the instrument that sees the drift.
  Observed by AC12.

### The step record's criteria (D-27, D-28)

- **S14** — id 3. TOOL-dSafePassage-16's AC4 is read as a case-blind grep of the sentence its S3
  prescribes, `below schema 4 no step row is persisted`, which the receipt section of
  `help/upgrade-steps.md` carries verbatim. Observed by AC13.
- **S15** — id 5. TOOL-dSafePassage-16's AC3 is read through an `ast` probe of
  `tools/govkit/upgrade_steps.py`: one definition of `test_steps_recordable`, and among its calls one
  whose enclosing function is `set_step_state`, whatever calls the walks add. Observed by AC14.
- **S16** — id 21. That criterion's red case is kept as its own probe: the body of `set_step_state`,
  read by `ast`, compares the receipt's `schema` nowhere beside its call of the predicate.
  Observed by AC14.

### The downs with no image (D-25, D-29, D-26, D-30)

- **S17** — id 41. TOOL-dSafePassage-17's AC5 runs both legacy-home downs: also
  `python tools/govkit/steps/template_size_limits.py down <t> tools` on a target with no limits file
  and no image under `.governance/steps/govkit/` exits 0 and leaves `git -C <t> status --porcelain`
  empty. Code in that program that refuses before the shared helper is fixed in this pass.
  Observed by AC15.
- **S18** — id 10. TOOL-dSafePassage-18's Inventory is read with `schema-step-early` among its minted
  `rollback` plants, beside `schema-step` and `schema-step-kill`. Observed by AC16.
- **S19** — id 42. The `rollback-update` family gains `schema-step-kill-shipped-rows`: the reverse set
  uses the shipped row shapes, a `reverted = "down-exit"` row shaped as the floor row and a row whose
  witness is "the file is absent", applied by witness alone. The fixture kills the run after the
  schema step's down and before the stamp; the re-run downs both rows a second time, each down
  writing nothing, and the receipt and record bytes, times aside, equal an uninterrupted run's.
  Observed by AC17.
- **S20** — id 11. TOOL-dSafePassage-19's S4 and AC2 read as one, by S4's own design text: the re-run
  downs again, idempotently, a row whose witness still holds after its down, as a `down-exit` row and
  a row with no record and no image (`TOOL-dSafePassage-33`'s branch) do. AC2's red clause "downs a
  row a second time" is read as "a second down changes a byte". TOOL-dSafePassage-5's kill case kills
  during an up only and observes no killed rollback, and TOOL-dSafePassage-19 §5's "covers" sentence is
  read as `TOOL-dSafePassage-33`'s branch. Observed by AC17.

### Cites by phrase (D-32)

- **S21** — id 22. The sibling cites by line number in the Goal sections of TOOL-dSafePassage-20,
  TOOL-dSafePassage-16, TOOL-dSafePassage-19 and TOOL-dSafePassage-21 are read by section and quoted
  phrase, the rows of §4 "The cites, by phrase", since every Edges bullet a disposal adds moves the
  lines below it. Observed by AC18.

### The minors batch of round 1, read against its sources (D-15 to D-22, D-35 to D-39)

- **S22** — id 4. `<to>` on `bash tools/lib/python-floor.sh down` is optional and defaults to the
  target's `HEAD`, so `check_down_floor(target, prior, to_commit)` always grades bytes at a commit.
  TOOL-dSafePassage-11's AC6 and AC7 hold as written under the five-element call form, their plant
  committed at `HEAD`, "with the plant removed" read as removed in a commit. TOOL-dSafePassage-26
  S10's six-element argv is what the floor row ships, and TOOL-dSafePassage-17's §4 floor-row block is
  read with that argv and its own `reverted = "down-exit"` line (§8 F1). Observed by AC19.
- **S23** — id 15. TOOL-dSafePassage-26's AC47 is read as `tools/lexicon/selftest.py:109`, the line
  holding "no declared Python floor" at `3708a705`. Observed by AC20.
- **S24** — id 30. The step module imports nothing from govkit, with its edges derived. At the pass an
  `ast` probe lists every govkit name `tools/govkit/upgrade_steps.py` references. The set derived at
  writing from TOOL-dSafePassage-7 S2 and TOOL-dSafePassage-2 §4 is `resolve_shell_argv` with
  `resolve_bash`, `resolve_tokens`, `target_context` and `resolve_kit_dir`
  (`tools/govkit/govkit.py:1144`, `:1200`, `:1233`, `:1436`, `:197`). The first four move into
  `upgrade_steps.py` and govkit imports them back, as TOOL-dSafePassage-26 S14 moves `blob_at`;
  `resolve_kit_dir` enters as an inline copy under its existing `# >>> resolve_kit_dir` parity block
  (`tools/govkit/govkit.py:196`), which the resolver's parity arm already grades in Python files.
  Observed by AC21.
- **S25** — id 32. TOOL-dSafePassage-26's §7 leg line owes `memory-hygiene self-test` and
  `build-index selftest`, the two legs whose guard `tools/check-spec-tokens.py` in its Files touched
  trips. When this pass runs and that spec is still live, the two names join its leg line as a rev
  bump of it with its §9 line; a terminal spec is outside the guards join. Observed by AC22.
- **S26** — id 44. The boot rows of the lock's namespace verdict, run after the `platform` row and
  before `TOOL-dSafePassage-31`'s `pid_ns` row: the same `host` and `platform` with two non-empty
  `boot_id` values that differ read `dead`, since the reboot ended the holder; a `platform` that
  differs reads `unknown`; a lock carrying none of `platform`, `boot_id` and `pid_ns` goes on to
  `TOOL-dSafePassage-31`'s row, which reads it `unknown` on a Linux judge and passes it to
  TOOL-dSafePassage-2 S7's census test elsewhere. TOOL-dSafePassage-26 §4 "Migration" is read as these
  rows. Observed by AC23.
- **S27** — id 45. TOOL-dSafePassage-26 S13's carried `core.autocrlf` and `core.eol` are read in the
  target: `git -C <target> config --get core.autocrlf`, and the same for `core.eol`, under the parent's
  ambient environment, so each carried pair equals the target's own effective value, its local
  setting included. Observed by AC24.
- **S28** — id 46. TOOL-dSafePassage-26 S31's corrupt image: an image that does not parse is
  discarded and rewritten only when `git -C <t> status --porcelain`, the image and its sibling aside,
  prints nothing, so no path has changed since `HEAD`; otherwise the up exits 1 naming the image (§8
  F3). A stale `<image>.govkit-new` sibling, which `write_atomic` leaves on a kill
  (`tools/govkit/govkit.py:4198-4221`), is unlinked by the walk before the up spawns and is never
  staged. That unit's AC30 is read with the image planted by a direct write. Observed by AC25.
- **S29** — id 47. TOOL-dSafePassage-26's AC46 is read with `GOV_PYTHON` unset and `python3`, `python`
  and `py` all fakes first on `PATH`: `python3` exits 1 under `-I` and 0 without, the other two exit
  9009, since `tools/lib/resolve-python.sh:30` tries every candidate before it refuses. The run exits
  non-zero and stderr names `python3` with `did not run`. Observed by AC26.
- **S30** — id 6. TOOL-dSafePassage-26 S40 is read as a recorded reading, that the build-order table's
  `Parallel` column is M6's candidate set; the edges it names already exist at HEAD, so S40 declares
  none. NOT OBSERVED: a reading of that item's role, and no pass changes what it reads.
- **S31** — id 20. TOOL-dSafePassage-26's AC39 is read as a regression guard, green before that unit's
  pass by the audit's measurement, kept so that a later edit taking one of those edges out reds it.
  NOT OBSERVED: the criterion stays as written, and only its role in the ledger changes.
- **S32** — id 7. TOOL-dSafePassage-26's AC48 is read as a figure note under its S50, a recorded
  reading: 5832 and 5382 tracked paths at `3708a705`, re-run at this disposal on 2026-10-23 (PINNED).
  NOT OBSERVED: the figure is pinned at a fixed sha, which no pass can move.
- **S33** — id 33. TOOL-dSafePassage-26's AC49 is read the same way under its S51: 80 matches of
  `make_target(` at `3708a705`, one the definition at line 679, re-run at this disposal (PINNED).
  NOT OBSERVED, for S32's reason.
- **S34** — id 8. TOOL-dSafePassage-26's Inventory is read with `resolve_landing_base` under "Moved,
  not minted": from `tools/govkit/govkit.py`, where TOOL-dSafePassage-10 mints it (its §4 "The
  base"), into `tools/govkit/upgrade_steps.py`, govkit importing it back, and its S2 names that unit's
  function by name. Observed by AC27.
- **S35** — id 23. TOOL-dSafePassage-26 S2's sentence on readers is read as: at TOOL-dSafePassage-10's
  landing `resolve_landing_base` is called by `cmd_epoch` in `tools/govkit/govkit.py` and by
  `tools/govkit/step_gate.py`, and `derive_push_base` by `cmd_frozen` in `tools/govkit/upgrade_steps.py`;
  its §10 cites TOOL-dSafePassage-10 §4 "The base" as the seam extended. Observed by AC27.
- **S36** — id 9. TOOL-dSafePassage-26 S52's first kit-resolution site is read as
  `tools/push-main.sh:445`, where `resolve_kit_dir "$py"` sits; `:440` is that pair's
  `resolve_python` line. NOT OBSERVED: a cite, and TOOL-dSafePassage-26's AC50 finds every site
  whatever the cite says.
- **S37** — id 27. The same site, read by the reuse lens: TOOL-dSafePassage-26 §10's `:445` is the one
  anchor for it, so S52 and §10 carry one number. NOT OBSERVED, for S36's reason.
- **S38** — id 34. The same site, read by the blast-radius lens at HEAD and at `3708a705` alike:
  `grep -n 'resolve_kit_dir "$py"' tools/push-main.sh` printed 445, 735, 763, 809 and 831 at this
  disposal. NOT OBSERVED, for S36's reason.
- **S39** — id 26, the skeptic's corrected fix. `render_row_order_key(kind, path)` in
  `tools/govkit/govkit.py` holds the one `update-<kind>-{render_order_slug(path)}` spelling. TOOL-dSafePassage-26
  S18's `write_row_order` and `write_conflict_candidate` (`tools/govkit/govkit.py:9063-9072`) both
  call it, the latter for its candidate directory, so the order and its directory share one key.
  That unit's AC17 is read as AC28 of this unit. Observed by AC28.

## 3. Non-goals (OUT)

- Every high: units 27 to 34.
- Rewriting a built spec. An item that corrects a built spec's text states the reading here; S25 edits
  a live spec only.
- The report's left-shift lints beyond the arms named in §7: a spec lint for `<path>:<line>` cites, an
  already-green-at-HEAD check, and the checklist entries the report proposes per item.

### Edges

- **consumes-from** `TOOL-dSafePassage-16` — the predicate and its criteria, which S14, S15 and S16 read
- **consumes-from** `TOOL-dSafePassage-17` — the no-image downs and the floor-row block, which S17 and S22 read
- **consumes-from** `TOOL-dSafePassage-18` — the schema-step plants, which S18 reads
- **consumes-from** `TOOL-dSafePassage-19` — the kill-before-stamp re-run and its AC2, which S19 and S20 extend and read
- **consumes-from** `TOOL-dSafePassage-20` — the Goal's cites and the Inventory's refusal-join sentence, which S9 and S21 read
- **consumes-from** `TOOL-dSafePassage-21` — `read_plan_destinations` and the file class's sources, which S1, S2 and S3 amend
- **consumes-from** `TOOL-dSafePassage-22` — the lock plants and `REUSE_MARGIN_S`, which S4, S5 and S7 amend, and the leg its arm runs in, which S6 guards
- **consumes-from** `TOOL-dSafePassage-23` — the resolver's AC6, which S13 reads
- **consumes-from** `TOOL-dSafePassage-24` — the step contract's refusal and its uncovered sentence, which S8 and S9 extend and read
- **consumes-from** `TOOL-dSafePassage-25` — the gov-first snapshot sites and their fixture, which S10, S11 and S12 amend
- **consumes-from** `TOOL-dSafePassage-26` — the base rule, the floor down, the step module, the lock's namespace, the carried keys, the image writer, the outbox orders and the criteria S22 to S39 read
- **consumes-from** `TOOL-dSafePassage-27` — the prepared path's one snapshot, which S10 routes through the helper
- **consumes-from** `TOOL-dSafePassage-29` — `STEP_REFUSED_KEYS`, which S8 extends with the credential values
- **consumes-from** `TOOL-dSafePassage-31` — the `pid_ns` row, before which S26 places the boot rows
- **consumes-from** `TOOL-dSafePassage-32` — the boot frame of the reuse estimate, which S5 and S7 state per backend
- **consumes-from** `TOOL-dSafePassage-33` — the no-record branch of the down's verdict, which S19 and S20 rest on
- **hands-off** `TOOL-dSafePassage-38` — S8's credential rows restated as one predicate over keys and values, and every refusal line's keys redacted, the repair of finding 30 of the spec audit of units 27 to 35
- **hands-off** `TOOL-dSafePassage-42` — findings 25, 3, 13 and 19 of the spec audit of units 27 to 35, AC9 counting code lines and `remove_new_untracked` calling `write_untracked_snapshot`; finding 11, AC12's population as the parity arm's own; finding 12, S24's moved set as its ast closure, `demand_safe_token` and eight constants included; findings 4 and 15, AC18 read as a regression guard; and finding 16, the `BRANCH_PIN` and filter cites
- **hands-off** `TOOL-dSafePassage-44` — S8's `remote.<x>.url` and `remote.<x>.pushurl` rows, which that unit's pass removes in favour of `test_credential_bearing` and its ssh exemption, finding 3 of the spec audit of units 43 to 46

## 4. Design

### The cites, by phrase

S21's readings. Each phrase is quoted from the cited spec's text at this disposal, and each prints
once under `git grep -c -F`.

| Citing spec | Cited spec | Section | Phrase |
|---|---|---|---|
| TOOL-dSafePassage-20 §1 | TOOL-dSafePassage-1 | §4, the derived introducing commit | `The derivation reads the declaring files' blobs commit by commit` |
| TOOL-dSafePassage-20 §1 | TOOL-dSafePassage-2 | §4 | `is the reader's derived value` |
| TOOL-dSafePassage-20 §1 | TOOL-dSafePassage-3 | §4 Data model | `that is neither a 40-hex string nor` |
| TOOL-dSafePassage-16 §1 | TOOL-dSafePassage-3 | §4 Data model | `an id that is not a string, a state outside the three` |
| TOOL-dSafePassage-16 §1 | TOOL-dSafePassage-2 | §3 | `how the schema step's own row` |
| TOOL-dSafePassage-19 §1 | TOOL-dSafePassage-4 | §4 Migration | `ends with that step's down` |
| TOOL-dSafePassage-21 §1 | TOOL-dSafePassage-10 | §4, the class table | `in gov's source-mode receipt` |
| TOOL-dSafePassage-21 §1 | TOOL-dSafePassage-10 | §4, the verdict | `class whose tip population is empty is exit 2` |

### The lock's namespace verdict, whole

The rows after this unit, in the order `check_holder_dead` applies them:

| Test | Verdict |
|---|---|
| lock `host` differs (TOOL-dSafePassage-2 S7) | `unknown` |
| lock `platform` differs (TOOL-dSafePassage-26 S33) | `unknown` |
| same `host` and `platform`, both `boot_id` non-empty and different (S26) | `dead` |
| `pid_ns` differs, or absent on a Linux judge (`TOOL-dSafePassage-31`) | `unknown` |
| otherwise | the census test of TOOL-dSafePassage-2 S7, in `TOOL-dSafePassage-32`'s frame |

### Inventory

Minted: `write_untracked_snapshot` in `tools/push-main.sh` (cell `sh.function`, verb `write`, OK by
`python tools/lexicon/lexicon.py --suggest write_untracked_snapshot --as sh.function` on 2026-10-23);
`render_row_order_key` in `tools/govkit/govkit.py` (cell `py.function`, verb `render`, OK by the same
command with `--as py.function`); the plants `stale-receipt`, `local-url-userinfo`,
`schema-step-kill-shipped-rows`, `lock-other-boot`, `lock-no-namespace`, `autocrlf-local`,
`corrupt-image` and `stale-image-sibling`. Moved, not minted: `resolve_shell_argv`, `resolve_bash`,
`resolve_tokens` and `target_context`, into `tools/govkit/upgrade_steps.py`. No conf key, gate leg or
policy key; S6 edits one leg's guard. S28's refusal is one new `raise Refusal` site, so
`tools/govkit/refusal_join.py`'s `BRANCH_PIN` moves by one.

### Migration

Additive. No receipt at the base records a step, no lock carries a namespace field, and no landed
step row exists, so no item changes a recorded value.

### Rollout

Live at landing. It builds at order 8, after every unit of the build, units 27 to 34 included. Its
items share `tools/govkit/govkit.py`, `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py`
with each other, and the lander items' fixtures run govkit's walk, so the pass is one unit: the minors
do not split into two disjoint write sets by M6.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/upgrade_steps.py`
- `tools/govkit/step_gate.py`
- `tools/govkit/selftest.py`
- `tools/govkit/steps/template_size_limits.py`
- `tools/govkit/refusal_join.py`
- `tools/gate-legs.json`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/lib/python-floor.sh`
- `tools/lib/python_floor.py`
- `tools/lib/resolve-python.test.sh`
- `help/upgrade-steps.md`

TOOL-dSafePassage-26's spec joins this unit's `--dispatch --writes` when S25 edits it.

### Alternatives rejected

- **Two batch units, the lander's three items apart.** Their fixtures run govkit's walk, whose code the
  other items write, so the second would read the first's output as an acceptance input (M6 clause 2).
- **Folding each minor into its unit's spec.** The disposal promotes, never folds (BUILD-METHOD M4).
- **A receipt cross-check in the file class (S3).** On a branch the receipt is the last landing's, so
  a cross-check would differ on every branch that changes a destination.

## 5. Production-readiness checklist

- security: S8 refuses credential-bearing values and never prints one; S27 carries the target's own
  line-ending values and no credential; S26 reclaims only a lock a reboot provably ended on one host.
- perf / scale: one `git config` read per step for S27; nothing else measurable.
- error / empty / loading states: S11's unwritable snapshot and S28's corrupt image each refuse by
  name, never silently.
- observability: every new refusal names its file, key or stage.
- risks: S26 reads a differing `boot_id` as dead on one hostname, so two kernels that share a hostname
  and a tree would be judged one host, which the help page states; S24 moves four functions other
  suites monkeypatch, and govkit re-imports each name.
- testing: the probes and fixtures of §6 and the arms of §7.
- migration: §4 "Migration".
- user docs: `help/upgrade-steps.md` (S8, S14, S26).

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/govkit.py` by path and calls
  `read_plan_destinations` on gov's root, no destination starts with `.gitattributes:` and each is the
  `dest` of a `kind == "write"` row with empty `missing`; on a scratch gov planting an `lf_pin` and a
  `project-owned` rule, `read_file_members` returns neither.
  Red when: an `order` or `side-effect` row's destination is a member.
- **AC2** — When `python tools/govkit/govkit.py update --target . --write` runs in a scratch clone of
  gov, the receipt's `files` paths equal the set `read_plan_destinations` returns on that tree.
  Red when: the receipt records a pseudo-destination.
  fixture: a scratch clone under `%TEMP%`.
- **AC3** — When `python "tools/govkit/step_gate.py" --fixture --plant stale-receipt` runs, a branch
  carrying the last landing's source receipt that deletes a shipped file exits 1 naming the `file:`
  member.
  Red when: the class reads the stale receipt and the branch is green.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-live-slow-census`
  runs, the take refuses busy and exits 1, and the same plant run against a judge copy that reads the
  clock after the census reclaims.
  Red when: the plant is green under the staged judge copy.
- **AC5** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-reused` runs five
  times in a row, each reclaims and exits 0, and the lock it planted reads a `started` 600 s before the
  run.
  Red when: any run reads the reused pid `live`.
- **AC6** — When a `python -c` probe loads `tools/gate-legs.json`, the `govkit selftest` leg's guard
  holds `{prefix}/process-monitor/census.py`.
  Red when: an edit to the census alone selects no leg that runs the reclaim's arm.
- **AC7** — When `git grep -n -A4 "REUSE_MARGIN_S =" -- tools/govkit/upgrade_steps.py` runs, the
  comment names `windows-join` with 0.5 s and `posix-ps` with 1 s.
  Red when: one bound is stated for both backends.
- **AC8** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant local-url-userinfo`
  runs, with `remote.origin.url` an `https` URL carrying a user and a password, the step is refused
  naming `remote.origin.url` and `.git/config`, the output holds neither the user nor the password,
  and the run exits 1; with an scp-form `git@host:x` URL it is not refused.
  Red when: a credential in a URL passes, or the refusal prints it.
- **AC9** — When `git grep -n "write_untracked_snapshot" -- tools/push-main.sh` runs, it prints the
  definition and three calls, and `git grep -c "ls-files --others --exclude-standard -z" -- tools/push-main.sh`
  prints 2, the helper's and `remove_new_untracked`'s.
  Red when: a snapshot site keeps its own inline line.
- **AC10** — When `bash tools/push-main.sh --prepare --slug fx` runs in TOOL-dSafePassage-8's AC5
  fixture with `TMPDIR` naming a file, so `mktemp` fails, it exits 1 with the gov-first stage's
  refusal line, and no receipt or before-image exists in the fixture.
  Red when: the walk runs after the snapshot failed.
- **AC11** — When the attended landing of TOOL-dSafePassage-8's fixture runs with its planted failing
  witness, it exits 1 and `git status --porcelain` prints nothing; the retry without the plant exits 0
  and `git show --name-only` of its mint, steps and regeneration commits names no file the refused
  run made.
  Red when: the attended refusal leaves the walk's files for the retry's `git add -A`.
- **AC12** — When a `bash -c` probe extracts every `resolve_python` block between its markers in the
  files `git grep -l "# >>> resolve_python"` prints, strips CR bytes and compares each with the
  canonical block of `tools/lib/resolve-python.sh`, no copy differs; with one copy staged on the
  pre-unit echo rule, the probe names it and `python tools/lib/python_floor.py check` stays silent.
  Red when: TOOL-dSafePassage-23's ledger answers AC6 with a command that cannot see the drift.
- **AC13** — When `git grep -n -i -F "below schema 4 no step row is persisted" -- help/upgrade-steps.md`
  runs, it prints the receipt section's sentence.
  Red when: the page words the rule another way and the criterion's literal is fitted to it.
- **AC14** — When a `python -c` probe parses `tools/govkit/upgrade_steps.py` with `ast`, it finds one
  `def test_steps_recordable`, one call of it inside `set_step_state`, and no `Compare` node in
  `set_step_state` reading `schema`.
  Red when: the writer keeps a schema comparison of its own beside the predicate.
- **AC15** — When `python tools/govkit/steps/template_size_limits.py down <t> tools` runs on a scratch
  target with no limits file and no image under `.governance/steps/govkit/`, it exits 0 and
  `git -C <t> status --porcelain` prints nothing.
  Red when: the program refuses before the shared helper for want of an image.
- **AC16** — When `git grep -n -F "schema-step-early" -- tools/govkit/upgrade_steps.py` runs, it prints
  the plant's definition in the `rollback` family.
  Red when: the criterion's plant is not built.
- **AC17** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant schema-step-kill-shipped-rows`
  runs, the re-run exits 0, both shipped-shape rows are downed a second time with their targets'
  bytes unchanged by that down, and the receipt and record bytes, times aside, equal an uninterrupted
  run's.
  Red when: the re-run stops on a row whose witness no down can falsify, or a second down changes a
  byte.
- **AC18** — When `git grep -c -F "<phrase>" -- <cited spec>` runs for each row of §4 "The cites, by
  phrase", each prints 1.
  Red when: a phrase is quoted that its spec does not carry, or carries twice.
- **AC19** — When `bash tools/lib/python-floor.sh down 3.11 <clone>` runs from a scratch clone whose
  plant `v = f"{"X" if c else "y"}"` is committed at `HEAD`, it exits 1 naming the plant, and
  `bash tools/lib/python-floor.sh down 3.11 <clone> <to>` with `<to>` before the plant exits 0.
  Red when: the call without `<to>` grades the working tree, or either call form refuses the other.
  fixture: a scratch clone under `%TEMP%`, in `static` mode on node d, as TOOL-dSafePassage-11's AC6
  runs.
- **AC20** — When `python tools/lib/python_floor.py check --rev 3708a705` runs, it prints seven
  statements, `tools/lexicon/selftest.py:109` among them.
  Red when: the pattern is widened until line 108 matches.
  figure: seven and the line are PINNED at `3708a705`, re-derived by this command.
- **AC21** — When a `python -c` probe parses `tools/govkit/upgrade_steps.py` with `ast`, it finds no
  import of `govkit` and no name govkit defines that the module does not define or copy itself, and
  `git grep -c "^# >>> resolve_kit_dir" -- tools/govkit/upgrade_steps.py` prints 1.
  Red when: the step module reaches back into govkit for a function.
- **AC22** — When `python tools/check-spec-tokens.py` runs after the pass, its guards line names no
  hit `memory-hygiene self-test <- tools/check-spec-tokens.py` or
  `build-index selftest <- tools/check-spec-tokens.py` against TOOL-dSafePassage-26's spec.
  Red when: that spec is live and its leg line still omits either leg.
- **AC23** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-other-boot` runs,
  a lock from this host and platform with a different non-empty `boot_id` is reclaimed and the run
  exits 0; `--plant lock-no-namespace` is judged by the census on node d and reads `unknown` under the
  fixture's Linux stub of `read_pid_namespace`.
  Red when: a lock a reboot ended refuses forever, or a lock with no namespace field is reclaimed on
  Linux.
- **AC24** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant autocrlf-local`
  runs, with the target's local `core.autocrlf=false` and the parent's global `true`, the step's
  `git hash-object --path` oid equals the one `git -C <t> hash-object --path` prints in the parent's
  environment, and the run exits 0.
  Red when: the parent's global value overrides the target's local one.
- **AC25** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant corrupt-image` runs on
  a clean scratch target, the image written as non-JSON is rewritten and the step applies; with
  another tracked path changed, the up exits 1 naming the image; `--plant stale-image-sibling` leaves
  no `.govkit-new` file under `.governance/steps/` and `git -C <t> diff --cached --name-only` names
  none.
  Red when: a corrupt image is read, discarded over a changed path, or its sibling is staged.
- **AC26** — When `bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh` runs with
  `GOV_PYTHON` unset and fakes for `python3`, `python` and `py` first on `PATH`, it exits non-zero and
  stderr names `python3` with `did not run`.
  Red when: a real launcher or the override satisfies the resolver and the fake is never probed.
- **AC27** — When `git grep -n "resolve_landing_base" -- tools/govkit` runs, it prints one definition in
  `tools/govkit/upgrade_steps.py`, govkit's import of it, and the calls in `cmd_epoch`, `cmd_frozen` and
  `tools/govkit/step_gate.py`.
  Red when: a second definition survives in govkit, or a named caller resolves its base itself.
- **AC28** — When `git grep -n -e 'update-conflict-' -e 'outbox / f"update-' -- tools/govkit/govkit.py tools/govkit/upgrade_steps.py`
  runs, every hit keyed on a row's path or a step's slug sits inside `render_row_order_key`, comment
  and glob lines aside.
  Red when: the conflict candidate's directory is named by its own f-string.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `push-main self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC3 AC4 AC5 AC8 AC17 AC23 AC24 AC25 · the self-test runs each plant this unit adds or pins, its failing cases staged by the staged judge copy, the stubs and committed direct writes · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by one
New arm: tools/push-main.test.sh · covers AC10 AC11 · the unwritable-snapshot landing and the attended landing with a failing witness, each failing case staged by a lander copy whose snapshot site keeps its inline line · none
New arm: tools/lib/resolve-python.test.sh · covers AC26 · every launcher faked and the override unset, its failing case staged by a fake set that leaves `py` real · none

## 8. Open questions

- **F1 — Is `<to>` optional on the floor down (S22)?** Options: optional, defaulting to the target's
  `HEAD`; or required, with TOOL-dSafePassage-11's AC6 and AC7 read with `<to>` named. Both satisfy
  every criterion; the first leaves TOOL-dSafePassage-11's two criteria standing as written and keeps
  one code path, grading at a commit either way. RESOLVED (agent, 2026-10-23, delegated): optional,
  defaulting to `HEAD`, on rung 3. widens: none · relaxes: none
- **F2 — A second down on a re-run after a killed rollback (S20).** Options: accept it, idempotent,
  narrowing TOOL-dSafePassage-19's AC2; or keep a progress marker so the re-run skips rows already
  rolled back. TOOL-dSafePassage-19 S4's own design re-probes and re-downs, and the marker would be a
  second record of progress beside the receipt's. RESOLVED (agent, 2026-10-23, delegated): accept the
  idempotent second down, on rung 3. widens: none · relaxes: none
- **F3 — When may a corrupt image be discarded (S28)?** Options: when no path has changed since
  `HEAD`; when no path of a declared write set has changed; never, always refusing. No step declares a
  write set, so the second cannot be built; the first keeps TOOL-dSafePassage-26 S31's recovery on a
  clean tree and refuses wherever it cannot tell. RESOLVED (agent, 2026-10-23, delegated): the first,
  on rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the round-1 spec audit of units 15 to 26's 20
  MEDIUM and 19 LOW findings, one scope item per raw id.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-38`, `TOOL-dSafePassage-42`; no other section moved.
- rev-3 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 43 to 46, written by the disposal stage: `TOOL-dSafePassage-44`; no other section moved.

## 10. Reuse audit

The seams extended are named per item: `planned_writes` and `LANDABLE_ROLES`
(`tools/govkit/govkit.py:3830`, `:3988`), the lander's snapshot pair (`tools/push-main.sh:777-793`),
the resolver's parity arm (`tools/lib/resolve-python.test.sh:159-233`), `write_atomic`
(`tools/govkit/govkit.py:4198-4221`), `write_conflict_candidate` (`:9063-9072`) and
`render_order_slug` (`:5735`), the census backends (`tools/process-monitor/census.py:63-70`,
`:194-228`), the leg guards (`tools/gate-legs.json`), and the specced seams of units 16 to 33.
`python tools/codebase-map/reuse_lookup.py "snapshot the untracked files before a stage"` ranked
`before`, `corpus_files` and `stage_or_fail`, none of them the lander's pair, which the batch found by
reading `tools/push-main.sh`; every other seam was found by reading the line the report cites, and
where the report and the source disagreed by a line, the source's line is cited.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`

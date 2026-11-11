**Serves:** journal PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-7

# Round-4 fold returns — the two spec-writers, 2026-11-04

## units 11, 41, 20 (handoff 2026-11-04-prompt-PLAY-dConvergedCharter-11-2-spec-writer)

I folded the round-4 findings for units 11, 41 and 20. Two things need you:
- Unit 11 grew to 88,324 bytes, about 12.6 KB past the 75.7 KB the owner accepted, so its size needs a fresh ruling.
- Unit 41 now has an open owner fork (F3, below).

The token check was not run: the role guard refuses `python tools/check-spec-tokens.py` for a spec-writer, so the main loop has to run it. Units 12 and 21 needed no reciprocal edit, I wrote no deviation record, and nothing is committed.

## Specs

| Spec | Rev | Bytes |
|---|---|---|
| unit 11 (`2026-11-03-spec-PLAY-dConvergedCharter-11.md`) | rev-6 → rev-7 | 88,324 |
| unit 41 (`2026-11-04-spec-PLAY-dConvergedCharter-41.md`) | rev-2 → rev-3 | 44,748 |
| unit 20 (`2026-11-03-spec-PLAY-dConvergedCharter-20.md`) | rev-5 → rev-6 | 44,331 |

Each spec stays DEFERRED on the same base and has one §9 line naming `2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1`.

## Findings

Unless a line says otherwise, I folded the fix the review judged sound. Findings 20, 25 and 27 were refuted, so nothing was folded for them.

- **1 and 11 (B1), unit 11:** the caps that move into `budgets.<cap>` are now worked out from `caps.toml` rows of class `switch` (five at base, not six). `READ_PATH_WAIVER` becomes an ordinary list-type row, so 96 rows are minted instead of 95. New AC27 checks that `policy.py check` passes and that check 16 still reads gov's waiver.
- **2 and 12 (H1), units 11 and 41:** `budgets.py resolve` gains `--rev`. The hygiene engine and `gotchas.py` read the caps at `HEAD`, with the reasoning stated: at base these values sat in an unguarded working-tree file, so reading the guarded file at `HEAD` loosens nothing. AC24 now runs on a clone whose remote predates the fold, and includes the case where the landed revision lacks the value. Unit 41's half is folded under 36.
- **28 (H2), units 11 and 41:** unit 11 S4 re-points `drift_report.py`'s two history readers of `LANGS`. The staleness check now picks the newest commit where the `LANGS` value actually changed, so the fold itself does not count. §4 names history readers, the two drift-audit legs are in §7, and AC28 plus an arm cover it. Unit 41 §3 says `drift_report.py` belongs to unit 11.
- **34 (H3), unit 11:** the three walk-up root resolvers apply the presence test at every level, in one condition: "the home exists here, or this level holds `.git` and `legacy` prints a folded key". This is the skeptic's corrected fix in a form that `arm_folded_homes` passes without new exemption rows. `--root` is never refused. AC29 covers the two Python resolvers. `adopt-codebase-map.sh` has no `--check` flag, so its walk is graded only by the presence arm.
- **35 (H4), unit 20:** S1 now states the adopter's commit route, which is unit 11's two commits applied at the adopter. The owner commits only `.governance/policy.toml` from a terminal, then the agent renders the mirror and commits it with the removed home lines. The step prints the route as its last line. Until that second commit, scratch-guard reads UNARMED; the spec says so, and the route needs no routed write in that window. AC10 and AC11 are new.
- **3 (M2), units 11 and 41:** the guards of the re-pointed suites' legs gain `policy.py`, plus `policy-mirror.js` for the hook legs (unit 11 AC30, unit 41 AC12). The `--legs-for` flag the review cites does not exist, so both ACs read `tools/gate-legs.json` directly.
- **5 (M4), unit 11:** AC25 now takes its names from `legacy <home> --keys`, prints the count, and goes red at 0 or at any count other than 96.
- **6 (M5), unit 41:** S1's delete-or-reword list is defined as whatever AC2's command prints at the pass's base. The four lines the review found are named as of `52945ea0d`.
- **9 (L3), unit 11:** §4 now keeps only the `CODE_PATHSPECS` hits for re-pointing and rewords the prose hits.
- **13 (M6), unit 11:** the seam is now cited at `run-gates.sh:2829-2843`. The condition at `:2830` is replaced and the prelude's test at `:1543` goes.
- **18 (L5), unit 11:** the toplevel lookup is now cited at `policy.py:1409`.
- **21 (M10), units 41 and 11 — needs you:** the straggler guard's function is renamed `read_policy_backlog_mode` and held to `parse_policy` by a spelling table, and §5 is corrected. Neither fix is mine to decide: one makes an exception to the "one reader of the policy file" decision, the other breaks the guard's python-free rule. Both are recorded rulings, so I wrote them as new open fork F3. I recommend (a): keep the guard's narrow shell read under that parity table, as the guard already does for its conf. Unit 11 §4 now points to F3.
- **22 (M11), unit 41:** `read_modes` reads through `render_folded_lines` once per distinct pair of blobs, and AC3 checks it equals `legacy --rev` at each commit.
- **23 (M12), units 11 and 20:** the type names now use the catalogue's own vocabulary, and both the rendering and its inverse use `render_toml_value`'s spellings. AC1 in unit 20 and AC14 in unit 11 now say `list` and `count` rows.
- **24 (M13), units 11, 20 and 41:** `derive_home_folds(rows, home)` now lives in `policy.py` as the only reader of the `legacy` field, exposed as `legacy --keys`. Unit 20 imports it and no longer mints it, unit 41's placeholder arm calls `--keys`, and unit 11's AC33 is the parity check.
- **29 (M15), unit 11:** S2 says govkit check 7h3 has nothing to grade on gov's tree after the fold, and selftest M5 grades a planted line instead of gov's. AC31 shows 7h3 still going red on a planted shipped assignment.
- **30 (M16), unit 11:** `manifest-check self-test` is added to §7.
- **31 (M17), unit 11:** the fork-ceiling rows a re-point affects are now found by measuring before and after, not by listing them. Rows that copy a folded home (`unattended-status` among them) also copy `.governance/policy.toml`, and F5 names `unattended-status`.
- **32 (M18), unit 11:** the help page, the hooks README and `agent-cap.js`'s denial messages are reworded to point at the policy-file key. AC32 is a grep that checks it.
- **36 (M19), unit 41:** `held_halves.py` reads the gate file through `legacy` at `HEAD` instead of `get`, and a failed read is refused through `print_refusal` (AC4). As a result no folded key is read through `get` any more, so every row in unit 11 now has a derived default (S1 and F2 simplified).

One extra fix in unit 41: AC10 used to run `straggler-guard.test.sh`, which ACs may not name, so it now runs the guard's `read_conf_modes` directly.

## Checks
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`: exit 0, no red on this build's specs. The first run flagged one item in unit 11 (a value spelled in backticks inside S2's readers list); I fixed it and reran.
- `python tools/check-spec-tokens.py`: not run (refused by the role guard, as above).

No acceptance criterion names the bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run. The one path that does not exist yet, `conf_to_policy.py`, appears by basename in AC33.

## units 7, 9, 13, 17, 38, 40 (handoff 2026-11-04-prompt-PLAY-dConvergedCharter-7-1-spec-writer)

I folded all 13 findings into the six specs in my set. My six specs pass the hygiene gate, but its exit is 1 because of a red in unit 11, which belongs to the parallel writer. I could not run the spec-token check: the role allowlist blocks it.

**Specs** (each status still DEFERRED, base unchanged, one revision-log line naming `2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1`):

| Unit | New rev | Bytes |
|---|---|---|
| PLAY-dConvergedCharter-7 | rev-5 | 45,987 |
| PLAY-dConvergedCharter-9 | rev-5 | 34,913 |
| PLAY-dConvergedCharter-13 | rev-5 | 27,771 |
| PLAY-dConvergedCharter-17 | rev-4 | 27,948 |
| PLAY-dConvergedCharter-38 | rev-3 | 17,449 |
| PLAY-dConvergedCharter-40 | rev-2 | 18,434 |

**Findings:**
- **4 → unit 17.** The review's fix. S4 now says a records path ending `/build` and followed by a space, quote or `)` is a value hit. S4 sorts every hit it missed:
  - re-pointed: `SESSION-KICKOFF.md:54` and `VERBS.template.md:821` with its render;
  - rewritten with a trailing `/`: `WIRE-INTO-PROJECT.md:328`;
  - moved into the held set: the comments at `selftest.py:2818,9547`, `.gitattributes:141` and `adopt-roles.sh:2,35,375`;
  - excepted: the records paths in `unattended.test.sh`.
  
  AC4's except set is now worked out at the pass from S4's sort of the readers command's output, not typed.
- **7, 17, 33 → unit 7.** The review's fix, widened by `git grep` at base. S8's readers gain:
  - `fork-ceilings.txt:20`: setup `cp` and argv re-pointed, count re-measured, which is not a ceiling raise;
  - the moved `manifest-check.test.sh`, whose fixtures spell the old path;
  - `memory/README.md`;
  - six map dossiers, with `memory/map/generated/` regenerated;
  - three gotcha pages, which the dead-path gate treats as live.
  
  §7 gains the spawn-budget and codebase-map legs. AC10 now also leaves out `memory/DECISIONS.md` and `memory/archive`.
- **8 → unit 38.** The review's fix. The §6 preamble gives the real `--fixture [--strict-from <dir>] [<case>]` grammar and drops the claim that unit 11 owns the verb.
- **10 → unit 13.** The review's fix. The hands-off edge now names `guide_move.py`, S4's write route and `--residue`. Unit 1's consumes-from edge already names all three, so I made no edit outside my set.
- **14 → unit 38.** The review's fix. AC2's "no bash sees" case is injected by replacing `resolve_bash` in process. AC2 states why: Git for Windows' fixed paths (`check_policy.py:903`) always see the script on gov's nodes. The new-arm line names the injected case.
- **15 → unit 7.** The review's fix. S8 gains a commit route: the owner commits the two `.governance/deploy.toml` edits and the manifest's `git mv` from a terminal, before any agent commit. The Migration and Files touched say the same. New AC14 watches the guard refuse an agent-staged edit.
- **16 → unit 40.** The review's fix. `Successor` is dropped and `Proof` is set to `none — agent pass`. AC1 holds the record to the parent's `edit` field set.
- **19 → unit 13.** The review's fix. §4 Evidence and F4 now cite the live `resolve_bash_py` row (`resolve-python.test.sh:369`) and mark `render_envelope` as unbuilt.
- **26 → unit 9.** The skeptic's corrected fix.
  - The UP clears the old path, then writes the row's forwarder at the target's old path under the `skill` kind's write rule.
  - The DOWN clears the forwarder first. The WITNESS requires a file at the old path that is not a kit render.
  - A file carrying the row's marker is treated as the forwarder and never classified.
  - The Migration's `shims.py --write` sentence is gone. New AC10 checks for the forwarders after `govkit update --write` at a scratch adopter, and is red when the UP skips the forwarder.
- **37 → units 13 and 40.** The skeptic's corrected fix, closed more simply in unit 40.
  - Unit 13: `written` holds only when both the row and its change record exist, and `write` writes only the missing part. New plant `feature-record-interrupted`.
  - Unit 40: the amend writes its record before the row. That is the only order in which `Before` can still be read, because after the row is rewritten a re-run cannot recover it. Each part is skipped by its own test. New plant `amend-interrupted`.
- **38 → unit 40.** The review's refusal option. A plan with two entries on one `target` exits 2, naming both sections and the tag, and all three refusals read the manifest on disk. New plant `amend-two-sections`. I recorded the choice as fork F1 in §8, resolved: refuse rather than merge.
- **20, 25, 27:** refuted, nothing folded.

No fold departs from a clause, so I wrote no deviation records.

**Checks:**
- **Hygiene** (`check-memory-hygiene.sh --only 2,12,25`): exit 1. My six specs are clean. The one red is check 25 on unit 11 S2 (`GATE_DOC_PATHS="memory/ README.md"`). My first rerun also caught unit 9 S4: "removes" set off the retire predicate, so I reworded it to "clears".
- **Spec tokens** (`check-spec-tokens.py`): not run, because scratch-guard blocks that leg for gov-spec-writer. The main loop needs to run it. My own probe of the backticked paths I added found no new unresolved name. The ones that don't exist yet sit under READER NOT IN TREE or were already in the specs.
- **Criteria:** no criterion I added names the bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run. Paths not present at HEAD are cited by basename.

**Not folded, for the next round:** unit 13 S4's add record names no `Proof`, which the parent grammar requires. No finding covered it.

Files are in `C:\projects\coding-governance\.claude\worktrees\unattended-dconvergedcharter-51d347\memory\builds\dConvergedCharter\spec\`:
- `2026-11-03-spec-PLAY-dConvergedCharter-7.md`
- `2026-11-03-spec-PLAY-dConvergedCharter-9.md`
- `2026-11-03-spec-PLAY-dConvergedCharter-13.md`
- `2026-11-03-spec-PLAY-dConvergedCharter-17.md`
- `2026-11-04-spec-PLAY-dConvergedCharter-38.md`
- `2026-11-04-spec-PLAY-dConvergedCharter-40.md`

## Follow-ups to the units 11, 41, 20 writer

- The owner resolved unit 41's F3 as (a) on 2026-11-04; the writer marked it `RESOLVED (owner, 2026-11-04)` with the
  ruling record's path after the closing paren (its first mark put the path inside the parentheses, which the fork
  readers' closed grammar reads as unresolved), and re-pointed unit 11 §4's mention of F3.
- Unit 11 F4's mark, wrapped across two lines since rev-1, joined onto one line; no content change, riding rev-7.

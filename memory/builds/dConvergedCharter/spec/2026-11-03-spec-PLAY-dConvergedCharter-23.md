# PLAY-dConvergedCharter-23 — the release asks' join: one key hash and one ask text for Maintain's and `release.route`'s `release-verify-failed` filings

**Status:** OPEN · rev-3 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 9 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0502@fbfa8f4f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 |
| [2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md](../build/2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md) | research | PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |
| [2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-39 |

<!-- /gen:spec-records -->

## 1. Goal

A red verify under `deploy.on-verify-fail = roll-forward` reaches two filers: `release.route` files an ask at
verify time (DEPL-dShippedRelease-15 S10) and Maintain's `release-verify-failed` event later files its own
(TOOL-dTendedCadence-15 S2). As specced the two key the failure differently, so one failure leaves two open asks,
the clause's seen-red case (layer-expansions `[design-observability]`, B5-F14). This unit gives both filers one
key hash, `derive_key_hash`, moved to `tools/lib/key_hash.py`, and one ask text rendered by one block, so the
second filing lands on the first ask as a `seen` row, and it owns the fixture that joins the two real halves.

## 2. Scope (IN)

Build-run preconditions, each specced and DEFERRED at base `0d1c1dda`, all in ancestors of this build so landed
before its build run: DEPL-dShippedRelease-15 S10 (`run_release_route`, `tools/integrations/release.py`, its
fixture `tools/integrations/release_fixture.py`), TOOL-dTendedCadence-15 S2 (`write_breach_ask`,
`tools/drift-audit/maintain_file.py`), TOOL-dTendedCadence-8 (the `[[reading]]` row and the I5 offender key),
TOOL-dTendedCadence-2 S3-S4 (`EVENT_PRODUCERS`), TOOL-dCalibratedLens-5 S8 (`derive_key_hash` in
`tools/loop/loop_review.py`), TOOL-dWellOiledMachine-27 S1 (`intake.py file --origin cadence`) and S4 (Entry places
a cadence intake as an `ask`), and the four asks §8 F4 states. None of these files exists at base.

- **S1** — The key hash factory. `tools/lib/key_hash.py` holds the canonical block
  `# >>> derive_key_hash — canonical copy: key_hash.py in gov's lib dir (byte-identical; gated)`, defining
  `derive_key_hash(kind, key) -> str`, the first 16 hex of the SHA-256 of the UTF-8 bytes of `"<kind>\t<key>"`.
  `<prefix>/lib/` ships nothing, so each consumer carries the block inline, as `resolve_kit_dir` is carried
  (`tools/lib/resolve_kit_dir.py:1-14`): `maintain_file.py` (TOOL-dTendedCadence-15 S2's hash),
  `loop_review.py` (TOOL-dCalibratedLens-5 S8's function of the same name and arguments) and `release.py`. Each
  consumer's own hash expression gives way to a call of the inline function, its bytes unchanged. Observed by AC1
  and AC5.
- **S2** — The one ask text. `render_breach_text(reading, offender_key, band, probe)` returns
  `maintain key <derive_key_hash(reading, offender_key)> · <reading> over its pin · <offender key>` followed by
  the clause tail TOOL-dTendedCadence-15 S2 spells, `accept <reading> back under its pin for this offender`,
  `data band <band>`, and `data probe <probe>` when `probe` is given, each joined by the ` · ` separator
  `render_clauses` writes (`tools/memory-tree/backlog.py:76`, `:1523`). It is extracted from
  `write_breach_ask` as the canonical block `render_breach_text` in `maintain_file.py`, which `write_breach_ask`
  then calls, and carried inline in `release.py`. Observed by AC2 and AC5.
- **S3** — `release.route`'s filing. `run_release_route` files, under each value of `deploy.on-verify-fail` that
  files, the text `render_breach_text("release-verify-failed", "<sha> <E>", "act", None)` through
  `python intake.py file --origin cadence --filer item.release.route`, in place of S10's text
  `release-verify-failed <sha> <E>`. The offender key is I10's, `<40-hex sha> <E>`, space-separated. Its key is
  then the reading `release-verify-failed` and (SHA, E), the clause's (reading, (SHA, E)). Observed by AC2 and
  AC3.
- **S4** — The joined fixture. `python release_fixture.py --case verify-join` plants a red verify under
  `roll-forward` in a scratch repository with both halves real and a stub Entry that places each intake as an ask
  in a fixture `BACKLOG.md`. It runs `run_release_route`, then Maintain's `run_breach_route` with the breach
  `release-verify-failed` and offender key `<sha> <E>`, once under each `maintain.tiers` value, and asserts one
  open ask carrying `maintain key <16 hex>`, one `seen` row on it, and the route `seen` printed. Its second order,
  Maintain filing before Entry places the route's intake, asserts one intake with two receipts. Its plant
  `two-keys` stages the route's pre-join text and reds on the second ask. Observed by AC3 and AC4.
- **S5** — The inline parity. Two `PARITY_ROWS` rows in `tools/lib/resolve-python.test.sh` (`:351-370`):
  `derive_key_hash|<lib>/key_hash.py|<lib>/key_hash` and `render_breach_text|<drift-audit>/maintain_file.py|<drift-audit>/maintain_file`,
  the drift-audit directory found by the file's inline `resolve_kit_dir`, as `UNATTENDED_DIR` is (`:168`). Each
  row reds a drifted copy and an empty copy population (`:410-413`). Observed by AC5.
- **S6** — The docs. `help/release.md` (DEPL-dShippedRelease-15 S17) says a `release-verify-failed` ask carries
  the marker `maintain key <16 hex>` and that Maintain's later filing for the same SHA and environment adds a
  `seen` row to it; `help/maintain.md` names `release.route` as the reading's second filer. Observed by AC6.

## 3. Non-goals (OUT)

- Registering `release-verify-failed`'s producer in `EVENT_PRODUCERS` and its `[[reading]]` row: no spec carries
  it (scout D disagreement 5); §8 F4 asks it of dShippedRelease.
- Changing either parent's spec. Each change S1 to S3 makes to landed parent code is mirrored by an ask (§8 F4),
  never by an edit of another build's spec.
- The drift history's `key_hash` column (`tools/drift-audit/drift_report.py:3762-3777`). It hashes the sorted,
  LF-joined offender keys of a record with no kind, a different payload, so it is not a copy of
  `derive_key_hash` and keeps its bytes (§4 "Evidence").
- The release ref's hash, `derive_release_ref` in `tools/integrations/release.py`: `env-` and the first
  12 hex of the SHA-256 of an environment name (DEPL-dShippedRelease-15,
  `memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-15.md:250-252`), written by
  `release.py record`. Its payload is an
  environment name, not a `kind`/`key` filing pair, so it keeps its bytes and every committed
  `refs/gov/release/…env-<hex>` ref keeps its name.
- The intake's content key (TOOL-dPlacedRequest-19 S1), Entry's placement (TOOL-dWellOiledMachine-27 S4) and
  the `seen` clause's writer (TOOL-dTendedCadence-15 S2). This unit makes two texts equal and calls them.
- The stand-ins each parent builds against while the other is unlanded: both parents land before this build
  run, so their `[[stand-in]]` rows are the parents' (§8 F3, asks A1 and A3).

### Edges

- **hands-off** `PLAY-dConvergedCharter-14` — `derive_key_hash`, the factory unit 14's declined-part arm keys a part's `keep` record through
- **consumes-from** external — DEPL-dShippedRelease-15 S10 and S17, TOOL-dTendedCadence-15 S2, -8, -2 S3-S4, TOOL-dCalibratedLens-5 S8 and TOOL-dWellOiledMachine-27 S1 and S4, each specced and DEFERRED at base and landed in an ancestor before the build run

## 4. Design

### Evidence

- DEPL-dShippedRelease-15 S10 files `release-verify-failed <sha> <E>` through `intake.py file`
  (`memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-15.md:106-113`).
- TOOL-dTendedCadence-15 S2 files `maintain key <key hash> · <reading> over its pin · <offender key>` plus a
  clause tail, the hash over `<reading>\t<offender key>`, and first looks for an open ask carrying the marker
  (`memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-15.md:56-75`).
- The two texts differ, so `request.py key` (TOOL-dPlacedRequest-19 S1) gives two content keys and the route's
  ask carries no `maintain key` marker: two asks, the review record
  `memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md:75` (M4).
- TOOL-dCalibratedLens-3 S7 keys a loop proposal by the first 16 hex of the SHA-256 of `<ledger kind>\t<id>`,
  and TOOL-dCalibratedLens-5 S8 names it `derive_key_hash(kind, id)`. That is the second specced instance of
  the same function, and this unit's call is the third: the charter's `[reuse]` rule asks one factory.
- At base, `drift_report.py:3777` hashes `"\n".join(sorted(keys))` with no kind: a set hash, not this function.
  TOOL-dTendedCadence-15 S2 cites it only as the precedent of the 16-hex truncation (scout D disagreement 8).
- `tools/lib/` is gov-internal and ships nothing; a copy-installed kit carries a shared function inline, and
  `tools/lib/resolve-python.test.sh` holds every copy to its canonical (`:342-424`).

### Data flow

```
verify red under roll-forward
  release.route ─ render_breach_text("release-verify-failed", "<sha> <E>", "act", None)
                  ─ intake.py file --origin cadence --filer item.release.route ─ Entry ─ ask (marker: maintain key H)
  later, Maintain's release-verify-failed event ─ run_breach_route ─ write_breach_ask
      (1) open ask carrying "maintain key H"? ─ yes ─▶ SCOPE row, seen clause          (seen)
      (2) else intake.py file, render_breach_text(same args) ─ same content key ─▶ receipt (seen)
H = derive_key_hash("release-verify-failed", "<sha> <E>")
```

The marker joins after Entry places the route's intake; the equal text joins before it, since one text is one
content key. Both orders end at one ask.

### Inventory

Minted, each asked of `lexicon.py --suggest <name> --as py.function` at base and answered OK:
`render_breach_text`. `derive_key_hash` is TOOL-dCalibratedLens-5's spelling, also answered OK. The module
`tools/lib/key_hash.py` (the `py.file` cell is undeclared at base), the two `PARITY_ROWS` stems
`derive_key_hash` and `render_breach_text`, and the fixture case `verify-join` with its plant `two-keys`.

### Files touched (estimate)

- `tools/lib/key_hash.py` (new): S1
- `tools/lib/resolve-python.test.sh`: S5
- `tools/drift-audit/maintain_file.py`: S1, S2
- `tools/drift-audit/selftest.py`: the arm of §7 for `render_breach_text`'s callers
- `tools/loop/loop_review.py`: S1
- `tools/integrations/release.py`: S1, S2, S3
- `tools/integrations/release_fixture.py`: S4
- `help/release.md`, `help/maintain.md`: S6

### Alternatives rejected

- **Join by the marker alone.** The route files its own head-only text, and Maintain's step (1) finds the ask by
  `maintain key H`. Rejected by the order test of S4: when Maintain's event fires before Entry places the route's
  intake, step (1) finds nothing and step (2) files a text with a different tail, so two intakes stand.
- **Join by the content key of the bare text `release-verify-failed <sha> <E>`.** Maintain's text carries a
  clause tail its band sets, so the two content keys still differ; and the route's ask still carries no marker,
  so step (1) never finds it.
- **`release.route` calls Maintain's filer as a subprocess.** The integrations kit requires `loop` and `runtime`
  (DEPL-dShippedRelease-15 S1), never drift-audit, so the call adds a kit dependency no clause names.
- **Re-pointing the drift history's `key_hash` column at `derive_key_hash`.** It hashes another payload, and
  moving its bytes reds every committed history row's comparison.

## 5. Production-readiness checklist

- security — no new write surface: both filers keep their existing `intake.py file` call; the text carries a
  SHA and an environment name, both already in the route's record.
- perf / scale — one SHA-256 per filing.
- error / empty / loading states — an empty `kind` or `key` raises `ValueError` in `derive_key_hash`; a filer
  whose intake call fails keeps its parent's handling.
- observability — the ask's marker names the key hash, and `run_breach_route` prints `seen` for the join.
- risks — the text is equal only while the reading's band for a red verify is `act`; §8 F1's ask makes the
  reading's edges say so and S4 re-derives it under both `maintain.tiers` values.
- testing — AC1 to AC5, and the arms of §7.
- migration — none: neither parent ships before this build, so no filed ask carries the pre-join text.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When `python -c` imports `key_hash.py` from `tools/lib/` and calls
  `derive_key_hash("release-verify-failed", "<40-hex> production")`, it prints 16 lowercase hex equal to
  `hashlib.sha256(b"release-verify-failed\t<40-hex> production").hexdigest()[:16]`, and
  `derive_key_hash("", "x")` raises `ValueError`.
  Red when: the payload drops the tab or the kind, or the length is not 16.
- **AC2** — When `python release_fixture.py --case verify-join` runs, the route's filed text and Maintain's
  rendered text for the same breach are byte-equal and both begin `maintain key `.
  Red when: either filer renders its own text.
  fixture: a scratch repository under `%TEMP%/<short>`, both kits copied in, no `core.hooksPath`.
- **AC3** — When the same case runs in the route-first order under `maintain.tiers = "pins"` and again under
  `"bands"`, each planted in `.governance/policy.toml`, the fixture `BACKLOG.md` holds one ask carrying the
  marker and one `SCOPE` row with a `seen` clause, and `run_breach_route` prints `file — release-verify-failed ·
  key <16 hex> · seen`.
  Red when: a second ask is placed, the clause's seen-red case.
- **AC4** — When `python release_fixture.py --case verify-join --plant two-keys` stages the route's pre-join
  text `release-verify-failed <sha> <E>`, the case exits 1 naming two open asks for one (SHA, E); in the
  Maintain-first order without the plant, `intake.py show` lists one intake with two receipts.
  Red when: the plant's two asks pass, or the Maintain-first order files two intakes.
- **AC5** — When the parity table's extractor, the `awk` program of its `blk` function, runs over
  `maintain_file.py`, `loop_review.py` and `release.py` for the `# >>> derive_key_hash` and
  `# >>> render_breach_text` blocks, each block is byte-equal to its canonical with CRs dropped, and
  `git grep -n -E 'sha256' -- tools/drift-audit/maintain_file.py tools/loop/loop_review.py
  tools/integrations/release.py` prints only lines inside a `# >>> derive_key_hash` … `# <<<` span of
  its file or inside a function of the declared allowlist, each hit graded against the span's line
  range, so `hashlib.sha256(`, `from hashlib import sha256` and `hashlib.new("sha256")` are all seen.
  The allowlist is one row, `(tools/integrations/release.py, derive_release_ref, "env- ref of an
  environment name, DEPL-dShippedRelease-15; not a filing key")` (§3), and each hit it admits is
  printed with its reason, never skipped silently. Over a scratch copy with a planted `hashlib.sha256(`
  line outside every block and allowlisted function, the same grep prints that line.
  Red when: a copy is edited by one byte, a consumer computes the filing hash outside the block, an
  allowlisted hit is admitted without its printed reason, or a pathspec matches no tracked file and so
  finds nothing.
- **AC6** — When `grep -n "maintain key" release.md maintain.md` runs under `help/`, each page names the marker,
  and `release.md` says Maintain's later filing adds a `seen` row.
  Red when: either page still describes two asks for one failure.

## 7. Gates

`drift-audit selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The `verify-join` arm's file, `tools/integrations/release_fixture.py`, and `release.py` are run by the
parent legs `integrations release` and `integrations adapters` (DEPL-dShippedRelease-15), and
`loop_review.py` by `loop-review selftest` (TOOL-dCalibratedLens-2 S11); none is in the manifest at base,
and each runs this unit's edits once its parent lands, before this build run.

New arm: tools/lib/resolve-python.test.sh · covers AC5 · two `PARITY_ROWS` rows, `derive_key_hash` and `render_breach_text`, each staged red by a one-byte edit to one inline copy · none

New arm: tools/integrations/release_fixture.py · covers AC2 AC3 AC4 · the case `verify-join` in both orders and both `maintain.tiers` values, its failing case the plant `two-keys` · none

New arm: tools/drift-audit/selftest.py · covers AC2 · `write_breach_ask` rendering through `render_breach_text`, staged red by a tail joined with another separator · none

## 8. Open questions

- **F1 — Which identity joins the two filings?** (a) Equal texts: the route files exactly what
  `write_breach_ask` files for the breach, through one block, so the content key joins before placement and the
  marker after it; (b) the marker alone, each filer rendering its own text; (c) the bare text the route spells
  today. (b) fails the clause's "one open ask" when Maintain files before Entry places the route's intake
  (§4 "Alternatives rejected"); (c) keys the two filings apart outright. (a) meets every criterion, and its one
  condition, the band, is re-derived by AC3 under both `maintain.tiers` values. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F2 — Where does the key hash live?** (a) `tools/lib/key_hash.py` as a canonical block every consumer carries
  inline under `PARITY_ROWS`; (b) each kit keeps its own function; (c) one consumer kit owns it and the others
  import it. (b) is three copies with nothing comparing them, against the charter's `[reuse]` rule; (c) adds a
  cross-kit import that a copy install cannot resolve (TOOL-dGroundRules-1 §4). (a) is the house pattern for a
  shared function (`tools/lib/resolve-python.test.sh:342-370`). Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F3 — Who builds the stand-ins the clause names?** The clause has each parent build its half against a
  stand-in for the other's. Options: (a) each parent, by ask, registers a `[[stand-in]]` row (TOOL-dDeclaredLoop-13
  S8) for the other's item, `item.release.route` owner `dShippedRelease` and `item.maintain.file` owner
  `dTendedCadence`, with a fixture stub filing the S2 text, and deletes it when the other lands; (b) this unit
  registers them. Both parents are ancestors, so both land before this build run and a stand-in this unit wrote
  would be deleted in the same pass. (a) keeps the clause's own assignment. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a), through asks A1 and A3. widens: none · relaxes: none
- **F4 — The asks this unit needs filed.** Each states a change to a parent spec this unit never edits.
  RESOLVED (agent, 2026-11-03, delegated): file A1 to A4. widens: none · relaxes: none
  Ask A1 for dShippedRelease, target build dShippedRelease: "DEPL-dShippedRelease-15 S10 files
  `render_breach_text("release-verify-failed", "<sha> <E>", "act", None)`, carrying `derive_key_hash` and
  `render_breach_text` inline, and its fixture files against a `[[stand-in]]` row for `item.maintain.file` until
  dTendedCadence lands"; accept: AC10's filed text begins `maintain key <16 hex>`, seen on the fixture.
  Ask A2 for dShippedRelease, target build dShippedRelease: "register `release-verify-failed`'s producer in
  `EVENT_PRODUCERS` and its `[[reading]]` row, offender key `<40-hex sha> <E>`, with band edges putting one red
  verify in `act`"; accept: TOOL-dTendedCadence-2 S4's `· no producer registered` line is absent with
  integrations installed, and the reading's band for one red verify reads `act` under both `maintain.tiers`
  values, seen on a fixture.
  Ask A3 for dTendedCadence, target build dTendedCadence: "TOOL-dTendedCadence-15 S2 hashes through the inline
  `derive_key_hash` block of `tools/lib/key_hash.py` and renders its text through the canonical block
  `render_breach_text`, and its join arm files against a `[[stand-in]]` row for `item.release.route` until
  dShippedRelease lands"; accept: the drift-audit selftest's `file-ask` case keeps its bytes, seen with the
  block in place.
  Ask A4 for dCalibratedLens, target build dCalibratedLens: "TOOL-dCalibratedLens-5 S8's `derive_key_hash` is
  the inline block of `tools/lib/key_hash.py`, held by its `PARITY_ROWS` row"; accept: `loop_review.py`'s keep
  file names keep their bytes, seen on its keep fixture.

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the spec brief's unit row, scout D's row and disagreements 5, 6
  and 8, and the parent specs read at base.
- rev-2 · 2026-11-04 · AC5 · folded `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` finding
  50: AC5's grep spells the three full paths and every `sha256` form, grades each hit against its
  file's block span, and stages its red with a planted hash outside a block.
- rev-3 · 2026-11-04 · §3 AC5 §7 · folded `2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1`
  findings 41 (`derive_release_ref`'s SHA-256 of an environment name keeps its bytes, a §3 non-goal, and
  AC5's grep admits it through a declared, printed allowlist row) and 10 (§7 names `memory hygiene` and
  `spec tokens`, and the parent legs `integrations release`, `integrations adapters` and `loop-review
  selftest` that run the `verify-join` arm, `release.py` and `loop_review.py`).

## 10. Reuse audit

The seams extended: `tools/lib/`'s canonical-block pattern and its parity table
(`tools/lib/resolve-python.test.sh:342-424`, the `resolve_kit_dir` row at `:355`), TOOL-dTendedCadence-15 S2's
`write_breach_ask` (the first instance of the text, whose renderer this unit extracts), TOOL-dCalibratedLens-5
S8's `derive_key_hash` (the name kept), and DEPL-dShippedRelease-15's fixture, which gains a case.
`python tools/codebase-map/reuse_lookup.py "hash a filing key so two filers of one finding join one ask"`
ranked name stems only (`key`, `ask`, `derive_clause_hash` in `tools/memory-tree/design_lib.py`); the last
hashes a clause's text for a pin and is not a filing key, so no existing callable fits beyond the specced
instances. Where a record and source disagreed: scout D's row names `drift_report.py:3777` as a copy of the
hash, and source shows a set hash over another payload (§4 "Evidence"); scout D proposed `tools/lib/filing_key.py`,
and the brief's I9 spelling `tools/lib/key_hash.py` is the one used.

Recall terms used: `python tools/memory-recall/query.py "how do two filers of the same release verify failure land on one ask instead of two" --terms "release-verify-failed release.route maintain.file filing key content key seen clause intake ask join"`
— its top hits were the scout row, the round-3 fold review's M4 and the skeptic brief's B5-F14, which agree
with §4.

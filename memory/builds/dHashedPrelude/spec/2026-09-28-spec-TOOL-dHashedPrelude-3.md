# TOOL-dHashedPrelude-3 — the kit's published facts stop being a typed count, and its version moves

**Status:** CLOSED · rev-3 · 2026-09-28 · node d · Tier-1 · base 3cf05f29 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-28-build-TOOL-dHashedPrelude-1-1-acceptance-ledger.md](../build/2026-09-28-build-TOOL-dHashedPrelude-1-1-acceptance-ledger.md) | journal | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-closing-diff-round2.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-closing-diff-round2.md) | diff-review | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-closing-diff.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-closing-diff.md) | diff-review | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round1.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 |
| [2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round2.md](../reviews/2026-09-28-review-TOOL-dHashedPrelude-1-2-3-spec-audit-round2.md) | spec-audit | TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-recall/README.md` line 26 tells a reader the selftest is "18 checks". It has not been
18 since 2026-08-03, and unit 2 moves the number again. Replace the typed figure with a pointer to
the run's own summary line, and move the kit version markers, which must not land in an earlier
commit than the last change to the kit's shipped bytes.

## 2. Scope (IN)

- **S1** — `tools/memory-recall/README.md` line 26 describes `selftest.py` by its role and by where
  a reader finds the number of checks, which is the summary line the run itself prints. No figure is
  typed into that table. Observed by AC1.
- **S2** — `KIT_MEMORY_RECALL_VERSION` in `tools/memory-recall/recall_conf.py` moves from 1.12 to
  1.13, and so do the two `gov:kit memory-recall@` markers, one in that file's docstring at line 4
  and one in the README's HTML comment at line 3. Those three lines are the whole population that
  carries a version literal. Observed by AC2.
- **S3** — The backlog row `TOOL-aProbedToolkit-14` records that its memory-recall half is answered
  here and that its `tools/lexicon/README.md` half is still open. Observed by AC3.
- **S4** — The two deferrals units 2 and 3 name are PARKED in the build README, because a non-goal
  pointing at a record nobody writes defers the work to nobody. They are the selftest summary line
  carrying both figures, and an `eol=lf` pin over `tools/**/*.py`, whose absence let a CRLF working
  copy put wrong byte offsets into a spec at rev-2. Each entry carries its question, the option
  seen and the reason it was refused, which is where the owner gets the turn this build did not
  take. Observed by AC4.

## 3. Non-goals (OUT)

The lexicon half of `TOOL-aProbedToolkit-14` is not touched: it is a different kit, a different
sample paste, and this build edits neither. No other figure in this README is audited — the row is
specific about which claims it measured, and the ones it checked and found correct stay as they are.
No change to how the version enters `Conf.digest()`, and no change to the selftest's summary line
or to any `eol` pin: S4 parks both, and neither is built in this build.

## 4. Design

Three lines carry the version literal. `tools/check-kit-versions.sh` compares the constant against
the README marker only, but `test_version_marker` in the selftest scans every `gov:kit
memory-recall@` in both `README.md` and `recall_conf.py` against the constant, and §7 lists
`memory-recall kit selftest` as a gate — so all three are bound by something this unit runs.

The bump lands in this unit's commit and not in unit 1's or unit 2's, because `govkit epoch` reds
when a kit's last bump precedes the last commit that moved its shipped bytes: this unit is the one
that edits `README.md`, whose role in `kit.toml` is `engine` and which is therefore inside the
measured set. `selftest.py` is `project-owned` and is not, so units 1 and 2 move no bytes that
`epoch` grades.

That is also why the bump is recorded as contested rather than routine. The kit's own rule asks for
no bump on account of units 1 and 2, and the value enters the conf digest, so every node rebuilds a
warm cache for a file no adopter holds. The owner ruled on 2026-09-28 that an edit inside the kit
directory is a kit edit. The ruling stands and this unit implements it; the build README's parked
section carries the reasoning so the next reader does not re-derive it.

### Files touched (estimate)

`tools/memory-recall/README.md` · `tools/memory-recall/recall_conf.py` · `memory/backlog/TOOL.md`

## 6. Acceptance criteria

- **AC1** — When line 26 of `tools/memory-recall/README.md` is read, it names no check count, and
  `grep -c "18 checks" tools/memory-recall/README.md` prints 0.
  Red when: a fresh figure is typed in place of the stale one, which restores the class rather than
  answering it.
- **AC2** — When `grep -rn 'gov:kit memory-recall@[0-9]\|^KIT_MEMORY_RECALL_VERSION = '
  tools/memory-recall/README.md tools/memory-recall/recall_conf.py` runs, it prints exactly three
  lines and every one carries 1.13. `bash tools/check-kit-versions.sh` exits 0, and
  `python tools/govkit/govkit.py epoch --base 3cf05f29` prints a `clean` row for `memory-recall`
  with no `FAILED` line for it.
  figure: the three lines are DERIVED by that command, which was run as written at BASE and printed
  exactly those three, all carrying 1.12; 1.13 is PINNED. The count is the carrier list of S2, not a
  count over an unanchored pattern — the rev-1 form of this criterion asserted three lines from a
  pattern that prints twelve.
  Red when: one of the three is left at 1.12, or the bump rides unit 1's or unit 2's commit and so
  precedes the README edit that moves engine bytes.
- **AC3** — When `TOOL-aProbedToolkit-14` is read in `memory/backlog/TOOL.md`, it names which half
  this build answered and which half is still open, and its status token still reflects that one
  half remains.
  Red when: the row is closed outright, which would claim the lexicon README was fixed here.
- **AC4** — When the `## Parked decisions` section of `memory/builds/dHashedPrelude/README.md` is
  read, it carries an entry for each of the two deferrals, and each names the spec section that
  deferred it, the option seen and the reason it was refused.
  Red when: a spec's non-goal defers to a record nobody writes, which is a deferral to nobody
  wearing the shape of a tracked one. Also red when an entry names only the deferral: a parked
  item without its reason is indistinguishable from a forgotten one.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `row-keyed merge driver replay` · `hook destinations self-test` · `memory-recall skill wiring`

New arm: none. This unit adds no arm; AC1 and AC2 are direct greps and two checker runs.

## 8. Open questions

none — the one fork this unit carried was the version bump, resolved before the spec was written.
RESOLVED (owner, 2026-09-28): bump 1.12 to 1.13, against the recommendation recorded in §4 and in
the build README's parked section.

## 9. Revision log

- rev-1 · 2026-09-28 · initial draft.
- rev-2 · 2026-09-28 · §1 · §2 S2 · §3 · §4 · AC1 · AC2 · folded the round-1 spec audit. AC2's
  pattern printed twelve lines rather than the three it asserted, nine of them carrying no version
  literal, so the criterion could not go green on a correct build; it is now anchored on the value
  forms and was run as written before being written down (D-3). The Goal said units 1 and 2 move the
  check count while unit 1's own edges and AC4 say unit 1 changes nothing — unit 2 alone moves it
  (D-6). §4 records that `test_version_marker` binds all three markers, which `check-kit-versions.sh`
  alone does not. Sections 5 and 10 are absent by the Tier-1 light profile, not by omission.
- rev-3 · 2026-09-28 · §2 S4 · §3 · AC4 · folded the round-2 spec audit. Two specs deferred work
  to "a backlog row" that no unit wrote and no id named; S4 and AC4 give both deferrals a home in
  the build README's parked section. A backlog row was written first and reverted: hygiene check
  20 holds `memory/backlog/TOOL.md` at a shrink-only pin of 417 live rows and the shard is AT it,
  so a row cannot be added without draining two, which is not this build's to do.

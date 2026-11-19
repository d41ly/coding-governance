# TOOL-dTrackedAtlas-10 — the page's staleness digest covers the merge history the landed predicate reads

**Status:** CLOSED · rev-1 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · ratified 2026-11-19 · records-only · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-10-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-10-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-10-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-10-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md) | research | TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-11 |
| [2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-11 |

<!-- /gen:spec-records -->

## 1. Goal

`--check --page` certifies a page current at a landing merge while the page shows the wrong landed
state, because the stamp's digest hashes tree content and the landed predicate reads merge history
(closing review H3). This unit folds that history, read by the derivation's own landing reader, and
the default-branch ref it is measured against into the stamp's digest, so the merge-only case the
review plants reads stale.

## 2. Scope (IN)

- **S1** — The stamp's `digest` covers, beside the tree listing of `TOOL-dTrackedAtlas-3`, each chain
  build's landing candidates and the default-branch ref name, by §4 "The digest". Observed by AC1,
  AC2 and AC3.
- **S2** — The landing candidates are read by `read_landings`, which calls
  `TOOL-dTrackedAtlas-1`'s `derive_landings` as `TOOL-dTrackedAtlas-9` leaves it, never a second
  copy of its git reads. Observed by AC2.
- **S3** — `check_page` re-resolves the stamp's `default_ref` name at check time and re-reads the
  candidates at `--ref` against it, so a page reads stale when the default branch takes the commit it
  was stamped at, and stays current when the default branch moves past without taking a landing the
  page shows. Observed by AC3 and AC4.
- **S4** — The stamp gains the fields `default_ref` and `landings`, `STAMP_SCHEMA` becomes `2`, and
  `read_stamp` validates both, so a page of schema `1` reads unstamped. Observed by AC5.
- **S5** — A stale answer names each build whose landing candidates moved, before its commit lines.
  Observed by AC1 and AC3.
- **S6** — A default-branch ref that no longer resolves, or any failure of the derivation's module,
  is the exit-2 answer `atlas: cannot check:`, never a traceback and never stale. Observed by AC6.
- **S7** — The generator loads `TOOL-dTrackedAtlas-1`'s module through one loader,
  `load_build_state`, in place of the two inline copies in `read_git` and `derive_actual`, and its
  module docstring states the new digest. Observed by AC7.

## 3. Non-goals (OUT)

- The functions this unit touches are `read_git`, `derive_actual`, `derive_input_digest`,
  `build_stamp`, `read_stamp` and `check_page`, the constant `STAMP_SCHEMA`, and the module
  docstring, and it adds `load_build_state` and `read_landings` (§4 "Inventory"). In `derive_actual`
  it replaces only the three lines that load the module. `main`, `derive`, the template and the
  `--check` that derives stay as they are; `main`'s option reading is `TOOL-dTrackedAtlas-11`'s.
- A new option. `check_page` keeps its signature `(page, ref)`, and the default-branch ref comes
  from the stamp, so `--page` mode admits exactly what it admits today.
- The landed predicate itself and the state document's `default_ref` and `default_commit`: those are
  `TOOL-dTrackedAtlas-9`'s. This unit reads them and changes neither.
- The template's header line. It keeps showing the stamp's commit and digest, both of which keep
  their shape.
- Run claims, the code under `tools/` the derivation reuses, and a hand edit to the page: they stay
  outside the digest, as `TOOL-dTrackedAtlas-3`'s "What it does not check" states.
- `TOOL-dTrackedAtlas-3`'s spec, which is CLOSED and stays frozen. Its AC2, which recomputes the
  digest as the SHA-256 of the tree listing alone, no longer reproduces the stamp's digest after this
  unit; this spec's AC2 states the digest that replaces it.
- A gotcha file or a suite arm. This repository's `review.left-shift` is `second-occurrence`, so a
  first occurrence of `freshness-digest-omits-what-the-derivation-reads` owes no gotcha file, and the
  regression is observed by AC1 and AC3, red before the change and green after.
- Any file under `tools/`, any new file under `memory/builds/dClosedLoop/build/`, and the page,
  which is never committed.

### Edges

- **consumes-from** `TOOL-dTrackedAtlas-9` — `derive_landings(root, commit, default_commit, m, names)`,
  `resolve_default_ref(root, default_ref)`, and the state document's `default_ref` and
  `default_commit`; without them there is no default-branch line to measure and no name to re-resolve.
- **consumes-from** `TOOL-dTrackedAtlas-3` — the stamp, `derive_input_digest`, `read_stamp`,
  `check_page` and its exit table, which this unit extends and whose exit codes it keeps.
- **consumes-from** `TOOL-dTrackedAtlas-1` — the module at `STATE_PATH`, its `StateError`, and
  `GIT_TIMEOUT`.
- **hands-off** `TOOL-dTrackedAtlas-11` — `main`'s one reader for valued options; this unit adds no
  option for it to read.

## 4. Design

### Where it lands

The generator is `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`.
`derive_input_digest` hashes `git ls-tree -r -z <commit> -- <inputs>` alone
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#derive_input_digest`),
and `build_stamp` and `check_page` both call it
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#build_stamp`,
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#check_page`). The
landed state the page shows comes from
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive_landings`,
which reads `git log --first-parent --merges` per build: commit-graph history no tree listing covers.
The module docstring says a page reads stale "only when an input moved, never because the commit
did"
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@2b57a776e68945c686ea9538150f6eaa198b8649:23`),
which is the sentence the review names as hiding the case.

Measured on 2026-11-19 (PINNED) with a scratch probe calling unit 1's `derive_landings` as built:
the tree digest is equal at `c1f80c002` and its run-branch parent `5125f93ea`, as the review found,
while dDeclaredLoop's candidates are `3fdeb642d`, `67f1ffb18` at `5125f93ea` and `3fdeb642d`,
`c1f80c002` at `c1f80c002`. The probe read all `22` builds in `0.8` to `1.0` s per commit (PINNED,
2026-11-19).

The generator loads the module at `STATE_PATH` twice today, inline in `derive_actual`
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@2b57a776e68945c686ea9538150f6eaa198b8649:735`)
and inline in `read_git` for `GIT_TIMEOUT`
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@2b57a776e68945c686ea9538150f6eaa198b8649:804`).
`read_landings` is a third use, so this unit extracts `load_build_state` and all three call it.

### What `TOOL-dTrackedAtlas-9` gives this unit

Read from that unit's spec, rev-1. `derive_landings(root, commit, default_commit, m, names)` lists
each build's merges on `default_commit`'s first-parent line touching its `RUN.md` and drops those
`commit` does not contain. `resolve_default_ref(root, default_ref)` returns `(name, commit)` and raises
`StateError` for a name that resolves to no commit. The state document carries `default_ref`, the ref
as passed or the remote ladder's `refs/remotes/<remote>/<branch>`, and `default_commit`. The Atlas
passes no default ref, so its pages carry the ladder's name.

### The digest

```python
landings = {slug: [merge sha, ...]}   # oldest first, every chain build, from read_landings
history = json.dumps({"default_ref": default_ref, "landings": landings},
                     sort_keys=True, separators=(",", ":")).encode("utf-8")
digest = sha256(<raw stdout of git ls-tree -r -z <commit> -- <inputs>> + b"\0" + history).hexdigest()
```

`derive_input_digest(commit, inputs, default_ref, landings)` computes it, for `build_stamp` at the
stamp's commit and for `check_page` at the ref. The candidates are every merge `derive_landings`
returns, not only those whose `RUN.md` carries a run's base: each one's base and subject are fixed by
its sha, and the run records' bases are tree content the listing already covers. The default
branch's commit is not folded, only its name, by §7 F3.

### The landing reader

`read_landings(commit, builds, default_ref, default_commit=None)` returns `{slug: [sha, ...]}` for each
slug of `builds`. It loads the module through `load_build_state`; when `default_commit` is `None` it
resolves it with the module's `resolve_default_ref(str(REPO), default_ref)`; it then calls the
module's `derive_landings(str(REPO), commit, default_commit, m, tuple(builds))` and keeps each
candidate's sha. `m` is the memory root as the generator's own layout gives it,
`BUILD.parent.parent` relative to `REPO`, the root `build_stamp` already forms each build's input
folder under. A `StateError` the module raises becomes a `StampError` carrying its text, so every
caller keeps its one refusal path.

### The stamp

`build_stamp(data)` keeps every field of `TOOL-dTrackedAtlas-3`'s stamp table and changes these:

| Field | Value |
|---|---|
| `schema` | `2` |
| `default_ref` | `data["state"]["default_ref"]` |
| `landings` | `read_landings(commit, <the state's build slugs>, default_ref, data["state"]["default_commit"])` |
| `digest` | `derive_input_digest(commit, inputs, default_ref, landings)` |

It passes the state's `default_commit` rather than resolving the name again, so the stamp answers for
the default commit the page was derived against even if the default branch moved during the
derivation. A state without a string `default_ref` or a 40-hex `default_commit` is a `StampError`,
which `main` already turns into `atlas: cannot stamp the page: <reason>` and exit 1.

`read_stamp` adds two rules and changes one:

| Field | Rule |
|---|---|
| `schema` | the integer `2` |
| `default_ref` | a string matching `^[A-Za-z0-9._][A-Za-z0-9._/-]*$` |
| `landings` | a non-empty object, each key matching `^[A-Za-z0-9._-]+$`, each value a list of `40`-hex lowercase strings |

A page stamped by `TOOL-dTrackedAtlas-3`'s generator reads `atlas: unstamped` on its `schema`. That
is the right answer: its digest does not cover the history, so it cannot be certified current, and a
caller that regenerates on exit 1 regenerates it.

### The page check

`check_page` keeps the exit table and the order of `TOOL-dTrackedAtlas-3` §4 "The page check":
absent, unstamped, the ref and the digest at it, dirty, stale, current. The digest at the ref is now
`derive_input_digest(at, stamp["inputs"], stamp["default_ref"], read_landings(at, sorted(stamp["landings"]), stamp["default_ref"]))`,
so the default-branch name is resolved at check time. A `StampError` from either read is exit 2 with
one `atlas: cannot check: <reason>` line on stderr.

A stale answer prints, directly under its first line and before the existing commit lines, one line
per build whose re-read candidates differ from `stamp["landings"]`, in key order:

```
  landings of <slug> moved: <h12 of its newest candidate at the ref, or none>
```

When the default branch has taken the stamp's own commit, the commit range is empty and these lines
are the whole report.

### The module docstring

The paragraph opening `--out stamps the page (TOOL-dTrackedAtlas-3)` keeps its first sentence. Its
second becomes: `--check --page derives nothing: it hashes the stamped inputs at --ref, with each
chain build's landing merges read against the stamp's default_ref (TOOL-dTrackedAtlas-10), and
compares, so a page reads stale when an input or a landing it shows moved, never because the commit
alone did.` Its does-not-see sentence keeps its three items and adds: whether the default-branch ref
is current with its remote, since nothing is fetched.

### Inventory

| Name | Kind | Value or signature |
|---|---|---|
| `STAMP_SCHEMA` | constant, changed | `2` |
| `load_build_state()` | function, new | the module at `STATE_PATH`, loaded once and cached |
| `read_landings(commit, builds, default_ref, default_commit=None)` | function, new | `{slug: [sha, ...]}`; `StampError` on the module's `StateError` |
| `derive_input_digest(commit, inputs, default_ref, landings)` | function, changed | the digest of §4 "The digest" |
| `build_stamp(data)` | function, changed | the stamp with `default_ref` and `landings` |
| `read_stamp(page)` | function, changed | the rules above |
| `check_page(page, ref)` | function, changed | the digest with the history, and the landing lines of a stale answer |

Both new names lead with a verb `.lexicon.conf` declares, checked with
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` on 2026-11-19.

### What it does not check

- Whether the default-branch ref is current with its remote: a landing the remote took and this
  repository has not fetched reads as not taken, as `TOOL-dTrackedAtlas-9` states for the
  derivation.
- It over-reports: a merge touching a build's `RUN.md` whose `RUN.md` carries no run's base moves
  the digest though the landed state the page shows does not.
- Whether a run's base commit is present in the checking repository, which decides a run's kind.
- Run claims, the code under `tools/`, and a hand edit to the page, as before.

### Files touched (estimate)

`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-10-ledger.md`

### Alternatives rejected

- Hashing a `git log --first-parent --merges` the generator runs itself: §7 F1 (a).
- Comparing the landings beside the digest instead of folding them in: §7 F1 (c).
- Folding the default branch's commit: §7 F3 (a).
- A `--default-ref` option on `--check --page`: §7 F3 (c).

## 5. Acceptance criteria

The commands run in a clone of the worktree at the run branch's tip carrying this unit, at
`%TEMP%/ta10fx`, from the clone's root, with these names set and the remote ladder's two environment
overrides unset. Pages are written to the run's scratch directory, never into the clone or the
worktree, and every generation passes `--claims none`. The clone's default branch is its own
`refs/remotes/origin/main`, which each criterion sets; the real repository's refs are never written.

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
WT=<the worktree root>
ATLAS=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py
S=<the run's scratch directory>
unset GOV_REMOTE GOV_DEFAULT_BRANCH
git clone -q --shared "$WT" "$TEMP/ta10fx" && cd "$TEMP/ta10fx"
T0=$(git rev-parse HEAD)
git update-ref refs/remotes/origin/main "$T0"
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
git checkout -q -B fx-run "$T0"
git mv memory/builds/dWitnessedBar/RUN.md memory/builds/dWitnessedBar/RUN.LANDED.00000001.md
printf '# dWitnessedBar run\n\n## Run facts\n\nphase: LANDING\nbase: %s\n' "$(git rev-parse 9e21ac760)" \
  > memory/builds/dWitnessedBar/RUN.md
git add memory/builds/dWitnessedBar && git commit -q -m "fixture: dWitnessedBar's build run"
B=$(git rev-parse HEAD)
```

- **AC1** — When `"$PY" "$ATLAS" --claims none --out "$S/p0.html"` runs at `$B`, its
  `--check --page "$S/p0.html"` exits 0; and when the default branch then takes `$B` through a merge
  of its own (`git checkout -q -B fx-main "$T0"`, a commit appending a line to
  `memory/builds/dTrackedAtlas/README.md`, `git merge -q --no-ff fx-run -m "fixture: land"`,
  `M=$(git rev-parse HEAD)`, `git update-ref refs/remotes/origin/main "$M"`), then
  `git diff --name-only "$B" "$M"` prints only `memory/builds/dTrackedAtlas/README.md`, and
  `"$PY" "$ATLAS" --check --page "$S/p0.html" --ref "$M"` exits 1 with `atlas: stale`, a line
  `  landings of dWitnessedBar moved:` ending in `$M`'s first `12` hex, and a commit line beginning
  with them. `--ref "$B"` still exits 0. `--claims none --out "$S/p1.html"` at `$M` then checks with
  exit 0, and `p1.html`'s `state.landed` names dWitnessedBar where `p0.html`'s does not.
  Red when: the digest covers the tree listing alone, `TOOL-dTrackedAtlas-3`'s, which answers
  `atlas: current` with exit 0 at `$M`: the review's merge-only case, observed red on a staged digest
  of that shape before green.
  cost: two generations of the page, minutes each.
- **AC2** — When the stamp of `$S/p1.html` is read by a `"$PY"` one-liner, its `schema` is `2`, its
  `default_ref` is `refs/remotes/origin/main`, its `landings` holds one key per build of the page's
  `state.builds`, and `landings.dWitnessedBar` equals the reversed output of
  `git log --first-parent --merges --format=%H "$M" -- memory/builds/dWitnessedBar/RUN.md`; and the
  same one-liner, hashing `git ls-tree -r -z "$M" -- <the stamp's inputs>`, a NUL byte and the
  compact sorted JSON of `default_ref` and `landings` by §4 "The digest", prints the stamp's `digest`.
  Red when: the digest omits the history, which the plain `git ls-tree -r -z ... | sha256sum` of
  `TOOL-dTrackedAtlas-3`'s AC2 then matches.
  figure: DERIVED, the build count from the page's `state` at observation time.
- **AC3** — When a prepared merge the default branch has not taken is stamped
  (`git checkout -q -B fx-prep "$T0"`, `git merge -q --no-ff fx-run -m "fixture: prepare"`,
  `P=$(git rev-parse HEAD)`, `git update-ref refs/remotes/origin/main "$T0"`,
  `--claims none --out "$S/p2.html"` at `$P`), its check at `--ref "$P"` exits 0; and after
  `git update-ref refs/remotes/origin/main "$P"`, the same check at the same `--ref "$P"` exits 1
  with `atlas: stale` and the line `  landings of dWitnessedBar moved:` ending in `$P`'s first `12`
  hex, and no commit line.
  Red when: the check measures the landings against the stamp's resolved default commit rather than
  re-resolving `default_ref`, which reads `atlas: current` with exit 0 after the default branch took
  `$P`.
  cost: one generation of the page.
- **AC4** — When the default branch moves past `$M` without a landing (`git checkout -q fx-main`, a
  second commit appending to `memory/builds/dTrackedAtlas/README.md`,
  `git update-ref refs/remotes/origin/main "$(git rev-parse HEAD)"`), then
  `"$PY" "$ATLAS" --check --page "$S/p1.html" --ref "$M"` still exits 0 with `atlas: current`.
  Red when: the digest folds the default branch's commit, §7 F3 (a), which reads this move as stale.
- **AC5** — When `$S/p1.html` is copied by a `"$PY"` one-liner with `stamp.schema` set to `1` into
  `$S/p1-old.html`, with `stamp.landings.dWitnessedBar` set to `["abc"]` into `$S/p1-bad.html`, and
  with `stamp.default_ref` set to `-x` into `$S/p1-dash.html`, each `--check --page` exits 1 with
  `atlas: unstamped` and a reason naming `schema`, `landings` and `default_ref` respectively.
  Red when: any of the three exits 0, or the dash value reaches git.
- **AC6** — When `git update-ref -d refs/remotes/origin/main` runs and
  `"$PY" "$ATLAS" --check --page "$S/p1.html" --ref "$M"` follows, it exits 2 with nothing on stdout
  and one stderr line beginning `atlas: cannot check:` and naming `refs/remotes/origin/main`; the ref
  is then restored to `$M`.
  Red when: the module's `StateError` escapes as a traceback, or the check reads the missing ref as
  stale with exit 1.
- **AC7** — When `grep -c "spec_from_file_location" "$ATLAS"` runs, it prints `1`, and
  `grep -c "TOOL-dTrackedAtlas-10" "$ATLAS"` prints at least `1`, from the docstring sentence of §4
  "The module docstring".
  Red when: `read_landings` carries a third inline loader, where the first `grep` prints `3`.

## 6. Gates

The close runs the plain bar once. The legs below are those the files touched keep green, the last
two owed because `tools/gate-legs.json` guards `memory/builds/dClosedLoop/build/` with them. No suite
arm is added or moved, so no arm line is declared.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `chain-packet self-test` · `policy fixtures`

## 7. Open questions

- **F1 — How does the digest cover the merge history the landed predicate reads?**
  (a) The generator runs `git log --first-parent --merges --format=%H <commit> -- <build>/RUN.md`
  per build itself and hashes it, the review's first option. Rejected: it is a second copy of the
  predicate's read, and `TOOL-dTrackedAtlas-9` already moves that read to the default branch's line,
  so the copy would drift on the first change, the class this unit closes.
  (b) Fold the candidates that unit 1's `derive_landings`, as `TOOL-dTrackedAtlas-9` leaves it,
  returns at the commit into the one digest. One reader, and the digest answers as the derivation
  reads.
  (c) Store the landings in the stamp and compare them beside an unchanged digest, the review's second
  option. Rejected: the brief asks that the digest cover the history, and two deciders make the
  check's answer depend on which runs first.
  (d) Re-run the whole derivation at the check. Rejected: minutes per check, where (b) costs about a
  second, and `TOOL-dTrackedAtlas-3` keeps the check deriving nothing else.
  (b) satisfies every criterion and trips none of M3's vetoes: it adds no write path and changes no
  governance carrier.
  RESOLVED (agent, 2026-11-19, delegated): (b), the most feature-rich option by M3's rule.
- **F2 — Does a stale answer name the builds whose landings moved?**
  (a) Yes: the stamp keeps `landings`, and the check prints one line per build that differs.
  (b) No: the commit lines suffice. Rejected: when the default branch takes the stamped commit itself
  the commit range is empty, so the answer would read stale with nothing under it.
  RESOLVED (agent, 2026-11-19, delegated): (a), the most feature-rich option by M3's rule.
- **F3 — What of the default branch does the digest fold, and which default does the check use?**
  (a) The name and the resolved commit, as `TOOL-dTrackedAtlas-9`'s hands-off line words it.
  Rejected: every move of the default branch would stale every page, even one checked at its own
  commit, the false-red class `TOOL-dTrackedAtlas-3`'s F1 rejected the commit rule for, and
  `TOOL-dTrackedAtlas-4`'s hook would regenerate on each; AC4 is its red.
  (b) The name, with the candidates re-read at check time against that name resolved then. The
  commit's effect reaches the digest only through the landings it selects, so a page reads stale
  exactly when a landing it shows moved.
  (c) As (b), with a `--default-ref` option on `--check --page` overriding the stamp's name.
  Rejected: no caller needs it, `TOOL-dTrackedAtlas-9` gives the Atlas no such option, and it would be
  one more value for `TOOL-dTrackedAtlas-11`'s reader.
  (b) satisfies every criterion here and trips none of M3's vetoes. The difference from
  `TOOL-dTrackedAtlas-9`'s hands-off wording is a choice this unit owns, since that unit only records
  the two fields; that spec's line is left as written for its own writer to align.
  RESOLVED (agent, 2026-11-19, delegated): (b), the most feature-rich option by M3's rule.

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft, from the closing review's H3
  (2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1) and the brief
  2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.

## 9. Reuse audit

The seam extended is the generator's own stamp, `derive_input_digest`, `build_stamp`, `read_stamp`
and `check_page`, with `TOOL-dTrackedAtlas-1`'s
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive_landings`
as the one landing reader. `python tools/codebase-map/reuse_lookup.py "fold the merge history a derivation reads into a freshness digest of a generated page"`
ranked name-stem helpers only, none a digest over history: `tools/run-gates/gate-fingerprint.sh`
hashes the whole tree, which `TOOL-dTrackedAtlas-3`'s F1 rejected, and the `read_git` helpers it
listed under `tools/` each read a ref, not a landing line. The recall probe returned the review's H3
finding, `TOOL-dTrackedAtlas-3`'s spec and ledger, and `TOOL-dTrackedAtlas-4`'s regeneration, which
reads the check's exit code; nothing else digests merge history.

Recall terms used: `python tools/memory-recall/query.py "how does the atlas page know a landing merge moved the landed state when no input file changed" --terms "atlas stamp digest landing merge first-parent history derive_landings stale check_page default-branch dTrackedAtlas"`

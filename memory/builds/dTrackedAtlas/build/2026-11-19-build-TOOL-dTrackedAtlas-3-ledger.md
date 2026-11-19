# TOOL-dTrackedAtlas-3 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-3

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command in a scratch clone of the worktree at `%TEMP%/ta3fx`, from the clone's root, with the unit's
generator and template carried in as one fixture commit, `e0bcd2298e37`, on top of the pass's base
`d0743a938`; every page went to the run's scratch directory, written `$S` below, and every generation
passed `--claims none`. The clone was removed after. Each red was observed on the shape the criterion
names: the page of the generator as it stood at `d0743a938`, written `p-red.html`, or a staged break
run by a scratch probe that compiles the clone's generator with one substitution under the generator's
own path and runs it in memory, so no tracked file was edited to stage a red.

**Evidences:** TOOL-dTrackedAtlas-3
- AC1 — `--out "$S/p0.html"` exited `0`; its stamp read schema `1`, `commit`
  `e0bcd2298e377015a9570882d2a015631a8c3ddf`, which `git rev-parse HEAD` printed, and `dirty` `[]`.
  `--check --page "$S/p0.html"` exited `0` with the one line
  `atlas: current — $S/p0.html: inputs 7afb66d0f673 at HEAD (e0bcd2298e37) match the stamp of e0bcd2298e37`.
  Red: the same check over `p-red.html` exited `1` with `atlas: unstamped — $S/p-red.html: its data carries no stamp`.
- AC2 — the stamp's `inputs` are `.memory-tree.conf`, `memory/builds/dClosedLoop/README.md`,
  `memory/builds/dClosedLoop/build/`, `memory/builds/dClosedLoop/reviews/`, the module of
  TOOL-dTrackedAtlas-1 and one `memory/builds/<slug>/` per chain build, `27` in all (DERIVED, `5` plus
  the `22` builds of the page's `state`). `git ls-tree -r -z HEAD -- <inputs> | sha256sum` printed
  `7afb66d0f673ade0945e5de33eed2867119477272756021c47e2ba02618ceb4b`, the stamp's `digest`, over `7460`
  entries (PINNED at `e0bcd2298e37`). Red: the same listing without `-z` hashed to
  `4b3023af4af2f69c88c1e159ddd5be4d2cd7eca1c589d7e8710c7826683fa6db`, which the stamp does not carry.
- AC3 — with a line appended to `memory/builds/dClosedLoop/README.md`, `--out "$S/p2.html"` stamped
  `dirty` `['memory/builds/dClosedLoop/README.md']` and the `digest` `7afb66d0f673`, AC2's at `HEAD`; the
  check exited `1` with `atlas: dirty — $S/p2.html: generated with 1 uncommitted input(s), first memory/builds/dClosedLoop/README.md`;
  `git checkout --` restored the file and `git status --short` printed nothing. With `R` resolving to
  `d0743a938cb6a822dd5b91d93d1799d2f416825d`, `--ref "$R" --out "$S/p3.html"` stamped that `commit` and
  `dirty` listing the template and the generator, and its check exited `1` with `atlas: dirty`. Red: a
  staged stamp whose `dirty` is always `[]` gave both pages an empty `dirty`; the README page's check
  exited `0` reading `atlas: current`, and the page at `R` read `atlas: current` under `--ref "$R"`.
- AC4 — each check exited `1`: the template with `atlas: unstamped — <template>: its data carries no stamp`;
  `p0-bare.html` with `atlas: unstamped — $S/p0-bare.html: its data carries no stamp`; `p0-bad.html`
  with `atlas: unstamped — $S/p0-bad.html: the stamp's inputs field fails its rule: ["../x"]`; and
  `none.html` with `atlas: absent — no page at $S/none.html`. Red: no staged break made one exit `0`.
  With the field rules staged away `p0-bad.html` exited `2`, git refusing `../x` as outside the
  repository; with the stamp-absent refusal staged away `p0-bare.html` exited `1` on a traceback.
- AC5 — after a fixture commit appending to `memory/builds/dTrackedAtlas/README.md`, `3358d5013029`,
  the check of `p0.html` exited `0` with
  `atlas: current — $S/p0.html: inputs 7afb66d0f673 at HEAD (3358d5013029) match the stamp of e0bcd2298e37`.
  Red: a staged check comparing the commit rather than the digest read the same commit, as `HEAD^1`
  after AC6's merge, as `atlas: stale` with exit `1` and no commit listed under it.
- AC6 — a branch appending to `memory/builds/dWitnessedBar/RUN.md`, merged with `git merge --no-ff` as
  `e48d674a37b4`: the check of `p0.html` exited `1` with
  `atlas: stale — $S/p0.html: the inputs stamped at e0bcd2298e37 moved by HEAD (e48d674a37b4)` and the
  line `  e48d674a37b4 fixture: AC6 merge`; with `--ref HEAD^1` it exited `0` reading `atlas: current`;
  `--out "$S/p1.html"` at the merge then checked `0`, its inputs hashing to `eacaf307f4b9`. Red: a staged
  check hashing the inputs at the stamp's commit instead of the ref passed the old page after the merge,
  exit `0` with `atlas: current`.
- AC7 — `--ref no-such-ref` exited `2`, stdout empty, stderr the one line
  `atlas: cannot check: no-such-ref resolves to no commit: git rev-parse --verify -q no-such-ref^{commit} failed: exit 1, nothing on stderr`;
  with `--plant view-unread` it exited `2`, stdout empty, stderr
  `atlas: cannot check: --page takes a page path and runs with --check and an optional --ref alone, not --plant`;
  `--check --claims none` printed `atlas: derived — 264 records, 4594 sections, 220 decision sections, 16 comparison areas, 42 principles`
  with exit `0`; with `--plant view-unread` added it exited `1` with
  `atlas: v2's sections ['planned'] map to a view that reads none of them; map them to records or render them`.
  Red: a staged answer helper returning `1` exited `1` on the unresolvable ref.
- AC8 — `grep -n "D.stamp.commit" "$S/p0.html"` printed line `2308`, the statement assigning the
  `#derived` element's text. Red: the same grep over `p-red.html` counted `0`. The browser pane could not
  be opened from this pass: owed to the close. A headless Edge `--dump-dom` of the pages served by
  `python -m http.server` from the scratch directory stood in: `p0.html`'s header read
  `264 records · latest revision 2026-10-20 · digest 256d5cfc0b82 · generated from e0bcd2298e37 · inputs 7afb66d0f673`,
  `p2.html`'s ended `· 1 uncommitted input`, and `p-red.html`'s ended at `· digest 256d5cfc0b82`.

Probed beside the criteria: a stamp naming an absent commit answered `atlas: stale` with the line
`  the stamp's commit 0123456789ab is not in this repository`; one naming `HEAD~300` listed `20` commits
and `  and 160 more`; `--page` without `--check`, with `--out` or `--claims`, with no value, with a bare
`--ref` or with `--ref -x` each exited `2` with nothing on stdout; and a staged state without a 40-hex
`commit` stopped `--out` with `atlas: cannot stamp the page: the chain state carries no 40-hex commit, but None`,
exit `1`, writing no page.

Owed to the close: the plain bar, whose legs §6 names; AC8 in the browser pane, with its red on the page
of the generator at `d0743a938`.

Owed to the close, and since observed by the main loop in the browser pane: AC8. Green at the close tip
`2d8acb04e93b`, on its page (`git hash-object` `11f11aeed5cb`): `#derived` reads
`264 records · latest revision 2026-10-20 · digest 256d5cfc0b82 · generated from 2d8acb04e93b · inputs b225d5a03556`,
and `--check --page` on it at `HEAD` printed `atlas: current` with exit `0`. Red on the page the generator at
`d0743a938` wrote with `--claims none --out` (`git hash-object` `cf12260418f2`): `#derived` reads
`264 records · latest revision 2026-10-20 · digest 256d5cfc0b82`, with no `generated from` field, and the close
tip's `--check --page` on it printed `atlas: unstamped` with exit `1`.

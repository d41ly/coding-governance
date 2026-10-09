# The design every unit spec builds from: what was read, what was decided, and why

**Serves:** research TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1

Written by the main loop on 2026-10-09 at base `5a836bf0f`, before any spec. Line numbers are at that
base. Every spec in this build cites the decision it implements as `design D<n>`; a spec that needs
to depart from one changes this record first, by a rev line at the foot.

## 1. What was read

- `.githooks/pre-push`, lines 1047-1617: the forcing predicates 1 to 8 in `check_green_record`
  (1185-1248), the three green candidates (1162-1176), the inherited green (1330-1351), the decision
  line (1453-1469), the bar run and its verdict-record check (1563-1617).
- `tools/run-gates/run-gates.sh`: `LEGS_FILE` (216), the turnstile keyed on the git common dir
  (1088-1512), `input_key` (2196-2220), the run header (2224-2275), the opt-in reuse block
  (2280-2304), the ledger write (3636-3685), the `gate-full-green` stamp and its seven preconditions
  (3862-3913).
- `tools/run-gates/gate-fingerprint.sh`: its rev form hashes `<rev>^{tree}` with two empty
  components, so on a clean tree a recorded fingerprint equals the rev form at any commit whose tree
  is the same. Tree equality is therefore already measurable with the helper as it stands.
- `tools/unattended/unattended.sh` 10126-10260, the `gates-green` arm: under `LANDER_MODE=in-place`
  it runs `env GATE_FULL=1 … $GATE_CMD` over the prepared merge, which is the very commit the lander
  then pushes.
- inCMS at `81800a0f9`: `GOV_GATE_CMD="bash scripts/gate.sh"`, inCMS's own leg iterator. Gov's legs
  run as ONE of its legs, `gov-bar`, through `scripts/gov-bar.sh`, which derives a manifest under the
  git dir and `exec`s `scripts/run-gates/run-gates.sh` with `GATE_LEGS` pointing at it. nc declares
  `GATE_CMD="bash scripts/unattended-bar.sh"`.
- The recall probe (terms in §5) and the open asks on the three touched files, among them
  `TOOL-aSurfacedLexicon-25` (a push proceeded with no bar run while the hook said FULL),
  `TOOL-aReapedSpinner-13` (a kill -9 strands the turnstile beacon) and `TOOL-aPacedTurnstile-13`
  (an empty fingerprint on both sides reads as agreement).

## 2. A finding that changes unit A's fix

**The runner's `gate-full-green` in inCMS is not a green of inCMS's bar.** `gov-bar` is one leg of
`scripts/gate.sh`; the nested runner it starts sees a clean tree, a GREEN verdict over gov's legs, and
stamps `gate-full-green` in inCMS's git dir. That stamp proves gov's SUBSET. Today it is refused only
because its `manifest_blob` (the derived file under the git dir) differs from the blob of
`scripts/run-gates/gate-legs.json`. The literal fix in the prompt, "hash the manifest the bar actually
ran", would make the two equal and the boundary would then trust a subset green as a whole bar: an
inCMS push could scope from a sha where an inCMS pytest leg was red. So ABL-aYieldedFork-1 is fixed
by keying the record on the BAR, not by re-hashing the runner's stamp (D2, D3).

## 3. Decisions

- **D1 — staleness counts first-parent landings.** Predicate 3 becomes
  `git rev-list --first-parent --count "$r_sha..$main_local"`, and its message says
  `first-parent landings`. A green earned on a branch tip that lands as a merge's second parent then
  counts the landing merge plus the default-branch commits since the branch last took main, which is
  what the bound was written to measure. `INHERITED_RED_MAX_AGE` already counts this way.
- **D2 — the runner's stamp names its manifest, and the boundary trusts a runner stamp only for a
  runner bar.** The stamp gains `manifest\t<repo-relative path, or the absolute path when outside the
  tree>`. Predicate 7 compares the blob of the RECORDED manifest path at the pushed tip, and refuses a
  record whose manifest is not the manifest the push's bar reads (`${KP}gate-legs.json` for the
  default bar). When the push's bar is not the runner (`bar_record=other`), no runner stamp is a
  candidate at all: the decision line says so. A record with no `manifest` key (every stamp written
  before this build) is read as the kit sibling, which is what every such stamp ran.
- **D3 — the boundary records the green of the bar IT ran: `gate-bar-green`.** A record written by
  the process that ran the declared bar and saw it exit 0, never by a nested runner. Key-per-line,
  the grammar of `gate-full-green`: `sha`, `tree` (`git rev-parse <sha>^{tree}`), `bar` (the bar
  command string), `bar_paths` (each tracked path token of the command, space-separated), `kind`
  (`full`, or `scoped`), `base` (the `GATE_BASE` a scoped run was handed, empty for full),
  `selftests`, `run_id`, `by` (`pre-push` or `unattended`), `stamped`. Written to the git dir and,
  from a linked worktree, as `<common-dir>/gate-bar-green.shared`, exactly as the runner shares its
  stamp. Writers: pre-push after its bar exits 0 on its own verdict (not through the inherited-red
  landing) with HEAD unmoved (TOOL-2); the unattended `gates-green` arm after its bar exits 0 on a
  clean, unmoved tree (TOOL-3). Neither writes on a STUB bar.
- **D4 — a push whose tip TREE equals a recorded green's tree runs nothing: decision `covered`.**
  Before predicates 2 to 8, each candidate (the runner stamps for a runner bar, then the
  `gate-bar-green` records for any bar) is tested for cover: its sha is an ancestor of the tip, its
  tree equals `<tip>^{tree}` (both non-empty, so a failed read on both sides is never agreement,
  `TOOL-aPacedTurnstile-13`), its bar equals the push's vetted bar, its `selftests` covers what this
  push needs (predicate 8's relation), and it is `kind full`, or `kind scoped` with `base` equal to
  the base this push's own decision would pick (D9). A runner stamp's tree is read through
  `gate-fingerprint.sh` at the tip against its `fingerprint`. Covered: one decision line naming the
  record, its sha, its run id and where it was found; the vetted-bar file is still written, so the
  lander marker is unchanged; no bar runs; the run log records decision `covered`. Accepted gap,
  stated in the hook header: legs that read HISTORY rather than the tree (gov's `impure` legs:
  `pass-order history`, `brief-recorded`, `unattended kit gate`) are not re-graded over the landing
  merge commit; under E the post-merge full bar grades them.
- **D5 — re-run only what failed is the runner's `GATE_REUSE=lineage`, set by the boundary itself.**
  Ledger rows gain three fields after `ended-at`: `run` (run id), `full` (`1` when the run was
  `GATE_FULL` on a clean start tree), `manifest_blob`, and `head` (the sha graded). Under
  `GATE_REUSE=lineage` a leg is reused only when every existing term holds (not impure, row `ok`,
  key equal) AND the row is `full 1`, its `manifest_blob` is this run's, and its `head` is an ancestor
  of HEAD. A reusing run may stamp `gate-full-green` when every reused leg met the lineage terms; the
  stamp then carries `reused <n>`. `GATE_REUSE=1` keeps today's meaning and still forbids the stamp.
  pre-push keeps scrubbing an inherited `GATE_REUSE` and, on a FULL decision for a runner bar,
  exports `GATE_REUSE=lineage` itself. Cost stated plainly: an unguarded leg is keyed on the
  whole-tree fingerprint, so any fix re-runs every unguarded leg (61 of 128 in gov at base); the
  saving is the guarded legs a fix does not touch. A wrapper bar such as inCMS's `gate.sh` gets this
  only for the legs it hands to the runner.
- **D6 — one bar per machine: the turnstile lives in a host directory.** `TS_COMMON` is replaced, for
  the beacon and the queue only, by `${GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile}` resolved
  absolutely; the health log, the spawn floor and everything else stay per common dir. The beacon
  gains `repo` (the holder's top level), `run` and `ttl`; a waiter judges staleness against the
  HOLDER's ttl and announces `another bar holds this host — <repo> run <id> pid <pid> — queued at
  position N (waited Ns)`, keeping the byte-stable tail the turnstile suite greps. A holder exports
  `GATE_TURNSTILE_HOLDER=<nonce>`; a runner that inherits a nonce equal to the live beacon's is
  NESTED inside that bar and does not queue (`gate queue: nested under <run>`), which is what keeps a
  suite's scratch-repo bar and inCMS's `gov-bar` from deadlocking on their own parent. A new verb
  `run-gates.sh --hold -- <command…>` takes the turnstile, exports the holder nonce, runs the command
  and releases: how a bar that is not the runner joins the queue. pre-push scrubs
  `GATE_TURNSTILE_DIR` from the bar's environment like the other arm seams.
- **D7 — the post-merge full bar is `tools/run-gates/post-merge.sh <sha>`.** It makes a detached
  scratch worktree of the sha, runs the bar declared at that sha (`GOV_GATE_CMD` from the gate-env
  file, else the runner) with `GATE_FULL=1` through `--hold` (D6, so it takes the next idle local
  slot), writes `gate-bar-green` from that worktree (D3, `by post-merge`), and publishes the verdict
  as a ref on the remote: RED pushes `<sha>:refs/gov/bar-red` (only when that ref is absent or is an
  ancestor of the sha); GREEN deletes `refs/gov/bar-red` when it names an ancestor of, or equals, the
  sha. A local copy, `<common-dir>/gate-post-merge`, names the last verdict for a reader with no
  network. Remote CI runs the same script on the landed sha with credentials that can push a ref.
- **D8 — a post-merge red binds at the boundary.** Only where `GATE_POST_MERGE` is declared in the
  gate-env file AT R (read like `INHERITED_RED`, never from the pushed tree): pre-push reads
  `refs/gov/bar-red` with one bounded `git ls-remote`. Present and an ancestor of the tip, it forces
  FULL unless the adopted full green's sha descends from it — so the fix's own FULL bar, once green,
  clears the force for every later push from that git dir, and the next post-merge green deletes the
  ref for every node. An unreadable ref under a declaration forces FULL. Undeclared, nothing is read
  and every decision is today's.
- **D9 — the boundary's decision is callable: `pre-push --decide`.** Given the tip and R on its
  command line, it prints one line, `full <why>`, `scoped <base>` or `covered <record>`, runs no bar
  and writes nothing. The unattended close calls it (D10) so that the close's bar and the landing's
  decision are one computation.
- **D10 — the lander starts the post-merge bar.** After a landing push that succeeded, where the
  landed tip declares `GATE_POST_MERGE=local`, `tools/push-main.sh` starts `post-merge.sh <tip>`
  detached, records its pid with the process-monitor convention, and prints one line naming it.
  `GATE_POST_MERGE=ci` starts nothing locally: the declaration says remote CI runs it.
- **D11 — the unattended close under a declared post-merge bar runs the boundary's decision.** Where
  `GATE_POST_MERGE` is declared at the default-branch side, the in-place `gates-green` arm asks
  `pre-push --decide` for the prepared merge against R and runs the bar with `GATE_FULL=1` (full),
  `GATE_BASE=<base>` (scoped) or not at all (covered, which the item reports as met by that record).
  Its green is a `gate-bar-green` record (D3) of the same kind and base, so the landing push that
  follows is `covered` by construction. Undeclared, the arm keeps `GATE_FULL=1`.
- **D12 — the text.** `UNATTENDED-PROTOCOL.md`'s landing rule, the charter template's §1 Landing (and
  its render in `AGENTS.md`) and `WIRE-INTO-PROJECT.md` state the scoped-then-full path, the binding
  red and its recorded state, and the adopter declarations below. The prompt asks for this text in
  terms, so writing it is the mandate and not a fork this run resolves.

## 4. What an adopter declares to use each part

| Part | Declaration | Where |
|---|---|---|
| D1, D4, D5 | nothing: a `govkit update` | — |
| D3 for a wrapper bar | nothing: the boundary and the close record it | — |
| D6 for a bar that is not the runner | its bar enters through `run-gates.sh --hold -- <bar>`, or the bar script re-execs itself through it | the bar script |
| D7, D8, D10, D11 | `GATE_POST_MERGE=local` or `GATE_POST_MERGE=ci`, committed | `.githooks/gate-env.sh` |
| D11 for inCMS | relaxing its CLAUDE.md unattended condition 3 | inCMS, the adoption session's change |

## 5. Recall terms used

`pre-push full green stamp staleness lag GATE_FULL_MAX_LAG fingerprint scoped boundary reuse
turnstile manifest_blob`. `reuse_lookup.py` cannot see `.sh` (memory note "reuse_lookup cannot see
shell seams"), so the seams above were found by reading the files named in §1.

## 6. Revisions after the spec pass (main loop, 2026-10-09, from the twelve specs' §8)

- **rev D4/D11 — the in-place landing push does not carry the graded tree.** `write_close_commit`
  commits the run-state record on top of the merge the close graded (TOOL-2 F1, TOOL-3 F1, TOOL-9
  F1), so a first close's landing is never `covered`. Resolved by TOOL-9 F2 option (b), built in
  TOOL-2 rev-2: a `gate-bar-green` record is a CANDIDATE for the boundary's scoped path, not only a
  cover. A `kind full` record passes predicates 2, 3, 5, 6 and 8 exactly as a runner stamp does,
  with the bar compared in place of the manifest blob and the tree in place of the fingerprint. A
  `kind scoped` record at M is adoptable as the scoped base only when its own `base` is a full green
  the decision would adopt by the same predicates, with the staleness bound counted from that base,
  so scoped records cannot chain past a full green. The in-place landing then scopes over the record
  commit alone. Option (c), grading the record commit, reorders the protocol's in-place close and is
  an owner turn, not taken. The text units must not say the landing push is `covered` after a close.
- **rev D6** — `GATE_TURNSTILE_DIR` and `GATE_TURNSTILE_HOLDER` are classified INERT at the
  boundary, not scrubbed (TOOL-5 F1): `GATE_TURNSTILE=0` already reaches the bar, and a scrubbed
  holder would queue a pushing leg behind its own parent bar.
- **rev D9** — `--decide` exits 1 with an empty stdout where the push would be refused (TOOL-7 F1);
  a red on exactly the adopted green's sha does not clear (TOOL-7 F2, strict descent).
- **rev D10** — the process-monitor kit has no registration input (TOOL-8 F1): the post-merge
  child's argv carries its absolute path under the repository root, and its pid lands in the
  lander's own start record.
- **rev D11** — the declaration the close reads is the hook's own gate-env file at R (TOOL-9 F3).

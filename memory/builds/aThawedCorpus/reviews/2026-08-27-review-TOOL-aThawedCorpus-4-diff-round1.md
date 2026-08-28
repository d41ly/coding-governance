**Serves:** diff-review TOOL-aThawedCorpus-5 TOOL-aThawedCorpus-4 TOOL-aThawedCorpus-1

# aThawedCorpus — Tier-2 diff review, round 1

Node `a` · 2026-08-27 · reviewed at HEAD `460a820e`. Review shape: raw 7, confirmed 5, refuted 2,
unverified 0, precision 0.71. Every finding below was re-run in this worktree before it was written
down; nothing here is inferred from the specs or from the finders' prose.

Range: `f1be0b495f216a6b02e1f4e70b852eccfa2a1d2b...HEAD`

## Verdict: BLOCKED

Two blockers, no highs, one medium. The five confirmed findings collapse to three distinct defects:
raw ids 1, 3 and 7 are three reports of one stale stamp, folded here into F1 and adjudicated once at
blocker. Both blockers are BOOKKEEPING, not logic — neither lives in the product change. The one
file this build actually rewrote survived the hunt described below without a confirmed defect, which
is the result that matters for a merge-bar gate. But the branch is red at the push boundary on two
unguarded legs, so it cannot land as it stands, and a third leg is red for a reason this build did
not cause and did not clear.

| # | Severity | Where | Defect |
|---|---|---|---|
| F1 | BLOCKER | `memory/guides/SESSION-KICKOFF.md:8` | `last-body-change` not advanced while the §B body changed; manifest-check check 9 reds at 11 watched commits against a threshold of 10 |
| F2 | BLOCKER | `tools/memory-tree/check-memory-hygiene.sh:13` | `KIT_MEMORY_TREE_VERSION` frozen at 2.47 while 33 behaviour-bearing engine lines moved; `check-verdict-epoch.sh` reds, and the parity harness's baseline floor now points before the rewrite |
| F3 | MEDIUM | `tools/memory-tree/check-memory-hygiene.sh:1137` | Unit 5's compensating control depends on `memory hygiene` never declaring a guard, and nothing asserts that |

## BLOCKER

### F1 — `memory/guides/SESSION-KICKOFF.md:8` · the manifest body changed and its stamp did not

The commit re-stamped `last-audit` and left `last-body-change` on `2196414866`, even though this
same branch revised the §B body: it removed the dated 2026-08-23 self-tests bullet and added two
Environment-traps bullets about the collapsed leg and the pre-commit check-23 exemption. The three
product commits `faf5b7fb`, `5e928f5b` and `3bdc0ce6` each touch `tools/memory-tree/check-memory-hygiene.sh`,
which is a watched path, so the watched-commit count crossed the threshold.

Reproduced at HEAD:

```
MANIFEST check 9 FAILED — the manifest body has not changed across ten or more watched commits,
so its front-loaded claims are drifting unverified; re-read §B and advance last-body-change to a
current sha: 11 non-merge commits since 2196414866a0e2db52759ebd015aae4a79dd0e8d
```

Check 9 is the ONLY red from that script at HEAD, which is how the finding was proven fresh rather
than inherited: at the pinned base the script fails on check 5 alone (the stale `last-audit` this
build correctly repaired), and `git rev-list --count --no-merges 2196414866..<rev> -- <watch set>`
returns 8 there against 11 here. The age arm is not involved — one day against a ninety-day
threshold — so the count arm is the sole trigger and the base/HEAD delta is decisive.

Reachability is not in question. The `kickoff-manifest ratchet` leg in `tools/gate-legs.json` is
`{"argv": ["bash", "skills/session-kickoff/manifest-check.sh"], "chunk": "records", "subject":
"repo", "ceiling": 60}` with NO `guard` key and no `--staged` flag, so it runs on the scoped
`GATE_BASE` branch of `.githooks/pre-push` and under `GATE_FULL=1` alike, and it blocks the push.
There is no waiver path for check 9.

**Fix.** Advance `last-body-change` on line 8 to the sha of the commit that revised the §B body —
`3bdc0ce69cb519474dad8e6bfd5ad34b440b655e` — in a follow-up commit, since a commit cannot embed its
own sha. Then `bash skills/session-kickoff/manifest-check.sh` and confirm exit 0. Re-stamping
`last-audit` does not clear check 9: the two keys measure different events, and a body edit is
exactly what `last-body-change` exists to record.

**Left-shift.** The gate that caught this only fires at the push boundary, which is why a build
carrying three product commits reached a wrap-up with it red. Give `manifest-check.sh` an arm that
gates the CLASS rather than the count proxy: compare a hash of the §B body in the working tree
against the same hash at the commit `last-body-change` names, and red with "the body changed and the
stamp did not" the moment they differ. That arm is cheap enough for the pre-commit fast leg, where
the count arm is not, and it fires on the first commit of a body edit instead of on the tenth
watched commit after it. Stage the break and observe it RED before wiring it, per §7.

### F2 — `tools/memory-tree/check-memory-hygiene.sh:13` · the constant that dates the engine's verdicts did not move

`KIT_MEMORY_TREE_VERSION=2.47   # gov:kit memory-tree@2.47` is unchanged while the engine underneath
it was rewritten. Reproduced at both ends: `bash tools/memory-tree/check-verdict-epoch.sh` exits 0 in
a detached worktree of the base and exits 1 at HEAD with

```
verdict-epoch: FAILED — 33 behaviour-bearing line(s) of the engine moved in faf5b7fb..., and NO
verdict-epoch: commit in f1be0b49..HEAD changes KIT_MEMORY_TREE_VERSION (still 2.47).
```

Not inherited, by construction: the check resolves its base as `git merge-base origin/<default>
HEAD`, which is the branch base, so the range is empty there and green by definition. Not guarded
off either — the `verdict epoch (kit version dates the engine)` leg is `chunk: declarations`,
`subject: repo`, with no `guard` key, and it is a distinct leg from the guarded `verdict-epoch
self-test`, so the held-by-default self-test policy does not save it.

The red row is the smaller half of the damage. `hygiene-parity.test.sh` derives its byte-identity
baseline floor with `git log -S"KIT_MEMORY_TREE_VERSION=$KITV"`, and with the constant frozen that
floor resolves to `d18db6d2` (2026-08-25) — before all three product commits. That harness would
therefore accept the PRE-rewrite base as a legal baseline and assert byte-identity against it, while
`TOOL-aThawedCorpus-5` deliberately changed what `--staged` prints. The one instrument whose job is
to date a verdict change would be lying about this one. That second-order damage surfaces only on a
`GATE_SELFTESTS=1` run, since the parity harness is held by default; the RED unguarded leg is
independently proven and does not depend on it.

**Fix.** Bump the constant and the `gov:kit memory-tree@` marker on that same line, plus line 1 of
`tools/memory-tree/HYGIENE.template.md` and line 1 of `memory/HYGIENE.md` — all three must move
together — in a commit at or after `faf5b7fb`, then
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The gate prints this exact remedy.

**Left-shift.** F1 and F2 are one class wearing two hats: a build changed a versioned or watched
artifact and did not advance the stamp that dates it, and in both cases the only gate that says so
runs at push. One `stamps` leg, runnable under `--staged`, covering both the kit-version constant
and the manifest body hash, would move both to commit time for well under the pre-commit budget.
Wiring `check-verdict-epoch.sh` alone into the pre-commit fast leg is the cheaper half and is worth
doing on its own — it is seconds, against the 16 s the manifest ratchet costs.

## MEDIUM

### F3 — `tools/memory-tree/check-memory-hygiene.sh:1137` · the exemption's compensating control is held in prose only

The header states the basis of unit 5's exemption plainly: "`memory hygiene` DECLARES NO GUARD in
`tools/gate-legs.json`, so it executes on both branches", and `TOOL-aThawedCorpus-2` was retired
specifically to preserve that property. The property is real — `run-gates.sh` skips a guarded leg
whose pathspecs did not change against BASE, and `.githooks/pre-push` takes the scoped `GATE_BASE`
branch whenever its force-predicates all pass, so a guard on this leg would let a scoped
default-branch push skip check 23 while pre-commit already skips it under `--staged`.

Nothing asserts it. The `memory hygiene` row simply OMITS `guard`; `tools/memory-tree/kit.toml:74`
says `guard = []`; the only tracked mentions of the property are comments. Neither of the leg-
correspondence checks helps: `7h` compares name and subject between descriptor and manifest, and `7c`
classifies guard PATHSPECS while asserting nothing about a leg that declares none. Adding a `guard`
key to that row reds no leg, silently reopens the acceptance-ledger hole at both boundaries, and
leaves a green bar throughout. This is the lockstep-invariant-without-a-guard shape, and the move
that breaks it was already proposed once in this very build.

**Fix and left-shift are the same edit.** One assertion over gov's own manifest — cheapest home is
`tools/run-gates/run-gates.gov.test.sh`, beside the existing ceiling arms — that the leg named
`memory hygiene` carries no `guard` key, failing with the reason: "TOOL-aThawedCorpus-5's --staged
exemption leans on this leg running on both pre-push branches". Observe it red against a staged
`"guard": ["memory/"]` on that row before landing it.

## What was hunted and came back clean

The product change is one file and it is a merge-bar gate, so the hunt was weighted toward silent
loss of detection rather than toward crashes. Old and new were read side by side, `f1be0b49` against
HEAD, for check 23's two awk passes and check 21's `proj21`.

- **Per-record state reset.** The retired ledger spelling got `j` and `u` reset free from a fresh
  awk process per file; the new single-pass form resets both explicitly at the top of each path
  record. Present and correct — losing it would attribute one record's criteria to the next.
- **The status header.** Both forms read the first six RAW lines and take the first `**Status:**`
  match. The new one deliberately does not unfence, matching the retired `sed -n '1,6p' | grep -m1`
  and differing from check 12 on purpose.
- **Grandfather position.** In both forms the exemption is applied AFTER the id read and BEFORE the
  population is incremented, so a grandfathered spec leaves the count. Verified against the retired
  `case ... continue` sitting immediately above `alpop=$((alpop + 1))`.
- **First-wins.** `sort -u -t\t -k2,2n -k4,4` restores exactly the retired order — stream order
  across specs, `sort -u` within one — and the `ALFORM` map is populated first-wins, which is what
  reproduces `grep -m1`. A bash associative array is last-wins by default, and getting this backwards
  would have silently reclassified a unit whose ledger carries two lines for one criterion. It is
  written the right way round.
- **Quoting and hostile inputs.** The retired forms were the fragile ones: `for sp in $alspecs` and
  `for r in $(git ls-files ...)` word-split on whitespace, and `while IFS='|' read -r p ids`
  mis-split any path containing a pipe. The tagged path streams and `-F'\t'` are strictly safer, not
  merely equivalent. CRLF, UTF-8 bytes and a missing trailing newline behave identically under
  `getline line < f` and under awk's own operand read; label extraction strips the `\r` in both.
- **awk portability.** No gawk extension is used — `getline`, `close`, `match`/`RSTART`/`RLENGTH`,
  `split`, `substr`, `index`, dynamic regex and `-v` are all POSIX, and `next` inside a `for` inside
  an action is legal in both gawk and mawk. `FAM_ALT` arrives by `-v` rather than being interpolated
  into the program text, which is the corpus's own `heredoc-escape-reaches-the-regex` class avoided
  deliberately.
- **Field-count semantics in `proj21`.** The retired `sed` required all four fields and the new
  `NF < 4 { next }` matches it. `ids = $4` versus the retired `\2` differs only for an S row with
  five or more fields, which `-F'\t'` makes unreachable for the emitter's documented shape.
- **Fail branches and message bytes.** All four check-21 branches and all three check-23 branches
  remain reachable, and the failure strings — including the em dashes in the two `proj21` diagnostic
  lines — are byte-identical to the retired ones. No arm was stranded.
- **`pop_guard` under `--staged`.** Worth stating because it is the obvious worry about unit 5:
  `pop_guard` already returns 0 immediately when `STAGED=1` (`:181`), so check 23's liveness assertion
  was inert on the fast leg before this change and unit 5 removes no signal. The four structural
  siblings announce nothing either; `--staged` is a whole-mode convention, not a per-check skip.

One measurement caveat, not a finding. On this node the post-change full hygiene leg runs 2 m 23 s
wall (5.9 s user, 11.7 s sys), not 34 s. The direction of the collapse is not in doubt and the
controlled pairs in the build record are internally consistent; the absolute figure simply does not
travel across nodes, and the number quoted in the build's own prose should be read as node-scoped.

## Inherited red, not this build's

`bash tools/memory-tree/check-memory-hygiene.sh` exits 1 at HEAD on three check-14 orphans:
`TOOL-aBoundedCeiling-2`, `-3` and `-4`, cited but never defined and unwaived. Verified NOT
attributable to this diff — `python tools/memory-tree/corpus_ids.py --check` in a detached worktree
of `f1be0b49` prints the same three lines and exits 1. The records repair in `617d3c87` added `-2`
to that build's `ids:` roster, which changed nothing here, because check 14 resolves against spec H1
definitions and not against a README roster. Flagged because it is red at the push boundary on the
same leg this build exists to speed up, and clearing F1 and F2 will not clear it.

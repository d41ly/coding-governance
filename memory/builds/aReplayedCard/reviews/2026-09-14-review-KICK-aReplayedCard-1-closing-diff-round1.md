**Serves:** diff-review KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5

# Tier-2 closing diff review — the aReplayedCard build

*Adversarial pass over the cumulative diff of all eight units, run at the integration boundary. Node
`a`, 2026-09-14, ROUND 1. A fan of four primed finder lenses, a skeptic stage in five batches
prompted to REFUTE each finding, one synthesis. Every finding below survived its skeptic; each carries
its address, its fix, and the gate that would have caught it before a reader had to. The synthesis
re-read every cited line at source and ran nothing; what it re-read and what it did not run is listed
at the end. The bug-class checklist for this range, `gotchas.py --for-diff cf401f0e..HEAD`, selected
38 anchored and 5 universal classes and was handed to every lens; the class each finding lands in is
named beside it.*

**Reviewed range:** `cf401f0ef134882d58a9da7fa3c0110097dbd95d...HEAD` — 112 files, +8504/-737, 27
commits, HEAD at `8012832b`.

## Verdict: CLEAN WITH FIXES

No finding rises to BLOCKER as I adjudicate it. Two are HIGH, and both end the same way: a
`--card --append` that exits 2 for a reason unrelated to the body, a card that therefore keeps the
writer's sentinel, a `checkOriented` that then denies every main-loop `git commit`, and a printed
remedy — `/session-kickoff` — that re-runs the refusing append. That is a lockout with no exit the
refusal text names. Neither is a blocker because neither reaches a registered node: this repository
has memory-recall installed and a real `python` on every node in the registry, and an adopter meets
either only after the manual fragment-application step that `TOOL-aReplayedCard-15` already holds
open as a contract change. They are HIGH because the kit is shipped, the configurations are ones the
registry declares supported, and the fix for each is a few lines in one file. Every other finding is
a fix, not a stop: four MEDIUM defects in the deny's target resolution and the merger's marker join,
two MEDIUM coverage gaps in the tests and the token extractor, and five LOW.

## Review shape

Raw 23, confirmed 16, refuted 7, unverified 0, precision 0.70.

**Run integrity — all zero, so this run is complete.** Lenses 4/4 returned, 0 DIED. Skeptic batches
5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded,
0 duplicates. No lens died, so a zero count in a class below is evidence, not a gap. The seven refuted
findings' text was not handed to the synthesis, so this record does not list them; the refuted count
is the pipeline's and is stated as received.

**One adjudication the pipeline's duplicate counter did not make.** Four pairs of confirmed findings
describe one defect each, found by different lenses and each cleared by its own skeptic: ids 2 and 13
(the bare `--write`/`--replay` marker), ids 12 and 18 (the AC10 writer blob pinned at `c95fe32a`),
ids 1 and 7 (a `cd <dir> &&` prefix the deny never reads), and ids 8 and 20 (a `-C` target that does
not exist, walked up into the wrong repository). The pipeline reported 0 duplicates because it
dedupes before adjudication, not after; I merged each pair below. So the honest pair is **16
confirmed reports over 12 distinct defects**. Id 7 straddles the last two pairs — its `cd` half is F3
and its unexpandable-variable half is F4's mechanism — and is counted once, under F3.

**Commits reviewed** (the range's unit-bearing tips): 1e625c21, 2ee24eca, 7dbbf796, e4325047,
35b9e148, 53dafb0a, 39df2b1a, 3e351465, b7f70470, plus the four shared-records commits and the fold
and review commits that precede them.

## Findings

| # | Sev | Ids | Address | Defect |
|---|-----|-----|---------|--------|
| F1 | HIGH | 16 | `skills/session-kickoff/manifest-check.sh:362` | `--card --append` exits 2 whenever `corpus_ids.py` is present but the memory-recall kit is not; the sentinel stands and every commit is denied with a remedy that fails the same way |
| F2 | HIGH | 17 | `skills/session-kickoff/manifest-check.sh:361` | `py=${GOV_PYTHON:-python}` is a second, narrower python resolver; a host with only `python3`, or the Store stub, gets the same lockout |
| F3 | MEDIUM | 1, 7 | `tools/hooks/scratch-guard.js:539` | `checkOriented` never reads a `cd <dir> &&` prefix, so the compound form is judged against the payload cwd: a wrong deny with a wrong remedy in one direction, a silent cross-tree allow in the other |
| F4 | MEDIUM | 8, 20 | `tools/hooks/scratch-guard.js:425` | `resolveToplevel` never stats its start, so a `-C` target that does not exist — a typo, or `$VAR`/`~` read literally — walks up into the nearest ancestor's `.git` and the check runs on a tree the commit does not target |
| F5 | MEDIUM | 2, 13 | `tools/settings-merge.py:264` | The card fragments' markers are the bare tokens `--write`/`--replay`; `set_group`, the rewrite loop and `check-wiring.sh`'s `matchers_of` all treat any SessionStart command containing one as this hook, so an adopter's own hook is silently replaced |
| F6 | MEDIUM | 12, 18 | `tools/hooks/scratch-guard.test.sh:416` | AC10, the only cross-kit arm, runs the writer from a frozen blob 208 lines behind HEAD; the guard this diff added re-runs an arm that cannot observe the live writer |
| F7 | MEDIUM | 19 | `skills/session-kickoff/manifest-check.sh:342` | `extract_card_tokens` emits `path` only for a token with a slash, so a root-level file cited by name is not a token; the header claims the spec-token lint's rule and implements half of it |
| F8 | LOW | 4 | `skills/session-kickoff/manifest-check.sh:335` | A `..`-segment token reaches `git ls-files`, which fatals `outside repository`, and the whole append is refused rather than the token marked UNVERIFIED |
| F9 | LOW | 11 | `skills/session-kickoff/manifest-check.sh:468` | `--card --check` grades the writer's `recent —` block, so a commit subject naming a since-removed path reds the card |
| F10 | LOW | 21 | `tools/hooks/scratch-guard.js:490` | `readMode` matches `authorized-by:` anywhere in the README while the driver reads it only inside the front matter; the AC11 parity arm pins the value set, not the scope |
| F11 | LOW | 5 | `tools/unattended/SKILL.template.md:693` | The Resume prose says the deny refuses a resumed session's first commit; the shipped predicate allows exactly the two card states the sentence names |
| F12 | LOW | 23 | `tools/govkit/entries/check-wiring.kit.toml:10` | The descriptor and `tools/hooks/README.md:61` claim `check-wiring.sh` grades every SessionStart fragment's matcher; `check_card` reads only the two card fragments |

---

### F1 — HIGH — `skills/session-kickoff/manifest-check.sh:362` — id 16

**`--card --append` refuses every body when the memory-tree kit is installed without the
memory-recall kit, and the refusal is a lockout whose printed remedy reproduces it.**

`check_card_citations` resolves `corpus_ids.py`, spawns it with `--print-defined-ids`, and exits 2
on any non-zero status (lines 361-364), on the stated ground that a set that could not be read is
unknown rather than empty. `_render_defined_ids` (`tools/memory-tree/corpus_ids.py:737-738`) calls
`walk()` and `grammar()` unconditionally, and `grammar()` (line 271) raises whenever
`memory-recall/extract.py` is absent — printing a message that says "a pin is set" when none is.
`print_defined_ids`'s own docstring says the pins do not gate it; the grammar does. The memory-tree
descriptor's `requires_if` declares the memory-recall edge only `when_any_key_set` names a pin, and
the kickoff-manifest entry has `requires = []`, so memory-tree + kickoff-manifest + hooks without
memory-recall is a configuration the registry calls supported.

The skeptic reproduced it on a scratch repo holding memory-tree alone: every append exits 2 with the
reader's text. With scratch-guard 1.1 wired the card keeps `READY — none yet`, `checkOriented`
(`scratch-guard.js:541-556`) denies every main-loop `git commit`, and the remedy it prints is the
kickoff whose Step 5 append just refused. Nothing in the refusal names an exit. This repository is
not affected — memory-recall is installed — which is why it is HIGH and not BLOCKER.

Classes: allowlist-narrower-than-the-root-it-guards; amendment-leaves-its-other-half-standing (the
new verb is a memory-recall edge the descriptor does not carry).

**Fix.** Make the missing grammar a NAMED degradation rather than a refusal, in two places. In
`print_defined_ids`, catch the grammar `Problem` and exit 3 with one line naming the missing kit.
In `check_card_citations`, map exit 3 onto the existing `NOTE: id citations unchecked` branch so
paths are still judged and the append proceeds; keep exit 2 for every other non-zero status. Add
`--print-defined-ids` to memory-tree's `requires_if` edge so the descriptor states the dependency.

**Gate.** Stage the break in `manifest-check.test.sh`: reader present, `extract.py` absent, a body
citing one tracked path — expect exit 0, the NOTE line, and the path judged. Observe it RED before
the fix lands (§7).

### F2 — HIGH — `skills/session-kickoff/manifest-check.sh:361` — id 17

**`py=${GOV_PYTHON:-python}` is a second python resolver, narrower than the canonical one and never
run as a probe, and it produces the F1 lockout on a stock Debian host or under the Store stub.**

Line 361 is the file's only python use, introduced in e4325047. It tries one bare candidate and never
executes it. Every sibling that spawns a kit python — `check-memory-hygiene.sh` via `$_PY`,
`run-gates.sh`, every adopter script — inlines the canonical `resolve_python` block from
`tools/lib/resolve-python.sh`, which tries `GOV_PYTHON`, `python3`, `python`, `py` and RUNS each,
because the Microsoft Store `python3` stub answers `command -v` and exits 9009 (charter §11). On a
host with only `python3` (stock Debian and Ubuntu without `python-is-python3`) or where `python` is
the Store alias, the spawn exits 127 or 9009, line 364 exits 2, nothing is appended, and the same
sentinel lockout as F1 follows. The kickoff-manifest kit is copy-installed flat with `requires = []`,
so nothing else on the adopter host supplies the resolver. The refusal prints the failing launcher
name, which is a hint, but never names `GOV_PYTHON`, which is the exit. Registered nodes all carry a
real `python`, so the impact is adopter-side.

Class: second-implementation-is-not-a-second-opinion.

**Fix.** Inline the canonical block between the `# >>> resolve_python — canonical copy` markers and
call `py=$(resolve_python "${GOV_PYTHON:-}") || exit 2` before the spawn; the resolver's own refusal
then names every candidate it ran.

**Gate.** `tools/lib/resolve-python.test.sh` already byte-compares every inlined copy against the
canonical one, so the copy is covered the moment it lands. The class is not: run a predicate over the
real tree (§7) for any tracked `.sh` that spawns a python launcher without sourcing the library or
carrying the block, print hits and near-misses, and wire it as an arm of that same test once its
population is known.

### F3 — MEDIUM — `tools/hooks/scratch-guard.js:539` — ids 1, 7

**`checkOriented` resolves the commit's tree from the payload cwd plus literal `-C` values only, so
`cd <tree> && git commit` — the compound shape the charter itself expects from a session that opens
at the worktrees' parent — is judged against the wrong tree in both directions.**

Line 539 builds `start` from `data.cwd` and `extractCommitTarget`'s `-C` values; no `cd` token is
read anywhere. The skeptic reproduced both directions on a scratch primary with a linked worktree.
Card cell = worktree, payload cwd = primary, command `cd .claude/worktrees/wt && git commit -m y`:
exit 2, `names tree <wt> and this commit targets <primary>`, remedy `cd <primary> &&
/session-kickoff` — which sends the agent to kick off in the tree it is NOT committing to, where the
append's base-not-HEAD refusal then loops it. Mirror: card cell = primary, same command: exit 0,
silently, a cross-tree commit the tree rule exists to catch. `git -C .claude/worktrees/wt commit`
from the same payload gives the right verdict both ways, so the rule binds only to one spelling.
Id 7 adds the false-deny direction that bites before kickoff: a session that has not kicked off
cannot commit into a scratch fixture it just built with `cd $S && git commit` — the deny names a card
that has nothing to do with that repository.

Neither the header's WHAT ESCAPES IT list nor spec S6 names the `cd` form; the header's `does not
follow a cd` line (line 28) belongs to the scratch predicate's ponytail note, not the orientation
check.

Class: grammar-bound-to-the-wrong-root; containment-tested-one-way.

**Fix.** In `extractCommitTarget`, also collect `(?:^|[\s;&|(])cd\s+<token>` occurrences in the view
BEFORE `m.index`, last one wins, read via `readTokenAt` from the original like `-C`; resolve it
against cwd first, then the `-C` chain. Until that lands, list the `cd` form under WHAT ESCAPES IT
and make the remedy name the command's own target.

**Gate.** Two AC arms in `scratch-guard.test.sh`: `cd <wt> && git commit` with cell = wt → allow,
stderr empty; the same command with cell = primary → deny naming `<wt>`. Both RED on the current
hook.

### F4 — MEDIUM — `tools/hooks/scratch-guard.js:425` — ids 8, 20

**`resolveToplevel` never stats its start directory, so a `-C` target that does not exist inherits
the nearest ancestor's `.git` — and in this repo's `.claude/worktrees/` layout that ancestor is the
PRIMARY tree.**

Two reachable cases, one mechanism. A typo'd relative target: from a worktree with a real card naming
it, `git -C ../nope commit` walks from the nonexistent path up to the primary's `.git`, denies with
`names tree <wt> and this commit targets c:/projects/coding-governance`, and prints a remedy that
would re-home the card's tree cell to the primary via `render_tree_cell` — for a commit git itself
refuses with `cannot change to '../nope'`. Following the remedy then denies the worktree's real
commits until a second kickoff. An unexpandable target: `readTokenAt` (lines 214-234) returns
`$ROOT`, `~/x` and `$(pwd` literally, `path.resolve(cwd, '$root')` names a directory that does not
exist, and the walk lands on cwd's own `.git`. So `git -C "$PRIMARY" commit` from a worktree session
with a READY card naming the worktree ALLOWS a cross-tree commit, and with a sentinel card DENIES
naming the worktree as the target. The header's `unwalkable -C target → witness` branch (line 49)
is unreachable for this whole class, because cwd is always inside a repository. Spec S2's stated
intent — a target git would refuse allows with a witness — is contradicted.

Class: grammar-bound-to-the-wrong-root; degradation-known-but-unreported (the witness branch that
cannot fire).

**Fix.** Before `resolveToplevel`, treat the target as unwalkable when `start` does not exist
(`fs.existsSync`) or when any `-C` or `cd` token starts with `$` or `~`, or contains `${` or a
backtick: return `{ witness: 'orientation not checked — target <tok> does not exist or is not a
literal path; git will refuse the commit itself' }`, the existing witness shape. One guard covers
both ids.

**Gate.** Two arms: `git -C ../nope commit` from the worktree → exit 0 with the witness line;
`git -C "$X" commit` on a sentinel card → exit 0 with the witness line. Both RED today (the first
denies, the second denies).

### F5 — MEDIUM — `tools/settings-merge.py:264` — ids 2, 13

**The two card fragments are the only fragments whose marker is a bare flag rather than a script
basename, and all three readers join on that substring, so an adopter's own SessionStart hook
carrying `--write` or `--replay` is moved, overwritten and reported as the wired card.**

`set_group` (line 264) strips from every other-matcher SessionStart group any command containing the
marker and drops a group it emptied; the rewrite loop (line 305) replaces the first in-group command
containing the marker with the card command; `check-wiring.sh`'s `matchers_of` (line 213) greps the
same bare token over a whitespace-stripped view. The skeptics reproduced it twice with the shipped
merger: a settings.json holding `python ".../tools/foo.py" --write` under `startup`, and another
holding `node ".../tools/mine.js" --write-log` under `startup`, each came out of
`settings-merge.py --fragment orientation-card.fragment.json` with the foreign hook and its whole
group gone and the card writer in `startup|clear`; stdout said only `wired ... (backed up)`. Spec
`TOOL-aReplayedCard-2` S1 asserts the markers occur in no other command of THIS repo's settings.json,
which says nothing about an adopter's. Not a duplicate of `TOOL-aReplayedCard-15`, which is about
whether fragments get applied at all; this is what happens when they are. The `.bak` softens a silent
deletion and does not remove it.

Class: grammar-bound-to-the-wrong-root; two-answers-to-one-question (three readers, one substring).

**Fix.** Join on two keys that are already in the fragment: `marker in command AND
basename(hook_path) in command`, in `set_group`, in the rewrite loop, and as a second `grep -F -e
"<basename>"` in `matchers_of`/`wired` — the stripped view keeps a basename intact. Have
`load_fragment` refuse a marker that names no part of `hook_path`'s basename, so a future fragment
cannot reintroduce the bare shape.

**Gate.** One selftest arm in `settings-merge.py`'s suite: a foreign SessionStart command carrying
`--write-log` under `startup` survives the merge byte-identical and in its group. RED on the current
merger.

### F6 — MEDIUM — `tools/hooks/scratch-guard.test.sh:416` — ids 12, 18

**AC10, the only arm that runs the writer's card into the deny's reader, runs the writer from
`SG_WRITER_BASE=c95fe32a` — 598 lines against HEAD's 806 — so a change to the live writer's `tree —`
or `READY —` bytes keeps every suite green while the deny misreads every real card.**

The pinned blob predates e4325047 (`--card --append`, `--card --check`) and has no
`render_tree_cell`; the arm runs its `--card --write` and then replaces the sentinel by `sed`, so the
live writer's tree-cell re-render and appended READY line never reach the hook. The comment's reason
— the live writer was being edited in the same step — expires at the merge. This diff added
`skills/session-kickoff/` to the leg's guard in `tools/gate-legs.json`, which re-runs an arm that
cannot see the file the guard names. No other gate compares the two kits' spellings:
`manifest-check.test.sh` never invokes `scratch-guard.js`, and `READY — none yet` appears only in
the writer, the hook and their two tests, with no parity leg. Where `c95fe32a` is absent the arm
FAILs rather than skips — but `scratch-guard.test.sh` is `role = "project-owned"` in
`tools/hooks/kit.toml`, so no adopter runs it, and the shallow-clone case one finder raised is
gov-only and unrealistic. The staleness is the defect; the severity is MEDIUM for that reason, and
one finder's HIGH is overruled.

Class: staged-break-substitutes-a-synthetic-value; pin-copied-from-another-corpus.

**Fix.** Default to the working-tree writer: run `$ROOT/skills/session-kickoff/manifest-check.sh`
when `SG_WRITER_BASE` is unset, take a blob only when it is given explicitly, and announce a skip
naming the missing kit when neither exists. Keep the `--card --write --session sgtest-w1` invocation
and assertions unchanged, and add one arm that runs the live writer's `--card --append` with a real
READY body and expects the hook to allow with empty stderr — that is the cross-kit fold AC10 was
written for.

**Gate.** The arm is the gate once it reads the live file; its RED is any spelling change in either
kit, which is the point.

### F7 — MEDIUM — `skills/session-kickoff/manifest-check.sh:342` — id 19

**`extract_card_tokens` emits `path` only when `k>1` (a slash) and `base` only with a `:line` tail,
so a root-level file cited by name — `AGENTS.md`, `README.md`, `SESSION-KICKOFF.md` — is not a token
at all, and a body citing only such files is refused as a DEAD PROBE.**

The header (line 317) claims "the rule the spec-token lint applies", but `tools/check-spec-tokens.py`
(lines 21-22) defines path-shaped as "a slash AND an extension, OR an exact tracked path
(`TOOL-dRetiredFork-20` F2)"; the extractor implements the first half only, and the omitted half was
added to the sibling by a recorded decision for precisely this class. The skeptic reproduced the
lockout: `scope: touch README.md` plus a real READY line → exit 1, the card keeps the sentinel, and
scratch-guard's remedy reproduces the refusal. The impact is edge-case — a realistic Step 5 body
carries a slashed entrypoint or an id — but an adopter whose governing docs sit at the root gets its
most-cited files reported as nothing to check, which is the inverted fixture class: a checkable claim
reported as no claim.

Class: fixture-passes-by-finding-nothing.

**Fix.** Let a slashless dotted token join the `git ls-files` pathspec as a CANDIDATE and count it as
a `path` token only on an exact tracked hit — the sibling's "exact tracked path" arm. That verifies
`AGENTS.md` in the spawn the extractor already makes and never turns `e.g` into an UNVERIFIED. A
basename-only token keeps the `base` kind only when it carries a range, as now. Correct the header to
say both halves.

**Gate.** One arm in `manifest-check.test.sh`: a body citing only a root-level tracked file and an
id → appended, 2 tokens, 0 unverified. RED today (DEAD PROBE).

### F8 — LOW — `skills/session-kickoff/manifest-check.sh:335` — id 4

**A `..`-segment path token reaches `git ls-files -- <tok>`, which fatals `outside repository`, and
the whole append is refused with nothing appended.**

The awk filter (lines 335-350) skips absolute, `~`, `$`, `<`, `{{`, drive-letter and glob tokens as
non-claims about this tree, and lets `../../outside.md` through. Reproduced end-to-end: a body citing
`README.md and ../../outside.md` with a base-matching READY line → `MANIFEST env ERROR — git
ls-files failed over the cited paths`, exit 2, card unchanged. A sibling-repo or worktree-relative
citation from the worktrees' parent is enough. The refusal is loud and names the token, so nothing is
lost; it is a false red on an innocent body and is documented nowhere as a ceiling.

Class: bounded-through-a-pipe-is-unbounded (one token's fatal takes the whole batch).

**Fix.** Skip tokens with a `..` segment in the awk filter — `t ~ /(^|\/)\.\.(\/|$)/` — or pre-mark
them UNVERIFIED without joining them into the pathspec; keep the ls-files refusal for a reader that
genuinely could not answer.

**Gate.** One arm: a body carrying a `..` citation beside a tracked path → appended, the `..` token
absent from the count or marked UNVERIFIED, exit 0. RED today.

### F9 — LOW — `skills/session-kickoff/manifest-check.sh:468` — id 11

**`--card --check` runs the citation check over the WHOLE stored card, including the writer's
`recent —` block, so a `git log --oneline` subject carrying a path-shaped token is graded as a
citation.**

`check_card` passes `$CARD_FILE` to `check_card_citations`, whose extractor blanks only
`UNVERIFIED —` lines. Reproduced in a scratch repo: `--card --write` then `--card --check` on an
untouched card printed `UNVERIFIED — tools/gone.sh · line 7` (and line 8 for the earlier `add`
subject) and exited 1. The check reds on text the session never wrote and cannot fix, and a card whose
only miss is a commit subject is indistinguishable from one with a stale kickoff citation. Nothing
auto-invokes `--check` and no arm covers the recent block, so LOW.

Class: fold-text-is-unreviewed-surface (git-authored lines graded as authored ones).

**Fix.** In `check_card`, run `extract_card_parts` first and blank the `recent —` run the way
annotation lines are blanked — blanking, not deleting, so line numbers still address the rows they
belong to — before handing the file to `check_card_citations`.

**Gate.** One arm whose fixture commit subject names an untracked path, expecting a clean `--check`.
RED today.

### F10 — LOW — `tools/hooks/scratch-guard.js:490` — id 21

**`readMode` matches `authorized-by:` anywhere in the README bytes with `/m`, while the unattended
driver (`unattended.sh:1375-1379`) reads the key only between line 2 and the closing `---`, and
`PROTOCOL.template.md:46` defines it as a front-matter key.**

A NEW `builds/<x>/README.md` whose front matter omits the key but whose body carries a column-0
`authorized-by: prompt` line — a fenced example, copied prose — exempts every commit of the session
in the hook and authorizes nothing in the driver. Two readers of one key with different scopes. The
AC11 parity arm (`scratch-guard.test.sh:444-452`) compares only the value set against
`SECOND_ANCHOR_MODES`, so the scope split is invisible to it. Spec S4 says "bytes carry", so the hook
matches the spec's wording, but the spec's own §10 names the driver's set as the source. Evasion
only — an evader would put the key in the front matter — so the real exposure is an accidental
exemption, and LOW.

Class: two-answers-to-one-question.

**Fix.** Apply the regex to the slice of `bytes` between the first `---` line and the next `---`
line, and to nothing else.

**Gate.** One AC4 arm with the key in the body only, expecting the sentinel deny. RED today.

### F11 — LOW — `tools/unattended/SKILL.template.md:693` — id 5

**The Resume prose says a resumed session's first commit is "the one a card-reading commit deny
refuses"; the shipped predicate ALLOWS both card states the sentence names.**

Lines 691-693 (and the rendered `.claude/skills/unattended/SKILL.md:693`) say a resumed session
"starts with no card, or a replay-written one" and that the deny refuses its first commit.
`scratch-guard.js:545` allows an absent card with a witness line, `:547` allows a `--card --replay`
header, and `--card --replay` on a missing card writes a fresh one under its own name
(`manifest-check.sh:279-280`), so a `resume|compact` SessionStart yields an allowed card. Spec
`TOOL-aReplayedCard-1` §8 resolved absence and replay to ALLOW; the `TOOL-aReplayedCard-3` prose
written on top of it claims the opposite. The step's conclusion — the resumed run owes the kickoff —
survives, because the deny does bind a NEW session after process death; its premise and its backstop
claim are both false, and a `--resume`d run that skips Step 5b commits with no refusal.

Class: two-answers-to-one-question; amendment-leaves-its-other-half-standing.

**Fix.** Reword to the actual contract: the deny does not reach an absent or replay-written card, so
the resumed run owes the kickoff because nothing else will orient it. If a backstop is wanted, that is
a predicate change in `scratch-guard.js`, not prose.

**Gate.** None fits a sentence; this joins the §10 checklist as a documented check — a template that
names a hook's behaviour is graded by reading the hook's evaluation-order comment beside it.

### F12 — LOW — `tools/govkit/entries/check-wiring.kit.toml:10` — id 23

**The descriptor and `tools/hooks/README.md:61-63` claim `check-wiring.sh` reds on any SessionStart
entry under a matcher that is not its fragment's; `check_card` (`check-wiring.sh:534-536`) iterates
only `orientation-card` and `orientation-replay`.**

No arm reads `tools/check-wiring.fragment.json` or
`tools/process-monitor/procmon-session.fragment.json`. Reproduced in a scratch clone: narrowing the
`startup|resume|clear` group holding `check-wiring.sh --session` and `procmon-hook.js` to `startup`
produced byte-identical `check-wiring.sh --check` output, and `adopt-process-monitor.sh --check`
still exits 0 because `measure_hook_entries` (line 198) counts entries per event and never reads the
matcher. Spec `TOOL-aReplayedCard-2` S6 scoped the arm to the two card fragments; the prose generalised
it. A gate's own header states what it does NOT check (§7); this one states coverage it lacks. LOW
because the merger re-matches on apply, but a hand edit or a later narrowing passes green.

Class: degradation-known-but-unreported.

**Fix.** Either generalise `check_card` into a loop over every shipped `*.fragment.json` whose
`event` is `SessionStart` — marker, matcher and hook path all read from the fragment, as the card arm
already does — or strike the "gradeable" and "reds on an entry under a matcher that is not the
fragment's" sentences and name the two ungraded entries in the README.

**Gate.** If generalised: one arm per shipped SessionStart fragment, narrowed to `startup`, expecting
UNWIRED. If struck: nothing to gate, and the README's claim shrinks to what the checker does.

---

## The classes that drew nothing

The lenses were primed with 43 classes; the findings above land in 12 of them. All four lenses
returned, so a class with no finding was in scope for four readers and is a zero with a live probe
behind it — evidence, not a gap, as far as the lenses' own coverage goes. The synthesis ran no probe
of its own over those classes and asserts nothing further about them: in particular it did not
re-run the lexicon leg, the hook-destinations gate or the conf-sourcing checks at the tip, and this
record does not claim they are green.

## What the synthesis re-read, and what it did not run

Re-read at source for every finding above: `scratch-guard.js` lines 400-556 (the predicate,
`resolveToplevel`, `readMode`, `checkOriented`) and its header lines 1-61; `manifest-check.sh` lines
305-480 (`extract_card_tokens`, `check_card_citations`, `add_card_body`, `check_card`);
`corpus_ids.py` lines 262-290 and 720-745; `settings-merge.py` lines 255-310; `check-wiring.sh`
lines 205-218 and 528-560; `scratch-guard.test.sh` lines 405-470; both card fragments;
`tools/hooks/kit.toml`'s role rows; `tools/memory-tree/kit.toml`'s `requires_if`;
`SKILL.template.md` lines 686-696; `check-wiring.kit.toml` lines 8-13; `tools/hooks/README.md` lines
59-64; `tools/lib/resolve-python.sh`'s header. Every line number in the table was verified with
`grep -n` at HEAD; one finder's `settings-merge.py:308` for the rewrite loop is line 305.

Not run: no reproduction was re-executed by the synthesis. Every "reproduced" above is the skeptic's
own observation, stated as received. Not read: the seven refuted findings, the eight acceptance
ledgers and the eight spec folds beyond the lines the findings cite — the brief names them as
unreviewed surface and this round did not review them; that is a gap, not a clean result.

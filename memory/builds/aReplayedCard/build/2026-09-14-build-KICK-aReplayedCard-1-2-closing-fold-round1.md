# The closing review's round 1, folded — twelve of twelve

**Serves:** journal KICK-aReplayedCard-1 KICK-aReplayedCard-2 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3

The fold of `memory/builds/aReplayedCard/reviews/2026-09-14-review-KICK-aReplayedCard-1-closing-diff-round1.md`
(CLEAN WITH FIXES, F1–F12), node `a`, 2026-09-14, at review tip `e54c3849`. Every gate the review
named is an arm that was OBSERVED RED before its fix landed; the how is on each line. Where the
review offered two fixes, the smaller one the gate could prove was taken and the other is named.
No spec moved: all eight units are CLOSED, so a fold to a closed unit's code is recorded here.

## What moved, per finding

- F1 — `tools/memory-tree/corpus_ids.py` `print_defined_ids` exits 3 with one line naming the memory-recall kit when `extract.py` is absent; `skills/session-kickoff/manifest-check.sh` `check_card_citations` maps 3 onto the `NOTE: id citations unchecked` branch and still judges paths; `tools/memory-tree/kit.toml` `requires_if` gains `when_verb_used`.
  RED, twice: the corpus selftest arm `--print-defined-ids with no memory-recall kit exits 3` run on a clone with the guard removed — 1 of 57 arms failed, printing the grammar's Problem; the `manifest-check.test.sh` arms `F1 a reader with no memory-recall kit degrades to the NOTE` and its READY-line check run against HEAD's checker in a frozen clone — exit 2. Then GREEN.
- F2 — `skills/session-kickoff/manifest-check.sh` carries the canonical `resolve_python` block inline and spawns `py=$(resolve_python)`; `tools/lib/resolve-python.test.sh` gains the parameter-default shape `:-python}` in `bare_scan` with three plants (two spellings that shipped, one near-miss `${GOV_PYTHON:-}`); `tools/install-prefix-carried.txt` rises 2 → 3 for the marker line, hand-justified.
  The class predicate over the real tree, printed before wiring: 7 hits — the defect and six test suites (`tools/check-kit-placeholders.test.sh`, `tools/check-spec-tokens.test.sh`, `tools/check-wiring.test.sh`, `tools/process-monitor/adopt-process-monitor.test.sh`, `tools/run-gates/run-gates.evidence.test.sh`, `tools/run-gates/run-gates.turnstile.test.sh`), each now resolving by running with the house `gov:literal-python` fallback where `../lib/` may be absent. RED: the leg listed all seven before the six were fixed. The leg was ALREADY red at HEAD on three older-ban offenders nobody saw because `subject = kit` legs are held off the bar: `manifest-check.test.sh` `REAL_PY="$(command -v python)"` (now resolved) and `GOV_PYTHON=python` (a marked shim name), and `run-gates.evidence.test.sh` `DC_PY=python` (marked fallback, block moved above its first use). The S1 arm now shadows all three launcher names with a shim that passes the `-c` probe and fails the reader, because a resolver that RUNS candidates falls through `GOV_PYTHON=false` to the real python.
- F3 — `tools/hooks/scratch-guard.js` `extractCommitTarget` reads the last `cd <dir>` before the git token (last one wins) and resolves it before the `-C` chain; the header's evaluation order and WHAT ESCAPES IT say so. Four `scratch-guard.test.sh` arms: absolute `cd <wt>` from the primary with cell = wt → allow, relative `cd sgwt` from the fixtures' parent → allow, cell = primary → deny naming `<wt>` and `cd <wt> && /session-kickoff`, two `cd`s → the last wins.
  RED: all four failed on HEAD's hook in the frozen clone (exit 2 want 0, non-empty stderr, exit 0 want 2, non-empty stderr).
- F4 — `checkUnwalkableTarget` refuses an empty, `-`, `$`/`~`-leading, `${` or backtick target as a witness, and `fs.existsSync` refuses a start that is not on disk before `resolveToplevel` walks; the AC9 `/nowhere/x` arm now expects the does-not-exist line and a new arm keeps the no-`.git`-above line on an existing directory under no repository. Four arms: `git -C ../sgfix/nope` (the walk would land on the PRIMARY's `.git`) → does-not-exist line; `git -C "$X"`, `cd $S`, `cd ~/x` on a sentinel card → not-a-literal-path line.
  RED: all four failed on HEAD's hook (the first walked and allowed with the wrong line; the other three denied).
- F5 — `tools/settings-merge.py` `check_ours` joins on marker AND `basename(hook_path)` in `set_group` and the rewrite loop; `tools/check-wiring.sh` `matchers_of` takes the basename as `$2` (defaulting to the marker, so one-key callers read as before), `wired` passes it, `check_card` supplies it. Selftest arm 14c: a foreign `node ".../tools/mine.js" --write-log` under `startup` survives the card merge byte-identical and in its group.
  RED: on a clone with the join reverted to marker-only, 14c failed with the foreign hook gone and the writer in its place. The `load_fragment` refusal the review also offered was NOT taken: the shipped card markers `--write`/`--replay` name no part of `manifest-check.sh` by design, so that refusal would reject the fragments it exists to protect; the two-key join is what the gate proves.
- F6 — `tools/hooks/scratch-guard.test.sh` AC10 runs the WORKING TREE's `skills/session-kickoff/manifest-check.sh`; `SG_WRITER_BASE=<sha>` takes a blob only when given; neither present is an announced `SKIP`. The `--card --write --session sgtest-w1` invocation and its three assertions are unchanged; one new arm runs the live writer's `--card --append` with a real READY body at the worktree's HEAD and expects the hook to allow with empty stderr — the cross-kit fold.
  RED: `SG_WRITER_BASE=c95fe32a bash tools/hooks/scratch-guard.test.sh` — the pinned blob has no `--card --append`, so the fold arm fails on it, which is the staleness the finding names; on the live writer the suite is `PASS (137 assertions)`.
- F7 — `extract_card_tokens` emits a `cand` kind for a slashless dotted token, which joins the one `git ls-files` pathspec and counts as a path token ONLY on an exact tracked hit — the spec-token lint's second half; the header states both halves. Arm: a body citing `AGENTS.md` by name, `e.g.` and the clone fixture's one defined id → appended, `2 tokens · 0 unverified`, `e.g` nothing.
  RED: on HEAD's checker the arm appended 1 token (the id alone).
- F8 — the awk filter skips a token with a `..` segment before it can reach the pathspec. Arm: `skills/session-kickoff/SKILL.md` beside `../../outside.md` → appended, `1 tokens · 0 unverified`.
  RED: on HEAD's checker exit 2, `git ls-files failed over the cited paths`.
- F9 — `check_card` blanks the `recent —` run (the heading and every `<sha> <subject>` line beneath it, blanked not deleted) into `$CARD_TMP/checked` before `check_card_citations`. Arms: an empty fixture commit `drop tools/gone.sh from the bar` in worktree B, a card written over it, a body appended, then `--card --check` → exit 0, prints nothing.
  RED: on HEAD's checker exit 1, an `UNVERIFIED — tools/gone.sh` line printed for a subject git wrote.
- F10 — `readMode` in `checkAuthorizedReadme` applies the key regex to the slice between the opening `---` on line 1 and the next `---` line and to nothing else, the unattended driver's scope. AC4 arm: a staged NEW README with the key in the BODY only (a fenced example) → deny.
  RED: on HEAD's hook exit 0 want 2 — the body key exempted the commit.
- F11 — `tools/unattended/SKILL.template.md` Resume prose reworded to the contract: an absent card and a replay-written one are two states the deny does NOT reach (both allow, with a witness line), so the resumed run owes the kickoff because nothing else orients it, and a backstop would be a predicate change in the hook. Re-rendered by `bash tools/unattended/adopt-unattended.sh`; `--check` reports in sync. No gate fits a sentence: the documented check joined `memory/gotchas/two-answers-to-one-question.md` as its prose form — a template naming a hook's behaviour is graded by reading the hook's evaluation-order comment beside it.
- F12 — the generalisation was NOT taken (a fragment-discovery loop with skip semantics per fragment and one arm per fragment in `check-wiring.test.sh` is over the 30-line bound); the claims were corrected to what `check_card` grades: `tools/govkit/entries/check-wiring.kit.toml` says the fragment makes the entry RE-MATCHABLE, not graded; `tools/hooks/README.md` names the two ungraded entries; `tools/check-wiring.sh` `check_card` carries a WHAT THIS DOES NOT CHECK paragraph. Nothing to gate; the claim shrank to the checker.

## The bump the epoch leg demanded

`corpus_ids.py` moved behaviour-bearing lines after `53dafb0a`'s 2.75 bump, so `KIT_MEMORY_TREE_VERSION` is 2.76
in every carrier: the constant and its marker in `tools/memory-tree/check-memory-hygiene.sh`, the four
templates under `tools/memory-tree/`, and their four renders under `memory/` via
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`; `bash tools/check-kit-versions.sh` is clean.
`tools/install-prefix-waivers.txt` re-keyed its two `corpus_ids.py` rows (971 → 997, 975 → 1001) after
the insertions above them, the line-keyed-registry class this repo already names.

## Floors

`skills/session-kickoff/manifest-check.test.sh` `FLOOR_ASSERTIONS` 165 → 174 (nine arms: F1 ×3, F7,
F8, F9 ×4); `tools/hooks/scratch-guard.test.sh` 122 → 134 (F10, F3 ×4, F4 ×4, the split AC9 unwalkable
arm, the AC10 fold pair); `tools/lib/resolve-python.test.sh` counts its own arms (59, from 56).

## What this fold did not do

It did not re-review the fold text; that is round 2's subject. It did not gate the `cd` reading against
a `cd` inside a subshell or after a `||` — `(cd x && git commit)` and `cd x || exit; git commit` are read,
`cd "$(pwd)/x"` is a witness. It left `tools/check-wiring.sh` with no arm for the two-key join of its
own; the join is exercised by `settings-merge.py` arm 17, which lifts `matchers_of` verbatim and calls
it one-keyed, and by `check-wiring.test.sh`'s 103 arms over the live checker.

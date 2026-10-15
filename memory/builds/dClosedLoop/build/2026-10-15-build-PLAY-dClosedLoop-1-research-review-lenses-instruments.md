# Research: the review system, which lenses gov should carry: the instruments

**Serves:** research PLAY-dClosedLoop-1

Dispatch 37 wrote these in the session scratchpad and cited them from its return,
`build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses.md`. Every file is kept verbatim as
fenced text, because the lexicon gate grades every tracked Python file. None was run again for this
record. A file that was not UTF-8 is decoded from Windows-1252, and its heading says so.

## `corpus.py`

```python
"""Report-level census of every review report: kind, verdict token, lens-set evidence. Read-only."""
import os, re, sys, glob, collections
repo = sys.argv[1]
files = sorted(glob.glob(os.path.join(repo, "memory/builds/*/reviews/*.md")))
V = collections.Counter(); L = collections.Counter(); tally = collections.Counter()
LENSKEYS = ["underspecification","contradiction","unstated-assumption","prior-art","coherence","grounding","reuse","blast-radius","failure-envelope",
            "security","correctness","seams","verification","intent","regressions","data-integrity","dead-code","integration-seams","performance"]
mentions = collections.defaultdict(collections.Counter)
for f in files:
    t = open(f, encoding="utf-8", newline="").read()
    head = "\n".join(t.splitlines()[:12])
    m = re.search(r"^\*\*Serves:\*\* ([a-z-]+)", head, re.M); kind = m.group(1) if m else "?"
    if kind not in ("spec-audit","diff-review"): continue
    vm = re.findall(r"^## Verdict:\s*\**\s*([A-Z][A-Z \-]+?)\**\s*$", t, re.M)
    V[(kind, vm[0].strip() if vm else "(no ## Verdict line)")] += 1
    month = os.path.basename(f)[:7]
    for k in LENSKEYS:
        if re.search(r"(?<![\w-])" + re.escape(k) + r"(?![\w-])", t): mentions[(kind, month)][k] += 1
    tm = re.search(r"Adjudicated tally by item: (\d+) items, of which (\d+) are blockers, (\d+) high, (\d+) medium and (\d+) low", t)
    if tm:
        tally[(kind,"reports")] += 1
        for i, s in enumerate(["items","blocker","high","medium","low"]): tally[(kind, s)] += int(tm.group(i+1))
print("== verdict token by kind")
for k, n in sorted(V.items()): print(f"  {k[0]:12s} {k[1]:24s} {n}")
print("== structured 'Adjudicated tally by item' lines")
for k, n in sorted(tally.items()): print(f"  {k[0]:12s} {k[1]:10s} {n}")
print("== reports mentioning each lens key, by kind and month (a mention is not an attribution)")
for k in sorted(mentions):
    print(f"  {k}: " + ", ".join(f"{x} {n}" for x, n in mentions[k].most_common()))
```

## `escape_class.py`

```python
"""Tally the researcher's lens classification of each gotcha (the judgment is the MAP below,
shown whole), split by whether gotchas.py found a build named in it reviewed on or before it was filed.
Refuses if a gotcha in gotchas.out is unmapped or a mapped name is absent. Usage: python escape_class.py gotchas.out"""
import sys, collections
MAP = {
# verification: a check that cannot fail / proves the wrong thing
**{k: "verification" for k in """a-grep-for-a-word-is-a-presence-probe a-helper-extraction-blinds-a-per-function-rule ab-arm-never-did-the-work
absence-assertion-over-whole-file-text arm-literal-strands-on-message-edit armed-but-unreachable-rule assertion-between-two-derived-values
borrowed-seed-inherits-its-head-state fallback-fabricates-the-passing-value fixed-sleep-does-not-place-a-signal fixture-passes-by-finding-nothing
fixture-removes-the-path-under-test floor-left-below-the-arms-it-guards git-rm-cached-refuses-a-diverged-index-blob line-claim-matched-over-the-whole-output
line-count-reads-empty-capture-as-one liveness-negative-from-another-population observation-before-the-last-fold-of-the-same-commit
observed-by-claim-no-arm-discharges overlap-judged-from-the-invocation-interval pin-gated-checks-arm-nothing-without-a-pin
second-implementation-is-not-a-second-opinion staged-break-runs-stale-bytecode staged-break-substitutes-a-synthetic-value status-set-in-a-subshell
swallowed-delegate-reads-as-clean test-oracle-read-from-a-historical-sha vacuous-selector-empty-population""".split()},
**{k: "correctness" for k in """a-merge-of-the-default-branch-read-as-additions a-new-local-collides-in-a-long-function a-pair-exists-and-it-is-the-wrong-one
anchor-literal-resolves-above-its-target check-format-grades-two-populations destructive-step-before-its-precondition empty-field-collapses-unless-it-is-last
guard-fed-the-value-it-supersedes heredoc-escape-reaches-the-regex id-matched-as-a-substring inline-fence-swallows-the-rest-of-the-file
inline-marker-breaks-a-line-continuation join-key-widened-by-a-shared-location ledger-token-wrapped-across-a-line-joins-nothing
line-keyed-registry-reds-on-a-file-that-grew name-search-resolves-a-namesake nt-against-a-missing-file-is-true one-value-field-records-a-mixed-outcome
porcelain-diff-names-a-rename-by-its-destination record-file-read-by-line-position sourced-conf-blank-overrides-the-default structured-record-split-on-whitespace
trailing-comma-counted-as-an-element two-answers-to-one-question two-guards-one-question-two-answers two-readers-of-one-config-one-re-derived
verdict-printed-before-the-step-that-reverts-it waiver-row-that-hides-nothing-reds""".split()},
**{k: "seams" for k in "degradation-known-but-unreported format-derived-from-arity guard-above-a-fold-makes-its-fallback-dead merge-keeps-both-sides-of-one-derivation".split()},
**{k: "security" for k in """a-view-fix-trades-one-blindness-for-another conf-value-interpolated-into-a-regex containment-tested-one-way decision-re-derived-by-a-second-process
inputs-inside-the-subjects-reach withheld-value-recovered-from-a-derived-one""".split()},
**{k: "coherence" for k in "amendment-leaves-its-other-half-standing criterion-asserts-what-its-own-command-cannot-show orchestrator-hand-off-owed-a-disposition".split()},
**{k: "grounding" for k in "spec-names-code-its-base-lacks".split()},
**{k: "blast-radius" for k in """a-folded-field-leaves-its-row-shape-docs-behind a-new-leg-trips-a-growing-set-of-meta-gates a-runner-knob-owes-a-push-class
a-spelling-change-strands-its-readers hand-named-gate-list-green-while-the-bar-reds held-suite-guard-misses-a-sibling-kit naming-leg-grades-what-python-named
record-citing-a-foreign-id-defines-or-orphans-it record-without-serves-or-with-a-round-counter reflowed-prompt-string-reads-as-a-deleted-stop
retirement-inventory-misses-readers-by-value""".split()},
**{k: "failure-envelope" for k in """a-merged-in-check-can-refuse-a-pinned-record allocation-knob-without-a-ceiling async-job-starts-with-sigint-ignored beacon-published-before-it-is-complete
invariant-held-on-one-admission-path row-driver-emits-a-plausible-file-with-rows-missing signal-trap-runs-the-exit-handler-twice trapped-signal-waits-for-the-foreground-child""".split()},
# candidate lenses
**{k: "portability" for k in """allowlist-narrower-than-the-root-it-guards bash-c-multiline-flattens-under-msys fixture-inherits-ambient-machine-state gate-green-by-accident-on-generated-bytes
msys-grep-counts-cr-on-every-line signal-killed-hook-reads-as-success subprocess-resolves-a-different-shell text-mode-read-eats-a-bare-cr worktree-crlf-outside-the-gated-population""".split()},
**{k: "adopter" for k in """a-gate-that-walks-the-repo-root-reads-other-worktrees fixture-lacks-a-gate-the-consumer-has grammar-bound-to-the-wrong-root pin-copied-from-another-corpus
shipped-checker-edit-is-an-adopter-contract-change""".split()},
**{k: "cost" for k in "bounded-through-a-pipe-is-unbounded concurrency-is-not-a-budget process-creation-is-the-suite-cost trace-profile-measures-itself".split()},
**{k: "assumptions" for k in "node-check-is-not-a-syntax-gate settings-edit-takes-effect-mid-session".split()},
**{k: "topology" for k in """hookspath-resolves-into-another-checkout index-derivation-reads-a-half-staged-move-as-a-deletion inherited-git-dir-pins-the-work-tree-to-the-cwd
predicate-bounded-by-its-own-count suite-edited-while-bash-executes-it suite-invalidated-by-a-commit-under-it witness-graded-against-a-fact-written-after-it""".split()},
**{k: "no lens (review shape or run order)" for k in "fold-text-is-unreviewed-surface history-leg-graded-before-the-reconcile-commit".split()},
**{k: "(invariant, not an escape)" for k in "canary-waits-on-a-rendezvous-not-a-clock concurrent-runs-are-announced-not-refused sweep-issues-no-cost-verdict".split()},
}
PRESET = {"verification": "diff", "correctness": "diff", "seams": "diff", "security": "diff", "intent": "diff",
          "coherence": "spec", "grounding": "spec", "reuse": "spec", "blast-radius": "spec", "failure-envelope": "spec"}
rows = [l.split(" | ") for l in open(sys.argv[1], encoding="utf-8", errors="replace").read().splitlines()[1:]]
names = {r[2] for r in rows}
miss = sorted(names - set(MAP)); extra = sorted(set(MAP) - names)
if miss or extra: sys.exit(f"unmapped {miss} / mapped-but-absent {extra}")
tot = collections.Counter(); rev = collections.Counter()
for r in rows:
    c = MAP[r[2]]; tot[c] += 1
    if r[3] != "reviewed-before: -": rev[c] += 1
print(f"gotchas {len(rows)}")
print("| lens | preset kind | gotchas | of which name a build reviewed before the gotcha was filed |")
print("|---|---|---|---|")
for c, n in tot.most_common(): print(f"| {c} | {PRESET.get(c, 'not in a preset')} | {n} | {rev[c]} |")
inp = sum(n for c, n in tot.items() if c in PRESET); cand = sum(n for c, n in tot.items() if c in ("portability","adopter","cost","assumptions","topology"))
print(f"in a preset lens's brief: {inp}; candidate lens: {cand}; no lens: {tot['no lens (review shape or run order)']}; invariants: {tot['(invariant, not an escape)']}")
```

## `gotchas.out`, decoded from Windows-1252

```text
gotchas 121; naming a build 95; naming a build reviewed on or before the gotcha was added 83
2026-10-04 | class | a-folded-field-leaves-its-row-shape-docs-behind | reviewed-before: aWindowedPass | a review fold adds a key to a declared row shape in the code and its gate, and the spec body and the README that describe that shape keep the old key set
2026-10-13 | class | a-gate-that-walks-the-repo-root-reads-other-worktrees | reviewed-before: cListedCensus | a gate that lists its files by walking the disk from the repo root also reads every untracked worktree an adopter parks inside the tree, so it reds on files the commit does not hold, and an attribution re-run in a fresh worktree calls that red OWN
2026-10-05 | class | a-grep-for-a-word-is-a-presence-probe | reviewed-before: aGraftedHelix | a grep for a word over a source file proves the word is there, not that the code around it runs, so a comment or a dead block satisfies the criterion it was written to observe
2026-10-06 | class | a-helper-extraction-blinds-a-per-function-rule | reviewed-before: aGraftedHelix | a source rule that pairs two facts on lines of ONE function goes blind when a refactor moves one half into a new helper, naming a correct function or exempting one that no longer holds the half
2026-10-13 | class | a-merge-of-the-default-branch-read-as-additions | reviewed-before: dSweptBranches | a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot
2026-10-05 | class | a-merged-in-check-can-refuse-a-pinned-record | reviewed-before: aEvidencedLens,aGraftedHelix,aWardedAudit | a merge of the remote's default branch into a run branch brings in a check, or narrows one, that the running record cannot satisfy because the bytes it grades are pinned at BASE; nothing grades it again until the verb that owns it, and for a non-overridable it
2026-09-14 | class | a-new-leg-trips-a-growing-set-of-meta-gates | reviewed-before: - | adding one gate leg trips a set of meta-gates that grows as new ones land, and a check inside an existing gate is far cheaper — but not free
2026-10-02 | class | a-new-local-collides-in-a-long-function | reviewed-before: aHalvedInstall | a local added to a function thousands of lines long can share its name with one a distant block already binds, and the later binding silently replaces the new value only on the inputs that reach that block
2026-09-01 | class | a-pair-exists-and-it-is-the-wrong-one | reviewed-before: dMispairedQuote | a scanner that pairs a delimiter with the next one of its kind finds a pair for a delimiter that opens nothing, and the span it then blanks is where the defect hides
2026-10-11 | class | a-runner-knob-owes-a-push-class | reviewed-before: aPrimedIndex | a new GATE_ or GOV_ knob the gate runner reads has no push-boundary class until it joins one, and the arm that says so is guarded away from the unit that adds it
2026-09-30 | class | a-spelling-change-strands-its-readers | reviewed-before: aRepatriatedFork | a shared file changes how it SPELLS its values, the readers someone migrated resolve the new spelling, and every reader nobody listed compares the raw one and matches nothing
2026-09-05 | class | a-view-fix-trades-one-blindness-for-another | reviewed-before: aWeldedTribunal | a scanner that grades source through a rendered view has a blind spot, and building a better view moves it rather than closing it, each move a new fail-open or false-deny
2026-09-06 | class | ab-arm-never-did-the-work | reviewed-before: aQuenchedHarness | a timing A/B whose arms are not each asserted to have DONE the work measures a refusal against a run, and the fast arm looks like the good one
2026-08-08 | class | absence-assertion-over-whole-file-text | reviewed-before: aBatchedLintel | a ban that greps whole file text reds on the comment documenting its own fix
2026-10-12 | class | allocation-knob-without-a-ceiling | reviewed-before: aPairedSlots | a knob that sizes an allocation or a loop, validated only as a positive integer, hangs the process on a mistyped value before anything it guards runs
2026-08-20 | class | allowlist-narrower-than-the-root-it-guards | reviewed-before: aTetheredScratch | a guard keyed on a path prefix denies the sanctioned destination too, because on this platform the sanctioned destination is INSIDE the prefix
2026-08-27 | class | amendment-leaves-its-other-half-standing | reviewed-before: dTieredTribunal | a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts
2026-09-28 | class | anchor-literal-resolves-above-its-target | reviewed-before: dHashedPrelude | a check that locates code by searching its own source for a literal finds an earlier occurrence inside a docstring or a string constant, so the comparison it anchors is made against the wrong place and reds on a correct file
2026-08-21 | class | arm-literal-strands-on-message-edit | reviewed-before: - | editing a fail message strands its arm silently — the branch stays armed-looking, the count drops by one, and only the arms gate notices
2026-08-16 | class | armed-but-unreachable-rule | reviewed-before: - | a declaration can be non-empty, well-formed and still impossible to violate — testing that a rule EXISTS is not testing that it can FIRE
2026-08-10 | class | assertion-between-two-derived-values | reviewed-before: - | a check comparing two values the same code derives from one source is a tautology, and it arms cleanly
2026-09-13 | class | async-job-starts-with-sigint-ignored | reviewed-before: - | a job a non-interactive shell starts with `&` has SIGINT ignored, bash cannot trap a signal it started with ignored, so an INT sent to it, or to anything it starts, is silently dropped
2026-09-14 | class | bash-c-multiline-flattens-under-msys | reviewed-before: aReplayedCard | a multi-line script handed to `bash -c` from a Windows python re-parses as one line under the MSYS layer, and a backslashed `C:\` path handed to MSYS bash loses its separators, so a probe that works in a shell fails from a subprocess with an error naming neith
2026-10-12 | class | beacon-published-before-it-is-complete | reviewed-before: aPairedSlots | a lock or presence directory made visible before the files that let others judge it leaks forever when its writer dies in between, because every sweep needs those files
2026-09-20 | class | borrowed-seed-inherits-its-head-state | reviewed-before: aWokenSentinel | a fixture built from another suite's seed inherits that seed's HEAD state, and a probe that reads HEAD is dead on an unborn one
2026-08-20 | class | bounded-through-a-pipe-is-unbounded | reviewed-before: - | a wall-clock timeout captured through a command substitution bounds the verdict and not the clock, and reports success on schedule while the caller blocks
2026-10-05 | invariant | canary-waits-on-a-rendezvous-not-a-clock | reviewed-before: aPacedTurnstile,cSteadyMetronome | the run-gates canary never compares elapsed times, and that is the ruling, not a gap
2026-09-14 | class | check-format-grades-two-populations | reviewed-before: dHonouredPark | the build README slot gate binds every tracked README on one axis and only the declared ones on the other, so a new folder can red on a rule its author never opted into
2026-08-08 | class | concurrency-is-not-a-budget | reviewed-before: - | a per-item verify fan-out passes a concurrency cap and still spawns one agent per finding
2026-10-05 | invariant | concurrent-runs-are-announced-not-refused | reviewed-before: aDeferredBar,aGraftedHelix,aUnblockedFleet | two live unattended runs of different builds are announced at preflight and never refused, and that is the ruling, not a gap
2026-09-14 | class | conf-value-interpolated-into-a-regex | reviewed-before: aDeclaredBound | a config value spliced into a regex must be VALIDATED as a plain path, not escaped — a quoted value matches nothing and a value with a pipe swallows a subtree, both silently
2026-08-21 | class | containment-tested-one-way | reviewed-before: - | a guard asking only "is this path under the protected one" refuses the narrow declarations and admits the one that claims everything
2026-09-05 | class | criterion-asserts-what-its-own-command-cannot-show | reviewed-before: aJoinedCanon,aLoosenedCeiling | an acceptance criterion names a command and then asserts a figure that command never prints, a field nothing the change moves, a state that holds when the scope item is skipped, or an absence its own records break by quoting the pattern
2026-09-24 | class | decision-re-derived-by-a-second-process | reviewed-before: aRepatriatedFork | a second process that re-derives a decision the first one already acted on, from its OWN inputs, answers a different question whenever those inputs differ, and the gap is exactly where an attacker stands
2026-08-26 | class | degradation-known-but-unreported | reviewed-before: dTieredTribunal | a pipeline computes how badly its own run degraded and then fails to say so where it matters, so a degraded run produces a clean bill
2026-09-20 | class | destructive-step-before-its-precondition | reviewed-before: aBranchedMandate,aWokenSentinel | a destructive step ordered before the probe for the precondition that makes it useful runs on exactly the case where nothing can follow it, so the harm lands and the benefit never does
2026-09-07 | class | empty-field-collapses-unless-it-is-last | reviewed-before: - | `IFS=$'\t' read -r a b c d` collapses a run of tabs because tab is IFS whitespace, so a field that can be empty silently shifts every field after it and the branch reading them is dead
2026-08-23 | class | fallback-fabricates-the-passing-value | reviewed-before: dScriptedRepeat | a degraded-mode substitute spelled with the value some assertion reads as clean turns a broken subject into a silent green
2026-09-13 | class | fixed-sleep-does-not-place-a-signal | reviewed-before: - | a test that sleeps a fixed time and then signals assumes the child it means to interrupt is already running; under load the signal lands before that child exists or after it ended
2026-08-19 | class | fixture-inherits-ambient-machine-state | reviewed-before: - | a hermetic-looking fixture silently reads machine-global config, so it passes everywhere it was written and fails where it was not
2026-09-13 | class | fixture-lacks-a-gate-the-consumer-has | reviewed-before: dPolishedVitrine | a runbook's fixture passes because it lacks a commit-time gate the consumer runs, and the consumer refuses the step the fixture let through
2026-08-08 | class | fixture-passes-by-finding-nothing | reviewed-before: - | a test arm whose fixture never triggers the rule passes, and proves nothing
2026-09-07 | class | fixture-removes-the-path-under-test | reviewed-before: aQuenchedHarness | a fixture stabilised by DELETING a dependency stops the branch under test from executing, so both A/B arms run the other code twice and agree
2026-10-12 | class | floor-left-below-the-arms-it-guards | reviewed-before: aPairedSlots | a suite's assertion floor not raised when arms land leaves those arms stranded, so deleting them keeps the suite green
2026-08-26 | class | fold-text-is-unreviewed-surface | reviewed-before: dFramedEntrypoint,dTieredTribunal | a review round's fixes are folded into fresh prose nobody has reviewed, and that prose is where the next round's findings are
2026-09-08 | class | format-derived-from-arity | reviewed-before: aQuenchedHarness | a producer that picks its output FORMAT from the number of items has two shapes, and a consumer written against the many-item one reads the single-item case as empty
2026-08-08 | class | gate-green-by-accident-on-generated-bytes | reviewed-before: - | a byte-compare gate over a generated file is CRLF-red on Windows and green only right after a render
2026-09-14 | class | git-rm-cached-refuses-a-diverged-index-blob | reviewed-before: aReplayedCard | `git rm --cached` refuses a path whose index blob differs from both HEAD and the worktree, so a fixture cleanup without `-f` silently leaves the file staged and the next arm measures the wrong fixture
2026-08-08 | class | grammar-bound-to-the-wrong-root | reviewed-before: - | a module-level grammar resolved at import describes the repo the KIT lives in, not the tree being classified
2026-09-21 | class | guard-above-a-fold-makes-its-fallback-dead | reviewed-before: cMendedVintage | a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage
2026-09-21 | class | guard-fed-the-value-it-supersedes | reviewed-before: aWokenSentinel | a guard on a relaunch reads only the pid the launch it guards was meant to replace, so the process the launch itself created is invisible to the next launch and the guard never sees the duplicate it exists to stop
2026-09-16 | class | hand-named-gate-list-green-while-the-bar-reds | reviewed-before: aBranchedMandate,aProbedUnit,dBackdatedFixture,dPromptedSeam,dSealedTally | a spec names the legs its author expects the change to move, the unit is green on exactly those, and the bar is red on an unguarded leg the list never named
2026-10-13 | class | held-suite-guard-misses-a-sibling-kit | reviewed-before: aHeardState | a held self-test reads another kit's file, but its leg's guard names only its own kit, so an edit to the sibling skips the leg or reuses its stale green
2026-08-08 | class | heredoc-escape-reaches-the-regex | reviewed-before: - | source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem
2026-10-10 | class | history-leg-graded-before-the-reconcile-commit | reviewed-before: aRoutedQuill | a history-wide leg graded before the reconcile commit is graded on the wrong history, because the merge adds commits to the population without touching a file the fix touched
2026-08-24 | class | hookspath-resolves-into-another-checkout | reviewed-before: dUnstalledConvoy | an ABSOLUTE core.hooksPath makes every worktree it governs run the hook files of the one checkout it names, so a push is gated by whatever that checkout happens to have checked out
2026-08-21 | class | id-matched-as-a-substring | reviewed-before: dUnstalledConvoy | every id ending in a 1-up sequence is a prefix of nine others, so an unanchored match joins the wrong record
2026-10-09 | class | index-derivation-reads-a-half-staged-move-as-a-deletion | reviewed-before: cSteadyMetronome,dHomedResolver | a derivation over git ls-files reads a move whose destination is not yet staged as a deletion, and a writer driven by it renders that deletion into every file citing what moved
2026-10-05 | class | inherited-git-dir-pins-the-work-tree-to-the-cwd | reviewed-before: aCandidStub,aCollapsedScan,aGraftedHelix,aPacedTurnstile,aRepatriatedFork,aSealedCaravan,dRetiredFork,dScrubbedConduit | with GIT_DIR set and no GIT_WORK_TREE, git takes the current directory for the work tree's top, so a `git -C <dir>` probe answers about <dir> as if it were the root; git exports GIT_DIR into a linked worktree's hooks, so a location probe that passed in a shell
2026-09-05 | class | inline-fence-swallows-the-rest-of-the-file | reviewed-before: - | a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view
2026-09-13 | class | inline-marker-breaks-a-line-continuation | reviewed-before: - | appending a per-line annotation to the lines a gate selected breaks any of them that ended in a backslash, and the result is valid shell that silently drops the rest of the command
2026-08-14 | class | inputs-inside-the-subjects-reach | reviewed-before: - | a check whose inputs are all supplied by the thing it distrusts is not a check, however sound its logic
2026-10-12 | class | invariant-held-on-one-admission-path | reviewed-before: aPairedSlots | an invariant one admission path enforces is silently absent on every other path into the same resource, and the spec that states it reads as covering them all
2026-09-14 | class | join-key-widened-by-a-shared-location | reviewed-before: dLoggedFlight | a join keyed on WHERE something happened takes every place the subject ever touched, and one of those places is shared by every subject, so the key admits everyone's lines
2026-09-14 | class | ledger-token-wrapped-across-a-line-joins-nothing | reviewed-before: aReplayedCard | hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered
2026-10-10 | class | line-claim-matched-over-the-whole-output | reviewed-before: aBenchedProbe | an arm that asserts a line names X tests two substrings over the whole output, so it passes when X appears on some other line and the line it means names something else
2026-09-21 | class | line-count-reads-empty-capture-as-one | reviewed-before: aWokenSentinel | a line count over a captured variable that adds a newline before counting reads an EMPTY capture as one line, so a one-line assertion cannot fail on a command that wrote nothing
2026-09-06 | class | line-keyed-registry-reds-on-a-file-that-grew | reviewed-before: dHonouredPark,dTracedLattice | a waiver keyed <path>:<line> stops matching when anything is inserted above it, so a gate reds on a file whose waived line nobody touched
2026-10-04 | class | liveness-negative-from-another-population | reviewed-before: dUnstuckLanding | a probe is shown able to read negative on inputs it will never act on, while over its real population a positive is structural, so the liveness assertion passes and certifies nothing
2026-09-21 | class | merge-keeps-both-sides-of-one-derivation | reviewed-before: cMendedVintage | a conflict-free merge leaves two derivations of one value, disagreeing, and the first is a dead store
2026-09-14 | class | msys-grep-counts-cr-on-every-line | reviewed-before: aReplayedCard | on an MSYS node `grep -c $'\r'` matches every line of an LF-only file, so a CR probe reports the whole file as CRLF and a clean tree as dirty
2026-10-09 | class | name-search-resolves-a-namesake | reviewed-before: dHomedResolver | a resolver that SEARCHES for a file by name where the file's location is declared admits every file sharing the name, and its finding then blames the subject for a collision it did not cause
2026-09-06 | class | naming-leg-grades-what-python-named | reviewed-before: - | the naming gate grades nested helpers and dunder methods, and its armed set follows symbols.json, so a new file reds on a later unrelated commit and only at the lander
2026-09-14 | class | node-check-is-not-a-syntax-gate | reviewed-before: - | node --check exits 0 on a file whose parse fails, because module auto-detection retries the parse and swallows the failure, so a gate built on it cannot go red
2026-09-13 | class | nt-against-a-missing-file-is-true | reviewed-before: - | a -nt b is TRUE when b does not exist, so a has-it-changed test against a stamp nobody wrote yet reports a change on the very first call
2026-09-14 | class | observation-before-the-last-fold-of-the-same-commit | reviewed-before: aDeferredBar | an acceptance observation taken before the last fold of the same commit is an observation of nothing, because the tree it saw is one the commit never held
2026-10-01 | class | observed-by-claim-no-arm-discharges | reviewed-before: aSightedSkeptic | a spec scope item says a behaviour is "Observed by ACn", the arm that criterion names never reads the surface the behaviour renders on, and a staged break of the behaviour leaves the suite green
2026-09-01 | class | one-value-field-records-a-mixed-outcome | reviewed-before: dFoldedVerdict,dMispairedQuote | a per-subject field holding ONE value has to record an outcome that was mixed — take the value that DEMANDS something, never the one that demands nothing
2026-10-05 | class | orchestrator-hand-off-owed-a-disposition | reviewed-before: aGraftedHelix | a spec that hands a discovery to "this run's orchestrator" names a recipient the run tracks nowhere, so the discovery is dropped silently unless the close checks every such line resolves to a unit or a parked row
2026-10-12 | class | overlap-judged-from-the-invocation-interval | reviewed-before: aPairedSlots | a guard that two jobs ran at once, timed around the commands that started them, includes their queue wait, so a pair the scheduler serialized still overlaps
2026-08-08 | class | pin-copied-from-another-corpus | reviewed-before: - | a threshold measured on one tree is vacuous or permanently red on another
2026-09-14 | class | pin-gated-checks-arm-nothing-without-a-pin | reviewed-before: - | hygiene checks 13-15 alone are behind a declared pin, so a fixture conf without one arms nothing there and the checks report clean by never loading
2026-09-30 | class | porcelain-diff-names-a-rename-by-its-destination | reviewed-before: dAlignedCarrier | a touched-set read built on porcelain `git diff --name-only` names a renamed file by its destination alone, so a prefix match misses a file moved OUT of the prefix
2026-10-12 | class | predicate-bounded-by-its-own-count | reviewed-before: aPairedSlots | a predicate about other processes' holdings that walks only up to this process's own configured count misses a neighbour configured higher
2026-08-23 | class | process-creation-is-the-suite-cost | reviewed-before: - | a shell suite that is 93% not-CPU is paying an on-access antivirus scanner per exec, so its cost is spawn count and nothing in the code reads that way
2026-09-05 | class | record-citing-a-foreign-id-defines-or-orphans-it | reviewed-before: - | writing another build's id into a record either DEFINES it or ORPHANS it, and the orphan count sees only one of those, so the obvious check passes on the worse half
2026-10-12 | class | record-file-read-by-line-position | reviewed-before: aPairedSlots | a key-TAB-value record file read by its first line takes whatever key the writer put first, and a TAB inside that value shifts every column after it in the row that copies it
2026-09-14 | class | record-without-serves-or-with-a-round-counter | reviewed-before: - | a new build record owes a Serves line and a filename that projects it, and a round counter in that filename mints an id nothing defines
2026-09-14 | class | reflowed-prompt-string-reads-as-a-deleted-stop | reviewed-before: aReplayedCard | check 12 of the unattended gate greps the kickoff engine's READY prompt string as one fixed string on one physical line, so a reflow that wraps it at the house width reads as the READY stop having been deleted
2026-09-20 | class | retirement-inventory-misses-readers-by-value | reviewed-before: dLoggedFlight | an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing
2026-09-14 | class | row-driver-emits-a-plausible-file-with-rows-missing | reviewed-before: dDerivedDocket | the backlog row driver never errors on a wrong input order or a two-sided rotation — it emits a well-formed shard with the other side's rows silently gone
2026-08-11 | class | second-implementation-is-not-a-second-opinion | reviewed-before: - | a gate that recomputes the driver's answer from the driver's inputs confirms it rather than checking it, and the same hole opens at the READ path
2026-09-14 | class | settings-edit-takes-effect-mid-session | reviewed-before: - | an edit to the hooks settings file is live on the next tool call, not at the next session, so a throwaway hook fires on the call that checks for it
2026-09-14 | class | shipped-checker-edit-is-an-adopter-contract-change | reviewed-before: - | the manifest checker in this repo is the copy every adopter installs, so an edit made for this repo's own kickoff changes what every adopter's gate demands on their next pull
2026-10-11 | class | signal-killed-hook-reads-as-success | reviewed-before: aRoutedQuill,aSignalledHook,aSurfacedLexicon | on Git for Windows a git hook that dies by a signal is read by git as exit 0, so an untrapped TERM, HUP or INT, a KILL or a TerminateProcess lands a push the hook was about to refuse
2026-09-13 | class | signal-trap-runs-the-exit-handler-twice | reviewed-before: dLoggedFlight | a signal trap that calls the exit handler and then exits runs that handler twice, because the exit fires the EXIT trap too, so anything the handler appends is appended twice
2026-09-14 | class | sourced-conf-blank-overrides-the-default | reviewed-before: aDeclaredBound | an engine that presets its keys and then SOURCES the conf over them lets a blank line override a default with blank, and blank is what every measured pin uses to mean skip
2026-08-21 | class | spec-names-code-its-base-lacks | reviewed-before: dUnstalledConvoy | a spec written from review records instead of from the code names machinery a commit ancestral to its own base already deleted
2026-09-14 | class | staged-break-runs-stale-bytecode | reviewed-before: dLoggedFlight | a harness that edits a Python module and re-runs its arm can execute the previous edit's cached bytecode, because two same-size edits inside one second pass the cache's check
2026-08-23 | class | staged-break-substitutes-a-synthetic-value | reviewed-before: dScriptedRepeat | an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value
2026-08-21 | class | status-set-in-a-subshell | reviewed-before: - | a gate that prints FAILED from inside a pipeline sets a status the parent never sees, so it reports the violation and exits 0
2026-08-23 | class | structured-record-split-on-whitespace | reviewed-before: dScriptedRepeat | a multi-field record iterated with an unquoted shell expansion degenerates into its first field, and every assertion built on the later fields becomes unfalsifiable
2026-08-08 | class | subprocess-resolves-a-different-shell | reviewed-before: - | Python subprocess resolving the bare name bash finds the WSL launcher, which sees another filesystem
2026-09-14 | class | suite-edited-while-bash-executes-it | reviewed-before: aReplayedCard | bash reads a script incrementally by byte offset, so editing a suite file while a long run of it is executing corrupts the parse at the old offset and the run dies with a syntax error that names no edit
2026-09-07 | class | suite-invalidated-by-a-commit-under-it | reviewed-before: - | a suite that pins gov's revision at import and stamps fixtures from live HEAD is silently invalidated by any commit made while it runs, and the failures name the product
2026-09-11 | class | swallowed-delegate-reads-as-clean | reviewed-before: - | a gate that discards its delegate's exit status reads a delegate that never ran as a clean population
2026-10-05 | invariant | sweep-issues-no-cost-verdict | reviewed-before: aPooledSweep | the self-test sweep never grades a suite's wall clock against its budget, and that is the ruling, not a gap
2026-10-12 | class | test-oracle-read-from-a-historical-sha | reviewed-before: aOrientedCast | a test compares its subject with a copy read out of git at a literal sha, so every later legitimate edit of the subject reds it and the fix is always "move the sha"
2026-08-25 | class | text-mode-read-eats-a-bare-cr | reviewed-before: dHonouredPark | reading a CRLF worktree file in text mode turns a bare CR inside a regex into a newline
2026-08-23 | class | trace-profile-measures-itself | reviewed-before: - | a per-line set -x profile charges its own write overhead to the next line, so its seconds rank by call count and an optimisation aimed at them moves nothing
2026-08-11 | class | trailing-comma-counted-as-an-element | reviewed-before: aNumeralWarden | a counter scoring one-plus-every-top-level-comma reads a trailing comma as a real item, so every multi-line literal measures one too many
2026-09-13 | class | trapped-signal-waits-for-the-foreground-child | reviewed-before: - | a bash script that TRAPS TERM, HUP or INT runs the handler only after its foreground child returns, so a killed script outlives the kill for as long as that child runs
2026-08-08 | class | two-answers-to-one-question | reviewed-before: - | a fact stated in two places drifts, and the copies need not disagree loudly to be wrong
2026-08-24 | class | two-guards-one-question-two-answers | reviewed-before: dUnstalledConvoy | two guards that ask one question different ways become jointly unsatisfiable, and the tree they wedge has no legal move left
2026-08-23 | class | two-readers-of-one-config-one-re-derived | reviewed-before: dScriptedRepeat | one reader of a config file re-parses what the others source, so a legal spelling gives the guard a value nothing can match while it reports itself armed
2026-08-08 | class | vacuous-selector-empty-population | reviewed-before: - | a path selector that matches nothing prints nothing, and nothing is what a passing check prints
2026-10-11 | class | verdict-printed-before-the-step-that-reverts-it | reviewed-before: dRemeasuredRender | a verb prints a verdict about bytes it just wrote, and a later step of the same run can revert those bytes, so the operator reads a verdict about a tree the run did not leave
2026-09-14 | class | waiver-row-that-hides-nothing-reds | reviewed-before: cGradedDebt,dDerivedDocket | a curation-debt row whose file would pass unwaived is itself a failure, and check 8's population is the backlog shards alone — so a row listed for a fault it does not earn reds instead of protecting
2026-09-14 | class | withheld-value-recovered-from-a-derived-one | reviewed-before: dLoggedFlight | a schema withholds a value by name and still publishes one derived from it, so a reader recovers the withheld value from the rendered one by arithmetic
2026-09-21 | class | witness-graded-against-a-fact-written-after-it | reviewed-before: aWokenSentinel | a sidecar line that outlives the lease it was written under is graded against the id the new lease replaced, so a dead incarnation's witness passes the check the live one owes
2026-09-14 | class | worktree-crlf-outside-the-gated-population | reviewed-before: - | a worktree checkout lands CRLF on eol-pinned files, no wiring gate sees it, and the reader that breaks is a consumer no gate byte-compares
```

## `gotchas.py`

```python
"""Each gotcha: its add date (git), its kind, the builds its body names, and whether any of those
builds holds a review report dated on or before the add date. Read-only. Usage: python gotchas.py <repo>"""
import os, re, sys, glob, subprocess
repo = sys.argv[1]
def git(*a): return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, encoding="utf-8").stdout
builds = {os.path.basename(p) for p in glob.glob(os.path.join(repo, "memory/builds/*")) if os.path.isdir(p)}
reviews = {}
for p in glob.glob(os.path.join(repo, "memory/builds/*/reviews/*.md")):
    b = p.replace("\\", "/").split("/builds/")[1].split("/")[0]
    reviews.setdefault(b, []).append(os.path.basename(p)[:10])
rows = []
for f in sorted(glob.glob(os.path.join(repo, "memory/gotchas/*.md"))):
    if f.endswith("INDEX.md"): continue
    rel = os.path.relpath(f, repo).replace("\\", "/")
    added = git("log", "--diff-filter=A", "--follow", "--format=%as", "--", rel).split()
    added = added[-1] if added else "?"
    t = open(f, encoding="utf-8").read()
    kind = (re.search(r"^kind:\s*(\S+)", t, re.M) or [None, "?"])[1]
    desc = (re.search(r"^description:\s*(.+)$", t, re.M) or [None, ""])[1]
    named = sorted({m for m in re.findall(r"\b[A-Z]{3,4}-([a-d][A-Z][a-z]+[A-Z][a-z]+)-\d+", t) if m in builds} |
                   {m for m in re.findall(r"\b([a-d][A-Z][a-z]+[A-Z][a-z]+)\b", t) if m in builds})
    rev = [b for b in named if any(d <= added for d in reviews.get(b, []))]
    rows.append((os.path.basename(f)[:-3], added, kind, named, rev, desc))
n = len(rows); withrev = sum(1 for r in rows if r[4])
print(f"gotchas {n}; naming a build {sum(1 for r in rows if r[3])}; naming a build reviewed on or before the gotcha was added {withrev}")
for r in rows:
    print(f"{r[1]} | {r[2]} | {r[0]} | reviewed-before: {','.join(r[4]) or '-'} | {r[5][:260]}")
```

## `lens_yield.py`

```python
"""Per-lens yield over every review report under memory/builds/*/reviews/ that carries
an '## Appendix' finding table. Read-only. Usage: python lens_yield.py <repo>"""
import os, re, sys, glob, collections
repo = sys.argv[1]
SEV = ["blocker", "high", "medium", "low"]
files = sorted(glob.glob(os.path.join(repo, "memory/builds/*/reviews/*.md")))
cov = collections.Counter(); rows = []
for f in files:
    t = open(f, encoding="utf-8", newline="").read()
    m = re.search(r"^\*\*Serves:\*\* ([a-z-]+)", "\n".join(t.splitlines()[:12]), re.M)
    kind = m.group(1) if m else "?"
    cov[(kind, "all")] += 1
    if "\n## Appendix" not in t:
        continue
    tail = t.split("\n## Appendix", 1)[1]
    hdr = next((l for l in tail.splitlines() if l.startswith("| id |")), None)
    if not hdr:
        cov[(kind, "appendix-unparsed")] += 1; continue
    cov[(kind, "appendix")] += 1
    build = f.replace("\\", "/").split("/builds/")[1].split("/")[0]
    n = 0
    for l in tail.splitlines():
        if not re.match(r"^\| \d+ \|", l): continue
        c = [x.strip() for x in l.strip().strip("|").split(" | ")]
        fid, lens, ref, sev, ssev, verdict = c[:6]
        rows.append(dict(f=f, build=build, kind=kind, lens=lens, sev=(ssev or sev).lower(), fsev=sev.lower(), verdict=verdict.lower()))
        n += 1
    if n == 0: cov[(kind, "appendix-empty")] += 1
print("== coverage (reports)")
for k in sorted(cov): print(f"  {k[0]:12s} {k[1]:18s} {cov[k]}")
print(f"== finding rows parsed: {len(rows)}")
bad = [r for r in rows if r['verdict'] not in ('confirmed','refuted','uncertain','unverified')]
print(f"   rows with an unknown verdict token: {len(bad)}", collections.Counter(r['verdict'] for r in bad).most_common(5))
def table(sel, title):
    print(f"\n== {title}")
    print("| lens | reports | raw | confirmed | refuted | uncertain | unverified | precision | blocker | high | medium | low | high+blocker share of confirmed |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    by = collections.defaultdict(list)
    for r in sel: by[r['lens']].append(r)
    tot = []
    for lens in sorted(by, key=lambda k: -len(by[k])):
        rs = by[lens]; tot += rs
        print(line(lens, rs))
    print(line("ALL", tot))
def line(lens, rs):
    v = collections.Counter(r['verdict'] for r in rs)
    conf = [r for r in rs if r['verdict'] == 'confirmed']
    s = collections.Counter(r['sev'] for r in conf)
    p = v['confirmed'] / (v['confirmed'] + v['refuted']) if (v['confirmed'] + v['refuted']) else float('nan')
    hb = (s['blocker'] + s['high']) / len(conf) if conf else float('nan')
    reps = len({r['f'] for r in rs})
    return f"| {lens} | {reps} | {len(rs)} | {v['confirmed']} | {v['refuted']} | {v['uncertain']} | {v['unverified']} | {p:.2f} | {s['blocker']} | {s['high']} | {s['medium']} | {s['low']} | {hb:.2f} |"
table([r for r in rows if r['kind']=='spec-audit'], "spec-audit, every appendix")
table([r for r in rows if r['kind']=='spec-audit' and r['build']!='dClosedLoop'], "spec-audit, unit specs only (dClosedLoop excluded)")
table([r for r in rows if r['kind']=='spec-audit' and r['build']=='dClosedLoop'], "spec-audit, dClosedLoop design records only")
table([r for r in rows if r['kind']=='diff-review'], "diff-review, every appendix")
print("\n== reports per build with an appendix")
print(collections.Counter((r['kind'], r['build']) for r in {(r['f'],): r for r in rows}.values()).most_common())
```

## `shapes/run.py`

```python
import json, subprocess, sys, glob, os
hook = sys.argv[1]
for f in sorted(glob.glob("s*.js")):
    src = open(f, encoding="utf-8").read()
    payload = json.dumps({"tool_name": "Workflow", "tool_input": {"script": src}, "session_id": "probe", "prompt_id": "probe", "tool_use_id": "probe", "cwd": os.getcwd(), "hook_event_name": "PreToolUse"})
    p = subprocess.run(["node", hook], input=payload, capture_output=True, text=True, encoding="utf-8")
    out = (p.stdout + p.stderr).strip().replace("\n", " ")
    print(f"{f}: rc {p.returncode} :: {out[:420] or '(no output: admitted)'}")
```

## `shapes/s1-three-presets.js`

```javascript
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap) out.push(...(await Promise.all(thunks.slice(i, i + cap).map((t) => t())))) // gov:bounded-fanout
  return out
}
const a = args
const isSpec = a.kind === "spec-audit"
const isDesign = a.kind === "design-audit"
const A1 = { key: "a" }; const A2 = { key: "b" }; const A3 = { key: "c" }; const A4 = { key: "d" }; const A5 = { key: "e" }; const A6 = { key: "f" }; const A7 = { key: "g" }; const A8 = { key: "h" }
const SPEC_LENSES = [A1, A2, A3, A4, A5]
const DIFF_LENSES = [A1, A2, A3, A4, A5]
const DESIGN_LENSES = [A1, A6, A7, A8, A5]
const LENSES = isSpec ? SPEC_LENSES : isDesign ? DESIGN_LENSES : DIFF_LENSES // gov:fixed-verifiers
const res = await boundedParallel(LENSES.map((L) => () => agent("lens " + L.key, {})))
```

## `shapes/s2-swap-slot.js`

```javascript
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap) out.push(...(await Promise.all(thunks.slice(i, i + cap).map((t) => t())))) // gov:bounded-fanout
  return out
}
const a = args
const isSpec = a.kind === "spec-audit"
const isDesign = a.kind === "design-audit"
const A1 = { key: "a" }; const A2 = { key: "b" }; const A3 = { key: "c" }; const A4 = { key: "d" }; const A5 = { key: "e" }; const A6 = { key: "f" }; const A7 = { key: "g" }; const A8 = { key: "h" }
const SPEC_LENSES = [A1, A2, (a.optIn === "security" ? A6 : A3), A4, A5]
const LENSES = SPEC_LENSES // gov:fixed-verifiers
const res = await boundedParallel(LENSES.map((L) => () => agent("lens " + L.key, {})))
```

## `shapes/s2b-swap-slot-direct.js`

```javascript
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap) out.push(...(await Promise.all(thunks.slice(i, i + cap).map((t) => t())))) // gov:bounded-fanout
  return out
}
const a = args
const isSpec = a.kind === "spec-audit"
const isDesign = a.kind === "design-audit"
const A1 = { key: "a" }; const A2 = { key: "b" }; const A3 = { key: "c" }; const A4 = { key: "d" }; const A5 = { key: "e" }; const A6 = { key: "f" }; const A7 = { key: "g" }; const A8 = { key: "h" }
const SPEC_LENSES = [A1, A2, (a.optIn === "security" ? A6 : A3), A4, A5]
const res = await boundedParallel(SPEC_LENSES.map((L) => () => agent("lens " + L.key, {})))
```

## `shapes/s3-concat-optin.js`

```javascript
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap) out.push(...(await Promise.all(thunks.slice(i, i + cap).map((t) => t())))) // gov:bounded-fanout
  return out
}
const a = args
const isSpec = a.kind === "spec-audit"
const isDesign = a.kind === "design-audit"
const A1 = { key: "a" }; const A2 = { key: "b" }; const A3 = { key: "c" }; const A4 = { key: "d" }; const A5 = { key: "e" }; const A6 = { key: "f" }; const A7 = { key: "g" }; const A8 = { key: "h" }
const SPEC_LENSES = [A1, A2, A3, A4, A5]
const OPT = [A6, A7, A8]
const LENSES = SPEC_LENSES.concat(OPT.filter((L) => (a.optIn || []).includes(L.key))) // gov:fixed-verifiers
const res = await boundedParallel(LENSES.map((L) => () => agent("lens " + L.key, {})))
```

## `shapes/s4-catalogue-filter.js`

```javascript
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap) out.push(...(await Promise.all(thunks.slice(i, i + cap).map((t) => t())))) // gov:bounded-fanout
  return out
}
const a = args
const isSpec = a.kind === "spec-audit"
const isDesign = a.kind === "design-audit"
const A1 = { key: "a" }; const A2 = { key: "b" }; const A3 = { key: "c" }; const A4 = { key: "d" }; const A5 = { key: "e" }; const A6 = { key: "f" }; const A7 = { key: "g" }; const A8 = { key: "h" }
const ALL_LENSES = [A1, A2, A3, A4, A5, A6, A7, A8]
const LENSES = ALL_LENSES.filter((L) => (a.lenses || []).includes(L.key)).slice(0, 5) // gov:fixed-verifiers
const res = await boundedParallel(LENSES.map((L) => () => agent("lens " + L.key, {})))
```

## `shapes/s5-two-waves.js`

```javascript
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap) out.push(...(await Promise.all(thunks.slice(i, i + cap).map((t) => t())))) // gov:bounded-fanout
  return out
}
const a = args
const isSpec = a.kind === "spec-audit"
const isDesign = a.kind === "design-audit"
const A1 = { key: "a" }; const A2 = { key: "b" }; const A3 = { key: "c" }; const A4 = { key: "d" }; const A5 = { key: "e" }; const A6 = { key: "f" }; const A7 = { key: "g" }; const A8 = { key: "h" }
const SPEC_LENSES = [A1, A2, A3, A4, A5]
const OPT_LENSES = [A6, A7, A8]
const PASS2 = (a.optIn && a.optIn.length) ? OPT_LENSES.filter((L) => a.optIn.includes(L.key)) : [] // gov:fixed-verifiers
const LENSES = SPEC_LENSES // gov:fixed-verifiers
const res = await boundedParallel(LENSES.map((L) => () => agent("lens " + L.key, {})))
const res2 = await boundedParallel(PASS2.map((L) => () => agent("lens2 " + L.key, {})))
```

## `shapes/s6-opt-subset.js`

```javascript
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap) out.push(...(await Promise.all(thunks.slice(i, i + cap).map((t) => t())))) // gov:bounded-fanout
  return out
}
const a = args
const isSpec = a.kind === "spec-audit"
const isDesign = a.kind === "design-audit"
const A1 = { key: "a" }; const A2 = { key: "b" }; const A3 = { key: "c" }; const A4 = { key: "d" }; const A5 = { key: "e" }; const A6 = { key: "f" }; const A7 = { key: "g" }; const A8 = { key: "h" }
const OPT_LENSES = [A6, A7, A8, A1, A2]
const LENSES = (a.optIn && a.optIn.length) ? OPT_LENSES.filter((L) => a.optIn.includes(L.key)) : OPT_LENSES // gov:fixed-verifiers
const res = await boundedParallel(LENSES.map((L) => () => agent("lens " + L.key, {})))
```

## `sole_lens.py`

```python
"""For the runtime A/B: per lens, the defects (from the comparison record's [map]) on which it is the
ONLY lens with a confirmed finding across both rounds, and the highs among them. Read-only."""
import re, collections
cmp=open("build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md",encoding="utf-8").read().split("## [map]",1)[1].split("\n## ",1)[0]
rows={}
for r in "ab":
    t=open(f"reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-{r}.md",encoding="utf-8").read().split("## Appendix",1)[1]
    for l in t.splitlines():
        m=re.match(r"^\| (\d+) \|",l)
        if m:
            c=[x.strip() for x in l.strip().strip("|").split(" | ")]
            rows[(r.upper(),int(c[0]))]=(c[1],(c[4] or c[3]).lower(),c[5])
sole=collections.defaultdict(list); multi=collections.Counter(); per=collections.Counter()
for l in cmp.splitlines():
    if not l.startswith("| `"): continue
    c=[x.strip() for x in l.strip().strip("|").split(" | ")]
    lenses=set(); hi=False
    for r,cell in (("A",c[2]),("B",c[3])):
        for i in re.findall(r"\d+",cell):
            lens,sev,v=rows[(r,int(i))]
            if v=="confirmed": lenses.add(lens); hi|=sev in("high","blocker")
    for x in lenses: per[x]+=1
    if len(lenses)==1: sole[next(iter(lenses))].append(c[0].strip("`")+("*" if hi else ""))
    elif lenses: multi[len(lenses)]+=1
print("defects reached by k lenses (k>1):",dict(multi))
for k,v in sorted(sole.items(),key=lambda kv:-len(kv[1])): print(f"{k}: reaches {per[k]} defects; sole lens on {len(v)}: {', '.join(v)}")
print("(* = high on some confirmed finding)")
```

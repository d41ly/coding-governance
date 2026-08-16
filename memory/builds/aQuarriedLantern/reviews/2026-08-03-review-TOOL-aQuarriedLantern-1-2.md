# Closing review — TOOL-aQuarriedLantern (memory-recall port)

**Serves:** diff-review TOOL-aQuarriedLantern-1  <!-- inferred: this build defines exactly one spec id, so the record can serve nothing else -->

**Scope:** the cumulative diff landing on `main` for the memory-recall port — U1 (kit), U2 (invocation
surfaces), U3 (registrations) — 33 files, +5581/-40.
**Base:** 9368d1e8 · **Head:** 20f2337 (`f564109` spec, `aedf8e3` U1, `3e427de` manifest re-stamp,
`4d3eba5` U2, `f140b19` U3, `20f2337` gate-run note).
**Harness:** Tier-2 indexed, five primed lenses (adopter · silent-degradation · fidelity ·
wiring-integrity · contract) → batched default-refute skeptics keyed by orchestrator index → this
synthesis.
**Counts:** 17 raw findings · 14 confirmed · 3 refuted · **precision 0.82** · 0 no-verdict.
**Severity after skeptic correction:** 1 blocker · 1 high · 8 medium · 4 low.

Every confirmed finding below was reproduced by execution, not by reading — the skeptics built
throwaway adopter repos, ran the runbook verbatim, and mutated source to check that the gates could
see what they claim to see. Three of the fourteen (F2, F11, F12) share one root cause: no runbook
step ever delivers `tools/settings-merge.py` into an adopting project.

## Verdict

**PUSH AFTER FIXES.** The port's retrieval core is sound — the record/chunk/alias arms, the conf
resolution, the cache keying and the CLI's own diagnostics all behave correctly, and 18/18 selftest
checks pass in this repo. What fails is the *adoption* surface, which is the entire point of a
governance kit: a fixture guard in `tools/memory-recall/selftest.py` makes the kit's own mandated
gate leg exit 1 in every conformant adopter (F1), the hook opt-in prints a remedy that cannot run and
is watched by a verifier that skips instead of warning (F2, F11, F12), the runbook's step-2
verification is unsatisfiable on the fresh tree the runbook itself scaffolds (F3), and the Skill —
the kit's primary agent-facing surface — hardcodes a bare `python` launcher that is exit 127 on a
stock Debian adopter (F4). None of these are architectural; the blocker is a one-token fixture
rename and the rest are a delivery step, four doc/string edits and three gate arms. Fix F1 through
F5 before the push, take F6 through F14 in the same bookkeeping pass, and this lands clean.

### F1 — blocker — the kit's own mandated gate leg exits 1 in every conformant adopter

`tools/memory-recall/selftest.py:390` builds its fixture with `make_repo(kitname="memory-recall")`
and line 393 then asserts `here != kitdir.name`, where `here = KIT.relative_to(repo_root())`. In this
repo `here` is `tools/memory-recall`, so the guard passes. The runbook mandates the kit be copied to
the adopter as memory-recall/ — `WIRE-INTO-PROJECT.md:188-189` calls that "the fixed name the gate
legs and the wiring check resolve — don't rename" — so in an adopter `here` is exactly the fixture
name and the guard trips. `WIRE-INTO-PROJECT.md:205` mandates the selftest as a standing gate leg
and line 348 repeats it as a chain-verification step, so the adopter's merge bar is red the moment
they finish the runbook, with failure text ("fixture kit dir must not spell like this repo's") that
names an internal fixture concern they cannot act on.

Reproduced by cloning to a temp dir (green baseline: 18/18, exit 0), then `git mv tools/memory-recall
memory-recall` to reproduce the mandated layout and re-running: **17/18, exit 1**, with exactly that
assertion. Every other arm passed in the adopter layout, so this is a pure false red. A gate that is
green only in the repo that authored it is the third-shape defect this kit exists to prevent.

**Fix:** at `tools/memory-recall/selftest.py:390`, change `make_repo(kitname="memory-recall")` to a
name no adoption layout can mandate — e.g. `make_repo(kitname="mrecall-fixture-kit")` — and keep the
`here != kitdir.name` assertion, which then holds against both spellings. Then add an arm that runs
the selftest once from a fixture repo whose kit sits at the adopter's root-level memory-recall/
location, so the layout the runbook actually ships is on the merge bar.

### F2 — high — the hook opt-in's remedy is undeliverable, and the alarm meant to catch that skips

`WIRE-INTO-PROJECT.md:219-220` promises: "Copying the hook and skipping the merge is the one bad
state — it prints UNWIRED at every session start until you merge it." It never does. No runbook step
delivers `tools/settings-merge.py` into an adopter — the eight `cp` steps in the doc do not name it,
both invocations (lines 216, 327) use the `<gov>/tools/settings-merge.py` form run out of this
checkout, and the "Result — what the project now has" tree (lines 372-393) does not list it. So in a
conformant adopter two things break at once: `tools/memory-recall/adopt-memory-recall.sh:109` prints
a next-step command that dies with errno 2, and `tools/check-wiring.sh:105` takes its
`settings-merge.py absent, cannot verify` branch, prints `skip` and exits 0.

Reproduced end to end: `--scaffold --with-hook` installed the hook and printed the merge command;
running it verbatim gave `[Errno 2] No such file or directory`, exit 2. Then, in the exact state the
doc calls "the one bad state" (hook file present, settings.json absent), `check-wiring.sh` printed
`skip     recall    — settings-merge.py absent, cannot verify` and **EXIT=0**, in both `--check` and
`--session` form. The AC8 arm that should have caught this greens on a fabricated precondition:
`tools/check-wiring.test.sh:87` copies `settings-merge.py` into its fixture repo before asserting
state 3 UNWIRED — a gate proven at a precondition no runbook step creates, which is the
ARCH-dWaryGatepost-1 corollary this project already catalogs.

**Fix:** deliver the tool with the hook. Add `cp <gov>/tools/settings-merge.py <project>/tools/` to
WIRE §3c step 4 before the merge command, list it in the Result tree, and point both the WIRE command
and `tools/memory-recall/adopt-memory-recall.sh:109` at the project-relative path that then exists.
If the tool is deliberately governance-only instead, have line 109 print the `<gov>/tools/...` form
and have `tools/check-wiring.sh:105` print UNWIRED rather than `skip` when the hook file is present
but the verifier is absent — an unverifiable opt-in that was explicitly taken is not a skip. Extend
`t_printed_invocations_resolve` to fold the adopt script's `--with-hook` stdout into `seen`.

### F3 — medium — the runbook's step-2 verification is unsatisfiable on a fresh adoption

`WIRE-INTO-PROJECT.md:198-200` reads: "The header must report a **non-zero record count**. `index 0
records + N chunks` plus a `ZERO RECORDS` block on stderr means `FAMILIES` matches no id in the
corpus — fix the conf and re-run." That is a single-cause diagnosis, and it is wrong for the case the
runbook itself creates: §3 step 2 scaffolds discipline folders whose DECISIONS.md files are 90-96
bytes of header, and nothing between there and §3c step 2 writes a record. Line 348 repeats the same
unsatisfiable check as a §6 chain-verification step.

Reproduced by running the documented sequence in an isolated fresh repo: `index 0 records + 72
chunks` plus the ZERO RECORDS block, exit 0, with a *correct* conf whose FAMILIES resolved to exactly
the scaffolded disciplines. The shipped tool is right where the shipped runbook is wrong —
`tools/memory-recall/extract.py:259-261` prints the dual diagnosis, "Either no decision has been
written yet, or FAMILIES does not describe this corpus's ids." An adopter following the doc will
chase a nonexistent conf bug or edit a correct FAMILIES value. Spec AC1 scopes the non-zero-record
claim to this repo with a 9-record baseline; the runbook generalizes it where it does not hold.

**Fix:** reword `WIRE-INTO-PROJECT.md:198-200` to mirror the CLI's own dual diagnosis — zero records
on a fresh tree is expected and indicates a FAMILIES problem only when the corpus already contains
decision ids. Then make the step verifiable: add a line to §3c step 2 telling the adopter to write
one throwaway decision record carrying one of their own family ids and confirm the record arm anchors
it. Apply the same wording to the §6 bullet at line 348.

### F4 — medium — the rendered Skill hardcodes a bare `python`, exit 127 on a python3-only adopter

`tools/memory-recall/adopt-memory-recall.sh:76` substitutes `{{QUERY_CLI}}` with the literal `python
$REL/query.py`. That string lands in the Skill's `description` (`tools/memory-recall/SKILL.template.md:11`)
and in both code blocks, so every command the kit's primary agent-facing surface shows starts with a
launcher that a stock Debian/Ubuntu host without `python-is-python3` does not have. The kit already
knows this host is real and dangerous: the same script's header (lines 16-19) resolves python3-first
precisely because such an adopter "would red the whole gate suite", and `$PY` is computed at line 35
— then not used in the render. The failure is quiet: the Skill's own guidance says a miss is ordinary
and to fall back to Grep, so a 127 reads as "retrieval didn't help here."

Reproduced with a cut-down PATH holding git, bash and python3 but no `python` (isolated the way the
kit's own `t_python3_only` arm does it): the literal Skill command gave `bash: python: command not
found`, **exit 127**, while the runbook's `python3` form on the same PATH gave exit 0. No gate covers
it — `t_printed_invocations_resolve` checks that printed *paths* resolve, and
`t_skill_description_invariants` checks flags and banned tokens, neither the interpreter.

One correction to the filed rationale: "every other surface says python3" is false.
`tools/memory-recall/query.py:100` is `CLI = "python " + _self_path()`, so the CLI's own refusal text
and its `--opened` hand-back print bare `python` too. Fixing only the render leaves the Skill and the
tool it launches disagreeing.

**Fix:** render `python3` at `tools/memory-recall/adopt-memory-recall.sh:76`, and change
`tools/memory-recall/query.py:100` to match so both surfaces agree. Do **not** substitute the
resolved `$PY` — the Skill is committed and shared across a fleet, so baking one node's answer makes
`--check` red on nodes that resolve differently. Add an assertion to `t_skill_description_invariants`
that no `query.py` line in the rendered Skill is preceded by a bare `python` token.

### F5 — medium — the `--with-hook` remedy hardcodes a path the kit resolves everywhere else

`tools/memory-recall/adopt-memory-recall.sh:109` prints `$PY tools/settings-merge.py --fragment
$REL/recall-opened.fragment.json` — the fragment path goes through the resolved `$REL` while the tool
path is hardcoded, unlike `tools/check-wiring.sh:103` (which uses `first_of`) and
`WIRE-INTO-PROJECT.md:216` (which uses the `<gov>/` form). This is the last instruction an adopter
sees at the moment they take the opt-in, and it is the step whose omission leaves the hook inert.
Running it verbatim in an adopter: `[Errno 2] No such file or directory`, exit 2, with `ls tools/`
showing only `check-wiring.sh`.

The kit's own guard cannot see it: `tools/memory-recall/selftest.py:388-406` drives only `query.py`
(`--help`, a refusal, one answered query) and folds those three streams into `seen`, so a check whose
docstring is "every invocation the CLI prints resolves to a file that exists in the adopter" reports
"1 distinct printed path(s), all resolve" while the kit's other printed invocation does not.

**Fix:** print the same form F2 settles on, resolved rather than hardcoded, and extend
`t_printed_invocations_resolve` to run `adopt-memory-recall.sh --scaffold --with-hook` and fold its
stdout into `seen`. Without the gate arm the next path baked into a printed remedy repeats this.

### F6 — medium — the wiring verifier is blind to settings-wired-but-hook-missing

`tools/check-wiring.sh:99-102` returns on `[ ! -f .claude/hooks/recall-opened.js ]` before ever
consulting settings.json, so the state where settings.json dispatches the PostToolUse hook while the
script file is absent reports `skip recall — recall-opened hook opt-in not taken` — a false all-clear
on a genuinely half-installed kit that makes Claude Code invoke `node` against a missing file on
every Read.

Reproduced in a clone: running the single documented command from `WIRE-INTO-PROJECT.md:216` merged
happily (exit 0) and wrote the `node ".../recall-opened.js"` command into settings.json, while the
hooks directory still contained only `agent-cap.js`; re-running the verifier printed the same
opt-in-not-taken skip and did not increment `unwired`. The state is reachable from WIRE §3c step 4,
whose two commands are separate lines, and from any later loss of the untracked hook file. The
enumeration gap is explicit — the AC8 block in `tools/check-wiring.test.sh` is commented "all FOUR
states" and pins exactly four; this fifth is unpinned.

**Fix:** root-cause it once for every kit in `tools/settings-merge.py` — it already reads the
fragment's `hook_path` in `load_fragment` (line 63, used at line 270) — by refusing the merge when
that path does not exist. Then in the js-absent branch of `tools/check-wiring.sh`, run the
`--check --fragment` form first and print UNWIRED naming the missing script if it reports wired. Add
the fifth AC8 case.

### F7 — medium — an alias set that joins to zero records is reported nowhere by the CLI

`tools/memory-recall/query.py:264` is `E.join_aliases(records, E.load_aliases()[0])`, discarding the
int return that `tools/memory-recall/extract.py:226` declares and documents ("Returns how many were
augmented") and that `extract.py:457` prints as `aliases N records aliased (ids X, unresolved Y)`.
The CLI — the path every session actually uses — prints no equivalent, and `--stats` carries
`alias_digest` (a content hash used for cache keying) but no coverage count. An adopter authoring
alias data against the wrong id family gets a silently 100%-dead third FTS5 column whose only symptom
is slightly worse ranking.

Reproduced: baseline in a clean clone gave `index 12 records + 1088 chunks / 26 hits`; authoring a
correctly-shaped alias file with three ids from a foreign family produced byte-identical header and
hit count, exit 0, nothing on stderr. This is not the ratified "empty-alias is a first-class state"
item — that ratifies the *absent* case; this is present-but-zero-join, a distinct state. It is the
dead-plumbing class, and `query.py:258-263`'s own comment argues the identical principle one line
before violating it. Bounded: the alias column is a down-weighted ranking aid, so the record and
chunk arms are unaffected.

**Fix:** capture the return at `tools/memory-recall/query.py:264`, carry `aliased` and `alias_ids`
into the manifest at `build_cache`, and print a one-line diagnosis when `alias_ids > 0 and aliased ==
0` naming the alias path and the resolved FAMILIES — the same shape as the record-arm block.

### F8 — medium — the wiring verifier cannot resolve its own verifier in the adopter layout

`tools/check-wiring.sh:103` resolves `settings-merge.py` only at `tools/settings-merge.py` or the
repo root, neither of which exists in an adopter (F2's root cause), so the arm short-circuits at
lines 104-106 and the state the runbook calls "the one bad state" prints `skip … cannot verify` with
exit 0. Reproduced in a synthetic adopter built verbatim per WIRE §3c: `ok hooks`, `skip agent-cap`,
`skip recall — settings-merge.py absent, cannot verify`, **EXIT=0**, with the hook file present and
settings.json absent. All four AC8 states are pinned in this repo's layout, not the adopter's
(`tools/check-wiring.test.sh:90` copies the tool in first), so the cases can never see it. The same
blind spot pre-exists in the agent-cap arm at line 70; what is new with this port is the doc claim
that contradicts it.

Filed high, corrected to medium: the state that goes unreported is an opt-in telemetry hook silently
not recording opened-ranks, not a correctness or security surface, and nothing here gates a push. The
durable defects are the false doc claim and the untested adopter layout.

**Fix:** drop the python dependency for the wired signal — `tools/memory-recall/recall-opened.fragment.json`
already declares `marker`, so a `grep -qF "$marker" .claude/settings.json` is the whole test and
removes the skip state (verified in the adopter: it correctly reports UNWIRED). Keep the
`settings-merge.py --check` path for when it *is* resolvable, and add an AC8 case with no
`settings-merge.py` present asserting UNWIRED plus exit 1.

### F9 — medium — the kickoff Skill's recall probe hardcodes one spelling and misses this repo's kit

`skills/session-kickoff/SKILL.md:148` gates the Step-4 recall probe on "a memory-recall/ directory
with `query.py`" and line 150 gives the matching command, with line 154 as "No kit → skip (one
clause)." This repo keeps the kit at `tools/memory-recall/` and has no root-level directory of that
name, so the literal condition is false and the literal command is a wrong path in the very repo that
owns and dogfoods the kit. `.claude/SESSION-KICKOFF.md` declares no query path to compensate — it
names memory-recall only in the pointer-map row (line 43) and the gate-command comment (line 49).

It is also the third shape against the two sibling kits: `skills/session-kickoff/SKILL.md:142` uses a
manifest-supplied `<MAP_ROOT>` backed by the `{{CODEBASE_MAP}}` slot at
`skills/session-kickoff/MANIFEST-TEMPLATE.md:89`, and memory-tree is conf-driven; memory-recall alone
hardcodes. One honest qualification: the Skill is advisory prose read by a model, not a shell
predicate, so an agent may still glob and find the kit — the defect is the wrong, inconsistent
spelling, not a deterministic skip.

**Fix:** resolve both spellings in the clause and the command, matching `tools/check-wiring.sh:94`
(one line), or add a `{{MEMORY_RECALL}}` manifest slot beside `{{CODEBASE_MAP}}` and fill it in
`.claude/SESSION-KICKOFF.md`. Note the manifest ratchet watches `tools/gate-legs.json`, not the
Skill, so the clause edit alone does not re-open it.

### F10 — medium — extract.py's fork header undercounts its fork and cites the wrong provenance sha

`tools/memory-recall/extract.py:4-7` states the fork is "five constructs wide" and that "Everything
else is upstream's, byte for byte." There is a sixth: lines 42-46 add `sys.dont_write_bytecode =
True`, `import recall_conf` and `CONF = recall_conf.resolve()`, none of which exist upstream —
verified by grepping the source blob, which has zero occurrences of either. `tools/memory-recall/query.py:4-10`
enumerates the identical preamble correctly as its construct (2), so the two headers disagree.
Separately, line 4 claims the file "last changed fd6274d"; upstream `git log -1 5318064 --
scripts/recall/extract.py` returns 958bd35c3, and fd6274d never touched that file.

The header's stated purpose is "so a future re-pull is a three-way merge rather than archaeology."
`sys.dont_write_bytecode = True` is the one line of that preamble a re-pull can silently drop — the
other two are load-bearing (without CONF, `FAMILIES = CONF.families` is a NameError) — and it is the
whole of the kit's advertised "writes nothing inside your worktree" property on this file's own
documented entry point. Confirmed by mutation off a green 18/18 baseline in a clean clone (shell
probed as Msys first; the first attempt reported TARGET LINE NOT FOUND because the checkout is CRLF,
which would have scored a fake kill): deleting the line, asserting the bytes changed on disk, then
re-running the selftest gave **18/18 SURVIVED**, and running extract.py created a `__pycache__`
directory inside the worktree, hidden from `git status` by the `__pycache__/` ignore rule — exactly
the concealment the selftest's own `make_repo` docstring warns a status-based check cannot see. The
wrong sha is merge-harmless (both revisions point at the same blob) but false in a header whose only
job is provenance.

**Fix:** rewrite `tools/memory-recall/extract.py:4-7` to name six constructs, adding the
`sys.dont_write_bytecode` plus `recall_conf` preamble in the same words `query.py:5-10` uses, and
correct the sha to 958bd35c3. Then close the gate: in `t_zero_records_is_loud`, after the existing
direct `script="extract.py"` call, assert no `__pycache__` appears under the fixture. That assertion
was validated both directions — it reds under the mutation (17/18, "extract.py wrote bytecode") and
greens on reverted code.

### F11 — low — the ZERO RECORDS diagnosis is suppressed when the chunk arm is also empty

`tools/memory-recall/extract.py:255` opens with `if n_records or not n_chunks: return None`, so the
0-records-and-0-chunks state — which a one-character `MEMORY_ROOT` typo produces, and MEMORY_ROOT is
one of the three keys the adopter hand-edits — is structurally excluded from the loud diagnosis.
Reproduced in a clone off a green baseline (`index 12 records + 1088 chunks`, 24 hits): editing
MEMORY_ROOT to a nonexistent directory and asserting the file changed on disk gave `index 0 records +
0 chunks`, `0 hits`, exit 0, and no ZERO RECORDS block.

Filed high, corrected to **low**. The mechanism and the fix are real, but the load-bearing rhetoric
is not: this is not "total silence" and not "strictly worse than upstream." stdout leads with `index
0 records + 0 chunks` and follows with `0 hits`, extract.py under the same conf prints `corpus 0
files` as its first line, and `WIRE-INTO-PROJECT.md:198` tells the adopter the header must report a
non-zero record count, which 0 fails. The residual is only that no message *names* MEMORY_ROOT as the
suspect. Note the same 0+0 is the honest state of a fresh adopter with an empty tree — which is why
the record-arm diagnosis is a print, not a refusal. The spec citation is also weak: "empty corpus"
appears in the states list with no prescribed output, so this is not an unimplemented spec item.

**Fix:** split the guard — keep `if n_records: return None`, then add an `if not n_chunks:` branch
printing a distinct diagnosis naming MEMORY_ROOT as the prime suspect, reusing the same resolved-values
block. Add a selftest arm beside `t_zero_records_is_loud` pointing MEMORY_ROOT at a nonexistent
directory and asserting the diagnosis is non-empty.

### F12 — low — REL compares two independently-derived path spellings, so `--check` flips per cwd

`tools/memory-recall/adopt-memory-recall.sh:32` is `REL="${HERE#"$ROOT"/}"`, where HERE comes from
`pwd` after cd-ing to a possibly-relative `$0` (inheriting the caller's cwd spelling) and ROOT from
`pwd` after cd-ing to git's canonical path. When an MSYS mount alias makes those disagree the strip
no-ops, REL stays absolute, and it is interpolated into the Skill's description, the `{{QUERY_CLI}}`
block and the `--opened` example.

Verified both directions on the same clone at the same commit: from the `/c/Users/...` spelling,
`--check` printed "SKILL.md matches the conf" with EXIT=0; from the `/tmp/...` spelling of the
identical tree it printed "has DRIFTED" with a three-hunk diff and EXIT=1, the diff showing an
absolute machine-local `query.py` path. The `--check` direction is loud; the `--scaffold` direction
writes that committed artifact silently. The gate cannot see it — `adopt()` in the selftest invokes
bash with an absolute path from an absolute cwd, so both operands land on the same alias. Lines 27-29
already document and patch the git-vs-pwd half of exactly this class; this is the remaining half.
Honest precondition: it cannot trigger from this repo's canonical path.

**Fix:** let git compute the relative path so the two operands cannot disagree — `REL="$(cd "$HERE"
&& git rev-parse --show-prefix)"; REL="${REL%/}"` — and assert in `t_printed_invocations_resolve`
that REL is relative (`case "$REL" in /*|?:*) fail;; esac`).

### F13 — low — the `--terms` refusal ships another project's domain vocabulary as its worked example

`tools/memory-recall/query.py:163-165` prints, as the only worked example in the refusal that fires
on every invocation missing `--terms`, the question "why did the editor stop saving my page" with
terms including `puck_data` and `document_guard` — inCMS module names, carried verbatim from that
project's CLAUDE.md. This is the first message a new adopter sees, in a governance-template repo that
has no editor, no Puck and no such module.

The port already found and fixed the *path* half of this same string — `query.py:5-10` construct (3)
records that all three references "named a path that does not exist in an adopter repo" — and
correctly renders the CLI path. The content half was left. The spec's edit table lists the refusal's
fix as "derived from `__file__`", path only, so this is not a ratified keep. The two surfaces
disagree: `.claude/skills/memory-recall/SKILL.md:37-43` teaches term-writing generically with no
foreign example. Confirmed by running the CLI with no `--terms`: exit 2, block printed as quoted. A
repo-wide grep for the inCMS identifiers returns only these two lines, and for scripts/recall only
`tools/memory-recall/bench.py` lines 20 and 223, which `tools/memory-recall/README.md:122-126`
declares as a deliberate stated-not-patched deviation preserving wholesale re-pull. So this is the
last functional leftover.

**Fix:** replace the example at `tools/memory-recall/query.py:163-165` with a corpus-agnostic one —
e.g. a question about a build gate with terms described as "a family id, a module name, an error
code, a flag key, a filename" — which teaches the same lesson without naming another repo's
internals. Keep the measured recall figures; they are correctly attributed in the Skill.

### F14 — low — the spec Status header is still SPECCED with all three units built and gate-green

`memory/tooling/builds/2026-08-03-TOOL-aQuarriedLantern/spec/2026-08-03-spec-aQuarriedLantern-1.md`
line 3 reads `**Status:** SPECCED · rev-2 · 2026-08-03 · node a · Tier-2 · base 9368d1e8 · ratified
2026-08-03` while `aedf8e3`, `4d3eba5` and `f140b19` are in this diff and the ledger row in
`memory/project/in-flight/a.md` says "U3 landed; gates green". `memory/TEMPLATE-SPEC.md` defines
SPECCED as "complete, awaiting owner scope approval" and requires the header be updated in place on
every state change, so this was already stale three commits ago, not merely awaiting a pre-push flip.
Hygiene check 12 validates the header's *shape* only — confirmed live by mutation (a malformed header
reds it, exit 1) and confirmed blind to a stale token.

**Fix:** flip line 3 to **INPROGRESS** now, or to CLOSED only together with a §8 rewrite — check 12
rejects a terminal Status with unresolved §8 open questions unless the first non-empty line is
`none`/`N/A`, and this spec's §8 still carries unresolved Q1, Q4, Q5 and the deliberately-open Q6.
Update the ledger row to `merged:<sha>` in the same pre-push bookkeeping commit, per the Landing rule
that bookkeeping lands before `git push`.

## Unverified (no skeptic verdict)

None. Every one of the 17 raw findings received an explicit skeptic verdict; 14 confirmed, 3 refuted.
No finding fell through the index join, and the verdict count was reconciled against the finding
count before synthesis.

## Fix checklist

- [ ] F1 (blocker): rename the fixture kit dir at `tools/memory-recall/selftest.py:390` to a name no adoption layout can mandate, keep the `here != kitdir.name` assertion, and add a selftest run from a root-level adopter-layout fixture.
- [ ] F2 (high): deliver `tools/settings-merge.py` into the adopter (add the copy step to WIRE §3c step 4 and the Result tree), point the printed remedy at the path that then exists, or else make `tools/check-wiring.sh:105` print UNWIRED instead of `skip`; extend `t_printed_invocations_resolve` to cover the adopt script's `--with-hook` output.
- [ ] F3 (medium): reword `WIRE-INTO-PROJECT.md:198-200` and line 348 to the CLI's dual diagnosis, and seed §3c step 2 with one throwaway record so the step is satisfiable.
- [ ] F4 (medium): render `python3` at `tools/memory-recall/adopt-memory-recall.sh:76`, match it at `tools/memory-recall/query.py:100`, and assert no bare-`python` launcher in `t_skill_description_invariants`.
- [ ] F5 (medium): resolve the `settings-merge.py` path printed at `tools/memory-recall/adopt-memory-recall.sh:109`, and fold that script's `--with-hook` stdout into `t_printed_invocations_resolve`.
- [ ] F6 (medium): refuse the merge in `tools/settings-merge.py` when the fragment's `hook_path` is absent, make the js-absent branch of `tools/check-wiring.sh` consult settings.json, and pin the fifth AC8 state.
- [ ] F7 (medium): capture the `join_aliases` return at `tools/memory-recall/query.py:264`, carry the counts into the manifest, and diagnose a present-but-zero-join alias set.
- [ ] F8 (medium): switch the wired signal in `tools/check-wiring.sh` to a grep on the fragment's `marker`, keeping `--check` where resolvable, and add an AC8 case with no `settings-merge.py` present asserting UNWIRED plus exit 1.
- [ ] F9 (medium): resolve both kit spellings in `skills/session-kickoff/SKILL.md:148-150`, or add a `{{MEMORY_RECALL}}` manifest slot and fill it in `.claude/SESSION-KICKOFF.md`.
- [ ] F10 (medium): correct `tools/memory-recall/extract.py:4-7` to six constructs and sha 958bd35c3, and assert no `__pycache__` in `t_zero_records_is_loud`.
- [ ] F11 (low): split the guard at `tools/memory-recall/extract.py:255` so the zero-chunk case gets its own diagnosis naming MEMORY_ROOT, with a selftest arm.
- [ ] F12 (low): derive REL from `git rev-parse --show-prefix` at `tools/memory-recall/adopt-memory-recall.sh:32`, and assert REL is relative in the selftest.
- [ ] F13 (low): replace the inCMS worked example at `tools/memory-recall/query.py:163-165` with a corpus-agnostic one.
- [ ] F14 (low): flip the spec Status header to INPROGRESS (or CLOSED with a resolved §8) and update the ledger row, in the pre-push bookkeeping commit.

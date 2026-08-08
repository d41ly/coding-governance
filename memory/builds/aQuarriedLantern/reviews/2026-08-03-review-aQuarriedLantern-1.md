# Pre-code review — TOOL-aQuarriedLantern-1 (memory-recall kit port), rev-1

**Reviewed:** `memory/tooling/builds/2026-08-03-TOOL-aQuarriedLantern/spec/2026-08-03-spec-aQuarriedLantern-1.md`
(483 lines, SPECCED · rev-1 · node a · Tier-2 · base 9368d1e8) — the port of the inCMS retrieval CLI
into this repo as a copy-in kit reading `.memory-tree.conf`.

**Harness:** pre-code adversarial review, three finder lenses (portability · wiring · fidelity), then a
batched **default-refute** skeptic pass with index-keyed verdicts, then this synthesis. Findings were
verified against source in both repos, and four of them by experiment in throwaway git repos.

**Counts:** 15 raw findings · 14 confirmed · 1 refuted · **precision 0.93** · 0 unverified.
Skeptic severity corrections applied: two blockers → one high, one medium; two highs → medium.
Final: **2 blockers · 5 high · 7 medium.**

## Verdict

**NOT READY TO BUILD.** Two blockers are structural, not polish. The first is that the cache
freshness key does not include the conf, so the exact value the port's whole thesis moves from source
into `.memory-tree.conf` becomes a *cold* input to a *hot* cache: AC2 cannot pass on a warm cache,
and — worse — an adopter who reads the S7 diagnosis, fixes `FAMILIES` and re-queries gets byte-identical
stale output and the same diagnosis, so the one remediation path for the headline defect is itself a
silent no-op (proven by experiment, both directions). The second is that both of this kit's gates are
wired only into this repo's own `tools/gate-legs.json`; the spec adds no adopter-side gate-wiring step,
which both existing kits carry, so a project can copy the kit in and have the drift check silently never
run — the ARCH-aGrittedFlagstone-1 class the spec itself cites. Under those sit five highs that are all
cheap and all real: two internal contradictions the build would have to resolve at the keyboard
(escape-hatch flags the Inventory forbids; a kickoff clause this repo's engine does not implement), one
false property the spec asserts by measurement (`__pycache__` written inside the worktree, which fails
AC4 as written), and two factual errors load-bearing enough to change decisions (`--stats` does not read
the query log, and the coupling inventory is blind to a second project literal that the CLI *prints to
the caller* on every run). None of this is a redesign — fold rev-2, re-check, build.

### F1 — blocker — The cache freshness key does not include the conf, so every construct the port moves into `.memory-tree.conf` is served stale

`ensure_cache` (query.py:287-296) computes freshness from exactly five things: `CACHE_VERSION`,
`CHUNK_MAX`, the corpus digest (mtime+size over the memory tree's `.md` files only), the alias digest,
and the two `.db` files existing. Nothing hashes the id grammar, because upstream it is a source
constant nobody edits. The port makes it an adopter-editable config value sitting at the repo root, so
it never enters the corpus digest either. Consequences in order of harm: AC2 fails on a warm cache
(header count and searched records both come from the stale index); the *repair* path is a silent
no-op; and `MEMORY_ROOT` partially self-heals (a new root changes the file set, hence the digest) while
`FAMILIES` never does, which makes the failure look intermittent.

Evidence: proven by experiment in a throwaway repo carrying the three upstream scripts and a decision
file with `ARCH-aFoo-1/-2`. Run 1 `index 2 records + 1 chunks (rebuilt 2.27s)`; then `FAMILIES` mutated
`ARCH`→`ZZZZ` with the mutation asserted applied (before-and-not-after, plus grep both ways); run 2
`index 2 records + 1 chunks (cached …)` — the grammar change is invisible to the predicate. Inverse
direction: `--rebuild` with the wrong grammar gives `index 0 records + 1 chunks (rebuilt 0.97s)`, and
repairing `FAMILIES` back to `ARCH` then querying plainly gives `index 0 records + 1 chunks (cached …)`.
The precedent the spec needs already exists in the source it is forking: the alias digest is in the
manifest for precisely this reason (query.py:213-220 — an alias edit "would otherwise leave a stale
cache serving un-joined results with no signal at all"). Nothing in 483 lines mentions a conf digest;
§4's Cache paragraph says the shape is unchanged from upstream, and AC6 covers the alias digest only.
A `--rebuild` flag exists (query.py:117/755/894) but no spec text and no S7 diagnosis points an adopter
at it, and it is absent from `--help`.

**Fix:** add a `conf_digest` to the manifest and to the `fresh` predicate in `ensure_cache`, hashing the
RESOLVED values (`MEMORY_ROOT`, the sorted families tuple, the node-tag class) rather than the raw file
bytes, so a comment edit does not force a rebuild. Then rewrite AC2 to assert the rebuild, not the
message: flip `FAMILIES`, re-query, assert the header says `rebuilt` AND the record count moved. Have
the S7 diagnosis name `--rebuild` as the escape hatch, and document that flag in `--help`.

### F2 — blocker — Both of this kit's gates are wired only in this repo; no adopter-side gate-wiring step exists

`selftest.py` and the skill-drift `--check` land as legs in `tools/gate-legs.json` (S13) and nowhere
else. Both existing kits carry an explicit adopter gate-wiring step: `WIRE-INTO-PROJECT.md` §3 step 3
for memory-tree ("Wire the gate in all three places" — CI job, local gate runner, pre-commit) and §3b
step 5 for codebase-map, which ends "Without this the freshness/coverage ratchet silently never runs";
§6 even re-verifies the codebase-map leg is standing in CI and the gate runner rather than merely
runnable by hand. The spec's `WIRE-INTO-PROJECT.md` row enumerates exactly four additions — a §0
decision row, an adopt section, a Result-tree line, a Maintenance paragraph — in a table it introduces
as stating the exact addition per row, and a gate step is not among them. AC9 exists solely to catch
skill drift, so in an adopter that never wires `--check`, the drift check silently never runs: kit
copied in plus a skill file never rendered reads as fully wired.

**Fix:** add a numbered step to the new `WIRE-INTO-PROJECT.md` adopt section mirroring §3b step 5 — add
the kit's selftest and its `--check` to the project's gate runner AND its CI config, grep-guarded
against duplication, carrying the same "without this the check silently never runs" warning. Amend §7's
"What gates this kit in an adopter project" to name the mechanism, not just the file. (The finder also
asked for a SKILL arm in `tools/check-wiring.sh`; note that that file has only two arms today and
neither existing kit has one, so that half is a new pattern rather than a contract this kit must match —
optional, and not what the blocker rests on.)

### F3 — high — The no-conf refusal is specified to print two flags the spec's own Inventory forbids it from having

Spec line 170 says the refusal "offers the explicit escape hatch `--memory-root` plus `--families` …
printed in the refusal and never inferred". Spec line 289 (Inventory) states "CLI flags are unchanged
from upstream minus `--export`" — an explicit positive statement that no flag is added, so this is a
contradiction, not an omission. Upstream has neither flag: `KNOWN_FLAGS` (query.py:111-123) is
`--k --budget --stats --opened --qid --rebuild --help --terms --no-terms --export --tag`, and the value
and bare flag lists match. S2 exposes only the three conf values with no override path, S5 lists only
removals, and the adopt script gets only `--scaffold`/`--check`. No AC covers them — AC3 asserts only a
non-zero exit naming the memory-tree kit. Built to the Inventory, the first message a new adopter ever
sees names two flags the parser answers with "unknown flag". This also matters beyond a doc nit: §4
leans on the escape hatch to justify the refusal being acceptable rather than hostile for a project that
has a memory tree without the hygiene kit.

**Fix:** pick one and make it binding. (a) Put the two flags in S2/S5 scope, list them in the Inventory
as the two new flags, and add an AC that runs a real query in a conf-less repo using both and asserts a
non-zero record count. Or (b) delete the escape-hatch sentence and have the refusal print a
copy-pasteable two-line conf stub plus the memory-tree kit pointer — which serves that population just
as well and adds no flags. (b) is the smaller diff.

### F4 — high — The ported skill description defers to a `/session-kickoff` step this repo's engine does not implement

Upstream's description ends "Skip it while /session-kickoff is running; that skill's Step 3 issues this
query itself" — true in inCMS, where that repo's kickoff Step 3 literally issues the query. Here,
`skills/session-kickoff/SKILL.md` Step 3 is "Derive a CLOSED task scope" and issues no query; the probe
analogue codebase-map earned lives in Step 4 ("Codebase map as the first probe (when the project has
one)"). Grepping this repo for "recall" across `skills/`, `AGENTS.md` and `CLAUDE.md` returns zero hits,
so nothing on the kickoff path would issue it. Spec §4's skill section enumerates the skill's project
coupling as exactly two items (the five inCMS families, the one script path) and names two invariants to
preserve; the kickoff clause is a third coupling it misses, and the wiring table gives `skills/` nothing.
Ported verbatim, the clause actively suppresses the tool during the exact moment the spec's own Goal
targets ("before touching an unfamiliar area"); dropped silently, the positive wiring is still missing.

**Fix:** rewrite or delete the kickoff clause in the skill template, and add a memory-recall probe
paragraph to `skills/session-kickoff/SKILL.md` Step 4 beside the codebase-map one, conditioned on the kit
being present. Add a selftest arm asserting the rendered description makes no claim about a kickoff step
the engine does not implement — the same class of check the spec already applies to the augments-grep
clause and to the parseable invocations.

### F5 — high — "Writes nothing inside the worktree" is false as specified: the kit writes `__pycache__` into the adopter's tree, so AC4 fails

query.py:63-66 inserts its own directory on `sys.path` and imports its siblings, so CPython writes their
bytecode next to the source — inside the worktree, not under the common git dir. §4's measurement missed
it because it ran from the upstream script directory, where the pycache already existed and inCMS's
`.gitignore` hides it.

Evidence: throwaway git repo, kit copied to a `tools/` subdirectory, one query run. `git status --porcelain`
before = empty; after = one untracked `__pycache__/` entry; the files created inside the worktree are the
two sibling `.pyc` files, neither of which resolves under the common git dir. Both halves of AC4 therefore
fail — the path enumeration fails even in the reference adopter (this repo's `.gitignore` lines 1-2 carry
`__pycache__/` and `*.pyc`, so its status stays clean while the files still land in the tree), and the
status half fails in any adopter without that rule. Grepping `WIRE-INTO-PROJECT.md`, both kit READMEs and
`AGENTS.md` for pycache/gitignore/pyc returns zero hits, so the wiring docs never tell an adopter to add
it, and the Non-goals line claiming §4 shows by measurement that nothing needs ignoring is false as stated.
One sub-claim is corrected: nothing in this repo's tooling actually refuses on the resulting dirty tree —
`tools/push-main.sh` gates on the untracked-ignoring form — so the harm is the false property, a red AC4 at
build time, and untracked noise in an adopter's tree, not a blocked push. Fix verified in the same repo:
with the one-line suppression added, exactly four files are created and all four sit under the common git
dir.

**Fix:** set `sys.dont_write_bytecode = True` immediately above the `sys.path` insert in the forked
`query.py`, and in `selftest.py`, which imports the same modules. Name it in §2/S5 as a third fork edit.
Keep AC4's path enumeration exactly as specified — it is the gate that catches this — and add an arm that
enumerates paths under the kit directory as well as under the worktree root. Correct the Non-goals line.

### F6 — high — `--stats` does not read the query log; it prints the cache manifest, and that false statement is the stated mitigation for dropping `--export`

query.py:923-924 is the whole of `--stats`: it dumps the manifest dict returned by the cache builder
(version, chunk_max, n_files, counts, digest, alias_digest, built_s, built_at). `grep -n "read_log" query.py`
returns two lines: the definition at 550 and one call site at 726, inside `export()`. Drop `--export` per S5
and nothing in the kit reads the query log at all — the hook appends, `--opened` appends, `log_event` appends,
and no code path ever reports. `--stats` is not even a standalone mode; without a question the CLI prints its
usage refusal. The spec asserts the opposite in §4 ("`--stats` stays; it reads the log and prints, and it
covers the traffic question without the tracked write"), in §4 Alternatives, and in Q2's recommended option
(a). This is not a restatement of the open fork: Q2 openly asks whether `--export` should go and concedes
that (a) leaves no artifact to compare — what is refuted is the stated mitigation, which is verifiably wrong.
Trimming the finder's framing: the credential-into-git argument and the unconditional writes-nothing property
stand on their own; `--stats` is offered as the consolation, not the entire justification.

**Fix:** either (a) rewrite the three §4/§8 sentences to say plainly that v1.0 ships a write-only log with no
reader, and record the traffic-reporting gap as the priced cost of dropping `--export`; or (b) take Q2 option
(b) — keep the aggregation but write it beside the log under the common git dir, which closes the
credential-into-git path without losing the reader. Either way, move `--stats`'s real content to §5
observability as a CACHE fact, which is how §5 already describes it.

### F7 — high — The coupling inventory is derived from a grep for the corpus root, so it cannot see the second project literal — the script's own path, which the CLI prints on every run

§4 states the literal counts come from `grep -c "memory/" scripts/recall/*.py`, which is structurally blind
to the other baked-in project constant: the script's own directory. Recount: 7 occurrences in query.py
(lines 13, 14, 15, 16, 134, 608, 976) and 2 in bench.py (lines 20, 223) — so "six edited constructs in
extract.py and one in query.py" and "bench.py … zero project coupling → byte-identical" are both undercounts.

The worst instance breaks a fix the port is otherwise carrying. query.py:975-976 prints, after every
successful query, `logged as qid N — record which hit answered it:` followed by an invocation naming the
upstream script path. That line IS the F17 fix from commit fd6274df7 ("`--opened` takes an explicit `--qid`
and the query path prints the qid it logged") — the change that made `--opened` usable at all. Ported
unedited, the kit hands every adopter an instruction to run a file that does not exist in their repo, so the
outcome-recording rate the hook exists to raise stays at zero by a second route. The same literal sits in
`REFUSAL` (query.py:134), the first thing a caller sees when they forget `--terms`, and in the module
docstring usage block. The spec already knows the script path is a project value — it templates that path
into the skill and gates that every invocation the skill prints still parses — but that invariant covers the
skill file only; nothing covers the CLI's own printed invocations. (bench.py:223 likewise raises a
`SystemExit` naming the upstream path, so S4's "zero project coupling" is an overclaim even though the
table's narrower "zero occurrences of the corpus root" is accurate. The finder's incidental "twice in 110
queries" figure does not match the spec's own "3 records against 178 queries"; neither was re-derived here,
and it is decoration, not substance.)

**Fix:** add the self-path to the fork list in §2/S5 and to the §4 coupling table: derive the printed
invocation from `__file__` relative to the repo root as one expression, reused by the refusal text, the
docstring usage block and the qid hand-back. Add an AC asserting every path the CLI PRINTS exists in the
adopter — the mirror of the skill-side invariant §4 already gates. For bench.py, either keep it
byte-identical and say in the kit README that its two usage strings are upstream spellings, or re-scope S4's
claim to "zero coupling on the query path".

### F8 — medium — (Duplicate of F5, reported independently by the portability lens)

The portability lens found the same `__pycache__` defect from the adopter angle: the kit ships no
`.gitignore` change (an explicit Non-goal), the wiring doc never mentions pycache, so an adopter without that
rule gets a permanently dirty tree from a read-only query. Same mechanism, same one-line fix, verified in the
same way. No separate action — F5's fix closes it. Recorded here only so the count matches the harness output.

### F9 — medium — The new `--check` merge-bar leg defaults its interpreter to bare `python`, and the gate runner's argv rewrite cannot rescue it

§4 says the shell entry points take an override defaulting to `python`, mirroring
`tools/codebase-map/adopt-codebase-map.sh:14`. That is the one launcher in this repo with no `python3`
fallback, and it guards a MANUAL `--scaffold` where a missing interpreter is a one-off loud failure. The two
detectors that actually ride gates both probe python3 first (`tools/run-gates.sh:9` and
`tools/check-wiring.sh:69`). Promoting the python-only form to a merge-bar leg means a stock Debian/Ubuntu
adopter without `python-is-python3` reds the whole gate suite on a working kit. `tools/run-gates.sh:52`
rewrites `argv[0]` only when it is `python` or `python3`; this leg's first token is `bash`, so the resolver
provably never sees it. Additional confirmation the finder did not cite: today not one bash leg in
`tools/gate-legs.json` shells out to python at all —
`tools/agent-instructions/adopt-agent-instructions.sh:56` says it computes its path in pure shell
specifically to avoid this — so this would be the first, and the first with an unprobed default.

**Fix:** use the `tools/check-wiring.sh:69` form inside the adopt script — try `python3`, fall back to
`python`, keep an explicit env override — and add one selftest arm that runs the adopt script with `python`
removed from `PATH` and asserts exit 0. Without that arm, every node with both binaries keeps the leg green
and the defect invisible.

### F10 — medium — Q3's recommended "ship it dark" outcome is unreachable given S9, and the mirrored arm will print a permanent false UNWIRED

Q3(b) states that shipping the hook unwired makes `tools/check-wiring.sh` report it "not adopted" rather than
"UNWIRED". The arm it mirrors keys "not adopted" on the hook file's ABSENCE
(`tools/check-wiring.sh:64-67`), and present-but-unmerged falls through to the UNWIRED branch. S9 copies the
hook file into `.claude/hooks/` unconditionally, so under Q3(b) the file is present and the settings block is
absent, and a faithful mirror prints UNWIRED — the exact opposite of the stated outcome. This repo runs that
script as its own SessionStart hook (`.claude/settings.json`), so the reference adopter would print a
permanent false alarm at every session start, which is the fastest way to train every node to ignore the
wiring verifier. Two consequences the finder claimed do not hold, hence the downgrade: `--session` exits 0
early so session start never breaks, and `WIRE-INTO-PROJECT.md` explicitly says not to run the wiring check
itself as a merge-bar leg (only `tools/check-wiring.test.sh` is a leg), so no gate goes red. What survives is
the false alarm plus new test cases with no defined expectation, because S11 and Q3(b) contradict each other.

**Fix:** pick one and write it down. Either `--scaffold` does not copy the hook file unless an explicit
opt-in flag is passed (so absence is a real signal), or the recall arm gets a three-state predicate — kit
adopted, hook file present, settings block absent → a `skip … wiring opt-in per WIRE §n` line, with only an
explicit opt-in marker promoting it to UNWIRED. Pin BOTH states as cases in `tools/check-wiring.test.sh`, and
correct Q3(b)'s stated outcome.

### F11 — medium — The governance playbook template gets no row, and there are 33 bytes of headroom to add one

`bash tools/check-template-size.sh` prints `template-size OK — parallel-coding-governance.template.md:
32735 / 32768 bytes (33 under, 99.9%)`, and the gate's own text forbids raising the ceiling to fit new prose.
Both existing kits hold an "Optional —" bullet in the template's §5 (lines 106 and 107), each running roughly
560-600 bytes, so a matching third does not fit in 33 bytes. The spec mentions the template nowhere: it
appears in neither the Wiring inventory nor the Files-touched table, and the `AGENTS.md` row does not cover it
(that file is this repo's own working guide, not the adopter-facing playbook). This matters because the
template is the operational ruleset an agent reads every session — it is what makes the CLI actually get used
upstream, where the charter mandates the query at DoR. Without a template line, the skill description is the
sole trigger and the DoR mandate does not travel with the kit. Related incoherence: the spec's planned §0
"adopt memory-recall?" row has nothing to delete on a "no", because unlike the memory-tree and codebase-map
rows there are no template/DoR/DoD lines to remove.

**Fix:** add a template bullet in the optional-kits list beside the other two, plus the §0 row stating the
dependency on memory-tree (S8 refuses without the conf) and what to delete on "no". Budget the bytes
explicitly in the Files-touched table — name the prose being trimmed or moved to
`parallel-coding-governance.domain-rules.md`, which is the gate's own prescribed remedy.

### F12 — medium — The `--fragment` file has no declared home, no declared schema, and no declared adopter-side path

S11 makes `tools/check-wiring.sh` call `settings-merge.py --check --fragment FILE`, so that file must resolve
from the repo root in an adopter — but S1's nine kit files do not include it, the Files-touched table does not
list it, and the Inventory paragraph does not claim it as a key; only S10 and the §4 wiring row say a fragment
ships. The schema gap is the load-bearing half: `tools/settings-merge.py` hardcodes all three of the event
(line 57), the matcher (line 61) and the dedup marker (line 42), and its own docstring says that marker IS the
deployer's is-it-wired signal — which is exactly what S11 delegates detection to. A fragment with no declared
marker leaves the recall arm nothing to join on. Second gap: the spec never states the adopter-side kit
directory name, while both existing kits are copied to a FIXED root-level name (`WIRE-INTO-PROJECT.md`:98 for
memory-tree, :139-140 for codebase-map, whose step adds "the fixed name the gate template resolves — don't
rename"); every path in the spec is this repo's own `tools/` spelling. The finder's third leg — that
"roughly 30 lines" under-scopes the PreToolUse lift — is refuted: S10's word "generalised" implies lifting the
hardcodes, AC10 already pins that the recall fragment adds the PostToolUse/Read block, and the estimate sits
in a table headed as an estimate.

**Fix:** name the fragment's shipped path in S1 and in the Inventory, and state its schema — event key,
matcher, dedup marker — since all three are hardcoded today. State the adopter-side kit directory name in the
new adopt section and use that name (not this repo's `tools/` path) in the check-wiring arm.

### F13 — medium — `recall-opened.js` hardcodes the corpus root and is absent from the coupling inventory

The hook's path resolver tests a literal `memory/` prefix (recall-opened.js:81) and then scans for the literal
`/memory/` boundary (line 86); both return null for a corpus rooted anywhere else, and `main()` bails before
appending — indistinguishable from "no read matched". `tools/memory-tree/.memory-tree.conf.example:6` ships
`MEMORY_ROOT=memory` as a documented per-repo value, so a non-`memory` root is a supported adopter state.
§4's coupling table stops at the five Python files, because line 76 says the counts came from a `.py`-only
grep that structurally could not see a `.js` hook the same unit ships. AC11 exercises only the default root,
so no gate sees it, and this is the silent-nothing class S7 exists to kill, reintroduced in the one file S7's
counter-based diagnosis cannot watch. Downgraded from high because Q3(b) lands the hook dark, upstream has it
wired on no node, and the reference adopter's root is literally `memory` — no measured population is affected
today.

**Fix:** cheapest honest option — match on the shown-paths array the hook already parses out of the log, which
is root-agnostic by construction. Otherwise render the hook from the conf at adopt time the way the skill
template is rendered, and let `--check` catch drift the way AC9 does for families. Add the hook as a row in
the §4 coupling table and add an AC11 sibling running it against a repo whose root is not `memory`.

### F14 — medium — S6's eviction reclaims 38% of the growth §5 cites to justify it, and its one dangerous branch is unspecified

§5 lists the risk as unbounded git-directory growth "measured at 555 MB upstream and mitigated by S6", which
reads as the number being addressed. Recomputed by hashing each cache directory name against the live worktree
list: of five cache directories, THREE belong to worktrees that exist and survive eviction. Live 343.2 MiB
(114.6 + 114.6 + 114.1), orphaned 209.4 MiB (99.2 + 110.2), total 552.6 MiB of cache plus 2.3 MiB of log =
555 MiB. Eviction reclaims **37.9%**, not the whole figure. The real driver is ~115 MiB of cache per LIVE
worktree against a 40 MB corpus, in a repo shape that mandates many concurrent worktrees — at the seven
currently checked out, a perfectly-evicted cache is ~800 MiB. Separately, S6 and AC7 specify only the two
cases where a worktree path IS recorded. The reachable third case is a sibling mid-first-build: the builder
mkdirs the directory and writes both `.db` files BEFORE the manifest (deliberately, "manifest last, and
atomically"), so the manifest read returns nothing and the branch is undefined — treating that as evictable
deletes a live sibling's cache mid-build; treating it as keep-forever is safe.

**Fix:** state the measured split in §5 (evictable 209 MiB, live 343 MiB across three worktrees, ~115 MiB
each) so the risk row is not read as solved, and add a per-worktree size cap or an LRU on `built_at` if
bounding the total is actually wanted. Spell the missing-manifest branch explicitly — "a cache directory with
no readable manifest is NEVER evicted" is the safe default — and make AC7 assert it as a third case.

## Unverified (no skeptic verdict)

None. Every raw finding received a verdict; 14 confirmed, 1 refuted, 0 fell through the join. (The
index-keyed verdict join was used specifically to prevent the silent all-refuted failure mode; the verdict
count was checked back against the finding count.)

## Fold checklist

- [ ] F1 (blocker): add `conf_digest` (resolved values, not raw file bytes) to the manifest and the `fresh` predicate; rewrite AC2 to assert `rebuilt` plus a moved record count; have S7's diagnosis name `--rebuild`, and document that flag in `--help`.
- [ ] F2 (blocker): add an adopter gate-wiring step to the new `WIRE-INTO-PROJECT.md` section (selftest + `--check` into the project's gate runner AND CI, grep-guarded, with the "silently never runs" warning), and amend §7 to name the mechanism.
- [ ] F3 (high): resolve the flag contradiction — either scope `--memory-root`/`--families` into S2/S5 with an Inventory entry and an AC, or delete the escape-hatch sentence and print a copy-pasteable conf stub instead.
- [ ] F4 (high): rewrite or delete the `/session-kickoff` clause in the skill template, add a memory-recall probe paragraph to `skills/session-kickoff/SKILL.md` Step 4, and add a selftest arm pinning that the rendered description claims no kickoff step the engine lacks.
- [ ] F5 (high): set `sys.dont_write_bytecode = True` above the `sys.path` insert in the forked `query.py` and in `selftest.py`; name it as a fork edit in §2/S5; extend AC4 to enumerate paths under the kit directory; correct the Non-goals claim that nothing needs ignoring.
- [ ] F6 (high): correct the three §4/§8 sentences — `--stats` prints the cache manifest, not the log — and either price the traffic-reporting gap explicitly or take Q2(b) and write the aggregation outside the worktree.
- [ ] F7 (high): add the script's own path to the fork list and the §4 coupling table, derive every printed invocation from `__file__`, and add an AC that every path the CLI prints exists in the adopter; re-scope S4's "zero project coupling" claim for bench.py.
- [ ] F8 (medium): no separate action — closed by F5.
- [ ] F9 (medium): make the adopt script probe `python3` first with `python` as fallback (the `tools/check-wiring.sh:69` form) and add a selftest arm running it with `python` off `PATH`.
- [ ] F10 (medium): decide hook shipping explicitly — no hook copy without an opt-in flag, or a three-state predicate in the recall arm — pin both states in `tools/check-wiring.test.sh`, and correct Q3(b)'s stated outcome.
- [ ] F11 (medium): add the `parallel-coding-governance.template.md` optional-kit bullet and the §0 adopt row, and budget the ~600 bytes in the Files-touched table by naming the prose trimmed or moved to `parallel-coding-governance.domain-rules.md`.
- [ ] F12 (medium): declare the fragment file's shipped path in S1 and the Inventory, state its schema (event key, matcher, dedup marker), and state the adopter-side kit directory name used by the check-wiring arm.
- [ ] F13 (medium): make the hook root-agnostic (match the shown-paths array it already parses, or render it from the conf), add it to the §4 coupling table, and add an AC11 sibling for a non-`memory` root.
- [ ] F14 (medium): correct §5's growth figure to the measured split (evictable 209 MiB of 555 MiB), decide whether a per-worktree cap or LRU is wanted, and specify plus gate the no-readable-manifest branch as never-evict.

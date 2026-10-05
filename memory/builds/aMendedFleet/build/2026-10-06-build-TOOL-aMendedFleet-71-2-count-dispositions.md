# TOOL-aMendedFleet-71 — the dispositions of every present-tense count the census printed

**Serves:** journal TOOL-aMendedFleet-71

**Starting commit** `2a44284c96ed4bc85039db8f9ab7422e0d673b2c`, read with `git rev-parse HEAD` before
the pass's first edit, node a, 2026-10-06. The census ran in a `git clone --local` of the worktree
checked out at that sha under `%TEMP%/c71`, with the script from this folder:

```
python memory/builds/aMendedFleet/build/2026-10-06-build-TOOL-aMendedFleet-71-1-count-census.py
```

Its population line at the starting commit, as printed:

```
files by kind: sh 117 · py 75 · js 19 · hook 4
product: files 137 · paragraphs 10648 · candidates 72 · near-misses 0 · wide-only 771
test: files 78 · paragraphs 8795 · candidates 21 · near-misses 2 · wide-only 550
```

Every kind read more than zero files, so a short list below is a short list and not a dead walk.

## How the list was narrowed

The spec's rev-2 predicate, with `now`, `live` and `tracked` as present-tense markers, printed 1414
candidates at this same commit. Spec rev-3 records why those three left the marker set and what the
census still prints about them: `wide-only` above is the count of sentences carrying a count and only
one of the dropped words. Nothing in that set is dispositioned here.

The census reads full-line comments and Python docstrings. It opens files with `newline=""`, because
`tools/unattended/check-unattended.sh` holds raw CR bytes and universal-newline mode reads each as a
line break; the first run without it placed four candidates in that file two lines late.

## S4 and AC2

Both sentences the report names are in the list: `tools/unattended/unattended.sh:4184` ("Five
tracked specs produce the first row today") and `tools/unattended/unattended.sh:4190`, the wrapped
one ("zero of 277 tracked specs" on line 4190, "disagree today" on line 4191). Neither had been
rewritten by a sibling unit, so both halves were observable.

## Frozen near-misses

The census printed two, neither owed a row: `tools/unattended/check-unattended.test.sh:232` (a
fixture date, `2099-01-01`) and `tools/unattended/check-unattended.test.sh:444` (dated to base
`0422ea2e`, 2026-09-13).

## The dispositions

One row per candidate at the starting commit, joined on path and line. FROZEN rows name the commit
that wrote the figure, the newest commit in `git log -L <line>,<line>:<path>` whose added lines carry
it. The AC6 cell names the six-word fragment of the base wording, `git grep -F` at the starting
commit, and what it found outside the edited file.

| Location | Sentence at the starting commit | Disposition | Reason, or the edit | AC6 |
|---|---|---|---|---|
| `.githooks/pre-push:1060` | The design pass recommended 1 — behaviourally today's bar — and that was refused on the record: the owner's stated goal is to stop paying the full bar per landing, and 1 defers essentially all of the saving. | NOT-A-COUNT | `1` names a design-pass option, and `today's bar` is the bar's behaviour, not a population | — |
| `tools/check-placeholders.sh:73` | Without it this mode's verdict is the LAST COMMAND's status, correct today only by short-circuit accident: `rc=1` makes the `[` fail and the AND-list returns 1. | NOT-A-COUNT | `1` is an exit status and `today` qualifies a verdict's behaviour | — |
| `tools/check-spec-tokens.py:248` | the set the floor excludes TODAY is derived and printed on every run, never typed. | NOT-A-COUNT | `every run` is a rule; the sentence already says the set is derived and printed, never typed | — |
| `tools/codebase-map/gen_map.py:7` | exit 1 python <kit>/gen_map.py --seed-baseline   # rewrite baseline.toml from unclaimed python <kit>/gen_map.py --seed-affordance-baseline  # grace today's dossiers (adopt) python <kit>/gen_map.py --seed-affordances --top 10 # worklist: undeclared hot seams | NOT-A-COUNT | usage text in the module docstring: `--top 10` is an argument and `today's dossiers` a flag's description | — |
| `tools/codebase-map/map_lib.py:453` | Measured: every one of the six files under ``tools/`` yields at least one definition today (19, 4, 1, 2, 2, 2), so the floor is a measurement rather than an assumption. | FROZEN | dated to 5966e3109 (2026-08-17), `today` made `when this was written` | `yields at least one definition today`: only this file; quoted by 1 memory record(s), none a gate or test |
| `tools/codebase-map/reuse_lookup.py:91` | This corpus has NEITHER today — measured, and said plainly, because an earlier revision of this comment claimed it had both in the build that shipped the rule against assertions with no observation behind them. | FROZEN | dated to 504533fb4 (2026-09-05), `has NEITHER today` made `had NEITHER when this was written` | `This corpus has NEITHER today —`: only this file |
| `tools/codebase-map/selftest.py:2288` | AC4 first: `symbols.json` is the ONLY conditional tier today, so a criterion that enumerated the tiers would grade a population of one and could not fail. | FROZEN | dated to 7ad94fbb2 (2026-09-06): `symbols.json` was the only conditional tier when this was written | `is the ONLY conditional tier today,`: only this file |
| `tools/drift-audit/drift_report.py:316` | The spec's rev-1 gave that case to a `COVERAGE_FLOOR` that rev-2 cut, so it is currently VISIBLE (the fraction moves, and the lexicon gate prints it every run) and not gated. | NOT-A-COUNT | `rev-1` and `rev-2` are spec revisions and `currently VISIBLE` describes a design state, not a population | — |
| `tools/drift-audit/drift_report.py:838` | `never drained` is the seed reading's one surviving case, a list seeded with rows that holds at least as many today. | NOT-A-COUNT | `one surviving case` counts the signal's own logic branches, and `today` is its reading against the seed | — |
| `tools/drift-audit/drift_report.py:1563` | `drift-audit records` is an unguarded merge-bar leg, so a pin set N days ahead of today's count becomes a scheduled refusal: the day the count crosses it every merge reds until someone raises the pin or closes rows, which is the refusal this signal exists to make unnecessary. | NOT-A-COUNT | `N days` is a variable and `today's count` is the signal's own reading at run time | — |
| `tools/drift-audit/drift_signals.py:65` | Today the narrowing changes no verdict; | REWRITTEN | "It is taken before it changes a verdict, not after one." | `Today the narrowing changes no verdict;`: only this file; quoted by 1 memory record(s), none a gate or test |
| `tools/drift-audit/drift_signals.py:124` | It said "empty today and meant to stay so" while the row beside it printed `entries 3`, so an operator reading the JSON was told the opposite of the derived value standing next to it (TOOL-aScouredKit-8). | NOT-A-COUNT | quotes a past comment and its `entries 3` reading as the history of a fixed defect | — |
| `tools/drift-audit/drift_signals.template.py:45` | The signal reports each one's seed count vs its count today. | NOT-A-COUNT | `today` is the signal's reading at run time, the behaviour being described | — |
| `tools/govkit/govkit.py:686` | Same defect as the renormalize guards, one repository over — gov's own tree today has no such path, which is exactly why it would rot. | REWRITTEN | "a tree carrying no such path never exercises the split, which is exactly why it would rot." | `gov's own tree today has no`: only this file |
| `tools/govkit/govkit.py:832` | Kahn with an alphabetical ready-queue, so the result is deterministic and reduces to today's alphabetical order whenever no edge applies. | NOT-A-COUNT | `today's alphabetical order` is the prior behaviour; `no edge` is a condition | — |
| `tools/govkit/govkit.py:1054` | Falls back to the argv unchanged when no bash resolves, so a machine with none behaves exactly as it does today instead of newly refusing on a path that never needed this. | NOT-A-COUNT | `a machine with none` is a condition and `as it does today` the prior behaviour | — |
| `tools/govkit/govkit.py:1200` | What makes it safe today is `SEEDED_TOKENS` above: ---- every token that reaches an argv is gov's own and a target cannot supply one. | NOT-A-COUNT | `every token` is the invariant `SEEDED_TOKENS` enforces, already pointed at its owner | — |
| `tools/govkit/govkit.py:2034` | Same defect as the renormalize guards, one repository over — gov's own tree today has no such path, which is exactly why it would rot. | REWRITTEN | the same sentence as line 686, the same rewrite | `gov's own tree today has no`: only this file |
| `tools/govkit/govkit.py:2503` | Measured on gov today it IS zero: both shipped carve-outs sit in front of a seed rule that already wins the same destination. | FROZEN | dated to 0dfc56ffa (2026-08-16): `it IS zero` made `it WAS zero` | `Measured on gov today it IS`: only this file |
| `tools/govkit/govkit.py:3445` | No descriptor here declares one today, so that half is correct and unexercised by the shipped tree; | REWRITTEN | "Whether a shipped descriptor declares one is the descriptors' fact and not this docstring's" | `No descriptor here declares one today,`: only this file |
| `tools/govkit/govkit.py:3720` | THE ONE WRITER for every destination `ADOPTER_BAR_PATHS` declares, which today is the gate-leg manifest an adopter's whole bar reads. | NOT-A-COUNT | `every destination` ranges over a declared constant and `today is` names its member; that is A3's restated-value ban, not this unit's class | — |
| `tools/govkit/govkit.py:4094` | This is the read-only join that needs no receipt, writes nothing, and returns a number for a real adopter today. | NOT-A-COUNT | `a number` is the join's output, and `today` its behaviour | — |
| `tools/govkit/govkit.py:4203` | Every one is gov-controlled ---- TODAY, and each row exists so the next reader has to re-answer that when a caller changes. | REWRITTEN | "Each was gov-controlled when its row was written" | `Every one is gov-controlled`: only this file |
| `tools/govkit/govkit.py:4733` | `classify_outcome` returns None both when no block matches and when none is declared, so the fall-through below is today's answer exactly. | NOT-A-COUNT | `none is declared` is a condition and `today's answer` the prior behaviour | — |
| `tools/govkit/govkit.py:7912` | The spec's grounds, attributed: on the live target every `relocate` row proves on raw bytes and none needs the composition, so composing buys nothing today and adds a fourth rung's worth of surface. | FROZEN | dated to 1f84f5841 (2026-08-25): the spec's measurement is now past tense and `today` made `then` | `composition, so composing buys nothing today`: only this file |
| `tools/govkit/govkit.py:8941` | This call stays: it is the narrowest scope, it is the one that survives a `--kits` narrowing of the preamble's own list, and a guard removed because another one covers it today is how the next reordering reopens the hole. | NOT-A-COUNT | `another one covers it today` is a hypothetical about a guard, not a count | — |
| `tools/govkit/govkit.py:12727` | ALREADY ABSORBED (F2), reported as a class-1 proposal CARRYING THE CONTRARY EVIDENCE rather than as a fifth class: every added line already appears in gov's own copy, so gov took this change under different bytes and this is the row the adopter can delete today. | NOT-A-COUNT | `class-1` and `fifth class` are taxonomy labels, and `today` qualifies the adopter's action | — |
| `tools/govkit/matrix.py:198` | none does today. | REWRITTEN | the clause `none does today` deleted; the rule before it stands alone | `silent widening; none does today.`: only this file |
| `tools/govkit/selftest.py:636` | No arm grades either field over these fixtures today; | REWRITTEN | "An arm that grades either field over these fixtures must rewind them first." | `No arm grades either field over`: only this file |
| `tools/govkit/selftest.py:2316` | Zero carve-outs-that-change is the true state of gov today and must NOT red; | REWRITTEN | "Zero carve-outs-that-change is a true state gov has been in" | `Zero carve-outs-that-change is the true`: only this file |
| `tools/govkit/selftest.py:12428` | Its receipt belongs to a fixture the AC8 arms re-adopt READ-ONLY afterwards, so re-reading it here would work today and stop working the first time somebody adds a `--write` to one of those arms. | NOT-A-COUNT | `AC8` is a criterion label and `would work today` the fixture's behaviour | — |
| `tools/hooks/agent-cap.js:204` | That makes the change monotone in the DENY direction by construction, so no script this hook denies today can be admitted after it. | NOT-A-COUNT | `no script this hook denies today` names the deny set before the change: a monotonicity property | — |
| `tools/hooks/agent-cap.js:351` | `main()` runs the whole rule set, and if nothing denied, sets the mode to `shipped` and runs it again: a denial from EITHER pass stands, so no script this hook denies today can be admitted after the change. | NOT-A-COUNT | the same monotonicity property as line 204 | — |
| `tools/hooks/agent-cap.js:519` | Measured before wiring, over all eight tracked *.js: ZERO lines match the widened form and not the old one, so nothing currently admitted becomes denied. | FROZEN | dated to 3ff9cc140 (2026-09-05): `match` and `becomes` made past tense, `currently admitted` made `admitted when this was written` | `so nothing currently admitted becomes denied.`: only this file |
| `tools/lexicon/lexicon.py:2384` | `sys.stdlib_module_names` IS 3.10+, and that costs this kit nothing it had not already spent: `lexicon_conf.load_conf(path: str \| Path)` is a PEP-604 annotation evaluated at definition time, so an adopter on 3.9 cannot import this engine at all today. | NOT-A-COUNT | `3.10` and `3.9` are Python versions and `PEP-604` an id | — |
| `tools/lexicon/lexicon.py:3946` | Harmless today — this module's body is assignments and a `sys.path.insert`, with no I/O — but `lex.KNOWN_EXTS` inside the scaffold is then a DIFFERENT object from the one this function holds, so nothing across that boundary may be compared by identity. | NOT-A-COUNT | `no I/O` describes the module body's code, read beside it | — |
| `tools/lexicon/selftest.py:2400` | This is the state every adopter of an unshipped language is in today, and it is the reason the block exists: the language is declared, no set answers it, and the walk refuses one line before any predicate. | NOT-A-COUNT | `every adopter of an unshipped language` defines a class by its condition; `one line` is an offset | — |
| `tools/lexicon/selftest.py:5577` | This is the best an adopter can do today with no code change at all, and unit 1 measured it at 0.6% type recall over the whole tree. | NOT-A-COUNT | the 0.6% is past tense and attributed to the unit that measured it; `today` qualifies what the shipped set can do | — |
| `tools/lib/resolve-python.test.sh:271` | Measured today: three such lines, each a launcher NAME printed or rendered rather than executed (a remedy string, a committed Skill render, an adopter-layout fallback). | POINTED | "Which lines carry it is a grep for the marker, not a figure kept here" | `Measured today: three such lines, each`: only this file |
| `tools/memory-recall/check-recall.py:120` | So 0.60 sits one step above the observed maximum -- tight enough that copied text cannot pass, loose enough that today's set is not sitting on the boundary. | NOT-A-COUNT | `one step` is the threshold's increment; the measured figures sit in the sentence before, which carries no marker | — |
| `tools/memory-recall/selftest.py:2095` | A drift between them is silent today: an ensemble naming a substrate `rank_with` cannot dispatch scores zero and reports it as a result. | NOT-A-COUNT | `scores zero` is the failure the drift would produce, not a population | — |
| `tools/memory-recall/selftest.py:2327` | Driven inside a throwaway repo: both return before any log write TODAY, and an arm that relies on that is one refactor away from writing to the live log this suite exists to leave alone. | NOT-A-COUNT | `both` names two functions and `TODAY` their present behaviour, which the arm is warned not to rely on | — |
| `tools/memory-tree/backlog.py:1108` | V11 — a REOPEN naming no record that currently closes or declines its target. | NOT-A-COUNT | a rule's definition: `V11` is a label and `no record that currently closes` its condition | — |
| `tools/memory-tree/check-memory-hygiene.sh:661` | A dated recording under build/ is legal today and has no stable resume target, which is why the name is fixed here rather than left to the recording grammar. | NOT-A-COUNT | `legal today` is the grammar's behaviour | — |
| `tools/memory-tree/check-memory-hygiene.sh:921` | gov deliberately sets NO locale here, and its own comment says why: pinning one "would silently re-decide the cap on any adopter whose awk counts characters today". | NOT-A-COUNT | quotes another comment's reasoning about an adopter whose awk counts characters | — |
| `tools/memory-tree/check-memory-hygiene.sh:948` | Measured: no index-set member opens with front matter today, so this changes no current verdict. | FROZEN | dated to 20f7f2a40 (2026-08-17): `opens` made `opened when this was written`, `changes no current verdict` made `changed no verdict then` | `no index-set member opens with front`: only this file; quoted by 2 memory record(s), none a gate or test |
| `tools/memory-tree/check-memory-hygiene.sh:1137` | THIS NARROWS A POPULATION, which is why the preset block refuses a cutoff dated after today: a future date exempts every record and the check reports clean over nothing. | NOT-A-COUNT | `after today` is the date semantics of a cutoff, and `every record` the consequence of a future one | — |
| `tools/memory-tree/check-memory-hygiene.test.sh:1485` | On a build that does not honour `{8}` the header regex demands those literal bytes and never matches, so every post-cutoff spec reds with "missing/invalid **Status:** header" — a loud break of a check that works today. | NOT-A-COUNT | `{8}` is a regex quantifier and `works today` the check's behaviour | — |
| `tools/memory-tree/check-verdict-epoch.test.sh:205` | It cannot demand a specific clean REASON: which of the two holds depends on whether this branch currently carries an engine change, and both are correct answers. | NOT-A-COUNT | `the two` are the arm's own two clean reasons and `currently` qualifies a branch's state | — |
| `tools/memory-tree/gen_build_index.py:1960` | No file in the live corpus reaches it today, which is exactly why it went unnoticed. | REWRITTEN | "It went unnoticed because no file in the live corpus reached it." | `in the live corpus reaches it today,`: only this file |
| `tools/memory-tree/gen_build_index.py:2449` | The seven the fold can derive, plus the placeholder it renders : when a hold target names nothing — a reader asking "what is UNRESOLVED right now" is asking the : same question as one asking what is BLOCKED, and leaving it out would make that question : unanswerable by the one mode built to answer it. | NOT-A-COUNT | `seven` counts the fold's own statuses in the code beside it, and `right now` sits inside a quoted question | — |
| `tools/memory-tree/gen_build_index.py:3046` | THE REDIRECT IS AROUND THE WHOLE READ, not around the two notices this file happens to print today. | REWRITTEN | "not around whichever notices this file happens to print" | `not around the two notices this`: only this file |
| `tools/memory-tree/gen_build_index.py:3255` | The three probes are the ones that are cheap AND decisive for a BUILD slug — has any commit ever touched that build folder, does any tracked file name the token today, and does any commit message name it. | NOT-A-COUNT | `three probes` are the ones the code beside it runs, and `today` sits inside a probe's question | — |
| `tools/memory-tree/gen_build_index.py:5692` | No arm below reads this repository's own conf: an arm satisfied by whatever gov happens to declare today would be green over a reader that never looked at the rev at all. | NOT-A-COUNT | `whatever gov happens to declare today` is the hazard, not a count | — |
| `tools/memory-tree/merge-rows.py:1289` | `k` and `h` are what make an inert grammar visible during a real merge: on the governed indexes `h` is 0 today, and a FAMILIES drift turns every row hashed without moving any other number. | REWRITTEN | "`h` reads 0 while the grammar is in step" | `indexes `h` is 0 today, and`: only this file |
| `tools/memory-tree/migrate_backlog.py:1141` | today no spec in a shards-mode corpus carries either, and a second reader of them would be a second answer the day one does. | REWRITTEN | "a second reader of them would be a second answer the first day a spec in a shards-mode corpus carries either" | `today no spec in a shards-mode corpus`: only this file |
| `tools/memory-tree/row_grammar.py:239` | They contribute no keyed rows today, so the naive widening looks harmless — measured, it moves the row count by nothing and the `loose` count by seven — but a quoted example row inside one would red the `unkeyed` branch on a file nobody is permitted to edit, and the only remedy would be to edit it. | FROZEN | dated to 993b64c54 (2026-09-13): `contribute`, `looks` and `moves` made past tense | `They contribute no keyed rows today,`: only this file; quoted by 1 memory record(s), none a gate or test |
| `tools/memory-tree/row_grammar.py:517` | `keyed` is False when the id is a bare family with no slug and no sequence, which is a ROW without an id rather than a line that is not a row — the distinction hygiene check 8 cannot make and the reason eleven BRAND rows go uncounted today. | REWRITTEN | "the reason BRAND rows of that shape go uncounted" | `reason eleven BRAND rows go uncounted`: only this file |
| `tools/memory-tree/row_grammar.py:1526` | `opened` is empty on every real row today; | REWRITTEN | "`opened` may be empty on every real row" | `is empty on every real row today;`: only this file |
| `tools/process-monitor/scope.py:29` | 3  `--check-conf` only: the declaration is WELL FORMED and nothing live matches it right now. | NOT-A-COUNT | `3` is an exit code in a usage table | — |
| `tools/run-gates/adopt-run-gates.sh:158` | ADOPT mode writes nothing today, and says so rather than exiting 0 in silence. | NOT-A-COUNT | `exiting 0` is a status and `writes nothing today` the mode's behaviour | — |
| `tools/run-gates/derive-ceilings.py:154` | A NON-`ok` row counts only when its seconds land inside the CLOSED WINDOW `[ceiling, ceiling + CEILING_WINDOW_S]`, against the ceiling the leg manifest declares for that leg TODAY: that is a run the ceiling itself stopped, so the CEILING is a LOWER BOUND on the work, which is the one property a monotone maximum needs and the property `ok` rows are admitted for. | NOT-A-COUNT | the ceiling the manifest declares `TODAY` is the run-time read the rule describes, already pointed at its owner | — |
| `tools/run-gates/run-gates.evidence.test.sh:965` | Reachable without contrivance: GATE_LEGS produces a one-leg bar, guards scope a run to a handful, and resetting every leg that currently has a retained reading is the plain case. | NOT-A-COUNT | `one-leg bar` and `every leg that currently has` describe a reachable case, not a count | — |
| `tools/run-gates/run-gates.runlog.test.sh:37` | the two such functions today, `prof_die` and the turnstile ticker, run only above it. | REWRITTEN | "such a function must run only above it, as `prof_die` and the turnstile ticker do" | `the two such functions today,`: only this file |
| `tools/run-gates/run-gates.sh:50` | what is NOT covered is a partial update or a hand copy of one file, and unlike the 1.1 case above no govkit floor withholds the table today. | REWRITTEN | "no govkit floor was written to withhold the table" | `no govkit floor withholds the table today.`: only this file |
| `tools/run-gates/run-selftests.test.sh:356` | THE NAMES BELOW MUST STAY MUTUALLY NON-PREFIXING, because a substring filter is exactly the id-matched-as-a-substring shape: `deadl.sh` must not select `deadl9.sh`, and `both.sh` must not select `deadboth.sh` — the `.sh` and the `/` in front are what keep each one alone today. | NOT-A-COUNT | `deadl9.sh` is a fixture name, and `today` qualifies why the names stay apart | — |
| `tools/unattended/adopt-unattended.sh:137` | Every adopter shipped today declares it blank, which is legal and means the strict anchor; | REWRITTEN | "An adopter that declares it blank is the common case" | `Every adopter shipped today declares it blank,`: only this file |
| `tools/unattended/adopt-unattended.sh:140` | TOOL-aNamedGesture-1 - AUTH_PARAM is the SECOND such key, and for the reason ANCHOR_SCOPE gives: no adopter declares it today, so keeping the placeholder would red the placeholder arm for every one of them. | REWRITTEN | "an adopter that declares nothing is the ordinary case" | `no adopter declares it today, so keeping`: only this file |
| `tools/unattended/check-brief-recorded.sh:500` | What stops that today is NOT this leg: `git ls-tree <commit> -- ""` REFUSES an empty pathspec — measured, it prints `fatal: empty string is not a valid pathspec` — so the empty row currently reds one branch further down, on the path rather than on the hash. | NOT-A-COUNT | `one branch further down` locates a refusal; `today` and `currently` describe behaviour | — |
| `tools/unattended/check-playbook.test.sh:423` | A liveness arm would pass over two independent derivations that happen to agree today. | NOT-A-COUNT | `two independent derivations` names the arm's own subjects | — |
| `tools/unattended/check-unattended.sh:693` | A record before it was written when the driver accepted `fold` at a blocker-bearing exit, and reading it by today's rule redded sixteen tracked append-only records no verb can rewrite. | NOT-A-COUNT | a past-tense report of the event that motivated the cutoff, the brief's precedent for `it kept`; `today's rule` names the rule | — |
| `tools/unattended/check-unattended.sh:1372` | Two runs share one path, and their records share whole lines - `memory/builds/aBoundedVerdict/RUN.md` and its ABORTED sibling carry thirteen identical non-blank lines today. | FROZEN | dated to 14d5c6a41 (2026-09-21): `carry` made `carried` | `ABORTED sibling carry thirteen`: only this file |
| `tools/unattended/check-unattended.sh:2398` | Every one of them is VACUOUS on a record with no `asks:` ---- fact, which is every record in this tree today, so the count is announced after the loop: ---- a skip that looks like a pass is indistinguishable from coverage. | REWRITTEN | "which can be every record in a tree" | `which is every record in this tree today,`: only this file |
| `tools/unattended/check-unattended.sh:3131` | Undeclared is the empty set, which is every adopter today. | REWRITTEN | "Undeclared is the empty set, the ordinary case for an adopter." | `empty set, which is every adopter today.`: only this file |
| `tools/unattended/check-unattended.sh:3380` | The checker column is deliberately not joined: measured today three cells read `machine, PRE-LANDING` or `agent-attested` against the constant's `machine`/`agent`, and those spellings say something true the constant has no room for. | FROZEN | dated to 5e5d97837 (2026-08-16), `measured today` made `measured at` | `not joined: measured today three cells read`: only this file |
| `tools/unattended/check-unattended.test.sh:2668` | GREEN CONTROL: undeclared is the empty set, which is every adopter today, and is what keeps this change from reddening anyone who uses no extras. | REWRITTEN | "undeclared is the empty set, an adopter's ordinary case" | `empty set, which is every adopter today, and`: only this file |
| `tools/unattended/check-unattended.test.sh:2760` | Collides with check 17: a frozen waiver's handle graded against today's set. | NOT-A-COUNT | `check 17` is a label and `today's set` names the set graded | — |
| `tools/unattended/lib-unattended.sh:1515` | Seven tracked build READMEs are in that state today. | FROZEN | dated to ed281374b (2026-08-31): `are` made `were` | `Seven tracked build READMEs are in that`: only this file; quoted by 1 memory record(s), none a gate or test |
| `tools/unattended/unattended.sh:296` | Today they are one fact: a consumer that finds no rows reports a dead probe whether the producer was silent, talking on the other stream, or never answered at all -- and a green-looking zero from a broken redirect is indistinguishable from a clean run. | NOT-A-COUNT | `one fact` means unified, not a count | — |
| `tools/unattended/unattended.sh:1163` | `read_derived_phase` is the EFFECTIVE phase — what the record MEANS right now — and it is where every later derivation goes; | NOT-A-COUNT | a definition of the effective phase; `every later derivation` is a rule | — |
| `tools/unattended/unattended.sh:2566` | ABSENT is `slug` - every build README in every adopter's tree today declares nothing, and that is the ordinary case, not a defect. | REWRITTEN | "a build README that declares nothing is the ordinary case, not a defect" | `every build README in every adopter's tree today`: only this file |
| `tools/unattended/unattended.sh:4060` | Its input is the empty string on every call until TOOL-dDerivedDocket-16 builds the predicate that fills it, so the ladder prints today exactly what the three assignments printed. | NOT-A-COUNT | `three assignments` are the code it replaced, and `today` its unchanged output | — |
| `tools/unattended/unattended.sh:4067` | WHY RUNG 4 SITS BELOW RUNG 2 - today's behaviour, not a change. | NOT-A-COUNT | `RUNG 4` and `RUNG 2` are labels and `today's behaviour` the ordering | — |
| `tools/unattended/unattended.sh:4184` | Five tracked specs produce the first row today and ZERO produce the second, which the driver's own comment below already states - so the second is armed by fixture or not at all. | FROZEN | S4, the first sentence: dated to c80d92333 (2026-08-25), `produce` made `produced` | `Five tracked specs produce the first row today`: only this file; quoted by 1 memory record(s), none a gate or test |
| `tools/unattended/unattended.sh:4190` | Latent — zero of 277 tracked specs disagree today — and removed rather than left to be discovered by the first one that does. | FROZEN | S4, the wrapped sentence: dated to 1ce89563a (2026-08-25), `disagree today` made `disagreed at` | `zero of 277 tracked specs`: only this file |
| `tools/unattended/unattended.sh:5518` | Written unconditionally these drifted on a re-preflight — the base stayed pinned while the anchor evidence beside it moved to whatever the remote said today, so the record described two different observations as one. | NOT-A-COUNT | `two different observations` names the defect's shape; `today` is what the remote said | — |
| `tools/unattended/unattended.sh:5538` | Only a `slug` README can reach here carrying one, because the check above refuses the key under every other mode, so every other run pins `none` - and so does a `slug` README that declares nothing, which is every README in this tree today. | REWRITTEN | "so does a `slug` README that declares nothing, the ordinary case" | `README in this tree today. Printed,`: only this file |
| `tools/unattended/unattended.sh:5544` | TOOL-dDerivedDocket-16 S3 - THE THREE ASK FACTS, pinned ONCE for the reason `base` and the anchor triple are: a re-preflight that rewrote them would re-point the mandate, the tree it was asserted against and its grades at whatever today says, while the base they are evidence beside stayed pinned - and evidence for a pinned value that moves is evidence for nothing. | NOT-A-COUNT | `THE THREE ASK FACTS` are the code's own pinned set and `whatever today says` the hazard | — |
| `tools/unattended/unattended.sh:8666` | Two of 307 tracked CLOSED specs grade THIN today, both from a ---- pre-kit July build, and a term that reds a landed spec no run may rewrite is unlandable. | FROZEN | dated to 788908bcb (2026-08-31): `grade` made `graded` | `Two of 307 tracked CLOSED specs grade THIN`: only this file; quoted by 2 memory record(s), none a gate or test |
| `tools/unattended/unattended.test.sh:2202` | ---- no roster marker at all: today's output, today's sentence, and the caveat is then TRUE. | NOT-A-COUNT | `today's output` and `today's sentence` name the behaviour the arm pins | — |
| `tools/unattended/unattended.test.sh:2567` | ...and rung 4 sits BELOW rung 2, which is today's behaviour and is now said by an arm rather than by a sentence. | NOT-A-COUNT | `rung 4` and `rung 2` are labels and `today's behaviour` the ordering | — |
| `tools/unattended/unattended.test.sh:5288` | At this ---- unit's landing every LIVE kind is `surfaced`, so an implementation that counted every parked ---- line would satisfy any fixture built only from today's kinds — the fixture has to carry a kind ---- outside the taxonomy on purpose. | NOT-A-COUNT | dated to the unit's landing already; `today's kinds` names the taxonomy, not a count | — |
| `tools/unattended/unattended.test.sh:5309` | A second ---- spelling is correct today and silently wrong the moment a kind is added, and no runtime arm can ---- see the difference while every live kind is surfaced. | NOT-A-COUNT | `A second spelling` and `every live kind` describe a hazard and a condition, not a population figure | — |

Totals, counted from the rows above: 14 FROZEN, 1 POINTED, 23 REWRITTEN, 55 NOT-A-COUNT.

## Rows the census does not print

| Location | Sentence at the starting commit | Disposition | Reason, or the edit | AC6 |
|---|---|---|---|---|
| `.memory-tree.conf:577` | A cache here measures about 113 MB per worktree, and upstream measured ~110 MB per LIVE worktree, of which only 37.9% was evictable by the dead-worktree rule — hence a size budget rather than a liveness one. | FROZEN | the brief's row, outside the census's roots and carrying no marker; dated to 6e7022f3f (2026-10-05), `measures` made `measured` | `A cache here measures about 113 MB`: only this file; quoted by 1 memory record(s), none a gate or test |
| `tools/memory-recall/query.py:436` | under existence alone it kept its ~113 MB cache forever (TOOL-aMendedFleet-32, F2). | NOT-A-COUNT | past tense and attributed to the unit and finding that observed it, as the brief reads it; the census carries no marker for it either | — |

## At the tip (AC4)

The census run over the pass's working tree, after the edits, printed 55 candidates, and every one
is a NOT-A-COUNT row above, joined on path and sentence text: the 38 applied rows left the list and
nothing joined it. Its population line:

```
files by kind: sh 117 · py 75 · js 19 · hook 4
product: files 137 · paragraphs 10648 · candidates 40 · near-misses 0 · wide-only 772
test: files 78 · paragraphs 8795 · candidates 15 · near-misses 2 · wide-only 550
```

## AC5

`git diff 2a44284c -- <every touched file>` filtered with `grep -vE '^[-+][[:space:]]*(#|//|$)'`
leaves only docstring lines, in `map_lib.py`, `codebase-map/selftest.py`, `govkit.py`,
`govkit/selftest.py`, `gen_build_index.py`, `migrate_backlog.py` and `row_grammar.py`. A second
read placed every added and removed line inside a comment block or docstring the census itself reads,
in the new file and the old one: zero lines outside one. No `*.template.*` file was touched, so the
render half of AC5 has no pair to compare.

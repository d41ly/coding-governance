# Research: the lexicon kit, the kit as built and as enforced

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 27's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-8-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md`.

---

# Researcher A: the lexicon kit as built and as enforced (PLAY-dClosedLoop-1)

**The answer in short:**
- A name counts as an offender when its first subtoken is not in the 23-verb VERBS table. The kit has no class for names a third-party kit forces on you, and the advice it gives about them is wrong.
- The one binding check is a corpus count against a pin, run at the bar. Nothing checks at commit time.
- I recommend a set comparison at the bar instead: block only the offenders a branch adds that the base does not have. The bar already computes that comparison, but only to label a red, never to decide it.

All commands were run read-only from the worktree root.

## Inventory

### 1. Mechanics

| Key or part | Meaning | Where |
|---|---|---|
| `BANNED_SUFFIXES` | Rule P2: a type name ending in Manager, Helper, Util, Utils, Handler, Processor, Data or Info is an offender. A type named exactly `Manager` is not exempt. | `.lexicon.conf:17`, `lexicon.py:2967-2976` |
| `LANGS` | One `ext:pattern-set:mode` entry per extension. Mode is `parser`, `probe` or `dark`. An extension in the corpus but missing here is a refusal. | `.lexicon.conf:24`, `lexicon.py:2852-2856`, `lexicon_conf.py:486-498` |
| `VERB_OFFENDER_PIN` / `SUFFIX_OFFENDER_PIN` | Scalar pins on the unwaived counts. Today they must match exactly in both directions. | `.lexicon.conf:268-269`, `lexicon.py:3281-3293` |
| `ratified` | A free-text "date node" stamp. The only check is that it is not empty. | `.lexicon.conf:306`, `adopt-lexicon.sh:427-435` |
| `CELLS:` | `<ext>.<surface>[+kind:literal] <convention> [vocab]`. Surfaces are function, type, file and constant. Conventions are snake, screaming, camel, pascal, kebab and dark. | `lexicon_conf.py:41-42,217-286` |
| Selectors | `prefix`, `decorator` (parser languages only) and `returns:jsx` (`tsx-tokens` only). All three match on the name or the body, never the path. A name that matches two selectors is refused. | `lexicon_conf.py:72,436-461`, `lexicon.py:3687-3710` |
| `PINS:` | `<cell>.{conv,debt,unruled} N`. Two adjacent rows are refused. A pin row whose cell has no CELLS row is refused. A pin nothing reads is refused as UNREAD PIN. | `lexicon_conf.py:289-319,462-466`, `lexicon.py:3127-3139` |
| `PATTERNS:` | Adopter-declared regex extractors, exactly one capture group each. | `lexicon_conf.py:322-362` |
| `CANON:` and `canon_unfrozen` | An owner overlay on the shipped clusters. A stamp that carries no reason is refused. | `lexicon_conf.py:365-390`, `adopt-lexicon.sh:446-463` |
| `VERBS:` | `verb gloss — NOT \`token\``. A row with no negative is a refusal. So is a negative that is itself a row. | `lexicon.py:2834-2849`, `lexicon_conf.py:470-484` |
| Canon | 20 frozen clusters (120 spellings). It labels an offender DEBT (a rename exists) or UNRULED. It never decides whether a name passes. | `canon.py`, `lexicon.py:275-300,2945-2965` |
| Waivers | `tools/lexicon/lexicon-{verb,suffix}-waivers.txt`, keyed on the bare name across the whole corpus. The reason is optional. Both files are comments only, so the live count is 0. | `lexicon.py:2324-2337,3049` |

**How a verb is parsed.** Every language goes through `leading_verb`: strip leading underscores, split on case, `_` and digit boundaries, take the first subtoken in lowercase (`subtokens.py:30,39-48`). The extractor is what differs by language:

| Language | Extractor | Methods and nested functions graded? |
|---|---|---|
| py | `ast.walk` over every FunctionDef and ClassDef | yes, all (`lexicon.py:425-437`) |
| sh | tokenizer (`parse_shell_defs`) | functions (`lexicon.py:747`) |
| js | probe regex: `function` declarations and `const` arrow functions | no class members (`lexicon.py:142-148`) |
| ts / tsx | tokenizer | shipped, but this repo declares no ts or tsx row (`lexicon.py:117-119`) |

Under this parse, `__str__` grades as `str`, while `__init__` passes only because `init` happens to be in the table.

**CLI verbs** (`lexicon.py:4356-4428`):

| Verb | Reads | Prints or exits |
|---|---|---|
| bare or `--check` | conf, waivers, the whole tracked corpus | counts on green and on red; exits 1 on any pin mismatch or refusal |
| `--list` | same | every offender, waived or not |
| `--offenders` | same | `path TAB rule TAB identifier` keys, no line numbers; exits as `--check` does |
| `--measure` | same | the pin rows the current tree produces |
| `--suggest <n> --as <cell>` | conf and canon only, no corpus walk | one line; exits only 0 or 2 |
| `--expand` | corpus and canon | proposed clusters; writes nothing |
| `--merge-losses a..b` | git objects | exits 1 when a merge loses a definition |
| `--brief`, `--help` | nothing | usage text, exit 2. Neither mode exists any more. |

### 2. Enforcement points

| Point | Moment a name is judged | What it checks | On an offense |
|---|---|---|---|
| `/lexicon` Skill (`.claude/skills/lexicon/SKILL.md`, rendered from `SKILL.template.md`) | writing, if the agent asks | `--suggest` | advice only |
| `gov-builder` role (`.claude/agents/gov-builder.md:24-25`), `policy.toml:27-28` | writing | "Ask the repository's naming lexicon before you name a new function"; builders and spec-writers may run the naming-predicates leg | advice only |
| Kickoff and the handoff template (`tools/roles/handoff.py`) | none | zero `lexicon` mentions in `skills/session-kickoff/`; no lexicon or `--suggest` key in `handoff.py` | — |
| `.githooks/pre-commit` | none | it runs "cheap staged-scoped gates" (`:3`) but no lexicon | — |
| `.githooks/pre-push:923-952` | push | `--merge-losses` only: lost definitions, not naming | refused |
| Leg "lexicon naming predicates" (`gate-legs.json:1414-1435`) | the bar | full `lexicon.py`; guarded on `{prefix}/`, `skills/session-kickoff/`, `.githooks/`, `.claude/`, `.lexicon.conf` | red, or absorbed if the count still equals the pin |
| Leg "lexicon wiring" (`gate-legs.json:1451-1461`, `adopt-lexicon.sh:394-564`) | every bar (no guard) | the conf parses, `ratified` is not empty, VERBS is not empty, the canon stamp, the Skill render is in sync, and the full grade again (`:552-561`) | red |
| Leg "lexicon selftest" | the bar, kit changes only | the kit's own arms; in the `selftests` chunk, which `GATE_FULL` does not reach (`adopt-lexicon.sh:470-474`) | red |
| Red attribution (`run-gates.sh:4348-4350`) | the bar | the `--offenders` key set at the branch tip compared with the set at the base (INHERITED means the tip's set is a subset of the base's) | labels the red; decides nothing |
| `signal_lexicon_verbs_unused` (`drift_report.py:1245-1312`) | audit | declared verbs no definition uses | gateable |
| `signal_lexicon_ratified_stale` (`:1315-1350`) | audit | the `ratified` stamp is older than the last LANGS edit | gateable |
| `build_lexicon_marginal_offense_rate` (`:1434-1567`) | audit | offenders added per definition added since adoption; ignores waivers | report only (`gateable: False`) |

### 3. Exceptions

| Mechanism | Who may use it | Reason needed? | Is the reason checked? |
|---|---|---|---|
| Verb or suffix waiver | anyone; the file is `role="seed"` (`kit.toml:63-64`) | optional (`lexicon.py:2336`) | no. Only a stale waiver is refused (`:3050-3053`) |
| Scalar pin | anyone, by editing the conf | no; the reason lives in comments | no |
| Per-cell PINS row | anyone | no | no |
| Un-armed cell (`py.file`, `py.constant`) | owner, by edit | comment only (`.lexicon.conf:485-500`) | no |
| `dark` extension or cell | anyone | no | no |
| `ratified` | anyone | no | only that it is not empty |
| `CANON:` overlay | owner, per the conf comment | yes, date + node + reason | the shape only, by regex (`adopt-lexicon.sh:456`) |
| Ungradeable names (no word characters) | automatic | — | — |

**What the kit tells an agent to do with a name a third-party kit forces on it: nothing.**
- The Skill's "When a name genuinely will not fit" section gives three steps: re-read the function, check the negatives, then treat the table as wrong (`SKILL.template.md:68-76`). None of them covers a forced name.
- The only forced-name guidance anywhere is about the case convention, not P1: a member's name "is its container's KEY, spelled by the API that reads it" (`README.md:88-90`).
- The README's waiver section covers keying and staleness only (`README.md:644-650`).

### 4. How the vocabulary changes

- Anyone can edit `.lexicon.conf`. The edit is checked for shape only (the wiring leg) and by a full re-grade.
- Nothing checks the `ratified` stamp against an edit to VERBS. The staleness signal compares it only with LANGS edits (`drift_report.py:1340`).
- Four re-stamps record outright that "the seed itself was NOT re-curated" (`.lexicon.conf:279,291,297,301`).

## Sequence

How one name moves through the system today:

1. The agent may run `--suggest`.
2. It writes the name.
3. The commit runs no lexicon check.
4. At push, the bar runs the naming-predicates leg (if its guard matches) and the wiring leg (always).
5. If the count rose, the leg goes red and the author either renames or raises the pin with a written narrative. If the count fell, the author pastes the lower number.
6. Attribution may label the red INHERITED.
7. The drift audit reports the marginal rate afterwards.

At no step is an individual name refused. The judgement is always on a count.

## Measurements

```
$ python tools/lexicon/lexicon.py --check        # real 0m5.500s, rc=1
lexicon: verb offenders 1088 over pin 1087:
lexicon: sh.function.conv 6 of 2069 against snake — violation 4, ambiguous 2 ...
lexicon: UNDECLARED EXTENSIONS (declare each in LANGS, `dark` if nothing extracts it): html, svg
lexicon: P1 verb   graded=5710 offenders=1088 (debt=87 + unruled=1001) waived=0
lexicon: P2 suffix graded=66 offenders=0 waived=0
lexicon: coverage — armed 272 of 275 definition-carrying file(s) (98.9%)
```

- **The `html, svg` red** is this build's own records: `memory/builds/dClosedLoop/build/*-design-overview-*.{html,svg}`.
- **The +1 offender** does not come from this branch. `git diff --name-only ebce889c7 HEAD` lists no code file, and ebce889c7 is the merge base with origin/main. I did not measure main itself. Main has gained new definitions since 301a36664, the commit that set 1087.

```
$ python tools/lexicon/lexicon.py --offenders | cut -f2 | sort | uniq -c
      1 problem
      6 sh.function.conv
   1088 verb
```

43 of the verb offenders sit under `memory/builds/` (frozen records). The remainder by area: `tools/unattended` 273, `tools/memory-tree` 198, `tools/govkit` 155.

**Forced names among today's offenders:**
- `boundedParallel` ×9 and `chunk` ×8, all forced by `tools/hooks/agent-cap.js`.
- `__str__` ×1, in the lexicon kit's own `Offender` class (`lexicon.py:256`).
- Dunder offenders in total: 1.

**What `--suggest` tells an agent about framework names** (each exited 0):

| Name | Advice | Effect |
|---|---|---|
| `get_queryset` | "use `read_queryset` — the declaration says `read`, NOT `get`" | breaks the Django override |
| `do_GET` | "use `cmd_get`", then re-cased to snake | breaks `BaseHTTPRequestHandler` dispatch |
| `visit_Call` | "SCOPING question", then "re-cased to snake" | breaks `NodeVisitor` dispatch |
| `__str__` | "`str` is not in the declared table … SCOPING question" | no usable answer |

**Vocabulary history (git):**

| Measure | Result |
|---|---|
| Commits touching the conf since b06261529 (2026-08-16) | 55 |
| Commits changing the `VERB_OFFENDER_PIN=` line | 31 |
| Commits changing a VERBS row | 4, and only one changed the verb set: `cmd` added in 95737bc85 (22 → 23 verbs). The other three edited glosses. |
| `ratified` changes | 6, all re-stamps for `dark` LANGS entries |
| CELLS or PINS row changes | 2 |
| Renames of graded files (since 2026-08-16) | 5, out of 1,897 commits touching graded files |

**Reader probe** (a scratch conf in the scratchpad: a PINS block with one row, a later empty `PINS:`, then two VERBS blocks):

```
PINS {}
VERBS ['load']
```

A repeated block header silently replaces the earlier block. The live conf already carries a stray empty `PINS:` at `.lexicon.conf:451`, inside comment prose. It is harmless today only because the real block comes later, at `:510`.

**Calls to modes that no longer exist:** `--brief` and `--help` both exit 2. With the handed counts of 54 and 76, about 130 of 2,324 Bash invocations went to these.

## Gaps

| # | Gap | Evidence |
|---|---|---|
| G1 | No class for forced names. P1 grades every extracted function, and no CELLS row can switch it off (`lexicon.py:3815-3822`). A selector routes only the case convention. | probe above |
| G2 | `--suggest` advises renames that break a framework override. | probe above |
| G3 | A waiver needs no reason, and nothing checks one. The key is the bare name, so it waives every copy in the corpus; that is why the waiver was refused for `boundedParallel` (`.lexicon.conf:178-179`). | `lexicon.py:2336,3049` |
| G4 | A count cannot see substitution: one fixed offender plus one new one nets to zero. The engine admits this itself (`lexicon.py:3486-3488`). | `check_pass:3281-3293` |
| G5 | Records are in the graded population. 43 verb offenders sit under `memory/builds/`, the pin "absorbs" them (`.lexicon.conf:262-267`), and this branch is red on `html, svg`. | measured |
| G6 | Every drain or raise forces a hand-written narrative. Nine RECONCILED or RE-MEASURED entries record merge-time re-measurement. | `.lexicon.conf:83-267` |
| G7 | Nothing judges a name at commit time, or at all before the bar. | hooks, legs |
| G8 | `ratified` certifies nothing about VERBS edits. | `drift_report.py:1340` |
| G9 | The reader accepts a repeated block header and keeps only the last one. | probe |
| G10 | Records disagree with the code and the settled design. The Skill says a non-fitting name is refused ("or the gate refuses it", `SKILL.template.md:10-11`), but the gate absorbs it up to the pin. The conf and the waiver headers say "TWO-SIDED EQUALITY" (`.lexicon.conf:55-60`), while the README calls waivers "Shrink-only" (`README.md:650`) and the settled design defaults to `shrink-only`. | as cited |

## Candidates: where enforcement sits

| | C1: diff-scoped check at commit | C2: corpus count against a pin at the bar (today) | C2′: offender set compared with the base, at the bar | C3: vocabulary handed at the point of naming |
|---|---|---|---|---|
| **Mechanism** | A new staged-scoped arm in `.githooks/pre-commit`: extract the definitions in staged files and refuse any added or renamed name that offends. | The length of the unwaived offender list must match `VERB_OFFENDER_PIN` (shrink-only under the settled design). | Red when the tip's `--offenders` keys are not a subset of the base's. This reuses `render_offender_keys` (`lexicon.py:3482-3515`) and the subset classifier the bar already runs (`run-gates.sh:4348-4350`). | The work order carries the VERBS rows, the `--suggest` answers and the forced-name exemptions for the item's new names. |
| **Test that could make it lose** | (a) Over the last 60 days, more than 2 s per commit; (b) merge commits refusing names the committer did not write; (c) `--no-verify` bypass, which the hook advertises (`pre-commit:67`). | Rename one offender to a declared verb and add one new offender on one branch: if the leg is green, C2 loses. | (a) A file move makes inherited offenders look new: count false reds over the last 60 days of merges. (b) A forced name added with no declarable exemption is an unfixable red. | Builder-added definitions offend at a rate no lower than the 584/4,948 (11.8%) baseline; or the handed advice is wrong. |
| **Result** | Not run, because it needs a build. (b) is structural: the diff of a merge commit carries the other parent's names. (c) holds by reading the hook. The cost side is unproven; the whole corpus takes 5.5 s. | **Loses, by reading the code.** `check_pass` compares only `len(unwaived)` with the pin (`:3281-3293`), and the engine's own docstring (`:3486-3488`) says a count misses this case. Also lost on history: 412 → 1,087 with records absorbed. | (a) **Survives as measured:** 5 renames of graded files in 1,897 commits, so the false-new rate is bounded and small. (b) **Loses until G1 is closed:** `visit_Call`, `do_GET` and `get_queryset` would be unfixable reds. | **Loses as the sole mechanism.** Units "asked AFTER they were first written" (`.lexicon.conf:165-167,196-197,212-214`), and `--suggest` gives wrong forced-name advice. It cannot refuse anything. Its effect is not yet measured. |

C4, enforcement by the audit signal alone, is rejected. Its losing test: does the marginal rate drive any refusal? No; it is report-only (`drift_report.py:1567`, `gateable: False`).

## Pick

I recommend **C2′ as the binding check, C3 as the supply, and the shrink-only C2 count kept as the backstop** the settled design already provides.

C2′ is the only candidate that:
- judges exactly the names a branch adds, with no exposure to substitution or pin arithmetic;
- extends a seam that already exists: the `--offenders` signature plus the subset classifier, today used only to label a red;
- binds at the bar remote CI runs, where `--no-verify` cannot reach it.

It owes two things before it can bind:
1. **A declared forced-name class (G1).** Without it, the losing test in (b) holds. The class's shape belongs to researcher C.
2. **A path selector that keeps `memory/builds/**` out of the population** (G5, `TOOL-aSurfacedLexicon-23`).

The build must run C2′'s own losing test first: replay the merges since 2026-08-16 through the subset rule, and count the reds that come from moved or renamed files rather than new names. If that count is not near zero, the keys need a move-aware form.

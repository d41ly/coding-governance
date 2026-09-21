**Serves:** diff-review TOOL-aBlindedTrial-7 TOOL-aBlindedTrial-8 KICK-aBlindedTrial-1

# Closing diff review, round 1 — aBlindedTrial units 7, 8 and KICK-1: the project-wide spec-audit default, the guards join, the kickoff question

Node `a` · 2026-09-21 · Tier-2 · on `branch/spec-audit-followups` · adversarial fan through `tier2-review.js` (4 finder lenses → 5 skeptic batches → this synthesis). Every confirmed finding below was re-read at source and, where it names behaviour, re-executed in this synthesis before it was adjudicated: the hook driven with ten crafted conf spellings, the driver's line-1539 idiom sliced verbatim and run under `set -u` against nine blob shapes, the checker run over four fixture repos and in `--list` mode over the live corpus, the manifest measured for guard breadth. Nothing was taken from the skeptic's word alone.

**Reviewed range:** `0e61932de7183008cc040c2a009b701993b00a74...HEAD` — **ROUND 1**. HEAD is `144cd1fb196e`; the base resolves (`git cat-file -t` → commit) and is the landing of units 2–5. Four commits, 49 files, +1242/−176: the three specs, `unattended.sh` (+`SPEC_AUDIT_DEFAULT` at BASE, fail 54, `AUTH_SPEC_AUDIT_FROM`, the third preflight spelling), `agent-cap.js` (+`readSpecAuditDefault`, the worktree-conf fallback in rule 0), `check-spec-tokens.py` (+the guards join behind `SPEC_GUARD_LEGS_CUTOFF`), `SKILL.md` (Step 3 question, Step 5 `## open` line, Step 5b sentence), the four conf carriers, the protocol and Skill renders, three test files, the dossiers and version markers.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing. The three units do what their specs say: a dated conf default at BASE opts a silent-README build in and `--close` blocks on it (AC1, AC4 arms green in the driver slice), a non-date is refused at both readers (fail 54; hook deny), a malformed README key still wins (fail 52), the guards join reds a post-cutoff spec that omits a tripped deep-guarded leg and stays quiet on a one-segment guard, and the kickoff engine asks once and records the answer. `check-spec-tokens.test.sh` is 55/55 and `agent-cap.test.sh` 294/294 at HEAD. What this round finds is one predicate that reaches the wrong population and a set of seams between the units and the carriers they did not touch: the guards exclusion is written on guard DEPTH while its rationale is guard BREADTH, so on the real manifest `tools/lib/` (30 legs) is joined and `.githooks/` (5 legs) is excluded — one HIGH, arming tomorrow. Five MEDIUMs: the BASE-conf read fails open whenever the eval'd blob ends before the read (`return`, an unbound variable, a syntax error), a declared directory under `### Files touched` is dropped before the join with no NEAR row, the join reds a Tier-1 spec that has no Gates heading while the template says such a spec is not graded, the build method still names one opt-in source where the driver now owes on two, and all three specs of this very diff omit legs their own files-touched trips. Six LOWs are wording, a regex edge, one unobserved predicate branch and a count typed in prose five times. Every fix is a few lines plus an arm; the units are INPROGRESS, so they fold before the close.

## Review shape

Raw **24** · confirmed **21** · refuted **3** · unverified **0** · precision **0.88**.

Precision is well above the 0.5 floor §8 sets. The twenty-one confirmed collapse to **12 items**: five groups reported the same defect with the same repro from different lenses (ids 1, 15 and 17 · ids 5 and 14 · ids 9, 12 and 18 · ids 6, 13 and 19 · ids 7 and 21 · ids 4 and 22), and those merges are mine, at write time; the pipeline discarded no duplicates. The three refuted (ids 3, 8 and 20) did not reach this synthesis as text, only as the count, so they are not re-adjudicated here.

Adjudicated, by item: **0 BLOCKER · 1 HIGH · 5 MEDIUM · 6 LOW** (12 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 1 HIGH · 10 MEDIUM · 10 LOW** (21 findings; every id takes the severity of the item that holds it — ids 15 and 9 were rated low by their finders and take the MEDIUM of R2 and R5, and id 13 was rated medium by its finder and takes the LOW of R7, each for the reason its item states).

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so a zero in this report is evidence of absence and not of a hole. The six duplicate groups were judged by hand in this synthesis, as stated above.

What this synthesis ran, per the lens instruction. `node tools/hooks/agent-cap.js` against a scratch tree (`sarepo/memory/builds/tSA/README.md` carrying no key) with ten conf spellings: double-quoted, `=2026-09-21#c`, `"2026-09-21"; X=1`, single-quoted with a trailing comment, the date followed by `return 0`, the date followed by `X="$UNSET"`, `"later"`, bare `=`, indented `export`, `=$OTHER`. The line-1539 idiom `_sad=$( SPEC_AUDIT_DEFAULT=""; eval "$_cf" >/dev/null 2>&1; printf '%s' "${SPEC_AUDIT_DEFAULT:-}" )` copied byte-for-byte into a function under `set -u` (bash 5.3.9) and run against nine blob shapes, the subshell status captured beside the value. `python tools/check-spec-tokens.py` over four fixture repos (a backdated setting commit so the cutoff relation holds; manifest `tools/x/` + exact-file `tools/x/thing.sh`): a spec with no Gates heading, a spec declaring the directory `tools/x/`, a spec declaring `tools/x/thing.sh.bak`, a spec declaring `tools/x/thing.sh`; and `--list` over the live corpus at HEAD (264 `NEAR [guards]` rows). `tools/gate-legs.json` walked for legs-per-guard. `bash tools/check-spec-tokens.test.sh` — **55 assertions, exit 0**. `bash tools/hooks/agent-cap.test.sh` — **294 passed, 0 failed**. `gotchas.py --for-diff 0e61932d..HEAD` — 51 classes by anchor + 5 universal. The engine's three additions read against Steps 3, 5 and 5b of `SKILL.md` and against the method carrier they grep. The bar and the driver suite whole were not run, as instructed; the driver's new slice (`unattended.test.sh:5728-5829`) was read, not run. All suite output went to files and was grepped, never read through `tail`.

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| R1 | HIGH | 10 | `tools/check-spec-tokens.py:242` | The guards exclusion tests guard DEPTH (`count('/') == 0`) where the design names guard BREADTH: `tools/lib/` (30 legs) is joined, `.githooks/` (5 legs) is excluded. |
| R2 | MED | 1, 15, 17 | `tools/unattended/unattended.sh:1539` | The BASE-conf eval fails OPEN: a `return`, an unbound variable, a syntax error or an `exit` in the blob ends the subshell before the read, `_sad` is empty, and the case reads "no default". |
| R3 | MED | 2 | `tools/check-spec-tokens.py:333`, `:485` | A directory token under `### Files touched` (`tools/run-gates/`) is dropped by the trailing-slash rule before the join and announced by no NEAR row; writing the folder instead of the files satisfies the arm. |
| R4 | MED | 5, 14 | `tools/check-spec-tokens.py:490` | The guards join has no Gates-heading precondition: a Tier-1 spec with no `## N. Gates` gets one hit per tripped leg while the same run counts it under "carry no Gates heading to grade". |
| R5 | MED | 9, 12, 18 | `tools/memory-tree/BUILD-METHOD.template.md:116` (render `memory/guides/BUILD-METHOD.md:116`); `tools/unattended/SKILL.template.md:100` | M4's **When** clause still names ONE opt-in source; the driver now owes on two; the kickoff engine greps this carrier. |
| R6 | MED | 11 | `…spec-TOOL-aBlindedTrial-7.md:135`, `…spec-KICK-aBlindedTrial-1.md:94`, `…spec-TOOL-aBlindedTrial-8.md:124` | All three specs omit legs their own §4 files-touched trips — 15 `NEAR [guards]` rows at HEAD, grandfathered by the one-day cutoff. |
| R7 | LOW | 6, 13, 19 | `skills/session-kickoff/SKILL.md:152-157`, `:206` | Step 3 asks the spec-audit question without consulting `SPEC_AUDIT_DEFAULT`; under a dated default a "no" writes nothing and the card records `not declared (owner)` while preflight prints `opted in by project default`. |
| R8 | LOW | 7, 21 | `tools/hooks/agent-cap.js:1774` | `SPEC_AUDIT_DEFAULT=2026-09-21#c` reads as the date at the hook (admit) and as `2026-09-21#c` in the shell (fail 54); `"2026-09-21"; X=1` reads as no assignment at the hook (deny) and as the date in the shell. |
| R9 | LOW | 4, 22 | `tools/unattended/PROTOCOL.template.md:489`; `.unattended.conf:192-193`; `tools/unattended/.unattended.conf.example:204-205` | "a YYYY-MM-DD date FROM WHICH every build owes the audit" — the value is compared to nothing; any date is an unconditional opt-in for every silent-README build. |
| R10 | LOW | 16 | `tools/unattended/unattended.sh:3951` | The owed-but-unevidenced sentence attributes the opt-in to "its spec-audit: key" although the build may owe it through the conf with no README key; `AUTH_SPEC_AUDIT_FROM` is in scope and unused here. |
| R11 | LOW | 23 | `.memory-tree.conf:283`; `tools/check-spec-tokens.py:57`; `tools/memory-tree/SPEC-TEMPLATE.template.md:195` (render `memory/TEMPLATE-SPEC.md:195`); `memory/map/features/spec-tokens.md:83` | "eleven legs guard bare `tools/`" — a manifest-derived count typed into prose in five carriers; the checker derives `broad` at runtime and never prints its size. |
| R12 | LOW | 24 | `tools/check-spec-tokens.test.sh:372` | Every guards arm uses the `tools/x/` directory guard against `tools/x/thing.sh`; the `path == guard` branch and the docstring's `x.sh.bak` non-prefix claim are observed by no arm. |

### R1 — HIGH · the exclusion predicate is depth, the rationale is breadth (id 10)

`tools/check-spec-tokens.py:232-244`:

```python
for g in r.get("guard") or []:
    if g.rstrip("/").count("/") == 0:
        broad.add(g)
    else:
        deep.append(g)
```

The header (`:56-58`), the spec's §8 F1 and `.memory-tree.conf:283-284` all give one reason for excluding a guard: eleven legs carry bare `tools/`, so a rule that owes eleven names per spec "is obeyed by paste and read by nobody". That is a statement about how many legs share a guard. The predicate reads how many slashes the guard has. Measured over `tools/gate-legs.json` at HEAD, legs per guard: `tools/lib/` **30** (depth 1, JOINED) · `tools/` 11 (depth 0, excluded) · `tools/memory-tree/` 9 (joined) · `tools/run-gates/` 6 (joined) · `tools/hooks/` 5 (joined) · `tools/memory-recall/` 5 (joined) · `.githooks/` **5** (depth 0, EXCLUDED, carried by `branch-guard self-test`, `pre-push self-test`, `pre-push run-log line`, `push-main self-test`, `lexicon naming predicates`). The one-segment set is exactly `.claude/ .githooks/ memory/ tools/`.

So on the real manifest the proxy produces both failure directions. A post-cutoff spec touching `tools/lib/resolve-python.sh` owes thirty leg names — the outcome F1 rejected at eleven, nearly three times over, for the most-edited shared directory in the tree. And `.githooks/pre-push` owes nothing although two self-tests guard exactly that directory, so the motivating class (touch a guarded file, omit its self-test) is unreachable for a hook edit. `SPEC_GUARD_LEGS_CUTOFF` is `2026-09-22` (`.memory-tree.conf:309`), so this arms on the next spec written. The brief's by-design note covers "one-segment guards excluded"; it does not cover the predicate selecting a population the design did not describe. Classes: `allowlist-narrower-than-the-root-it-guards` (both directions), `two-answers-to-one-question` (header versus predicate).

Why HIGH and not BLOCKER: no spec at HEAD is dated at or after the cutoff, so nothing reds today, `--list` shows what would, and the fix is a predicate plus arms. Why not MEDIUM: the gate's stated property is contradicted by its own code on the first manifest it runs against, and one of the two outcomes is a false green for the exact class the unit was built to catch.

**Fix.** Derive `broad` from breadth. In `derive_guarded_legs`, count legs per guard while walking `rows`, then exclude a guard carried by more than a file constant (`BROAD_LEG_FLOOR`, stated in the header and printed on the report line) whatever its depth, and keep every narrower guard whatever its depth. Pick the floor from the measured distribution above, with the constraint that `tools/hooks/` (5) — the motivating case — stays joined: a floor of 5 excludes `tools/lib/ tools/ tools/memory-tree/ tools/run-gates/` and joins the rest, `.githooks/` included. Print the excluded set WITH its per-guard counts on the `guards join` line so the exclusion announces itself (this also discharges R11). Update the header, the conf comment, the TEMPLATE-SPEC §7 paragraph and the dossier. The AC4 arm's fixture guard `tools/` is carried by one leg and would no longer be excluded; its fixture needs floor+1 legs sharing one guard.

**Left-shift.** Two arms in `check-spec-tokens.test.sh`, observed RED first: a two-segment guard carried by floor+1 legs → NEAR, no hit; a one-segment guard carried by one leg → `[guards]` hit. Re-run `--list` over the live corpus before wiring and record the excluded set in the spec's §9.

### R2 — MEDIUM · the BASE-conf read fails open when the eval does not finish (ids 1, 15, 17)

`tools/unattended/unattended.sh:1539`:

```sh
_sad=$( SPEC_AUDIT_DEFAULT=""; eval "$_cf" >/dev/null 2>&1; printf '%s' "${SPEC_AUDIT_DEFAULT:-}" )
```

The subshell inherits the driver's `set -u` (`:42`), the eval's status is discarded, and `$(...)`'s status is never read. Reproduced with the line copied byte-for-byte into a function under `set -u`, bash 5.3.9, blob → `_sad` / subshell rc:

- `SPEC_AUDIT_DEFAULT="2026-09-21"` → `2026-09-21`, rc 0 (control).
- …followed by `return 0` → **empty**, rc 0.
- …followed by `X="$UNSETVAR"` → **empty**, rc 1.
- `X="$UNSETVAR"` then the key → **empty**, rc 1.
- a syntax error above the key → **empty**, rc 0 (the eval fails, `printf` still runs, the variable was never assigned).
- …followed by `exit 0` → **empty**, rc 0 (the case the comment at `:1535-1536` sanctions).

Every empty value falls into the `"") ;;` arm at `:1541` and the run grades `specs-audited` as `not owed` at `:3916-3917` with a sentence asserting that "the project conf at BASE declares no SPEC_AUDIT_DEFAULT". That is the read-as-absent opt-out fail 52 and fail 54 exist to refuse, through the one path the diff left ungraded: the comment names only `exit`, spec S1 names only "an absent blob or blank key" as undeclared, and no arm in the U7 slice (`unattended.test.sh:5728-5829`) stages a dying eval. The hook reads the same bytes with a regex and sees the date, so the two readers disagree in the direction that lets an owed audit go unrecorded.

Reachability differs by shape, and that is why this is MEDIUM. The unbound-variable and syntax-error blobs also kill the driver at `. "$CONF"` (`:348`) when the working copy carries them, so they need a BASE conf that differs from the branch's — a conf that broke `main` and was repaired on the branch. The `return 0` shape needs no divergence: a top-level `return` in a `.`-sourced file is legal and stops the source (verified: `. conf` with the key then `return 0` sets the variable and returns 0), so the SAME bytes read as the date at `:348` and as absent at `:1539`. Class: `fallback-fabricates-the-passing-value`, `swallowed-delegate-reads-as-clean`.

**Fix.** Make the subshell prove it finished and that the eval succeeded, in one line:

```sh
_sad=$( SPEC_AUDIT_DEFAULT=""; eval "$_cf" >/dev/null 2>&1 && printf 'OK %s' "${SPEC_AUDIT_DEFAULT:-}" )
case "$_sad" in
  "OK "*) _sad=${_sad#OK } ;;
  *) fail 55 "the project conf at the pinned BASE could not be evaluated to the end, so whether it declares SPEC_AUDIT_DEFAULT is unknown and is not read as absent"; return 1 ;;
esac
```

Then the existing `case "$_sad"`. This covers all four modes: a failed eval never reaches `printf` (`&&`), and a `return`, `exit` or unbound death leaves the subshell before it. It also turns the sanctioned `exit` case into the refusal; that is the right outcome — "unknown" is not "absent" — but it changes a sentence the comment and the spec's checklist state, so the fold rewrites both.

**Left-shift.** Three arms in the U7 slice, RED first: a BASE conf declaring the date then `return 0` → `hit` fail 55, `miss` `not owed`; the date then an unbound reference (branch conf repaired) → fail 55; a syntax error above the key → fail 55. Add `return` to the comment's list of ways the blob can end early.

### R3 — MEDIUM · a declared directory declares nothing, silently (id 2)

`check_path_shaped` (`:318-335`) returns False for any token ending in `/` ("prose about path normalisation, not a path"), and `extract_files_touched` (`:205-222`) routes every files-touched token through it before the guards join at `:485`. So `tools/run-gates/` under `### Files touched` contributes nothing. Reproduced on a fixture: a post-cutoff spec declaring `` `tools/x/` `` against a leg guarded on `tools/x/`, leg omitted → exit 0, `guards join · 0 declared path(s) examined in 1 live spec(s)`, and `--list` prints no row naming `tools/x/` (the near loop at `:507` iterates the already-filtered `declared`). The header says the join "reads a guard as a directory or an exact file"; it does not say a declared directory is not read at all.

Measured over the corpus at HEAD: 77 (spec, leg) pairs where a declared directory token equals or contains a deep guard — `aGradedDoorway-7` (INPROGRESS) declares `tools/run-gates/` and names none of `run-gates turnstile`, `run-gates gov canary`, `run-selftests self-test`, `profile-bar selftest`; `aQuarriedLantern-1` (INPROGRESS) declares `tools/memory-recall/` over five legs. Post-cutoff, writing the folder instead of the files is a clean pass indistinguishable from coverage. Class: `containment-tested-one-way`, `green-by-absence`.

**Fix.** In `extract_files_touched`, keep a token that ends in `/` and carries two or more segments as a declared PREFIX (skip it only in the path and cite joins, where the trailing-slash rule is right). Make `check_guard_trips` symmetric for a prefix: with `p` and `g` both `rstrip('/')`, trip when `p == g`, `p.startswith(g + '/')`, or the declared token was directory-shaped and `g.startswith(p + '/')`. State the directory rule in the header.

**Left-shift.** Two arms, RED first: `` `tools/x/` `` against guard `tools/x/` → hit; `` `tools/` `` against guard `tools/x/` → hit (the declared root contains the guard). Raise `FLOOR_ASSERTIONS` by two.

### R4 — MEDIUM · the join grades a spec the template says is not graded (ids 5, 14)

The no-heading branch at `:414-420` sets `gates = ""`, `noheading += 1` and leaves `named` empty; the guards loop at `:490` has no `extract_gates(text) is not None` precondition, unlike the legline arm at `:448`. Reproduced on a fixture: a Tier-1 spec dated after the cutoff with `### Files touched (estimate)` naming `tools/x/thing.sh` and no Gates heading → exit 1 with `[guards] guarded leg <- tools/x/thing.sh` and `[guards] exact leg <- tools/x/thing.sh`, while the same run prints `1 carry no Gates heading to grade`. `memory/TEMPLATE-SPEC.md:178` says "A spec carrying no Gates heading at all is not graded" and `:186-188` calls the heading precondition "the whole of the Tier-1 accommodation"; the new paragraph at `:190-198` says "the leg line must ALSO name", presupposing a leg line. The U8 spec never decides the case. Zero live specs carry the sub-head without a Gates heading today, so no red lands at HEAD; from `2026-09-22` a format-legal light spec reds. This is the class `TOOL-aJoinedCanon-7` fixed for the legline arm. Class: `two-answers-to-one-question`.

**Fix.** Mirror the legline arm: compute `missing` only when `extract_gates(text) is not None`, count the others on the guards report line (`· N carry no Gates heading`). If the demand on a Tier-1 spec is intended instead, say so in the TEMPLATE-SPEC paragraph and the header's "WHAT THIS DOES NOT CHECK" block — but the template's own accommodation sentence argues against it.

**Left-shift.** One arm, RED first: the no-heading fixture above → exit 0 and the count on the report line.

### R5 — MEDIUM · the build method names one source, the driver owes on two (ids 9, 12, 18)

`tools/memory-tree/BUILD-METHOD.template.md:114-116` and its render still read: "**When**, and `specs-reviewed` is owed only then: the build README's front matter carries `spec-audit: <date>`. Undeclared, none is owed". This diff changed only the `memory-tree@2.82` marker in both files (2 lines each, `git diff --stat`). `tools/unattended/SKILL.template.md:100` still reads "when the build declares it". Meanwhile `PROTOCOL.template.md:351` and `:489`, the `unattended` Skill and `unattended.sh:1537-1546` all owe the audit under `SPEC_AUDIT_DEFAULT` with no README key, and `--close` blocks on it (AC4 arm). U7's S5 lists the MUST comment, the Skill, the protocol and the dossier as the prose it updates; the build method is neither listed nor named as a non-goal, so it is a missed carrier. Two consequences: an attended session following M4 in a defaulted project skips an audit the driver later demands at `--close`; and `SKILL.md:153` greps this very carrier to decide the question is worth asking. Class: `two-answers-to-one-question`.

**Fix.** One clause in M4's **When** sentence, template and render in one commit (the `kit/dogfood doc parity` leg holds the pair): "…carries `spec-audit: <date>`, or the project's `.unattended.conf` at BASE declares a dated `SPEC_AUDIT_DEFAULT` and the README declares no key (TOOL-aBlindedTrial-7). Under neither, none is owed…". Widen the `specs-reviewed` row in `SKILL.template.md:100` to "when the build or its project declares it" and re-render.

**Left-shift.** None machine-shaped; the parity leg keeps the renders paired. Add the build method to U7's S5 list in the spec's rev-2.

### R6 — MEDIUM · the three specs are the class the gate was built for, one day early (id 11)

`python tools/check-spec-tokens.py --list` at HEAD prints exactly 15 `NEAR [guards]` rows for these specs, each `predates SPEC_GUARD_LEGS_CUTOFF 2026-09-22`: U7 declares `tools/hooks/agent-cap.js` and `tools/hooks/scratch-guard.js` (guard `tools/hooks/`, 5 legs) and its §7 (`:135`) names only `agent-cap self-test` — missing `scratch-guard self-test`, `verifier fan-out self-test`, `review-join self-test`, `hook destinations self-test`; KICK-1 declares `skills/session-kickoff/SKILL.md` (guard `skills/session-kickoff/`) and its §7 (`:94`) names none of `manifest-check self-test`, `scratch-guard self-test`, `lexicon naming predicates`; U8 declares `tools/memory-tree/.memory-tree.conf.example` and its §7 (`:124`) names none of the eight `tools/memory-tree/`-guarded self-tests. U7 is the literal motivating case from round 1's F7: it edits `scratch-guard.js` (the diff touches it) and omits `scratch-guard self-test`. The day-after cutoff is by design per the conf's relation rule, but that only means the gate cannot grade these specs, not that they are correct — the closing review is again the only reader. Records-only. Class: `hand-named-gate-list-green-while-the-bar-reds`.

**Fix.** Name the tripped legs on each §7 line, bump each spec's rev and log it in §9. If R1 lands first with a floor of 5, `tools/memory-tree/` (9 legs) leaves the join and U8 owes nothing; U7's four and KICK-1's three stand under any floor that keeps the motivating case.

**Left-shift.** The gate itself, from tomorrow. Nothing more.

### R7 — LOW · the engine asks a question whose answer cannot change the outcome (ids 6, 13, 19)

`skills/session-kickoff/SKILL.md:152-157` gates the question only on `grep -q 'spec-audit:'` over the method carrier and mentions neither `.unattended.conf` nor `SPEC_AUDIT_DEFAULT` (grep over the engine: no hit). Under a dated default: the engine asks, may recommend "no" for a one-unit build, a "no" writes nothing, Step 5 (`:206`) records `spec audit: not declared (owner)`, and the driver's preflight (`unattended.sh:2970-2971`) prints `opted in by project default` while the hook admits from the worktree conf. U7 §3 states there is no per-build opt-out under a default, so the offered "no" is a no-op the card then misrecords. Both units shipped in this diff to the same adopters. LOW, not the MEDIUM id 13 carried: gov's own conf is blank (F1), the binding records — the pinned `spec-audit` fact and the preflight line — are correct, and only the convenience card misstates. Class: `two-answers-to-one-question`.

**Fix.** One clause on the Step 3 guard: when `<repo>/.unattended.conf` declares a dated `SPEC_AUDIT_DEFAULT`, do not ask; write `spec audit: project default <date>` on the `## open` line (a third spelling beside the two Step 5 defines). The engine is 18187 bytes against an 18432 cap — 245 bytes of headroom, enough for one sentence. Add the third spelling to KICK-1's AC3.

**Left-shift.** `check-template-size.sh` holds the cap; AC3's grep gains the third spelling.

### R8 — LOW · a glued `#` reads as a comment at the hook and as a word in the shell (ids 7, 21)

`tools/hooks/agent-cap.js:1774`: the bare alternative `([^\s#]*)` stops at `#` and `\s*(?:#.*)?$` swallows the rest. Reproduced on identical bytes. `SPEC_AUDIT_DEFAULT=2026-09-21#c` → hook exit 0 (admit); shell `_sad=2026-09-21#c` → fail 54. `SPEC_AUDIT_DEFAULT="2026-09-21"; X=1` → hook null → exit 2 (deny); shell → the date. The header at `:1742-1743` claims the reader is kept honest by taking the spellings the shell does; these are two spellings where it does not, one in the permissive direction. Spelling unusual, severity low, divergence real. Class: `two-readers-of-one-config-one-re-derived`.

**Fix.** Let a bare word run to whitespace and require whitespace before a comment: `(?:"([^"]*)"|'([^']*)'|(\S*))(?:\s+#.*)?\s*$`. The `;`-joined line then still reads as no assignment (deny — the safe direction); state that in the header as a second limit beside the bare `spec-audit:` line.

**Left-shift.** Two arms in `agent-cap.test.sh` beside the trailing-comment allow: `=2026-09-21#note` → deny naming `SPEC_AUDIT_DEFAULT` and `not a date`; `"2026-09-21"; X=1` → deny (documented).

### R9 — LOW · "from which" beside a value compared to nothing (ids 4, 22)

`PROTOCOL.template.md:489`, `.unattended.conf:192-193` and `.unattended.conf.example:204-205` all describe the key as "a YYYY-MM-DD date from which every build owes the pre-code spec audit". Every sibling row in that table (`PASS_ORDER_CUTOFF`, `BRIEF_RECORDED_CUTOFF`, `SPEC_THIN_CUTOFF`) opens with the same phrase and then names its grading anchor (`opened:` date, spec FILENAME date); this row names none because there is none — the driver's `case` at `:1540-1545` and the hook's `/^\d{4}-\d{2}-\d{2}$/` test presence and shape only. An adopter who sets a future date expecting the phased rollout the sibling keys grant opts every open build in on landing day. The spec's own data model calls the value "the day the project ruled audits on" — a record, not a threshold. Class: `two-answers-to-one-question`.

**Fix.** Prose, in one commit across the three carriers (check 22 holds the protocol and its render in lockstep): "OPTIONAL: a YYYY-MM-DD date recording the day the project ruled audits on. Any dated value opts EVERY build in whose README declares no key, for every run whose BASE carries it; the date is a record, not a threshold, and is compared to nothing." Grading it as the siblings are graded (owe only when the README's `opened:` is at or after the value) is the alternative; pick one and make the row say which.

**Left-shift.** None; check 22 keeps the pair.

### R10 — LOW · the unevidenced-audit sentence names a key the build may not have (id 16)

`unattended.sh:3951` reads "the pre-code review pass this build opted into with its spec-audit: key left no evidence". Under `AUTH_SPEC_AUDIT_FROM=project` the path is reachable (AC4's arm drives exactly it: `init_sa_run` then `git rm --cached audit.md`) and the operator is told to look for a README key that does not exist. The fail-53 sentence (`:3913`), the not-owed `DOD_OUT` (`:3917`) and the preflight line were all widened to both sources; this one was not, though `AUTH_SPEC_AUDIT_FROM` is in scope. The AC4 arm asserts `specs-audited` and the unit id only, so the wording was never checked.

**Fix.** Drop the attribution and name the date: "the pre-code review pass this build owes (spec-audit $AUTH_SPEC_AUDIT, from ${AUTH_SPEC_AUDIT_FROM:-readme}) left no evidence".

**Left-shift.** The AC4 arm gains a `hit` on `from project`.

### R11 — LOW · a derived count typed into prose, five times (id 23)

"eleven legs guard bare `tools/`" at `.memory-tree.conf:283`, `tools/check-spec-tokens.py:57`, `tools/memory-tree/SPEC-TEMPLATE.template.md:195`, its render `memory/TEMPLATE-SPEC.md:195`, and `memory/map/features/spec-tokens.md:83`. The figure is right today (11, measured above) and nothing compares any of the five sentences to the manifest; `derive_guarded_legs` computes `broad` at runtime and never prints its size. The charter's §7 rule is "NO count of a derived population is written in prose". Present tense and undated, so the next leg to gain or drop a bare `tools/` guard makes five carriers wrong.

**Fix.** "several legs" in all five, and the `guards join` report line prints the excluded guards with their leg counts — which R1's fix does anyway.

**Left-shift.** The report line is the derived figure; the prose stops carrying one.

### R12 — LOW · the exact-file branch of `check_guard_trips` has never been seen to fail (id 24)

The suite's only manifests are `{"guard":["tools/x/"]}` (`:372`) and `{"guard":["tools/"]}` (`:433`), every declared path is `tools/x/thing.sh`, so `path == guard` and the docstring's "`tools/x.sh` does not trip on `tools/x.sh.bak`" are asserted by docstring alone; a regression to bare `startswith(guard)` keeps all 55 arms green. Verified the predicate is correct today on a fixture with an exact-file guard `tools/x/thing.sh`: declaring `tools/x/thing.sh.bak` → no hit, exit 0; declaring `tools/x/thing.sh` → the `[guards]` hit. The live manifest carries 25 exact-file guards, so the untested branch is the one the real tree relies on. Class: the §7 "a gate you have only ever seen pass".

**Fix.** One arm pair over the shared repo, exactly the two fixtures above; raise `FLOOR_ASSERTIONS` by two.

**Left-shift.** That arm.

## By design — not re-reported

Stated in the brief and confirmed unchanged at source; none of these is a finding.

- The hook reads the WORKTREE conf and the driver reads BASE — `agent-cap.js:1749-1750` and `tools/hooks/README.md` state it; the BASE read is the one that binds.
- A bare `spec-audit:` line reads as absent to the hook and falls to the conf while the driver refuses it (fail 52) — the hook header's stated limit at `:1747-1749`, in the admitting direction.
- One-segment guards excluded from the join — the design; R1 is about the predicate selecting a different population than the one the design names.
- One hit per missing leg, not per (leg, path) — `:492-494`.
- No per-build opt-out under a project default — U7 §3; R7 is about the engine offering one anyway.
- No kit version bump for the kickoff engine — KICK-1 §3, `TOOL-aReplayedCard-17`'s shape.
- A run with shell access defeats both reads — protocol §9.

## Checklist classes run

`gotchas.py --for-diff 0e61932d..HEAD` selected 51 classes by anchor + 5 universal. Produced a confirmed finding: `allowlist-narrower-than-the-root-it-guards` (R1), `fallback-fabricates-the-passing-value` and `swallowed-delegate-reads-as-clean` (R2), `containment-tested-one-way` (R3), `two-answers-to-one-question` (R4, R5, R7, R9), `hand-named-gate-list-green-while-the-bar-reds` (R6), `two-readers-of-one-config-one-re-derived` (R8), and the §7 never-seen-RED rule (R12). Run and clean on this range: `fixture-passes-by-finding-nothing` (the U7 slice's AC1 arm asserts the positive spelling and `miss`es both others), `staged-break-substitutes-a-synthetic-value` (the fail-54 arm commits `later` to BASE and pushes), `conf-value-interpolated-into-a-regex` (`SPEC_GUARD_LEGS_CUTOFF` is compared as a string, never interpolated; the hook's date test is a literal), `id-matched-as-a-substring` (`_sa_named` join is `grep -qxF`), `criterion-asserts-what-its-own-command-cannot-show` (every U7/U8 AC names a command whose output carries the asserted text).

## Left-shift summary

| # | Gate or documented check |
|---|---|
| R1 | `check-spec-tokens.test.sh` arms: a deep guard carried by floor+1 legs → NEAR; a one-segment guard carried by one leg → hit. Report line prints the excluded guards with counts. |
| R2 | `unattended.test.sh` arms in the U7 slice: BASE conf with the date then `return 0` / an unbound reference / a syntax error → fail 55, `miss` `not owed`. |
| R3 | `check-spec-tokens.test.sh` arms: `tools/x/` declared against guard `tools/x/` → hit; `tools/` declared against guard `tools/x/` → hit. |
| R4 | `check-spec-tokens.test.sh` arm: no Gates heading + a tripping path → exit 0, counted on the guards line. |
| R5 | Prose; the `kit/dogfood doc parity` leg holds template and render together. |
| R6 | The gate itself from `2026-09-22`; records edit now. |
| R7 | `check-template-size.sh` holds the cap; KICK-1 AC3 gains the third spelling. |
| R8 | `agent-cap.test.sh` arms: `=2026-09-21#note` → deny; `"2026-09-21"; X=1` → deny (documented limit). |
| R9 | Prose; check 22 holds the protocol pair. |
| R10 | The AC4 arm gains a `hit` on the source clause. |
| R11 | The guards report line carries the derived figure; the five sentences drop theirs. |
| R12 | `check-spec-tokens.test.sh` arm pair over an exact-file guard: `.bak` sibling → clean; the file → hit. |

State at synthesis: `branch/spec-audit-followups` at `144cd1fb196e` · base `0e61932de718` · `check-spec-tokens.test.sh` 55/55 · `agent-cap.test.sh` 294/294 · driver suite not run (sliced idiom only) · bar not run.

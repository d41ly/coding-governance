**Serves:** diff-review TOOL-aBlindedTrial-7 TOOL-aBlindedTrial-8 KICK-aBlindedTrial-1

# Closing diff review, round 2 — aBlindedTrial units 7, 8 and KICK-1: the fold of round 1's twelve findings

Node `a` · 2026-09-21 · Tier-2 · on `branch/spec-audit-followups` · adversarial fan through `tier2-review.js` (4 finder lenses → 5 skeptic batches → this synthesis). Round 1's record is `2026-09-21-review-TOOL-aBlindedTrial-7-8-kick1-closing-diff-round1.md` in this folder (R1–R12). Every confirmed finding below was re-read at source and, where it names behaviour, re-executed in this synthesis before it was adjudicated: the checker run over three fixture repos (one carrying the LIVE manifest) and in `--list` mode over the live corpus, `derive_guarded_legs` and `check_dir_shaped` probed in-process, the driver's line-1544 idiom sliced byte-for-byte and run under `set -u` against six blob shapes beside the startup reader, the hook driven with nine crafted confs, the kickoff-manifest ratchet run at HEAD exactly as the manifest invokes it. Nothing was taken from a skeptic's word alone.

**Reviewed range:** `144cd1fb196e0c38f7f6aee50816817606de2c69...HEAD` — **ROUND 2**. HEAD is `315201b0cf4c`, one commit, 26 files, +603/−137: the fold of round 1. The base is round 1's HEAD and resolves (`git cat-file -t` → commit).

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing, and eleven of round 1's twelve items are closed at source: the exclusion is breadth with the floor printed (R1), the BASE-conf read refuses a blob that dies before the read (R2), a declared directory trips (R3), a no-Gates spec is not joined (R4), M4's When sentence and the Skill row name both sources (R5), the three §7 lines name their tripped legs (R6), the engine does not ask under a dated default and the card has a third spelling (R7), the glued `#` is part of the word (R8, re-driven: `=2026-09-21#note` → deny, `"2026-09-21"; X=1` → deny, trailing comment behind whitespace → allow), the date is a record (R9), the unevidenced sentence names date and source (R10), "eleven" is gone from the five carriers (R11), the exact-file pair is observed (R12). `check-spec-tokens.test.sh` is 62/62 and `agent-cap.test.sh` 298/298 at HEAD. What this round finds is one fix that overshot: R3's fold kept ONE-segment directory tokens as declared prefixes, which round 1 had prescribed against, so prose that NEGATES a tree — "No file under `tools/` is touched", the corpus's most common way to say it — is read as declaring the whole root and, from the cutoff tomorrow, owes every non-broad leg under it: 34 hits on the live manifest. One HIGH. Four MEDIUMs: the fold's fail-55 return leaves the `specs-audited` grader over an unfinished derivation and it prints the very absence the refusal just declined to assert; U8's spec body still describes rev-1 and its AC4 names as its red condition the arm the fold ships as passing; the kit's adopter-facing example conf still ships the depth rule; and the kickoff-manifest ratchet is RED at HEAD on a leg all three specs name. Seven LOWs are counts, wording, a deny-direction false refusal and two half-applied folds. Every fix is a few lines plus an arm, or records; the units are INPROGRESS, so they fold before the close.

Why not BLOCKED: no spec at HEAD is dated at or after `SPEC_GUARD_LEGS_CUTOFF` (2026-09-22), so the HIGH reds nothing today and `--list` shows exactly what it would; the red ratchet leg has the remedy the charter's merge exception already prescribes for a stamp; every other item is deny-direction, a report figure, or records.

## Review shape

Raw **23** · confirmed **21** · refuted **2** · unverified **0** · precision **0.91**.

Precision is well above the 0.5 floor §8 sets. The twenty-one confirmed collapse to **12 items**: seven groups reported the same defect with the same repro from different lenses (ids 1 and 6 · ids 2 and 13 · ids 3, 15 and 19 · ids 4 and 12 · ids 7, 14 and 21 · ids 10 and 20 · ids 16 and 22), and those merges are mine, at write time; the pipeline discarded no duplicates. The two refuted (ids 5 and 18) did not reach this synthesis as text, only as the count, so they are not re-adjudicated here.

Adjudicated, by item: **0 BLOCKER · 1 HIGH · 4 MEDIUM · 7 LOW** (12 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 1 HIGH · 7 MEDIUM · 13 LOW** (21 findings; every id takes the severity of the item that holds it — ids 4, 15 and 23 were rated low by their finders and take the MEDIUM of R4, R3 and R5, each for the reason its item states; ids 2 and 13 keep the LOW their finders gave).

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so a zero in this report is evidence of absence and not of a hole. The seven duplicate groups were judged by hand in this synthesis, as stated above.

What this synthesis ran, per the lens instruction. `python tools/check-spec-tokens.py --list` over the live corpus at HEAD (190 `NEAR [guards]` rows, 34 of them `<leg> <- tools/` for one spec, exit 0 by `--list`'s design). Three fixture repos with a staged, uncommitted cutoff so the relation is announced rather than refused: the LIVE `tools/gate-legs.json` (111 legs) with a post-cutoff spec whose sub-head reads `New: `memory/builds/tOne/build/note.md`. No file under `tools/` is touched, and no gate leg is added or moved.` → exit 1, 36 `[guards]` hits; a no-Gates spec declaring five tokens → exit 0 and the double-counted guards line; the `derive_guarded_legs` duplicate-entry manifest in-process. `extract_files_touched` walked over every spec under `memory/builds/*/spec/**` for one-segment directory tokens. The line-1544 idiom copied byte-for-byte into a function under `set -u` (bash 5.3.9) against six blob shapes, beside `bash -uc '. conf'` on the same bytes; the in-eval sentinel R6 proposes run against ten shapes. `node tools/hooks/agent-cap.js` against a scratch tree (README carrying no key) with nine conf spellings, including R8's two and the two R6 shapes. `bash skills/session-kickoff/manifest-check.sh memory/guides/SESSION-KICKOFF.md` at HEAD. `bash tools/check-spec-tokens.test.sh` — **62 assertions, exit 0**. `bash tools/hooks/agent-cap.test.sh` — **298 passed, 0 failed**. `gotchas.py --for-diff 144cd1fb..HEAD` — 37 classes by anchor + 5 universal. The bar and the driver suite whole were not run, as instructed; the driver's fail-55 slice (`unattended.test.sh:5840-5862`) was read, not run. All suite output went to files and was grepped, never read through `tail`.

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| R1 | HIGH | 17 | `tools/check-spec-tokens.py:244`, `:261` | A ONE-segment directory token is a declared root and trips symmetrically, so "No file under `tools/` is touched" owes every non-broad leg under `tools/` — 34 hits on the live manifest; 25 such tokens across 16 live builds, every one prose. |
| R2 | MED | 11 | `tools/unattended/unattended.sh:1517` | `AUTH_SPEC_AUDIT_DERIVED=1` is set before the conf half; fail 54 and fail 55 `return 1` with it set and `AUTH_SPEC_AUDIT` empty, so the `specs-audited` grader prints `not owed … declares no SPEC_AUDIT_DEFAULT` or `at BASE: (none)` — the absence the refusal just declined to assert. |
| R3 | MED | 3, 15, 19 | `…spec-TOOL-aBlindedTrial-8.md:28-40`, `:67`, `:82`, `:113-115`, `:134-136`; `…aBlindedTrial/README.md:75` | The spec body still states the depth rule and "eleven" three times; AC4's red condition is the arm the fold ships as passing (`check-spec-tokens.test.sh:466`). |
| R4 | MED | 4, 12 | `tools/memory-tree/.memory-tree.conf.example:145` | The adopter-facing example conf still says one-segment guards are excluded; the checker joins them under the floor and the fold's own arm asserts it. |
| R5 | MED | 23 | `memory/guides/SESSION-KICKOFF.md:5`, `:8` | The fold re-stamped `last-audit` and left `last-body-change` at `85d930a9`; `kickoff-manifest ratchet` (unguarded, on every bar) is RED at HEAD: check 9, 13 watched commits. All three specs name that leg. |
| R6 | LOW | 2, 13 | `tools/unattended/unattended.sh:1544`, `:1547` | The sentinel is gated on the eval's exit STATUS: a blob whose LAST statement returns non-zero is evaluated to the end and refused as "could not be evaluated to the end"; the startup reader sees the date. |
| R7 | LOW | 1, 6 | `tools/check-spec-tokens.py:276` | `derive_guarded_legs` counts guard OCCURRENCES, not legs: a guard listed twice in one leg's array counts 2; three live guards sit at exactly the floor. |
| R8 | LOW | 7, 14, 21 | `tools/check-spec-tokens.py:542-543`, `:552-559`, `:244` | A no-Gates spec's paths are "examined" and "not joined" on one line; a declared path tripping a joined guard in it gets no NEAR row; `./`, `../`, `tools/./` are admitted as declared. |
| R9 | LOW | 8 | `tools/check-spec-tokens.py:65`; `memory/TEMPLATE-SPEC.md:196` (template `:196`) | "thirty guard `tools/lib/`" and "`tools/` among them" — manifest-derived facts typed in present tense, two lines from "no count of it lives in prose". |
| R10 | LOW | 9 | `skills/session-kickoff/SKILL.md:157-159`, `:206-208` | The no-ask clause has no README precedence; a README `spec-audit: <d1>` under a default `<d2>` is carded as `project default <d2>` while preflight prints the README's `<d1>`. |
| R11 | LOW | 10, 20 | `…spec-KICK-aBlindedTrial-1.md:22-31`, `:111` | S1 asks unconditionally and S2 names two `## open` spellings; AC3 (rev-2) names three and reds on asking under a default; the rev-2 line lists §6 and §7 only. |
| R12 | LOW | 16, 22 | `tools/memory-tree/BUILD-METHOD.template.md:114` (render `:114`); `tools/unattended/SKILL.template.md:594` (render `:594`) | M4's heading and the drive-the-build sentence keep "only where/when the build declares it" under a body that names two sources. |

### R1 — HIGH · a one-segment root in prose declares the whole tree (id 17)

`tools/check-spec-tokens.py:244-250`:

```python
def check_dir_shaped(tok):
    if NOT_A_TOKEN.match(tok) or " " in tok or "*" in tok or "?" in tok:
        return False
    return tok.endswith("/") and tok.rstrip("/") != ""
```

and the symmetric arm at `:261`, `return path.endswith("/") and g.startswith(p + "/")`. Round 1's R3 prescribed keeping a trailing-slash token "that carries two or more segments" as a declared prefix; the fold kept every segment count, wrote `tools/` and `tools/run-gates/` alike into the header (`:56-58`), and added the arm `a declared root that CONTAINS the guard trips it and REDS` (`check-spec-tokens.test.sh:480`) over bare `tools/`, locking the choice in.

Measured. `extract_files_touched` over the sentence `No file under `tools/` is touched` returns `['tools/']`. Over every live spec's sub-head: **25** one-segment directory tokens across **16** builds — `tools/` 14 in 10 builds, `memory/` 6 in 5, and one each of `.githooks/`, `ledger/`, `codebase-map/`, `generated/`, `fixtures/` — and every one I read is prose: a negation, a guard description, a table header, a scope sentence, never a write declaration. `--list` at HEAD already prints 34 `NEAR [guards]` rows for `aMendedLedger-2-u1` from exactly that sentence (`:280` of its spec), each `predates SPEC_GUARD_LEGS_CUTOFF 2026-09-22`. On a fixture carrying the LIVE manifest and a post-cutoff spec whose sub-head reads `New: `memory/builds/tOne/build/note.md`. No file under `tools/` is touched, and no gate leg is added or moved.`: exit 1, **36** `[guards]` hits — 34 `<leg> <- tools/` and 2 `<leg> <- memory/builds/tOne/build/note.md` (the `memory/` guard, 2 legs, joined by the floor and correctly so). From tomorrow the most common way to write "I do not touch tools" reds with 34 names to add, which is the paste-by-rote outcome the breadth floor exists to prevent, one join over. The brief's by-design list covers broad GUARDS excluded by the floor; it says nothing about a declared TOKEN selecting the whole tree. Classes: `a-view-fix-trades-one-blindness-for-another` (R3 closed the folder-declared fail-open and opened a root-mentioned false-deny), `containment-tested-one-way`.

Why HIGH and not BLOCKER: nothing reds at HEAD (no spec is dated at or after the cutoff), `--list` shows precisely what would, the fix is one predicate plus retargeting one arm. Why not MEDIUM: the false-deny is reachable from the first post-cutoff spec, lands on a sentence the corpus writes fourteen times, and costs 34 names per spec — the rev-1 outcome F1 rejected at eleven, three times over.

**Fix.** A one-segment directory token declares nothing and says so. Either place works as long as `--list` names the token; the shorter is in the trip: at the top of `check_guard_trips`, `if path.endswith("/") and "/" not in p: return False` (`p` is already `rstrip`ped), and in the near loop at `:552` a row before the broad test — `if p.endswith("/") and "/" not in p.rstrip("/"): near.append((f, "guards", p, "a one-segment root declares nothing, not joined")); continue`. Two-or-more-segment directories keep R3's symmetric trip. Then the carriers of the "`tools/` and `tools/run-gates/` alike" sentence (header `:56-58`; `.memory-tree.conf:282-283`; `memory/TEMPLATE-SPEC.md:193` and its template `:193`; `memory/map/features/spec-tokens.md:88-89`) say "of two or more segments", and the header names the residual: a two-segment directory named in prose is still read as declared.

**Left-shift.** Retarget the `:480` arm from bare `tools/` to a containment the design wants — declared `tools/x/` against an exact-file guard `tools/x/y.sh` → REDS — and add one arm carrying the live sentence `No file under `tools/` is touched.` against the `tools/x/` manifest → exit 0 plus a NEAR row under `--list`. Observe both RED first on the HEAD checker. Re-run `--list` over the live corpus before wiring and record the row count in the spec's §9.

### R2 — MEDIUM · fail 55 leaves the grader over half a derivation (id 11)

`unattended.sh:1517` sets `AUTH_SPEC_AUDIT_DERIVED=1` immediately after the README half of the derivation, before the conf half at `:1542-1556`. Both fail 54 (`:1553`) and the fold's fail 55 (`:1547`) `return 1` from inside that half with `DERIVED=1` and `AUTH_SPEC_AUDIT` still empty. The DoD loop (`:3301`) grades every item regardless of an earlier unmet one, and the `specs-audited` not-gradable branch (`:3917`) keys on `DERIVED` alone, so the item proceeds: with no pinned fact it prints MET `specs-audited — not owed: … the project conf at BASE declares no SPEC_AUDIT_DEFAULT` (`:3927`), and with a pinned fact it fails 53 with `at BASE: (none)`. Both sentences assert the absence fail 55 exists to refuse, in the same output as the refusal. The global's own header (`:795`) documents `DERIVED` as "set to 1 on the line after the derivation", which the U7 second half broke. Direction stays safe — the close is held by `authorization-reachable` — so the cost is a false DoD line and run-log entry. Reachable when preflight and close disagree about the blob: a driver revision between them (rev-1's preflight read these very blobs as "no default"), or an eval whose outcome depends on the environment under `set -u`, which the kit's resume support invites. The pre-existing fail 52 `(empty)` arm shares the seam (bare `spec-audit:` line → `AUTH_SPEC_AUDIT` empty, `DERIVED=1`), from units 2–5; one move covers all three. Class: `swallowed-delegate-reads-as-clean`.

**Fix.** Move `AUTH_SPEC_AUDIT_DERIVED=1` to after the conf block's closing `fi` (`:1556`), so every refusing return leaves it blank and the grader lands on its existing "not gradable … unknown here" branch. Update the header sentence at `:795` to say "after BOTH halves".

**Left-shift.** One `--close` arm in the U7 slice over one of the four fail-55 shapes already staged at `unattended.test.sh:5853`: `hit 'not gradable'`, `miss 'not owed'`, `miss 'at BASE: (none)'`. RED first on HEAD.

### R3 — MEDIUM · U8's spec describes rev-1 and grades against it (ids 3, 15, 19)

`memory/builds/aBlindedTrial/spec/2026-09-21-spec-TOOL-aBlindedTrial-8.md` is INPROGRESS at rev-2, and its rev-2 line (`:141-142`) opens "S3 · §7 · §8 · closing diff review round 1 folded … the exclusion is BREADTH, not the depth S3 and F1 describe" — and then leaves S3 and F1 standing. `git diff 144cd1fb..HEAD` on the file touched the status line, the generated block, the §7 leg line and §9, nothing else. Standing at HEAD: S2 (`:28-30`) routes tokens through `check_path_shaped` only and names the asymmetric predicate (the code takes `check_dir_shaped` at `:239` and trips symmetrically at `:261`); S3 (`:31-33`) says one-segment guards are EXCLUDED and "eleven legs carry the bare `tools/` guard"; S5 (`:40`) lists "a one-segment guard (near-miss, no hit)"; the design bullet (`:67`) says `derive_guarded_legs` has "one-segment guards split out"; the rejected alternative (`:82`) types "eleven"; AC4 (`:113-115`) reads "a path under a one-segment guard only … exits 0 … Red when: a bare `tools/` guard produces a hit"; F1 (`:134-136`) is RESOLVED as "deeper than one segment … Eleven legs". The fold's own arm at `check-spec-tokens.test.sh:466` is `a one-segment guard carried by ONE leg is joined and REDS` — AC4's red condition, asserted as correct — and the live manifest joins `memory/` (2 legs) and `.githooks/` (5), which is why this spec's §7 gained `recall floor` and `recall floor arms`. The build README's brief row (`README.md:75`) still reads "gate guards deeper than one segment". R11 removed "eleven" from five carriers and left it three times in the unit's own spec. Whoever grades AC4 at close, or reads S3 to learn the rule, gets the rev-1 answer. Records only, hence MEDIUM rather than HIGH; MEDIUM rather than LOW because an acceptance criterion contradicting its own passing arm blocks a truthful close. Classes: `amendment-leaves-its-other-half-standing`, `criterion-asserts-what-its-own-command-cannot-show`, `two-answers-to-one-question`.

**Fix.** Rewrite S2 (both extractors, symmetric trip), S3 (breadth: a guard carried by more than `BROAD_LEG_FLOOR` legs whatever its depth; a one-segment guard under the floor is joined), S5 (the breadth pair, the prefix pair, the exact-file pair, the no-Gates arm), the `derive_guarded_legs` bullet ("broad guards split out by breadth"), AC4 ("a path matching only a guard carried by more than `BROAD_LEG_FLOOR` legs exits 0 and `--list` prints NEAR with the count; Red when: a broad guard produces a hit, or a one-leg one-segment guard does not"), F1 (a dated superseding line: "RESOLVED rev-2: by breadth"), the three "eleven" → "several", and the brief row. Make the rev-2 (or a rev-3) line list the sections actually amended. If R1 lands, AC4 and S2 also say a one-segment ROOT under the sub-head declares nothing.

**Left-shift.** None machine-shaped beyond `spec tokens` and hygiene; the spec's own AC4 becomes dischargeable by the shipped arms.

### R4 — MEDIUM · the example conf an adopter receives ships the depth rule (ids 4, 12)

`tools/memory-tree/.memory-tree.conf.example:145-146`: "One-segment guards such as `tools/` are excluded and listed by `--list` as near-misses". The checker excludes by breadth (`BROAD_LEG_FLOOR = 5` at `:141`, `broad = {g: n … if n > BROAD_LEG_FLOOR}` at `:277`, header `:63` "broad is BREADTH, not depth"); this repo's own `.memory-tree.conf:283-286` was rewritten to say so; `memory/TEMPLATE-SPEC.md:197-198` tells the adopter they "receive this paragraph and the blank key in the example conf". `git show --stat 315201b0` confirms the fold touched `.memory-tree.conf`, `TEMPLATE-SPEC.md`, `SPEC-TEMPLATE.template.md` and `.unattended.conf.example`, and NOT this file — R11 only replaced "eleven", which the example never typed, so nothing in round 1's fix table reached it. The example's own comment at `:149` says the example-parity arm cannot see this key, and no gate compares the two carriers' comment text. `adopt-memory-tree.sh:56` copies this file in as the adopter's conf. On an adopter's manifest where five or fewer legs guard `tools/`, that guard is JOINED and reds, the opposite of the sentence the adopter reads as the contract. MEDIUM because it is the one carrier the kit ships to every adopter and it contradicts code, the fold's own arm and its sibling docs; the unit's own Files touched already names the file.

**Fix.** Port the `.memory-tree.conf:280-288` comment: BROAD guards — carried by more than the checker's `BROAD_LEG_FLOOR` legs, whatever their depth — are excluded and listed by `--list` as NEAR; the excluded set prints with its counts on every run; a directory token under the sub-head (of two or more segments, once R1 lands) is a declared prefix and trips symmetrically; a spec with no Gates heading is not joined.

**Left-shift.** None machine-shaped today; the parity arm's blind spot is documented in the file. Note it under the unit's §7 as the compensating manual check.

### R5 — MEDIUM · the ratchet leg the specs name is red at HEAD (id 23)

`bash skills/session-kickoff/manifest-check.sh memory/guides/SESSION-KICKOFF.md` at HEAD, exactly as `tools/gate-legs.json` invokes the leg `kickoff-manifest ratchet` (no `guard`, so it runs on every bar): rc 1, `MANIFEST check 9 FAILED … 13 non-merge commits since 85d930a90b8d…`. `SESSION-KICKOFF.md:5` shows `last-audit` re-stamped to `144cd1fb` by the fold while `:8` keeps `last-body-change` at `85d930a9`. The same check reported 12 at the base, so the leg was already red before the fold; the fold touched four watched paths (`.memory-tree.conf`, `.unattended.conf`, `memory/guides/BUILD-METHOD.md`, `skills/session-kickoff/SKILL.md`), advanced the count to 13, and re-stamped one of the two stamps a watched-file commit owes — the memory note "stamps are not one stamp" names this exact half. All three specs name `kickoff-manifest ratchet` in §7 (U7 `:141`, U8 `:128`, KICK-1 `:100`). The landing's pre-push bar reds on a leg the specs claim, and the hook refuses the push. MEDIUM rather than LOW because a named leg is red at HEAD and the push blocks on it; rather than HIGH because the remedy is the one the charter's merge exception already prescribes. Class: `hand-named-gate-list-green-while-the-bar-reds`, inverted — the named leg is red before the landing.

**Fix.** Re-read §B of the manifest against the merged tree, advance `last-body-change` to a current sha with the delta line in the commit message, re-run `manifest-check.sh`; do it in the post-merge follow-up commit the charter's kickoff-manifest merge exception already owes, BEFORE the push.

**Left-shift.** The leg itself; nothing more.

### R6 — LOW · a fully evaluated blob is refused for its last statement's status (ids 2, 13)

`unattended.sh:1544`: `_sad=$( SPEC_AUDIT_DEFAULT=""; eval "$_cf" >/dev/null 2>&1 && printf 'OK %s' "${SPEC_AUDIT_DEFAULT:-}" )`. The `&&` gates the sentinel on the eval's exit STATUS, which is the LAST statement's status, not on the blob having been read to its end. Reproduced with the idiom sliced byte-for-byte under `set -u`, bash 5.3.9: `SPEC_AUDIT_DEFAULT="2026-09-21"` then `false` → no sentinel, fail 55; then `[ -n "${NOPE:-}" ]` → fail 55; then the ordinary conf idiom `[ -n "${OPT:-}" ] && Y=1` with `OPT` unset → fail 55. The driver's own startup reader (`:348`, `. "$CONF"` under `set -u` and no `set -e`) sources the same bytes without complaint and sees the date (verified: `bash -uc '. conf'` → `[2026-09-21]`, rc 1), and the hook admits the same two blobs (driven: exit 0 on both). So three readers of one conf: two see the date, the binding one refuses with `could not be evaluated to the end … a return, an exit, an unbound reference or a syntax error`, naming a cause that did not occur and sending the operator to hunt one. Non-overridable (authorization-reachable is in `DOD_NO_OVERRIDE`), recorded in `RUNLOG_CHECKS` under a false cause. Direction is deny, both shipped confs are pure assignments (measured: no non-assignment line in `.unattended.conf` or the example), so unreachable on HEAD; the kit is copy-installed and the conf header bans nothing beyond assignments, so LOW and real. Class: `two-readers-of-one-config-one-re-derived`.

**Fix.** Print the sentinel from INSIDE the eval'd text, on a descriptor the blob's redirect does not cover, so it appears iff evaluation reached the end whatever the last status:

```sh
_sad=$( SPEC_AUDIT_DEFAULT=""; exec 3>&1
        eval "$_cf"$'\n''printf "OK %s" "${SPEC_AUDIT_DEFAULT:-}" >&3' >/dev/null 2>&1 )
```

Verified on ten shapes in this synthesis: `return 0`, `exit 0`, an unbound reference, a syntax error above and below the key → no sentinel (fail 55, as now); a trailing `false`, a trailing conditional, an echoing conf, a trailing comment → the date. The `$'\n'` matters: without it a blob ending in a comment line swallows the printf. Alternatively keep the `&&` and make the sentence true — "did not evaluate to the end with status 0 — … or a last statement that itself returned non-zero" — and add that fifth shape to the comment at `:1535-1541`; the first is the honest one, the second the cheaper one.

**Left-shift.** One arm in the `_sa_shape` loop at `unattended.test.sh:5853`: the date then `false` → `hit 'opted in by project default'` (or, under the cheaper fix, `hit` the fifth-shape sentence). RED first on HEAD.

### R7 — LOW · breadth is counted in guard entries, not legs (ids 1, 6)

`tools/check-spec-tokens.py:274-277`: `for g in r.get("guard") or []: count[g] = count.get(g, 0) + 1`, no per-leg dedup. The docstring (`:265-266`), the `BROAD_LEG_FLOOR` comment (`:137-141`), the report line (`carried by more than 5 legs: g (n)`) and the NEAR text (`n legs`) all present `n` as a LEG count. Reproduced in-process: five legs on `tools/x/`, one of them `["tools/x/","tools/x/"]` → `derive_guarded_legs` returns `([], {'tools/x/': 6})` — excluded, printed as six legs for five. Live manifest measured: no duplicate array today, and `tools/hooks/`, `tools/memory-recall/` and `.githooks/` each sit at exactly the floor, so one duplicated entry in any of their legs silently drops the motivating class (`tools/hooks/`) out of the join. Nothing refuses a duplicate: `run-gates.sh` splits the guard field and calls `changed` over it (harmless there), `govkit.py` appends each `kit.toml` guard without dedup, the run-gates canary refuses an untracked path but not a repeated one. Latent, hence LOW; but the code does not compute what its own docstring says it returns.

**Fix.** `for g in set(r.get("guard") or []):` at `:275`. One token.

**Left-shift.** One arm: a guard carried by exactly `BROAD_LEG_FLOOR` legs with one row listing it twice stays joined and REDS on an omitted leg. RED first on HEAD (today it is excluded).

### R8 — LOW · the no-Gates skip is counted as examined, and its paths are named nowhere (ids 7, 14, 21)

`:532-535` takes the `g_nogates += 1` branch for a post-cutoff spec with declared paths and no Gates heading and never runs the join; `:541-543` then does `g_specs += 1; g_examined += len(declared)` unconditionally under `g_armed`. Reproduced: a post-cutoff spec declaring `tools/x/thing.sh`, `./`, `../`, `tools/./`, `tools/x/` with no Gates heading → exit 0 and one line reading `5 declared path(s) examined in 1 live spec(s) … · 1 declare a path and carry no Gates heading, not joined` — the same spec counted as examined and as not joined, on the line whose comment says these are separate categories and whose job is to size the skip. Under `--list` no NEAR row names `tools/x/thing.sh` or `tools/x/`, although both trip the joined guard: the near loop at `:552-553` `continue`s on any joined-guard match, and the join branch never ran, so the skip has a size and the path it skipped has no name. Second half: `check_dir_shaped` admits `./`, `../` and `tools/./` (probed: all `True`; `NOT_A_TOKEN` at `:104` matches none and `rstrip('/')` leaves `.`, `..`, `tools/.`), and `extract_files_touched` puts them in `declared`, inflating the same figure with tokens that can trip nothing. The R4 arm at `check-spec-tokens.test.sh:492` asserts only the `not joined` substring, so the inflated figure is untested. Class: `two-answers-to-one-question`.

**Fix.** Move `g_specs += 1; g_examined += len(declared)` into the joined branch (`elif extract_gates(text) is not None:`), and in the no-Gates branch append `near.append((f, "guards", p, "no Gates heading, not joined"))` for each declared `p` that trips a joined guard. In `check_dir_shaped`, reject a token whose `rstrip('/')` is `.` or `..` or ends in `/.`.

**Left-shift.** Extend the `:492` arm's expected string to `0 declared path(s) examined in 0 live spec(s)`, and add a `--list` assertion that the no-Gates fixture prints one NEAR row naming its path. RED first on HEAD.

### R9 — LOW · a fresh derived count, typed where the last one was removed (id 8)

`git show 315201b0` confirms the fold replaced R11's "eleven legs guard bare `tools/`" at the checker header with "several legs guard bare `tools/` and thirty guard `tools/lib/`" (`:64-65`) — an undated present-tense count of a manifest-derived population, two lines before "no count of it lives in prose" (`:67`). The dated comment beside `BROAD_LEG_FLOOR` (`:137-140`, "Measured on the manifest at 144cd1fb") is the sanctioned form; the header sentence is not, and R11's own fix table said "the five sentences drop theirs". `memory/TEMPLATE-SPEC.md:196` and `tools/memory-tree/SPEC-TEMPLATE.template.md:196` pin `tools/` as "among" the excluded set, which the floor derives per manifest and which is false for an adopter with five or fewer legs guarding `tools/`. No parity gate compares either carrier to the manifest. Same class as R11, one commit later.

**Fix.** Header: "several guard bare `tools/` and far more guard `tools/lib/`", or drop the second clause (the report line prints the figure). Template and render: "as the printed set shows" for "`tools/` among them".

**Left-shift.** The report line is the derived figure; prose stops carrying one. The `kit/dogfood doc parity` leg holds the template pair.

### R10 — LOW · the no-ask clause misrecords a README that already answered (id 9)

`SKILL.md:157-159`: "Do NOT ask when `<repo>/.unattended.conf` declares a dated `SPEC_AUDIT_DEFAULT` … record it on the card", and `:206-208` gives `spec audit: project default <date>` "when the conf answered". Neither mentions a README that already carries `spec-audit:`. The driver's rule is README first: `unattended.sh:1516-1526` reads the README key and `:1542` consults the conf ONLY when the README has no `spec-audit=` line at all. So a second design pass into an existing build whose README declares `spec-audit: <d1>` under a project default `<d2>` is carded as `project default <d2>` while preflight prints `opted in by README spec-audit: <d1>` — the convenience record disagreeing with the binding one, the class R7 was fixed for. Reachable: adding units to an existing build is this repo's own practice (this build got 7–8 after 2–5). The engine is 18425/18432 bytes, so the fix is byte-neutral or trades words elsewhere. LOW: narrow, and the binding records are right.

**Fix.** Fold the README check into the same clause: "Do NOT ask when the build README already carries `spec-audit:` (record `declared <date>`) or `<repo>/.unattended.conf` declares a dated `SPEC_AUDIT_DEFAULT` (record `project default <date>`)", and trim the equivalent bytes from the surrounding sentence.

**Left-shift.** `check-template-size.sh` holds the cap; KICK-1's AC3 grep already names the three spellings.

### R11 — LOW · KICK-1's scope items describe rev-1 (ids 10, 20)

`…spec-KICK-aBlindedTrial-1.md` S1 (`:22-28`) gates the question only on the method carrier naming `spec-audit:` with no `SPEC_AUDIT_DEFAULT` exemption; S2 (`:29-31`) defines the `## open` line as exactly two spellings. AC3 (`:86-90`, stamped rev-2) names three and reds when the engine "asks under a project default"; the engine (`SKILL.md:158`, `:206-208`) carries the clause and the third spelling. The rev-2 line (`:111`) names §6 and §7 only, so the stale scope items are not recorded as unfolded. One live spec, two behaviours. Class: `amendment-leaves-its-other-half-standing`.

**Fix.** One clause each: S1 "… ask ONE `AskUserQuestion` — unless `<repo>/.unattended.conf` declares a dated `SPEC_AUDIT_DEFAULT`, in which case do not ask (R7)"; S2 "… `spec audit: declared <date>`, `spec audit: not declared (owner)` or `spec audit: project default <date>`". Add §2 to the rev-2 sections list, or a rev-3 line.

**Left-shift.** Records only.

### R12 — LOW · R5 half-applied: the heading and the drive sentence (ids 16, 22)

`tools/memory-tree/BUILD-METHOD.template.md:114` and its render `memory/guides/BUILD-METHOD.md:114` still read `## M4 — The spec audit — owed only where the build declares it`, while the **When** sentence two lines down (`:116-118`) now names the project's `.unattended.conf` `SPEC_AUDIT_DEFAULT` as a second source. `tools/unattended/SKILL.template.md:594-596` (render `.claude/skills/unattended/SKILL.md:594`) tells the operator the harness runs AUDIT "only when the build declares `spec-audit:`" and in the same bullet says to pass `specAudit` when preflight read `opted in by project default SPEC_AUDIT_DEFAULT: <date>`. `git show 315201b0` on both templates confirms the fold changed only the When paragraph and the `specs-reviewed` table row (`:100`). The heading is the line a reader scans and the table of contents shows; the drive sentence is the operator's rule. The parity leg pairs template and render byte-wise and cannot see the contradiction. Class: `amendment-leaves-its-other-half-standing`.

**Fix.** `## M4 — The spec audit — owed only where the build or its project declares it`, and `only when the build or its project declares the audit — AUDIT and DISPOSAL…` at `:594`; re-render both, one commit.

**Left-shift.** The `kit/dogfood doc parity` leg holds each pair; nothing sees the sense.

## Observed, not a finding

Stated so the next reader does not re-derive it. Under the breadth floor `memory/` (2 legs: `recall floor`, `recall floor arms`) is JOINED, and every spec declares files under `memory/builds/`, so from the cutoff every post-cutoff spec that declares its own records owes those two names on its §7 line — the three specs of this diff already carry them. That is the floor doing what round 1's R1 asked; whether two by-rote names per spec is a cost worth a floor of 5 is the owner's call and the printed excluded set is what to decide it from. Not adjudicated.

## By design — not re-reported

Stated in the brief and confirmed unchanged at source; none of these is a finding.

- The hook reads the WORKTREE conf and the driver reads BASE — `agent-cap.js:1749-1750`; the BASE read binds.
- A bare `spec-audit:` line falls to the conf at the hook and is refused (fail 52) by the driver — the hook header's stated limit, admitting direction.
- Broad guards excluded by the floor — R1's rule; this round's R1 is about a declared TOKEN, not a guard.
- One hit per missing leg, not per (leg, path) — `:539-540`.
- No per-build opt-out under a project default — U7 §3.
- No version marker on the kickoff engine — KICK-1 §3.
- The `;`-joined conf line reads as no assignment at the hook and denies — driven this round: exit 2, as the header now states.

## Checklist classes run

`gotchas.py --for-diff 144cd1fb..HEAD` selected 37 classes by anchor + 5 universal. Produced a confirmed finding: `a-view-fix-trades-one-blindness-for-another` and `containment-tested-one-way` (R1), `swallowed-delegate-reads-as-clean` (R2), `amendment-leaves-its-other-half-standing` (R3, R11, R12), `criterion-asserts-what-its-own-command-cannot-show` (R3), `two-answers-to-one-question` (R3, R4, R8, R9), `hand-named-gate-list-green-while-the-bar-reds` (R5), `two-readers-of-one-config-one-re-derived` (R6). Run and clean on this range: `fixture-passes-by-finding-nothing` (every new arm asserts a positive substring; the R1 and R3 arms were observed RED on the rev-1 checker per their comments), `staged-break-substitutes-a-synthetic-value` (the fail-55 arms commit the dying blob to BASE and push), `heredoc-escape-reaches-the-regex` (the hook regex takes no conf value into its pattern), `inline-fence-swallows-the-rest-of-the-file` (the `_sa_named` awk toggles on fences; no new fence reader in the diff).

## Left-shift summary

| # | Gate or documented check |
|---|---|
| R1 | `check-spec-tokens.test.sh`: retarget `:480` to `tools/x/` vs exact-file guard `tools/x/y.sh` → REDS; add `No file under `tools/` is touched.` → exit 0 + NEAR row. |
| R2 | `unattended.test.sh` `--close` arm over a fail-55 shape: `hit 'not gradable'`, `miss 'not owed'`, `miss 'at BASE: (none)'`. |
| R3 | Records; AC4 becomes dischargeable by the shipped arms. |
| R4 | Documented check in U8's §7: the example-parity arm cannot see this key. |
| R5 | The `kickoff-manifest ratchet` leg, re-stamped post-merge before the push. |
| R6 | `unattended.test.sh` arm: the date then `false` → `opted in by project default`. |
| R7 | `check-spec-tokens.test.sh` arm: a floor-count guard with one duplicated entry stays joined and REDS. |
| R8 | Extend the `:492` arm to `0 declared path(s) examined in 0 live spec(s)`; a `--list` NEAR row for the skipped path. |
| R9 | The report line carries the figure; `kit/dogfood doc parity` holds the template pair. |
| R10 | `check-template-size.sh` holds the cap; AC3's grep. |
| R11 | Records only. |
| R12 | `kit/dogfood doc parity` holds each pair. |

State at synthesis: `branch/spec-audit-followups` at `315201b0cf4c` · base `144cd1fb196e` · `check-spec-tokens.test.sh` 62/62 · `agent-cap.test.sh` 298/298 · `manifest-check.sh` rc 1 (check 9) · driver suite not run (sliced idiom only) · bar not run.

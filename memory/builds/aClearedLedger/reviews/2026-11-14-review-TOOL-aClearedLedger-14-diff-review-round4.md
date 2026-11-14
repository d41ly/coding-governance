**Serves:** diff-review TOOL-aClearedLedger-14

# aClearedLedger — Tier-2 diff review, round 4

*2026-11-14. Subject: the cumulative diff landing on main. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent: neither `specs` nor `context` was supplied, so the lenses had only the range's commit messages to read intent from. Lens notes: none supplied, so every lens ran on the kit's generic brief. Checklist: 30 items, acquired by the harness from `--for-diff 64673441a3e6698a63af859fdf7b8f9381f580c8..HEAD`, each assigned to exactly one of the 5 lenses (6 each). By design: none supplied, no caller byDesign and a block of 0.*

**Range reviewed: `64673441a3e6698a63af859fdf7b8f9381f580c8...998b627aad9ffcadfe45e0d478696b32b5a326f3`**

**Round: 4.**

## Verdict: BLOCKED

One HIGH item stands. The diff reopens a bypass of row D6 in the gate guard that the base denied: a glued redirection target whose quoting opens just after the operator, such as `>'>x.log'`, lets the full self-test suite run at BUILDING (H1, id 1). The guard is an enforcement hook and this diff introduced the regression, so the range should not land until H1 is fixed. One MEDIUM item and three LOW items also stand. M1: no gate arm fails if the deny-side half of the new drop test is weakened (id 6). L1: an empty quote pair before `>` is read into the word, which contradicts the new comment (id 3). L2: the README and the hook header give `'>' x.log` as a redirection example when it holds none (id 4). L3: a lint docstring gives the wrong reason the lint over-reads a quoted `&` (id 5).

## Review shape

Intensity full, raw 6, confirmed 5, refuted 0, merged 1, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 3 | 2 | 0 | 1 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |

Adjudicated tally by item: 5 items, 0 BLOCKER, 1 HIGH, 1 MEDIUM, 3 LOW. By raw confirmed finding: 5 findings, 0 BLOCKER, 1 HIGH, 1 MEDIUM, 3 LOW. Every finding keeps its binding grade.

The merged finding is id 2 (correctness). Its skeptic marked it a duplicate of id 1: the same line, the same greedy-match defect, the same probe and the same fix. It is counted once, inside H1, and it is not a confirmed id of its own.

| item | severity | ids | defect |
|---|---|---|---|
| H1 | HIGH | 1 | A quoted operator character at the start of a glued redirection target bypasses row D6 |
| M1 | MEDIUM | 6 | No arm fails when the deny-side half of the new drop test is weakened |
| L1 | LOW | 3 | An empty quote pair before `>` reads the `>` into the word, against the stated rule |
| L2 | LOW | 4 | `'>' x.log` is given as a redirection example and holds no redirection |
| L3 | LOW | 5 | The lint docstring gives the wrong reason a quoted `&` is over-read |

## Run integrity

Lenses 5/5 returned, 0 died. Skeptic batches 3/3 returned, 0 died. 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 1 duplicate refutation counted as a merged confirmation (id 2 into id 1), 0 spurious verdicts discarded, 0 duplicates. Fixes on confirmed findings: 5 judged sound, 0 judged UNSOUND, 0 judged INSTANCE-ONLY, 0 none proposed, 0 not judged. Severity on confirmed findings: 0 ungraded by the skeptic, 0 re-graded by the skeptic. Unverified findings: 0 answered uncertain, 0 with no usable verdict. Refuted findings shown: 0. Same-address pairs shown: 0. Dispositions: unclassed refuse, 30 class slugs handed, 174 leg names read from `tools/gate-legs.json`.

Every count above is zero where a non-zero would mark the run incomplete, so the run is complete.

No refuted finding was shown, so no twin is flagged.

## Items

### H1 — HIGH — a quoted operator character at the start of a glued redirection target bypasses row D6 (id 1; id 2 merged)

**Where:** `tools/unattended/gate-guard.js@07723a18:622`, with the token read at `tools/unattended/gate-guard.js@07723a18:395-399` and `REDIRECT_RE` at `:486`.

**What is wrong:** in `>'>x.log'` or `2>'>x.log'`, readTokenAt adds the quoted `>` to the word, so the word is `>>x.log` with quotedAt=1. The new keep-as-word test `q < redir[0].length` compares that offset with REDIRECT_RE's greedy match over the whole word. The match is `>>` (length 2), which runs past the real one-character operator, so 1 < 2 and the token is kept as an argument word. Bash reads the same text as the leg with its output redirected to a file named `>x.log`.

**Consequence:** checkSuiteLeg sees `[..., "--selftest", ">>x.log"]`, a longer spelling that its rule 2 counts as a miss. The guard then allows the full self-test suite at BUILDING when it should deny it. A read-only probe against the real manifest gave a hit for `python3 tools/memory-tree/gen_build_index.py --selftest >x.log` and no hit for the same command with `>'>x.log'` or `2>'>x.log'`. At the base 64673441a the same input was dropped as a glued redirection and denied, so this diff introduced the regression. The grade is HIGH, not BLOCKER, because only an unusual spelling reaches it: a quoted `>` or `<` at the start of a glued target. The two new allow arms (`'&'>x.log`, `'>'>x.log`) cover only quoting that opens at offset 0, so the gate never saw this case.

**Fix (judged SOUND by the skeptic):** when q >= 0, run REDIRECT_RE on `toks[j].slice(0, q)`, the unquoted prefix alone, and treat the word as a redirection only if that prefix matches. Keep the bare-operator `j++` step for `redir[0] === toks[j]` with q < 0. The skeptic on id 2 checked this fix against the other spellings: `'&'`, `'>'` and `2'>'x` have prefixes ``, `` and `2`, which do not match, so they stay words. `>'>'x` and `2>"x.log"` have matching prefixes, so they stay redirections. Add deny arms `$M_FLAG >'>x.log'` and `$M_FLAG 2>'>x.log'`, raise FLOOR_ASSERTIONS by their count, and show each new arm fails (exit 0 where it should exit 2) before the fix lands.

**Left-shift gate:** in `tools/unattended/gate-guard.test.sh`, pair every allow arm that quotes an operator character with a deny arm that quotes the same character just after a complete operator. Every new branch of the drop test then has an arm on each side of its boundary.

### M1 — MEDIUM — no arm fails when the deny-side half of the new drop test is weakened (id 6)

**Where:** `tools/unattended/gate-guard.js@07723a18:622`; the arms at `tools/unattended/gate-guard.test.sh@8d3a1720:814` and `:824-825`.

**What is wrong:** the half `q < redir[0].length` keeps a quote that opens after the operator (`>"x.log"`, `2>"x.log"`) as a redirection. No arm exercises it. The new arms at `:824-825` put the quote inside the operator, where q=0 keeps the word under any version of the predicate. The only quoted-target arm, `>> "$LOG"` at `:814`, is spaced: `>>` is a bare unquoted operator and `j++` skips the target without consulting q. A scratch copy with the predicate weakened to `(!redir || q >= 0)` read `python3 zz-kit/planted_suite.py --selftest >"x.log"` as `[..., --selftest, ">x.log"]`, which no longer matches the leg, and every existing arm still passed. Spec rows U8 to U10 are read only by the AC1 build-time probe that no gate runs again. The spec's "What it does not check" list (spec lines 318-335) names quoted digits, `<`, empty pairs and spaced operators, and leaves U8 to U10 out.

**Consequence:** today's behaviour is correct. A later change that widens the predicate to "any quoting makes a word" keeps run-gates green. Row D6 would then let an over-bound suite run as `$M_FLAG >"x.log"` or `2>"x.log"` during BUILDING. The spec also implies the deny side is covered when it is not.

**Fix (judged SOUND by the skeptic):** add two run_planted deny arms to the same block: `"D6 the leg with a quoted glued redirection target -> deny" 2 "$B" "$M_FLAG"' >"x.log"'` and one for `2>"x.log"`. Raise FLOOR_ASSERTIONS by 2 and record the raise in a RAISED comment. Before landing, show each arm goes red with the predicate weakened to `q >= 0`. Until the arms land, add the glued quoted target (U8 to U10) to the spec's "What it does not check" list.

**Left-shift gate:** extend the `harness arms (fail branches armed or pinned)` leg, or the project checklist, so a spec row confirmed only by a build-time scratch probe must name the gate arm that re-runs it, or else appear in the spec's "What it does not check" list.

### L1 — LOW — an empty quote pair before `>` reads the `>` into the word, against the stated rule (id 3)

**Where:** `tools/unattended/gate-guard.js@07723a18:408`; the comment at `:369-370` and `:412-414`; spec fact line 105.

**What is wrong:** the break condition requires `out !== ''`. After `""`, out is still empty, so in `"">x.log` the unquoted `>` is read into the word and the token comes out as `>x.log` with quotedAt=0. The keep-as-word test (q=0 is less than the match length) then keeps it as an argument. The rewritten comment and the spec ("an empty pair included") both say a word holding quoting ends at `>`. Bash reads the text as an empty argument followed by a redirection.

**Consequence:** contained. The word count matches bash's, and checkSuiteLeg matches neither `''` nor `>x.log` against a literal leg word, so the D6 verdict does not change. Only the word text disagrees with the stated rule. The base dropped this token as a redirection, so both the comment and the keep are new in this diff.

**Fix (judged SOUND by the skeptic):** change the break condition to `(out !== '' || quotedAt >= 0)` ahead of the quoting test, so `""` ends as an empty quoted word, which scanSegments already keeps through `t.quotedAt >= 0`. Alternatively, narrow the comment to say an empty-quoted word is read on.

**Left-shift gate:** add a token-level arm in `gate-guard.test.sh` that asserts scanSegments returns `''` and a dropped redirection for `"">x.log`, so the read and the comment cannot drift apart.

### L2 — LOW — `'>' x.log` is given as a redirection example and holds no redirection (id 4)

**Where:** `tools/unattended/README.md@0d61b8b1:128-129`, and the hook header at `tools/unattended/gate-guard.js@07723a18:68`.

**What is wrong:** both list `'>' x.log` as an example of "a quoted operator character before a redirection". It is a quoted `>` argument followed by a spaced plain argument. The spec's own fact (line 104) shows `printf '[%s]' a '>' x.log` printing `[a][>][x.log]`. It belongs on the list only because the lint strips quotes and over-reads it as `> x.log`, and the label does not say so. Both lines are new in this diff.

**Consequence:** documentation only. The hook allows the command, matching spec row U6 ("miss"). A reader, or the next fold's test author, may take `'>' x.log` for a redirection case.

**Fix (judged SOUND by the skeptic):** use `'>'>x.log`, which the new test arm pins, as the second example in both the README and the gate-guard.js header. Alternatively, describe `'>' x.log` separately as a quoted operator character used as an argument.

**Left-shift gate:** this is an instance of the checklist class fold-text-is-unreviewed-surface. Each example a fold writes into prose should name the test arm that pins it, so an example with no arm stands out at review.

### L3 — LOW — the lint docstring gives the wrong reason a quoted `&` is over-read (id 5)

**Where:** `tools/check-spec-tokens.py@40b55ac9:531`; the split pattern at `:479`.

**What is wrong:** the new check_bar docstring clause says the lint over-reads a quoted operator character because "this reader reads [the word] with its quotes out". For `'&'>x.log` that is not the cause. SIMPLE_COMMAND_SPLIT (`[;|(){}`\n]|(?<!>)&(?!>)`) has no quote state, so it cuts the command at the quoted `&` before any word is unquoted. A probe split `python3 kit/s.py --selftest '&'>x.log` into `["python3 kit/s.py --selftest '", "'>x.log"]`. The clause is right for `'>'>x.log`, which stays one command.

**Consequence:** no behaviour change, since the lint still reports a hit as the clause claims. The stated reason is wrong for one of the two spellings the hook header and the README name. A later change that adds quote state to the word reader would expect this difference to go away, and it would not, because the split still cuts at the `&`.

**Fix (judged SOUND by the skeptic):** reword the clause to give both reasons. A quoted `&` splits the command here because the split pattern has no quote state. A quoted `>` is read with its quotes out and dropped as a redirection. The hook keeps both as an argument.

**Left-shift gate:** a spec-tokens self-test arm per named spelling that asserts which stage of the lint (split or word read) produces the over-read, so a docstring that names the mechanism is pinned to it.

review-shape kind=diff-review round=4 intensity=full at=synth raw=6 confirmed=5 refuted=0 merged=1 unverified=0 blocker=0 high=1 medium=1 low=3 agents=9 out-tokens=42719
review-round round=4 limit=- prior=- count=1 state=-

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/gate-guard.js@07723a18:622 | high | high | confirmed | Reproduced with the exported scanDenyHits. At head, `python3 a/s.py --selftest >'>x.log'` and `2>">x.log"` give candidate words ending in `>>x.log` and `2>>x.log`, because readTokenAt adds the quoted `>` to the word with quotedAt=1. REDIRECT_RE (line 486) greedily matches `>>` (length 2), so the new check `q < redir[0].length` at line 622 keeps the token as a word, and checkSuiteLeg reads the result as a longer spelling. I ran the same input against the base file from 64673441a: there the token was dropped as a glued redirection and the words were exactly the leg, so this diff introduced the regression. It is a real bypass of D6 enforcement. I graded it high and not blocker because only an unusual spelling reaches it, a quoted `>` or `<` at the start of a glued target. | sound | - | new:operator-length-measured-across-a-quote |
| 2 | correctness | tools/unattended/gate-guard.js@07723a18:622 | high | - | refuted | duplicate of id=1. It is the same defect at the same line, `q < redir[0].length` measured against REDIRECT_RE's greedy match over the unquoted text. I reproduced its probe exactly: `>">"x.log` gives words [python3,a/s.py,--selftest,>>x.log] at head, while the base gives [python3,a/s.py,--selftest]. Its proposed fix is the same one as id=1's: match REDIRECT_RE on the prefix before the quote. That fix is sound. `'&'`, `'>'` and `2'>'x` have prefixes ``, `` and `2`, none of which match, so they stay words. `>'>'x` and `2>"x.log"` have prefixes that match, so they stay redirections. | sound | - | - |
| 3 | correctness | tools/unattended/gate-guard.js@07723a18:408 | low | low | confirmed | I ran scanSegments and scanDenyHits on `python3 a/s.py --selftest "">x.log`. The tokens came back `[python3, a/s.py, --selftest, >x.log]` with quotedAt `[-1,-1,-1,0]`, and the D6 candidate words were the same. In readTokenAt (line 408) the break needs `out !== ''`. After `""`, out is still empty, so the unquoted `>` is read into the word. The rewritten comment (lines 369-370 and 412-414) and spec fact line 105 ('an empty pair included') both say a word holding quoting ends at `>`. The new keep-as-word test in scanDenyHits (q=0 < length of the match) then keeps `>x.log` as an argument. Bash reads the same text as an empty argument plus a redirection. The base dropped this token as a redirection, so both the comment and the keep are new in this diff. The effect is contained. The word count matches bash's, and checkSuiteLeg matches neither `''` nor `>x.log` against a literal leg word, so the verdict is unchanged. Only the word text and the stated rule disagree. | sound | - | new:empty-quote-pair-reads-as-unquoted |
| 4 | correctness | tools/unattended/README.md:129 | low | low | confirmed | tools/unattended/README.md:128-129 and the gate-guard.js header at line 68 list `'>' x.log` as an example of 'a quoted operator character before a redirection'. It has no redirection: it is a quoted `>` argument, then a spaced plain argument. The spec's own fact (line 104) shows `printf '[%s]' a '>' x.log` printing `[a][>][x.log]`. It belongs on the list only because the lint strips quotes and over-reads it as `> x.log`, and the label does not describe that. Both lines are new in this diff. The fault is documentation only: the hook allows the command, which matches spec row U6, 'miss'. | sound | fold-text-is-unreviewed-surface | class:fold-text-is-unreviewed-surface |
| 5 | seams | tools/check-spec-tokens.py@40b55ac9:531 | low | low | confirmed | SIMPLE_COMMAND_SPLIT at tools/check-spec-tokens.py@40b55ac9:479 is `[;\|(){}`\n]\|(?<!>)&(?!>)` and has no quote state. I loaded the module and ran the probe. `python3 kit/s.py --selftest '&'>x.log` splits into ["python3 kit/s.py --selftest '", "'>x.log"], so the command is cut at the quoted `&` before any word is unquoted. `'>'>x.log` stays one command. The docstring clause added at :531 ('which this reader reads with its quotes out') is therefore wrong for the `'&'>x.log` spelling, which the hook header names. The lint still reports a hit, so behaviour does not change. This is a comment-only defect. | sound | - | new:stated-reason-names-the-wrong-mechanism |
| 6 | verification | tools/unattended/gate-guard.js@07723a18:622 | medium | medium | confirmed | The predicate `!redir \|\| (q >= 0 && q < redir[0].length)` at tools/unattended/gate-guard.js@07723a18:622 is new in this diff. I checked every D6 arm in gate-guard.test.sh. The only quoted redirection target is :814, `>> "$LOG"`, which is spaced. There `>>` is an unquoted bare operator and `j++` skips the quoted target, so `q` is never consulted. The new arms at :824-825 put the quote inside the operator, where `q=0` keeps the word under both the original and the mutant. With the predicate weakened to `q >= 0`, a glued quoted target such as `>"x.log"` (q=1) would be kept as a word, and every arm would still pass. No arm feeds rows U8 to U10. The spec's 'What it does not check' list (spec lines 318-335) names quoted digits, `<`, empty pairs and spaced operators but not U8 to U10. Those rows are read only by the AC1 build-time probe. The gap is reachable through a later edit and could let an over-bound suite run during BUILDING. Today's behaviour is correct, so the effect is contained to verification. | sound | - | class:observed-by-claim-no-arm-discharges |

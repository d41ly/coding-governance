# TOOL-dPlacedRequest-63 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-63

The unit was observed from its spec at rev-5 on base `4009c1d2e`. It builds nothing and touches no
product file: every criterion reads the text of the CLOSED specs 59, 61 and 57, or the driver,
through the readers `sec`, `bullet` and `entries` and the live sweep, each cut from its fence in spec
59's `### The criterion readers` and `### The live sweep` sections and sourced unchanged. No gate,
suite or bar ran in this pass. Every reading below is the criterion's own read over the tree, or over
a scratch copy made under the run's scratch directory, paired with a control read that comes back
without its token. The items the spec marks NOT OBSERVED (S2, S3, S5, S6, S13, S15 to S17, S20, S21)
carry no criterion and were not read.

**Evidences:** TOOL-dPlacedRequest-63
- AC1 — `RUN\.md|fixture's( later)? base`: the read of `sec 59 '### The live sweep'` holds it as a fixed string, once; the read of `### The shared key reader` holds it zero times. (DERIVED)
- AC1 — `grep -cE "RUN\.md|fixture's( later)? base"`: the line `the fixture's later base` piped to it printed 1; the line `the fixture's earlier base` printed 0, and the pre-fold alternation `RUN\.md|fixture's base` over the later-base line printed 0. (DERIVED)
- AC1 — `63's S1 and S9`: `bullet 59 S3` names it once; `bullet 59 S2` names it zero times. (DERIVED)
- AC4 — `memory/builds/dPlacedRequest/spec/`: 59's live sweep run over the folder at this pass printed nothing; its population was this spec and 64's, whose joined criteria held no bullet matching the oracle pattern before the base filter, so the hit set is empty. (DERIVED)
- AC4 — `memory/builds/dPlacedRequest/spec/`: over a scratch copy of the folder whose 59 has its status cell respelled INPROGRESS, the sweep printed nothing, 59's AC2 naming the fixture's later base; with that copy's AC21 also respelling `the fixture's` as `a`, the sweep printed 59's AC21 bullet. (DERIVED)
- AC4 — `grep -L -E '^\*\*Status:\*\* (CLOSED|WONTDO)'`: over the folder it listed this spec and 64's, and not the CLOSED spec 62. (DERIVED)
- AC7 — `slice_fn CLAIM_KV_AWK var`: `sec 59 "### The suite's rows"` names it once, and `awk -v BINMODE=3` once; the read of `### The shared key reader` names neither. (DERIVED)
- AC7 — `too late for stdin`: `sec 59 '### Evidence'` names it once, and `BEGIN{BINMODE=3}` once; the read of `### The suite's rows` names neither. (DERIVED)
- AC7 — `BEGIN{BINMODE=3}`: `printf 'status: live\r\n'` piped to the criterion's awk under it printed 12, with GNU Awk 5.4.0. (PINNED 2026-11-20)
- AC7 — `awk -v BINMODE=3`: the same line piped under it printed 13; `status: live` with no CR under it printed 12. (PINNED 2026-11-20)
- AC8 — `live|4`: `bullet 59 AC7` names it once; `bullet 59 AC3` names it zero times. (DERIVED)
- AC8 — `sub(/\r$/, "", line)`: 59's one `New arm:` line names it once, and `live and a CR` once; that line names `sub(/\r$/, "", x)` zero times, and this spec carries no `New arm:` line. (DERIVED)
- AC9 — `§4's live sweep`: `bullet 59 AC3` names it once; `bullet 59 AC7` names it zero times. (DERIVED)
- AC9 — `[^.]`: `bullet 59 AC3` holds it zero times; `bullet 59 S3`, which quotes the sweep's pattern, holds it once. (DERIVED)
- AC10 — `--dispatch`: the F1 span of `sec 61 '## 8.'`, from its `- **F1 ` line to the next `- **F` line and joined, names it once, and `fail 49` and `unattended-build.js#ordered` once each; the F2 span names `fail 49` zero times. (DERIVED)
- AC10 — `grep -c 'is a new leg\|That is harmless'`: over 61's spec joined by `tr -s '[:space:]' ' '` it printed 0; over 61 at `fad031a8c`, before its rev-6, it printed 1. (DERIVED)
- AC10 — `neither CLOSED nor WONTDO, so the consumer would build`: `grep -c` over `tools/unattended/unattended.sh` printed 1, a line of `tools/unattended/unattended.sh#verb_dispatch`; over `tools/workflows/unattended-build.js` it printed 0. (DERIVED)
- AC11 — `base=$1`: in the read of `sec 59 '### The one version oracle'` it sits on line 3, `base does not resolve` on line 5 and the first `rev-list` on line 6. (DERIVED)
- AC11 — `base does not resolve`: over a scratch copy of 59 with `base=$1` moved below the refusal inside that section alone, the read put the refusal on line 4 and `base=$1` on line 5. (DERIVED)
- AC11 — `deadbeefdeadbeefdeadbeefdeadbeefdeadbeef`: `bullet 59 AC21` names it once, and `the empty string` once; `bullet 59 AC2` names neither. (DERIVED)
- AC12 — `[[:blank:]]`: the read of `sec 59 '### The shared key reader'` holds it once and `[ \t]` zero times; over a scratch copy of 59 with the class respelled `[ \t]`, the same read holds `[ \t]` once and `[[:blank:]]` zero times. (DERIVED)
- AC12 — `with a tab`: `sec 59 "### The suite's rows"` names it once; the read of `### The shared key reader` names it zero times. (DERIVED)
- AC14 — `§4's block`: `bullet 59 S21` names it once, and `superseded` once; `bullet 59 S20` names neither. (DERIVED)
- AC14 — `grep -lE '^t=\$\(git rev-list'`: over the specs neither CLOSED nor WONTDO, this spec and 64's, it printed nothing; 59's spec is CLOSED at rev-7 and outside that population (Items diverged). (DERIVED)
- AC18 — `grep -cE 'TOOL-dPlacedRequest-60\b.*AC2'`: `entries 57` piped to it printed 1. (DERIVED)
- AC18 — `grep -cE 'TOOL-dPlacedRequest-60\b.*AC2'`: over a scratch copy of 57 with its rev-5 entry, the one naming unit 60's read, removed, `entries` gave 4 entries where the tree gives 5, and the count printed 0. (DERIVED)
- AC19 — `tr -s ' '`: the `bullet` line of `sec 59 '### The criterion readers'` holds it once; its `sec` line holds it zero times. (DERIVED)
- AC19 — `fixture's base`: over a scratch copy of 59 whose AC21 wraps between `fixture's` and `base` at every occurrence, `bullet` printed it once in its joined line, and unit 60 S1's form without the join printed it zero times while printing `fixture's` on 3 lines. (DERIVED)

## Readings beside the criteria

- The tree's 59 AC21 already wraps once, after its first line; unit 60's form finds the phrase twice over the tree, from the two lines that do not wrap, so the scratch copy rewraps those two. (DERIVED)
- Over the whole folder, `grep -lE '^t=\$\(git rev-list'` listed the specs of units 55, 56 and 59, each CLOSED; 59's §4 names the blocks of 55 and 56 superseded by its own. (DERIVED)
- The unit's commits change no file outside the build folder and the spec's status cell, so no function is minted, renamed or deleted. (DERIVED)
- The bug-class checklist over the pass commit selected `fixture-passes-by-finding-nothing`: every zero above is paired with a read of the same population that printed its token, AC4's empty sweep with a scratch folder over which it printed a bullet, and every hold with a label, heading or scratch copy that reads otherwise. (DERIVED)
- It selected `heredoc-escape-reaches-the-regex`: a first `sed` respelling of AC12's class wrote a tab byte where `\t` was meant, and its section read held no `[ \t]`; the scratch copy was rebuilt by Python with the backslash spelled as a code point, and the probes ran from files written by the edit tools. (DERIVED)
- It selected `staged-break-substitutes-a-synthetic-value`: AC11's move, AC12's respelling, AC18's removed entry, AC19's rewrap and AC4's respelled base each change the shipped text of the spec they read, never a stand-in. (DERIVED)
- It selected `criterion-asserts-what-its-own-command-cannot-show` and `amendment-leaves-its-other-half-standing`: AC14's population clause names a spec its own selector excludes once 59 closed, the clause the re-grounding left beside its rev-5 order; it is recorded under Items diverged, not read as held. (DERIVED)
- It selected `one-value-field-records-a-mixed-outcome`: the close commit names AC14's diverged clause beside the criteria observed. (DERIVED)
- It selected `ledger-token-wrapped-across-a-line-joins-nothing`: every answer keeps its tokens on one line, and a probe found each answer's first token in its criterion's joined text. (DERIVED)
- It selected `inline-fence-swallows-the-rest-of-the-file` and `pipe-in-a-code-span-splits-a-table-cell`: this record holds no fence and no table, so its pipes sit in list items. (DERIVED)

## Items diverged

- AC14's second clause, that the `grep -lE` over the specs neither CLOSED nor WONTDO prints 59's spec alone, cannot be observed as written: 59's spec closed at rev-7 before this pass, so the live population is this spec and 64's, and over it the grep printed nothing. The fact the clause guards, one live copy of the oracle's sketch at most, holds: no live spec carries a copy, and the three CLOSED specs that do are 59 and the two it supersedes.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop. The spec declares no new arm.

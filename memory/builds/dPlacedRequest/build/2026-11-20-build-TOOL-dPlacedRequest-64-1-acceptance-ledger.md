# TOOL-dPlacedRequest-64 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-64

The unit was observed from its spec at rev-4 on base `cf35e61ff`. It builds nothing and touches no
product file: every criterion reads the text of the CLOSED specs 59, 61, 62, 63 and 52, or this
spec, through the readers `sec`, `bullet` and `entries` cut from the fence of spec 59's
`### The criterion readers` section and sourced unchanged. No gate, suite or bar ran in this pass.
Every reading below is the criterion's own read over the tree, or over a scratch copy made under the
run's scratch directory, paired with a control read that comes back without its token. A control
named "at `c1fdd8f36^`" reads the spec as it stood before the re-grounding that made this unit's
amendments, taken by `git show`. The items the spec marks NOT OBSERVED or resolved in its design
(S2, S4, S11, S16) carry no criterion and were not read.

**Evidences:** TOOL-dPlacedRequest-64
- AC1 — `grep -c 'is a new leg\|That is harmless'`: over 61's spec joined by `tr -s '[:space:]' ' '` it printed 0; over 61 at `c1fdd8f36^` it printed 1. (DERIVED)
- AC1 — `fail 49`: the risks clause of `sec 61 '## 5.' | tr -s '[:space:]' ' '`, cut from its `risks — ` to the next clause, names it once and `--dispatch` once; the security clause of the same read names neither, and so does 61's risks clause at `c1fdd8f36^`. (DERIVED)
- AC1 — `tr -s '[:space:]'`: `bullet 63 AC10` names it once; `bullet 63 AC9` names it zero times. (DERIVED)
- AC3 — `fixture's( later)? base`: `sec 59 '### The live sweep'` piped to `grep -cF` printed 1; the read of `### The criterion readers` printed 0, and 59's live sweep at `c1fdd8f36^` printed 0. (DERIVED)
- AC3 — `bullet 63 S1`: it names `fixture's( later)? base` once; `bullet 63 S2` names it zero times. (DERIVED)
- AC5 — `too late for stdin`: `sec 59 '### Evidence' | tr -s '[:space:]' ' '` names it once; 59's Evidence at `c1fdd8f36^` names it zero times. (DERIVED)
- AC5 — `from a file and through a pipe`: the same joined read holds it zero times; over a scratch copy of 59 whose Evidence's first bullet reads `from a file and` at a line end and `through a pipe` on the next, the joined read holds it once and a line-wise `grep -cF` prints 0. (DERIVED)
- AC5 — `BEGIN{BINMODE=3}`: `bullet 63 AC7` names it twice; `bullet 63 AC8` names it zero times. (DERIVED)
- AC6 — `slice_fn CLAIM_KV_AWK var`: `sec 59 "### The suite's rows"` holds it once, and `[ "${2:-}" = var ]` once; the read of `### The shared key reader` holds neither, and 59's rows section at `c1fdd8f36^` holds no guard. (DERIVED)
- AC6 — `grep -c 'eval "'`: the same rows read piped to it printed 1; the shared key reader's read printed 0, and so did 59's rows section at `c1fdd8f36^`. (DERIVED)
- AC7 — `%s|%d`: the `read_kv_row` definition in `sec 59 "### The suite's rows"`, its first line and the next, holds it once; the read of `### The shared key reader` holds it zero times. (DERIVED)
- AC7 — `live|4`: the rows read names it once, and `od -c` once; the shared key reader's read names neither. (DERIVED)
- AC8 — `52's`: `bullet 59 AC13` names it once, and the backticked `sec` once; `bullet 59 AC20` names neither. (DERIVED)
- AC8 — `bullet 62 S2`: it names `52's` once; `bullet 62 S3` names it zero times. (DERIVED)
- AC8 — `^### The oracle`: `grep -c` over 52 printed 1; over 59, whose oracle heading is `### The one version oracle`, it printed 0. (DERIVED)
- AC9 — `fixture's base`: a scratch copy of 59 whose AC21 says `a base` at each of its three occurrences, one wrapped, changes three lines; `bullet` given its path, piped to the criterion's `grep -cE`, printed 0, the same bullet still naming `deadbeefdeadbeefdeadbeefdeadbeefdeadbeef`; given 59's own path it printed 1. (DERIVED)
- AC10 — `grep -rlE '^bullet\(\) ' memory/builds/dPlacedRequest/spec/`: it printed 59's spec alone; the same pattern over the folder at `c1fdd8f36^` printed 63's spec alone, and over the readers cut from 59's fence it printed that file. (DERIVED)
- AC10 — `unit 59 §4's readers`: `sec 62 '## 6.'` names it once and `sec 63 '## 6.'` once; `sec 62 '## 5.'` names it zero times, and so does 63's §6 at `c1fdd8f36^`. (DERIVED)
- AC12 — `line 7[0-9]`: `sec 62 '### Evidence'` piped to `grep -c` printed 0; 62's Evidence at `c1fdd8f36^` printed 1. (DERIVED)
- AC13 — `"^### The oracle's head"`: `sec 62 '### Evidence'` names it once, and `'^### The one version oracle'` once; the read of 62's `### Files touched` names neither. (DERIVED)
- AC14 — `extract_run_facts`: `sec 62 '## 10.'` names it twice, and `index() == 1` once. (DERIVED)
- AC14 — `sed -n '/^## 2`: the same read piped to `grep -c` printed 0; 62's §10 at `c1fdd8f36^` printed 1. (DERIVED)
- AC15 — `entries`: `bullet 62 AC4` names the backticked reader four times and `bullet 63 AC18` once; `bullet 62 AC3` names it zero times. (DERIVED)
- AC15 — `grep -lE "awk '/\^## 9"`: over the specs neither CLOSED nor WONTDO, one file and that file this spec, it printed nothing; over the whole folder it printed 24's spec, CLOSED, and over the copies of 52, 54, 59, 61, 62 and 63 at `c1fdd8f36^` it printed 62's and 63's. (DERIVED)
- AC17 — `grep -cE '\.(sh|js|py|md):[0-9]'`: each of 59's, 61's, 62's, 63's and this spec printed 0; at `c1fdd8f36^` 59 printed 2, 61 printed 8 and 63 printed 10, and 62 and this spec printed 0. (DERIVED)
- AC17 — `unattended.sh#fact`: `sec 63 '### The closed specs'` names it once, and `lib-unattended.sh#extract_run_facts` once; the read of 63's `### Evidence` names neither. (DERIVED)
- AC18 — `sec "$1" '## 9.'`: the `entries` line of `sec 59 '### The criterion readers'` holds it once; that section's `bullet` line holds it zero times. (DERIVED)
- AC18 — `tr '\n' ' '`: `bullet 62 AC4` and `bullet 63 AC18` each hold it zero times; the readers section holds it once, in `bullet`'s own join. (DERIVED)
- AC18 — `AC13`: over a scratch copy of 61 whose rev-6 entry wraps between `TOOL-dPlacedRequest-62` and `to AC13`, no physical line holding both, `entries` printed six entries and `grep -cE 'TOOL-dPlacedRequest-62\b.*AC13'` over them printed 1; over a copy with that entry's id respelled `unit 62`, `entries` printed 0 while the whole log joined by `tr '\n' ' '` printed 1, crossing from rev-2's id to rev-6's `AC13`. (DERIVED)
- AC19 — `deadbeefdeadbeefdeadbeefdeadbeefdeadbeef`: `bullet 59 AC21` names it once, and `the empty string` once; `bullet 59 AC2` names neither. (DERIVED)
- AC19 — `an empty base and an absent sha`: `sec 59 '## 5.'` names it once, line by line and joined; 59's §5 at `c1fdd8f36^` names it zero times. (DERIVED)

## Readings beside the criteria

- The tree's 61 already wraps its rev-6 entry between the id and `to AC13`, so AC18's scratch copy is the tree's bytes, and the respelled copy is the one that changes them. (DERIVED)
- The text 59's rows section states is the shipped code: `tools/unattended/unattended.test.sh#slice_fn` holds the guard `[ "${2:-}" = var ]`, and the same file's `read_kv_row` prints `%s|%d` and is followed by `slice_fn CLAIM_KV_AWK var`. (DERIVED)
- The unit's commits change no file outside the build folder and the spec's status cell, so no function is minted, renamed or deleted. (DERIVED)

## Items diverged

None.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop. The spec declares no new arm.

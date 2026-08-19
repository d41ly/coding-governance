# Tier-2 review — the cumulative diff landing on main, `75a664fbeedf0e9b41bbde56194d14ee37bc018d...HEAD`

**Serves:** diff-review TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5

## Verdict: BLOCKED

## Review shape

- **raw 27 · confirmed 25 · refuted 2 · unverified 0 · precision 0.93**
- Confirmed severities as rated: **0 BLOCKER · 6 HIGH · 11 MEDIUM · 8 LOW.**
- After dedupe the 25 confirmed findings collapse to **15 distinct defects: 4 HIGH, 8 MEDIUM, 3 LOW.**
  Nothing was downgraded; the duplicates are the same defect reached by separate lenses. The raw id
  set behind each defect is printed in its heading so the join back to the pipeline stays checkable.
- Every finding below survived an adversarial skeptic pass and carries a reproduction. No finding is
  outstanding for want of a verdict.

Nothing was rated BLOCKER upstream. The verdict is BLOCKED anyway, on H1/H2/H3/H4: the unit's own
premise fails at three of the four. The new gate certifies a tree it cannot actually read (H1) and is
silent over six live carriers of the exact sentence it exists to remove (H2); the shipped docs now
assert a per-repository declaration mechanism that does not exist anywhere in the tree (H3); and the
BINDING protocol contradicts itself about where the number lives, with both gates green over the
contradiction (H4). Those are not polish items — they are the deliverable not doing the thing.

---

## HIGH

### H1 — the new gate's scan silently drops files, swallows its own errors, and reports a count it did not grep
`tools/check-agent-cap-restatement.sh:54` (raw ids 1, 11) · ships to adopters via
`tools/govkit/entries/check-agent-cap-restatement.kit.toml`

Line 54 is `hits=$(printf '%s\n' "$pop" | xargs grep -InE "$PAT" 2>/dev/null || true)`. Three defects
in one line:

1. **Newline-delimited paths into bare `xargs`.** Any tracked `.md` whose name holds a space, quote
   or backslash is split into fragments and never opened. Reproduced: a scratch repo with
   `Design Notes.md` containing `A review spawns at most 5 agents TOTAL.` exits 0 and prints
   `agent-cap-restatement: clean — 2 markdown file(s) scanned, 0 waiver(s)`.
2. **`2>/dev/null || true` swallows both channels.** `printf '%s\n' "Design Notes.md" "README.md" |
   xargs grep -InE x` emits `grep: Design: No such file or directory` and rc=123; the redirect eats
   the stderr and `|| true` eats the exit code, so the scan cannot report that it failed.
3. **The reported count is a lie by construction.** The `N markdown file(s) scanned` line at :99 is
   derived from `$pop` — files *listed* — not from what grep actually opened.

The same line omits `-H`, so when a batch holds a single file grep prints no path. Reproduced in a
one-md-file repo: the failure block reads `  3:A review spawns at most 5 agents TOTAL.` under a
remedy line saying "Point at the file that resolves it", naming no file. A fresh adopter tree is
exactly the single-file case. The self-test misses it only because `mk()` always creates `README.md`
alongside the fixture, giving grep a two-file argv.

This is the vacuity class the script guards for the *population* at :47-52 and does not guard for the
*scan*.

**Fix.** NUL-delimit and force the filename, and stop treating a failed scan as "no hits":

```sh
hits=$(git ls-files -z '*.md' | grep -zvE "$FROZEN" | xargs -0 grep -HInE "$PAT")
rc=$?; [ "$rc" -le 1 ] || { echo "agent-cap-restatement: the scan FAILED"; exit 2; }
```

**Left-shift gate.** Add a self-test arm whose fixture filename contains a space, and one whose
population is a single `.md` file asserting the failure text carries `<path>:<line>:`. Both are `ck`
calls in the existing suite; neither exists today.

---

### H2 — the gate reports `clean` while six live in-population carriers still state the bound as a bare digit
`tools/check-agent-cap-restatement.sh:43` (raw id 20)

`bash tools/check-agent-cap-restatement.sh` exits 0 on this tree
(`clean — 61 markdown file(s) scanned, 1 waiver(s)` — verified). Piping the six carriers below
through the gate's own `BOUND`/`NOUN`/`PAT` returns zero matches:

| carrier | text |
|---|---|
| `parallel-coding-governance.template.md:182` | `CONCURRENCY ≤ 5, ALWAYS` · `cap-5 helpers` · `at most 5 verify agents TOTAL` |
| `parallel-coding-governance.template.md:189` | `the ≤5 cap` |
| `AGENTS.md:30` | `the ≤5-verifier arity rule` |
| `README.md:72` | `the cap-5 … helpers` |
| `WIRE-INTO-PROJECT.md:510` | `the cap-5 … helpers` |
| `tools/drift-audit/README.md:9` | `protocol's ≤5` |

All six are inside the scanned 61-file population — none is under a `FROZEN` prefix. Three blind
spots produce this: `NOUN` has no `verify`, no `cap`, no `helpers`; the space before the noun is
mandatory so `5-verifier` cannot match; and `PAT` cannot express the reversed form `cap-5` where the
bound word follows the digit. `at most 5 verify agents TOTAL` is the canonical target shape and is
missed only because `verify` sits between the digit and `agents`.

The AGENTS.md bullet added by this same diff states the bar property as "no LIVE prose asserts the
fan-out bound as a bare number". That is false on the tree the gate just certified green — and the
strongest carrier, the shipped playbook, ships unfixed.

**Fix.** `NOUN='(agents?|verifiers?|lens(es)?|skeptics?|helpers?|verify|cap|concurrent|verify-stage|…)'`,
make the space optional (` ?` → `[ -]?`) so `5-verifier` matches, and add a reversed alternative
`cap-?[0-9]+`. Then fix or waive the six hits; the three in `parallel-coding-governance.template.md`
and `AGENTS.md:30` are precisely the restatements this unit set out to remove.

**Left-shift gate.** A self-test arm per *carrier shape actually present in this corpus* — feed the
six literal strings above as fixtures and require a hit on each. A gate written from a pattern rather
than from the measured population is the shape that produced this; freezing the measured shapes is
what stops it recurring.

---

### H3 — three shipped documents assert a per-repository declaration mechanism that does not exist
`README.md:75`, `memory/guides/REVIEW-PROTOCOL.md:13`, `tools/workflows/REVIEW-PROTOCOL.template.md:13`
(raw ids 12, 22)

README.md:75 now reads "That number is DECLARED per repository and read by
`tools/hooks/agent-cap.js`". The hook holds `const CAP = 5` (`:55`) and `const MAX_VERIFIERS = 5`
(`:114`); its header at `:26` reads "CAP: 5, a FILE CONSTANT and not overridable"; `:53-54` says "A
BARE LITERAL, never an environment read"; `:52` says the file "is deployed verbatim", which kills the
charitable per-repo-copy reading. The only external read in the whole file is `process.env.AGENT_CAP`,
which is *refused*, not honored. There is no conf read and no declaration channel.

The diff replaced a true sentence ("The 5 is a FILE CONSTANT and not overridable") with a false one.
`tools/workflows/check-protocol-parity.test.sh:83-85` concedes it in its own new comment: "the second
half — that the pointed-at carrier is one the hook actually reads — belongs to the commit that makes
the hook read it, and no such commit exists yet". HEAD's own commit message says the same ("Unit 4 is
parked and agent-cap.js still holds a bare literal").

Consequence: `WIRE-INTO-PROJECT.md:513` still says "a file constant — there is no environment
override", so the two front-door documents shipped in one release disagree, and an adopter is sent
looking for a declaration that is nowhere in the tree. HEAD (93a0574) fixed three carriers of this
claim and missed these three.

**Fix.** Restore the accurate wording in all three: the number is a file constant inside
`tools/hooks/agent-cap.js`, resolved at the call site, at the helper's default parameter and at the
`gov:bounded-fanout` width. Re-add "declared per repository" in the commit that makes the hook read a
declaration, not before.

**Left-shift gate.** Extend `check-playbook-parity.sh`'s declared-pair table with a pair whose
extraction reads `^const CAP = ([0-9]+)` from the hook and whose claim side is the README/protocol
sentence *shape* — i.e. red when a document claims a declaration channel while the hook's only
carrier is a literal. Cheaper interim: a grep leg banning `DECLARED per repository` in any file
shipped alongside a hook that contains `never an environment read`.

---

### H4 — the BINDING protocol contradicts itself about where the number lives, and both gates are green over it
`memory/guides/REVIEW-PROTOCOL.md:13` vs `:127`/`:129` (raw ids 8, 13, 21) · mirrored byte-for-byte in
`tools/workflows/REVIEW-PROTOCOL.template.md`

Line 13 (added by this diff): "The NUMBER is not written here." The same document then writes it:

- `:115` — `boundedParallel(thunks, 5)` / `boundedPipeline(items, 5, …stages)` (an instruction to an
  agent, not a measurement)
- `:127` — "A K it cannot resolve to an integer ≤ 5 is denied"
- `:129` — "The 5 is a FILE CONSTANT. There is no environment override"
- `:153` — "The lens allowance is **5**"

`:127`/`:129` sit inside the section this same diff retitled to "Concurrency — the at-once bound
`agent-cap.js` resolves, always". A reader holding this one document gets two answers to "what is the
cap and where does it live" — the exact class the unit was written to close.

Neither gate can see it, and both failure modes are structural:

- `check-agent-cap-restatement.sh` needs a bound word adjacent to a fan-out noun. "is denied" and "is
  a FILE CONSTANT" are in neither list. Ran it: exit 0.
- `tools/workflows/check-protocol-parity.test.sh` builds its per-section body with
  `/^## / { inb = … } inb { print }`, which **prints the heading line itself**, and both headings
  already contain the literal `agent-cap.js`. `grep -qF 'agent-cap.js'` therefore passes on the
  heading regardless of the body. The arm cannot detect the body losing its pointer. It is also green
  because the shipped template carries the identical contradiction at its own `:127`/`:129` —
  "in parity" here means both copies are wrong, which is the failure its own header warns about.

**Fix.** Pick one answer. Either de-number `:127`/`:129`/`:153` the way `:7`/`:13` were, or narrow
`:13`'s claim to the bound it actually covers ("the verify-stage total is not written here"). Render
the template copy the same way in the same commit. `:115` is executable code an agent inlines — give
it an explicit keep-with-reason disposition rather than leaving it to be inferred.

**Left-shift gate.** Two changes to `check-protocol-parity.test.sh`: (a) drop the heading from
`_body` (`/^## /{ inb=…; next }`) so the pointer arm grades the body it claims to grade; (b) add an
arm asserting no section that carries the "not written here" sentence also carries a bare digit
matching `\b[0-9]+\b` adjacent to `cap|constant|denied|allowance`. Both are self-contained and would
have reded this commit.

---

## MEDIUM

### M1 — an ambient `WAIVERS` env var can repoint the waiver registry and green the gate with no diff
`tools/check-agent-cap-restatement.sh:34` (raw id 2)

`WAIVERS=${WAIVERS:-tools/agent-cap-restatement-waivers.txt}`. Reproduced: with two real violations in
the tree, `WAIVERS=<blanket file> bash tools/check-agent-cap-restatement.sh` printed
`clean — 3 markdown file(s) scanned, 2 waiver(s)`, exit 0. A gate on the merge bar neutralised with no
diff and no committed evidence — the same channel this very diff *retires* one file over
(`check-memory-hygiene.sh:686`: "an env override that outranks a committed declaration leaves no diff
behind"). The bare generic name also makes accidental collision with an exported `WAIVERS` from a
wrapper or CI env plausible.

Sibling gates prove the convention: `check-install-prefix.sh:32` and `check-testsuite-counts.sh:28`
hardcode their registry paths; `check-playbook-parity.sh:33` uses the namespaced
`PLAYBOOK_KIT_WAIVERS` for the identical self-test need. "The self-test needs it" is not a defence — a
namespaced name serves that need.

**Fix.** Hardcode the path; give the self-test a private knob
(`AGENT_CAP_RESTATEMENT_WAIVERS_TEST`) or pass it as `$1`.

**Left-shift gate.** A repo-wide grep leg: no gate script under `tools/` may read an unnamespaced
`${WAIVERS:-…}` / `${CUTOFF:-…}`-shaped default for a committed registry or declaration. This class
has now recurred within one build (`SPEC10_CUTOFF` retired in unit 2, reintroduced in unit 5), which
is the standard for making it mechanical.

---

### M2 — a waiver row is matched against `path:line:text`, so a path fragment waives a whole subtree
`tools/check-agent-cap-restatement.sh:69` (raw id 3)

`case "$h" in *"$w"*` matches the row against the whole hit line. Reproduced: a single row
`docs/<TAB>one reason` against violations in `docs/A.md` and `docs/B.md` yields
`clean — 3 markdown file(s) scanned, 1 waiver(s)`, exit 0 — and the stale-waiver arm at `:89-94`
stays silent because it matches the same way. The implementation contradicts its own contract at
`:56-59` ("WAIVERS key on the MATCHED TEXT, never on `<path>:<line>`"): it accepts a path key, and
accepts it as a wildcard.

The accidental path is as real as the hostile one — a row whose text is a short fragment of a real
sentence silently waives every present and future file carrying it. The one committed control on this
gate (shrink-only staleness) is structurally blind to over-breadth: a row waiving a subtree is
indistinguishable from one waiving a sentence.

**Fix.** Strip the prefix before matching: `htext=${h#*:}; htext=${htext#*:}` then
`case "$htext" in *"$w"*)`.

**Left-shift gate.** A self-test arm asserting a path-fragment row does **not** waive, plus one
asserting a row that matches no *text* (only a path) reds as stale.

---

### M3 — `FROZEN` hardcodes `memory/` while the memory-tree kit lets an adopter relocate the tree
`tools/check-agent-cap-restatement.sh:40` (raw id 6)

`FROZEN='^memory/(builds|archive|gotchas|backlog)/'`, and the script reads no conf. `MEMORY_ROOT` is a
first-class configuration axis here, not a hypothetical: `.memory-tree.conf:2` declares it,
`adopt-memory-tree.sh:41` instructs the adopter to "EDIT IT (MEMORY_ROOT, …)", and the flagship gate
binds `M="$MEMORY_ROOT"` at `check-memory-hygiene.sh:82` and even carries the remedy "set MEMORY_ROOT
to the tree that has one".

In a target with `MEMORY_ROOT=docs/memory`, every build record, archive page, gotcha and backlog row
that QUOTES a fan-out carrier becomes a finding on first run. The only escape left is a text-keyed
waiver — which this file's own `:36-39` rules out for frozen records precisely because a text key
silences the live carriers sharing that sentence. The govkit descriptor is `scope = "repo"` with
`argv = []` and `why_no_adopter`, so nothing rewrites the constant on install.

**Fix.** Read `MEMORY_ROOT` from `.memory-tree.conf` when present, default `memory`, and build
`FROZEN="^${MEMORY_ROOT}/(builds|archive|gotchas|backlog)/"`.

**Left-shift gate.** Extend `check-install-prefix.sh`'s remit (or add a sibling predicate) to catch a
literal `^memory/` in any kit script that does not source `.memory-tree.conf` — the same "a path
SPELLED in something the adopter receives fails quietly" argument that gate already makes.

---

### M4 — `_read_lookback` is called outside main's `try/except DriftError`, so a bad declaration traceback-crashes as exit 1
`tools/drift-audit/drift_report.py:928` (raw ids 5, 14)

The call sits at `:927-928` inside the `if args.check:` block; main's `try/except DriftError → return 2`
only wraps `repo_root` / `load_conf` / `load_project_layer` at `~:858-865`, and `__main__` is a bare
`raise SystemExit(main())`. Reproduced twice — with `RATCHET_LOOKBACK = "14"` (a string) and with
`= 0` — the report prints normally, then `DriftError` propagates out of `main()`: raw traceback,
**rc=1**.

rc=1 is the gate leg's "a gateable signal is over its pin" exit. The `drift-audit records` leg
therefore reports drift where there is a config error, and the docstring's promise at `:145-152` — "a
refusal on the same channel `load_project_layer` uses", i.e. exit 2 with the `drift-report: ` prefix —
is broken at the only call site. Secondarily the call is reached only under `--check`, so the Tier-0
report an adopter is told to run *first* never validates the key at all. `selftest.py:951` imports
`_read_lookback` directly and catches `DriftError`, so it proves the raise and not that it reaches the
channel — it stays green.

**Fix.** Resolve it beside the other project-layer reads inside the existing `try:` (next to
`proj = load_project_layer(root)`) and pass the value into `ratchet_findings`.

**Left-shift gate.** A selftest arm that drives the **CLI** (`main(["--check"])` or a subprocess) with
an unusable `RATCHET_LOOKBACK` and asserts rc==2 *and* the `drift-report: ` prefix on stderr. The
existing arm's shape — call the function, catch the exception — is what let this through; the repo's
own idiom is to assert the message or the on-disk effect, never the raise alone.

---

### M5 — the `agent-cap` dossier claims the two new legs but its `globs` omit the three files that implement them
`memory/map/features/agent-cap.md:29` (raw id 15)

`[claims].gate-legs` names "agent-cap restatement" and "agent-cap restatement self-test";
`[paths].globs` lists only `tools/hooks/*`, `.claude/hooks/agent-cap.js`, three `tools/workflows/*`
files and the two `REVIEW-PROTOCOL` copies. Ran `python tools/codebase-map/map_diff.py 75a664f...HEAD
--verbose`: `tools/check-agent-cap-restatement.sh`, `tools/check-agent-cap-restatement.test.sh` and
`tools/agent-cap-restatement-waivers.txt` all land in **UNMAPPED**, while the structurally identical
sibling `tools/workflows/check-verifier-fanout.sh` resolves to `agent-cap`. They are not parked in
`memory/map/baseline.toml` either, so this is an omission rather than a declared deferral.

The coverage gate stays green because `test_codebase_map.py`'s ten inventories cover leg *names*, not
file paths. Root-level `tools/check-*.sh` gates plus their waiver registries are globbed by other
dossiers (`install-prefix.md:23-24`, `playbook.md:23-27`, `testsuite-counts.md:23-24`), so the
convention is unambiguous.

**Fix.** Add the three paths to `globs` and re-render the map.

**Left-shift gate.** An eleventh inventory in `test_codebase_map.py`: every tracked file reachable
from a claimed gate leg's own command line resolves to a dossier or a baseline row. That closes the
"claims the leg, does not glob the leg's files" gap generally, not just here.

---

### M6 — the shipped hygiene rule-set still states check 7's budget as a bare 300 after this diff made it a declaration
`tools/memory-tree/HYGIENE.template.md:61` and `:161`; `memory/HYGIENE.md:61` and `:161` (raw ids 16, 24)

This diff added `ENTRY_CAP_CHARS=300 ; BUILD_README_ENTRY_CAP_CHARS=350` to
`check-memory-hygiene.sh:52`, added both to the validation loop at `:61`, and deliberately de-numbered
the engine's own prose (`:409` lost "plus check 7's 350 chars"; `:444` became "at check 7's declared
entry budget"). The rule-set document was not touched: `:161` still reads
`**entry budget** — index entry lines ≤ 300 chars`, `:61` still says "is ONE physical line, ≤ 300
chars", and the 350 build-README tier is absent from the document entirely. `memory/HYGIENE.md`
carries the identical text at the identical lines, so kit/dogfood parity keeps both wrong together.

An adopter who declares `ENTRY_CAP_CHARS="400"` commits a rule-set document stating 300. The "File
caps" bullet directly above already does it correctly ("every cap is declared in `.memory-tree.conf`"
+ "The shipped defaults are"), and rule 6 at `:138-141` uses the key-name-plus-default idiom — so the
two halves of one section now disagree about whether the number is a declaration.

*(One correction to the raw finding: the missing 350 tier predates this diff. What this diff
introduced is a documented number the adopter can now override.)*

**Fix.** Rewrite `:61` and `:161` in the `:138` idiom — "index entry lines ≤ `ENTRY_CAP_CHARS` (300 by
default); a build `README.md` ≤ `BUILD_README_ENTRY_CAP_CHARS` (350)" — in the template, then
re-render `memory/HYGIENE.md` so `check-method-carriers.sh` stays byte-equal.

**Left-shift gate.** Add a declared pair to `check-playbook-parity.sh`'s in-script table (or a
sibling predicate for the hygiene documents): every key in the engine's `for _k in` cap loop must be
named in `HYGIENE.template.md`, and no bare integer equal to a shipped default may appear in a rule
line whose key is declared. Anti-vacuity applies — a pair matching nothing reds.

---

### M7 — the hook's only remediation string routes the operator into a document made deliberately silent, and into a red bar
`tools/hooks/agent-cap.js:697` (raw id 25)

The `AGENT_CAP` refusal reads: "to change the number, change it in `tools/hooks/agent-cap.js` and in
`memory/guides/REVIEW-PROTOCOL.md`, where the rule is stated." After this diff that document says "The
NUMBER is not written here" (`:13`), and `check-protocol-parity.test.sh` was rewritten in the same
diff to freeze the pointer instead of the digit — so the design now forbids the second half of the
instruction.

Following it also reds the bar. `tools/check-agent-cap-restatement.sh` is a registered leg
(`gate-legs.json:548`), its `PAT` matches "at most 7 agents" (verified), `memory/guides/` is not a
`FROZEN` prefix, and the only waiver row is the measurement line. Reachable on any run with
`AGENT_CAP` set; no gate scans `.js` for this string.

**Fix.** Trim the message to name `tools/hooks/agent-cap.js` alone as the place the number changes.

**Left-shift gate.** Extend `check-agent-cap-restatement.sh`'s population beyond `*.md` to the string
literals in `tools/hooks/*.js` and `tools/workflows/*.js`, or add a narrow leg asserting no shipped
remedy string names `REVIEW-PROTOCOL.md` as a place to write the number. The markdown-only population
is what made this carrier invisible, and unit 4's spec review already flagged the same blind spot.

---

### M8 — a literal `\n` in a test arm passes a stray file operand to `grep`
`tools/memory-tree/check-memory-hygiene.test.sh:1267` (raw ids 18, 23)

`cat -A` confirms the line is `grep -qE "^$_k=" "$EX" \n    || { … }` — an unquoted `\n`, which the
shell unquotes to the word `n`, so grep receives a second file operand named `n`. The correct
`\`-newline idiom is used 85 lines down at `:1354`, which makes this a typo rather than intent — the
escape reached the source as a control sequence, this repo's own `heredoc-escape-reaches-the-regex`
class.

Green today only by accident: GNU `grep -q` short-circuits on the first match and never opens `n`; on
a miss it exits 2 from the missing file, so the FAIL branch still fires (and leaks
`grep: n: No such file or directory` to stderr on every failing iteration). Reproduced the hole: after
creating an `n` containing `BAR=9`, `grep -qE '^BAR=' ex.conf n` exits 0 — a key genuinely missing
from the shipped `.memory-tree.conf.example` passes silently. The line predates this diff, but this
diff rewrote the loop it is the body of (hand-kept list → `_engkeys` derived from the engine)
specifically to make this assertion reliable, and left the broken operand in place.

**Fix.** Delete `\n    `; the `||` is already on the same physical line.

**Left-shift gate.** `tools/gate-lint/` already scans `.ps1` for classes that make a script misbehave
*silently*. Add the shell sibling: a scan for an unquoted `\n`/`\t` token in a `*.test.sh` or `*.sh`
command position. It is a byte-level regex, it fits the kit's stated remit, and it catches the whole
class rather than this line.

---

## LOW

### L1 — a padding `n=$((n+1))` inflates the reported assertion count
`tools/check-agent-cap-restatement.test.sh:78` (raw id 9)

Exactly 8 `ck` calls execute (`:32, :39, :45, :54, :55, :62, :69, :76`), each incrementing `n` inside
`ck()`. `:78` is a bare `n=$((n+1))` with no assertion behind it, and `FLOOR_ASSERTIONS=9` at `:79`.
The suite prints `PASS (9 assertions)`. No sibling suite does this — checked
`check-testsuite-counts.test.sh:106`, `unattended.test.sh:1670`, `check-unattended.test.sh:1028`,
`check-memory-hygiene.test.sh:1358`, `manifest-check.test.sh:664`; all count only real arms.

`tools/check-testsuite-counts.sh` grades this printed number against a shrink-only floor, so the floor
is calibrated one above the true arm count: a future editor who deletes the padding trips "arms are
UNREACHABLE rather than absent" without having removed an arm.

**Fix.** Delete `:78` and set `FLOOR_ASSERTIONS=8` — or convert the padding into the real arm it was
standing in for (the space-in-filename arm H1 needs is the obvious candidate).

**Left-shift gate.** `check-testsuite-counts.sh` already derives its population from
`gate-legs.json`. Add one predicate to it: in a compliant suite, the number of `n=$((n+1))` sites
outside the counter helper must be zero. Cheap, structural, and it names exactly this shape.

---

### L2 — a second, hand-kept example-conf key loop survives below the derived one it was meant to replace
`tools/memory-tree/check-memory-hygiene.test.sh:1352` (raw ids 19, 27)

`main` carried two hand-kept loops. This diff replaced the 7-key one at old `:1231` with the derived
loop at `:1265` (`$_engkeys` yields all ten cap keys plus `READ_PATH_HEADROOM`) and left the older
5-key one at `:1352` untouched — `INDEX_CAP_BYTES INDEX_CAP_LINES GUIDE_CAP_BYTES
BUILD_README_CAP_BYTES DOSSIER_CAP_BYTES`, a strict subset asserting the identical property over the
identical file. Its only diff-context change was the `FLOOR_ASSERTIONS` bump below it.

Harmless at runtime — a subset can only under-cover — but it is exactly the hand-kept-list drift
class the change existed to remove, and it is the copy that will silently fall behind the next engine
key. A reader who greps for the assertion may land on the stale one and conclude coverage is five keys.

**Fix.** Delete `:1349-1357` and re-derive `FLOOR_ASSERTIONS` from an actual run, which the floor's
own comment sanctions.

**Left-shift gate.** Fold into the L1 predicate's home: `check-testsuite-counts.sh` can assert that no
suite contains two `for _k in` loops greping the same file for the same `^KEY=` shape. Narrower and
likelier to stick: a comment convention is not a gate — the derived loop should be the only site that
names `.memory-tree.conf.example`, and one grep asserts that.

---

### L3 — half-applied edit leaves the curation-debt header truncated with an unbalanced parenthesis
`memory/project/curation-debt.txt:2` (raw ids 10, 17, 26)

`git diff 75a664f...HEAD -- memory/project/curation-debt.txt` shows exactly one changed line:
`(25600 B / 350 chars)` → `(BUILD_README_CAP_BYTES`. The closing paren, the second key (the
per-line char cap, now `BUILD_README_ENTRY_CAP_CHARS`) and the noun that "already above it" referred
to were all dropped. Lines 2-3 now read:

```
# Two build READMEs entered the index set at TOOL-aRuledFrontispiece-5's tier (BUILD_README_CAP_BYTES
# already above it. Both are other builds' records, so slimming them is not this build's to do —
```

Comment-only, so nothing breaks. But the registry is shrink-only and its rows drain when an owner
reads this reason, and the reason no longer names which entry cap the READMEs exceed — the one fact
that reader needs.

**Fix.** `… tier (BUILD_README_CAP_BYTES / BUILD_README_ENTRY_CAP_CHARS) already above it.`

**Left-shift gate.** None worth building — a prose-balance check over comment headers is more gate
than the class deserves. This is what a reviewer reading the diff catches; the honest left-shift is
that a de-digitizing pass should be applied by search-and-replace over the *key pair*, never one half
at a time.

---

## What I did not check

- Whether the diff's four declarations are collectively *sufficient* for the build's Tier-2 bar, as
  opposed to individually correct.
- The `parallel-coding-governance.template.md` byte budget after unit 5's edits.
- Any adopter-tree run of the new gate or the new govkit entries; H1/H3/M3 are all reasoned from
  descriptors and scratch repos, not from a real adoption.
- Whether any prose in the diff is a fluent paraphrase that is subtly wrong — the structural gates
  say plainly they cannot see that class, and neither can this pass at scale.

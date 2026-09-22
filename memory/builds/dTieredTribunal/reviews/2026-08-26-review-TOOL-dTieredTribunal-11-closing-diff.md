**Serves:** diff-review TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15

# Review — dTieredTribunal run 2, the cumulative diff landing on main

**Measured on:** node `a`, worktree `C:/projects/coding-governance/.claude/worktrees/dtieredtribunal-build-spec-7218ea`, clean.
Every finding below was re-read or re-run against the shipped file before it was written down. Line
numbers are from that read, not from the finder's report, and the reproductions quoted in each
`Evidence` block were re-executed here.

**Range:** `cd971285f95e8373a2ce8cd078973f51e1c523db...HEAD` (`eb4b0660`) — ten commits, 39 files,
+3463/-180. Five product units (`b599fcb6`, `91c5d3ac`, `fb2d692e`, `f96738b7`, `eb4b0660`) sit on
top of five records-only commits.

**Round:** 1. First adversarial review of run 2's CODE. The two spec-audit rounds already in
`reviews/` audited the SPEC set; this is a different subject.

## Verdict: BLOCKED

Two blockers, and neither is a matter of taste. Unit 14 introduced a knob that silently disables
three of the hook's four script rules, declared one mechanical control against it, and that control
cannot fire against the command spelling this repo actually ships. Unit 11 gave the review harness a
spec arm that can return `clean: 0 findings` having read nothing — the exact false-clean family unit
15 added to the gotcha catalogue in this same diff. Both are one-expression fixes. Neither is
observable from a green bar today, which is why they are blockers rather than fixes-on-the-way-past.

**Shape:** raw 24 · confirmed 21 · refuted 3 · unverified 0 · precision 0.88.

The 21 confirmed collapse to **11 distinct defects** — the lens fan raised the check-wiring hole three
times (ids 1, 12, 18), the `subjects.find` collapse three times (ids 3, 6, 20), the stranded kit
marker three times (ids 8, 15, 22), the check-review-join delegation three times (ids 11, 16, 19),
and two more twice each. Adjudicated severity is **2 blockers · 2 highs · 5 mediums · 2 lows**.

Two raises against the raw labels. D2 went high → blocker: a review harness that reports a clean bill
on a run that reviewed nothing is the one defect class this build spent a whole unit cataloguing, and
it shipped an instance of it in the same diff. D4 went medium → high: it is a documented coverage
REGRESSION against the awk it replaced, not a gap — the gate landed strictly weaker than what it
retired, in a build whose subject is checks that cannot fail. Everything else sits at the highest
label its duplicates carried.

Precision 0.88 is well above §8's ~0.5 floor and roughly triple the run-1 closing review's 0.30. The
lens priming was tight for this diff; the cost was that four lenses spent most of their budget on the
same four files, which is why the duplicate rate is high and the surface coverage is narrow. Nothing
in `memory/`, the dossiers or the generated regions drew a confirmed finding beyond D11.

## The recurring-bug-class checklist

`python tools/memory-tree/gotchas.py --for-diff cd971285..HEAD` selected 12 classes — 4 universal and
8 by anchor. Two of the anchored ones were written by this build. Classes that actually caught
something here:

| Class | Caught |
|---|---|
| `degradation-known-but-unreported` | D2 — added by unit 15, instantiated by unit 11 |
| `fixture-passes-by-finding-nothing` | D1, D4 — a guard whose failing case was never staged |
| `two-answers-to-one-question` | D5, D6, D7 — kit marker, gate header, BUILD-METHOD pointer |
| `absence-assertion-over-whole-file-text` | D4 — the ban's view discards where the join is written |
| `concurrency-is-not-a-budget` | D3 — a marked receiver accepted as bounded, one agent per element |

`heredoc-escape-reaches-the-regex`, `staged-break-substitutes-a-synthetic-value`,
`allowlist-narrower-than-the-root-it-guards`, `containment-tested-one-way`,
`hookspath-resolves-into-another-checkout`, `fold-text-is-unreviewed-surface` and
`trailing-comma-counted-as-an-element` were run over the touched area and produced nothing.

## Findings

| # | Sev | Site | One line |
|---|---|---|---|
| D1 | blocker | `tools/check-wiring.sh:143` | The `--only` assertion can never fire against the shipped command spelling |
| D2 | blocker | `tools/workflows/tier2-review.js:124` | A spec audit that resolved no subjects returns `clean: 0 findings` |
| D3 | high | `tools/hooks/agent-cap.js:210` | `boundedBranch`'s tail swallows any chain, so an unbounded receiver passes |
| D4 | high | `tools/hooks/agent-cap.js:819` | Rule 5 is blind to `${…}` interpolations, where a join is likeliest written |
| D5 | medium | `tools/hooks/scratch-guard.js:41` | Half-applied kit bump — one kit, two advertised versions |
| D6 | medium | `tools/workflows/tier2-review.js:116` | `find(...) \|\| null` kills the validator's only falsy arm |
| D7 | medium | `tools/workflows/check-review-join.sh:80` | The delegation false-reds with an empty reason and can false-green |
| D8 | medium | `tools/check-agent-cap-restatement.sh:36` | Three carriers claim both digits were deleted; one is still there |
| D9 | medium | `memory/guides/BUILD-METHOD.md:118` | M4 points at an `args` header that does not carry the spelling |
| D10 | low | `tools/hooks/agent-cap.js:255` | `markedWhy` is never invalidated, so a refusal can print a false reason |
| D11 | low | `memory/gotchas/degradation-known-but-unreported.md:75` | The anchor accounting is one short of the derived set |

---

### D1 — blocker — `tools/check-wiring.sh:143`

The S7 assertion that a wired agent-cap command carries no `--only` can never fire. Its
`grep -o '"command"[^"]*"[^"]*agent-cap\.js[^"]*"'` cannot cross the JSON-escaped `\"` inside the
command value, which is the canonical wiring form the hook's own header documents and the form
actually present in `.claude/settings.json`.

**Evidence.** `.claude/settings.json:9` is
`"command": "node \"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\""`. The `\"` after `node `
terminates the first `[^"]*` run, so the grep exits 1 with no output against the live file —
re-confirmed here. Splicing ` --only=join` into that same command (valid JSON) leaves it exit 1 too,
so control falls through to `echo "ok       agent-cap — PreToolUse hook wired"`. `--only=join` is a
real flag (`agent-cap.js:840`) that runs rule 5 alone and turns rules 1–4 — raw-primitive,
verifier-arity, cap-resolution — off with no diff. `wired()` at `:72` compares matchers only, so
nothing else catches it. `tools/hooks/README.md:58` and `memory/map/features/agent-cap.md` both claim
this file enforces the ban; `:143` is the only assertion anywhere, and `tools/check-wiring.test.sh`
is untouched by this diff, so the refusal's failing case has never been observed.

**Why blocker.** This is the single mechanical protection unit 14 declares for a bypass unit 14
itself introduced, and it is inert. It is also the precise shape recorded in this file's own comment
above it — the `AGENT_CAP` knob "that survived two releases by appearing to work".

**Fix.** Normalise before matching, the way `matchers_of()` already does:

```sh
tr -d ' \t\r\n' < .claude/settings.json | sed 's/{"matcher":/\n{"matcher":/g' \
  | grep -F agent-cap.js | grep -q -- '--only'
```

`grep -o 'agent-cap\.js[^,]*' .claude/settings.json | grep -q -- '--only'` also works and was
verified to fire on the tampered file and stay silent on the clean one.

**Left-shift gate.** Add a staged-break arm to `tools/check-wiring.test.sh`: write a scratch
`settings.json` carrying the `\"`-escaped spelling WITH `--only=join` and assert the `UNWIRED` row.
§7 requires a new gate's failing case be observed before it lands; this one never was, and the arm is
what makes that structural rather than remembered.

---

### D2 — blocker — `tools/workflows/tier2-review.js:124`

On the spec arm at round 1, an empty or unresolvable `subjects` is logged as a WARNING and the run
continues with an empty subject list. Four lenses are handed nothing to read, all return no findings,
and the harness returns `note: 'clean: 0 findings'`. The degradation is computed and never reaches
the verdict.

**Evidence.** `:111` defaults `subjects` to `[]`; `:113–116` sets `badSubject = 'none supplied'`
(truthy, so `!== null`); at round 1 `:124` logs and falls through. The acquire sentence then renders
`SUBJECTS:` followed by `[].map(...).join('\n')` — nothing. Lenses still complete, so `lensesDead` is
0, `allFindings` is empty, and control reaches `:341`, which returns
`{confirmed: [], report: null, blockers: null, highs: null, lensesRun: 4, lensesDead: 0, note: 'clean: 0 findings'}`.
No field in that return distinguishes "audited four specs, found nothing" from "audited zero specs".
The neighbouring dead-lens path at `:336` gets this exactly right — `UNVERIFIED: … nothing was
reviewed` — so the file already knows the shape and one of its two zero-finding exits does not use it.

Spec-11's parity claim ("a refusal above round 1 and a warning at round 1, matching the diff arm
exactly") does not hold: the diff arm's round-1 warning is about an unpinned base and its lens still
runs a real `git diff` against `origin/main`, while the spec arm's lens is handed an empty list.

**Why blocker.** `memory/gotchas/degradation-known-but-unreported.md`, added by unit 15 in this same
diff, defines this family; `tools/workflows/tier2-review.js` is one of its declared anchors. The
build shipped a fresh instance of the class it was cataloguing, in the file the catalogue points at.

**Fix.** On the spec arm an empty `subjects` has no degraded mode — there is no subject — so refuse
it at every round rather than only above round 1. If the warn-at-round-1 ladder must stay for a
malformed-but-present subject, carry the degradation into the verdict: set a `degraded` flag at `:124`
and make the `:341` return emit
`note: 'UNVERIFIED: subjects were not resolved — nothing was reviewed'`.

**Left-shift gate.** The general form, not this instance: a self-check arm asserting that every
zero-finding return path whose run was degraded emits a `note` starting `UNVERIFIED:` or `partial:`.
`clean:` must be unreachable whenever `lensesDead > 0` or the subject set is empty. That arm catches
the next zero-finding exit somebody adds, which is the class rather than the line.

---

### D3 — high — `tools/hooks/agent-cap.js:210`

`boundedBranch`'s identifier form is
`/^([A-Za-z_$][\w$]*)((?:\s*\.\s*(?:filter|slice)\s*\([\s\S]*\))?)$/`. The tail `[\s\S]*` swallows any
chain that merely STARTS with `.filter(` or `.slice(` and ends with `)`, so the only thing stopping a
growing chain is whether a literal word from the `grows` blacklist at `:243` happens to appear in the
source text.

**Evidence.** Against the shipped file, a Workflow call whose script is

```js
const LENSES = ['a','b','c']
const L = LENSES.slice(0).map((g) => allFindings).reduce(merge, []) // gov:fixed-verifiers
boundedParallel(L.map((x) => () => agent(x)), 5)
```

exits 0. Swapping `merge` for the inline `(a, b) => a.concat(b)` exits 2 with "its right-hand side can
GROW the receiver". Identical semantics, opposite verdict: the accept is decided by vocabulary, not by
what the chain does. The S3 comment three lines above claims "a chain of operations that cannot grow
it", which is not what the regex says, and the hole survives unit 13's S1 rewrite whose declared
purpose was to make every branch qualify on its own text.

**Fix.** Anchor the whole tail to the closed operation set rather than swallowing it:

```js
/^([A-Za-z_$][\w$]*)(?:\s*\.\s*(?:filter|slice)\s*\((?:[^()]|\([^()]*\))*\))*$/
```

Any other method in the chain then fails to match and the branch is denied, which is the right
default for a guard.

**Left-shift gate.** A self-test arm for `X.slice(0).map(...).reduce(merge, [])` asserting exit 2. No
current arm exercises a non-blacklisted growing method, which is why a blacklist could pass for a
whitelist for two releases. Pair it with an arm using a method name invented for the test, so the arm
cannot be satisfied by extending `grows`.

---

### D4 — high — `tools/hooks/agent-cap.js:819`

Rule 5 reads `blankLiterals`, which discards template-literal contents INCLUDING `${…}`
interpolations, so a ref-keyed join written inside an interpolation is invisible to the hook and to
the gate that now delegates to it.

**Evidence.** `blankLiterals` (`:443`) enters `tmpl` mode on a backtick and discards every byte to the
closing backtick. A two-line fixture

```js
const line = `verdict is ${byRef.get(f.ref)} for ${f.ref}`
const other = `${verdictByRef}`
```

exits 0 under `node tools/hooks/agent-cap.js --only=join`; the same two joins outside a template exit
2 and name both lines. The awk this replaced (`git show c7ccb18d`) tracked quote state but appended
every character, so it kept template contents and flagged both — `check-review-join.sh` lost coverage
it had.

**Why high, not medium.** The narrowing is disclosed in spec-14 §4, but its justification — "a
verdict join is a code construct and cannot live inside a string literal" — is false for an
interpolation, and the false positive it protects against (prompt PROSE in `tier2-review.js` template
literals) is fully avoided by blanking literal TEXT while keeping `${…}` contents. The design goal
never required the hole. The same file's `stripStrings` comment states the opposite — "template
literals are left ALONE — they can hold real `${code}`" — so the file now carries two answers to one
question. Report and prompt rendering in these harnesses is all template literals, which is the
likeliest place a ref join is actually written.

**Fix.** Give rule 5 a view that keeps interpolations: blank only the literal text between `${` and
`}` inside a template, tracking brace depth, or run `scanJoinFindings` over the per-line
`stripStrings` view that already leaves backticks alone for exactly this reason.

**Left-shift gate.** Both fixtures above as permanent arms in
`tools/workflows/check-review-join.test.sh`, beside the two that pin the string-contents narrowing —
so the two directions of the narrowing are pinned together and neither can be widened silently.

---

### D5 — medium — `tools/hooks/scratch-guard.js:41`

Half-applied kit bump. Unit 13 moved this marker 1.6 → 1.7 in step with agent-cap; unit 14 took the
kit to 1.8 in both agent-cap copies and left scratch-guard behind.

**Evidence.** `grep -rn 'gov:kit agent-cap@' tools/hooks/ .claude/hooks/` returns four carriers and
two answers: `tools/hooks/agent-cap.js:52` and `.claude/hooks/agent-cap.js:52` at `@1.8`,
`tools/hooks/scratch-guard.js:41` and `.claude/hooks/scratch-guard.js:41` at `@1.7`. The marker is
described in-file as what "ships inside the hooks kit entry" — it is the deployer's version signal in
an adopting tree. Spec-14 S10 names both scratch-guard sites explicitly among the four carriers, so
this is the unit's own AC11 failing on half of them. `tools/check-kit-versions.sh:47` greps the marker
only inside `tools/hooks/agent-cap.js`, so `bash tools/check-kit-versions.sh` exits 0 with the
mismatch present.

**Fix.** Set both scratch-guard copies to `gov:kit agent-cap@1.8`.

**Left-shift gate.** Extend the agent-cap block in `tools/check-kit-versions.sh` to derive its
population instead of naming one file: `git grep -l 'gov:kit agent-cap@'`, then assert every marker
equals `$ac`. That is how the memory-tree and unattended blocks already work, and it is the
presence-only hole that file's own header records for two earlier kits, recurring a third time.

---

### D6 — medium — `tools/workflows/tier2-review.js:116`

`subjects.find(pred) || null` collapses a falsy offending element back to the pass sentinel, so the
`!x` arm of the subject validator — the only arm that can return a falsy value — can never trigger
the refusal it was written for.

**Evidence.** Verified in node against the exact expression. `[null]`, `[undefined]`, `[0]`, `['']`
and `[false]` all yield `badSubject === null` and skip both the round-1 warning and the round>1
throw; a truthy offender `[{path:'a',blob:'zzz'}]` correctly refuses. Because `find` returns the
FIRST match, a genuinely bad subject after a falsy one is masked too. Downstream: `:298` renders
`  - undefined  blob undefined` and `:479` instructs the record to open with `<path>@<blob>`, so a
moving ref gets recorded as the immutable anchor the check exists to forbid; `[null]`/`[undefined]`
instead die at `x.path` with an opaque TypeError rather than the written refusal. A caller building
subjects by lookup (`paths.map(p => index[p])`) produces exactly this shape.

**Fix.** Use an index sentinel and reject non-objects explicitly:

```js
const i = subjects.findIndex((x) => !x || typeof x !== 'object' ||
  typeof x.path !== 'string' || !/^[0-9a-f]{7,40}$/.test(String(x.blob)))
const badSubject = subjects.length === 0 ? 'none supplied' : (i === -1 ? null : subjects[i])
```

**Left-shift gate.** A self-check arm with a falsy element (`[null]`) asserting the refusal fires at
round 2 — the arm that would have caught this is the one nobody wrote, because every existing fixture
supplies a truthy bad subject. Generalise it: any validator whose predicate contains a `!x` arm needs
one fixture whose offender is falsy.

---

### D7 — medium — `tools/workflows/check-review-join.sh:80`

The delegated gate reads only the pipeline's last exit status and filters the hook's message through
`sed -n '/^  L/,$p'`, so it both false-reds with an empty reason and can silently pass. Two symptoms,
one root: the loop treats "the hook exited non-zero" as "rule 5 fired".

**Evidence, false red.** `AGENT_CAP=7 bash tools/workflows/check-review-join.sh` prints
`review-join: FAILED — a ref-keyed verdict join reappeared` and lists all six scanned files with a
blank body. `agent-cap.js:861` exits 2 on its environment refusal before any rule runs, and that
message has no line starting with two spaces and `L`, so the sed discards it while the non-zero
status still populates `hits`. The remedy text then sends the operator to rewrite a join that is not
there. The sibling gate `check-verifier-fanout.sh` prints the whole message and diagnoses correctly.

**Evidence, false green.** `:27` sets `set -u` and never `pipefail`, and `:80` is
`out=$(node -e '…' "$f" | node "$HOOK" --only=join 2>&1)`, so only the hook's status is read. Empty
stdin reaches `JSON.parse` at `:852`, whose catch exits 0. A producer that threw (`readFileSync` on a
missing path) piped into the hook returns exit 0 with the producer's ENOENT on stderr, and the file is
recorded clean. Reachability is narrow — TOCTOU after the `[ -f ]` filter at `:66`, permissions, node
OOM — which is why this arm alone would be low; it rides on the same fix.

**Fix.** `set -o pipefail` beside `set -u`, then branch on the code: a status from the builder, or any
hook status other than 0 and 2, is a misconfiguration refusal that prints `$out` whole and exits 2;
only hook exit 2 WITH at least one `  L` line is a rule hit. Keep the full `$out` when the sed filter
yields nothing: `body=$(printf '%s' "$out" | sed -n '/^  L/,$p'); [ -n "$body" ] || body=$out`.

**Left-shift gate.** Two arms in the gate's own test: one running it with `AGENT_CAP` set, asserting
a misconfiguration refusal rather than a join report; one with an unreadable input, asserting a
refusal rather than a pass. The gate's own header preaches that a probe which cannot move must say
so, and it is currently the counterexample.

---

### D8 — medium — `tools/check-agent-cap-restatement.sh:36`

Three carriers say `TOOL-aDeclaredBound-6` was closed by deleting both disagreeing digits. Only one
digit was deleted.

**Evidence.** `git show f96738b7 -- tools/workflows/tier2-review.js` removed only the
`ONE <=6-wide wave` comment. `tools/workflows/tier2-review.js:7` still reads
`detail: '4 finder lenses, one wave, ≤5 concurrent'`, and `:5` spells `≤5` twice more. The in-code S11
comment at `:226–231` is honest and correctly scoped — "No digit is written HERE now" — but
`memory/backlog/TOOL.md:148` ("The fix writes NO digit at either site … so the two carriers cannot
disagree again"), `memory/builds/dTieredTribunal/README.md:59–60` ("deleted both disagreeing digits")
and this gate header all say otherwise, with the row marked CLOSED. The stated invariant does not
hold: changing `boundedParallel`'s default re-creates the drift, and this gate scans markdown only, so
nothing is watching.

**Fix.** Say what happened: the disagreeing `<=6` was deleted and the surviving `≤5` carriers now
agree with `boundedParallel`'s default, so the pair no longer contradicts. Correct all three carriers,
or delete the digit from `meta.phases[0].detail` and `meta.description` and let the claim stand as
written.

**Left-shift gate.** None available cheaply — this gate's own header records that widening its
population to source files took the false-positive rate to 64%. Route it into §10 as a documented
check instead: when a decision row claims a value was DELETED, the closing commit greps the named file
for that value. One line in the fold checklist, no new gate.

---

### D9 — medium — `memory/guides/BUILD-METHOD.md:118`

The amended M4 rule sends the reader to `tier2-review.js`'s `args` header for the spec-kind spelling,
and that header names neither `kind` nor `subjects`.

**Evidence.** The only `args` block in the file is the comment at `tools/workflows/tier2-review.js:27–31`,
listing `base, head, repo, context, byDesign, reviewDir` — no `kind`, no `subjects`, and unit 14's
`priorFindings`/`round` are missing too. The spelling lives at `:68–123`, outside that header. Unit 11
added the fields without extending the header it was about to be pointed at, and unit 12 declared any
change to `tier2-review.js` a non-goal, so nothing closed the loop. Spec-12 S8 pins the pointer to
`:27–32` deliberately, so the rule cannot go stale — aimed at a block that lacks the fact.

The consequence is the failure M4 exists to prevent: an omitted `kind` silently defaults to
`diff-review` (a mis-typed one refuses; an absent one does not), giving a code-shaped review of a
spec. A determined reader will still find `KINDS` forty lines below, so this is a stale pointer rather
than an unanswerable question — but the identical sentence is at
`tools/memory-tree/BUILD-METHOD.template.md:118`, so every adopter renders it too.

**Fix.** Extend the `args` header with `kind: "diff-review" | "spec-audit"` and
`subjects: [{ path, blob }]` (spec-audit only), and `round`/`priorFindings` while there.

**Left-shift gate.** The general form is cheap and worth having: a check that every field read off
`cfg`/`a` in `tier2-review.js` appears in that `args` comment block. It is a grep of destructured
names against the comment, it catches the next field somebody adds, and it makes the pointer M4 hands
the reader structurally true instead of true-when-written.

---

### D10 — low — `tools/hooks/agent-cap.js:255`

`markedWhy` is a cache that is never invalidated. A name refused on scan pass 1 and accepted on pass 2
keeps its pass-1 reason, and if the later bare-reassignment sweep removes the name from `ok`, the
refusal prints the stale — and false — pass-1 reason instead of naming the reassignment.

**Evidence.** Reproduced with a five-line fixture: `let LENSES = ALL.filter((L) => L.on) // gov:fixed-verifiers`
above `const ALL = [1,2,3]`, then `LENSES = args.custom`. `lines.forEach(scan)` runs twice (`:306–307`);
pass 1 refuses because `ALL` is not yet in `ok` and writes the reason, pass 2 accepts the same branch
via the early return at `:245–248` without clearing it, and the reassignment sweep at `:311–316`
deletes `LENSES` from `ok`. The fan-out line at `:384` falls back to `markedWhy.get(hit.name)` and
prints "the branch `ALL.filter((L) => L.on)` is not one of the bounded forms" — a branch pass 2
accepted. The verdict is correctly DENY, so this is diagnostic only; it is also the exact "operator
fixes it by guessing" failure the S4 comment at `:250–254` says the map was added to remove.

**Fix.** `markedWhy.delete(name)` beside `ok.add(name)` on the accept path, and have the reassignment
sweep set its own reason wherever it calls `ok.delete(m[1])`.

**Left-shift gate.** A self-test arm asserting the DENY message CONTAINS "REASSIGNED" for that
fixture. Message-text arms are cheap here — the file already asserts `why` strings elsewhere — and a
guard whose reason is wrong is a guard nobody can act on.

---

### D11 — low — `memory/gotchas/degradation-known-but-unreported.md:75`

The record's own anchor accounting is one short. It declares the taken set as the directory token
`tools/workflows/` plus three harness citations; the derived set has five members.

**Evidence.** Running the shipped module, `gotchas.records()` returns five anchors for this file: the
three `tools/workflows/*.js` citations, the directory token `tools/workflows/`, and
`memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-closing-diff.md`. The
fifth comes from the backticked path at line 32 in "Where it bit" and is live, not inert —
`selectable()` returns a tracked file for it, so a diff touching that build record selects this class.
The section that exists to state exactly which anchors were taken does not name it. The two width
figures do check out (1.15% taken, 19.83% for the refused bare `tools` token).

**Fix.** Either name the review-record anchor in the anchors section, or drop the backticks around
that path in "Where it bit", the way the section already de-backticks the refused `tools` token.

**Left-shift gate.** The hygiene gate already parses these records — have it compare the anchor count
a record's own accounting section declares against `records()`'s derived set and red on a mismatch. A
record whose stated anchors differ from its real ones is the same derived-vs-authored drift the gate
exists for, and this one is the first instance.

---

## What was refuted

Three of 24 did not survive the skeptic. They are not itemised here because none named a defect the
confirmed set does not already cover; the refutations were reachability arguments, not disagreements
about what the code does.

## Notes for the next round

Two things about this review's own shape, for the corpus audit §8 asks for.

Duplicate rate was 21 confirmed → 11 distinct, which is the highest this build has seen. Four lenses
over four files converges hard. On a diff this concentrated, coverage would have been better served by
priming one lens on `memory/` and the generated regions, which drew exactly one confirmed finding
between them.

Both blockers are guards that have never been observed RED, and both were introduced by this run.
That is not a coincidence and it is not a lens artefact: §7's "a gate you have only ever seen pass is
an assertion about nothing" is the rule this run broke twice, in a run whose subject is checks that
cannot fail.

# agent-cap — the fan-out guard, and the grammar it enforces

A `PreToolUse` hook that bounds review fan-out at the tool call, where the rule actually gets broken.
The charter (`§8`) states the two rules; this file states the GRAMMAR the hook recognises, because a
grammar is implementation detail of one hook and does not belong in a ruleset every session reads.

## The two rules

- **The verify-stage TOTAL is whatever `agent-cap.js` resolves.** Batching grows the batch, never
  the agent count.
- **Concurrency is a SECOND bound, its own constant in the same file.** How many run at once is not
  how many exist; they are two rules.

## Wiring

The matcher is the exact pair `Workflow|Agent`. `Workflow` alone leaves direct spawns unguarded,
which is the configuration this hook was rewritten to stop shipping.

**ONE COPY SHIPS, and the wired command names it.** Until `TOOL-dRetiredFork-14` this hook was
installed to `{prefix}/hooks/` AND `.claude/hooks/`, byte-identical, and the wired command named the
second. Two copies meant every policy value in the file was stated twice, and every carve-out over
it doubled before anyone edited anything.

`.claude/hooks/` had one property that made it attractive and that nobody wrote down: it is the same
path in every repo, so a wired command naming it was correct for every adopter with nothing to
resolve. Naming the kit directory gives that up, so the fragments declare their path with a `{kit}`
token and both consumers expand it **against the fragment's own location** — two directories up from
the `.fragment.json`. That is the rule on the writing side (`settings-merge.py`) and on the reading
side (`check-wiring.sh`), and it has to be the same rule or one of them wires a path the other
cannot find.

**Migrating an installed tree is two steps, and the order is not optional.** The wired command moves
to the surviving copy FIRST; the second copy is withdrawn SECOND. Reversed, the hook is unwired for
the window between — a security guard silently off, which is the one failure mode this whole change
had to avoid.

    python tools/settings-merge.py                 # repaths an already-wired command in place
    bash tools/check-wiring.sh --check             # says which copy is wired, every session

`settings-merge.py` repaths rather than no-ops: a command whose marker matches but whose path
differs is rewritten. It used to return unchanged in that case, which meant every already-wired tree
ignored the new path entirely.

Nothing deletes an adopter's second copy. `govkit update --write-withdrawals` does, on their timing,
and `check-wiring.sh` REPORTS a legacy copy rather than redding so that a half-migrated tree is told
rather than blocked.

**The fragment schema.** Five keys are required — `name`, `event`, `matcher`, `marker`,
`hook_path` — and two are optional, added by `TOOL-aReplayedCard-2`: `interpreter` (`node` or
`bash`, default `node`; a closed pair, because it is the first word of a command Claude Code runs)
and `args` (a list of tokens, default empty, rendered UNQUOTED after the quoted path and held to a
closed character class for that reason). A fragment carrying neither renders exactly as before. The
`hook_path` names its script through one of two tokens: `{kit}`, two directories up from the
fragment, for a kit that ships its directory; and `{here}`, the fragment's own directory, for a
`kind = "flat"` kit whose engine and fragments ship side by side at `{prefix}/`. Both readers and
the hook-destinations gate expand them identically, and the gate refuses when they do not. The
`marker` must be a substring of the rendered command under the merger's plain view AND under
`check-wiring.sh`'s whitespace-stripped view — space-free, therefore — and it may lead with a dash:
the card fragments use `--write` and `--replay` — and BOTH readers join on the marker AND the hook's
basename, so an adopter's own hook carrying `--write-log` is never taken for the card writer. A
SessionStart fragment ALWAYS declares a matcher from `startup|resume|clear|compact`; the merger
re-matches an entry it finds under the wrong one, and `check-wiring.sh`'s card arm reds on a CARD
entry under a matcher that is not its fragment's, because a SessionStart hook that never fires looks
exactly like one that is wired. The `check-wiring.sh --session` and process-monitor session entries
are NOT graded by any arm: their matchers are re-matched on apply and never read afterwards, so a
hand narrowing passes green (the aReplayedCard closing review, F12).

## What the hook DENIES, and how to satisfy it

- A raw `parallel(` / `pipeline(` primitive. Route through a bounded helper instead —
  `boundedParallel(thunks, 5)` or `boundedPipeline(items, 5, …)`, inlined, because workflow scripts
  cannot import. The line carries a `gov:bounded-fanout` marker.
- Any `agent(` fanned over a receiver the hook cannot PROVE bounded. The batching assignment carries
  a `gov:fixed-verifiers` marker, and EVERY top-level value branch of that assignment must qualify on
  its own — a marked line is admitted only when all of its branches do, never when the first one that
  matches does. A branch qualifies in one of three ways and no fourth: a bounded split, spelling
  `chunk(x, Math.ceil(x.length / K))` or `splitInto(x, K)` with a `K` the hook can resolve; an array
  LITERAL whose element count it can count here; or an identifier it has already proven bounded,
  alone or followed by operations that cannot grow it. A branch it cannot delimit never qualifies, so
  an expression the hook cannot read lands on the deny side rather than being waved through.
- An `agent(` inside a `for (const x of <identifier>)` body. This is the ONE loop shape the hook
  admits, and only under `gov:sequential-agents(<K>)` written as a line comment on the LOOP HEADER.
  It exists because a ratified `parallelism route: none` verdict forbids the bounded PARALLEL fan the
  hook permits, while the hook forbade the strictly sequential dispatch that verdict requires — a
  harness iterating a build's units sat in the gap and could not be written at all.
  EVERY clause below must hold and the refusal names the first that does not. The marker is read
  from the RAW header line, since both code views break their scan on `//`. It carries a bound token,
  and that token resolves through the same `<K>` definition every other consumer uses. The header
  matches a STRICT `for (const|let|var <name> of <identifier>)` in the literal-blanked view — read as
  a whole from the `for (` itself, never as the first `of <name>)` on the line, and a `while` is
  refused outright because it has no iteration source this scan can size. That identifier must
  already be in the hook's proven-bounded set, which is what makes the marker's number real rather
  than asserted. The call is directly preceded by `await`, and no `=>` or `function` sits between the
  header and it, because a deferred call is a thunk array.
  THREE MORE conditions bound the TOTAL rather than the shape, and each of them was a working bypass
  before it existed. A header line carrying more than one loop opener is refused, because this scan
  cannot tell which loop the call belongs to. The marked loop may have NO enclosing loop, marked or
  not — an outer loop multiplies the bound by a count nothing here can size, and it is never
  evaluated on its own because no `agent(` line is attributed to it. And a script may carry only ONE
  marked loop: the sweep bounds a single body and relates no two headers, so two honest markers
  multiplied or summed with every other clause satisfied.
  Finally, exactly ONE awaited call may resolve to any one header, counted per OCCURRENCE and not
  per line — five calls on one line contributed a single entry once, which turned the bound into a
  line count.
- The marked DERIVATION receiver, which is the third form above and was undocumented until now. A
  marked assignment may derive its receiver from something already proven bounded — a `.filter()` or
  a `.slice()`, which cannot grow an array — and the bound is inherited. Mentioning a bounded name is
  not enough: the whole right-hand side is still vetoed if it can grow, and the derivation must be
  ROOTED on the bounded value rather than merely referring to one. Accepted only WITH the marker —
  spelled `gov:fixed-verifiers`, on the assignment line — so it stays a deliberate claim rather than
  something inferred from a name. Every top-level branch of that right-hand side is judged on its own
  text, and the chain after a bounded root must CONSUME to a close: a tail this file cannot delimit
  is refused rather than assumed shrink-only.
- Any `K` it cannot resolve to an integer ≤5. It RESOLVES a bound wherever it is written — the call
  site, a helper's default parameter, or a `gov:bounded-fanout` slice width — and the burden is on
  the fan-out.

- A REF-KEYED VERDICT JOIN. A review harness that joins each finding to its skeptic verdict on a
  `file:line` STRING loses findings to echo drift, and COLLAPSES two findings at one location so both
  inherit whichever verdict landed last. The class has no runtime signal — a mis-keyed harness reports
  a clean bill. Three spellings are refused: an object or Map literal indexed by a `.ref` string,
  `.get`/`.set`/`.has`/`.delete` called on one, and the retired `verdictByRef` identifier in any
  position. Key the join on the integer id the orchestrator assigns before the skeptic sees the
  finding. This rule reads the literal-blanked view, so a mention inside a string is not a hit, and a
  REGEX literal is — which is why a gate holding the ban table excludes itself from its own
  population.
- An UNDECLARED SPEC AUDIT. A `Workflow` call whose structured `args` carry `kind: "spec-audit"` is
  denied unless the build README at `<args.repo>/<parent of args.reviewDir>/README.md` carries
  `spec-audit: <YYYY-MM-DD>` in its FRONT MATTER — the slice between the opening `---` and the next,
  the same scope `scratch-guard.js` reads `authorized-by:` in, through the one reader both hooks
  share. A body mention (a fenced example) is not front matter, and `spec-audit: yes` is a claim
  with no owner date behind it and reads as absent. The pre-code spec audit is OPT-IN by the owner's
  ruling (`TOOL-aBlindedTrial-6`), and this rule is what makes it FORBIDDEN in an attended session
  rather than merely not required; the remedy is the key, dated, on the build README. It reads
  `tool_input.args` ONLY — an object, or the JSON string the Workflow tool often delivers — and
  never the script text, which both shipped harnesses fill with the word. It fails CLOSED for this
  kind alone: a `repo` that is not a string, a `reviewDir` not directly under a `builds/<slug>/`
  folder or climbing through `..`, a `subjects[].path` under any OTHER build than the one `reviewDir`
  places (the declaration is read from where the record lands, so the subjects must sit under that
  same build), and a README it cannot read are each a deny naming the field or the path, and every
  throw inside it is returned as a deny because a hook that crashes at exit 1 admits. `kind` is
  compared as `String(kind)`, the callee's own derivation, so `["spec-audit"]` is a spec audit to
  both; on Windows `repo` is folded from MSYS drive spelling (`/c/…`) before it is resolved, and a
  repo under any other MSYS mount (`/tmp/…`) is not folded — it is denied by name, since Node cannot
  place it. A subject that is absolute or `~`-rooted is denied too: a direct spec-audit subject is
  repo-relative by the harness's contract, and a same-slug `builds/` folder in a second checkout is
  otherwise indistinguishable from this one. A PROJECT-WIDE DEFAULT (`TOOL-aBlindedTrial-7`): when
  the README is readable and carries NO key, the hook reads `SPEC_AUDIT_DEFAULT` from
  `<args.repo>/.unattended.conf` — the worktree copy, last assignment wins, both quote styles and a
  trailing `# comment` read as the shell would — and a date admits, a non-date denies by name, a
  missing file or a blank is no default. The README key wins whatever it says, so a malformed key
  never falls back to the default. TWO LIMITS, stated
  rather than implied. The `workflow()` a running harness calls from INSIDE its script is a runtime
  call and not a tool call, so the programmatic route is the unattended driver's to refuse
  (`TOOL-aBlindedTrial-3`); and this hook reads the WORKTREE README and conf while that driver reads
  both at BASE, so the two can disagree for exactly one uncommitted edit. An `args` string that does
  not parse shows the hook no `kind` and is admitted here; the harness itself throws on it, so no
  audit runs.

## Running ONE rule

`--only=<rule>` narrows the hook to a single rule, over a closed set whose only member today is
`join`. Anything outside the set is REFUSED with the set named, rather than silently matching
nothing. It exists so a file gate can share this predicate instead of re-implementing it.

**A WIRED command must never carry it.** `--only=join` in `.claude/settings.json` would turn the cap
rules off with no diff and a hook that still looks wired. `tools/check-wiring.sh` asserts its absence.

An array LITERAL of ≤5 elements — the finder-lens fan — is a RECEIVER the hook can size, which is
one of the three ways a receiver branch qualifies above; it needs no helper. It is not a blanket
exemption for the shape: a raw `parallel([...])` over five literal elements is still denied,
because the allowance is a property of what an `agent(` fan runs OVER and not of the literal.

## Direct spawns are COUNTED, not parsed

A direct `Agent` spawn carries no script for the hook to read, so it is counted instead: the
effective cap's worth per user prompt, claimed as atomic slots. That count is the only enforcement
reaching a fan-out made outside a workflow script, which is why the matcher must name both tools.

`AGENT_CAP` in the environment is REFUSED, not honoured — the ceiling is a file constant. A ready-made
harness that satisfies every rule above ships at `tools/workflows/tier2-review.js`.

## Lowering the cap — `.agent-cap.conf`

A repo that runs a LOWER fan-out cap than the hook's ceiling declares it once, in a tracked file at
its checkout root:

```sh
# .agent-cap.conf
FANOUT_CAP=4
```

The hook reads it on every `Workflow` and `Agent` call and enforces the smaller of that value and its
file constant everywhere it resolves a bound: the helper call site, the helper's default parameter,
the `gov:bounded-fanout` width, the verify-stage total and the direct-spawn slots. Every denial then
prints the effective cap and names the file that lowered it. The lens allowance does not move with it.

- **Lower only.** The value must be an integer from 1 up to the hook's `MAX_VERIFIERS`. Anything else,
  including a word, zero or a value above the ceiling, DENIES every call and names the file. An absent
  file or key means the ceiling. A value that can only lower the cap raises nothing, which is why a
  tracked file is admissible where the `AGENT_CAP` environment knob is not.
- **Grammar.** `FANOUT_CAP=4` or `FANOUT_CAP="4"`; the last such line wins, as a shell `.` reads it.
  A linked worktree reads its own checkout's file.
- **One key for both rules.** The charter's concurrency bound and its verify-stage total are two
  rules, and this one number lowers both (TOOL-aRepatriatedFork-7 F1; a second key is additive later).
- **The shipped harnesses follow it.** The review-harness kit renders `{{FANOUT_CAP}}` from this same
  file into `tier2-review.js`, `unattended-build.js` and both drift-audit workflows, so a repo that
  lowers the cap re-renders them rather than forking them: run
  `bash <kit>/check-protocol-parity.test.sh --render` in the same commit as the conf line, or the
  cap-ceiling renders are denied by the hook and the verifier fan-out leg reds.

**The two mechanisms are mutually exclusive, and the slot ledger must not be extended to `Workflow`.**
The script rules bound the fan-out inside one script; the slot ledger bounds the spawns made without
one. Neither wants the other's population. A harness that dispatches one `Workflow` call per unit of
a build issues a SEQUENCE of single-agent acts from one prompt, and a per-prompt slot budget written
for a BURST of verifiers would deny it partway through its own roster — a refusal with nothing fanned
out behind it. The slot budget is LIFETIME-PER-PROMPT, so it is the TOTAL and not the concurrency
bound, and a total is the wrong instrument for a dispatch sequence whose count is a function of the
roster size. Count what carries no script; parse what does.

## scratch-guard's second check: a `git commit` on an un-oriented card

`scratch-guard.js` is the other hook in this home, on the `Bash|PowerShell` matcher, and after its
scratch verdict it runs ONE more check, `checkOriented` (`TOOL-aReplayedCard-1`). A `git commit`
issued by the main loop is refused, exit 2, while the session's orientation card — the file the
kickoff kit's `manifest-check.sh --card --write` writes at session start under
`<git-common-dir>/orientation/<session_id>.md` — still holds the writer's sentinel `READY — none yet`,
or names a different tree than the commit targets. The deny names the card path, the condition and
the remedy: `/session-kickoff`, or `cd <target-tree> && /session-kickoff` when the trees differ,
because the kickoff's `--card --append` rewrites the card's `tree —` cell to the tree it runs in.

**The grammar.** The command's string-blanked view must hold the argv token `git`, then any number of
dash-prefixed tokens — `-C`, `-c`, `--git-dir`, `--work-tree`, `--namespace`, `--exec-path` and
`--config-env` each take the one value token after them unless written `--x=v`, and a quoted value
is one token — and then the whole token `commit` followed by whitespace or the end. So
`git -C "C:/p q" commit -m y` and `git -c a=b commit` match; `git merge-base`, `git commit-tree`,
`git log --grep commit`, a quoted `commit`, `merge` and `push` never do — the kickoff engine's own
Step 1 is a `git merge --ff-only`, and a deny on it would refuse its own remedy. The toplevel is the
`-C` target when there is one, else the payload `cwd`, both drive-folded through
`buildComparablePath` BEFORE the walk up to the directory holding `.git`, and the card's tree cell
is compared through the same fold — the writer prints `C:/…`, the harness hands `C:\…`, and the
nodes type `/c/…`.

**What ALLOWS, and what it prints.** A payload carrying `agent_id` (a subagent), or lacking
`session_id` or `cwd`, allows silently. An unwalkable target, an ABSENT card, and a card whose
header names `--card --replay` as its writer — one the replay wrote fresh for a session that started
before the writer was wired — allow with ONE witness line on stderr. That line departs from the
print-nothing protocol both hooks otherwise keep, and it reaches the debug log and the self-test
only: the harness discards stderr on exit 0, so nothing reaches the session. A present `--write` card
that passes prints nothing.

**The exemption.** The commit that CREATES a build's authorization: a `README.md` directly under a
`builds/<one>/` segment, NEW — staged as added, or untracked, which covers the single-call
`git add … && git commit` form whose index is empty at PreToolUse — whose bytes carry
`authorized-by:` with a value in the unattended driver's `SECOND_ANCHOR_MODES` (`prompt` or
`recipe`, pinned by a parity arm rather than restated). The staged BLOB is read for a staged file.
A folder already in HEAD exempts nothing, or every commit after a landed prompt-path build would be
exempt forever. This is the only step that spawns git, so the common path pays no spawn.

**The ceiling.** A commit made by a script, a heredoc or a non-git tool; a deleted, hand-written or
refused card; a `cd`/`-C` target that is not a literal path or does not exist (the last `cd <dir>`
before the git token IS read, and a target the shell would expand or that is absent from disk is a
witness rather than a walk into an ancestor's `.git`); a session that started before the wiring and
never restarted — all escape. The guard stops forgetting, not evasion. A READY line's PRESENCE is
asserted, never its correctness, and there is no waiver.

## The authoring rule for kit files

*Here because the charter template had no room for it: it sits within a few hundred bytes of its
gated ceiling and already past its recorded high-water, so adding a rule there would price it
against the ceiling rather than against its value. This README and the repo charter carry it.*

**A kit file names nothing outside itself by literal.**

- Its own kit directory and the tool root are DERIVED at run time. An empty derivation is a
  REFUSAL — never a fallback to a guessed prefix, which is the shape that makes a broken install
  look like a working one.
- A sibling kit is a token the render channel fills. So is anything a non-program document must
  SAY rather than execute. An unresolved token is a refusal, not an emitted brace.
- A replicated policy value is extracted or rendered from the one file that owns it. Retyping it
  creates two answers to one question, and the copy is always the one that rots.

**Why it is a rule and not a preference.** The deployer writes gov's bytes VERBATIM. A literal
naming a kit path therefore arrives unchanged in a target that installed at its own prefix, where
it resolves to nothing — silently, at the moment somebody needed it.

**How it is enforced.** The carried-prefix arm of the install-prefix gate. As of
`TOOL-dRetiredFork-17` it is a BAN rather than a shrink-only ratchet: its writer may lower a
count or drop a row that reached zero, and may NOT add one. That single change is the whole
conversion — before it, the remedy the gate printed was a self-service exemption form, and a new
literal could be absorbed by anyone who followed the gate's own advice.

A literal that is genuinely correct is justified BY HAND, as a reason column on its row in the
ban list, in the pass that wants it. Those reasons survive later writes. A definitional widening
of the predicate — which necessarily makes many literals newly visible at once — goes through a
separate re-baseline mode guarded by a declared predicate epoch, so it can be spent once per
change to the predicate and never to absorb a literal.

## scratch-guard — the write-target guard, and what it cannot see

The second hook in this home, wired on `Bash|PowerShell`, reads each tool call's TEXT for write
targets (redirects, `tee`/`touch`/`mkdir`, the last argument of `cp`/`mv`/`install`/`rsync`, and a
`TMPDIR=`/`TMP=`/`TEMP=` assignment) and denies one that lands where agent scratch does not belong.
Deny is stderr plus exit 2; allow prints nothing. The sanctioned roots are DERIVED, never authored:
`TMPDIR`, `TEMP` and `TMP` at run time, `<home>/.claude`, and the CLI's own scratch base
`<os.tmpdir()>/claude`. A target under one of those is allowed before any rule runs.

**The five rules**, each a `kind` the deny message names in its own sentence:

- `home` — a target under the operator's home directory that is not under a sanctioned root.
- `drive-root` — a target that creates a NEW top-level entry at a drive root, `C:/gvi`; the
  conventional names are `DRIVE_ROOT_CONVENTIONAL` in the hook.
- `empty-var` — a target opening with `$TMPDIR`, `${TMP}`, `$TEMP` (any of the three, braced or
  not) whose variable is empty or unset in the hook's environment, so the bytes land at the
  filesystem root. A non-empty variable is expanded and grading continues on the result; a
  `${TMPDIR:-default}` form expands to its default when the variable is empty; a variable the SAME
  command assigns (`TMP=$(mktemp -d); echo x > $TMP/f`) is not graded, because its value is
  unknowable textually.
- `tmp` — a target at or under `/tmp`, denied by owner ruling on 2026-09-14 even on a Git-Bash host
  where `/tmp` is a mount onto TEMP, because the habit is what is being ended. A temp variable
  whose value is exactly `/tmp` contributes NO allowed root, or `TEMP=/tmp` would re-open every
  write the rule closes; `/tmp/sub` as a value still does. `<os.tmpdir()>/claude` stays allowed
  INSIDE the prefix, so a POSIX host whose scratchpad sits under `/tmp` keeps its one destination.
- `posix-root` — a target that creates a new top-level entry at the POSIX root, `/mir/x`; the
  conventional names are `POSIX_ROOT_CONVENTIONAL`, with `tmp` and `temp` deliberately absent so
  the two rules cannot disagree about `/tmp`.

**What the predicate does NOT catch, because it is textual and stays so.** Four shapes walk past
it, and the upgrade path if they stop being rare is a real tokenizer rather than more regexes:

- Variable indirection beyond the three temp spellings and `~`/`$HOME`: `D=/tmp; echo x > $D/f`
  is graded as an unresolved token that misses every rule.
- A `cd`: `cd /tmp && echo x > y` writes a relative path the hook reads as repo-relative.
- A heredoc'd script: a Python `open('/tmp/x','w')` inside a `<<EOF` body is blanked before
  scanning, so nothing inside it is a target.
- A PowerShell variable spelling: `$env:TEMP\x` opens with `$env:`, which none of the three
  spellings match; the corpus measurement that motivated the rules was Bash-shaped, so this is
  stated rather than closed.

The suite is `scratch-guard.test.sh`. Its arms hand every environment override to the hook from
INSIDE node — a JavaScript prelude on `process.env`, the hook spawned as that node's child — because
on a Git-Bash host the MSYS runtime rewrites a POSIX-shaped `TEMP=/tmp` on its way to native
`node.exe`, and GNU `env` refuses `-u` after an assignment.

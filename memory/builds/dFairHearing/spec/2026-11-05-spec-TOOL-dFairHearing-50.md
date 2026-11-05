# TOOL-dFairHearing-50 — the reds of the close's first suite baseline

**Status:** INPROGRESS · rev-3 · 2026-11-05 · node d · Tier-2 · base bdd2e5f3 · streams tooling · order 33

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 TOOL-dFairHearing-43 TOOL-dFairHearing-44 TOOL-dFairHearing-45 TOOL-dFairHearing-46 TOOL-dFairHearing-47 TOOL-dFairHearing-48 |
| [2026-11-05-build-TOOL-dFairHearing-50-deviation-501.md](../build/2026-11-05-build-TOOL-dFairHearing-50-deviation-501.md) | deviation | — |
| [2026-11-05-build-TOOL-dFairHearing-50-deviation-502.md](../build/2026-11-05-build-TOOL-dFairHearing-50-deviation-502.md) | deviation | — |
| [2026-11-05-prompt-TOOL-dFairHearing-50-1-spec-writer.md](../prompts/2026-11-05-prompt-TOOL-dFairHearing-50-1-spec-writer.md) | journal | — |
| [2026-11-05-prompt-TOOL-dFairHearing-50-build-brief.md](../prompts/2026-11-05-prompt-TOOL-dFairHearing-50-build-brief.md) | research | — |
| [2026-11-05-prompt-TOOL-dFairHearing-50-spec-brief.md](../prompts/2026-11-05-prompt-TOOL-dFairHearing-50-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

No pass may run a suite, so the close's baseline at `948e4141b` was the first run of these arms, and
six of twelve suites read red. This unit repairs every red that baseline logged, so each named suite
exits 0 at the close. It also lands unit 48's two leftovers, and the three further reds the bar read
at `57b1cf127`.

## 2. Scope (IN)

Each scope id is its item's number, S1 to S11 from the brief and S13 to S16 from the main loop's
messages on the bar at `57b1cf127`. Line numbers are read at `bdd2e5f3`. The brief is
`2026-11-05-prompt-TOOL-dFairHearing-50-spec-brief`, and the Design section's table says where its
reading of a log held and where it did not. Item 12 holds traps and no work, so it takes no scope id:
it is answered under "Generated files", "Rollout" and "Files touched (estimate)".

- **S1** — Item 1. The field regex of the args-header arm stops reading a property named `a` as the
  args alias. Observed by AC1.
- **S2** — Item 2. A checklist return whose head lines state one item or more and which holds no `- `
  line is a `checklistError`, in `tools/workflows/tier2-review.template.js` and its render. A return
  stating none stays `no bug class selected`, which a new arm pins. `tools/workflows/README.md`
  says so. Observed by AC2.
- **S3** — Item 3. The `harness: the verifier count is bounded` needle spells `verifyOrder.length`.
  Observed by AC3.
- **S4** — Item 4. The `$E` and `$H4` fixtures hold their hook copy at the `.claude/hooks/` rung.
  `SELF_EXCLUDE` stays as it is. Observed by AC4.
- **S5** — Item 5. `tools/workflows/check-verifier-fanout.sh` hands `--slots` a spelling node can
  open. Observed by AC5.
- **S6** — Item 6. The empty-derivation arm's staging takes the third kit too. Observed by AC6.
- **S7** — Item 7. The two needles carry the `merged` key. Observed by AC7.
- **S8** — Item 8. The fan-out gate exits 2 when its rule could not run, and the writer-split arms
  stage what still reaches a hook. Observed by AC8.
- **S9** — Item 9. The renamed-kit fixture holds the rows and files a real install holds, and the
  `check-verifier-fanout.sh` count moves to 2. Observed by AC9.
- **S10** — Item 10. `measure_legs.py` joins `PARITY_EXEMPT`. Observed by AC10.
- **S11** — Item 11. The two docstrings of `tools/check-spec-tokens.py` state the true filter homes.
  No document lists the harness's stop exits, so no list gains `walk-red`. Observed by AC11.
- **S13** — Item 13. The site unit 48 added spells `printf -v`, so
  `tools/workflows/unattended-build.test.sh` measures its registered 66. Observed by AC13.
- **S14** — Item 14. `check_spec_audit_optin` in `tools/check-wiring.sh` spends no fork in a tree with
  no receipt, so the entrypoint measures its ceiling of 45. Observed by AC14.
- **S15** — Item 15. The forge arm of `tools/lib/resolve-python.test.sh` derives each kit segment.
  Observed by AC15.
- **S16** — Item 16. The five review rows of `tools/policy/catalogue.toml` name `dDeclaredLoop` as
  `owner`, and the two homes of the catalogue's owner rule state the exception. Observed by AC16.

## 3. Non-goals (OUT)

- No edit to `tools/run-gates/run-gates.sh`, because a run that edits the grader cannot land itself.
- No edit to `tools/gate-legs.json`. S10's list lives in the suite, so the manifest stays as it is.
- No edit to `memory/project/spawn-idiom-sites.txt` or `memory/project/fork-ceilings.txt`. S13 and S14
  bring the tree back to the rows, and neither row rises.
- No fork taken out of `check_scratch_guard`. See "The wiring forks (S14)".
- No edit to `memory/builds/dFairHearing/BACKLOG.md`. Its dead cite is the main loop's records fix, and
  S16's ask is the main loop's too.
- No policy-file reader for any review key. Specs 11 and 18 leave that to dDeclaredLoop, and
  `TOOL-dDeclaredLoop-20` S2 owns the two it names.
- No edit to any dDeclaredLoop spec. S16 hands that gap off.
- No new catalogue field, and no exemption in `arm_reader_coverage`.
- No edit to `tools/workflows/REVIEW-PROTOCOL.template.md`, to `tools/lib/render-doc.sh` or to any
  marked inline block. S9's finding is that the render and the template are right.
- No wholeness check for the build harness's own resolver at
  `tools/workflows/unattended-build.template.js:1539`. It takes a `--for-paths` return, it never had
  one, and no log line asks for it.
- No wording change to the writer-split notice at `tools/workflows/check-protocol-parity.test.sh:733`.
- No bullet for `walk-red` in `memory/guides/UNATTENDED-VERBS.md`. Its return carries `next`, and the
  brief's condition, a document that lists the exits, does not hold.
- No hand count of a floor. The close confirms each from a real run.

### Edges

- **hands-off** external — `TOOL-dDeclaredLoop-20` S2 reads `review.opt-in` and `review.unclassed` and
  must also take a reader for `review.twin` and the two `review.design-audit.*` keys, or the reader-coverage
  arm reds them when dDeclaredLoop lands

## 4. Design

### Tier

Tier-2, past the brief's Tier-1 default, for two reasons.

- S8 changes the exit contract of a merge-bar gate that a second file reads:
  `tools/workflows/check-protocol-parity.test.sh:724` branches on it. That is a shared contract.
- S2 changes which reason a review's RUN INTEGRITY line carries for a cut return.

S5 stays mechanical, and S9 turned out to be fixture work with no product change.

### What the brief read, against the tree

| Item | Held | Correction |
|---|---|---|
| 1 | yes | The arm's own label moves to `all 30 fields`, because the count is computed. |
| 1, 2 | no | The log's third tier2-review red, `executed 636 assertions against a floor of 638`, is no separate red. `executed` is the `passed` count (`tools/workflows/tier2-review.test.sh:3988`), and that run read 636 passed and 2 failed. |
| 2 | yes | The test is the head lines' whole `n + u + k`, not the classes alone, so an invariant count cannot slip past it. |
| 3, 4, 6, 7 | yes | None. S7's real output is the probe's, below. |
| 5 | yes | The whole-tree run is relative, so the bar's own leg never met this red. |
| 8 | no | The brief offers the arms, the notice or the gate. The arms and the gate are wrong, and the notice is right. See S8. |
| 9 | no | It is no real gap. The render misses nothing a real install holds. See S9. |
| 10 | yes | Two parity arms redded, not one, and the same list clears both. The second is `parity: graded 55 + exempt 14 != the manifest's 70 selftests legs`. |
| 11 | no | No document lists the stop exits. See S11. |
| 13 | yes | The scanner confirms unit 48's arm as the source. |
| 14 | yes | All four forks are one arm's, and a builtin does the work of each, so the ceiling stands. |
| 15 | yes | A fixture directory name cannot serve, because these segments are the kit homes. |
| 16 | partly | The move stands, but three keys have no planned reader, unit 18 is the design-audit keys' carrier, and the arm already redded at `57b1cf127`, before any close. See S16. |

### The args-header regex (S1)

`tools/workflows/tier2-review.test.sh:451` reads `\ba\.`, and `\b` holds after a dot, so
`twinFigures.a.length` at `tools/workflows/tier2-review.js:3235` reads as a field. The regex takes a
lookbehind:

```js
const fields = [...new Set([...src.slice(alias).matchAll(/(?<![\w$.])a\.([A-Za-z_$][\w$]*)/g)].map((m) => m[1]))].sort()
```

Run in node at `bdd2e5f3`, the old regex finds 31 fields and misses `length`, and this one finds 30
and misses none, PINNED. No other suite carries this regex.

The probe, saved to `$TEMP/fh50args.js`:

```js
const fs = require('fs')
const m = /^const fields = .*matchAll\((\/.*\/g)\)\]/m.exec(fs.readFileSync('tools/workflows/tier2-review.test.sh', 'utf8'))
const src = fs.readFileSync('tools/workflows/tier2-review.js', 'utf8')
const fields = new Set([...src.slice(src.indexOf('\nconst a = cfg')).matchAll(eval(m[1]))].map((x) => x[1]))
console.log(fields.size + ' field(s), length ' + (fields.has('length') ? 'read' : 'not read'))
```

### The cut with no item left (S2)

`tools/workflows/tier2-review.template.js:1454` computes `cut` only when a `- ` line exists, so a
return cut above its first item falls through to `no bug class selected` at :1458. The stated count
leaves `checkChecklistWhole` for a pure helper of its own, because the acquisition now reads it too:

```js
// TOOL-dFairHearing-50 S2 - the item count the head lines state, n + u + k, or null with no selection line.
function deriveStatedItems(text) {
  const sel = /^# (\d+) class\(es\) selected by an anchor \+ (\d+) universal/m.exec(text)
  if (!sel) return null
  const inv = /^# invariants are read at \S+; (\d+) that /m.exec(text)
  return Number(sel[1]) + Number(sel[2]) + (inv ? Number(inv[1]) : 0)
}
```

`checkChecklistWhole` calls it over `before`, and returns its no-selection-line refusal on `null`.
The acquisition reads:

```js
  const said = res && typeof res.checklist === 'string' ? res.checklist : ''
  const cut = /^- /m.test(said) || deriveStatedItems(said) > 0 ? checkChecklistWhole(said) : ''
```

Lines :1455 to :1459 stay as they are, and the comment above :1454 names this unit. The three cases:

| Return | Stated | Reason logged |
|---|---|---|
| head lines stating 1, no item, no by-design head | 1 | `checklistError: the returned checklist is cut — it carries no` the by-design head |
| head lines stating 0, by-design head, no item | 0 | `no bug class selected` |
| a header with no selection line | null | `no bug class selected`, the arm at `tools/workflows/tier2-review.test.sh:1434` |

The new arm follows the `FH15 AC3` loop. It hands the second row's return to the checklist agent and
requires a warning opening `WARNING: no checklist was acquired — no bug class selected`. Its label
opens `FH50 AC2`. Without it a fix reading any head line as a cut stays green, because the fixture at
:1434 holds no selection line.

`tools/workflows/README.md:282` gains, after `never passes as complete.`, with the phrase
`state one item or more` on one line: "A return whose head lines state one item or more and which
holds no `- ` line is cut the same way, and one stating none stays `no bug class selected`."

The render is `[[files]]`-declared, so the pass runs the parity script's `--render` mode and declares
both files. What this does not check: that the head lines themselves are true. A return that lost
those lines as well reads as a genuine zero, as it does today.

The probe, saved to `$TEMP/fh50cut.js`:

```js
const src = require('fs').readFileSync('tools/workflows/tier2-review.js', 'utf8')
const a = src.indexOf('function deriveStatedItems')
if (a === -1) { console.log('no deriveStatedItems'); process.exit(0) }
const { deriveStatedItems, checkChecklistWhole } = new Function(src.slice(a, src.indexOf("phase('Resume')", a)) + '\nreturn { deriveStatedItems, checkChecklistWhole }')()
const head = (n) => '# recurring-bug-class checklist for b..c (1 file(s))\n# ' + n + ' class(es) selected by an anchor + 0 universal\n'
console.log('stated one ' + deriveStatedItems(head(1)) + ' — ' + checkChecklistWhole(head(1)))
console.log('stated none ' + deriveStatedItems(head(0)))
console.log('no head ' + deriveStatedItems('# recurring-bug-class checklist for b..c (0 file(s))\n'))
```

### The two review-join fixtures (S3, S4)

`tools/workflows/check-review-join.test.sh:386` greps the name the harness no longer spells. The
needle becomes `Math.ceil(verifyOrder.length / MAX_VERIFIERS)`, which
`tools/workflows/tier2-review.template.js:2071` carries.

The gate resolves its hook before it reads its population, so each fixture still needs one
(`tools/workflows/check-review-join.sh:303-304`). The `.claude/hooks/` rung sits outside `POP_RE`
(:71-73), and neither fixture's probes find a kit once the copy moves, so that rung answers.

- `tools/workflows/check-review-join.test.sh:442` becomes
  `mkdir -p "$E/.claude/hooks" && cp "$ROOT/${HOOKS_DIR}/agent-cap.js" "$E/.claude/hooks/agent-cap.js"`.
  The comment above it says why the copy sits there.
- :476 copies to `"$H4/.claude/hooks/agent-cap.js"`, and :474 no longer makes `"$H4/scripts/$HKK"`.
  `HKK` at :473 then has no reader and goes.

The `.claude/hooks/ban-table.js` arm at :483 is unaffected, because that path stays outside the
population. An empty prefix would put the hook back in it, and no run of this suite has one:
`tools/run-gates/foreign-prefix.gov.test.sh:83` refuses a root install.

### The slot spelling (S5)

MSYS converts an absolute path only when it is a whole argument. Measured on this host at
`bdd2e5f3`: `/tmp/x/a.txt` reached node as `C:/Users/.../a.txt`, `/tmp/x/a.txt:12` reached it
unconverted, and `rel/a.js:3` unchanged. `tools/workflows/check-verifier-fanout.sh:360` builds the
second form, so node reads ENOENT and :367 exits 2. `check-verifier-fanout.js` splits on the last
colon (`tools/workflows/check-verifier-fanout.js:835`), so a drive colon is safe.

The loop at :357-361 gains one line above the `for`, and the `for` reads `_nf`:

```bash
  # MSYS converts an absolute path only as a whole argument, so `<path>:<line>` reached node unconverted
  # and unreadable. `cygpath -m` spells it for node; a relative path needs no spawn, and where cygpath
  # is absent the path is already native (TOOL-dFairHearing-50 S5).
  case "$f" in /*) _nf=$(cygpath -m "$f" 2>/dev/null) || _nf=$f ;; *) _nf=$f ;; esac
  for _l in ${_ml//$'\r'/}; do locs+=("$_nf:$_l"); done
```

**A Linux run sees the spelling it sees today.** `cygpath` is absent, the substitution fails, and
`_nf` is `$f`, so node gets `/abs/x.js:12`. An MSYS relative path takes the second arm and spawns
nothing, and the whole-tree mode's population is `git ls-files` output, so the bar's leg spawns
nothing new. A `C:/x.js` argument takes the second arm too and passes through. The idiom is the one
at `tools/unattended/stop-guard.test.sh:265`.

The arms read the verdict text and not the path, so no arm moves.

The probe, saved to `$TEMP/fh50slots`. It evaluates the gate's own new line and asks node for the
path, and runs no gate. On Linux it reads green at the base too, so only MSYS observes this.

```bash
t=$(mktemp -d) || exit 2; trap 'rm -rf "$t"' EXIT
f=$t/five.js; _nf=$f; printf 'x\n' > "$f"
eval "$(grep -E '^  case "\$f" in /' tools/workflows/check-verifier-fanout.sh)"
node -e 'const l = process.argv[1]; console.log(require("fs").existsSync(l.slice(0, l.lastIndexOf(":"))) ? "node opens it" : "node cannot open it")' "$_nf:1"
```

### The third kit (S6)

`arm` runs `git add -A` after its staging (`tools/check-playbook-parity.test.sh:344`), so the planted
workflows kit, which the fixture's registry declares at :291, is tracked again and the derivation
returns it. The staging at :492 adds `'"${PFX}${WF}"'` to its `rm -rf`. The gate then reaches its
empty-set refusal at `tools/check-playbook-parity.sh:318`.

### The merged key (S7)

The return orders `refuted`, `merged`, `unverified` (`tools/workflows/tier2-review.template.js:3160-3162`).
The real output, read through the suite's own runner and doubles at `bdd2e5f3`, PINNED:

```text
"raw":48,"confirmed":0,"refuted":0,"merged":0,"unverified":48
"raw":46,"confirmed":16,"refuted":30,"merged":0,"unverified":0
```

`tools/workflows/unattended-build.test.sh:1098` takes the needle
`'"confirmed":0,"refuted":0,"merged":0,"unverified":48'`, and :1120 takes
`'"raw":46,"confirmed":16,"refuted":30,"merged":0,"unverified":0'`.

The probe, saved to `$TEMP/fh50merged`. It extracts the runner and the doubles and runs no arm:

```bash
T=tools/workflows/unattended-build.test.sh; s=$(mktemp) || exit 2; trap 'rm -f "$s"' EXIT
{ echo 'HERE=tools/workflows; F=tools/workflows/unattended-build.js'
  sed -n '/^run_wf() {/,/^}$/p;/^build_merged_returns() {/,/^}$/p;/^MT_T2=/p;/^MT_ARGS=/p;/^MT20_SHAPE=/p;/^MT20_MERGED=/p;/^run_merged_review() {/p' "$T"
  echo 'run_merged_review "$(build_merged_returns "[]" 0)" | grep -o "\"raw\":[^}]*\"unverified\":[0-9]*" | head -1'
  echo 'run_merged_review "$(build_merged_returns "$MT20_MERGED" 46 "$MT20_SHAPE")" | grep -o "\"raw\":[^}]*\"unverified\":[0-9]*" | head -1'
} > "$s"; bash "$s"
```

### The writer split (S8)

**The question no longer reaches a stub hook.** The hook is asked through its exports. `loadHook`
`require`s it (`tools/workflows/check-verifier-fanout.js:37`) and reads seven names, and the writer
bound is the one thing a hook can answer, through `readWriterBound` (:794). A stub that speaks the
retired stdin protocol exports none of them, so `main` refuses at :830 with exit 2 before any rule
runs, and the stub's `end` handler never fires.

**The arms are wrong.** The `sed` at `tools/workflows/unattended-build.test.sh:2301` stages a constant
the hook no longer holds, and the stubs at :2312 and :2321 stage a protocol it no longer speaks.

**The gate is wrong too.** `tools/workflows/check-verifier-fanout.sh:328` reads every non-zero as
`FAILED` and exits 1, so the rule's refusal reaches `tools/workflows/check-protocol-parity.test.sh:728`
as a denial. The notice then reports `check-verifier-fanout: cannot load agent-cap's exports` as the
hook's reason for refusing a split it was never asked about. The parity script's comment at :711-713
says the reverse: an exit other than 0 or 1 is no verdict. The gate's own slot call already holds that
line at :367. The gate's header at :11, which calls a refusal exit 1, is the sentence that moves.

**The notice is right.** A real denial still reaches it, and `Update it` is still the remedy.

The body at :328-332 becomes:

```bash
  out=$(node "$FANJS" --hook "$HOOK" "$f" 2>&1); _fr=$?
  case "$_fr" in
    0) ;;
    1)
      echo "verifier-fanout: FAILED — $f"
      printf '%s\n' "$out" | sed 's/^/    /'
      st=1 ;;
    *) echo "verifier-fanout: the rule could not run on $f — $out"; exit 2 ;;
  esac
```

The `printf` keeps a line of its own, so the file's `var-pipe` count stays 1. That count and S5's line
leave the file's registry rows as they are, read through the scanner's function over a scratch patch
at `bdd2e5f3`.

Line :11 and the sentence ending :320 read:

```text
# Exit 0 = clean · 1 = the rule is broken · 2 = misconfigured, or its check refused a harness.
Its exit 1 is a finding, and its 2 a refusal that ends this gate at exit 2, as the slot count's does
below (TOOL-dFairHearing-50 S8).
```

The comment at `tools/workflows/check-protocol-parity.test.sh:705-708` states a hook rule that left
in NT-27, so it is corrected in place. Its first sentences read: `unattended-build.js` bounds its
spec-writer split under `// gov:fixed-writers`, and the fan-out rule reads that bound through the
hook's `readWriterBound`, so a hook answering below the rendered width, or refusing, denies the
split. The clause at :713 reads `for want of the hook, a hook the rule can load, node or a checkout`.

**The arms**, in `tools/workflows/unattended-build.test.sh`, each staged at the hook's real bound:

| Line | Today | Becomes |
|---|---|---|
| :2294-2299 | says the old hook is staged by its marker | says the hook is staged at its bound, and why no stub can be |
| :2301 | `sed` over `WRITER_MARK` | the `readWriterBound` stage below |
| :2302 | `DGR74 LIVENESS the layout's hook no longer carries the writer marker` | `DGR74 LIVENESS the layout's hook refuses the writer bound`, grepping the stage's text |
| :2304 | `DGR74 a hook that predates the writer marker: --render still renders` | `DGR74 a hook that refuses the writer bound: --render still renders` |
| :2312 | stub printing a reason | the `MAX_VERIFIERS` stage below, with its own `DGR74 LIVENESS the layout's hook holds a total below the fallback's` |
| :2316 | needle naming the stub | `does not admit the writer split: BLOCKED by agent-cap: a verify/fan-out stage spawns one agent per item. The review protocol caps verify-stage agents at 4 TOTAL` |
| :2321 | stub reading stdin | `printf '%s\n' "process.exit(1)"`, the one hook that still ends in a silent exit 1 |

```bash
sed -i "s/^function readWriterBound(repo) {\$/function readWriterBound(repo) { return { why: 'a staged hook that bounds no writer split' }/" "$WS/scripts/$HOOKS/agent-cap.js"
sed -i 's/^const MAX_VERIFIERS = 5$/const MAX_VERIFIERS = 4/' "$WS/scripts/$HOOKS/agent-cap.js"
```

Every other `DGR74` and `DGR83` arm keeps its needle. Measured at `bdd2e5f3` through the rule's
exports over the real render and the fallback's spans: the first stage denies the split and admits
the fallback, and with the second the fallback is denied too.

**The new arms** sit before the no-hook arms, and each label opens `FH50 AC8`:

```bash
printf '%s\n' "module.exports = {}" > "$WS/scripts/$HOOKS/agent-cap.js"
o=$( (cd "$WS" && bash scripts/$WFK/check-protocol-parity.test.sh --render 2>"$LAY/old-hook.err"; echo "rc=$?") ); e=$(<"$LAY/old-hook.err")
has "FH50 AC8 a hook the rule cannot load: --render refuses" "$o" "rc=2"
has "FH50 AC8 ...naming the gate that could not ask the hook" "$e" "the fan-out gate exited 2 and could not ask the agent-cap hook"
has "FH50 AC8 ...and the rule's own reason" "$e" "it exports no MAX_VERIFIERS"
hasnt_ "FH50 AC8 ...never as the hook's denial" "$e" "does not admit the writer split"
```

Read at `bdd2e5f3`, no fixture depends on a refusal exiting 1: the two `FAILED` arms of
`tools/workflows/check-verifier-fanout.test.sh` (:275, :539) are real findings, and the only hook
stubs that reach this gate are the two above. The one consumer of the value is the parity script, and
the leg reads any non-zero as red.

What this leaves standing: the second ask at `tools/workflows/check-protocol-parity.test.sh:736` still
calls any non-zero a denial. It runs only after the first ask answered 1, against the same hook.

Two probes, each saved to the name it carries. `$TEMP/fh50bound` reads the suite's own two stages and
asks the rule through its exports. `$TEMP/fh50gate` sources the gate's own new block for each node
exit, then loads a stub through `loadHook`. Neither runs a gate.

```bash
T=tools/workflows/unattended-build.test.sh
t=$(mktemp -d) || exit 2; trap 'rm -rf "$t"' EXIT
cp tools/hooks/agent-cap.js "$t/agent-cap.js"
sed 's/^const SPEC_WRITERS = .*/const SPEC_WRITERS = 5/; s/\(SPEC_WRITERS)) \/\/ gov:fixed-\)writers/\1verifiers/' tools/workflows/unattended-build.js > "$t/fallback.js"
stage() { eval "$(grep -E "^sed -i .*$1" "$T" | sed 's#"$WS/scripts/$HOOKS/agent-cap.js"#"$t/agent-cap.js"#')"; }
ask() { node -e 'const m = require(require("path").resolve("tools/workflows/check-verifier-fanout.js")); m.loadHook(process.argv[1])
console.log(process.argv[3] + " findings " + m.scanFanout(require("fs").readFileSync(process.argv[2], "utf8")).length)' "$t/agent-cap.js" "$1" "$2"; }
stage readWriterBound; ask tools/workflows/unattended-build.js 'bound: split'; ask "$t/fallback.js" 'bound: fallback'
stage 'const MAX_VERIFIERS'; ask "$t/fallback.js" 'total: fallback'
```

```bash
t=$(mktemp) || exit 2; trap 'rm -f "$t"' EXIT
sed -n '/^  case "\$_fr" in$/,/^  esac$/p' tools/workflows/check-verifier-fanout.sh > "$t"
for _fr in 0 1 2; do ( f=x.js; out=why; st=0; . "$t"; echo "exit $_fr: carries on, st=$st" ); echo "exit $_fr: subshell $?"; done
printf 'module.exports = {}\n' > "$t"
node -e 'try { require(require("path").resolve("tools/workflows/check-verifier-fanout.js")).loadHook(process.argv[1]) } catch (e) { console.log("load refused: " + e.message.slice(0, 28)) }' "$t"
```

### The renamed kit (S9)

**It is no real gap.** `derive_kit_paths` resolves each citation through `resolve_kit_dir`, whose
receipt rung needs a row and the file (`tools/lib/render-doc.sh:125-134`). The fixture's receipt
carries four rows, and `tools/workflows/kit.toml:13-15` installs every kit file under `**`, so a real
install rows them all. The six lines the arm counts are the citations the fixture holds no row for:

| Template line | Citation | Row | File in the layout |
|---|---|---|---|
| :41, :204 | `check-verifier-fanout.js` | absent | present |
| :46 | `check-review-join.js` | absent | absent |
| :47 | `check-review-join.sh` | absent | absent |
| :48 | `spec-audit-optin.js` | absent | absent |
| :161 | `lenses.toml` | absent | present |

A fixture holding those rows and files reads 0 through the real `derive_kit_paths` and
`render_kit_cites`. Measured at `bdd2e5f3` in scratch: 6 with four rows, 0 with nine, PINNED.

**The first count is a legitimate cite.** Unit 10 rewrote that section, so the protocol now cites
`check-verifier-fanout.sh` at :43 and :172, where the arm was written against one line. The arm's
number moves to 2 and its label to `RA6-1 ...and its check-verifier-fanout.sh twice`.

In `build_renamed` (`tools/workflows/unattended-build.test.sh:2564`):

```bash
    cp "$HERE/check-review-join.sh" "$HERE/check-review-join.js" "$HERE/spec-audit-optin.js" "$1/scripts/rh/"
```

That line sits above its `rm -f`. The receipt's `printf` gains five `engine` rows of the shape its
last row has, for `check-verifier-fanout.js`, `check-review-join.sh`, `check-review-join.js`,
`spec-audit-optin.js` and `lenses.toml`, and its argument list reaches nine `"$WFK"`. The comments at
:2556 and :2564 say nine rows. `RA7-3` writes its own receipt, so it is unaffected.

What this does not check: a citation with no row and no probe answer still falls through to the tool
root plus gov's home, silently, by design (`tools/lib/render-doc.sh:101`). A kit whose receipt lost a
row renders a dead path and no gate says so. The arm now covers each citation the template carries
today, and a new citation with no row reds it again, which is how this red arose.

The probe, saved to `$TEMP/fh50cites`. It reads the suite's own `build_renamed`, over a stub
`build_layout`. Run at `bdd2e5f3` it printed `old home 6` and `fanout gate 2`.

```bash
root=$(pwd); t=$(mktemp -d) || exit 2; trap 'rm -rf "$t"' EXIT
HERE=$root/tools/workflows; WFK=workflows; UNK=unattended
build_layout() { mkdir -p "$1/scripts/rh" "$1/scripts/hooks" "$1/memory/guides"; git -C "$1" init -q
  cp "$HERE/REVIEW-PROTOCOL.template.md" "$HERE/lenses.toml" "$HERE/check-verifier-fanout.sh" "$HERE/check-verifier-fanout.js" "$HERE/tier2-review.js" "$HERE/unattended-unit.js" "$1/scripts/rh/"
  cp "$root/tools/hooks/agent-cap.js" "$1/scripts/hooks/"; }
eval "$(sed -n '/^  build_renamed() {/,/^  }/p' "$HERE/unattended-build.test.sh")"
. "$root/tools/lib/render-doc.sh"
build_renamed "$t/r"; cp "$HERE/tier2-review.js" "$t/r/scripts/rh/"; cd "$t/r" || exit 2
KIT_PATHS=$(derive_kit_paths "$(command -v python)" scripts/rh scripts/rh/REVIEW-PROTOCOL.template.md) || exit 2
out=$(cat scripts/rh/REVIEW-PROTOCOL.template.md); render_kit_cites; out=${out//\{\{TOOL_ROOT\}\}/scripts/}
printf 'old home %s\n' "$(grep -cF "scripts/$WFK/" <<<"$out")"
printf 'fanout gate %s\n' "$(grep -cF 'scripts/rh/check-verifier-fanout.sh' <<<"$out")"
```

### The exempt list (S10)

`tools/check-spec-tokens.test.sh:1019` gains `measure_legs.py`, and the comment at :1014-1016 gains it
beside its siblings: `measure_legs.py --selftest (ceiling 500 s)`. The ceiling stood at `8bec4cefd`
already, read from that commit, so this red is inherited. The loop's exempt branch precedes its bound
test, so one word clears both parity arms: 55 graded plus 15 exempt is the manifest's 70.

The probe, saved to `$TEMP/fh50exempt.py`:

```python
import json, re
t = open("tools/check-spec-tokens.test.sh", encoding="utf-8").read()
exempt = set(re.search(r'^PARITY_EXEMPT="([^"]*)"', t, re.M).group(1).split())
bound = int(re.search(r"^DIRECT_CHECK_BOUND=(\d+)", t, re.M).group(1))
legs = [l for l in json.load(open("tools/gate-legs.json", encoding="utf-8")) if l.get("chunk") == "selftests"]
name = lambda l: next((a.rsplit("/", 1)[-1] for a in l["argv"] if "/" in a), "")
over = [l["name"] for l in legs if "--selftest" in l["argv"] and l.get("ceiling", 0) > bound and name(l) not in exempt]
print("undeclared", len(over), over)
print("stale", sorted(exempt - {name(l) for l in legs}))
```

### Unit 48's leftovers (S11)

The WONTDO filter has two homes. `read_carries_specs` filters through the generator's grammar
(`tools/check-spec-tokens.py:964`), and `main` builds `unretired` with `WONTDO_STATUS` (:1551) for the
arm-labels join. So a spec whose header the grammar refuses is set apart by the carries join, under
`unparsed`, and stays graded by the arm-labels join.

`tools/check-spec-tokens.py:936` opens instead:

```text
THE CARRIES JOIN'S WONTDO FILTER (TOOL-dTrueNorth-16 S9), one of two: `main` sets a WONTDO spec apart
for the arm-labels join with `WONTDO_STATUS`, a header regex, so a header the grammar below refuses
is graded there and set apart here. Each status is the generator's
```

The docstring's next words carry on from `parse_spec_text`. At :995 the clause reads
`` `read_carries_specs` is this join's WONTDO filter, so a superseded unit's binding lines never ``.

**The stop exits.** None of the four documents lists them. `grep` for an `exit:` value finds
`deferred-platform` alone:

| Document | What it holds |
|---|---|
| `memory/guides/UNATTENDED-VERBS.md:807` | one procedure for that one exit, which needs a re-run |
| `memory/guides/UNATTENDED-STOPS.md:142` | a `hold-run` field row naming that exit |
| `memory/guides/REVIEW-PROTOCOL.md:189` | the review harness's own exit |
| `tools/workflows/README.md:593`, :786 | the review harness's return fields |

The build harness's two `exit` values are `deferred-platform` and `walk-red`
(`tools/workflows/unattended-build.template.js:1827`, :1862). A `walk-red` return carries its own
`next`, and `roster: []` stops the caller. So nothing moves in any of the four.

### The printf site (S13)

The registry row is right and the tree moved. `tools/workflows/unattended-build.test.sh:593` is unit
48's walk-red arm, confirmed by the scanner's own function: 66 sites at `af1d9fa91~1`, 67 at
`af1d9fa91`, and the one new site is this line, PINNED. The leg's pathspec excludes suites from its
product population, and the registry classes still count every tracked `*.test.sh`
(`memory/project/spawn-idiom-sites.txt:12-13`).

The line's two-line command takes a variable:

```bash
rec CONVERGED >/dev/null; printf -v wr_ret '{"spec-write":%s,"workflow":{"blockers":null,"confirmed":2,"highs":null,"unverified":0,"report":"r.md","walkGaps":["x"]},"record":%s,"dispose":%s}' \
    "$SPEC_OK" "$_rec" "$DISPOSE_OK"; o=$(run_wf "$UNITS" "$wr_ret")
```

`memory/project/spawn-idiom-sites.txt:318` stays at 66. S7, S8 and S9 add no site to this file.

The probe, saved to `$TEMP/fh50sites.py`. It calls the scanner's function and runs no leg:

```python
import importlib.util, sys
spec = importlib.util.spec_from_file_location("sh_hygiene", "tools/gate-lint/sh_hygiene.py")
m = importlib.util.module_from_spec(spec); sys.modules["sh_hygiene"] = m; spec.loader.exec_module(m)
text = open("tools/workflows/unattended-build.test.sh", encoding="utf-8", errors="replace").read()
print("printf-subst", sum(1 for site in m.scan_spawn_file(text)["printf-subst"] if site[1]))
```

### The wiring forks (S14)

**How the ceiling is declared.** It is the third field of the `check-wiring` row at
`memory/project/fork-ceilings.txt:21`, which `tools/gate-lint/fork-count.sh` reads as its first
argument. A change to it touches no line of `tools/run-gates/run-gates.sh`. This unit does not change
it, because no fork here is needed.

**Where the four forks are.** The row's fixture is an empty repository. Unit 16 added
`check_spec_audit_optin` (`tools/check-wiring.sh:1103`), and every other line of this build's diff to
that file spends nothing there. On that fixture the arm spends exactly four:

| Fork | Site | What it buys there |
|---|---|---|
| 1 | `$(resolve_receipt_path ...)` | nothing: the function returns at once with no receipt (:346) |
| 2 | `$(resolve_kit_file ...)` | a table lookup in plain bash (:686-691) |
| 3 | `miss=$(derive_receipt_miss ...)` | nothing with no receipt |
| 4 | the `p=$(resolve_receipt_path ...)` inside it (:362) | nothing with no receipt |

**The fix.** `resolve_kit_file` also leaves its answer in `_kit_file`, the idiom `first_of` carries at
:325, so a caller running it with `>/dev/null` in this shell spends no fork. Its existing callers keep
their substitution and their output.

- :677 reads `local d i=0; _kit_file=""`.
- The print at :682 becomes `{ _kit_file=$d/$2; printf '%s\n' "$_kit_file"; return 0; }`.
- The print at :688 becomes `{ _kit_file=${_KF_DIRS[$i]}/$2; printf '%s\n' "$_kit_file"; }`.
- The print at :695 becomes `{ _kit_file=$d/$2; printf '%s\n' "$_kit_file"; }`.

The arm's opening reads as below, and its comment names this unit. `resolve_kit_file` keeps its two
literal arguments, so the pair arm at `tools/check-wiring.test.sh:1766` still reads them.

```bash
  local first rp="" miss=""
  [ -f .governance/install.json ] && rp=$(resolve_receipt_path workflows spec-audit-optin.fragment.json)
  resolve_kit_file workflows spec-audit-optin.fragment.json >/dev/null
  first_of "$rp" "$_kit_file" >/dev/null; first=$_first_of
  if [ -z "$first" ]; then
    [ -f .governance/install.json ] && miss=$(derive_receipt_miss workflows spec-audit-optin.fragment.json)
```

With no receipt each skipped call answered empty, so the arm's output does not change. With a receipt
it spends what it spends today, less the lookup. Measured at `bdd2e5f3` on bash 5.3 with this patch in
a scratch copy: 49 forks before, 45 after, PINNED. The skip line reads the same, and the file's
`pure-fn-subst` count stays 5, so no registry row moves.

`check_scratch_guard` carries the same four forks, and they stand. They predate the ceiling, and
taking them would owe a lowered row in this commit, since a ceiling more than three above its count
reds.

The probe, saved to `$TEMP/fh50forks`. It runs the wiring tool under the leg's own trace variables in
an empty repository, and runs no leg:

```bash
root=$(pwd); f=$(mktemp -d) || exit 2; trap 'rm -rf "$f"' EXIT; cd "$f" || exit 2
git init -q . && git config user.email t@t.test && git config user.name t && git commit -q -m seed --allow-empty
env SHELLOPTS=xtrace BASH_XTRACEFD=87 PS4='+${BASHPID}|${BASH_SOURCE##*/}:${LINENO}|' bash "$root/tools/check-wiring.sh" --check 87>"$f/.trace" >/dev/null 2>&1
printf 'forks %s\n' "$(($(cut -d'|' -f1 "$f/.trace" | grep -o '[0-9]*$' | sort -u | wc -l) - 1))"
```

### The forge arm's kit paths (S15)

`tools/check-install-prefix.sh:393` counts a literal kit segment followed by a file, under any lead.
The leg's header says a kit's name held in a variable spells no literal, and that is the one remedy,
because the ban takes no waiver. Read at `bdd2e5f3`: 10 spellings on 7 lines, :770 to :775 and :778,
as the bar printed them, all in unit 48's arm.

A fixture directory name is not open here. The `k/` homes are what `resolveKitDir` probes, and each
row's `source` must end `<home>/<anchor>` (`tools/lib/resolve_kit_dir.py`), so these segments are the
kit homes. They come from the suite's own derived directories, as
`tools/workflows/check-review-join.test.sh:473` does. After `FG="$TMP/fg"` at :766:

```bash
FG_HK=${HOOKS_DIR##*/}; FG_POL=${POLICY_DIR##*/}; FG_WF=${WORKFLOWS_DIR##*/}
```

Every `hooks`, `policy` and `workflows` segment of the arm's fixture paths, :767 to :778, takes its
variable, so the directories and the files read alike. The receipt at :774 moves its four spellings
into `%s` slots with the arguments `"$FG_POL" "$FG_POL" "$FG_HK" "$FG_HK"`, as `build_renamed` does.
Each variable holds today's string, so the arm's behaviour does not change.

### The five review keys (S16)

**What reds.** `arm_reader_coverage` grades a key once its catalogue `owner` has landed, every spec in
that build's folder terminal at the landed revision (`tools/policy/check_policy.py:446`,
`tools/policy/check_policy.py:530`). A key counts as read only where a call spells it
(`tools/policy/check_policy.py:483`), and no code spells these five. They reach the harness as pin
arguments, `tools/workflows/review_pin.py:100-108`.

The red came early. Spec 50 is absent from `57b1cf127`, so every spec of that tree's folder was
terminal. Once this spec is committed the arm goes quiet on this owner, and it reds again at the
CLOSED flip. So the repair has to land inside this unit.

**Each key's route, from the records:**

| Key | Carried by | The route its spec names | Planned reader |
|---|---|---|---|
| `review.opt-in` | unit 3 | `review.pin`, until dDeclaredLoop | `TOOL-dDeclaredLoop-20` S2 |
| `review.unclassed` | unit 8 | `review.pin`, until dDeclaredLoop | `TOOL-dDeclaredLoop-20` S2 |
| `review.twin` | unit 11 | a pin argument until `review.trigger` lands (spec 11, Non-goals) | none |
| `review.design-audit.runs` | unit 18 | `review.pin`, until `review.trigger` lands (spec 18, Non-goals) | none |
| `review.design-audit.seed` | unit 18 | the same | none |

The brief's list needs one correction: unit 18 carries the two `review.design-audit.*` nodes, and unit
7 only mentions `review.twin` as a non-goal.

**Three keys have no planned reader.** `TOOL-dDeclaredLoop-20` S2 reads `review.opt-in`,
`review.unclassed` and `review.blocks`, and no other. `TOOL-dBoundRoles-16` names `review.twin` and
says it reads no value of it. Grepped across every build's specs at `bdd2e5f3`, no other spec names
these three. So specs 11 and 18 point at a verb whose own spec does not take them.

**The pick, from the records.** All five rows' `owner` move to `dDeclaredLoop`, since that is the one
route any spec names. For the three keys it is a promise with no spec behind it yet, and the arm keeps
it honest: when dDeclaredLoop lands, the arm reds them by name unless a reader has come. That is
deferred coverage and not lost coverage. dDeclaredLoop holds no terminal spec of its 99, so it grades
nothing until then.

**What moving `owner` touches, read at `bdd2e5f3`:**

- The arm is the field's one reader. `policy.py` only requires the field (`tools/policy/policy.py:103`).
- The carries join does not read it. A `node:policy-key.*` owner comes from the frozen design through
  `DESIGN_NODES` (`tools/memory-tree/design_lib.py:342`), so the `Carries:` lines of units 3, 8, 11 and
  18 stay true.
- No render holds it. `.governance/policy.json` has no `owner` key, so it needs no mirror write, and no
  map file names these keys.
- `tools/policy/guarded-paths.txt` does not list `tools/policy/catalogue.toml`, so the guard admits it.

**It departs from the design, and it loosens.** The design's `[policies]` table names dFairHearing on
all five rows, and two homes state that a row's `owner` is that table's own. Each gains the exception:

- `tools/policy/catalogue.toml:2-4`, the header.
- `tools/policy/README.md:6-7`, the opening paragraph.

```text
each row's `name` and `owner` that table's own, but for `review.opt-in`, `review.unclassed`, `review.twin`
and the two `review.design-audit.*` rows, whose `owner` is the build their reader lands in, dDeclaredLoop,
and not the table's dFairHearing (TOOL-dFairHearing-50 S16).
```

The arm stops grading these keys until dDeclaredLoop lands, and until then a value set in the policy
file for any of them still does nothing. That is the state today, so no behaviour moves. It is still a
gate seeing less, so its risk class is `loosening`.

**The main loop's two records.** Neither is the builder's.

- The deviation record `2026-11-05-build-TOOL-dFairHearing-50-deviation-502`, departing from
  `dFairHearing [policies]`, with risk `loosening`. The as-built view re-renders with it.
- One ask in this build's backlog: `TOOL-dDeclaredLoop-20` S2 takes no reader for `review.twin` and the
  two `review.design-audit.*` keys. The deviation record's Follow-through names it.

The probe, saved to `$TEMP/fh50owner.py`:

```python
import tomllib
rows = tomllib.load(open("tools/policy/catalogue.toml", "rb"))["key"]
five = ("review.opt-in", "review.unclassed", "review.twin", "review.design-audit.runs", "review.design-audit.seed")
print("moved", sum(1 for r in rows if r["name"] in five and r["owner"] == "dDeclaredLoop"))
print("dFairHearing rows", sum(1 for r in rows if r["owner"] == "dFairHearing"))
```

### Inventory

- `deriveStatedItems`, a function in `tools/workflows/tier2-review.template.js` and its render
  (`js.function`, OK by `--suggest`).
- `said`, a local of the acquisition. `_nf` and `_fr`, shell locals of the fan-out gate. `_kit_file`, a
  global of `tools/check-wiring.sh`, beside `_first_of`. `wr_ret`, `FG_HK`, `FG_POL` and `FG_WF`,
  suite variables. No cell declares any of these, so none is graded.
- Two arm groups, labelled `FH50 AC2` and `FH50 AC8`, each in a suite the Gates section's `New arm:` lines
  cover.

### Generated files

No generated file is declared beside its generator, so `--dispatch` has no pair to refuse and the
unit does not split. This write set declares none of `gen_map.py`, `gen_build_index.py`, `backlog.py`,
`gotchas.py`, `policy.py` or `render_agents.py`, nor `asbuilt_view.py`, which `.unattended.conf:418`
pairs. It declares three of their outputs: `memory/map/generated/symbols.json`, `memory/LIVE.md` and
`memory/backlog/TOOL.md`. The parity script writes `tools/workflows/tier2-review.js` and is no
`[[generated]]` generator, so declaring both breaks no pair.

`memory/map/generated/symbols.json` moves by two rows, `deriveStatedItems` in the template and in the
render, as `deriveTwinFigures` carries two. `python tools/codebase-map/gen_map.py --write` renders it.
No other map file should move, and the pass confirms that from what the command touches.

No kit version moves on the branch, because the lander mints it (`tools/govkit/govkit.py:13845`).

### Rollout

One pass, with no sibling open. The commit carries no `Decided:` trailer, because no fork stands.

This unit stages no path the kickoff manifest watches, so it owes no `last-audit` re-stamp and no
delta line. `tools/gate-legs.json` stays unstaged, and the watch list holds none of the Files touched
paths, read at `bdd2e5f3`.

The new comments cite this unit's id, which the drift signal counts as product-source evidence until
the header reads CLOSED. The bar runs after that flip, as it does for every unit of this build.

The floors move in `tools/workflows/tier2-review.test.sh` (`FLOOR_ASSERTIONS`, 638 at `bdd2e5f3`) and
`tools/workflows/unattended-build.test.sh` (925). The close confirms each from a real run and takes no
count from this spec. `tools/check-spec-tokens.test.sh` and the other suites gain no assertion.

### The header's ask clause

The header carries neither `closes` nor `advances`, for the reason unit 43's Design section gives
under this same heading.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`
- `tools/workflows/check-review-join.test.sh`
- `tools/workflows/check-verifier-fanout.sh`
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/check-playbook-parity.test.sh`
- `tools/check-spec-tokens.test.sh`
- `tools/check-spec-tokens.py`
- `tools/check-wiring.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/policy/catalogue.toml`
- `tools/policy/README.md`
- `memory/map/generated/symbols.json`
- `memory/builds/dFairHearing/build/2026-11-05-build-TOOL-dFairHearing-50-1-acceptance-ledger.md`
- `memory/builds/dFairHearing/spec/2026-11-05-spec-TOOL-dFairHearing-50.md`
- `memory/builds/dFairHearing/README.md`
- `memory/LIVE.md`
- `memory/backlog/TOOL.md`

The last three are the renders the status flip forces, as unit 44 declares them. S16's deviation record,
its ask and the as-built view they move are the main loop's, and sit outside this list.

### Alternatives rejected

- **S16: move only the two keys `TOOL-dDeclaredLoop-20` reads.** The other three stay red at the close.
- **S16: build a policy-file reader for the five now.** Specs 11 and 18 rule it out, and
  `TOOL-dDeclaredLoop-20` S2 owns the route. `review.opt-in`'s set of names also differs from the pin's
  JSON grammar, so this is design work and no repair. A reader written only to satisfy the arm is worse.
- **S16: a new `reader` field beside `owner`.** It keeps the design's cell, and it adds to the policy
  kit's documented schema for five rows.
- **S16: an exemption list in the arm.** The arm has none, and one is a gate a pass can grant itself.
- **S16: `dBoundRoles` for `review.twin`.** `TOOL-dBoundRoles-16` says it reads no value of the key.
- **Moving only S8's needles to what the code prints.** The notice would then pin a false sentence: a
  hook that was never asked reported as denying.
- **Deleting the `printed no reason` branch of the parity script.** A hook ending the process with a
  silent exit 1 still reaches it, so the branch is live and keeps its arm.
- **Staging S8 at `WRITER_MARK` in the layout's `check-verifier-fanout.js`.** It stages a mismatch
  inside one kit, which no install can hold, and it names no hook.
- **A two-argument `--slots`, `<file> <line>`.** It moves a documented grammar and its readers to
  clear one spelling.
- **Fixing S9 in the render by guessing a home for an unresolved citation.** The render refuses to
  guess, on purpose, and the install it would serve does not exist.
- **Deriving S9's rows from the template.** It is more fixture than the five rows it saves.
- **Raising the `check-wiring` ceiling to 49.** A builtin does the work of each of the four forks, and
  the ceiling is shrink-only by intent.
- **A shared no-fork lookup for both fragment arms.** It lowers the row for no red, in a unit that
  repairs reds.
- **Raising the `printf-subst` row to 67.** The registry drains downward, and `printf -v` is its stated
  form.
- **`agent-cap.js` back in `SELF_EXCLUDE`.** Unit 16 took it out on purpose: it holds no ban now.

## 5. Production-readiness checklist

- security — N/A: no new write path, and no surface moves. S8 makes a gate refuse more plainly.
- perf / scale — S5 adds one `cygpath` spawn per absolute explicit file, and none on the bar's leg.
  S14 takes four forks off a session-start tool, and S13 one off a suite arm.
- error / empty / loading states — S2 names the cut, S8 exits 2 with the rule's own reason, and a
  genuine zero selection keeps its reason.
- observability — S2's reason reaches RUN INTEGRITY's `Checklist:` line. S8's refusal goes to stdout,
  and the parity script quotes it on stderr.
- risks — S16 loosens: `arm_reader_coverage` stops grading five keys until dDeclaredLoop lands, and
  three of them have no planned reader yet, so they red there unless the hand-off is taken up. S8 stops
  the gate at the first refusal where it used to carry on to the next file. A
  harness the rule cannot read now hides any finding in a later file until that is fixed.
- testing — the arms the Gates section declares, each observed RED then GREEN at the close, and the
  probes of the acceptance criteria.
- migration — none. A hook the rule cannot load refused at exit 2 before this unit too, by way of the
  fallback, so an adopter's render outcome does not change. Only the message does.
- user docs — N/A: no `help/` page names these surfaces, grepped at `bdd2e5f3`.

## 6. Acceptance criteria

Every `$TEMP` probe is the Design section's fenced block of that name, run from the repository root
and removed after the pass. Each criterion names the suite or leg the close's run observes, and the
probe a pass can run. A pass runs no suite, and no probe here runs a gate.

- **AC1** — When `node $TEMP/fh50args.js` runs, it prints `30 field(s), length not read`. At the close
  the tier2-review suite reads its arm `the args header documents all 30 fields read off` green.
  Red when: the regex still takes a property for the alias, as at `bdd2e5f3`, where the probe prints
  `31 field(s), length read`.
  figure: 30 is PINNED at `bdd2e5f3`; a new args field moves it.
- **AC2** — When `node $TEMP/fh50cut.js` runs, it prints a `stated one 1` line naming the missing
  by-design head, `stated none 0` and `no head null`. When
  `grep -c 'deriveStatedItems(' tools/workflows/tier2-review.js` runs it prints 3, and the same grep
  over `tools/workflows/tier2-review.template.js` prints 3. When
  `grep -c 'state one item or more' tools/workflows/README.md` runs it prints 1. At the close the
  tier2-review suite reads `FH23 AC27 the real stdout cut inside its item list` and
  `FH50 AC2 a head stating no class` green.
  Red when: a head line stating a class and no item reads as no selection, as at `bdd2e5f3`, where the
  probe prints `no deriveStatedItems`, or a head stating none reads as a cut.
- **AC3** — When `grep -c 'verifyOrder.length...MAX_VERIFIERS' tools/workflows/check-review-join.test.sh`
  runs it prints 1, the same grep over `tools/workflows/tier2-review.js` prints 1, and
  `grep -c 'allFindings.length...MAX_VERIFIERS' tools/workflows/check-review-join.test.sh` prints 0.
  At the close the review-join suite reads `harness: the verifier count is bounded` green.
  Red when: the needle names a variable the harness does not spell, as at `bdd2e5f3`, where the first
  grep prints 0 and the last prints 1.
- **AC4** — When `grep -c '.claude/hooks/agent-cap.js' tools/workflows/check-review-join.test.sh` runs
  it prints at least 2, `grep -c 'HKK' tools/workflows/check-review-join.test.sh` prints 0, and
  `printf '.claude/hooks/agent-cap.js\n' | grep -cE '^(tools|\.claude/workflows)/.*\.js$'` prints 0,
  so the moved copy sits outside the population's shape. At the close the review-join suite reads
  `discovery: an empty population is still not a pass` and
  `an empty refusal names both directories` green.
  Red when: a fixture's hook copy sits under the kit prefix, as at `bdd2e5f3`, where the first grep
  prints 0 and the second prints 3.
- **AC5** — When `bash $TEMP/fh50slots` runs on MSYS, it prints `node opens it`. When
  `grep -c '_nf=$(cygpath.-m' tools/workflows/check-verifier-fanout.sh` runs it prints 1. At the close
  the fan-out suite reads its six arms green: `AC3: a sixth slot`, `AC5: strings, comments`,
  `FH27 AC1: a zero-row opt-in literal`, `AC25: five slot calls`,
  `AC25: a counter splitting on every comma` and `AC26`.
  Red when: an absolute path reaches node with its suffix unconverted, as at `bdd2e5f3`, where the
  probe prints `node cannot open it`.
  permission: a Linux run reads this green at the base too, so only an MSYS host observes the red.
- **AC6** — When `grep -c 'rm -rf .*PFX}.{WF}' tools/check-playbook-parity.test.sh` runs, it prints 1.
  At the close the playbook-parity suite reads
  `S1 an empty kit derivation reds before reporting coverage` green.
  Red when: a declared kit survives the staging, as at `bdd2e5f3`, where the grep prints 0 and the gate
  reports the lost sentinel.
- **AC7** — When `bash $TEMP/fh50merged` runs, it prints the two lines "The merged key" pins. When
  `grep -c '"confirmed":0,"refuted":0,"merged":0,"unverified":48' tools/workflows/unattended-build.test.sh`
  runs it prints 1, and
  `grep -c '"raw":46,"confirmed":16,"refuted":30,"merged":0,"unverified":0' tools/workflows/unattended-build.test.sh`
  prints 1. At the close the unattended-build suite reads
  `MT zero confirmed and 48 unverified reaches the synthesis` and
  `MT20 the callee ran over the measured shape` green.
  Red when: a needle predates the key, as at `bdd2e5f3`, where each grep prints 0.
- **AC8** — When `bash $TEMP/fh50gate` runs, it prints `exit 1: carries on, st=1`,
  `verifier-fanout: the rule could not run on x.js — why`, `exit 2: subshell 2` and a line opening
  `load refused: it exports no`. When `bash $TEMP/fh50bound` runs, it prints
  `bound: split findings 1`, `bound: fallback findings 0` and `total: fallback findings 1`. When
  `grep -c 'WRITER_MARK' tools/workflows/unattended-build.test.sh` runs it prints 0,
  `grep -c '^function readWriterBound(repo) {$' tools/hooks/agent-cap.js` prints 1, and
  `grep -c '^const MAX_VERIFIERS = 5$' tools/hooks/agent-cap.js` prints 1. At the close the
  unattended-build suite reads each `DGR74 LIVENESS` arm,
  `DGR74 ...after a stderr notice carrying that hook's reason`,
  `DGR83 a hook that denies printing nothing: the notice says so` and the `FH50 AC8` arms green.
  Red when: a load failure reads as a denial, as at `bdd2e5f3`, where `$TEMP/fh50gate` prints
  `exit 2: carries on, st=0`, because the gate holds no such block, and `$TEMP/fh50bound` ends
  `total: fallback findings 0`.
- **AC9** — When `bash $TEMP/fh50cites` runs, it prints `old home 0` and `fanout gate 2`. When
  `grep -c 'check-verifier-fanout.sh once' tools/workflows/unattended-build.test.sh` runs it prints 0.
  At the close the unattended-build suite reads
  `RA6-1 ...and its check-verifier-fanout.sh twice` and
  `RA6-1 ...and the tool root plus gov's home for them nowhere` green.
  Red when: the fixture holds fewer rows than the template has citations, as at `bdd2e5f3`, where the
  probe prints `old home 6`.
  figure: 2 is DERIVED, the template's lines naming that file.
- **AC10** — When `python $TEMP/fh50exempt.py` runs, it prints `undeclared 0 []` and `stale []`. At the
  close the spec-tokens suite reads `parity: BAR matches every whole-suite selftests argv` and its
  `graded` and `exempt` arm green.
  Red when: a `--selftest` leg sits above the bound undeclared, as at `bdd2e5f3`, where the probe prints
  `undeclared 1` naming `measure-legs selftest`.
- **AC11** — When `grep -c 'THE ONE HOME OF THE WONTDO FILTER' tools/check-spec-tokens.py` runs it
  prints 0, and `grep -c "WONTDO filter's one home" tools/check-spec-tokens.py` prints 0. When
  `grep -c 'is graded there and set apart here' tools/check-spec-tokens.py` runs it prints 1. When
  `grep -c 'walk-red' memory/guides/UNATTENDED-VERBS.md` runs it prints 0, and the same grep over
  `memory/guides/UNATTENDED-STOPS.md`, `memory/guides/REVIEW-PROTOCOL.md` and
  `tools/workflows/README.md` each prints 0.
  Red when: a docstring keeps claiming one home, as at `bdd2e5f3`, where the first two print 1 and the
  third 0, or a document here starts listing the exits with `walk-red` left out, which this grep does
  not see.
- **AC13** — When `python $TEMP/fh50sites.py` runs, it prints `printf-subst 66`, and
  `grep -c 'printf -v wr_ret' tools/workflows/unattended-build.test.sh` prints 1. At the close the leg
  `shell hygiene (a fork spent on builtin work)` reads green.
  Red when: a suite site sits above its row, as at `bdd2e5f3`, where the probe prints
  `printf-subst 67`.
  figure: 66 is that file's `printf-subst` registry row, which the probe's count must equal.
- **AC14** — When `bash $TEMP/fh50forks` runs under bash 5.3, it prints `forks 45`. When
  `grep -c '_kit_file=' tools/check-wiring.sh` runs it prints 4. At the close the leg
  `spawn budget (forks per hot entrypoint)` reads its `check-wiring` row green.
  Red when: the arm forks on a tree with no receipt, as at `bdd2e5f3`, where the probe prints
  `forks 49` and the grep prints 0.
  figure: 45 is PINNED on bash 5.3 at `bdd2e5f3`, and another bash counts differently.
- **AC15** — When `grep -cE '(k|f|t)/(hooks|policy|workflows)/[a-z-]+\.js' tools/lib/resolve-python.test.sh`
  runs it prints 0, and `grep -c 'FG_HK=' tools/lib/resolve-python.test.sh` prints 1. At the close the
  leg `install-prefix (shipped surface)` reads green, and the resolver suite reads its `FH48 AC1` arms
  green.
  Red when: an arm spells a kit path, as at `bdd2e5f3`, where the first grep prints 7.
- **AC16** — When `python $TEMP/fh50owner.py` runs, it prints `moved 5` and `dFairHearing rows 0`. When
  `grep -c 'TOOL-dFairHearing-50 S16' tools/policy/catalogue.toml` runs it prints 1, the same grep over
  `tools/policy/README.md` prints 1, and `grep -c '"owner":' .governance/policy.json` prints 0. At the
  close the leg `policy check` reads `arm_reader_coverage` with no finding, and with no change to the
  mirror.
  Red when: a row names a landed owner and has no reader, as at `bdd2e5f3`, where the probe prints
  `moved 0` and `dFairHearing rows 5`.
  figure: 5 is PINNED to the five rows the bar named at `57b1cf127`.

## 7. Gates

`tier2-review self-test` · `review-join self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `playbook parity selftest` · `spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` · `dead-path carriers self-test` · `kit-placeholders self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `straggler-guard arms` · `transition-audit arms` · `shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` · `install-prefix (shipped surface)` · `policy check`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 · the args-header arm's regex moved, staged by restoring `\b`, which reads `length` · none, a moved arm

New arm: tools/workflows/tier2-review.test.sh · covers AC2 · `FH50 AC2`, staged by reading any head line as a cut, which logs `checklistError` · `FLOOR_ASSERTIONS` moves, the close confirms it

New arm: tools/workflows/check-review-join.test.sh · covers AC3 · the needle moved, staged by restoring `allFindings` · none, a moved arm

New arm: tools/workflows/check-review-join.test.sh · covers AC4 · the two fixtures moved, staged by restoring the kit-prefix copy, which reads the hook as population · none, a moved arm

New arm: tools/workflows/check-verifier-fanout.test.sh · covers AC5 · no arm moves; the six read RED at `948e4141b` on MSYS · none

New arm: tools/check-playbook-parity.test.sh · covers AC6 · the staging moved, staged by leaving `${WF}` out, which names the lost sentinel · none, a moved arm

New arm: tools/workflows/unattended-build.test.sh · covers AC7 · the two needles moved, each read RED at `948e4141b` · none, a moved arm

New arm: tools/workflows/unattended-build.test.sh · covers AC8 · the `DGR74` and `DGR83` stages and `FH50 AC8`, staged against the gate at `bdd2e5f3`, which exits 1 and names a denial · `FLOOR_ASSERTIONS` moves, the close confirms it

New arm: tools/workflows/unattended-build.test.sh · covers AC9 · the fixture's rows and the moved count, staged by cutting one row, which leaks that citation · none, a moved arm

New arm: tools/check-spec-tokens.test.sh · covers AC10 · the list moved, read RED at `948e4141b` · none, a moved arm

New arm: tools/workflows/unattended-build.test.sh · covers AC13 · the walk-red arm respelled, its leg read RED at `57b1cf127` · none, a moved arm

New arm: tools/lib/resolve-python.test.sh · covers AC15 · the forge arm's paths moved, its leg read RED at `57b1cf127` · none, a moved arm

These verdicts come from each leg's source, the baseline's logs and the bar's lines, because this
spec's author may run only `memory hygiene` and the lexicon. S14 and S16 add no arm: their legs are
the spawn budget and `policy check`, each read RED at `57b1cf127`. The main loop reads the first real output at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-05 · S1 to S11, S13 to S15 · AC1 to AC11, AC13 to AC15 · initial draft from brief
  `2026-11-05-prompt-TOOL-dFairHearing-50-spec-brief`, every item re-grounded at `bdd2e5f3`. The tier
  moves to Tier-2 for S2 and S8. S8 corrects the gate as well as the arms, S9 finds no real gap, and
  S11 finds no list of stop exits. S13 to S15 are the main loop's three items from the bar at
  `57b1cf127`, folded before this draft was committed.
- rev-2 · 2026-11-05 · AC2, AC8 · the labels bullet opens `Two arm groups` until the build, because the
  arm-labels join reads a label's suite and these arms do not exist yet; the CLOSED flip restores the
  opener so the join grades them from then on.
- rev-3 · 2026-11-05 · S16 · AC16 · the five review rows' `owner` move to `dDeclaredLoop`, from the bar's
  `policy check` at `57b1cf127`. Three of the keys have no planned reader, which the hand-off edge
  carries. No fork stands: the records name the one route.

## 10. Reuse audit

Each item extends a seam the tree carries: `checkChecklistWhole` (`tools/workflows/tier2-review.template.js:1415`)
for S2, the `.claude/hooks/` rung (`tools/workflows/check-review-join.sh:303`) for S4, the slot call's
own case block (`tools/workflows/check-verifier-fanout.sh:364`) for S8's loop, and `PARITY_EXEMPT` for
S10. S5 takes the idiom at `tools/unattended/stop-guard.test.sh:265`. S9 extends `build_renamed`. S14
takes `first_of`'s setter idiom (`tools/check-wiring.sh:325`), and S15 the derived-segment idiom of
`tools/workflows/check-review-join.test.sh:473`. S16 edits catalogue data, and its reader stays
`arm_reader_coverage`.

`python tools/codebase-map/reuse_lookup.py "a gate hands a native program a path with a line suffix on Windows"`
and `"a checklist return is cut before its first item"` ranked generic name stems only, so no
existing seam fits beyond the sites above, each read by hand. Recall put `TOOL-dGroundRules-83` first,
which sets the rule S8 applies: a gate that could not ask the hook is no verdict. The records and the
code disagreed in one place: that spec's comment lists the hook, node or a checkout as the causes, and
a hook the rule cannot load is a fourth, which S8 adds.

Recall terms used: `python tools/memory-recall/query.py "a gate that could not ask the hook is no verdict, and a msys path with a suffix is not converted" --terms "fan-out gate exit refusal writer-split stub hook cygpath msys readWriterBound loadHook parity render"`

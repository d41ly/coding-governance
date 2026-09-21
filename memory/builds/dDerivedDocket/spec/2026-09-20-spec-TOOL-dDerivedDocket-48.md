# TOOL-dDerivedDocket-48 — the ask witness reads a stream the capture does not merge

**Status:** CLOSED · rev-2 · 2026-09-21 · node d · Tier-2 · base fb07ca25 · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-build-TOOL-dDerivedDocket-48-1-acceptance-ledger.md](../build/2026-09-21-build-TOOL-dDerivedDocket-48-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md) | spec-audit | TOOL-dDerivedDocket-49 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54 |

<!-- /gen:spec-records -->

## 1. Goal

The `ASKS_CMD` witness parses a TSV in which every line must lead with `ask` or `examined`, while
the one bounded runner it is called through redirects the command's stdout and stderr into a single
capture file and reads that file back (`tools/unattended/unattended.sh:199-204`, at this unit's
parent; every citation below that names the capture BEFORE the split names that commit). Every notice unit
15 routed to stderr therefore arrives inside the text the parse refuses on, so a healthy producer
reads as a DEAD PROBE. Split the capture once, inside `run_bounded`, so the row stream and the
notice stream reach the caller as two values.

## 2. Scope (IN)

- **S1** `run_bounded` captures the two streams into two files rather than one, both under a
  single scratch directory from one `mktemp -d`, under the same `timeout -k 5s` wrapper, the same
  `</dev/null` and the same file form in both branches, and publishes three values beside
  `RB_TOOK`: `RB_STDOUT`, the command's stdout alone; `RB_ERR`, its stderr alone; and `RB_OUT`,
  which keeps every byte both streams produced. The teardown moves with the capture: the `rm -f` of
  the one file (`tools/unattended/unattended.sh:205` at the parent) becomes a recursive removal of
  that directory. On the `mktemp -d` refusal branch `RB_STDOUT` and `RB_ERR` are set empty and `RB_TOOK`
  is set to 0, while `RB_OUT` KEEPS that branch's existing sentence,
  `run_bounded: cannot create a capture file`, byte-for-byte: it is the branch's only diagnostic
  and three callers print it. Observed by AC1.
- **S2** The one behaviour delta is declared: `RB_OUT` becomes stdout followed by stderr rather than
  the two interleaved in arrival order. No byte is lost, so EVERY caller that reads it keeps its
  whole diagnosis and loses only the relative order of the two streams. The three this unit grades
  are `$WIRING_CHECK` (`tools/unattended/unattended.sh:1573`), `$GATE_CMD` (`:4556`) and
  `$SPEC_TOKENS_CLI` (`:6159`); five more arrived from unit 3 after this spec's base and each prints
  `RB_OUT` whole through the same idiom — `check_lander_mode` (`:1624` and `:1627`),
  `check_inplace_preconditions` (`:4158`), `check_landing_carry` (`:4207`) and `write_close_commit`
  (`:4238`). None of the eight is edited. Observed by AC3.
- **S3** The row stream is named. The `ASKS_CMD` parse reads `RB_STDOUT`, never `RB_OUT`, and the
  refusal it prints on a real column change quotes the line it refused on. This unit states which
  capture the parse is handed; the parse itself is unit 16's, and units 17, 18 and 24 route the same
  call. Observed by AC4.
- **S4** One helper, `read_stderr_tail`, returns a bounded tail of `RB_ERR` — at most the first 20
  lines and 2000 bytes, with a line naming how many lines were dropped, printed even at zero so a
  short producer and a truncated one stop reading the same. Its consumers are
  `derive_stream_verdict` and the witness units that parse `RB_STDOUT`, and NOT the refusals that
  quote a bounded call's output: those quote `RB_OUT`, which is already the concatenation, so a tail
  beside it would print the producer's stderr twice. What keeps a checker whose whole diagnosis is on
  stderr from being reported with an empty reason is that concatenation, and AC3 grades it. Observed
  by AC5 and AC6.
- **S5** A stdout-empty call is no longer one undivided fact, and the discrimination has a subject
  at THIS unit's order rather than only in consumers that do not exist yet. A second helper,
  `derive_stream_verdict`, takes `RB_STDOUT`, `RB_ERR` and the bounded call's status and RETURNS
  one of three distinct strings: the producer wrote only to stderr, carrying `read_stderr_tail`'s
  output; both streams empty, which is the DEAD PROBE it is today; and a bound breach, which keeps
  the never-answered wording the `gates-green` item already DRAWS
  (`tools/unattended/unattended.sh:4561`). It decides and prints nothing, and which callers adopt
  it is unit 16's and unit 17's, per §3. Observed by AC5.
- **S6** Every new refusal branch gets an arm in `tools/unattended/unattended.test.sh`, each observed
  RED with its fix unstaged. The `tools/unattended/unattended.sh` pair of `ARMS_FLOORS` in
  `.memory-tree.conf` does NOT move: `tools/memory-tree/check-arms.py` counts `fail <n> "` call
  sites, this unit adds none — the capture refusal is an existing branch and neither helper refuses
  through `fail` — and the count is the same at this commit as at its parent. A floor is one-sided
  upward, so an unchanged count leaves it holding and `.memory-tree.conf` out of the write set.
  Observed by AC8.
- **S7** This unit's delta on every capped carrier is ZERO. It writes no conf key, so leg check 22
  owes it no protocol table row, and it writes no guide, Skill or dossier prose. The unattended
  dossier is the tight carrier here and is not opened: it held 20467 B of a 20480 B cap at this unit's
  parent, which is 13 B of headroom — 93 B when this spec was written, and re-measured for rev-2, and no claim key moves because the codebase map does
  not scan `.sh` at all. Observed by AC7.

## 3. Non-goals (OUT)

- The `--asks --tsv` projection, its eleven fields and the rule that its notices go to stderr are
  unit 15's. This unit changes no producer.
- The `ASKS_CMD` key, its call shapes, the pinned mandate and the parse are unit 16's. The
  `asks-disposed` term and the landing freeze are unit 17's, the leg's second opinions are unit
  18's, and the inherited-red read-back is unit 24's. Each routes the call this unit fixes and none
  of them is rewritten here. Units 16, 17 and 18 declare the edge to this unit, and the Edges block
  below names all three back. Unit 24 declares none and this unit declares none to it: that unit
  reaches this capture through the consumes-from edge it already declares to unit 16, whose own
  consumes-from edge names this unit, so every hop is declared and check 12's edge arm grades each
  one for order (`tools/memory-tree/check-memory-hygiene.sh:1796`). A direct edge would buy no
  guarantee that two-hop chain does not already give and would owe a reciprocal bullet in that
  unit's own Edges block, so §4 reaches that read-back transitively rather than claiming it as
  coverage of its own.
- The per-slug process ledger that wraps `run_bounded` is unit 28's. This unit changes the capture
  inside that wrapper and builds no ledger; the pin that unit's S1 places on the capture is the one
  sentence that moves, and it moves in that unit's own spec.
- The lease refresh placed inside `run_bounded` is not moved, re-scoped or re-conditioned. Its
  placement is unit 4's and this unit preserves it.
- The declared gate wall and the driver's bound stack are unit 27's. `GATE_BOUND`, `GATE_BOUND_LIVE`
  and the `timeout -k 5s` wrapper are read and never rewritten here.
- Option (b) of the promoting record — a parse that skips non-row lines — is rejected in §4 and is
  not built, in whole or as a fallback.
- The companion guide and the Skill text that describe a refusal's shape are unit 20's.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-15` — the rule that under `--tsv` stdout carries the `ask`
  lines and the `examined` line and nothing else, while the waiver line and every other notice go to
  stderr. Without it the split buys nothing, because the rows and the notices would still share one
  stream and AC4 could not tell a clean row stream from a merged one. That unit's spec already
  carries the reciprocal, at
  `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md:106`.
- **hands-off** `TOOL-dDerivedDocket-16` — which capture the `ASKS_CMD` witness is handed:
  `run_bounded` keeps the producer's stderr out of the row stream, so that unit's contract and S5
  stand as written and its parse refusal fires on a real column change rather than on a notice.
- **hands-off** `TOOL-dDerivedDocket-17` — the same capture under the `asks-disposed` witness, so
  that unit's T2 reports a DEAD PROBE only for a producer that is actually short, and `run_bounded`
  is no longer the reason a healthy one is refused.
- **hands-off** `TOOL-dDerivedDocket-18` — the same capture under S8's re-derivation, the leg's one
  second opinion that executes a producer, which routes `ASKS_CMD` through `run_bounded` as the
  driver does.
- **hands-off** `TOOL-dDerivedDocket-28` — the capture that unit's S1 pins as unchanged. It is two
  files after this unit rather than one, under the same `timeout -k` wrapper, so that pin is
  restated rather than dropped and the ledger still wraps exactly one `run_bounded`. That unit's own
  Edges block already carries the reciprocal in its own words: the two-file capture inside
  `run_bounded` is what its ledger WRAPS rather than rewrites, and without this unit landing first
  its own pin would read as forbidding the split, leaving the two units contradicting each other on
  one function.

## 4. Design

### The capture today, and why it defeats the fix it was supposed to carry

`run_bounded` is one function with two branches, and both redirect the same way:

```
timeout -k 5s "$GATE_BOUND" "$@" </dev/null >"$_f" 2>&1; _rc=$?
...
"$@" </dev/null >"$_f" 2>&1; _rc=$?
...
RB_OUT=$(cat "$_f" 2>/dev/null)
```

`tools/unattended/unattended.sh:199-204` at the parent. One buffer, both streams. The file form itself is
load-bearing and is kept: the function's own header records that a command substitution reads until
EOF and EOF arrives when the last inherited write end closes, so a surviving grandchild holds it
while `timeout` reports on schedule. That class is named in
`memory/gotchas/bounded-through-a-pipe-is-unbounded.md` and this unit does not reopen it.

The producer writes a notice on every healthy call. `collect()` prints its waiver line
unconditionally, including at zero (`tools/memory-tree/gen_build_index.py:988`), and unit 7's
liveness line joins it. Both are on stderr by unit 15's output rule. The `2>&1` puts them back in
front of a parse that refuses any line whose first field is not `ask`.

### The capture after

Both branches redirect the two streams to two paths under one scratch directory, and the function
reads each back. The stdout path feeds `RB_STDOUT` and the stderr path feeds `RB_ERR`, each by its
own command substitution. `RB_OUT` is read by ONE substitution over BOTH capture files in that
order, and never by joining the two VALUES with a separator. The difference is not style. `cat`
over an empty file contributes nothing, so a call that wrote only to stderr still leaves `RB_OUT`
opening on the producer's first stderr line, where a join would open it on a blank line — and
`tools/unattended/unattended.sh:6245` names `head -1` of `RB_OUT` in the `--dispatch` refusal, so
that blank line is a refusal naming nothing on exactly the input this unit exists to make
readable.

Every byte both streams produced is still in `RB_OUT`, which is why the three callers below need no
edit. What changes is the interleaving: a command that alternates between the streams now reads as
two blocks rather than one conversation. That is stated here because it is the only observable
difference for a reader of a refusal, and because an arm that greps `RB_OUT` for a phrase is
unaffected by it.

The refusal branch is widened deliberately, and NOT in the direction a first reading suggests. At the
parent that branch is one line, `tools/unattended/unattended.sh:193`: it SETS `RB_OUT` to the string
`run_bounded: cannot create a capture file` and returns, before `RB_TOOK` is assigned at `:203`.
`RB_OUT` is therefore not stale on that path. It is the freshest and only thing the caller gets,
and the three callers this unit grades print it: `check_wiring` (`:1673`), `gates-green` through
`DOD_OUT` (`:4452`), and `--dispatch` through `head -1` (`:6245`). Emptying it would make a failed
capture refuse with no reason at all, which is this unit's own defect arriving on the one path it
opens deliberately. The value that genuinely carries over from the previous call is `RB_TOOK`, which
`:6246` prints in the `--dispatch` refusal. So the branch sets the two NEW values empty, sets `RB_TOOK` to 0, and
leaves `RB_OUT`'s sentence untouched.

### Who reads which

| Caller | Reads | Why |
|---|---|---|
| `$WIRING_CHECK` in `check_wiring` (`tools/unattended/unattended.sh:1656`) | `RB_OUT` | the wiring report is for a human and both streams are wanted |
| `$GATE_CMD` in `gates-green` (`:4553`) | `RB_OUT` | `DOD_OUT` quotes the bar's whole output into the unmet item |
| `$SPEC_TOKENS_CLI` at `--dispatch` (`:6239`) | `RB_OUT` | the checker's refusal is printed whole |
| the `ASKS_CMD` witness | `RB_STDOUT`, with `read_stderr_tail` beside it | the rows are data to parse; the notices are evidence to report |

The witness row covers the three callers this unit declares an edge to: unit 16's call shapes 1 and
2, unit 17's witness at close and at the freeze, and unit 18 S8's re-derivation. Unit 24's
working-tree read-back runs the same call and is reached TRANSITIVELY rather than claimed here — it
takes the call contract from unit 16, which is the edge that unit declares, and §3 says so. All four
are one parse by those specs' own rule, so naming the capture once here is what keeps it one parse.

### The three verdicts a stdout-empty call can carry

A parse that sees no `ask` line is three different facts, and today they are one.

| State | Verdict |
|---|---|
| `RB_STDOUT` holds rows | parse them; a line that is neither `ask` nor `examined` is a parse refusal quoting that line |
| `RB_STDOUT` empty, `RB_ERR` non-empty | the producer wrote only to stderr, quoting `read_stderr_tail` |
| both empty | DEAD PROBE, as today |
| the bound fired | never answered, as today (`tools/unattended/unattended.sh:4557-4562`) |

The second row is the one this unit adds, and it is the liveness assertion the charter's quality-gate
rules ask of any probe: a producer that is talking and a producer that is dead stop reporting the
same way.

`derive_stream_verdict` (S5) is the one reader of THE LAST THREE ROWS of that table. It reads the
two captures and takes the call's status, so the discrimination is written once and is gradeable at
this unit's order rather than re-derived inside each of the four consumers that route this call.

The first row is the CALLER's and the helper has no string for it, which is a precondition and is
enforced rather than assumed: asked for a verdict while `RB_STDOUT` holds rows, it returns 1 and
prints nothing. Returning one of the three there would report a producer that is plainly talking as
one of the three states none of which it is in, and printing nothing without a status would hand the
caller a blank line. It still returns exactly one of three distinct strings whenever it returns one
at all.

The never-answered string is DRAWN from the `gates-green` item's wording, not copied from it. That
sentence names the merge bar and `$GATE_CMD`, and a helper with no caller knows neither, so the
clause that carries the meaning is kept verbatim — did not answer within the declared bound and was
killed after the elapsed figure, unanswered because the command never returned rather than because
it said no — with "the declared command" where the item says "the merge bar".

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `RB_STDOUT`, `RB_ERR` | driver globals beside `RB_OUT` and `RB_TOOK` | screaming snake, as both siblings; `.lexicon.conf` declares no shell constant cell, so no naming arm grades them |
| `read_stderr_tail` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest read_stderr_tail --as sh.function` answered OK on 2026-09-20 |
| `derive_stream_verdict` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest derive_stream_verdict --as sh.function` answered OK on 2026-09-20 |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh`. NOT `.memory-tree.conf`:
rev-2's S6 measured the `fail` branch count as unmoved, so `ARMS_FLOORS` stays where it is. No
protocol copy, no guide, no Skill and no dossier (S7).

### Rollout

Order 15, shared with units 15 and 49, and shared deliberately rather than for want of a number.
Orders 1 to 38 are all occupied, so no free integer sits between unit 15's step and unit 16's, and
both this unit and unit 49 have to land before unit 16 consumes them. Sharing is legal where the
dependency runs: check 12's edge arm reds a consumes-from whose target sits at a LATER order
(`tools/memory-tree/check-memory-hygiene.sh:1796`) and a hands-off whose target sits EARLIER
(`:1798`), and says nothing about an equal one, so this unit's consumes-from edge to unit 15 is
satisfied at the same step. Dispatch is strictly sequential including within a shared `order` value
(`tools/workflows/unattended-build.js:70`), and the harness sorts by step and then by id as a string
(`:314`, with the tiebreak at `:318`), which runs unit 15 first, this unit second and unit 49 third —
the sequence AC4 needs, because it reads unit 15's stderr routing and its builds-mode fixture.
Disjointness is not proven for the group and is not claimed, and the DRIVER does not supply the
sequence either: `--dispatch`'s own order gate blocks only on a sibling at a STRICTLY earlier order
(`tools/unattended/unattended.sh:5010`), under a rule that reads a shared value as a parallel group
which does not block (`:4983`), so a dispatch of this unit while unit 15 is still open is permitted
there. What holds the sequence is the harness's roster order and nothing else. A renumber must keep
this unit at or after unit 15's step and at or before unit 16's, or AC4 loses the fixture it grades
against and unit 16's consumes-from edge reds.

The change is dark for the witness, because no gov README carries an `asks:` key and `ASKS_CMD` is
blank until unit 35 arms it. It is live for the three existing callers from this commit, which is
why AC3 exists. `read_stderr_tail` and `derive_stream_verdict` are dark with the witness, which is
why AC5 and AC6 grade them by DIRECT call over a stub rather than through a caller's output: a
helper with no live caller at this order has no failing case otherwise, and a layer that stays
inert while its suite reads green is the shape this build files elsewhere.

### Alternatives rejected

- **Option (b), a parse that skips non-row lines.** It reverses the fix this build already made at
  the producer, it gives up the ability to tell a dead probe from a chatty one, and it needs a rule
  saying what distinguishes a notice from a malformed row — which is exactly the discrimination the
  `ask`-led eleven-field rule exists to make. It would also have to be written in four consumers
  where the split is written in one function.
- **A second bounded runner beside `run_bounded`.** Two bounded runners are two answers to one
  question. The lease refresh and the process ledger each wrap the one runner, so a second one
  either duplicates both or silently leaves the witness call unleased and unrecorded.
- **Discarding stderr at the call site.** It makes the row stream clean and throws away the
  producer's only evidence on a red, which is the absence-of-crash-evidence class the charter's
  cross-OS section names.
- **Moving the notices back to stdout.** It reverses unit 15 AC6 and unit 7's output rule, and puts
  a count inside the row stream that every consumer must then skip.

## 5. Production-readiness checklist

- security — no new input is trusted and no new path is written. `RB_ERR` is producer output quoted
  into a refusal, so the tail is bounded (S4) to keep a chatty command from flooding a park row.
- perf / scale — the `mktemp` at `tools/unattended/unattended.sh:193` (at the parent) is SWAPPED for a `mktemp -d`
  rather than added, so the directory costs nothing extra; the reads go from the one `cat` at
  `:204` to three, because §4 forbids joining the two VALUES and `RB_OUT` takes its own
  substitution over both files, which is two extra reads per bounded call against calls that are
  already a subprocess and a bound. The teardown goes from `rm -f` to a recursive removal of one
  directory (S1). The file form that makes the bound real is unchanged.
- error / empty / loading states — the three stdout-empty states above are separated and
  `derive_stream_verdict` returns one string per state; the `mktemp -d` refusal empties the two new
  values and zeroes `RB_TOOK` while KEEPING `RB_OUT`'s existing sentence, which is that branch's
  only diagnostic; and a bound breach keeps its own wording.
- observability — a refusal now names which stream it read and quotes the other, so a run that
  refuses says whether the producer was silent or merely noisy.
- risks — `RB_OUT` stops interleaving, which is the one observable delta and is pinned by AC3. A
  second risk is scope creep into the runner's bound, which §3 cuts explicitly.
- testing — arms for the split, for both existing bound properties, for the three callers, for the
  real producer's two streams, for the three stdout-empty verdicts, and for the tail bound. Each is
  observed RED with its fix unstaged.
- migration — none. No file format, conf key or record field changes.
- user docs — none owed. This unit writes no conf key, so leg check 22 asks for no protocol row, and
  the guide and Skill prose that describe refusal shapes are unit 20's.

## 6. Acceptance criteria

- **AC1** — When a stub command writes one known line to stdout and a different known line to
  stderr and the driver's `run_bounded` runs it over a scratch fixture, `RB_STDOUT` holds the first
  and not the second, `RB_ERR` holds the second and not the first, and `RB_OUT` holds both. When
  `mktemp -d` is made to fail on the same stub, the function returns 1, `RB_STDOUT` and `RB_ERR`
  are empty, `RB_OUT` still reads `run_bounded: cannot create a capture file` verbatim, and
  `RB_TOOK` reads 0. The arm SEEDS `RB_TOOK` with a non-zero sentinel immediately before that
  refusing call rather than leaning on a prior successful one: the stub returns inside a second and
  `tools/unattended/unattended.sh:227` computes `RB_TOOK` in whole seconds from `date +%s`, so a
  prior call leaves it at 0 already and the zeroing assertion would pass whether or not the branch
  zeroes anything. The arm extracts the function from the driver the way the kit's existing bound
  arms do (`tools/unattended/unattended.test.sh:5374`).
  Red when: either branch of `run_bounded` still merges the two streams into one capture file, so
  `RB_STDOUT` holds the stderr line and a healthy producer reads as a parse refusal; or the refusal
  branch empties `RB_OUT`, so a failed capture refuses with no reason at all through the three
  callers that print it at `tools/unattended/unattended.sh:1673`, `:4452` and `:6245`; or it leaves
  `RB_TOOK` holding the previous call's figure, so the `--dispatch` refusal at `:6246` reports an
  elapsed time this call never measured.
- **AC2** — When the extracted `run_bounded` runs against a 2s `GATE_BOUND` over a 30s sleeper it
  returns in under 20s with status 124 or 137, and when it runs against a command that backgrounds a
  30s grandchild and exits it does not block — the two properties
  `tools/unattended/unattended.test.sh:5392-5406` already pin, re-observed against the two-file
  form.
  Red when: the split is written as a command substitution or a pipe, so the runner blocks on a
  surviving grandchild and the bound becomes a decoration.
  cost: about 40s of sleepers, which is the cost those two arms already carry.
  fixture: a host with a runnable `timeout -k`; where there is none the arms announce the skip they
  announce today (`tools/unattended/unattended.test.sh:5371`), and the skip names which property went
  unexercised.
- **AC3** — When `$WIRING_CHECK`, `$GATE_CMD` and `$SPEC_TOKENS_CLI` are each stubbed in a scratch
  fixture conf to write one line to stdout and one to stderr, each of the three refusals the driver
  prints quotes both lines, and the `gates-green` unmet item still quotes the bar's whole output
  through `DOD_OUT`. When `$SPEC_TOKENS_CLI` is stubbed again to write NOTHING to stdout and one
  known line to stderr, the `--dispatch` refusal's own tail
  (`tools/unattended/unattended.sh:6245`) names that stderr line and not an empty string.
  Red when: `RB_OUT` is set from stdout alone, so a checker whose entire diagnosis is on stderr
  refuses with an empty reason and the run reports a failure nobody can read; or `RB_OUT` is built
  by joining an empty `RB_STDOUT` to a non-empty `RB_ERR` with a separator, so it opens on a blank
  line and that same refusal names nothing while every byte is still present — the failure a
  one-line-to-each-stream stub cannot reach, which is why the second stub is here.
  permission: the `$WIRING_CHECK` and `$GATE_CMD` halves run the driver's `--preflight` and
  `--close` verbs over the suite's own fixture, which a pass may not run, so both are deferred to the
  run the main loop makes at VERIFYING. The `$SPEC_TOKENS_CLI` half is NOT deferred: its refusal's
  tail derivation is extracted from the driver the way AC1 extracts `run_bounded` and run over a stub
  in the pass, and the `RB_OUT` property all three depend on is observed directly there, with both
  of the Red-when breaks staged.
- **AC4** — When the producer this repository declares runs under `--asks --tsv` through
  `run_bounded` over the builds-mode fixture tree, with the fixture's ask count known, `RB_STDOUT`
  is exactly that many `ask` lines followed by one `examined` line and nothing else, every line
  leading with one of those two words, while `RB_ERR` carries the waiver line. The count read from
  `RB_STDOUT` equals the fixture's ask count rather than resolving to a DEAD PROBE. The waiver line
  needs no arranging: `tools/memory-tree/gen_build_index.py:988` prints it on every call, including
  at zero.
  Red when: the bounded runner hands the row stream a notice, so a producer that is working reads as
  a parse refusal and every mandated preflight refuses as a DEAD PROBE. This is the arm whose
  absence let the producer-side fix look landed, and it is observed RED by restoring the merged
  redirect in one branch before it is allowed to pass.
  fixture: the builds-mode fixture tree unit 15 AC7 builds, and unit 15's stderr routing, which the
  shared step's dispatch order lands before this unit runs. The fixture is rebuilt from that unit's
  own renderers in a scratch repo and the producer is run over it in the pass; no arm for it is
  written into `tools/unattended/unattended.test.sh`, because a kit file names nothing outside itself
  by literal and the declared route to that producer, `ASKS_CMD`, is blank until unit 35. Its
  permanent arm is the witness units', which reach the producer through that key.
- **AC5** — When the arm extracts `derive_stream_verdict` from `tools/unattended/unattended.sh`
  the way AC1 extracts `run_bounded` (`tools/unattended/unattended.test.sh:5374`) and calls it
  directly after a stub that wrote nothing to stdout and one line to stderr, it returns the
  wrote-only-to-stderr string, carrying `read_stderr_tail`'s output; after a stub that wrote to
  neither it returns the DEAD PROBE string; and on a status of 124 or 137 it returns the
  never-answered string, whose wording is DRAWN from the one the `gates-green` item already writes
  at `tools/unattended/unattended.sh:4561` — the same "did not answer within the declared …s bound
  and was killed after …s" clause, with "the declared command" where that item names the merge bar,
  which a helper with no caller cannot know. The three returned strings differ from each other. A
  fourth call, made while `RB_STDOUT` holds rows, returns 1 and prints nothing.
  Red when: a talking producer with an empty stdout is given the DEAD PROBE string, so a broken
  redirect and a dead command are one verdict and a green-looking zero means nothing; or two of the
  three strings are equal, so a caller printing them cannot tell the states apart.
- **AC6** — When a stub writes 500 lines to stderr and the arm extracts `read_stderr_tail` from
  `tools/unattended/unattended.sh` the way AC1 extracts `run_bounded`
  (`tools/unattended/unattended.test.sh:5374`), what it returns holds at most 20 of those lines,
  names how many were dropped, and is at most 2000 bytes.
  Red when: the tail is unbounded, so one chatty producer fills a park row and a refusal nobody can
  read replaces the one that was readable.
  figure: 20 lines and 2000 bytes are PINNED literals declared in the driver beside
  `read_stderr_tail`, not derived from anything.
- **AC7** — When this unit's commit is compared with its parent, `git cat-file -s` at the parent
  equals `wc -c` at the commit for `memory/map/features/unattended.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md`, and the line
  count of each protocol copy, read with `git cat-file -p` piped to `wc -l` at both commits,
  matches.
  Red when: this unit spends the unattended dossier's headroom, which is 13 B at this unit's
  parent, or touches a protocol copy this build has priced for other units.
  figure: the headroom is PINNED and was RE-MEASURED for rev-2, because it moved: 93 B on
  2026-09-20 at `fb07ca25` (20387 B), and 13 B on 2026-09-21 at this unit's parent (20467 B),
  against the unchanged `DOSSIER_CAP_BYTES` of `tools/memory-tree/check-memory-hygiene.sh:90`; the dossier's
  line half is declared 0 on that same line and is therefore off, while the guides' line half is
  declared at `:84` and is read here.
- **AC8** — When the driver suite runs, every refusal branch this unit adds has an arm and the
  suite's executed-assertion floor holds. The `tools/unattended/unattended.sh` pair of `ARMS_FLOORS`
  in `.memory-tree.conf` is UNCHANGED, and the observation is that `fail <n> "` call sites in
  `tools/unattended/unattended.sh` number the same at this commit as at its parent — S6's reason.
  Red when: a branch lands with no arm, so the refusal this unit adds is never exercised and the
  floors still pass on the old count; or a `fail` branch did land, in which case an unmoved pair is
  a floor that has gone slack by exactly that branch.
  permission: the suite run and the `harness arms (fail branches armed or pinned)` leg over the real
  tree are runs this pass may not make, so both are deferred to the run the main loop makes at
  VERIFYING after the last unit. In the pass each new arm is observed RED by hand against a scratch
  fixture with its fix unstaged, which is this criterion's direct check.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · restoring the merged redirect in either branch of
`run_bounded`, and separately stubbing a producer that writes only to stderr · the driver suite's
executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/unattended.sh`

## 8. Open questions

- **F1 — which half of the promoting record's fork this unit takes.** Option (a) is a capture that
  keeps stderr on its own channel; option (b) is a parse rule that skips non-row lines. RESOLVED
  (agent, 2026-09-20, delegated): (a). Three reasons, in order of weight. It honours the
  producer-side fix this build already made rather than reversing it at the other end. It keeps the
  ability to tell a dead probe from a chatty one, which option (b) gives up by construction. And it
  is written once, in the one function all four consumers route through, where option (b) is written
  in four consumers and can be forgotten in a fifth.
- **F2 — what happens to `RB_OUT`.** Options: keep it as the two streams concatenated; retire it and
  re-point the three existing callers at `RB_STDOUT` and `RB_ERR`; or keep it and deprecate it.
  RESOLVED (agent, 2026-09-20, delegated): keep it as the concatenation. Retiring it makes this unit
  edit three refusal paths it has no other reason to open, one of them the `gates-green` item, which
  is a write path this build is already changing elsewhere. The concatenation loses interleaving and
  nothing else, and AC3 pins that the three callers still see both streams.
- **F3 — where the stderr tail bound is declared.** Options: a literal beside `read_stderr_tail`, or
  a conf key. RESOLVED (agent, 2026-09-20, delegated): a literal. A new conf key owes a protocol
  key-table row under leg check 22, and spending capped-carrier bytes is the one thing this unit set
  out not to do (S7). The literal is named PINNED in AC6 so a later session knows it was chosen
  rather than measured.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft. Promoted from the G3 round-2 spec audit's standing blocker B1
  (raw id 21) at the review's bounded exit. The design takes option (a) of that record's fork and
  states why option (b) is refused; AC4 is the left-shift arm that record asks for, written against
  the real declared producer with a notice that is guaranteed present; the Edges block names the
  four siblings that route the same call.
- rev-1 · 2026-09-20 · §3 §4 · close-out of the same rev, folding the p1 verifier's three problems.
  The Rollout states why order 15 is shared rather than chosen: orders 1 to 38 are occupied, both new
  units land before unit 16, and check 12's edge arm grades an equal order as satisfied. §4's
  witness-row note claims only the three callers this spec declares an edge to, and §3 states how
  unit 24 reaches the same capture through unit 16 rather than through an edge nobody declared.
  Extended by the close-out's verifier, same base and rev · §3 · §4 · the Rollout no longer says a
  shared `order` is not a parallel instruction. `--dispatch`'s own order gate reads it as exactly
  that: it blocks only on a STRICTLY earlier sibling (`tools/unattended/unattended.sh:5010`) under
  the rule stated at `:4983`, so the sequence AC4 depends on rests on the harness's roster order
  alone, which the Rollout now says. §3 also drops an ordinal count of this pass's cross-edits,
  which no later reader can check.
- rev-1 · 2026-09-20 · §2 · §3 · §4 · §5 · §6 · §9 · fold of the G7 round-1 spec audit
  (`memory/builds/dDerivedDocket/reviews/2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md`),
  findings H2 (26), M1 (3), L2 (22) and L3 (23), all disposed FOLD by the orchestrator. H2: the
  premise was false at HEAD. `tools/unattended/unattended.sh:185` SETS `RB_OUT` to the branch's
  only diagnostic and returns before `RB_TOOK` is assigned at `:195`, so S1, §4 and AC1 now keep
  that sentence byte-for-byte, empty the two NEW values and zero `RB_TOOK` instead; built as it
  read before, a failed capture would have refused with an empty reason through `:1208`, `:3285`
  and `:4974`. M1: AC5 named no subject and every caller this spec names reads `RB_OUT`, so S5 now
  declares `derive_stream_verdict`, §4 names it as the verdict table's one reader, the Rollout says
  why it is graded by direct call, and AC5 grades its three strings at this unit's commit; AC6 took
  the same treatment for `read_stderr_tail`, which had the same unnamed subject. L2: §5's perf row
  priced a SWAPPED `mktemp` as an extra one and one extra read where §4's design needs three, and
  the spec never stated the teardown, which S1 now carries. L3: both siblings' reciprocals are live
  at HEAD (`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md:106` and
  `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-28.md:97`), so the
  owes-the-line clauses are struck from both Edges bullets and from the entry above. None of that
  report's left-shift candidates is wired or cited here: only one of its eleven was ever run over
  the tree, and none was run by this fold.
  Extended by that fold's verifier, same base and rev · AC1 · one repair, which moves no
  assertion. AC1's refusal arm was written to run after "a prior successful call has left `RB_TOOK`
  non-zero", which the stub cannot deliver: `tools/unattended/unattended.sh:195` computes `RB_TOOK`
  in whole seconds from `date +%s` and a one-line stub returns inside one, so the precondition was
  met only when a call straddled a second boundary and the `RB_TOOK` reads 0 assertion otherwise
  passed on a value the branch never touched. The arm now SEEDS a non-zero sentinel before the
  refusing call, which is the same state deterministically. Two further items are reported to the
  orchestrator rather than edited here, because both need a ruling: S4's driver-wide clause has no
  observer left now that AC5 grades a helper instead of a caller, and AC5's never-answered string is
  tied to a `gates-green` sentence that names the merge bar and `$GATE_CMD`. §10 gains the reuse
  lookup the new helper owed, run for this repair on 2026-09-20; its result changes no decision.
  Extended once more on the same pass, same base and rev · §3 Edges · the `hands-off` bullet to
  `TOOL-dDerivedDocket-28` stopped citing that spec's own line number. A hand-off payload is read
  against the TARGET's text, and a citation of the target's own lines can never occur there, so the
  bullet now names what that unit carries in its words — the two-file capture its ledger WRAPS rather
  than rewrites, and the pin that would otherwise read as forbidding the split. Every backticked
  token left in the bullet occurs in that spec. The L3 reading the previous entry records is
  unchanged: the reciprocal is live at HEAD, and only the way this bullet POINTS at it moved.
- rev-2 · 2026-09-21 · §2 · §3 · §4 · §6 · §9 · the build pass, which diverged from rev-1 in six
  places and changed the spec before the code. **S6 and AC8**: the `ARMS_FLOORS` pair does not move.
  `tools/memory-tree/check-arms.py` counts `fail <n> "` call sites and this unit adds none — the
  capture refusal is an existing branch and neither new helper refuses through `fail` — so the count
  is 256 at this commit and 256 at its parent, the one-sided floor holds unchanged, and
  `.memory-tree.conf` left the write set. **S4**: the driver-wide clause is struck. Every refusal
  that quotes a bounded call's output quotes `RB_OUT`, which IS the concatenation, so quoting
  `read_stderr_tail` beside it would print the producer's stderr twice; the property S4 wanted is
  delivered by that concatenation and graded by AC3, and the helper's consumers are
  `derive_stream_verdict` and the witness units. This is the first of the two items rev-1's verifier
  reported to the orchestrator for a ruling, ruled here because this is the pass that would have
  built it. **AC5 and §4**: the second of those two. The never-answered string is DRAWN from the
  `gates-green` sentence rather than copied, because that sentence names the merge bar and
  `$GATE_CMD` and a helper with no caller knows neither; the clause that carries the meaning is kept
  verbatim. **§4 and AC5 again**: `derive_stream_verdict` enforces its precondition — asked for a
  verdict while `RB_STDOUT` holds rows it returns 1 and prints nothing, rather than reporting a
  talking producer as one of three states it is not in. **S2**: the caller set understated. Unit 3
  landed five more readers of `RB_OUT` after this spec's base — `check_lander_mode` twice,
  `check_inplace_preconditions`, `check_landing_carry` and `write_close_commit` — each printing it
  whole through the same idiom, so all eight keep their diagnosis and none is edited. **AC4**: no arm
  for it is written into this kit's suite, because a kit file names nothing outside itself by literal
  and `ASKS_CMD` is blank until unit 35; it is observed in the pass over a rebuilt fixture and its
  permanent arm is the witness units'. **AC3** gains a `permission:` line for its two verb-level
  halves, which need the driver's own fixture; its `$SPEC_TOKENS_CLI` half and the `RB_OUT` property
  all three rest on were observed in the pass. Every line citation in §1, §2, §4, §5 and §6 was re-read
  and corrected: they are this unit's own commit, except the ones that name the capture BEFORE the
  split, which name its parent and say so. §3's Edges, the Rollout and §10 keep the numbers they
  were written with — their CLAIMS were re-read and stand, including check 12's edge arm, which
  still reds a `consumes-from` at a LATER order and a `hands-off` at an EARLIER one and says nothing
  about an equal one. AC7's pinned dossier headroom was RE-MEASURED rather than re-cited: it fell
  from 93 B to 13 B between the base and this parent, which does not move this unit's verdict
  because it opens no dossier, and would have moved it for any unit that did.

  The pass ran no gate, no suite and no bar. Each new arm was observed RED against a staged break in
  a scratch copy of the driver, and AC4 over a rebuilt builds-mode fixture with the merged redirect
  restored in one branch. AC8's suite run, and AC3's two verb-level halves, are owed to the bar the
  main loop runs at VERIFYING.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a bounded runner captures a command's output"` returned
`run_bounded` in `tools/process-monitor/census.py` — a different kit's python bounded runner, which
shares the name and none of the job — plus `boundedParallel` in the workflow scripts and the
`.unattended.conf` affordance seam. Its own header line reports that `.sh` is an unscanned layer, so
the map is blind to the driver and cannot have found the seam this unit extends; the `unattended`
dossier names no second capture. The seam is therefore read from source rather than from the map:
the one `run_bounded` at `tools/unattended/unattended.sh:183`, its three callers at `:1206`, `:3283`
and `:4968`, and the extraction idiom the kit's own bound arms already use at
`tools/unattended/unattended.test.sh:5348`. No existing helper returns a bounded tail of a captured
stream, so `read_stderr_tail` is new rather than an extension.

`derive_stream_verdict` was looked up separately, after the G7 fold added it:
`python tools/codebase-map/reuse_lookup.py "a helper maps an empty capture to one of three distinct
verdict strings"` returned `derive_verdict` and `scan_verdicts` in
`tools/process-monitor/classify.py:38` and `:52`, which classify a process row against a ceiling and
a spin rate and share a name stem with this helper and nothing else, plus `derive_layer_verdict` in
`tools/codebase-map/reuse_lookup.py`. It reports the same unscanned `.sh` layer, so it is blind to
the driver here too. The discrimination this helper names exists today only inline, in the
`gates-green` breach branch (`tools/unattended/unattended.sh:3289-3291`), so it is an extraction of
one existing branch plus the row the verdict table adds, and not a second answer to a question some
other helper already answers.

Recall returned `TOOL-aReapedSpinner-17`, which measured a command substitution costing about 300s
per capture against a file redirect and is the reason the file form is kept here, and
`TOOL-aProvenReuse-6`, which records that the bound arms are wall-clock assertions and flake under
fleet load — the reason AC2 states its cost and its host condition rather than asserting a duration
silently.

Recall terms used: `run_bounded bounded capture stderr stdout DEAD PROBE witness TSV parse refusal
liveness notice waiver line timeout`

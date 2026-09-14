**Serves:** diff-review TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3

# aLeakedHandle — Tier-2 diff review, the cumulative diff landing on main

*Adversarial pass over the whole build's landing diff — three units, seventeen commits, 41 files. Node `a`, 2026-09-10. Unlike this build's two earlier rounds, the subject here is SHIPPED SOFTWARE rather than a document: every finding below was checked against the code as it stands in the worktree, and the five that could be executed were reproduced.*

**Range — ROUND 1**, the cumulative diff at `eff1b6b15081355897038b3df3b9497d94f4b069...HEAD`.

## Verdict: BLOCKED

One blocker, and it is not in the runner this build set out to repair. `tools/gate-lint/kit.toml` now declares two gate legs, and the first one's argv names a registry file that no kit ships and no intake token asks for — so `govkit apply` fails at every adopter selecting `gate-lint`, while gov's own bar stays green because the predicate that catches this class only ever runs against a target. Three artifacts in this same diff assert the opposite. One high sits behind it: the new shell scanner treats a trailing `# … <<EOF` comment on a `done` line as a real heredoc opener and reds the file, on a leg that is unguarded and runs at the push boundary. The remaining seven are four mediums and three lows, all in the ceiling-evidence path or in prose that states a count the manifest owns.

### Review shape

Raw 16 · confirmed 10 · refuted 6 · unverified 0 · precision 0.63.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. No arm of this run failed to report, so the zero counts here are positive evidence rather than an absence of it, and the finding set is complete as far as four lenses reach. This run is complete.

Precision 0.63, against 0.28 in round 2 and 0.30 in round 1, and above the ~0.5 floor §8 sets. The jump is the subject changing, not the lenses improving: a claim about running code can be executed, and six of this round's ten confirmations were settled by running something rather than by argument.

### What was reproduced rather than argued

Five of the nine findings below were re-run against the tree while writing this record, and every one behaved exactly as reported:

- `scan_file('done < "$f"   # used to be <<EOF\nx=$(git log)\n')` returns `{'loop-heredoc-sub': [(1, 'EOF')]}`, and `loop-heredoc-sub` is in `GATED` — F2.
- The same function over a heredoc whose terminator is indented two spaces returns `loop-heredoc-plain`, a near miss on the gated class — F3.
- `python tools/run-gates/derive-ceilings.py --report` prints `memory-hygiene self-test  900.5  2  900  -0  900  UNDER` — F5.
- `govkit.py plan` against a bare fixture target reports `SILENT [gate-lint] leg '…' names memory/project/substitution-fed-loops.txt, which no kit ships here` — F1.
- `tools/gate-legs.json` parses to 106 legs, every one carrying an integer ceiling — F8, whose row says 104.

`derive-ceilings.py --check` is GREEN on this tree today and no leg is red, so nothing here is a live bar failure. F1 is a break at a boundary this repo's own bar cannot see.

### Consolidation

The ten confirmed findings describe **nine distinct defects**. Two merges, both across lenses that read the same lines: raw 7 and raw 16 are one row in `memory/backlog/TOOL.md`, and raw 8 is the second half of raw 15 — the `CEILING_WINDOW_S` sizing comment — which is carried here as its own row because its fix is independent of the admission-clamp half.

Severities are the ones adjudicated HERE and differ from the raw labels in two places, both stated in the row. **Adjudicated totals: 1 blocker, 1 high, 4 mediums, 3 lows.**

| # | Sev | Address | Defect | Raw ids |
|---|-----|---------|--------|---------|
| F1 | BLOCKER | `tools/gate-lint/kit.toml:42` | The new leg's argv names a registry no kit ships and no token asks for, so `apply` exits 1 at every adopter | 10 |
| F2 | HIGH | `tools/gate-lint/sh_hygiene.py:135` | A trailing `# … <<TAG` comment on a `done` line is parsed as a heredoc opener and reds an innocent file | 5 |
| F3 | MEDIUM | `tools/gate-lint/sh_hygiene.py:106` | `probe.strip() == tag` ends a body at an indented terminator, so the gated class is missed | 4 |
| F4 | MEDIUM | `tools/run-gates/derive-ceilings.py:240` | `--write --reset <leg>` is inert while the run that produced the reading is still retained | 11 |
| F5 | MEDIUM | `tools/run-gates/derive-ceilings.py:205` | `cmd_report` still labels a REACHED reading `UNDER` and offers a `need` target | 14 |
| F6 | MEDIUM | `tools/run-gates/derive-ceilings.py:157` | An admitted failing row enters the monotone file at raw elapsed rather than clamped to its ceiling | 15 |
| F7 | LOW | `tools/run-gates/derive-ceilings.py:44` | The window's sizing comment says 0.481 s where this same diff records 12 s against a 2 s bound | 8, 15 |
| F8 | LOW | `memory/backlog/TOOL.md:6` | `all 104 legs` against a manifest holding 106, stale at the instant it was committed | 7, 16 |
| F9 | LOW | `memory/project/substitution-fed-loops.txt:18` | The paragraph declaring that the count is the rows writes two numbers, one of which is not the row count | 9 |

Two gradings moved. **Raw 10 is promoted from high to BLOCKER**, because it is a functional break in shipped product behaviour rather than a defect in what a record says: `apply` exits 1, the leg is withheld, the receipt records no coverage, and the kit.toml comment landing beside it declares a permanent recorded gap discharged. **Raw 5 is promoted from medium to HIGH**, because the leg it defects is `subject = "repo"` with no guard and therefore runs on every bar and inside `.githooks/pre-push` — a false RED there blocks every push on this repo with no clean remedy, and the registry cannot absorb it.

---

## What this round found, in four sentences

**The units did their jobs and the packaging did not.** All three mechanisms work: the pipe deadlock is closed, a timed-out leg now contributes evidence, and a killed leg reports its own seconds. Every finding below is in the machinery bolted around those mechanisms — a kit descriptor, a scanner's line parser, a second reader of one artifact, and four counts written in prose beside the sources that own them.

**The blocker is the one place nothing here could have caught it.** `silenced_legs` exists precisely to refuse a leg whose argv names a path the target does not hold, and its own docstring says it was written after gov handed an adopter exactly this. It runs from `cmd_plan` and `cmd_apply` and never from `selfcheck`, so a defect it was built to catch, introduced into gov's own descriptor, is invisible on gov's own bar. That is the gate-shaped hole this round is really reporting, and F1's left-shift is the fix for the class rather than the instance.

**The scanner shipped without its false-positive corpus.** §7 asks for a candidate predicate to be run over the real tree with hits AND near-misses printed. The hits were swept — the registry's nineteen rows are that sweep — and the near-misses were not, which is why F2 and F3 are both first found here rather than by the build. Neither is live in the tree today; both are one ordinary future edit away.

**The prose findings are one class, three times.** F7, F8 and F9 are all a number written beside the source that owns it, and one of them was already stale when it was typed. §7 states the rule and this build broke it in three carriers, one of which is the registry header that states the rule in its own second sentence.

---

## F1 — BLOCKER — the new gate leg names a file no adopter has

**`tools/gate-lint/kit.toml:42`**

```toml
argv = ["python3", "{kit}/sh_hygiene.py", "{memory_root}/project/substitution-fed-loops.txt"]
```

`{memory_root}` is in govkit's `derived` set (`tools/govkit/govkit.py:8159`), so `intake` never asks an operator for it and it resolves unconditionally to `memory/project/substitution-fed-loops.txt`. No `[[files]]` rule in any kit writes anything under `memory/project` — the only `{memory_root}` destinations across every descriptor are `HYGIENE.md`, `TEMPLATE-SPEC.md` and four files under `guides/`. So the leg names a file that arrives at no target by any route.

`silenced_legs` (`tools/govkit/govkit.py:2257`) is the predicate for exactly this, and it fires. Against a fixture target holding nothing but a `deploy.toml` and one `.sh`, `govkit.py plan --target <fixture> --kits gate-lint` reports:

```
SILENT [gate-lint] leg 'shell hygiene (a loop fed by a command substitution)' names
memory/project/substitution-fed-loops.txt, which no kit ships here
```

In `cmd_apply` every such hit lands in `_silenced_found`, and `govkit.py:5182` turns each one into `r.fail`. The consequence at every target selecting `gate-lint`: the leg is withheld from the emitted manifest (or listed under WITHHELD in `.governance/outbox/gate-legs.md`), `apply` exits 1, and the receipt records no coverage for it. Even if it were emitted, `sh_hygiene.py:339` would exit 2 — `no registry at …` — on that adopter's first bar.

Three artifacts in this same diff say the opposite. `kit.toml:26` declares the `gate-lint-leg-wiring` hole discharged because "the kit now declares legs, and a target that copies it receives them". `tools/gate-legs.json`'s sibling README says "an adopter points it at their own list", which the fixed path forbids. `memory/map/features/gate-lint.md` repeats it. A hole that carried `discharge = { command = ["bash", "-c", "exit 1"] }` — undischargeable by construction, recorded honestly — is now marked discharged by a change that does not discharge it.

This is not a new class here. `tools/govkit/registry.toml` carries `[[exempt_leg]]` rows for `kickoff engine size <=18KiB` and `build-method size` whose `why` records that `DEPL-dCarriedReceipt-6` withdrew those legs for naming an engine gov never ships, and `selftest.py:8693` states outright that leaving such a row in a descriptor made "every adopter apply exit 1 with one problem per withheld suite". Neither `gate-lint` leg is in that exempt list.

**Fix.** Take the pattern the other data-file legs already use. Either make the registry a NON-derived intake token — `{sh_hygiene_registry}`, the way `check-microformats` takes `{playbook_path}` and `kickoff-manifest` takes `{manifest_path}` — so `needed_answers` asks and the operator supplies a path their tree actually holds; or ship a seed registry inside the kit under `{prefix}`/`{kit}`, the way `check-agent-cap-restatement` ships `tools/agent-cap-restatement-waivers.txt`. Then correct all three claims: the `kit.toml` discharge comment, the README's "an adopter points it at their own list", and the dossier's matching sentence.

**Left-shift.** Run `silenced_legs` from `selfcheck`, against a synthetic bare target built in a `mktemp -d` holding only a minimal `deploy.toml` — the same fixture this review used. That aims the existing predicate at gov's own descriptors, where the defect is authored, instead of only at the adopter who receives them. It is the one check that would have turned this from a shipped break into a red line during the build, and it costs one fixture and one call to a function that already exists. Stage the break to observe it RED before landing, per §7: this finding IS the staged break, and the leg should red on the tree as it stands.

---

## F2 — HIGH — a comment mentioning a heredoc becomes a heredoc

**`tools/gate-lint/sh_hygiene.py:135`**

`scan_file` skips a line only when `line.lstrip().startswith("#")`. A line that is code with a trailing comment is scanned whole, so `<<TAG` inside that comment is matched by `HEREDOC` and treated as a real opener. `extract_heredoc_body` then swallows the remainder of the file as the body, `check_substitution` finds a substitution in it, and the site is reported under a GATED key.

Reproduced against the shipped module. This two-line file:

```sh
done < "$f"   # used to be <<EOF
x=$(git log)
```

returns `{'loop-heredoc-sub': [(1, 'EOF')]}`. The here-string variant — `done < "$f"   # see <<<"$(x)"` — returns `loop-herestring-sub`. Both keys are in `GATED`.

The leg is unguarded and authoritative. `tools/gate-legs.json` declares `shell hygiene (a loop fed by a command substitution)` with `chunk = product`, `subject = repo` and no guard, deliberately and correctly, because no subset of paths bounds a scan of every tracked `*.sh`. So it runs on every bar and inside `.githooks/pre-push`, which runs the full bar and blocks a red push. One comment of that shape in any tracked shell file reds an innocent file and blocks every push on the repo.

The registry cannot absorb it either: `read_registry` enforces set equality in both directions on `(path, delimiter)`, so the remedies available to whoever hits it are to edit the comment, or to declare a registry row keyed on a delimiter that is not a real heredoc. A gate whose steady state is red gets bypassed — the registry's own header says this repo has already paid two cycles for one.

The module's `WHAT THIS DOES NOT CHECK` block names quoted delimiters, two heredocs on one line, and line continuations. All three are MISSES. It names no false positive, and neither does the dossier's Gaps section.

Corroborating, and the reason this reads as a pattern rather than an accident: `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` records that the sibling scan in `tools/unattended/unattended.test.sh` was deliberately "scoped to code lines so the comment documenting the fix does not red it". The same class, already hit once in this kit, unfixed here — in the scanner that generalised it.

**Fix.** Cut an unquoted trailing comment before classifying: strip from the first `#` that is at line start or preceded by whitespace and sits outside single and double quotes, then run `DONE`, `PROCESS_SUB`, `HERESTRING` and `HEREDOC` over the remainder.

**Left-shift.** Two `--selftest` arms, not one: a false-positive arm asserting that a `done` line carrying a trailing `# <<EOF` produces NO hit, and a control arm asserting the same line without the comment still does. A false-positive arm alone can pass by the scanner going dark, which is the shape §7 warns about; the control is what proves it did not.

---

## F3 — MEDIUM — an indented terminator ends the body early, and the gated class is missed

**`tools/gate-lint/sh_hygiene.py:106`**

```python
probe = lines[i].lstrip("\t") if dash else lines[i]
if probe.strip() == tag:
```

For an unquoted `<<TAG` heredoc, bash ends the body only on a line that is EXACTLY the tag at column 0; tabs are stripped only for `<<-`. `.strip()` accepts an indented or trailing-whitespace terminator that bash does not, so the scanner's body ends where bash's does not, and the scanner then resumes at the fake terminator and grades the remaining true body as code.

Reproduced against the shipped module. This fixture:

```sh
while read -r x; do :; done <<EOF
  EOF
$(git log)
EOF
```

is a genuine loop-heredoc-substitution site — bash's body holds the `$(git log)` — and `scan_file` returns `loop-heredoc-plain`, a NEAR MISS on the gated class. The leg passes green on the exact deadlock class it exists to refuse.

Two things cap the severity, and both belong in whatever fix lands. All 105 tracked `*.sh` were swept with a CR-tolerant strict terminator: ZERO live disagreements, so nothing is missed in the tree today. And the `.strip()` is load-bearing for a CRLF working copy — a naive column-0 exact match flips three innocent sites in `tools/check-wiring.sh` (547, 571, 586) into GATED hits on this checkout, so the obvious fix is itself a false-positive generator.

**Fix.** Compare exactly, keeping only the CR tolerance the strip was actually buying:

```python
probe = lines[i].lstrip("\t") if dash else lines[i]
if probe.rstrip("\r") == tag:
```

If that is not taken, the honest alternative is a written entry in the module's own `WHAT THIS DOES NOT CHECK` list — a gate's header stating what it does not check is §7's rule, and the module's own text says an unstated blind spot is how the sibling scanner got its first one.

**Left-shift.** A `--selftest` arm whose fixture indents the terminator and asserts the site lands in `loop-heredoc-sub`, plus the CRLF control — the same fixture with `\r\n` line endings must still classify identically, which pins the `rstrip("\r")` against a future tidy-up. One optional extra, if a cheap leg is wanted for the CLASS rather than these two instances: a differential arm that scans every tracked `*.sh` with a strict terminator and asserts zero disagreement against the shipped parser, which turns "I swept it by hand once" into something that stays true.

---

## F4 — MEDIUM — `--reset` is inert in exactly the window it exists for

**`tools/run-gates/derive-ceilings.py:240`**

`read_runs` now admits a failing row inside the window, and `cmd_write` re-derives `mx` from the same retained `.leg` files on every invocation:

```python
if prev and prev[0] >= mx and name not in (args.reset or []):
    rows[name] = prev; held += 1
else:
    rows[name] = (mx, len(vals), node, date)
```

`--reset` bypasses the monotone hold and nothing else. While the run that produced the offending reading is still retained, `mx` is unchanged and the reset writes the same value straight back. Proved on a fixture with ceiling 100 and rows `fail 100.4` / `ok 20.0`: `--write` wrote `leg-a 100.4`, and `--write --reset leg-a` wrote `leg-a 100.4` again.

`GATE_RUN_KEEP` defaults to 5 (`run-gates.sh:1057`), so the row is pinned for the next five bars. Before this unit a failing run produced no row at all, so the hazard is new — and the docstring at lines 133-135 rests the whole mitigation of the monotone-floor hazard on this escape: "lowering one is `--write --reset <leg>`, which exists for exactly this". The operator who follows that sentence sees the ceiling-evidence leg stay red with the REACHED message, and has no legal move except raising the ceiling — which the same message tells them not to do — or deleting a run directory nobody documents, while the evidence file's own header says "Do not hand-edit".

**Fix.** Make `--reset <leg>` reset: for a named leg, drop its non-`ok` rows from the admitted set for that run (or ignore its retained `gate-run` rows), so the reset re-derives from `ok` readings alone. If that is not wanted, amend the docstring to name the real remedy — wait for `GATE_RUN_KEEP` rotation — instead of an escape that does nothing.

**Left-shift.** An arm in `run-gates.evidence.test.sh` that writes a failing row, runs `--write --reset <leg>` with the run still retained, and asserts the value LOWERED. It fails today, which is the point: §7's rule is that a new gate is not landed until its failing case has been observed, and this arm makes the docstring's promise falsifiable instead of decorative.

---

## F5 — MEDIUM — one reading, two verdicts, and the wrong one is on the human path

**`tools/run-gates/derive-ceilings.py:205`**

`cmd_check` gained a REACHED branch that deliberately suppresses the headroom arithmetic for a ceiling-reaching reading, because "the headroom arithmetic reads as an invitation to size a new ceiling from the evidenced maximum". `cmd_report` — the table an operator actually sizes a ceiling from — was not amended. Its state ladder is still `no-ceiling` / `UNDER` / `ok` on `over < need`.

Live on this tree:

```
memory-hygiene self-test	900.5	2	900	-0	900	UNDER
```

Two things are wrong in one row. `UNDER` plus `need 900` invites sizing the new ceiling at 900.5 + 900 from a reading the sibling reader calls a LOWER BOUND on the work. And `'%.0f' % -0.481` renders as `-0`, so a BREACHED ceiling displays as zero headroom.

The raise-or-optimise decision this build deliberately parked with the owner is the decision this table feeds. The machine-facing reader is right and the human-facing one is wrong, which is the wrong way round.

**Fix.** In `cmd_report`, ahead of the `over < need` branch:

```python
if isinstance(ceiling, int) and mx >= ceiling:
    state = "REACHED"
```

and print `-` for `have` and `need` on that row, so no sizing target is offered for a lower-bound reading. Same condition as `cmd_check:297`, derived from the same two values, so the two readers cannot disagree.

**Left-shift.** A parity arm rather than a per-reader assertion: feed one at-ceiling reading and assert that `--report` and `--check` agree on it — no `need` target on a row `--check` calls REACHED. The class is `amendment-leaves-its-other-half-standing`, and the general form is that two readers of one artifact get a parity arm, not two separate ones.

---

## F6 — MEDIUM — a killed leg's teardown becomes permanent evidence

**`tools/run-gates/derive-ceilings.py:157`**

```python
per.setdefault(p[0], []).append(secs)
```

An admitted failing row is recorded at its raw elapsed seconds. Only the CEILING is a provable lower bound on the work — the leg was killed there — and the excess is kill-path and teardown overhead. `run-gates.sh:1488` says so in this repo's own words: "the elapsed value on that path is the ceiling plus kill-path overhead". The docstring nonetheless asserts of the recorded number that "its seconds are a LOWER BOUND on the work", which is true of the ceiling and false of the overshoot.

`ceiling-evidence.txt` is MONOTONE and the required margin is `max(120, 1.0 × max)`, so an inflated reading permanently raises the demanded ceiling and only `--write --reset` can lower it — which F4 shows is inert while the run is retained. Concretely, at the 10 s overshoot this build itself recorded, a 60 s-ceiling leg (`codebase-map gate coverage` is one) killed at its bound records ~70 s, and `--check` then demands 190 s of ceiling where the evidence supports 180.

**Fix.** Clamp on admission. In `read_runs`, for a non-`ok` row inside the window, append `min(secs, ceiling)` rather than `secs`. That is exactly the property the docstring already claims, and it drops the teardown noise without touching the admission rule.

**Left-shift.** An arm asserting that an admitted rc=124 row enters at exactly its ceiling rather than at raw elapsed — fixture with a ceiling of 2 and a recorded 12 s, asserting `2.0` in the written artifact. It pins the docstring's claim to the code, and it fails today.

---

## F7 — LOW — two answers to one question, 300 lines apart, in one build

**`tools/run-gates/derive-ceilings.py:44`** against **`tools/run-gates/run-gates.sh:1488`**

`CEILING_WINDOW_S` is written as `5 + 30` and defended by a comment: "Sized against what this repo has recorded rather than against comfort: the worst overshoot on record is 0.481 s". `run-gates.sh:1488`, edited in this same diff, records the same quantity — elapsed above the declared bound on a bounded kill — at "12 s against a 2 s bound under load". A 10 s overshoot, 20x the figure the window is defended against.

The different-populations defence fails at the primary source. `run-gates.test.sh:129` states the measurement and adds that "it does NOT shrink when the sleeper does" — a fixed cost that applies to a 900 s leg exactly as to a 2 s one. So the constant is right (35 covers 10) and its only written justification understates the observed worst by 20x, in the comment that decides which failing readings enter a monotone tracked artifact. The comment does argue against tightening, which caps the damage; but "sized against what this repo has recorded" is the load-bearing sentence and the repo recorded 10 s.

**Fix.** Reconcile at the source. State the 0.481 s figure as the worst overshoot recorded against a 900 s ceiling, and cite the 12 s-against-2 s reading beside it as the worst RELATIVE overshoot, so the 30 s teardown allowance is defended against the larger of the two.

**Left-shift.** This repo already has the machinery for a value that must agree across carriers: `tools/check-playbook-parity.sh` machine-compares pinned values against the sources that own them. Either add this pair to it, or — lazier and preferred under §6 — delete the figure from one carrier and point at the other, so there is one text and nothing to compare.

---

## F8 — LOW — a count that was stale at the instant it was committed

**`memory/backlog/TOOL.md:6`**

`TOOL-aLeakedHandle-5` states "MEASURED 2026-09-10 … all 104 legs in `tools/gate-legs.json` declare a ceiling, so the population this branch would serve is EMPTY today".

`git show 013b1af9:tools/gate-legs.json` parses to 104 legs. The working tree parses to 106 — the two added by this same build, `shell hygiene (a loop fed by a command substitution)` and `shell-hygiene selftest`. And `git show 9f93ac71:tools/gate-legs.json`, the very commit that wrote this row, already held 106. So the number was wrong when it was typed, not merely overtaken later, which drains the usual "MEASURED `<date>`" defence.

The row's substance survives: all 106 declare an integer ceiling, verified, so the deferred rc=137 branch would still ship dead. The damage is a false stale-signal in a record that will be read when that branch is picked up — a future session comparing 104 against the manifest has to re-derive whether the premise still holds.

**Fix.** State the property and name the source: "every leg in `tools/gate-legs.json` declares a ceiling, measured 2026-09-10 — count them there". The same edit the merge-bar section of `AGENTS.md` already applies to leg counts.

**Left-shift.** One drift-audit signal covering this and F9 together: flag any tracked record whose prose writes a numeral within a sentence naming `tools/gate-legs.json` or a `memory/project/*.txt` registry, and compare it to that source's own length. One probe, two findings, and it fits the tier-0 audit that already exists to ask whether this repo's records still describe it. A dedicated gate for a numeral in prose would be over-built for the return.

---

## F9 — LOW — the paragraph that forbids a number writes two

**`memory/project/substitution-fed-loops.txt:18`**

Line 15 declares "the count is the rows, never a number written in this paragraph". Line 18, inside that same paragraph, writes two: "nineteen edits across six files". Measured: the file holds 18 data rows, whose count column sums to 19 sites across 6 distinct files. So `nineteen` is a SITE count in a paragraph whose preceding sentence says the count is the ROW count — a reader who takes the header at its word gets 19 for a quantity that is 18.

Nothing gates the header: `read_registry` skips every `#` line. The registry is shrink-only, so draining any single site falsifies `nineteen` and possibly `six`. And the scanner already prints the pair correctly — "N declared site(s) in M row(s)" at `sh_hygiene.py:364` — with a comment insisting the two are different numbers, which the header muddles.

**Fix.** Delete the numerals from line 18: "The rest are carried across two kits and the tool root — run the scanner for the site and row counts, which it derives and prints on every run." That leaves the paragraph consistent with the rule it states one line above.

**Left-shift.** Covered by F8's single drift-audit probe. No second mechanism.

---

## What was refuted, and why it is worth one line

Six raw findings did not survive the skeptic. The pattern in them is worth recording for whoever scopes the next round over this area: they were claims about the RUNNER's new behaviour argued from the diff rather than from a run, and each dissolved when the code was executed. The three findings above that concern `derive-ceilings.py` survived for the opposite reason — each was reproduced. Precision 0.63 over a fresh write path is comfortable, and a round 2 scoped to the repairs alone would be the cheaper shape than a re-sweep.

## The gate-shaped summary

Three of the nine defects would have been caught by a check this repo already owns, aimed one step differently:

- F1 — `silenced_legs` exists and is never pointed at gov's own descriptors.
- F2, F3 — §7's candidate-predicate dry run was performed for HITS and not for NEAR-MISSES, which is the half that catches a predicate redding innocent files.
- F5 — a second reader of an artifact was amended on one side, with no parity arm between them.

The other six are the counts-in-prose class (F7, F8, F9) and the new admission path's own edges (F4, F6). Every one of them has a suggested arm above, and four of those arms fail on the tree as it stands, which is the state §7 asks a new gate to be observed in before it lands.

**Serves:** diff-review TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2 TOOL-aLeakedHandle-3

# aLeakedHandle — Tier-2 diff review, round 2, the cumulative diff landing on main

*Adversarial pass over the same landing diff after the three fix commits that answer round 1's closing review. Node `a`, 2026-09-10. The subject is shipped software, so every finding below was checked against the worktree and four of the five were reproduced by running something rather than by argument.*

**Range — ROUND 2**, the cumulative diff at `9f93ac713bf854aa98859bceb81c2a95a07fbf99...HEAD` — three commits, 18 files: `77bb3530` (F4 F5 F6 F7), `f1a05f8e` (F1 F2 F3), `2bc5c0b0` (F8 F9).

## Verdict: BLOCKED

One blocker and one high, and both are the same shape: a round-1 finding whose fix does not close it, with an artifact in this same diff asserting that it does. The blocker is `--reset`, which round 1 reported as inert for the whole `GATE_RUN_KEEP` window; the fix moved the inertness one step later rather than removing it, and the new test arm added beside it asserts a row's PRESENCE where it needed to assert its VALUE, so the re-raise happens inside a green arm. The high is F1's replacement selfcheck arm, which grades 21 of gov's 26 descriptors while printing a count over all 26 — F1's own class, an under-derived population carrying a confident derived count, reproduced inside F1's own fix. The remaining three are one medium and two lows in the same ceiling-evidence path. Nothing here is red on the bar today.

### Review shape

Raw 15 · confirmed 9 · refuted 6 · unverified 0 · precision 0.60.

**Run integrity — all clean.** Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every arm of this run reported, so the zero counts above are positive evidence rather than an absence of it, and the finding set is complete as far as four lenses reach. This run is complete.

Precision 0.60 against round 1's 0.63 on the same area. That is a flat result on a narrower and freshly-hardened surface, which §8 predicts: a round scoped to repairs manufactures more refuted noise than a sweep over a fresh write path, and the six refusals were again claims argued from the diff rather than from a run.

### What was reproduced rather than argued

Four of the five defects were re-run against the tree or an isolated fixture while writing this record.

- `--reset` re-raise (D1): fixture with `LEGA` at ceiling 100 holding `fail 124 100.4` and `ok 20.0`. `--write` → 100.0; `--write --reset LEGA` → 20.0 with `1 lowered by --reset`; a plain `--write` immediately after → **100.0 again**, printing `1 raised`.
- No-op reset mislabel (D4): running `--write --reset LEGA` twice leaves the row at 20.0 and the second run prints `1 raised, 0 lowered by --reset`.
- DEAD-PROBE preemption (D3): fixture with one leg whose only reading is `fail 124 14.0` against a ceiling of 10. `--write` stores 10.0; `--write --reset killed-leg` exits **2** with `DEAD PROBE — no readings to write` and rewrites nothing; the stale row survives.
- Population split (D2): loading `govkit.py` against `registry.toml` gives 26 entries, `derive_install_order(all_kits(descs), descs)` gives 21, the five excluded are exactly `check-agent-cap-restatement`, `check-install-prefix`, `check-line-length`, `check-microformats`, `check-placeholders`, and they carry 9 gate legs and 20 argv elements. `_leg_argv` sums 133; the selection covers 113.
- The proposed one-line fix for D2 was also run: `derive_install_order(sorted(descs), descs)` over all 26 yields **0 hits**, so widening lands green today.

**What I did not reproduce.** D3's report also claims `--check` stays RED after the failed reset. My fixture reds `--check` for an unrelated reason (no `ceiling-margin.txt`), so I am carrying the exit-2-and-stale-row half as reproduced and the `--check` half as read-from-code only. D5 was verified by reading its two cited sources, not by running anything — there is nothing to run.

### Consolidation

The nine confirmed findings describe **five distinct defects**. Two merges, both large and both across lenses reading the same lines: raw 1, 5, 9 and 14 are one defect (the selfcheck arm's population), and raw 4 and 8 are one defect (the reset's lifetime). The run reported 0 duplicates discarded, which is correct — these are four and two independent arrivals at the same lines, not repeats of one report.

Severities are the ones adjudicated HERE. **Adjudicated totals: 1 blocker, 1 high, 1 medium, 2 lows.**

| # | Sev | Address | Defect | Raw ids |
|---|-----|---------|--------|---------|
| D1 | BLOCKER | `tools/run-gates/derive-ceilings.py:179` | `--reset` lowers a row for one invocation; the next plain `--write` re-raises it from the same retained reading | 4, 8 |
| D2 | HIGH | `tools/govkit/govkit.py:1852` | The replacement `gate legs` arm grades 21 of 26 descriptors and prints a count over all 26 | 1, 5, 9, 14 |
| D3 | MEDIUM | `tools/run-gates/derive-ceilings.py:273` | The DEAD-PROBE return fires before the documented reset-drop path, so the drop never runs and the operator is misdiagnosed | 2 |
| D4 | LOW | `tools/run-gates/derive-ceilings.py:283` | A reset that re-derives the identical value is counted and printed as `1 raised` | 12 |
| D5 | LOW | `tools/run-gates/derive-ceilings.py:52` | F7's replacement wording says "single-digit-seconds" of two sources that both record a 10 s overshoot | 15 |

One grading moved from its raw label. **Raw 4 and 8 are promoted from high to BLOCKER.** Round 1 graded the underlying defect MEDIUM, and on its own merits it still would be — an operator escape hatch that does not stick. What promotes it is what landed beside it: the docstring at `derive-ceilings.py:152`, the artifact header at line 313, and a new test arm at `run-gates.evidence.test.sh:791` all assert the escape now works, and the arm asserts it in the one way that cannot see the failure. A round whose entire purpose is discharging round 1's findings must not land a false discharge guarded by a blind arm — that is §7's could-not-fail shape, and it is worse than the untouched defect was.

---

## What this round found, in three sentences

**Two of the three fix commits fixed their findings. `f1a05f8e` closed F1, F2 and F3 — `silenced_legs` now runs inside `selfcheck`, the registry ships, and the scanner's line parser was rewritten — and `2bc5c0b0` closed F8 and F9 by deleting the numerals. `77bb3530` closed F5 and F6, and left F4 and F7 standing in smaller form.**

**Both surviving defects are the same failure mode, and it is this build's own recurring class: the fix was written, the claim that it worked was written beside it, and nothing was pointed at the claim.** D1's arm asserts a row exists rather than what it says; D2's arm prints a population it never visited; D5's comment cites two sources and then paraphrases a magnitude neither of them supports.

**Nothing here is red today.** `derive-ceilings.py --check` is green on this tree, `govkit selfcheck` exits 0, and widening D2's selection to all 26 descriptors also yields 0 hits. Every finding below is a latent hole or a false statement in a record, not a broken bar.

---

## D1 — BLOCKER — `--reset` lowers the row for exactly one invocation

**`tools/run-gates/derive-ceilings.py:179`** (the filter), **`:283`** (the hold bypass), **`:152-160`** (the docstring that claims otherwise), **`:313`** (the artifact header), **`tools/run-gates/run-gates.evidence.test.sh:791-800`** (the blind arm).

`reset` is a per-invocation argument. `read_runs` consumes it at line 179 to drop the named leg's non-`ok` rows, and it is persisted nowhere. The `.leg` file that holds the killed reading stays in the `GATE_RUN_KEEP` window, so the very next ordinary `--write` re-admits that reading through the clamp-and-window rule, `max(vals)` returns it, and the monotone hold restores the floor the operator just cleared.

Reproduced on an isolated fixture — `LEGA` at ceiling 100 with rows `fail 124 100.4` and `ok 20.0`:

```
--write                    → LEGA 100.0   (0 raised, 0 lowered)
--write --reset LEGA       → LEGA  20.0   (0 raised, 1 lowered by --reset)
--write                    → LEGA 100.0   (1 raised, 0 lowered)
```

Round 1's F4 said `--reset` was inert for the whole retention window. This fix moved the inertness from "the whole window" to "until the next `--write`" — which is the next bar on that node, five bars away at `GATE_RUN_KEEP=5` in the best case. The docstring rejects exactly that outcome in its own words, saying the pre-fix behaviour was unacceptable because it left the escape inert "for the whole `GATE_RUN_KEEP` window ... which is precisely the window an operator reaches for it in", and the tracked artifact's header states flatly that `--reset <leg>` lowers a row "and that is a decision somebody made". The decision is reversed by a line reading `1 raised`.

The drop path has the identical hole: `--reset LEGB` where `LEGB` has only a killed reading drops the row, and the next plain `--write` re-derives `LEGB` at 2.0 from that same killed reading — not "once the window holds a finished run", as the comment at line 289 says.

§5 of the spec rests the entire mitigation of the monotone-floor hazard on this escape.

**Fix.** Make the discard outlive the invocation. The laziest version: in `cmd_write`, when `reset` is non-empty, delete the named leg's non-`ok` rows from the retained `<git-dir>/gate-run/*/*.leg` files. They are untracked scratch, and removing them is what "somebody chose it" actually means. If the run files must stay intact, record the reset (leg plus the newest run directory at reset time) in a sibling `<git-dir>/gate-run/reset.txt` and have `read_runs` skip that leg's non-`ok` rows from runs at or below the marker, so the discard expires with the reading rather than with the process.

**Left-shift.** Change the control at `run-gates.evidence.test.sh:792-794` from a presence check to a VALUE check: after the reset, run a plain `--write` and require `at-ceiling`'s row to still read the reset value. The arm as written runs exactly that ordinary `--write` and then asks only whether a row exists, so today it certifies the re-raise. Do the same for the drop arm at line 795: after the drop, one more ordinary `--write` must not restore `kill-overhead` from its killed reading. Stage the break and confirm both RED before wiring — §7 does not consider a gate landed until its failing case has been observed, and this pair fails on the tree as it stands.

---

## D2 — HIGH — the arm that replaced F1 grades 21 of 26 descriptors and counts 26

**`tools/govkit/govkit.py:1852`** (the selection), **`:1859`** (the count), **`:1869`** (the note), **`memory/map/features/gate-lint.md:63`** (the dossier restating it), **`tools/govkit/selftest.py:8284`** (the guard weakened in the same commit).

`_bare_sel = derive_install_order(all_kits(descs), descs)`, and `all_kits` filters on `selectable != "conditional"` at line 484. `silenced_legs` iterates `for eid in selection` only. Measured on this tree: 26 registry entries in, 21 out, and the five dropped — `check-agent-cap-restatement`, `check-install-prefix`, `check-line-length`, `check-microformats`, `check-placeholders` — carry 9 gate legs and 20 argv elements between them, including `{prefix}/agent-cap-restatement-waivers.txt`, which is a data file a leg reads. That is F1's shape exactly.

Meanwhile `_leg_argv` at line 1859 sums argv over `descs.values()`, i.e. all 26, so the note prints `gate legs: 133 argv element(s) resolved against a bare target` for a population of 113, of which fewer still reach the `have` join (the rest are skipped as non-paths or unresolved intake tokens). The dossier at `gate-lint.md:63` says the check "now resolves every one against a bare target". Neither statement is true.

The excluded entries are genuinely installable. `resolve_selection`'s `kits` mode validates against `descs`, not `all_kits`, so `govkit apply --kits check-microformats` installs one and emits its legs ungraded. A leg added to one of those five naming a path no rule ships would pass gov's selfcheck and surface as `apply` exiting 1 at the adopter — which is verbatim the harm the arm's own comment says it exists to prevent.

No live hit: I ran `silenced_legs` over all 26 entries with `have` derived from the same widened selection and got 0 hits, with no new false positives. This is a coverage hole plus a false derived count, not a break.

The guard that would have caught the drift was loosened in the same commit. `selftest.py:8284` now asserts only the substring `"· 0 naming a path no rule produces"`, so the number in that note is not gated by anything.

**Fix.** One line: `_bare_sel = derive_install_order(sorted(descs), descs)`. Verified to yield 0 hits over all 26 on this tree, so it lands green, and the two documented process-monitor withholds stay green because `_bare_have` is taken at every kind. If the exclusion is deliberate instead, then `_leg_argv` must be summed over `_bare_sel` and the note must name the ungraded entries and why. Either way, correct `memory/map/features/gate-lint.md:63` in the same commit — and drop "every one", since two `{manifest_path}`/`{gate_file}` elements are still deliberately left to `apply`'s refusal.

**Left-shift.** Two arms, both cheap. First, restore a numeric pin in `selftest.py:8284` so the disclosure is itself gated — a count nothing asserts is a count that drifts silently, which is what happened here. Second, and this is the one that gates the CLASS rather than the instance: assert inside `selfcheck` that the graded selection covers every registry entry (`len(_bare_sel) == len(descs)`), so a future `selectable = "conditional"` entry cannot fall out of the grading without redding. Stage a fake conditional entry to see it RED before wiring.

---

## D3 — MEDIUM — the DEAD-PROBE return preempts the reset's own drop path

**`tools/run-gates/derive-ceilings.py:271-274`** (the early return), **`:299-302`** (the unreachable drop), **`:152-160`** (the docstring promising the drop).

`cmd_write` reads `runs = read_runs(gd, read_legs(root), reset)` and returns 2 on an empty result. `read_runs` has already dropped every non-`ok` row for a reset leg, so a leg whose only retained readings are the killed ones contributes nothing — and if it is the only leg with readings at all, `runs` is empty and the documented drop path forty lines below never executes.

Reproduced: one leg `killed-leg`, ceiling 10, a single `fail 124 14.0` reading. `--write` stores 10.0. `--write --reset killed-leg` exits 2 with `DEAD PROBE — no readings to write` and rewrites nothing; the stale row survives. There ARE readings — the reset excluded them — so the message misdiagnoses the state, which is this build's own "a wrong diagnosis is worse than no diagnosis" class turned on itself.

Reachable without contrivance: `GATE_LEGS` overrides the manifest at `run-gates.sh:91`, so a one-leg bar is producible; leg guards scope a run down to a handful; and the plain case is resetting every leg that currently has a retained reading.

The new arm cannot see it — its fixture keeps `at-ceiling` with an `ok` row, so `runs` is never empty there.

**Fix.** Split the emptiness question in two: read the runs once WITHOUT `reset`, DEAD-PROBE only if that is empty, then apply the reset filter and let the drop path run.

**Left-shift.** An arm whose fixture makes the reset leg the ONLY leg with readings, asserting exit 0 and the row dropped. Confirm it RED against the current code before wiring — it fails today.

---

## D4 — LOW — a reset that changes nothing prints `1 raised`

**`tools/run-gates/derive-ceilings.py:283`.**

The hold condition is `if prev and prev[0] >= mx and name not in reset`. For a reset leg whose re-derived max EQUALS the stored one, the `name not in reset` clause forces the else branch, where `mx < prev[0]` is false and `elif prev` counts it as raised. Without `--reset` the same equal-value case lands in `held`, so the mislabel is specific to reset legs.

Reproduced: running `--write --reset LEGA` twice leaves the row at 20.0, and the second run prints `1 raised, 0 lowered by --reset`. That summary line is the only feedback `--write` gives, and re-running the reset is the most natural gesture an operator makes when the first one appears not to have stuck — which, per D1, it did not. Artifact bytes are correct and `--check` is unaffected, hence low.

**Fix.** Tally on actual movement: `lowered` when `mx < prev[0]`, `raised` when `mx > prev[0]`, `held`/`unchanged` otherwise, independent of whether the leg was reset.

**Left-shift.** Fold it into D1's value-checking arm rather than adding a third: have that arm grade the summary LINE's counters, not just the rows. One arm, two classes, and it is the same run.

---

## D5 — LOW — F7's replacement understates the quantity F7 was about

**`tools/run-gates/derive-ceilings.py:52`.**

The comment correctly refuses to restate the overshoot figure and points at the two sources that own it. Then it paraphrases the magnitude anyway: "the recorded worst is a single-digit-seconds figure that 30 clears several times over". Both cited sources record a 12 s elapsed against a 2 s bound — `run-gates.sh:1488` and `run-gates.test.sh` arm 1c — which is a 10 s absolute overshoot, and the sentence's own sizing argument is explicitly about the largest ABSOLUTE overshoot. The same commit's new `kill-overhead` fixture in `run-gates.evidence.test.sh` encodes ceiling 2 against a 12.0 reading, i.e. the 10 s the comment denies.

No functional break — `CEILING_WINDOW_S = 35` admits 10 s comfortably. But F7 was a finding about this comment understating this exact quantity, and the replacement leaves a smaller version of it standing beside the sources it points at.

**Fix.** Delete the magnitude clause and let the citation carry it: "...has to clear the largest ABSOLUTE overshoot on record rather than the largest one relative to its ceiling — read it in `run-gates.sh`'s rc=124 block and `run-gates.test.sh` arm 1c." Nothing is lost, because the sizing argument is the part that belongs here and the number is the part that belongs there.

**Left-shift.** None worth building, and that is the point: the general form of this defect is a magnitude paraphrased beside a pointer, which no cheap predicate can grade without redding every legitimate adjective in the tree. The structural fix is to carry no magnitude at all, which makes the class impossible in this comment rather than gated. Recording that here so a later round does not re-derive the same conclusion.

---

## What was refuted, and why it is worth one line

Six raw findings did not survive the skeptic, and the pattern repeats round 1's exactly: claims about the repaired code argued from the diff rather than from a run, each dissolving when the code was executed. Precision held at 0.60 on a surface that had just been hardened, which is a better result than the flat number suggests — §8 predicts heavy multi-lens review over recently-fixed code manufactures refuted noise. A round 3 scoped to D1 and D2's fixes alone is the right shape; a re-sweep of this area would not pay.

## The gate-shaped summary

Four of the five defects are one class, one level up from the class this build was already fixing: **a claim about a repair, landed beside the repair, with nothing pointed at the claim.**

- D1 — a control arm asserting a row's existence where the defect is its value.
- D2 — a printed population derived over a wider set than the predicate visits, with the numeric guard loosened to a substring in the same commit.
- D4 — a counter that reports the opposite of what happened, in a file whose comments insist a count nobody reads is the same as no count.
- D5 — a magnitude paraphrased beside the pointer that exists to avoid paraphrasing it.

D3 is the odd one out and the ordinary kind of bug: a guard placed above the branch it was supposed to let through.

Every arm suggested above fails on the tree as it stands, which is the state §7 asks a new gate to be observed in before it lands.

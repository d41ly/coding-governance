**Serves:** journal TOOL-dDerivedDocket-17

# TOOL-dDerivedDocket-17 — acceptance ledger

The thirteenth Definition-of-Done item, `asks-disposed`; the `asks-at-landing` freeze and the
refusal that guards it; `CORE_FLOOR`'s DoD half; the protocol row and the paragraph that funds it;
and the report-only drift signal that makes ruling D12-b's override countable.

AC1, AC10 and AC12 each carry a `permission:` line deferring an observation to a run the main loop
makes after the last unit is terminal, so they get no line here and the orchestrator writes them
after that run. Everything below was observed in this pass, against a scratch fixture repository or
a staged break. No merge bar, no gate leg over the real tree and no `*.test.sh` suite was run: the
suite arms were exercised by hand, on a hand-built fixture repository whose shape mirrors the arms
this unit adds.

What AC1's own size and phrase reads said in this pass, recorded here because they are measurements
rather than the leg run AC1 defers: each protocol copy is 59779 B at this commit against 59827 B at
its parent and 672 lines against the 750-line half of the guide cap, so the row is net NEGATIVE on
its carrier; `memory/guides/UNATTENDED-VERBS.md` reads 15127 B and 165 lines; and
`grep -c 'the only way to write one'` returns 1 in each half of the verbs pair and 0 in each
protocol copy here, with exactly the reverse at the parent.

**Evidences:** TOOL-dDerivedDocket-17
- AC2 — `skipped — asks-disposed` — `--close` on a fixture build with no `asks:` mandate and a blank
  `ASKS_CMD` reports the item MET and prints the NOT ADOPTED announcement. The second half of term
  zero is AC18's.
- AC3 — `askmode short` — the fixture's declared generator answers for the first id of a two-id
  scope. `--close` is UNMET, the message carries `DEAD PROBE`, and it names `EXMP-tDisp-7`, the id
  that never came back. The scope is two because the build files an ask of its own, which is the
  only way a one-ask mandate can be short-changed.
- AC4 — `BLOCKED` — four fixtures on one mandated ask. Derived OPEN with no row at all is UNMET
  naming the admitted end states; the same ask held by a row in the FILING HOME's own `BACKLOG.md`
  is still UNMET, because only this build's file admits anything; the same row in this build's file
  with no parked decision is UNMET under the F3 hardening; and with a `decision` park row whose
  reason spells `veto 2` the item is MET.
- AC5 — `read_run_commits` — two fixtures. A mandated ask recorded CLOSED by a commit of this run
  that is not a CLOSED unit's build commit is UNMET and the message names that sha. A foreign
  build's commit landed on the fixture's default branch after `m-base:`, pushed to the fixture's
  origin and merged into the run branch, is NOT named by T4 — the advertised tip is excluded — and
  T5 names the ask instead.
- AC6 — `KEEP` — three fixtures. A KEEP row with a CLOSED spec of this build carrying only
  `order 1` is UNMET; the same row with that spec carrying `advances EXMP-aFoo-3` is MET; and the
  same verb on a SPECCED spec is UNMET again, which is the control that keeps CLOSED load-bearing.
  The in-range WONTDO half: a `yes` ask written off by a row this run added after its `m-base` is
  UNMET, and the same row carrying a `stale:` reason beside a parked decision is MET.
- AC7 — `--override asks-disposed` — on a fixture whose run is landed and whose item fails T3, the
  close reports `override recorded for 'asks-disposed'` and `close OK`, and the record afterwards
  holds exactly one `override · item asks-disposed · reason …` park row. The same call with no
  `--reason` is refused by check 12, and NOT by check 21 — the item is not in `DOD_NO_OVERRIDE`.
- AC8 — `asks-at-landing` — `--landed` on a mandated fixture writes exactly one freeze line, it
  lists `EXMP-aFoo-3=CLOSED EXMP-tDisp-2=WONTDO EXMP-tDisp-10=OPEN` — `-2` before `-10`, which a
  string sort reverses — and it sits on the line ABOVE `units-at-landing`, which is `set_fact`'s
  newest-first order. `--landed` on a record with no mandate and no filing of its own writes no such
  line. With the generator silenced the verb refuses, the record still reads `LANDING`, and it
  carries no freeze line.
- AC9 — `check-unattended.sh` — the leg's own command over a scratch copy of this tree carrying the
  break. With `asks-disposed` deleted from `DOD_CORE` and `.unattended.conf` declaring `13:13`,
  check 3 reds with `the kit's CORE Definition-of-Done set has shrunk below its floor … 12 against
  13`. The same copy unbroken exits 0 with no FAILED line at all, which is the control.
- AC11 — `drift_report.py` — a fixture holding two `override … item asks-disposed` rows, one
  `override … item gates-green` row and one `decision` row naming the same item reads
  `asks_disposed_overrides` = 2, `of` = 2, `live` true and `gateable` false, with a per-record
  detail row each. A third override raises it to 3. A fixture with no run-state file at all reads
  value 0 with `live` false, which the human table prints as a DEAD PROBE rather than a clean zero.
- AC13 — `BACKLOG.md` — `--close` on a no-mandate fixture whose own folder files
  `EXMP-tDispF-1`, with `ASKS_CMD` set, is UNMET naming that ask and its derived `OPEN`. The same
  ask with a `KEEP` row in that file is admitted, which is the green control.
- AC14 — `askmode short` — the same run as AC3. F is enumerated from the tree before the witness
  runs, so the omitted F ask is named rather than silently dropped from the scope.
- AC15 — `asks-at-landing` — `--landed` on a fixture with no mandate whose build filed one ask
  writes `EXMP-tDispF-1=CLOSED`, so a self-filed ask's answer is frozen on the same terms a
  mandated one's is.
- AC16 — `closes` — a mandated ask derived CLOSED by a CLOSED spec of this build whose header
  `closes` it makes `--close` silent on `asks-disposed` entirely. Without this arm every arm above
  is satisfied by an item that reds everything.
- AC17 — `build_commit` — the same fixture with the ask recorded `CLOSED · … · by <sha>` where the
  sha is the commit whose subject names the CLOSED unit and which touches a path outside the build
  folder. T4 does not name it. The neighbouring commit, `chore: something else entirely`, IS named,
  which is what says the exemption is the build commit and not any commit of the run.
- AC18 — `examined` — four fixtures, in order. `ASKS_CMD` set with no mandate and an empty F prints
  `nothing to dispose`; a mandate with `ASKS_CMD` blank is UNMET naming the preflight refusal that
  should have fired; a generator whose `examined` count exceeds the scope while every row arrives is
  UNMET as a DEAD PROBE; and a generator that sleeps past the declared bound is UNMET printed as
  never answered, with the DEAD PROBE wording absent.
- AC19 — `PARK_ACTS_OWED` — a mandated `legacy` ask held by this build's own row with no park row
  naming it is UNMET under T5. A `rescope · item retire <id>` row, whose act is in that constant,
  makes it MET.
- AC20 — `veto 2` — three fixtures. A `yes` ask held by this build's row and named by a `decision`
  park row carrying neither veto is UNMET; a `yes` ask whose hold TARGET is an ask this run filed
  under its own slug is UNMET; and the same self-filed hold on an ask graded `no`, with its parked
  decision, is MET.

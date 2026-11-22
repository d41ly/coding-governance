# KICK-dKeptSession-36 — acceptance ledger

**Serves:** journal KICK-dKeptSession-36

The pass built in its own worktree reset to `d06e2a65`, where `KICK-dKeptSession-5` has landed
(`tools/loop/loop_transition.py#read_mail_rows`, `MailHeld`, the `mail-open` and `mail-disposed`
plants). No merge bar, no self-test suite and no gate leg ran in it. The criteria below were read by
probes of the changed code: the three new plants each run alone by direct CLI, the resolver probes of
AC1 and AC2, an import of the module for AC6, and greps of the two user texts for AC5.

Read against the tree before the first edit: `read_mail_rows` already launches
`[resolve_bash(<driver>), <driver>, "--mail", "read", <slug>]` with `resolve_kit_dir` and
`loop_witness` imported inside the function, and already raises `mail unknown: no bash that can see
<driver>`, so S2's launch and S3's words were left as unit 5 landed them and this unit's diff is the
plants and the texts. S5's claim that both fixture-cases sentences omit `mail-open` and
`mail-disposed` did not hold at this base, since unit 5 added them; only `descope-spent` was missing,
and the outcome S5 asks, every key of `PLANTS` named, is the same.

Owed to the close: every leg the spec's section 7 names, the `loop transition record` leg's run of
the five new selftest cases and `check_plant_tokens` over the re-priced row among them; and the
`New arm:` line's RED-first observation, `mail-argv` read MISSED against a scratch copy of
`read_mail_rows` launching the bare `bash`, and `mail-no-bash` read failing against one taking a
`None` bash as the locator's refusal.

**Evidences:** KICK-dKeptSession-36
- AC1 — the probe printed the `bash.exe` in Git for Windows' `bin` directory, under `Program Files`,
  and not the System32 launcher (DERIVED, that run, 2026-11-23).
- AC2 — with `GOV_BASH` naming the System32 `bash.exe`, the probe printed `None`, and
  `scan_bash(<driver>)[2]` read `GOV_BASH is set to '<the launcher>' and answered Linux, so nothing
  after it is tried` (DERIVED, that run).
- AC3 — `python tools/loop/loop_transition.py --fixture --plant mail-argv` exited 0, the move
  recorded `planning -> designing`, and it printed `loop: fixture · mail-argv · held`: one `--mail`
  call recorded, `argv[1]` the located driver, `argv[0]` `resolve_bash(argv[1])` and the rest
  `--mail read tFix` (DERIVED, that run). Its red over a bare `bash` is owed (above).
- AC4 — `--plant mail-no-driver` exited 0, printing `loop: mail · unarmed · no unattended kit holding
  unattended.sh in this install`, the three places looked after it, then `loop: recorded · planning
  -> designing`; `--plant mail-no-bash` exited 2 printing `loop: unanswered · mail unknown: no bash
  that can see` the worktree's driver, then `loop: fixture · commits unchanged` (DERIVED, that run).
- AC5 — `grep -n "GOV_BASH" help/loop.md` names the guard paragraph's new sentence, which says
  `mail unknown`; `grep -c "mail-no-bash"` counted 1 in `help/loop.md` and 1 in
  `tools/loop/README.md` (DERIVED, that run), and a probe found no key of `PLANTS` missing from
  either cases sentence. `docs_leg.py --fingerprints` still prints `930359dc` for the page's
  `script:tools/loop/loop_transition.py` anchor (DERIVED, that run), so the anchor was not re-stamped.
- AC6 — the import printed 18 (DERIVED, that run), the five `mail-` keys among `PLANTS`, and the
  `loop transition record` row of `tools/run-gates/selftest-budgets.txt` carries `plants=18` and no
  other `plants=` token, re-priced to 67 from r 44.3s, the earlier r 40.8s plus mail-argv 1.6s,
  mail-no-driver 1.4s and mail-no-bash 0.5s (PINNED, node d, 2026-11-23).

## The pass's own reads

- `python tools/lexicon/lexicon.py --suggest` answered OK for `run_mail_spawn`, `resolve_empty_kit`
  and `resolve_no_bash`; the full run exits 1 on the corpus's verb offenders over their pin, and
  `--offenders` lists none in `tools/loop/loop_transition.py` (DERIVED, that run).
- `python tools/codebase-map/gen_map.py --write` left `memory/map/generated/symbols.json`
  unchanged, the plants' wrappers being nested functions of `run_transition_fixture`.
- `python tools/playbook/writing_practice.py check pinned-facts` printed `green · 0 red`.

# TOOL-aOrientedCast-13 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-13

Direct checks only: under the owner's rule for this run no gate, suite, slice or self-test ran in
this pass. What ran: a scratch probe calling `roles_lib.load_policy` over a scratch kit policy and a
scratch `gate-legs.json`, once against this pass's library and once against the parent's
(`git show HEAD:tools/roles/roles_lib.py`) as the RED; a probe calling `render_agents.build_fixture`
and `run_mode("write")` over a scratch repository; a `load_policy` call over gov's own seed beside a
read of gov's `.claude/roles.json`; a probe of `check_roles_install(runner=True)` with `make_target`
stubbed, which printed the deploy text and parsed it with `tomllib`; and `py_compile` over the four
touched Python files. RED first, for the library: the parent's `load_policy` raised R12 on the
optional grant `"lexicon naming predicates?"`, and on `"memory hygiene", "x?"`; this pass's
admitted both with a note. Owed to the main loop at the close (M8): the two `New arm:` lines of §7,
render self-test arm 13 and the govkit `OC13` runner arm, each RED on its staged break and GREEN
restored, and every leg §7 lists.

**Evidences:** TOOL-aOrientedCast-13
- AC1 — `lexicon naming predicates` — over a scratch manifest holding only `memory hygiene`, `load_policy` returned `{'gov-builder': ['lexicon naming predicates']}` with one note naming `lexicon naming predicates` as optional; the bare grant raised `R12 — gates.gov-builder — 'lexicon naming predicates' names no leg`; `"?"` raised `'?' names no leg`; the parent's library raised on the optional grant.
- AC2 — `absent` — `run_mode("write")` over a scratch repository whose policy grants `["memory hygiene", "absent?"]` to `r-one` beside a manifest lacking `absent` returned 0, printed a `render_agents: note` line naming `'absent'`, and `.claude/roles.json` held `['memory hygiene', 'absent']` for `r-one`.
- AC3 — owed to the main loop — the `roles render wiring` and `roles catalogue` legs: `render_agents.py --check` and `check_roles.py` exit 0 in gov, with `.claude/roles.json` byte-identical to the parent's. The pass observed only that `load_policy` over the seed returns the same leg names gov's index holds for `gov-builder` and `gov-spec-writer`.
- AC4 — owed to the main loop — the `govkit selftest` leg, sliced to `check_roles_install(tmp, runner=True)`: the target's manifest lacks `lexicon naming predicates`, and its `adopt-roles.sh --check` and `check_roles.py` exit 0, RED with the seed's grant staged bare.

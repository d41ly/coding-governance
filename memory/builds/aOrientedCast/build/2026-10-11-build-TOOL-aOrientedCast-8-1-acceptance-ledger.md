# TOOL-aOrientedCast-8 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-8

Direct checks only; no gate, suite or bar ran in either pass. The second pass applied the first
pass's work at `e995df7c1` and built rev-4's exit-3 outcome and S13 over it. Every criterion below
was observed in the worktree on the pass's tree before its commit, except AC3, AC4 and AC13, which
`govkit apply` can observe only against committed bytes and which land in a follow-up commit, as
the spec's section 6 preamble says. Staged breaks observed RED and then GREEN once restored in this
pass: `"roles",` taken out of the registry default (AC2, two arms red naming the default set and the
aged registry); `check_roles` replaced by an unconditional `ok` in a copy the check-wiring slice ran
(AC6 and AC13, six of nine arms red); one byte appended to `gov-builder.md` (AC5); an `EXTRA_TOKEN`
declared on the Skill row (AC8); the README marker set to `9.9` (AC10); four adopter copies with the
stage binding, the surviving-token refusal, the agent compare and the usage refusal staged out
(AC11, each slice red on its arm); and the `tools:` line deleted from `gov-builder.agent.md` (AC12).
The check-wiring slice and the adopter slices ran their fixtures under a short `%TEMP%` root. The
close owes the merge bar, which runs `govkit selftest`, `govkit acceptance matrix`, the
`check-wiring self-test` and `roles adopter self-test` whole, and the rest of section 7.

After the pass commit `15588db90` the follow-up observed AC3 as written. AC4 and AC13 are NOT
observed as written: `check_roles_install` hands its target's `adopt-roles.sh` and `check-wiring.sh`
to a bare `bash`, which a Windows python resolves to the WSL launcher, so those arms fail on a path
WSL cannot see. With a probe that swapped in `govkit.resolve_bash()` both printed `[]`: the apply,
the nine agent types, the `--check`, the `ok` and `UNWIRED` lines, and on the no-doc target the
Skill alone and the `UNWIRED  roles` line naming `AGENTS.md` and `CHARTER`. The write gate refused
the one-line fix because the spec is CLOSED, so their ledger lines wait for that fix. The reopened
fix pass replaced the three bare `bash` launches in `check_roles_install` with
`govkit_module().resolve_bash()`, the launcher the same file already uses, and AC4 and AC13 are
observed by the main loop against the committed fix, which this pass does not run.

**Evidences:** TOOL-aOrientedCast-8
- AC1 — `0 unclaimed` — `govkit.py selfcheck --write` exited 0: legs 134 in the manifest, 64 claimed and 70 exempt, `per-file claim: 0 unclaimed file(s)`, surface `0 unclaimed`, and `generated outputs: 8 [[generated]] row(s)`, the 6 at `744e55db` plus this unit's two; it added the `roles adopter self-test` row to the subject pins.
- AC2 — `[]` — `check_roles_default()` printed `[]` in about six seconds; with `"roles",` taken out of the default it printed `OC8 AC2 the default set holds roles` and `OC8 AC2 a registry aged before roles joined the default gains it`, and printed `[]` again once restored.
- AC3 — `ORDER|project-owned` — a default `plan` into a matrix shape 6 target at `%TEMP%/oc8p`, made with no `kits` list, exited 0. It previewed the ten `house/` overlays as `write [seed]` rows, the Skill as a `SIDE [rendered]` row, `adopt-roles.test.sh` as an `ORDER [project-owned]` row and three `.gitattributes` rows for the roles kit. The mark counts were `SIDE|rendered` 6, `write|seed` 13 and `ORDER|project-owned` 32, the three figures the default-plan arm pins at `selftest.py:6125` and `:6157-6158`.
- AC4 — `govkit apply` — observed by the main loop after the fix pass `7ed62a262`: `check_roles_install` over a default apply into a scratch target under a short `%TEMP%` root printed six `ok` lines (exit 0, the role index, nine agent types, ten seeded overlays, the `/build` Skill, a fresh `--check`) and `FAILURES []`, run 1637 s for both shapes
- AC5 — `git diff --exit-code -- .claude/` — `adopt-roles.sh --check` exited 0 in gov; one byte appended to `gov-builder.md` exited 1 naming `drift .claude/agents/gov-builder.md` and the `--scaffold` remedy; `--scaffold` restored it and the diff exited 0.
- AC6 — `UNWIRED  roles` — the slice of the prologue and the roles block passed 9 of 9: the unrendered kit read `UNWIRED  roles` naming `.claude/roles.json` and the scaffold with exit 1 and the same line with exit 0 under `--session`, the rendered fixture read `ok` counting its agent types with one `note` for its absent harness and no `UNWIRED`, the CRLF agent type was named by the eol arm, and a tree without the kit skipped; with `check_roles` printing `ok` unconditionally six arms failed.
- AC7 — `18 problem(s) · pin 18` — `check_runbook_parity.py` printed it with no line naming `roles`, and the `govkit:entry roles` anchor is one line of `WIRE-INTO-PROJECT.md`.
- AC8 — `python tools/check-kit-placeholders.py` — exited 0 and `--list` names `adopter tools/roles/adopt-roles.sh` for roles; with `EXTRA_TOKEN` added to the Skill row it exited 1 naming `{{EXTRA_TOKEN}}` and the adopter that never substitutes it.
- AC9 — `grep -c "roles render wiring" tools/gate-legs.json` — printed 1, its argv names `adopt-roles.sh` and `--check`, and `test_codebase_map.py` passed its eight tests after `gen_map.py --write` added `check_roles`, `check_roles_default`, `check_roles_install` and the adopter self-test's helpers, with the dossier claiming `roles adopter self-test`.
- AC10 — `bash tools/check-kit-versions.sh` — printed `clean — 17 declared carrier(s)`, one more than the 16 at `744e55db`; with the README marker at `9.9` it exited 1 naming `tools/roles/README.md` and `KIT_ROLES_VERSION (1.0)`.
- AC11 — `bash tools/check-testsuite-counts.sh` — each of four slices (arms 1 and 2, 3, 4, 5) printed `PASS` against the adopter as built and `FAIL` on its arm against the copy with the stage binding, the surviving-token refusal, the agent compare or the usage refusal staged out; the counts checker then exited 0 and printed no problem line.
- AC12 — `bash tools/check-install-prefix.sh --offenders` — printed no key naming a file under the roles kit; `check_roles.py` exited 0, and exited 1 naming `R2` and `'tools' is absent on an agent role` with the `tools:` line deleted from `gov-builder.agent.md`; `render_agents.py --selftest` printed `PASS (24 assertions)`; `render_agents.py --check` exited 0.
- AC13 — `charter=False` — observed by the main loop in the same run: with no doc at the seed's `CHARTER`, the apply exited 0, rendered the `/build` Skill, wrote no agent type and no role index, and check-wiring read `UNWIRED  roles` naming the doc and the `CHARTER` key, four `ok` lines and `FAILURES []`; its red half is the rev-3 adopter's exit 1, which the first pass observed failing the apply

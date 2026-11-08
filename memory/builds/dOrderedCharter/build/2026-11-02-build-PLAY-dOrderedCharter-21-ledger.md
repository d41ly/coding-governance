# PLAY-dOrderedCharter-21 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-21

Each line is a probe this pass ran at rev-4 of the spec, with the pass applied. No leg, suite or `--selftest`
ran in the pass. The scratch copy of gov's tree is `git archive HEAD` of `tools`, `help`, `skills`,
`.governance`, the charter, the conf and the build's README, the pass applied over it, committed on `main` in a
fresh repository under the system temp folder. The `role-unregistered`, `role-registered` and `code-refused`
plants of `load_sets.py --fixture` were run one at a time and each printed what its `playbook render selftest`
row asserts. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-21
- AC1 — `python tools/roles/check_roles.py --root .` over the scratch copy exited 0, `0 defect(s)`, its README re-rendered by `--write` in gov. With the `build` row's `step` line dropped it exited 1 printing `R6 — entry 5 (build) is missing key 'step'` and the README region's R11 line; with `step = "buld"` it exited 1 printing `R6 — entry 5 (build) step 'buld' is not one of entry plan design build test deploy review none` and the R11 line; restored, exit 0.
- AC2 — `python tools/playbook/load_sets.py derive --reader role.gov-builder` in gov exited 0 printing `role — unarmed — role.*: no role namespace is registered`, `reach — step build · 20 unit(s)` with the foundation-set note, and twenty units from `practice.yagni.build` to `practice.roles.build`; `practice.contract`, whose row reaches `design` and not `build`, listed none. For `role.gov-session` it printed `reach — step none · 0 unit(s)` and no unit.
- AC3 — `python tools/roles/handoff.py render --role gov-builder --build dOrderedCharter --unit PLAY-dOrderedCharter-21 --input prompt=<a brief> --input spec=<the spec> --stdout` in gov exited 0, its `## Task` section ending with `### Practices at build` and `- [yagni] delete rather than disable` first. In the scratch copy with a committed `charter.practices = ["practice.reuse", "practice.verify", "practice.contract"]`, the same render exited 0 with a block of two lines, `[reuse]` and `[verify]`, and no `[yagni]` line.
- AC4 — `python tools/playbook/instruction_units.py practices --check-charter AGENTS.md` in gov exited 0, `one line per practice · green`. Over a scratch copy with `- [yagni] delete rather than disable` planted after the `[reuse]` line it exited 1 printing `line 91 is no practice's one line: - [yagni] delete rather than disable`. A `python -c` call of `check_charter_practices` over the plant's own charter, the shipped catalogue's untokened rows, answered no fault, one fault naming the planted reach line, and one `repeats the practice yagni` fault for a doubled line.
- The charter render — `python tools/playbook/render_playbook.py --target . --check` in gov printed `render-playbook OK — region matches a fresh render`, its practice lines now read through `instruction_units#read_active_practices`.

**Owed to the close.** The bar, and the RED-first observation of the two `New arm:` lines: the AC1 arm in arm 10 of `tools/roles/adopt-roles.test.sh` (deviation 211) under the `roles adopter self-test` leg, and the `practices-reach` plant of `tools/playbook/instruction_units.py` under the `instruction units selftest` leg. The `work-order` plant's pinned bytes, unchanged by construction since its tree holds no playbook kit, and the `roles catalogue` leg over gov are read there too. The `--check-charter` verb runs in no leg over gov's own charter.

# TOOL-aOrientedCast-18 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-18

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: AC1's
`--answers ROLE_ROSTER` call and `handoff.py roster` in the worktree, compared line for line by a
`python -c` probe; a scratch probe script that imported `render_playbook` and called `render` over
§4's fixture, written under the session scratchpad, for AC2 to AC5; and the `grep` and `git grep`
of AC6 and AC8. The four selftest arms were not run here. Owed to the main loop at the close (M8):
each of the four `New arm:` lines of §7, observed RED on its staged break and GREEN once restored —
the kept-fence arm against `derive_role_roster` returning its stdout without the first line, the
unreached arm against `render` resolving every declared derived row before its token loop, the
failing-verb arm against `derive_role_roster` raising `Refusal` on a non-zero exit, and the
absent-kit arm against `derive_role_roster` swallowing the `LookupError` without its stderr line —
and every leg §7 lists.

**Evidences:** TOOL-aOrientedCast-18
- AC1 — `--answers ROLE_ROSTER` — exited 0, and its JSON `ROLE_ROSTER` value equalled the stripped stdout of `handoff.py roster` line for line (10 lines at observation).
- AC2 — `ran` sentinel — with `roles` selected under the v4.4 fixture template the body held both stub bullets verbatim between the one-line markers and the sentinel existed; with only `lexicon` selected, and with `roles` under the token-less `v3.5` template, the render returned, held neither bullet, and no sentinel existed.
- AC3 — `render-playbook: ROLE_ROSTER:` — the stub exiting 1 made `render` raise `Refusal` naming `ROLE_ROSTER` and `role_roster`, with stderr `render-playbook: ROLE_ROSTER: the roster verb exited 1: stub reason`; with `role_roster = "- answered"` the render returned a body holding `- answered` and the note `answered  ROLE_ROSTER = - answered   (probe derives nothing)`.
- AC4 — `looked in` — with no stub the stderr line read `render-playbook: ROLE_ROSTER: no roles kit holding handoff.py in this install: looked in ...` naming the receipt and both probe dirs, and `render` raised `Refusal` naming `ROLE_ROSTER`.
- AC5 — `PROBES["role_roster"]` — `tomllib` found exactly one `ROLE_ROSTER` row with `class = "derived"`, `probe = "role_roster"` and `kit = "roles"`, and `render_playbook.PROBES["role_roster"] is render_playbook.derive_role_roster` was true.
- AC6 — `KIT_PLAYBOOK_RENDER_VERSION` — its one line reads `"1.28"` and `playbook-render@1.28`.
- AC7 — `derive_role_roster` — `gen_map.py --write` rewrote `memory/map/generated/symbols.json`, which carries the symbol's `id` line, staged in the unit's commit.
- AC8 — `git grep -nE` — over `tools/playbook` and over `tools/govkit/entries/playbook.kit.toml` the pattern printed nothing (exit 1 both), and a working-tree `grep` of the two edited playbook files printed nothing too.

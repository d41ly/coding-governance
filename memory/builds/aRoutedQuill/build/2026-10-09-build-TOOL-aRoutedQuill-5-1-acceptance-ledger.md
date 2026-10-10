# TOOL-aRoutedQuill-5 — acceptance ledger

**Serves:** journal TOOL-aRoutedQuill-5

No merge bar and no self-test suite ran in this pass. `govkit` reads landed bytes from gov's
COMMITTED tree, so every install criterion was observed from a frozen `git clone --local` of this
branch under a short TEMP root, carrying the unit's changes as one scratch commit on top of the
pinned base, into scratch targets beside it. The new selftest arms ran as a slice over gov's own
registry and held 11 of 11; the matrix's new shape ran as a slice and held 11 of 11; the hygiene
self-test's new arm ran as a slice and held. The check-wiring self-test's new arms ran as a slice
too, and held its first 14 arms; the slice then ran out of its 590 s bound on a contended host
before reaching the two AC8 arms, so those two arms are unobserved here and AC8 rests on the direct
observation below. One staged break was observed red: the event filter in `matchers_of` replaced by
`cat` read a PreToolUse matcher wired under SubagentStart as `ok`, and the restored copy named it
`UNWIRED`. `govkit selfcheck` reports clean. The close still owes the legs §7 names, the held
`govkit selftest`, `govkit acceptance matrix`, `check-wiring self-test` and `memory-hygiene
self-test` among them, run whole.

**Evidences:** TOOL-aRoutedQuill-5
- AC1 — `python tools/govkit/govkit.py plan` — against a scratch target whose `deploy.toml` declares no `kits`, the selection read `check-wiring, kickoff-manifest, memory-tree, playbook, run-gates, settings-merge, agent-cap, check-microformats, codebase-map, memory-recall` with no unsatisfied requirement printed, and `govkit.py selfcheck` exited 0 after `check-agent-cap-restatement` lost its conditional mark (spec rev-5).
- AC2 — `kickoff-manifest` — `apply --kits agent-cap,settings-merge` into a fresh target exited 2 with `'agent-cap' requires 'kickoff-manifest'` and wrote no kit file.
- AC3 — `not wired` — a default `apply` printed `wired` for the two scratch-guard fragments, both card fragments and `check-wiring.fragment.json`, one line `recall-opened.fragment.json not wired — tools/memory-recall/recall-opened.js is not installed here`, and no `landed UNWIRED` or REFUSED line; the target's `check-wiring.sh --check` then printed `ok` for agent-cap, both scratch entries, card and routed.
- AC4 — `default-gained` — a target installed at the base vintage, its card fragments `landed UNWIRED`, moved by `update --write` to the scratch commit: three `default-gained` lines, the entries landed, every fragment wired, agent-cap's adopter run, `--arm-routing` appended both keys and the receipt re-stamped; after `settings-merge.py --unwire` of the gate's fragment, an update to a later scratch commit wired nothing and `check-wiring.sh --check` named the PreToolUse entry `UNWIRED`.
- AC5 — `adopt-memory-tree.sh --scaffold` — in a fixture tracking `src/`, `lib/`, `.github/` and `memory/` with no conf, the seeded conf held `ROUTED_PATHS="lib/ src/"` and `ROUTED_COMMIT_CUTOFF="2026-10-10"`, and the run exited 1 with a message naming both.
- AC6 — `adopt-memory-tree.sh --arm-routing` — on a conf assigning neither key it appended both, printing `lib/ src/`, and exited 0; on a conf assigning `ROUTED_PATHS=""`, and on one assigning `ROUTED_COMMIT_CUTOFF` alone, it wrote nothing, said so, and the conf compared byte-identical.
- AC7 — `UNWIRED  routed` — with the gate wired, `ROUTED_PATHS=""` gave the line naming the key and exit 1 under `--check`, the same line and exit 0 under `--session`; with the conf moved away the line named the absent conf; entries `/abs/`, `../up/`, `memory/` and `nothere/` each gave their own reason, and `src/` read `ok`.
- AC8 — `SubagentStart` — with `scratch-guard-subagent.fragment.json` unwired, `check-wiring.sh --check` named the SubagentStart entry `UNWIRED` beside an `ok` PreToolUse entry; with the PreToolUse group moved under `SubagentStart`, it named the PreToolUse entry `UNWIRED`, which the staged break above read as `ok`.
- AC9 — `UNWIRED  skill` — with the gate wired and `HOME` at an empty scratch directory, `check-wiring.sh --check` printed the line naming `WIRE-INTO-PROJECT.md` §1; with both gate fragments unwired it printed the old `skip`.
- AC10 — `ROUTED_COMMIT_CUTOFF` — `grep -n 'NotebookEdit' WIRE-INTO-PROJECT.md` hit the §5 table row that lists the gate beside the other five hooks a default install wires, each with its event and matcher, and §3 names `ROUTED_PATHS` and `ROUTED_COMMIT_CUTOFF` with the scaffold and `--arm-routing`.

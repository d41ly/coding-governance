# TOOL-dGroundRules-88 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-88

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `9437976a8`, `cae57b1d8`, `b8088597d` or `399ec42de^`, or at `64c85a989`, each break staged alone and restored: `packet.py --fixture --build dGroundRules --plant run-live-owner` at `64c85a989` exits 0 (`--repin admitted: an owner at a console`, byte compare green), `--plant run-live-agent` exits 1 (`--repin refused: an agent's call (AI_AGENT set in its environment)`) and `--plant run-live-detached` exits 1 (`--repin refused: no terminal on stdin, so no owner typed this (refused by default)`); on the packet.py before this unit (`399ec42de^`) none of the three plants exists (argparse exits 2, invalid choice), and that guard refuses every caller inside a live chain run.

**Evidences:** TOOL-dGroundRules-88

Observed by the builder at its build commit `399ec42de` through each criterion's own command, and by the main loop at `64c85a989` for AC4 and AC5.

- AC1 — `owner` — the direct `derive_caller` call printed `['owner', 'unknown', 'unknown', 'agent', 'agent', 'agent']` with nothing raised, so the agent markers decided before the confirmation was ever asked.
- AC2 — `an agent's call` — `--repin packet.py` from the builder's session exited 1 printing `refused: --repin is the owner's ... an agent's call (AI_AGENT, CLAUDECODE set in its environment)`, and `git status` of the packets was empty afterwards.
- AC3 — `/dev/null` — with both markers unset and stdin from `/dev/null` (which Windows Python reports as a terminal), the empty answer went down the confirmation path, printed `refused by default` and exited 1; no packet changed.
- AC4 — `REPIN` — `--fixture --build dGroundRules --plant run-live-owner` exited 0 printing `--repin admitted: an owner at a console`, `byte compare green`, `record read back: yes` and `record once the pin moves: none`.
- AC5 — `--plant run-live-detached` — `--plant run-live-agent` exited 1 with `--repin refused: an agent's call (AI_AGENT set in its environment)`, and `--plant run-live-detached` exited 1 with `--repin refused: no terminal on stdin, so no owner typed this (refused by default)`.
- AC6 — `run-live` — the five plants printed the spec's §4 base lines and exits: `run-live` and `run-unpushed` 1, `run-landed` and `run-pushed` 0, `run-dirty` 1; `run-unpushed`'s shas differ per run.
- AC7 — `--repin` — the three greps over packet.py counted 2, 0 and 1 as specified.

The owner's repin at a console (rollout step 3) was admitted by this guard inside the live dGroundRules run and rewrote all 22 chain packets, committed at `0d9b531f9`; each packet carries the guard's record line.

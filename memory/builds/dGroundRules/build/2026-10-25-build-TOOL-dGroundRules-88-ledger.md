# TOOL-dGroundRules-88 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-88

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `9437976a8`, `cae57b1d8`, `b8088597d` or `399ec42de^`, or at `64c85a989`, each break staged alone and restored: `packet.py --fixture --build dGroundRules --plant run-live-owner` at `64c85a989` exits 0 (`--repin admitted: an owner at a console`, byte compare green), `--plant run-live-agent` exits 1 (`--repin refused: an agent's call (AI_AGENT set in its environment)`) and `--plant run-live-detached` exits 1 (`--repin refused: no terminal on stdin, so no owner typed this (refused by default)`); on the packet.py before this unit (`399ec42de^`) none of the three plants exists (argparse exits 2, invalid choice), and that guard refuses every caller inside a live chain run.

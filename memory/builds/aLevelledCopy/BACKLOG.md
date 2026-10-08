# aLevelledCopy — asks

## Asks
- TOOL-aLevelledCopy-4 · filed 2026-10-09 · `tools/push-main.sh` sets `GIT_SSH_COMMAND` whenever the environment has none, and an environment value outranks `core.sshCommand`, so a lander push drops whatever identity or proxy an operator put in `core.sshCommand`. The `:=` was written to keep a caller's own `GIT_SSH_COMMAND` and never considered the config key. Once check-wiring sets the same keepalive string as `core.sshCommand` the two agree on a wired tree, so the exposure is an operator value only; deferring to it would drop the keepalive on a value that lacks one, so neither reading is strictly better and this is a decision, not a fix · seen `tools/push-main.sh`@ce9192c0:180 · accept with `core.sshCommand` set to a fixture value naming an identity file and no `GIT_SSH_COMMAND` in the environment, a lander push's ssh invocation carries that identity; with `core.sshCommand` unset it carries the keepalive options; the chosen rule for a value without a keepalive is written beside the definition line

## Dispositions
- SEV · TOOL-aLevelledCopy-4 · LOW · pre-existing; an operator identity in `core.sshCommand` is the only exposure, and no adopter is known to carry one

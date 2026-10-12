# Build brief — TOOL-aBriskPreflight-10: the tracked pre-commit hook is executable again

**Serves:** research TOOL-aBriskPreflight-10

Built inline by the main loop, one index operation: `git update-index --chmod=+x .githooks/pre-commit`,
blob unchanged. Verified by the spec's AC1 (`git ls-files -s` against `origin/main`'s blob) and AC2
(`check-wiring.sh --check` in the A/B clone `%TEMP%/bp/AN`, whose own `.githooks` carries the
regressed mode: the `UNWIRED hooks` line before the repair, the `ok` line after). No suite, no bar.

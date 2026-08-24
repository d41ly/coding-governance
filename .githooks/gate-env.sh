#!/usr/bin/env sh
# gate-env.sh — THIS REPOSITORY'S gate policy, and nothing else's. TOOL-dUnstalledConvoy-28.
#
# WHY THIS FILE EXISTS AT ALL. `.githooks/pre-push` is shipped VERBATIM as engine payload to every
# push-main adopter (`tools/govkit/entries/push-main.kit.toml`), so a policy written into that hook
# is a policy every adopter inherits without choosing it. Setting `GATE_SELFTESTS` there would turn
# the kit self-tests back ON for exactly the repositories TOOL-dUnstalledConvoy-26 exists to spare,
# at exactly the boundary it was measured for. The MECHANISM — the hook sourcing this file when it
# is present — travels; the CHOICE does not, because no kit ships this path.
#
# That property is ASSERTED rather than trusted: govkit's selfcheck derives every path any kit ships
# and refuses if a file carrying a bare `GATE_SELFTESTS` assignment is among them. If someone later
# widens push-main's include list to `**`, the bar reds instead of quietly shipping this line.
#
# WHY THIS REPO WANTS THE SWITCH ON. It is the repo that EDITS the kits. A kit self-test has a job
# exactly when the kit's source changes, which here is most days — and it has no job in a tree that
# copy-installs a kit and never touches it, which is every adopter. Same mechanism, opposite answer,
# which is the whole reason the answer is a file rather than a default.
export GATE_SELFTESTS=1

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
# THE SWITCH IS OFF, BY OWNER RULING 2026-08-27: self-checks run ON DEMAND ONLY, here as well as in
# every adopter. This file previously set it, on the argument that gov is the repo that EDITS the
# kits and so has a job for them most days. That argument was true and was outweighed: the cost lands
# on every push, including the great majority that touch no kit source, and a bar nobody can afford
# to run at the boundary is a bar that gets bypassed. It also completes the 2026-08-23 ruling, which
# said a kit's self-tests are not merge-bar legs "in this repo and in every adopter alike" -- this
# file was the one place still making gov the exception.
#
# WHAT THIS COSTS, said plainly rather than discovered later. Nothing exercises the kit self-tests
# automatically any more, at any boundary. A change under a kit directory that guts a check lands
# green. The compensating check is a person running them, and the DoD for work touching a kit is a
# GREEN verdict pasted into the landing report:
#     bash tools/unattended/run-unattended-gates.sh --selftests
#     GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh
# It also costs the drift detection TOOL-aBoundedCeiling-10 filed: a held leg stops reporting when it
# breaks, and two such reds were found on main in one session. That row is the follow-up.
#
# THE MECHANISM IS UNTOUCHED AND STILL ARMED. `.githooks/pre-push` still sources this file, and
# `pre-push.test.sh` arm 24 still drives that sourcing through its own fixture, so the switch remains
# testable and reachable -- what changed is only gov's answer. Setting `GATE_SELFTESTS=1` in an
# environment still works for anyone who wants it for one run.
#
# The `export` line is DELETED rather than commented out. A commented assignment is a line somebody
# uncomments without reading the paragraph above it.

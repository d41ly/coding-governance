#!/usr/bin/env sh
# gate-env.sh — THIS REPOSITORY'S gate policy, and nothing else's. TOOL-dUnstalledConvoy-28.
#
# WHY THIS FILE EXISTS AT ALL. `.githooks/pre-push` is shipped VERBATIM as engine payload to every
# push-main adopter (`<prefix>/govkit/entries/push-main.kit.toml`), so a policy written into that hook
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
# green. The compensating check is a person running them, and the DoD for work touching a kit is
# this: `--serial --attribute` against the build's BASE reads `verdict clean` — no NEW FAIL, no DEAD
# PROBE at L and no OVER BUDGET at L — and every suite reporting an INHERITED FAIL or a DEAD PROBE at
# R is named by a filed backlog record. Beside it, for the unattended kit, a GREEN parity verdict
# pasted into the landing report (the pooled evidence bound, TOOL-aBatchedArm-5):
#     bash <prefix>/run-gates/run-selftests.sh --serial --attribute <BASE>
#     bash <prefix>/unattended/run-unattended-gates.sh --selftests --serial --attribute <BASE>
#     bash <prefix>/unattended/run-unattended-gates.sh --selftests --pooled
#     GATE_SELFTESTS=1 bash <prefix>/run-gates/run-gates.sh
# The wording was a bare GREEN until `TOOL-dDerivedDocket-1`, and that was unreachable: several of
# the held suites are red at any base for causes filed against other units, so the DoD named a state
# nobody could produce and the red it produced instead was not about the change being graded.
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
#
# THE KEYS THIS FILE MAY DECLARE. Gov declares GOV_KITROOT and the inherited-red pair at the bottom.
#   GOV_KITROOT=<dir>         where this tree keeps its kits, relative to the root. It is the LAST rung
#                             both hooks walk, after the install receipt and a root install, so a tree
#                             govkit installed never needs it (TOOL-aRepatriatedFork-24). pre-push
#                             reads it from the sourced file; pre-commit reads the one assignment
#                             and never sources it. Gov keeps no receipt, so it declares one.
#   GATE_SELFTESTS=1          run the kit self-tests on every default-branch push (the switch above).
#   GOV_PYTHON=<launcher>     the python the hook and its bar resolve first, and likewise a kit's own
#                             `<KIT>_PY`. The hook DROPS the environment's copy of each before this file
#                             runs (TOOL-aRepatriatedFork-49), so only a value declared here is honoured,
#                             and it must be `export`ed to reach the bar.
#   GOV_GATE_CMD=<cmd>        the merge bar, when it is not `run-gates.sh`. It must run a script this
#                             repo tracks, unmodified in the working tree, at word 1 or after bash/sh,
#                             AND equal the GATE_CMD `.unattended.conf` declares at the pushed sha; the
#                             hook refuses anything else. An adopter's bar may read GATE_PUSH_BASE,
#                             the remote's sha for the default branch before the push, which the hook
#                             sets from git's own ref line and never inherits (TOOL-aRepatriatedFork-8
#                             S5).
#   GOV_BRANCH_GATE_CMD=<cmd> a bar for a push that does NOT touch the default branch, vetted by the
#                             same rule at HEAD and fed git's pre-push ref lines on stdin. Unset, such
#                             a push is ungated. It can only add a refusal, never remove one.
#   INHERITED_RED=park|land   whether a push may land over a red its default branch already carries.
#                             PARSED at the remote's tip by the hook and the unattended driver, never
#                             read from the sourced value; see the policy block below.
#   INHERITED_RED_MAX_AGE=<n> the age bound, in first-parent landings, past which an inherited
#                             red's ask is escalated BLOCKER. It decides no landing.
#                             PARSED at the remote's tip by the hook and the unattended driver, never
#                             read from the sourced value; see the policy block below.
# THIS FILE IS VETTED BEFORE IT IS SOURCED (TOOL-aRepatriatedFork-5, closing review round 1 H1): the
# hook sources it only when it is tracked at the pushed sha and its working copy matches, and refuses
# the push otherwise, so an ignored or excluded copy cannot set the test escape or `exit 0`.
# The default branch is deliberately NOT a key here: this file is sourced after the hook has decided
# which ref is the default, so a tracked file cannot choose which branch escapes the bar.
GOV_KITROOT=tools

# ---- THE INHERITED-RED POLICY, by owner ruling D12-i4 (2026-09-13). TOOL-dDerivedDocket-24 -------
# Gov LANDS over a red its default branch already carries, when every red leg reads INHERITED against
# the remote's own tip, at any age; one the run worsened still blocks. A red older than ten
# first-parent landings lands with its ask escalated to BLOCKER (ruling TOOL-dUnstuckLanding-22,
# superseding that part of D12-i4). The kit default is `land` since that ruling, and gov declares both
# lines anyway, so the bound it escalates at is written here and not inherited from a default.
#
# THESE TWO LINES ARE DATA, NOT SHELL, to both of their readers. `.githooks/pre-push` and the
# unattended driver each PARSE them out of this file as committed at the remote's tip - never out of
# the pushed tree and never by sourcing - so a branch that edits them here enables nothing until a
# gated push has landed the edit. The source above still sets them as variables; nothing reads those.
INHERITED_RED=land
INHERITED_RED_MAX_AGE=10

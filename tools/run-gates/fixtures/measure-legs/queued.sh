#!/usr/bin/env bash
# queued.sh — a measure-legs fixture leg whose own bar QUEUES on the host turnstile. TOOL-dRedressedBar-18, AC15.
#
# It runs the real runner's hold verb over `true` from the top level, the leg's working directory.
# The profile holds no turnstile, so this bar takes a ticket and waits behind whatever holds the
# host, and the profiler must read that wait from the queue. GATE_REGEN_CHECK=0 is set HERE, inside
# the leg, so the bar's generated-output preflight does not run before it queues.
set -u
here=${0%/*}
GATE_REGEN_CHECK=0 exec bash "$here/../../run-gates.sh" --hold -- true

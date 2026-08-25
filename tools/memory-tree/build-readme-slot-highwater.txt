# build-readme-slot-highwater.txt — the ADVISORY high-water mark per canonical slot.
# TOOL-dFramedEntrypoint-2. One row per slot: `<heading text>\t<bytes>`. Rewritten by
# `gen_build_index.py --bump`, which never touches build-readme-slot-limits.txt.
#
# Breaching a high-water PRINTS and does NOT change the exit code. Breaching the CEILING in the other
# file fails the bar. Both halves are copied from `tools/check-template-size.sh`, which is a hard
# declared ceiling PLUS an advisory ratchet — not, as a research pass in this build first reported, a
# warn-only gate.
#
# WHERE THE ADVISORY ACTUALLY GOES. `run-gates.sh` prints one ok line for a passing leg and echoes
# leg stdout only on failure, so an advisory inside a green leg reaches nobody through the runner.
# It is written to the leg's persisted per-leg log under the git common dir and surfaced by
# `gen_build_index.py --report`, which prints every slot's measured bytes against both numbers.
#
# ABSENT is legal and means every slot has no recorded high-water: an advisory baseline that does not
# exist yet is not a refusal, unlike an absent ceiling file. The two files are declared separately
# and fail differently, which is the whole reason they are two files.
#
# EMPTY of rows today, because the declared population is empty until TOOL-dFramedEntrypoint-7 seeds
# it. `--bump` writes the measured rows at that point.
## The problem this build exists to solve	693
## Expected improvements	468
## Detriments if this is not built	397
## Build-level rules	823
## Parked decisions	543

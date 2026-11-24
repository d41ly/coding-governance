**Serves:** research KICK-dKeptSession-67

# Brief — dKeptSession: KICK-dKeptSession-67 bound to the design

## The prompt

> /unattended dKeptSession

## The brief

### Goal

Committing `memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-67.md` is refused by hygiene check 29,
which reports that dKeptSession's coverage is red: unbound `memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-67.md`.
A chain build's INPROGRESS spec has to bind to its design. It does that with one of the binding lines that
`.memory-tree.conf` states the grammar of, next to `SPEC_CARRIES_CUTOFF`: `**Carries:**`, `**Derived:**`, `**Moved:**`,
`**Retired:**` or `**Deferred:**`. Thirty-six of this build's specs carry `**Derived:** PLAY-dClosedLoop-2`.

### Items

1. Add the binding line that fits a unit adopted at build time as a blocker to the run's landing. Read the design
   record and decision PLAY-dClosedLoop-2 in `memory/DECISIONS.md` to choose it, and say why in the return.
2. Bump the spec to rev-2, with one revision-log line naming this brief by its file stem.

### Acceptance

`python tools/memory-tree/gen_build_index.py --check` reports no unbound spec, and
`bash tools/memory-tree/check-memory-hygiene.sh --only 29` exits 0. `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`,
`python tools/check-spec-tokens.py --spec <path>`, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
and `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-67` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec` and `--only 29`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-67's.

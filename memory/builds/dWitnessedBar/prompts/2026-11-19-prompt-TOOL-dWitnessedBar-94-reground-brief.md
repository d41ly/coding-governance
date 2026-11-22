**Serves:** journal TOOL-dWitnessedBar-94

# Brief — dWitnessedBar: TOOL-dWitnessedBar-94 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The run's first two builders each stopped at a divergence, because the
specs were written at `cdfbd1cf` and the tree has moved since; each spec is now re-grounded before its dispatch.

## The brief

### Goal

Revise each spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read each spec whole against the code at HEAD and settle every claim the landed code has moved: every path,
   symbol, line citation, section name, count, population and edge. Re-derive each PINNED count with the command the
   spec states and re-pin it with today's date. A population the spec enumerates is re-derived, every new member listed
   in Files touched with the legs its guard names on the gates section's leg line, and a prose-only mention named as
   outside the population. Cite moved code-file lines as `path#symbol` or blob-pinned, never a bare `path:line`; leave a carried clause token byte-identical.
   What is built so far:
   - Built and landed through order 48: every unit up to and including 4, 25, 40, 23, 42, 3, 44, 5, 41,
     55, 8, 1, 59, 30, 29, 7, 21, 6, 2, 43, 51, 56, 57, 58, 60, 62, 63, 64, 65, 66, 69, 68, 67, 70, 71, 72, 74, 75, 73
     (`563d828df`), 76 (`3596751cf`: `CANARY_KEYS`, `check_canary_keys`), 77 (`18907b769`: one failure line per value
     in `rgf_whats`), 79 (`b9326245e`: `check_key_variant <key>:<var> <replacement> <label> <passed reason> <other
     lead>`, called for a tail and a length variant per key), 80 (`c0310ecd8`: the tail call passes
     `'${_rg_v%?}x'`, label `'tail '`, reason `the tail variant passed a value whose last byte is not CR`), 81 (`778c11528`:
     records only; its records in units 74's and 76's ledgers are owed at the close), 78 (`0e5103294`:
     `read_bar_file` and the new `read_inherited_green` read with `read_green_file`'s rules; the gov suite's
     shell-role row is 820, the hook's 1743), 87 (`300c033ce`: records only; its records in units 76's and 81's ledgers and its clone arm are owed at the close), 82 (`e8cdc8e3c`: `FLOOR_ASSERTIONS=74` with a `# RAISED 72 -> 74 by TOOL-dWitnessedBar-82` comment below it; its lines in units 76's, 77's and 78's ledgers are written; its `# RAISED` comment sits on the line BELOW the constant), 83 (`d9d627c44`: records only; it derives the floor owner from the `New arm:` specs, `TOOL-dWitnessedBar-90` today, and reads the owner comment with `grep -B1 '^FLOOR_ASSERTIONS=' | head -1`), 84 (`bd7804842`: `check_cr_reached` returns 2 for an unread file or record and 1 only for a measured failure; `check_canary_keys` and the liveness loop count the pairs they visit against `rgf_km`, the canary failure goes to stderr with return 2; the private `_derive_case_keys <cut-file> <prefix>` replaces both key derivations; `FLOOR_ASSERTIONS=76` with its `# RAISED 74 -> 76 by TOOL-dWitnessedBar-84` comment below the constant; the gov suite's shell-role row is 850), 85 (`42aa8827c`: the tail and length `check_key_variant` calls in the liveness loop each add one to `a` on return 0, at the loop's top level; `FLOOR_ASSERTIONS=80` with its `# RAISED 76 -> 80 by TOOL-dWitnessedBar-85` comment directly below the constant, above unit 84's), 86 (`1613b596c`: records only; its records in units 79's, 80's and 82's ledgers and its clones are owed at the close), 88 (`7cf3999b8`: `check_canary_keys` returns 0 when it printed nothing, 1 when it printed a variable and 2 on an unreadable file or failed visit count; `check_key_variant` accepts only a 1 with exactly `<var>`; the `<key>)` match takes bare, quoted, braced, braced-quoted and aligned arms; the length call's fifth argument is `the length variant named`; the canary guard gains `.githooks/`; ask TOOL-dWitnessedBar-105 filed; `FLOOR_ASSERTIONS` unchanged with no line added above it), 89 (`05fdf49d3`: `check_canary_keys` returns `3` on a failed visited count and `check_key_variant` passes the `3` through silently; on a `3` the liveness loop sets `fail=1` and the canary call site reds with `rgf_ok` left `0`; the `<key>)` sed match is the whole-token form; `FLOOR_ASSERTIONS=80` and every comment around it untouched; the gov suite's shell-role row is `852`), 90 (`b5a33a39c`: the canary call site reds on any `check_canary_keys` return outside `0` to `3` and sets `rgf_ok` only on `0` or `1`; the one line above `FLOOR_ASSERTIONS=80` is the owner line naming unit 90, and the floor-history comments are deleted; the gov suite's shell-role row is `853`), 91 (`81ec5dded`: records only; its clone counts and its S2 note in unit 90's ledger are owed at the close) and 92 (`27a6568ef`: records only; it wrote its own acceptance ledger, every note in units 87 to 90's ledgers and every run of its §4 note check owed at the close). Every unit this spec consumes from is CLOSED.
   - Unit 28 is NOT built: it waits on three dOrderedCharter changes (asks TOOL-dWitnessedBar-101 to -103) and the run
     defers it; any item of this spec that needs it leaves the scope, named in §3 as waiting with unit 28.
   - Order 49 is units 93, 94, 95 and 96, all consuming unit 92; their re-grounds run side by side now. List Files touched exactly, so the run can tell which of them share a file and must build one at a time; unit 97 (order 50) consumes all four. Unit 90 is the floor owner and has landed its owner line. List Files touched exactly.
   - Unit 75 rev-3 F3 took the `rec_fp` slot value from unit 77, so a spec saying unit 77 mints it now names unit 75.
     Unit 74 rev-3 F3 made AC2's break a `check_cr_reached` whose comparison is `true`, and retired the grep
     `grep -n 'tail -c1'`; a spec quoting rev-2's `-ge 0` break or that grep re-grounds to the landed shape.
   - `tools/gate-legs.json` is GENERATED by `leg_factory.py --write`; never feed a `while` loop from a here-string or
     heredoc whose value came from `$(...)`; bash 5.3.9 (cygwin) turns a `$'\r'` written inside `$(...)` into an
     empty string. Suite floors and shell-role rows at HEAD: read each from its file, never from this spec.
   - Settle every claim about the landed shape of each unit this spec consumes from against the tree, reading each
     unit's committed builder return under `memory/builds/dWitnessedBar/build/` where the spec relies on what it built.
2. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.
3. A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix (shipped surface)`; keep every home under
   `memory/project/`. Blob-pin code-file line citations only at a commit HEAD holds. A spec over its ceiling of
   49152 B (PINNED 2026-11-20 by the spec size check) is tightened in prose you touch, never by dropping a criterion.
4. Name every new function the spec introduces with a verb from `.lexicon.conf`'s VERBS table, nested helpers
   included: the lexicon leg grades them.
Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-94` and
`python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for every spec; each spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-94. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

Each status header keeps its status. The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-94.md` alone.

### Reuse

Each spec's §10 seam, re-verified at HEAD.

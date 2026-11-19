# TOOL-dPlacedRequest-18 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-18

The unit was built from its spec at rev-4 on base `a77031982`. `tools/unattended/unattended.sh#check_cadence_segment`
holds a cadence to the tag grammar's `seg` production, `[a-z0-9][a-z0-9-]*` within 64 bytes (PINNED, the
grammar's cap), under `LC_ALL=C` so the range is ASCII under any collation and the length counts bytes; a
refusal sets `LEASE_WHY` to `outside seg [a-z0-9][a-z0-9-]*` or `over 64 bytes (<n>)` and prints it (S1).
`tools/unattended/unattended.sh#derive_lease_ref` asks it of a `run` lease's cadence after
`tools/unattended/unattended.sh#check_lease_segment`, refusing `the cadence '<name>' is <rule>`. The
reserved slug `run` (S3) was already refused by TOOL-dPlacedRequest-1's builder; its refusal now names the
reservation, `the slug run is reserved`. `tools/unattended/unattended.sh#read_claims` was already free of
any cadence kind and is unchanged. Section 7 of `tools/unattended/STOPS.template.md` names the form, the
grammar and the reservation (S4), and `memory/guides/UNATTENDED-STOPS.md` is its byte-identical render.

No gate, suite or bar ran in this pass. Each criterion below was observed by a probe script in the run's
scratch directory: the driver sourced for AC1, AC3 and AC4, and for AC2 and AC5 a fixture of the suite's
own `mkconf` and `write_lease_fixture` read out of `tools/unattended/unattended.test.sh` by `awk`, a bare
origin and one clone with `RUN_CLAIMS=on` under the node's short temp path.

**Evidences:** TOOL-dPlacedRequest-18
- AC1 — over the probe set `nightly-audit maintain 9am Nightly -x a.b`, a 59-byte and a 65-byte name (PINNED),
  the predicate returned `0 0 0 1 1 1 0 1`; the four refusals printed `outside seg [a-z0-9][a-z0-9-]*`
  three times and `over 64 bytes (65)` (PINNED). An empty name and `é` were refused `outside seg` too.
- AC2 — `--lease acquire run nightly-audit 2026-10-25` printed
  `lease — run/nightly-audit/2026-10-25 · create · epoch 1` and exited 0 (PINNED); the origin held
  `refs/gov/leases/run/nightly-audit/2026-10-25`, and `--claims` printed its row
  whose first field is `run/nightly-audit/2026-10-25` and whose fleet tag is `a`.
  `--lease acquire run Nightly 2026-10-25` exited 2 (PINNED), printing `lease not written — the cadence 'Nightly' is outside seg [a-z0-9][a-z0-9-]*`, the origin
  still holding 1 ref (DERIVED).
- AC3 — `git grep -nE "maintain|review" -- tools/unattended/unattended.sh` printed only the `VERBS_SLUG`
  line, no line of the builder or the reader, and `declare -f derive_lease_ref read_claims
  check_cadence_segment | grep -cE 'maintain|review'` printed 0 (DERIVED).
- AC4 — `parse_tag` over each `unit.<name>`, a name admitted where the tag reads as namespace `unit` and that
  one segment, printed `0 0 0 1 1 1 0 1`, equal to the predicate's row for row. A copy of the predicate
  planted with `[a-z][a-z0-9-]*` printed `0 0 1 1 1 1 0 1`, refusing `9am`, so the parity reds on it.
- AC5 — `--lease acquire build run` and `--lease acquire unit run x` each exited 2 (PINNED), printing
  `lease not written — the slug run is reserved: a <kind> lease of it would read as the cadence namespace
  refs/gov/leases/run/`, and the origin held no `refs/gov/leases/run/build`.
- AC6 — `grep -n "run/<cadence>/<period>" tools/unattended/STOPS.template.md` printed the section-7 line
  of the grammar, which goes on to name `<cadence>` any tag-grammar segment and `The slug \`run\` is
  reserved`.

**Reading of AC4.** `parse_tag("unit.a.b")` succeeds as namespace `unit` with two segments, so a bare
success would admit the row `a.b` the spec expects refused. The spec checks each name "as the tag
`unit.<name>`" and gives `a.b` the reason "a dot ends the segment", so the parity reads a name admitted
only where the tag parses to `unit` and exactly that name; the suite's arm reads it so.

**Owed at the close.** The `New arm:` line of section 7: the region-8 block `TOOL-dPlacedRequest-18` in
`tools/unattended/unattended.test.sh`, 15 assertions (DERIVED), RED-first against the base driver,
which has no `check_cadence_segment`; the arm carries its own planted-copy RED for AC4 beside it. The
suite is waived for this build's landing by README rule 8.

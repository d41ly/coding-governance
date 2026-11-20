# TOOL-dWitnessedBar-56 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-56

This pass ran no merge bar, no gate leg and no self-test suite. Every criterion below was checked on node
d on 2026-11-20 by probing the unit's own code: the runner over a scratch clone under `%TEMP%`, driven by a
probe script in the session scratchpad; `verdict_backends.py --fixture --plant` for every local-hook and
peer plant named below, each over a scratch repository under `%TEMP%`; `keep_tails.py`'s `run_keep` and
`check_controls_case` called in process over `write_fixture_repo`'s scratch; the hook's `read_bar_file`
sourced alone over a planted record; `guard.py --fixture --plant signers-owner-only`; and greps over the
tree. The close owes every leg of section 7 and the RED-first observation of its five `New arm:` lines:
the hook suite's TAB plants, ` · ` note case, parity arms and knob-clear arm, staged red by restoring the
` · ` join in `check_tree_selection`; the evidence suite's selection, `base_from` and temp arms, staged red
by joining `selection.<n>` with ` · `; the gov suite's ten new plants, staged red by reading `verdict
GREEN` alone in `read_local_verdict`; the verdict backends' plants, staged red by reading standard output
for the principal; and the keep's `controls` case, staged red by skipping the escape.

**Evidences:** TOOL-dWitnessedBar-56
- AC1 — `selection.1` — a full run under a CRLF selection whose one `quarantine` row's note holds ` · `:
  `awk -F'\t' '$1=="selection.1"{print NF}'` printed 4, `selection` equalled `git hash-object` of the LF
  canonical text, and the LF twin yielded the same `selection`. The hook's `read_bar_file` kept a row's
  TABs, an empty last field's included. The hook adopting the record where R derives the row is owed at
  the close, by the hook suite's `dot` and `derived` cases.
- AC2 — `selection_ignored 2` — the same file's three-field row and `bogus`-source row: the record held one
  `selection.<n>`, `selection_ignored 2`, and a `selection` hashed over the accepted row alone.
- AC3 — `reused_cache.t0.*selection.tnone` — the grep named `.githooks/pre-push.test.sh:2477`, the one plant
  line of `write_bg_verdict`.
- AC4 — `GATE_BASE_FROM=inherited` — NOT OBSERVED here: `TOOL-dWitnessedBar-58`'s stub-bar and
  runner-boundary arms, order 33, observe it, and its S3 writes it observed.
- AC5 — `keyless` — present at HEAD: the suite's AC6-8 loop plants the `keyless` case and
  `check_tree_reuse`'s keyless branch names the missing pair; read, not run; the close's `pre-push
  self-test` observes it.
- AC6 — `read --backend local-hook` — `reused-cache`, `reused-alone`, `no-pair`, `no-selection`,
  `edited-selection` and `underived-selection` each printed `verdict: local-hook · NONE`, the last naming
  the row R does not derive, and `clean` printed `GREEN` under `selection none` and over the row R derives;
  `local-green` still held 4 of 4. The hook's agreement is the parity arms, owed at the close.
- AC7 — `check_knob_classes` — both knobs stay in `BAR_INERT_KNOBS` alone and the hook clears both before
  any bar, a STUB included; the class check and the arm whose caller sets `GATE_BASE_FROM=inherited` on a
  full decision are owed at the close, in `pre-push self-test`.
- AC8 — `base_from` — a scoped run under `GATE_BASE` and `GATE_BASE_FROM=inherited` wrote the header row
  `base_from`, `GATE_BASE…`, `inherited`, and printed `no gate-verdict written — scoped on an inherited
  green, as the run record header's base_from row reads`.
- AC9 — `RUNROOT` — present at HEAD: unit 51's AC24 arm ages both verdicts 31 days through one
  `os.utime`, so a sweep restricted to `RUNROOT` reds it; read, not run; the close's `run-gates
  evidence` observes it.
- AC10 — `controls` — the keep over a tail of 3000 invalid bytes before an ANSI colour sequence, a lone CR
  and a NUL wrote one record whose fenced block held none of the three raw bytes, held `\x1b`, `\x0d`
  and `\x00`, measured at most `TAIL_BYTES`, and whose `Hash` named the tail file's bytes.
- AC11 — `tail.<n><n>.tmp` — a sweep over `tail.123456.tmp`, `tail.AbCdEfGh` and `tail.AbCdEfGh.cut` aged ten
  days and a fresh `tail.999.tmp` removed the three aged temps and kept the fresh one.
- AC12 — `reuse cache` — the grep named the comment beside the tail sweep and the one beside the per-tree
  verdict prune, each citing the reuse cache's 30-day `cut`.
- AC13 — `peer-tip-missing` — `DEAD PROBE` naming `git fetch origin refs/gov/verdict/<sha>`;
  `peer-no-ssh-keygen` `DEAD PROBE` naming `verify-tag --raw`; `peer-bad-signature` `NONE` naming the bad
  signature; `peer-unsigned` `NONE` `unsigned`; and `grep -n 'mkstemp' verdict_backends.py` named the
  signer file.
- AC14 — `peer-signed` — node a read `GREEN`, signed by node b's registered key; the re-pointed read is
  the close's staged red.
- AC15 — `run-gates gov canary` — the `python -c` over `tools/gate-legs.json` printed `True`, and the grep
  for the four peer plants printed 4.
- AC16 — `signers-owner-only` — `guard.py --fixture --plant signers-owner-only` exited 1 with its one
  scenario held, naming `verdict.peer.signers: owner-only`, and the grep named unit 43's ledger AC3 line.
- AC17 — `FLOOR_ASSERTIONS` — raised by reading: evidence 302 to 309 (unit 41's two, this unit's five),
  gov canary 21 to 35 (unit 43's four, this unit's ten), adopter e2e 17 to 23 (unit 45's six), hygiene
  789 to 796 (unit 46's three, unit 51's four), unattended 3408 to 3410 with `FLOOR_SHARD_3` 469 to 471
  (unit 51's two), each with a dated `RAISED` comment; the executed counts are owed at the close.
- AC18 — `selection_ignored` — the grep named the selection paragraph and the migration note in
  `tools/run-gates/README.md`, `each TAB after it turned into` counted 0, and `What an adopter receives`
  named its table in `tools/memory-tree/README.md`.

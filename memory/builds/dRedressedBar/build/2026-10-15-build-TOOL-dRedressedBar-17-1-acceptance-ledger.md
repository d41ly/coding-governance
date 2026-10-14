# TOOL-dRedressedBar-17 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-17

This is the build pass of the units-12-15 spec audit's minors batch. `<w17>` is `857edcad7`, the
spec-writer pass that corrected specs 9, 12, 13, 14 and 15. `<p17>` is `6057a55c1`, the product
commit, and `<p17m>` is `d3d0dabf9`, the manifest re-stamp. `<p15a>` is `0a178ed8f`, `<p15>` is
`4d3cae332` and `<p14>` is `109fbb4ab`, as unit 15's ledger names them. The tree before this pass,
`51c6e772b`, holds the same `tools/` as `<p15>`, so a red half read on that engine is read on
`<p15>`'s.

The product commit adds `scan_entry_argv` after `silenced_legs` in `tools/govkit/govkit.py`.
`silenced_legs`, `resolve_adopter_argv` and selfcheck's cross-entry join read it, and both selfcheck
notes count its tuples. The `via` rules gain a first and a sixth rule, `check_entry_producer`'s
docstring is restated, `receipt_path` joins `ADOPTER_BAR_PATHS`, all six receipt writes go through
`write_atomic`, and `apply` writes the receipt once more after the `oid` re-stamp when RENORMALIZE
ran. `tools/govkit/selftest.py` takes the S1, S2, S3, S11, S13 and S24 checks, and
`tools/gate-legs.json` widens the `govkit selftest` guard. `memory/map/generated/symbols.json` came
from `gen_map.py --write`, run alone. The kickoff ratchet's staged check refused the product commit
until it carried a re-stamp, so `<p17>` holds one at its parent, as `b357641ed` did, and `<p17m>`
re-stamps at `<p17>`. `<p17>` also carries spec 17's dispatched INPROGRESS header and the build
index rendered from it, because hygiene check 9 renders that index once product source naming the
unit is staged.

No merge bar, no self-test suite and no gate leg ran in this pass. scratch-guard refused
`python tools/govkit/govkit.py selfcheck` in a clone of gov as row G1, the `govkit selfcheck` leg,
so AC10's and AC16's note lines are read here through a stand-in, and the leg's own run is owed to
the close. Every other criterion was observed with a direct probe. Targets were fresh `git init`
trees under `%TEMP%/d17*` with `DEPLOY_FULL`'s answers. The green halves ran from the worktree or
from `<p17>`. The red halves ran from a local clone at `%TEMP%/d17g15`, checked out at `<p15>`,
`<p14>` or `<p17>`, each staged break written to its `govkit.py` alone and restored from git after.
The section 7 gates are owed to the close, with the RED-first observation of all five `New arm:`
lines.

**Evidences:** TOOL-dRedressedBar-17
- AC1 — `[dRB-14]` — a python program cut `tools/govkit/selftest.py` from the first to the last line
  carrying `[dRB-14]`, lines 3608 to 3641 at `<p17>`, and found six `check(` calls, none carrying
  `kit 'agent-cap'`. The `[dRB-15]` span, 3652 to 6061, held the check that no line opens
  `govkit: kit '`. Spec 14's section 2 carries `TOOL-dRedressedBar-17`, and spec 15's section 5
  carries `[dRB-14]`. Over the `<p15>` file the same program found two chunks in the `[dRB-14]` span
  carrying `kit 'agent-cap'`, beside the same `[dRB-15]` check.
- AC2 — `.governance/install.sums` — over `%TEMP%/d17a2`, step 1 applied
  `agent-cap,settings-merge,kickoff-manifest` and step 2 `settings-merge`, each committed after.
  Step 2's line carrying `/RECEIPT]` read `18 row(s), 3 kit(s)`, the lengths of the receipt's
  `files` and `kits`. The sidecar's 14 pairs equalled the receipt's 14 hashed rows, the 13 carried
  `agent-cap` and `kickoff-manifest` rows among them. `check --target` printed no sidecar line and
  the note `sidecar: 14 line(s) compared against 14 hashed row(s)`. After spec 14's AC1 apply, at
  `[kit.agent-cap] prefix = "scripts"`, the sidecar equalled the receipt's 14 hashed rows. Red: a
  `<p17>` copy writing the sidecar from `rows` alone made `check` print 13 lines carrying
  `which install.sums does not`, one per carried hashed row. A copy whose step line counts `rows`
  and `selection` printed `2 row(s), 1 kit(s)`.
- AC3 — `write_vintage_receipt(` — at `<p17>`, each marker line occurs once, at 3434 and 3479. The
  span between them calls `write_vintage_receipt(` once, with the check that the appended agent-cap
  row carries none of `commit`, `sha256` and `gov_oid` before it and the check for all three after
  it. Spec 13's rev-6 line names report id 3 and AC3. Over the `<p15>` file both markers are absent.
  The staged break, a row appended with the three keys set, is the `New arm:` line owed to the close.
- AC4 — `tools/gate-legs.json` — spec 15's section 7 cut carries `format-guard self-test`,
  `kit placeholders (a declared token its adopter substitutes)` and `floor`. A python program joined
  the eight paths under its Files touched against every guard in `tools/gate-legs.json`, `{prefix}`
  read as `tools`, skipping a guard more than 5 legs carry. It found eleven legs and none unnamed on
  the leg line.
- AC5 — `README.md` — spec 14's Edges cut carries the consumes-from line for
  `TOOL-dRedressedBar-13`, and spec 13's the hands-off line for `TOOL-dRedressedBar-14`. Both
  sentence counts printed 0, and spec 14's "Order, and unit 7" cut carries `README.md` and
  `build-order`.
- AC6 — `build-order` — spec 13's section 1, joined, counts 0 for `ordered after every unit` and
  carries `build-order`.
- AC8 — `:11119-11120` — in spec 13, `which decode strictly` counts 0, `:10986-10987` counts 0 and
  `:10986-10988` counts 3. Its section 5, joined, carries `:11119-11120`.
- AC9 — `:7424` — spec 14's section 4, joined, counts 0 for `The only appends are` and carries
  `:7424`, `:7502`, `:7540`, `:7593`, `:7616`, `:7621` and `rows.append`. Read at `46eb75ed`, lines
  7233 to 8031 of `govkit.py` hold `rows.append` at exactly those six lines.
- AC10 — `scan_entry_argv` — a python program imported `govkit` from the worktree at `<p17>`'s bytes
  and read `read_descriptors` over a bare target. The `[[gate_leg]]` tuples whose resolved text
  carries `/`, whose `missing` is empty and which are not in `have` grouped to exactly what
  `silenced_legs` returned, `[]`, and that list equalled HEAD's `silenced_legs` over the same input.
  The `{gate_file}` element of `codebase-map coverage + freshness` came back with kind
  `[[gate_leg]]`. `inspect.getsource` of `silenced_legs` and of `resolve_adopter_argv` each carries
  `scan_entry_argv(` and no `resolve_tokens(`. The walk yielded 169 `[[gate_leg]]` tuples and 279 in
  all, 105 graded. A stand-in for the refused leg recomputed the two notes through the engine's own
  functions at `%TEMP%/d17g15` checked out at `<p17>`: `gate legs:` offers 169, and
  `cross-entry argv:` offers 279 across 29 entries, 105 graded, 0 naming. `symbols.json` holds
  `scan_entry_argv` with file `tools/govkit/govkit.py`, and spec 15's section 10 carries
  `silenced_legs` and `scan_entry_argv`. Red, over the `<p15>` engine: the name is absent,
  `silenced_legs` carries `resolve_tokens(`, and the join skips a declared element with no `/`. The
  two `selfcheck` note lines themselves are owed to the close.
- AC11 — `carries a rendered, generated or merged rule` — `check_entry_producer`'s docstring carries
  `resolve_adopter_argv` and `via` and not the deleted CONFIGURE quote. Scratch govs under
  `%TEMP%/d17x`, shaped as `build_scratch_gov_cross` builds them, ran
  `<g>/tools/govkit/govkit.py selfcheck`. The `rendered` gov printed one line opening
  `govkit: entry 'demo' declares [adopt] via` and carrying that reason. The same gov without the
  rule, the `via` gov, printed none. Red: around the `<p15>` `govkit.py`, under `%TEMP%/d17y`, the
  `rendered` gov printed no such line.
- AC13 — `can't open file` — the S13 target at `%TEMP%/d17u1`: `check-wiring,kickoff-manifest` at
  OLD and `[kit.agent-cap] prefix = "scripts"`, then `update --target <t> --write`, run by
  `<p17>`'s engine bytes with `--to 51c6e772b`, whose shipped bytes equal `<p17>`'s. Of the lines
  opening `govkit update — default-gained ` and carrying `adopter exit`, one named
  agent-cap or settings-merge, `default-gained agent-cap: adopter exit 2`, and no line carried
  `can't open file`. Red over `<p14>`, in `%TEMP%/d17u2`: two such lines, agent-cap's and
  settings-merge's, and agent-cap's problem line carried `can't open file`. Red over a `<p17>` copy
  whose gained loop resolves the declared `[adopt].argv`, in `%TEMP%/d17u3`: the one such line
  opened `default-gained settings-merge:`. All three halves read as the spec derived them.
- AC16 — `tools/hooks/kit.toml` — a stand-in for the refused `selfcheck` leg. The join program above
  read the hit count 0 at `<p17>`, and 1 with `tools/hooks/kit.toml` checked out from `<p14>`:
  agent-cap's `[adopt]` naming `tools/settings-merge.py`, owned by settings-merge. Matching
  `, (\d+) naming` on the `cross-entry argv:` line is owed to the close.
- AC18 — `manifest-audit:` — the `govkit selftest` guard holds `{prefix}/govkit/`,
  `{prefix}/hooks/kit.toml` and `{prefix}/settings-merge.py`, and each new path is carried by 1 leg.
  `last-audit:` names `6057a55c14275d3468eefc23a44d2925499a1e69`, `<p17>`, whose
  `tools/gate-legs.json` holds both paths. `<p17m>`'s body carries `manifest-audit:`. At `<p15>` the
  guard is `{prefix}/govkit/` alone and `last-audit:` names `ebce889c7`.
- AC19 — `render_playbook.py` — spec 14's reader-table cut carries `render_playbook.py` and
  `':!*.test.sh'`. At `<p17>` the `git grep` prints five files, `adopt-lexicon.sh`,
  `adopt-memory-tree.sh`, `render_playbook.py`, `settings-merge.py` and `adopt-unattended.sh`, each
  named in the cut.
- AC20 — `2026-10-14-spec-TOOL-dRedressedBar-9.md` — `declares the same argv` counts 0 in spec 9.
  Its section 4, joined, carries `via` and `TOOL-dRedressedBar-15`. Spec 15's section 2, joined,
  carries `2026-10-14-spec-TOOL-dRedressedBar-9.md`.
- AC21 — `gen_map.py --write` — spec 15's section 2, joined, carries `gen_map.py --write` and no
  `regen.py --write`. `<p15a>` moved four paths, all under spec 15's Files touched, and its rev-5
  line names the four and says none moved outside.
- AC22 — `raise RuntimeError("drb17 staged fault")` — the target state, derived: `%TEMP%/d17r2`
  with `core.autocrlf false` and `docs/PARALLEL.md`, the playbook seed's destination under its
  `{playbook_path}` pin, committed with CRLF bytes, then settled with `git update-index --refresh`
  after the racy window. A first try without the settle refused the renormalize as dirty. A
  `<p17>` copy with that line before `step(STEP_LEGS, ...)` ran `apply --kits playbook` and exited
  1. RENORMALIZE moved the seed's index blob from `f1752b30` to `1844b4ce`, and the receipt's `oid`
  read `1844b4ce`. The tip's apply over the same uncommitted target printed no `DIRTY` line. Red: a
  copy with the same fault and without S22's write left that row's `oid` at `f1752b30`, against
  index `1844b4ce`, so the red half's differing row was observed. Its re-run printed no `DIRTY`
  line either: both re-runs exit 1 on the renormalize guard, naming `docs/PARALLEL.md` as not clean
  relative to HEAD. A seed row is outside the dirty check's population, since `seed` dispatches to
  `report-reseed`. An `autocrlf true` target applying agent-cap, settings-merge and
  kickoff-manifest moved no pinned engine row's blob, with every `oid` equal and no S22 write, so no
  state found makes the `DIRTY` clause discriminate. That clause is returned to the main loop and
  not counted.
- AC23 — `write_atomic` — `grep -c 'receipt_path.write_text'` prints 0 at `<p17>`, and
  `ADOPTER_BAR_PATHS` holds `receipt_path`. A program wrapping `pathlib.Path.write_text` to write
  half and raise `OSError` on `install.json` or `install.json.govkit-new` called `govkit.main` with
  `apply --target <t> --kits check-wiring` over `%TEMP%/d17w1`. The call raised the `OSError` on
  `install.json.govkit-new`, and `install.json` parsed and equalled its earlier bytes, with no
  sibling left. Spec 14's "When CONFIGURE fails" table carries `write_atomic`. The routing walk the
  `[-21] AC2` arm runs, copied into a probe, found 0 direct writes and 8 routed ones. With
  `receipt_path` declared, HEAD's engine showed six direct writes. Red over the `<p15>` engine, in
  `%TEMP%/d17w2`: the fault hit `install.json` itself, and `json.loads` refused what was left.
- AC24 — `is not a non-empty string` — the `empty` and `list` scratch govs under `%TEMP%/d17x`, with
  `via = ""` and `via = ["other"]`, each printed one line opening
  `govkit: entry 'demo' declares [adopt] via` and carrying `is not a non-empty string`, and neither
  output carried `Traceback`. Importing the `empty` gov's `govkit`, `resolve_adopter_argv` for demo
  raised `KeyError` naming demo. Red, around the `<p15>` `govkit.py` under `%TEMP%/d17y`: each
  printed one such line carrying `names no registry entry`, with no `Traceback`, and
  `resolve_adopter_argv` returned `[]`.
- AC25 — `TOOL-dRedressedBar-17` — `<w17>` gives specs 9, 12, 13, 14 and 15 one header rev change
  and one new revision line each, and each newest line names `TOOL-dRedressedBar-17` and every
  report id the table assigns it. All five were CLOSED at `<w17>~1`. Under the spec folder, `<p17>`
  changed this spec alone, its dispatched status cell, and `<p17m>` none. This record carries
  `**Serves:** journal TOOL-dRedressedBar-17`.

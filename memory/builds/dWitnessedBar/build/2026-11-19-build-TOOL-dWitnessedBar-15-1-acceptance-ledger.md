# TOOL-dWitnessedBar-15 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-15

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: the canonical
`tools/lib/legacy_ledger.py seed` run in a scratch git repository at `%TEMP%/ll15`, holding a copy of
the lib directory, a copy of the policy kit and a `[[ledger]]` registration whose seed argv prints one
row per word of a keys file; and both adopters run over a scratch target at `%TEMP%/ad15` holding the
codebase-map, memory-tree and drift-audit kits. The two `New arm:` lines of spec section 7, section
`2o`'s seed cases in `tools/lib/resolve-python.test.sh` and arm 7 of
`tools/codebase-map/adopt-codebase-map.test.sh`, were written and syntax-checked with `bash -n` only;
each still owes its RED-first observation, which the main loop makes at the close, and so does every
leg that section names.

**Evidences:** TOOL-dWitnessedBar-15
- AC1 — `armed p 2` — `seed --population p` over an absent home printed `armed p 2`, exit 0, and the
  home held the rendered header and the rows `a` and `b`, each `1`, HEAD's full sha and `seeded`. No
  `.tmp` or `.seed` file was left in the fixture after the probe's runs.
- AC2 — `present p` — with a third key planted in the keys file and committed, the rerun printed
  `present p`, exit 0, and `cmp` found the home byte-identical to its copy taken after AC1.
- AC3 — `widened:R1` — the same rerun with `--widen R1` printed `widened p c`, exit 0; the home's
  first three lines equalled the AC1 copy and its fourth read `c`, `1`, the planted commit's sha and
  `widened:R1`. A second `--widen R2` printed `widened p` and left the bytes unchanged.
- AC4 — `unarmed p exit 1` — with the seed exiting 1 over an absent home, `seed` printed
  `unarmed p exit 1`, exit 1, and the home held the header and `# unarmed · exit 1 · <sha>` and no
  row; with the seed printing `dead probe: no files` it printed `unarmed p dead probe` and the home
  held `# unarmed · dead probe · <sha>`; repaired, the rerun printed `armed p 3`. A `--widen` whose
  seed exited 1 over the armed home printed `unarmed p exit 1; the armed home is unchanged` and left
  its bytes equal (deviation 154).
- AC5 — `unarmed` — a registration homed at `nodir/r.txt`, `nodir` existing and holding no tracked
  file, printed `unarmed r home directory nodir holds no tracked file, so the hygiene check has not
  admitted it`, exit 1, the reason also on stderr, and `nodir/r.txt` was not created.
- AC6 — `unarmed q no seed` — a registration with `seed = []` printed `unarmed q no seed`, exit 0;
  with `.governance/policy.toml` committed on `main` reading `unseeded = "refuse"` under
  `[retrofit]`, `seed --all` exited 2 with `legacy_ledger: retrofit.unseeded is refuse, so each
  registration declaring seed = [] is refused: q`; with the policy kit removed and committed it
  printed `unarmed q no seed`, exit 0, and one stderr line naming `retrofit.unseeded` and the three
  places the lookup tried. A policy file with no valid revision exited 2 with the reader's own
  `policy: refused · .governance/policy.toml@430e6833:2 · …` line. `grep -c 'retrofit\.unseeded'
  help/policy.md` printed 1, the consumer list's new bullet.
- AC7 — `affordance-exempt.toml` — over the scratch target, the adopt after the scaffold was committed
  wrote `affordance-exempt.toml` with `exempt = []`; with a dossier lacking the `## Reuse affordance`
  section planted and committed, the next adopt printed `present memory/map/affordance-exempt.toml`,
  `cmp` found the list byte-identical, and the installed gate failed
  `test_dossier_affordance_present_or_graced`, the planted violation still live. The drift-audit
  adopter printed `drift-audit: armed tools/drift-audit/drift_signals.py` on its first run and
  `drift-audit: present tools/drift-audit/drift_signals.py` on the next, a tuned file's `cksum`
  unchanged. On the scaffolding run itself, `memory/map` not yet tracked, the seed printed `unarmed`
  with the home-test reason and wrote nothing, the fresh-install break TOOL-dWitnessedBar-47 repairs.
- AC8 — `item.test.seed` — NOT OBSERVED: asks TOOL-dDeclaredLoop-118 (§8 F4 as F7 words it) and
  TOOL-dDeclaredLoop-119 (§8 F5), filed in `memory/builds/dDeclaredLoop/BACKLOG.md` in this pass, have
  not landed, so `check_program` still refuses the row and `tools/loop/loop.toml` was left unwritten.

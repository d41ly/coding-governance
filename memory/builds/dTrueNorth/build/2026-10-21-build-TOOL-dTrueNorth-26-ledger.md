# TOOL-dTrueNorth-26 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-26

No merge bar, no self-test suite and no gate leg ran in this pass; the naming lexicon answered the six
functions the pass mints (`--suggest <name> --as py.function`, OK for each). Every criterion below was
observed by a probe of the changed code over `83ead7089`, its red-when by the same probe over the base
kit, `git archive 83ead7089 tools` unpacked under `%TEMP%/u26h`. Fixture repositories sat under short
`%TEMP%` paths with no hook installed. The suite arms the `New arm:` lines name, and their RED-first
observation, are owed to the close, and so is AC21's wrapped `render_lines` run of `run_plant_arms`,
which is the deviation selftest's own body.

**Evidences:** TOOL-dTrueNorth-26
- AC1 — `design_lib.run_git` — with every `tree_lib.GIT_ENV_LEAKS` name exported and
  `subprocess.run` capturing its env, neither runner's env held a leak name and
  `routed_commits` had no `GIT_LOCATION_VARS`. Over the base kit `design_lib.run_git` passed all
  twelve names, `routed_commits.run_git` the four pathspec names and `GIT_NAMESPACE`, and the
  second list stood.
- AC2 — `python tools/memory-tree/asbuilt_view.py --fixture` — with `GIT_DIR` naming scratch
  repository A's, `design_lib.run_git` over B answered B's HEAD, and the fixture exited 0 with
  `findings 0`, A's HEAD unchanged. The base kit's runner answered A's HEAD, and its fixture died
  on a failed `git fast-import`, exit 1, its `git init` having re-initialised A.
- AC3 — `scan_carries` — `part 1/2` with `part 2/3` gave one `parts` finding naming the totals
  2 and 3; `part 1/2` with `part 2/2` gave none. The base checker gave no finding for the first.
- AC4 — `tier2-review self-test` — `--legs-for` over the generator listed the leg, and a
  `json.load` of the manifest shows its guard holding `{prefix}/memory-tree/gen_build_index.py`.
- AC5 — `scan_chain_specs` — with a blank cutoff over a chain spec and `spec/notes.md` it kept the
  spec alone, counting `unnamed 1`, and `read_spec_revisions` over the kept path returned without
  `DesignRefusal`. Over the base kit the notes file was kept, and the reader refused it as outside
  its pathspec.
- AC6 — `python tools/memory-tree/deviation_join.py --fixture --plant spec-notes` — exit 0, two
  chain-build specs and six members, none unjoined, the notes file measured as no spec; under
  `--policy refuse`, exit 0 as well.
- AC7 — `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md` — the `--scan` over
  every tracked spec printed 0 empty-id lines, against 2 before the change, this file and
  aQuenchedHarness-13's; a scratch spec holding the backticked words foo bar still printed one.
- AC8 — `unattended.sh --dispatch` — in a scratch fixture whose CLOSED sibling declares the
  backticked `none`, the consumer's dispatch printed `dispatch declared`. The base driver refused it
  with check 49, naming a consumes-from line from which no unit id is read.
- AC9 — `deviation_join.read_records` — over a base fixture it and `read_view_inputs` read 4
  records each; an untracked draft moved neither, and after `git add` both read 5, the draft among
  them. The base join and view each read the untracked draft, 4 to 5.
- AC10 — `git ls-files` — after `write_tree` the fixture's index listed 14 paths, every path of the
  branch's tree. The base fixture's index listed 0.
- AC11 — `design_lib.py` — the probe found `asbuilt_view._CL` and `deviation_join._CL` to be
  `design_lib._CL` itself, and the grammar's one spelling in the kit's `*.py` is one line of
  `design_lib.py`. The base kit's modules held their own, and 4 such lines.
- AC12 — `ROW_FOLLOW` — the new scan over `asbuilt_view.py` flagged exactly `ROW_FOLLOW` and
  `ROW_DEPARTS` before the allow-list and nothing after, and over a copy holding an added
  `SECOND = re.compile(r"^\| " + _CL)` it flagged `SECOND`. The base scan flagged nothing there.
- AC13 — `(no spec)` — the scratch fixture's consumer, consuming from a unit on the authored
  `roster:units` pair with no spec, was refused with check 49 naming both units and `(no spec)`,
  and with that producer's spec CLOSED printed `dispatch declared`; a malformed pair was refused
  naming the README. The base driver declared all three.
- AC14 — `read_design_view` — a scratch view row whose text holds a bare CR came back with the CR
  in its text cell. The base reader raised `DesignRefusal`, naming the split row.
- AC15 — `load_kit_module("tree_lib")` — with a namesake `tree_lib` in `sys.modules` it returned
  the kit's `tree_lib.py` and left the namesake in the slot. The base loader returned the namesake.
- AC16 — `check_index_input` — the grep for the superseded trigger printed 0, and lines 1 to 40
  name check 30, `check_index_input` and the block comments of checks 29 and 30.
- AC17 — `check_cutoff_value` — the nine lines above `SPEC_CARRIES_CUTOFF=` name
  `read_design_conf` and `check_cutoff_value`, and neither `read_cutoff_key` nor the
  nothing-reads-it sentence.
- AC18 — `merge=ours` — in a clone of this worktree under `%TEMP%/u26c`, this pass's files copied
  in and committed there, `--check-asbuilt` exited 0 with its clean count line; with the view's
  line out of `.gitattributes` it exited 1 naming `DESIGN_VIEW` and `merge=ours`; restored, 0.
  The base generator over the same line-less clone exited 0 with the clean count line.
- AC19 — `grep -c 'GENERATED_INDEXES' .gitattributes` — printed 1, and the two `gitattributes`
  greps over `.unattended.conf` and `.memory-tree.conf` printed 1 each.
- AC20 — `read_blobs_at` — over a scratch fixture `read_blobs` answered None for a blob that is not
  UTF-8 and the text for one that is; with `tree_lib.read_git_output` stubbed to raise `OSError` it
  raised `Unmeasured`; its `ast` holds a call of `read_blobs_at` and no `--batch` string. The base
  reader decoded the blob with replacement characters.
- AC21 — `derive_plant_needle` — it maps 12 plants to None, the eleven at `190c1eea` and
  `spec-notes`, each exit 0 in `PLANT_EXITS`; each one's fixture under `--policy refuse` exited 0,
  so the findings count its report arm now reads is 0 over the plant. The wrapped run of
  `run_plant_arms` is owed to the close.
- AC22 — `python tools/memory-tree/deviation_join.py --approval by-risk` — its header read
  `refused 3`, deviation-20, deviation-21 and deviation-26 on `refused:` lines and deviation-27 on
  none, exit 0; under `--approval author-recorded` it read 27 records, none malformed and none
  refused, no line naming deviation-25, deviation-26 or deviation-27, exit 0.

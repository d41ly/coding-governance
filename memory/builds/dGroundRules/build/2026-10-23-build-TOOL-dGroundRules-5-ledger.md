# TOOL-dGroundRules-5 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-5

No merge bar, gate leg or self-test suite ran in this pass. Each criterion was observed on the built
tree before the commit, by the kit's own CLIs or by scratch probes that import `check_policy` and
call `run_fixture("<case>")` or an arm in process, never the leg. Every fixture repository sat under
the system temp directory with the `pol-` prefix. The naming lexicon ran, and read P1 verb offenders
1213, the pin, with `js.type` graded at 0 of 1 against `pascal`. The red-first observation of each
`New arm:` line, and the policy legs themselves, are left for the close.

**Evidences:** TOOL-dGroundRules-5
- AC1 — `python policy.py mirror --write` — on the built tree it printed "policy: mirror written ·
  259 keys · policy 43fa1bb1 · catalogue 79782691". The file parsed as JSON. Its `policy_blob`
  equalled `git rev-parse HEAD:.governance/policy.toml` and its `catalogue_blob` the catalogue's
  blob at HEAD. Its `keys` held all 259 catalogue names with no pattern segment, a count derived
  from the catalogue at observation, each with exactly `value`, `source` and `reason`. A second
  `--write` printed "policy: mirror fresh", and the sha256 of the file was 973a277e… both times.
- AC2 — `--fixture mirror-absent` — `run_fixture("mirror-hand-edited")` printed "RED as planted"
  then "green unplanted", the finding being `runtime.agents-in-flight`: "differs from the render at
  HEAD". `run_fixture("mirror-absent")` printed the same pair, the finding being
  `.governance/policy.json`: "absent". Each case reported 2 assertions, 0 wrong. On the built tree
  `python policy.py mirror --check` printed "policy: mirror fresh", exit 0, before the commit. The
  render names the rendered commit's sha8 in each reason, so the committed mirror reads stale at the
  commit that carries it; that is finding 1, which TOOL-dGroundRules-65 repairs.
- AC3 — `uncommitted changes` — in a scratch fixture repository with the kit's three files
  committed, a written mirror and an uncommitted edit of the policy file, `mirror --write` and
  `mirror --check` each exited 2 printing "policy: refused · .governance/policy.toml:0 · uncommitted
  changes; the mirror renders a revision, commit first", and the mirror's bytes were unchanged. An
  uncommitted edit of the catalogue copy refused the same way, naming the catalogue. Restored,
  `--check` printed "policy: mirror fresh". The same probe read a hand-edited mirror as "stale ·
  .governance/policy.json · mailbox.fetch-seconds", a deleted one as "absent", and `{not json` as
  "unparsable", each exit 1.
- AC4 — `python tools/run-gates/regen.py --list` — on the built tree it printed "regen: stage 2 ·
  policy · .governance/policy.json", then "write  python tools/policy/policy.py mirror --write" and
  "check  python tools/policy/policy.py mirror --check".
- AC5 — `node policy-mirror.js get runtime.agents-in-flight --repo <fixture>` —
  `run_fixture("mirror-worktree-loosened")` landed L with the limit 2 and its fresh mirror, and set
  the working-tree mirror to 8 with its blob ids kept. The four-line fixture hook asked for 3 and
  exited 2. The helper printed `2`, exit 0. `arm_mirror_landed` found nothing over the 2 keys the
  file at L sets. 3 assertions, 0 wrong.
- AC6 — `mirror stale at` — `run_fixture("mirror-stale-last-valid")` landed L setting 3 with the
  mirror rendered at 2. The helper printed `3`, and `--explain` printed "policy:
  runtime.agents-in-flight · file · mirror stale at c5dd7116; set in .governance/policy.toml at
  c5dd7116, upstream/main, the landed revision". `arm_mirror_landed` found nothing. 2 assertions, 0
  wrong.
- AC7 — `policy: refused · .governance/policy.json:0` — `run_fixture("mirror-stale-refuse")`: the
  helper exited 2, nothing on stdout, stderr "policy: refused · .governance/policy.json:0 · stale at
  2286ddaa; policy-file.on-invalid is refuse", and `arm_mirror_landed` redded naming both keys the
  file sets, `runtime.agents-in-flight` among them. `run_fixture("mirror-absent-refuse")`: under
  `refuse` the helper exited 2 with "... · absent at b5f003da; policy-file.on-invalid is refuse";
  after a landing that set `last-valid` it printed `3`, the reader's value, with a reason opening
  "mirror absent at d29d4815", and `arm_mirror_landed` found nothing. 5 assertions, 0 wrong.
- AC8 — `diff` — the awk range of the parity arm cut `remote_ladder_sh` and `resolve_python` out
  of `policy-shim.sh` and out of `tools/lib/resolve-remote.sh` and `tools/lib/resolve-python.sh`,
  CR stripped; both diffs were empty, over 43 and 31 lines.
- AC9 — `derive_landed_revision` — `run_fixture("mirror-landed-parity")`: with two remotes and
  `GOV_REMOTE` naming the second both answered a0bf8011…; with two remotes and none chosen both
  refused, the shim with "policy: refused · .governance/policy.toml:0 · cannot choose a remote: ...";
  with one remote and with no remote both answered 69a2ff58…. 4 assertions, 0 wrong.
- AC10 — `python policy.py get runtime.agents-in-flight --json` — on the built tree it printed one
  object whose sorted keys were `reason`, `source` and `value`, the value 6 that plain `get`
  printed. `get no.such.key --json` printed nothing on stdout and exited 2 with "policy: refused ·
  <kit>/catalogue.toml:0 · no.such.key is not a catalogue key".
- AC11 — `arm_mirror_readers` — `run_fixture("mirror-direct-reader")` printed "RED as planted",
  the finding naming the fixture's tracked consumer outside the kit, then "green unplanted": 2 assertions, 0 wrong. On the built
  tree the arm graded 255 tracked code files with no finding; an independent `git ls-files` count of
  the same pathspecs outside the kit, `memory/` and `help/` read 255.
- AC12 — `eol: lf` — `git check-attr eol -- .governance/policy.json` printed
  ".governance/policy.json: eol: lf".

## What the close observes

- The live `arm_mirror_landed` over this branch reads a zero population, so it is a finding: the
  landed revision, the remote's `main`, carries no policy file until this build lands. The per-arm
  empty rule of TOOL-dGroundRules-21 and the `announce` declaration of TOOL-dGroundRules-25 decide it.
- `adopter-fresh-target` can only grade a committed kit, because the deployer installs from HEAD.
  Over a fresh target the parity arm reds on the absent mirror and the readers arm on an empty
  population, which TOOL-dGroundRules-21 S5 and S15 settle.
- The four `New arm:` lines' red-first observations, the `policy check` and `policy fixtures` legs,
  kit epoch, encoding posture, the resolver parity rows over `policy-shim.sh`, remote literals,
  install-prefix, shell hygiene and codebase-map coverage.

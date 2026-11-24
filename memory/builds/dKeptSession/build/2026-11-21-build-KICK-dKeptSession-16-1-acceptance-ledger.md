# KICK-dKeptSession-16 — acceptance ledger

**Serves:** journal KICK-dKeptSession-16

No merge bar, no self-test suite and no gate leg ran in this pass, and no `--fixture` case ran: the
legs the spec's section 7 names were not run as commands. The criteria were observed on win32 at
the pass's base `b4b570ef` by probes of the unit's own code: `policy.py lists --write` and
`lists --check` run as commands in the policy kit; and a probe script in the session scratchpad
that builds its own scratch repositories under the system temp directory, each holding a copy of
the kit's catalogue, lists and cap census at `tools/policy`, the scaffold committed and a
remote-tracking ref at that commit, then calls `run_arm` over `arm_purposes` and the four `[[key]]`
arms in process, `seed_namespace_new` and `check_namespaces` directly, and, for the drain, a copy
holding `policy.py` and `budgets.py` too, pushed to one bare remote, whose own `policy.py lists`
it runs as a subprocess. Each new name was passed by `lexicon.py --suggest --as py.function`,
the nested `run_arm_quietly` included.

Owed to the close: every leg the spec's section 7 names; the `policy fixtures` run of the five
`purposes-*` cases, and of `legacy-homes`, `legacy-homes-main-dropped` and `legacy-homes-present`,
whose `build_legacy_repo` copy now carries `unpurposed-namespaces.txt`, of every seed case, whose
`build_repo` copy and saved files now carry it, and of `arms-empty-declared`, `arms-empty-target`
and `adopter-fresh-target`, whose "Each arm in an adopter" join now holds an `arm_purposes` row;
and the RED-first observation of the `New arm:` line, the five `purposes-*` cases in
`tools/policy/check_policy.py`, red on `purposes-new`'s planted `zz.planted`.

**Evidences:** KICK-dKeptSession-16
- AC1 — `arm_purposes` over a scratch copy with `seed_namespace_new` applied, the planted `zz.planted`: `1 finding(s) · 60 namespace(s), 14 purposed, 45 awaiting review` (DERIVED, that probe), the one finding
  `zz: a new policy namespace declares no purpose: add a [[namespace]] row`; the same copy
  unplanted, `0 finding(s) · 59 namespace(s), 14 purposed, 45 awaiting review` (DERIVED, that
  probe). With `zz` also added to the working list above the base, the one finding was the
  factory's own, `added to a shrink-only list above the base`.
- AC2 — `arm_purposes` over a scratch copy whose committed `unpurposed-namespaces.txt` lists 45 namespaces (DERIVED, that probe): no finding, and one line printed,
  `policy purposes: 45 awaiting review · actions, annotations, …`, naming every listed namespace in
  the list's order. With `actions` dropped from the working list alone, the one finding named
  `actions` with the new-namespace reason, and the line counted 44 (DERIVED, that probe).
- AC3 — `policy.py lists --check` of a copy pushed to a bare remote, its catalogue given a `[[namespace]]` row for the listed `actions`: exit 1, its one finding the stale line naming `actions`,
  `policy lists: RED · 1 finding(s)`; `lists --write` exit 0, `policy lists: wrote
  unpurposed-namespaces.txt · drained 1: actions`, the list then the base's 45 less `actions`, 44
  (DERIVED, that probe), no name gained; `lists --check` again exit 0, `policy lists: green`.
- AC4 — `check_namespaces` over a scratch copy with four `[[namespace]]` rows planted printed four findings, one per row (DERIVED, that probe): `zz-none` names no policy namespace,
  `bar` is written twice, `actions` declares an empty or absent `purpose`, `annotations` carries the
  unknown field `owner`. `load_catalogue` read 273 rows before and after (DERIVED, that probe), and
  `arm_schema`, `arm_shape`, `arm_summaries` and `arm_direction` each kept its verdict and findings.
  `arm_purposes` itself added the factory's stale finding for `annotations`, the one planted row
  with a purpose, beside the four.
- AC5 — `memory.map-purpose = "refuse"` committed in the scratch copy's `.governance/policy.toml` and the `upstream/main` ref moved to it: `arm_purposes` printed
  `policy purposes: memory.map-purpose refuse is dTotalRecall's to arm; graded as review until it lands`,
  its verdict and findings equal to the unplanted run's, which printed no such line. Committed and
  not yet landed, `ledger` printed the landed `refuse` line, so the read is the landed revision's;
  landed, `ledger` printed its own line, the verdict equal again. With the remote-tracking ref
  deleted, the one `policy purposes: NOTE - memory.map-purpose did not read (…); graded as review,
  its catalogue default` line printed, the verdict equal again.
- AC6 — `python policy.py lists --check` in the policy kit printed `policy lists: unpurposed-namespaces.txt · no comparison: tools/policy/unpurposed-namespaces.txt is absent at c2a407b0390f (merge-base of HEAD and origin/main), and absent is never an empty list`,
  green, 0 findings, since the list is new at this pass. Over the pushed scratch copy, whose base
  carries it, the line read `base … (upstream/main tip) carried 45, the list carries 45`, and 45 is
  the 59 derived namespaces less the 14 `[[namespace]]` rows (DERIVED, that probe, from the
  catalogue as built); `grep -vc "^#" unpurposed-namespaces.txt` printed 45 (DERIVED, that run).
- AC7 — `grep -n "unpurposed-namespaces.txt" policy.md` in `help/` printed lines 152 and 157 (DERIVED, that run), both in the section "What each policy namespace is for",
  whose last bullet names `memory.map-purpose`, its default `review` and the stand-in line.
- AC8 — `grep -A1 "^\[\[namespace\]\]" catalogue.toml` in the kit printed 14 `name` lines (DERIVED, that run), the 14 summarised namespaces PINNED in the spec at `c2a407b0`, re-derived
  here as the same 14 (DERIVED, at `b4b570ef`). Each purpose is derived from the summaries of its
  namespace's rows in `tools/policy/catalogue.toml`, the source rows:
  - `bar` — `bar.inline-red-fixes`.
  - `budgets` — `budgets.enforce`, `budgets.pinned`.
  - `charter` — `charter.override`, `charter.practices`.
  - `core` — `core.bypass`, `core.exceptions`.
  - `help` — `help.enforce`.
  - `install` — `install.deprecation-window`, `install.on-shim-call`, `install.retired-edits`.
  - `instructions` — `instructions.checks`, `instructions.edit`, `instructions.proof`,
    `instructions.exclude`, `instructions.stale`, `instructions.legacy`.
  - `memory` — `memory.staged-render`.
  - `pass` — `pass.fast-legs`.
  - `platforms` — `platforms.provision`.
  - `policy-file` — `policy-file.on-invalid`.
  - `review` — `review.spec-audit.disposal`, `review.spec-audit.chain-stop`,
    `review.spec-audit.chain-ceiling`.
  - `runtime` — `runtime.agents-in-flight`.
  - `tags` — `tags.slice`, `tags.retired-cites`, `tags.positional`, `tags.bare-refs`, `tags.bundle`,
    `tags.bundle-rows`.

  The other 45 namespaces carry no summarised row and stay on `unpurposed-namespaces.txt`, each
  with nothing found to derive a purpose from: `actions`, `annotations`, `asks`, `attendance`,
  `build`, `builds`, `card`, `commits`, `context`, `currency`, `decisions`, `deploy`, `deps`,
  `design`, `deviation`, `driver`, `flow`, `hooks`, `integrations`, `kickoff`, `kits`, `landing`,
  `leases`, `lexicon`, `mailbox`, `maintain`, `notices`, `notify`, `observability`, `orient`,
  `patch`, `placement`, `plan`, `probe`, `prompts`, `release`, `resume`, `retrofit`, `reuse`,
  `roles`, `run`, `tests`, `trace`, `transitions`, `verdict`. The one ask putting them to the owner
  in this build's `BACKLOG.md` is the main loop's, as S8 states, and is not filed by this pass.
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `purposes-new`: the list is compared with nothing
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `purposes-listed`: a listed namespace reds
- seen-red — `policy fixtures` — red `45016a2c4` — green `45016a2c4` — `purposes-map-purpose`: a value other than `review` said nowhere
- seen-red — `policy fixtures` — red `f6a0d7aaf` — green `f6a0d7aaf` — `purposes-shape`: the namespace rows read unchecked

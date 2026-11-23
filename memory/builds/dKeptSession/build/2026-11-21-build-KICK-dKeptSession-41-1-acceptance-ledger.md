# KICK-dKeptSession-41 — acceptance ledger

**Serves:** journal KICK-dKeptSession-41

No merge bar, no self-test suite and no gate leg ran in this pass, and the legs the spec's section 7
names were not run as commands. The criteria were observed on win32 from the pass's base `2ccd8a72`,
with units 8, 11, 17, 61 and 18 landed in it. The catalogue edit, the drained list, the reference
page and the docs list row landed in the pass's first commit; `policy.py mirror --write` then rendered
the mirror at that commit and it landed in the second, as S5 states. The reference render wrote
`help/reference/drive.md`, `help/reference/kinds.md` and `help/reference/units.md` with LF endings over
a CRLF checkout and no content change, so `git diff` read nothing in them and they were restored.

Owed to the close: every leg the spec's section 7 names, among them `policy check`, `help reference
pages`, `docs`, `recall floor`, `recall floor arms` and `memory hygiene`. The spec declares no `New
arm:` line, so no RED-first observation is owed.

**Evidences:** KICK-dKeptSession-41
- AC1 — the spec's `tomllib` probe, run in the policy kit over `catalogue.toml`, printed
  `('actions.free', 1, ['What a tool '])`, `('notify.owner', 1, ['Which events'])` and
  `('attendance', 1, ['Whether the '])`: one row per name, each summary opening with S1's text
  (DERIVED, that probe).
- AC2 — `policy.py lists --write` printed `drained 3: actions.free, attendance, notify.owner` for
  `unsummarised-keys.txt` (DERIVED, that run), and the spec's `grep -cx` over the list then printed `0`
  (DERIVED, that probe).
- AC3 — `policy.py mirror --write`, run once the catalogue edit was committed, printed `mirror written
  · 260 keys` with catalogue blob `d754425f` (DERIVED, that run); `mirror --check` at the pass's last
  commit printed `policy: mirror fresh` (DERIVED, that probe).
- AC4 — over the rendered page and the edited list, the spec's four greps printed `1`, `2`, `0` and
  `0` (DERIVED, that probe), against `0`, `0`, `3` and `3` at `edb4a01e` (PINNED 2026-11-23, the
  spec's AC4). `docs_leg.py --fingerprints` then printed `policy:notify.owner` with `42cdf26c` and
  `help/reference/policy.md` as its page, and `policy:actions.free` with `c5786fdc` and
  `policy:attendance` with `603ed07d` on their own pages, unmoved by S1's text (DERIVED, that probe).
- AC5 — `git diff --name-only` from the pass base to HEAD over the specs and acceptance ledgers of
  units 8, 11 and 17 printed nothing (DERIVED, that probe); the `tr -s` collapse of this ledger counted
  the quoted phrase 3 times and each of the three criterion names once (DERIVED, that probe), one
  entry per unit below, each quoting that unit's S1 sentence whole.

## S4 — the three units' criteria, read as observations

Units 8, 11 and 17 are CLOSED at the pass base, so their records are not written; each criterion is
answered here (spec §8 F2).

- KICK-dKeptSession-8 AC8 — its S1: "This unit writes none of the three: the row's `summary` and
  `usage` are KICK-dKeptSession-41's." The `tomllib` probe printed `dKeptSession read-only-probes`;
  `node tools/policy/policy-mirror.js get actions.free` printed `read-only-probes`; `docs_leg.py
  --fingerprints` printed `policy:actions.free` with `c5786fdc` and `help/orientation-card.md`, the
  fingerprint that page's anchor carries; and `grep -c 'policy:actions.free'` over
  `memory/project/docs-undocumented.txt` printed `0` (DERIVED, that probe).
- KICK-dKeptSession-11 AC6 — its S1: "This unit writes neither file: the row's `summary` and `usage`
  are KICK-dKeptSession-41's, so the policy mirror does not move." The `tomllib` probe printed
  `dKeptSession turn-micro-formats`, and `python tools/policy/policy.py get notify.owner` printed
  `turn-micro-formats` (DERIVED, that probe). The mirror this unit renders moves its catalogue blob
  alone; no key's value moves.
- KICK-dKeptSession-17 AC7 — its S1: "This unit writes neither file, runs no factory and moves no
  mirror: the row's `summary` and `usage` are KICK-dKeptSession-41's." The `tomllib` probe printed
  `dKeptSession unattended`; `grep -c 'usage: policy:attendance '` over `help/loop.md` printed `1`; and
  the `grep -cP` for the member's row over `memory/project/docs-undocumented.txt` printed `0` (DERIVED,
  that probe).

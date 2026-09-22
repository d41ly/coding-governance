# TOOL-aWokenSentinel-10 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-10

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule three. The pass verified with the direct checks the spec's
section 6 names: the AC1 to AC3 greps over the working tree and over `git show 12b3701d:<path>`,
check 22's three-way join read by hand — the awk-cut section 8 key column of the rendered protocol
against `grep -oE '^[A-Z_]+='` over the example and over the root conf, in the three directions the
check reports — and `bash tools/unattended/adopt-unattended.sh --check` after the render. The join
was observed RED before the row landed: the two edited confs against the protocol at `HEAD`
(`3853a7da`) read `undocumented: [STOP_GUARD_BLOCKS]` and `proj_extra: [STOP_GUARD_BLOCKS]`; the
same confs against the rendered protocol at the tip read all three directions empty. Those stand in
for the `unattended kit gate` (check 22 the join, check 10 the render parity), `unattended skill
wiring`, `kickoff-manifest ratchet`, `memory hygiene` and `spec tokens` legs, which run once at the
close.

**Evidences:** TOOL-aWokenSentinel-10
- AC1 — `grep -c '^STOP_GUARD_BLOCKS="6"$' tools/unattended/.unattended.conf.example` printed `1` at the tip and `0` over `git show 12b3701d:tools/unattended/.unattended.conf.example`; `grep -c 'STOP_GUARD_BLOCKS' tools/unattended/kit.toml` printed `1` at the tip, the `optional_keys` line, and `0` at base; the line above the key in the example starts with `# the stop-guard blocks a bound session'`; `grep -oE 'BLOCKS_DEFAULT = [0-9]+' tools/unattended/stop-guard.js` printed `BLOCKS_DEFAULT = 6`, one default. OBSERVED.
- AC2 — the section 8 region of `memory/guides/UNATTENDED-PROTOCOL.md`, cut by `awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f'`, grepped for `STOP_GUARD_BLOCKS` printed `1` at the tip and `0` over `git show 12b3701d:memory/guides/UNATTENDED-PROTOCOL.md`; the same over `tools/unattended/PROTOCOL.template.md` printed `1`. The join by hand at the tip: example keys 38, root conf keys 37, section 8 key column 38; `undocumented` (example minus table) empty, `phantom` (table minus example) empty, `proj_extra` (root conf minus table) empty. The same join with the row withheld — the edited confs against `git show HEAD:memory/guides/UNATTENDED-PROTOCOL.md` — read `undocumented: [STOP_GUARD_BLOCKS]` and `proj_extra: [STOP_GUARD_BLOCKS]`, the two lines check 22 would print. `node -e` over `run-lease.js`'s `readBoundKey(root, 'STOP_GUARD_BLOCKS', 6)` at the tip printed `{"value":6,"source":"declared","raw":"6"}`, so the hook on this repo reads the declared line and prints no NOTE. OBSERVED; check 22 itself `observed at --close`.
- AC3 — `grep -c '^STOP_GUARD_BLOCKS="6"$' .unattended.conf` printed `1` at the tip and `0` over `git show 12b3701d:.unattended.conf`; the line above it starts with `# the stop-guard blocks a bound session'` and closes with `TOOL-aWokenSentinel-10.`; the pass commit stages `.unattended.conf` together with `memory/guides/SESSION-KICKOFF.md`, whose `last-audit` moved from `2026-09-20T20:53:11+03:00 @ 4cf0944d…` to `2026-09-20T22:36:30+03:00 @ 4cf0944d…` — `git merge-base origin/main HEAD` at the commit, the ratchet's rule for a run branch — and whose message carries `manifest-audit: delta none · watch-commits-since-stamp: 1`, the `git rev-list --count 4cf0944d..HEAD -- <watch…>` read before re-stamping. The commit's file list is read by `git show --name-only --format= HEAD` after it lands; the `kickoff-manifest ratchet` is `observed at --close`. AMENDED at rev-3: the stamp rule read "the commit's parent or a later sha", which the ratchet's `STAMP_SHA_RULE` contradicts on a run branch; the spec's §9 line carries it.
- AC4 — `bash tools/unattended/adopt-unattended.sh` re-rendered the protocol and the Skill, then `bash tools/unattended/adopt-unattended.sh --check` printed `unattended: in sync (skill rendered from template + .unattended.conf)` and exited 0. OBSERVED; check 10's byte-compare `observed at --close`.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, ratchet leg or `*.test.sh` suite ran inside this pass;
every one is `--close`'s and each row above says so. No arm was added: check 22 is the existing arm
and this unit is the row it was reading for. No identifier was minted. `memory/LIVE.md` and
`memory/ledger/2026-09.md` were not declared: `--dispatch` refused the first declaration because
unit 16's row on `memory/LIVE.md` never closes (its pass never wrote it), and neither index moves for
a unit status flip — both key the BUILD, which stays `SPECCED` until the close. The build README's
authored roster row for this unit moved `PLANNED` to `CLOSED` beside the spec header.

## The guide cap, an exemption and its compensating check

The first commit attempt was refused by the pre-commit's staged hygiene pass: check 6,
`memory/guides/UNATTENDED-PROTOCOL.md (61633B 683L > 61440B/750L)`. The render sat at 61345 B at
`3853a7da`, 95 B under `GUIDE_CAP_BYTES`, and the one row this unit owes is 288 B. The pass added
a `memory/project/curation-debt.txt` row for the render — the escape `memory/HYGIENE.md` check 6
declares, check-6-only on a guide — and parked the owner call (raise the cap, or split the
protocol) on the run-state record as `guide-cap TOOL-aWokenSentinel-10`, with the four options and
the refusals stated there. Compensating check: `bash tools/memory-tree/check-memory-hygiene.sh
--staged` printed no `FAILED` line and exited 0 with the row staged; the registry's stale-row guard
reds the row the run the render fits again. The declaration was dispatched as a second `--writes`
row before the registry was touched. This is an exemption and not coverage: the protocol is 193 B
over what the owner declared a session should read, and unit 6's section 5 prose lands on it next.

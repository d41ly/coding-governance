# Spec brief — TOOL-aDeferredBar-2 — the spec gate: a bar or suite is not an acceptance observation

**Serves:** journal TOOL-aDeferredBar-2

The writer authors `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-2.md` at
Tier 2 against `memory/TEMPLATE-SPEC.md`. Read the research record under `build/` whole first;
its section 1 (carrier A) and section 3 (candidate C1) are this unit.

## The mechanism, in one sentence

`tools/check-spec-tokens.py` gains a FOURTH join, `bar`: in a non-terminal spec whose filename
date is at or after a new `.memory-tree.conf` cutoff, a backticked token inside a `## 6.
Acceptance criteria` bullet, or on the `## 7. Gates` leg line, that spells a merge-bar or
self-test-suite invocation is a HIT, waivable through the existing
`memory/project/spec-token-waivers.txt` under a `[bar]` kind.

## What the predicate matches, and what it deliberately does not

A backticked token carrying any of: `run-gates.sh` (any path prefix, with or without `bash`),
a `GATE_FULL=` or `GATE_SELFTESTS=` assignment, `run-selftests.sh`, `run-unattended-gates.sh`,
or a token ending in `.test.sh`. It reads the SAME populations the `paths` and `legs` joins
already extract — the AC bullets of section 6 and the leg-list line of section 7 — so a mention
in prose, in section 4, in a `New arm:` line (which is prose by that join's own rule and is
exactly where a suite path belongs), or in a fenced block is NOT a hit. Near-misses are printed
under `--list`, as the other joins print theirs.

The refusal message names the substitute: observe the checker on a staged break, a `--selftest`
flag, or a fixture; name the suite under `New arm:`; the bar and the suites run once, after the
build is complete.

## The cutoff, and why it is required rather than tidy

Measured on 2026-09-13 over every tracked spec: **25 non-terminal specs** across eleven builds
carry such a token today, the newest dated 2026-09-04, and none is this build's to rewrite. So
the join is date-gated on the spec's FILENAME date by a new key — suggested spelling
`SPEC_DIRECT_CUTOFF`, beside `SPEC_LEGLINE_CUTOFF` in `.memory-tree.conf`, read through the
existing `read_conf_key` — set to `2026-09-13`. BLANK or absent turns the join OFF and the checker
ANNOUNCES that on every run rather than passing silently; that is the idiom every sibling cutoff
uses, and section 4 cites the one in `tools/check-spec-tokens.py` at `LEGLINE_KEY`.

## The write set (section 4 files table)

1. `tools/check-spec-tokens.py` — the join, its `--list` reporting, the header's WHAT IT DOES NOT
   CHECK paragraph gaining the fourth population, the printed graded count.
2. `tools/check-spec-tokens.test.sh` — arms: a fixture spec dated after the cutoff with a bar
   token in an AC bullet REDS naming `[bar]`; the same token in section 4 prose is NOT a hit; a
   `.test.sh` path under `New arm:` is NOT a hit; a spec dated before the cutoff is NOT graded and
   the skip is announced; a `[bar]` waiver row clears a hit and a stale one refuses. Run the SUITE
   ONLY IF it is seconds — measure first with `time`; if it is not, observe each arm by running
   `python tools/check-spec-tokens.py` on the fixture directly and say so in the ledger.
3. `.memory-tree.conf` — the new key, with a comment in the register of its neighbours: what it
   gates, why the date is the landing date, what BLANK does.
4. `tools/memory-tree/SPEC-TEMPLATE.template.md` — one paragraph under the §6 rules, beside the
   `SPEC_WITNESS_CUTOFF` and `SPEC_FAILURE_MODE_CUTOFF` paragraphs, stating the rule and the
   substitute; rendered to `memory/TEMPLATE-SPEC.md`. `KIT_MEMORY_TREE_VERSION` and the render
   marker move together, one step past wherever unit 1 left them.
5. `memory/project/spec-token-waivers.txt` — only if the join's first real run over the tree finds
   a hit dated at or after the cutoff that is not this build's; expected empty.

NOT in the write set: the memory hygiene gate (this join lives in the spec-token checker, one
mechanism); any live spec of another build (the cutoff excludes them by construction).

## The acceptance criteria — direct, or this unit reds its own gate

Each criterion names a backticked command whose output IS the observation:
`python tools/check-spec-tokens.py` exit 1 with `[bar]` in stdout over a staged fixture;
`python tools/check-spec-tokens.py --list` printing the near-miss count; the OFF announcement with
the key blanked in a scratch conf; `bash tools/check-kit-versions.sh` exit 0. NOT ONE criterion
names the bar, a `GATE_*=` prefix, or the suite as its observation — this unit's own spec is the
first document the new join grades, and it must pass it.

§7 leg line: `spec tokens (a spec's own names resolve)` · `memory hygiene` · `kit version
markers` · `verdict epoch (kit version dates the engine)` · `kit/dogfood doc parity` if that leg
exists in `tools/gate-legs.json` (verify with `--list`; drop it if not).

## Resolved forks — mark RESOLVED (agent, 2026-09-13, delegated)

- **Hygiene check vs spec-token join** → the spec-token checker, which already extracts both
  populations and owns the waiver file.
- **Ban `*.test.sh` in an AC, or only the unattended suites** → every suite: the owner's third
  sentence names the class, and the ledger shows `govkit selftest` at 3445 s and
  `manifest-check self-test` at 2162 s beside the unattended pair.
- **Cutoff or drain** → cutoff at the landing date; the 25 live specs are other builds'.

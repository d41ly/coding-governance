**Serves:** research PLAY-dOrderedCharter-1

# The parents' specs: what dOrderedCharter's re-ground found off, and where each is fixed

Node d, 2026-10-25, base `c63aabbb4` (origin/main). The cross-check record
([2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck.md](2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck.md))
and the five spec writers of the re-ground
([2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md))
named things in dSafePassage's and dGroundRules' specs that look wrong or missing. The owner asked for
them audited and fixed where possible. This record is that audit, and each item says where it is fixed.

## Who may be edited

- **dSafePassage** — its run claim `refs/gov/runs/dSafePassage` last beat 2026-10-23 09:42, and no branch
  of it moved since its specs landed at `5e2007467`, so its specs are fixed here, in this commit, by
  `../../dSafePassage/prompts/2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`.
- **dGroundRules** — its run claim beat 2026-10-25 00:35, and its unattended build run's branch
  `origin/branch/unattended-dgroundrules-e47ae1` holds 117 unlanded commits at `df4912bd`, building
  `tools/policy/` and revising 64 of its spec files. No dGroundRules file is touched here. Each of its
  items is either answered by that branch's built code or fixed inside dOrderedCharter's own scope.

## The items

| # | What looks off | Verdict | Where it is fixed |
|---|---|---|---|
| P1 | dGroundRules unit 9's `budgets.py` has only `resolve` and `check`; a `constant:` home's value comes back only when the caller hands it in, so dOrderedCharter specs 6 and 11 each parse the `codex-instructions` census row | real: two readers of one row | dOrderedCharter spec 6, the first caller by build order, adds `budgets.py home <cap>`; specs 11 and 34 call it |
| P2 | dSafePassage unit 1 S8 rewrites seven `caps.toml` rows to a `policy` home form; dGroundRules unit 9 defines four forms, and the built `budgets.py` holds `HOME_FORMS = ("limits", "file", "conf", "constant")` | real: S8 writes a form no reader admits | dSafePassage unit 1 adds the form |
| P3 | dSafePassage unit 9's `read_policy_value(key, root)` takes no revision, so a govkit reader cannot read at `--rev HEAD` | real | dSafePassage unit 9 gives it `rev=None`; dOrderedCharter spec 33 reads `instructions.stale` with `rev="HEAD"` |
| P4 | dOrderedCharter spec 32's overlay `[[policy]]` rows: dGroundRules units 5 and 19 key the mirror and the guard's mirror shape on the policy file and the catalogue only | real, in spec 32's own extension | dOrderedCharter spec 32 names the mirror and guard half |
| P5 | dGroundRules unit 1 (`:69-71`) refuses a member v2 admits as "registered" or "repo-declared" | answered by the build: the built catalogue gives `charter.practices` and `instructions.exclude` an `item` pattern, and the built `check_value` admits a member it matches | evidence in dOrderedCharter specs 1 (F4) and 36 |
| P6 | dGroundRules unit 6 S3 admits an agent's raise only where the cap's last segment is a tracked file, so `memory/builds/*/spec/` is never raised by an agent | intended: a class cap is the owner's | no change |
| P7 | dSafePassage unit 1 S9 freezes the bytes of a program a landed argv names, not the modules it imports | real gap, kept on purpose: dOrderedCharter spec 31 keeps its class reader in an imported module | dSafePassage unit 1 states it |
| P8 | dSafePassage unit 13's row sources are a closed list, its hand-off asks later builds to restate members' rows (against its S2), and a `none`-shape class's `rows` spelling is unstated | real | dSafePassage unit 13 |
| P9 | dSafePassage unit 9's arm takes engine rows only; the seed override (`tools/govkit/govkit.py:9988-10000`) grades an edited seeded copy gov stops shipping `patched` with no order | real; the owner picked spec 31 F7 (a) | dSafePassage unit 9, so no ask is filed |
| P10 | dSafePassage unit 6 (`:89-91`) names dOrderedCharter's `map_lib` re-export among the first shim rows | real; the owner picked spec 31 F6 (a) | dSafePassage unit 6, so no ask is filed |
| P12 | dSafePassage unit 26 is 54423 bytes against the 49152 class cap, and `tools/template-size-highwater.txt` holds no row for it, so the size join reds it once it is live | real, found by this audit's size sweep | dSafePassage unit 26, trimmed in its prose |
| P11 | dOrderedCharter specs 35 and 36 call `instructions.exclude`'s default `none`; the built catalogue holds `default = []`, `empty = "allowed"` | real, dOrderedCharter-side | dOrderedCharter specs 35, 36 and 46 |

The owner-forks brief's item 6 placed the verb in spec 11. Its writer moved it to spec 6, which builds
first (order 19 against 21) and is the verb's first caller, so no edge consumes a unit that lands later;
spec 6's §8 F5 records it.

## What this does not check

- dGroundRules' built code beyond the four files read for P1, P2, P5 and P11 (`budgets.py`,
  `policy.py`'s `check_value`, `caps.toml`'s home lines, two `catalogue.toml` rows). Its run lands
  later; the re-ground's assumptions about its interfaces want one more read against what it lands.
- Whether the dSafePassage revisions hold together beyond the items named; no audit or review ran.

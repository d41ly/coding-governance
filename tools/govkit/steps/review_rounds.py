#!/usr/bin/env python3
"""review_rounds.py — the upgrade step `unattended/review-rounds-to-policy` (TOOL-dDeclaredLoop-21, S7).

    python <prefix>/govkit/steps/review_rounds.py up|down|witness <target>

Its row is the unattended descriptor's `[[upgrade]]`. The UP takes `.unattended.conf`'s
`REVIEW_ROUNDS`, the spec audit's round bound the driver no longer reads, out of the conf once the
policy keys that now carry it read the same bound, and it never writes the policy file, which stays
the owner's (TOOL-dDeclaredLoop-56 S40); the DOWN restores the conf byte-identical; the WITNESS exits
0 when no `REVIEW_ROUNDS` assignment is left in the conf, or there is no conf, which is the step applied.

THE UP, in order. No `.unattended.conf`, or no `REVIEW_ROUNDS` line in it: exit 0, nothing written.
Otherwise the conf is read in `conf_to_policy.py`'s grammar, the last assignment winning and a blank
reading as unset. The up exits 1 WRITING NOTHING on a value that is not an integer of at least 1, or
where the conf or the policy file differs from its blob at HEAD. An unset value and 1 are the
catalogue's default, `review.design.rounds = "one"`, and map to no key. A value N above 1 maps to
`review.design.rounds = "fixed-count"` and `review.design.round-count = N`, and `review.max-rounds = N`
where N exceeds the catalogue's ceiling of 3, since the loop kit refuses a fixed count above the
ceiling. The policy file is parsed with `tomllib`, an absent one setting nothing: each mapped key it
does not set prints `policy_edit.py set <key> <value>` for the owner to run, each it sets to another
value prints `conflict · <key> · policy <value> · conf <value>`, and either exits 1 WRITING NOTHING,
the conf line kept. Once every mapped key reads its value, every `REVIEW_ROUNDS` line is taken out of
the conf, which is kept; the before-image lists the conf alone. A re-run over a killed up recomputes
from the first before-image and converges.

Exit 0 done, 1 refused naming the file or a policy key proposed or in conflict (nothing written), 2 a
usage error.
"""

import importlib.util
import pathlib
import sys
import tomllib

STEP_ID = "unattended/review-rounds-to-policy"
CONF = ".unattended.conf"
KEY = "REVIEW_ROUNDS"
POLICY = ".governance/policy.toml"
CEILING_DEFAULT = 3  # the catalogue's `review.max-rounds` default


def load_conf_to_policy():
    """The shared step helpers beside this file, imported by their path: the runner's `-I` drops
    this file's own directory from `sys.path`."""
    path = pathlib.Path(__file__).resolve().parent / "conf_to_policy.py"
    mod = sys.modules.get("conf_to_policy")
    if mod is not None and getattr(mod, "__file__", None) and pathlib.Path(mod.__file__).resolve() == path:
        return mod
    spec = importlib.util.spec_from_file_location("conf_to_policy", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["conf_to_policy"] = mod
    spec.loader.exec_module(mod)
    return mod


C2P = load_conf_to_policy()
Refusal = C2P.Refusal


def derive_settings(n: int | None) -> list:
    """The `(table, key, value)` rows the bound `n` writes: none for the default."""
    if n is None or n == 1:
        return []
    rows = [("review.design", "rounds", "fixed-count"), ("review.design", "round-count", n)]
    return rows + ([("review", "max-rounds", n)] if n > CEILING_DEFAULT else [])


def cmd_up(target: pathlib.Path) -> int:
    conf = target / CONF
    if not conf.is_file() or not C2P.check_assigned(conf.read_bytes(), KEY):
        print(f"review-rounds: up · no {KEY} in {CONF} at {target.as_posix()}, so there is nothing to move")
        return 0
    rows = derive_settings(C2P.parse_conf(conf.read_bytes(), CONF, KEY))
    for rel in (CONF, POLICY):
        if not C2P.check_committed(target, rel):
            raise Refusal(f"{rel}: differs from its blob at HEAD, and the policy reader reads "
                          f"committed revisions only; commit it, then re-run the step")
    # THE OWNER WRITES THE POLICY FILE (TOOL-dDeclaredLoop-56 S40): each mapped key the file does not set
    # is a proposal, and each it sets otherwise a conflict; either writes nothing and exits 1.
    pol = target / POLICY
    # ponytail: a policy file that does not parse raises here; the policy leg grades that file at HEAD.
    held = tomllib.loads(pol.read_bytes().decode("utf-8")) if pol.is_file() else {}
    owed = []
    for table, key, value in rows:
        node = held
        for part in table.split("."):
            node = node.get(part) if isinstance(node, dict) else None
        have = node.get(key) if isinstance(node, dict) else None
        if have is None:
            owed.append(f"policy_edit.py set {table}.{key} {value}")
        elif have != value:
            owed.append(f"conflict · {table}.{key} · policy {have} · conf {value}")
    if owed:
        for line in owed:
            print(line)
        print(f"review-rounds: up · {POLICY} does not set every key {CONF}'s {KEY} maps to; run each "
              f"policy_edit.py line above, settle each conflict, commit, then re-run the step; nothing written")
        return 1

    def derive_after(before):
        return {CONF: C2P.render_conf_rest(conf.read_bytes() if before is None else before[CONF], KEY)}

    after = C2P.STEPS.write_before_image(target, STEP_ID, derive_after)
    conf.write_bytes(after[CONF])  # the witness reads the line's absence
    print(f"review-rounds: up · {CONF} kept, its {KEY} taken out"
          + (f" · {POLICY} already sets the review bound keys" if rows else
             f" · its bound is the catalogue default, so {POLICY} is unchanged"))
    return 0


def cmd_down(target: pathlib.Path) -> int:
    restored = C2P.STEPS.write_from_before_image(target, STEP_ID)
    print(f"review-rounds: down · restored {', '.join(restored) or 'nothing: no before-image, no up applied'}")
    return 0


def cmd_witness(target: pathlib.Path) -> int:
    conf = target / CONF
    held = conf.is_file() and C2P.check_assigned(conf.read_bytes(), KEY)
    print(f"review-rounds: witness · {CONF} " + (f"assigns {KEY}: not applied" if held else
                                                f"assigns no {KEY}, or is absent: applied"))
    return 1 if held else 0


def main(argv: list[str]) -> int:
    verbs = {"up": cmd_up, "down": cmd_down, "witness": cmd_witness}
    if len(argv) != 2 or argv[0] not in verbs:
        sys.stderr.write("usage: python review_rounds.py up|down|witness <target>\n")
        return 2
    try:
        return verbs[argv[0]](pathlib.Path(argv[1]).resolve())
    except Refusal as e:
        sys.stderr.write(f"review-rounds: {argv[0]} refused · {e}\n")
        return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    raise SystemExit(main(sys.argv[1:]))

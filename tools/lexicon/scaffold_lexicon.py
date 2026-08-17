#!/usr/bin/env python3
"""scaffold_lexicon.py — DERIVE a proposed `.lexicon.conf` from the adopting repo's own corpus.

Called by `tools/lexicon/adopt-lexicon.sh --scaffold`; not a user-facing entry point.

The seed is derived and then FROZEN. For one moment a derived table is exactly the hand-kept mirror
companion §12 bans, and the resolution is procedural rather than clever: mark it PROPOSED, leave
`ratified` empty, and let `--check` red until a human has curated it. What this file must NOT do is
pretend the derivation is the answer — the frequency ranking is a starting vocabulary, and the rows
that make a verb table worth having are the NEGATIVE definitions a human writes.

`LAYERS` is deliberately seeded EMPTY. There is no `--scaffold` proposal for P3: an import-direction
map is a statement about intended architecture, and a frequency count cannot observe intent. An
empty `LAYERS` makes the engine report NOT ARMED and red, which is the fail-closed behaviour the
unit spec requires — a fresh adopter gets a refusal that names what to declare, never a green run
over a predicate that is not checking anything.
"""

import collections
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lexicon as lex  # noqa: E402

#: How many leading tokens to propose. Not a tuning knob so much as a legibility bound: a table
#: nobody reads is not closed in any sense that matters.
SEED_VERBS = 25

#: Extensions this kit can extract today. Everything else present in the corpus is seeded `dark`,
#: which is a DECLARATION, not a gap — it is named on every run rather than silently absent.
KNOWN = {"py": ("python-ast", "parser"), "js": ("js-regex", "probe")}

HEADER = """\
# .lexicon.conf — the naming lexicon this repo declares. Read by tools/lexicon/lexicon.py through
# tools/lexicon/lexicon_conf.py, which is the ONE reader; nothing else parses this file.
#
# GRAMMAR: single-line keys use the sibling KEY=VALUE form (`.memory-tree.conf`, `.codebase-map.conf`
# ) — a value with spaces is double-quoted and no comment follows it on the line. Block keys are a
# `KEY:` header followed by INDENTED rows, ending at the first non-indented line.
#
# THIS FILE WAS DERIVED AND IS MARKED **PROPOSED**. The verb table below is a frequency ranking of
# what this corpus already does, which is a mirror of the code, not a vocabulary. Curate it: delete
# the verbs you do not mean, and give the ones you keep their NEGATIVE definitions — `build` not
# `create`, `load` not `fetch`. Those are the rows that make the table worth gating. Then stamp
# `ratified=` and the gate stops refusing.
"""


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: scaffold_lexicon.py <conf-path>\n")
        return 2
    dest = Path(argv[1])
    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                               capture_output=True, text=True, check=True).stdout.strip())
    files = lex.tracked_files(root)

    exts = sorted({lex.ext_of(f) for f in files})
    langs = [f"{e}:{KNOWN[e][0]}:{KNOWN[e][1]}" if e in KNOWN else f"{e}::dark" for e in exts]

    counts: collections.Counter = collections.Counter()
    types_seen = 0
    for rel in files:
        ext = lex.ext_of(rel)
        if ext not in KNOWN:
            continue
        pset, mode = KNOWN[ext]
        try:
            got = lex.extract(root / rel, mode, pset)
        except (SyntaxError, OSError):
            continue
        if not got:
            continue
        funcs, types_, _ = got
        types_seen += len(types_)
        for name, _ln in funcs:
            v = lex.leading_verb(name)
            if v:
                counts[v] += 1

    # ALPHABETIC only. `leading_verb` can return a digit run (`2fa_check` -> `2`), and the conf
    # reader REFUSES a non-alphabetic verb row — so an unfiltered seed could write a file its own
    # reader rejects, which is the worst possible first experience of a kit.
    seeded = [v for v, _n in counts.most_common() if v.isalpha()][:SEED_VERBS]
    total_defs = sum(counts.values())
    verb_offenders = sum(n for v, n in counts.items() if v not in set(seeded))

    body = [HEADER, ""]
    body.append('# Type-name suffixes that name a responsibility nobody scoped. Seeded from the source')
    body.append('# charter\'s eight; edit freely — this one is safe to inherit because it is prescriptive.')
    body.append('BANNED_SUFFIXES="Manager Helper Util Utils Handler Processor Data Info"')
    body.append("")
    body.append("# <ext>:<pattern-set-id>:<mode>, one per extension PRESENT in this corpus. An extension")
    body.append("# here with no declaration is a named refusal, never a silent skip.")
    body.append(f'LANGS="{" ".join(langs)}"')
    body.append("")
    body.append("# MEASURED against this corpus at scaffold time, AGAINST THE DERIVED SEED BELOW —")
    body.append("# which you are about to rewrite. Re-measure after curating:")
    body.append("#     python tools/lexicon/lexicon.py --measure")
    body.append("# Shrink-only thereafter: the count may fall, never rise. A pin copied from a larger")
    body.append("# tree is either vacuous or permanently red.")
    body.append(f'VERB_OFFENDER_PIN="{verb_offenders}"')
    body.append('SUFFIX_OFFENDER_PIN="0"')
    body.append('LAYER_OFFENDER_PIN="0"')
    body.append("")
    body.append("# The date and node that CURATED the seed below. While this is empty,")
    body.append("# `adopt-lexicon.sh --check` reds: an underived table nobody edited is a mirror of the")
    body.append("# code, and that is the one shape a naming gate must not have.")
    body.append('ratified=""')
    body.append("")
    body.append(f"# PROPOSED — derived from {total_defs} definition(s) across {len(files)} tracked file(s).")
    body.append("# Meanings are BLANK on purpose: writing them is the curation this seed is asking for.")
    body.append("VERBS:")
    for v in seeded:
        body.append(f"  {v}")
    body.append("")
    body.append("# FORBIDDEN import directions, `<glob> -> <glob>`. Seeded EMPTY and the gate REDS until")
    body.append("# you declare one: a frequency count cannot observe intended architecture, so there is")
    body.append("# no derived proposal for this predicate. Declare the direction you actually mean, e.g.")
    body.append("#   src/core/* -> src/adapters/*")
    body.append("LAYERS:")
    body.append("")

    # newline="" — write LF, never the platform default. `write_text` translates `\n` to `\r\n` on
    # Windows, and a CRLF conf INVERTS the unratified-seed refusal: `adopt-lexicon.sh` strips the
    # trailing quote with an anchored `s/"$//` that a carriage return defeats, leaving `"\r`, which
    # reads as a non-empty `ratified` value. The seed then passes the one check that exists to stop
    # an uncurated table reaching the merge bar. Caught by the scaffold arm in selftest.py.
    with open(dest, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(body))
    print(f"scaffold: {len(seeded)} verb(s) proposed from {total_defs} definition(s); "
          f"VERB_OFFENDER_PIN={verb_offenders}; {types_seen} type definition(s) scanned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

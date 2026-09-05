#!/usr/bin/env python3
"""scaffold_lexicon.py — DERIVE a proposed `.lexicon.conf` from the adopting repo's own corpus.

Called by `tools/lexicon/adopt-lexicon.sh --scaffold`; not a user-facing entry point.

WHAT IS DERIVED HERE IS MEMBERSHIP, NOT SPELLING. The corpus is asked one question per cluster —
does any form of this concept have a live definition site — and the answer seeds the cluster's
representative from `canon.py`, which is element 0 unconditionally. A frequency ranking was the
first cut and was the defect: it adopted whatever the repo already did most, so the gate certified
the habit it was installed to change, and all six of the owner's deliberately-bad names passed.

The seed is still marked PROPOSED with `ratified` empty, because a canon-sourced table is a
starting vocabulary and not a curated one — but it is no longer the hand-kept mirror companion §12
bans, because its vocabulary comes from outside the tree it grades.

THERE IS NO IMPORT-DIRECTION SEED, and since TOOL-aSurfacedLexicon-2 there is nothing to seed: the
declared `LAYERS` predicate is deleted. The one constraint it really held — the kit imports nothing
outside the stdlib and its own directory — is now a refusal inside the engine, derived from the
kit's own source, so it needs no declaration and cannot be scaffolded wrong.
"""

import collections
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import canon
import lexicon as lex  # noqa: E402

#: Extensions this kit can extract today, READ FROM THE ENGINE rather than restated. Everything else
#: present in the corpus is seeded `dark`, which is a DECLARATION, not a gap — it is named on every
#: run rather than silently absent. The two copies had already diverged on the `py` pattern-set id
#: within one build — a real divergence with no observable consequence, since nothing compares a
#: pattern-set id against `""`. Collapsed because two carriers of one fact is the defect, not because
#: this one had bitten. Closing review M7, trimmed by round 2.
KNOWN = lex.KNOWN_EXTS

HEADER = """\
# .lexicon.conf — the naming lexicon this repo declares. Read by tools/lexicon/lexicon.py through
# tools/lexicon/lexicon_conf.py, which is the ONE reader; nothing else parses this file.
#
# GRAMMAR: single-line keys use the sibling KEY=VALUE form (`.memory-tree.conf`, `.codebase-map.conf`
# ) — a value with spaces is double-quoted and no comment follows it on the line. Block keys are a
# `KEY:` header followed by INDENTED rows, ending at the first non-indented line.
#
# THIS FILE WAS DERIVED AND IS MARKED **PROPOSED** — but the table below is NOT a ranking of what
# this corpus already does. Every row is a representative from the kit's frozen canon, carrying the
# negative definition the canon states. The corpus only VOTED on which concepts are live here; it
# could not promote a spelling it happens to prefer, and it could not nominate a verb the canon does
# not hold. That is the whole difference between a vocabulary and a mirror. Curate it anyway: delete
# the rows you do not mean, add the ones your domain needs, then stamp `ratified=` and the gate
# stops refusing.
"""



#: Authored ONCE. This tuple and the `BANNED_SUFFIXES=` line the scaffold emits were two copies of
#: one list, so a curated eighth entry here would have measured a pin against a set the emitted
#: declaration did not carry. Closing review L2.
BANNED_SUFFIXES = ("Manager", "Helper", "Util", "Utils", "Handler", "Processor", "Data", "Info")


def _measure_suffix_offenders(scanned) -> int:
    """Type definitions ending in a banned suffix, over the SAME scan the verb pin uses.

    It takes the scan rather than the repo root, and that is the whole of this unit's change here.
    It used to walk the corpus a second time — its own `git ls-files`, its own `extract` per file —
    to answer a question the first walk already had the definitions for. Two walks over one tree is
    also two chances to disagree about which files are armed.
    """
    banned = BANNED_SUFFIXES
    n = 0
    for _rel, _ext, got, _problem in scanned:
        if got is None:
            continue
        for name, _ln in got[1]:
            if any(name.endswith(b) for b in banned):
                n += 1
    return n


def main(argv: list[str]) -> int:
    # A FLAG IS NOT A PATH, and the guard here used to be an ARITY check alone.
    # `scaffold_lexicon.py --help` is a well-formed one-argument call, so `--help` became the
    # DESTINATION: this script derived a whole seed and wrote it to a file literally named
    # `--help`. Measured on a real adopter (incms/main, 2026-08-23), where that file was
    # committed, pushed, and then survived every leg of a 62-leg bar. Nothing downstream can
    # see it -- `adopt-lexicon.sh --check` looks for `.lexicon.conf` BY NAME, so a stray sibling
    # is invisible to it -- and a file whose name is a flag breaks every unquoted glob in its
    # directory from then on. The WRAPPER already refuses an unknown flag; this script is the
    # one that WRITES, so the refusal has to be here too. `./--help` still reaches a genuine
    # leading-dash path, which is the usual convention.
    if len(argv) != 2 or argv[1].startswith("-"):
        sys.stderr.write("usage: scaffold_lexicon.py <conf-path>\n")
        if len(argv) == 2:
            sys.stderr.write(f"scaffold_lexicon.py: {argv[1]!r} is a flag, not a destination "
                             f"-- this script takes one conf PATH and has no options of its "
                             f"own.\n")
        return 2
    dest = Path(argv[1])
    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                               capture_output=True, text=True, check=True).stdout.strip())
    # THE ONE WALK, and every figure below comes out of it. There used to be two — this function's
    # and `_measure_suffix_offenders`'s — each re-deriving which extensions are armed and each
    # SWALLOWING an extraction failure, so an unparseable file was invisible here while `run()`
    # refused the same file by name. `scan_corpus` owns that decision now and reports it; nothing
    # below is allowed to drop it on the floor.
    scanned = list(lex.scan_corpus(root, KNOWN))
    files = [rel for rel, _e, _d, _p in scanned]
    refused = [p for _r, _e, _d, p in scanned if p]
    for _p in refused:
        sys.stderr.write(f"scaffold: NOT EXTRACTED - {_p}\n")

    exts = sorted({ext for _r, ext, _d, _p in scanned})
    # S8 — `conf` is seeded UNCONDITIONALLY, present or not. This scaffold runs BEFORE the file it
    # writes is tracked, so the extension it is about to create cannot be in `exts` — and the
    # adopter's very first `git add .lexicon.conf` then reds with UNDECLARED EXTENSIONS. Every fresh
    # adoption hit that in its first five minutes (TOOL-dScaffoldedMirror-1's second finding).
    exts = sorted(set(exts) | {"conf"})
    langs = [f"{e}:{KNOWN[e][0]}:{KNOWN[e][1]}" if e in KNOWN else f"{e}::dark" for e in exts]

    # S2 — WHICH CLUSTERS enter is decided by the corpus; WHICH FORM represents one is decided by
    # the canon, always element 0. Two questions, two deciders. The frequency ranking this replaces
    # answered both with the corpus, which is why it legalised whatever a repo already did most.
    forms = canon.build_form_index()
    counts: collections.Counter = collections.Counter()   # surface form -> live sites
    types_seen = 0
    for _rel, _ext, got, _problem in scanned:
        if got is None:
            continue
        funcs, types_, _ = got
        types_seen += len(types_)
        for name, _ln in funcs:
            v = lex.leading_verb(name)
            if v:
                counts[v] += 1

    total_defs = sum(counts.values())
    suffix_offenders = _measure_suffix_offenders(scanned)
    # A cluster enters when ANY of its forms has a live site. The corpus votes on membership and
    # nothing else: it cannot promote a spelling, and a token in no cluster cannot enter at all.
    live = {forms[v] for v in counts if v in forms}
    seeded = [rep for rep, _gloss, _others in canon.CLUSTERS if rep in live]
    # DEBT, which is the corpus's one other job here: every live site spelled as a non-first form.
    debt = sorted(((v, n) for v, n in counts.items() if v in forms and forms[v] != v),
                  key=lambda kv: (-kv[1], kv[0]))
    verb_offenders = sum(n for v, n in counts.items() if v not in set(seeded))

    body = [HEADER, ""]
    body.append('# Type-name suffixes that name a responsibility nobody scoped. Seeded from the source')
    body.append('# charter\'s eight; edit freely — this one is safe to inherit because it is prescriptive.')
    body.append('BANNED_SUFFIXES="%s"' % " ".join(BANNED_SUFFIXES))
    body.append("")
    body.append("# <ext>:<pattern-set-id>:<mode>, one per extension PRESENT in this corpus. An extension")
    body.append("# here with no declaration is a named refusal, never a silent skip.")
    body.append(f'LANGS="{" ".join(langs)}"')
    body.append("")
    body.append("# BOTH MEASURED against this corpus at scaffold time. The verb pin counts every")
    body.append("# definition whose leading token is outside the proposal; the suffix pin counts its own")
    body.append("# offenders. They used to be hardcoded `0` under a comment that called them measured, so")
    body.append("# a corpus with one `Manager` type scaffolded green and redded on its first gate run,")
    body.append("# against a pin the tool itself had written (TOOL-dScaffoldedMirror-1).")
    body.append("# Re-measure after curating: python tools/lexicon/lexicon.py --measure")
    body.append("# Shrink-only thereafter: the count may fall, never rise.")
    body.append(f'VERB_OFFENDER_PIN="{verb_offenders}"')
    body.append(f'SUFFIX_OFFENDER_PIN="{suffix_offenders}"')
    body.append("")
    body.append("# The date and node that CURATED the seed below. While this is empty,")
    body.append("# `adopt-lexicon.sh --check` reds: an underived table nobody edited is a mirror of the")
    body.append("# code, and that is the one shape a naming gate must not have.")
    body.append('ratified=""')
    body.append("")
    body.append(f"# PROPOSED from the SHIPPED CANON, over {total_defs} definition(s) in {len(files)} tracked")
    body.append("# file(s). The corpus chose WHICH concepts appear; it did not choose what any of them is")
    body.append("# CALLED — that is the canon's element 0, always, at every frequency. A frequency ranking")
    body.append("# would adopt whatever this repo already does most, which is how a naming gate ends up")
    body.append("# certifying the habit it was installed to change.")
    body.append("#")
    body.append("# The glosses below are the canon's. CURATE THEM ANYWAY, and add the NEGATIVE each row")
    body.append("# needs — the gate refuses a row that carries none, because a row with only a positive")
    body.append("# gloss cannot tell two verbs apart.")
    body.append("VERBS:")
    for v in seeded:
        body.append(f"  {v:<9} {canon.read_gloss(v)}{canon.render_negative(v)}")
    body.append("")
    # THE DEBT IS EMITTED. It was measured and dropped on the floor, which made it a variable that
    # could not be wrong because nothing read it. It is the one thing this corpus can say that the
    # canon cannot: which live sites are spelled as a non-representative form, i.e. exactly the
    # renames adopting this table will owe. Closing review L3.
    if debt:
        owed = sum(n for _v, n in debt)
        body.append(f"# RENAMES THIS TABLE WILL OWE: {owed} definition(s) across {len(debt)} spelling(s)")
        body.append("# already use a non-representative form of a seeded concept. Highest first; this is a")
        body.append("# work list, not a declaration, and deleting these lines changes nothing the gate reads.")
        for v, n in debt[:12]:
            body.append(f"#   {v} -> {forms[v]}  ({n} site(s))")
        if len(debt) > 12:
            body.append(f"#   ...and {len(debt) - 12} more; `--measure` prints the live count.")
    else:
        body.append("# RENAMES THIS TABLE WILL OWE: none. Every live site of a seeded concept already")
        body.append("# uses the representative spelling.")
    body.append("")

    # newline="" — write LF, never the platform default. `write_text` translates `\n` to `\r\n` on
    # Windows, and a CRLF conf INVERTS the unratified-seed refusal: `adopt-lexicon.sh` strips the
    # trailing quote with an anchored `s/"$//` that a carriage return defeats, leaving `"\r`, which
    # reads as a non-empty `ratified` value. The seed then passes the one check that exists to stop
    # an uncurated table reaching the merge bar. Caught by the scaffold arm in selftest.py.
    with open(dest, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(body))
    print(f"scaffold: {len(seeded)} verb(s) proposed from {total_defs} definition(s); "
          f"VERB_OFFENDER_PIN={verb_offenders}; {types_seen} type definition(s) scanned"
          + (f"; {len(refused)} file(s) NOT EXTRACTED, named on stderr" if refused else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

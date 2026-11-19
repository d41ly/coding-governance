#!/usr/bin/env python3
"""request.py — the content key of an owner's request, `request_content_key` (TOOL-dPlacedRequest-19, I11).

    python request.py key <file>                  # the request's content key, twelve hex digits
    python request.py --fixture --plant <case>    # one fixture case
    python request.py --selftest                  # every case

`derive_request_content_key` keys a request by its text alone: the first twelve hex digits of the
SHA-256 over the UTF-8 bytes of the memory-tree kit's `derive_content_key` of the text, the normaliser
that drops links to their text, ISO dates and emphasis and folds case and whitespace, so two typings of
one request differing only in those key alike. A text that normalises to nothing is refused, never
keyed. It is imported from that kit's `row_grammar.py`, found by `resolve_kit_dir` under the loop kit's
existing edge to it, so no second copy of the normaliser exists.

`key <file>` reads the file as bytes and decodes them strictly as `utf-8-sig`, so a leading byte-order
mark never reaches the key and no platform default decoding is ever used. It prints the key alone and
exits 0, or prints one `request — refused: <why>` line and exits 2: a file that is not UTF-8, naming
the offset of its first undecodable byte, an empty normalised text, an unreadable file, or a
memory-tree kit that does not resolve. Exit 2 is a usage error too.

`--fixture --plant <case>` runs one case of `PLANTS`, printing one `request: <case> · ...` line ending
`held` or `MISSED`, and exits 0 when it held, 1 when it missed; each case writes its files under one
scratch directory of the system temp folder and removes it. `--selftest` runs every case through
`loop_lib.run_selftest_cases`, the leg gov's own `loop request fixtures` runs.

WHAT THIS DOES NOT CHECK: that the file holds the owner's words, which the unattended driver's
`--request` trusts its caller for until the intake hook lands; and two requests whose texts differ
only in what the normaliser drops are one request by design.
"""
import argparse
import contextlib
import hashlib
import io
import pathlib
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import read_memory_tree, run_selftest_cases  # noqa: E402

SAY = "request"
#: The key's length in hex digits, the twelve-hex convention of the roles kit's `derive_section_sha`.
KEY_HEX = 12
#: `--plant`'s cases and what each owes: AC1's two and AC7's two.
PLANTS = {"normalised-pair": "two texts differing only in case, whitespace and an ISO date: one key",
          "empty-refused": "a text empty once normalised: refused, exit 2",
          "bom-pair": "one text saved with and without a UTF-8 byte-order mark: one key",
          "undecodable-refused": "a cp1252 byte after the text: refused, exit 2, naming not UTF-8"}


def read_request_text(path):
    """The text of the request file at `path`, its bytes decoded strictly as `utf-8-sig`. ValueError
    naming the offset of the first byte that does not decode; OSError where the file cannot be read."""
    data = pathlib.Path(path).read_bytes()
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        # the decoder reports the offset into what it read, the bytes past a stripped mark
        raise ValueError("%s is not UTF-8 at byte %d" % (path, e.start + len(data) - len(e.object))) from None


def derive_request_content_key(text):
    """`request_content_key` (I11): the first twelve hex digits of the SHA-256 over the UTF-8 bytes of
    `derive_content_key(text)`. ValueError on a text that normalises to nothing; LookupError where the
    memory-tree kit does not resolve."""
    read_memory_tree("row_grammar.py")
    from row_grammar import derive_content_key
    norm = derive_content_key(text)
    if not norm:
        raise ValueError("the request is empty once normalised")
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:KEY_HEX]


def run_request_plant(case):
    """One case of `PLANTS`: its `request: <case> · ...` line, and 0 when it held, 1 when it missed. Each
    file goes through this module's own `key` verb, in process, so the decoding is the one a caller gets."""
    texts = {"normalised-pair": (b"Fix the lander push on 2026-11-19\n", b"  fix   THE\tlander push on\n"),
             "empty-refused": (b" \n\t\n",),
             "bom-pair": (b"Fix the lander", b"\xef\xbb\xbfFix the lander"),
             "undecodable-refused": (b"Fix\xe9",)}[case]
    said = []
    with tempfile.TemporaryDirectory(prefix="rq") as scratch:
        for n, body in enumerate(texts):
            f = pathlib.Path(scratch) / ("req-%d.md" % n)
            f.write_bytes(body)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = main(["key", str(f)])
            said.append((rc, out.getvalue().strip()))
        left = sorted(p.name for p in pathlib.Path(scratch).iterdir())
    keys = [s for rc, s in said if rc == 0]
    if case in ("normalised-pair", "bom-pair"):
        held = (len(keys) == 2 and keys[0] == keys[1] and len(keys[0]) == KEY_HEX
                and all(c in "0123456789abcdef" for c in keys[0]))
        seen = [k or "-" for _, k in said] + ["equal" if held else "different or refused"]
    else:
        rc, line = said[0]
        needle = "not UTF-8" if case == "undecodable-refused" else "empty once normalised"
        held = rc == 2 and line.startswith("%s — refused: " % SAY) and needle in line and left == ["req-0.md"]
        seen = ["exit %d" % rc, line[:120] or "-"]
    print("%s: %s · %s · %s" % (SAY, case, " · ".join(seen), "held" if held else "MISSED"))
    return 0 if held else 1


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="request.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run one fixture case")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="run every fixture case")
    sub = ap.add_subparsers(dest="verb")
    key = sub.add_parser("key", help="print the request's content key")
    key.add_argument("file")
    args = ap.parse_args(argv)
    if args.selftest:
        if args.fixture or args.plant or args.verb:
            ap.error("--selftest takes no verb and no plant")
        cases = [(p, ["--fixture", "--plant", p], 0, "%s: %s · " % (SAY, p), "· held") for p in PLANTS]
        return run_selftest_cases(main, cases, "%s: selftest" % SAY)
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if args.fixture:
        return run_request_plant(args.plant)
    if args.verb == "key":
        try:
            print(derive_request_content_key(read_request_text(args.file)))
        except ValueError as e:
            why = str(e)
            print("%s — refused: %s" % (SAY, why if why.startswith(args.file) else "%s: %s" % (args.file, why)))
            return 2
        except (OSError, LookupError) as e:
            print("%s — refused: %s cannot be keyed: %s" % (SAY, args.file, e))
            return 2
        return 0
    ap.error("a verb, key, or --fixture --plant <case>, or --selftest")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""lexicon_conf.py — the ONE reader of `.lexicon.conf`.

Three consumers need this file: the engine (`tools/lexicon/lexicon.py`), the adopter script
(`tools/lexicon/adopt-lexicon.sh`, in bash), and — when its unit unparks — this repo's
`map_extractors.py`. Two or three hand-written parsers for one file is the
two-answers-to-one-question class, so the bash side calls `--print-verbs` here rather than
reimplementing the grammar, and any other consumer imports `load_conf`.

THE GRAMMAR, and why it is not exactly the sibling one. `.memory-tree.conf` and
`.codebase-map.conf` are a RESTRICTED line-based `KEY=VALUE` that bash can `source` and Python can
parse line-wise. That grammar cannot carry `VERBS`: a closed verb table is one row per verb with a
prose meaning, and the negative definitions ("`build` not `create`") are the rows that make the
table worth having. So this grammar is the sibling one PLUS block keys:

    KEY="value"            # single-line, sibling grammar: no inline comment after a value
    KEY:                   # block key: rows are the indented lines that follow
      row one
      row two
    NEXT_KEY="..."         # a non-indented line ends the block

A block ends at the first non-indented, non-blank line, or at EOF. Blank lines inside a block are
skipped, not terminators — a table with a blank line between groups is the shape a human writes.
"""

import re
import sys
from pathlib import Path

#: Keys whose value is an indented block rather than a single line.
BLOCK_KEYS = ("VERBS", "LAYERS")

_SCALAR_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)=(.*)$')
_BLOCK_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*):[ \t]*$')


class ConfError(Exception):
    """A refusal naming the file and line. Never a silent default: an unreadable declaration must
    not degrade into an empty one, because every predicate here reads green over an empty set."""


def load_conf(path: str | Path) -> dict:
    """Parse `.lexicon.conf` into `{scalars..., "VERBS": {verb: meaning}, "LAYERS": [(from, to)]}`.

    Raises ConfError on an unreadable file or a malformed line. It does NOT validate that any
    particular key is present — arming is the engine's question, and a reader that refuses an
    absent key cannot be used by the scaffolder that is about to write it.
    """
    p = Path(path)
    try:
        raw = p.read_text(encoding="utf-8")
    except OSError as e:
        raise ConfError(f"{p}: cannot read: {e}") from e

    out: dict = {k: ({} if k == "VERBS" else []) for k in BLOCK_KEYS}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        mb = _BLOCK_RE.match(line)
        if mb and mb.group(1) in BLOCK_KEYS:
            key = mb.group(1)
            i += 1
            rows = []
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    i += 1
                    continue
                if not nxt[:1].isspace():
                    break
                body = nxt.strip()
                if not body.startswith("#"):
                    rows.append((i + 1, body))
                i += 1
            out[key] = _parse_block(key, rows, p)
            continue

        ms = _SCALAR_RE.match(line)
        if ms:
            val = ms.group(2).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            out[ms.group(1)] = val
            i += 1
            continue

        raise ConfError(f"{p}:{i + 1}: not a KEY=VALUE line, a KEY: block header, or a comment: {stripped!r}")

    return out


def _parse_block(key: str, rows: list[tuple[int, str]], p: Path):
    if key == "VERBS":
        table: dict[str, str] = {}
        for lineno, body in rows:
            parts = body.split(None, 1)
            verb = parts[0].rstrip(":")
            if not verb.isalpha():
                raise ConfError(f"{p}:{lineno}: a verb must be alphabetic, got {verb!r}")
            table[verb.lower()] = parts[1].strip() if len(parts) > 1 else ""
        return table

    pairs: list[tuple[str, str]] = []
    for lineno, body in rows:
        if "->" not in body:
            raise ConfError(f"{p}:{lineno}: a LAYERS row is `<glob> -> <glob>`, got {body!r}")
        lhs, rhs = body.split("->", 1)
        lhs, rhs = lhs.strip(), rhs.strip()
        if not lhs or not rhs:
            raise ConfError(f"{p}:{lineno}: a LAYERS row needs a glob on both sides, got {body!r}")
        pairs.append((lhs, rhs))
    return pairs



def build_negatives(conf: dict) -> dict:
    r"""`{verb: {banned-token, ...}}` from the NOT clauses in each VERBS gloss.

    THE BACKTICKS ARE THE GRAMMAR, not decoration. Measured against the table this landed on: the
    pattern ``NOT\s+`([A-Za-z]+)` `` matches exactly the rows a bare `\bNOT\b` word match does, so
    there is no un-backticked `NOT` anywhere in the corpus this must govern — it parses every
    existing row with zero rewrites and zero false positives. A looser pattern would have to guess
    where the token ends, and the prose after the comma is the half a reader actually needs.

    A row may carry SEVERAL build_negatives. The gloss keeps its prose; only the tokens are extracted.
    """
    out = {}
    for verb, gloss in (conf.get("VERBS") or {}).items():
        out[verb] = set(re.findall(r"NOT\s+`([A-Za-z][A-Za-z0-9_]*)`", gloss or ""))
    return out

def langs(conf: dict) -> list[tuple[str, str, str]]:
    """`LANGS` as `(ext, pattern_set_id, mode)` triples. An empty pattern-set id is legal and is
    what a `dark` declaration looks like — it names no extractor on purpose."""
    out = []
    for tok in (conf.get("LANGS") or "").split():
        parts = tok.split(":")
        if len(parts) != 3:
            raise ConfError(f"LANGS entry must be `<ext>:<pattern-set-id>:<mode>`, got {tok!r}")
        ext, pset, mode = parts
        if mode not in ("parser", "probe", "dark"):
            raise ConfError(f"LANGS mode must be parser, probe or dark, got {mode!r} in {tok!r}")
        out.append((ext.lstrip("."), pset, mode))
    return out


def _main(argv: list[str]) -> int:
    """`--print-verbs <conf>` — one verb per line, for the bash side. Anything else is a usage
    refusal: this module is a library first and a CLI only for the one consumer that cannot import."""
    if len(argv) != 3 or argv[1] != "--print-verbs":
        sys.stderr.write("usage: python tools/lexicon/lexicon_conf.py --print-verbs <conf>\n")
        return 2
    try:
        conf = load_conf(argv[2])
    except ConfError as e:
        sys.stderr.write(f"lexicon-conf: {e}\n")
        return 1
    for verb in sorted(conf.get("VERBS") or {}):
        print(verb)
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv))

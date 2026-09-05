# **Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-7
# Committed as evidence for the recall measurement. The root is DERIVED here; the
# Accessor names are conformed to this repo's declared VERBS table; behaviour is unchanged
# and every rename is applied across all committed copies, so cross-file calls follow. The
# figures in the report were produced by the scratchpad originals, which differ from these
# copies in the derived root and in these names only.
# scratchpad original hardcoded this session's worktree and would resolve to nothing.
"""Shared measurement harness for LENS 5. Imports the kit's own map_lib so every figure is the
tool's real behaviour, not a re-implementation."""
from __future__ import annotations
import inspect, json, os, re, sys
from pathlib import Path

import subprocess as _sp
ROOT = pathlib.Path(_sp.run(["run_git", "rev-parse", "--show-toplevel"],
                            capture_output=True, text=True).stdout.strip())
KIT = ROOT / "tools" / "codebase-map"
sys.path.insert(0, str(KIT))
import map_lib as m  # noqa

# --- a blanked-source variant of map_lib._identifier_tokens, derived from its OWN source so the
# --- comment/string stripping is byte-identical to what the tool does.
_src = inspect.getsource(m._identifier_tokens)
_src = _src.replace("def _identifier_tokens(", "def _blanked_source(")
_src = _src.replace("return set(_IDENT_TOKEN_RE.findall(source))", "return source")
_src = _src.replace('return set(_IDENT_TOKEN_RE.findall("".join(out)))', 'return "".join(out)')
assert "_blanked_source" in _src and _src.count("return source") == 1
_ns = dict(m.__dict__)
exec(compile(_src, "<blanked>", "exec"), _ns)
blanked_source = _ns["_blanked_source"]

IDENT = m._IDENT_TOKEN_RE
SKIP = m._SKIP_DIRS

def read_symbols():
    d = json.loads((ROOT / "memory/map/generated/read_symbols.json").read_text(encoding="utf-8"))
    return d["read_symbols"]

def scan_files():
    """Exactly the file set build_reference_index walks for this repo's read_symbols.json."""
    rows = read_symbols()
    files = sorted({r["file"] for r in rows})
    roots = sorted({f.split("/", 1)[0] for f in files if f})
    exts = frozenset(Path(f).suffix for f in files if Path(f).suffix)
    out = []
    for top in roots:
        base = ROOT / top
        if not base.is_dir():
            continue
        for dirpath, dirnames, names in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP]
            for name in sorted(names):
                if exts and Path(name).suffix not in exts:
                    continue
                p = Path(dirpath) / name
                try:
                    p.read_text(encoding="utf-8")
                except (UnicodeDecodeError, OSError):
                    continue
                out.append(p)
    return out

def build_occurrence_table():
    """rel -> {token: [n_bare, n_dotted]} over the blanked source (comments/strings removed)."""
    table = {}
    for p in scan_files():
        rel = p.relative_to(ROOT).as_posix()
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        b = blanked_source(text, p.suffix)
        counts = {}
        for mt in IDENT.finditer(b):
            tok = mt.group(0)
            j = mt.start() - 1
            while j >= 0 and b[j] in " \t\r\n":
                j -= 1
            dotted = j >= 0 and b[j] == "."
            c = counts.setdefault(tok, [0, 0])
            c[1 if dotted else 0] += 1
        table[rel] = counts
    return table

def build_index_from(table, *, bare_only=False):
    idx = {}
    for rel, counts in table.items():
        for tok, (nb, nd) in counts.items():
            if bare_only and nb == 0:
                continue
            idx.setdefault(tok, set()).add(rel)
    return idx

"""read_open — which `open` audit event is a read, and of which source file (TOOL-aLightenedLoop-3 S3).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a
copy that drifts. The policy kit's guard trace and the spec-token checker's input record both filter
their audit hooks through it, so a write, a descriptor and a bytecode-cache read are judged by one
rule, never two. The block uses `os` and `importlib.util`, which every consumer already imports.
"""
import importlib.util
import os


# >>> read_open_py -- canonical copy: read_open.py in the gov lib dir (byte-identical; gated)
def derive_read_path(path, mode, flags):
    """-> (path, refused) for an `open` audit event that reads, or None for one that does not.

    A descriptor is None. With mode None the intent is in the flags, and any of `O_WRONLY`, `O_RDWR`
    or `O_CREAT` is None (TOOL-dGroundRules-43 S9); a mode that is not a string, or holds any of `w`,
    `a`, `x` or `+`, is None. A `.pyc` under a `__pycache__` directory is the source file it was
    compiled from (TOOL-dGroundRules-35 S1); a cache name `source_from_cache` refuses is kept as
    spelled, with `refused` true (TOOL-dGroundRules-52 S25). The path is returned through realpath.
    """
    if isinstance(path, int):
        return None
    if mode is None:
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT):
            return None
    elif not isinstance(mode, str) or any(c in mode for c in "wax+"):
        return None
    p = os.fsdecode(path)
    refused = False
    # TOOL-dGroundRules-52 S20: no `.pyc.<digits>` cut, since the flag filter above drops importlib's temporary write
    if os.path.basename(os.path.dirname(p)) == "__pycache__" and p.endswith(".pyc"):
        try:
            p = importlib.util.source_from_cache(p)
        except ValueError:
            refused = True
    return os.path.realpath(p), refused
# <<< read_open_py

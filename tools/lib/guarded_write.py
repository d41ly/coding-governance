"""guarded_write -- the guarded write's two steps, the owner's terminal proof and the write-then-record
(TOOL-dDeclaredLoop-2 S5).

The canonical copy of the guarded-write factory, extracted at its second instance: the instruction
command's terminal test and its write-then-record with the restore of the target's prior bytes, and
the policy command's. `<prefix>/lib/` is gov-internal and ships nothing, so each consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a
copy that drifts. Two carry it: the playbook kit's `instructions_edit.py` and the loop kit's
`policy_edit.py`. A typed confirmation is the caller's own step, outside the block.
"""
import os
import pathlib
import sys
import tempfile


# >>> guarded_write_py -- canonical copy: guarded_write.py in the gov lib dir (byte-identical; gated)
def check_terminal_proof():
    """The owner's proof `tty-cli` where standard error is an interactive terminal, else None: the one
    stream dOrderedCharter-15 S5 tests, and the one an agent's shell lacks. A pty wrapper giving an agent
    a terminal passes it, the threat the owner accepted (SA-1)."""
    return "tty-cli" if sys.stderr.isatty() else None


def write_guarded(path, new_text, record):
    """`new_text` written to `path` as UTF-8, or called with the path where it is a callable writing the
    path itself, then `record()`, the caller's record writer, called and its record's path returned.
    Where either step raises, the path's prior bytes are put back, the path removed where it did not
    exist, and the error raised again: no write lands without its record.
    Each write, the restore included, goes to a sibling temp `<name>.<random>.tmp` made by `mkstemp`
    and is `os.replace`d over the path, so the path holds its prior bytes or the new ones, never a
    part of either; a callable is handed that temp, already holding the prior bytes. No fsync."""
    path = pathlib.Path(path)
    held = path.read_bytes() if path.is_file() else None

    def write_target(fill):
        fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
        try:
            with os.fdopen(fd, "wb") as fh:
                fh.write(fill if isinstance(fill, bytes) else held or b"")
            if callable(fill):
                fill(pathlib.Path(tmp))
            os.replace(tmp, path)
        except BaseException:
            pathlib.Path(tmp).unlink(missing_ok=True)
            raise

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        write_target(new_text if callable(new_text) else new_text.encode("utf-8"))
        return record()
    except BaseException:
        if held is None:
            path.unlink(missing_ok=True)
        elif path.is_file() and path.read_bytes() != held:
            write_target(held)
        raise
# <<< guarded_write_py

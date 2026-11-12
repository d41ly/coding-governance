"""retired_kits — a target's kit selection read through the registry's `[[retired]]` rows (PLAY-dOrderedCharter-31 S10).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a
copy that drifts. Its two copies are govkit's selection resolver's and the playbook renderer's kit
readers', so an id that left the registry with a successor reads the same in both.

The block reads only a row's `id` and `successor`; the rest of the succession grammar is validated by
the step reader on gov's bar. A malformed row raises `ValueError`, which each caller turns into its
own refusal, so it denies rather than maps.
"""


# >>> retired_kits — canonical copy: retired_kits.py in gov's lib dir (byte-identical; gated)
def resolve_retired_kits(kits, entries, retired):
    """<kits> with each id that is not in <entries> and that a row of <retired> names replaced by the
    row's successor, or dropped where the successor is "none", in first-seen order with no id twice.
    An id no entry and no row names comes back as it was, for its caller's own refusal."""
    succ = {}
    for n, row in enumerate(retired or [], 1):
        rid, to = (row.get("id"), row.get("successor")) if isinstance(row, dict) else (None, None)
        if not (isinstance(rid, str) and rid and isinstance(to, str) and to):
            raise ValueError(f"[[retired]] row {n} needs a non-empty string id and successor")
        succ[rid] = to
    out = []
    for k in kits:
        k = k if k in entries else succ.get(k, k)
        if k != "none" and k not in out:
            out.append(k)
    return out
# <<< retired_kits

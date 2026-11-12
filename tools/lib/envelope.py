"""envelope — a load-bearing document's envelope, its identity and its level (PLAY-dOrderedCharter-3 S3).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so the block below travels INLINE,
byte-identical, in the playbook kit's `render_playbook.py` and the roles kit's `roles_lib.py`, both
copy-installed, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy that drifts.

An envelope is two whole lines around a document's body: the opener `[<path> · Level <n> · <direction>]`
and the closer `[/<path>]`, `<path>` the document's own repo-relative path. `render_envelope` writes them;
`read_envelopes` reads every line of a text that is one, an opener or a closer, paired or not.
"""
from __future__ import annotations


# >>> render_envelope — canonical copy: envelope.py in the gov lib dir (byte-identical; gated)
def render_envelope(doc, level, direction, body):
    """`body` between the opener and the closer naming `doc`; an empty body renders the two lines alone."""
    if body and not body.endswith("\n"):
        body += "\n"
    return "[%s · Level %d · %s]\n%s[/%s]\n" % (doc, level, direction, body, doc)


def read_envelopes(text):
    """Each whole line of `text` that is an envelope line, in order: `(line number, "open", doc, level,
    direction)` for an opener and `(line number, "close", doc, None, None)` for a closer."""
    import re
    opener = re.compile(r"^\[([^\[\]/][^\[\]]*?) · Level (\d+) · ([^\]]*)\]$")
    closer = re.compile(r"^\[/([^\[\]]+)\]$")
    found = []
    for n, line in enumerate(text.replace("\r\n", "\n").split("\n"), 1):
        m = opener.match(line)
        if m:
            found.append((n, "open", m.group(1), int(m.group(2)), m.group(3)))
            continue
        m = closer.match(line)
        if m:
            found.append((n, "close", m.group(1), None, None))
    return found
# <<< render_envelope

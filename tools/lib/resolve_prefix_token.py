"""resolve_prefix_token — the `{prefix}` token resolved against a tool root (TOOL-aRepatriatedFork-47 S1).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a
copy that drifts. Its shell twin, with the same contract, is the `resolve_prefix_sh` block in
`kit-rel.sh` beside this file, and the same test's behaviour arm runs both over one truth table.

The block carries no single quote: `run-gates.sh` inlines it inside a single-quoted `-c` program.
"""

# >>> resolve_prefix_token -- canonical copy: resolve_prefix_token.py in the gov lib dir (byte-identical; gated)
def resolve_prefix_token(spelled, troot):
    """<spelled> with its {prefix} token resolved against the tool root <troot>.

    An empty or "." root is a root install: the token drops with its slash, and a bare token
    becomes ".". Any other root replaces the token. Text with no token passes unchanged.
    """
    spelled = str(spelled)
    if not troot or troot == ".":
        return spelled.replace("{prefix}/", "").replace("{prefix}", ".")
    return spelled.replace("{prefix}", troot)
# <<< resolve_prefix_token

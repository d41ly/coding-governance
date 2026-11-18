"""needs_graph — the order of a needs graph and its cycles (TOOL-dDeclaredLoop-12 S5).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a
copy that drifts. Three readers carry it: govkit orders a kit selection after its `requires`, the
backlog grader reports each hold cycle among live asks, and the loop reader orders each step's items
after their `needs`. The block imports nothing.
"""


# >>> needs_graph_py -- canonical copy: needs_graph.py in the gov lib dir (byte-identical; gated)
class NeedsCycle(ValueError):
    """No order exists. `stuck` holds the nodes left unplaced, sorted: every node on a cycle and every
    node that needs one, so `scan_cycles` is what names the cycles themselves."""

    def __init__(self, stuck):
        super().__init__("a needs cycle among %s" % ", ".join(stuck))
        self.stuck = stuck


def derive_needs_order(nodes, needs):
    """`nodes` in an order where each follows every node `needs[node]` names: Kahn, each ready tier
    sorted, so the order is sorted order wherever no edge applies. A need outside `nodes` constrains
    nothing, and a node needing itself is a cycle. NeedsCycle where no order exists."""
    want = set(nodes)
    deps = {n: {d for d in needs.get(n, ()) if d in want} for n in nodes}
    out, placed = [], set()
    while len(out) < len(nodes):
        ready = sorted(n for n in nodes if n not in placed and deps[n] <= placed)
        if not ready:
            raise NeedsCycle(sorted(n for n in nodes if n not in placed))
        out.extend(ready)
        placed.update(ready)
    return out


def scan_cycles(edges, live=None):
    """Every cycle of `edges`, `{node: the nodes it points at}`, each reported ONCE and rotated to its
    smallest member, in sorted order; a node pointing at itself is a cycle of one. `live`, a predicate
    over a node, leaves out each node it answers False for, as a start and as a step; None keeps all.
    Once and rotated, because a cycle found from each of its members is one finding."""
    keep = live if live is not None else (lambda node: True)
    found = {}
    for start in [a for a in sorted(edges) if keep(a)]:
        stack = [(start, (start,))]
        while stack:
            node, path = stack.pop()
            for nxt in sorted(edges.get(node, ())):
                if not keep(nxt):
                    continue
                if nxt == start:
                    low = path.index(min(path))
                    key = path[low:] + path[:low]
                    found.setdefault(key, key)
                elif nxt not in path:
                    stack.append((nxt, path + (nxt,)))
    return [found[k] for k in sorted(found)]
# <<< needs_graph_py

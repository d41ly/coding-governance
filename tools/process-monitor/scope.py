#!/usr/bin/env python3
"""scope.py — which census rows are OURS. The safety property the whole kit rests on.

gov:kit process-monitor@0.1

Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-2.md

ATTRIBUTION IS A PROPERTY OF THE TREE, NOT OF A ROW. A row is a ROOT when a declared prefix matches
its resolved program path or one of its path-shaped argument tokens; the in-scope set is those roots
plus their transitive descendants. That is why a `sleep 900` whose argv names nothing, and a leg
shell carrying a relative script path, are both reapable — their ancestry starts somewhere declared
— while an unrelated editor is invisible.

WHAT IS MATCHED, AND WHAT IS NOT. The command line is DECOMPOSED first, never matched as one string.
Every `NAME=value` token is stripped wherever it appears, including after `export`, `env`, `declare`
and `set`, and including inside a `-c` body, which is itself word-split and processed by these same
rules. Measured on the machine this was built for: every agent shell carries
`bash.exe -c "... && export TEMP='<tempdir>' ..."`, so a raw-string match on a root under that
directory admits every agent session in every repository on the box.

WHAT THIS CANNOT DO, and it is a limit rather than a bug: a process whose command line names no
declared root AND whose ancestry is dead is UNATTRIBUTABLE. The count is reported. On the build
machine that population was real — a 7.5-hour `sleep 27200` and three `tail -f /tmp/...`.
"""
import os
import re
import sys

ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
ASSIGNMENT_LEADERS = ("export", "env", "declare", "set", "local", "readonly")
BODY_FLAGS = ("-c", "-command", "/c", "-encodedcommand")
MIN_ROOT_LEN = 8


class ScopeRefused(RuntimeError):
    """The declaration is unusable. Never degraded into an empty set."""


def build_normalized(text):
    """One path, one spelling: forward slashes, case-folded, no trailing separator.

    The same directory is spelled `C:/x`, `C:\\x` and `/c/x` by three different producers inside a
    single command line on this platform.
    """
    out = (text or "").replace("\\", "/").lower()
    while "//" in out:
        out = out.replace("//", "/")
    return out.rstrip("/")


def parse_tokens(command):
    """A command line -> the tokens that may carry a path.

    Assignments are dropped wherever they appear, and a `-c` body is split and processed by these
    same rules rather than treated as one opaque token.
    """
    if not command:
        return []
    out, pending_body, skip_leader = [], False, False
    for raw in re.findall(r'"[^"]*"|\'[^\']*\'|\S+', command):
        tok = raw.strip("\"'")
        if pending_body:
            pending_body = False
            out.extend(parse_tokens(tok))
            continue
        low = tok.lower()
        if low in BODY_FLAGS:
            pending_body = True
            continue
        if low in ASSIGNMENT_LEADERS:
            skip_leader = True
            continue
        if ASSIGNMENT.match(tok):
            skip_leader = False
            continue
        skip_leader = False
        out.append(tok)
    return out


def check_root_shape(roots):
    """Both directions of the containment test, before any row is graded."""
    if not roots:
        raise ScopeRefused(
            "PROCMON_ROOTS is blank. A blank roots list is a REFUSAL, not an empty set: the fence "
            "would match nothing and every report would read as a clean tree it never examined.")
    for r in roots:
        norm = build_normalized(r)
        if len(norm) < MIN_ROOT_LEN or norm in ("", "/", "c:"):
            raise ScopeRefused(
                "PROCMON_ROOTS entry %r is too broad to be a declaration — it would admit "
                "processes this repo has no claim over." % r)
    return [build_normalized(r) for r in roots]


def check_token_under(token, root):
    """Separator-anchored prefix. `/c/x` admits `/c/x/y` and refuses `/c/x-other`."""
    norm = build_normalized(token)
    return norm == root or norm.startswith(root + "/")


def check_is_root(row, roots):
    """Is this row ATTRIBUTABLE on its own command line? Returns the admitting root, or None."""
    for tok in parse_tokens(row.get("command")):
        for root in roots:
            if check_token_under(tok, root):
                return root
    return None


def build_edges(rows):
    """winpid -> set of PARENT winpids, over the union of both graphs.

    Every `msys_ppid` is TRANSLATED through the census's own msys_pid -> winpid join first. A raw
    MSYS id is never looked up in the winpid-keyed map: the two namespaces disagree on this
    platform — measured, 7 of 330 overlaid rows — so an untranslated union either degenerates to
    the Windows graph or attaches whatever process happens to hold that integer.

    An edge whose CHILD is older than its claimed parent is dropped: a recycled pid cannot have
    fathered a process that predates it.
    """
    by_win = {r["winpid"]: r for r in rows}
    by_msys = {r["msys_pid"]: r["winpid"] for r in rows if r.get("msys_pid") is not None}
    edges, dropped, unmapped = {}, 0, 0
    for r in rows:
        parents = set()
        for key, translate in (("win_ppid", False), ("msys_ppid", True)):
            pid = r.get(key)
            if pid is None:
                continue
            parent = by_msys.get(pid) if translate else pid
            if parent is None:
                unmapped += 1
                continue
            if parent == r["winpid"] or parent not in by_win:
                continue
            if r["age_s"] > by_win[parent]["age_s"]:
                dropped += 1
                continue
            parents.add(parent)
        edges[r["winpid"]] = parents
    return edges, dropped, unmapped


def derive_scope(rows, roots, self_chain=()):
    """The in-scope set. Returns (scope, counts).

    `scope` maps winpid -> {"root": <admitting root>, "killable": bool}.

    SELF-CHAIN ROWS ARE IN SCOPE AND MAY BE ROOTS. They are never KILL TARGETS. Conflating "ours"
    with "killable" empties the set in the shape this kit ships into: the monitor runs from a
    session whose shell is the process carrying the absolute repo path, so that shell is both the
    only attributable root and a member of the self chain.
    """
    roots = check_root_shape(roots)
    self_chain = set(self_chain or ())
    edges, dropped, unmapped = build_edges(rows)

    children = {}
    for winpid, parents in edges.items():
        for p in parents:
            children.setdefault(p, set()).add(winpid)

    seeds = {}
    for r in rows:
        hit = check_is_root(r, roots)
        if hit is not None:
            seeds[r["winpid"]] = hit

    # The closure, under a VISITED-SET. At least one cycle was measured in this union over 337 live
    # rows, so termination is a guarantee this walk has to carry rather than an assumption.
    scope, frontier, visited = {}, list(seeds), set()
    for winpid, root in seeds.items():
        scope[winpid] = {"root": root, "killable": winpid not in self_chain}
    while frontier:
        winpid = frontier.pop()
        if winpid in visited:
            continue
        visited.add(winpid)
        for kid in children.get(winpid, ()):  # noqa: B007
            if kid not in scope:
                scope[kid] = {"root": scope[winpid]["root"], "killable": kid not in self_chain}
                frontier.append(kid)

    counts = {
        "census": len(rows),
        "roots": len(seeds),
        "in_scope": len(scope),
        "killable": sum(1 for v in scope.values() if v["killable"]),
        "unattributable": sum(1 for r in rows
                              if r["winpid"] not in scope and not r.get("command")),
        "dropped_edges": dropped,
        "unmapped_msys_parents": unmapped,
    }
    return scope, counts


def read_roots(conf_text):
    """PROCMON_ROOTS out of a conf file's text."""
    for line in conf_text.splitlines():
        line = line.strip()
        if line.startswith("PROCMON_ROOTS="):
            return line.split("=", 1)[1].strip().strip("\"'").split()
    return []


def load_conf(root_dir):
    path = os.path.join(root_dir, ".process-monitor.conf")
    if not os.path.exists(path):
        raise ScopeRefused("no .process-monitor.conf at %s" % path)
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return read_roots(fh.read())


def build_self_chain(rows, winpid):
    """The calling process and its ancestors, over the same union graph, under a visited-set."""
    edges, _dropped, _unmapped = build_edges(rows)
    chain, frontier = set(), [winpid]
    while frontier:
        cur = frontier.pop()
        if cur in chain:
            continue
        chain.add(cur)
        frontier.extend(edges.get(cur, ()))
    return chain


def main(argv):
    import census
    root_dir = os.environ.get("PROCMON_ROOT", os.getcwd())
    try:
        roots = load_conf(root_dir)
        rows, _counts = census.scan_processes(os.environ.get("PROCMON_BACKEND", ""))
        chain = build_self_chain(rows, os.getpid())
        scope, counts = derive_scope(rows, roots, chain)
    except (ScopeRefused, census.CensusRefused) as exc:
        sys.stderr.write("scope: REFUSED — %s\n" % exc)
        return 1

    if "--check-conf" in argv:
        if not scope:
            sys.stderr.write(
                "scope: REFUSED — the declared roots admit NOTHING on this machine. A conf whose "
                "roots match no live process is one nobody can tell from a quiet machine.\n")
            return 1
        print("scope: conf admits %(in_scope)d of %(census)d row(s) from %(roots)d root(s)"
              % counts)
        return 0

    if "--explain" in argv:
        want = argv[argv.index("--explain") + 1] if len(argv) > argv.index("--explain") + 1 else ""
        if not want.isdigit():
            sys.stderr.write("scope: REFUSED — --explain takes a WINPID, got %r. A caller holding "
                             "an MSYS id translates it through the census first.\n" % want)
            return 1
        hit = scope.get(int(want))
        if hit is None:
            print("scope: %s is NOT in scope (no declared root reaches it)" % want)
        else:
            print("scope: %s is IN SCOPE via root %s · killable=%s"
                  % (want, hit["root"], hit["killable"]))
        return 0

    print("scope: %(in_scope)d of %(census)d in scope · %(roots)d root(s) · %(killable)d killable "
          "· %(unattributable)d unattributable · %(dropped_edges)d edge(s) dropped on age · "
          "%(unmapped_msys_parents)d unmapped msys parent(s)" % counts)
    return 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv[1:]))

"""map_imports.py — an import target to the repo paths it may DENOTE, by AST.

WHAT IT RETURNS, and it is the whole contract: `resolve_import` returns CANDIDATE repo paths. An
EMPTY list means the target is external or unresolvable, which is not an error and not a violation —
a caller can only conclude something about what it can locate.

LANGUAGE-BRANCHED ON THE IMPORTER'S EXTENSION, not on the target's shape. A dot means different
things in different languages: `lodash.debounce` is one JS package name, `pkg.mod.helper` is a
Python namespace path. An earlier cut branched on `"." in target` — a Python rule applied to every
language — and that correction is the reason this function is worth rescuing rather than rewriting.
Within Python: a dotted target names its package FROM THE ROOT and the importer's directory gets no
precedence; a LEADING dot is a relative package import decoded from the extractor's `node.level`;
and a BARE name prefers the importer's own directory but FALLS BACK to every same-stem hit, so it is
not directory-bound. Every other language treats a bare specifier as a package path whose dots are
part of a name.

WHAT THIS IS NOT. It resolves IMPORT STATEMENTS and nothing else — not call sites, not attribute
receivers, not types. It counts nothing and reports no coverage. **A consumer that reads its output
as a call graph will be wrong**, and the figures sometimes quoted for attribute-site resolution
belong to a research prototype under `memory/builds/dTracedLattice/build/`, not to this module.

PROVENANCE. Copied from the lexicon kit's P3 predicate, which is specced for deletion. The five
functions below are byte-identical to their originals — with ONE exception, stated because a
provenance claim nobody can check is worth nothing: the helper spelled `ext_of` there is
`derive_ext` here. It is COPIED rather than moved (the lexicon kit reads it at eight further sites
and keeps its own), and the lexicon kit's engine module is not an ARMED layer for the naming gate
while this directory is, so the copy had to satisfy a table the original was never graded against.
Behaviour is unchanged and the parity arm compares it. Rescue recorded as `TOOL-dTracedLattice-6`.

This module imports nothing from a sibling kit, and a selftest arm asserts it.
"""

def derive_ext(path: str) -> str:
    """The extension used for a LANGS lookup. A file with no dot in its BASENAME reports `<none>`,
    which must be declared like any other: two such files are tracked here, and letting them fall
    through unnamed is exactly the silent skip the fail-closed law refuses."""
    base = path.rsplit("/", 1)[-1]
    return base.rsplit(".", 1)[-1] if "." in base else "<none>"


def _check_path_suffix(path: str, suffix: str) -> bool:
    """Does `path`, minus its extension, end with `suffix` AT A PATH BOUNDARY?

    This is what makes a dotted import target mean something. Without it, `concurrent.helper` and
    `thirdparty.helper` — imports touching nothing in the repo — resolved onto any file whose stem
    happened to be `helper` and RED as layer crossings. A false positive there is worse than the
    false negative it replaced: the only escape is a waiver, and that waiver then permanently
    silences the genuine violation it is hiding.
    """
    base = path.rsplit("/", 1)[-1]
    stem_path = path[: -(len(base) - base.rfind("."))] if "." in base else path
    return stem_path == suffix or stem_path.endswith("/" + suffix)


def build_module_index(files: list[str]) -> dict[str, list[str]]:
    """`{module-stem: [repo paths]}` over the tracked corpus, for P3's resolver.

    A LAYERS glob is spelled as a repo PATH. An import target is a NAMESPACE. Turning one into the
    other by swapping dots for slashes only works when the two happen to coincide, and it silently
    fails whenever they do not — most importantly when a directory name contains a character no
    module name may contain. `tools/codebase-map/` is exactly that case: no Python import can ever
    produce the hyphen, so a rule naming it was unmatchable by construction and P3 reported a clean
    zero over a population it could not select. That is the vacuous-selector class this kit's own
    docstring names as its dominant failure mode.
    """
    index: dict[str, list[str]] = {}
    for rel in files:
        base = rel.rsplit("/", 1)[-1]
        stem = base.rsplit(".", 1)[0] if "." in base else base
        index.setdefault(stem, []).append(rel)
    return index


def _resolve_relative(spec: str, here: str, index, ext: str) -> list[str]:
    """A `./`-or-`../` specifier against the importer's directory. `[]` means it escapes the repo.

    ESCAPING IS EXTERNAL, NOT CLAMPED. The first cut silently ignored a `..` with nothing left to
    pop, so `../../../outside/thing.js` landed back inside the tree and could FABRICATE a crossing
    against a path the import never names.
    """
    stack: list[str] = [p for p in here.split("/") if p]
    for part in [p for p in spec.split("/") if p not in ("", ".")]:
        if part == "..":
            if not stack:
                return []
            stack.pop()
        else:
            stack.append(part)
    cand = "/".join(stack)
    out = [cand]
    # BOUNDARY, not prefix: a bare `startswith` is the same defect the glob anchoring removed, and
    # it let `../shared/thing` resolve onto `web/shared/thingamajig.js`.
    out.extend(p for p in index.get(cand.rsplit("/", 1)[-1], [])
               if derive_ext(p) == ext and _check_path_suffix(p, cand))
    return out


def resolve_import(target: str, importer: str, index: dict[str, list[str]]) -> list[str]:
    """Candidate repo paths an import target may denote. Empty means EXTERNAL or unresolvable, which
    is not a violation — a rule can only forbid what it can locate.

    LANGUAGE-AWARE, and that is the correction. An earlier cut branched on `"." in target`, which is
    a PYTHON namespace rule: it treated the JS package specifier `lodash.debounce` as a dotted module
    path and stripped its importer-local precedence. A dot means different things in different
    languages and the importer's extension is what says which.
    """
    here = importer.rsplit("/", 1)[0] if "/" in importer else ""
    ext = derive_ext(importer)

    if target.startswith("./") or target.startswith("../"):
        return _resolve_relative(target, here, index, ext)

    if ext == "py":
        # A leading dot is a RELATIVE package import: one dot is this package, each extra dot walks
        # up one. `node.level` is preserved by the extractor precisely so this is decidable.
        if target.startswith("."):
            level = len(target) - len(target.lstrip("."))
            rest = target[level:].replace(".", "/")
            up = "../" * (level - 1)
            return _resolve_relative("./" + up + rest, here, index, ext)

        if "." in target:
            # A dotted target names its own package FROM THE ROOT, so the importer's directory gets
            # no precedence — but the candidate must be PATH-CONSISTENT with the dots, or the stem
            # lookup degenerates into "any file with this basename".
            dotted = target.replace(".", "/")
            out = [dotted]
            out.extend(p for p in index.get(target.rsplit(".", 1)[-1], [])
                       if derive_ext(p) == ext and _check_path_suffix(p, dotted))
            return out

        # A BARE name is the flat `sys.path`-insert shape — the commonest one in this tree, and the
        # only one where the importer's own directory legitimately wins.
        hits = [p for p in index.get(target, []) if derive_ext(p) == ext]
        local = [p for p in hits if (p.rsplit("/", 1)[0] if "/" in p else "") == here]
        return local or hits

    # Every other language: a bare specifier is a PACKAGE PATH, and its dots are part of a name
    # rather than separators. Resolve it as a path and by its final segment's stem; anything that
    # denotes nothing tracked is external, which is not a violation.
    out = [target]
    tail = target.rsplit("/", 1)[-1]
    stem = tail.rsplit(".", 1)[0] if "." in tail else tail
    out.extend(p for p in index.get(stem, []) if derive_ext(p) == ext and _check_path_suffix(p, target))
    return out

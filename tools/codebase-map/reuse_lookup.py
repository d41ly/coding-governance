"""reuse-lookup — the behaviour->seam discovery entrypoint (codebase-map kit, S3).

    python codebase-map/reuse_lookup.py "normalise a display name into a url slug"

Assembles a candidate corpus from the map's four recall sources — generated/symbols.json
ids/kinds, generated/inventories.json keys, every dossier's `## Reuse affordance` seam line,
and every `## Shared seams` prose block — and prints a ranked SHORTLIST for an agent to read.
The shortlist is NOT a hard top-K lexical cut (that scores ~0% behavioural recall): it is the
UNION of token-stem matches (the seeds) AND a capped set of structural neighbours (same kind or
same file as a seed), so a seam whose name doesn't literally contain the query word still
surfaces for the agent to judge. Fan-in is computed ON DEMAND here (never committed) to rank
hot seams. A recall-dark layer (declared in .codebase-map.conf) prints a partial-recall notice
so an empty result is never a falsely-confident "no seam fits".

Portable: reads only committed artifacts + dossiers + the conf via the repo root
(CODEBASE_MAP_ROOT overrides), so it needs NO project map_extractors.py — it runs the same in
any adopting repo. This is bThriftyCompass S1's portable re-implementation; an adopting repo
retires any bespoke reuse-audit script and repoints its "reuse before building" step here. The
CLI produces the shortlist; the agent-instruction reuse-lookup.agent.md turns it into a
decision (wire through seam X, or "no seam fits").
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import map_lib as m  # noqa: E402

#: cap on the structural-neighbour set (seeds are NEVER capped — the whole point is that the
#: lexical shortlist is not a hard top-K; only the "here's what lives next to a hit" widening is).
NEIGHBOUR_CAP = 12


@dataclass(frozen=True)
class Candidate:
    """One reusable thing the query might already have a home in. Merged by name across the
    sources it appears in (a symbol that is also a declared affordance seam is ONE row)."""

    name: str
    sources: tuple[str, ...]        # subset of {symbol, inventory, affordance-seam, shared-seams}
    kind: str = ""                  # symbol kind (function/class/component/const-export), else ""
    file: str = ""                  # def file (symbols only) — for fan-in + "read this"
    detail: str = ""                # inventory id / owning dossier — human context


@dataclass
class Corpus:
    candidates: dict[str, Candidate]        # name -> merged candidate
    shared_seams: dict[str, str]            # feature -> `## Shared seams` prose
    symbol_files: list[str]                 # symbols.json file list (reference-scan roots)
    recall_dark: tuple[str, ...] = ()       # layers declared uncovered in .codebase-map.conf
    threshold: int = m.SEAM_FANIN_THRESHOLD_DEFAULT
    has_symbols: bool = False               # was symbols.json present (recall tier adopted)?


@dataclass
class Ranked:
    candidate: Candidate
    is_seed: bool                           # a token-stem / prose match to the query
    fanin: int
    reason: str                             # why it is on the list (for the agent)
    is_seam: bool = False                   # a symbol whose fan-in >= the seam threshold


@dataclass
class Shortlist:
    query: str
    ranked: list[Ranked]
    recall_dark: tuple[str, ...]
    threshold: int
    corpus_counts: dict[str, int] = field(default_factory=dict)

    @property
    def empty(self) -> bool:
        return not self.ranked


# ======================================================================================
# Corpus loading (committed artifacts + dossiers + conf — no project code needed)
# ======================================================================================


def _section_body(text: str, heading: str) -> str:
    """The lines under a `## Heading` up to the next `## ` heading (prose blob, joined)."""
    lines = text.splitlines()
    try:
        i = next(k for k, ln in enumerate(lines) if ln.strip() == heading)
    except StopIteration:
        return ""
    body: list[str] = []
    for ln in lines[i + 1:]:
        if ln.strip().startswith("## "):
            break
        body.append(ln)
    return "\n".join(body).strip()


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_corpus(root: Path | None = None) -> Corpus:
    """Assemble the recall corpus from the committed map. Fail-open on a missing source (an
    opt-out repo has no symbols.json; a fresh repo has no dossiers) — the lookup is advisory, so
    a thin corpus is a thin shortlist, never a crash. A MALFORMED committed artifact still
    raises (json errors propagate): a broken symbols.json is a real problem, not an empty menu."""
    root = root or m.repo_root()
    conf = m.load_conf(root)
    map_dir = m.map_root(root)
    gen = map_dir / "generated"

    candidates: dict[str, Candidate] = {}

    def merge(name: str, source: str, *, kind: str = "", file: str = "", detail: str = "") -> None:
        if not name:
            return
        prev = candidates.get(name)
        if prev is None:
            candidates[name] = Candidate(name, (source,), kind, file, detail)
            return
        candidates[name] = Candidate(
            name,
            tuple(dict.fromkeys(prev.sources + (source,))),
            kind or prev.kind,
            file or prev.file,
            detail or prev.detail,
        )

    symbol_files: list[str] = []
    has_symbols = (gen / "symbols.json").is_file()
    if has_symbols:
        for s in _read_json(gen / "symbols.json").get("symbols", []):
            merge(s["id"], "symbol", kind=s["kind"], file=s["file"])
            symbol_files.append(s["file"])

    if (gen / "inventories.json").is_file():
        for inv_id, keys in _read_json(gen / "inventories.json").get("inventories", {}).items():
            for key in keys:
                merge(key, "inventory", detail=inv_id)

    shared_seams: dict[str, str] = {}
    for feature, text in _dossier_texts(map_dir).items():
        for seam in m.parse_affordance(text).seams:
            merge(seam, "affordance-seam", detail=feature)
        prose = _section_body(text, "## Shared seams")
        if prose:
            shared_seams[feature] = prose

    recall_dark = tuple(t for t in re.split(r"[,\s]+", conf.get("RECALL_DARK_LAYERS", "")) if t)
    return Corpus(
        candidates=candidates,
        shared_seams=shared_seams,
        symbol_files=sorted(set(symbol_files)),
        recall_dark=recall_dark,
        threshold=m.seam_fanin_threshold(root),
        has_symbols=has_symbols,
    )


def _dossier_texts(map_dir: Path) -> dict[str, str]:
    texts: dict[str, str] = {}
    foundation = map_dir / "FOUNDATION.md"
    if foundation.is_file():
        texts["foundation"] = foundation.read_text(encoding="utf-8")
    features = map_dir / "features"
    if features.is_dir():
        for path in sorted(features.glob("*.md")):
            texts[path.stem] = path.read_text(encoding="utf-8")
    return texts


# ======================================================================================
# Shortlist assembly (pure — the tested core)
# ======================================================================================


def assemble_shortlist(query: str, corpus: Corpus, ref_index: dict[str, set[str]]) -> Shortlist:
    """The pure heart: query + corpus + reference index -> a ranked shortlist. Seeds = every
    candidate sharing a token stem with the query, PLUS the dossier of any `## Shared seams`
    prose that shares a stem (behavioural recall beyond names). Structural neighbours = symbols
    with the same kind OR the same file as a symbol seed, capped. Ranked seeds-first, then by
    fan-in desc, then name — deterministic. Empty seeds -> empty shortlist -> 'no seam fits'."""
    qstems = m.stems(query)
    if not qstems:
        return Shortlist(query, [], corpus.recall_dark, corpus.threshold, _counts(corpus))

    # rank against a LOCAL pool — synthetic prose candidates are added here, never back into the
    # caller's corpus (assemble must be idempotent: two queries on one corpus must not leak).
    pool = dict(corpus.candidates)

    seeds: dict[str, str] = {}  # name -> reason
    for name, cand in pool.items():
        shared = qstems & m.stems(name)
        if shared:
            seeds[name] = f"name stem: {', '.join(sorted(shared))}"

    # prose seeds: a `## Shared seams` block that talks about the behaviour points at its seams.
    for feature, prose in corpus.shared_seams.items():
        shared = qstems & m.stems(prose)
        if not shared:
            continue
        # surface the feature's declared affordance seams (already candidates) as prose hits,
        # and the feature dossier itself if it has none.
        feat_seams = [
            n for n, c in pool.items()
            if "affordance-seam" in c.sources and c.detail == feature
        ]
        if feat_seams:
            for n in feat_seams:
                seeds.setdefault(n, f"shared-seams prose ({feature}): {', '.join(sorted(shared))}")
        else:
            name = f"{feature} (## Shared seams)"
            pool.setdefault(name, Candidate(name, ("shared-seams",), detail=feature))
            seeds[name] = f"shared-seams prose ({feature}): {', '.join(sorted(shared))}"

    # structural neighbours of the symbol seeds — same kind OR same def file, capped.
    seed_syms = [pool[n] for n in seeds if pool[n].kind]
    seed_kinds = {c.kind for c in seed_syms}
    seed_files = {c.file for c in seed_syms if c.file}
    neighbours: dict[str, str] = {}
    for name, cand in sorted(pool.items()):
        if name in seeds or not cand.kind:
            continue
        if cand.file and cand.file in seed_files:
            neighbours[name] = f"neighbour: same file as a hit ({cand.file})"
        elif cand.kind in seed_kinds:
            neighbours[name] = f"neighbour: same kind ({cand.kind})"

    ranked: list[Ranked] = []
    for name, reason in seeds.items():
        ranked.append(_rank(pool, corpus.threshold, ref_index, name, True, reason))
    for name, reason in sorted(neighbours.items())[:NEIGHBOUR_CAP]:
        ranked.append(_rank(pool, corpus.threshold, ref_index, name, False, reason))

    ranked.sort(key=lambda r: (not r.is_seed, -r.fanin, r.candidate.name))
    return Shortlist(query, ranked, corpus.recall_dark, corpus.threshold, _counts(corpus))


def seed_affordances(corpus: Corpus, ref_index: dict[str, set[str]], top: int) -> list[tuple[Candidate, int]]:
    """S4b — the bounded big-bang worklist: the ``top`` highest-fan-in seams (fan-in >= the seam
    threshold) that NO dossier yet declares as a `## Reuse affordance` seam, so the
    reinvention-prone active surface converges first. A symbol already carrying an affordance seam
    line has BOTH 'symbol' and 'affordance-seam' in its merged sources and is DONE (excluded);
    a symbol below the threshold is not a seam and is not worklist-worthy. Pure + deterministic:
    ranked by fan-in desc then id. Fan-in is on demand (never committed) — same math as the lookup
    and --converge so 'a seam' means one thing everywhere."""
    scored: list[tuple[Candidate, int]] = []
    for cand in corpus.candidates.values():
        if "symbol" not in cand.sources or not cand.file:
            continue  # only indexable symbols can have a fan-in / def file to point at
        if "affordance-seam" in cand.sources:
            continue  # already declared — off the worklist
        fanin = m.fan_in(ref_index, cand.name, cand.file)
        if fanin >= corpus.threshold:
            scored.append((cand, fanin))
    scored.sort(key=lambda cf: (-cf[1], cf[0].name))
    return scored[:top]


def _rank(pool: dict[str, Candidate], threshold: int, ref_index: dict[str, set[str]],
          name: str, is_seed: bool, reason: str) -> Ranked:
    cand = pool[name]
    fanin = m.fan_in(ref_index, cand.name, cand.file) if cand.file else 0
    is_seam = bool(cand.kind) and fanin >= threshold
    return Ranked(cand, is_seed, fanin, reason, is_seam)


def _counts(corpus: Corpus) -> dict[str, int]:
    c = {"symbol": 0, "inventory": 0, "affordance-seam": 0}
    for cand in corpus.candidates.values():
        for s in cand.sources:
            if s in c:
                c[s] += 1
    c["shared-seams"] = len(corpus.shared_seams)
    return c


# ======================================================================================
# Rendering
# ======================================================================================


def render(shortlist: Shortlist, corpus: Corpus) -> str:
    # ASCII-only output: this prints to a console whose encoding is not guaranteed UTF-8 (a C/
    # ASCII locale in CI, a Windows codepage), and a `print` of `—`/`·` there raises
    # UnicodeEncodeError. Data (ids, paths) is already ASCII; keep the separators ASCII too.
    q = shortlist.query
    cc = shortlist.corpus_counts
    out: list[str] = [
        f'# reuse-lookup: "{q}"',
        f"# corpus: {cc.get('symbol', 0)} symbols | {cc.get('inventory', 0)} inventory keys | "
        f"{cc.get('affordance-seam', 0)} affordance seams | {cc.get('shared-seams', 0)} dossiers",
        f"# a seam = fan-in >= {shortlist.threshold} (SEAM_FANIN_THRESHOLD)",
        "",
    ]
    if shortlist.empty:
        out.append("no seam fits - nothing in the corpus shares a token stem with the query.")
        out.append("If the behaviour is genuinely new, build it; record `none - <why>` in the "
                   "dossier's ## Reuse affordance.")
    else:
        out.append("## candidates (ranked - read these before building)")
        for r in shortlist.ranked:
            out.append(_line(r))
        out.append("")
        out.append("## sources to open")
        for line in _sources(shortlist, corpus):
            out.append(f"- {line}")

    if shortlist.recall_dark:
        out.append("")
        out.append(
            f"recall partial: layers {', '.join(shortlist.recall_dark)} have no symbol extractor "
            "- a matching seam THERE would not appear above; check that layer by hand before "
            'concluding "no seam fits".'
        )
    elif not corpus.has_symbols:
        out.append("")
        out.append("note: symbol recall tier not adopted (inventory + affordance corpus only).")

    out.append("")
    out.append('Decision: wire the behaviour through one seam above, or reply "no seam fits" '
               "if none matches - then record the reuse decision in the feature's ## Reuse affordance.")
    return "\n".join(out) + "\n"


def _line(r: Ranked) -> str:
    c = r.candidate
    bits = []
    if c.kind:
        bits.append(c.kind)
    if c.file:
        bits.append(c.file)
    if c.file:
        bits.append(f"fan-in {r.fanin}")
    if r.is_seam:
        bits.append("SEAM")
    if c.detail and not c.kind:
        bits.append(c.detail)
    meta = " | ".join(bits)
    tag = "" if r.is_seed else " (neighbour)"
    src = "/".join(c.sources)
    return f"- {c.name}{tag}  [{meta}]  ({r.reason}; via {src})" if meta else f"- {c.name}{tag}  ({r.reason}; via {src})"


def _sources(shortlist: Shortlist, corpus: Corpus) -> list[str]:
    """The concrete files/records to open, in shortlist order, deduped. A candidate points at
    its OWN source: a symbol -> its def file; a declared/prose seam -> its dossier; an inventory
    key -> the inventory (via the generated MAP). `detail` is overloaded per source, so branch
    on which source the candidate came from, not on kind."""
    root_name = m.map_root().name
    lines: list[str] = []
    seen: set[str] = set()

    def add(line: str) -> None:
        if line not in seen:
            seen.add(line)
            lines.append(line)

    for r in shortlist.ranked:
        c = r.candidate
        if c.file:
            add(f"symbol def: {c.file}")
        if ("affordance-seam" in c.sources or "shared-seams" in c.sources) and c.detail:
            where = "FOUNDATION.md" if c.detail == "foundation" else f"features/{c.detail}.md"
            add(f"dossier: {root_name}/{where}")
        elif "inventory" in c.sources and not c.file:
            add(f"inventory `{c.detail}` (see {root_name}/generated/MAP.md)")
    return lines or ["(no file-backed sources - inspect the candidates above)"]


# ======================================================================================
# CLI
# ======================================================================================


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="+", help="a behaviour description, e.g. 'send a templated email'")
    args = parser.parse_args(argv)
    query = " ".join(args.query)

    corpus = load_corpus()
    ref_index = m.build_reference_index(corpus.symbol_files) if corpus.symbol_files else {}
    shortlist = assemble_shortlist(query, corpus, ref_index)
    print(render(shortlist, corpus), end="")
    return 0  # advisory: always succeeds (never a gate)


if __name__ == "__main__":
    sys.exit(main())

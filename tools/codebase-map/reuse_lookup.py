"""reuse-lookup — the behaviour->seam discovery entrypoint (codebase-map kit, S3).

    python <kit>/reuse_lookup.py "normalise a display name into a url slug"

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
any adopting repo, at any kit install prefix. Having no project layer also means nothing here
fails closed on a mis-rooted run, so the CLI asserts the resolved root is ADOPTED (it carries
.codebase-map.conf) and exits 2 if not: `corpus: 0 symbols` + `no seam fits` at exit 0 is a
confident answer from an empty population, which is worse than no answer.
This is bThriftyCompass S1's portable re-implementation; an adopting repo
retires any bespoke reuse-audit script and repoints its "reuse before building" step here. The
CLI produces the shortlist; the agent-instruction reuse-lookup.agent.md turns it into a
decision (wire through seam X, or "no seam fits").
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import UTC, datetime
from dataclasses import dataclass, field
from pathlib import Path

# `abspath`, NOT `resolve()`: this insert decides which path string `map_lib.__file__` carries,
# and map_lib.kit_dir()/the gate template both use abspath. Under a junctioned kit dir resolve()
# yields the LINK TARGET, so this entrypoint would stamp one prefix into the byte-compared
# artifacts while the gate re-renders another — a permanently STALE gate whose own printed
# remedy re-writes the wrong spelling and never converges (measured).
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent))

try:  # a non-UTF-8 stdout (stripped CI locale) must degrade a non-ASCII query echo, not crash it
    sys.stdout.reconfigure(errors="replace")
except (AttributeError, ValueError):
    pass

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
    for feature, text in m.load_dossier_texts(map_dir).items():
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

    # RANK THE WHOLE NEIGHBOUR POOL, THEN CAP. The cap used to slice `sorted(neighbours.items())`,
    # which is ALPHABETICAL, so the twelve slots went to the twelve names that sort earliest and
    # `_rank` only ever saw those twelve -- the sort below then ordered a pool the alphabet had
    # already chosen. Measured at base c4fcf5ad on the phrase this unit's spec records: every class
    # name here starts uppercase and every function name does not, ASCII orders uppercase first, so
    # a seed set containing one class filled all twelve slots from the 28 class names before any of
    # the 616 functions was considered. The twelve retained summed to fan-in 8; the twelve the
    # ranking keeps sum to 271, and the two sets do not intersect.
    #
    # Cost: `_rank` is one `fan_in` lookup per name, so this ranks the pool rather than a slice of
    # it. That is the price of the cap meaning anything, and it is paid once per probe.
    neighbour_ranked = [
        _rank(pool, corpus.threshold, ref_index, name, False, reason)
        for name, reason in sorted(neighbours.items())
    ]
    neighbour_ranked.sort(key=_shortlist_key)
    ranked.extend(neighbour_ranked[:NEIGHBOUR_CAP])

    ranked.sort(key=_shortlist_key)
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


def _shortlist_key(r: Ranked) -> tuple:
    """THE ordering key, stated once and read twice: once to CAP the neighbour pool, once to sort
    the shortlist that is printed.

    A second, retyped copy is exactly how the cap came to select by a criterion nobody chose --
    the slice was alphabetical while the sort was by fan-in, so the two disagreed silently and the
    ranking only ever ran on what the alphabet had already kept. Seeds sort first and are never
    capped; within a group it is descending fan-in, then name for a stable tie-break.
    """
    return (not r.is_seed, -r.fanin, r.candidate.name)


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
        # What the neighbour ranking does NOT mean. Twelve high-fan-in names read as twelve SEAMS
        # to everybody who did not write the ranker, and the fan-in behind them counts bare
        # identifier tokens with no symbol resolution (TOOL-aScouredKit-16) -- so a common short
        # name scores high for reasons that have nothing to do with reuse. The line discloses the
        # signal's limit rather than repairing it, which is a different unit.
        "# neighbours are ranked by fan-in, which counts NAME TOKENS and resolves no symbols:",
        "# a high rank means 'this name appears a lot', never 'this is the seam you want'",
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
    # Repo-RELATIVE map root (e.g. "memory/map"), not its leaf name — the default MAP_ROOT is
    # nested, and printing "map/features/…" would send the reader to a path that does not exist.
    try:
        root_name = m.map_root().relative_to(m.repo_root()).as_posix()
    except ValueError:
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


def _resolve_git_dir(root: Path) -> Path | None:
    """The COMMON git dir for ``root``, or None. Pure path math and two small file reads — NO
    child process, matching ``map_lib.resolve_root``'s own refusal to shell out and mirroring how
    ``memory-recall``'s ``recall-opened.js`` finds the same directory.

    In a primary tree ``.git`` is a DIRECTORY and is the answer. In a linked worktree it is a FILE
    holding ``gitdir: <path>``; that directory's ``commondir``, when present, names the shared one.
    The common dir is the point: every worktree of a repo shares it, so a probe run in one worktree
    is visible to a reader in another, which is what a five-worktree fleet needs.
    """
    dot = root / ".git"
    if dot.is_dir():
        return dot
    if not dot.is_file():
        return None
    m_gd = re.match(r"^gitdir:\s*(.+)$", dot.read_text(encoding="utf-8").strip())
    if not m_gd:
        return None
    gitdir = Path(os.path.abspath(root / m_gd.group(1).strip()))
    commondir = gitdir / "commondir"
    if commondir.is_file():
        return Path(os.path.abspath(gitdir / commondir.read_text(encoding="utf-8").strip()))
    return gitdir


def write_lookup(root: Path, query: str, n_shown: int) -> None:
    """Append one JSONL row recording that this probe RAN. Never fatal, never gating.

    WHY: ``BUILD-METHOD`` M5 names two reuse probes and only the recall one left evidence, so a
    checker asking "did a reuse probe run" could observe half the obligation. This is the other
    half. TOOL-aClosedDocket-2, from backlog row TOOL-aProvenReuse-4.

    ITS OWN FILE, under this kit's own name. Sharing ``memory-recall``'s log would make this kit
    depend on that kit's convention, which neither descriptor declares and which is exactly why the
    backlog row was filed rather than built when it was first found.

    THE FIELD NAMES ARE THE RECALL LOG'S, deliberately: ``type``, ``at``, ``query``, ``worktree``
    and ``n_shown``, so one reader parses both without a per-kit branch. ``type`` is not decoration —
    the existing reader FILTERS on it first, and a row without one is invisible to a reader built in
    that log's image.

    NEVER FATAL, and the whole body is inside the try INCLUDING the resolution. ``main`` records
    that a RESULT never fails and only its refusal exits non-zero; a telemetry line must not be the
    thing that breaks that. ``log_event`` in the recall kit leaves its own path resolution outside
    its ``try`` — a hole worth not copying.
    """
    try:
        common = _resolve_git_dir(root)
        if common is None:
            return
        path = common / "codebase-map" / "lookups.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        row = {
            "type": "lookup",
            "at": datetime.now(UTC).isoformat(timespec="seconds"),
            "query": query,
            "worktree": str(root),
            "n_shown": n_shown,
        }
        with path.open("a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    except OSError as exc:  # pragma: no cover - the answer outlives the record
        print(f"warning: lookup log not written ({exc})", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    # `<kit>` resolved, so the usage line --help prints names this install's real prefix.
    parser = argparse.ArgumentParser(description=__doc__.replace("<kit>", m.kit_rel()))
    parser.add_argument("query", nargs="+", help="a behaviour description, e.g. 'send a templated email'")
    args = parser.parse_args(argv)
    query = " ".join(args.query)

    # Refuse BEFORE loading: an unadopted/mis-rooted root yields an empty corpus, and every line
    # below would then render a confident "no seam fits" over a population that was never read.
    try:
        m.require_adopted_root()
    except m.MapError as exc:
        print(f"reuse-lookup refused: {exc}", file=sys.stderr)
        return 2

    corpus = load_corpus()
    ref_index = m.build_reference_index(corpus.symbol_files) if corpus.symbol_files else {}
    shortlist = assemble_shortlist(query, corpus, ref_index)
    print(render(shortlist, corpus), end="")
    # AFTER the answer is rendered, so a row means a lookup that ANSWERED. Before it, a crash in
    # render() would leave evidence of a probe whose result nobody ever saw.
    write_lookup(m.repo_root(), query, len(shortlist.ranked))
    return 0  # advisory: a RESULT never fails (never a gate). Only the refusal above exits non-zero.


if __name__ == "__main__":
    sys.exit(main())

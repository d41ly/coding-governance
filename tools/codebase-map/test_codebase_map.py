"""The codebase-map coverage + freshness gate (codebase-map kit).

Copied from `<kit>/test_codebase_map.template.py` at adoption into the directory named by
`.codebase-map.conf` GATE_FILE — it must live where the project's EXISTING test suite collects
it (zero CI changes: a test file is its own deployment). Also runnable standalone in projects
without a test framework: `python <this file>`. `<kit>` is wherever the kit is installed; the
gate finds it by walking up from itself, and every remedy it PRINTS spells the real prefix.

Remedies when this gate fails on your change:
- claim the new key in the owning `<MAP_ROOT>/features/<feature>.md` (create it from any
  existing dossier — headings are pinned, prose is free), or
- claim it in `<MAP_ROOT>/FOUNDATION.md` if it is shared substrate;
- `baseline.toml` never gains a key: the gate refuses one the baseline at the branch's base did not
  carry (the merge-base with the remote default branch) — claim it in a dossier instead;
- claim edits: regen artifacts with the command the failure prints (`map_lib.regen_cmd()`).

WHAT THIS GATE DOES NOT CHECK, stated here because a structural check reads as a semantic one to
everybody who did not write it:
- It does not read your CODE. Coverage is over the keys your extractors ENUMERATE, so a feature
  whose extractor does not see it is invisible to this gate and to the map.
- It does not check that a dossier's PROSE is true, only that its headings are present and its
  claimed keys exist. A dossier can describe a mechanism that was deleted last month.
- Freshness is a BYTE COMPARE of the artifacts this gate knows how to render. An artifact
  `gen_map.py` writes and this gate does not list is not compared at all — which is
  `TOOL-dTracedLattice-4`, a different unit, and it is why the tier list below is explicit rather
  than derived from the directory.
- A CONDITIONAL tier whose live population is empty compares nothing, and says so on every run
  rather than passing quietly. That announcement is not a verdict about your tree: it means this
  gate had nothing to compare, which is different from having compared and agreed.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


def _kit_dir() -> Path:
    """The kit dir — the directory holding map_lib.py — found from this gate file's own location,
    so the gate still needs no per-project placeholders.

    Two things vary independently. GATE_FILE points at whatever directory the project's test suite
    collects, which may be inside the kit dir or nowhere near it; and the kit dir may sit at any
    PREFIX under the repo root. So each ancestor of this file is probed in order: the ancestor
    itself (gate installed inside the kit dir), `<ancestor>/codebase-map` (the root convention),
    then `<ancestor>/*/codebase-map` (a one-segment prefix such as `<prefix>/`). The walk stops after
    the ancestor holding `.codebase-map.conf` OR `.git`, so it can never leave the project.

    The conf is in that boundary, not just `.git`, because `.git` is absent from perfectly ordinary
    trees — a `git archive` tarball, a docker build whose `.dockerignore` drops it, a vendored
    source drop. Measured with only the `.git` test: in such a tree the walk ran to the filesystem
    root and the `*/codebase-map` glob matched an UNRELATED kit copy outside the project, which the
    module-level import below then loaded and executed — the gate byte-comparing this repo's
    artifacts against a foreign engine at a foreign KIT version. The conf is committed, so it
    survives every export that drops `.git`.

    The kit dir's NAME is still the fixed convention — only its prefix is free. A prefix deeper
    than one segment is deliberately not searched: walking a whole repo downward is slow and
    ambiguous. The failure below names every path it probed, so a deeper install is TOLD what the
    gate looked for instead of being guessed at. `abspath`, not `resolve()`: a junctioned kit dir
    must anchor to the adopting repo, matching map_lib.resolve_root."""
    probed: list[str] = []
    here = Path(os.path.abspath(__file__))
    for parent in here.parents:
        candidates = [parent]
        # TOOL-aRepatriatedFork-46: the root-convention rung is the sibling-kit resolver's, which reads
        # the install receipt before it probes `<ancestor>/codebase-map`, so a renamed kit dir the
        # receipt records is found too. Its miss is recorded, never raised: the glob rung still runs.
        try:
            candidates.append(resolve_kit_dir("codebase-map", "map_lib.py", parent))
        except LookupError as exc:
            probed.append(f"{parent} (the sibling-kit resolver: {exc})")
        candidates += sorted(p for p in parent.glob("*/codebase-map") if p.is_dir())
        for candidate in candidates:
            if (candidate / "map_lib.py").is_file():
                return candidate
            probed.append(str(candidate))
        if (parent / ".codebase-map.conf").is_file() or (parent / ".git").exists():
            break
    raise RuntimeError(
        f"codebase-map kit dir (the directory holding map_lib.py) not found above {here}.\n"
        "Probed:\n  " + "\n  ".join(probed)
    )


sys.path.insert(0, str(_kit_dir()))

import map_extractors as ext  # noqa: E402
import map_lib as m  # noqa: E402

INVENTORY_IDS = ext.inventory_ids()
ID_RE = getattr(ext, "DECISION_ID_RE", m.DEFAULT_DECISION_ID_RE)


# ======================================================================================
# Real-tree assertions
# ======================================================================================


def test_every_inventory_key_is_claimed_or_baselined() -> None:
    inventories = ext.all_inventories()
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    cov = m.compute_coverage(inventories, m.owners_of(tree), tree.baseline)
    assert cov.clean, (
        "codebase-map coverage violations.\n"
        f"UNCLAIMED (new key? claim it in a feature dossier, or FOUNDATION.md for shared "
        f"substrate; baseline.toml is reserved for the initial backfill): {cov.unclaimed}\n"
        f"STALE CLAIMS (a dossier names a key that no longer exists): {cov.stale_claims}\n"
        f"STALE BASELINE (delete the line — the item is gone): {cov.stale_baseline}\n"
        f"LAZY BASELINE (now claimed — delete its baseline line): {cov.lazy_baseline}"
    )


def test_baseline_never_gains_a_key() -> None:
    """The baseline is SHRINK-ONLY, graded against its own earlier self: a key the baseline at the
    branch's base did not carry is a refusal. The four coverage asserts above cannot see it, since
    moving a claim from a dossier into the baseline keeps every one of them clean.

    UNGRADED, AND SAYS SO, when there is no base to read — no fetched `origin` default branch, or
    no baseline at the base. The compared sha and both sides' key counts print on every graded run,
    so a comparison of the committed file against itself (CI on the landed tip) is visible."""
    root = m.repo_root()
    base, why = m.resolve_compare_base(root)
    if base is None:
        print(f"     UNGRADED: {why}")
        return
    added, note = m.derive_baseline_additions(root, base)
    if added is None:
        print(f"     UNGRADED: {note} ({why})")
        return
    print(f"     compared against {base[:12]} ({why}): {note}")
    assert not added, (
        "baseline.toml GAINED keys its base did not carry — claim each in a feature dossier, or "
        "FOUNDATION.md for shared substrate, and delete it from the baseline:\n"
        + "\n".join(f"  {inv}: {key}" for inv, keys in added.items() for key in keys)
    )


def test_dossier_prose_headings_pinned() -> None:
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    features_dir = m.map_root() / "features"
    for d in tree.dossiers:
        text = (features_dir / f"{d.feature}.md").read_text(encoding="utf-8")
        for heading in m.REQUIRED_HEADINGS:
            assert heading in text, f"{d.source}: required section missing: {heading}"


def test_dossier_affordance_present_or_graced() -> None:
    """GRACED presence of the `## Reuse affordance` section: every dossier NOT on the shrink-only
    affordance-exempt list must carry the heading with at least one `seam:` line or a `none`
    declaration. New dossiers are never exempt (the list only shrinks + drops on touch), so a new
    feature is forced to record its reuse decision; the exempt baseline keeps adoption from
    retro-redding the fleet. Content quality is the un-gatable ceiling — reported, never gated."""
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    features_dir = m.map_root() / "features"
    texts = {
        d.feature: (features_dir / f"{d.feature}.md").read_text(encoding="utf-8")
        for d in tree.dossiers
    }
    offenders = m.affordance_offenders(texts, m.load_affordance_exempt())
    assert not offenders, (
        f"dossiers missing the '{m.AFFORDANCE_HEADING}' section — add a `seam: <id> — reuse for "
        f"<need>; extend via <point>` line per reusable seam, or `none — <why feature-specific>`: "
        f"{offenders}"
    )


# A NEW DOSSIER'S `decisions` LIST STARTS EMPTY AND IS NOT FINISHED THERE. It holds the unit ids
# that govern the feature, it is graded shrink-only by the check below, and it is filled as those
# ids are learned rather than guessed — a guessed id RESOLVES, which makes it worse than a visibly
# empty list. This guidance sits here, beside the check that reads the population, rather than in
# the scaffolder: the skeleton it was first written into is the one file the dossier loader
# EXCLUDES from that population, so the check could never see it.
def test_dossier_decisions_are_declining() -> None:
    """How many dossiers declare NO decisions, against a shrink-only pin.

    An empty list passes validation, so nothing has ever failed on the field, so nobody fills
    it, so the reuse audit returns a seam with no rationale. That is the vacuous-selector
    class: a rule that binds nothing reports clean forever. The pin is what converts "legal"
    into "declining".

    UNSET OR EMPTY IS UNGRADED, AND SAYS SO. A fresh adopter has no measurement of their own
    corpus, and a number copied from another tree is either vacuous or permanently red. Reading
    an absent pin as 0 would red their first run; reading it as "skip" silently would make this
    check the very thing it exists to close. So it announces.
    """
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    if not tree.dossiers:
        # UNGRADED, not failed. A freshly seeded tree has no dossiers yet, and asserting over
        # an empty population is how this check reds an adopter on their first run. It binds
        # the day the first dossier lands -- the same shape the unset-pin branch below uses.
        print("     UNGRADED: no dossiers under the map root yet; this check grades a "
              "population that does not exist, and binds when the first dossier lands")
        return
    empty = sorted(d.feature for d in tree.dossiers if not d.decisions)
    raw = (m.load_conf().get("DOSSIER_DECISIONS_EMPTY_PIN", "") or "").strip()
    if not raw:
        print(f"     UNGRADED: {len(empty)} of {len(tree.dossiers)} dossier(s) declare no decisions; "
              "set DOSSIER_DECISIONS_EMPTY_PIN in the kit conf to a value measured on THIS corpus")
        return
    pin = int(raw)
    assert len(empty) <= pin, (
        f"{len(empty)} of {len(tree.dossiers)} dossier(s) declare no decisions, over a "
        f"shrink-only pin of {pin}. Fill one, or lower the pin with the reading beside it.\n"
        f"empty: {empty}"
    )


def test_dossier_prose_carries_no_typed_count() -> None:
    """No present-tense digit count of an inventory population in dossier prose.

    The map derives every inventory's size into MAP.md, so "the 86 legs" in a dossier is a second
    answer that goes stale on the next leg (charter §7). A sentence reading as a past measurement
    is frozen and passes. NOT checked: counts spelled as words, counts inside fences (the toml
    title included) or code spans, and nouns outside the map's inventories.
    """
    texts = m.load_dossier_texts(m.map_root())
    hits: list[str] = []
    candidates = frozen = 0
    for name, text in texts.items():
        found, n_frozen = m.measure_typed_counts(text, INVENTORY_IDS)
        candidates += len(found) + n_frozen
        frozen += n_frozen
        source = "FOUNDATION.md" if name == "foundation" else f"{name}.md"
        hits.extend(f"{source}:{line}: {match}" for line, match in found)
    print(f"     typed-count lint: {candidates} candidate(s) read in {len(texts)} dossier(s), {frozen} frozen")
    assert not hits, (
        "a present-tense count of an inventory population in dossier prose:\n  "
        + "\n  ".join(hits)
        + "\nRemedy, one of: freeze it as a past-tense reading that cites the record which measured "
        "it; point at the file that owns it; or rewrite the sentence without it."
    )


def test_path_derived_keys_are_posix() -> None:
    for inv_id, keys in ext.all_inventories().items():
        offenders = [k for k in keys if "\\" in k]
        assert not offenders, f"{inv_id}: non-POSIX keys {offenders}"



#: CONDITIONAL TIERS — an artifact whose population may legitimately be empty in an adopting repo.
#: `(tier name, extractor attribute, artifact filename, map_lib renderer)`.
#:
#: THE LIST IS THE MECHANISM, and that is `TOOL-dTracedLattice-2` S3. The reporter below walks THIS
#: list, so adding a tier is adding a row here and nothing else — an author cannot forget to write
#: the reporting line, because there is no reporting line to write. Before this, the symbol tier was
#: an `if symbols:` with no `else`, so an empty population compared nothing and the gate passed,
#: which is indistinguishable from having compared and agreed.
CONDITIONAL_TIERS: list[tuple[str, str, str, str]] = [
    ("symbol", "all_symbols", "symbols.json", "render_symbols_json"),
]

def test_generated_artifacts_are_fresh() -> None:
    inventories = ext.all_inventories()
    tree = m.load_map_tree(INVENTORY_IDS, decision_id_re=ID_RE)
    owners = m.owners_of(tree)
    gen_dir = m.map_root() / "generated"
    fresh = {
        gen_dir / "inventories.json": m.render_inventories_json(inventories, INVENTORY_IDS),
        gen_dir / "MAP.md": m.render_map_md(inventories, INVENTORY_IDS, owners, tree.baseline),
        gen_dir / "CARDS.md": m.render_cards_md(tree, INVENTORY_IDS),
    }
    # CONDITIONAL tiers, one record each. A tier that does not run is REPORTED, never omitted: an
    # `if population:` with no `else` compares nothing and passes, which reads exactly like a tier
    # that compared and agreed. Renderers are byte-deterministic (sorted ids, POSIX, LF), so every
    # byte-compare below holds identically on Windows and Linux.
    skipped: list[tuple[str, str, bool]] = []
    for tier, attr, artifact, renderer in CONDITIONAL_TIERS:
        population = getattr(ext, attr, list)()
        path = gen_dir / artifact
        if population:
            fresh[path] = getattr(m, renderer)(population)
        else:
            skipped.append((tier, artifact, path.is_file()))

    regen = m.regen_cmd()  # spelled for THIS install's prefix — a remedy must name a real path

    # ANNOUNCE BEFORE COMPARING. A skip printed after the compare loop is swallowed by the first
    # unrelated staleness failure, and "which tiers did not run" is exactly what a reader needs
    # when something else is red. The refusal below still runs last, because it is a verdict.
    orphaned = [(tier, artifact) for tier, artifact, committed in skipped if committed]
    for tier, artifact, committed in skipped:
        if not committed:
            print(f"skipped {tier} tier — this project declares no live population for it, and no "
                  f"{artifact} is committed, so NOTHING WAS COMPARED for this tier")

    for path, expected in fresh.items():
        assert path.is_file(), f"missing generated artifact {path} — regen: {regen}"
        committed = m.lf(path.read_text(encoding="utf-8"))
        assert committed == expected, f"STALE {path.name} — regen: {regen}"
    assert not orphaned, "\n".join(
        f"DARK {tier} tier — {artifact} IS committed and the live population is EMPTY, so this gate "
        f"compared nothing while a generated artifact sits in the tree claiming to be current. "
        f"Either restore the extractor that produced it, or delete {artifact}. — regen: {regen}"
        for tier, artifact in orphaned)


# ======================================================================================
# Standalone runner (projects without a test framework)
# ======================================================================================

if __name__ == "__main__":
    failures = 0
    for fn in (
        test_every_inventory_key_is_claimed_or_baselined,
        test_baseline_never_gains_a_key,
        test_dossier_prose_headings_pinned,
        test_dossier_affordance_present_or_graced,
        test_dossier_decisions_are_declining,
        test_dossier_prose_carries_no_typed_count,
        test_path_derived_keys_are_posix,
        test_generated_artifacts_are_fresh,
    ):
        try:
            fn()
            print(f"ok   {fn.__name__}")
        except AssertionError as exc:
            print(f"FAIL {fn.__name__}\n{exc}")
            failures += 1
    sys.exit(1 if failures else 0)

"""tag_bundle — `gov tag bundle`, a tag's node and every inbound edge as ranges to pull, and the two edge
arms `gov_tag.py check --only` runs (PLAY-dOrderedCharter-25).

    python gov_tag.py bundle <address> [--inline --bytes <n>] [--under <dir>] [--json]
    python gov_tag.py check --only type-registered|target-resolves [--base <rev>]
    python tag_bundle.py --selftest

A bundle is the node, `show`'s row, then every inbound edge grouped by type in `edges.toml`'s order:
the declared edges `edge_grammar.read_tree_edges` reads whose target `resolve_edge` resolves to the node,
each the `(target, inverse, source)` triple `derive_inverse_edges` derives, and the `cites` rows `refs`
prints. Each row is one range, `path:span · type · bytes`, `span` the innermost extent the index holds
around the source's line, else `whole`. Members are the `part-of` rows, instructions the `instructs`
rows, regions every row carrying a span; an empty one renders a slot state, never a blank.

Past `tags.bundle-rows` rows, rows fold by their source's kit directory (`<tool root>/<kit>/`, else the
path's first segment), the largest (type, directory) group first, until the count is within the budget;
`--under <dir>` lists one directory's rows unfolded, matched against row paths and never joined to a
filesystem path. `--inline --bytes <n>` inlines whole rows in manifest order while the running total
stays within `<n>`; the first row that would pass it, and every row after, stays a manifest row.
`tags.bundle` is `manifest` (refuses `--inline`), `inline` (inlines every call, refuses one without
`--bytes`) or `both`. gov_tag.py reads both keys and passes them here.

The two arms call `check_edges` and `run_resolve` over `read_tree_edges`' edges and never re-derive
them; they run only when `--only` names them, so `gov_tag.py check` keeps its own verdict.
Exit 0 green, 1 red or an address that resolves to no row, 2 a refusal.
"""
from __future__ import annotations

import os
import pathlib
import subprocess
import sys

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

import edge_grammar as eg  # noqa: E402
import tag_index as ti  # noqa: E402

MODES = ("manifest", "inline", "both")
ARMS = ("type-registered", "target-resolves")
#: the two named sections that are type views; regions is every row carrying a span
SECTIONS = {"part-of": "members", "instructs": "instructions"}
REGIONS_NOT_INSTALLED = ("not-installed: dTotalRecall's span extractors feed it; the fallback is the "
                         "whole-file range each row names")


def read_node_spans(con, path) -> list[tuple]:
    """`(first, last)` of every node the index defines in `path`."""
    rows = con.execute(ti.VIEW_ROWS + f" WHERE p.path=? AND p.kind IN ({','.join('?' * len(ti.DEFINE_KINDS))})",
                       (path, *ti.DEFINE_KINDS)).fetchall()
    return [(line, ti.read_text_of(con, blob, ex, kind, line)[0]) for _t, _p, line, kind, blob, ex in rows]


def derive_span(spans, line):
    """The innermost span holding `line`, the latest first line; None where the index holds none."""
    inside = [s for s in spans if s[0] <= line <= s[1]]
    return max(inside, key=lambda s: (s[0], -s[1])) if inside else None


def read_range(root, path, span) -> bytes:
    """The bytes of `span` of the working-tree file, or the whole file for None; b"" for no file."""
    try:
        data = (pathlib.Path(root) / path).read_bytes()
    except OSError:
        return b""
    return data if span is None else b"".join(data.splitlines(keepends=True)[span[0] - 1:span[1]])


def derive_group(path, tool_root) -> str:
    """A row's fold group: its kit directory under the tool root, else its path's first segment."""
    parts = path.split("/")
    if f"{'/'.join(parts[:-1])}/".startswith(f"{tool_root}/") and len(parts) > tool_root.count("/") + 2:
        return "/".join(parts[:tool_root.count("/") + 2]) + "/"
    return parts[0] + "/" if len(parts) > 1 else path


def read_bundle_rows(root, con, ns_path, node, refs, tool_root) -> list[dict]:
    """Every inbound row of `node`, typed rows and `refs`' cites, in registry order, one per range."""
    types = eg.read_edge_types()
    tag = node["tag"]
    rc = eg.build_resolve_context(root, ns_path)
    rc["con"] = con  # the caller's index, its view loaded; the caller closes it
    edges, _refused = eg.read_tree_edges(root, None)  # a refused line is the edges leg's red
    # ponytail: only an edge naming the tag can resolve to it, so the rest are never resolved
    named = [e for e in edges if any(t.partition("@")[0] == tag for t in e["targets"])]
    type_of = {r["inverse"]: t for t, r in types.items()}
    hits = []
    for target, inverse, source in eg.derive_inverse_edges(named, types):
        if target.partition("@")[0] != tag:
            continue
        state, why = eg.resolve_edge(target, rc)
        if state == "resolved" and why.split(" · ")[0] == tag:
            path, _, line = source.rpartition(":")
            hits.append((type_of[inverse], path, int(line)))
    hits += [("cites", r["path"], r["line"]) for r in refs]
    order = {t: i for i, t in enumerate(types)}
    rows, seen, spans = [], set(), {}
    for kind, path, line in hits:
        if path not in spans:
            spans[path] = read_node_spans(con, path)
        span = derive_span(spans[path], line)
        if (kind, path, span) in seen:
            continue
        seen.add((kind, path, span))
        rows.append({"type": kind, "path": path, "span": f"{span[0]}-{span[1]}" if span else "whole",
                     "bytes": len(read_range(root, path, span)), "range": span,
                     "group": derive_group(path, tool_root)})
    return sorted(rows, key=lambda r: (order.get(r["type"], len(order)), r["path"], r["range"] or (0, 0)))


def fold_rows(rows, budget) -> tuple[list, bool]:
    """`(entries, over)`: the rows with the largest (type, group) folded first until the count is within
    `budget`; a fold entry stands where its group's first row stood. `over` when every group that folds
    has folded and the count still passes the budget: the bundle prints folded, never cut."""
    groups: dict = {}
    for r in rows:
        groups.setdefault((r["type"], r["group"]), []).append(r)
    folded, count = set(), len(rows)
    for key in sorted(groups, key=lambda k: (-len(groups[k]), k)):
        if count <= budget or len(groups[key]) < 2:  # a one-row group folds to one row: nothing gained
            break
        folded.add(key)
        count -= len(groups[key]) - 1
    out, done = [], set()
    for r in rows:
        key = (r["type"], r["group"])
        if key not in folded:
            out.append(r)
        elif key not in done:
            done.add(key)
            out.append({"type": key[0], "fold": key[1], "rows": len(groups[key]),
                        "bytes": sum(g["bytes"] for g in groups[key])})
    return out, count > budget


def run_bundle(root, con, ns_path, node, refs, *, tool_root, mode, budget, inline, nbytes, under, as_json) -> int:
    """S1-S4 over one resolved node: refusals first, then the manifest, folded or inlined as asked."""
    import json
    if mode not in MODES:
        print(f"tags: refused · tags.bundle is '{mode}', which is none of {', '.join(MODES)}", file=sys.stderr)
        return 2
    if mode == "manifest" and inline:
        print("tags: refused · tags.bundle is manifest, which refuses --inline", file=sys.stderr)
        return 2
    inline = inline or mode == "inline"
    if inline and nbytes is None:
        print(f"tags: refused · inlining needs its byte budget, --bytes <n> (tags.bundle is {mode})", file=sys.stderr)
        return 2
    rows = read_bundle_rows(root, con, ns_path, node, refs, tool_root)
    over = False
    if under is not None:
        rows = [r for r in rows if r["group"].rstrip("/") == under.rstrip("/")]
        entries = rows
    else:
        entries, over = fold_rows(rows, budget)
    inlined, total = 0, 0
    if inline:
        stop = False
        for e in entries:
            if "fold" in e:
                continue
            stop = stop or total + e["bytes"] > nbytes
            if not stop:
                e["inline"] = read_range(root, e["path"], e["range"]).decode("utf-8", errors="replace")
                total += e["bytes"]
                inlined += 1
    n_span = sum(r["range"] is not None for r in rows)
    sections = {name: sum(r["type"] == kind for r in rows) or "searched-empty" for kind, name in SECTIONS.items()}
    sections["regions"] = n_span or REGIONS_NOT_INSTALLED
    span = (node["line"], node["end_line"])
    head = {"tag": node["tag"], "path": node["path"], "span": f"{span[0]}-{span[1]}", "kind": node["kind"],
            "bytes": len(read_range(root, node["path"], span))}
    if as_json:
        keep = ("path", "span", "type", "bytes", "inline", "fold", "rows")
        print(json.dumps({"node": head, "rows": [{k: e[k] for k in keep if k in e} for e in entries],
                          "sections": sections, "over_budget": over}, indent=2))
        return 0
    print(f"tags: bundle · {head['tag']} · {head['path']}:{head['span']} · {head['kind']} · {head['bytes']} bytes")
    by_type: dict = {}
    for e in entries:
        by_type.setdefault(e["type"], []).append(e)
    order = list(eg.read_edge_types())  # the registry's order, the two named sections printed empty too
    for kind in sorted(set(by_type) | set(SECTIONS), key=lambda k: order.index(k) if k in order else len(order)):
        group = by_type.get(kind, [])
        label = f"{SECTIONS[kind]} · {kind}" if kind in SECTIONS else kind
        n = sum(e.get("rows", 1) for e in group)
        print(f"tags: {label} · " + (f"{n} row{'s' if n != 1 else ''}" if group else "searched-empty"))
        for e in group:
            if "fold" in e:
                print(f"tags:   {e['fold']} · {kind} · {e['rows']} rows · {e['bytes']} bytes · "
                      f"open with --under {e['fold']}")
                continue
            print(f"tags:   {e['path']}:{e['span']} · {kind} · {e['bytes']} bytes")
            for ln in e.get("inline", "").splitlines():
                print(f"tags:     | {ln}")
    print(f"tags: regions · {n_span} of {len(rows)} rows carry a span" if n_span else f"tags: regions · {sections['regions']}")
    shown = len(entries)
    if under is not None:
        print(f"tags: {shown} rows under {under}, unfolded")
    else:
        print(f"tags: {shown} rows of {len(rows)}, budget {budget} (tags.bundle-rows), "
              f"{sum('fold' in e for e in entries)} groups folded")
    if over:
        print(f"tags: still over the budget of {budget} with every group folded; printed folded, never cut")
    if inline:
        print(f"tags: inlined {inlined} rows, {total} of {nbytes} bytes; "
              f"{sum('fold' not in e for e in entries) - inlined} stay manifest rows")
    return 0 if rows or under is None else 1


def run_edge_arm(root, con, ns_path, arm, base) -> int:
    """`check --only <arm>`: `check_edges`' reds over the tree's edges, or `run_resolve`'s, one line each."""
    types = eg.read_edge_types()
    rc = eg.build_resolve_context(root, ns_path)
    rc["con"] = con
    edges, _refused = eg.read_tree_edges(root, base)
    reds = eg.check_edges(edges, types, ti.read_namespaces(ns_path), rc["classes"])
    if arm == "target-resolves":  # check_edges marks the unarmed targets run_resolve passes over
        reds, _counts = eg.run_resolve(edges, rc)
    for r in reds:
        print(f"tags: {arm} · {r.removeprefix('edges: ')}")
    print(f"tags: {arm} · {'RED' if reds else 'green'} · {len(edges)} edge(s), {len(reds)} red")
    return 1 if reds else 0


# ------------------------------------------------------------------------------------------ the plants

TAG = "practice.land"
EDGE = "**Edges:** {}={}\n"
LAND = ("# Land\n\n## Members\n\n" + EDGE.format("part-of", TAG) + "\n## Cites\n\nsee `" + TAG + "` here\n")
NOTE = "# gov:note fixture refs=" + TAG + "\n"
#: AC1's sources: a part-of in a guide section and one in a whole record, a unit selecting the tag, a cite
MANIFEST = {"memory/guides/LAND.md": LAND, "memory/notes/whole.md": EDGE.format("part-of", TAG),
            "tools/corekit/instructions.toml": f'[[unit]]\ntag = "unit.alpha"\nselect = ["{TAG}"]\n'}


def derive_fold_files(alpha, beta, notes) -> dict:
    files = {f"tools/alpha/a{i:02d}.py": NOTE for i in range(alpha)}
    files.update({f"tools/beta/b{i:02d}.py": NOTE for i in range(beta)})
    files.update({f"memory/notes/n{i:02d}.md": EDGE.format("part-of", TAG) for i in range(notes)})
    return files


#: AC4's records: four of 70 bytes and a last of 33, so the last would fit the budget the fourth broke
INLINE = {f"memory/notes/n{i}.md": EDGE.format("part-of", TAG) + "x" * (36 if i < 4 else 0) + ("\n" if i < 4 else "")
          for i in range(5)}
PLANT_FILES = {
    "bundle-manifest": MANIFEST, "bundle-mode-values": MANIFEST,
    "bundle-fold": derive_fold_files(30, 12, 8), "bundle-rows-values": derive_fold_files(25, 12, 8),
    "bundle-inline": INLINE,
    "bundle-unregistered-type": {"memory/notes/site.md": EDGE.format("relates-to", TAG)},
    "bundle-dangling-target": {"memory/notes/site.md": EDGE.format("instructs", "practice.nosuch")},
    "bundle-empty-sections": {"memory/notes/whole.md": EDGE.format("part-of", TAG)},
}
#: S8: each bundle case sets the fixture's `practice` row to `selects`, as the tree registers it
PRACTICE_ROLE = ('extractor = "fixture_tags:extract_declared"\nrole = "describes"',
                 'extractor = "fixture_tags:extract_declared"\nrole = "selects"')


def read_printed(lines) -> tuple[list, list, dict]:
    """`(rows, folds, headers)` of a text bundle: each row `(path, span, type, bytes)`, each fold
    `(dir, type, n)`, and each type header's text by its first word."""
    import re
    row_re = re.compile(r"^tags:   (\S+):(\d+-\d+|whole) · (\S+) · (\d+) bytes$")
    fold_re = re.compile(r"^tags:   (\S+/) · (\S+) · (\d+) rows · \d+ bytes · open with --under \S+$")
    rows, folds, heads = [], [], {}
    for ln in lines:
        m, f = row_re.match(ln), fold_re.match(ln)
        if m:
            rows.append((m.group(1), m.group(2), m.group(3), int(m.group(4))))
        elif f:
            folds.append((f.group(1), f.group(2), int(f.group(3))))
        elif ln.startswith("tags: ") and not ln.startswith("tags:  "):
            heads.setdefault(ln[6:].split(" · ")[0], ln)
    return rows, folds, heads


def run_bundle_plant(plant, run, say, write) -> int:
    """One `bundle-*` case over the fixture `gov_tag.py` built with its files: `run(verb, address, sets,
    **opts)` -> (exit, printed lines); `write(files)` edits the working tree. 0 only when every step held."""
    import json
    if plant in ("bundle-unregistered-type", "bundle-dangling-target"):
        arm, good = (("type-registered", EDGE.format("part-of", TAG)) if plant == "bundle-unregistered-type"
                     else ("target-resolves", EDGE.format("instructs", TAG)))
        rc, out = run("check", None, only=arm)
        want = ("memory/notes/site.md:1", "relates-to" if arm == "type-registered" else "instructs=practice.nosuch")
        named = rc == 1 and any(all(w in ln for w in want) for ln in out)
        write({"memory/notes/site.md": good})
        rc2, _ = run("check", None, only=arm)
        say(f"{arm}: rc={rc}, {'named' if named else 'NOT named'} {' and '.join(want)}; "
            f"with {good.strip().removeprefix('**Edges:** ')}: rc={rc2}")
        return rc if named and rc2 == 0 else 1 if rc == 0 else 3
    if plant == "bundle-manifest":
        rc, out = run("bundle", TAG)
        rows, _f, heads = read_printed(out)
        _r, refs = run("refs", TAG)
        cited = sorted(ln[6:].rpartition(":")[0] for ln in refs if ln.startswith("tags: ") and "citation(s)" not in ln)
        first = bool(out) and out[0].startswith(f"tags: bundle · {TAG} · ")
        members = [r for r in rows if r[2] == "part-of"]
        ok = (rc == 0 and first and len(members) == 2 and sum(r[2] == "instructs" for r in rows) == 1
              and sorted(r[0] for r in rows if r[2] == "cites") == cited and cited
              and heads.get("members", "").endswith("2 rows") and heads.get("instructions", "").endswith("1 row")
              and any(r[1] != "whole" for r in members))
        say(f"manifest: node first {first}, {len(members)} members, {len(rows)} rows each a span and bytes, "
            f"cites {'equal' if ok else 'checked'} to refs" + ("" if ok else " · FAILED"))
        return 0 if ok else 1
    if plant == "bundle-fold":
        rc, out = run("bundle", TAG)
        rows, folds, _h = read_printed(out)
        rc2, under = run("bundle", TAG, under="tools/alpha/")
        u_rows, u_folds, _h = read_printed(under)
        ok = (rc == 0 and len(rows) + len(folds) <= 40 and folds == [("tools/alpha/", "cites", 30)]
              and rc2 == 0 and len(u_rows) == 30 and not u_folds and all(r[0].startswith("tools/alpha/") for r in u_rows))
        say(f"fold: {len(rows) + len(folds)} rows printed of 50, folded {folds}; "
            f"--under tools/alpha/ listed {len(u_rows)} rows unfolded" + ("" if ok else " · FAILED"))
        return 0 if ok else 1
    if plant == "bundle-rows-values":
        seen = []
        for value in ("20", "40", "80"):
            rc, out = run("bundle", TAG, {"tags.bundle-rows": value})
            rows, folds, _h = read_printed(out)
            seen.append((value, rc, len(rows) + len(folds), bool(folds)))
        ok = [s[3] for s in seen] == [True, True, False] and all(s[1] == 0 and s[2] <= int(s[0]) for s in seen[:2]) \
            and seen[2][2] == 45
        say("rows values: " + ", ".join(f"{v} -> {n} rows{' folded' if f else ''}" for v, _rc, n, f in seen)
            + ("" if ok else " · FAILED"))
        return 0 if ok else 1
    if plant == "bundle-inline":
        rc, out = run("bundle", TAG, inline=True, nbytes=200, as_json=True)
        rows = json.loads("\n".join(out))["rows"] if rc == 0 else []
        flags = ["inline" in r for r in rows]
        total = sum(r["bytes"] for r in rows if "inline" in r)
        whole = all(len(r["inline"].encode("utf-8")) == r["bytes"] for r in rows if "inline" in r)
        cut = flags.index(False) if False in flags else len(flags)
        ok = (rc == 0 and len(rows) == 5 and flags == [True] * cut + [False] * (len(flags) - cut) and 0 < cut < 5
              and total <= 200 and total + rows[cut]["bytes"] > 200 and total + rows[-1]["bytes"] <= 200 and whole)
        say(f"inline: {cut} of {len(rows)} rows inlined, {total} of 200 bytes, every range whole {whole}; "
            "the row past the budget and every row after stay manifest rows" + ("" if ok else " · FAILED"))
        return 0 if ok else 1
    if plant == "bundle-mode-values":
        key = "tags.bundle"
        m_rc, m_out = run("bundle", TAG, {key: "manifest"}, inline=True, nbytes=200)
        i_rc, i_out = run("bundle", TAG, {key: "inline"})
        i2_rc, i2_out = run("bundle", TAG, {key: "inline"}, nbytes=200)
        b_rc, b_out = run("bundle", TAG, {key: "both"})
        b2_rc, b2_out = run("bundle", TAG, {key: "both"}, inline=True, nbytes=200)

        def inlined(out):
            return any(ln.startswith("tags:     | ") for ln in out)
        got = {"manifest --inline": (m_rc, any(key in ln for ln in m_out)),
               "inline bare": (i_rc, any("--bytes" in ln for ln in i_out)),
               "inline --bytes": (i2_rc, inlined(i2_out)), "both bare": (b_rc, not inlined(b_out)),
               "both --inline": (b2_rc, inlined(b2_out))}
        ok = got == {"manifest --inline": (2, True), "inline bare": (2, True), "inline --bytes": (0, True),
                     "both bare": (0, True), "both --inline": (0, True)}
        say("mode values: " + ", ".join(f"{k} rc={v[0]}{'' if v[1] else ' WRONG'}" for k, v in got.items()))
        return 0 if ok else 1
    # bundle-empty-sections: one whole-record member, no instructs row and no span
    rc, out = run("bundle", TAG)
    _rows, _f, heads = read_printed(out)
    ok = (rc == 0 and heads.get("instructions", "").endswith("· searched-empty")
          and heads.get("regions", "") == f"tags: regions · {REGIONS_NOT_INSTALLED}")
    say("empty sections: instructions searched-empty, regions not-installed naming its fallback" if ok
        else f"empty sections: FAILED · {heads}")
    return 0 if ok else 1


# ------------------------------------------------------------------------------------------ the selftest

#: `<plant and flags>|<exit>|<a line it must print>`: each row reads `gov_tag.py --fixture --plant <row>`'s run
SELFTEST_ROWS = """\
bundle-manifest|0|tags: bundle · practice.land · tools/corekit/core.tags:1-1 · tag ·
bundle-manifest|0|cites equal to refs
bundle-fold|0|fold: 21 rows printed of 50, folded [('tools/alpha/', 'cites', 30)]; --under tools/alpha/ listed 30 rows unfolded
bundle-rows-values|0|rows values: 20 -> 10 rows folded, 40 -> 21 rows folded, 80 -> 45 rows
bundle-inline|0|inline: 2 of 5 rows inlined, 140 of 200 bytes, every range whole True;
bundle-mode-values|0|mode values: manifest --inline rc=2, inline bare rc=2, inline --bytes rc=0, both bare rc=0, both --inline rc=0
bundle-unregistered-type|1|type-registered: rc=1, named memory/notes/site.md:1 and relates-to; with part-of=practice.land: rc=0
bundle-dangling-target|1|target-resolves: rc=1, named memory/notes/site.md:1 and instructs=practice.nosuch; with instructs=practice.land: rc=0
bundle-empty-sections|0|empty sections: instructions searched-empty, regions not-installed naming its fallback
"""


def run_selftest() -> int:
    """The `tags bundle selftest` leg: every bundle plant, each row's exit and line."""
    failed, runs = 0, {}
    rows = [r.split("|") for r in SELFTEST_ROWS.splitlines() if r.strip()]
    for plant, rc, want in rows:
        if plant not in runs:  # one run per plant and flags, read by each of its rows
            runs[plant] = subprocess.run([sys.executable, str(KIT_DIR / "gov_tag.py"), "--fixture", "--plant",
                                          *plant.split()], capture_output=True, text=True, encoding="utf-8",
                                         errors="replace")
        p = runs[plant]
        out = p.stdout + p.stderr
        if p.returncode == int(rc) and want in out:
            print(f"arm ok    bundle plant {plant}")
            continue
        failed += 1
        print(f"arm FAIL  bundle plant {plant} — wanted rc={rc} + {want}, got rc={p.returncode}")
        print("".join(f"      {ln}\n" for ln in out.splitlines()), end="")
    if failed:
        print(f"FAIL — {failed} of {len(rows)} bundle plant rows failed")
        return 1
    print(f"PASS — the bundle plants, {len(rows)} rows")
    return 0


if __name__ == "__main__":
    if sys.argv[1:] != ["--selftest"]:
        print("usage: python tag_bundle.py --selftest; the verb is `gov_tag.py bundle <address>`", file=sys.stderr)
        sys.exit(2)
    sys.exit(run_selftest())

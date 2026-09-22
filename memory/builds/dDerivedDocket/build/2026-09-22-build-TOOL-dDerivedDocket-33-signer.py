#!/usr/bin/env python3
# **Serves:** journal TOOL-dDerivedDocket-33
"""signer — the delegated signing of the D2 same-id table and the D6 triage table.

    python <this file>                                   # sign unit 11's worksheet pair
    python <this file> --check                           # re-derive both records, diff the tracked copies
    python <this file> --worksheets <same-id> <triage> [--tail landing|switch] [--check]

WHAT THIS IS. The owner delegated two signatures to the dDerivedDocket run instead of giving them
personally (the mandate record's "The single owner turn" section). This file IS the signature: it
reads the planner's two worksheets, applies the rules of TOOL-dDerivedDocket-33's spec section 4,
and writes two markdown records beside itself. It is a pure function of the worksheets and of the
tree it runs in, so `--check` re-derives both records and fails naming every row that no longer
re-derives. No byte of either record is authored.

WHAT IT READS, AND WHERE.
  - U4, T2, T3 and T5's liveness read the SIGNING TREE — the checkout this file sits in.
  - T4 and T5 read a triage row's own text with `git show <sha>:<file>` at the sha the triage
    worksheet's `#` line records, never from the working tree: the landing reconcile re-signs after
    the shards became views, and a row read from the tree would be another ask's text or nothing.
  - The planner's history evidence (specced-in-place, born-in-spec-commit, the overlap score) is
    CONSUMED from the worksheet and never re-walked: a second walk is a second answer.

WHAT IT DOES NOT CHECK, said out loud because a signature reads as a judgment to everybody who did
not write it. It does not decide whether a commit or a spec ANSWERS an ask; it decides whether the
evidence names the ask in the one place the rule accepts (a spec header's `closes` verb, a commit
subject). A commit whose subject names an ask and answers half of it signs CLOSED, and D4's REOPEN
is the repair. It never originates a hold: T5 signs one only when the row's own author wrote the
target. It assigns no severity. It writes no BACKLOG.md: the switch-over applies these records.

A BUILD RECORD, NOT A KIT FILE. It ships nowhere, so the design-named set below is a literal list
and the kit's modules are imported from this repo's own `tools/memory-tree/`.
"""
from __future__ import annotations

import collections
import difflib
import io
import os
import re
import subprocess
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))

#: This file's unit, read off its own recording name, so the records it names cannot disagree with
#: the file that wrote them. Empty when the name carries none, and `main` then refuses.
UNIT_ID = "".join(re.findall(r"^\d{4}-\d{2}-\d{2}-build-(.+-\d+)-signer\.py$",
                             os.path.basename(__file__)))

#: The spec revision whose section 4 these rules implement. A constant, not a read of the spec's
#: header: a rev bump that changes no rule must not red `--check` at the flip.
RULES_REV = "rev-6"

#: Who signed, and under what. Pinned by the spec's section 4 Outputs.
SIGNER = "(agent, 2026-09-14, delegated)"

#: U2 — the pairs design section 2.3 names as a row and a spec about DIFFERENT subjects (two spot
#: checked by the designer, two added by the critiques; carried into the migration by design
#: section 9 step 5). Literal on purpose: an input that can arrive empty would let a design-named
#: collision sign `unit` because its denial never loaded (AC3).
DESIGN_NAMED = frozenset((
    "TOOL-dFramedEntrypoint-1", "TOOL-aSealedCaravan-1", "TOOL-cBriefedPilot-23",
    "TOOL-aBoundedVerdict-22"))

#: T1 — excluded from the triage because the flip disposes it as superseded (design section 14),
#: and one file may carry only one disposition per target.
T1_EXCLUDED = {"TOOL-aWeighedCompass-3": "the flip disposes it as WONTDO, superseded by the flip "
                                         "unit (design section 14), and a second disposition here "
                                         "would put two for one target in one file"}

#: The planner unit whose worksheets are signed by default.
PLANNER_UNIT = "TOOL-dDerivedDocket-11"

TAILS = ("landing", "switch")
PROPOSALS = ("none", "CLOSED", "WONTDO", "BLOCKED", "DEFERRED")
UNIT_EVIDENCE = ("specced-in-place", "born-in-spec-commit")
SAME_ID_HEADER = "| Rule | Ask | Spec | Verdict | Evidence |"
TRIAGE_HEADER = "| Rule | Ask | Verdict | Field | Evidence | Severity |"
NL = "\n"


class Refusal(Exception):
    """A named refusal, exit 2. Never raised for a row the rules merely decline: that row is KEEP."""


# ----------------------------------------------------------------------------------- the seams
def run_git(root: str, *argv, data: bytes | None = None, check: bool = True) -> bytes:
    proc = subprocess.run(("git",) + argv, cwd=root, input=data, capture_output=True)
    if check and proc.returncode != 0:
        raise Refusal(f"signer: `git {' '.join(argv)}` failed: "
                      f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout if proc.returncode == 0 else b""


def resolve_root() -> str:
    """The repository this file sits in. The signing tree is its checkout, whatever the cwd."""
    return run_git(HERE, "rev-parse", "--show-toplevel").decode("utf-8").strip()


def read_text(path: str) -> str:
    """`newline=""`: a universal-newlines read rewrites a lone CR and silently splits a row."""
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read()


def render_path(root: str, path: str) -> str:
    """Repo-relative with forward slashes when inside the tree, absolute otherwise."""
    full = os.path.abspath(path)
    try:
        rel = os.path.relpath(full, root)
    except ValueError:                  # another drive on Windows: nothing is relative to it
        rel = ".."
    return (full if rel.startswith("..") else rel).replace("\\", "/")


def read_blob_sha(root: str, path: str) -> str:
    return run_git(root, "hash-object", "--", os.path.abspath(path)).decode("utf-8").strip()


def read_context(root: str) -> dict:
    """The kit's own readers, bound to this tree: grammar, spec index, conf. One load per run."""
    kit = os.path.join(root, "tools", "memory-tree")
    if kit not in sys.path:
        sys.path.insert(0, kit)
    import backlog                      # noqa: E402
    import gen_build_index as index     # noqa: E402
    import migrate_backlog as planner   # noqa: E402
    conf = index.load_conf(root)
    families = planner.derive_families(conf)
    grammar = backlog.build_grammar(families)
    spec_index = read_spec_index(root, conf, index)
    return {"backlog": backlog, "index": index, "planner": planner, "conf": conf,
            "families": families, "grammar": grammar, "specs": spec_index["specs"],
            "backlog_out": spec_index["backlog_out"], "memory_root": conf["MEMORY_ROOT"]}


def read_spec_index(root: str, conf: dict, index) -> dict:
    """Every spec H1 at the signing tree: path, status token and its header's `closes` ids."""
    out: dict = {}
    with redirect_stdout(io.StringIO()):
        try:
            builds = index.collect(root, conf, out)
        except index.Problem as exc:
            raise Refusal(f"signer: the build index refused this tree: {exc}") from None
    specs = {}
    for build in builds:
        for unit in build["units"]:
            specs[unit["id"]] = {"path": render_path(root, unit["path"]), "status": unit["status"],
                                 "closes": tuple(unit.get("closes") or ())}
    return {"specs": specs, "backlog_out": out}


# ----------------------------------------------------------------------------- the worksheets
def parse_worksheet(root: str, path: str, kind: str, columns: tuple, parse_row, ctx: dict) -> dict:
    """One planner worksheet -> {sha, rows, path, blob}. REFUSES rather than skipping anything.

    An empty worksheet, a row of the wrong shape, a duplicate id, a missing or disagreeing total:
    each names the worksheet and the line, because a skipped row signed nothing and the liveness
    line would still print a count that reads exactly like a clean signing (AC11).
    """
    shown = render_path(root, path)
    try:
        text = read_text(path)
    except OSError as exc:
        raise Refusal(f"signer: {shown}: the {kind} worksheet cannot be read: {exc}") from None
    lines = text.split(NL)
    if lines and lines[-1] == "":
        lines.pop()
    if not lines:
        raise Refusal(f"signer: {shown}:1: the {kind} worksheet is empty")
    prov = next((n for n, ln in enumerate(lines[:3], 1)
                 if ln.startswith(f"# {kind} worksheet · computed at ")), 0)
    if not prov:
        raise Refusal(f"signer: {shown}:2: no `# {kind} worksheet · computed at <sha>` line in the "
                      f"first three lines, so the tree its rows were read at is unknown")
    found = re.match(r"^# \S+ worksheet · computed at ([0-9a-f]{40})\b", lines[prov - 1])
    if not found:
        raise Refusal(f"signer: {shown}:{prov}: the provenance line names no 40-hex sha")
    sha = found.group(1)
    head_at = prov + 1
    if head_at > len(lines) or lines[head_at - 1] != "\t".join(columns):
        raise Refusal(f"signer: {shown}:{head_at}: the header row is not the planner's "
                      f"`{' '.join(columns)}`, so no column can be located")
    rows, seen = [], {}
    total_at = 0
    for num in range(head_at + 1, len(lines) + 1):
        line = lines[num - 1]
        if line.startswith("examined\t"):
            total_at = num
            break
        cells = line.split("\t")
        if len(cells) != len(columns):
            raise Refusal(f"signer: {shown}:{num}: {len(cells)} cell(s) where the header has "
                          f"{len(columns)}: {line[:80]!r}")
        row = dict(zip(columns, cells))
        why = parse_row(row, ctx)
        if why:
            raise Refusal(f"signer: {shown}:{num}: {why}: {line[:80]!r}")
        if row["id"] in seen:
            raise Refusal(f"signer: {shown}:{num}: {row['id']} is listed twice (first at line "
                          f"{seen[row['id']]}), and one target takes one signature")
        seen[row["id"]] = num
        rows.append(row)
    if not total_at:
        raise Refusal(f"signer: {shown}:{len(lines)}: no `examined <n>` total, so a truncated "
                      f"worksheet cannot be told from a whole one")
    if total_at != len(lines):
        raise Refusal(f"signer: {shown}:{total_at + 1}: a line follows the `examined` total")
    declared = lines[total_at - 1].split("\t", 1)[1]
    if declared != str(len(rows)):
        raise Refusal(f"signer: {shown}:{total_at}: the total says {declared} and {len(rows)} "
                      f"row(s) were read")
    if not rows:
        raise Refusal(f"signer: {shown}:{total_at}: the {kind} worksheet holds no row, and a "
                      f"signing over nothing looks exactly like a clean one")
    return {"sha": sha, "rows": rows, "path": shown, "blob": read_blob_sha(root, path)}


def parse_same_id_row(row: dict, ctx: dict) -> str:
    """"" when the row is well formed, else why not."""
    b = ctx["backlog"]
    if not b.check_id(row["id"], ctx["grammar"]):
        return f"`{row['id']}` is not a well-formed id"
    if not row["spec"]:
        return "the spec cell is empty"
    if row["legacy"] not in b.LEGACY_TOKENS:
        return f"`{row['legacy']}` is not a legacy token"
    if row["evidence"] not in ctx["planner"].EVIDENCE_CLASSES:
        return f"`{row['evidence']}` is not an evidence class"
    if row["sha"] != "-" and not b.SHA_RE.match(row["sha"]):
        return f"`{row['sha']}` is neither `-` nor a sha"
    if row["low_overlap"] not in ("yes", "no"):
        return f"low_overlap `{row['low_overlap']}` is neither yes nor no"
    if not re.fullmatch(r"\d+\.\d+", row["overlap"]):
        return f"overlap `{row['overlap']}` is not a decimal"
    return ""


def parse_triage_row(row: dict, ctx: dict) -> str:
    b = ctx["backlog"]
    if not b.check_id(row["id"], ctx["grammar"]):
        return f"`{row['id']}` is not a well-formed id"
    if not re.fullmatch(r"[^:\s]+:[1-9][0-9]*", row["source"]):
        return f"source `{row['source']}` is not <path>:<line>"
    if row["legacy"] not in b.LEGACY_TOKENS:
        return f"`{row['legacy']}` is not a legacy token"
    if row["derived"] != "OPEN":
        return f"it derives `{row['derived']}`, and the triage population is asks deriving OPEN"
    if row["proposal"] not in PROPOSALS:
        return f"proposal `{row['proposal']}` is not one of {' '.join(PROPOSALS)}"
    ev = row["evidence"]
    if ev != "-" and not b.check_id(ev, ctx["grammar"]) and not b.SHA_RE.match(ev):
        return f"evidence `{ev}` is neither `-`, an id nor a sha"
    if not row["basis"]:
        return "the basis cell is empty"
    if row["dead_pointer"] not in ("yes", "no"):
        return f"dead_pointer `{row['dead_pointer']}` is neither yes nor no"
    return ""


# ------------------------------------------------------------------------ the evidence readers
def read_commit_messages(root: str, shas) -> dict:
    """{sha: message} for every name that resolves to a COMMIT, in one `git cat-file --batch`."""
    shas = sorted(set(shas))
    if not shas:
        return {}
    buf = run_git(root, "cat-file", "--batch", data=("\n".join(shas) + "\n").encode("utf-8"))
    out, pos = {}, 0
    for sha in shas:
        end = buf.index(b"\n", pos)
        head = buf[pos:end].decode("utf-8", "replace").split()
        pos = end + 1
        if len(head) != 3:
            continue
        size = int(head[2])
        body = buf[pos:pos + size]
        pos += size + 1
        if head[1] == "commit":
            text = body.decode("utf-8", "replace")
            out[sha] = text.split("\n\n", 1)[1] if "\n\n" in text else ""
    return out


def read_shard_lines(root: str, sha: str, paths, cache: dict) -> None:
    """Each cited file's lines AT THE WORKSHEET'S SHA, one `git show` per file, into `cache`."""
    for path in sorted(set(paths)):
        if (sha, path) in cache:
            continue
        blob = run_git(root, "show", f"{sha}:{path}", check=False)
        cache[(sha, path)] = blob.decode("utf-8", "replace").split(NL) if blob else None


def extract_row_text(lines, num: int) -> str | None:
    """The logical legacy row starting at line `num`, with indented continuations joined the way
    the planner's permissive parser joins them. None when that line starts no list row."""
    if lines is None or num > len(lines):
        return None
    line = lines[num - 1].rstrip("\r")
    if not line.startswith("- "):
        return None
    for more in lines[num:]:
        more = more.rstrip("\r")
        if more[:1] in (" ", "\t") and more.strip():
            line += " " + more.strip()
            continue
        break
    return line


def build_hold_check(root: str, ctx: dict):
    """Is a hold target live at the signing tree? -> True, False, or None (no such target).

    One rule per layout. Under `builds` it is backlog.py's own `check_hold_live` over the fold the
    build index derived. Under `shards` asks live in the legacy shards, so an ask is live when its
    surviving copy's token is not terminal. In both, an ask wins a tie with a spec H1 and a spec is
    live when its status is not terminal — `_check_live`'s rule, not a second one.
    """
    b, planner = ctx["backlog"], ctx["planner"]
    specs = ctx["specs"]
    mode = b.read_conf(ctx["conf"]).mode
    if mode == "builds":
        corpus, fold = ctx["backlog_out"].get("corpus"), ctx["backlog_out"].get("fold")
        return lambda target: b.check_hold_live(corpus, fold, target)
    live, arch, _ = planner.resolve_row_docs(root, ctx["conf"], ctx["families"])
    copies, _ = planner.parse_legacy_rows(root, live + arch, set(live), ctx["grammar"])
    by_id = collections.defaultdict(list)
    for copy in copies:
        by_id[copy.id].append(copy)
    tokens = {i: planner.resolve_copy(cs)[0].token for i, cs in by_id.items()}

    def check_live(target):
        if target in tokens:
            return tokens[target] not in b.TERMINAL
        if target in specs:
            return specs[target]["status"] not in b.TERMINAL
        return None
    return check_live


def measure_level_words(root: str, sha: str, ctx: dict, cache: dict) -> tuple:
    """(rows, rows carrying an upper-case level word) over the live shards AT `sha`. Decides
    nothing: every triage row's severity is `unlabelled` whatever this returns (spec F2)."""
    b = ctx["backlog"]
    paths = [f"{ctx['memory_root']}/backlog/{fam}.md" for fam in ctx["families"]]
    read_shard_lines(root, sha, paths, cache)
    level = re.compile(r"\b(?:" + "|".join(b.SEVERITIES) + r")\b")
    rows = hits = 0
    for path in paths:
        lines = cache.get((sha, path))
        if lines is None:
            continue
        for num in range(1, len(lines) + 1):
            text = extract_row_text(lines, num)
            if text is None or b.read_legacy_row(text, ctx["grammar"]).id is None:
                continue
            rows += 1
            if level.search(text):
                hits += 1
    return rows, hits


# ----------------------------------------------------------------------------------- the rules
def derive_same_id_verdict(root: str, row: dict, ctx: dict) -> tuple:
    """-> (rule, verdict, evidence). U2, U1, U3, U4 in that order; the first a pair FAILS decides."""
    ask, ev, sha = row["id"], row["evidence"], row["sha"][:8]
    if ask in DESIGN_NAMED:
        return ("U2", "not-unit", "design section 2.3 names this row and its spec as different "
                                  f"subjects; evidence {ev}")
    if ev not in UNIT_EVIDENCE:
        return ("U1", "not-unit", f"evidence {ev}: not specced in place, not born in its spec's "
                                  f"commit")
    if row["low_overlap"] == "yes":
        return ("U3", "not-unit", f"{ev} {sha}, but the planner flags the pair low-overlap at "
                                  f"{row['overlap']}")
    full = os.path.join(root, row["spec"])
    if not os.path.isfile(full):
        return ("U4", "not-unit", f"{ev} {sha}, but the named spec file does not exist here")
    h1 = next((ln for ln in read_text(full).split(NL) if ln.startswith("# ")), "")
    if not ctx["planner"].check_names_id(h1, ask):
        return ("U4", "not-unit", f"{ev} {sha}, but the named spec's H1 does not carry the ask id")
    return ("all", "unit", f"{ev} {sha} · overlap {row['overlap']} · the spec's H1 carries the id")


def derive_triage_verdict(row: dict, ctx: dict, sheet_sha: str, commits: dict, cache: dict,
                          check_hold) -> tuple:
    """-> (rule, verdict, field, evidence). T1 to T6 in order; the first that matches decides.

    A verdict reads its OWN row and the signing tree, never a population statistic, so re-signing a
    worksheet that gained a row changes that one row and the counts (AC10).
    """
    b, planner, grammar, specs = ctx["backlog"], ctx["planner"], ctx["grammar"], ctx["specs"]
    ask, prop, ev = row["id"], row["proposal"], row["evidence"]
    if ask in T1_EXCLUDED:
        return ("T1", "excluded", "-", T1_EXCLUDED[ask])
    refused = []
    if prop == "CLOSED" and ev == "-":
        refused.append(("T2", "the proposal cites no spec and no sha to re-read"))
    if prop == "CLOSED" and b.check_id(ev, grammar):
        spec = specs.get(ev)
        if ev == ask:
            refused.append(("T2", "the proposal names the ask's own same-id spec, which is D2's "
                                  "question, signed in the same-id record"))
        elif spec is None:
            refused.append(("T2", f"{ev} is no spec H1 at the signing tree"))
        elif spec["status"] != "CLOSED":
            refused.append(("T2", f"spec {ev} reads {spec['status']}"))
        elif ask not in spec["closes"]:
            refused.append(("T2", f"spec {ev} reads CLOSED, but its header carries no `closes` "
                                  f"verb naming the ask; a mention in its body is not a closure"))
        else:
            return ("T2", "CLOSED", ev, f"spec {ev} reads CLOSED and its header closes the ask")
    if prop == "CLOSED" and b.SHA_RE.match(ev):
        message = commits.get(ev)
        subject = message.split(NL, 1)[0] if message is not None else ""
        if message is None:
            refused.append(("T3", f"{ev[:8]} resolves to no commit here"))
        elif ask in specs:
            refused.append(("T3", f"the ask is a spec H1, so commit {ev[:8]} is evidence about "
                                  f"that spec, which is D2's question, signed in the same-id "
                                  f"record"))
        elif not planner.check_names_id(subject, ask):
            refused.append(("T3", f"commit {ev[:8]} names the ask in its body only, which is a "
                                  f"citation"))
        else:
            return ("T3", "CLOSED", ev, f"commit {ev[:8]} resolves and its subject names the ask")
    path, _, num = row["source"].rpartition(":")
    loc = f"{path}:{num} at {sheet_sha[:8]}"
    text = extract_row_text(cache.get((sheet_sha, path)), int(num))
    own = b.read_legacy_row(text, grammar) if text is not None else None
    unreadable = ""
    if own is None or own.id != ask:
        unreadable = f"{loc} holds no row for this ask"
    elif own.withdrawn or own.status == "WONTDO":
        word = "WITHDRAWN" if own.withdrawn else "WONTDO"
        return ("T4", "WONTDO", "-", f"{loc} reads {word} in the row's own status slot")
    if prop == "WONTDO":
        refused.append(("T4", unreadable or f"{loc} reads {own.status}, not a withdrawal; prose "
                                            f"is never read as one"))
    if prop in ("BLOCKED", "DEFERRED"):
        why = ""
        if unreadable:
            why = unreadable
        elif not b.check_id(ev, grammar):
            why = "the proposal carries no hold target"
        elif not planner.check_names_id(text, ev):
            why = f"the row at {loc} does not name {ev}"
        else:
            live = check_hold(ev)
            if live is None:
                why = f"{ev} is neither a filed ask nor a spec H1 at the signing tree"
            elif not live:
                why = f"{ev} is not live at the signing tree"
            elif prop == "DEFERRED" and own.status != "DEFERRED":
                why = (f"DEFERRED needs the row's own token to read DEFERRED, and it reads "
                       f"{own.status}")
        if not why:
            return ("T5", prop, ev, f"the row at {loc} names {ev}, live at the signing tree")
        refused.append(("T5", why))
    if refused:
        rule, why = refused[0]
        reason = f"{rule} refused: {why}"
    else:
        reason = "no evidence for T2 to T5"
        if unreadable:
            reason += f"; {unreadable}"
    if row["dead_pointer"] == "yes":
        reason += "; the pointer is dead, which is not evidence"
    return ("T6", "KEEP", "-", reason)


# --------------------------------------------------------------------------------- the records
def build_signing(root: str, same_path: str, triage_path: str) -> dict:
    """Both worksheets, every verdict, and the counts. Reads; writes nothing."""
    ctx = read_context(root)
    planner = ctx["planner"]
    same = parse_worksheet(root, same_path, "same-id", planner.SAME_ID_COLUMNS, parse_same_id_row,
                           ctx)
    tri = parse_worksheet(root, triage_path, "triage", planner.TRIAGE_COLUMNS, parse_triage_row,
                          ctx)
    order = planner.build_id_sort_key
    same_rows = []
    for row in sorted(same["rows"], key=lambda r: order(r["id"])):
        rule, verdict, why = derive_same_id_verdict(root, row, ctx)
        same_rows.append((rule, row["id"], row["spec"], verdict, why))
    cache: dict = {}
    read_shard_lines(root, tri["sha"], [r["source"].rpartition(":")[0] for r in tri["rows"]], cache)
    commits = read_commit_messages(root, [r["evidence"] for r in tri["rows"]
                                          if r["proposal"] == "CLOSED"
                                          and ctx["backlog"].SHA_RE.match(r["evidence"])])
    holds: list = []

    def check_hold(target):
        if not holds:
            holds.append(build_hold_check(root, ctx))
        return holds[0](target)
    tri_rows, excluded = [], []
    for row in sorted(tri["rows"], key=lambda r: order(r["id"])):
        rule, verdict, field, why = derive_triage_verdict(row, ctx, tri["sha"], commits, cache,
                                                          check_hold)
        if verdict == "excluded":
            excluded.append((row["id"], why))
            continue
        tri_rows.append((rule, row["id"], verdict, field, why, ctx["backlog"].UNLABELLED))
    census = measure_level_words(root, tri["sha"], ctx, cache)
    return {"same": same, "triage": tri, "same_rows": same_rows, "tri_rows": tri_rows,
            "excluded": excluded, "census": census, "ctx": ctx}


def render_liveness(s: dict) -> str:
    sv = collections.Counter(r[3] for r in s["same_rows"])
    sr = collections.Counter(r[0] for r in s["same_rows"] if r[3] == "not-unit")
    tv = collections.Counter(r[2] for r in s["tri_rows"])
    rows, hits = s["census"]
    return (f"signer — same-id {len(s['same_rows'])} pair(s): unit {sv['unit']}, not-unit "
            f"{sv['not-unit']} (U1 {sr['U1']}, U2 {sr['U2']}, U3 {sr['U3']}, U4 {sr['U4']}) · "
            f"triage {len(s['tri_rows']) + len(s['excluded'])} ask(s): "
            + ", ".join(f"{v} {tv[v]}" for v in ("KEEP", "CLOSED", "WONTDO", "BLOCKED",
                                                  "DEFERRED"))
            + f", excluded {len(s['excluded'])} · level words {hits} of {rows} legacy row(s) at "
              f"{s['triage']['sha'][:8]}")


def resolve_sibling(root: str, folder: str, suffix: str) -> str:
    """The one file in this build's `folder` whose name ends `suffix`, repo-relative. Refuses on
    none or several, because a header citing the wrong authority is worse than no record."""
    base = os.path.join(os.path.dirname(HERE), folder)
    hits = sorted(p for p in os.listdir(base) if p.endswith(suffix))
    if len(hits) != 1:
        raise Refusal(f"signer: {len(hits)} file(s) in {render_path(root, base)} end `{suffix}`, "
                      f"and the record header cites exactly one")
    return render_path(root, os.path.join(base, hits[0]))


def render_header(root: str, s: dict, title: str) -> list:
    spec_path = resolve_sibling(root, "spec", f"-spec-{UNIT_ID}.md")
    mandate_path = resolve_sibling(root, "prompts", "-owner-mandate.md")
    me = render_path(root, os.path.abspath(__file__))
    out = [f"**Serves:** journal {UNIT_ID}", "", f"# {title} — {UNIT_ID}", "",
           f"Signed under delegation, by rule and not by hand. Signer: {SIGNER}. Authority: the "
           f"owner mandate record's \"The single owner turn\" section, `{mandate_path}`. Rule set: "
           f"section 4 of `{spec_path}` at {RULES_REV}.", "",
           f"Written by `{me}`. Re-derive it with that file's `--check`, naming the two worksheets "
           f"below with `--worksheets` and passing `--tail` when this record's name carries one; "
           f"it exits 0 only when every line re-derives byte for byte. No byte here is authored.",
           ""]
    for kind in ("same", "triage"):
        w = s[kind]
        name = "same-id" if kind == "same" else "triage"
        out.append(f"- the {name} worksheet: `{w['path']}` · blob `{w['blob']}` · computed at "
                   f"`{w['sha']}`")
    out.append(f"- the counts: {render_liveness(s)[len('signer — '):]}")
    out.append("")
    return out


def render_same_id_record(root: str, s: dict) -> str:
    out = render_header(root, s, "The signed same-id table")
    out += ["Evaluated U2, U1, U3, U4; the first rule a pair fails decides `not-unit` and is named. "
            "A `unit` row passed all four. `unit` makes the spec's terminal status the ask's, so a "
            "wrong `unit` closes an ask nobody answered, and every doubt signs `not-unit`, which "
            "leaves the ask live.", "", SAME_ID_HEADER, "|---|---|---|---|---|"]
    for rule, ask, spec, verdict, why in s["same_rows"]:
        out.append(f"| {rule} | {ask} | {spec} | {verdict} | {why} |")
    out.append("")
    return NL.join(out)


def render_triage_record(root: str, s: dict) -> str:
    rows, hits = s["census"]
    out = render_header(root, s, "The signed triage table")
    out += ["Evaluated T1 to T6; the first rule that matches decides, and a row no rule decides is "
            "KEEP with the reason naming the rule it came closest to. CLOSED is signed only from a "
            "spec header's `closes` verb or a commit SUBJECT, re-read here; a commit that names an "
            "ask only in its body is a citation. A commit whose subject names an ask and answers "
            "half of it would sign a wrong CLOSED, which D4's REOPEN repairs.", "",
            f"Severity: every row reads `unlabelled`. Census at the worksheet's sha: {hits} of "
            f"{rows} legacy row(s) carry an upper-case level word, so no mechanical rule could label "
            f"one without inventing it (spec F2; D7 is forward-only).", "",
            "Where these land: the switch-over writes each disposition into this build's own "
            "BACKLOG.md, the signer's file, and applies the table exactly.", "",
            TRIAGE_HEADER, "|---|---|---|---|---|---|"]
    for rule, ask, verdict, field, why, sev in s["tri_rows"]:
        out.append(f"| {rule} | {ask} | {verdict} | {field} | {why} | {sev} |")
    out += ["", "## Exclusions", ""]
    for ask, why in s["excluded"]:
        out.append(f"- T1 excludes `{ask}`: {why}.")
    missing = sorted(set(T1_EXCLUDED) - {a for a, _ in s["excluded"]})
    for ask in missing:
        out.append(f"- T1 names `{ask}`, which this worksheet does not list, so nothing is "
                   f"excluded for it.")
    out.append("")
    return NL.join(out)


def resolve_record_path(root: str, kind: str, tail: str, create: bool) -> str:
    """The tracked record for (kind, tail), found by name; a new one is dated by HEAD's commit day,
    never the clock, so two runs over one tree name the same file."""
    suffix = f"-build-{UNIT_ID}-signed-{kind}" + (f"-{tail}" if tail else "") + ".md"
    hits = sorted(p for p in os.listdir(HERE)
                  if p.endswith(suffix) and re.match(r"^\d{4}-\d{2}-\d{2}" + re.escape(suffix)
                                                     + r"$", p))
    if len(hits) > 1:
        raise Refusal(f"signer: {len(hits)} records end `{suffix}`: {' '.join(hits)}")
    if hits:
        return os.path.join(HERE, hits[0])
    if not create:
        raise Refusal(f"signer: no tracked record ends `{suffix}` in "
                      f"{render_path(root, HERE)}, so there is nothing to check against")
    day = run_git(root, "show", "-s", "--format=%cd", "--date=format:%Y-%m-%d",
                  "HEAD").decode("utf-8").strip()
    return os.path.join(HERE, day + suffix)


def extract_table_rows(text: str) -> dict:
    """{ask: (rule, verdict)} off one record's table, located by its pinned header row."""
    out, started = {}, False
    for line in text.split(NL):
        if line in (SAME_ID_HEADER, TRIAGE_HEADER):
            started = line
            continue
        if not started or line.startswith("|---"):
            continue
        if not line.startswith("| "):
            started = False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        verdict = cells[3] if started == SAME_ID_HEADER else cells[2]
        out[cells[1]] = (cells[0], verdict)
    return out


def check_records(root: str, texts: dict) -> int:
    """Diff each re-derived record against its tracked copy; name every row that moved."""
    bad = 0
    for path, text in texts.items():
        shown = render_path(root, path)
        tracked = read_text(path)
        if tracked == text:
            continue
        bad += 1
        for line in difflib.unified_diff(tracked.split(NL), text.split(NL), f"tracked {shown}",
                                         "re-derived", n=0, lineterm=""):
            print(line)
        old, new = extract_table_rows(tracked), extract_table_rows(text)
        for ask in sorted(set(old) | set(new)):
            if old.get(ask) == new.get(ask):
                continue
            was = " ".join(old[ask]) if ask in old else "absent"
            now = " ".join(new[ask]) if ask in new else "absent"
            print(f"signer: {shown}: {ask} — tracked {was}, re-derived {now}")
    return bad


def write_records(texts: dict) -> None:
    for path, text in texts.items():
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)


def main(argv: list) -> int:
    args = argv[1:]
    check = "--check" in args
    args = [a for a in args if a != "--check"]
    tail, sheets = "", []
    while args:
        head = args.pop(0)
        if head == "--tail" and args:
            tail = args.pop(0)
            if tail not in TAILS:
                raise Refusal(f"signer: --tail takes one of {' '.join(TAILS)}, not `{tail}`")
        elif head == "--worksheets" and len(args) >= 2:
            sheets = [os.path.abspath(args.pop(0)), os.path.abspath(args.pop(0))]
        else:
            raise Refusal(f"signer: `{head}` is not an option; see this file's docstring")
    if not UNIT_ID:
        raise Refusal("signer: this file's name carries no unit id, so its records cannot be named")
    root = resolve_root()
    if not sheets:
        for kind in ("same-id", "triage"):
            hits = sorted(p for p in os.listdir(HERE)
                          if p.endswith(f"-build-{PLANNER_UNIT}-{kind}.tsv"))
            if len(hits) != 1:
                raise Refusal(f"signer: {len(hits)} {kind} worksheet(s) filed by {PLANNER_UNIT} "
                              f"in {render_path(root, HERE)}; name the pair with --worksheets")
            sheets.append(os.path.join(HERE, hits[0]))
    s = build_signing(root, sheets[0], sheets[1])
    texts = {resolve_record_path(root, "same-id", tail, not check): render_same_id_record(root, s),
             resolve_record_path(root, "triage", tail, not check): render_triage_record(root, s)}
    print(render_liveness(s))
    if check:
        bad = check_records(root, texts)
        print(f"signer: --check — {len(texts) - bad} of {len(texts)} record(s) re-derive "
              f"byte-identical")
        return 1 if bad else 0
    write_records(texts)
    for path in texts:
        print(f"signer: wrote {render_path(root, path)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Refusal as exc:
        print(exc, file=sys.stderr)
        sys.exit(2)

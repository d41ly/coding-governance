#!/usr/bin/env python3
"""gotchas.py — the bug-class catalogue's index and its per-diff checklist (memory-tree kit 1.5).

    python <prefix>/memory-tree/gotchas.py --check                 # checks 17-19 + INDEX freshness
    python <prefix>/memory-tree/gotchas.py --write                 # render INDEX.md
    python <prefix>/memory-tree/gotchas.py --report                # the counts the budget is measured on
    python <prefix>/memory-tree/gotchas.py --for-diff <base>..<head>   # STDOUT IS THE CHECKLIST
    python <prefix>/memory-tree/gotchas.py --for-paths [--base <rev>] <path>...   # the same checklist, no diff yet
    python <prefix>/memory-tree/gotchas.py --declares < record.md   # prints `declares: yes|no`; rc 0 / 1, 2 unreadable
    python <prefix>/memory-tree/gotchas.py --selftest

`--for-diff`'s STDOUT IS THE CHECKLIST. That is the point: a reviewer is handed the classes their
diff can actually hit instead of being pointed at a catalogue and trusted to remember which entries
apply. A checklist nobody can finish is not a checklist.

ANCHORS ARE DERIVED, NOT DECLARED. A record's anchors are the backtick-quoted path-like tokens in its
body. An authored `anchors:` list is a second copy of what the body already says, and this catalogue
has an entry for exactly that. The trade is stated rather than discovered: derivation is
recall-biased, so `--for-diff` OVER-selects, and a record naming no path at all matches nothing and
is REPORTED as unanchored rather than silently never firing.

AN INVARIANT IS THE OTHER HALF OF A REVIEWER'S BRIEF (TOOL-aGraftedHelix-3). A `kind: invariant` record
names a ruling a reviewer keeps mistaking for a bug, by its `decision:` id, in five sections. It is
selected by the same anchors, and printed AFTER the checklist as the by-design block
(`# by design — <n> invariant(s) this selection touches`, the head printed on every non-empty
selection, `0` included). The review harness cuts the block back out of `checklist` and hands it to
every lens and skeptic as `byDesign`.

THE BLOCK IS READ AT THE SUBJECT'S BASE (TOOL-aGraftedHelix-29). Read from the tree under review, a
range that added or edited an invariant handed its own review an instruction to refute whatever that
ruling covers. `--for-diff` reads the block from the records as they stood at the commit its range
diffs from, and `--for-paths --base <rev>` at that revision. An invariant the subject adds, edits or
takes out is never by design there: it prints as a `NEW/CHANGED invariant` checklist item, because
an item can only widen a review. `--for-paths` with no base reads the working tree and says so on a
header line. Classes keep reading the working tree for the same reason.

THREE UPSTREAM HARVEST DEFECTS ARE CARRIED, each with its own arm in --selftest — TWO as behaviour
this implementation shares, ONE as a difference:
  1. SHARED   — a token containing `::` inside backticks harvests to nothing.
  2. NOT HERE — upstream required a non-empty tail after the slash, so a directory anchor written
                `<prefix>/memory-tree/` harvested to nothing and its record was silently unanchored.
                Here the tail may be empty, the directory token IS harvested, and it selects
                everything beneath it. The arm pins the DIFFERENCE, so a future tightening of the
                pattern reintroduces the upstream defect loudly instead of quietly.
  3. SHARED   — an anchor's BASENAME matches tree-wide, however much path precedes it. Kept: it is
                what makes short-form anchors usable at all.
Documented behaviour that no test pins is indistinguishable from a bug nobody has noticed. A future
change that "fixes" one of these must fail loudly and be made deliberately.
"""
from __future__ import annotations

import os
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
HYGIENE = HERE / "check-memory-hygiene.sh"
BEGIN, END = "<!-- BEGIN GENERATED -->", "<!-- END GENERATED -->"
# The front-matter pattern is `tree_lib.FM_RE`, imported below with the conf parser
# (TOOL-aGraftedHelix-9): `row_grammar.py` reads the same block for check 27.
# A path-ish token inside backticks: at least one `/`, or a known source extension.
ANCHOR_RE = re.compile(r"`([^`\s]+(?:/[^`\s]*|\.(?:md|py|sh|js|json|ts|toml|yml|yaml|conf|txt)))`")
# A record DECLARES its resolution by naming a gate, or by saying in as many words that it has none.
# Both are acceptable; silence is not, because "no gate named" and "gate not yet written" are
# indistinguishable from outside and the second one quietly never happens.
#
# THE ONE COPY OF THIS PREDICATE. Upstream shipped it typed twice — this alternation and a hand-copied
# grep in the shell gate — and the two did not agree: the shell grepped the WHOLE file while the
# module searched only the post-front-matter body, so a `description` carrying the word "gated"
# satisfied one and not the other. Every consumer calls `declares()`; nobody re-types the alternation.
DECLARES_RE = re.compile(r"gated by|gated in|gated at|documented[ -]check|no machine gate", re.I)
KINDS = ("class", "note", "superseded", "invariant")
# TOOL-aGraftedHelix-3 — an INVARIANT is a ruling a reviewer keeps mistaking for a bug: intended
# behaviour, cited by its decision id, selected by the same anchors a class is. Its five body sections
# (I5), each graded present and non-empty by check 18, and the head of the by-design block `--for-diff`
# and `--for-paths` print after the checklist (I4), which the review harness cuts back out of
# `checklist` and hands its lenses as `byDesign`. One spelling of the head: the harness matches it.
INVARIANT_SECTIONS = ("Looks wrong", "Actually", "Do", "Do not", "Guarded by")
BY_DESIGN_HEAD = "# by design — {n} invariant(s) this selection touches"
# TOOL-aGraftedHelix-29 — where the block was read from, said on every checklist. Each opens `# `, so
# the review harness reads it as preamble and the build harness's union as a head line; none opens
# `# by design —`, so no pattern takes it for the block's head.
INVARIANTS_AT_BASE = ("# invariants are read at {sha}; {n} that this subject adds, edits or takes out "
                      "are listed as items, never by design")
INVARIANTS_UNPINNED = ("# invariants are read from the working tree; with no --base, a record this "
                       "subject adds or edits can stand as by design")
INVARIANTS_UNPARSED = "# {n} record(s) at {sha} did not parse, so none of them is by design: {paths}"
MOVED_INVARIANT_ITEM = "- [ ] NEW/CHANGED invariant {name} — verify the ruling before treating it as by design"
GUARD_TOKEN_RE = re.compile(r"`([^`]+)`")


class Problem(Exception):
    """A named, user-facing failure. Never a traceback."""


def run(*argv, cwd=None):
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True, encoding="utf-8", check=True).stdout


def read(path) -> str:
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8", "replace").replace("\r\n", "\n")


def write(path, text):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(text.encode("utf-8"))


# TOOL-aWeldedTribunal-5 -- ONE `.memory-tree.conf` parser for the whole kit. Six readers held an
# identical naive body while the shell gate SOURCES the same file, so a legal spelling bash accepts
# and the python half mis-read REMOVED coverage with the gate still green. TOOL-aRepatriatedFork-9
# moved it into `tree_lib.py`, so this engine no longer needs a sibling ENGINE to import.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tree_lib import FM_RE, kit_rel, parse_conf  # noqa: E402  the kit's ONE conf parser

def load_conf(root: str) -> dict:
    conf = {"MEMORY_ROOT": "memory", "UNIVERSAL_BUDGET": "", "LEG_MANIFEST": ""}
    p = os.path.join(root, ".memory-tree.conf")
    if os.path.isfile(p):
        parse_conf(read(p), conf)
    return conf


def append_only_re(root: str) -> re.Pattern:
    """The append-only classification, ASKED of the script that owns it — never retyped here.

    The sibling raises ITS OWN `Problem` class, which this module's `except Problem` cannot catch —
    two classes with one name are two classes. Every failure crossing this boundary is re-raised as
    ours, so a hygiene gate never emits a traceback.
    """
    import importlib.util

    src = HERE / "corpus_ids.py"
    if not src.is_file():
        raise Problem(f"gotchas: {src} is missing — it owns the append-only classification "
                      f"checks 17-19 read")
    try:
        spec = importlib.util.spec_from_file_location("corpus_ids", src)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return re.compile(mod.ask_shell("--print-append-only-ere", root).strip() or r"(?!)")
    except Problem:
        raise
    except Exception as exc:  # noqa: BLE001 — including the sibling's own Problem, a different class
        raise Problem(f"gotchas: could not ask corpus_ids for the append-only classification: "
                      f"{type(exc).__name__}: {exc}") from None


def load_defined_ids(root: str, grammar_dir=None):
    """`(ids, None)`: every id this corpus DEFINES, from `corpus_ids`' one walk — or `(None, why)` when
    the id grammar's kit is absent, which check 18 ANNOUNCES rather than reds (TOOL-aGraftedHelix-3).

    The set `corpus_ids.py --print-defined-ids` prints, reached in-process the way `append_only_re`
    reaches its sibling, so there is still ONE id grammar: a decision recorded as a spec H1 or a backlog
    row resolves exactly as a decision-log row does. `grammar_dir` exists for the self-test's
    absent-kit arm and points the loaded module at a directory holding no grammar.
    """
    import importlib.util

    src = HERE / "corpus_ids.py"
    if not src.is_file():
        raise Problem(f"gotchas: {src} is missing — it owns the defined-id set check 18 resolves "
                      f"an invariant's decision against")
    try:
        spec = importlib.util.spec_from_file_location("corpus_ids", src)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if grammar_dir is not None:
            mod.GRAMMAR_DIR = pathlib.Path(grammar_dir)
        if not (mod.GRAMMAR_DIR / "extract.py").is_file():
            return None, "the id grammar lives in the memory-recall kit, which is not installed beside this one"
        return set(mod.walk(root, mod.load_conf(root))["defs"]), None
    except Exception as exc:  # noqa: BLE001 — the sibling's own Problem is a different class
        raise Problem(f"gotchas: could not ask corpus_ids for the defined-id set: "
                      f"{type(exc).__name__}: {exc}") from None


def load_leg_names(root: str, conf: dict):
    """The leg names the manifest `LEG_MANIFEST` declares, or None when the key is blank.

    Blank is legal and ANNOUNCED by the caller: a guard token that is no tracked path then cannot be
    judged, and saying so beats both a false red and a silent pass. A SET key naming a file that does
    not read as a list of `{name: ...}` rows is a named failure, never a traceback.
    """
    import json

    rel = conf.get("LEG_MANIFEST", "").strip()
    if not rel:
        return None
    try:
        rows = json.loads(read(os.path.join(root, rel)))
        if not isinstance(rows, list):
            raise ValueError("the top level is not a list of leg rows")
        return {r["name"] for r in rows if isinstance(r, dict) and isinstance(r.get("name"), str)}
    except (OSError, ValueError) as exc:
        raise Problem(f"gotchas: LEG_MANIFEST names {rel}, which cannot be read as a leg manifest "
                      f"({type(exc).__name__}: {exc}) — fix the path, or blank the key so a leg-name "
                      f"guard is announced unresolved instead") from None


# ------------------------------------------------------------------------------------------ records
def parse_sections(body: str) -> dict:
    """`## <heading>` -> the lines of that section's FIRST paragraph, stripped, blank lines before it
    skipped. A heading inside a fenced block is read as a heading — ponytail: no record needs one."""
    out, cur, para = {}, None, None
    for line in body.split("\n"):
        if line.startswith("## "):
            cur = line[3:].strip()
            out[cur] = para = []
            continue
        if cur is None:
            continue
        s = line.strip()
        if s:
            if para is not None:
                para.append(s)
        elif para:
            para = None          # the first paragraph ended; the rest of the section is not read
    return out
def parse_front_matter(path: str, text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        raise Problem(f"{path}: no front matter — a record opens with a '---' block at line 1")
    fm = {}
    for i, line in enumerate(m.group(1).split("\n"), 2):
        if not line.strip():
            continue
        if line[:1].isspace():
            # A key indented under a parent (`metadata:` / `nested:`) is SILENTLY DROPPED by every
            # simple parser, and a dropped `kind` or `universal` changes what the checklist emits.
            raise Problem(f"{path}:{i}: front-matter key is indented — keys live at COLUMN 0, and an "
                          f"indented key is dropped without a word")
        if ":" not in line:
            raise Problem(f"{path}:{i}: front-matter line is not 'key: value'")
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    for key in ("name", "description"):
        if key not in fm:
            raise Problem(f"{path}: front matter is missing required key '{key}'")
    kind = fm.get("kind", "class")
    if kind not in KINDS:
        raise Problem(f"{path}: kind '{kind}' is not one of {' '.join(KINDS)}")
    fm["kind"] = kind
    fm["universal"] = fm.get("universal", "").lower() in ("true", "yes", "1")
    return fm


def declares(text: str) -> bool:
    """Does this record name a gate, or say in as many words that it has none?

    The BODY only, never the front matter — a `description` carrying the word "gated" is prose about
    the class, not a declaration about its resolution.
    """
    m = FM_RE.match(text)
    return bool(DECLARES_RE.search(text[m.end():] if m else text))


def build_record(rel: str, text: str) -> dict:
    """ONE record from its repo-relative path and its LF-folded text: the shape `records` builds from
    the working tree and `load_records_at` from a commit (TOOL-aGraftedHelix-29). `text` is kept so the
    two can be compared. A record that does not parse raises `Problem`."""
    fm = parse_front_matter(rel, text)
    body = text[FM_RE.match(text).end():]
    return {
        "path": rel, "name": fm["name"], "description": fm["description"],
        "kind": fm["kind"], "universal": fm["universal"],
        "declares": declares(text),
        "anchors": sorted(set(ANCHOR_RE.findall(body))),
        # Read for an invariant only; a class carries neither key's meaning.
        "decision": fm.get("decision", ""),
        "sections": parse_sections(body) if fm["kind"] == "invariant" else {},
        "text": text,
    }


def records(root: str, m: str) -> list:
    d = os.path.join(root, m, "gotchas")
    out = []
    if not os.path.isdir(d):
        return out
    for name in sorted(os.listdir(d)):
        if not name.endswith(".md") or name == "INDEX.md":
            continue
        out.append(build_record(f"{m}/gotchas/{name}", read(os.path.join(d, name))))
    return out


def load_records_at(root: str, m: str, sha: str) -> tuple:
    """`(records, unparsed)`: the catalogue as it stood at commit `sha` (TOOL-aGraftedHelix-29).

    ONE `git ls-tree` lists it and ONE `git cat-file --batch` reads every record, never a spawn per
    record. The batch is parsed as BYTES by each header's size field, then decoded and LF-folded as
    `read` does: a text-mode read misaligns the sizes on any multibyte character. A base with no
    catalogue holds zero records. A base record that does not parse is named in `unparsed`; it
    exempts nothing and never refuses the checklist.
    """
    try:
        listing = subprocess.run(["git", "ls-tree", "-z", sha, "--", f"{m}/gotchas/"], cwd=root,
                                 capture_output=True, check=True).stdout
        want = []
        for entry in listing.split(b"\0"):
            meta, tab, path = entry.partition(b"\t")
            name = path.decode("utf-8", "replace").rsplit("/", 1)[-1]
            if tab and meta.split()[1:2] == [b"blob"] and name.endswith(".md") and name != "INDEX.md":
                want.append((f"{m}/gotchas/{name}", meta.split()[2]))
        batch = subprocess.run(["git", "cat-file", "--batch"], cwd=root, capture_output=True, check=True,
                               input=b"".join(oid + b"\n" for _, oid in want)).stdout if want else b""
    except subprocess.CalledProcessError as exc:
        raise Problem(f"gotchas: could not read the catalogue at {sha[:12]} — "
                      f"{exc.stderr.decode('utf-8', 'replace').strip()}") from None
    recs, unparsed, pos = [], [], 0
    for rel, oid in want:
        try:
            nl = batch.index(b"\n", pos)
            size = int(batch[pos:nl].split()[2])
        except (ValueError, IndexError):
            raise Problem(f"gotchas: git cat-file returned no blob for {rel} at {sha[:12]}") from None
        text = batch[nl + 1:nl + 1 + size].decode("utf-8", "replace").replace("\r\n", "\n")
        pos = nl + 1 + size + 1
        try:
            recs.append(build_record(rel, text))
        except Problem:
            unparsed.append(rel)
    return recs, unparsed


def selectable(anchor: str, paths, m: str) -> set:
    """The paths an anchor can select. THE ONE COPY of the selection predicate.

    Substring both ways plus a BASENAME equality — the basename arm is harvest defect 3, kept
    deliberately: `check-memory-hygiene.sh` in a record selects that file wherever it lives, which is
    what makes short forms usable at all.

    The catalogue EXCLUDES ITSELF. Every record cites paths under `gotchas/` while describing its own
    class, and with basename matching a record naming `INDEX.md` would select every `INDEX.md` in the
    tree — so a diff that touches the catalogue would emit most of the catalogue. Noise on a
    checklist is how reviewers learn to skip it.
    """
    skip = f"{m}/gotchas/"
    return {p for p in paths
            if not p.startswith(skip)
            and (anchor in p or p in anchor or os.path.basename(p) == os.path.basename(anchor))}


def inert_only(rec: dict, paths, m: str, append_only: re.Pattern) -> bool:
    """True when every tracked path this record's anchors can REACH is append-only.

    Resolve THEN classify, never string-match the anchor token: an anchor is judged by what it
    selects. Upstream matched the append-only pattern against the raw token and the arm went green
    for every short-form anchor in the corpus.
    """
    hits = set()
    for a in rec["anchors"]:
        hits |= selectable(a, paths, m)
    return bool(hits) and all(append_only.match(p) for p in hits)


def check_invariant(rec: dict, tracked: set, legs, defined, why_undefined: str) -> tuple:
    """Check 18 over ONE invariant record: `(findings, announcements)`.

    `legs` is None when `LEG_MANIFEST` is blank and `defined` is None when the id grammar's kit is
    absent; each turns its arm into an ANNOUNCEMENT, printed at exit 0, rather than a red. WHAT THIS
    DOES NOT CHECK: that the ruling still describes the code, or that the guard named actually pins
    it — a resolving token proves the name exists, not that the gate asserts this behaviour.
    """
    p, bad, notes = rec["path"], [], []
    dec = rec["decision"]
    if not dec:
        bad.append(f"check 18: {p} is an invariant with no `decision:` — an invariant cites the ruling "
                   f"that makes it intended, or it is an opinion")
    elif defined is None:
        notes.append(f"gotchas: {p} decision {dec} NOT resolved — {why_undefined}")
    elif dec not in defined:
        bad.append(f"check 18: {p} names decision {dec}, which no record in this corpus defines")
    for h in INVARIANT_SECTIONS:
        if not rec["sections"].get(h):
            bad.append(f"check 18: {p} has no non-empty `## {h}` section — an invariant carries all of "
                       f"{', '.join(INVARIANT_SECTIONS)}")
    guard = rec["sections"].get("Guarded by") or []
    if guard:
        line = guard[0]
        toks = GUARD_TOKEN_RE.findall(line)
        rest = GUARD_TOKEN_RE.sub("", line)
        if line.rstrip(".").strip().lower() == "no machine gate":
            pass
        elif not toks or not re.fullmatch(r"(?:[\s,;·]|and)*", rest):
            bad.append(f"check 18: {p}'s `## Guarded by` opens with neither `no machine gate` nor backticked "
                       f"tokens alone: {line}")
        else:
            for t in toks:
                if t in tracked or any(x.startswith(t.rstrip("/") + "/") for x in tracked):
                    continue
                if legs is None:
                    notes.append(f"gotchas: {p} guard `{t}` NOT resolved — LEG_MANIFEST is blank, so a "
                                 f"token that is not a tracked path cannot be checked against a leg name")
                elif t not in legs:
                    bad.append(f"check 18: {p} guard `{t}` is neither a tracked path nor a leg name in "
                               f"the leg manifest")
    if rec["universal"]:
        bad.append(f"check 19: {p} is an invariant marked universal — a by-design line on every review "
                   f"skips the selection and the universal budget alike")
    return bad, notes


# ---------------------------------------------------------------------------------------- rendering
def render(recs: list, m: str) -> str:
    head = [
        f"# {m}/gotchas/ — the recurring bug-class catalogue",
        "",
        "One authored record per class. The table below is GENERATED from each record's front matter",
        "and its DERIVED anchors — do not hand-edit between the markers.",
        "",
        "Hand a reviewer the classes their diff can hit:",
        "",
        "```bash",
        # THIS install's path, derived, because INDEX.md is committed in the adopter's tree (S5).
        f"python {kit_rel()}/gotchas.py --for-diff <base>..<head>",
        f"python {kit_rel()}/gotchas.py --for-paths <path>...",
        "```",
        "",
        BEGIN,
        "",
        "| Class | Kind | Anchors | Universal | Description |",
        "|---|---|---:|---|---|",
    ]
    for r in recs:
        head.append(f"| [{r['name']}]({os.path.basename(r['path'])}) | {r['kind']} | "
                    f"{len(r['anchors'])} | {'yes' if r['universal'] else ''} | {_cell(r['description'])} |")
    classes = [r for r in recs if r["kind"] == "class"]
    head += [
        "",
        f"{len(recs)} record(s): {len(classes)} class, "
        f"{sum(1 for r in recs if r['kind'] == 'note')} note, "
        f"{sum(1 for r in recs if r['kind'] == 'invariant')} invariant, "
        f"{sum(1 for r in recs if r['kind'] == 'superseded')} superseded · "
        f"{sum(1 for r in classes if r['universal'])} universal · "
        f"{sum(1 for r in classes if not r['anchors'] and not r['universal'])} unanchored",
        "",
        END,
        "",
    ]
    return "\n".join(head)


def _cell(s: str) -> str:
    """A pipe inside a cell ends the cell — GFM drops the rest of the row silently."""
    return s.replace("|", "\\|").strip()


# ------------------------------------------------------------------------------------------- checks
def cmd_check(root: str, conf: dict) -> int:
    m = conf["MEMORY_ROOT"]
    recs = records(root, m)
    bad = []
    # 17 — INDEX freshness.
    idx = os.path.join(root, m, "gotchas", "INDEX.md")
    want = render(recs, m)
    if recs or os.path.exists(idx):
        if not os.path.exists(idx):
            bad.append(f"check 17: {m}/gotchas/INDEX.md is missing — run gotchas.py --write")
        elif read(idx) != want:
            bad.append(f"check 17: {m}/gotchas/INDEX.md is stale — run gotchas.py --write")
    notes = []
    if recs:
        paths = [p for p in run("git", "ls-files", cwd=root).split("\n") if p]
        ao = append_only_re(root)
        # TOOL-aGraftedHelix-3 — the invariant arms' two inputs, read only when an invariant exists:
        # the defined-id walk costs a corpus pass, and a catalogue of classes alone pays nothing.
        invs = [r for r in recs if r["kind"] == "invariant"]
        if invs:
            legs = load_leg_names(root, conf)
            defined, why_undefined = load_defined_ids(root)
            tracked = set(paths)
        for r in recs:
            if r["kind"] == "invariant":
                b, n = check_invariant(r, tracked, legs, defined, why_undefined)
                bad += b
                notes += n
                # 19 for an invariant: no universal escape, so an unanchored one is always a finding.
                if not r["anchors"]:
                    bad.append(f"check 19: {r['path']} derives no anchor — an invariant reaches a review "
                               f"only through its anchors, so it can never be handed to one")
                elif inert_only(r, paths, m, ao):
                    bad.append(f"check 19: {r['path']} has INERT anchors — every path they reach is "
                               f"append-only, so the record is reachable on paper and dead in practice")
                continue
            if r["kind"] != "class":
                continue
            # 18 — declares a gate, or says it has none.
            if not r["declares"]:
                bad.append(f"check 18: {r['path']} names no gate and does not say it has none — "
                           f"'no gate named' and 'gate not yet written' are indistinguishable from outside")
            # 19 — the INERT-ANCHOR arm.
            if not r["anchors"] and not r["universal"]:
                bad.append(f"check 19: {r['path']} derives no anchor and is not marked universal — "
                           f"it can never appear on a checklist")
            elif r["anchors"] and inert_only(r, paths, m, ao):
                bad.append(f"check 19: {r['path']} has INERT anchors — every path they reach is "
                           f"append-only, so the record is reachable on paper and dead in practice")
        budget = conf.get("UNIVERSAL_BUDGET", "")
        if budget:
            n = sum(1 for r in recs if r["kind"] == "class" and r["universal"])
            if n > int(budget):
                bad.append(f"check 19: {n} universal record(s) against a budget of {budget} — every one "
                           f"is emitted on EVERY checklist, so raise the budget in a commit that says why")
    # Announcements first and never prefixed `HYGIENE`: they print at exit 0, and the engine shows a
    # green run's output (TOOL-aGraftedHelix-3 S7) so a skip is never mistaken for a pass.
    for line in notes:
        print(line)
    for line in bad:
        print("HYGIENE " + line)
    return 1 if bad else 0


def cmd_write(root: str, conf: dict) -> int:
    m = conf["MEMORY_ROOT"]
    recs = records(root, m)
    idx = os.path.join(root, m, "gotchas", "INDEX.md")
    if not recs and not os.path.isdir(os.path.dirname(idx)):
        print("gotchas: no catalogue to render")
        return 0
    write(idx, render(recs, m))
    print(f"gotchas: wrote {m}/gotchas/INDEX.md ({len(recs)} record(s))")
    return 0


def cmd_report(root: str, conf: dict) -> int:
    m = conf["MEMORY_ROOT"]
    recs = records(root, m)
    classes = [r for r in recs if r["kind"] == "class"]
    print(f"records          : {len(recs)}")
    print(f"classes          : {len(classes)}")
    print(f"invariants       : {sum(1 for r in recs if r['kind'] == 'invariant')}")
    print(f"universal        : {sum(1 for r in classes if r['universal'])}  "
          f"(budget {conf.get('UNIVERSAL_BUDGET') or 'unset'})")
    print(f"unanchored       : {sum(1 for r in classes if not r['anchors'] and not r['universal'])}")
    for r in recs:
        print(f"    {r['kind']:<10} {len(r['anchors']):>2} anchor(s)  {r['name']}")
    return 0


def normalise_paths(root: str, paths) -> list:
    """Caller-supplied paths to the repo-relative POSIX shape `selectable` was written against.

    A no-op for the git-derived caller, which is the point: BOTH callers pass through it, so this is
    ONE normalising entry rather than a guard bolted onto the new one. It closes two defects that were
    unreachable until a path-based verb existed, because `git diff --name-only` emits neither shape:

    - `selectable`'s basename arm calls `os.path.basename`, which is PLATFORM-DEPENDENT. A backslash
      path matches on Windows (`ntpath` splits it) and silently does not on POSIX (`posixpath` returns
      the whole string). Same code, two answers, and the CI answer is the wrong one.
    - The catalogue's self-exclusion is a repo-RELATIVE prefix test, so an ABSOLUTE path under
      `<memory>/gotchas/` slips past it and the catalogue starts selecting itself — the exact noise
      this module's docstring says destroys a checklist.

    No subprocess: `run` sets `check=True` and `main` catches only `Problem`, so shelling out to git
    here would turn an unexpected failure into a traceback out of a gate.
    """
    out = []
    for p in paths:
        q = p.replace("\\", "/").strip()
        if os.path.isabs(q) or (len(q) > 1 and q[1] == ":"):
            try:
                q = os.path.relpath(q, root).replace("\\", "/")
            except ValueError:      # a different drive on Windows: not in this repo, so unselectable
                continue
        while q.startswith("./"):
            q = q[2:]
        # A path that normalises to the repo root selects EVERY anchor through the substring arm, so
        # the checklist becomes the whole catalogue and stops meaning anything. Refused by name
        # rather than emitted as noise nobody will read.
        if q in ("", ".", "/", ".."):
            raise Problem(f"gotchas: '{p}' selects the whole tree — pass the paths a change touches, "
                          f"not the root")
        q = q.rstrip("/")
        if q:
            out.append(q)
    return out


def cmd_for_paths(root: str, conf: dict, paths, label: str = None, noun: str = "file",
                  base: str = None, changed=None) -> int:
    """STDOUT IS THE CHECKLIST. The ONE selection path; `cmd_for_diff` delegates into it.

    With `base`, a full sha, the by-design block is read from the invariant records AT THAT COMMIT,
    less every record the subject changed, and each invariant the subject moved prints as a checklist
    item instead (TOOL-aGraftedHelix-29). `changed` is the range's paths under `--for-diff`; under
    `--for-paths --base` it is derived here: every record whose text differs between the base and the
    working tree, exists on one side only, or did not parse at the base. Without `base` the block is
    read from the working tree and a header line says so. Classes always read the working tree.
    """
    m = conf["MEMORY_ROOT"]
    recs = records(root, m)
    paths = normalise_paths(root, paths)
    if not paths:
        print(f"gotchas: {label or 'those paths'} selects no file — nothing to check")
        return 0
    hit, uni, inv = [], [], []
    for r in recs:
        if r["kind"] not in ("class", "invariant"):
            continue
        if r["kind"] == "class" and r["universal"]:
            uni.append(r)
            continue
        for a in r["anchors"]:
            if selectable(a, paths, m):
                (inv if r["kind"] == "invariant" else hit).append(r)
                break
    head, moved = [INVARIANTS_UNPINNED], []
    if base:
        at_base, unparsed = load_records_at(root, m, base)
        if changed is None:
            now = {r["path"]: r["text"] for r in recs}
            then = {r["path"]: r["text"] for r in at_base}
            changed = {p for p in set(now) | set(then) if now.get(p) != then.get(p)} | set(unparsed)
        changed = set(normalise_paths(root, changed))
        moved = derive_moved_invariants(recs, at_base, changed, paths, m)
        inv = [r for r in at_base if r["kind"] == "invariant" and r["path"] not in changed
               and any(selectable(a, paths, m) for a in r["anchors"])]
        head = [INVARIANTS_AT_BASE.format(sha=base[:12], n=len(moved))]
        if unparsed:
            head.append(INVARIANTS_UNPARSED.format(n=len(unparsed), sha=base[:12], paths=" ".join(unparsed)))
    print(f"# recurring-bug-class checklist for {label or f'{len(paths)} path(s)'} ({len(paths)} {noun}(s))")
    print(f"# {len(hit)} class(es) selected by an anchor + {len(uni)} universal")
    for line in head:
        print(line)
    for r in uni + hit:
        print(f"\n- [ ] {r['name']}{' (universal)' if r['universal'] else ''}\n      {r['description']}\n      {r['path']}")
    for r in moved:
        print(f"\n{MOVED_INVARIANT_ITEM.format(name=r['name'])}\n      {r['description']}\n      {r['path']}")
    # The block stays LAST: the review harness ends it at the first line not opening `- `.
    for line in render_by_design(inv):
        print(line)
    return 0


def derive_moved_invariants(recs: list, at_base: list, changed, paths, m: str) -> list:
    """The invariants a subject MOVED, to print as items (TOOL-aGraftedHelix-29): every record of kind
    `invariant` at either end whose path is in `changed`, and whose own path is one of `paths` or
    whose anchors at either end select one. The own-path clause is what keeps the anchors from
    deciding: under `--for-diff` a moved record's path is always one of `paths`, so a range cannot
    write anchors that keep its own ruling off its review. Named from the working tree's record where
    one exists, else from the base's; sorted by path. `m` is the memory root `selectable` excludes."""
    now = {r["path"]: r for r in recs if r["kind"] == "invariant"}
    then = {r["path"]: r for r in at_base if r["kind"] == "invariant"}
    out = []
    for p in sorted((set(now) | set(then)) & set(changed)):
        ends = [r for r in (now.get(p), then.get(p)) if r]
        if p in paths or any(selectable(a, paths, m) for r in ends for a in r["anchors"]):
            out.append(ends[0])
    return out


def resolve_range_base(root: str, rng: str) -> str:
    """The full sha a range DIFFS FROM (TOOL-aGraftedHelix-29): the merge base of `A...B`, the left side
    of `A..B`, and the revision itself for a single revision, an empty side read as `HEAD` as git
    reads it. A range or side opening `-` is refused before any git call, because git would read it
    as an option; a value git cannot resolve is a named `Problem`, never a traceback."""
    sep = "..." if "..." in rng else ".." if ".." in rng else None
    sides = [s or "HEAD" for s in rng.split(sep, 1)] if sep else [rng]
    if any(s.startswith("-") for s in [rng] + sides):
        raise Problem(f"gotchas: '{rng}' opens with '-', which git would read as an option — pass a "
                      f"range or a revision")
    try:
        if sep == "...":
            return run("git", "merge-base", sides[0], sides[1], cwd=root).strip()
        return run("git", "rev-parse", "--verify", sides[0] + "^{commit}", cwd=root).strip()
    except subprocess.CalledProcessError as exc:
        raise Problem(f"gotchas: '{rng}' does not resolve to a base commit — "
                      f"{((exc.stderr or '').strip().splitlines() or [f'git exited {exc.returncode}'])[0]}") from None


def render_by_design(inv: list) -> list:
    """The by-design block (I4): its head ALWAYS, `0` included, so a reader can tell "no invariant
    touched" from a kit that predates the block; then one line per selected invariant, built from the
    first paragraph of its `## Looks wrong` and `## Actually` sections."""
    out = ["", BY_DESIGN_HEAD.format(n=len(inv))]
    for r in inv:
        s = r["sections"]
        out.append(f"- {r['name']} — {' '.join(s.get('Looks wrong') or [])} → "
                   f"{' '.join(s.get('Actually') or [])} ({r['decision']})")
    return out


def cmd_for_diff(root: str, conf: dict, rng: str) -> int:
    """STDOUT IS THE CHECKLIST. Derives the paths from git, then delegates.

    `noun` keeps this caller's header BYTE-IDENTICAL to what it printed before the split. A refactor
    is not allowed to change existing output, and an arm asserts it rather than trusting it.

    The by-design block is read at the commit the range diffs from (TOOL-aGraftedHelix-29). A range
    opening `-` is refused before `git diff` sees it, since `--output=<file>` would write a file, and a
    range git refuses is a named `Problem` where it was a traceback.

    The touched set names BOTH sides of a rename (TOOL-aGraftedHelix-36 S1): porcelain `git diff`
    detects renames and names only the destination, which left a renamed invariant's base record
    outside `changed` and so inside the by-design block, exempting the very ruling the range moved.
    NUL-separated, so a path carrying a newline or a space is one entry.
    """
    if rng.startswith("-"):
        raise Problem(f"gotchas: '{rng}' opens with '-', which git would read as an option — pass a range")
    try:
        changed = [p for p in run("git", "diff", "--no-renames", "--name-only", "-z", rng, cwd=root).split("\0") if p]
    except subprocess.CalledProcessError as exc:
        raise Problem(f"gotchas: git diff cannot read the range '{rng}' — "
                      f"{((exc.stderr or '').strip().splitlines() or [f'git exited {exc.returncode}'])[0]}") from None
    if not changed:
        print(f"gotchas: {rng} touches no file — nothing to check")
        return 0
    base = resolve_range_base(root, rng)
    return cmd_for_paths(root, conf, changed, label=rng, noun="changed file", base=base, changed=changed)


# ----------------------------------------------------------------------------------------- selftest
def _rec(name, desc, body, kind=None, universal=None, indent=False):
    fm = [f"name: {name}", f"description: {desc}"]
    if kind:
        fm.append(f"kind: {kind}")
    if universal is not None:
        fm.append(f"universal: {'true' if universal else 'false'}")
    if indent:
        fm.append("  nested: dropped-without-a-word")
    return "---\n" + "\n".join(fm) + "\n---\n\n" + body


def _scratch(tmp: str, recs: dict, extra=None):
    PFX = derive_install_prefix()   # TOOL-aRepatriatedFork-28
    run("git", "init", "-q", ".", cwd=tmp)
    run("git", "config", "user.email", "t@t.test", cwd=tmp)
    run("git", "config", "user.name", "t", cwd=tmp)
    write(os.path.join(tmp, ".memory-tree.conf"),
          'MEMORY_ROOT=memory\nDISCIPLINES="arch"\nFAMILIES="arch:ARCH"\nUNIVERSAL_BUDGET="1"\n')
    write(os.path.join(tmp, "memory", "HYGIENE.md"), "sentinel\n")
    write(os.path.join(tmp, "memory", "README.md"), "# r\n")
    # A POPULATED append-only area: check 19's inert arm can only fire when an anchor is able to
    # reach one, so on a tree with an empty append-only area the rule ships green forever.
    write(os.path.join(tmp, "memory", "DECISIONS.md"), "# d\n\n- ARCH-tOne-1 · a decision\n")
    write(os.path.join(tmp, "memory", "archive", "OLD.2026-01-01.md"), "frozen\n")
    write(os.path.join(tmp, PFX, "some-gate.sh"), "#!/usr/bin/env bash\n")
    write(os.path.join(tmp, "deep", "nested", "some-gate.sh"), "#!/usr/bin/env bash\n")
    for name, text in recs.items():
        write(os.path.join(tmp, "memory", "gotchas", name), text)
    for rel, text in (extra or {}).items():
        write(os.path.join(tmp, rel), text)
    run("git", "add", "-A", cwd=tmp)
    run("git", "commit", "-q", "-m", "f", "--no-verify", cwd=tmp)
    return load_conf(tmp)


def derive_install_prefix() -> str:
    """The install prefix WITH its trailing slash, derived from where this file sits and empty at a
    root install. Every fixture and host path the self-test builds is spelled through it, never
    through a literal prefix (TOOL-aRepatriatedFork-28)."""
    import pathlib
    here = pathlib.Path(__file__).resolve().parent
    for anc in here.parents:
        if (anc / ".git").exists():
            rel = here.parent.relative_to(anc).as_posix()
            return "" if rel == "." else rel + "/"
    raise SystemExit(f"{pathlib.Path(__file__).name}: not inside a git repository, so there is no "
                     "install prefix to derive")


def cmd_selftest() -> int:
    PFX = derive_install_prefix()   # TOOL-aRepatriatedFork-28
    import io
    import contextlib

    fails = []

    def arm(label, want, fn):
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                rc = fn()
            got = buf.getvalue() + f"[rc={rc}]"
        except Problem as exc:
            got = str(exc)
        except Exception as exc:  # noqa: BLE001 — a traceback here IS the finding
            got = f"UNEXPECTED {type(exc).__name__}: {exc}"
        ok = (want in got) if want else ("[rc=0]" in got)
        print(("arm ok    " if ok else "arm FAIL  ") + label + ("" if ok else f" — expected {want!r}, got: {got.strip()}"))
        if not ok:
            fails.append(label)

    GOOD = _rec("good-class", "a real class", f"Fires on `{PFX}some-gate.sh`. Gated by the hygiene gate.\n")
    with tempfile.TemporaryDirectory() as base:
        t = os.path.join(base, "clean"); os.makedirs(t)
        c = _scratch(t, {"good-class.md": GOOD})
        cmd_write(t, c)
        run("git", "add", "-A", cwd=t); run("git", "commit", "-q", "-m", "idx", "--no-verify", cwd=t)
        arm("a rendered catalogue is clean", None, lambda: cmd_check(t, c))

        # 17 — freshness.
        write(os.path.join(t, "memory", "gotchas", "INDEX.md"), "hand-edited\n")
        arm("check 17 catches a stale INDEX", "INDEX.md is stale", lambda: cmd_check(t, c))

        # 18 — declares.
        t2 = os.path.join(base, "nogate"); os.makedirs(t2)
        c2 = _scratch(t2, {"x.md": _rec("x", "d", f"Fires on `{PFX}some-gate.sh`. Nothing said about a gate.\n")})
        cmd_write(t2, c2); run("git", "add", "-A", cwd=t2); run("git", "commit", "-q", "-m", "i", "--no-verify", cwd=t2)
        arm("check 18 catches a record that names no gate", "names no gate and does not say it has none",
            lambda: cmd_check(t2, c2))
        arm("--declares is the one predicate: 'no machine gate' declares", "[rc=0]",
            lambda: 0 if declares(_rec("x", "d", "There is no machine gate for this.\n")) else 1)
        arm("--declares reads the BODY, not the front matter", "[rc=0]",
            lambda: 0 if not declares(_rec("x", "gated by nothing", "plain body\n")) else 1)

        # 19 — inert anchors, and the unanchored case.
        t3 = os.path.join(base, "inert"); os.makedirs(t3)
        c3 = _scratch(t3, {"i.md": _rec("i", "d", "Only ever touches `memory/archive/OLD.2026-01-01.md`. Gated by nothing.\n")})
        cmd_write(t3, c3); run("git", "add", "-A", cwd=t3); run("git", "commit", "-q", "-m", "i", "--no-verify", cwd=t3)
        arm("check 19 catches INERT anchors", "has INERT anchors", lambda: cmd_check(t3, c3))
        t4 = os.path.join(base, "unanch"); os.makedirs(t4)
        c4 = _scratch(t4, {"u.md": _rec("u", "d", "Applies everywhere. No machine gate.\n")})
        cmd_write(t4, c4); run("git", "add", "-A", cwd=t4); run("git", "commit", "-q", "-m", "i", "--no-verify", cwd=t4)
        arm("check 19 catches an unanchored non-universal record", "derives no anchor",
            lambda: cmd_check(t4, c4))
        t5 = os.path.join(base, "uni"); os.makedirs(t5)
        c5 = _scratch(t5, {"u.md": _rec("u", "d", "Applies everywhere. No machine gate.\n", universal=True)})
        cmd_write(t5, c5); run("git", "add", "-A", cwd=t5); run("git", "commit", "-q", "-m", "i", "--no-verify", cwd=t5)
        arm("a universal record needs no anchor", None, lambda: cmd_check(t5, c5))

        # the universal BUDGET.
        t6 = os.path.join(base, "budget"); os.makedirs(t6)
        c6 = _scratch(t6, {
            "u1.md": _rec("u1", "d", "Everywhere. No machine gate.\n", universal=True),
            "u2.md": _rec("u2", "d", "Everywhere too. No machine gate.\n", universal=True)})
        cmd_write(t6, c6); run("git", "add", "-A", cwd=t6); run("git", "commit", "-q", "-m", "i", "--no-verify", cwd=t6)
        arm("the universal budget is enforced", "against a budget of 1", lambda: cmd_check(t6, c6))

        # front matter: an indented key is NAMED, not dropped.
        t7 = os.path.join(base, "indent"); os.makedirs(t7)
        c7 = _scratch(t7, {"n.md": _rec("n", "d", f"Body cites `{PFX}some-gate.sh`. No machine gate.\n", indent=True)})
        arm("an indented front-matter key is named", "keys live at COLUMN 0", lambda: cmd_check(t7, c7))

        # ---- the THREE CARRIED HARVEST DEFECTS. Each is asserted as OBSERVED behaviour so that a
        # ---- future "fix" fails loudly and has to be made deliberately.
        d1 = ANCHOR_RE.findall("a `Class::method` reference\n")
        arm("harvest defect 1: `::` inside backticks harvests to nothing", "[rc=0]",
            lambda: 0 if d1 == [] else 1)
        # Defect 2 is the one this implementation does NOT share, and the arm says so rather than
        # asserting upstream's behaviour out of deference. Upstream's token pattern required a
        # non-empty tail after the slash, so a directory-only kit token harvested to nothing and a record
        # written that way was silently unanchored. Here the tail may be empty, the directory token
        # IS harvested, and it selects everything beneath it. The arm pins the DIFFERENCE, so a
        # future tightening of the pattern reintroduces the upstream defect loudly.
        d2 = ANCHOR_RE.findall(f"a directory `{PFX}{HERE.name}/` reference\n")
        arm("harvest defect 2 does NOT apply here: a trailing slash harvests the directory", "[rc=0]",
            lambda: 0 if d2 == [f"{PFX}{HERE.name}/"] else 1)
        arm("...and that directory anchor selects everything beneath it", "[rc=0]",
            lambda: 0 if selectable(f"{PFX}{HERE.name}/", [f"{PFX}{HERE.name}/gotchas.py"], "memory")
            == {f"{PFX}{HERE.name}/gotchas.py"} else 1)
        paths = [f"{PFX}some-gate.sh", "deep/nested/some-gate.sh", "memory/README.md"]
        sel = selectable("some-gate.sh", paths, "memory")
        arm("harvest defect 3: a basename selects tree-wide", "[rc=0]",
            lambda: 0 if sel == {f"{PFX}some-gate.sh", "deep/nested/some-gate.sh"} else 1)
        arm("the catalogue never selects itself", "[rc=0]",
            lambda: 0 if selectable("INDEX.md", ["memory/gotchas/INDEX.md"], "memory") == set() else 1)

        # A failure crossing the corpus_ids boundary is NAMED, not a traceback. The sibling raises
        # its OWN Problem class, which this module's `except Problem` cannot catch — two classes
        # with one name are two classes, and the first run of this arm printed a WinError stack out
        # of a hygiene gate.
        t9 = os.path.join(base, "boundary"); os.makedirs(t9)
        c9 = _scratch(t9, {"g.md": GOOD})
        cmd_write(t9, c9); run("git", "add", "-A", cwd=t9); run("git", "commit", "-q", "-m", "i", "--no-verify", cwd=t9)
        old_bash = os.environ.get("GOV_BASH")
        os.environ["GOV_BASH"] = os.path.join(base, "no-such-bash")
        try:
            arm("a failure crossing the corpus_ids boundary is named, not a traceback",
                "could not ask corpus_ids", lambda: cmd_check(t9, c9))
        finally:
            if old_bash is None:
                del os.environ["GOV_BASH"]
            else:
                os.environ["GOV_BASH"] = old_bash

        # --for-diff: anchors that intersect, plus universal, and nothing else.
        t8 = os.path.join(base, "diff"); os.makedirs(t8)
        c8 = _scratch(t8, {
            "hit.md": _rec("hit", "d", f"Fires on `{PFX}some-gate.sh`. Gated by the hygiene gate.\n"),
            "miss.md": _rec("miss", "d", "Fires on `memory/README.md`. Gated by the hygiene gate.\n"),
            "uni.md": _rec("uni", "d", "Everywhere. No machine gate.\n", universal=True),
            "note.md": _rec("note", "d", f"A policy, not a class. Touches `{PFX}some-gate.sh`. No machine gate.\n", kind="note")})
        cmd_write(t8, c8); run("git", "add", "-A", cwd=t8); run("git", "commit", "-q", "-m", "i", "--no-verify", cwd=t8)
        write(os.path.join(t8, PFX, "some-gate.sh"), "#!/usr/bin/env bash\n# edited\n")
        run("git", "add", "-A", cwd=t8); run("git", "commit", "-q", "-m", "edit", "--no-verify", cwd=t8)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cmd_for_diff(t8, c8, "HEAD~1..HEAD")
        text = out.getvalue()
        arm("--for-diff emits the anchored hit", "[rc=0]", lambda: 0 if "- [ ] hit" in text else 1)
        arm("--for-diff emits every universal record", "[rc=0]", lambda: 0 if "- [ ] uni (universal)" in text else 1)
        arm("--for-diff omits a record whose anchors miss", "[rc=0]", lambda: 0 if "- [ ] miss" not in text else 1)

        # ---- --for-paths: the same predicate, reached without a diff --------------------------------
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cmd_for_paths(t8, c8, [f"{PFX}some-gate.sh"])
        ptext = out.getvalue()
        arm("--for-paths emits the anchored hit", "[rc=0]", lambda: 0 if "- [ ] hit" in ptext else 1)
        arm("--for-paths omits a record whose anchors miss", "[rc=0]",
            lambda: 0 if "- [ ] miss" not in ptext else 1)

        # THE ARM THAT FAILS WITHOUT normalise_paths. `os.path.basename` is platform-dependent, so a
        # backslash path matches on Windows and silently does not on POSIX. A path-based verb is the
        # FIRST caller that can receive one — git diff emits none — so this is the only place the split
        # is reachable at all, and CI is the side that would have been silently wrong.
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cmd_for_paths(t8, c8, ["tools\\some-gate.sh"])
        btext = out.getvalue()
        arm("--for-paths reads a backslash path identically to a forward-slash one", "[rc=0]",
            lambda: 0 if btext == ptext else 1)

        # An ABSOLUTE path under the catalogue must not defeat the self-exclusion, which is a
        # repo-relative prefix test: without normalisation the catalogue starts selecting itself.
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cmd_for_paths(t8, c8, [os.path.join(t8, "memory", "gotchas", "INDEX.md")])
        atext = out.getvalue()
        arm("--for-paths: an absolute catalogue path does not select the catalogue", "[rc=0]",
            lambda: 0 if "- [ ] hit" not in atext and "- [ ] miss" not in atext else 1)

        arm("--for-paths refuses a path that selects the whole tree", "selects the whole tree",
            lambda: cmd_for_paths(t8, c8, ["."]))
        arm("--for-diff omits a non-class record", "[rc=0]", lambda: 0 if "- [ ] note" not in text else 1)

        # ---- TOOL-aGraftedHelix-3: the invariant kind (I5), its check 18/19 arms, and the by-design
        # ---- block (I4). The decision `ARCH-tOne-1` is DEFINED by the fixture's decision-log row, so
        # ---- the clean arms resolve it through the real walk rather than a stubbed set.
        conf_text = 'MEMORY_ROOT=memory\nDISCIPLINES="arch"\nFAMILIES="arch:ARCH"\nUNIVERSAL_BUDGET="1"\n'
        legs = {".memory-tree.conf": conf_text + 'LEG_MANIFEST="legs.json"\n',
                "legs.json": '[{"name": "fixture leg"}]\n'}

        def build_invariant(name, over=None, decision="ARCH-tOne-1", universal=False):
            secs = {"Looks wrong": f"It looks wrong in `{PFX}some-gate.sh`.", "Actually": "It is the ruling.",
                    "Do": "Keep it.", "Do not": "Change it.", "Guarded by": "no machine gate"}
            secs.update(over or {})
            fm = [f"name: {name}", "description: an invariant", "kind: invariant"]
            fm += [f"decision: {decision}"] if decision else []
            fm += ["universal: true"] if universal else []
            return ("---\n" + "\n".join(fm) + "\n---\n\n" +
                    "".join(f"## {h}\n{t}\n\n" for h, t in secs.items() if t is not None))

        def build_tree(label, recs, extra=None):
            t = os.path.join(base, label); os.makedirs(t)
            c = _scratch(t, recs, extra)
            cmd_write(t, c); run("git", "add", "-A", cwd=t); run("git", "commit", "-q", "-m", "i", "--no-verify", cwd=t)
            return t, c

        ti, ci = build_tree("inv", {"inv.md": build_invariant("inv-one")})
        arm("an invariant with five sections, a defined decision and a declared guard is clean", None,
            lambda: cmd_check(ti, ci))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cmd_for_paths(ti, ci, [f"{PFX}some-gate.sh"])
        itext = out.getvalue()
        want_line = f"- inv-one — It looks wrong in `{PFX}some-gate.sh`. → It is the ruling. (ARCH-tOne-1)"
        arm("--for-paths ends with the by-design block on a hit", "[rc=0]",
            lambda: 0 if itext.rstrip("\n").endswith(BY_DESIGN_HEAD.format(n=1) + "\n" + want_line) else 1)
        arm("...and the invariant is never a checklist item", "[rc=0]", lambda: 0 if "- [ ] inv-one" not in itext else 1)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cmd_for_paths(ti, ci, ["memory/README.md"])
        mtext = out.getvalue()
        arm("--for-paths prints the 0 header on a miss", "[rc=0]",
            lambda: 0 if mtext.rstrip("\n").endswith(BY_DESIGN_HEAD.format(n=0)) else 1)

        # The two announcements: printed at exit 0, never a red.
        tb, cb = build_tree("inv-blank", {"b.md": build_invariant("b", over={"Guarded by": "`fixture leg`"})})
        arm("a leg-name guard under a blank LEG_MANIFEST is announced and exits 0",
            "LEG_MANIFEST is blank, so a token that is not a tracked path cannot be checked against a leg name\n[rc=0]",
            lambda: cmd_check(tb, cb))
        real_load = load_defined_ids
        globals()["load_defined_ids"] = lambda root: real_load(root, grammar_dir=os.path.join(base, "no-grammar"))
        try:
            arm("an absent id-grammar kit is announced NOT resolved and exits 0",
                "decision ARCH-tOne-1 NOT resolved — the id grammar lives in the memory-recall kit, which is "
                "not installed beside this one\n[rc=0]", lambda: cmd_check(ti, ci))
        finally:
            globals()["load_defined_ids"] = real_load

        # A leg name resolves through a fixture manifest, and the reds a SET manifest makes possible.
        tl, cl = build_tree("inv-leg", {"l.md": build_invariant("l", over={"Guarded by": "`fixture leg`"})}, legs)
        arm("a leg name in the LEG_MANIFEST fixture resolves", None, lambda: cmd_check(tl, cl))
        tr, cr = build_tree("inv-red", {
            "dec.md": build_invariant("dec", decision="ARCH-tNone-9"),
            "sec.md": build_invariant("sec", over={"Do not": None}),
            "path.md": build_invariant("path", over={"Guarded by": f"`{PFX}no-such-gate.sh`"}),
            "leg.md": build_invariant("leg", over={"Guarded by": "`no such leg`"}),
            "una.md": build_invariant("una", over={"Looks wrong": "It looks wrong."}),
            "uni.md": build_invariant("uni", universal=True),
            "ine.md": build_invariant("ine", over={"Looks wrong": "It reads `memory/DECISIONS.md`."})}, legs)
        # ONE check run over the seven offenders, each arm reading its own line out of it: a walk per arm
        # would cost seven corpus passes to ask one question.
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rrc = cmd_check(tr, cr)
        rtext = out.getvalue()
        for label, want in (
                ("check 18 reds an unresolved decision", "dec.md names decision ARCH-tNone-9, which no record"),
                ("check 18 reds a missing section", "sec.md has no non-empty `## Do not` section"),
                ("check 18 reds a guard path that is not tracked", f"path.md guard `{PFX}no-such-gate.sh` is neither"),
                ("check 18 reds a leg name the manifest lacks", "leg.md guard `no such leg` is neither"),
                ("check 19 reds an unanchored invariant", "una.md derives no anchor"),
                ("check 19 reds a universal invariant", "uni.md is an invariant marked universal"),
                ("check 19 reds an invariant anchored only on the decision log", "ine.md has INERT anchors")):
            arm(label, want, lambda: (print(rtext, end=""), rrc)[1])

        # A SET manifest naming a missing file: the PROCESS prints one HYGIENE line, never a traceback.
        tm, _ = build_tree("inv-missing", {"m.md": build_invariant("m", over={"Guarded by": "`fixture leg`"})},
                           {".memory-tree.conf": conf_text + 'LEG_MANIFEST="missing.json"\n'})
        pm = subprocess.run([sys.executable, os.path.abspath(__file__), "--check"], cwd=tm,
                            capture_output=True, text=True, encoding="utf-8")
        arm("a LEG_MANIFEST naming a missing file is a HYGIENE line, not a traceback", "[rc=0]",
            lambda: 0 if pm.returncode == 1 and pm.stdout.startswith("HYGIENE gotchas: LEG_MANIFEST names missing.json")
            and "Traceback" not in pm.stdout + pm.stderr else 1)

        # ---- TOOL-aGraftedHelix-29: the by-design block is read at the subject's BASE, and an invariant
        # ---- the subject moved is a checklist ITEM. Each arm read `arm FAIL` against the parent's
        # ---- checker with these arms grafted in, which read every invariant from the working tree.
        def run_capture(fn):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    fn()
            except Exception as exc:  # noqa: BLE001 — a grafted parent's TypeError is the arm's finding
                buf.write(f"\nUNEXPECTED {type(exc).__name__}: {exc}\n")
            return buf.getvalue()

        def write_commit(t, files):
            for rel, text in files.items():
                if text is None:
                    os.remove(os.path.join(t, rel))
                else:
                    write(os.path.join(t, rel), text)
            run("git", "add", "-A", cwd=t); run("git", "commit", "-q", "-m", "c", "--no-verify", cwd=t)

        def extract_block(text):
            lines = text.rstrip("\n").split("\n")
            at = [i for i, line in enumerate(lines) if line.startswith("# by design — ")]
            return lines[at[0]:] if at else ["(no block)"]

        gate, cat, item = f"{PFX}some-gate.sh", "memory/gotchas/", "- [ ] NEW/CHANGED invariant "
        head0, head1 = BY_DESIGN_HEAD.format(n=0), BY_DESIGN_HEAD.format(n=1)

        def run_cli(t, *args):
            return subprocess.run([sys.executable, os.path.abspath(__file__), *args], cwd=t,
                                  capture_output=True, text=True, encoding="utf-8")

        # --for-paths --base over a working tree holding an UNCOMMITTED invariant; then with no base.
        tb, cb = build_tree("bd-base", {"inv-one.md": build_invariant("inv-one")})
        x = run("git", "rev-parse", "HEAD", cwd=tb).strip()
        write(os.path.join(tb, cat, "inv-new.md"), build_invariant("inv-new"))
        ptext = run_capture(lambda: cmd_for_paths(tb, cb, [gate], base=x))
        arm("--for-paths --base: an uncommitted invariant is an item, and the block holds the base's alone", "[rc=0]",
            lambda: 0 if extract_block(ptext) == [head1, want_line]
            and item + "inv-new" in ptext.split("# by design")[0] else 1)
        utext = run_capture(lambda: cmd_for_paths(tb, cb, [gate]))
        arm("--for-paths with no base says the block was read from the working tree", "[rc=0]",
            lambda: 0 if "\n# invariants are read from the working tree; with no --base" in utext else 1)
        os.remove(os.path.join(tb, cat, "inv-new.md"))
        pu = run_cli(tb, "--for-paths", "--base")
        arm("--for-paths --base with no revision is the usage line at exit 2", "[rc=0]",
            lambda: 0 if pu.returncode == 2 and pu.stdout.startswith("usage: gotchas.py --for-paths [--base <rev>]") else 1)

        # A range touching only the script, beside an UNCOMMITTED edit to the base's ruling.
        write_commit(tb, {gate: "#!/usr/bin/env bash\n# edit 1\n"})
        write(os.path.join(tb, cat, "inv-one.md"), build_invariant("inv-one", over={"Actually": "UNCOMMITTED ruling."}))
        dtext = run_capture(lambda: cmd_for_diff(tb, cb, "HEAD~1..HEAD"))
        arm("--for-diff: a block line carries the base's committed text, never a working-tree edit", "[rc=0]",
            lambda: 0 if extract_block(dtext) == [head1, want_line] else 1)
        run("git", "checkout", "-q", "--", f"{cat}inv-one.md", cwd=tb)

        # A range that EDITS the ruling, then one that TAKES IT OUT, each beside a script edit.
        write_commit(tb, {gate: "#!/usr/bin/env bash\n# edit 2\n",
                          f"{cat}inv-one.md": build_invariant("inv-one", over={"Actually": "It is the edited ruling."})})
        etext = run_capture(lambda: cmd_for_diff(tb, cb, "HEAD~1..HEAD"))
        arm("--for-diff: an invariant the range EDITS is an item and never in the block", "[rc=0]",
            lambda: 0 if extract_block(etext) == [head0] and item + "inv-one" in etext else 1)
        write_commit(tb, {gate: "#!/usr/bin/env bash\n# edit 3\n", f"{cat}inv-one.md": None})
        rtext = run_capture(lambda: cmd_for_diff(tb, cb, "HEAD~1..HEAD"))
        arm("--for-diff: an invariant the range TAKES OUT is an item named from the base's text", "[rc=0]",
            lambda: 0 if extract_block(rtext) == [head0] and item + "inv-one" in rtext else 1)

        # A range that RENAMES the ruling with a small edit (TOOL-aGraftedHelix-36 S1). Porcelain diff
        # names only the destination, so the read without `--no-renames` left the base's inv-one in
        # the block as an exemption; read red against that touched set.
        tr2, cr2 = build_tree("bd-mv", {"inv-one.md": build_invariant("inv-one")})
        write_commit(tr2, {gate: "#!/usr/bin/env bash\n# rename\n", f"{cat}inv-one.md": None,
                           f"{cat}inv-two.md": build_invariant("inv-two", over={"Actually": "It is the moved ruling."})})
        mtext = run_capture(lambda: cmd_for_diff(tr2, cr2, "HEAD~1..HEAD"))
        arm("--for-diff: an invariant the range RENAMES is two items and never in the block", "[rc=0]",
            lambda: 0 if extract_block(mtext) == [head0] and item + "inv-one" in mtext
            and item + "inv-two" in mtext else 1)

        # Two refusals, through the process: a range git cannot resolve, and one git would read as an option.
        pb = run_cli(tb, "--for-diff", "nosuchrev..HEAD")
        arm("--for-diff over a range git cannot resolve is a HYGIENE line at exit 1, not a traceback", "[rc=0]",
            lambda: 0 if pb.returncode == 1 and pb.stdout.startswith("HYGIENE gotchas:")
            and "Traceback" not in pb.stdout + pb.stderr else 1)
        target = os.path.join(tb, "injected.txt")
        po = run_cli(tb, "--for-diff", f"--output={target}")
        arm("--for-diff refuses a range opening '-' before git can read it as an option", "[rc=0]",
            lambda: 0 if po.returncode == 1 and po.stdout.startswith("HYGIENE gotchas:")
            and not os.path.exists(target) else 1)

        # A range that ADDS an invariant; then a three-dot range from a side branch over that tree.
        tc, cc = build_tree("bd-add", {"inv-one.md": build_invariant("inv-one")})
        write_commit(tc, {gate: "#!/usr/bin/env bash\n# add\n", f"{cat}inv-new.md": build_invariant("inv-new")})
        atext = run_capture(lambda: cmd_for_diff(tc, cc, "HEAD~1..HEAD"))
        arm("--for-diff: an invariant the range ADDS is an item before the block, which holds the base's", "[rc=0]",
            lambda: 0 if extract_block(atext) == [head1, want_line]
            and item + "inv-new" in atext.split("# by design")[0] else 1)
        run("git", "branch", "side", cwd=tc)
        write_commit(tc, {f"{cat}inv-one.md": build_invariant("inv-one", over={"Actually": "It is the newer ruling."})})
        left = run("git", "rev-parse", "HEAD", cwd=tc).strip()
        run("git", "checkout", "-q", "side", cwd=tc)
        write_commit(tc, {gate: "#!/usr/bin/env bash\n# side\n", f"{cat}inv-side.md": build_invariant("inv-side")})
        sblk = extract_block(run_capture(lambda: cmd_for_diff(tc, cc, f"{left}...HEAD")))
        arm("--for-diff A...B reads the block at the merge base, never at the left side", "[rc=0]",
            lambda: 0 if want_line in sblk and not any("inv-side" in s or "newer" in s for s in sblk) else 1)

        # A base with no catalogue at all; then a base record whose front matter does not parse.
        td = os.path.join(base, "bd-none"); os.makedirs(td)
        cd = _scratch(td, {})
        write_commit(td, {gate: "#!/usr/bin/env bash\n# first\n", f"{cat}inv-new.md": build_invariant("inv-new")})
        ntext = run_capture(lambda: cmd_for_diff(td, cd, "HEAD~1..HEAD"))
        arm("--for-diff over a base with no catalogue prints a block of 0 and itemises the invariant", "[rc=0]",
            lambda: 0 if extract_block(ntext) == [head0] and item + "inv-new" in ntext else 1)
        te = os.path.join(base, "bd-bad"); os.makedirs(te)
        ce = _scratch(te, {"inv-bad.md": "---\nname: inv-bad\nkind: invariant\n---\n\nno description key\n"})
        write_commit(te, {gate: "#!/usr/bin/env bash\n# fixed\n", f"{cat}inv-bad.md": build_invariant("inv-bad")})
        ftext = run_capture(lambda: cmd_for_diff(te, ce, "HEAD~1..HEAD"))
        arm("--for-diff: a base record that does not parse is announced, exempts nothing and is an item", "[rc=0]",
            lambda: 0 if any(s.startswith("# 1 record(s) at ") and s.endswith(f": {cat}inv-bad.md")
                             for s in ftext.split("\n"))
            and extract_block(ftext) == [head0] and item + "inv-bad" in ftext else 1)

    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed")
        return 1
    print("PASS — gotchas: all arms held")
    return 0


def main(argv: list) -> int:
    # UTF-8 BEFORE ANYTHING PRINTS (TOOL-aGraftedHelix-3 S4). The by-design block carries `→`, which
    # cp1252 cannot encode, and a piped stdout takes the locale codec on a node without PYTHONUTF8=1.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    mode = argv[1] if len(argv) > 1 else "--check"
    if mode == "--selftest":
        return cmd_selftest()
    if mode == "--declares":
        # rc ALONE cannot carry the verdict: an uncaught exception also exits 1 and would read as
        # "this record names no gate". So the verdict is PRINTED as a completion probe, and a
        # consumer refuses a run that did not print one. The record is read as BYTES decoded UTF-8,
        # never through the locale's text stdin.
        try:
            text = sys.stdin.buffer.read().decode("utf-8", "replace")
        except OSError as exc:
            print(f"gotchas --declares: could not read the record on stdin: {exc}", file=sys.stderr)
            return 2
        verdict = declares(text)
        print(f"declares: {'yes' if verdict else 'no'}")
        return 0 if verdict else 1
    try:
        root = run("git", "rev-parse", "--show-toplevel").strip()
    except Exception:  # noqa: BLE001
        print("gotchas: not a git repo")
        return 2
    conf = load_conf(root)
    try:
        if mode == "--check":
            return cmd_check(root, conf)
        if mode == "--write":
            return cmd_write(root, conf)
        if mode == "--report":
            return cmd_report(root, conf)
        if mode == "--for-diff":
            if len(argv) < 3:
                print("usage: gotchas.py --for-diff <base>..<head>")
                return 2
            return cmd_for_diff(root, conf, argv[2])
        if mode == "--for-paths":
            args, base = argv[2:], None
            if args[:1] == ["--base"]:
                if len(args) < 3:
                    print("usage: gotchas.py --for-paths [--base <rev>] <path>...")
                    return 2
                base, args = resolve_range_base(root, args[1]), args[2:]
            if not args:
                print("usage: gotchas.py --for-paths [--base <rev>] <path>...")
                return 2
            return cmd_for_paths(root, conf, args, base=base)
        print("usage: gotchas.py [--check|--write|--report|--for-diff <range>|"
              "--for-paths [--base <rev>] <path>...|--declares|--selftest]")
        return 2
    except Problem as exc:
        print(f"HYGIENE {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

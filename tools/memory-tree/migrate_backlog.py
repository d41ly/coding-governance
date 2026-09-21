#!/usr/bin/env python3
"""migrate_backlog.py — the shards-to-builds backlog migration PLANNER. Read-only.

    python migrate_backlog.py --plan
    python migrate_backlog.py --plan --record <dir> --record-as <unit-id>
    python migrate_backlog.py --plan --signed same-id=<path> --signed triage=<path>
    python migrate_backlog.py --plan --design-named <id> [--design-named <id> …]
    python migrate_backlog.py --selftest

WHAT THIS IS. Before any shard is rewritten somebody has to know exactly what the migration will do
to every id: which copy of it survives, which legacy pairs are one subject, which open asks on
finished builds still need a disposition, and what each id's status will be afterwards. `--plan`
builds that knowledge, files it as records a delegated signer signs, and the switch-over applies the
signed answer exactly.

WHAT `--plan` DOES NOT DECIDE, said out loud because a reader who over-trusts a planner is worse off
than one who does not run it. It never decides whether a backlog row and a spec with the same id are
ONE subject: it reports the evidence class, the sha that shows it and a heuristic overlap score, and
owner ruling D2 leaves the verdict to a signature. It never proposes a same-id spec as the evidence
that closes an ask, because that is the same question through a back door. It never mints an id —
the hold a legacy row leaves unaddressed previews as the literal placeholder `TRIAGE_ASK` below, and
the switch-over substitutes the id it mints. It mines no `filed` date: status is date-free, the
relocation engine already mines the date from its delta walk, and a second miner would be a second
answer. And it writes NOTHING unless `--record` names a directory, and then only inside it.

THE REPO IT PLANS IS THE ONE IT IS RUN IN — `git rev-parse --show-toplevel` of the working
directory, never this module's own location. An adopter runs the identical file in their own
deployer build, and the switch-over's landing reconcile runs it over a worktree of the remote tip,
where the module's tree is the wrong answer.

THE ROW GRAMMAR, THE RENDERERS AND THE FOLD ARE `backlog.py`'s, and the spec index and build statuses
are `gen_build_index.collect`'s. Nothing here re-spells any of them: a second grammar and a second
status rule are two answers to one question, and the copy is always the one that rots.
"""
from __future__ import annotations

import collections
import io
import os
import re
import subprocess
import sys
from contextlib import redirect_stdout

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import backlog                      # noqa: E402  — a sibling of this file, never a spelled path
import gen_build_index as index     # noqa: E402

# --------------------------------------------------------------------------------- the constants
#: The `filed` value every simulated ask row carries. It is a PLACEHOLDER and is never written into
#: a record: the prediction is a function of sets and reads no date, and the real date is the
#: relocation engine's to mine. A constant keeps two runs over one tree byte-identical.
FILED_PLACEHOLDER = "2026-01-01"

#: What a hold naming no resolvable id previews as. The switch-over files ONE triage ask and
#: substitutes its minted id for this token; the planner mints nothing.
TRIAGE_ASK = "TRIAGE-ASK"
#: The well-formed stand-in the SIMULATION files under that placeholder. The fold resolves a hold
#: against filed asks and spec H1s, so a hold on an unparseable token would derive UNRESOLVED and
#: the preview would report a status the switch-over will not produce. The stand-in never leaves
#: this module: every worksheet cell naming it is printed as `TRIAGE_ASK` above.
TRIAGE_SIM_SLUG = "migrationTriageAsk"

#: Below this, a row and its same-id spec are flagged low-overlap. A HEURISTIC, stated as one: its
#: only effect is to push a pair toward `not-unit` in the signer's rules, which is the recoverable
#: error.
OVERLAP_FLOOR = 0.12
#: Words that carry no subject. Removed from both sides before the overlap is measured, so a row and
#: a spec do not score for sharing `the`.
STOPWORDS = frozenset((
    "a an and are as at be but by for from has have in into is it its of on or that the their then "
    "there these this to was were when which will with would not no so").split())

#: The closing phrases the design measured in spec prose. A phrase alone is not evidence: the ask id
#: must appear on the SAME line, and the spec must not be the ask's own same-id spec.
CLOSING_PHRASES = ("closed against", "absorbs", "absorbed", "→ closed", "-> closed")

#: The signed records, by kind, and the header cells each must carry. The planner locates a column
#: by its cell and refuses a record missing one — the signer unit's own section 4 pins the same
#: rows, and these bytes are the interface between the two.
SIGNED_CELLS = {"same-id": ("Ask", "Verdict"), "triage": ("Ask", "Verdict", "Field")}

SAME_ID_COLUMNS = ("id", "spec", "legacy", "evidence", "sha", "low_overlap", "overlap")
TRIAGE_COLUMNS = ("id", "home", "source", "legacy", "derived", "proposal", "evidence", "basis",
                  "dead_pointer")
STATUS_COLUMNS = ("id", "legacy", "predicted", "class", "decided_by")

#: The evidence classes of the same-id worksheet, and the proposal bases of the triage worksheet.
#: Declared as data so a consumer iterates them rather than retyping the list.
EVIDENCE_CLASSES = ("specced-in-place", "born-in-spec-commit", "none")
PROPOSAL_BASES = ("mined-closure", "commit-names-ask", "row-names-hold", "design-named", "none")
STATUS_CLASSES = ("same", "mirror-closed", "stale-spec", "mined-closure", "recovered-flip",
                  "collision-kept-live", "triaged")

#: The declared normalizations, in the order section 4 of the spec lists them. A prospective ask row
#: may differ from its chosen legacy copy in these ways and in NO other; each is counted and the
#: count is printed, so the population of every one of them is known before the switch-over's commit.
NORMALIZATIONS = ("status-slot-removed", "filed-inserted", "unit-inserted", "wrapped-row-joined",
                  "relative-link-rebased", "archive-citation-unbackticked")

#: The recording kind a `--record` directory implies. Derived from the directory's own name so a
#: record filed into `reviews/` is not named as a build record; anything else files as a build
#: record, which is what a planner produces.
RECORD_KINDS = {"prompts": "prompt", "spec": "spec", "build": "build", "reviews": "review"}

#: The self-test's executed-assertion floor. A block of arms stranded past an early return is
#: exactly what a floor catches and a green line does not.
FLOOR_ASSERTIONS = 71

NEWLINE = chr(10)

_PROCESSES = [0]


class Problem(Exception):
    """A named, user-facing failure. Never a traceback, and never raised by row CONTENT."""


# ------------------------------------------------------------------------------- the process seam
def run(*argv, cwd=None) -> str:
    """One git call, counted. The liveness line prints the count, which is why it lives here."""
    _PROCESSES[0] += 1
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise Problem(f"migrate-backlog: `{' '.join(argv)}` failed: {proc.stderr.strip()}")
    return proc.stdout


def read_text(path: str) -> str:
    """`newline=""` on BOTH halves of every read in this file. A universal-newlines read rewrites a
    lone CR into a line break, which silently splits a row into two and reports neither."""
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read()


def resolve_root(start=None) -> str:
    """The repository being PLANNED: the checkout the call was made in.

    Never `__file__`'s tree. The kit is copy-installed, an adopter plans their own repo with this
    exact file, and the switch-over's landing reconcile plans a worktree of the remote tip — in both
    cases the module's own tree is a different corpus, and a planner bound to it would file a
    worksheet about somebody else's rows at exit 0.
    """
    return run("git", "rev-parse", "--show-toplevel", cwd=start or os.getcwd()).strip()


def derive_families(conf: dict) -> tuple:
    """The DECLARED family tokens, sorted. One derivation, read by the grammar and by the docs.

    THE THIRD READER OF `FAMILIES` IN THIS KIT, and that is stated rather than hidden: the
    generator splits the same key inside `collect`, and `row_grammar.derive_families` spells a
    third. They are one expression apart and can only disagree on a MALFORMED token, which is why
    this one refuses the pair shape here and hands the tokens straight to
    `backlog.build_grammar` — that function validates each family against `[A-Za-z][A-Za-z0-9]*`
    and refuses by name, and it is called before any of these tokens reaches a regex. Escaping
    instead of refusing is the shape the kit has already measured: a quoted value matches nothing
    and a value carrying a pipe swallows a subtree, both in silence.
    """
    fams = []
    for pair in conf.get("FAMILIES", "").split():
        head, sep, tail = pair.partition(":")
        if not sep or not tail:
            raise Problem(f"migrate-backlog: FAMILIES token '{pair}' is not <discipline>:<FAMILY> "
                          f"with a non-empty family, and this token goes into a regex where a "
                          f"malformed value silently re-scopes the id grammar")
        fams.append(tail)
    if not fams:
        raise Problem("migrate-backlog: FAMILIES is empty, so no row could be recognised and this "
                      "plan would certify conservation by finding nothing")
    return tuple(sorted(set(fams)))


def resolve_row_docs(root: str, conf: dict, families: tuple) -> tuple:
    """-> (live shard paths, family-archive paths), both sorted, both repo-relative.

    THE DECISION LOG AND ITS ARCHIVES ARE DELIBERATELY OUT. `row_grammar.row_docs` keeps them
    because its question is "is this a row document"; this one's question is "is this a BACKLOG row
    document", and a decision row migrates nowhere.

    The archive name is the conjunction the rest of this kit already spells — a DECLARED family
    stem, then the rotation date, then an optional same-day disambiguator — so the planner and check
    10 select the same files. A dated file that is not a family stem and a family-named file that is
    not dated are both out.
    """
    tracked = [p for p in run("git", "ls-files", "--", conf["MEMORY_ROOT"] + "/",
                              cwd=root).split("\n") if p]
    m = conf["MEMORY_ROOT"]
    stems = "|".join(re.escape(f) for f in families)
    rot = re.compile(r"(?:" + stems + r")\.[0-9]{4}-[0-9]{2}-[0-9]{2}[a-z0-9]*\.md\Z")
    live = sorted(p for p in tracked
                  if re.fullmatch(re.escape(m) + r"/backlog/(?:" + stems + r")\.md", p))
    arch = sorted(p for p in tracked
                  if p.startswith(f"{m}/archive/")
                  and "/" not in p[len(f"{m}/archive/"):]
                  and rot.match(os.path.basename(p)))
    return live, arch, tracked


# --------------------------------------------------------------------- the permissive legacy parser
Copy = collections.namedtuple("Copy", "id token withdrawn body path line raw live joined")


def parse_legacy_rows(root: str, paths: list, live_paths: set, grammar) -> tuple:
    """-> (copies, unreadable). Every logical row of every shard and archive, keyed or REPORTED.

    IT NEVER DROPS A ROW AND NEVER GUESSES A STATUS. A row-shaped line that reads as nothing comes
    back in `unreadable` with its file and line; the caller refuses on a non-empty list, because a
    skipped row makes the distinct-id count one short under a green exit and the conservation proof
    then certifies a migration that loses it.

    THE DECLARED WRAPPED ROW IS JOINED HERE, and only here. `backlog.read_legacy_row` reads ONE
    physical line by design and says so; an indented continuation beneath a row is folded onto it
    with a single space before that reader ever sees it, and the join is counted as its own
    normalization so the population is known.
    """
    copies, unreadable = [], []
    for rel in paths:
        text = read_text(os.path.join(root, rel))
        lines = [ln[:-1] if ln.endswith("\r") else ln for ln in text.split("\n")]
        logical: list = []
        for num, line in enumerate(lines, 1):
            if line.startswith("- "):
                logical.append([num, line, 0])
            elif line[:1] in (" ", "\t") and line.strip() and logical:
                logical[-1][1] += " " + line.strip()
                logical[-1][2] += 1
        for num, line, joined in logical:
            leg = backlog.read_legacy_row(line, grammar)
            if leg.id is None:
                unreadable.append((rel, num, leg.why, line.strip()))
                continue
            copies.append(Copy(leg.id, leg.status, leg.withdrawn, leg.body, rel, num, line,
                               rel in live_paths, joined))
    return copies, unreadable


def build_id_sort_key(ident: str):
    """Family, slug, then the sequence as a NUMBER. Lexical order puts `-10` before `-2`, which
    reads as data loss to anyone scanning a worksheet for the newest id."""
    parts = ident.split("-")
    seq = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0
    return (parts[0], parts[1] if len(parts) > 1 else "", seq, ident)


def read_slug(ident: str) -> str:
    """The build folder an id belongs to. An id SPELLS its build — family, slug, sequence — so the
    routing needs no side table and cannot disagree with the roster the generator derives."""
    parts = ident.split("-")
    return parts[1] if len(parts) > 2 else ""


def resolve_copy(copies: list) -> tuple:
    """One id's surviving copy, and whether the choice RECOVERED a flip. -> (Copy, recovered).

    A LIVE COPY BEATS AN ARCHIVED ONE, and among archived copies a TERMINAL one beats a
    non-terminal one. The second half is the whole reason this rule is written down rather than
    left to file order: the 2026-08-17 reconcile lost flips exactly where a non-terminal archived
    copy outranked a terminal one, and a planner that took the first copy it met would write that
    loss down a second time.
    """
    live = [c for c in copies if c.live]
    if live:
        return sorted(live, key=lambda c: (c.path, c.line))[0], False
    arch = sorted(copies, key=lambda c: (c.path, c.line))
    terminal = [c for c in arch if c.token in backlog.TERMINAL]
    if terminal and len(arch) > len(terminal):
        return terminal[0], True
    return (terminal or arch)[0], False


# --------------------------------------------------------------------------------- the history walks
History = collections.namedtuple("History", "added token_runs terminal specced")


def scan_row_history(root: str, paths: list, grammar) -> History:
    """Every row's token as history moved it — ONE git process, whatever the census size.

    A `-U0` patch walk rather than a blob walk. Reconstructing each commit's file contents would be
    one `git show` per (commit, path) and the process count would grow with the corpus; a row's
    token can only change in a commit that touches its file, so the added lines of the patch carry
    every transition there is.

    MERGES ARE READ AGAINST THEIR FIRST PARENT. A plain `--raw`/`-p` walk prints no diff for a merge
    at all, so a token a conflict RESOLUTION set would be invisible — and a resolution is exactly
    where a flip is most likely to be lost.
    """
    out = run("git", "log", "--reverse", "--format=%x01%H", "-p", "-U0", "--no-renames",
              "--diff-merges=first-parent", "--", *paths, cwd=root)
    added: dict = {}
    runs: dict = {}
    sha = ""
    for line in out.split("\n"):
        if line.startswith("\x01"):
            sha = line[1:].strip()
            continue
        if not line.startswith("+") or line.startswith("+++"):
            continue
        body = line[1:]
        if not body.startswith("- "):
            continue
        leg = backlog.read_legacy_row(body, grammar)
        if leg.id is None:
            continue
        added.setdefault(leg.id, sha)
        seq = runs.setdefault(leg.id, [])
        if not seq or seq[-1][1] != leg.status:
            seq.append((sha, leg.status))
    terminal, specced = {}, {}
    for ident, seq in runs.items():
        for pos, (sha, token) in enumerate(seq):
            if ident not in terminal and token in backlog.TERMINAL:
                terminal[ident] = sha
            if (ident not in specced and pos > 0 and token in ("SPECCED", "INPROGRESS")
                    and seq[pos - 1][1] == "OPEN"):
                specced[ident] = sha
    return History(added, runs, terminal, specced)


def scan_spec_adds(root: str, memory_root: str) -> dict:
    """path -> the sha that first ADDED it. One git process.

    A RENAMED spec file is not followed, deliberately: `--follow` takes one path and this walk takes
    the whole tree, so the choice is between one process and hundreds. A spec whose file was renamed
    simply yields no `born-in-spec-commit` evidence, which understates the class and never invents
    it — the direction an evidence report may err in.
    """
    out = run("git", "log", "--reverse", "--diff-filter=A", "--format=%x01%H", "--name-only",
              "--", f"{memory_root}/builds", cwd=root)
    adds: dict = {}
    sha = ""
    for line in out.split("\n"):
        if line.startswith("\x01"):
            sha = line[1:].strip()
            continue
        rel = line.strip()
        if rel and "/spec/" in rel:
            adds.setdefault(rel, sha)
    return adds


Commit = collections.namedtuple("Commit", "sha message outside_memory")


def scan_commit_messages(root: str, memory_root: str) -> list:
    """Every commit, its message and whether it touched anything outside the memory tree.

    ONE process over the whole history. The second field is what makes F2's ruling checkable: a
    commit that names an ask and touched only records is a commit that FILED or re-worded the row,
    not one that did the work the row asked for.
    """
    out = run("git", "log", "--reverse", "--format=%x01%H%x02%s%x02%b%x02", "--name-only",
              cwd=root)
    commits = []
    for chunk in out.split("\x01"):
        if not chunk.strip():
            continue
        head, _, tail = chunk.partition("\x02")
        subject, _, tail = tail.partition("\x02")
        body, _, names = tail.partition("\x02")
        paths = [p.strip() for p in names.split("\n") if p.strip()]
        outside = any(not p.startswith(memory_root + "/") for p in paths)
        commits.append(Commit(head.strip(), subject + "\n" + body, outside))
    return commits


# ------------------------------------------------------------------------------- the same-id sheet
def measure_overlap(row_text: str, spec_words: frozenset) -> float:
    """How much of the row's subject the spec's H1 and Goal also carry, 0.0 to 1.0.

    A HEURISTIC AND NOTHING ELSE. It is reported with its score beside the flag it sets, it moves a
    pair only toward `not-unit`, and no rule in this module reads it back.
    """
    words = {w for w in re.findall(r"[A-Za-z][A-Za-z0-9_-]+", row_text.lower())
             if w not in STOPWORDS and len(w) > 2}
    if not words or not spec_words:
        return 0.0
    return round(len(words & spec_words) / len(words), 3)


def read_spec_words(root: str, rel: str, title: str) -> frozenset:
    """The spec's H1 title plus its Goal section, as a word set. Nothing else of the body: a spec's
    scope and design mention every neighbouring id, and scoring against them would make every pair
    in a busy build look like a match."""
    try:
        text = read_text(os.path.join(root, rel))
    except OSError:
        return frozenset()
    goal: list = []
    taking = False
    for line in text.split("\n"):
        if re.match(r"^##\s", line):
            taking = bool(re.match(r"^##\s+1\.\s|^##\s+Goal", line))
            continue
        if taking:
            goal.append(line)
    blob = (title + " " + " ".join(goal)).lower()
    return frozenset(w for w in re.findall(r"[A-Za-z][A-Za-z0-9_-]+", blob)
                     if w not in STOPWORDS and len(w) > 2)


def build_same_id_sheet(root: str, chosen: dict, specs: dict, history: History,
                        spec_adds: dict) -> list:
    """One row per census id that equals a spec H1: the pair, its evidence class and the sha.

    THE PLANNER PROPOSES NOTHING HERE. Owner ruling D2 says pairing is declared and never inferred —
    four measured pairs in the originating corpus are a row and a spec about different subjects —
    so this worksheet reports what can be SHOWN and the signer decides `unit`.
    """
    rows = []
    for ident in sorted(chosen, key=build_id_sort_key):
        spec = specs.get(ident)
        if spec is None:
            continue
        copy = chosen[ident]
        evidence, sha = "none", "-"
        if copy.token in ("SPECCED", "INPROGRESS"):
            evidence = "specced-in-place"
            sha = history.specced.get(ident, history.added.get(ident, "-"))
        elif ident in history.specced:
            evidence, sha = "specced-in-place", history.specced[ident]
        elif (ident in history.added and spec_adds.get(spec["path"]) == history.added[ident]):
            evidence, sha = "born-in-spec-commit", history.added[ident]
        score = measure_overlap(copy.body, read_spec_words(root, spec["path"], spec["title"]))
        rows.append({
            "id": ident, "spec": spec["path"], "legacy": copy.token, "evidence": evidence,
            "sha": sha, "low_overlap": "yes" if score < OVERLAP_FLOOR else "no",
            "overlap": f"{score:.3f}",
        })
    return rows


# -------------------------------------------------------------------------------- the triage sheet
def check_names_id(text: str, ident: str) -> bool:
    """Does this text name THIS id, as a whole token?

    `ident in text` is the defect, and it is not theoretical: `EXMP-aBar-2` is a substring of
    `EXMP-aBar-20`, so a spec closing the twentieth ask reads as closing the second. The arm
    below caught exactly that against the first cut of this module, which is why the test is a
    function with a stated rule rather than an `in`.
    """
    return bool(re.search(r"(?<![A-Za-z0-9-])" + re.escape(ident) + r"(?![A-Za-z0-9-])", text))


#: A HOLD PHRASE, not a mention. An OPEN row naming another id is doing what every row in this
#: corpus does — citing its neighbours — and proposing a hold from a bare mention put 97 of 334
#: triage rows under a BLOCKED proposal on the first real-tree run, every one of them a citation.
#: The target still has to resolve live; this pattern is what makes the resolution mean something.
ROW_HOLD_RE = re.compile(
    r"\b(?:blocked|block|held|holds|hold|waiting|waits|depends|depend|pending|deferred|defer)\s+"
    r"(?:on|upon|until|for)\s+[`\[*]*([A-Za-z][A-Za-z0-9]*-[A-Za-z0-9]+-\d+)", re.I)


def read_row_hold(body: str, grammar, known) -> str:
    """The hold target an OPEN row's own text names, or "" when it names none that resolves.

    Deliberately NOT `read_named_hold` below. That reader answers "which id does this HOLD ROW hold
    on", where the row's own verb already established that it is a hold; this one has to establish
    that first, and a row that merely cites a neighbour is not a hold on it.
    """
    for hit in ROW_HOLD_RE.finditer(body):
        token = hit.group(1)
        if backlog.check_id(token, grammar) and token in known:
            return token
    return ""


def read_named_hold(body: str, grammar, known) -> str:
    """The id a legacy hold row names, or "" when it names none that this corpus can resolve.

    A SHORTHAND (`blocked on -4`) AND A DECISION ID BOTH COUNT AS NAMING NONE, and that is the whole
    point of resolving against `known` rather than against the id grammar alone: a hold on a token
    nothing files derives UNRESOLVED in the fold, which would land in the switch-over as a V6
    verdict instead of as the triage ask the design routes it to.
    """
    for token in re.findall(r"[A-Za-z][A-Za-z0-9]*-[A-Za-z0-9]+-\d+", body):
        if backlog.check_id(token, grammar) and token in known:
            return token
    return ""


def build_triage_sheet(chosen: dict, population: list, specs: dict, history: History,
                       commits: list, spec_bodies: dict, tracked: set, grammar, known,
                       design_named: tuple, memory_root: str) -> list:
    """One row per ask deriving OPEN on a finished build, with a PROPOSAL and the rule that made it.

    THE RULES ARE SELECTORS AND NEVER VERDICTS, in this order, first hit winning:
      `mined-closure`    a spec OTHER than the ask's same-id spec whose body carries a closing
                         phrase on the same line as the ask id. The same-id spec is excluded
                         because that is owner ruling D2's question and the triage must not answer
                         it a second way, through the back door of a sweep.
      `commit-names-ask` a commit whose message names the ask, which did not FILE its row, and
                         which touched a path outside the memory tree (fork F2 (b)). Option (a),
                         any commit naming the ask, proposes a closure for every ask there is: the
                         filing commit names every row it files.
      `row-names-hold`   the row's own text names a hold target this corpus still holds live.
      `design-named`     the id was supplied by `--design-named` and no rule above selected it.
                         Supplied by the OPTION and never by a constant: a constant would ship this
                         repo's ids inside a module every adopter runs.
    """
    rows = []
    for ident in population:
        copy = chosen[ident]
        proposal, evidence, basis = "none", "-", "none"
        for spec_id, body in spec_bodies.items():
            if spec_id == ident:
                continue
            if any(phrase in line.lower() for line in body.split(NEWLINE)
                   if check_names_id(line, ident) for phrase in CLOSING_PHRASES):
                proposal, evidence, basis = "CLOSED", spec_id, "mined-closure"
                break
        if basis == "none":
            for commit in commits:
                if not check_names_id(commit.message, ident):
                    continue
                if commit.sha == history.added.get(ident) or not commit.outside_memory:
                    continue
                proposal, evidence, basis = "CLOSED", commit.sha, "commit-names-ask"
                break
        if basis == "none":
            hold = read_row_hold(copy.body, grammar, known)
            if hold:
                proposal, evidence, basis = "BLOCKED", hold, "row-names-hold"
        if basis == "none" and ident in design_named:
            proposal, evidence, basis = "CLOSED", "-", "design-named"
        pointer = read_pointer(copy.body)
        rows.append({
            "id": ident,
            "home": f"{memory_root}/builds/{read_slug(ident)}/BACKLOG.md",
            "source": f"{copy.path}:{copy.line}",
            "legacy": copy.token,
            "derived": "OPEN",
            "proposal": proposal, "evidence": evidence, "basis": basis,
            "dead_pointer": "yes" if pointer and pointer not in tracked else "no",
        })
    return rows


def read_pointer(body: str) -> str:
    """An ask's pointer tail, unwrapped. A repo-relative path only: a pointer naming a build folder
    or a backticked path is still a pointer, and a `dead_pointer` flag over a token that was never a
    path would be noise the signer has to re-check by hand."""
    _, arrow, tail = body.rpartition(backlog.ARROW)
    if not arrow:
        return ""
    tail = tail.strip().strip("`").rstrip("/")
    return tail if re.fullmatch(r"[A-Za-z0-9._/-]+", tail or "") else ""


# ---------------------------------------------------------------- the migration's own dispositions
Disposition = collections.namedtuple("Disposition", "verb target value why mined")


def derive_dispositions(chosen: dict, history: History, grammar, known, triage_sim: str,
                        signed_triage: dict) -> dict:
    """The rows the switch-over's writer will put in the owner's folder, previewed for every id.

    A terminal legacy token becomes a terminal disposition; a hold naming a resolvable id becomes
    that hold; a hold naming none becomes a hold on the one triage ask the switch-over files. A
    SIGNED triage verdict outranks all three, because that signature is the whole point of the
    worksheet this planner files.
    """
    out: dict = {}
    for ident, copy in chosen.items():
        verdict = signed_triage.get(ident)
        if verdict:
            out[ident] = verdict
            continue
        why = copy.body.strip() or "migrated from the legacy status slot"
        if copy.token == "CLOSED":
            named = read_named_hold(copy.body.split(backlog.SEP)[0], grammar, known)
            mined = not named
            value = named or history.terminal.get(ident) or history.added.get(ident) or ""
            if not value:
                continue
            out[ident] = Disposition("CLOSED", ident, value, why, mined)
        elif copy.token == "WONTDO":
            out[ident] = Disposition("WONTDO", ident, "", why, False)
        elif copy.token in ("BLOCKED", "DEFERRED"):
            named = read_named_hold(copy.body, grammar, known)
            out[ident] = Disposition(copy.token, ident, named or triage_sim, why, False)
    return out


# ------------------------------------------------------------------ the simulated migrated corpus
def scan_archive_citations(text: str, names: frozenset) -> list:
    """Every BACKTICKED span naming a backlog archive the switch-over deletes. -> [(start, end)].

    ONE reader, two consumers: the normalization that unbackticks the span and the census finding
    that names the row. Two spellings of "is this a citation" would disagree on exactly the rows
    that are hardest to see — a `../`-relative spelling, a basename alone, a `<path>:<line>` suffix
    — and the copy that rots would be the one the switch-over is told to rewrite.
    """
    spans = []
    for hit in re.finditer(r"`([^`]+)`", text):
        token = hit.group(1).split(":")[0].strip()
        if token in names or os.path.basename(token) in names:
            spans.append((hit.start(), hit.end()))
    return spans


def render_ask_text(copy: Copy, names: frozenset, counts: dict) -> str:
    """One ask's prospective TEXT: the legacy body with the declared normalizations applied.

    The status slot is already gone (the legacy reader removed it) and the wrapped join already
    happened (the permissive parser did it); both are counted here so one place holds the tally.
    What this function performs is the two that are TEXT edits: a relative link rebased for the
    file's new depth, and a backticked citation of an archive the switch-over deletes rewritten as
    plain text.
    """
    counts["status-slot-removed"] += 1
    counts["filed-inserted"] += 1
    if copy.joined:
        counts["wrapped-row-joined"] += 1
    text = copy.body

    def render_rebase(match):
        counts["relative-link-rebased"] += 1
        return "](../" + match.group(1) + ")"

    # ONE LEVEL DEEPER. A row moves from `<M>/backlog/<FAMILY>.md` to
    # `<M>/builds/<slug>/BACKLOG.md`, so a `../` target that resolved from the shard resolves from
    # one segment further down and needs one more hop. Only `../` targets move: an absolute path, a
    # URL and a bare anchor all resolve the same from either depth.
    text = re.sub(r"\]\((\.\./[^)\s]*)\)", render_rebase, text)
    for start, end in reversed(scan_archive_citations(text, names)):
        counts["archive-citation-unbackticked"] += 1
        text = text[:start] + text[start + 1:end - 1] + text[end:]
    return text


def build_simulation(chosen: dict, dispositions: dict, units: set, names: frozenset,
                     memory_root: str, grammar, triage_sim: str, counts: dict) -> tuple:
    """The migrated corpus as `backlog.parse_file` will read it. -> (files, texts).

    ONE FILE PER SLUG, plus the file the switch-over's triage ask lands in. The ask row of every id
    is rendered by the parser unit's own renderer and the dispositions by its own row renderers, so
    a row this simulation predicts and a row the switch-over writes cannot differ in a byte that
    either module chooses.

    The third return value is the NORMALIZED text per id. A row that does not parse back has no
    entry among the parsed asks at all, and the conservation proof must REPORT that rather than
    fail to find it.
    """
    asks: dict = collections.defaultdict(list)
    rows: dict = collections.defaultdict(list)
    normalized: dict = {}
    for ident in sorted(chosen, key=build_id_sort_key):
        slug = read_slug(ident)
        text = render_ask_text(chosen[ident], names, counts)
        normalized[ident] = text
        if ident in units:
            counts["unit-inserted"] += 1
        asks[slug].append(backlog.render_ask_row(ident, FILED_PLACEHOLDER, text,
                                                 unit=ident in units))
    for ident in sorted(dispositions, key=build_id_sort_key):
        disp = dispositions[ident]
        rows[read_slug(ident)].append(
            backlog.render_status_row(disp.verb, disp.target, disp.why, disp.value))
    triage_slug = read_slug(triage_sim)
    asks[triage_slug].append(backlog.render_ask_row(
        triage_sim, FILED_PLACEHOLDER,
        "the one triage ask the switch-over files for every hold that named no id"))
    files, texts = [], {}
    for slug in sorted(set(asks) | set(rows)):
        rel = f"{memory_root}/builds/{slug}/BACKLOG.md"
        body = [f"# {slug} — asks", "", backlog.H_ASKS, ""] + asks[slug]
        if rows[slug]:
            body += ["", backlog.H_DISPOSITIONS, ""] + rows[slug]
        text = "\n".join(body) + "\n"
        texts[rel] = text
        files.append(backlog.parse_file(rel, text, grammar))
    return files, texts, normalized


def check_conservation(chosen: dict, texts_by_id: dict, units: set, grammar) -> list:
    """Render, re-parse, compare — the proof that no row's text changed in an undeclared way.

    The comparison is against the chosen legacy copy MODULO the declared normalizations, so what is
    asserted here is the half a normalization cannot explain: that the renderer and the parser agree
    about the bytes in between. Returns the offending ids; the caller refuses on a non-empty list.
    """
    bad = []
    for ident in sorted(chosen, key=build_id_sort_key):
        want = texts_by_id[ident]
        line = backlog.render_ask_row(ident, FILED_PLACEHOLDER, want, unit=ident in units)
        row = backlog.extract_row(line, grammar)
        if row is None or row.cls != "ask" or row.target != ident:
            bad.append((ident, "the rendered row does not parse back as this ask",
                        row.why if row else "no row at all"))
            continue
        got = row.why + (backlog.ARROW + row.extra["pointer"] if row.extra["pointer"] else "")
        if got != want or row.extra["unit"] != (ident in units):
            bad.append((ident, "the re-parsed text is not the normalized text", got))
    return bad


# ------------------------------------------------------------------------------ the signed records
def read_signed_record(kind: str, path: str) -> dict:
    """One signer's markdown table, located by the header cells `Ask`, `Verdict` and `Field`.

    BY CELL AND NEVER BY POSITION. The signer names its columns in prose and this module reads them
    from a file that signer wrote; a positional read would take a column somebody inserted as the
    verdict and apply it silently. A record missing a pinned cell REFUSES, naming the record and
    the cell, because a record read as all `not-unit` is a plan that quietly ignores a signature.
    """
    want = SIGNED_CELLS[kind]
    text = read_text(path)
    header, cells = None, []
    for line in text.split("\n"):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().strip("*` ") for c in line.strip().strip("|").split("|")]
        if all(w in cells for w in want):
            header = cells
            break
        if any(w in cells for w in want):
            missing = [w for w in want if w not in cells]
            raise Problem(f"migrate-backlog: the signed {kind} record {path} has a header row that "
                          f"lacks the cell(s) {' '.join(missing)}, so the planner cannot locate the "
                          f"column it must read and would report the record as unsigned")
    if header is None:
        raise Problem(f"migrate-backlog: the signed {kind} record {path} carries no header row "
                      f"holding the cells {' '.join(want)}")
    out: dict = {}
    started = False
    for line in text.split("\n"):
        if not line.strip().startswith("|"):
            continue
        row = [c.strip().strip("*` ") for c in line.strip().strip("|").split("|")]
        if row == header:
            started = True
            continue
        if not started or set("".join(row)) <= set("-: "):
            continue
        if len(row) != len(header):
            continue
        out[row[header.index("Ask")]] = {w: row[header.index(w)] for w in want}
    return out


def read_signed_verdicts(signed: dict) -> tuple:
    """-> (units, triage dispositions). The two signatures, turned into the shapes the fold reads."""
    units, triage = set(), {}
    for ask, cells in (signed.get("same-id") or {}).items():
        if cells["Verdict"] == "unit":
            units.add(ask)
    for ask, cells in (signed.get("triage") or {}).items():
        verb, field = cells["Verdict"], cells["Field"]
        if verb == "KEEP":
            continue
        if verb not in backlog.STATUS_VERBS:
            raise Problem(f"migrate-backlog: the signed triage record gives {ask} the verdict "
                          f"`{verb}`, which is not one of: {' '.join(backlog.STATUS_VERBS)}")
        if verb in ("CLOSED", "BLOCKED", "DEFERRED") and (not field or field == "-"):
            raise Problem(f"migrate-backlog: the signed triage record gives {ask} a `{verb}` "
                          f"verdict with no Field value, and a {verb} row needs one")
        triage[ask] = Disposition(verb, ask, "" if verb == "WONTDO" else field,
                                  "signed triage verdict", False)
    return units, triage


# ---------------------------------------------------------------------------------- the status sheet
def derive_status_class(ident: str, legacy: str, predicted: str, chosen: dict, specs: dict,
                        units: set, signed_triage: dict, dispositions: dict,
                        recovered: set) -> str:
    """Which of the seven declared classes this id's prediction falls in.

    ORDERED, FIRST MATCH WINNING, and total by construction — the last branch is `same` and the two
    branches above it cover every remaining difference. Three of the seven are REPORTED even where
    the prediction agrees with the legacy token, because each is a provenance signal the signer
    needs: a recovered flip, a mined closure and a signed pairing are all things that happened TO
    this id, not merely differences in its status.
    """
    if ident in signed_triage:
        return "triaged"
    if ident in units:
        return "mirror-closed"
    if ident in recovered:
        return "recovered-flip"
    if predicted != legacy:
        if ident in specs:
            return "collision-kept-live"
        return "stale-spec"
    disp = dispositions.get(ident)
    if disp is not None and disp.mined:
        return "mined-closure"
    return "same"


def build_status_sheet(chosen: dict, fold, specs: dict, units: set, signed_triage: dict,
                       dispositions: dict, recovered: set, triage_sim: str) -> list:
    """Every census id: its legacy token, the status the fold predicts, the class and what decided."""
    rows = []
    for ident in sorted(chosen, key=build_id_sort_key):
        predicted = fold.statuses.get(ident, backlog.UNRESOLVED)
        decided = fold.decided.get(ident) or "-"
        rows.append({
            "id": ident,
            "legacy": chosen[ident].token,
            "predicted": predicted,
            "class": derive_status_class(ident, chosen[ident].token, predicted, chosen, specs,
                                         units, signed_triage, dispositions, recovered),
            "decided_by": TRIAGE_ASK if decided == triage_sim else decided,
        })
    return rows


# ----------------------------------------------------------------------------------- the records
def render_worksheet(kind: str, columns: tuple, rows: list, unit_id: str, head: str) -> str:
    """One TAB-separated worksheet: a Serves line, the provenance line, the header, rows, a total.

    NO DATA ROW LEADS WITH AN ID IN A LIST OR TABLE SHAPE. A TSV row does not, which is why these
    are TSV: a markdown table whose first cell is an id ANCHORS that id, and a worksheet listing
    every ask in the corpus would then claim every one of them in this build's folder.
    """
    out = [f"# **Serves:** journal {unit_id}",
           f"# {kind} worksheet · computed at {head}",
           "\t".join(columns)]
    for row in rows:
        out.append("\t".join(str(row[c]) for c in columns))
    out.append(f"examined\t{len(rows)}")
    return "\n".join(out) + "\n"


def render_census(unit_id: str, head: str, summary: dict) -> str:
    """The census, as markdown prose. Deliberately NOT a table keyed on ids, for the reason above."""
    out = [f"**Serves:** journal {unit_id}", "",
           f"# The backlog migration census — {unit_id}", "",
           f"Computed by `migrate_backlog.py --plan` at {head}. Every figure below is DERIVED at "
           f"run time; none of them is authored anywhere, here or in a spec.", ""]
    out.append("## The corpus")
    out.append("")
    for line in summary["corpus"]:
        out.append(f"- {line}")
    out.append("")
    out.append("## Findings the switch-over's commit must absorb")
    out.append("")
    for heading, lines in summary["findings"]:
        out.append(f"### {heading}")
        out.append("")
        out += ([f"- {x}" for x in lines] or ["- none."])
        out.append("")
    out.append("## The conservation proof")
    out.append("")
    for line in summary["conservation"]:
        out.append(f"- {line}")
    out.append("")
    return "\n".join(out)


def write_records(root: str, record_dir: str, unit_id: str, day: str, head: str,
                  sheets: dict, summary: dict) -> list:
    """The four records, named by the recording grammar and dated by HEAD's COMMIT day.

    NEVER THE CLOCK. Two runs over one tree must write byte-identical records or the signer's
    signature stops meaning anything, and a wall-clock stamp is the one field that cannot hold.
    """
    kind = RECORD_KINDS.get(os.path.basename(record_dir.rstrip("/\\")), "build")
    target = record_dir if os.path.isabs(record_dir) else os.path.join(root, record_dir)
    os.makedirs(target, exist_ok=True)
    written = []
    files = [(f"{day}-{kind}-{unit_id}-census.md", render_census(unit_id, head, summary))]
    for name, columns in (("same-id", SAME_ID_COLUMNS), ("triage", TRIAGE_COLUMNS),
                          ("status", STATUS_COLUMNS)):
        files.append((f"{day}-{kind}-{unit_id}-{name}.tsv",
                      render_worksheet(name, columns, sheets[name], unit_id, head)))
    for name, text in files:
        dest = os.path.join(target, name)
        with open(dest, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        written.append(dest)
    return written


# ------------------------------------------------------------------------------------- the planner
Plan = collections.namedtuple("Plan", "sheets summary counts head day census normalized")


def read_index(fn, *argv):
    """One seam onto the generator, re-raising its failure as this file's own named one.

    `collect` is reached through a single call site here and an unfamiliar exception class at it is
    a traceback rather than the named line every refusal in this module promises.
    """
    try:
        return fn(*argv)
    except index.Problem as exc:
        raise Problem(f"migrate-backlog: {exc}") from None


def build_plan(root: str, design_named=(), signed=None) -> Plan:
    """The whole read-only pass. Raises `Problem` on every refusal; writes nothing."""
    conf = read_index(index.load_conf, root)
    memory_root = conf["MEMORY_ROOT"]
    families = derive_families(conf)
    grammar = backlog.build_grammar(families)
    live_paths, archive_paths, tracked = resolve_row_docs(root, conf, families)
    if not live_paths and not archive_paths:
        raise Problem(
            f"migrate-backlog: {memory_root}/backlog/ holds no shard for any declared family and "
            f"{memory_root}/archive/ holds no family archive, so this plan would prove conservation "
            f"over an empty corpus — which proves nothing and looks exactly like a clean run")

    copies, unreadable = parse_legacy_rows(root, live_paths + archive_paths, set(live_paths),
                                           grammar)
    if unreadable:
        lines = "\n".join(f"  {p}:{n}: {why} — {text[:80]}" for p, n, why, text in unreadable)
        raise Problem(f"migrate-backlog: {len(unreadable)} row-shaped line(s) read as nothing, and "
                      f"a row this planner cannot key is a row the migration would silently drop:\n"
                      f"{lines}")
    if not copies:
        raise Problem("migrate-backlog: the shards and archives hold no row copy at all, so the "
                      "conservation proof would hold trivially")

    by_id: dict = collections.defaultdict(list)
    for copy in copies:
        by_id[copy.id].append(copy)
    twolive = {i: [c for c in cs if c.live] for i, cs in by_id.items()
               if len([c for c in cs if c.live]) > 1}
    if twolive:
        lines = "\n".join(
            f"  {i}: " + " and ".join(f"{c.path}:{c.line}" for c in sorted(cs, key=lambda c: c.path))
            for i, cs in sorted(twolive.items()))
        raise Problem(f"migrate-backlog: {len(twolive)} id(s) carry TWO live copies, and "
                      f"conservation would need two asks for one id:\n{lines}")

    chosen, recovered = {}, set()
    for ident, cs in by_id.items():
        pick, flipped = resolve_copy(cs)
        chosen[ident] = pick
        if flipped:
            recovered.add(ident)

    builds = read_index(index.collect, root, conf)
    specs: dict = {}
    for build in builds:
        for unit in build["units"]:
            rel = os.path.relpath(unit["path"], root).replace("\\", "/")
            specs[unit["id"]] = {"path": rel, "status": unit["status"], "title": unit["title"]}
    build_status = {b["slug"]: b["status"] for b in builds}

    history = scan_row_history(root, live_paths + archive_paths, grammar)
    spec_adds = scan_spec_adds(root, memory_root)
    commits = scan_commit_messages(root, memory_root)

    triage_sim = f"{families[0]}-{TRIAGE_SIM_SLUG}-1"
    if triage_sim in chosen:
        raise Problem(f"migrate-backlog: {triage_sim} is a real ask in this corpus, and this module "
                      f"needs that id as the stand-in for the triage ask the switch-over files")

    signed = signed or {}
    units, signed_triage = read_signed_verdicts(signed)
    known = set(chosen) | set(specs) | {triage_sim}

    archive_names = frozenset(archive_paths) | {os.path.basename(p) for p in archive_paths}
    counts = {k: 0 for k in NORMALIZATIONS}

    # THE TRIAGE POPULATION IS COMPUTED UNDER OWNER RULING D2's DEFAULT — no `unit` at all, a
    # superset (fork F1 (a)). An ask the signer later links and whose spec is CLOSED simply derives
    # CLOSED, and a triage KEEP on it is inert; the other way round, a planner guessing `unit` makes
    # a verdict it may not make and shortens the sweep on its own authority.
    plain_disp = derive_dispositions(chosen, history, grammar, known, triage_sim, {})
    plain_files, _, _ = build_simulation(chosen, plain_disp, set(), archive_names, memory_root,
                                         grammar, triage_sim, dict(counts))
    plain_fold = backlog.derive_statuses(backlog.build_corpus(plain_files, {}, build_status))
    population = [i for i in sorted(chosen, key=build_id_sort_key)
                  if plain_fold.statuses.get(i) == "OPEN"
                  and build_status.get(read_slug(i)) in backlog.TERMINAL]

    outside = [i for i in design_named if i not in population]
    if outside:
        raise Problem(f"migrate-backlog: --design-named names {' '.join(sorted(outside))}, which "
                      f"is outside the triage population, so the worksheet would carry a proposal "
                      f"for a row it does not list")

    spec_bodies = {}
    for ident, spec in specs.items():
        try:
            spec_bodies[ident] = read_text(os.path.join(root, spec["path"]))
        except OSError:
            spec_bodies[ident] = ""

    triage_rows = build_triage_sheet(chosen, population, specs, history, commits, spec_bodies,
                                     set(tracked), grammar, known, tuple(design_named),
                                     memory_root)

    dispositions = derive_dispositions(chosen, history, grammar, known, triage_sim, signed_triage)
    files, texts, normalized = build_simulation(chosen, dispositions, units, archive_names,
                                                memory_root, grammar, triage_sim, counts)
    fold = backlog.derive_statuses(backlog.build_corpus(files, build_spec_index(specs), build_status))

    bad = check_conservation(chosen, normalized, units, grammar)
    if bad:
        lines = "\n".join(f"  {i}: {why} — {got[:90]}" for i, why, got in bad)
        raise Problem(f"migrate-backlog: {len(bad)} row(s) differ from their chosen legacy copy in "
                      f"a way no declared normalization explains:\n{lines}")

    same_rows = build_same_id_sheet(root, chosen, specs, history, spec_adds)
    status_rows = build_status_sheet(chosen, fold, specs, units, signed_triage, dispositions,
                                     recovered, triage_sim)

    summary = build_summary(conf, chosen, live_paths, archive_names, len(archive_paths), copies,
                            specs, build_status, same_rows, triage_rows, fold, texts, counts,
                            families, memory_root, root)
    head = run("git", "rev-parse", "HEAD", cwd=root).strip()
    day = run("git", "show", "-s", "--format=%cd", "--date=format:%Y-%m-%d", "HEAD",
              cwd=root).strip()
    headline = (f"{head} · signed "
                f"{'+'.join(sorted(signed)) if signed else 'none'} · design-named "
                f"{' '.join(sorted(design_named)) if design_named else 'none'}")
    sheets = {"same-id": same_rows, "triage": triage_rows, "status": status_rows}
    return Plan(sheets, summary, counts, headline, day, chosen, normalized)


def build_spec_index(specs: dict) -> dict:
    """The spec index in the shape the fold reads: id -> `backlog.Spec`.

    The two backlog header verbs come from the generator's own parse and are deliberately NOT
    re-read here; today no spec in a shards-mode corpus carries either, and a second reader of them
    would be a second answer the day one does.
    """
    return {i: backlog.Spec(i, s["path"], s["status"], (), ()) for i, s in specs.items()}


def build_summary(conf, chosen, live_paths, archive_names, archive_count, copies, specs,
                  build_status, same_rows, triage_rows, fold, texts, counts, families,
                  memory_root, root) -> dict:
    """Every derived figure the census prints, and the three findings the switch-over must absorb."""
    tracked = set(run("git", "ls-files", "--", memory_root + "/", cwd=root).split("\n"))
    slugs = sorted({read_slug(i) for i in chosen})
    homeless = [s for s in slugs if f"{memory_root}/builds/{s}/README.md" not in tracked]
    # A BLANK OR UNUSABLE CAP DISARMS THIS PROBE, so it says so rather than reporting zero. A
    # cap of "" read as 0 makes every comparison false and the finding prints `none`, which is the
    # same bytes a tree with nothing over cap prints — a reassuring zero from a signal that cannot
    # move. The hygiene engine REFUSES on the same value; this is a report, so it reports.
    cap_raw = (conf.get("INDEX_CAP_BYTES") or "").strip()
    cap = int(cap_raw) if cap_raw.isdigit() and int(cap_raw) > 0 else 0
    sizes = {}
    for rel, text in texts.items():
        sizes[rel] = len(text.encode("utf-8"))
    over = sorted((rel, n) for rel, n in sizes.items() if cap and n > cap)

    views = {}
    asks = [a for rel, text in sorted(texts.items())
            for a in backlog.parse_file(rel, text,
                                        backlog.build_grammar(families)).asks]
    kit = index.kit_rel()
    for family in families:
        views[family] = len(backlog.render_family_view(
            family, asks, fold, memory_root, kit, index.GEN_HEADER,
            backlog.read_excerpt_chars(conf)).encode("utf-8"))

    citations = []
    for ident in sorted(chosen, key=build_id_sort_key):
        copy = chosen[ident]
        spans = scan_archive_citations(copy.body, archive_names)
        if spans:
            cited = " and ".join(sorted({copy.body[a + 1:b - 1] for a, b in spans}))
            citations.append(f"{copy.path}:{copy.line} cites {cited}")

    corpus = [
        f"{len(copies)} row copies over {len(live_paths)} live shard(s) and "
        f"{archive_count} family archive(s); {len(chosen)} distinct ids.",
        f"{sum(1 for c in copies if c.live)} live copies and "
        f"{sum(1 for c in copies if not c.live)} archived ones.",
        f"{len(slugs)} slugs own rows; {len(same_rows)} ids equal a spec H1.",
        f"{len(triage_rows)} ask(s) derive OPEN on a build whose derived status is terminal, over "
        f"{len({read_slug(r['id']) for r in triage_rows})} such build(s).",
        "prospective family view sizes, in bytes, uncapped by owner ruling D3: "
        + " · ".join(f"{f} {views[f]}" for f in families) + ".",
        f"{len([b for b in build_status.values() if b in backlog.TERMINAL])} of "
        f"{len(build_status)} indexed builds are terminal.",
    ]
    findings = [
        ("Prospective ask files over the declared row cap",
         [f"{rel} would be {n} bytes against INDEX_CAP_BYTES of {cap}" for rel, n in over]
         if cap else
         [f"DEAD PROBE — INDEX_CAP_BYTES is '{cap_raw}', not a positive whole number, so no "
          f"prospective ask file can be over cap and this finding's silence means nothing"]),
        ("Slugs owning rows with no build README — the prospective filing homes",
         [f"slug {s} owns rows and has no tracked README" for s in homeless]),
        (f"Rows whose text cites a backlog archive the switch-over deletes — "
         f"{counts['archive-citation-unbackticked']} backticked citation(s), the population unit "
         f"34's fifth normalization rewrites",
         citations),
    ]
    conservation = [f"{name}: {counts[name]}" for name in NORMALIZATIONS]
    conservation.append(
        f"every one of the {len(chosen)} prospective ask rows re-parsed to its own id and its own "
        f"normalized text; no other difference was found.")
    return {"corpus": corpus, "findings": findings, "conservation": conservation,
            "views": views, "over": over, "homeless": homeless, "citations": citations,
            "sizes": sizes}


def print_plan(plan: Plan) -> None:
    """The census summary and the liveness line. Every count is derived; none is authored."""
    for line in plan.summary["corpus"]:
        print(f"migrate-backlog: {line}")
    for heading, lines in plan.summary["findings"]:
        print(f"migrate-backlog: {heading}: {len(lines)}")
        for line in lines:
            print(f"migrate-backlog:   {line}")
    for line in plan.summary["conservation"]:
        print(f"migrate-backlog: conservation · {line}")
    print(f"migrate-backlog: worksheets · same-id {len(plan.sheets['same-id'])} · "
          f"triage {len(plan.sheets['triage'])} · status {len(plan.sheets['status'])} rows · "
          f"{_PROCESSES[0]} git process(es) spent")


def cmd_plan(root: str, args: dict) -> int:
    signed = {}
    for kind, path in args["signed"]:
        signed[kind] = read_signed_record(kind, path)
    plan = build_plan(root, design_named=tuple(args["design_named"]), signed=signed)
    print_plan(plan)
    if args["record"]:
        if not args["record_as"]:
            raise Problem("migrate-backlog: --record needs --record-as <unit-id>, because every "
                          "record this planner files carries a Serves line naming the unit it "
                          "serves and a filename built from that id")
        written = write_records(root, args["record"], args["record_as"], plan.day, plan.head,
                                plan.sheets, plan.summary)
        for dest in written:
            print(f"migrate-backlog: wrote {os.path.basename(dest)}")
    return 0


# ----------------------------------------------------------------------------------- the self-test
def write_file(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def render_conf(cap: str = "61440") -> str:
    return ("MEMORY_ROOT=memory\n"
            'DISCIPLINES="one two"\n'
            'FAMILIES="one:EXMP two:OTHR"\n'
            f'INDEX_CAP_BYTES="{cap}"\n'
            'INDEX_CAP_LINES="0"\n')


def render_readme(slug: str, status: str = "", ids: str = "") -> str:
    head = ["---", f"slug: {slug}", "node: a", "opened: 2026-01-01", "streams: one",
            "roster: EXMP", f"ids: {ids}"]
    if status:
        head.append(f"status: {status}")
    head += ["---", "", f"# {slug}", "", "A fixture build.", ""]
    return "\n".join(head)


def render_spec(ident: str, status: str, title: str, goal: str = "a goal", body: str = "") -> str:
    return (f"# {ident} — {title}\n\n"
            f"**Status:** {status} · rev-1 · 2026-01-01 · node a · Tier-1 · base 0123abcd\n\n"
            f"## 1. Goal\n\n{goal}\n\n## 2. Scope (IN)\n\n{body}\n")


def run_commit(tmp: str, message: str, files: dict) -> str:
    for rel, text in files.items():
        write_file(os.path.join(tmp, rel), text)
    run("git", "add", "-A", cwd=tmp)
    run("git", "commit", "-q", "-m", message, "--no-verify", cwd=tmp)
    return run("git", "rev-parse", "HEAD", cwd=tmp).strip()


def init_repo(tmp: str) -> None:
    os.makedirs(tmp, exist_ok=True)
    run("git", "init", "-q", "-b", "main", ".", cwd=tmp)
    run("git", "config", "user.email", "t@t.test", cwd=tmp)
    run("git", "config", "user.name", "t", cwd=tmp)
    run("git", "config", "commit.gpgsign", "false", cwd=tmp)
    # HERMETIC AGAINST THIS MACHINE'S GLOBAL CONFIG. `core.autocrlf` is a user-global setting on
    # every Windows node here, and it decides what the fixture's own shards look like on disk —
    # so an arm counting rows would be grading the checkout convention rather than the parser.
    run("git", "config", "core.autocrlf", "false", cwd=tmp)


WAIVER = "# no waived header" + chr(10)

_SHARD_HEAD = "# {family} backlog\n\n> Mutable.\n"


def render_shard(family: str, rows: list) -> str:
    return _SHARD_HEAD.format(family=family) + "\n".join(rows) + "\n"


def seed_corpus(tmp: str) -> None:
    """The shared fixture: one repo with real history, holding one case per selector and refusal."""
    init_repo(tmp)
    seed_rows = [
        "- EXMP-aFoo-1 · OPEN · a planner module that reads legacy rows and reports evidence",
        "- EXMP-aFoo-2 · OPEN · an ask nothing in this corpus closes",
        "- EXMP-aFoo-3 · BLOCKED · held until EXMP-aFoo-2 lands, and then it can move",
        "- EXMP-aFoo-4 · BLOCKED · blocked on -4 and -11, shorthand the corpus cannot resolve",
        "- EXMP-aFoo-5 · DEFERRED · only on the owner's word, naming nothing",
        "- EXMP-aFoo-6 · CLOSED · a terminal row carrying its own reason",
        "- EXMP-aFoo-7 · WONTDO · declined, and here is the reason it was declined",
        "- EXMP-aFoo-8 · BLOCKED · blocked on EXMP-dRuling-9, a decision id nothing files",
        "- EXMP-aFoo-9 · OPEN · a row whose text wraps",
        "  across a second physical line",
        "- EXMP-aBar-1 · OPEN · a bowl of custard needing a sibling spec to absorb it",
        "- EXMP-aBar-2 · OPEN · a lantern a product commit names when it finishes the work",
        "- EXMP-aBar-3 · OPEN · a pointer that goes nowhere → memory/gone/nowhere.md",
        "- EXMP-aBar-4 · OPEN · marmalade windmills grinding pewter thimbles nightly",
        "- EXMP-aBar-5 · OPEN · a trellis, blocked on EXMP-aFoo-2 for the moment",
        "- EXMP-aBar-6 · CLOSED · a closed ask sitting on a finished build",
        "- EXMP-aBar-7 · OPEN · the first design-named closure with no evidence anywhere",
        "- EXMP-aBar-8 · OPEN · the second design-named closure with no evidence anywhere",
        "- EXMP-aBar-9 · OPEN · the third design-named closure with no evidence anywhere",
        "- EXMP-aBar-10 · OPEN · an ask only its own filing commit ever names",
        "- EXMP-aBar-11 · OPEN · an ask only a records-only commit ever names",
        "- EXMP-aBar-12 · OPEN · the rest of it is in `memory/archive/EXMP.2026-01-01.md` still",
        "- EXMP-aBar-13 · OPEN · see [the archive](../archive/EXMP.2026-01-01.md) for the rest",
        "- EXMP-aLoose-1 · OPEN · a row whose slug has no build folder at all",
        "- OTHR-aBaz-1 · OPEN · a row in the second declared family",
    ]
    arch_one = ["- EXMP-aOld-1 · CLOSED · an archived terminal copy of a flipped row",
                "- EXMP-aOld-3 · CLOSED · an archived TERMINAL copy that loses to the live one"]
    arch_two = ["- EXMP-aOld-1 · OPEN · the archived copy that lost the flip",
                "- EXMP-aOld-2 · CLOSED · an id only the second archive carries"]
    run_commit(tmp, "seed: file EXMP-aBar-10 and the rest of the corpus", {
        ".memory-tree.conf": render_conf(),
        "README.md": "fixture\n",
        "memory/backlog/EXMP.md": render_shard("EXMP", seed_rows),
        "memory/backlog/OTHR.md": render_shard("OTHR", []),
        "memory/archive/EXMP.2026-01-01.md": render_shard("EXMP", arch_one),
        "memory/archive/EXMP.2026-01-02.md": render_shard("EXMP", arch_two),
        "memory/project/stale-header-waiver.txt": WAIVER,
        "memory/builds/aFoo/README.md": render_readme("aFoo"),
        "memory/builds/aBar/README.md": render_readme("aBar"),
        "memory/builds/aBaz/README.md": render_readme("aBaz", status="OPEN"),
        "memory/builds/aOld/README.md": render_readme("aOld", status="CLOSED"),
        "memory/builds/aFoo/spec/2026-01-01-spec-EXMP-aFoo-1.md": render_spec(
            "EXMP-aFoo-1", "OPEN", "a planner module",
            "reads legacy rows and reports evidence about them"),
    })
    # EXMP-aOld-3's live copy, which must beat the archived one.
    run_commit(tmp, "records: the live copy of EXMP-aOld-3", {
        "memory/backlog/EXMP.md": render_shard("EXMP", seed_rows + [
            "- EXMP-aOld-3 · OPEN · the live copy, which outranks the archived one"]),
    })
    # The OPEN -> SPECCED flip, in history, for the specced-in-place evidence class.
    rows = seed_rows + ["- EXMP-aOld-3 · OPEN · the live copy, which outranks the archived one"]
    rows[0] = "- EXMP-aFoo-1 · SPECCED · a planner module that reads legacy rows and reports evidence"
    run_commit(tmp, "records: EXMP-aFoo-1 is specced", {"memory/backlog/EXMP.md": render_shard("EXMP", rows)})
    # A row born in its own spec's commit, and the two specs the triage reads.
    rows = rows + ["- EXMP-aBar-30 · OPEN · a pewter thimble ground by marmalade windmills"]
    run_commit(tmp, "records: born with its spec", {
        "memory/backlog/EXMP.md": render_shard("EXMP", rows),
        "memory/builds/aBar/spec/2026-01-01-spec-EXMP-aBar-30.md": render_spec(
            "EXMP-aBar-30", "CLOSED", "pewter thimbles ground by marmalade windmills",
            "grind pewter thimbles with marmalade windmills"),
    })
    run_commit(tmp, "records: the same-id spec of EXMP-aBar-4, added on its own", {
        "memory/builds/aBar/spec/2026-01-01-spec-EXMP-aBar-4.md": render_spec(
            "EXMP-aBar-4", "CLOSED", "an entirely different subject",
            "resolve python launchers across operating systems",
            "This unit absorbs EXMP-aBar-4, which owner ruling D2 does not let a sweep read."),
        "memory/builds/aBar/spec/2026-01-01-spec-EXMP-aBar-20.md": render_spec(
            "EXMP-aBar-20", "CLOSED", "the sibling that absorbs a custard bowl",
            "absorb the custard", "This unit absorbs EXMP-aBar-1 whole."),
    })
    run_commit(tmp, "product: finish the lantern of EXMP-aBar-2", {"src/lantern.txt": "done\n"})
    run_commit(tmp, "records: mention EXMP-aBar-11 and touch nothing else",
            {"memory/builds/aBar/NOTES.md": "EXMP-aBar-11 was discussed\n"})
    # THE TIP ROW. The second worktree below sits one commit back and therefore holds one row
    # fewer, which is the only way an arm can tell "read the call's repo" from "read a repo".
    run_commit(tmp, "records: one more row, only at the tip", {
        "memory/backlog/OTHR.md": render_shard("OTHR", [
            "- OTHR-aBaz-9 · OPEN · a row only the tip commit carries"])})


def run_plan(tmp: str, **kw):
    buf = io.StringIO()
    with redirect_stdout(buf):
        plan = build_plan(tmp, **kw)
    return plan


def read_sheet_row(plan, kind: str, ident: str) -> dict:
    for row in plan.sheets[kind]:
        if row["id"] == ident:
            return row
    return {}


def cmd_selftest() -> int:  # noqa: C901 — one arm list, deliberately flat and readable
    import shutil
    import tempfile

    fails, count = [], [0]

    def arm(label: str, want, fn):
        count[0] += 1
        try:
            got = fn()
        except Problem as exc:
            got = f"PROBLEM {exc}"
        except Exception as exc:                      # noqa: BLE001 — a traceback here IS the finding
            got = f"UNEXPECTED {type(exc).__name__}: {exc}"
        if str(want) in str(got):
            print(f"arm ok    {label}")
        else:
            fails.append(label)
            print(f"arm FAIL  {label}\n      expected to see: {want}\n      got: {got}")

    base = tempfile.mkdtemp(prefix="migplan")
    try:
        main_tree = os.path.join(base, "corpus")
        seed_corpus(main_tree)
        plan = run_plan(main_tree)

        # ---- AC1: the census reads every copy, joins the wrapped row, prefers the live copy.
        arm("the census counts every row copy across shards and archives",
            "31 row copies", lambda: plan.summary["corpus"][0])
        arm("the wrapped row is joined onto one logical row",
            "a row whose text wraps across a second physical line",
            lambda: plan.census["EXMP-aFoo-9"].body)
        arm("the wrapped-row join is counted as its own normalization",
            1, lambda: plan.counts["wrapped-row-joined"])
        arm("a relative link is rebased for the ask file's new depth, and counted",
            1, lambda: plan.counts["relative-link-rebased"])
        arm("the rebased link gained exactly one hop",
            "](../../archive/EXMP.2026-01-01.md)",
            lambda: plan.normalized["EXMP-aBar-13"])
        arm("a backticked archive citation is unbackticked, and counted",
            1, lambda: plan.counts["archive-citation-unbackticked"])
        arm("a live copy beats an archived one, even a TERMINAL archived one",
            "OPEN", lambda: plan.census["EXMP-aOld-3"].token)
        arm("among archived copies a terminal one beats a non-terminal one",
            "CLOSED", lambda: plan.census["EXMP-aOld-1"].token)
        arm("that recovered flip is reported as its own status class",
            "recovered-flip", lambda: read_sheet_row(plan, "status", "EXMP-aOld-1")["class"])

        # The same pair in the opposite file order still resolves to the terminal copy.
        flipped = os.path.join(base, "flipped")
        init_repo(flipped)
        run_commit(flipped, "seed", {
            ".memory-tree.conf": render_conf(),
            "memory/project/stale-header-waiver.txt": WAIVER,
            "memory/backlog/EXMP.md": render_shard("EXMP", ["- EXMP-aFoo-1 · OPEN · a live row"]),
            "memory/archive/EXMP.2026-01-01.md": render_shard(
                "EXMP", ["- EXMP-aOld-1 · OPEN · the non-terminal copy, first by file order"]),
            "memory/archive/EXMP.2026-01-02.md": render_shard(
                "EXMP", ["- EXMP-aOld-1 · CLOSED · the terminal copy, second by file order"]),
            "memory/builds/aFoo/README.md": render_readme("aFoo", status="OPEN"),
            "memory/builds/aOld/README.md": render_readme("aOld", status="CLOSED"),
        })
        arm("the archived terminal copy wins under the other file order too",
            "CLOSED", lambda: run_plan(flipped).census["EXMP-aOld-1"].token)

        # ---- AC1 negative: one row-shaped line that reads as nothing refuses the whole plan.
        broken = os.path.join(base, "broken")
        shutil.copytree(main_tree, broken)
        run_commit(broken, "records: a line that reads as nothing", {
            "memory/backlog/OTHR.md": render_shard("OTHR", ["- not an id at all · OPEN · nothing keys"]),
        })
        arm("a row-shaped line that reads as nothing refuses, naming its file and line",
            "read as nothing", lambda: run_plan(broken))
        arm("with the file and the line it sits on",
            "memory/backlog/OTHR.md:4:", lambda: run_plan(broken))
        arm("that refusal says a dropped row is what it is preventing",
            "silently drop", lambda: run_plan(broken))
        arm("and no worksheet is written for it",
            False, lambda: os.path.isdir(os.path.join(broken, "out")))

        # ---- AC2: two live copies of one id are a blocker.
        dupe = os.path.join(base, "dupe")
        shutil.copytree(main_tree, dupe)
        run_commit(dupe, "records: a second live copy", {
            "memory/backlog/OTHR.md": render_shard(
                "OTHR", ["- OTHR-aBaz-1 · OPEN · the second live copy of one id"]),
        })
        arm("two live copies of one id refuse by name",
            "carry TWO live copies", lambda: run_plan(dupe))
        arm("naming both files",
            "and memory/backlog/OTHR.md:", lambda: run_plan(dupe))

        # ---- AC13: an empty corpus refuses rather than certifying conservation over nothing.
        empty = os.path.join(base, "empty")
        init_repo(empty)
        run_commit(empty, "seed", {
            ".memory-tree.conf": render_conf(),
            "memory/project/stale-header-waiver.txt": WAIVER,
            "memory/builds/aFoo/README.md": render_readme("aFoo", status="OPEN")})
        arm("a corpus with no shard and no family archive refuses by name",
            "proves nothing", lambda: run_plan(empty))

        # ---- AC3: the three evidence classes, their shas, and the overlap flag.
        arm("a row flipped OPEN to SPECCED in history reads specced-in-place",
            "specced-in-place", lambda: read_sheet_row(plan, "same-id", "EXMP-aFoo-1")["evidence"])
        arm("its showing sha is a real commit",
            True, lambda: len(read_sheet_row(plan, "same-id", "EXMP-aFoo-1")["sha"]) == 40)
        arm("a row added in its same-id spec's own commit reads born-in-spec-commit",
            "born-in-spec-commit", lambda: read_sheet_row(plan, "same-id", "EXMP-aBar-30")["evidence"])
        arm("its showing sha is a real commit too",
            True, lambda: len(read_sheet_row(plan, "same-id", "EXMP-aBar-30")["sha"]) == 40)
        arm("a pair with neither reads none",
            "none", lambda: read_sheet_row(plan, "same-id", "EXMP-aBar-4")["evidence"])
        arm("and carries no sha",
            "-", lambda: read_sheet_row(plan, "same-id", "EXMP-aBar-4")["sha"])
        arm("a pair sharing no words with its spec's H1 and Goal is flagged low-overlap",
            "yes", lambda: read_sheet_row(plan, "same-id", "EXMP-aBar-4")["low_overlap"])
        arm("the flag carries the score that set it",
            "0.000", lambda: read_sheet_row(plan, "same-id", "EXMP-aBar-4")["overlap"])
        arm("a matching pair is not flagged",
            "no", lambda: read_sheet_row(plan, "same-id", "EXMP-aBar-30")["low_overlap"])

        # ---- AC4: the triage population and every proposal rule.
        arm("an ask another spec's body closes is proposed CLOSED by that spec",
            "EXMP-aBar-20", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-1")["evidence"])
        arm("with the mined-closure basis",
            "mined-closure", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-1")["basis"])
        arm("an ask a product commit names is proposed CLOSED by that commit",
            "commit-names-ask", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-2")["basis"])
        arm("an ask whose pointer path is untracked carries the dead-pointer flag",
            "yes", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-3")["dead_pointer"])
        arm("and is proposed nothing",
            "none", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-3")["basis"])
        arm("an ask whose same-id spec reads CLOSED is proposed nothing",
            "none", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-4")["basis"])
        arm("an ask named only by the commit that filed it is proposed nothing",
            "none", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-10")["basis"])
        arm("an ask named only by a records-only commit is proposed nothing",
            "none", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-11")["basis"])
        arm("an ask whose row names a live hold proposes that hold",
            "row-names-hold", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-5")["basis"])
        arm("naming the target it holds on",
            "EXMP-aFoo-2", lambda: read_sheet_row(plan, "triage", "EXMP-aBar-5")["evidence"])
        arm("a CLOSED ask on a finished build is absent from the triage worksheet",
            {}, lambda: read_sheet_row(plan, "triage", "EXMP-aBar-6"))
        named = ("EXMP-aBar-7", "EXMP-aBar-8", "EXMP-aBar-9")
        arm("without the option no row reads design-named",
            0, lambda: len([r for r in plan.sheets["triage"] if r["basis"] == "design-named"]))
        arm("with the option the three named rows are proposed CLOSED on that basis",
            3, lambda: len([r for r in run_plan(main_tree, design_named=named).sheets["triage"]
                            if r["basis"] == "design-named"]))
        arm("and each carries no evidence",
            ["-", "-", "-"],
            lambda: [r["evidence"] for r in run_plan(main_tree, design_named=named).sheets["triage"]
                     if r["basis"] == "design-named"])
        arm("an id the option names outside the triage population refuses by name",
            "names EXMP-aFoo-6, which is outside the triage population",
            lambda: run_plan(main_tree, design_named=("EXMP-aFoo-6",)))

        # ---- AC5: the dispositions preview, and the hold that names nothing.
        arm("a legacy CLOSED row previews as CLOSED",
            "CLOSED", lambda: read_sheet_row(plan, "status", "EXMP-aFoo-6")["predicted"])
        arm("a legacy WONTDO row previews as WONTDO",
            "WONTDO", lambda: read_sheet_row(plan, "status", "EXMP-aFoo-7")["predicted"])
        arm("a hold naming an ask the same corpus files previews as that hold",
            "BLOCKED", lambda: read_sheet_row(plan, "status", "EXMP-aFoo-3")["predicted"])
        arm("and its decided-by names that ask",
            "EXMP-aFoo-2", lambda: read_sheet_row(plan, "status", "EXMP-aFoo-3")["decided_by"])
        arm("a hold naming only a shorthand previews as a hold on the triage ask",
            TRIAGE_ASK, lambda: read_sheet_row(plan, "status", "EXMP-aFoo-4")["decided_by"])
        arm("a hold naming a decision id nothing files does the same",
            TRIAGE_ASK, lambda: read_sheet_row(plan, "status", "EXMP-aFoo-8")["decided_by"])
        arm("a DEFERRED row naming nothing previews as DEFERRED on the triage ask",
            "DEFERRED", lambda: read_sheet_row(plan, "status", "EXMP-aFoo-5")["predicted"])
        arm("held on the placeholder the switch-over substitutes",
            TRIAGE_ASK, lambda: read_sheet_row(plan, "status", "EXMP-aFoo-5")["decided_by"])

        # ---- AC6: the signed records, and the conservation refusal.
        signed_dir = os.path.join(base, "signed")
        os.makedirs(signed_dir, exist_ok=True)
        same_rec = os.path.join(signed_dir, "same-id.md")
        write_file(same_rec, "| Rule | Ask | Spec | Verdict | Evidence |\n|---|---|---|---|---|\n"
                         "| U1 | EXMP-aBar-4 | spec | unit | specced |\n")
        triage_rec = os.path.join(signed_dir, "triage.md")
        write_file(triage_rec, "| Rule | Ask | Verdict | Field | Evidence | Severity |\n"
                           "|---|---|---|---|---|---|\n"
                           "| T1 | EXMP-aBar-2 | CLOSED | EXMP-aBar-20 | signed | LOW |\n")
        bare = os.path.join(signed_dir, "no-field.md")
        write_file(bare, "| Rule | Ask | Verdict | Evidence |\n|---|---|---|---|\n"
                     "| T1 | EXMP-aBar-2 | CLOSED | signed |\n")

        def read_signed(*kinds):
            out = {}
            for kind, path in kinds:
                out[kind] = read_signed_record(kind, path)
            return run_plan(main_tree, signed=out)

        arm("a signed unit pair whose spec reads CLOSED predicts CLOSED",
            "CLOSED", lambda: read_sheet_row(read_signed(("same-id", same_rec)), "status",
                                     "EXMP-aBar-4")["predicted"])
        arm("and its class is mirror-closed",
            "mirror-closed", lambda: read_sheet_row(read_signed(("same-id", same_rec)), "status",
                                            "EXMP-aBar-4")["class"])
        arm("a signed triage verdict of CLOSED predicts CLOSED",
            "CLOSED", lambda: read_sheet_row(read_signed(("triage", triage_rec)), "status",
                                     "EXMP-aBar-2")["predicted"])
        arm("and its class is triaged",
            "triaged", lambda: read_sheet_row(read_signed(("triage", triage_rec)), "status",
                                      "EXMP-aBar-2")["class"])
        arm("a triage record whose header lacks Field is REFUSED rather than read as unsigned",
            "PROBLEM", lambda: read_signed_record("triage", bare))
        arm("naming the record",
            "no-field.md", lambda: read_signed_record("triage", bare))
        arm("and naming the cell it lacks",
            "Field", lambda: read_signed_record("triage", bare))

        undeclared = os.path.join(base, "undeclared")
        shutil.copytree(main_tree, undeclared)
        run_commit(undeclared, "records: a row whose text cannot survive a render", {
            "memory/backlog/OTHR.md": render_shard("OTHR", ["- OTHR-aBaz-2 · OPEN · unit"]),
        })
        arm("a row whose text no normalization explains refuses the plan",
            "no declared normalization explains", lambda: run_plan(undeclared))

        # ---- AC7: the size, filing-home, view-size and archive-citation findings.
        arm("a slug whose prospective ask file exceeds the declared cap is named with its size",
            "memory/builds/aBar/BACKLOG.md",
            lambda: read_over_cap_findings(base, main_tree))
        arm("a blank row cap says the probe cannot move instead of reporting zero",
            "DEAD PROBE", lambda: read_over_cap_findings(base, main_tree, cap=""))
        arm("the README-less slugs are listed as filing homes",
            "slug aLoose", lambda: plan.summary["findings"][1][1][0])
        arm("a row citing a family archive by path is named with its file and line",
            "memory/backlog/EXMP.md", lambda: plan.summary["findings"][2][1][0])
        arm("and the census carries the archive-citation count",
            1, lambda: len(plan.summary["findings"][2][1]))
        grew = measure_view_delta(base, main_tree, "- EXMP-aFoo-20 · OPEN · one more live ask")
        arm("a family view's prospective size grows when the family gains a live ask",
            True, lambda: grew > 0)
        held = measure_view_delta(base, main_tree, "- EXMP-aFoo-21 · CLOSED · one more terminal ask")
        arm("and does not change when it gains a terminal one",
            0, lambda: held)

        # ---- AC8: the records, named by the recording grammar and byte-identical across runs.
        out_dir = os.path.join(main_tree, "out")
        first = write_fixture_records(main_tree, out_dir)
        second = write_fixture_records(main_tree, out_dir)
        arm("--record writes four records", 4, lambda: len(first))
        arm("named by the recording grammar with HEAD's commit day",
            True, lambda: all(re.fullmatch(r"\d{4}-\d{2}-\d{2}-build-EXMP-aFoo-1-"
                                           r"(census\.md|same-id\.tsv|triage\.tsv|status\.tsv)",
                                           os.path.basename(p)) for p in first))
        arm("each carrying its Serves line",
            True, lambda: all("**Serves:** journal EXMP-aFoo-1" in read_text(p) for p in first))
        arm("and two runs over one tree are byte-identical",
            True, lambda: all(read_text(a) == read_text(b) for a, b in zip(first, second)))
        arm("git status shows nothing outside the record directory",
            True, lambda: all(line[3:].startswith("out/")
                              for line in run("git", "status", "--porcelain",
                                              cwd=main_tree).split("\n") if line.strip()))

        # ---- AC12: the repo is the one the CALL was made in, never the module's own tree.
        older = run("git", "rev-parse", "HEAD~1", cwd=main_tree).strip()
        side = os.path.join(base, "side")
        run("git", "worktree", "add", "-q", "--detach", side, older, cwd=main_tree)
        arm("--plan run from a second worktree counts that worktree's rows, one fewer",
            "30 row copies", lambda: run_plan_in(side).summary["corpus"][0])
        arm("so the tree the CALL was made in decided the census, not the module's own",
            len(plan.census) - 1, lambda: len(run_plan_in(side).census))
    finally:
        shutil.rmtree(base, ignore_errors=True)

    if count[0] < FLOOR_ASSERTIONS:
        print(f"migrate-backlog selftest: {count[0]} assertions executed, below the declared floor "
              f"of {FLOOR_ASSERTIONS} — a block of arms is stranded")
        return 1
    if fails:
        print(f"FAIL — {len(fails)} arm(s) failed: {'; '.join(fails)}")
        return 1
    print(f"PASS ({count[0]} assertions)")
    return 0


def write_fixture_records(tree: str, out_dir: str) -> list:
    buf = io.StringIO()
    with redirect_stdout(buf):
        plan = build_plan(tree)
        return write_records(tree, out_dir, "EXMP-aFoo-1", plan.day, plan.head, plan.sheets,
                             plan.summary)


def run_plan_in(tree: str):
    return run_plan(resolve_root(tree))


def read_over_cap_findings(base: str, main_tree: str, cap: str = "400") -> str:
    """The same corpus under a declared cap the caller chooses.

    A cap small enough that a real slug breaches it, or a BLANK one — the value that used to
    make the probe report zero slugs and read exactly like a tree with nothing over cap.
    """
    import shutil
    tiny = os.path.join(base, "cap" + (cap or "blank"))
    if not os.path.isdir(tiny):
        shutil.copytree(main_tree, tiny)
        run_commit(tiny, "records: a declared cap this corpus is graded against",
                   {".memory-tree.conf": render_conf(cap)})
    findings = run_plan(tiny).summary["findings"][0][1]
    return "\n".join(findings)


def measure_view_delta(base: str, main_tree: str, row: str) -> int:
    """How the EXMP family view's prospective size moves when the fixture gains one more ask."""
    import shutil
    name = "grown" + str(abs(hash(row)) % 9999)
    grown = os.path.join(base, name)
    shutil.copytree(main_tree, grown)
    text = read_text(os.path.join(grown, "memory/backlog/EXMP.md"))
    run_commit(grown, "records: one more ask", {"memory/backlog/EXMP.md": text.rstrip("\n")
                                             + "\n" + row + "\n"})
    return run_plan(grown).summary["views"]["EXMP"] - run_plan(main_tree).summary["views"]["EXMP"]


# ------------------------------------------------------------------------------------------- CLI
USAGE = ("usage: migrate_backlog.py --plan [--record <dir> --record-as <unit-id>] "
         "[--signed <same-id|triage>=<path>] [--design-named <id>] … | --selftest")


def read_args(argv: list) -> dict:
    args = {"mode": "", "record": "", "record_as": "", "signed": [], "design_named": []}
    rest = list(argv)
    while rest:
        token = rest.pop(0)
        if token in ("--plan", "--selftest"):
            args["mode"] = token
        elif token == "--record":
            args["record"] = read_flag_value(rest, token)
        elif token == "--record-as":
            args["record_as"] = read_flag_value(rest, token)
        elif token == "--design-named":
            args["design_named"].append(read_flag_value(rest, token))
        elif token == "--signed":
            value = read_flag_value(rest, token)
            kind, sep, path = value.partition("=")
            if not sep or kind not in SIGNED_CELLS or not path:
                raise Problem(f"migrate-backlog: --signed takes <kind>=<path> where kind is one "
                              f"of {' '.join(sorted(SIGNED_CELLS))}, not '{value}'")
            args["signed"].append((kind, path))
        else:
            raise Problem(f"migrate-backlog: unknown argument '{token}'\n{USAGE}")
    return args


def read_flag_value(rest: list, flag: str) -> str:
    if not rest:
        raise Problem(f"migrate-backlog: {flag} needs a value\n{USAGE}")
    return rest.pop(0)


def main(argv: list) -> int:
    args = read_args(argv[1:])
    if args["mode"] == "--selftest":
        return cmd_selftest()
    if args["mode"] != "--plan":
        print(USAGE)
        return 2
    return cmd_plan(resolve_root(), args)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Problem as exc:
        print(str(exc))
        sys.exit(1)

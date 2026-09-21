#!/usr/bin/env python3
"""migrate_backlog.py — the shards-to-builds backlog PLANNER and the relocation ENGINE.

    python migrate_backlog.py --plan                             # read-only; the planner
    python migrate_backlog.py --plan --record <dir> --record-as <unit-id>
    python migrate_backlog.py --plan --signed same-id=<path> --signed triage=<path>
    python migrate_backlog.py --plan --design-named <id> [--design-named <id> …]
    python migrate_backlog.py --relocate --as <slug> [--from <ref>]   # after merging the default
    python migrate_backlog.py --repair <merge-sha> --as <slug>       # a transition already landed
    python migrate_backlog.py --ingest <ref> --as <slug>             # a ref nobody will revisit
    python migrate_backlog.py --stragglers [--local] [--tsv]         # who still owes a relocation
    python migrate_backlog.py --recipe                               # the one relocation recipe
    python migrate_backlog.py --selftest

Add `--dry-run` to any writing verb: it prints the plan and the conservation table and touches
nothing. Exit 0 means the plan would write, 1 that the plan itself refuses and a human must answer
it, and 2 that a condition or a form is missing — the switch-over's landing reconcile and the
adopter runbook both re-run a rehearsal only when it did not exit 1, so those two codes are not
interchangeable.

WHAT THE RELOCATION ENGINE IS. A branch that forked before the flip and kept editing authored
backlog shards carries row changes that no longer have a file to land in. The three writing verbs
move every changed row into the per-build files, write one provenance row per delta entry, and
refuse to finish while any change is unaccounted. The DELTA and the ACCOUNTING PREDICATE are
`transition_audit.py`'s, called and never re-spelled; the row GRAMMARS and the status FOLD are
`backlog.py`'s; the recipe is the ONE constant that unit keeps. What is this module's own is the
classification table — which record each kind of change becomes, and in whose folder.

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
import pathlib
import re
import subprocess
import sys
from contextlib import redirect_stdout

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import backlog                      # noqa: E402  — a sibling of this file, never a spelled path
import gen_build_index as index     # noqa: E402
import transition_audit as audit    # noqa: E402  — the delta and the accounting predicate

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
#: exactly what a floor catches and a green line does not. It moved from 71 to 205 when the
#: relocation engine's arms landed; the figure is the count the suite executes, and it is RAISED in
#: the same commit as the arms, because a floor left behind is a floor that stops measuring.
FLOOR_ASSERTIONS = 205

NEWLINE = chr(10)

_PROCESSES = [0]


class Problem(Exception):
    """A named, user-facing failure. Never a traceback, and never raised by row CONTENT."""


class Refusal(Problem):
    """A refusal that exits 2: a missing condition, a malformed value, a form not admitted.

    DELIBERATELY DISTINCT FROM 1, which means "the plan itself refuses and a human must answer it".
    The switch-over's landing reconcile and the adopter runbook both re-run a rehearsal WITHOUT
    `--dry-run` only when it did not exit 1, so collapsing the two codes would park them on a
    condition that is merely absent.
    """

    code = 2


# ------------------------------------------------------------------------------- the process seam
def run(*argv, cwd=None, env=None) -> str:
    """One git call, counted. The liveness line prints the count, which is why it lives here."""
    _PROCESSES[0] += 1
    proc = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True,
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


def build_rotated_archive_re(memory_root: str, families) -> "re.Pattern":
    """The rotated FAMILY archive predicate, as a whole repo-relative path pattern.

    ONE spelling, two readers: the census below and the relocate restore. It selects the same names
    the hygiene engine's `--print-rotated-archive-ere` does under the family alternation; the
    decision log, which no family owns, is in that engine's pattern and deliberately not in this
    one. A second spelling here was exactly the two-answers class: one keyed on the basename and
    one on the path, agreeing until the day a family token changed shape.
    """
    stems = "|".join(re.escape(f) for f in families)
    return re.compile(re.escape(memory_root) + r"/archive/(?:" + stems + r")"
                      r"\.[0-9]{4}-[0-9]{2}-[0-9]{2}[a-z0-9]*\.md\Z")


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
    rot = build_rotated_archive_re(m, families)
    live = sorted(p for p in tracked
                  if re.fullmatch(re.escape(m) + r"/backlog/(?:" + stems + r")\.md", p))
    arch = sorted(p for p in tracked if rot.fullmatch(p))
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


# -------------------------------------------------------------------------- the relocation engine
#: The two POLICY SETS of section 4. Not a mode, not a flag: a set of four policies the same engine
#: runs under, so the switch-over's whole-corpus migration and a straggler's relocation are one
#: planner rather than two that drift.
STRAGGLER_SET = "straggler"
MIGRATION_SET = "migration"

#: The classification a planned entry lands in when no rule below fits. It is not a record: the
#: whole plan refuses while one of these is in it, because a half-relocated tree is one
#: `git add memory/` away from being committed (section 8 F2).
HUMAN = "NEEDS-HUMAN"

#: What a straggler-set hold naming no id becomes. The migration set's value is the triage ask id
#: `--triage-ask` supplies; that is the whole of policy P3.
UNNAMED_HOLD_STRAGGLER = HUMAN

#: One planned row: the file it lands in, the section it sits under, its bytes, the id it is about,
#: and the existing line it REPLACES (section 8 F10) or "" when it is an insertion.
Record = collections.namedtuple("Record", "path section text ident replaces")

#: One entry path to the writer, from section 4's table. The verb and the four policies it fixes,
#: resolved ONCE at the CLI and passed down, so no function below re-decides which set it is in.
Form = collections.namedtuple("Form", "verb name policy provenance confirm")

#: The classification of one delta entry: what it is, what it writes, and the provenance kind.
Classified = collections.namedtuple("Classified", "ident kind classification records disposal why")

Relocation = collections.namedtuple(
    "Relocation", "form entries verdicts records human confirm before after cutoff table")


def run_unchecked(*argv, cwd=None) -> tuple:
    """One git call whose NON-ZERO exit is an ANSWER, not a failure. Counted like every other.

    `merge-base --is-ancestor` answers containment with its exit status and `rev-parse --verify`
    answers existence with its own; routing either through `run` would turn a legitimate "no" into
    a refusal naming a command the caller never asked about.
    """
    _PROCESSES[0] += 1
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    # BOTH STREAMS, joined. A refusal this engine needs to read — the row driver's recipe banner,
    # the generator's guarded-view remedy — goes to stderr, and a reader of stdout alone would see
    # an empty string and report that the command said nothing.
    return proc.returncode, proc.stdout + proc.stderr


def read_rev(root: str, rev: str) -> str:
    """`rev` as a 40-hex sha, or "" when this repository does not hold it."""
    code, out = run_unchecked("git", "rev-parse", "--verify", "--quiet", rev + "^{commit}", cwd=root)
    return out.strip() if code == 0 else ""


def check_contains(root: str, ancestor: str, descendant: str) -> bool:
    """Is `ancestor` in `descendant`'s history? The containment every `--ingest` admission reads."""
    code, _out = run_unchecked("git", "merge-base", "--is-ancestor", ancestor, descendant, cwd=root)
    return code == 0


def read_conf_mode(root: str, rev: str) -> str:
    """The backlog mode a rev's `.memory-tree.conf` BLOB declares, through unit 9's ONE reader.

    Never this tree's live conf and never a second parse: a straggler that pulled the new conf
    early has a tip that reads `builds` over a lineage that edited shards, which is the exact
    misreading unit 9's own classifier refuses to make.
    """
    base = pathlib.Path(root)
    return audit.read_modes(base, [rev], audit.derive_conf_rel(base)).get(rev, "shards")


def read_recipe(root: str, conf=None) -> list:
    """The relocation recipe, at THIS install's prefix and this tree's memory root.

    ONE constant, four renderings (unit 7 section 8 F5). This function holds no copy of the text:
    it fills the view layer's own constant, which is what makes the byte comparison in the selftest
    a comparison rather than two spellings agreeing by luck.
    """
    if conf is None:
        conf = read_index(index.load_conf, root)
    return backlog.render_relocation_recipe(index.kit_rel(), conf["MEMORY_ROOT"])


def build_recipe_refusal(root: str, why: str, conf=None):
    """A `--relocate` refusal, which always carries the recipe: every banner that sent the operator
    here printed one command, so a refusal that does not reprint it strands them mid-merge."""
    return Refusal(why + NEWLINE + NEWLINE.join(read_recipe(root, conf)))


def resolve_default_tip(root: str) -> tuple:
    """`(name, sha)` for the default branch, as `.githooks/pre-push` resolves it.

    THE OBSERVED `origin/HEAD` WINS and the environment only CROSS-CHECKS it. The recall hit
    `TOOL-aStandingWrit-5` records an environment value that named the branch already checked out
    and disabled a guard by doing so; a resolution that lets the environment SELECT repeats it.
    """
    code, out = run_unchecked("git", "symbolic-ref", "--short", "refs/remotes/origin/HEAD", cwd=root)
    observed = out.strip()[len("origin/"):] if code == 0 and out.strip() else ""
    declared = os.environ.get("GOV_DEFAULT_BRANCH", "").strip()
    if observed and declared and observed != declared:
        raise Refusal(f"migrate-backlog: GOV_DEFAULT_BRANCH names `{declared}`, which this clone "
                      f"does not observe as its default (`{observed}`). The straggler inventory is "
                      f"keyed on that branch, so an unrecognised name would list every ref or none")
    name = observed or declared
    if not name:
        raise Refusal("migrate-backlog: cannot determine the default branch — origin/HEAD is unset "
                      "and GOV_DEFAULT_BRANCH is unset. Refusing to guess `main`: a wrong default "
                      "makes every ref read as a straggler or none of them.\n"
                      "  Fix once: git remote set-head origin -a")
    sha = read_rev(root, f"refs/heads/{name}") or read_rev(root, f"refs/remotes/origin/{name}")
    if not sha:
        raise Refusal(f"migrate-backlog: the default branch resolves to `{name}`, which is no "
                      f"branch in this clone, so every ref would be compared against nothing")
    return name, sha


# ------------------------------------------------------------------------------- side resolution
def resolve_sides(root: str, args: dict) -> tuple:
    """-> `(form, ours, theirs)`. WHICH SIDE IS THE STRAGGLER, per section 2 S1, S6 and S7.

    Every verb ends at one call of unit 9's `delta(ours, theirs)` with no merge commit between
    them, bound POSITIONALLY as that unit's S13 binds it. Nothing here re-derives a transition or a
    row version; the only question this function answers is whose change is being relocated.
    """
    verb = args["mode"]
    if verb == "--relocate":
        return resolve_relocate_sides(root, args)
    if verb == "--ingest":
        return resolve_ingest_sides(root, args)
    return resolve_repair_sides(root, args)


def resolve_relocate_sides(root: str, args: dict) -> tuple:
    """S1 — MERGE_HEAD, else a merge HEAD's parents, else `--from`, else exit 2 with the recipe."""
    heads = audit.read_merge_heads(pathlib.Path(root))
    head = read_rev(root, "HEAD")
    if heads:
        ours, theirs, name = head, heads, "relocate (MERGE_HEAD)"
    else:
        parents = [p for p in run("git", "rev-list", "--parents", "-n", "1", "HEAD",
                                  cwd=root).split() if p][1:]
        if len(parents) > 1:
            ours, theirs, name = parents[0], parents[1:], "relocate (concluded merge)"
        elif args["from"]:
            ref = read_rev(root, args["from"])
            if not ref:
                raise Refusal(f"migrate-backlog: --from names `{args['from']}`, which is no commit "
                              f"in this repository")
            ours, theirs, name = ref, [head], "relocate (--from)"
        else:
            raise build_recipe_refusal(
                root, "migrate-backlog: --relocate found no MERGE_HEAD, no merge HEAD and no "
                      "--from, so it cannot tell which side is the straggler. Merge the default "
                      "branch first, or name the straggler's tip with --from.")
    for other in theirs:
        if read_conf_mode(root, other) != "builds":
            raise build_recipe_refusal(
                root, f"migrate-backlog: --relocate needs the OTHER side to be in builds mode, and "
                      f"{other[:12]}'s .memory-tree.conf reads shards — there is no per-build file "
                      f"to relocate into, and writing one would be a half-migration.")
    confirm = name == "relocate (--from)"
    return Form("--relocate", name, STRAGGLER_SET, True, confirm), ours, theirs


def resolve_ingest_sides(root: str, args: dict) -> tuple:
    """S6 — the two forms of `--ingest`, and section 8 F9's admission once a merge is concluded."""
    ref = read_rev(root, args["ref"])
    if not ref:
        raise Refusal(f"migrate-backlog: --ingest names `{args['ref']}`, which is no commit in "
                      f"this repository")
    head = read_rev(root, "HEAD")
    head_mode = read_conf_mode(root, head)
    landing = False
    if head_mode == "builds" and read_conf_mode(root, ref) == "shards":
        # A REPOSITORY WITH NO RESOLVABLE DEFAULT BRANCH IS SIMPLY NOT THE LANDING SHAPE. Letting
        # that refusal escape here would make every straggler-form `--ingest` depend on a remote
        # this verb never reads — the form is decided, not gated, by the question.
        try:
            _name, tip = resolve_default_tip(root)
            landing = tip == ref
        except Refusal:
            landing = False
    if not landing and head_mode != "builds":
        raise build_recipe_refusal(
            root, f"migrate-backlog: --ingest in its straggler form needs a builds-mode checkout, "
                  f"and HEAD's .memory-tree.conf reads {head_mode}. Its landing form needs the "
                  f"default tip in shards mode under a builds-mode HEAD, which this is not.")
    form = (Form("--ingest", "ingest (landing)", MIGRATION_SET, True, True) if landing
            else Form("--ingest", "ingest (straggler)", STRAGGLER_SET, True, True))
    if not check_contains(root, ref, head):
        # Before the merge, and DURING one: `git merge --no-ff --no-commit <tip>` leaves HEAD where
        # it was, so the ref is still uncontained and the delta is the same one the pre-merge run
        # would take. That is the state unit 34's landing reconcile ingests in.
        return form, ref, [head]
    parents = [p for p in run("git", "rev-list", "--parents", "-n", "1", head,
                              cwd=root).split() if p][1:]
    if (landing and len(parents) > 1 and parents[1] == ref
            and not check_contains(root, ref, parents[0])):
        return form, ref, [parents[0]]
    raise Refusal(
        f"migrate-backlog: HEAD already contains {args['ref']}, and this is not the one state "
        f"--ingest is admitted in afterwards — a landing-form run on a concluded merge whose "
        f"SECOND parent is that ref and whose first parent does not contain it. Use --repair "
        f"<merge-sha> --as <slug> instead, which plans only what is still unaccounted.")


def resolve_repair_sides(root: str, args: dict) -> tuple:
    """S7 — the shards side of a transition merge, classified by unit 9 and never a second time."""
    head = read_rev(root, "HEAD")
    if read_conf_mode(root, head) != "builds":
        raise build_recipe_refusal(
            root, f"migrate-backlog: --repair writes per-build files and HEAD's "
                  f"`.memory-tree.conf` reads shards, so its records would be a half-migration the "
                  f"generator's own mode guard reds.")
    merge = read_rev(root, args["ref"])
    if not merge:
        raise Refusal(f"migrate-backlog: --repair names `{args['ref']}`, which is no commit in "
                      f"this repository")
    walk = audit.Walk(pathlib.Path(root), [merge])
    pair = audit.derive_transition(walk, merge)
    if pair is None:
        raise Refusal(f"migrate-backlog: {merge[:12]} is not a transition merge — no parent's "
                      f"lineage edits authored shards under a builds-mode sibling — so there is "
                      f"nothing for this verb to repair")
    ours, theirs = pair
    return Form("--repair", "repair", STRAGGLER_SET, True, True), ours, list(theirs)


# --------------------------------------------------------------------------------- the tree reads
def read_target_texts(root: str, conf: dict) -> dict:
    """`{path: text}` for every tracked `<M>/builds/*/BACKLOG.md` IN THE WORKING TREE.

    The worktree and not a rev: `--relocate` runs inside a merge whose index is the thing about to
    be committed, and a fold read from a commit would grade a tree nobody is looking at.
    """
    m = conf["MEMORY_ROOT"]
    tracked = [p for p in run("git", "ls-files", "--", m + "/", cwd=root).split("\n") if p]
    out = {}
    for rel in sorted(p for p in tracked
                      if p.startswith(f"{m}/builds/") and p.endswith("/BACKLOG.md")):
        try:
            out[rel] = read_text(os.path.join(root, rel))
        except OSError:
            continue
    return out


def read_target_specs(root: str, conf: dict) -> tuple:
    """`(specs, build statuses)` — the fold's two non-row inputs, through the generator's collect."""
    builds = read_index(index.collect, root, conf)
    specs = {}
    for build in builds:
        for unit in build["units"]:
            rel = os.path.relpath(unit["path"], root).replace("\\", "/")
            specs[unit["id"]] = backlog.Spec(unit["id"], rel, unit["status"], (), ())
    return specs, {b["slug"]: b["status"] for b in builds}


def derive_fold(texts: dict, specs: dict, build_status: dict, grammar):
    """The status fold over a set of per-build files, unit 6's and never re-derived here."""
    files = [backlog.parse_file(rel, text, grammar) for rel, text in sorted(texts.items())]
    return backlog.derive_statuses(backlog.build_corpus(files, specs, build_status))


def read_slug_home(memory_root: str, slug: str) -> str:
    return f"{memory_root}/builds/{slug}/BACKLOG.md"


def add_row(text: str, section: str, line: str, replaces: str, slug: str) -> str:
    """One row into one file, under its section, REPLACING a named line where F10 says to.

    Appends at the END of the section rather than sorting: a generated order would make every
    concurrent relocation conflict on rows neither side authored, which is the property the view
    layer exists to avoid.
    """
    body = text if text.strip() else f"# {slug} — asks{NEWLINE}"
    lines = body.split(NEWLINE)
    bare = [ln.rstrip(chr(13)) for ln in lines]
    if replaces and replaces in bare:
        lines[bare.index(replaces)] = line
        return NEWLINE.join(lines).rstrip(NEWLINE) + NEWLINE
    if section not in bare:
        if section == backlog.H_ASKS and backlog.H_DISPOSITIONS in bare:
            at = bare.index(backlog.H_DISPOSITIONS)
            lines[at:at] = [section, "", line, ""]
        else:
            while lines and not lines[-1].strip():
                lines.pop()
            lines += ["", section, "", line]
        return NEWLINE.join(lines).rstrip(NEWLINE) + NEWLINE
    start = bare.index(section)
    end = len(lines)
    for n in range(start + 1, len(lines)):
        if bare[n].startswith("## "):
            end = n
            break
    while end > start + 1 and not lines[end - 1].strip():
        end -= 1
    lines[end:end] = [line]
    return NEWLINE.join(lines).rstrip(NEWLINE) + NEWLINE


def build_texts_with(texts: dict, records: list, memory_root: str) -> dict:
    """The target tree's files with the planned records applied — the fold's `after` input."""
    out = dict(texts)
    for rec in records:
        slug = rec.path.split("/")[-2]
        out[rec.path] = add_row(out.get(rec.path, ""), rec.section, rec.text, rec.replaces, slug)
    return out


# ------------------------------------------------------------------------------ the classifier
def read_version_row(version, grammar):
    """One delta version as `(token, body, line)`, or `(None, "", "")` when it holds no row.

    A version anchored on SEVERAL lines of one rev keeps all of them (unit 9 reads it that way);
    the FIRST is classified and the rest make the entry unreadable rather than a coin toss.
    """
    if not version:
        return None, "", ""
    lines = [ln for ln in version.split(NEWLINE) if ln.strip()]
    if len(lines) != 1:
        return None, "", lines[0] if lines else ""
    leg = backlog.read_legacy_row(lines[0].strip(), grammar)
    return leg.status, leg.body, lines[0].strip()


def read_base_version(entry: dict):
    """The row's version at the merge bases. The first non-empty one, by sorted base sha.

    A criss-cross merge has several bases and unit 9 reports an entry only when the version differs
    from EVERY one of them, so any base is an honest "before" — taking the sorted-first keeps two
    runs over one tree byte-identical.
    """
    for sha in sorted(entry["bases"]):
        if entry["bases"][sha]:
            return entry["bases"][sha]
    return None


PATH_TOKEN_RE = re.compile(r"[A-Za-z0-9._-]*/[A-Za-z0-9._/#-]*")


def check_path_repoint(old: str, new: str) -> bool:
    """Is this text change confined to PATH tokens (owner ruling D9)?

    Both sides with every slash-carrying token blanked out. Equal means the prose is untouched and
    only a location moved, which is the one text change this engine may rewrite unattended.
    """
    if old == new:
        return False
    return PATH_TOKEN_RE.sub("", old) == PATH_TOKEN_RE.sub("", new)


def check_names_hold(body: str, grammar, known) -> str:
    """P3's names-an-id test, which is unit 11 S7's census semantics and not a second rule."""
    return read_named_hold(body, grammar, known)


def build_verdicts(entries: list, form: Form, grammar, known: set, drops: dict,
                   triage_ask: str) -> list:
    """Section 4's classification table, one row per delta entry. Decides, writes nothing."""
    out = []
    for entry in entries:
        ident = entry["id"]
        if ident in drops:
            out.append(Classified(ident, entry["kind"], "dropped by hand", [], "dropped",
                                drops[ident]))
            continue
        out.append(build_verdict(entry, form, grammar, known, triage_ask))
    return out


def build_verdict(entry: dict, form: Form, grammar, known: set, triage_ask: str) -> Classified:
    """One delta entry's class, its record shapes and its provenance kind."""
    ident = entry["id"]
    kind = entry["kind"]
    tok_new, body_new, _line_new = read_version_row(entry["ours"], grammar)
    tok_old, body_old, line_old = read_version_row(read_base_version(entry), grammar)
    if kind == audit.REMOVED:
        if tok_old in backlog.TERMINAL:
            return Classified(ident, kind, "removed, terminal at the base", [], "dropped",
                            "terminal row removed")
        return Classified(ident, kind, HUMAN, [], "",
                        "a row that was live at the merge base was removed, and only a human can "
                        "say whether that was a withdrawal or an accident")
    if tok_new is None:
        return Classified(ident, kind, HUMAN, [], "",
                        "the row version at the straggler side is not one readable legacy row")
    change = entry["change"]
    if kind == audit.NEW:
        records = [("ask", ident, body_new, "")]
        disp = build_disposition_shape(ident, tok_new, body_new, grammar, known, form, triage_ask,
                                       change)
        if disp == HUMAN:
            return Classified(ident, kind, HUMAN, [], "", build_unnamed_why(ident))
        records += disp
        return Classified(ident, kind, "new ask", records, "kept", "new ask")
    if tok_old is None:
        return Classified(ident, kind, HUMAN, [], "",
                        "the row version at the merge base is not one readable legacy row")
    if tok_new != tok_old:
        if tok_new in backlog.TERMINAL and tok_old in backlog.TERMINAL:
            pass
        elif tok_new not in backlog.TERMINAL and tok_old in backlog.TERMINAL:
            return Classified(ident, kind, HUMAN, [], "",
                            f"a flip from the terminal `{tok_old}` back to `{tok_new}` is a "
                            f"reopening, and the engine never reopens an ask on its own")
        if tok_new in ("OPEN", "SPECCED", "INPROGRESS"):
            if check_path_repoint(body_old, body_new) or body_old == body_new:
                return Classified(ident, kind, "live flip, derived", [], "kept",
                                "live flip, derived")
            return Classified(ident, kind, HUMAN, [], "",
                            f"the flip to `{tok_new}` is derived now, but the row's prose changed "
                            f"with it and no record would carry that change")
        disp = build_disposition_shape(ident, tok_new, body_new, grammar, known, form, triage_ask,
                                       change,
                                       replaces=build_replaced_line(ident, tok_old, body_old,
                                                                    grammar, known, form,
                                                                    triage_ask))
        if disp == HUMAN:
            return Classified(ident, kind, HUMAN, [], "", build_unnamed_why(ident))
        label = {"CLOSED": "flip to CLOSED", "WONTDO": "flip to WONTDO"}.get(tok_new, "hold")
        return Classified(ident, kind, label, disp, "kept", label)
    if check_path_repoint(body_old, body_new):
        return Classified(ident, kind, "path repoint", [("repoint", ident, body_new, "")], "amended",
                        "path repoint")
    return Classified(ident, kind, HUMAN, [], "",
                    "the row's prose changed and only a human can say what the change means")


def build_unnamed_why(ident: str) -> str:
    return (f"{ident} is held on a target this corpus cannot resolve to an ask or a spec, so the "
            f"hold would derive UNRESOLVED wherever it landed")


def read_closing_evidence(body: str, grammar, known) -> str:
    """The id a legacy `CLOSED by <id>` row names in its FIRST body field, or "".

    Unit 11's `derive_dispositions` reads the same field for the same reason: the legacy grammar
    puts the closing evidence there and the rest of the body is prose. That named id is the only
    `by` value a DELTA can reproduce — the alternative unit 11 falls back to is a sha mined from a
    history walk this engine does not make.
    """
    return read_named_hold(body.split(backlog.SEP)[0], grammar, known)


def build_disposition_shape(ident: str, token: str, body: str, grammar, known, form: Form,
                            triage_ask: str, change: str = "", replaces: str = "") -> list:
    """The disposition rows a legacy token transfers into, or `HUMAN` for an unnamed hold.

    P1 decides the FILE and this decides the ROW; the two are separate because the migration set
    moves the same bytes into a different folder and nothing else about them changes.
    """
    why = body.strip() or ("withdrawn" if token == "WONTDO" else "relocated from a legacy row")
    if token == "CLOSED":
        value = read_closing_evidence(body, grammar, known) or change
        if not value:
            return HUMAN
        return [("status", ident, ("CLOSED", value, why), replaces)]
    if token == "WONTDO":
        return [("status", ident, ("WONTDO", "", why), replaces)]
    if token in ("BLOCKED", "DEFERRED"):
        named = check_names_hold(body, grammar, known)
        if not named:
            if form.policy != MIGRATION_SET or not triage_ask:
                return HUMAN
            named = triage_ask
        return [("status", ident, (token, named, why), replaces)]
    return []


def build_replaced_line(ident: str, token: str, body: str, grammar, known, form: Form,
                        triage_ask: str) -> str:
    """Section 8 F10 — the row the MIGRATION SET itself would have written from the BASE version.

    Only that line may be replaced, and only in the landing form. The migration wrote it, a writer
    changes its mind by editing its OWN row (unit 6 section 4), and any other existing row belongs
    to whoever put it there — overwriting one is lab case e09b's class.
    """
    if form.name != "ingest (landing)":
        return ""
    # A `CLOSED` merge-base row whose body names no closing id is DELIBERATELY not reproducible
    # here: `--write` fills that slot from a history walk (unit 11's `derive_dispositions`), and
    # guessing it would compare against a row the migration never wrote. With no candidate line the
    # collision stays NEEDS-HUMAN, which is F10's own default and never lab case e09b.
    shape = build_disposition_shape(ident, token, body, grammar, known, form, triage_ask, "")
    if shape == HUMAN or not shape:
        return ""
    verb, value, why = shape[0][2]
    return backlog.render_status_row(verb, ident, why, value)


# ------------------------------------------------------------------------------- the planner
def build_relocation(root: str, form: Form, ours: str, theirs: list, args: dict,
                     conf=None) -> Relocation:
    """The whole read-only pass of the three writing verbs: plan, confirm, conserve. Writes nothing.

    PLAN THEN WRITE, ALL OR NOTHING (section 8 F2). Everything here returns; the caller writes only
    when the NEEDS-HUMAN and CONFIRM lists are both empty.
    """
    conf = conf or read_index(index.load_conf, root)
    memory_root = conf["MEMORY_ROOT"]
    grammar = backlog.build_grammar(derive_families(conf))
    entries = audit.delta(ours, theirs, root) if args.get("entries") is None else args["entries"]
    # S7 — AN ENTRY ALREADY ACCOUNTED AT `HEAD` PLANS NOTHING, which is what makes every verb
    # idempotent: a second `--repair` over a tree whose records landed plans zero records rather
    # than a second set of them, which unit 9 would then red as a DUPLICATE. The predicate is that
    # unit's, bound to HEAD as S7 words it, and `plan.entries` keeps the FULL delta so the
    # post-write re-read still grades every entry.
    open_now = audit.accounted(entries, "HEAD", pathlib.Path(root))
    planned = [e for i, e in enumerate(entries) if open_now.get(i) != "ok"]

    texts = read_target_texts(root, conf)
    specs, build_status = read_target_specs(root, conf)
    before = derive_fold(texts, specs, build_status, grammar)

    signed = {kind: read_signed_record(kind, path) for kind, path in args["signed"]}
    units, signed_triage = read_signed_verdicts(signed)
    if form.policy != MIGRATION_SET:
        units, signed_triage = set(), {}

    # P3's known set, and it is deliberately the UNION of three populations: an ask the target tree
    # files, an ask THIS PLAN writes a row for, and a spec H1. Unit 11 S7's census semantics — a
    # delta that files X and holds on X keeps that hold in every form.
    filing = {e["id"] for e in planned if e["kind"] == audit.NEW}
    known = set(before.statuses) | filing | set(specs)

    drops = dict(args["drop"])
    verdicts = build_verdicts(planned, form, grammar, known, drops, args["triage_ask"])
    human = [(v.ident, v.why) for v in verdicts if v.classification == HUMAN]

    new_ids = {v.ident for v in verdicts if any(r[0] == "ask" for r in v.records)}
    filed = read_filed_days(root, ours, theirs, new_ids)
    records = build_records(verdicts, form, args["as_slug"], memory_root, filed, units, texts,
                            grammar, planned)
    records += build_triage_records(signed_triage, texts, args["as_slug"], memory_root, grammar)
    records, collisions = check_collisions(records, texts, grammar)
    human += collisions

    after = derive_fold(build_texts_with(texts, records, memory_root), specs, build_status, grammar)
    confirm = []
    if form.confirm:
        for ident in sorted({r.ident for r in records}):
            was, now = before.statuses.get(ident), after.statuses.get(ident)
            if was is not None and was != now and ident not in args["confirm"]:
                confirm.append((ident, was, now))
    cutoff = build_cutoff(conf, filed, records) if form.name == "ingest (landing)" else ""
    table = build_table(verdicts, records, before, after)
    return Relocation(form, entries, verdicts, records, human, confirm, before, after, cutoff,
                      table)


def build_records(verdicts: list, form: Form, as_slug: str, memory_root: str, filed: dict,
                  units: set, texts: dict, grammar, entries: list) -> list:
    """P1 — every planned row, in the file its class sends it to.

    A transferred legacy token goes to the `--as` folder under the straggler set and to the ask
    OWNER's folder under the migration set; an ask row always goes to its id's own folder; a
    provenance row always goes to the writer's, which is the `--as` folder (section 8 F3).
    """
    as_home = read_slug_home(memory_root, as_slug)
    change = {e["id"]: e["change"] for e in entries}
    out = []
    for verdict in verdicts:
        if verdict.classification == HUMAN:
            continue
        owner = read_slug_home(memory_root, read_slug(verdict.ident))
        for shape in verdict.records:
            cls, ident, value, replaces = shape
            if cls == "ask":
                out.append(Record(owner, backlog.H_ASKS, backlog.render_ask_row(
                    ident, filed.get(ident, FILED_PLACEHOLDER), value, unit=ident in units),
                    ident, ""))
            elif cls == "status":
                verb, slot, why = value
                home = owner if form.policy == MIGRATION_SET else as_home
                out.append(Record(home, backlog.H_DISPOSITIONS,
                                  backlog.render_status_row(verb, ident, why, slot), ident,
                                  replaces))
            elif cls == "repoint":
                out.append(build_repoint_record(owner, ident, value, texts, grammar))
        if form.provenance:
            # `verdict.ident` AND NEVER THE LOOP VARIABLE ABOVE. A verdict that writes no record —
            # a dropped row, a live flip — leaves that name bound to the PREVIOUS entry's id, and
            # the provenance row then names the wrong ask: two rows for one id, none for the other,
            # which unit 9 reads as a duplicate beside an unaccounted entry. Measured, not feared.
            out.append(Record(as_home, backlog.H_DISPOSITIONS, backlog.render_relocated_row(
                verdict.ident, change.get(verdict.ident, ""), verdict.disposal, verdict.why),
                verdict.ident, ""))
    return [r for r in out if r is not None]


def build_repoint_record(owner: str, ident: str, body: str, texts: dict, grammar):
    """D9's path repoint: the ask row in its home file, rewritten to the straggler's text.

    A REPLACEMENT and never an insertion — a second ask row for one id is what V3 reds, and the
    whole point of this class is that the ask already lives where it belongs.
    """
    for raw in texts.get(owner, "").split(NEWLINE):
        line = raw.rstrip(chr(13))
        row = backlog.extract_row(line, grammar)
        if row is not None and row.cls == "ask" and row.target == ident:
            return Record(owner, backlog.H_ASKS, backlog.render_ask_row(
                ident, row.value, body, unit=row.extra["unit"]), ident, line)
    return None


def build_triage_records(signed_triage: dict, texts: dict, as_slug: str, memory_root: str,
                         grammar) -> list:
    """P4 — the signed triage verdict, in the `--as` folder under EITHER policy set.

    An id the target tree already disposes in any file plans nothing, which is what makes the verb
    idempotent: a second run over a written tree writes a second time nothing.
    """
    disposed = read_disposed(texts, grammar)
    out = []
    for ident, disp in sorted(signed_triage.items()):
        if ident in disposed:
            continue
        out.append(Record(read_slug_home(memory_root, as_slug), backlog.H_DISPOSITIONS,
                          backlog.render_status_row(disp.verb, ident, disp.why, disp.value),
                          ident, ""))
    return out


def read_disposed(texts: dict, grammar) -> dict:
    """`{id: [path]}` — every target that any file already carries a STATUS row for."""
    out: dict = collections.defaultdict(list)
    for rel, text in sorted(texts.items()):
        for raw in text.split(NEWLINE):
            row = backlog.extract_row(raw.rstrip(chr(13)), grammar)
            if row is not None and row.cls == "status":
                out[row.target].append(rel)
    return out


def check_collisions(records: list, texts: dict, grammar) -> tuple:
    """V4 — one file states one status per target. A planned collision is NEEDS-HUMAN (F10).

    The landing form's REPLACEMENT is already carried on the record, so a record that names the row
    it replaces is not a collision: it IS the edit unit 6 section 4 sanctions.
    """
    disposed = read_disposed(texts, grammar)
    kept, bad = [], []
    for rec in records:
        # A `replaces` the file does NOT hold is not a replacement — it is an insertion whose
        # candidate row the receiving branch edited (section 8 F10's own exclusion). Treating it as
        # a replacement would land a second status row beside the edited one and red V4 at the
        # reconcile's `--check`, which is the collision this function exists to refuse.
        here = [ln.rstrip(chr(13)) for ln in texts.get(rec.path, "").split(NEWLINE)]
        present = bool(rec.replaces) and rec.replaces in here
        if rec.section != backlog.H_DISPOSITIONS or present:
            kept.append(rec)
            continue
        row = backlog.extract_row(rec.text, grammar)
        if row is not None and row.cls == "status" and rec.path in disposed.get(rec.ident, []):
            bad.append((rec.ident, f"{rec.path} already states a status for {rec.ident}, and one "
                                   f"file carries one status row per target"))
            continue
        kept.append(rec)
    dead = {ident for ident, _why in bad}
    return [r for r in kept if r.ident not in dead], bad


def build_cutoff(conf: dict, filed: dict, records: list) -> str:
    """`ASK_CUTOFF` after a landing: the LATER of the current value and the day after every `filed`.

    Never simply the day after the newest ask. A landing that LOWERED the cutoff would re-arm V9
    and V12 over every ask the switch-over already migrated, which only a fixture carrying a later
    current value can see.
    """
    import datetime
    current = backlog.read_conf(conf).cutoff or ""
    wrote = sorted({filed[r.ident] for r in records
                    if r.section == backlog.H_ASKS and r.ident in filed})
    if not wrote:
        return current
    newest = datetime.date.fromisoformat(wrote[-1]) + datetime.timedelta(days=1)
    return max(current, newest.isoformat())


def read_filed_days(root: str, ours: str, theirs: list, ids: set) -> dict:
    """`{id: YYYY-MM-DD}` — the author day of the OLDEST lineage commit whose blob holds the id.

    NOT the merge's day and not today's. An ask filed in March and relocated in September was
    asked for in March, and a `filed` value taken from the relocation run re-dates the whole corpus
    against `ASK_CUTOFF`. The walk is unit 9's own — its lineage, its watched paths and its anchor
    grammar — so the commits read here are exactly the commits the delta read.
    """
    if not ids:
        return {}
    base = pathlib.Path(root)
    walk = audit.Walk(base, [ours, *theirs])
    anchor, grammar = walk.resolve_grammar()
    lineage, _bases = audit.derive_lineage(walk.parents, ours, list(theirs), walk.anc)
    mine = sorted(lineage & walk.touching, key=lambda s: walk.pos.get(s, 0), reverse=True)
    if not mine:
        return {}
    versions = audit.read_versions(base, mine, walk.paths, anchor, grammar)
    days = {}
    for line in run("git", "log", "--no-walk", "--format=%H %ad", "--date=format:%Y-%m-%d",
                    *mine, cwd=root).split(NEWLINE):
        bits = line.split()
        if len(bits) == 2:
            days[bits[0]] = bits[1]
    filed: dict = {}
    for sha in mine:
        rows = versions.get(sha, {})
        for ident in ids:
            if ident not in filed and ident in rows and days.get(sha):
                filed[ident] = days[sha]
    return filed


def build_table(verdicts: list, records: list, before, after) -> list:
    """The conservation table: id, kind, classification, records, file, status before and after."""
    by_id: dict = collections.defaultdict(list)
    for rec in records:
        by_id[rec.ident].append(rec.path)
    rows = []
    for verdict in verdicts:
        paths = sorted(set(by_id.get(verdict.ident, []))) or ["-"]
        rows.append(f"  {verdict.ident} · {verdict.kind} · {verdict.classification} · "
                    f"{len(by_id.get(verdict.ident, []))} record(s) · {' '.join(paths)} · "
                    f"{before.statuses.get(verdict.ident) or '-'}"
                    f"{backlog.ARROW}{after.statuses.get(verdict.ident) or '-'}")
    return rows


# --------------------------------------------------------------------------------- the writer
def set_other_side(root: str, conf: dict, theirs: list) -> list:
    """S11 — every view path and every family backlog archive set to the OTHER side's version.

    After a transition merge a view carries conflict markers or authored rows and an archive
    carries a modify/delete conflict; the generator's data-loss guard reads both and refuses. The
    archive population is `build_rotated_archive_re`, the ONE derivation this module keeps of the
    rotated-family predicate — the same names the hygiene engine's `--print-rotated-archive-ere`
    selects under the family alternation, minus the decision log, which no family owns.
    """
    m = conf["MEMORY_ROOT"]
    families = derive_families(conf)
    rot = build_rotated_archive_re(m, families)
    other = theirs[0]
    wanted = {f"{m}/backlog/{f}.md" for f in families}
    for rev in [other, "HEAD"]:
        for rel in run("git", "ls-tree", "-r", "--name-only", rev, "--", f"{m}/archive/",
                       cwd=root).split(NEWLINE):
            if rel.strip() and rot.fullmatch(rel.strip()):
                wanted.add(rel.strip())
    at_other = {rel.strip() for rel in run("git", "ls-tree", "-r", "--name-only", other, "--",
                                           f"{m}/", cwd=root).split(NEWLINE) if rel.strip()}
    touched = []
    for rel in sorted(wanted):
        if rel in at_other:
            run("git", "checkout", other, "--", rel, cwd=root)
        else:
            code, _out = run_unchecked("git", "rm", "-q", "-f", "--ignore-unmatch", "--", rel, cwd=root)
            if code != 0:
                continue
        touched.append(rel)
    return touched


def render_views(root: str) -> None:
    """`gen_build_index.py --write`, as a PROCESS and not an import.

    The generator resolves its root from the working directory and this engine may be planning a
    tree that is not the module's own; a subprocess with an explicit `cwd` is the only invocation
    that cannot pick up the wrong one.
    """
    code, out = run_unchecked(sys.executable, os.path.join(_HERE, "gen_build_index.py"), "--write",
                        cwd=root)
    if code != 0:
        raise Problem(f"migrate-backlog: the view render refused, so the relocation stops before "
                      f"writing a row into a tree whose views are unreadable:{NEWLINE}{out}")


def write_relocation(root: str, plan: Relocation, conf: dict) -> list:
    """Every planned record onto disk and into the index, then nothing else."""
    memory_root = conf["MEMORY_ROOT"]
    texts = read_target_texts(root, conf)
    final = build_texts_with(texts, plan.records, memory_root)
    written = sorted({r.path for r in plan.records})
    for rel in written:
        write_file(os.path.join(root, rel), final[rel])
    if written:
        run("git", "add", "--", *written, cwd=root)
    return written


def check_accounted(root: str, plan: Relocation, conf: dict) -> list:
    """S3 — re-read the tree through unit 9's accounting predicate. One row per entry, or refuse.

    THE PREDICATE IS UNIT 9's and is not re-implemented here. What this asserts is that the rows
    this verb just wrote are the rows that unit's audit will read at the commit — the same
    question, asked by the same function, before the operator finds out from a hook.
    """
    verdicts = audit.accounted(plan.entries, audit.INDEX, pathlib.Path(root))
    bad = []
    for idx, entry in enumerate(plan.entries):
        got = verdicts.get(idx)
        if got != "ok":
            bad.append(f"  {entry['id']} ({entry['kind']}, changed by {entry['change'][:12]}): "
                       f"{'no RELOCATED row names it' if got == 'none' else 'named by ' + str(got)}")
    return bad


# ----------------------------------------------------------------------------------- the verbs
def print_plan_lines(plan: Relocation, root: str, args: dict) -> None:
    print(f"migrate-backlog: {plan.form.name} · policy set {plan.form.policy} · "
          f"{len(plan.entries)} delta entr(ies) · {len(plan.records)} record(s)")
    for line in plan.table:
        print(line)
    for rec in plan.records:
        print(f"  + {rec.path} · {rec.text}")
    for ident, why in plan.human:
        print(f"  {HUMAN} {ident}: {why}")
    for ident, was, now in plan.confirm:
        print(f"  CONFIRM {ident}: {was}{backlog.ARROW}{now} — pass --confirm {ident}")
    if plan.cutoff:
        print(f"ASK_CUTOFF={plan.cutoff}")


def build_rerun(args: dict, plan: Relocation) -> str:
    """The exact command that re-runs this plan with every refusal answered."""
    head = f"python {index.kit_rel()}/migrate_backlog.py {args['mode']}"
    if args["ref"]:
        head += f" {args['ref']}"
    if args["from"]:
        head += f" --from {args['from']}"
    head += f" --as {args['as_slug']}"
    for ident, _why in plan.human:
        head += f" --drop {ident}=<why>"
    for ident, _was, _now in plan.confirm:
        head += f" --confirm {ident}"
    return head


def cmd_relocate(root: str, args: dict) -> int:
    """The three writing verbs, which differ only in how their sides resolve and what they confirm.

    THE TREE IS TOUCHED ONLY ON THE WRITING PATH. S11's restore and the render run AFTER the plan
    is known to be clean and BEFORE the table prints, because a refusal must leave `git status`
    exactly as the merge left it (AC2) — a verb that repaired the views and then refused would hand
    the operator a half-acted tree and tell them nothing was written.
    """
    conf = read_index(index.load_conf, root)
    if not backlog.SLUG_RE.match(args["as_slug"] or ""):
        raise Refusal(f"migrate-backlog: --as takes a build slug — a node tag and a CamelCase "
                      f"adjective-noun, `[A-Za-z0-9]` with at least one capital — not "
                      f"'{args['as_slug']}'")
    form, ours, theirs = resolve_sides(root, args)
    if form.policy != MIGRATION_SET and (args["signed"] or args["triage_ask"]):
        raise Refusal(f"migrate-backlog: --signed and --triage-ask belong to the migration policy "
                      f"set, which only --write and the landing form of --ingest run. This is "
                      f"{form.name}.")
    plan = build_relocation(root, form, ours, theirs, args, conf)
    if args["dry_run"] or plan.human or plan.confirm:
        print_plan_lines(plan, root, args)
    if args["dry_run"]:
        if plan.human or plan.confirm:
            print(f"migrate-backlog: DRY RUN — this plan refuses. Re-run: {build_rerun(args, plan)}")
            return 1
        if not plan.records:
            print("migrate-backlog: DRY RUN — the plan is EMPTY: every delta entry is already "
                  "accounted at this tree, so a write would write nothing. This is exit 2 and not "
                  "1 deliberately, so a caller that re-runs unless the rehearsal refused still "
                  "re-runs.")
            return 2
        print("migrate-backlog: DRY RUN — nothing written; this plan would write "
              f"{len(plan.records)} record(s)")
        return 0
    if plan.human or plan.confirm:
        print(f"migrate-backlog: REFUSED — nothing written. Re-run: {build_rerun(args, plan)}")
        return 1
    if form.verb == "--relocate":
        touched = set_other_side(root, conf, theirs)
        render_views(root)
        # RE-STAGED AFTER THE RENDER, not before it. The restore stages the other side's blob and
        # the render then rewrites the same file, so a run that staged only the restore would leave
        # every view `MM` — staged at one content, on disk at another — which is the state an
        # operator reads as "the relocation half-finished".
        alive = [rel for rel in touched if os.path.isfile(os.path.join(root, rel))]
        if alive:
            run("git", "add", "--", *alive, cwd=root)
    written = write_relocation(root, plan, conf)
    bad = check_accounted(root, plan, conf)
    if bad:
        print("migrate-backlog: the records are written but the accounting re-read does not "
              "accept them, so this merge would still red check 25:")
        print(NEWLINE.join(bad))
        return 1
    print_plan_lines(plan, root, args)
    print(f"migrate-backlog: wrote {len(plan.records)} record(s) into "
          f"{len(written)} file(s) — {' '.join(written) if written else 'none'}")
    return 0


def cmd_stragglers(root: str, args: dict) -> int:
    """S8 — every ref still carrying an unaccounted row change against the default branch."""
    if run("git", "rev-parse", "--is-shallow-repository", cwd=root).strip() == "true":
        print("migrate-backlog: DEAD PROBE — this is a shallow clone, so a ref's history is "
              "truncated and every delta would be computed against a graft the walk cannot see")
        return 1
    scope = ["refs/heads"] if args["local"] else ["refs/heads", "refs/remotes"]
    refs = []
    for line in run("git", "for-each-ref", "--format=%(refname)", *scope, cwd=root).split(NEWLINE):
        ref = line.strip()
        if ref and not ref.endswith("/HEAD"):
            refs.append(ref)
    # THE REF POPULATION IS READ BEFORE THE DEFAULT BRANCH. A repository holding no ref holds no
    # default branch either, and resolving that first would report the missing branch — a REFUSAL,
    # exit 2 — where the honest answer is that this probe examined nothing.
    if not refs:
        print(f"migrate-backlog: DEAD PROBE — {' and '.join(scope)} hold no ref at all, so this "
              f"inventory would report zero stragglers without examining anything")
        return 1
    name, tip = resolve_default_tip(root)
    flagged, graph = scan_candidates(root, refs, tip)
    conf = read_index(index.load_conf, root)
    listed = []
    for ref in refs:
        sha = read_rev(root, ref)
        if not sha or sha == tip or not check_reaches(graph, sha, flagged):
            continue
        entries = audit.delta(sha, tip, root)
        if not entries:
            continue
        verdicts = audit.accounted(entries, tip, pathlib.Path(root))
        open_ones = [e for i, e in enumerate(entries) if verdicts.get(i) != "ok"]
        if open_ones:
            listed.append((ref, sha, len(open_ones), open_ones[0]["change"]))
    for ref, sha, count, change in listed:
        if args["tsv"]:
            print(f"straggler\t{ref}\t{sha}\t{count}\t{change}")
        else:
            print(f"straggler — {ref} · {sha[:12]} · {count} unaccounted · "
                  f"first change {change[:12]}")
    if args["tsv"]:
        print(f"examined\t{len(refs)}")
    else:
        print(f"migrate-backlog: examined {len(refs)} ref(s) against {name} at {tip[:12]} · "
              f"{len(listed)} straggler(s) · {_PROCESSES[0]} git process(es)")
    if not args["tsv"]:
        for line in read_recipe(root, conf):
            print("  " + line)
    return 0


def scan_candidates(root: str, refs: list, tip: str) -> tuple:
    """`(flagged commits, parent graph)` — two processes for every ref together (section 8 F11).

    THE WATCHED PATHS HERE ARE A DELIBERATE SUPERSET of unit 9's, which exclude every archive that
    is not family-named. One broad `git log` beats one pathspec per family, and a candidate whose
    delta turns out empty is simply not listed — the delta is unit 9's and this walk only decides
    whom to ask.

    `--source` is NOT used: it labels each commit with the first ref that reached it, so a pushed
    copy or a fork of a straggler would never be a candidate.
    """
    conf = read_index(index.load_conf, root)
    m = conf["MEMORY_ROOT"]
    flagged = {line.strip() for line in run(
        "git", "log", "--format=%H", *refs, "--not", tip, "--",
        f"{m}/backlog/", f"{m}/archive/", cwd=root).split(NEWLINE) if line.strip()}
    graph: dict = {}
    for line in run("git", "rev-list", "--parents", *refs, cwd=root).split(NEWLINE):
        bits = line.split()
        if bits:
            graph[bits[0]] = bits[1:]
    return flagged, graph


def check_reaches(graph: dict, tip: str, flagged: set) -> bool:
    """Does this tip reach a flagged commit? Computed IN MEMORY over the one parent graph, so a ref
    with no such commit costs no delta at all and two refs sharing a straggler are both candidates."""
    if not flagged:
        return False
    seen, stack = {tip}, [tip]
    while stack:
        sha = stack.pop()
        if sha in flagged:
            return True
        for parent in graph.get(sha, ()):
            if parent not in seen:
                seen.add(parent)
                stack.append(parent)
    return False


def cmd_recipe(root: str) -> int:
    """S10 — the recipe, from the ONE constant unit 7 keeps, holding no copy of its own."""
    for line in read_recipe(root):
        print(line)
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


# ------------------------------------------------------- the relocation engine's own fixtures
#: The four hold rows AC12 grades under BOTH policy sets. Shared with `seed_corpus` below rather
#: than copied into it: the planner's census and this engine's classifier answer the same question
#: about these four rows, and two spellings of one corpus is how they would come to disagree.
HOLD_ROWS = (
    "- EXMP-aFoo-2 · OPEN · an ask nothing in this corpus closes",
    "- EXMP-aFoo-3 · BLOCKED · held until EXMP-aFoo-2 lands, and then it can move",
    "- EXMP-aFoo-5 · DEFERRED · only on the owner's word, naming nothing",
    "- EXMP-aFoo-8 · BLOCKED · blocked on EXMP-dRuling-9, a decision id nothing files",
)

#: The transition fixture's three days, DISTINCT by construction. `filed` is mined from the oldest
#: lineage commit holding the row, so a fixture whose commits shared a day could not tell the right
#: source from the merge day or from the relocation run's own.
DAY_SEED, DAY_STRAG, DAY_LATER, DAY_HEAD = ("2026-03-01", "2026-04-02", "2026-04-20",
                                             "2026-05-03")

FX_SEED_ROWS = (
    "- EXMP-aFoo-1 · OPEN · the first ask, which the straggler closes",
    "- EXMP-aFoo-2 · OPEN · the second ask, pointing at memory/gone/old.md",
)
FX_STRAG_ROWS = (
    "- EXMP-aFoo-1 · CLOSED · the first ask, which the straggler closes",
    "- EXMP-aFoo-2 · OPEN · the second ask, pointing at memory/here/new.md",
    "- EXMP-aFoo-3 · OPEN · a brand new ask the straggler filed",
)
FX_HEAD_ASKS = (
    "- EXMP-aFoo-1 · filed 2026-03-01 · the first ask, which the straggler closes",
    "- EXMP-aFoo-2 · filed 2026-03-01 · the second ask, pointing at memory/gone/old.md",
)


def render_transition_conf(mode: str = "shards", cutoff: str = "") -> str:
    """The fixture conf. `ROTATION_MODE` is declared because section 4 reads shard and archive as
    ONE population under cut-mode rotation, which AC11 stages."""
    out = (render_conf() + 'ROTATION_MODE="cut"' + NEWLINE
           + f'{backlog.MODE_KEY}="{mode}"' + NEWLINE)
    if cutoff:
        out += f'{backlog.CUTOFF_KEY}="{cutoff}"' + NEWLINE
    return out


def read_kit_root() -> str:
    """The repository THIS MODULE is installed in — the fixtures' source, never their subject.

    Deliberately not `resolve_root()`, which answers "which repo is being planned": the arms below
    seed scratch repositories and need the tree the kit itself lives in to copy its sibling out of.
    """
    return run("git", "rev-parse", "--show-toplevel", cwd=_HERE).strip()


def seed_recall_kit(tree: str) -> None:
    """The memory-recall sibling, inside the fixture, because unit 9 keys every row through it.

    The SOURCE is resolved by that unit's own resolver from this repository's root, so nothing here
    spells a sibling kit's install path; the destination is its own basename at the fixture root,
    which is the second layout that resolver accepts.
    """
    import shutil
    src = audit.resolve_recall_kit(pathlib.Path(read_kit_root()))
    dst = os.path.join(tree, src.name)
    os.makedirs(dst, exist_ok=True)
    for name in ("extract.py", "recall_conf.py"):
        shutil.copyfile(str(src / name), os.path.join(dst, name))


def run_commit_on(tree: str, message: str, files: dict, day: str = "",
                  removals=()) -> str:
    """One dated fixture commit. The date is the AUTHOR date `filed` is mined from."""
    for rel in removals:
        path = os.path.join(tree, rel)
        if os.path.isfile(path):
            os.remove(path)
    for rel, text in files.items():
        write_file(os.path.join(tree, rel), text)
    env = dict(os.environ)
    if day:
        env["GIT_AUTHOR_DATE"] = day + "T12:00:00 +0000"
        env["GIT_COMMITTER_DATE"] = day + "T12:00:00 +0000"
    run("git", "add", "-A", cwd=tree)
    run("git", "commit", "-q", "-m", message, "--no-verify", cwd=tree, env=env)
    return run("git", "rev-parse", "HEAD", cwd=tree).strip()


def render_build_backlog(slug: str, asks=(), rows=()) -> str:
    body = [f"# {slug} — asks"]
    if asks:
        body += ["", backlog.H_ASKS, ""] + list(asks)
    if rows:
        body += ["", backlog.H_DISPOSITIONS, ""] + list(rows)
    return NEWLINE.join(body) + NEWLINE


def seed_shards_base(tree: str, rows, slugs=("aFoo", "aWho"), conf_text: str = "",
                     extra=None) -> str:
    """The pre-flip seed both fixture shapes start from: one shards-mode tree with one shard."""
    init_repo(tree)
    seed_recall_kit(tree)
    files = {
        ".memory-tree.conf": conf_text or render_transition_conf("shards"),
        "README.md": "fixture" + NEWLINE,
        "memory/backlog/EXMP.md": render_shard("EXMP", list(rows)),
        "memory/backlog/OTHR.md": render_shard("OTHR", []),
        "memory/project/stale-header-waiver.txt": WAIVER,
    }
    for slug in slugs:
        files[f"memory/builds/{slug}/README.md"] = render_readme(slug, status="OPEN")
    files.update(extra or {})
    return run_commit_on(tree, "seed: the pre-flip corpus", files, day=DAY_SEED)


def seed_transition(base: str, name: str, seed_rows=FX_SEED_ROWS, strag_rows=FX_STRAG_ROWS,
                    head_asks=FX_HEAD_ASKS, head_rows=(), slugs=("aFoo", "aWho"),
                    strag_files=None, strag_removals=(), head_files=None,
                    head_slug: str = "aFoo", seed_extra=None) -> tuple:
    """The straggler shape: a shards-mode seed, a branch that kept editing the shard, and a default
    branch that switched over. -> `(tree, seed sha, straggler sha, default sha)`."""
    tree = os.path.join(base, name)
    b0 = seed_shards_base(tree, seed_rows, slugs, extra=seed_extra)
    run("git", "checkout", "-q", "-b", "strag", cwd=tree)
    files = {"memory/backlog/EXMP.md": render_shard("EXMP", list(strag_rows))}
    files.update(strag_files or {})
    s1 = run_commit_on(tree, "strag: the rows this branch kept editing", files, day=DAY_STRAG,
                       removals=strag_removals)
    # A SECOND, LATER COMMIT THAT TOUCHES THE SHARD AND CHANGES NO ROW. Without it the straggler's
    # lineage holds ONE commit touching the watched paths, the oldest and the newest are the same
    # commit, and an arm grading `filed` cannot tell the two apart — a fixture that certifies
    # coverage it does not have.
    run_commit_on(tree, "strag: a later commit that edits the shard's prose alone",
                  {"memory/backlog/EXMP.md": render_shard("EXMP", list(strag_rows)).replace(
                      "> Mutable.", "> Mutable. Edited later, changing no row.")},
                  day=DAY_LATER)
    run("git", "checkout", "-q", "main", cwd=tree)
    files = {".memory-tree.conf": render_transition_conf("builds"),
             f"memory/builds/{head_slug}/BACKLOG.md": render_build_backlog(
                 head_slug, head_asks, head_rows)}
    files.update(head_files or {})
    for rel, text in files.items():
        write_file(os.path.join(tree, rel), text)
    for rel in ("memory/backlog/EXMP.md", "memory/backlog/OTHR.md"):
        path = os.path.join(tree, rel)
        if os.path.isfile(path):
            os.remove(path)
    render_views(tree)
    m1 = run_commit_on(tree, "main: the switch-over", {}, day=DAY_HEAD)
    return tree, b0, s1, m1


def seed_landing(base: str, name: str, tip_rows, seed_rows=FX_SEED_ROWS,
                 head_asks=FX_HEAD_ASKS, head_rows=(), cutoff: str = "",
                 slugs=("aFoo", "aWho"), head_slug: str = "aFoo") -> tuple:
    """The LANDING shape (S6): a shards-mode default tip under a builds-mode HEAD.

    `origin/HEAD` is written into the fixture, because the landing form admits a ref only when it
    IS the default tip and that resolution is the pre-push hook's — observed first, environment
    only as a cross-check.
    """
    tree = os.path.join(base, name)
    seed_shards_base(tree, seed_rows, slugs)
    run("git", "checkout", "-q", "-b", "flip", cwd=tree)
    files = {".memory-tree.conf": render_transition_conf("builds", cutoff),
             f"memory/builds/{head_slug}/BACKLOG.md": render_build_backlog(
                 head_slug, head_asks, head_rows)}
    for rel, text in files.items():
        write_file(os.path.join(tree, rel), text)
    for rel in ("memory/backlog/EXMP.md", "memory/backlog/OTHR.md"):
        os.remove(os.path.join(tree, rel))
    render_views(tree)
    flip = run_commit_on(tree, "flip: the switch-over", {}, day=DAY_HEAD)
    run("git", "checkout", "-q", "main", cwd=tree)
    tip = run_commit_on(tree, "main: the rows the default branch kept editing",
                        {"memory/backlog/EXMP.md": render_shard("EXMP", list(tip_rows))},
                        day=DAY_STRAG)
    run("git", "update-ref", "refs/remotes/origin/main", tip, cwd=tree)
    run("git", "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main", cwd=tree)
    run("git", "checkout", "-q", "flip", cwd=tree)
    return tree, flip, tip


def read_backlogs(tree: str) -> dict:
    """`{slug: text}` for every per-build backlog file on disk. The arms' comparison unit."""
    out = {}
    root = os.path.join(tree, "memory", "builds")
    for slug in sorted(os.listdir(root)) if os.path.isdir(root) else []:
        path = os.path.join(root, slug, "BACKLOG.md")
        if os.path.isfile(path):
            out[slug] = read_text(path)
    return out


def run_engine(tree: str, argv: list) -> tuple:
    """One CLI run of the relocation engine, in-process. -> `(exit code, everything it printed)`."""
    buf = io.StringIO()
    code = 0
    try:
        args = read_args(argv)
        with redirect_stdout(buf):
            if args["mode"] == "--stragglers":
                code = cmd_stragglers(tree, args)
            elif args["mode"] == "--recipe":
                code = cmd_recipe(tree)
            else:
                code = cmd_relocate(tree, args)
    except Problem as exc:
        return getattr(exc, "code", 1), buf.getvalue() + str(exc)
    return code, buf.getvalue()


def run_audit(tree: str, staged: bool = False) -> int:
    """Hygiene check 25's own module over a fixture, IN PROCESS and against an explicit root.

    NOT the CLI. That entry point resolves its repository from the module's own location, so a
    subprocess launched with `cwd=<fixture>` would audit THIS repository instead and return a
    verdict about the wrong tree — which reads exactly like a passing arm. Measured: the first cut
    of these arms reported a clean fixture that had never been looked at.
    """
    root = pathlib.Path(tree)
    buf = io.StringIO()
    with redirect_stdout(buf):
        if staged:
            return audit.cmd_staged(root)
        tip = run("git", "rev-parse", "HEAD", cwd=tree).strip()
        return audit.print_report(audit.scan_history(root, [tip], False, tip), False)


def seed_corpus(tmp: str) -> None:
    """The shared fixture: one repo with real history, holding one case per selector and refusal."""
    init_repo(tmp)
    seed_rows = [
        "- EXMP-aFoo-1 · OPEN · a planner module that reads legacy rows and reports evidence",
        HOLD_ROWS[0],
        HOLD_ROWS[1],
        "- EXMP-aFoo-4 · BLOCKED · blocked on -4 and -11, shorthand the corpus cannot resolve",
        HOLD_ROWS[2],
        "- EXMP-aFoo-6 · CLOSED · a terminal row carrying its own reason",
        "- EXMP-aFoo-7 · WONTDO · declined, and here is the reason it was declined",
        HOLD_ROWS[3],
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
        # ============================================== the relocation engine (unit 12)
        # HERMETIC AGAINST THIS MACHINE'S ENVIRONMENT. Every fixture that resolves a default branch
        # cross-checks the observed one against `GOV_DEFAULT_BRANCH`, so an ambient value naming
        # another branch would refuse arms that have nothing to do with it. Dropped here, set where
        # an arm needs it, and put back at the end of the section.
        prior_default = os.environ.pop("GOV_DEFAULT_BRANCH", None)
        # ---- AC1: the three side resolutions, one delta, records that agree byte for byte.
        fa, _fa0, fa_change, _fa1 = seed_transition(base, "rel_merge_head")
        run("git", "checkout", "-q", "strag", cwd=fa)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fa)
        rc_a, out_a = run_engine(fa, ["--relocate", "--as", "aWho"])
        books_a = read_backlogs(fa)
        arm("--relocate over a fresh transition merge exits 0", 0, lambda: rc_a)
        arm("the relocated new ask is filed in ITS OWN id's build folder",
            "- EXMP-aFoo-3 · filed " + DAY_STRAG, lambda: books_a.get("aFoo", ""))
        arm("its filed is the day the row was first added, not the merge's day",
            False, lambda: DAY_HEAD in books_a.get("aFoo", ""))
        arm("and not the day of the LATER lineage commit that also held the row",
            False, lambda: DAY_LATER in books_a.get("aFoo", ""))
        arm("the CLOSED disposition cites the CHANGE commit, never the merge",
            f"- CLOSED · EXMP-aFoo-1 · by {fa_change}", lambda: books_a.get("aWho", ""))
        arm("the repointed ask text carries the straggler's new path",
            "memory/here/new.md", lambda: books_a.get("aFoo", ""))
        arm("and no longer carries the old one",
            False, lambda: "memory/gone/old.md" in books_a.get("aFoo", ""))
        arm("every delta entry gets exactly one RELOCATED row",
            3, lambda: books_a.get("aWho", "").count("- RELOCATED · "))
        arm("each one in the --as folder, which is the writer's own",
            0, lambda: books_a.get("aFoo", "").count("- RELOCATED · "))
        run("git", "add", "-A", cwd=fa)
        arm("the pending merge then passes the transition audit against the index",
            0, lambda: run_audit(fa, staged=True))

        fb, _fb0, _fb1, _fb2 = seed_transition(base, "rel_concluded")
        run("git", "checkout", "-q", "strag", cwd=fb)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fb)
        run("git", "checkout", "main", "--", "memory/backlog/EXMP.md", cwd=fb)
        run("git", "commit", "-q", "-m", "merge the default branch", "--no-verify", cwd=fb)
        rc_b, _out_b = run_engine(fb, ["--relocate", "--as", "aWho"])
        arm("the concluded-merge form resolves the same two sides and exits 0", 0, lambda: rc_b)
        arm("and its records are byte-identical to the MERGE_HEAD run's",
            True, lambda: read_backlogs(fb) == books_a)

        fc, _fc0, _fc1, _fc2 = seed_transition(base, "rel_from")
        rc_c0, out_c0 = run_engine(fc, ["--relocate", "--from", "strag", "--as", "aWho"])
        arm("--relocate --from takes S5's confirmation, so an unconfirmed flip refuses",
            1, lambda: rc_c0)
        arm("naming the id and the option that answers it",
            "CONFIRM EXMP-aFoo-1: OPEN → CLOSED — pass --confirm EXMP-aFoo-1", lambda: out_c0)
        rc_c, _out_c = run_engine(fc, ["--relocate", "--from", "strag", "--as", "aWho",
                                         "--confirm", "EXMP-aFoo-1"])
        arm("the --from form writes once its status change is confirmed", 0, lambda: rc_c)
        arm("and its records are byte-identical to the other two forms'",
            True, lambda: read_backlogs(fc) == books_a)

        # ---- AC2: one unclassifiable prose change refuses the WHOLE plan, and --drop answers it.
        amend_seed = list(FX_SEED_ROWS) + [
            "- EXMP-aFoo-4 · OPEN · the fourth ask, whose prose this branch rewrites"]
        amend_strag = list(FX_STRAG_ROWS) + [
            "- EXMP-aFoo-4 · OPEN · a wholly different sentence about marmalade windmills"]
        amend_head = list(FX_HEAD_ASKS) + [
            "- EXMP-aFoo-4 · filed 2026-03-01 · the fourth ask, whose prose this branch rewrites"]
        fd, _fd0, _fd1, _fd2 = seed_transition(base, "rel_amended", seed_rows=amend_seed,
                                               strag_rows=amend_strag, head_asks=amend_head)
        run("git", "checkout", "-q", "strag", cwd=fd)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fd)
        before_status = run("git", "status", "--porcelain", cwd=fd)
        books_before = read_backlogs(fd)
        rc_d, out_d = run_engine(fd, ["--relocate", "--as", "aWho"])
        arm("an unclassifiable prose change refuses the whole plan", 1, lambda: rc_d)
        arm("naming the id under NEEDS-HUMAN", "NEEDS-HUMAN EXMP-aFoo-4", lambda: out_d)
        arm("and printing the exact --drop re-run", "--drop EXMP-aFoo-4=<why>", lambda: out_d)
        arm("the refusal writes NOTHING: every record file is exactly as it was",
            True, lambda: read_backlogs(fd) == books_before)
        arm("and the tree is exactly as the merge left it",
            True, lambda: run("git", "status", "--porcelain", cwd=fd) == before_status)
        rc_d2, _out_d2 = run_engine(fd, ["--relocate", "--as", "aWho",
                                           "--drop", "EXMP-aFoo-4=a human read it and let it go"])
        arm("re-run with --drop it exits 0", 0, lambda: rc_d2)
        arm("and writes one dropped row for that id, and no other record for it",
            1, lambda: read_backlogs(fd).get("aWho", "").count(
                "- RELOCATED · EXMP-aFoo-4 · by "))
        arm("that row is the dropped disposal carrying the human's reason",
            "dropped: a human read it and let it go", lambda: read_backlogs(fd).get("aWho", ""))

        # ---- AC3 and AC15: lab case e09b, through --repair, --ingest and --relocate --from.
        reopen_row = "- REOPEN · EXMP-aFoo-1 · of aFoo · the default branch reopened this on purpose"
        fe, _fe0, _fe1, _fe2 = seed_transition(base, "rel_reopen", head_rows=(reopen_row,))
        run("git", "checkout", "-q", "strag", cwd=fe)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fe)
        run("git", "checkout", "main", "--", "memory/backlog/EXMP.md", cwd=fe)
        run("git", "commit", "-q", "-m", "merge the default branch", "--no-verify", cwd=fe)
        fe_merge = run("git", "rev-parse", "HEAD", cwd=fe).strip()
        rc_e0, out_e0 = run_engine(fe, ["--repair", fe_merge, "--as", "aWho"])
        arm("--repair refuses a status-changing record over a deliberate reopen", 1, lambda: rc_e0)
        arm("naming the id, the status before and after, and --confirm",
            "CONFIRM EXMP-aFoo-1: OPEN → CLOSED — pass --confirm EXMP-aFoo-1", lambda: out_e0)
        arm("while the uncontested new ask is not held for confirmation",
            False, lambda: "CONFIRM EXMP-aFoo-3" in out_e0)
        rc_e1, _out_e1 = run_engine(fe, ["--repair", fe_merge, "--as", "aWho",
                                           "--confirm", "EXMP-aFoo-1"])
        arm("--repair writes once the id is confirmed", 0, lambda: rc_e1)
        arm("including the uncontested new ask, which needed no confirmation",
            "- EXMP-aFoo-3 · filed ", lambda: read_backlogs(fe).get("aFoo", ""))

        ff, _ff0, _ff1, _ff2 = seed_transition(base, "rel_reopen_ingest", head_rows=(reopen_row,))
        rc_f0, out_f0 = run_engine(ff, ["--ingest", "strag", "--as", "aWho"])
        arm("the straggler form of --ingest refuses the same contested id", 1, lambda: rc_f0)
        arm("naming it and --confirm too",
            "CONFIRM EXMP-aFoo-1: OPEN → CLOSED — pass --confirm EXMP-aFoo-1", lambda: out_f0)
        rc_f1, out_f1 = run_engine(ff, ["--relocate", "--from", "strag", "--as", "aWho"])
        arm("AC15: --relocate --from refuses it through the sibling write path", 1, lambda: rc_f1)
        arm("with the same id, statuses and option named",
            "CONFIRM EXMP-aFoo-1: OPEN → CLOSED — pass --confirm EXMP-aFoo-1", lambda: out_f1)
        rc_f2, _out_f2 = run_engine(ff, ["--relocate", "--from", "strag", "--as", "aWho",
                                           "--confirm", "EXMP-aFoo-1"])
        arm("and writes once confirmed", 0, lambda: rc_f2)

        # ---- AC4: an unaccounted transition, the repair that closes it, and its idempotence.
        fg, _fg0, _fg1, _fg2 = seed_transition(base, "rel_unaccounted")
        run("git", "checkout", "-q", "strag", cwd=fg)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fg)
        run("git", "checkout", "main", "--", "memory/backlog/EXMP.md", cwd=fg)
        run("git", "commit", "-q", "-m", "merge the default branch", "--no-verify", cwd=fg)
        fg_merge = run("git", "rev-parse", "HEAD", cwd=fg).strip()
        arm("a transition committed unaccounted reds check 25's own module",
            1, lambda: run_audit(fg))
        rc_g, _out_g = run_engine(fg, ["--repair", fg_merge, "--as", "aWho",
                                         "--confirm", "EXMP-aFoo-1"])
        arm("--repair writes the records it names", 0, lambda: rc_g)
        run("git", "add", "-A", cwd=fg)
        run("git", "commit", "-q", "-m", "records: the repair", "--no-verify", cwd=fg)
        arm("after which the audit accepts the same transition", 0, lambda: run_audit(fg))
        rc_g2, out_g2 = run_engine(fg, ["--repair", fg_merge, "--as", "aWho", "--dry-run"])
        arm("a second --repair plans ZERO records, because every entry is accounted",
            "the plan is EMPTY", lambda: out_g2)
        arm("and says so with exit 2 rather than 1 (AC7)", 2, lambda: rc_g2)

        # ---- AC5: an ingested ref stops being listed while it is still unmerged.
        fh, _fh0, _fh1, _fh2 = seed_transition(base, "rel_ingest")
        os.environ["GOV_DEFAULT_BRANCH"] = "main"
        try:
            _rc, out_h0 = run_engine(fh, ["--stragglers"])
            arm("the inventory lists the unmerged straggler before it is ingested",
                "straggler — refs/heads/strag", lambda: out_h0)
            rc_h, _out_h = run_engine(fh, ["--ingest", "strag", "--as", "aWho",
                                             "--confirm", "EXMP-aFoo-1"])
            arm("--ingest on the default branch writes its records", 0, lambda: rc_h)
            run("git", "add", "-A", cwd=fh)
            run("git", "commit", "-q", "-m", "records: the ingest", "--no-verify", cwd=fh)
            _rc, out_h1 = run_engine(fh, ["--stragglers"])
            arm("once they are committed the ref stops being listed, still unmerged",
                False, lambda: "straggler — refs/heads/strag" in out_h1)
            arm("which is a judgement about CONTENT, so the ref is still not an ancestor",
                False, lambda: check_contains(fh, read_rev(fh, "strag"), "HEAD"))
        finally:
            os.environ.pop("GOV_DEFAULT_BRANCH", None)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "strag", cwd=fh)
        run("git", "checkout", "HEAD", "--", "memory/backlog/EXMP.md", cwd=fh)
        run("git", "commit", "-q", "-m", "merge the straggler", "--no-verify", cwd=fh)
        arm("and the later merge passes the audit with no further record", 0, lambda: run_audit(fh))

        # ---- AC6: the straggler inventory, its two scopes, its fork case and its DEAD PROBES.
        os.environ["GOV_DEFAULT_BRANCH"] = "main"
        try:
            fi = os.path.join(base, "inv_three")
            seed_shards_base(fi, FX_SEED_ROWS)
            run("git", "checkout", "-q", "-b", "strag", cwd=fi)
            run_commit_on(fi, "strag: a row change the default branch lacks",
                          {"memory/backlog/EXMP.md": render_shard("EXMP", list(FX_STRAG_ROWS))},
                          day=DAY_STRAG)
            far = run("git", "rev-parse", "HEAD", cwd=fi).strip()
            run("git", "checkout", "-q", "main", cwd=fi)
            run("git", "update-ref", "refs/remotes/origin/far", far, cwd=fi)
            _rc, out_i = run_engine(fi, ["--stragglers"])
            arm("the inventory examines every local AND remote-tracking ref",
                "examined 3 ref(s)", lambda: out_i)
            arm("and lists both stragglers", 2, lambda: out_i.count("straggler — "))
            arm("including the remote-tracking one, which is another node's pushed copy",
                "straggler — refs/remotes/origin/far", lambda: out_i)
            _rc, out_i2 = run_engine(fi, ["--stragglers", "--local"])
            arm("--local narrows it to refs/heads", 1, lambda: out_i2.count("straggler — "))
            _rc, out_i3 = run_engine(fi, ["--stragglers", "--tsv"])
            arm("--tsv prints the machine-readable row", f"straggler\trefs/heads/strag\t",
                lambda: out_i3)
            arm("and its own liveness count", "examined\t3", lambda: out_i3)

            fj = os.path.join(base, "inv_fork")
            seed_shards_base(fj, FX_SEED_ROWS)
            run("git", "checkout", "-q", "-b", "strag", cwd=fj)
            run_commit_on(fj, "strag: a row change the default branch lacks",
                          {"memory/backlog/EXMP.md": render_shard("EXMP", list(FX_STRAG_ROWS))},
                          day=DAY_STRAG)
            run("git", "branch", "twin", cwd=fj)
            run("git", "checkout", "-q", "-b", "forked", cwd=fj)
            run_commit_on(fj, "forked: a commit touching no backlog row",
                          {"README.md": "forked" + NEWLINE}, day=DAY_HEAD)
            run("git", "checkout", "-q", "main", cwd=fj)
            _rc, out_j = run_engine(fj, ["--stragglers"])
            arm("two refs at one straggler tip and a fork above it are ALL candidates",
                3, lambda: out_j.count("straggler — "))

            empty = os.path.join(base, "inv_empty")
            os.makedirs(empty, exist_ok=True)
            run("git", "init", "-q", "-b", "main", ".", cwd=empty)
            rc_k, out_k = run_engine(empty, ["--stragglers"])
            arm("a repository holding no ref is a DEAD PROBE, not a clean inventory",
                "DEAD PROBE", lambda: out_k)
            arm("and exits 1", 1, lambda: rc_k)

            shallow = os.path.join(base, "inv_shallow")
            run("git", "clone", "-q", "--depth", "1",
                "file:///" + os.path.abspath(fi).replace(chr(92), "/"), shallow, cwd=base)
            rc_l, out_l = run_engine(shallow, ["--stragglers"])
            arm("a shallow clone is a DEAD PROBE too, because its history is truncated",
                "DEAD PROBE", lambda: out_l)
            arm("and exits 1 as well", 1, lambda: rc_l)
        finally:
            os.environ.pop("GOV_DEFAULT_BRANCH", None)

        # ---- AC7: --dry-run's three outcomes, and that it touches nothing.
        fm, _fm0, _fm1, _fm2 = seed_transition(base, "rel_dry")
        run("git", "checkout", "-q", "strag", cwd=fm)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fm)
        dry_before = run("git", "status", "--porcelain", cwd=fm)
        rc_m, out_m = run_engine(fm, ["--relocate", "--as", "aWho", "--dry-run"])
        arm("a dry run over a writable plan exits 0", 0, lambda: rc_m)
        arm("printing the plan and its conservation table",
            "EXMP-aFoo-1 · changed · flip to CLOSED", lambda: out_m)
        arm("and touching neither the worktree nor the index",
            True, lambda: run("git", "status", "--porcelain", cwd=fm) == dry_before)
        arm("not even by creating the file it would have written into",
            False, lambda: os.path.isfile(os.path.join(fm, "memory/builds/aWho/BACKLOG.md")))
        rc_m2, _out_m2 = run_engine(fd, ["--relocate", "--as", "aWho", "--dry-run"])
        arm("a dry run over a plan holding a NEEDS-HUMAN entry exits 1", 1, lambda: rc_m2)

        # ---- S2: the classification rows AC1 and AC2 do not reach — a removal on either side of
        # ---- the terminal line, a decline, and a flip the fold now derives for itself.
        cls_seed = [
            "- EXMP-aFoo-1 · CLOSED · a terminal row this branch rotates out of the shard",
            "- EXMP-aFoo-2 · OPEN · a live row this branch deletes outright",
            "- EXMP-aFoo-3 · OPEN · a row this branch declines",
            "- EXMP-aFoo-4 · OPEN · a row this branch marks as specced",
        ]
        cls_strag = [
            "- EXMP-aFoo-3 · WONTDO · a row this branch declines",
            "- EXMP-aFoo-4 · SPECCED · a row this branch marks as specced",
        ]
        cls_head = ["- EXMP-aFoo-%d · filed 2026-03-01 · %s" % (n, row.split(" · ", 2)[2])
                    for n, row in enumerate(cls_seed, 1)]
        fcl, _fcl0, _fcl1, _fcl2 = seed_transition(base, "rel_classes", seed_rows=cls_seed,
                                                   strag_rows=cls_strag, head_asks=cls_head)
        run("git", "checkout", "-q", "strag", cwd=fcl)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fcl)
        rc_cl0, out_cl0 = run_engine(fcl, ["--relocate", "--as", "aWho"])
        arm("a row that was LIVE at the merge base and is gone is NEEDS-HUMAN",
            "NEEDS-HUMAN EXMP-aFoo-2", lambda: out_cl0)
        arm("and it alone refuses the plan", 1, lambda: rc_cl0)
        rc_cl, out_cl = run_engine(fcl, ["--relocate", "--as", "aWho",
                                           "--drop", "EXMP-aFoo-2=a human checked: deliberate"])
        books_cl = read_backlogs(fcl)
        arm("a row that was TERMINAL at the merge base and is gone drops mechanically",
            "- RELOCATED · EXMP-aFoo-1 · by ", lambda: books_cl.get("aWho", ""))
        arm("with the dropped disposal and no status row of its own",
            "dropped: terminal row removed", lambda: books_cl.get("aWho", ""))
        arm("a flip to WONTDO carries the row's own reason",
            "- WONTDO · EXMP-aFoo-3 · a row this branch declines",
            lambda: books_cl.get("aWho", ""))
        arm("a flip between LIVE tokens writes no record, the fold deriving it now",
            "kept: live flip, derived", lambda: books_cl.get("aWho", ""))
        arm("so that id gets its provenance row and nothing else", 0,
            lambda: books_cl.get("aWho", "").count("· EXMP-aFoo-4 · a row this branch"))
        arm("and all four entries are accounted exactly once", 0, lambda: rc_cl)

        # ---- AC8: the recipe, one constant and three renderings.
        kit_root = read_kit_root()
        want_recipe = read_recipe(kit_root)
        view_block = NEWLINE.join("> " + line for line in want_recipe)
        arm("the rendered family view quotes the recipe --recipe prints, byte for byte",
            True, lambda: view_block in read_text(os.path.join(fa, "memory/backlog/EXMP.md")))
        shard_path = os.path.join(base, "mr_shard.md")
        view_path = os.path.join(base, "mr_view.md")
        empty_path = os.path.join(base, "mr_base.md")
        write_file(view_path, backlog.render_family_view(
            "EXMP", (), backlog.Fold({}, {}, {}, {}), "memory", index.kit_rel(),
            index.GEN_HEADER))
        write_file(shard_path, render_shard("EXMP", ["- EXMP-aFoo-1 · OPEN · an authored row"]))
        write_file(empty_path, "")
        _rc, mr_out = run_unchecked(sys.executable, os.path.join(_HERE, "merge-rows.py"), empty_path,
                              view_path, shard_path, "memory/backlog/EXMP.md", cwd=kit_root)
        arm("the row driver's shard-into-view banner carries the same bytes",
            True, lambda: NEWLINE.join(want_recipe) in mr_out)

        # ---- AC9: every refusal that is a missing CONDITION rather than an unanswered question.
        fn, _fn0, _fn1, _fn2 = seed_transition(base, "rel_refuse")
        rc_n0, out_n0 = run_engine(fn, ["--relocate", "--as", "aWho"])
        arm("--relocate with no MERGE_HEAD, no merge HEAD and no --from exits 2",
            2, lambda: rc_n0)
        arm("naming the missing condition", "found no MERGE_HEAD", lambda: out_n0)
        arm("and reprinting the recipe that sent the operator here",
            want_recipe[0], lambda: out_n0)
        run("git", "checkout", "-q", "strag", cwd=fn)
        rc_n1, out_n1 = run_engine(fn, ["--relocate", "--from", "main", "--as", "aWho"])
        arm("--relocate refuses a shards-mode OTHER side, which has no file to relocate into",
            2, lambda: rc_n1)
        arm("naming that side's mode", "reads shards", lambda: out_n1)
        rc_n2, out_n2 = run_engine(fn, ["--repair", "HEAD", "--as", "aWho"])
        arm("--repair from a shards-mode checkout exits 2 naming HEAD's mode", 2, lambda: rc_n2)
        arm("because its records would be a half-migration",
            "`.memory-tree.conf` reads shards", lambda: out_n2)
        rc_n3, out_n3 = run_engine(fn, ["--ingest", "main", "--as", "aWho"])
        arm("and so does the straggler form of --ingest from that checkout", 2, lambda: rc_n3)
        arm("which is the straggler form, the landing form needing a builds-mode HEAD",
            "straggler form needs a builds-mode checkout", lambda: out_n3)
        rc_n4, out_n4 = run_engine(fn, ["--relocate", "--as", "not a slug"])
        arm("an --as value outside the slug shape exits 2", 2, lambda: rc_n4)
        arm("naming the shape it wanted", "takes a build slug", lambda: out_n4)

        # ---- AC11: a flip rotated into a backlog archive is ONE change, and the archive goes.
        arch_rel = "memory/archive/EXMP.2026-04-02.md"
        fo, _fo0, fo_change, _fo2 = seed_transition(
            base, "rel_archive",
            strag_rows=[FX_STRAG_ROWS[1], FX_STRAG_ROWS[2]],
            strag_files={arch_rel: render_shard("EXMP", [FX_STRAG_ROWS[0]])})
        run("git", "checkout", "-q", "strag", cwd=fo)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fo)
        rc_o, _out_o = run_engine(fo, ["--relocate", "--as", "aWho"])
        arm("a flip rotated into a family archive relocates like any other", 0, lambda: rc_o)
        arm("accounted exactly once, as one population and not two",
            1, lambda: read_backlogs(fo).get("aWho", "").count("RELOCATED · EXMP-aFoo-1 · "))
        arm("and the archive the default side does not carry is removed from the worktree",
            False, lambda: os.path.isfile(os.path.join(fo, arch_rel)))
        arm("and from the index, where a tracked archive reds the post-flip verdict",
            False, lambda: arch_rel in run("git", "ls-files", "--", arch_rel, cwd=fo))

        # ---- AC12: one hold corpus, two policy sets, three different answers.
        hold_seed = ["- EXMP-aFoo-1 · OPEN · the row the seed already carries"]
        hold_strag = hold_seed + list(HOLD_ROWS)
        hold_head = ["- EXMP-aFoo-1 · filed 2026-03-01 · the row the seed already carries"]
        fp, _fp0, _fp1, _fp2 = seed_transition(base, "hold_straggler", seed_rows=hold_seed,
                                               strag_rows=hold_strag, head_asks=hold_head)
        run("git", "checkout", "-q", "strag", cwd=fp)
        run_unchecked("git", "merge", "--no-commit", "--no-ff", "main", cwd=fp)
        books_fp = read_backlogs(fp)
        rc_p, out_p = run_engine(fp, ["--relocate", "--as", "aWho"])
        arm("under the straggler set a hold naming nothing is NEEDS-HUMAN",
            "NEEDS-HUMAN EXMP-aFoo-5", lambda: out_p)
        arm("and so is a hold naming a decision id nothing files",
            "NEEDS-HUMAN EXMP-aFoo-8", lambda: out_p)
        arm("while a hold on an ask the SAME plan files names an id and is planned",
            "- BLOCKED · EXMP-aFoo-3 · on EXMP-aFoo-2", lambda: out_p)
        arm("that ask is never NEEDS-HUMAN", False, lambda: "NEEDS-HUMAN EXMP-aFoo-3" in out_p)
        arm("and the plan holding a NEEDS-HUMAN entry writes nothing at all",
            True, lambda: read_backlogs(fp) == books_fp)
        arm("refusing with exit 1", 1, lambda: rc_p)

        fq = os.path.join(base, "hold_migration")
        seed_shards_base(fq, hold_seed)
        fq_base = run("git", "rev-parse", "HEAD", cwd=fq).strip()
        fq_tip = run_commit_on(fq, "records: the hold rows arrive",
                               {"memory/backlog/EXMP.md": render_shard("EXMP", hold_strag)},
                               day=DAY_STRAG)
        mig_form = Form("--write", "write", MIGRATION_SET, False, False)
        mig_args = dict(read_args([]))
        mig_args.update({"as_slug": "aWho", "triage_ask": "EXMP-aFoo-9",
                         "entries": audit.delta(fq_tip, fq_base, fq)})
        mig_plan = build_relocation(fq, mig_form, fq_tip, [fq_base], mig_args)
        mig_rows = {r.text for r in mig_plan.records}
        arm("under the migration set a hold naming nothing holds on the triage ask",
            True, lambda: any(r.startswith("- DEFERRED · EXMP-aFoo-5 · until EXMP-aFoo-9 · ")
                              for r in mig_rows))
        arm("and so does one naming a decision id", True,
            lambda: any(r.startswith("- BLOCKED · EXMP-aFoo-8 · on EXMP-aFoo-9 · ")
                        for r in mig_rows))
        arm("while the hold on an ask the plan itself files is kept verbatim", True,
            lambda: any(r.startswith("- BLOCKED · EXMP-aFoo-3 · on EXMP-aFoo-2 · ")
                        for r in mig_rows))
        arm("each in the ask OWNER's folder, which is P1's migration value", True,
            lambda: all(r.path == "memory/builds/aFoo/BACKLOG.md" for r in mig_plan.records
                        if r.section == backlog.H_DISPOSITIONS))
        arm("and that set runs over a shards-mode HEAD, which no mode guard refuses",
            "shards", lambda: read_conf_mode(fq, fq_tip))
        arm("a straggler-set verb meeting --triage-ask exits 2 naming the form",
            2, lambda: run_engine(fp, ["--relocate", "--as", "aWho",
                                         "--triage-ask", "EXMP-aFoo-9"])[0])
        arm("no provenance under --write, because a linear switch-over is no transition",
            0, lambda: sum(1 for r in mig_plan.records if "RELOCATED" in r.text))

        # ---- AC13: the migration set's per-class disposition home, and its idempotence.
        fr = os.path.join(base, "mig_signed")
        seed_shards_base(fr, ["- EXMP-aFoo-1 · OPEN · the ask this corpus closes later",
                              "- EXMP-aBar-1 · OPEN · an open ask on a finished build",
                              "- EXMP-aBar-2 · OPEN · an ask the target already disposes"],
                         slugs=("aFoo", "aBar", "aWho"))
        fr_base = run("git", "rev-parse", "HEAD", cwd=fr).strip()
        fr_tip = run_commit_on(fr, "records: the legacy flip", {
            "memory/backlog/EXMP.md": render_shard("EXMP", [
                "- EXMP-aFoo-1 · CLOSED · the ask this corpus closes later",
                "- EXMP-aBar-1 · OPEN · an open ask on a finished build",
                "- EXMP-aBar-2 · OPEN · an ask the target already disposes"]),
            "memory/builds/aBar/BACKLOG.md": render_build_backlog(
                "aBar", (), ("- WONTDO · EXMP-aBar-2 · the target disposed this one already",)),
        }, day=DAY_STRAG)
        signed_path = os.path.join(base, "signed-triage.md")
        write_file(signed_path, NEWLINE.join((
            "# the signed triage record", "",
            "| Ask | Verdict | Field |",
            "|---|---|---|",
            "| EXMP-aBar-1 | CLOSED | 1234abc |",
            "| EXMP-aBar-2 | CLOSED | 1234abc |", "")))
        mig2_args = dict(read_args([]))
        mig2_args.update({"as_slug": "aWho", "signed": [("triage", signed_path)],
                          "entries": audit.delta(fr_tip, fr_base, fr)})
        mig2 = build_relocation(fr, Form("--write", "write", MIGRATION_SET, False, False),
                                fr_tip, [fr_base], mig2_args)
        homes = {r.text.split(backlog.SEP)[1]: r.path for r in mig2.records}
        arm("the transferred legacy CLOSED lands in the ask owner's folder",
            "memory/builds/aFoo/BACKLOG.md", lambda: homes.get("EXMP-aFoo-1"))
        arm("the signed triage verdict lands in the --as folder, the one-writer rule",
            "memory/builds/aWho/BACKLOG.md", lambda: homes.get("EXMP-aBar-1"))
        arm("and an id the target tree already disposes plans nothing",
            False, lambda: "EXMP-aBar-2" in homes)

        # ---- AC14, AC16 and AC17: the landing form of --ingest.
        land_tip_rows = [
            "- EXMP-aFoo-1 · CLOSED · the first ask, which the straggler closes",
            "- EXMP-aFoo-2 · OPEN · the second ask, pointing at memory/gone/old.md",
            "- EXMP-aBar-1 · OPEN · a new ask on a finished build",
            "- EXMP-aBar-2 · BLOCKED · held until EXMP-aBar-1 lands, and then it can move",
        ]
        amended_tip = land_tip_rows + [
            "- EXMP-aFoo-9 · OPEN · a sentence nothing in the base corpus ever said"]
        fs, fs_flip, fs_tip = seed_landing(
            base, "land_dry", amended_tip,
            seed_rows=list(FX_SEED_ROWS) + [
                "- EXMP-aFoo-9 · OPEN · the sentence the base corpus actually carries"],
            slugs=("aFoo", "aBar", "aWho"))
        books_fs = read_backlogs(fs)
        rc_s, out_s = run_engine(fs, ["--ingest", "main", "--as", "aWho",
                                        "--signed", "triage=" + signed_path, "--dry-run"])
        arm("the landing form lists both new asks", "EXMP-aBar-1 · new · new ask", lambda: out_s)
        arm("holds the flip for confirmation", "CONFIRM EXMP-aFoo-1", lambda: out_s)
        arm("puts the amendment under NEEDS-HUMAN", "NEEDS-HUMAN EXMP-aFoo-9", lambda: out_s)
        arm("prints the re-derived cutoff", "ASK_CUTOFF=", lambda: out_s)
        arm("exits 1 and writes nothing", 1, lambda: rc_s)
        arm("literally nothing: every record file is exactly as it was",
            True, lambda: read_backlogs(fs) == books_fs)

        ft, ft_flip, ft_tip = seed_landing(base, "land_write", land_tip_rows,
                                           slugs=("aFoo", "aBar", "aWho"))
        rc_t, out_t = run_engine(ft, ["--ingest", "main", "--as", "aWho",
                                        "--signed", "triage=" + signed_path,
                                        "--confirm", "EXMP-aFoo-1"])
        books_t = read_backlogs(ft)
        arm("with the amendment gone and the flip confirmed, the landing form writes", 0,
            lambda: rc_t)
        arm("each new ask in its own slug folder", "- EXMP-aBar-1 · filed ",
            lambda: books_t.get("aBar", ""))
        arm("the hold on the ask this same delta files, verbatim",
            "- BLOCKED · EXMP-aBar-2 · on EXMP-aBar-1 · ", lambda: books_t.get("aBar", ""))
        arm("the flip in the ask owner's folder, which is the migration set's home",
            "- CLOSED · EXMP-aFoo-1 · by ", lambda: books_t.get("aFoo", ""))
        arm("the signed triage verdict in the --as folder", "- CLOSED · EXMP-aBar-1 · by 1234abc",
            lambda: books_t.get("aWho", ""))
        arm("and one RELOCATED row per delta entry in the --as folder",
            3, lambda: books_t.get("aWho", "").count("- RELOCATED · "))
        arm("printing the cutoff as the day after the newest filed ask",
            "ASK_CUTOFF=2026-04-03", lambda: out_t)

        fu, _fu_flip, _fu_tip = seed_landing(base, "land_cutoff", land_tip_rows,
                                             cutoff="2027-01-01", slugs=("aFoo", "aBar", "aWho"))
        _rc, out_u = run_engine(fu, ["--ingest", "main", "--as", "aWho",
                                       "--signed", "triage=" + signed_path,
                                       "--confirm", "EXMP-aFoo-1"])
        arm("a current cutoff LATER than that day is printed unchanged, never lowered",
            "ASK_CUTOFF=2027-01-01", lambda: out_u)

        fv, _fv_flip, _fv_tip = seed_landing(base, "land_builds_tip", land_tip_rows,
                                             slugs=("aFoo", "aBar", "aWho"))
        run("git", "checkout", "-q", "-b", "sibling", cwd=fv)
        run_commit_on(fv, "sibling: a builds-mode ref that is not the default tip",
                      {"README.md": "a sibling" + NEWLINE})
        run("git", "checkout", "-q", "flip", cwd=fv)
        rc_v, out_v = run_engine(fv, ["--ingest", "sibling", "--as", "aWho",
                                        "--signed", "triage=" + signed_path])
        arm("the same command against a BUILDS-mode tip is not the landing form", 2, lambda: rc_v)
        arm("so --signed exits 2 naming the form it was given",
            "belong to the migration policy set", lambda: out_v)

        # AC16 — the in-progress merge and the concluded merge write the same bytes.
        fw, _fw_flip, _fw_tip = seed_landing(base, "land_inprogress", land_tip_rows,
                                             slugs=("aFoo", "aBar", "aWho"))
        run_unchecked("git", "merge", "--no-ff", "--no-commit", "main", cwd=fw)
        run("git", "checkout", "HEAD", "--", "memory/backlog/EXMP.md", cwd=fw)
        rc_w, _out_w = run_engine(fw, ["--ingest", "main", "--as", "aWho",
                                         "--signed", "triage=" + signed_path,
                                         "--confirm", "EXMP-aFoo-1"])
        arm("the landing form runs INSIDE the reconcile merge, the state unit 34 ingests in",
            0, lambda: rc_w)
        arm("writing the same bytes as the run before any merge",
            True, lambda: read_backlogs(fw) == books_t)

        fx, _fx_flip, _fx_tip = seed_landing(base, "land_concluded", land_tip_rows,
                                             slugs=("aFoo", "aBar", "aWho"))
        run_unchecked("git", "merge", "--no-ff", "--no-commit", "main", cwd=fx)
        run("git", "checkout", "HEAD", "--", "memory/backlog/EXMP.md", cwd=fx)
        run("git", "commit", "-q", "-m", "reconcile the landing", "--no-verify", cwd=fx)
        rc_x, _out_x = run_engine(fx, ["--ingest", "main", "--as", "aWho",
                                         "--signed", "triage=" + signed_path,
                                         "--confirm", "EXMP-aFoo-1"])
        arm("and so does a run on the concluded merge, against its FIRST parent", 0, lambda: rc_x)
        arm("byte for byte", True, lambda: read_backlogs(fx) == books_t)
        run("git", "checkout", "-q", "--", ".", cwd=fx)
        run("git", "clean", "-qfd", "--", "memory", cwd=fx)
        run_commit_on(fx, "one more commit on top of the concluded merge",
                      {"README.md": "moved on" + NEWLINE})
        rc_x2, out_x2 = run_engine(fx, ["--ingest", "main", "--as", "aWho",
                                          "--signed", "triage=" + signed_path])
        arm("one commit further on, the form is no longer admitted", 2, lambda: rc_x2)
        arm("and the refusal names --repair", "Use --repair", lambda: out_x2)

        fy, fy_flip, fy_tip = seed_landing(base, "land_firstparent", land_tip_rows,
                                           slugs=("aFoo", "aBar", "aWho"))
        run("git", "checkout", "-q", "main", cwd=fy)
        run_unchecked("git", "merge", "--no-ff", "--no-commit", "flip", cwd=fy)
        run("git", "checkout", fy_flip, "--", "memory/backlog/EXMP.md", cwd=fy)
        run("git", "commit", "-q", "-m", "merge the other way round", "--no-verify", cwd=fy)
        rc_y, out_y = run_engine(fy, ["--ingest", "main", "--as", "aWho",
                                        "--signed", "triage=" + signed_path])
        arm("a merge whose FIRST parent is the tip is not that state either", 2, lambda: rc_y)
        arm("and is sent to --repair as well", "Use --repair", lambda: out_y)
        rc_y2, out_y2 = run_engine(fh, ["--ingest", "strag", "--as", "aWho"])
        arm("the straggler form over a HEAD that already contains its ref exits 2 the same way",
            2, lambda: rc_y2)
        arm("naming --repair", "Use --repair", lambda: out_y2)

        # AC17 — the landing form replaces the migration's OWN unedited record, and nothing else.
        hold_line = backlog.render_status_row(
            "BLOCKED", "EXMP-aFoo-1", "the first ask, which the straggler closes", "EXMP-aFoo-9")
        fz, _fz_flip, _fz_tip = seed_landing(
            base, "land_replace", land_tip_rows,
            seed_rows=[FX_SEED_ROWS[0].replace("· OPEN ·", "· BLOCKED ·"), FX_SEED_ROWS[1]],
            head_rows=(hold_line,), slugs=("aFoo", "aBar", "aWho"))
        rc_z, _out_z = run_engine(fz, ["--ingest", "main", "--as", "aWho",
                                         "--signed", "triage=" + signed_path,
                                         "--triage-ask", "EXMP-aFoo-9",
                                         "--confirm", "EXMP-aFoo-1"])
        arm("the landing form replaces the hold the migration itself wrote", 0, lambda: rc_z)
        arm("with the flip, in the same file", "- CLOSED · EXMP-aFoo-1 · by ",
            lambda: read_backlogs(fz).get("aFoo", ""))
        arm("leaving ONE status row for that id, which is what V4 counts",
            False, lambda: hold_line in read_backlogs(fz).get("aFoo", ""))
        _rc, check_out = run_unchecked(sys.executable, os.path.join(_HERE, "gen_build_index.py"),
                                 "--check", cwd=fz)
        arm("and the generator names no V4 over the result",
            False, lambda: "V4 " in check_out)

        fza, _fza_flip, _fza_tip = seed_landing(
            base, "land_replace_edited", land_tip_rows,
            seed_rows=[FX_SEED_ROWS[0].replace("· OPEN ·", "· BLOCKED ·"), FX_SEED_ROWS[1]],
            head_rows=(hold_line + ", and the receiving branch edited this wording",),
            slugs=("aFoo", "aBar", "aWho"))
        rc_za, out_za = run_engine(fza, ["--ingest", "main", "--as", "aWho",
                                           "--signed", "triage=" + signed_path,
                                           "--triage-ask", "EXMP-aFoo-9",
                                           "--confirm", "EXMP-aFoo-1"])
        arm("a row the receiving branch EDITED is never replaced", 1, lambda: rc_za)
        arm("it is listed under NEEDS-HUMAN instead", "NEEDS-HUMAN EXMP-aFoo-1", lambda: out_za)
        arm("and nothing is written", True,
            lambda: hold_line + ", and the receiving branch edited this wording"
            in read_backlogs(fza).get("aFoo", ""))
        if prior_default is not None:
            os.environ["GOV_DEFAULT_BRANCH"] = prior_default
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
         "[--signed <same-id|triage>=<path>] [--design-named <id>] …\n"
         "       migrate_backlog.py --relocate --as <slug> [--from <ref>] [--drop <id>=<why>] "
         "[--confirm <id>] [--dry-run]\n"
         "       migrate_backlog.py --ingest <ref> --as <slug> [--signed <kind>=<path>] "
         "[--triage-ask <id>] [--confirm <id>] [--drop <id>=<why>] [--dry-run]\n"
         "       migrate_backlog.py --repair <merge-sha> --as <slug> [--confirm <id>] "
         "[--drop <id>=<why>] [--dry-run]\n"
         "       migrate_backlog.py --stragglers [--local] [--tsv] | --recipe | --selftest")

#: The three WRITING verbs of the relocation engine. `--write`, the switch-over's whole-corpus
#: migration, is a thin driver over the same engine and is NOT a mode of this file.
WRITING_MODES = ("--relocate", "--ingest", "--repair")
#: The two verbs that take a positional value straight after them.
VALUED_MODES = ("--ingest", "--repair")


def read_args(argv: list) -> dict:
    args = {"mode": "", "record": "", "record_as": "", "signed": [], "design_named": [],
            "ref": "", "as_slug": "", "from": "", "drop": [], "confirm": [], "triage_ask": "",
            "dry_run": False, "local": False, "tsv": False}
    rest = list(argv)
    while rest:
        token = rest.pop(0)
        if token in ("--plan", "--selftest", "--relocate", "--stragglers", "--recipe"):
            args["mode"] = token
        elif token in VALUED_MODES:
            args["mode"] = token
            args["ref"] = read_flag_value(rest, token)
        elif token == "--as":
            args["as_slug"] = read_flag_value(rest, token)
        elif token == "--from":
            args["from"] = read_flag_value(rest, token)
        elif token == "--triage-ask":
            args["triage_ask"] = read_flag_value(rest, token)
        elif token == "--confirm":
            args["confirm"].append(read_flag_value(rest, token))
        elif token == "--drop":
            value = read_flag_value(rest, token)
            ident, sep, why = value.partition("=")
            if not sep or not ident or not why.strip():
                raise Problem(f"migrate-backlog: --drop takes <id>=<why>, and a drop with no "
                              f"stated reason is a row lost with a record saying nothing: "
                              f"'{value}'")
            args["drop"].append((ident, why.strip()))
        elif token == "--dry-run":
            args["dry_run"] = True
        elif token == "--local":
            args["local"] = True
        elif token == "--tsv":
            args["tsv"] = True
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
    if args["mode"] == "--recipe":
        return cmd_recipe(resolve_root())
    if args["mode"] == "--stragglers":
        return cmd_stragglers(resolve_root(), args)
    if args["mode"] in WRITING_MODES:
        return cmd_relocate(resolve_root(), args)
    if args["mode"] != "--plan":
        print(USAGE)
        return 2
    return cmd_plan(resolve_root(), args)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Problem as exc:
        print(str(exc))
        # THE CODE IS THE EXCEPTION'S, defaulting to 1. `Refusal` carries 2, and the distinction is
        # read by the switch-over's landing reconcile and by the adopter runbook.
        sys.exit(getattr(exc, "code", 1))

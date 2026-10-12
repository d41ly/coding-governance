"""prose.py — a transcript measure of narration, interjections and BUILD/SPEC pair emission. gov:kit runlog@1.12

Contract: the spec for TOOL-aHeardState-2 under the build folder of that slug.

A TURN opens at any main-file user record whose typed text `extract._read_text` returns, whatever its
origin; a tool result never opens one, and back-to-back openers are one turn. In a turn the
FINAL MESSAGE is the assistant text after the turn's last `tool_use` block, and every other assistant
message carrying text, counted once per `message.id`, is one INTERJECTION. Report-only: nothing here
writes, gates or prints message text.

THE PAIR PREDICATE mirrors `format-guard.js` (TOOL-aHeardState-1) step for step: the shapes derived
from the charter's `<!-- microformats -->` fence, rule r1, the adjacency of SPEC under BUILD, and the
derived field shape. A parity arm in that hook's suite feeds both the same messages and requires equal
verdicts, so the two spellings of one predicate cannot drift silently.

WHAT THIS DOES NOT MEASURE: whether a turn ran under a routed build (the transcript does not say, so
every final message counts), any other micro-format, any field value, sub-agent transcripts, and any
record marked `isSidechain`.
"""
import pathlib
import re

import extract as ex

FENCE_OPEN = "<!-- microformats -->"
FENCE_CLOSE = "<!-- /microformats -->"
CHARTER_FILE = "AGENTS.md"
NARRATION_ALARM = 0.40
INTERJECTION_ALARM = 3
FIELD = r"(?:(?! · ).)+?"
FENCE_LINE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def build_shape_regex(definition: str):
    """One line regex from one charter definition, as `buildShapeRegex` in format-guard.js builds it."""
    def render_part(s):
        return "".join(FIELD if re.fullmatch(r"<[^>]*>", t) else re.escape(t)
                       for t in re.split(r"(<[^>]*>)", s))
    body, rest = "", definition
    while True:
        i = rest.find("[ · ")
        if i < 0:
            body += render_part(rest)
            break
        j = rest.find("]", i)
        if j < 0:
            body += render_part(rest)
            break
        body += render_part(rest[:i]) + "(?:" + render_part(rest[i + 1:j]) + ")?"
        rest = rest[j + 1:]
    body = re.sub(r"(?:\\ …|…)$", "(?: · .+)*", body)
    return re.compile("^- " + body + r"\s*$")


def read_charter_shapes(charter: pathlib.Path):
    """`(shapes, error)`: every fenced definition keyed by its head keyword, or why there are none."""
    try:
        lines = charter.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None, f"no {charter.name} at {charter.parent.as_posix()}"
    except UnicodeDecodeError:
        return None, f"{charter.as_posix()} is not readable as UTF-8"
    if FENCE_OPEN not in lines or FENCE_CLOSE not in lines:
        return None, f"no microformats fence in {charter.as_posix()}"
    a, b = lines.index(FENCE_OPEN), lines.index(FENCE_CLOSE)
    shapes = {}
    for line in lines[a + 1:b]:
        m = re.fullmatch(r"- `(.*)`", line)
        if m:
            shapes[m.group(1).split(" — ")[0]] = (m.group(1), build_shape_regex(m.group(1)))
    for need in ("BUILD", "SPEC"):
        if need not in shapes:
            return None, f"{charter.as_posix()}'s microformats fence defines no {need} shape"
    return shapes, ""


def scan_message_lines(message: str) -> list:
    """`(text, fenced)` per line, a fence line counted as fenced, as `scanMessageLines` does."""
    rows, fenced = [], False
    for text in message.split("\n"):
        text = text.rstrip("\r")
        m = FENCE_LINE.match(text)
        # An inline backtick span closed on the same line is not a fence, as in scanMessageLines.
        fence = bool(m) and not (m.group(1)[0] == "`" and "`" in m.group(2))
        rows.append((text, fenced or fence))
        if fence:
            fenced = not fenced
    return rows


def check_pair(rows, shapes, want_spec=True) -> list:
    """The pair defects of one message, the same conditions in the same order as `checkPair`."""
    defects = []

    def check_bare(row, head):
        return not row[1] and row[0].startswith(f"- {head} — ")
    for head in ("BUILD", "SPEC") if want_spec else ("BUILD",):
        hits = [r for r in rows if check_bare(r, head)]
        if not hits:
            loose = next((r for r in rows if f"{head} — " in r[0]), None)
            defects.append(f"{head} not bare" if loose else f"no {head}")
            continue
        if not shapes[head][1].match(hits[-1][0]):
            defects.append(f"{head} off shape")
    if want_spec and not defects:
        idx = max(i for i, r in enumerate(rows) if check_bare(r, "BUILD"))
        if idx + 1 >= len(rows) or not check_bare(rows[idx + 1], "SPEC"):
            defects.append("not adjacent")
    return defects


def resolve_charter(start: pathlib.Path) -> pathlib.Path:
    """`AGENTS.md` at the first directory at or above `start` that holds a `.git`, else beside `start`."""
    here = start.resolve()
    for d in (here, *here.parents):
        if (d / ".git").exists():
            return d / CHARTER_FILE
    return here / CHARTER_FILE


def scan_turns(tree) -> list:
    """Each turn's ordered items: `("text", message id, text)` or `("tool", message id, "")`.

    Any typed user record opens a turn, whatever its origin: an owner prompt, an idle-wake tick (which
    the harness marks `isMeta`), a task notification, a hook's feedback. A tool result never opens
    one, and an opener that follows another with nothing from the assistant between them joins its
    turn, so a slash command and the skill text it injects are one turn."""
    turns, cur = [], None
    for src, _, _, rec in ex.read_records(tree):
        if src != "main" or rec.get("isSidechain") is True:
            continue
        kind = rec.get("type")
        if kind == "user":
            if ex._read_text(rec) is not None and (cur is None or cur):
                cur = []
                turns.append(cur)
            continue
        if kind != "assistant" or cur is None:
            continue
        msg = rec.get("message") if isinstance(rec.get("message"), dict) else {}
        mid = msg.get("id")
        for block in msg.get("content") or ():
            if not isinstance(block, dict):
                continue
            if block.get("type") == "text" and str(block.get("text") or "").strip():
                cur.append(("text", mid, block["text"]))
            elif block.get("type") == "tool_use":
                cur.append(("tool", mid, ""))
    return turns


def measure_prose(turns, shapes) -> dict:
    """The figures over a list of turns. `pair` is None when `shapes` is None."""
    finals, interjections, narr_chars, final_chars, pairs = 0, [], 0, 0, 0
    for items in turns:
        last_tool = max((i for i, it in enumerate(items) if it[0] == "tool"), default=-1)
        before = [it for it in items[:last_tool + 1] if it[0] == "text"]
        after = [it for it in items[last_tool + 1:] if it[0] == "text"]
        narr_chars += sum(len(it[2]) for it in before)
        if not after:
            continue
        finals += 1
        interjections.append(len({it[1] for it in before}))
        final = "\n".join(it[2] for it in after)
        final_chars += len(final)
        if shapes is not None and not check_pair(scan_message_lines(final), shapes):
            pairs += 1
    total = narr_chars + final_chars
    return {
        "turns": len(turns), "finals": finals, "chars": total,
        "share": (narr_chars / total) if total else 0.0,
        "mean": (sum(interjections) / len(interjections)) if interjections else 0.0,
        "max": max(interjections, default=0),
        "above": sum(1 for n in interjections if n > INTERJECTION_ALARM),
        "pair": pairs if shapes is not None else None,
    }


def render_mark(alarm) -> str:
    return "ALARM" if alarm else "ok"


def render_prose_report(sid, fig, charter_error) -> list:
    mark = render_mark
    pair =(f"pair — {fig['pair']}/{fig['finals']} final messages carry the BUILD/SPEC pair"
            if fig["pair"] is not None else f"pair — unknown · {charter_error}")
    return [
        f"prose — {sid} · turns {fig['turns']} · final messages {fig['finals']}",
        f"narration — {fig['share'] * 100:.1f}% of {fig['chars']} assistant prose characters · "
        f"{mark(fig['share'] > NARRATION_ALARM)} above {NARRATION_ALARM * 100:.0f}%",
        f"interjections — mean {fig['mean']:.1f} · max {fig['max']} · turns above {INTERJECTION_ALARM} "
        f"{fig['above']} · {mark(fig['mean'] > INTERJECTION_ALARM)} above a mean of {INTERJECTION_ALARM}",
        pair,
    ]

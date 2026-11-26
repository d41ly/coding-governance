# invocation_segments.py — the CANONICAL `invocation_segments` block (TOOL-dTotalRecall-8): a shell command as
# its segments, and the word a segment runs past assignments, wrappers and an interpreter. This lib dir
# ships nothing, so the block between the markers travels INLINE, byte-identical, in runlog's `extract.py`,
# which read it first, and in the playbook kit's `code_record.py`; the `invocation_segments` row of the
# resolver test's PARITY_ROWS reds a copy that drifts. A carrier imports `re` itself.
import re


# >>> invocation_segments -- canonical copy: invocation_segments.py in the gov lib dir (byte-identical; gated)
ENV_ASSIGN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*=.*", re.S)
HEREDOC_RE = re.compile(r"<<-?[ \t]*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")
WRAPPERS = frozenset({"sudo", "command", "exec", "time", "nice", "env", "nohup"})
INTERPRETERS = frozenset({"bash", "sh", "zsh", "dash", "python", "python3", "py", "node", "pwsh",
                          "powershell"})
SEPARATORS = ("&&", "||", "|&", "|", ";", "&", "\n", "(", ")")
# The characters a separator can start with. The tokenizer tries the separator list only at these, so
# an ordinary character costs one set lookup rather than one `startswith` per separator. Profiled over
# the largest local session, trying the whole list at every character cost more than parsing the JSON.
SEPARATOR_HEADS = frozenset(sep[0] for sep in SEPARATORS)


def _derive_basename(word: str) -> str:
    return word.replace("\\", "/").rsplit("/", 1)[-1]


def _remove_heredocs(command: str) -> str:
    """Drop every heredoc body, delimiter line included. A body is text, never a command."""
    if "<<" not in command:
        return command
    out, pending = [], []
    for line in command.split("\n"):
        if pending:
            if line.strip() == pending[0]:
                pending.pop(0)
            continue
        out.append(line)
        for m in HEREDOC_RE.finditer(line):
            if m.start() > 0 and line[m.start() - 1] == "<":
                continue
            pending.append(m.group(2))
    return "\n".join(out)


def _read_separator(text: str, i: int) -> str | None:
    for sep in SEPARATORS:
        if text.startswith(sep, i):
            if sep == "&" and ((i > 0 and text[i - 1] in "<>") or text.startswith("&>", i)):
                return None
            return sep
    return None


def extract_segments(command: str) -> list:
    """A shell command as `(words, separator-after)` pairs, honouring quotes, escapes and heredocs.

    A mention inside quotes stays inside ONE word and a heredoc body is dropped whole, so a commit
    message that names a destructive command is not one. This is not a shell: `$(...)` inside quotes,
    `bash -c` and `eval` are not descended into, and a call nested in one is not seen.
    """
    text = _remove_heredocs(command)
    segs, words, cur = [], [], []
    in_word = False
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "'":
            j = text.find("'", i + 1)
            j = n if j < 0 else j
            cur.append(text[i + 1:j])
            in_word, i = True, j + 1
            continue
        if ch == '"':
            j, buf = i + 1, []
            while j < n and text[j] != '"':
                if text[j] == "\\" and j + 1 < n and text[j + 1] in '"\\$`':
                    buf.append(text[j + 1])
                    j += 2
                    continue
                buf.append(text[j])
                j += 1
            cur.append("".join(buf))
            in_word, i = True, j + 1
            continue
        if ch == "\\" and i + 1 < n:
            if text[i + 1] != "\n":
                cur.append(text[i + 1])
                in_word = True
            i += 2
            continue
        if ch in " \t\r":
            if in_word:
                words.append("".join(cur))
                cur, in_word = [], False
            i += 1
            continue
        if ch == "#" and not in_word:
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        sep = _read_separator(text, i) if ch in SEPARATOR_HEADS else None
        if sep:
            if in_word:
                words.append("".join(cur))
                cur, in_word = [], False
            segs.append((words, sep))
            words = []
            i += len(sep)
            continue
        cur.append(ch)
        in_word = True
        i += 1
    if in_word:
        words.append("".join(cur))
    if words:
        segs.append((words, ""))
    return segs


def _derive_program(words: list) -> int | None:
    """The index of the word a segment RUNS: past env assignments and wrappers, and past an
    interpreter and its options, so `bash -x run.sh` runs `run.sh` and `grep x run.sh` runs grep.
    None when the segment runs inline code (`-c`) or nothing at all."""
    i = 0
    while i < len(words):
        word = words[i]
        if ENV_ASSIGN_RE.fullmatch(word) or word in WRAPPERS:
            i += 1
        elif word == "timeout":
            i += 2 if i + 1 < len(words) and words[i + 1][:1].isdigit() else 1
        else:
            break
    if i >= len(words):
        return None
    if _derive_basename(words[i]).lower().removesuffix(".exe") not in INTERPRETERS:
        return i
    j = i + 1
    while j < len(words) and words[j].startswith("-"):
        if words[j] == "-c":
            return None
        if words[j] == "-m" and j + 1 < len(words):
            return j + 1
        j += 1
    return j if j < len(words) else i
# <<< invocation_segments
